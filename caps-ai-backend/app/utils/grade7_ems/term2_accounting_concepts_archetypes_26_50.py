"""Grade 7 Economic and Management Sciences - Term 2: Accounting Concepts (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/EMS_Gr7/Term 2/01. Accounting concepts.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import get_ems_scenario, NAMES
from .term2_accounting_concepts_archetypes_01_25 import (
    _fmt_r,
    _make_calc,
    _make_ledger,
    _make_mcq,
    _make_typed,
)


def _svg_record_flow(rng: random.Random, event_txt: str, doc_txt: str, amt: int) -> Dict[str, Any]:
    y_off = rng.randint(-2, 2)
    svg = (
        f'<svg viewBox="0 0 470 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="470" height="155" fill="#ffffff" stroke="#e2e8f0" rx="8"/>'
        f'<rect x="15" y="{42 + y_off}" width="125" height="68" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>'
        f'<text x="77" y="{66 + y_off}" font-size="10" font-weight="bold" fill="#1e3a8a" text-anchor="middle">1. Transaction</text>'
        f'<text x="77" y="{83 + y_off}" font-size="9" fill="#1e40af" text-anchor="middle">{event_txt}</text>'
        f'<text x="77" y="{98 + y_off}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{_fmt_r(amt)}</text>'
        f'<line x1="142" y1="{76 + y_off}" x2="170" y2="{76 + y_off}" stroke="#475569" stroke-width="2"/>'
        f'<polygon points="170,{76 + y_off} 163,{71 + y_off} 163,{81 + y_off}" fill="#475569"/>'
        f'<rect x="172" y="{42 + y_off}" width="125" height="68" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>'
        f'<text x="234" y="{66 + y_off}" font-size="10" font-weight="bold" fill="#065f46" text-anchor="middle">2. Financial Record</text>'
        f'<text x="234" y="{85 + y_off}" font-size="9" fill="#047857" text-anchor="middle">{doc_txt}</text>'
        f'<line x1="299" y1="{76 + y_off}" x2="327" y2="{76 + y_off}" stroke="#475569" stroke-width="2"/>'
        f'<polygon points="327,{76 + y_off} 320,{71 + y_off} 320,{81 + y_off}" fill="#475569"/>'
        f'<rect x="329" y="{42 + y_off}" width="125" height="68" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        f'<text x="391" y="{66 + y_off}" font-size="10" font-weight="bold" fill="#92400e" text-anchor="middle">3. SARS &amp; Audit</text>'
        f'<text x="391" y="{85 + y_off}" font-size="9" fill="#b45309" text-anchor="middle">Legal proof of earnings</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_bank_economy_cycle(rng: random.Random, loan_amt: int, jobs_n: int) -> Dict[str, Any]:
    y_off = rng.randint(-2, 2)
    svg = (
        f'<svg viewBox="0 0 460 175" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="460" height="175" fill="#ffffff" stroke="#e2e8f0" rx="8"/>'
        f'<rect x="20" y="{38 + y_off}" width="120" height="58" rx="6" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.5"/>'
        f'<text x="80" y="{62 + y_off}" font-size="10" font-weight="bold" fill="#312e81" text-anchor="middle">Commercial Bank</text>'
        f'<text x="80" y="{78 + y_off}" font-size="9" fill="#4338ca" text-anchor="middle">Loan: {_fmt_r(loan_amt)}</text>'
        f'<line x1="142" y1="{67 + y_off}" x2="170" y2="{67 + y_off}" stroke="#334155" stroke-width="2"/>'
        f'<polygon points="170,{67 + y_off} 163,{62 + y_off} 163,{72 + y_off}" fill="#334155"/>'
        f'<rect x="172" y="{38 + y_off}" width="120" height="58" rx="6" fill="#ecfeff" stroke="#0891b2" stroke-width="1.5"/>'
        f'<text x="232" y="{62 + y_off}" font-size="10" font-weight="bold" fill="#164e63" text-anchor="middle">Capital Investment</text>'
        f'<text x="232" y="{78 + y_off}" font-size="9" fill="#0e7490" text-anchor="middle">Equipment &amp; Expansion</text>'
        f'<line x1="294" y1="{67 + y_off}" x2="322" y2="{67 + y_off}" stroke="#334155" stroke-width="2"/>'
        f'<polygon points="322,{67 + y_off} 315,{62 + y_off} 315,{72 + y_off}" fill="#334155"/>'
        f'<rect x="324" y="{38 + y_off}" width="116" height="58" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>'
        f'<text x="382" y="{62 + y_off}" font-size="10" font-weight="bold" fill="#14532d" text-anchor="middle">Economic Growth</text>'
        f'<text x="382" y="{78 + y_off}" font-size="9" fill="#15803d" text-anchor="middle">{jobs_n} New Jobs</text>'
        f'<text x="230" y="135" font-size="10" fill="#475569" text-anchor="middle">Stimulates Needs, Wants &amp; National Output</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_equity_bars(rng: random.Random, assets: int, liab: int, cap: int, biz: str) -> Dict[str, Any]:
    scale = 175.0 / max(1, assets)
    a_w = int(assets * scale)
    l_w = max(25, int(liab * scale))
    c_w = max(25, a_w - l_w)
    y_off = rng.randint(-2, 2)
    svg = (
        f'<svg viewBox="0 0 450 165" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="450" height="165" fill="#ffffff" stroke="#e2e8f0" rx="8"/>'
        f'<text x="225" y="24" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{biz}: Capital &amp; Liabilities</text>'
        f'<text x="22" y="{58 + y_off}" font-size="10" font-weight="bold" fill="#1e3a8a">Assets ({_fmt_r(assets)})</text>'
        f'<rect x="155" y="{44 + y_off}" width="{a_w}" height="24" rx="4" fill="#2563eb"/>'
        f'<text x="22" y="{104 + y_off}" font-size="10" font-weight="bold" fill="#0f172a">Liabilities + Capital</text>'
        f'<rect x="155" y="{90 + y_off}" width="{l_w}" height="24" rx="3" fill="#ef4444"/>'
        f'<text x="{155 + l_w // 2}" y="{106 + y_off}" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">{_fmt_r(liab)}</text>'
        f'<rect x="{155 + l_w}" y="{90 + y_off}" width="{c_w}" height="24" rx="3" fill="#10b981"/>'
        f'<text x="{155 + l_w + c_w // 2}" y="{106 + y_off}" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">?</text>'
        f'<text x="225" y="144" font-size="10" fill="#475569" text-anchor="middle">Assets = Liabilities + Capital</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_financial_transaction_exchange_event(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(120, 850)
    prompt = (
        f"A customer walks into {sc['entrepreneur']}'s shop in {sc['area']} and pays {_fmt_r(amt)} cash in exchange for {sc['item_sold']}.\n\n"
        f"What accounting term describes any action or event where buyers and sellers exchange goods, services, or assets for money?"
    )
    correct = "Financial transaction"
    return _make_mcq(
        rng, "26_financial_transaction_exchange_event", "Defining Financial Transactions", prompt, correct,
        ["Credit note", "Capital budget", "Cash float"],
        f"Whenever buyers and sellers exchange assets, goods, or services for money ({_fmt_r(amt)}), a **{correct}** occurs.",
        "Identify the actual economic exchange action between buyer and seller.",
        "The event itself is a financial transaction; the receipt proves it happened.",
        ["confuses_transaction_with_record"], marks=2,
    )


def arch_27_financial_records_documentation_examples(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(350, 2400)
    prompt = (
        f"After completing sales worth {_fmt_r(amt)} in {sc['area']}, {sc['entrepreneur']} files till slips, bank deposit slips, employee payslips, credit notes, and electronic EFT bank notifications.\n\n"
        f"What collective term describes these written or electronic documents proving that transactions occurred?"
    )
    correct = "Financial records"
    return _make_mcq(
        rng, "27_financial_records_documentation_examples", "Examples of Financial Records", prompt, correct,
        ["Fixed assets", "Long-term liabilities", "Drawings"],
        f"Till slips, deposit slips, payslips, payrolls, credit notes, and bank EFT notifications are examples of **{correct}**.",
        "Think about the paper or digital proof kept after a transaction happens.",
        "Documents that record financial events are financial records.",
        ["unfamiliar_with_source_document_examples"], marks=2,
    )


def arch_28_records_vs_transactions_distinction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(450, 1900)
    prompt = (
        f"{sc['entrepreneur']} sells {_fmt_r(amt)} worth of {sc['item_sold']} in {sc['area']} and hands the customer a printed till slip.\n\n"
        f"Distinguish clearly between **financial transactions** and **financial records** using this example. (4 marks)"
    )
    pts = [
        f"A financial transaction is the actual economic event where a buyer and seller exchange goods, services, or assets for money (paying {_fmt_r(amt)} for {sc['item_sold']}).",
        "A financial record is the written or electronic document (such as the printed till slip) that records and proves that the transaction took place.",
        "Transactions occur first in business operations; records document them afterwards.",
        "Correct reference to the till slip as proof.",
    ]
    sample = (
        f"1. **Financial Transaction:** The real-life event where {sc['entrepreneur']} and the customer exchange {sc['item_sold']} for {_fmt_r(amt)}.\n"
        f"2. **Financial Record:** The printed till slip (or bank EFT notice) that captures and serves as permanent proof of that transaction."
    )
    return _make_typed(
        rng, "28_records_vs_transactions_distinction", "Financial Records vs Transactions", prompt,
        pts, ["exchange", "event", "written", "electronic", "till slip", "proof"], sample,
        "Separate the real-world exchange event from the paper or digital receipt.",
        "One is the action; the other is the documentation of that action.",
        ["confuses_record_with_transaction"], marks=4,
    )


def arch_29_importance_of_financial_records_fraud_sars(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    turnover = rng.randint(45, 160) * 1000
    prompt = (
        f"{sc['entrepreneur']} runs a growing {sc['business_type']} in {sc['area']} with annual revenue of {_fmt_r(turnover)}, "
        f"and is considering throwing away old till slips and bank statements to save space.\n\n"
        f"Explain why it is essential and legally mandatory for businesses to keep accurate financial records. (4 marks)"
    )
    pts = [
        "To prevent fraud and theft within the business by tracking all cash inflows and outflows.",
        "To provide accurate documentation to the South African Revenue Services (SARS).",
        "To prove that the earnings, expenses, and taxable profits declared are true and accurate.",
        "It is illegal not to keep proper financial records of a business's earnings.",
    ]
    sample = (
        f"Keeping financial records (covering the {_fmt_r(turnover)} revenue) is essential because:\n"
        f"1. **Fraud Prevention:** Accurate till slips and deposit records help detect and prevent internal theft or fraud.\n"
        f"2. **SARS Documentation:** Businesses must submit verifiable records to the **South African Revenue Services (SARS)**.\n"
        f"3. **Proving Declared Earnings:** Records prove that declared profits and tax calculations are correct.\n"
        f"4. **Legal Requirement:** Under South African law, it is illegal for a business not to keep financial records of its earnings."
    )
    return _make_typed(
        rng, "29_importance_of_financial_records_fraud_sars", "Importance of Keeping Financial Records", prompt,
        pts, ["fraud", "SARS", "earnings", "illegal", "documentation"], sample,
        "Consider internal theft control, South African tax reporting, and statutory law.",
        "Mention fraud prevention, SARS verification of declared earnings, and legality.",
        ["thinks_record_keeping_is_optional"], marks=4,
    )


def arch_30_transaction_to_record_flow_visual(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(600, 4800)
    ev, doc = rng.choice([
        ("Cash sale at till", "Till slip"),
        ("Cash banked", "Bank deposit slip"),
        ("Staff paid wages", "Payslip & payroll"),
        ("Goods returned", "Credit note"),
    ])
    dspec = _svg_record_flow(rng, ev, doc, amt)
    prompt = (
        f"Refer to the diagram illustrating how {sc['entrepreneur']}'s {sc['business_type']} in {sc['area']} documents a {_fmt_r(amt)} event ({ev}).\n\n"
        f"Which official body in Stage 3 relies on Stage 2's **{doc}** to verify that declared business earnings are accurate?"
    )
    correct = "South African Revenue Services (SARS)"
    return _make_mcq(
        rng, "30_transaction_to_record_flow_visual", "Transaction to Audit Record Flow", prompt, correct,
        ["Consumer Advertising Board", "Local Weather Bureau", "Sports Federation Council"],
        f"In Stage 3, the **South African Revenue Services (SARS)** requires verifiable financial records such as a {doc} ({_fmt_r(amt)}) to audit declared earnings.",
        "Check Stage 3 in the diagram: which national tax authority verifies declared business earnings?",
        "It is South Africa's national revenue and tax authority.",
        ["unfamiliar_with_sars_audit_role"], marks=2, diagram_spec=dspec,
    )


def arch_31_sole_trader_single_owner_concept(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap = rng.randint(15, 50) * 1000
    prompt = (
        f"{sc['entrepreneur']} invests {_fmt_r(cap)} alone to establish and manage a {sc['business_type']} in {sc['area']}, "
        f"keeping all net profits and bearing full responsibility for business debts.\n\n"
        f"What form of ownership describes a business owned and controlled by one single person?"
    )
    correct = "Sole trader"
    return _make_mcq(
        rng, "31_sole_trader_single_owner_concept", "Identifying a Sole Trader", prompt, correct,
        ["Partnership (two or more owners)", "Public listed corporation", "State-owned utility"],
        f"A business owned by a single individual ({sc['entrepreneur']} with {_fmt_r(cap)}) is a **{correct}**, not a partnership of two or more owners.",
        "Notice how many owners hold capital in the business.",
        "Sole means one single owner.",
        ["confuses_sole_trader_with_partnership"], marks=2,
    )


def arch_32_accounting_definition_recording_summarising(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tx_count = rng.randint(45, 180)
    prompt = (
        f"Every month in {sc['area']}, {sc['entrepreneur']} systematically records {tx_count} cash slips, classifies them into assets, liabilities, income, and expenses, "
        f"and summarises profit for decision-making.\n\n"
        f"Which term describes this systematic recording, classifying, and summarising of financial transactions?"
    )
    correct = "Accounting"
    return _make_mcq(
        rng, "32_accounting_definition_recording_summarising", "Defining Accounting", prompt, correct,
        ["Marketing", "Logistics", "Product packaging"],
        f"**{correct}** is the systematic process of recording, classifying, and summarising financial transactions ({tx_count} slips) to inform owners and stakeholders.",
        "Which discipline turns raw till slips into organised financial summaries?",
        "It is the language of business finance: recording, classifying, and summarising money events.",
        ["confuses_accounting_with_marketing"], marks=2,
    )


def arch_33_budget_planning_purpose_vs_business_plan(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    budget_amt = rng.randint(12, 35) * 1000
    prompt = (
        f"Before launching in {sc['area']}, {sc['entrepreneur']} prepares two separate documents: Document X outlines marketing strategy, target customers, and start-up goals; "
        f"Document Y estimates {_fmt_r(budget_amt)} in future monthly income, spending, savings, or borrowing.\n\n"
        f"Which statement correctly identifies Document X and Document Y?"
    )
    correct = "Document X is a business start-up plan (entrepreneurial strategy); Document Y is a budget (planning future income, spending, saving, and borrowing)."
    return _make_mcq(
        rng, "33_budget_planning_purpose_vs_business_plan", "Budget vs Entrepreneurial Start-Up Strategy", prompt, correct,
        [
            "Document X is a till slip; Document Y is a bank overdraft penalty.",
            "Both Document X and Document Y are identical definitions of a cash float.",
            "Document X only tracks past losses; Document Y records staff attendance.",
        ],
        f"Entrepreneurs use a comprehensive start-up strategy to launch a business, whereas a **budget** ({_fmt_r(budget_amt)}) specifically schedules future income, spending, saving, and borrowing.",
        "Separate a full start-up roadmap from a numeric income-and-spending forecast.",
        "A budget focuses on how to spend, save, or borrow money.",
        ["confuses_budget_with_business_plan"], marks=2,
    )


def arch_34_spend_vs_save_budget_allocation_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    windfall = 1_000_000
    edu = rng.randint(180, 260) * 1000
    housing = rng.randint(250, 350) * 1000
    needs_food = rng.randint(90, 140) * 1000
    spend_tot = edu + housing + needs_food
    emerg = rng.randint(100, 160) * 1000
    charity = rng.randint(30, 60) * 1000
    long_save = windfall - spend_tot - emerg - charity
    save_tot = emerg + charity + long_save
    prompt = (
        f"{sc['entrepreneur']} in {sc['area']} wins R1 000 000 and splits it carefully into **Spend** and **Save** columns:\n"
        f"- Spend — Education & Training: {_fmt_r(edu)}\n"
        f"- Spend — Accommodation & Transport: {_fmt_r(housing)}\n"
        f"- Spend — Monthly Needs (Food, Water, Electricity): {_fmt_r(needs_food)}\n"
        f"- Save — Emergency Reserve (Doctors & Repairs): {_fmt_r(emerg)}\n"
        f"- Save — Community Charity Support: {_fmt_r(charity)}\n\n"
        f"Complete the Spend & Save table to find **Total Spend**, **Long-term Notice Deposit**, and **Total Save** so all R1 000 000 is allocated."
    )
    headers = ["Allocation Item", "Column", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Education & Training", "editable": False}, {"cell_id": "r0_c1", "value": "Spend", "editable": False}, {"cell_id": "r0_c2", "value": str(edu), "editable": False}],
        [{"cell_id": "r1_c0", "value": "Accommodation & Transport", "editable": False}, {"cell_id": "r1_c1", "value": "Spend", "editable": False}, {"cell_id": "r1_c2", "value": str(housing), "editable": False}],
        [{"cell_id": "r2_c0", "value": "Monthly Needs (Food & Utilities)", "editable": False}, {"cell_id": "r2_c1", "value": "Spend", "editable": False}, {"cell_id": "r2_c2", "value": str(needs_food), "editable": False}],
        [{"cell_id": "r3_c0", "value": "Total Spend", "editable": False}, {"cell_id": "r3_c1", "value": "Spend", "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": str(spend_tot), "editable": True}],
        [{"cell_id": "r4_c0", "value": "Emergency Reserve", "editable": False}, {"cell_id": "r4_c1", "value": "Save", "editable": False}, {"cell_id": "r4_c2", "value": str(emerg), "editable": False}],
        [{"cell_id": "r5_c0", "value": "Community Charity Donation", "editable": False}, {"cell_id": "r5_c1", "value": "Save", "editable": False}, {"cell_id": "r5_c2", "value": str(charity), "editable": False}],
        [{"cell_id": "r6_c0", "value": "Long-term Notice Deposit", "editable": False}, {"cell_id": "r6_c1", "value": "Save", "editable": False}, {"cell_id": "r6_c2", "value": "", "expected": str(long_save), "editable": True}],
        [{"cell_id": "r7_c0", "value": "Total Save", "editable": False}, {"cell_id": "r7_c1", "value": "Save", "editable": False}, {"cell_id": "r7_c2", "value": "", "expected": str(save_tot), "editable": True}],
    ]
    cmap = {"r3_c2": str(spend_tot), "r6_c2": str(long_save), "r7_c2": str(save_tot)}
    chints = {
        "r3_c2": f"Sum Spend items: {edu} + {housing} + {needs_food}.",
        "r7_c2": f"Remaining after Total Spend: 1000000 - {spend_tot}.",
        "r6_c2": f"Total Save ({save_tot}) - Emergency ({emerg}) - Charity ({charity}).",
    }
    memo = (
        f"| Allocation Item | Column | Amount (R) |\n| :--- | :---: | :---: |\n"
        f"| Education & Training | Spend | {edu} |\n"
        f"| Accommodation & Transport | Spend | {housing} |\n"
        f"| Monthly Needs | Spend | {needs_food} |\n"
        f"| **Total Spend** | **Spend** | **{spend_tot}** |\n"
        f"| Emergency Reserve | Save | {emerg} |\n"
        f"| Charity Donation | Save | {charity} |\n"
        f"| **Long-term Notice Deposit** | **Save** | **{long_save}** |\n"
        f"| **Total Save** | **Save** | **{save_tot}** |"
    )
    return _make_ledger(
        rng, "34_spend_vs_save_budget_allocation_table", "R1 Million Spend & Save Planner",
        prompt, headers, rows, cmap, chints, memo,
        "Sum all Spend items first, subtract Total Spend from R1 000 000 to get Total Save, then find the Notice Deposit balance.",
        f"Total Spend = {spend_tot}; Total Save = 1000000 - {spend_tot}.",
        ["spends_all_windfall_without_saving"], marks=6,
    )


def arch_35_savings_short_term_goal_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    saved = rng.randint(3, 12) * 250
    prompt = (
        f"After paying all essential monthly expenses in {sc['area']}, {sc['entrepreneur']} puts away {_fmt_r(saved)} into a separate bank account for a short-term goal.\n\n"
        f"In EMS financial literacy, what is **savings**?"
    )
    correct = "Money set aside after covering expenses, kept safely for emergencies or short-term and future goals."
    return _make_mcq(
        rng, "35_savings_short_term_goal_definition", "Defining Savings", prompt, correct,
        [
            "Money borrowed from a store on a credit card to buy luxury shoes.",
            "Cash taken out of the till by an employee without permission.",
            "Mandatory income tax paid to SARS at year-end.",
        ],
        f"**Savings** ({_fmt_r(saved)}) is the surplus money put away once living or business expenses have been covered.",
        "Think about what remains after expenses are covered.",
        "Savings means setting money aside rather than spending everything earned.",
        ["confuses_savings_with_borrowing"], marks=2,
    )


def arch_36_seven_golden_rules_for_saving(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    income = rng.randint(5, 11) * 1000
    overspend = rng.randint(1, 3) * 1000
    prompt = (
        f"{name} earns {_fmt_r(income)} per month, spends {_fmt_r(income + overspend)} using store credit on designer clothes before buying groceries, "
        f"and keeps zero emergency cash.\n\n"
        f"Identify and explain **four sound guidelines for saving money** that {name} should apply to recover financially. (4 marks)"
    )
    pts = [
        "Never spend more than the amount you earn (avoid living on debt).",
        "Prioritise buying what you need first before carefully considering wants.",
        "Pay off all existing debt and stay out of unnecessary high-interest credit.",
        "Keep emergency funds for unexpected medical, vehicle, or household expenses (and plan long term beyond 5 years).",
    ]
    sample = (
        f"To recover from spending {_fmt_r(income + overspend)} on {_fmt_r(income)} income, {name} should follow four key saving rules:\n"
        f"1. **Live within earnings:** Never spend more than you earn.\n"
        f"2. **Needs before wants:** Buy basic necessities first and think carefully before buying luxury wants.\n"
        f"3. **Eliminate debt:** Pay off store credit and avoid interest charges.\n"
        f"4. **Emergency & long-term planning:** Keep emergency funds for medical/repair bills and plan long term (beyond five years)."
    )
    return _make_typed(
        rng, "36_seven_golden_rules_for_saving", "Guidelines for Wise Saving", prompt,
        pts, ["earn", "needs", "wants", "debt", "emergency", "long term"], sample,
        "Check what {name} did wrong: overspending, buying wants first, using credit, and holding no emergency cash.",
        "State four clear saving habits from financial literacy guidelines.",
        ["ignores_emergency_fund_and_needs_priority"], marks=4,
    )


def arch_37_banking_services_identification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} opens a business account at a South African commercial bank to manage payments from {sc['area']}.\n\n"
        f"Which group contains **only** authentic services provided by commercial banks?"
    )
    correct = "Cellphone and internet banking, bank statements, third-party payments, foreign exchange enquiries, loan applications, wills, and financial/retirement planning."
    return _make_mcq(
        rng, "37_banking_services_identification", "Services Offered by Banks", prompt, correct,
        [
            "Selling groceries, baking bread, repairing cars, and collecting municipal refuse.",
            "Printing national laws, policing highways, and grading school exams.",
            "Issuing matric certificates and manufacturing factory trucks.",
        ],
        "Banks offer digital cellphone/internet banking, balance enquiries, bank statements, third-party payments, exchange rate queries, account management, loans, wills, and retirement planning.",
        "Select the list containing genuine financial and banking services.",
        "Look for account statements, digital transfers, loans, and financial planning.",
        ["unfamiliar_with_banking_services"], marks=2,
    )


def arch_38_banking_digital_vs_branch_rural_access(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    dist = rng.choice([28, 35, 42, 55])
    prompt = (
        f"{sc['entrepreneur']} operates a {sc['business_type']} in {sc['rural_area']}, where the nearest physical bank branch is {dist} km away.\n\n"
        f"Explain how **cellphone and internet banking** plus **electronic bank statements** help overcome this rural access barrier. (4 marks)"
    )
    pts = [
        f"Saves travel time and taxi/transport costs over the {dist} km distance to a town bank branch.",
        "Allows instant payment to suppliers (third-party EFT payments) and checking bank balances anytime.",
        "Provides digital payment notifications and downloadable bank statements as official financial records.",
        "Enables safe cashless operations without carrying large amounts of physical cash.",
    ]
    sample = (
        f"1. **Saves Transport & Time:** {sc['entrepreneur']} avoids spending money and hours travelling {dist} km to town.\n"
        f"2. **Instant Third-Party Payments:** Suppliers can be paid via cellphone/internet EFT and balances checked immediately.\n"
        f"3. **Digital Financial Records:** Electronic payment notifications and bank statements act as reliable audit records.\n"
        f"4. **Cash Safety:** Reduces the risk of theft from carrying physical cash over long rural distances."
    )
    return _make_typed(
        rng, "38_banking_digital_vs_branch_rural_access", "Rural Banking & Digital Access", prompt,
        pts, ["travel", "third-party", "balances", "statements", "safety"], sample,
        f"Think about the challenges of being {dist} km from a branch when paying suppliers and checking balances.",
        "Mention cost savings, instant EFT payments, digital financial records, and safety.",
        ["overlooks_rural_banking_services"], marks=4,
    )


def arch_39_banking_economic_growth_capital_role(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    loan = rng.randint(50, 150) * 1000
    prompt = (
        f"A commercial bank lends {_fmt_r(loan)} to {sc['entrepreneur']} in {sc['area']} to purchase industrial equipment and expand production.\n\n"
        f"Explain why bank lending for capital investment is important for South Africa's broader economy. (4 marks)"
    )
    pts = [
        "Banks provide capital investment loans that enable businesses to buy equipment and expand capacity.",
        "Business expansion creates new employment (work opportunities) for local community members.",
        "Increased production and jobs promote the country's overall economic growth.",
        "Higher output and household wages stimulate and satisfy the country's needs and wants.",
    ]
    sample = (
        f"When banks lend {_fmt_r(loan)} for productive **capital investment**:\n"
        f"1. **Job Creation:** Expanding businesses hire more workers, creating employment opportunities.\n"
        f"2. **Economic Growth:** Higher business output grows South Africa's GDP and tax base.\n"
        f"3. **Needs & Wants:** Businesses produce more goods and employees earn wages to satisfy needs and wants."
    )
    return _make_typed(
        rng, "39_banking_economic_growth_capital_role", "Role of Banking in the Economy", prompt,
        pts, ["capital investment", "work opportunities", "economic growth", "needs and wants"], sample,
        "Trace what happens after a bank lends capital for equipment: hiring, output, and spending.",
        "Link bank capital loans to job creation, economic growth, and satisfying needs and wants.",
        ["thinks_banks_only_store_money"], marks=4,
    )


def arch_40_banking_capital_jobs_cycle_visual(rng: random.Random) -> Dict[str, Any]:
    loan = rng.randint(60, 200) * 1000
    jobs = rng.randint(3, 9)
    dspec = _svg_bank_economy_cycle(rng, loan, jobs)
    prompt = (
        f"Examine the economic banking cycle diagram showing a {_fmt_r(loan)} bank loan creating {jobs} new jobs.\n\n"
        f"What essential role does the commercial bank perform in the first block to trigger job creation and economic growth?"
    )
    correct = f"It channels deposited savings into productive capital investment loans ({_fmt_r(loan)}) so entrepreneurs can expand operations and employ {jobs} workers."
    return _make_mcq(
        rng, "40_banking_capital_jobs_cycle_visual", "Banking Capital & Jobs Cycle", prompt, correct,
        [
            "It prints bank notes independently and gives them away free without repayment.",
            "It prevents businesses from borrowing money so economic output shrinks.",
            "It pays employee salaries directly on behalf of every private spaza shop.",
        ],
        f"Banks boost the economy by lending {_fmt_r(loan)} for capital investment, which creates {jobs} work opportunities, drives growth, and stimulates needs and wants.",
        "Trace the arrow from the Commercial Bank to Capital Investment.",
        "Bank loans fund capital investments, creating jobs and growth.",
        ["misses_bank_capital_intermediation"], marks=2, diagram_spec=dspec,
    )


def arch_41_interest_cost_of_borrowing_on_credit(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    cash_price = rng.choice([6000, 8000, 10000, 12000])
    months = rng.choice([12, 18, 24])
    monthly_inst = int((cash_price * rng.choice([1.25, 1.30, 1.35])) // months)
    total_credit = monthly_inst * months
    extra_interest = total_credit - cash_price
    prompt = (
        f"{name} wants to buy business computer equipment priced at {_fmt_r(cash_price)} cash. Instead of saving first, {name} buys it on credit over "
        f"{months} monthly instalments of {_fmt_r(monthly_inst)} each.\n\n"
        f"Calculate the extra amount (interest cost) {name} pays in addition to the original cash price."
    )
    sol = (
        f"**Step 1:** Total Credit Paid = ${months} \\times {_fmt_r(monthly_inst)} = {_fmt_r(total_credit)}$\n"
        f"**Step 2:** Extra Interest Cost = ${_fmt_r(total_credit)} - {_fmt_r(cash_price)} = {_fmt_r(extra_interest)}$\n"
        f"**Answer:** **{_fmt_r(extra_interest)}**"
    )
    return _make_calc(
        rng, "41_interest_cost_of_borrowing_on_credit", "Cost of Buying on Credit",
        prompt, extra_interest, f"({months} × {monthly_inst}) - {cash_price}", sol,
        "First find the total paid across all monthly instalments, then subtract the cash price.",
        f"Compute {months} × {monthly_inst}, then subtract {cash_price}.",
        ["confuses_total_credit_paid_with_interest"], marks=3,
    )


def arch_42_comprehensive_accounting_concepts_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap = rng.randint(35, 65) * 1000
    van = rng.randint(25, 45) * 1000
    loan = rng.randint(10, 20) * 1000
    sales = rng.randint(12, 24) * 1000
    rent = rng.randint(3, 6) * 1000
    prompt = (
        f"Classify each accounting balance from {sc['entrepreneur']}'s {sc['business_type']} in {sc['area']} "
        f"into one of the five core elements: **Capital**, **Asset**, **Liability**, **Income**, or **Expense**, and calculate **Net Profit**."
    )
    net_prof = sales - rent
    headers = ["Account / Item", "Amount (R)", "Accounting Element"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Owner Start-up Funds", "editable": False}, {"cell_id": "r0_c1", "value": str(cap), "editable": False}, {"cell_id": "r0_c2", "value": "", "expected": "Capital", "editable": True}],
        [{"cell_id": "r1_c0", "value": "Delivery Van", "editable": False}, {"cell_id": "r1_c1", "value": str(van), "editable": False}, {"cell_id": "r1_c2", "value": "", "expected": "Asset", "editable": True}],
        [{"cell_id": "r2_c0", "value": "Long-Term Bank Loan", "editable": False}, {"cell_id": "r2_c1", "value": str(loan), "editable": False}, {"cell_id": "r2_c2", "value": "", "expected": "Liability", "editable": True}],
        [{"cell_id": "r3_c0", "value": f"Sales ({sc['item_sold']})", "editable": False}, {"cell_id": "r3_c1", "value": str(sales), "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": "Income", "editable": True}],
        [{"cell_id": "r4_c0", "value": "Shop Rent Paid", "editable": False}, {"cell_id": "r4_c1", "value": str(rent), "editable": False}, {"cell_id": "r4_c2", "value": "", "expected": "Expense", "editable": True}],
        [{"cell_id": "r5_c0", "value": "Net Profit (Sales - Rent)", "editable": False}, {"cell_id": "r5_c1", "value": "", "expected": str(net_prof), "editable": True}, {"cell_id": "r5_c2", "value": "Profit", "editable": False}],
    ]
    cmap = {"r0_c2": "Capital", "r1_c2": "Asset", "r2_c2": "Liability", "r3_c2": "Income", "r4_c2": "Expense", "r5_c1": str(net_prof)}
    chints = {
        "r0_c2": "Owner start-up money -> Capital.",
        "r1_c2": "Possession owned -> Asset.",
        "r2_c2": "Debt owed to bank -> Liability.",
        "r3_c2": "Receipts from customers -> Income.",
        "r4_c2": "Operational running cost -> Expense.",
        "r5_c1": f"Sales ({sales}) - Rent ({rent}).",
    }
    memo = (
        f"| Account / Item | Amount (R) | Element |\n| :--- | :---: | :--- |\n"
        f"| Owner Start-up Funds | {cap} | Capital |\n"
        f"| Delivery Van | {van} | Asset |\n"
        f"| Bank Loan | {loan} | Liability |\n"
        f"| Sales | {sales} | Income |\n"
        f"| Shop Rent | {rent} | Expense |\n"
        f"| **Net Profit** | **{net_prof}** | Profit |"
    )
    return _make_ledger(
        rng, "42_comprehensive_accounting_concepts_classification_table", "5-Element Accounting Classification",
        prompt, headers, rows, cmap, chints, memo,
        "Use exact terms: Capital, Asset, Liability, Income, Expense.",
        f"Profit = Sales ({sales}) - Rent ({rent}).",
        ["confuses_five_accounting_elements"], marks=6,
    )


def arch_43_statement_of_financial_position_equity_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    eq_a = rng.randint(20, 45) * 1000
    bank_a = rng.randint(6, 15) * 1000
    stock_a = rng.randint(8, 18) * 1000
    tot_a = eq_a + bank_a + stock_a
    lt_l = rng.randint(10, 22) * 1000
    cur_l = rng.randint(2, 6) * 1000
    tot_l = lt_l + cur_l
    equity = tot_a - tot_l
    prompt = (
        f"{sc['entrepreneur']} lists all assets and liabilities for a {sc['business_type']} in {sc['area']}:\n"
        f"- Equipment (Fixed Asset): {_fmt_r(eq_a)}\n"
        f"- Bank Balance (Current Asset): {_fmt_r(bank_a)}\n"
        f"- Trading Stock (Current Asset): {_fmt_r(stock_a)}\n"
        f"- 5-Year Bank Loan (Long-term Liability): {_fmt_r(lt_l)}\n"
        f"- Trade Creditors (Current Liability): {_fmt_r(cur_l)}\n\n"
        f"Complete the summary table to calculate **Total Assets**, **Total Liabilities**, and **Owner's Equity**."
    )
    headers = ["Section / Item", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Equipment (Fixed Asset)", "editable": False}, {"cell_id": "r0_c1", "value": str(eq_a), "editable": False}],
        [{"cell_id": "r1_c0", "value": "Bank Balance (Current Asset)", "editable": False}, {"cell_id": "r1_c1", "value": str(bank_a), "editable": False}],
        [{"cell_id": "r2_c0", "value": "Trading Stock (Current Asset)", "editable": False}, {"cell_id": "r2_c1", "value": str(stock_a), "editable": False}],
        [{"cell_id": "r3_c0", "value": "Total Assets", "editable": False}, {"cell_id": "r3_c1", "value": "", "expected": str(tot_a), "editable": True}],
        [{"cell_id": "r4_c0", "value": "5-Year Bank Loan (Long-term Liability)", "editable": False}, {"cell_id": "r4_c1", "value": str(lt_l), "editable": False}],
        [{"cell_id": "r5_c0", "value": "Trade Creditors (Current Liability)", "editable": False}, {"cell_id": "r5_c1", "value": str(cur_l), "editable": False}],
        [{"cell_id": "r6_c0", "value": "Total Liabilities", "editable": False}, {"cell_id": "r6_c1", "value": "", "expected": str(tot_l), "editable": True}],
        [{"cell_id": "r7_c0", "value": "Owner's Equity (Assets - Liabilities)", "editable": False}, {"cell_id": "r7_c1", "value": "", "expected": str(equity), "editable": True}],
    ]
    cmap = {"r3_c1": str(tot_a), "r6_c1": str(tot_l), "r7_c1": str(equity)}
    chints = {
        "r3_c1": f"Sum all three assets: {eq_a} + {bank_a} + {stock_a}.",
        "r6_c1": f"Sum both liabilities: {lt_l} + {cur_l}.",
        "r7_c1": f"Subtract Total Liabilities ({tot_l}) from Total Assets ({tot_a}).",
    }
    memo = (
        f"| Section / Item | Amount (R) |\n| :--- | :---: |\n"
        f"| Equipment | {eq_a} |\n| Bank Balance | {bank_a} |\n| Trading Stock | {stock_a} |\n"
        f"| **Total Assets** | **{tot_a}** |\n"
        f"| 5-Year Bank Loan | {lt_l} |\n| Trade Creditors | {cur_l} |\n"
        f"| **Total Liabilities** | **{tot_l}** |\n"
        f"| **Owner's Equity** | **{equity}** |"
    )
    return _make_ledger(
        rng, "43_statement_of_financial_position_equity_table", "Calculating Owner's Equity from Assets & Liabilities",
        prompt, headers, rows, cmap, chints, memo,
        "Sum Assets, sum Liabilities, then subtract Liabilities from Assets.",
        f"Total Assets = {tot_a}; Total Liabilities = {tot_l}; Owner's Equity = {equity}.",
        ["adds_liabilities_instead_of_subtracts"], marks=5,
    )


def arch_44_true_false_accounting_misconceptions_audit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    statements = [
        ("Loss occurs when expenses exceed receipts for services rendered.", "True", "Loss is indeed Expenses > Income."),
        ("Cash float is the money an owner takes home for personal use.", "False", "Drawings is for personal use; Cash float is till change."),
        ("A sole trader is a business owned by two partners.", "False", "A sole trader has only one single owner."),
        ("Trading stock consists of items bought to resell at a profit.", "True", "Trading stock is bought for resale at a profit."),
        ("Receipts that increase owner's equity are called income.", "True", "Income increases Owner's Equity."),
    ]
    rng.shuffle(statements)
    chosen = statements[:4]
    prompt = (
        f"{sc['entrepreneur']} is preparing for an accounting quiz in {sc['area']}. "
        f"Evaluate each statement in the schedule below by entering **True** or **False**."
    )
    headers = ["Accounting Statement", "True or False"]
    rows, cmap, chints, memo_lines = [], {}, {}, ["| Statement | Answer | Reason |", "| :--- | :---: | :--- |"]
    for idx, (stmt, ans, reason) in enumerate(chosen):
        cid = f"r{idx}_c1"
        rows.append([{"cell_id": f"r{idx}_c0", "value": stmt, "editable": False}, {"cell_id": cid, "value": "", "expected": ans, "editable": True}])
        cmap[cid] = ans
        chints[cid] = f"Check definition carefully: {reason}"
        memo_lines.append(f"| {stmt} | **{ans}** | {reason} |")
    return _make_ledger(
        rng, "44_true_false_accounting_misconceptions_audit", "Accounting Concepts True/False Audit",
        prompt, headers, rows, cmap, chints, "\n".join(memo_lines),
        "Enter exactly 'True' or 'False' in each cell.",
        "Check terms like cash float vs drawings, sole trader owner count, and profit/loss.",
        ["holds_common_accounting_definitions_myths"], marks=4,
    )


def arch_45_source_document_to_transaction_matching_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pairs = [
        (f"Customer buys {sc['item_sold']} for cash at counter", "Till slip"),
        ("Business deposits daily cash takings at the bank", "Bank deposit slip"),
        ("Monthly wages paid to shop assistant", "Payslip"),
        ("Customer returns damaged item for an allowance", "Credit note"),
    ]
    rng.shuffle(pairs)
    prompt = (
        f"Match each business event at {sc['entrepreneur']}'s {sc['business_type']} in {sc['area']} to its financial record by entering one of: "
        f"**Till slip**, **Bank deposit slip**, **Payslip**, or **Credit note**."
    )
    headers = ["Business Transaction", "Financial Record"]
    rows, cmap, chints, memo_lines = [], {}, {}, ["| Business Transaction | Financial Record |", "| :--- | :--- |"]
    for idx, (tx, rec) in enumerate(pairs):
        cid = f"r{idx}_c1"
        rows.append([{"cell_id": f"r{idx}_c0", "value": tx, "editable": False}, {"cell_id": cid, "value": "", "expected": rec, "editable": True}])
        cmap[cid] = rec
        chints[cid] = f"Which source record proves '{tx}'?"
        memo_lines.append(f"| {tx} | **{rec}** |")
    return _make_ledger(
        rng, "45_source_document_to_transaction_matching_table", "Matching Transactions to Financial Records",
        prompt, headers, rows, cmap, chints, "\n".join(memo_lines),
        "Choose among Till slip, Bank deposit slip, Payslip, Credit note.",
        "Sales -> Till slip; banking cash -> Bank deposit slip; wages -> Payslip; returns -> Credit note.",
        ["confuses_source_documents"], marks=4,
    )


def arch_46_sars_tax_compliance_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randint(150, 300) * 1000
    doc_exp = rng.randint(80, 120) * 1000
    lost_slips = rng.randint(10, 25) * 1000
    tax_rate = rng.choice([20, 25])
    # Without proof, SARS taxes higher taxable profit (only documented expenses deductible)
    taxable_without_proof = sales - doc_exp
    tax_owed = int(taxable_without_proof * tax_rate / 100)
    prompt = (
        f"{sc['entrepreneur']}'s {sc['business_type']} in {sc['area']} recorded {_fmt_r(sales)} in sales. "
        f"It has verified till slips and EFT records for {_fmt_r(doc_exp)} of expenses, plus {_fmt_r(lost_slips)} in undocumented cash spending where receipts were thrown away.\n\n"
        f"Because SARS only accepts documented expense deductions, calculate the tax payable at **{tax_rate}%** of documented taxable profit "
        f"(Sales − Documented Expenses)."
    )
    sol = (
        f"**Step 1:** Documented Taxable Profit = ${_fmt_r(sales)} - {_fmt_r(doc_exp)} = {_fmt_r(taxable_without_proof)}$ "
        f"(the {_fmt_r(lost_slips)} without slips cannot be deducted).\n"
        f"**Step 2:** Tax Payable = ${tax_rate}\\% \\times {_fmt_r(taxable_without_proof)} = {_fmt_r(tax_owed)}$\n"
        f"**Answer:** **{_fmt_r(tax_owed)}**"
    )
    return _make_calc(
        rng, "46_sars_tax_compliance_calculation", "SARS Record Verification & Tax Impact",
        prompt, tax_owed, f"({sales} - {doc_exp}) × {tax_rate}%", sol,
        "Remember: SARS only allows expenses that are backed by valid financial records.",
        f"Subtract {_fmt_r(doc_exp)} from {_fmt_r(sales)}, then take {tax_rate}%.",
        ["deducts_undocumented_expenses_for_sars"], marks=3,
    )


def arch_47_rural_spaza_accounting_case_study(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap = rng.randint(5, 12) * 1000
    draw = rng.randint(400, 1100)
    prompt = (
        f"**Case Study:** {sc['entrepreneur']} opened a tuckshop selling {sc['item_sold']} in {sc['rural_area']} using {_fmt_r(cap)} from personal savings. "
        f"{sc['entrepreneur']} does not keep till slips, leaves zero cash float in the morning, and takes {_fmt_r(draw)} from the till each weekend for family groceries without writing it down.\n\n"
        f"Diagnose **three accounting mistakes** in {sc['entrepreneur']}'s practices and recommend a practical fix for each. (6 marks)"
    )
    pts = [
        "No financial records (till slips/deposit records) kept: risks fraud/theft and violates SARS legal requirements -> keep a receipt book / daily sales log.",
        f"Unrecorded personal withdrawals ({_fmt_r(draw)}) are Drawings, not business income/loss -> record all Drawings separately from business expenses.",
        "No morning Cash Float -> set aside a fixed Cash Float in the till every morning to make change smoothly.",
        "Mixing personal household money with business cash hurts cash flow -> separate personal and business money.",
    ]
    sample = (
        f"1. **Missing Financial Records:** Not keeping slips invites theft/errors and breaks SARS tax rules. *Fix:* File till slips and daily sales totals.\n"
        f"2. **Unrecorded Drawings ({_fmt_r(draw)}):** Taking till cash for family groceries reduces Owner's Equity and distorts profit. *Fix:* Record all owner withdrawals as **Drawings**.\n"
        f"3. **No Cash Float:** Opening with zero change delays cash sales. *Fix:* Maintain a dedicated **Cash Float** in the till."
    )
    return _make_typed(
        rng, "47_rural_spaza_accounting_case_study", "Spaza Accounting Controls Case Study", prompt,
        pts, ["records", "SARS", "Drawings", "Cash Float", "separate"], sample,
        "Identify issues around receipts, personal till withdrawals, and till change.",
        "Discuss missing financial records, unrecorded Drawings, and lack of Cash Float.",
        ["treats_business_till_as_personal_wallet"], marks=6,
    )


def arch_48_net_worth_and_capital_bar_visual(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    liab = rng.randint(12, 30) * 1000
    cap = rng.randint(30, 70) * 1000
    assets = liab + cap
    dspec = _svg_equity_bars(rng, assets, liab, cap, sc["business_type"])
    prompt = (
        f"Study the accounting bar diagram for {sc['entrepreneur']}'s {sc['business_type']} in {sc['area']}.\n\n"
        f"Given Total Assets of {_fmt_r(assets)} and Liabilities of {_fmt_r(liab)}, calculate the missing **Capital** value marked `?`."
    )
    sol = (
        f"**Step 1:** $\\text{{Assets}} = \\text{{Liabilities}} + \\text{{Capital}}$\n"
        f"**Step 2:** $\\text{{Capital}} = {_fmt_r(assets)} - {_fmt_r(liab)} = {_fmt_r(cap)}$\n"
        f"**Answer:** **{_fmt_r(cap)}**"
    )
    return _make_calc(
        rng, "48_net_worth_and_capital_bar_visual", "Visual Capital & Liabilities Balance",
        prompt, cap, f"{assets} - {liab}", sol,
        "Both horizontal bars represent the exact same total value.",
        f"Subtract Liabilities ({_fmt_r(liab)}) from Assets ({_fmt_r(assets)}).",
        ["confuses_assets_minus_liabilities"], marks=3, diagram_spec=dspec,
    )


def arch_49_emergency_fund_target_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    rent = rng.randint(25, 45) * 100
    food = rng.randint(18, 30) * 100
    utils = rng.randint(6, 12) * 100
    months = rng.choice([3, 4, 6])
    monthly_ess = rent + food + utils
    target = monthly_ess * months
    prompt = (
        f"Following sound saving guidelines, {name} builds an emergency fund covering **{months} months** of essential household expenses:\n"
        f"- Accommodation: {_fmt_r(rent)}/month\n"
        f"- Basic food & water: {_fmt_r(food)}/month\n"
        f"- Electricity & medical buffer: {_fmt_r(utils)}/month\n\n"
        f"Calculate the total **Emergency Fund** target {name} needs to save."
    )
    sol = (
        f"**Step 1:** Monthly Essential Costs = ${_fmt_r(rent)} + {_fmt_r(food)} + {_fmt_r(utils)} = {_fmt_r(monthly_ess)}$\n"
        f"**Step 2:** {months}-Month Emergency Fund = ${months} \\times {_fmt_r(monthly_ess)} = {_fmt_r(target)}$\n"
        f"**Answer:** **{_fmt_r(target)}**"
    )
    return _make_calc(
        rng, "49_emergency_fund_target_calculation", "Calculating an Emergency Reserve Target",
        prompt, target, f"({rent} + {food} + {utils}) × {months}", sol,
        "Add the three monthly essential expenses first, then multiply by the number of months.",
        f"Monthly total = {_fmt_r(monthly_ess)}; multiply by {months}.",
        ["forgets_to_multiply_by_months"], marks=3,
    )


def arch_50_comprehensive_term2_concepts_synthesis(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_cap = rng.randint(40, 75) * 1000
    inc = rng.randint(22, 42) * 1000
    exp = rng.randint(12, 20) * 1000
    draw = rng.randint(2, 5) * 1000
    profit = inc - exp
    close_eq = open_cap + profit - draw
    prompt = (
        f"Complete the year-end accounting summary schedule for {sc['entrepreneur']}'s sole trader {sc['business_type']} in {sc['area']}:\n"
        f"- Opening Capital: {_fmt_r(open_cap)}\n"
        f"- Total Income (Sales): {_fmt_r(inc)}\n"
        f"- Total Expenses: {_fmt_r(exp)}\n"
        f"- Owner Drawings: {_fmt_r(draw)}\n\n"
        f"Calculate **Net Profit**, identify the **Impact on Equity** of Drawings (**Decreases**), and calculate **Closing Owner's Equity**."
    )
    headers = ["Financial Item", "Amount (R)", "Effect on Equity"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Opening Capital", "editable": False}, {"cell_id": "r0_c1", "value": str(open_cap), "editable": False}, {"cell_id": "r0_c2", "value": "Increases", "editable": False}],
        [{"cell_id": "r1_c0", "value": "Total Income", "editable": False}, {"cell_id": "r1_c1", "value": str(inc), "editable": False}, {"cell_id": "r1_c2", "value": "Increases", "editable": False}],
        [{"cell_id": "r2_c0", "value": "Total Expenses", "editable": False}, {"cell_id": "r2_c1", "value": str(exp), "editable": False}, {"cell_id": "r2_c2", "value": "Decreases", "editable": False}],
        [{"cell_id": "r3_c0", "value": "Net Profit (Income - Expenses)", "editable": False}, {"cell_id": "r3_c1", "value": "", "expected": str(profit), "editable": True}, {"cell_id": "r3_c2", "value": "Increases", "editable": False}],
        [{"cell_id": "r4_c0", "value": "Owner Drawings", "editable": False}, {"cell_id": "r4_c1", "value": str(draw), "editable": False}, {"cell_id": "r4_c2", "value": "", "expected": "Decreases", "editable": True}],
        [{"cell_id": "r5_c0", "value": "Closing Owner's Equity", "editable": False}, {"cell_id": "r5_c1", "value": "", "expected": str(close_eq), "editable": True}, {"cell_id": "r5_c2", "value": "Owner Share", "editable": False}],
    ]
    cmap = {"r3_c1": str(profit), "r4_c2": "Decreases", "r5_c1": str(close_eq)}
    chints = {
        "r3_c1": f"Income ({inc}) - Expenses ({exp}).",
        "r4_c2": "Personal withdrawals by the owner decrease equity ('Decreases').",
        "r5_c1": f"Opening Capital ({open_cap}) + Net Profit ({profit}) - Drawings ({draw}).",
    }
    memo = (
        f"| Financial Item | Amount (R) | Effect on Equity |\n| :--- | :---: | :--- |\n"
        f"| Opening Capital | {open_cap} | Increases |\n"
        f"| Total Income | {inc} | Increases |\n"
        f"| Total Expenses | {exp} | Decreases |\n"
        f"| **Net Profit** | **{profit}** | Increases |\n"
        f"| Owner Drawings | {draw} | **Decreases** |\n"
        f"| **Closing Owner's Equity** | **{close_eq}** | Owner Share |"
    )
    return _make_ledger(
        rng, "50_comprehensive_term2_concepts_synthesis", "Closing Owner's Equity Reconciliation",
        prompt, headers, rows, cmap, chints, memo,
        "Compute Net Profit first, classify Drawings' equity impact, then calculate Closing Equity.",
        f"Net Profit = {profit}; Drawings = Decreases; Closing Equity = {open_cap} + {profit} - {draw}.",
        ["forgets_to_deduct_drawings_from_equity"], marks=5,
    )


BUILDERS_26_50 = {
    "26_financial_transaction_exchange_event": arch_26_financial_transaction_exchange_event,
    "27_financial_records_documentation_examples": arch_27_financial_records_documentation_examples,
    "28_records_vs_transactions_distinction": arch_28_records_vs_transactions_distinction,
    "29_importance_of_financial_records_fraud_sars": arch_29_importance_of_financial_records_fraud_sars,
    "30_transaction_to_record_flow_visual": arch_30_transaction_to_record_flow_visual,
    "31_sole_trader_single_owner_concept": arch_31_sole_trader_single_owner_concept,
    "32_accounting_definition_recording_summarising": arch_32_accounting_definition_recording_summarising,
    "33_budget_planning_purpose_vs_business_plan": arch_33_budget_planning_purpose_vs_business_plan,
    "34_spend_vs_save_budget_allocation_table": arch_34_spend_vs_save_budget_allocation_table,
    "35_savings_short_term_goal_definition": arch_35_savings_short_term_goal_definition,
    "36_seven_golden_rules_for_saving": arch_36_seven_golden_rules_for_saving,
    "37_banking_services_identification": arch_37_banking_services_identification,
    "38_banking_digital_vs_branch_rural_access": arch_38_banking_digital_vs_branch_rural_access,
    "39_banking_economic_growth_capital_role": arch_39_banking_economic_growth_capital_role,
    "40_banking_capital_jobs_cycle_visual": arch_40_banking_capital_jobs_cycle_visual,
    "41_interest_cost_of_borrowing_on_credit": arch_41_interest_cost_of_borrowing_on_credit,
    "42_comprehensive_accounting_concepts_classification_table": arch_42_comprehensive_accounting_concepts_classification_table,
    "43_statement_of_financial_position_equity_table": arch_43_statement_of_financial_position_equity_table,
    "44_true_false_accounting_misconceptions_audit": arch_44_true_false_accounting_misconceptions_audit,
    "45_source_document_to_transaction_matching_table": arch_45_source_document_to_transaction_matching_table,
    "46_sars_tax_compliance_calculation": arch_46_sars_tax_compliance_calculation,
    "47_rural_spaza_accounting_case_study": arch_47_rural_spaza_accounting_case_study,
    "48_net_worth_and_capital_bar_visual": arch_48_net_worth_and_capital_bar_visual,
    "49_emergency_fund_target_calculation": arch_49_emergency_fund_target_calculation,
    "50_comprehensive_term2_concepts_synthesis": arch_50_comprehensive_term2_concepts_synthesis,
}
