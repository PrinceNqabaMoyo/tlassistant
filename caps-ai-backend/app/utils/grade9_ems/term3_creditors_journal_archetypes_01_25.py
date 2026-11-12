"""Grade 9 EMS - Credit Transactions (Creditors 1): Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Creditors 1).md
- curriculum_docs/EMS_Gr9/Term 3/10-Credit transactions Creditors (1).md
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Debtors 2).md (Lesson 6 Creditors Journal)

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "Credit transactions (Creditors 1)"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_creditors_journal"
CURRICULUM_REFERENCE = "Term 3 > Financial Literacy: Credit Transactions (Creditors 1)"

TRADER_SUFFIXES = [
    "Traders",
    "Stores",
    "Outfitters",
    "Hardware",
    "Suppliers",
    "Wholesalers",
    "Stationers",
    "Furnishers",
    "Boutique",
    "Emporium",
]

MONTH_DATA = [
    ("July", "2026", "Jul"),
    ("August", "2026", "Aug"),
    ("September", "2026", "Sep"),
    ("October", "2026", "Oct"),
    ("November", "2026", "Nov"),
    ("March", "2026", "Mar"),
]

CREDITOR_POOL = [
    ("Eggers Wholesalers", "C1"),
    ("Cotfab Distributors", "C2"),
    ("Pretorius Suppliers", "C3"),
    ("Pen & Paper Co.", "C4"),
    ("Klaasen Distributors", "C5"),
    ("Makhubo Wholesale", "C6"),
    ("CJ Office Supplies", "C7"),
    ("Zandvliet Distributors", "C8"),
]

STOCK_LINES = [
    "school tracksuits",
    "cotton T-shirts",
    "hardware toolboxes",
    "sports shoes",
    "solar lanterns",
    "winter jackets",
    "kitchenware sets",
    "canvas backpacks",
]

SUNDRY_ITEMS = [
    ("Equipment", "display shelving unit"),
    ("Equipment", "barcode scanner and till drawer"),
    ("Equipment", "heavy-duty shop counter"),
    ("Packing material", "printed carrier bags and boxes"),
    ("Repairs", "repair of store security gate"),
    ("Repairs", "servicing of delivery scooter"),
]

CJ_HEADERS = [
    "Doc No",
    "Day",
    "Creditor",
    "Fol",
    "Creditors Control",
    "Trading Stock",
    "Stationery",
    "Sundry Amount",
    "Sundry Details",
]

CAJ_HEADERS = [
    "Doc No",
    "Day",
    "Creditor",
    "Fol",
    "Creditors Control",
    "Trading Stock",
    "Stationery",
    "Sundry Amount",
    "Sundry Details",
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


def pick_creditors(rng: random.Random, n: int = 3) -> List[Tuple[str, str]]:
    chosen = rng.sample(CREDITOR_POOL, n)
    return [(name, f"C{i + 1}") for i, (name, _) in enumerate(chosen)]


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
    term: int = 3,
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
        "learning_objective_id": f"lo_g9_cj_{subskill}",
        "concept_id": subskill,
        "concept_group": "creditors_1",
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
        "diagnostic_tags": ["accounting", "creditors_journal", "credit_purchases"],
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
    term: int = 3,
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
        "learning_objective_id": f"lo_g9_cj_{subskill}",
        "concept_id": subskill,
        "concept_group": "creditors_1",
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
        "diagnostic_tags": ["accounting", "creditors_journal", "credit_purchases"],
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
    journal_type: str = "cj",
    transactions: Optional[List[str]] = None,
    term: int = 3,
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
        "learning_objective_id": f"lo_g9_cj_{subskill}",
        "concept_id": subskill,
        "concept_group": "creditors_1",
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
        "diagnostic_tags": ["accounting", "creditors_journal", "tabular"],
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
    accent: str = "#0f766e",
) -> str:
    """Render clean source-document card SVG (Original Credit Invoice / Debit Note)."""
    y = 84
    parts: List[str] = []
    for lbl, val in lines:
        parts.append(
            f'<text x="22" y="{y}" font-size="11" font-weight="bold" fill="#475569">{lbl}:</text>'
            f'<text x="175" y="{y}" font-size="11.5" font-weight="bold" fill="#0f172a">{val}</text>'
            f'<line x1="22" y1="{y + 7}" x2="518" y2="{y + 7}" stroke="#e2e8f0" stroke-width="1"/>'
        )
        y += 28
    h = max(195, y + 16)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 {h}" width="540" height="{h}">'
        f'<rect x="6" y="6" width="528" height="{h - 12}" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<rect x="6" y="6" width="528" height="44" rx="8" fill="{accent}"/>'
        f'<text x="22" y="33" font-size="13" font-weight="bold" fill="#ffffff">{header_title}</text>'
        f'<text x="518" y="24" font-size="11" font-weight="bold" text-anchor="end" fill="#f8fafc">Doc No: {doc_no}</text>'
        f'<text x="518" y="40" font-size="10" text-anchor="end" fill="#e2e8f0">Date: {date_str}</text>'
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


def arch_01_creditor_definition_current_liability_role(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    goods = rng.choice(STOCK_LINES)
    amt = rng.randint(15, 65) * 200
    days = rng.choice([30, 60, 90])

    prompt = (
        f"**{biz}** in {sc['area']} purchases **{goods}** worth **{fmt_r(amt)}** on credit from **{sup}**, "
        f"agreeing to settle the account within **{days} days**.\n\n"
        f"In the accounting books of **{biz}**, what is **{sup}** classified as?"
    )
    correct = (
        f"A Creditor — a Current Liability representing short-term money {biz} owes to {sup} for credit purchases."
    )
    distractors = [
        f"A Debtor — a Current Asset because {biz} will receive cash from {sup} within {days} days.",
        f"Owner's Equity — because credit stock increases {biz}'s net worth without reducing cash.",
        f"A Non-Current Asset — because trading stock purchased on credit stays in the shop permanently.",
    ]
    explanation = (
        f"- **Creditor definition**: A supplier to whom the business owes money after buying goods or services on credit.\n"
        f"- Because {biz} must pay {sup} **{fmt_r(amt)}** within **{days} days** (less than 12 months), "
        f"**{sup}** is a **Current Liability** in {biz}'s books."
    )
    hints = {
        "tier_1": "Ask yourself: does the business receive money or owe money in this transaction?",
        "tier_2": "A supplier who sells to you on credit creates a short-term obligation to pay later (Current Liability).",
        "tier_3": f"{biz} owes {sup} {fmt_r(amt)} within {days} days, so {sup} is a Creditor (Current Liability).",
    }
    return build_mcq(
        rng, qid="g9_cj_01", subskill="01_creditor_definition_current_liability_role",
        title="Creditor Definition & Current Liability Classification",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["creditor_vs_debtor_confusion", "liability_classification_error"],
    )


def arch_02_debtor_vs_creditor_perspective_comparison(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    buyer = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    goods = rng.choice(STOCK_LINES)
    amt = rng.randint(14, 55) * 200
    days = rng.choice([30, 45, 60])

    prompt = (
        f"**{sup}** sells **{goods}** worth **{fmt_r(amt)}** on **{days}-day credit** to **{buyer}**.\n\n"
        f"How do **BOTH** businesses classify the other party in their respective journals?"
    )
    correct = (
        f"{buyer} treats {sup} as a Creditor (Creditors Journal); "
        f"{sup} treats {buyer} as a Debtor (Debtors Journal)."
    )
    distractors = [
        f"Both {buyer} and {sup} treat the transaction as a Creditor entry in the CJ.",
        f"{buyer} treats {sup} as a Debtor (DJ); {sup} treats {buyer} as a Creditor (CJ).",
        f"Both businesses wait until payment in {days} days and only record it in the CRJ/CPJ.",
    ]
    explanation = (
        f"- **From {buyer}'s perspective (buyer on credit)**: {buyer} owes **{fmt_r(amt)}**, so **{sup}** is a **Creditor** recorded in {buyer}'s **Creditors Journal (CJ)**.\n"
        f"- **From {sup}'s perspective (seller on credit)**: {sup} is owed **{fmt_r(amt)}**, so **{buyer}** is a **Debtor** recorded in {sup}'s **Debtors Journal (DJ)**."
    )
    hints = {
        "tier_1": "One business is buying on credit and the other is selling on credit.",
        "tier_2": "Buyer on credit -> Creditors Journal (Creditor). Seller on credit -> Debtors Journal (Debtor).",
        "tier_3": f"{buyer} buys ({sup} = Creditor in CJ); {sup} sells ({buyer} = Debtor in DJ).",
    }
    return build_mcq(
        rng, qid="g9_cj_02", subskill="02_debtor_vs_creditor_perspective_comparison",
        title="Buyer vs Seller Perspective: Creditor vs Debtor",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["perspective_reversal_debtor_creditor"],
    )


def arch_03_creditors_accounting_cycle_step_sequence(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    goods = rng.choice(STOCK_LINES)

    prompt = (
        f"**{biz}** regularly buys **{goods}** on credit from **{sup}**.\n\n"
        f"Which sequence puts the **credit purchases accounting cycle** in the correct chronological order?"
    )
    correct = (
        "Order placed -> Goods & Original Invoice received -> Invoice checked & renumbered (C1, C2...) -> "
        "Recorded in Creditors Journal (CJ) -> Posted to Creditors Ledger & General Ledger -> Paid later via CPJ"
    )
    distractors = [
        "Recorded in CPJ -> Order placed -> Duplicate Invoice sent to supplier -> Posted to Debtors Ledger",
        "Original Invoice received -> Paid immediately via CRJ -> Renumbered as D1, D2 -> Recorded in DJ",
        "Posted to General Ledger -> Goods delivered -> Purchase order written -> Invoice issued by buyer",
    ]
    explanation = (
        f"1. **{biz}** orders {goods} from **{sup}**.\n"
        f"2. Goods arrive with **{sup}'s Original Credit Invoice**.\n"
        f"3. {biz} checks prices/quantities, **renumbers** the invoice sequentially (`C1, C2...`), and enters it in the **Creditors Journal (CJ)**.\n"
        f"4. Totals & individual entries are posted to the **Creditors Ledger** and **General Ledger**.\n"
        f"5. Later, when {biz} settles the account, the payment is recorded in the **CPJ**."
    )
    hints = {
        "tier_1": "Start with ordering/receiving goods and the source document, before writing up the CJ.",
        "tier_2": "Remember: invoices come from the supplier BEFORE recording in CJ, and settlement happens later in CPJ.",
        "tier_3": "Order -> Original Invoice received & renumbered -> CJ -> Ledgers -> Payment in CPJ.",
    }
    return build_mcq(
        rng, qid="g9_cj_03", subskill="03_creditors_accounting_cycle_step_sequence",
        title="Accounting Cycle for Credit Purchases",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["accounting_cycle_order_error"],
    )


def arch_04_original_invoice_renumbering_rule_cj(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = pick_creditors(rng, 2)
    sup1, _ = creds[0]
    sup2, _ = creds[1]
    inv_a = rng.randint(410, 999)
    inv_b = rng.randint(1050, 2999)
    start_c = rng.randint(1, 5)

    prompt = (
        f"During one week, **{biz}** buys stock on credit from **{sup1}** (supplier invoice **#{inv_a}**) "
        f"and stationery on credit from **{sup2}** (supplier invoice **#{inv_b}**).\n\n"
        f"Why must the bookkeeper at **{biz}** renumber these **original invoices** as **C{start_c}** and **C{start_c + 1}** "
        f"before entering them into the **Creditors Journal (CJ)**?"
    )
    correct = (
        "Suppliers use their own unrelated invoice numbering systems; renumbering sequentially (C1, C2...) "
        "gives a continuous audit trail for internal filing and prevents missing or duplicate entries."
    )
    distractors = [
        "Only duplicate invoices keep the supplier's number; original invoices are illegal to file in South Africa.",
        "Renumbering automatically reduces the invoice amount by the supplier's trade discount percentage.",
        f"Changing #{inv_a} to C{start_c} turns the liability into an asset in {biz}'s General Ledger.",
    ]
    explanation = (
        f"- In the **DJ**, the business issues its own *duplicate* invoices (`INV01, INV02...`), which are already in order.\n"
        f"- In the **CJ**, **{biz}** receives **original invoices** from many different suppliers (`#{inv_a}` from {sup1}, `#{inv_b}` from {sup2}).\n"
        f"- Renumbering them in order (`C{start_c}`, `C{start_c + 1}`) creates a **sequential internal audit trail** for filing and CJ cross-checking."
    )
    hints = {
        "tier_1": "Think about why two different suppliers' invoice numbers (`#410` and `#2099`) don't form a neat sequence.",
        "tier_2": "A journal's Doc No column needs an unbroken sequence so lost or unrecorded invoices are spotted easily.",
        "tier_3": f"Original invoices come from external suppliers with unrelated numbers, so {biz} renumbers them C{start_c}, C{start_c + 1} for filing and audit control.",
    }
    return build_mcq(
        rng, qid="g9_cj_04", subskill="04_original_invoice_renumbering_rule_cj",
        title="Original Invoices & Sequential Renumbering in CJ",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["duplicate_vs_original_invoice_confusion", "renumbering_purpose_unknown"],
    )


def arch_05_source_document_card_original_invoice_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    month, year, _ = rng.choice(MONTH_DATA)
    day = rng.randint(4, 24)
    sup_inv = f"INV-{rng.randint(310, 895)}"
    prev_c = rng.randint(2, 9)
    next_c = f"C{prev_c + 1}"
    goods = rng.choice(STOCK_LINES)
    list_price = rng.randint(15, 45) * 400
    disc_pct = rng.choice([5, 10, 15, 20])
    net_amt = list_price * (100 - disc_pct) // 100
    date_str = f"{day} {month} {year}"

    svg = source_doc_svg(
        header_title=f"ORIGINAL TAX INVOICE - {sup.upper()}",
        doc_no=sup_inv,
        date_str=date_str,
        lines=[
            ("Sold To (Buyer)", f"{biz}, {sc['area']}"),
            ("Terms", "30 Days Credit (No Cash Paid Today)"),
            ("Goods Supplied", f"{goods.capitalize()} (Trading Stock)"),
            ("List Price", fmt_r(list_price)),
            ("Less Trade Discount", f"{disc_pct}% (-{fmt_r(list_price - net_amt)})"),
            ("Net Amount Due", fmt_r(net_amt)),
        ],
        accent="#0f766e",
    )
    diagram_spec = {
        "kind": "inline_svg",
        "svg": svg,
        "title": f"Original Credit Invoice {sup_inv} from {sup}",
        "diagram_role": "context",
    }

    prompt = (
        f"Inspect the **Original Credit Invoice ({sup_inv})** from **{sup}** on **{date_str}**.\n\n"
        f"**{biz}**'s previous renumbered creditor invoice in the Creditors Journal was **C{prev_c}**.\n\n"
        f"State the **renumbered Doc No**, the **Net Amount** to record in the **Creditors Control** column of the CJ "
        f"(plain digits, no R or spaces), and the **analysis column** where this item belongs, separated by commas "
        f"(e.g. `C5, 7600, Trading Stock`)."
    )
    expected = f"{next_c}, {net_amt}, Trading Stock"
    worked = (
        f"**{expected}** [4 marks]\n\n"
        f"1. **Renumbered Doc No**: Previous invoice was `C{prev_c}`, so {sup_inv} is renumbered **`{next_c}`** [1 mark].\n"
        f"2. **Net Creditors Control Amount**: List price `{fmt_r(list_price)}` less `{disc_pct}%` trade discount (`{fmt_r(list_price - net_amt)}`) = **`{fmt_r(net_amt)}`** (`{net_amt}`) [2 marks].\n"
        f"3. **Analysis Column**: Merchandise bought for resale goes to **`Trading Stock`** [1 mark]."
    )
    hints = {
        "tier_1": "Check the net amount AFTER subtracting the trade discount, and advance the C-number by 1.",
        "tier_2": f"Net = List Price x (100% - {disc_pct}%). Only the net amount enters the CJ.",
        "tier_3": f"Doc No: {next_c}; Net: {list_price} - {list_price * disc_pct // 100} = {net_amt}; Analysis column: Trading Stock.",
    }
    return build_short(
        rng, qid="g9_cj_05", subskill="05_source_document_card_original_invoice_svg",
        title="Read an Original Credit Invoice & Renumber for CJ",
        prompt=prompt, expected_answer=expected, worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Correct sequential Doc No {next_c}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Correct net invoice amount {net_amt} after {disc_pct}% discount", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Identifies Trading Stock analysis column", "marks": 1, "editable": True},
        ],
        misconception_tags=["recorded_gross_instead_of_net", "failed_to_renumber_invoice"],
        marks=4, qtype="short_text", diagram_spec=diagram_spec,
    )


def arch_06_creditors_journal_purpose_and_cash_exclusions(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup1, sup2 = [c[0] for c in pick_creditors(rng, 2)]
    a1 = rng.randint(12, 35) * 200
    a2 = rng.randint(8, 25) * 100
    a3 = rng.randint(10, 30) * 150

    prompt = (
        f"**{biz}** recorded the following 4 events during the week:\n"
        f"1. Bought merchandise on credit from **{sup1}** for **{fmt_r(a1)}**.\n"
        f"2. Paid **{sup2}** **{fmt_r(a2)}** via EFT to settle last month's balance.\n"
        f"3. Bought stationery by debit card at the local stationer for **{fmt_r(a3)}**.\n"
        f"4. Owner **{sc['entrepreneur']}** bought groceries for personal family use on a private store card.\n\n"
        f"Which event(s) belong in **{biz}**'s **Creditors Journal (CJ)**?"
    )
    correct = f"Only event 1 ({fmt_r(a1)} credit purchase from {sup1}); events 2 and 3 belong in the CPJ, and event 4 is excluded."
    distractors = [
        "Events 1 and 2, because both transactions involve a supplier/creditor.",
        "Events 1, 2, and 3, because all three involve purchasing stock, stationery, or paying a supplier.",
        "Events 1 and 4, because both were bought on credit rather than paid immediately in cash.",
    ]
    explanation = (
        f"- **Rule**: The **Creditors Journal (CJ)** records **ONLY business credit purchases**.\n"
        f"- Event 1: Credit purchase of stock from {sup1} (**CJ**).\n"
        f"- Event 2: EFT payment to a creditor reduces Bank -> (**CPJ**).\n"
        f"- Event 3: Immediate debit card purchase -> (**CPJ**).\n"
        f"- Event 4: Private personal transaction violates the **business entity rule** -> (**Excluded** from {biz}'s books)."
    )
    hints = {
        "tier_1": "Only business purchases made ON CREDIT (pay later) belong in the CJ.",
        "tier_2": "Cash/EFT/card payments ALWAYS go to the CPJ, even if paid to a creditor. Private owner expenses stay out.",
        "tier_3": f"Only Event 1 ({sup1}) is a business credit purchase -> CJ.",
    }
    return build_mcq(
        rng, qid="g9_cj_06", subskill="06_creditors_journal_purpose_and_cash_exclusions",
        title="Creditors Journal Scope: Credit-Only & Business Entity Rules",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["entered_cash_payment_in_cj", "business_entity_violation"],
    )


def arch_07_cj_vs_cpj_bank_vs_creditors_control_comparison(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    amt = rng.randint(18, 48) * 200

    prompt = (
        f"Compare the **Cash Payments Journal (CPJ)** and the **Creditors Journal (CJ)** for **{biz}** "
        f"when buying equipment worth **{fmt_r(amt)}** from **{sup}**.\n\n"
        f"Why does the **Creditors Journal (CJ)** have a **Creditors Control** column right after `Fol` instead of a **Bank** column?"
    )
    correct = (
        "Because no cash leaves the bank account on the day of a credit purchase; instead, the total liability "
        "owed to creditors increases in Creditors Control."
    )
    distractors = [
        "Because the supplier deposits cash directly into the business bank account when selling on credit.",
        "Because Bank is only used for stationery and repairs, whereas Creditors Control is used for cash sales.",
        "Because South African accounting rules forbid recording any equipment purchases in the Bank column.",
    ]
    explanation = (
        f"- In the **CPJ**, money leaves the bank immediately, so the control column is **Bank**.\n"
        f"- In the **CJ**, **{biz}** receives the goods now and pays **{sup}** later, so **Bank is unchanged**; "
        f"instead, the business's liability rises, recorded in **Creditors Control** (**{fmt_r(amt)}**)."
    )
    hints = {
        "tier_1": "Ask whether cash leaves the bank account today when buying on credit.",
        "tier_2": "CPJ = Bank (cash paid now); CJ = Creditors Control (owed to creditors, paid later).",
        "tier_3": "No cash leaves the bank on credit purchase day; the debt owed increases Creditors Control.",
    }
    return build_mcq(
        rng, qid="g9_cj_07", subskill="07_cj_vs_cpj_bank_vs_creditors_control_comparison",
        title="Why CJ Uses Creditors Control Instead of Bank",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["bank_vs_creditors_control_confusion"],
    )


def arch_08_analysis_columns_selection_by_business_type(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    freq_items = rng.choice([
        ("Trading Stock and Packaging Material", "Equipment and Repairs"),
        ("Trading Stock and Stationery", "Vehicles and Computer Repairs"),
        ("Consumable Stores and Stationery", "Furniture and Advertising"),
    ])

    prompt = (
        f"When designing the **Creditors Journal (CJ)** for **{biz}**, management notes that "
        f"**{freq_items[0]}** are bought on credit every week, while **{freq_items[1]}** are bought on credit "
        f"only once or twice a year.\n\n"
        f"Which column layout should **{biz}** choose for its CJ?"
    )
    correct = (
        f"Create dedicated analysis columns for {freq_items[0]}, and record infrequent items "
        f"({freq_items[1]}) in Sundry Accounts."
    )
    distractors = [
        f"Create dedicated analysis columns for {freq_items[1]}, and put {freq_items[0]} into Sundry Accounts.",
        "Put every single credit purchase in Sundry Accounts so that no analysis columns are needed.",
        "Create 20 separate analysis columns for every possible expense in the economy before trading starts.",
    ]
    explanation = (
        f"- CJ analysis columns are tailored to each business's **most frequent credit purchases**.\n"
        f"- Weekly purchases (**{freq_items[0]}**) justify dedicated columns so monthly totals can be posted in one figure.\n"
        f"- Rare purchases (**{freq_items[1]}**) belong in **Sundry Accounts** (Amount + Details) to avoid dozens of empty columns."
    )
    hints = {
        "tier_1": "Which items occur repeatedly every week versus once or twice a year?",
        "tier_2": "Dedicated analysis columns save time for frequent transactions; Sundry Accounts handle occasional items.",
        "tier_3": f"Dedicated columns: {freq_items[0]}. Sundry Accounts: {freq_items[1]}.",
    }
    return build_mcq(
        rng, qid="g9_cj_08", subskill="08_analysis_columns_selection_by_business_type",
        title="Designing CJ Analysis Columns vs Sundry Accounts",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["analysis_column_design_error"],
    )


def arch_09_trade_discount_definition_and_purpose(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    pct = rng.choice([5, 10, 12, 15])
    list_p = rng.randint(20, 60) * 200
    net_p = list_p * (100 - pct) // 100

    prompt = (
        f"**{sup}** grants **{biz}** a **{pct}% trade discount** off the catalogue price of **{fmt_r(list_p)}**, "
        f"so the invoice total payable is **{fmt_r(net_p)}**.\n\n"
        f"How must **{biz}** treat this **{pct}%** trade discount in the **Creditors Journal (CJ)**?"
    )
    correct = (
        f"Record ONLY the net amount after trade discount ({fmt_r(net_p)}) in the CJ; "
        "do NOT record trade discount in a separate column or account."
    )
    distractors = [
        f"Enter {fmt_r(list_p)} in Creditors Control and subtract {fmt_r(list_p - net_p)} in the Sundry column.",
        f"Record {fmt_r(list_p - net_p)} as Discount Received in the CJ and record {fmt_r(list_p)} in Trading Stock.",
        f"Enter {fmt_r(list_p)} in the CJ now, then subtract {pct}% only when paying via the CPJ.",
    ]
    explanation = (
        f"- **Trade discount** is an immediate reduction off a supplier's catalogue/list price for bulk or trade buyers.\n"
        f"- **Golden Rule**: Trade discount is **deducted before recording**. Only the **net amount ({fmt_r(net_p)})** "
        f"appears in **Creditors Control** and **Trading Stock** (never recorded separately in the CJ)."
    )
    hints = {
        "tier_1": "Is trade discount ever written in its own column in the Creditors Journal?",
        "tier_2": "Trade discount adjusts the invoice price BEFORE bookkeeping begins. Contrast this with settlement discount later.",
        "tier_3": f"Deduct {pct}% first and enter ONLY {fmt_r(net_p)} in the CJ.",
    }
    return build_mcq(
        rng, qid="g9_cj_09", subskill="09_trade_discount_definition_and_purpose",
        title="Accounting Treatment of Trade Discount in CJ",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["trade_discount_entered_separately", "gross_price_recorded_in_cj"],
    )


def arch_10_calculate_net_invoice_single_trade_discount(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    goods = rng.choice(STOCK_LINES)
    pct = rng.choice([5, 10, 12, 12.5, 15, 20])
    # Choose list_price as multiple of 800 so 12.5% and 2.5% produce clean whole Rands
    list_price = rng.randint(4, 24) * 800
    disc_amt = int(round(list_price * pct / 100))
    net_amt = list_price - disc_amt
    pct_str = f"{pct}".replace(".", ",")

    prompt = (
        f"**{biz}** buys **{goods}** on credit from **{sup}** at a list price of **{fmt_r(list_price)}**, "
        f"less **{pct_str}% trade discount**.\n\n"
        f"Calculate the **net amount** (in Rand, plain number without R or spaces) to be entered into the **Creditors Journal**."
    )
    worked = (
        f"**{fmt_r(net_amt)}** (`{net_amt}`) [3 marks]\n\n"
        f"- **Step 1 (Trade Discount)**: "
        f"$\\text{{Discount}} = {fmt_r(list_price)} \\times \\frac{{{pct_str}}}{{100}} = {fmt_r(disc_amt)}$ [1 mark]\n"
        f"- **Step 2 (Net Invoice Amount)**: "
        f"$\\text{{Net}} = {fmt_r(list_price)} - {fmt_r(disc_amt)} = {fmt_r(net_amt)}$ [2 marks]\n"
        f"- Alternative: ${fmt_r(list_price)} \\times (100\\% - {pct_str}\\%) = {fmt_r(net_amt)}$."
    )
    hints = {
        "tier_1": f"First find {pct_str}% of {fmt_r(list_price)}, then subtract it from the list price.",
        "tier_2": f"Net price = List price x (100% - {pct_str}%).",
        "tier_3": f"{list_price} - ({list_price} x {pct}/100) = {list_price} - {disc_amt} = {net_amt}.",
    }
    return build_short(
        rng, qid="g9_cj_10", subskill="10_calculate_net_invoice_single_trade_discount",
        title="Calculate Net Invoice Amount After Trade Discount",
        prompt=prompt, expected_answer=str(net_amt), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Calculates {pct_str}% trade discount = {fmt_r(disc_amt)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Subtracts discount to get net invoice {fmt_r(net_amt)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["added_discount_instead_of_subtracting", "decimal_percent_error"],
        marks=3, qtype="math_short",
    )


def arch_11_calculate_original_list_price_before_trade_discount(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    pct = rng.choice([10, 12.5, 15, 20])
    pct_str = f"{pct}".replace(".", ",")
    # Construct exact integer net and list prices
    if pct == 12.5:
        base_unit = rng.randint(5, 20) * 800
    else:
        base_unit = rng.randint(6, 25) * 200
    list_price = base_unit
    net_amt = int(round(list_price * (100 - pct) / 100))

    prompt = (
        f"**{biz}** recorded a net amount of **{fmt_r(net_amt)}** in the Creditors Journal for stock bought on credit from **{sup}** "
        f"after receiving a **{pct_str}% trade discount**.\n\n"
        f"Calculate the **original catalogue (list) price** before the trade discount (plain number without R or spaces)."
    )
    rem_pct = f"{100 - pct}".replace(".", ",")
    worked = (
        f"**{fmt_r(list_price)}** (`{list_price}`) [3 marks]\n\n"
        f"- **Key Insight**: After a `{pct_str}%` discount, the net invoice represents **$100\\% - {pct_str}\\% = {rem_pct}\\%$** of the list price.\n"
        f"- **Calculation**: "
        f"$\\text{{List Price}} = {fmt_r(net_amt)} \\times \\frac{{100}}{{{rem_pct}}} = {fmt_r(list_price)}$ [3 marks]\n"
        f"- **Check**: ${fmt_r(list_price)} - {pct_str}\\% = {fmt_r(net_amt)}$."
    )
    hints = {
        "tier_1": f"Do NOT add {pct_str}% onto {fmt_r(net_amt)}! {fmt_r(net_amt)} equals {rem_pct}% of the original price.",
        "tier_2": f"List price = Net amount x 100 / (100 - {pct_str}).",
        "tier_3": f"{net_amt} x 100 / {100 - pct} = {list_price}.",
    }
    return build_short(
        rng, qid="g9_cj_11", subskill="11_calculate_original_list_price_before_trade_discount",
        title="Reverse Calculation: Original List Price Before Trade Discount",
        prompt=prompt, expected_answer=str(list_price), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Recognises {fmt_r(net_amt)} = {rem_pct}% of list price", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Calculates List Price = {fmt_r(list_price)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["reverse_percentage_added_on_net"],
        marks=3, qtype="math_short",
    )


def arch_12_calculate_implied_trade_discount_percentage(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    pct = rng.choice([5, 10, 12, 15, 20, 25])
    list_price = rng.randint(8, 30) * 200
    net_amt = list_price * (100 - pct) // 100
    disc_amt = list_price - net_amt

    prompt = (
        f"**{sup}**'s price list shows goods at **{fmt_r(list_price)}**, but the final credit invoice sent to **{biz}** "
        f"shows a net payable amount of **{fmt_r(net_amt)}**.\n\n"
        f"What **percentage trade discount** did **{sup}** grant **{biz}**? (Enter the number only, e.g. `12`.)"
    )
    worked = (
        f"**{pct}%** (`{pct}`) [3 marks]\n\n"
        f"- **Discount in Rand**: ${fmt_r(list_price)} - {fmt_r(net_amt)} = {fmt_r(disc_amt)}$ [1 mark]\n"
        f"- **Percentage**: $\\frac{{{fmt_r(disc_amt)}}}{{{fmt_r(list_price)}}} \\times 100 = {pct}\\%$ [2 marks]."
    )
    hints = {
        "tier_1": "First find how many Rand were knocked off the list price.",
        "tier_2": "Trade discount % = (Discount Rand / Original List Price) x 100.",
        "tier_3": f"({list_price} - {net_amt}) / {list_price} x 100 = {disc_amt} / {list_price} x 100 = {pct}%.",
    }
    return build_short(
        rng, qid="g9_cj_12", subskill="12_calculate_implied_trade_discount_percentage",
        title="Calculate Implied Trade Discount Percentage",
        prompt=prompt, expected_answer=str(pct), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Finds discount amount = {fmt_r(disc_amt)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Divides by list price {fmt_r(list_price)} x 100 = {pct}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["divided_discount_by_net_instead_of_list"],
        marks=3, qtype="math_short",
    )


def arch_13_split_multi_line_invoice_with_mixed_discount_and_sundries(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    sundry_acct, sundry_desc = rng.choice(SUNDRY_ITEMS)
    stock_list = rng.randint(10, 30) * 400
    disc_pct = rng.choice([5, 10, 12.5, 15])
    disc_str = f"{disc_pct}".replace(".", ",")
    net_stock = int(round(stock_list * (100 - disc_pct) / 100))
    stat_amt = rng.randint(4, 15) * 100
    sundry_amt = rng.randint(8, 25) * 200
    total_cc = net_stock + stat_amt + sundry_amt

    prompt = (
        f"**{biz}** receives a single original credit invoice from **{sup}** containing three items:\n"
        f"- Merchandise (Trading Stock): list price **{fmt_r(stock_list)}**, less **{disc_str}% trade discount**.\n"
        f"- Office Stationery: **{fmt_r(stat_amt)}** net.\n"
        f"- **{sundry_desc.capitalize()}** ({sundry_acct}): **{fmt_r(sundry_amt)}** net.\n\n"
        f"Calculate the total amount to enter in **Creditors Control** for this single invoice "
        f"(plain number, no R or spaces)."
    )
    worked = (
        f"**{fmt_r(total_cc)}** (`{total_cc}`) [4 marks]\n\n"
        f"- **Net Trading Stock**: ${fmt_r(stock_list)} - {disc_str}\\% = {fmt_r(net_stock)}$ [2 marks]\n"
        f"- **Stationery**: `{fmt_r(stat_amt)}` (net)\n"
        f"- **Sundry ({sundry_acct})**: `{fmt_r(sundry_amt)}` (net)\n"
        f"- **Total Creditors Control**: ${fmt_r(net_stock)} + {fmt_r(stat_amt)} + {fmt_r(sundry_amt)} = {fmt_r(total_cc)}$ (`{total_cc}`) [2 marks]."
    )
    hints = {
        "tier_1": f"Apply the {disc_str}% trade discount ONLY to Trading Stock, then add Stationery and {sundry_acct}.",
        "tier_2": "Creditors Control on a multi-line invoice equals the sum of all net items on that invoice.",
        "tier_3": f"Net stock = {net_stock}; + Stationery {stat_amt} + {sundry_acct} {sundry_amt} = {total_cc}.",
    }
    return build_short(
        rng, qid="g9_cj_13", subskill="13_split_multi_line_invoice_with_mixed_discount_and_sundries",
        title="Multi-Line Credit Invoice: Net Stock + Stationery + Sundry",
        prompt=prompt, expected_answer=str(total_cc), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Net Trading Stock after {disc_str}% = {fmt_r(net_stock)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Sums all three components to {fmt_r(total_cc)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["applied_discount_to_all_items", "omitted_sundry_from_creditor_total"],
        marks=4, qtype="math_short",
    )


def arch_14_cj_column_classification_stock_stationery_sundry_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    goods = rng.choice(STOCK_LINES)
    s_amt = rng.randint(14, 42) * 200
    st_amt = rng.randint(5, 16) * 100
    eq_amt = rng.randint(18, 45) * 200
    rep_amt = rng.randint(6, 18) * 150

    items = [
        (f"Bought {goods} on credit for resale", "Trading Stock", fmt_cell(s_amt), ""),
        ("Bought invoice books, printer paper & pens on credit", "Stationery", fmt_cell(st_amt), ""),
        ("Bought a steel display counter & till on credit", "Sundry Amount", fmt_cell(eq_amt), "Equipment"),
        ("Electrician repaired shop lights on 30-day credit", "Sundry Amount", fmt_cell(rep_amt), "Repairs"),
    ]
    rng.shuffle(items)

    headers = ["Credit Purchase Transaction", "CJ Analysis Column", "Amount", "Sundry Details (if Sundry)"]
    data_rows = [[desc, col, amt, det] for desc, col, amt, det in items]
    given_coords = {(r, 0) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        f"t0_r{r}_c1": "Choose 'Trading Stock', 'Stationery', or 'Sundry Amount'." for r in range(4)
    }

    prompt = (
        f"**{biz}**'s Creditors Journal has analysis columns for **Trading Stock**, **Stationery**, and **Sundry Accounts**.\n\n"
        f"Classify each credit purchase in the table below. Leave **Sundry Details** blank when an item has its own dedicated analysis column."
    )
    md_rows = "\n".join(f"| {d} | {c} | {fmt_r(int(a))} | {dt or '—'} |" for d, c, a, dt in items)
    worked = (
        f"**CJ Column Classification Table** [10 marks]\n\n"
        f"| Credit Purchase Transaction | CJ Analysis Column | Amount | Sundry Details |\n|---|---|---:|---|\n{md_rows}"
    )
    hints = {
        "tier_1": "Goods for resale -> Trading Stock; office consumables -> Stationery; assets/other expenses -> Sundry Amount.",
        "tier_2": "When entering Sundry Amount, you MUST name the account (Equipment or Repairs) in Sundry Details.",
        "tier_3": "Resale goods = Trading Stock; paper/pens = Stationery; counter/till = Sundry (Equipment); light fix = Sundry (Repairs).",
    }
    return build_table(
        rng, qid="g9_cj_14", subskill="14_cj_column_classification_stock_stationery_sundry_table",
        title="CJ Analysis Column Classification Table",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See classified CJ columns table.",
        marks=10, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Accurate CJ analysis column, amount, and Sundry Details", "marks": 10, "editable": True}],
        misconception_tags=["equipment_classified_as_trading_stock", "missing_sundry_details"],
        journal_type="cj_classification",
    )


def arch_15_cj_distinguish_credit_cj_vs_cash_cpj_routing_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    c1, c2 = [c[0] for c in pick_creditors(rng, 2)]
    a1 = rng.randint(15, 45) * 200
    a2 = rng.randint(8, 25) * 200
    a3 = rng.randint(6, 20) * 100
    a4 = rng.randint(10, 30) * 200

    cases = [
        (f"Bought trading stock on credit from {c1}, {fmt_r(a1)}", "CJ", "Original Invoice", "Creditors Control"),
        (f"Paid {c1} {fmt_r(a2)} via EFT for amount owing", "CPJ", "Bank Statement", "Bank"),
        (f"Bought office stationery via debit card for {fmt_r(a3)}", "CPJ", "Bank Statement", "Bank"),
        (f"Bought shop shelves on 60-day credit from {c2}, {fmt_r(a4)}", "CJ", "Original Invoice", "Creditors Control"),
    ]
    rng.shuffle(cases)

    headers = ["Transaction", "Journal (CJ or CPJ)", "Source Document", "Control Column"]
    data_rows = [[t, j, s, cc] for t, j, s, cc in cases]
    given_coords = {(r, 0) for r in range(4)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {f"t0_r{r}_c1": "Enter CJ (credit purchase) or CPJ (cash/EFT payment)." for r in range(4)}

    prompt = (
        f"For each transaction at **{biz}**, complete the table by identifying the **Journal (`CJ` or `CPJ`)**, "
        f"the **Source Document (`Original Invoice` or `Bank Statement`)**, and the **Control Column (`Creditors Control` or `Bank`)**."
    )
    md_rows = "\n".join(f"| {t} | {j} | {s} | {cc} |" for t, j, s, cc in cases)
    worked = (
        f"**Journal & Source Document Routing** [12 marks]\n\n"
        f"| Transaction | Journal | Source Document | Control Column |\n|---|---|---|---|\n{md_rows}"
    )
    hints = {
        "tier_1": "Buying on credit -> CJ. Paying now by EFT or card (even to a creditor!) -> CPJ.",
        "tier_2": "CJ uses Original Invoice & Creditors Control; CPJ uses Bank Statement & Bank.",
        "tier_3": "Credit purchases = CJ / Original Invoice / Creditors Control; EFT or card payment = CPJ / Bank Statement / Bank.",
    }
    return build_table(
        rng, qid="g9_cj_15", subskill="15_cj_distinguish_credit_cj_vs_cash_cpj_routing_table",
        title="Route Transactions Between CJ and CPJ",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer="See CJ vs CPJ routing table.",
        marks=12, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Correct Journal, Source Document, and Control Column for all 4 rows", "marks": 12, "editable": True}],
        misconception_tags=["eft_payment_to_creditor_put_in_cj"],
        journal_type="cj_cpj_routing",
    )


def arch_16_cj_trading_stock_and_stationery_3row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    creds = pick_creditors(rng, 3)
    days = sorted(rng.sample(range(3, 27), 3))
    inv_nums = [rng.randint(201, 299), rng.randint(410, 499), rng.randint(605, 699)]

    t1 = rng.randint(15, 40) * 200  # Trading Stock
    t2 = rng.randint(6, 18) * 100   # Stationery
    t3_ts = rng.randint(12, 30) * 200
    t3_st = rng.randint(4, 12) * 100
    t3 = t3_ts + t3_st

    tot_cc = t1 + t2 + t3
    tot_ts = t1 + t3_ts
    tot_st = t2 + t3_st

    tx_list = [
        f"{month} {days[0]}: Received original invoice #{inv_nums[0]} from {creds[0][0]} for trading stock purchased on credit, {fmt_r(t1)} (renumber C1).",
        f"{month} {days[1]}: Bought stationery on credit from {creds[1][0]}, original invoice #{inv_nums[1]}, {fmt_r(t2)} (renumber C2).",
        f"{month} {days[2]}: Received original invoice #{inv_nums[2]} from {creds[2][0]} for trading stock {fmt_r(t3_ts)} and office stationery {fmt_r(t3_st)} on credit (renumber C3).",
    ]

    data_rows = [
        ["C1", str(days[0]), creds[0][0], "C1", fmt_cell(t1), fmt_cell(t1), "", "", ""],
        ["C2", str(days[1]), creds[1][0], "C2", fmt_cell(t2), "", fmt_cell(t2), "", ""],
        ["C3", str(days[2]), creds[2][0], "C3", fmt_cell(t3), fmt_cell(t3_ts), fmt_cell(t3_st), "", ""],
        ["", "", "Totals", "", fmt_cell(tot_cc), fmt_cell(tot_ts), fmt_cell(tot_st), "0", ""],
    ]
    given_coords = {(r, 0) for r in range(3)} | {(r, 1) for r in range(3)} | {(r, 3) for r in range(3)} | {(3, 2)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        "t0_r2_c4": "Add Trading Stock + Stationery on the same invoice for total Creditors Control.",
        "t0_r3_c4": "Sum all Creditors Control entries; verify it equals Trading Stock + Stationery totals.",
    }

    prompt = (
        f"Record the following credit transactions for **{month} {year}** in the **Creditors Journal (CJ)** of **{biz}**, "
        f"and total all columns.\n\n"
        + "\n".join(f"- {t}" for t in tx_list)
        + "\n\nEnter numeric amounts without `R` or spaces; leave unused cells blank."
    )
    worked = (
        f"**Creditors Journal of {biz} — {month} {year}** [12 marks]\n\n"
        "| Doc No | Day | Creditor | Fol | Creditors Control | Trading Stock | Stationery | Sundry Amount | Sundry Details |\n"
        "|---|---:|---|---|---:|---:|---:|---:|---|\n"
        f"| C1 | {days[0]} | {creds[0][0]} | C1 | {fmt_cell(t1)} | {fmt_cell(t1)} | | | |\n"
        f"| C2 | {days[1]} | {creds[1][0]} | C2 | {fmt_cell(t2)} | | {fmt_cell(t2)} | | |\n"
        f"| C3 | {days[2]} | {creds[2][0]} | C3 | {fmt_cell(t3)} | {fmt_cell(t3_ts)} | {fmt_cell(t3_st)} | | |\n"
        f"| | | **Totals** | | **{fmt_cell(tot_cc)}** | **{fmt_cell(tot_ts)}** | **{fmt_cell(tot_st)}** | **0** | |\n\n"
        f"- **Cross-check**: ${tot_ts} + {tot_st} = {tot_cc}$."
    )
    hints = {
        "tier_1": "Enter each invoice in Creditors Control first, then split across Trading Stock and Stationery.",
        "tier_2": "Row 3 has BOTH Trading Stock and Stationery on one invoice: Creditors Control = their sum.",
        "tier_3": f"Totals: Creditors Control = {tot_cc}, Trading Stock = {tot_ts}, Stationery = {tot_st}.",
    }
    return build_table(
        rng, qid="g9_cj_16", subskill="16_cj_trading_stock_and_stationery_3row_table",
        title="Complete 3-Row CJ (Trading Stock & Stationery)",
        prompt=prompt, headers=CJ_HEADERS, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total Creditors Control = {fmt_r(tot_cc)}.",
        marks=12, hints=hints, transactions=tx_list,
        marking_points=[{"id": "mp_1", "desc": "Accurately records all 3 invoices and Totals row", "marks": 12, "editable": True}],
        misconception_tags=["omitted_combined_total_on_c3", "cross_cast_error"],
        journal_type="cj",
    )


def arch_17_cj_complete_with_sundry_accounts_and_trade_discount_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    creds = pick_creditors(rng, 4)
    days = sorted(rng.sample(range(2, 28), 4))
    disc1 = rng.choice([5, 10, 12.5])
    disc1_str = f"{disc1}".replace(".", ",")

    r1_list = rng.randint(12, 30) * 400
    r1_net = int(round(r1_list * (100 - disc1) / 100))

    r2_amt = rng.randint(8, 22) * 200  # Equipment (Sundry)

    r3_ts = rng.randint(10, 26) * 200
    r3_st = rng.randint(5, 14) * 100
    r3_cc = r3_ts + r3_st

    r4_list = rng.randint(6, 16) * 200
    r4_disc = rng.choice([5, 10])
    r4_net = r4_list * (100 - r4_disc) // 100

    tot_cc = r1_net + r2_amt + r3_cc + r4_net
    tot_ts = r1_net + r3_ts
    tot_st = r3_st
    tot_sun = r2_amt + r4_net

    tx_list = [
        f"Day {days[0]}: Received original invoice from {creds[0][0]} (C1) for trading stock, catalogue price {fmt_r(r1_list)} less {disc1_str}% trade discount.",
        f"Day {days[1]}: Bought shop display shelving on credit from {creds[1][0]} (C2) for {fmt_r(r2_amt)}.",
        f"Day {days[2]}: Bought trading stock ({fmt_r(r3_ts)}) and office stationery ({fmt_r(r3_st)}) on credit from {creds[2][0]} (C3).",
        f"Day {days[3]}: Bought printed packing material on credit from {creds[3][0]} (C4), list price {fmt_r(r4_list)} less {r4_disc}% trade discount.",
    ]

    data_rows = [
        ["C1", str(days[0]), creds[0][0], "C1", fmt_cell(r1_net), fmt_cell(r1_net), "", "", ""],
        ["C2", str(days[1]), creds[1][0], "C2", fmt_cell(r2_amt), "", "", fmt_cell(r2_amt), "Equipment"],
        ["C3", str(days[2]), creds[2][0], "C3", fmt_cell(r3_cc), fmt_cell(r3_ts), fmt_cell(r3_st), "", ""],
        ["C4", str(days[3]), creds[3][0], "C4", fmt_cell(r4_net), "", "", fmt_cell(r4_net), "Packing material"],
        ["", "", "Totals", "", fmt_cell(tot_cc), fmt_cell(tot_ts), fmt_cell(tot_st), fmt_cell(tot_sun), ""],
    ]
    given_coords = {(r, 0) for r in range(4)} | {(r, 1) for r in range(4)} | {(r, 3) for r in range(4)} | {(4, 2)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        "t0_r0_c4": f"Deduct {disc1_str}% trade discount from {fmt_r(r1_list)} before entering.",
        "t0_r1_c8": "Display shelving is an asset -> Equipment.",
        "t0_r3_c8": f"Packing material goes to Sundry Accounts after subtracting {r4_disc}%.",
    }

    prompt = (
        f"Complete the **Creditors Journal (CJ)** of **{biz}** for **{month} {year}** from the transactions below, "
        f"including all column totals. Enter amounts as plain numbers (no `R` or spaces) and leave unused cells empty.\n\n"
        + "\n".join(f"- {t}" for t in tx_list)
    )
    worked = (
        f"**Creditors Journal of {biz} — {month} {year}** [18 marks]\n\n"
        f"- **C1 Net Stock**: ${fmt_r(r1_list)} - {disc1_str}\\% = {fmt_r(r1_net)}$\n"
        f"- **C4 Net Packing material**: ${fmt_r(r4_list)} - {r4_disc}\\% = {fmt_r(r4_net)}$\n\n"
        "| Doc No | Day | Creditor | Fol | Creditors Control | Trading Stock | Stationery | Sundry Amount | Sundry Details |\n"
        "|---|---:|---|---|---:|---:|---:|---:|---|\n"
        f"| C1 | {days[0]} | {creds[0][0]} | C1 | {fmt_cell(r1_net)} | {fmt_cell(r1_net)} | | | |\n"
        f"| C2 | {days[1]} | {creds[1][0]} | C2 | {fmt_cell(r2_amt)} | | | {fmt_cell(r2_amt)} | Equipment |\n"
        f"| C3 | {days[2]} | {creds[2][0]} | C3 | {fmt_cell(r3_cc)} | {fmt_cell(r3_ts)} | {fmt_cell(r3_st)} | | |\n"
        f"| C4 | {days[3]} | {creds[3][0]} | C4 | {fmt_cell(r4_net)} | | | {fmt_cell(r4_net)} | Packing material |\n"
        f"| | | **Totals** | | **{fmt_cell(tot_cc)}** | **{fmt_cell(tot_ts)}** | **{fmt_cell(tot_st)}** | **{fmt_cell(tot_sun)}** | |\n\n"
        f"- **Cross-check**: ${tot_ts} + {tot_st} + {tot_sun} = {tot_cc}$."
    )
    hints = {
        "tier_1": "Apply trade discounts first, then route Trading Stock, Stationery, or Sundry Accounts (Equipment / Packing material).",
        "tier_2": "Verify that Trading Stock + Stationery + Sundry Amount totals equal Creditors Control total.",
        "tier_3": f"C1={r1_net}, C2={r2_amt} (Equipment), C3={r3_cc} ({r3_ts}+{r3_st}), C4={r4_net} (Packing material). Total CC = {tot_cc}.",
    }
    return build_table(
        rng, qid="g9_cj_17", subskill="17_cj_complete_with_sundry_accounts_and_trade_discount_table",
        title="Full Creditors Journal with Trade Discounts & Sundry Accounts",
        prompt=prompt, headers=CJ_HEADERS, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total Creditors Control = {fmt_r(tot_cc)}.",
        marks=18, hints=hints, transactions=tx_list,
        marking_points=[
            {"id": "mp_1", "desc": "Applies trade discounts on C1 and C4 accurately", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": "Routes Equipment and Packing material to Sundry Accounts", "marks": 6, "editable": True},
            {"id": "mp_3", "desc": "Balances Creditors Control total against analysis + Sundry columns", "marks": 8, "editable": True},
        ],
        misconception_tags=["trade_discount_not_deducted", "equipment_in_trading_stock", "cj_cross_cast_error"],
        journal_type="cj",
    )


def arch_18_cj_multi_item_single_invoice_split_rows_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    sup, _ = rng.choice(CREDITOR_POOL)
    day = rng.randint(5, 22)
    doc = f"C{rng.randint(1, 5)}"
    ts_amt = rng.randint(15, 40) * 200
    eq_amt = rng.randint(10, 28) * 200
    rep_amt = rng.randint(4, 12) * 150
    total_inv = ts_amt + eq_amt + rep_amt

    tx_list = [
        f"{month} {day} ({doc}): Received ONE combined original invoice from {sup} for trading stock {fmt_r(ts_amt)}, "
        f"new office printer (Equipment) {fmt_r(eq_amt)}, and shop counter repairs {fmt_r(rep_amt)}."
    ]
    data_rows = [
        [doc, str(day), sup, "C1", fmt_cell(total_inv), fmt_cell(ts_amt), "", fmt_cell(eq_amt), "Equipment"],
        ["", "", "", "", "", "", "", fmt_cell(rep_amt), "Repairs"],
        ["", "", "Totals", "", fmt_cell(total_inv), fmt_cell(ts_amt), "0", fmt_cell(eq_amt + rep_amt), ""],
    ]
    given_coords = {(0, 0), (0, 1), (0, 2), (0, 3), (2, 2)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        "t0_r0_c4": "Enter the full invoice total on line 1 ONLY (do not split Creditors Control).",
        "t0_r1_c4": "Leave Creditors Control blank on line 2 of the same invoice.",
        "t0_r1_c7": "Enter the second sundry item (Repairs) on line 2.",
    }

    prompt = (
        f"Record the single combined credit invoice below into the **Creditors Journal (CJ)** of **{biz}** for **{month} {year}**.\n\n"
        f"- {tx_list[0]}\n\n"
        f"Because there are **two different Sundry Accounts** (`Equipment` and `Repairs`) on one invoice, "
        f"enter the full **Creditors Control** total on Row 1 and place the second Sundry item on Row 2 (leaving Row 2 Doc No, Day, Creditor, Fol, and Creditors Control blank)."
    )
    worked = (
        f"**Multi-Line Sundry Invoice in CJ ({doc})** [10 marks]\n\n"
        "| Doc No | Day | Creditor | Fol | Creditors Control | Trading Stock | Stationery | Sundry Amount | Sundry Details |\n"
        "|---|---:|---|---|---:|---:|---:|---:|---|\n"
        f"| {doc} | {day} | {sup} | C1 | {fmt_cell(total_inv)} | {fmt_cell(ts_amt)} | | {fmt_cell(eq_amt)} | Equipment |\n"
        f"| | | | | | | | {fmt_cell(rep_amt)} | Repairs |\n"
        f"| | | **Totals** | | **{fmt_cell(total_inv)}** | **{fmt_cell(ts_amt)}** | **0** | **{fmt_cell(eq_amt + rep_amt)}** | |\n\n"
        f"- **Check**: ${ts_amt} + {eq_amt + rep_amt} = {total_inv}$."
    )
    hints = {
        "tier_1": "Creditors Control holds the total owed on the invoice once (Row 1), never repeated on Row 2.",
        "tier_2": "Line 1: Full Creditors Control + Trading Stock + Equipment. Line 2: Repairs only.",
        "tier_3": f"Row 1 CC = {total_inv}, TS = {ts_amt}, Sundry = {eq_amt} Equipment; Row 2 Sundry = {rep_amt} Repairs.",
    }
    return build_table(
        rng, qid="g9_cj_18", subskill="18_cj_multi_item_single_invoice_split_rows_table",
        title="Split Two Sundry Items on One CJ Invoice",
        prompt=prompt, headers=CJ_HEADERS, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total Creditors Control = {fmt_r(total_inv)}.",
        marks=10, hints=hints, transactions=tx_list,
        marking_points=[{"id": "mp_1", "desc": "Correctly enters total CC on row 1 and second sundry item on row 2", "marks": 10, "editable": True}],
        misconception_tags=["repeated_creditors_control_on_second_line"],
        journal_type="cj",
    )


def arch_19_cj_exclude_personal_drawings_or_cash_purchases_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    month, year, _ = rng.choice(MONTH_DATA)
    creds = pick_creditors(rng, 4)
    days = sorted(rng.sample(range(3, 27), 4))

    a1 = rng.randint(15, 42) * 200
    a_skip = rng.randint(8, 24) * 100
    a2 = rng.randint(6, 16) * 100
    a3 = rng.randint(12, 32) * 200

    skip_reason = rng.choice([
        f"Paid {creds[1][0]} {fmt_r(a_skip)} immediately by EFT for consumables (cash payment).",
        f"Owner {sc['entrepreneur']} bought a personal microwave for home on credit using {biz}'s order form ({fmt_r(a_skip)} — private drawings/personal, excluded from business CJ).",
    ])
    tx_list = [
        f"Day {days[0]}: Bought trading stock on credit from {creds[0][0]}, {fmt_r(a1)} (C1).",
        f"Day {days[1]}: {skip_reason}",
        f"Day {days[2]}: Bought stationery on credit from {creds[2][0]}, {fmt_r(a2)} (C2).",
        f"Day {days[3]}: Bought a delivery trolley (Equipment) on credit from {creds[3][0]}, {fmt_r(a3)} (C3).",
    ]

    tot_cc = a1 + a2 + a3
    data_rows = [
        ["C1", str(days[0]), creds[0][0], "C1", fmt_cell(a1), fmt_cell(a1), "", "", ""],
        ["C2", str(days[2]), creds[2][0], "C2", fmt_cell(a2), "", fmt_cell(a2), "", ""],
        ["C3", str(days[3]), creds[3][0], "C3", fmt_cell(a3), "", "", fmt_cell(a3), "Equipment"],
        ["", "", "Totals", "", fmt_cell(tot_cc), fmt_cell(a1), fmt_cell(a2), fmt_cell(a3), ""],
    ]
    given_coords = {(r, 0) for r in range(3)} | {(r, 3) for r in range(3)} | {(3, 2)}
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {"t0_r1_c1": f"Skip Day {days[1]}! Enter Day {days[2]} on row C2."}

    prompt = (
        f"Only **3** of the 4 transactions below qualify for **{biz}**'s **Creditors Journal (CJ)** in **{month} {year}**.\n\n"
        + "\n".join(f"- {t}" for t in tx_list)
        + "\n\nFilter out the non-CJ item and record ONLY the 3 qualifying credit purchases (plus Totals)."
    )
    worked = (
        f"**Filtered Creditors Journal of {biz} — {month} {year}** [14 marks]\n\n"
        f"- **Excluded**: Day {days[1]} ({fmt_r(a_skip)}) does not belong in the CJ.\n\n"
        "| Doc No | Day | Creditor | Fol | Creditors Control | Trading Stock | Stationery | Sundry Amount | Sundry Details |\n"
        "|---|---:|---|---|---:|---:|---:|---:|---|\n"
        f"| C1 | {days[0]} | {creds[0][0]} | C1 | {fmt_cell(a1)} | {fmt_cell(a1)} | | | |\n"
        f"| C2 | {days[2]} | {creds[2][0]} | C2 | {fmt_cell(a2)} | | {fmt_cell(a2)} | | |\n"
        f"| C3 | {days[3]} | {creds[3][0]} | C3 | {fmt_cell(a3)} | | | {fmt_cell(a3)} | Equipment |\n"
        f"| | | **Totals** | | **{fmt_cell(tot_cc)}** | **{fmt_cell(a1)}** | **{fmt_cell(a2)}** | **{fmt_cell(a3)}** | |"
    )
    hints = {
        "tier_1": "Check Day 2 carefully: is it a valid business credit purchase?",
        "tier_2": "Exclude cash/EFT purchases (CPJ) and private/personal purchases; enter only C1, C2, and C3.",
        "tier_3": f"Omit Day {days[1]} ({fmt_r(a_skip)}). Total CC = {a1} + {a2} + {a3} = {tot_cc}.",
    }
    return build_table(
        rng, qid="g9_cj_19", subskill="19_cj_exclude_personal_drawings_or_cash_purchases_table",
        title="Exclude Cash or Non-Business Transactions from CJ",
        prompt=prompt, headers=CJ_HEADERS, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total Creditors Control = {fmt_r(tot_cc)}.",
        marks=14, hints=hints, transactions=tx_list,
        marking_points=[{"id": "mp_1", "desc": f"Excludes Day {days[1]} and enters valid 3 entries", "marks": 14, "editable": True}],
        misconception_tags=["recorded_cash_or_personal_item_in_cj"],
        journal_type="cj",
    )


def arch_20_cj_cross_check_horizontal_and_vertical_totals_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    creds = pick_creditors(rng, 3)

    r1_ts = rng.randint(15, 35) * 200
    r2_ts = rng.randint(10, 25) * 200
    r2_st = rng.randint(5, 14) * 100
    r2_cc = r2_ts + r2_st
    r3_sun = rng.randint(12, 30) * 200

    tot_ts = r1_ts + r2_ts
    tot_st = r2_st
    tot_sun = r3_sun
    tot_cc = tot_ts + tot_st + tot_sun

    headers = ["Doc No", "Creditor", "Creditors Control", "Trading Stock", "Stationery", "Sundry Amount", "Sundry Details"]
    data_rows = [
        ["C1", creds[0][0], fmt_cell(r1_ts), fmt_cell(r1_ts), "", "", ""],
        ["C2", creds[1][0], fmt_cell(r2_cc), fmt_cell(r2_ts), fmt_cell(r2_st), "", ""],
        ["C3", creds[2][0], fmt_cell(r3_sun), "", "", fmt_cell(r3_sun), "Equipment"],
        ["", "Totals", fmt_cell(tot_cc), fmt_cell(tot_ts), fmt_cell(tot_st), fmt_cell(tot_sun), ""],
    ]
    # Leave strategic missing amounts and total cells blank for student to solve
    given_coords = {
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 3), (1, 4),
        (2, 0), (2, 1), (2, 5), (2, 6),
        (3, 1),
    }
    rows, cmap = make_grid_rows(data_rows, given_coords)
    cell_hints = {
        "t0_r0_c3": "C1 has only one item, so Trading Stock equals Creditors Control.",
        "t0_r1_c2": "Add Trading Stock + Stationery on row C2.",
        "t0_r3_c2": "Sum vertically AND cross-check horizontally: Trading Stock + Stationery + Sundry Amount.",
    }

    prompt = (
        f"The **Creditors Journal** excerpt below for **{biz}** has missing figures and missing column totals.\n\n"
        f"Use the horizontal and vertical cross-cast rules of the CJ to complete every empty numeric cell."
    )
    worked = (
        f"**Completed & Cross-Checked CJ Excerpt for {biz}** [10 marks]\n\n"
        "| Doc No | Creditor | Creditors Control | Trading Stock | Stationery | Sundry Amount | Sundry Details |\n"
        "|---|---|---:|---:|---:|---:|---|\n"
        f"| C1 | {creds[0][0]} | {fmt_cell(r1_ts)} | {fmt_cell(r1_ts)} | | | |\n"
        f"| C2 | {creds[1][0]} | {fmt_cell(r2_cc)} | {fmt_cell(r2_ts)} | {fmt_cell(r2_st)} | | |\n"
        f"| C3 | {creds[2][0]} | {fmt_cell(r3_sun)} | | | {fmt_cell(r3_sun)} | Equipment |\n"
        f"| | **Totals** | **{fmt_cell(tot_cc)}** | **{fmt_cell(tot_ts)}** | **{fmt_cell(tot_st)}** | **{fmt_cell(tot_sun)}** | |\n\n"
        f"- **Cross-check**: ${tot_ts} + {tot_st} + {tot_sun} = {tot_cc}$."
    )
    hints = {
        "tier_1": "Each row balances horizontally, and the Totals row balances both vertically and horizontally.",
        "tier_2": "Creditors Control Total = Trading Stock Total + Stationery Total + Sundry Amount Total.",
        "tier_3": f"C1 TS={r1_ts}, C2 CC={r2_cc}, C3 CC={r3_sun}; Totals: CC={tot_cc}, TS={tot_ts}, Stat={tot_st}, Sundry={tot_sun}.",
    }
    return build_table(
        rng, qid="g9_cj_20", subskill="20_cj_cross_check_horizontal_and_vertical_totals_table",
        title="Cross-Check & Complete Missing CJ Figures",
        prompt=prompt, headers=headers, rows=rows, correct_map=cmap, cell_hints=cell_hints,
        worked_solution=worked, sample_answer=f"Total Creditors Control = {fmt_r(tot_cc)}.",
        marks=10, hints=hints,
        marking_points=[{"id": "mp_1", "desc": "Solves all missing row cells and balances CJ Totals", "marks": 10, "editable": True}],
        misconception_tags=["cj_horizontal_balancing_error"],
        journal_type="cj",
    )


def arch_21_cj_find_missing_sundry_amount_from_totals_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    ts_tot = rng.randint(45, 95) * 200
    st_tot = rng.randint(12, 32) * 100
    sun_tot = rng.randint(18, 48) * 200
    cc_tot = ts_tot + st_tot + sun_tot

    prompt = (
        f"At month-end, **{biz}**'s **Creditors Journal** shows these totals:\n"
        f"- **Creditors Control**: {fmt_r(cc_tot)}\n"
        f"- **Trading Stock**: {fmt_r(ts_tot)}\n"
        f"- **Stationery**: {fmt_r(st_tot)}\n"
        f"- **Sundry Accounts**: **?** (missing due to ink smudge)\n\n"
        f"Calculate the missing **Sundry Accounts** total (plain number, no R or spaces)."
    )
    worked = (
        f"**{fmt_r(sun_tot)}** (`{sun_tot}`) [3 marks]\n\n"
        f"- **CJ Cross-Cast Equation**: "
        f"$\\text{{Creditors Control}} = \\text{{Trading Stock}} + \\text{{Stationery}} + \\text{{Sundry Accounts}}$\n"
        f"- $\\text{{Sundry Accounts}} = {fmt_r(cc_tot)} - ({fmt_r(ts_tot)} + {fmt_r(st_tot)}) = {fmt_r(cc_tot)} - {fmt_r(ts_tot + st_tot)} = {fmt_r(sun_tot)}$ (`{sun_tot}`) [3 marks]."
    )
    hints = {
        "tier_1": "Creditors Control equals the sum of all analysis columns plus Sundry Accounts.",
        "tier_2": "Sundry Accounts = Creditors Control - Trading Stock - Stationery.",
        "tier_3": f"{cc_tot} - {ts_tot} - {st_tot} = {sun_tot}.",
    }
    return build_short(
        rng, qid="g9_cj_21", subskill="21_cj_find_missing_sundry_amount_from_totals_calc",
        title="Recover Missing Sundry Total via CJ Cross-Cast",
        prompt=prompt, expected_answer=str(sun_tot), worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts Trading Stock + Stationery from Creditors Control = {sun_tot}", "marks": 3, "editable": True}
        ],
        misconception_tags=["added_totals_instead_of_subtracting"],
        marks=3, qtype="math_short",
    )


def arch_22_creditors_allowance_definition_and_reasons(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    goods = rng.choice(STOCK_LINES)
    amt = rng.randint(4, 18) * 200
    reason = rng.choice([
        "several cartons arrived water-damaged",
        "the wrong sizes were packed and delivered",
        f"{sup} overcharged the unit price on the invoice",
    ])

    prompt = (
        f"**{biz}** bought **{goods}** on credit from **{sup}**, then discovered that **{reason}** "
        f"and claims a price reduction/return of **{fmt_r(amt)}**.\n\n"
        f"What is this adjustment called, and how does it affect the business's books?"
    )
    correct = (
        f"A Creditors Allowance (recorded in the CAJ), which reduces {biz}'s liability owed to {sup} by {fmt_r(amt)}."
    )
    distractors = [
        f"A Debtors Allowance (recorded in the DAJ), which increases the cash {biz} receives from {sup}.",
        f"A Cash Refund (recorded in the CRJ), because {sup} always pays cash back for credit returns.",
        f"An extra credit purchase in the CJ, increasing {biz}'s debt to {sup} by {fmt_r(amt)}.",
    ]
    explanation = (
        f"- When a business returns goods bought on credit or receives an overcharge rebate, it is a **Creditors Allowance**.\n"
        f"- It is recorded in the **Creditors Allowance Journal (CAJ)** and **reduces** what {biz} owes **{sup}** (**Creditors Control decreases**)."
    )
    hints = {
        "tier_1": "Because the original purchase was on credit from a creditor, the return reduces what is owed.",
        "tier_2": "Returns/allowances to suppliers go into the Creditors Allowance Journal (CAJ).",
        "tier_3": f"Creditors Allowance -> CAJ -> reduces Creditors Control owed to {sup} by {fmt_r(amt)}.",
    }
    return build_mcq(
        rng, qid="g9_cj_22", subskill="22_creditors_allowance_definition_and_reasons",
        title="Creditors Allowance: Purpose & Effect on Liability",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["debtors_vs_creditors_allowance_confusion"],
    )


def arch_23_debit_note_source_document_card_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    month, year, _ = rng.choice(MONTH_DATA)
    day = rng.randint(8, 26)
    dn_no = f"DN{rng.randint(11, 29)}"
    orig_c = f"C{rng.randint(1, 4)}"
    gross_ret = rng.randint(6, 20) * 200
    disc_pct = rng.choice([5, 10, 15])
    net_ret = gross_ret * (100 - disc_pct) // 100
    date_str = f"{day} {month} {year}"

    svg = source_doc_svg(
        header_title=f"DEBIT NOTE - ISSUED BY {biz.upper()}",
        doc_no=dn_no,
        date_str=date_str,
        lines=[
            ("To (Creditor)", sup),
            ("Original Invoice Ref", orig_c),
            ("Reason for Claim", "Damaged trading stock returned to supplier"),
            ("Gross Return Value", fmt_r(gross_ret)),
            ("Less Original Trade Discount", f"{disc_pct}% (-{fmt_r(gross_ret - net_ret)})"),
            ("Net Allowance Claimed", fmt_r(net_ret)),
        ],
        accent="#b45309",
    )
    diagram_spec = {
        "kind": "inline_svg",
        "svg": svg,
        "title": f"Debit Note {dn_no} issued by {biz}",
        "diagram_role": "context",
    }

    prompt = (
        f"Inspect **Debit Note {dn_no}** issued by **{biz}** to **{sup}** on **{date_str}**.\n\n"
        f"State the **Journal (`CJ` or `CAJ`)** where {biz} records this document and the **net allowance amount** "
        f"(plain digits, no R or spaces), separated by a comma (e.g. `CAJ, 1800`)."
    )
    expected = f"CAJ, {net_ret}"
    worked = (
        f"**{expected}** [3 marks]\n\n"
        f"1. **Journal**: A **Debit Note** issued for returned credit stock goes into the **`CAJ`** (Creditors Allowance Journal) [1 mark].\n"
        f"2. **Net Amount**: Returns must use the **same net price** after the original `{disc_pct}%` trade discount: "
        f"${fmt_r(gross_ret)} - {disc_pct}\\% = {fmt_r(net_ret)}$ (`{net_ret}`) [2 marks]."
    )
    hints = {
        "tier_1": "Debit Notes belong to returns/allowances to creditors. Check the net amount after trade discount.",
        "tier_2": "Debit Note -> Creditors Allowance Journal (CAJ); deduct the original trade discount on returned stock.",
        "tier_3": f"CAJ, {gross_ret} - {gross_ret * disc_pct // 100} = {net_ret}.",
    }
    return build_short(
        rng, qid="g9_cj_23", subskill="23_debit_note_source_document_card_svg",
        title="Read a Debit Note & Extract CAJ Entry",
        prompt=prompt, expected_answer=expected, worked_solution=worked, hints=hints,
        marking_points=[
            {"id": "mp_1", "desc": "Identifies CAJ as journal for Debit Note", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Uses net allowance amount {net_ret} after {disc_pct}% discount", "marks": 2, "editable": True},
        ],
        misconception_tags=["debit_note_entered_in_cj", "used_gross_return_instead_of_net"],
        marks=3, qtype="short_text", diagram_spec=diagram_spec,
    )


def arch_24_why_document_is_called_debit_note_caj(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    amt = rng.randint(5, 18) * 100

    prompt = (
        f"When **{biz}** returns faulty stock worth **{fmt_r(amt)}** to **{sup}**, {biz} issues a **Debit Note**.\n\n"
        f"Why is this source document called a **Debit Note** rather than a Credit Note in **{biz}**'s books?"
    )
    correct = (
        f"Because {sup}'s account is a Liability with a Credit balance; returning stock reduces the liability, "
        f"so {biz} must DEBIT {sup}'s account by {fmt_r(amt)}."
    )
    distractors = [
        f"Because {biz}'s Bank account increases by {fmt_r(amt)} (Bank is debited) when returning stock.",
        f"Because Trading Stock is debited whenever faulty goods leave the shop floor.",
        f"Because {sup} owes {biz} cash immediately and becomes an Expense in the General Ledger.",
    ]
    explanation = (
        f"- **Liabilities increase on the Credit side (`+`) and decrease on the Debit side (`-`)**.\n"
        f"- Returning stock reduces what {biz} owes **{sup}**, so {biz} **debits** {sup}'s account (`-{fmt_r(amt)}` Liability) "
        f"— hence **{biz}** sends a **Debit Note** to notify {sup} that their account is being debited."
    )
    hints = {
        "tier_1": "Think of the double-entry side (Debit or Credit) that REDUCES a Creditor (Liability) account.",
        "tier_2": "Creditors have Credit balances. To decrease what you owe a creditor, you DEBIT their account.",
        "tier_3": f"Debiting {sup}'s creditor account reduces {biz}'s debt by {fmt_r(amt)}, so it is a Debit Note.",
    }
    return build_mcq(
        rng, qid="g9_cj_24", subskill="24_why_document_is_called_debit_note_caj",
        title="Why Buyers Issue a Debit Note for Creditors Allowances",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["debit_vs_credit_note_logic_unknown"],
    )


def arch_25_debit_note_vs_credit_note_perspective_comparison(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    buyer = biz_name(rng, sc)
    sup, _ = rng.choice(CREDITOR_POOL)
    amt = rng.randint(6, 22) * 100

    prompt = (
        f"**{buyer}** returns damaged stock worth **{fmt_r(amt)}** bought on credit from **{sup}**, "
        f"and **{sup}** accepts the return.\n\n"
        f"Which source document and journal pair applies to **each business**?"
    )
    correct = (
        f"{buyer} (buyer) issues an Original/Duplicate Debit Note for its CAJ; "
        f"{sup} (supplier) issues a Credit Note for its Debtors Allowance Journal (DAJ)."
    )
    distractors = [
        f"{buyer} issues a Credit Note for its DAJ; {sup} records a Debit Note in its CAJ.",
        "Both businesses issue a Credit Note and enter the return in the Creditors Journal (CJ).",
        f"{buyer} waits for an Original Invoice from {sup} and enters it as negative cash in the CPJ.",
    ]
    explanation = (
        f"- **Buyer ({buyer})**: reduces its Creditor -> issues a **Debit Note** -> enters in **CAJ**.\n"
        f"- **Supplier ({sup})**: reduces its Debtor -> issues a **Credit Note** -> enters in **DAJ**."
    )
    hints = {
        "tier_1": "Match Buyer -> Creditor -> Debit Note -> CAJ, and Supplier -> Debtor -> Credit Note -> DAJ.",
        "tier_2": "A buyer's Debit Note matches the supplier's Credit Note for the same return.",
        "tier_3": f"{buyer}: Debit Note (CAJ). {sup}: Credit Note (DAJ).",
    }
    return build_mcq(
        rng, qid="g9_cj_25", subskill="25_debit_note_vs_credit_note_perspective_comparison",
        title="Debit Note (CAJ) vs Credit Note (DAJ) Perspective",
        prompt=prompt, correct_text=correct, distractors=distractors,
        explanation=explanation, hints=hints,
        misconception_tags=["debit_note_vs_credit_note_swapped"],
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_creditor_definition_current_liability_role": arch_01_creditor_definition_current_liability_role,
    "02_debtor_vs_creditor_perspective_comparison": arch_02_debtor_vs_creditor_perspective_comparison,
    "03_creditors_accounting_cycle_step_sequence": arch_03_creditors_accounting_cycle_step_sequence,
    "04_original_invoice_renumbering_rule_cj": arch_04_original_invoice_renumbering_rule_cj,
    "05_source_document_card_original_invoice_svg": arch_05_source_document_card_original_invoice_svg,
    "06_creditors_journal_purpose_and_cash_exclusions": arch_06_creditors_journal_purpose_and_cash_exclusions,
    "07_cj_vs_cpj_bank_vs_creditors_control_comparison": arch_07_cj_vs_cpj_bank_vs_creditors_control_comparison,
    "08_analysis_columns_selection_by_business_type": arch_08_analysis_columns_selection_by_business_type,
    "09_trade_discount_definition_and_purpose": arch_09_trade_discount_definition_and_purpose,
    "10_calculate_net_invoice_single_trade_discount": arch_10_calculate_net_invoice_single_trade_discount,
    "11_calculate_original_list_price_before_trade_discount": arch_11_calculate_original_list_price_before_trade_discount,
    "12_calculate_implied_trade_discount_percentage": arch_12_calculate_implied_trade_discount_percentage,
    "13_split_multi_line_invoice_with_mixed_discount_and_sundries": arch_13_split_multi_line_invoice_with_mixed_discount_and_sundries,
    "14_cj_column_classification_stock_stationery_sundry_table": arch_14_cj_column_classification_stock_stationery_sundry_table,
    "15_cj_distinguish_credit_cj_vs_cash_cpj_routing_table": arch_15_cj_distinguish_credit_cj_vs_cash_cpj_routing_table,
    "16_cj_trading_stock_and_stationery_3row_table": arch_16_cj_trading_stock_and_stationery_3row_table,
    "17_cj_complete_with_sundry_accounts_and_trade_discount_table": arch_17_cj_complete_with_sundry_accounts_and_trade_discount_table,
    "18_cj_multi_item_single_invoice_split_rows_table": arch_18_cj_multi_item_single_invoice_split_rows_table,
    "19_cj_exclude_personal_drawings_or_cash_purchases_table": arch_19_cj_exclude_personal_drawings_or_cash_purchases_table,
    "20_cj_cross_check_horizontal_and_vertical_totals_table": arch_20_cj_cross_check_horizontal_and_vertical_totals_table,
    "21_cj_find_missing_sundry_amount_from_totals_calc": arch_21_cj_find_missing_sundry_amount_from_totals_calc,
    "22_creditors_allowance_definition_and_reasons": arch_22_creditors_allowance_definition_and_reasons,
    "23_debit_note_source_document_card_svg": arch_23_debit_note_source_document_card_svg,
    "24_why_document_is_called_debit_note_caj": arch_24_why_document_is_called_debit_note_caj,
    "25_debit_note_vs_credit_note_perspective_comparison": arch_25_debit_note_vs_credit_note_perspective_comparison,
}
