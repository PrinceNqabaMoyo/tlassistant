"""Grade 10 Accounting — Financial Information, Stakeholders & Conceptual Framework Generator.
100% Deterministic Python generator aligned with South African National Curriculum Standards (Term 1).
Covers 6 distinct subskills:
  1. users_of_financial_information (Internal vs External stakeholders table)
  2. qualitative_characteristics (Relevance, Faithful representation, Comparability, Verifiability, Timeliness, Understandability)
  3. business_forms_and_sectors (Sole trader, Partnership, Company; Service vs Trading vs Manufacturing)
  4. accounting_elements_classification (Assets, Liabilities, Owner's Equity, Income, Expenses table)
  5. capital_vs_operating_expenditure (Classifying capital vs operating expenditure & financial impact)
  6. gaap_in_financial_reporting (Applying GAAP concepts to financial reporting scenarios)
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from .scenario_builder import build_scenario


SUBSKILLS = [
    "users_of_financial_information",
    "qualitative_characteristics",
    "business_forms_and_sectors",
    "accounting_elements_classification",
    "capital_vs_operating_expenditure",
    "gaap_in_financial_reporting",
]


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt(val: float | int) -> str:
    return f"{int(round(val)):,}".replace(",", " ")


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def _build_users_of_financial_information(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    owner = scen["owner"]

    stakeholders = [
        ("The owner / proprietor", "Internal", "To evaluate net profit, return on owner's equity, and decide on drawings or expansion"),
        ("Store manager / supervisor", "Internal", "To plan daily operations, monitor expenses, and control trading stock"),
        ("Commercial bank (e.g. Access Bank / Nedbank)", "External", "To assess liquidity, solvency, and ability to repay a business loan and interest"),
        ("SARS (South African Revenue Service)", "External", "To verify taxable income, VAT obligations, and PAYE/UIF compliance"),
        ("Trade creditors / suppliers", "External", "To determine creditworthiness before granting 30-to-60-day credit terms"),
        ("Employees and trade unions", "External", "To assess job security and negotiate fair wage and salary increases"),
    ]
    chosen = r.sample(stakeholders, 4)

    headers = ["Stakeholder / User", "Internal or External", "Primary Decision / Interest in Financial Statements"]
    rows = []
    correct_map = {}
    for idx, (user_lbl, cat, interest) in enumerate(chosen):
        c1 = f"t0_r{idx}_c1"
        c2 = f"t0_r{idx}_c2"
        correct_map[c1] = cat
        correct_map[c2] = interest
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": user_lbl, "editable": False},
            {"cell_id": c1, "value": "", "expected": cat, "editable": True},
            {"cell_id": c2, "value": interest, "editable": False},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"{owner} prepares annual financial statements for **{business}**. Various internal and external stakeholders "
        f"analyse these statements before making financial decisions.\n\n"
        f"**REQUIRED:**\n"
        f"Complete the stakeholder classification table below by indicating whether each user of financial information "
        f"is **Internal** or **External**."
    )

    return {
        "id": _make_id("g10_fininfo_users"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "users_of_financial_information",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "explanation": "Internal users (owners and managers) manage the business from within; external users (banks, SARS, creditors, trade unions) are outside parties who rely on published financial reports.",
    }


def _build_qualitative_characteristics(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    owner = scen["owner"]

    characteristics = [
        ("Relevance", f"Financial information is capable of making a difference in {owner}'s business decisions by helping predict future cash flows or confirm past evaluations."),
        ("Faithful representation", f"Financial reports of {business} are complete, neutral, and free from material error so that they truthfully reflect the economic transactions."),
        ("Comparability", f"Financial statements of {business} are prepared using consistent accounting policies from year to year so {owner} can compare 2025 performance against 2026."),
        ("Verifiability", f"Every entry in the books of {business} is backed by an authentic source document (invoice, receipt, bank statement) that an independent bookkeeper can check."),
        ("Timeliness", f"Financial reports are completed shortly after the financial year-end while the figures are still current enough to influence {owner}'s pricing and cost decisions."),
        ("Understandability", f"Financial information is classified, grouped, and presented clearly in standard formats so users with reasonable business knowledge can interpret it."),
    ]
    chosen = r.sample(characteristics, 4)

    headers = ["Scenario / Requirement at " + business, "Qualitative Characteristic"]
    rows = []
    correct_map = {}
    for idx, (char_name, desc) in enumerate(chosen):
        cid = f"t0_r{idx}_c1"
        correct_map[cid] = char_name
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": desc, "editable": False},
            {"cell_id": cid, "value": "", "expected": char_name, "editable": True},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"For financial statements to be useful to users, they must possess specific qualitative characteristics: "
        f"*Relevance, Faithful representation, Comparability, Verifiability, Timeliness,* and *Understandability*.\n\n"
        f"**REQUIRED:**\n"
        f"Identify the qualitative characteristic of financial information described in each scenario for **{business}**."
    )

    return {
        "id": _make_id("g10_fininfo_qual"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "qualitative_characteristics",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "explanation": "Qualitative characteristics ensure financial statements are useful, trustworthy, comparable across periods, and verifiable via source documents.",
    }


def _build_business_forms_and_sectors(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    owner = scen["owner"]

    headers = ["Feature / Criterion", "Sole Trader", "Partnership", "Private / Public Company"]
    rows_spec = [
        ("Number of owners", "1 owner", "2 or more partners", "Shareholders (1+ for Pty Ltd; 7+ for Public)"),
        ("Legal personality", "Not a separate legal entity", "Not a separate legal entity", "Separate legal entity (juristic person)"),
        ("Liability of owners for business debts", "Unlimited liability", "Jointly and severally liable", "Limited liability"),
        ("Continuity / Lifespan", "Lack of continuity (dissolves on owner death)", "Dissolves when a partner changes", "Unlimited continuity (perpetual succession)"),
    ]
    rows = []
    correct_map = {}
    for idx, (crit, st, part, comp) in enumerate(rows_spec):
        c1 = f"t0_r{idx}_c1"
        c3 = f"t0_r{idx}_c3"
        correct_map[c1] = st
        correct_map[c3] = comp
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": crit, "editable": False},
            {"cell_id": c1, "value": "", "expected": st, "editable": True},
            {"cell_id": f"t0_r{idx}_c2", "value": part, "editable": False},
            {"cell_id": c3, "value": "", "expected": comp, "editable": True},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"{owner} operates **{business}** as a Sole Trader, and is comparing how a Sole Trader differs from a Partnership "
        f"and a Company in terms of ownership, legal status, liability, and continuity.\n\n"
        f"**REQUIRED:**\n"
        f"Complete the comparison table below for a **Sole Trader** and a **Company**."
    )

    return {
        "id": _make_id("g10_fininfo_forms"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "business_forms_and_sectors",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "explanation": "A sole trader has 1 owner with unlimited personal liability, while a company is a separate legal entity offering limited liability and perpetual continuity.",
    }


def _build_accounting_elements_classification(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]

    pool = [
        ("Delivery vehicle purchased for business deliveries", "Non-Current Asset", "Debit"),
        ("Trading stock on hand in the storeroom", "Current Asset", "Debit"),
        ("Amount owed by credit customers (Debtors Control)", "Current Asset", "Debit"),
        ("Mortgage loan from Nedbank repayable over 10 years", "Non-Current Liability", "Credit"),
        ("Amount owed to suppliers (Creditors Control)", "Current Liability", "Credit"),
        ("Bank overdraft facility used at month-end", "Current Liability", "Credit"),
        ("Capital contribution deposited by the owner", "Owner's Equity", "Credit"),
        ("Cash or goods taken by the owner for personal use (Drawings)", "Owner's Equity (reduces)", "Debit"),
        ("Sales of merchandise to customers", "Income", "Credit"),
        ("Water, electricity, and salaries paid for the month", "Expense", "Debit"),
    ]
    chosen = r.sample(pool, 5)
    headers = ["Account / Item Description", "Accounting Element Classification", "Normal Balance Side (Debit / Credit)"]
    rows = []
    correct_map = {}
    for idx, (desc, elem, side) in enumerate(chosen):
        c1 = f"t0_r{idx}_c1"
        c2 = f"t0_r{idx}_c2"
        correct_map[c1] = elem
        correct_map[c2] = side
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": desc, "editable": False},
            {"cell_id": c1, "value": "", "expected": elem, "editable": True},
            {"cell_id": c2, "value": "", "expected": side, "editable": True},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"The bookkeeper of **{business}** is classifying accounts in the General Ledger according to the Accounting Equation "
        f"($\\text{{Assets}} = \\text{{Owner's Equity}} + \\text{{Liabilities}}$).\n\n"
        f"**REQUIRED:**\n"
        f"For each item below, state its **Accounting Element Classification** (e.g. Non-Current Asset, Current Asset, "
        f"Current Liability, Non-Current Liability, Owner's Equity, Income, Expense) and its **Normal Balance Side** (Debit or Credit)."
    )

    return {
        "id": _make_id("g10_fininfo_elements"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "accounting_elements_classification",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 10,
        "explanation": "DEAD CLIC rule: Debits increase Expenses, Assets, and Drawings (Normal Debit balance); Credits increase Liabilities, Income, and Capital (Normal Credit balance).",
    }


def _build_capital_vs_operating_expenditure(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    veh_cost = r.choice([180000, 220000, 260000])
    fuel_cost = r.choice([4500, 6200, 7800])
    comp_cost = r.choice([18000, 24000, 32000])
    stat_cost = r.choice([1200, 1850, 2400])

    items = [
        (f"Purchased a new delivery van for R{_fmt(veh_cost)}", "Capital expenditure", "Statement of Financial Position (Balance Sheet)", _fmt(veh_cost)),
        (f"Paid R{_fmt(fuel_cost)} for fuel and routine oil service on the delivery van", "Operating expenditure", "Statement of Comprehensive Income (Income Statement)", _fmt(fuel_cost)),
        (f"Bought a point-of-sale computer system for R{_fmt(comp_cost)}", "Capital expenditure", "Statement of Financial Position (Balance Sheet)", _fmt(comp_cost)),
        (f"Purchased printer paper and toner cartridges for R{_fmt(stat_cost)}", "Operating expenditure", "Statement of Comprehensive Income (Income Statement)", _fmt(stat_cost)),
    ]

    headers = ["Transaction", "Expenditure Type (Capital / Operating)", "Financial Statement Affected", "Amount (R)"]
    rows = []
    correct_map = {}
    for idx, (tx, exp_type, stmt, amt) in enumerate(items):
        c1 = f"t0_r{idx}_c1"
        c2 = f"t0_r{idx}_c2"
        correct_map[c1] = exp_type
        correct_map[c2] = stmt
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": tx, "editable": False},
            {"cell_id": c1, "value": "", "expected": exp_type, "editable": True},
            {"cell_id": c2, "value": "", "expected": stmt, "editable": True},
            {"cell_id": f"t0_r{idx}_c3", "value": amt, "editable": False},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"During the financial year, **{business}** incurred the following payments. In Accounting, distinguishing between "
        f"**Capital expenditure** (acquiring long-term assets) and **Operating expenditure** (day-to-day running expenses) "
        f"is critical to avoid distorting Net Profit.\n\n"
        f"**REQUIRED:**\n"
        f"Classify each payment as **Capital expenditure** or **Operating expenditure** and state which Financial Statement it affects."
    )

    return {
        "id": _make_id("g10_fininfo_cap_vs_op"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "capital_vs_operating_expenditure",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "explanation": "Capital expenditure creates a tangible/non-current asset on the Balance Sheet, whereas operating expenditure is an expense deducted on the Income Statement.",
    }


def _build_gaap_in_financial_reporting(r: random.Random) -> Dict[str, Any]:
    scen = build_scenario(seed=r.randint(1, 100000))
    business = scen["business"]
    owner = scen["owner"]
    building_cost = r.choice([850000, 1200000, 1500000])
    market_val = building_cost + r.choice([350000, 450000, 600000])
    drawings_amt = r.choice([3500, 4800, 6500])
    prepaid_ins = r.choice([2400, 3600, 4200])

    headers = ["Case Study Scenario at " + business, "GAAP Principle Applied", "Amount Recorded in Financial Statements (R)"]
    cases = [
        (
            f"1. {business} purchased premises 4 years ago for R{_fmt(building_cost)}. An estate agent values the property today at R{_fmt(market_val)}.",
            "Historical cost",
            _fmt(building_cost),
        ),
        (
            f"2. {owner} used a business EFT of R{_fmt(drawings_amt)} to pay for a private family holiday. It must be excluded from business operating expenses.",
            "Business entity rule",
            _fmt(drawings_amt),
        ),
        (
            f"3. Insurance of R{_fmt(prepaid_ins)} was paid in February for March of the next financial year and must be deducted from this year's insurance expense.",
            "Matching principle",
            _fmt(prepaid_ins),
        ),
    ]

    rows = []
    correct_map = {}
    for idx, (sc_txt, princ, amt) in enumerate(cases):
        c1 = f"t0_r{idx}_c1"
        c2 = f"t0_r{idx}_c2"
        correct_map[c1] = princ
        correct_map[c2] = amt
        rows.append([
            {"cell_id": f"t0_r{idx}_c0", "value": sc_txt, "editable": False},
            {"cell_id": c1, "value": "", "expected": princ, "editable": True},
            {"cell_id": c2, "value": "", "expected": amt, "editable": True},
        ])

    prompt = (
        f"{scen['intro']}\n\n"
        f"**INFORMATION:**\n"
        f"{owner} is finalising the financial information of **{business}** and must apply Generally Accepted Accounting Practice (GAAP) "
        f"to ensure reliable financial reporting.\n\n"
        f"**REQUIRED:**\n"
        f"Complete the schedule below by stating the **GAAP Principle Applied** and the **Amount (R)** to be recognised."
    )

    return {
        "id": _make_id("g10_fininfo_gaap_rep"),
        "question_type": "table_completion",
        "modality": "ledger",
        "subskill": "gaap_in_financial_reporting",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "explanation": "Historical cost records assets at original purchase price; Business entity keeps personal transactions in Drawings; Matching aligns income and expenses to the financial year.",
    }


BUILDERS = {
    "users_of_financial_information": _build_users_of_financial_information,
    "qualitative_characteristics": _build_qualitative_characteristics,
    "business_forms_and_sectors": _build_business_forms_and_sectors,
    "accounting_elements_classification": _build_accounting_elements_classification,
    "capital_vs_operating_expenditure": _build_capital_vs_operating_expenditure,
    "gaap_in_financial_reporting": _build_gaap_in_financial_reporting,
}


def generate_questions(
    *,
    count: int = 1,
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    n = max(1, int(count or 1))
    req_sub = str(subskill or "").strip().lower()
    out: List[Dict[str, Any]] = []
    for i in range(n):
        if req_sub in BUILDERS:
            chosen_key = req_sub
        else:
            chosen_key = r.choice(SUBSKILLS)
        q = BUILDERS[chosen_key](r)
        q["difficulty"] = difficulty
        q["subskill"] = chosen_key
        out.append(q)
    return out
