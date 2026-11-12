"""Grade 9 EMS - Credit Transactions (Debtors 1): Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Debtors 1).md
- curriculum_docs/EMS_Gr9/Term 2/5-Credit transactions- Debtors 1.md

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "Credit transactions (Debtors 1)"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term2_debtors_journal"
CURRICULUM_REFERENCE = "Term 2 > Financial Literacy: Credit Transactions (Debtors 1)"

TRADER_SUFFIXES = [
    "Traders",
    "Stores",
    "Suppliers",
    "Hardware",
    "Wholesalers",
    "Boutique",
    "Outfitters",
    "Stationers",
    "Furnishers",
    "Sports Goods",
]

MONTH_DATA = [
    ("March", "2026", "Mar"),
    ("April", "2026", "Apr"),
    ("May", "2026", "May"),
    ("June", "2026", "Jun"),
    ("August", "2026", "Aug"),
    ("October", "2026", "Oct"),
]

DEBTOR_POOL = [
    ("S. Khumalo", "D1"),
    ("N. Dlamini", "D2"),
    ("J. Van der Merwe", "D3"),
    ("T. Naidoo", "D4"),
    ("L. Mthembu", "D5"),
    ("P. Mokwena", "D6"),
    ("G. Smith", "D7"),
    ("K. Botha", "D8"),
]

MERCHANDISE_LINES = [
    "school tracksuits",
    "hardware toolkits",
    "sports shoes",
    "solar lanterns",
    "cotton shirts",
    "kitchenware sets",
    "stationery hampers",
    "cycling helmets",
]


def fmt_r(amount: int | float) -> str:
    """Format South African Rand display with space thousands separator."""
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def fmt_cell(val: int | float) -> str:
    """Format numeric answer cell without currency symbol or spaces."""
    if isinstance(val, float) and not val.is_integer():
        return f"{val:.2f}".replace(".", ",")
    return str(int(round(val)))


def biz_name(rng: random.Random, sc: Dict[str, Any]) -> str:
    return f"{sc['entrepreneur']} {rng.choice(TRADER_SUFFIXES)}"


def pick_debtors(rng: random.Random, n: int = 3) -> List[Tuple[str, str]]:
    chosen = rng.sample(DEBTOR_POOL, n)
    return [(name, f"D{i + 1}") for i, (name, _) in enumerate(chosen)]


def _hint_sections(hints: Dict[str, str]) -> Dict[str, str]:
    return {
        "1_nudge": hints["tier_1"],
        "2_concept": hints["tier_2"],
        "3_breakdown": hints["tier_3"],
    }


def build_mcq(
    rng: random.Random,
    *,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    correct_text: str,
    distractors: List[str],
    explanation: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 2,
    term: int = 2,
    caps_weight: int = 40,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct_text] + list(distractors)
    rng.shuffle(options)
    c_idx = options.index(correct_text)
    letter = chr(65 + c_idx)
    ans_full = f"{letter}. {correct_text}"
    worked = f"**{ans_full}** [{marks} marks]\n\n{explanation}"
    q: Dict[str, Any] = {
        "id": f"{qid}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_dj_{subskill}",
        "concept_id": subskill,
        "concept_group": "debtors_1",
        "question_type": "mcq",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans_full,
        "expected_answer": ans_full,
        "sample_answer": ans_full,
        "ideal_answer": ans_full,
        "worked_solution": worked,
        "explanation": worked,
        "canonical_solution": worked,
        "marks": marks,
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "hint_sections": _hint_sections(hints),
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Selects {letter}: {correct_text}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "debtors_journal", "credit_sales"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def build_short(
    rng: random.Random,
    *,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_answer: str,
    worked_solution: str,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
    marks: int = 3,
    qtype: str = "math_short",
    term: int = 2,
    caps_weight: int = 40,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_dj_{subskill}",
        "concept_id": subskill,
        "concept_group": "debtors_1",
        "question_type": qtype,
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "correct_answer": expected_answer,
        "expected_answer": expected_answer,
        "sample_answer": expected_answer,
        "ideal_answer": expected_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "hint_sections": _hint_sections(hints),
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "debtors_journal", "credit_sales"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def build_table(
    rng: random.Random,
    *,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    worked_solution: str,
    sample_answer: str,
    marks: int,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
    journal_type: str = "dj",
    transactions: Optional[List[str]] = None,
    term: int = 2,
    caps_weight: int = 40,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_dj_{subskill}",
        "concept_id": subskill,
        "concept_group": "debtors_1",
        "question_type": "table_completion",
        "modality": "ledger",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "journal": {"journal_type": journal_type, "headers": headers, "rows": rows},
        "editable_cols": list(range(len(headers))),
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "correct_answer": sample_answer,
        "expected_answer": sample_answer,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "hint_sections": _hint_sections(hints),
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "debtors_journal", "tabular"],
    }
    if transactions:
        q["transactions"] = transactions
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def source_doc_svg(
    header_title: str,
    doc_no: str,
    date_str: str,
    lines: List[Tuple[str, str]],
    accent: str = "#1e40af",
) -> str:
    """Render clean source-document card SVG (Duplicate Invoice / Credit Note / Receipt)."""
    y = 84
    parts: List[str] = []
    for lbl, val in lines:
        parts.append(
            f'<text x="22" y="{y}" font-size="11" font-weight="bold" fill="#475569">{lbl}:</text>'
            f'<text x="165" y="{y}" font-size="11.5" font-weight="bold" fill="#0f172a">{val}</text>'
            f'<line x1="22" y1="{y + 7}" x2="498" y2="{y + 7}" stroke="#e2e8f0" stroke-width="1"/>'
        )
        y += 28
    h = max(190, y + 16)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 {h}" width="520" height="{h}">'
        f'<rect x="6" y="6" width="508" height="{h - 12}" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<rect x="6" y="6" width="508" height="44" rx="8" fill="{accent}"/>'
        f'<text x="22" y="33" font-size="13" font-weight="bold" fill="#ffffff">{header_title}</text>'
        f'<text x="498" y="24" font-size="11" font-weight="bold" text-anchor="end" fill="#f8fafc">Doc No: {doc_no}</text>'
        f'<text x="498" y="40" font-size="10" text-anchor="end" fill="#e2e8f0">Date: {date_str}</text>'
        + "".join(parts)
        + "</svg>"
    )


def make_grid_rows(
    data_rows: List[List[str]],
    given_coords: set[Tuple[int, int]] | None = None,
) -> Tuple[List[List[Dict[str, Any]]], Dict[str, str]]:
    """Build standardised 2D interactive ledger/journal grid cells and correct_map."""
    given_coords = given_coords or set()
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    for i, rvals in enumerate(data_rows):
        row_cells: List[Dict[str, Any]] = []
        for j, val in enumerate(rvals):
            coord = f"t0_r{i}_c{j}"
            is_given = (i, j) in given_coords
            is_empty = (val == "")
            if is_given:
                row_cells.append({
                    "coordinate": coord, "cell_id": coord, "value": val,
                    "type": "given", "editable": False,
                })
            else:
                correct_map[coord] = val
                row_cells.append({
                    "coordinate": coord, "cell_id": coord, "value": "",
                    "type": "must_be_empty" if is_empty else "required",
                    "editable": True,
                })
        rows.append(row_cells)
    return rows, correct_map


def arch_01_cash_sales_vs_credit_sales_distinction(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    goods = rng.choice(MERCHANDISE_LINES)
    amt = rng.randint(12, 48) * 100
    days = rng.choice([30, 60])

    prompt = (
        f"At **{biz}** in {sc['area']}, customer **{debtor}** takes possession of **{goods}** worth **{fmt_r(amt)}** today "
        f"and signs an agreement to pay the full amount within **{days} days**.\n\n"
        "Which statement accurately explains how this transaction differs from a cash sale?"
    )
    correct = (
        f"Ownership and goods pass to {debtor} immediately, while payment is postponed for {days} days; "
        "it is a credit sale recorded in the Debtors Journal (DJ) rather than the CRJ."
    )
    distractors = [
        f"{debtor} pays cash into the till immediately before taking the {goods}, so it enters the CRJ as Cash Sales.",
        "Credit sales cannot transfer goods until the entire balance has been cleared at month-end.",
        f"Because no cash enters Bank today, {biz} ignores the transaction until {days} days pass.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_01",
        subskill="01_cash_sales_vs_credit_sales_distinction",
        title="Cash Sales vs Credit Sales",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"In a **credit sale**, the buyer receives the {goods} right away, while payment of **{fmt_r(amt)}** "
            f"is postponed for {days} days. Credit sales are recorded in the **Debtors Journal (DJ)**, whereas cash sales enter the **CRJ**."
        ),
        hints={
            "tier_1": "Ask whether money changes hands immediately or is postponed to a later date.",
            "tier_2": "Delayed payment means it is a credit sale -> Debtors Journal (DJ), not Cash Receipts Journal (CRJ).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_credit_sales_with_cash_sales"],
    )


def arch_02_debtor_definition_current_asset_role(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt = rng.randint(15, 65) * 100
    days = rng.choice([30, 45, 60])

    prompt = (
        f"**{debtor}** owes **{biz}** **{fmt_r(amt)}** (due in {days} days) for trading stock bought on account.\n\n"
        f"In accounting, how is **{debtor}** classified in the books of **{biz}**?"
    )
    correct = f"A Debtor — classified as a Current Asset because the {fmt_r(amt)} owed is convertible into cash within 12 months."
    distractors = [
        f"A Creditor — classified as a Current Liability because {biz} must pay {debtor} in {days} days.",
        "An Operating Expense — classified under Owner's Equity because the stock left the storeroom.",
        "A Fixed Asset — classified under Land and Buildings until settlement is received.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_02",
        subskill="02_debtor_definition_current_asset_role",
        title="Debtor Definition & Asset Classification",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **debtor** is a customer or business that owes money to our enterprise for goods bought on credit. "
            f"Debtors are **Current Assets** because they represent cash expected to flow into the business in the short term (within 12 months)."
        ),
        hints={
            "tier_1": "Does the business expect to RECEIVE cash from this customer, or PAY cash to them?",
            "tier_2": "Receiving money from credit customers makes Debtors an Asset (specifically Current Assets).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_debtor_with_creditor"],
    )


def arch_03_national_credit_act_purpose_reckless_lending(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    income = rng.randint(60, 120) * 100
    requested = income * 3

    prompt = (
        f"A shopper earning **{fmt_r(income)}/month** applies at **{biz}** in {sc['area']} for an account with a credit limit of **{fmt_r(requested)}**.\n\n"
        "What is the primary purpose of South Africa's **National Credit Act (NCA)** in regulating this credit application?"
    )
    correct = "To discourage reckless lending, protect consumers from over-indebtedness, and ensure fair, transparent credit agreements."
    distractors = [
        "To abolish all store credit sales so businesses may accept cash or EFT payments only.",
        "To guarantee that sellers can charge unlimited interest without checking customer affordability.",
        "To replace the Debtors Journal with the Cash Payments Journal for retail stores.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_03",
        subskill="03_national_credit_act_purpose_reckless_lending",
        title="Purpose of the National Credit Act (NCA)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The **National Credit Act (NCA)** protects both consumers and credit providers by requiring affordability assessments, "
            "prohibiting **reckless lending**, and enforcing clear credit terms."
        ),
        hints={
            "tier_1": "Think about what stops stores from giving huge credit limits to people who cannot afford repayments.",
            "tier_2": "The NCA prevents over-spending/reckless lending and protects both borrower and lender.",
            "tier_3": correct,
        },
        misconception_tags=["misunderstanding_national_credit_act_role"],
    )


def arch_04_credit_limit_vs_credit_term_definitions(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    limit_amt = rng.choice([2500, 3500, 5000, 7500])
    term_days = rng.choice([30, 60, 90])

    ask_limit = rng.choice([True, False])
    if ask_limit:
        prompt = (
            f"**{biz}** sets a customer's credit agreement as **{fmt_r(limit_amt)}** and **{term_days} days**.\n\n"
            f"What does the **{fmt_r(limit_amt)}** figure represent?"
        )
        correct = f"Credit limit — the maximum Rand value a debtor may buy or owe on account at any time."
        distractors = [
            f"Credit term — the maximum number of days allowed before full payment is due.",
            "Trade discount — the immediate cash reduction granted on every credit invoice.",
            "Debtors allowance — the refund paid out when goods are damaged in delivery.",
        ]
    else:
        prompt = (
            f"**{biz}** approves a customer account with a maximum balance of **{fmt_r(limit_amt)}** payable within **{term_days} days**.\n\n"
            f"What does the **{term_days} days** condition specify?"
        )
        correct = f"Credit term — how much time the debtor has to pay/settle the outstanding account."
        distractors = [
            f"Credit limit — the maximum Rand balance the debtor is allowed to owe.",
            "Mark-up percentage — the profit percentage added to Cost Price.",
            "Credit bureau score — the customer's total monthly salary.",
        ]
    return build_mcq(
        rng,
        qid="g9_dj_04",
        subskill="04_credit_limit_vs_credit_term_definitions",
        title="Credit Limit vs Credit Term",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **credit limit** ({fmt_r(limit_amt)}) restricts the Rand value a client may owe, while a **credit term** "
            f"({term_days} days) specifies how long the client has to repay the debt."
        ),
        hints={
            "tier_1": "Notice whether the question asks about a Rand ceiling or a time period.",
            "tier_2": "Limit = maximum Rand value; Term = repayment timeframe (days).",
            "tier_3": correct,
        },
        misconception_tags=["swapping_credit_limit_and_credit_term"],
    )


def arch_05_creditworthy_vs_credit_reference_concepts(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    supplier = sc["supplier"]

    prompt = (
        f"Before granting credit to a new client in {sc['area']}, **{biz}** contacts **{supplier}** "
        "(where the client already holds an account) to verify whether the client pays reliably and on time.\n\n"
        "What is this verification process called, and what quality does it establish?"
    )
    correct = "Obtaining a credit reference to establish the applicant's creditworthiness (good repayment record and affordability)."
    distractors = [
        "Issuing a credit note to increase the applicant's Debt Allowance Journal balance.",
        "Posting to General Ledger Sundry Accounts before any goods are sold.",
        "Calculating Cost of Sales using the duplicate invoice number.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_05",
        subskill="05_creditworthy_vs_credit_reference_concepts",
        title="Creditworthiness & Credit References",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "A **credit reference** checks with existing credit providers to confirm **creditworthiness** — "
            "whether an applicant has a reliable payment history and sufficient affordability."
        ),
        hints={
            "tier_1": "Asking another store about an applicant's payment habits acts as a reference check.",
            "tier_2": "Credit reference checks trustworthiness; creditworthiness means a good record and affordability.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_credit_reference_with_credit_note"],
    )


def arch_06_credit_bureau_and_salary_advice_evaluation(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)

    prompt = (
        f"**{debtor}** applies for an instalment account at **{biz}** and submits a recent **salary advice (payslip)** "
        "plus consent for an ID-linked **Credit Bureau** enquiry.\n\n"
        "Why does **{biz}** require BOTH the salary advice and a Credit Bureau check?"
    )
    correct = "The salary advice proves employment and monthly affordability, while the Credit Bureau reveals all existing debt and repayment history linked to the applicant's ID."
    distractors = [
        "The salary advice records Sales in the DJ, while the Credit Bureau calculates Cost of Sales mark-up.",
        "Both documents are used solely to issue duplicate credit notes when stock is returned.",
        "The Credit Bureau pays the customer's monthly instalments directly out of Bank.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_06",
        subskill="06_credit_bureau_and_salary_advice_evaluation",
        title="Salary Advice & Credit Bureau Checks",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Businesses inspect **salary advice** for proof of employment and affordability, and query a **Credit Bureau** "
            "(using the applicant's ID number) to review existing loan/store debt and debit-order reliability."
        ),
        hints={
            "tier_1": "Think of what a payslip shows versus what an ID-based Credit Bureau report shows.",
            "tier_2": "Payslip -> income & employment; Credit Bureau -> existing debts and credit track record.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_affordability_or_bureau_checks"],
    )


def arch_07_credit_application_affordability_disposable_income_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    applicant, _ = rng.choice(DEBTOR_POOL)
    net_salary = rng.randint(9, 18) * 1000
    rent = rng.randint(25, 42) * 100
    groceries = rng.randint(18, 28) * 100
    existing_debt = rng.randint(10, 22) * 100
    instalment = rng.randint(6, 12) * 100
    disposable = net_salary - (rent + groceries + existing_debt)
    leftover = disposable - instalment

    prompt = (
        f"**{applicant}** applies for a credit account at **{biz}** with a proposed monthly instalment of **{fmt_r(instalment)}**.\n\n"
        f"Monthly budget declared on the application form:\n"
        f"- Net monthly salary: **{fmt_r(net_salary)}**\n"
        f"- Rent / bond: **{fmt_r(rent)}**\n"
        f"- Food & transport: **{fmt_r(groceries)}**\n"
        f"- Existing store/loan repayments: **{fmt_r(existing_debt)}**\n\n"
        f"Calculate **{applicant}**'s remaining disposable income **after** paying the proposed **{fmt_r(instalment)}** instalment [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Step 1 — Total Existing Monthly Commitments:**\n"
        f"`{fmt_r(rent)} + {fmt_r(groceries)} + {fmt_r(existing_debt)} = {fmt_r(rent + groceries + existing_debt)}` [1]\n\n"
        "**Step 2 — Disposable Income Before New Credit:**\n"
        f"`{fmt_r(net_salary)} - {fmt_r(rent + groceries + existing_debt)} = {fmt_r(disposable)}` [1]\n\n"
        "**Step 3 — Remaining Balance After New Instalment:**\n"
        f"`{fmt_r(disposable)} - {fmt_r(instalment)} = {fmt_r(leftover)}` -> Answer: `{leftover}` [1]"
    )
    return build_short(
        rng,
        qid="g9_dj_07",
        subskill="07_credit_application_affordability_disposable_income_calc",
        title="Credit Application Affordability Calculation",
        prompt=prompt,
        expected_answer=str(leftover),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "First add up all current monthly expenses and existing debt repayments.",
            "tier_2": f"Subtract total expenses ({fmt_r(rent + groceries + existing_debt)}) and the new instalment ({fmt_r(instalment)}) from Net Salary ({fmt_r(net_salary)}).",
            "tier_3": f"Remaining disposable income = {leftover}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sums existing expenses = {fmt_r(rent + groceries + existing_debt)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Disposable income before credit = {fmt_r(disposable)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Remaining after new instalment = {leftover}", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_existing_debt_from_affordability"],
    )


def arch_08_reasons_businesses_grant_credit_advantages(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    goods = rng.choice(MERCHANDISE_LINES)

    prompt = (
        f"**{biz}** in {sc['area']} previously traded on a strict cash-only basis and is considering offering 30-day credit "
        f"on **{goods}** to vetted customers.\n\n"
        "What is a valid commercial **advantage** of granting credit to creditworthy customers?"
    )
    correct = "It attracts more customers, increases overall sales volume (turnover), and builds customer loyalty."
    distractors = [
        "It guarantees immediate cash arrives in the Bank account on the exact day of sale.",
        "It completely removes the need to record Trading Stock or Cost of Sales.",
        "It reduces Total Assets because Debtors Control carries a negative balance.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_08",
        subskill="08_reasons_businesses_grant_credit_advantages",
        title="Advantages of Offering Credit",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Businesses offer credit mainly to **boost sales turnover**, attract shoppers who need time to pay until payday, "
            "and foster repeat custom—provided clients are properly vetted."
        ),
        hints={
            "tier_1": "Why do retailers allow shoppers to buy now and pay at month-end?",
            "tier_2": "Higher sales turnover and wider clientele are key benefits of credit.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_credit_eliminates_bookkeeping"],
    )


def arch_09_risks_and_disadvantages_of_credit_sales(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    amt = rng.randint(15, 45) * 1000

    prompt = (
        f"After expanding credit sales to **{fmt_r(amt)}/month**, **{biz}** struggles to pay its own suppliers on time "
        "and writes off several uncollectible customer accounts.\n\n"
        "Which pair of risks represents major **disadvantages** of selling on credit?"
    )
    correct = "Bad debts (customers failing to pay) and delayed cash flow plus higher credit administration costs."
    distractors = [
        "Lower total sales volume and inability to issue invoices to customers.",
        "Immediate doubling of Bank cash balances and zero need for Debtors Control.",
        "Automatic elimination of Trading Stock and supplier accounts.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_09",
        subskill="09_risks_and_disadvantages_of_credit_sales",
        title="Risks & Disadvantages of Credit Sales",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Selling on credit exposes a business to **bad debts** (non-payment), **cash-flow delays** (money tied up in debtors), "
            "and increased **administrative costs** (statements, credit checks, follow-ups)."
        ),
        hints={
            "tier_1": "Consider what goes wrong when money stays with customers instead of entering the bank.",
            "tier_2": "Non-payment (bad debts) and slow cash inflow are the primary credit risks.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_bad_debts_and_cashflow_risk"],
    )


def arch_10_debtors_accounting_cycle_sequence(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)

    prompt = (
        f"**{debtor}** orders merchandise on account from **{biz}**.\n\n"
        "Which option shows the **correct chronological sequence** in the credit-sales accounting cycle?"
    )
    correct = "Order & credit approval -> Issue invoice (keep duplicate) -> Record in Debtors Journal (DJ) -> Post to Debtors Ledger & General Ledger -> Receipt in CRJ when paid."
    distractors = [
        "Post directly to Trial Balance -> Issue Receipt -> Record in CPJ -> Issue duplicate invoice.",
        "Record in Debtors Allowance Journal -> Collect cash in CRJ -> Deliver order -> Issue invoice.",
        "Record in Creditors Journal -> Issue Debit Note -> Post to Debtors Ledger -> Check stock.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_10",
        subskill="10_debtors_accounting_cycle_sequence",
        title="Accounting Cycle for Credit Sales",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The credit-sales accounting cycle flows from **source document (duplicate invoice)** -> **subsidiary journal (DJ)** "
            "-> **Debtors Ledger & General Ledger** -> **CRJ receipt** on settlement."
        ),
        hints={
            "tier_1": "Accounting always begins with a source document, then enters a subsidiary journal before reaching ledgers.",
            "tier_2": "Source doc (Duplicate Invoice) -> DJ -> Debtors Ledger / General Ledger -> CRJ upon payment.",
            "tier_3": correct,
        },
        misconception_tags=["reversing_journal_and_ledger_order"],
    )


def arch_11_duplicate_invoice_source_document_card_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    inv_no = rng.randint(110, 490)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    day = rng.randint(2, 26)
    qty = rng.randint(4, 15)
    unit_p = rng.choice([150, 200, 250, 300, 450])
    total = qty * unit_p
    goods = rng.choice(MERCHANDISE_LINES)

    svg = source_doc_svg(
        f"DUPLICATE TAX INVOICE — {biz}",
        str(inv_no),
        f"{day:02d} {m_name} {yr}",
        [
            ("Debtor (Sold To)", debtor),
            ("Terms", "30 Days on Account"),
            ("Items", f"{qty} x {goods} @ {fmt_r(unit_p)}"),
            ("Invoice Total", fmt_r(total)),
        ],
        accent="#1e40af",
    )
    prompt = (
        f"Inspect the **Duplicate Credit Invoice** issued by **{biz}** shown in the source document card below.\n\n"
        f"What **Selling Price** must be recorded in the **Sales** column of the **Debtors Journal (DJ)** for Invoice **{inv_no}** ({debtor})?\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Source Document Identification (Duplicate Invoice):**\n"
        f"- Journal: **Debtors Journal (DJ)** (credit sale to debtor **{debtor}**)\n"
        f"- Document No.: **{inv_no}** | Date: **{day:02d} {m_name} {yr}**\n"
        f"- Sales Column Value: `{qty} × {fmt_r(unit_p)} = {fmt_r(total)}` -> Answer: `{total}`"
    )
    return build_short(
        rng,
        qid="g9_dj_11",
        subskill="11_duplicate_invoice_source_document_card_svg",
        title="Read Duplicate Credit Invoice Source Document",
        prompt=prompt,
        expected_answer=str(total),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Locate the Invoice Total line on the duplicate credit invoice card.",
            "tier_2": f"Multiply {qty} units by {fmt_r(unit_p)} per unit.",
            "tier_3": f"DJ Sales amount = {total}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Reads total {fmt_r(total)} from Invoice {inv_no}", "marks": 2, "editable": True},
        ],
        misconception_tags=["entering_unit_price_instead_of_invoice_total"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_12_duplicate_vs_original_invoice_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    inv_no = rng.randint(201, 399)

    prompt = (
        f"**{biz}** sells trading stock on credit to **{debtor}** and prepares Invoice **{inv_no}** in duplicate.\n\n"
        "Which copy serves as the **source document** for **{biz}**'s Debtors Journal (DJ), and why?"
    )
    correct = f"The Duplicate Invoice ({inv_no}), because the customer ({debtor}) legally receives the Original Invoice as proof of purchase."
    distractors = [
        f"The Original Invoice ({inv_no}), because the seller must post the original document into the CRJ.",
        "A Cheque Counterfoil, because all credit sales require an EFT payout immediately.",
        "A Debit Note received from the buyer prior to delivery.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_12",
        subskill="12_duplicate_vs_original_invoice_rule",
        title="Original vs Duplicate Credit Invoice Rule",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "When selling on credit, the business hands the **original invoice** to the customer (**debtor**) and keeps the "
            "**duplicate invoice** inside its invoice book as the source document for the **Debtors Journal**."
        ),
        hints={
            "tier_1": "Which copy leaves the shop with the customer, and which copy remains with the bookkeeper?",
            "tier_2": "Customer keeps the Original; the business records from the Duplicate Invoice.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_original_and_duplicate_invoices"],
    )


def arch_13_calculate_missing_invoice_line_and_total_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    inv_no = rng.randint(301, 450)
    q1, p1 = rng.randint(3, 8), rng.choice([120, 150, 200])
    q2, p2 = rng.randint(2, 6), rng.choice([250, 300, 350])
    sub1 = q1 * p1
    sub2 = q2 * p2
    grand = sub1 + sub2

    headers = ["Item Description", "Qty", "Unit Price (R)", "Line Total (R)"]
    data_rows = [
        [rng.choice(MERCHANDISE_LINES[:4]).title(), str(q1), str(p1), str(sub1)],
        [rng.choice(MERCHANDISE_LINES[4:]).title(), str(q2), str(p2), str(sub2)],
        ["TOTAL INVOICE (Sales)", "", "", str(grand)],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)})
    cell_hints = {
        "t0_r0_c3": f"Line 1 = {q1} × R{p1} = {sub1}.",
        "t0_r1_c3": f"Line 2 = {q2} × R{p2} = {sub2}.",
        "t0_r2_c3": f"Total Invoice = {sub1} + {sub2} = {grand}.",
    }
    prompt = (
        f"Complete the missing line totals and final **Invoice Total** on Duplicate Credit Invoice **{inv_no}** issued by **{biz}** to **{debtor}**.\n\n"
        "*(Enter whole digits without spaces or R.)*"
    )
    worked = (
        f"**Completed Credit Invoice {inv_no} ({debtor})** [4 marks]\n\n"
        "| Item | Qty | Unit Price | Line Total |\n| --- | --- | --- | --- |\n"
        f"| Item 1 | {q1} | {fmt_r(p1)} | **{fmt_r(sub1)}** |\n"
        f"| Item 2 | {q2} | {fmt_r(p2)} | **{fmt_r(sub2)}** |\n"
        f"| **TOTAL INVOICE** | | | **{fmt_r(grand)}** |"
    )
    return build_table(
        rng,
        qid="g9_dj_13",
        subskill="13_calculate_missing_invoice_line_and_total_table",
        title="Complete Duplicate Invoice Totals",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Line 1 = {sub1}; Line 2 = {sub2}; Total Invoice = {grand}",
        marks=4,
        hints={
            "tier_1": "Multiply Qty × Unit Price for each merchandise line, then sum for the invoice total.",
            "tier_2": f"Line 1 = {q1}×{p1}; Line 2 = {q2}×{p2}.",
            "tier_3": f"Line 1 = {sub1}, Line 2 = {sub2}, Grand Total = {grand}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Line 1 total = {sub1}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Line 2 total = {sub2}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Invoice total = {grand}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_unit_price_and_qty_instead_of_multiplying"],
        journal_type="invoice",
    )


def arch_14_debtors_journal_purpose_and_exclusions(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt1 = rng.randint(15, 35) * 100
    amt2 = rng.randint(20, 50) * 100
    amt3 = rng.randint(40, 80) * 100

    prompt = (
        f"During one week, **{biz}** records four transactions:\n"
        f"1. Sold old delivery equipment for **{fmt_r(amt3)}** cash.\n"
        f"2. Sold trading stock on credit to **{debtor}** for **{fmt_r(amt1)}**.\n"
        f"3. Received **{fmt_r(amt2)}** from a debtor in settlement of an existing account.\n"
        f"4. Paid electricity by EFT to the municipality.\n\n"
        "Which transaction(s) belong in the **Debtors Journal (DJ)**?"
    )
    correct = f"Only Transaction 2 ({fmt_r(amt1)} credit sale of trading stock to {debtor})."
    distractors = [
        f"Transactions 2 and 3, because both involve {debtor} and debtor accounts.",
        "Transactions 1 and 2, because both involve selling items to external parties.",
        "All four transactions, because every business entry enters the Debtors Journal.",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_14",
        subskill="14_debtors_journal_purpose_and_exclusions",
        title="Purpose & Scope of Debtors Journal (DJ)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The **Debtors Journal (DJ)** records **ONLY credit sales of trading stock**. "
            "Cash receipts (Transaction 1 & 3) enter the **CRJ**, and EFT payments (Transaction 4) enter the **CPJ**."
        ),
        hints={
            "tier_1": "The Debtors Journal tracks ONE very specific type of transaction.",
            "tier_2": "Only credit sales of merchandise enter the DJ; cash sales & debtor payments go to CRJ.",
            "tier_3": correct,
        },
        misconception_tags=["entering_debtor_payments_in_debtors_journal"],
    )


def arch_15_journal_classification_dj_daj_crj_cpj_matrix(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    bank_cases = [
        ("Duplicate invoice issued for merchandise sold on credit", "DJ"),
        ("Receipt issued in settlement of a debtor's account", "CRJ"),
        ("Duplicate credit note issued for damaged goods returned by debtor", "DAJ"),
        ("Cash sales recorded on the Cash Register Roll (CRR)", "CRJ"),
        ("Paid supplier by EFT / cashed cheque for wages", "CPJ"),
        ("Customer bought stock on account to pay in 30 days", "DJ"),
        ("Debtor returned wrong-size stock for an account reduction", "DAJ"),
        ("Bought a computer and paid immediately by EFT", "CPJ"),
    ]
    picked = rng.sample(bank_cases, 5)
    headers = ["Transaction Keyword / Clue", "Target Journal (DJ / DAJ / CRJ / CPJ)"]
    data_rows = [[clue, jrn] for clue, jrn in picked]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(i, 0) for i in range(5)})
    cell_hints = {
        f"t0_r{i}_c1": (
            "Credit sale -> DJ; Debtor return/credit note -> DAJ; Any receipt/cash sale -> CRJ; Any payment -> CPJ."
        )
        for i in range(5)
    }
    prompt = (
        "Classify each transaction clue into the correct subsidiary journal (**`DJ`**, **`DAJ`**, **`CRJ`**, or **`CPJ`**) in the table below."
    )
    md_rows = "\n".join(f"| {clue} | **{jrn}** |" for clue, jrn in picked)
    worked = (
        "**Subsidiary Journal Classification Memorandum** [5 marks]\n\n"
        "| Transaction Clue | Target Journal |\n| --- | --- |\n" + md_rows
    )
    return build_table(
        rng,
        qid="g9_dj_15",
        subskill="15_journal_classification_dj_daj_crj_cpj_matrix",
        title="Classify Keywords: DJ vs DAJ vs CRJ vs CPJ",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(j for _, j in picked),
        marks=5,
        hints={
            "tier_1": "Use keywords: credit sale = DJ, return/credit note = DAJ, receipt/cash sale = CRJ, payment = CPJ.",
            "tier_2": "Distinguish money flowing IN (CRJ) vs OUT (CPJ) vs goods sold on credit (DJ) vs returned (DAJ).",
            "tier_3": "; ".join(f"{c} -> {j}" for c, j in picked),
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Row {i+1} = {j}", "marks": 1, "editable": True}
            for i, (_, j) in enumerate(picked)
        ],
        misconception_tags=["confusing_crj_and_dj_on_debtors"],
        journal_type="classification_matrix",
    )


def arch_16_cost_price_from_selling_price_markup_formula(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    markup = rng.choice([25, 40, 50, 60, 80, 100])
    cp = rng.randint(10, 45) * 100
    sp = cp * (100 + markup) // 100
    inv = rng.randint(105, 290)

    prompt = (
        f"**{biz}** applies a consistent mark-up of **{markup}% on cost price**.\n\n"
        f"On Invoice **{inv}**, goods were sold on credit to **{debtor}** for **{fmt_r(sp)}** (Selling Price).\n\n"
        f"Calculate the **Cost of Sales** amount to enter in the **Debtors Journal** [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Step 1 — Cost Price Formula:**\n"
        f"$$\\text{{Cost Price}} = \\text{{Selling Price}} \\times \\frac{{100}}{{100 + \\text{{mark-up}}}} = \\text{{Selling Price}} \\times \\frac{{100}}{{{100 + markup}}}$$ [1]\n\n"
        "**Step 2 — Substitute Selling Price:**\n"
        f"$$\\text{{Cost of Sales}} = {sp} \\times \\frac{{100}}{{{100 + markup}}} = {fmt_r(cp)}$$ [2]\n\n"
        f"Answer: `{cp}`"
    )
    return build_short(
        rng,
        qid="g9_dj_16",
        subskill="16_cost_price_from_selling_price_markup_formula",
        title="Calculate Cost of Sales from Selling Price & Mark-up",
        prompt=prompt,
        expected_answer=str(cp),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Never subtract the mark-up % directly from Selling Price; Selling Price already equals 100% + mark-up%.",
            "tier_2": f"Use CP = SP × 100 / (100 + {markup}) = {sp} × 100 / {100 + markup}.",
            "tier_3": f"Cost of Sales = {cp}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct multiplier 100/{100 + markup}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Cost of Sales = {fmt_r(cp)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_markup_percentage_directly_from_selling_price"],
    )


def arch_17_selling_price_from_cost_price_markup_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    markup = rng.choice([25, 40, 50, 60, 80])
    cp = rng.randint(12, 50) * 100
    sp = cp * (100 + markup) // 100
    profit = sp - cp

    prompt = (
        f"**{biz}** supplies goods to credit customer **{debtor}** at a mark-up of **{markup}% on cost**.\n\n"
        f"If the **cost price** of the order is **{fmt_r(cp)}**, calculate the **Selling Price** to be invoiced in the **Sales** column of the DJ [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Step 1 — Selling Price Formula:**\n"
        f"$$\\text{{Selling Price}} = \\text{{Cost Price}} \\times \\frac{{100 + {markup}}}{{100}}$$ [1]\n\n"
        "**Step 2 — Calculation:**\n"
        f"`{fmt_r(cp)} + ({markup}% × {fmt_r(cp)}) = {fmt_r(cp)} + {fmt_r(profit)} = {fmt_r(sp)}` -> Answer: `{sp}` [2]"
    )
    return build_short(
        rng,
        qid="g9_dj_17",
        subskill="17_selling_price_from_cost_price_markup_calc",
        title="Calculate Selling Price from Cost Price & Mark-up",
        prompt=prompt,
        expected_answer=str(sp),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Add the mark-up profit percentage onto 100% of Cost Price.",
            "tier_2": f"Selling Price = {cp} × {100 + markup} / 100.",
            "tier_3": f"Selling Price = {sp}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Profit = {fmt_r(profit)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Selling Price = {sp}", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_instead_of_multiplying_when_finding_sp"],
    )


def arch_18_dj_missing_sales_and_cos_cells_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 3)
    markup = rng.choice([25, 50, 60, 80])
    cps = [rng.randint(8, 25) * 100 for _ in range(3)]
    sps = [c * (100 + markup) // 100 for c in cps]
    inv0 = rng.randint(201, 310)
    days = [4, 14, 23]

    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    data_rows = [
        [str(inv0), str(days[0]), debtors[0][0], debtors[0][1], str(sps[0]), str(cps[0])],
        [str(inv0 + 1), str(days[1]), debtors[1][0], debtors[1][1], str(sps[1]), str(cps[1])],
        [str(inv0 + 2), str(days[2]), debtors[2][0], debtors[2][1], str(sps[2]), str(cps[2])],
        ["", "", "TOTAL", "", str(sum(sps)), str(sum(cps))],
    ]
    # Give SP on row 0, CP on row 1, SP on row 2; ask missing counterpart + column totals
    given = {
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 5),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 2),
    }
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r0_c5": f"Cost of Sales = {sps[0]} × 100 / {100 + markup} = {cps[0]}.",
        "t0_r1_c4": f"Sales = {cps[1]} × {100 + markup} / 100 = {sps[1]}.",
        "t0_r2_c5": f"Cost of Sales = {sps[2]} × 100 / {100 + markup} = {cps[2]}.",
        "t0_r3_c4": f"Sum all 3 Sales entries = {sum(sps)}.",
        "t0_r3_c5": f"Sum all 3 Cost of Sales entries = {sum(cps)}.",
    }
    prompt = (
        f"**{biz}** maintains a uniform profit mark-up of **{markup}% on cost**.\n\n"
        f"Complete the missing **Sales**, **Cost of Sales**, and **TOTAL** cells in the Debtors Journal below *(leave blank cells empty; enter digits only)*."
    )
    worked = (
        f"**Completed Debtors Journal ({markup}% mark-up on cost)** [5 marks]\n\n"
        "| Doc No | Day | Debtor | Fol | Sales | Cost of Sales |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| {inv0} | {days[0]} | {debtors[0][0]} | {debtors[0][1]} | {sps[0]} | **{cps[0]}** |\n"
        f"| {inv0+1} | {days[1]} | {debtors[1][0]} | {debtors[1][1]} | **{sps[1]}** | {cps[1]} |\n"
        f"| {inv0+2} | {days[2]} | {debtors[2][0]} | {debtors[2][1]} | {sps[2]} | **{cps[2]}** |\n"
        f"| | | **TOTAL** | | **{sum(sps)}** | **{sum(cps)}** |"
    )
    return build_table(
        rng,
        qid="g9_dj_18",
        subskill="18_dj_missing_sales_and_cos_cells_table",
        title="Complete Missing DJ Sales, Cost of Sales & Totals",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"r0_cos={cps[0]}; r1_sales={sps[1]}; r2_cos={cps[2]}; Tot Sales={sum(sps)}; Tot CoS={sum(cps)}",
        marks=5,
        hints={
            "tier_1": f"From Sales to Cost of Sales: multiply by 100/{100+markup}. From Cost of Sales to Sales: multiply by {100+markup}/100.",
            "tier_2": f"Row 1 CoS={cps[0]}; Row 2 Sales={sps[1]}; Row 3 CoS={cps[2]}.",
            "tier_3": f"Total Sales = {sum(sps)}; Total Cost of Sales = {sum(cps)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Row 1 CoS = {cps[0]}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Row 2 Sales = {sps[1]}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Row 3 CoS = {cps[2]}", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Totals: Sales {sum(sps)}, CoS {sum(cps)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["mixing_up_cost_to_sales_and_sales_to_cost_formulas"],
    )


def arch_19_dj_complete_full_4row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    markup = rng.choice([25, 50, 80, 100])
    debtors = pick_debtors(rng, 3)
    order = [debtors[0], debtors[1], debtors[2], debtors[0]]
    days = [5, 11, 18, 26]
    inv0 = rng.randint(101, 250)
    cps = [rng.randint(10 + i * 3, 28 + i * 5) * 100 for i in range(4)]
    sps = [c * (100 + markup) // 100 for c in cps]

    txns = [
        f"Day {days[i]}: Sold trading stock on credit to {order[i][0]} ({order[i][1]}) for {fmt_r(sps[i])}. Issued duplicate invoice {inv0 + i}."
        for i in range(4)
    ]
    data_rows = [
        [str(inv0 + i), str(days[i]), order[i][0], order[i][1], str(sps[i]), str(cps[i])]
        for i in range(4)
    ]
    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints: Dict[str, str] = {}
    for i in range(4):
        cell_hints[f"t0_r{i}_c0"] = f"Duplicate invoice number is {inv0 + i}."
        cell_hints[f"t0_r{i}_c1"] = f"Day is {days[i]}."
        cell_hints[f"t0_r{i}_c2"] = f"Debtor is {order[i][0]}."
        cell_hints[f"t0_r{i}_c3"] = f"Debtors Ledger folio is {order[i][1]}."
        cell_hints[f"t0_r{i}_c4"] = f"Selling price in Sales column = {sps[i]}."
        cell_hints[f"t0_r{i}_c5"] = f"Cost of Sales = {sps[i]} × 100 / {100 + markup} = {cps[i]}."

    tot_s = sum(sps)
    tot_c = sum(cps)
    md_rows = "\n".join(f"| {inv0+i} | {days[i]} | {order[i][0]} | {order[i][1]} | {sps[i]} | {cps[i]} |" for i in range(4))
    worked = (
        f"**Debtors Journal of {biz} for {m_name} {yr}** [12 marks]\n\n"
        f"| Doc No | Day | Debtor | Fol | Sales | Cost of Sales |\n| --- | --- | --- | --- | --- | --- |\n"
        f"{md_rows}\n"
        f"| | | **TOTAL** | | **{tot_s}** | **{tot_c}** |\n\n"
        f"Check: `{tot_c} × {100 + markup}/100 = {tot_s}`."
    )
    prompt = (
        f"Complete the **Debtors Journal** of **{biz}** for **{m_name} {yr}**.\n"
        f"The business adds a **{markup}% mark-up on cost price** *(enter digits without spaces or R in money columns)*."
    )
    return build_table(
        rng,
        qid="g9_dj_19",
        subskill="19_dj_complete_full_4row_table",
        title="Complete Full Debtors Journal (4 Credit Sales)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Total Sales = {fmt_r(tot_s)}; Total Cost of Sales = {fmt_r(tot_c)}.",
        marks=12,
        hints={
            "tier_1": "Record Doc No, Day, Debtor, Fol, Selling Price (Sales), and Cost Price (Cost of Sales).",
            "tier_2": f"Compute Cost of Sales = Sales × 100 / {100 + markup} for every transaction.",
            "tier_3": f"Total Sales = {fmt_r(tot_s)}; Total Cost of Sales = {fmt_r(tot_c)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Accurate Doc No, Day, Debtor, Fol across 4 rows", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Sales column entries totaling {fmt_r(tot_s)}", "marks": 4, "editable": True},
            {"id": "mp_3", "desc": f"Cost of Sales entries totaling {fmt_r(tot_c)}", "marks": 4, "editable": True},
        ],
        misconception_tags=["confusing_selling_price_with_cost_price_in_dj"],
        transactions=txns,
    )


def arch_20_dj_filter_cash_and_cpj_transactions_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    markup = rng.choice([25, 50, 80])
    debtors = pick_debtors(rng, 2)
    cp1, cp2 = rng.randint(10, 22) * 100, rng.randint(12, 26) * 100
    sp1, sp2 = cp1 * (100 + markup) // 100, cp2 * (100 + markup) // 100
    cash_sale = rng.randint(25, 55) * 100
    cheque_amt = rng.randint(12, 24) * 100
    receipt_debt = rng.randint(8, 16) * 100
    inv0 = rng.randint(121, 190)

    txns = [
        f"Day 02: Cash sales according to Cash Register Roll, {fmt_r(cash_sale)}.",
        f"Day 06: {debtors[0][0]} ({debtors[0][1]}) bought goods on credit for {fmt_r(sp1)}. Issued invoice {inv0}.",
        f"Day 11: Paid {sc['supplier']} {fmt_r(cheque_amt)} by EFT for stationery (Cheque/EFT 044).",
        f"Day 19: Received {fmt_r(receipt_debt)} from a debtor in settlement of last month's account (Receipt 75).",
        f"Day 25: Issued invoice {inv0 + 1} to {debtors[1][0]} ({debtors[1][1]}) for merchandise on account, {fmt_r(sp2)}.",
    ]
    data_rows = [
        [str(inv0), "6", debtors[0][0], debtors[0][1], str(sp1), str(cp1)],
        [str(inv0 + 1), "25", debtors[1][0], debtors[1][1], str(sp2), str(cp2)],
    ]
    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": f"Only credit sale #1 (Day 06, Invoice {inv0}) enters DJ row 1.",
        "t0_r0_c5": f"{sp1} × 100 / {100 + markup} = {cp1}.",
        "t0_r1_c0": f"Only credit sale #2 (Day 25, Invoice {inv0 + 1}) enters DJ row 2.",
        "t0_r1_c5": f"{sp2} × 100 / {100 + markup} = {cp2}.",
    }
    prompt = (
        f"Read the 5 transactions of **{biz}** for **{m_name} {yr}** (mark-up **{markup}% on cost**) "
        "and record **ONLY** the transactions applicable to the **Debtors Journal (DJ)** *(exclude CRJ/CPJ items)*."
    )
    worked = (
        f"**Filtered Debtors Journal (2 Credit Sales Only)** [6 marks]\n\n"
        "| Doc No | Day | Debtor | Fol | Sales | Cost of Sales |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| {inv0} | 6 | {debtors[0][0]} | {debtors[0][1]} | {sp1} | {cp1} |\n"
        f"| {inv0+1} | 25 | {debtors[1][0]} | {debtors[1][1]} | {sp2} | {cp2} |\n\n"
        "*Excluded: Day 02 Cash Sales (CRJ), Day 11 EFT payment (CPJ), Day 19 Debtor receipt (CRJ).*"
    )
    return build_table(
        rng,
        qid="g9_dj_20",
        subskill="20_dj_filter_cash_and_cpj_transactions_table",
        title="Filter Out CRJ/CPJ Entries & Complete DJ",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Day 6 Inv {inv0} ({debtors[0][0]}: {sp1}/{cp1}); Day 25 Inv {inv0+1} ({debtors[1][0]}: {sp2}/{cp2})",
        marks=6,
        hints={
            "tier_1": "Cash sales and debtor receipts go to CRJ; EFT payments go to CPJ; ONLY credit sales go to DJ.",
            "tier_2": f"Only Days 6 (Inv {inv0}) and 25 (Inv {inv0+1}) belong in the Debtors Journal.",
            "tier_3": f"Inv {inv0}: Sales {sp1}, CoS {cp1}; Inv {inv0+1}: Sales {sp2}, CoS {cp2}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Excludes CRJ/CPJ distractors cleanly", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Records Day 6 & Day 25 Sales ({sp1}, {sp2}) and CoS ({cp1}, {cp2})", "marks": 4, "editable": True},
        ],
        misconception_tags=["including_cash_sales_or_debtor_receipts_in_dj"],
        transactions=txns,
    )


def arch_21_dj_column_totals_and_cos_control_check_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    markup = rng.choice([25, 40, 50, 60])
    cos_tot = rng.randint(24, 65) * 500
    sales_tot = cos_tot * (100 + markup) // 100
    error_diff = rng.choice([250, 400, 600, 900])
    recorded_cos = cos_tot + rng.choice([-1, 1]) * error_diff

    prompt = (
        f"At month-end, **{biz}** checks its Debtors Journal totals (standard mark-up is **{markup}% on cost**):\n"
        f"- Total **Sales** column: **{fmt_r(sales_tot)}**\n"
        f"- Recorded Total **Cost of Sales** column: **{fmt_r(recorded_cos)}**\n\n"
        f"What **should** the true Cost of Sales total equal according to the control check formula? [3]\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Step 1 — Control Check Rule:**\n"
        f"Total Cost of Sales must equal `Total Sales × 100 / (100 + {markup})` [1]\n\n"
        "**Step 2 — Verify True Total:**\n"
        f"`{fmt_r(sales_tot)} × 100 / {100 + markup} = {fmt_r(cos_tot)}` (so the recorded {fmt_r(recorded_cos)} contains an error of {fmt_r(error_diff)}). [2]\n\n"
        f"Answer: `{cos_tot}`"
    )
    return build_short(
        rng,
        qid="g9_dj_21",
        subskill="21_dj_column_totals_and_cos_control_check_calc",
        title="DJ Cost of Sales Column Control Check",
        prompt=prompt,
        expected_answer=str(cos_tot),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "When mark-up % is constant, Total Cost of Sales must reconcile with Total Sales.",
            "tier_2": f"Compute {sales_tot} × 100 / {100 + markup}.",
            "tier_3": f"True Cost of Sales total = {cos_tot}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Computes {sales_tot} × 100/{100 + markup} = {cos_tot}", "marks": 3, "editable": True},
        ],
        misconception_tags=["accepting_unreconciled_dj_column_totals"],
    )


def arch_22_dj_gross_profit_from_journal_totals_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    markup = rng.choice([25, 40, 50, 60, 75])
    cos_tot = rng.randint(15, 45) * 1000
    sales_tot = cos_tot * (100 + markup) // 100
    gp = sales_tot - cos_tot

    prompt = (
        f"The completed **Debtors Journal** of **{biz}** shows month-end totals of:\n"
        f"- **Sales:** {fmt_r(sales_tot)}\n"
        f"- **Cost of Sales:** {fmt_r(cos_tot)}\n\n"
        "Calculate the **Gross Profit** earned on credit sales **AND** state the achieved **mark-up % on cost**.\n"
        f"Give your numerical **Gross Profit** in Rands *(enter whole digits without spaces or R)* [3]."
    )
    worked = (
        "**Step 1 — Gross Profit from Credit Sales:**\n"
        f"`Gross Profit = Sales - Cost of Sales = {fmt_r(sales_tot)} - {fmt_r(cos_tot)} = {fmt_r(gp)}` [2]\n\n"
        "**Step 2 — Mark-up % Verification:**\n"
        f"`Mark-up % = ({gp} / {cos_tot}) × 100 = {markup}%` [1]\n\n"
        f"Answer: `{gp}`"
    )
    return build_short(
        rng,
        qid="g9_dj_22",
        subskill="22_dj_gross_profit_from_journal_totals_calc",
        title="Gross Profit & Mark-up % from DJ Totals",
        prompt=prompt,
        expected_answer=str(gp),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Gross profit is the difference between revenue (Sales) and stock cost (Cost of Sales).",
            "tier_2": f"Subtract {fmt_r(cos_tot)} from {fmt_r(sales_tot)}.",
            "tier_3": f"Gross profit = {gp} (representing a {markup}% mark-up).",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts Cost of Sales from Sales = {gp}", "marks": 3, "editable": True},
        ],
        misconception_tags=["adding_sales_and_cos_for_profit"],
    )


def arch_23_dj_folio_numbering_and_credit_sale_sorting_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 3)
    inv0 = rng.randint(401, 450)
    markup = rng.choice([25, 50])
    cps = [rng.randint(8, 20) * 100 for _ in range(3)]
    sps = [c * (100 + markup) // 100 for c in cps]
    days = [4, 15, 27]
    # Shuffle presentation of raw duplicate invoices in prompt so student orders chronologically
    items = [
        (inv0 + 0, days[0], debtors[0][0], debtors[0][1], sps[0], cps[0]),
        (inv0 + 1, days[1], debtors[1][0], debtors[1][1], sps[1], cps[1]),
        (inv0 + 2, days[2], debtors[2][0], debtors[2][1], sps[2], cps[2]),
    ]
    shuffled = list(items)
    rng.shuffle(shuffled)
    txns = [
        f"Duplicate Invoice {d[0]} (Day {d[1]}): {d[2]} (Folio {d[3]}), Selling Price {fmt_r(d[4])}."
        for d in shuffled
    ]

    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    data_rows = [[str(d[0]), str(d[1]), d[2], d[3], str(d[4]), str(d[5])] for d in items]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        f"t0_r{i}_c0": f"Earliest remaining invoice is {d[0]} on Day {d[1]}."
        for i, d in enumerate(items)
    }
    prompt = (
        f"The office clerk at **{biz}** dropped three duplicate invoices out of date order. "
        f"Sort them in **chronological / invoice-number order** into the Debtors Journal below (mark-up **{markup}% on cost**)."
    )
    md_rows = "\n".join(f"| {d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]} | {d[5]} |" for d in items)
    worked = (
        "**Chronologically Sorted Debtors Journal** [6 marks]\n\n"
        "| Doc No | Day | Debtor | Fol | Sales | Cost of Sales |\n| --- | --- | --- | --- | --- | --- |\n"
        + md_rows
    )
    return build_table(
        rng,
        qid="g9_dj_23",
        subskill="23_dj_folio_numbering_and_credit_sale_sorting_table",
        title="Sort Duplicate Invoices Chronologically in DJ",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"Day {d[1]} Inv {d[0]} ({d[2]} {d[4]}/{d[5]})" for d in items),
        marks=6,
        hints={
            "tier_1": "Journals must always be entered in strict chronological (date / invoice number) sequence.",
            "tier_2": f"Order by Day: {days[0]}, then {days[1]}, then {days[2]}.",
            "tier_3": f"Inv {inv0} (Day {days[0]}), Inv {inv0+1} (Day {days[1]}), Inv {inv0+2} (Day {days[2]}).",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Entries ordered strictly by Day / Doc No", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Correct Debtors, Folios, Sales & Cost of Sales", "marks": 4, "editable": True},
        ],
        misconception_tags=["entering_invoices_out_of_chronological_order"],
        transactions=txns,
    )


def arch_24_debtors_allowance_definition_and_reasons(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    scenario = rng.choice([
        "receives cracked goods and wrong shoe sizes",
        "discovers an invoice overcharge of R180",
        "receives the wrong colour stock from the order",
    ])

    prompt = (
        f"**{debtor}** bought goods on account from **{biz}** and **{scenario}**.\n\n"
        "Why does **{biz}** grant a **Debtors Allowance**, and which journal records it?"
    )
    correct = "To reduce the debtor's account for damaged, incorrect, or overcharged goods while preserving customer goodwill; recorded in the Debtors Allowance Journal (DAJ)."
    distractors = [
        "To add extra penalty interest onto the customer's debt in the Cash Receipts Journal (CRJ).",
        "To record supplier overcharges when the business buys equipment on account in the CJ.",
        "To replace the original credit sale entirely inside the Cash Payments Journal (CPJ).",
    ]
    return build_mcq(
        rng,
        qid="g9_dj_24",
        subskill="24_debtors_allowance_definition_and_reasons",
        title="Reasons for Granting Debtors Allowance",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Businesses grant **Debtors Allowances** (returns of faulty/wrong goods or price overcharge rebates) "
            "to settle valid complaints fairly and retain loyal customers; these are recorded in the **DAJ**."
        ),
        hints={
            "tier_1": "What does a seller offer a credit customer who returns faulty items or was overcharged?",
            "tier_2": "A Debtors Allowance reduces what the debtor owes and is recorded in the DAJ.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_debtors_allowance_with_creditors_allowance"],
    )


def arch_25_duplicate_credit_note_source_document_card_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    cn_no = rng.randint(15, 85)
    m_name, yr, _ = rng.choice(MONTH_DATA)
    day = rng.randint(8, 28)
    ret_amt = rng.randint(3, 18) * 100
    markup = rng.choice([25, 50])
    ret_cp = ret_amt * 100 // (100 + markup)

    svg = source_doc_svg(
        f"DUPLICATE CREDIT NOTE — {biz}",
        f"CN-{cn_no}",
        f"{day:02d} {m_name} {yr}",
        [
            ("Debtor Credited", debtor),
            ("Reason", "Damaged merchandise returned"),
            ("Credit Amount", fmt_r(ret_amt)),
            ("Journal", "DAJ (Mark-up " + f"{markup}% on cost)"),
        ],
        accent="#b45309",
    )
    prompt = (
        f"Examine the **Duplicate Credit Note** (`CN-{cn_no}`) issued by **{biz}** to **{debtor}** in the source document card below.\n\n"
        f"Calculate the **Cost of Sales** value to record in the **Debtors Allowance Journal (DAJ)** for this return [2].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Duplicate Credit Note CN-{cn_no} ({debtor}) -> DAJ Entry** [2 marks]\n\n"
        f"- Debtors Allowance column (Selling Price): **{fmt_r(ret_amt)}**\n"
        f"- Cost of Sales returned to stock: `{ret_amt} × 100 / {100 + markup} = {fmt_r(ret_cp)}`\n"
        f"- Answer: `{ret_cp}`"
    )
    return build_short(
        rng,
        qid="g9_dj_25",
        subskill="25_duplicate_credit_note_source_document_card_svg",
        title="Read Duplicate Credit Note Source Document",
        prompt=prompt,
        expected_answer=str(ret_cp),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "The credit note states the selling value returned; convert to cost price using mark-up %.",
            "tier_2": f"Cost of Sales = {ret_amt} × 100 / {100 + markup}.",
            "tier_3": f"DAJ Cost of Sales = {ret_cp}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates Cost of Sales returned = {ret_cp}", "marks": 2, "editable": True},
        ],
        misconception_tags=["entering_selling_price_in_daj_cost_of_sales"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_cash_sales_vs_credit_sales_distinction": arch_01_cash_sales_vs_credit_sales_distinction,
    "02_debtor_definition_current_asset_role": arch_02_debtor_definition_current_asset_role,
    "03_national_credit_act_purpose_reckless_lending": arch_03_national_credit_act_purpose_reckless_lending,
    "04_credit_limit_vs_credit_term_definitions": arch_04_credit_limit_vs_credit_term_definitions,
    "05_creditworthy_vs_credit_reference_concepts": arch_05_creditworthy_vs_credit_reference_concepts,
    "06_credit_bureau_and_salary_advice_evaluation": arch_06_credit_bureau_and_salary_advice_evaluation,
    "07_credit_application_affordability_disposable_income_calc": arch_07_credit_application_affordability_disposable_income_calc,
    "08_reasons_businesses_grant_credit_advantages": arch_08_reasons_businesses_grant_credit_advantages,
    "09_risks_and_disadvantages_of_credit_sales": arch_09_risks_and_disadvantages_of_credit_sales,
    "10_debtors_accounting_cycle_sequence": arch_10_debtors_accounting_cycle_sequence,
    "11_duplicate_invoice_source_document_card_svg": arch_11_duplicate_invoice_source_document_card_svg,
    "12_duplicate_vs_original_invoice_rule": arch_12_duplicate_vs_original_invoice_rule,
    "13_calculate_missing_invoice_line_and_total_table": arch_13_calculate_missing_invoice_line_and_total_table,
    "14_debtors_journal_purpose_and_exclusions": arch_14_debtors_journal_purpose_and_exclusions,
    "15_journal_classification_dj_daj_crj_cpj_matrix": arch_15_journal_classification_dj_daj_crj_cpj_matrix,
    "16_cost_price_from_selling_price_markup_formula": arch_16_cost_price_from_selling_price_markup_formula,
    "17_selling_price_from_cost_price_markup_calc": arch_17_selling_price_from_cost_price_markup_calc,
    "18_dj_missing_sales_and_cos_cells_table": arch_18_dj_missing_sales_and_cos_cells_table,
    "19_dj_complete_full_4row_table": arch_19_dj_complete_full_4row_table,
    "20_dj_filter_cash_and_cpj_transactions_table": arch_20_dj_filter_cash_and_cpj_transactions_table,
    "21_dj_column_totals_and_cos_control_check_calc": arch_21_dj_column_totals_and_cos_control_check_calc,
    "22_dj_gross_profit_from_journal_totals_calc": arch_22_dj_gross_profit_from_journal_totals_calc,
    "23_dj_folio_numbering_and_credit_sale_sorting_table": arch_23_dj_folio_numbering_and_credit_sale_sorting_table,
    "24_debtors_allowance_definition_and_reasons": arch_24_debtors_allowance_definition_and_reasons,
    "25_duplicate_credit_note_source_document_card_svg": arch_25_duplicate_credit_note_source_document_card_svg,
}
