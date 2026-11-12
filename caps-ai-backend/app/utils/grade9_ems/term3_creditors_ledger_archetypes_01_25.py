"""Grade 9 EMS — Credit Transactions (Creditors 2): Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards (Term 3: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Creditors 2).md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.ems_namelist import AREAS, NAMES

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_creditors_ledger"
TOPIC_NAME = "Credit transactions (Creditors 2)"
CURRICULUM_REF = "Term 3 > Financial Literacy: Credit Transactions (Creditors 2)"
SUPPLIER_NAMES = [
    "EMS Suppliers",
    "Makro Wholesalers",
    "Neverland Suppliers",
    "PaperCo Stationers",
    "Mega Wholesalers",
    "Sunrise Distributors",
]
TRADER_NAMES = [
    "Chelsea Traders",
    "Huguenot All Sorts",
    "Serotonin Traders",
    "Thierry's Furnishers",
    "Kalahari Retailers",
    "Karoo Supplies",
]


def _fmt_zar(amount: float, decimals: int = 0) -> str:
    if decimals == 0 and float(amount).is_integer():
        return f"R{int(round(amount)):,}".replace(",", " ")
    formatted = f"{amount:,.{decimals}f}".replace(",", " ").replace(".", ",")
    return f"R{formatted}"


def _fmt_comma(val: float, decimals: int = 2) -> str:
    return f"{val:.{decimals}f}".replace(".", ",")


def _base_meta(
    subskill: str,
    learning_objective_id: str,
    concept_id: str,
    marks: int,
    duration_mins: int,
    misconception_tags: List[str],
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "topic": TOPIC_NAME,
        "grade": 9,
        "subject": "Economic and Management Sciences",
        "term": 3,
        "caps_weight_percent": 20,
        "suggested_duration_mins": duration_mins,
        "curriculum_reference": CURRICULUM_REF,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "concept_group": "creditors_ledger",
        "marks": marks,
        "total_marks": marks,
        "misconception_tags": misconception_tags,
        "diagnostic_tags": diagnostic_tags or ["accounting", "creditors_ledger"],
    }


def _mcq(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    explanation: str,
    hints: Dict[str, str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    correct_idx = options.index(correct)
    letter = chr(65 + correct_idx)
    ws = f"({letter}) **{correct}** [{marks} marks]\n\n**Explanation / Working:**\n{explanation}"
    q: Dict[str, Any] = {
        **_base_meta(subskill, learning_objective_id, concept_id, marks, 2, misconception_tags),
        "id": f"g9_ems_c2_{subskill[:12]}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(correct_idx),
        "correct_answer": correct,
        "expected_answer": correct,
        "sample_answer": correct,
        "ideal_answer": correct,
        "explanation": ws,
        "worked_solution": ws,
        "canonical_solution": ws,
        "marking_points": [correct],
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}
            ],
            "carry_forward_rule": "strict",
        },
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _typed(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    sample_answer: str,
    marking_points: List[str],
    hints: Dict[str, str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    marks: Optional[int] = None,
    correct_answer: Optional[str] = None,
    correct_value: Optional[float] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
    worked_solution: Optional[str] = None,
) -> Dict[str, Any]:
    total_marks = marks if marks is not None else max(2, len(marking_points))
    ws = worked_solution or sample_answer
    ans_str = correct_answer or sample_answer
    q: Dict[str, Any] = {
        **_base_meta(subskill, learning_objective_id, concept_id, total_marks, max(3, total_marks), misconception_tags),
        "id": f"g9_ems_c2_{subskill[:12]}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "typed",
        "modality": "math" if correct_value is not None else "semantic",
        "solution_type": "numeric" if correct_value is not None else "marking_points",
        "prompt": prompt,
        "question": prompt,
        "marks": total_marks,
        "total_marks": total_marks,
        "marking_points": marking_points,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "correct_answer": ans_str,
        "expected_answer": str(correct_value) if correct_value is not None else ans_str,
        "explanation": ws,
        "worked_solution": ws,
        "canonical_solution": ws,
        "hints": hints,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": [
                {"id": f"mp_{idx + 1}", "desc": mp, "marks": 1, "editable": True}
                for idx, mp in enumerate(marking_points)
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
    }
    if correct_value is not None:
        q["correct_value"] = correct_value
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _table_q(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    raw_rows: List[List[Dict[str, Any]]],
    cell_hints: Dict[str, str],
    derivations: List[str],
    hints: Dict[str, str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    journal_type: str = "creditors_ledger",
    transactions: Optional[List[str]] = None,
) -> Dict[str, Any]:
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    marking_points: List[Dict[str, Any]] = []
    has_must_be_empty = False

    md_header = "| " + " | ".join(headers) + " |"
    md_sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    md_rows = [md_header, md_sep]

    mp_idx = 1
    for r_idx, row in enumerate(raw_rows):
        ui_row: List[Dict[str, Any]] = []
        md_cells: List[str] = []
        for c_idx, cell in enumerate(row):
            cell_id = f"r{r_idx}_c{c_idx}"
            ctype = cell["type"]
            if ctype == "given":
                val = str(cell["value"])
                ui_row.append({
                    "id": cell_id,
                    "coordinate": cell_id,
                    "type": "given",
                    "value": val,
                    "editable": False,
                    "label": headers[c_idx],
                })
                md_cells.append(val)
            elif ctype == "required":
                exp = str(cell["expected"])
                ui_row.append({
                    "id": cell_id,
                    "coordinate": cell_id,
                    "type": "required",
                    "value": "",
                    "expected": exp,
                    "editable": True,
                    "label": headers[c_idx],
                })
                correct_map[cell_id] = exp
                marking_points.append({
                    "id": f"mp_{mp_idx}",
                    "desc": f"{headers[c_idx]} (Row {r_idx + 1}): {exp}",
                    "marks": 1,
                    "editable": True,
                })
                mp_idx += 1
                md_cells.append(f"**{exp}**")
            else:
                has_must_be_empty = True
                ui_row.append({
                    "id": cell_id,
                    "coordinate": cell_id,
                    "type": "must_be_empty",
                    "value": "",
                    "expected": "",
                    "editable": False,
                    "label": headers[c_idx],
                })
                correct_map[cell_id] = ""
                md_cells.append("*(blank)*")
        rows.append(ui_row)
        md_rows.append("| " + " | ".join(md_cells) + " |")

    marks = max(1, len(marking_points))
    md_table = "\n".join(md_rows)
    deriv_text = "\n".join(f"- {d}" for d in derivations)
    memo = f"{md_table}\n\n**Derivations & Rules:**\n{deriv_text}"
    deductions = [{"rule": "must_be_empty_filled", "penalty": -1}] if has_must_be_empty else []

    out: Dict[str, Any] = {
        **_base_meta(subskill, learning_objective_id, concept_id, marks, max(4, marks), misconception_tags),
        "id": f"g9_ems_c2_tbl_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "journal": {"journal_type": journal_type, "headers": headers, "rows": rows},
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": marks,
        "total_marks": marks,
        "sample_answer": memo,
        "ideal_answer": memo,
        "expected_answer": "; ".join(f"{k}={v}" for k, v in correct_map.items()),
        "correct_answer": "; ".join(f"{k}={v}" for k, v in correct_map.items()),
        "worked_solution": memo,
        "canonical_solution": memo,
        "explanation": memo,
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": deductions,
            "carry_forward_rule": "consequential_accuracy",
        },
    }
    if transactions:
        out["transactions"] = transactions
    return out


def _svg_bar_chart(
    title: str,
    y_label: str,
    bars: List[Tuple[str, float, str]],
    max_val: float,
    unit_suffix: str = "",
) -> str:
    w, h = 620, 300
    left, top, right, bottom = 78, 52, 585, 240
    chart_h = bottom - top
    n = len(bars)
    slot_w = (right - left) / max(1, n)
    bar_w = min(68, slot_w * 0.56)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:620px;background:#FFFFFF;font-family:Arial,sans-serif;">',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#FAF8F3" stroke="#CBD5E1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">{title}</text>',
    ]
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = bottom - frac * chart_h
        tick_val = int(round(max_val * frac))
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="#E2E8F0" stroke-width="1"/>')
        lines.append(f'<text x="{left-8}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#475569">{tick_val}{unit_suffix}</text>')

    lines.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#1E293B" stroke-width="2"/>')
    lines.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#1E293B" stroke-width="2"/>')
    lines.append(
        f'<text x="20" y="{(top+bottom)//2}" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155" transform="rotate(-90 20 {(top+bottom)//2})">{y_label}</text>'
    )

    for idx, (label, val, color) in enumerate(bars):
        cx = left + slot_w * (idx + 0.5)
        bx = cx - bar_w / 2
        bh = (val / max(1e-6, max_val)) * chart_h
        by = bottom - bh
        val_lbl = f"{int(val)}{unit_suffix}" if float(val).is_integer() else f"{_fmt_comma(val, 1)}{unit_suffix}"
        lines.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" rx="4" fill="{color}" stroke="#0F172A" stroke-width="1"/>')
        lines.append(f'<text x="{cx:.1f}" y="{by-6:.1f}" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">{val_lbl}</text>')
        lines.append(f'<text x="{cx:.1f}" y="{bottom+18}" text-anchor="middle" font-size="11" font-weight="bold" fill="#1E293B">{label}</text>')

    lines.append("</svg>")
    return "".join(lines)


def _svg_linear_flow(title: str, stages: List[Tuple[str, str, str]]) -> str:
    w, h = 660, 175
    n = len(stages)
    box_w = 175
    gap = (w - 40 - n * box_w) // max(1, n - 1) if n > 1 else 0
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:660px;background:#FFFFFF;font-family:Arial,sans-serif;">',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#FAF8F3" stroke="#CBD5E1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">{title}</text>',
        '<defs><marker id="arr_c2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#334155"/></marker></defs>',
    ]
    for i, (head, body, fill_hex) in enumerate(stages):
        x = 20 + i * (box_w + gap)
        y = 50
        lines.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="96" rx="8" fill="#FFFFFF" stroke="{fill_hex}" stroke-width="2.2"/>')
        lines.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="28" rx="6" fill="{fill_hex}"/>')
        lines.append(f'<text x="{x + box_w/2:.1f}" y="{y + 19}" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFFFFF">{head}</text>')
        lines.append(f'<text x="{x + box_w/2:.1f}" y="{y + 52}" text-anchor="middle" font-size="11" fill="#1E293B">{body[:28]}</text>')
        if len(body) > 28:
            lines.append(f'<text x="{x + box_w/2:.1f}" y="{y + 70}" text-anchor="middle" font-size="11" fill="#1E293B">{body[28:56]}</text>')
        if i < n - 1:
            x1 = x + box_w + 4
            x2 = x + box_w + gap - 4
            ym = y + 48
            lines.append(f'<line x1="{x1}" y1="{ym}" x2="{x2}" y2="{ym}" stroke="#334155" stroke-width="2" marker-end="url(#arr_c2)"/>')
    lines.append("</svg>")
    return "".join(lines)


def arch_01_credit_transaction_and_creditor_current_liability(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    supplier = rng.choice(SUPPLIER_NAMES)
    amt = rng.choice([3400, 4800, 6200])
    prompt = (
        f"{trader} receives trading stock worth {_fmt_zar(amt)} from {supplier} with an agreement to settle the "
        f"account in 60 days.\n\n"
        f"How is {supplier} classified in {trader}'s accounting records?"
    )
    correct = "A creditor — a Current Liability because the debt must be repaid within one year"
    distractors = [
        "A debtor — a Current Asset representing cash owed to the business by customers",
        "Owner's equity — permanent capital contributed by the founder",
        "A non-current fixed asset kept for more than five years",
    ]
    return _mcq(
        rng,
        subskill="01_credit_transaction_and_creditor_current_liability",
        title="Creditors as Current Liabilities",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Suppliers to whom {trader} owes money for credit purchases are Creditors, classified as Current "
            f"Liabilities because short-term supplier accounts are normally settled within 12 months."
        ),
        hints={
            "tier_1": "Ask whether the business OWES money or IS OWED money, and when it must be settled.",
            "tier_2": "Suppliers we buy from on credit are Creditors, settled within one year.",
            "tier_3": "Select 'A creditor — a Current Liability because the debt must be repaid within one year'.",
        },
        learning_objective_id="lo_c2_creditor_liability",
        concept_id="creditor_current_liability",
        misconception_tags=["confuses_creditor_with_debtor"],
    )


def arch_02_national_credit_act_purpose_and_credit_cycle(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"When a hardware retailer in {area} buys stock on credit from suppliers, South African trade agreements fall "
        f"under the National Credit Act (NCA).\n\n"
        f"What is a PRIMARY goal of the National Credit Act alongside standard credit terms?"
    )
    correct = (
        "To protect borrowers from reckless lending, promote transparent credit agreements, and prevent over-indebtedness"
    )
    distractors = [
        "To forbid businesses from buying trading stock on 30-day credit invoices",
        "To allow creditors to double invoice totals secretly after delivery",
        "To replace all cheques and EFTs with informal barter",
    ]
    return _mcq(
        rng,
        subskill="02_national_credit_act_purpose_and_credit_cycle",
        title="National Credit Act & Credit Cycle",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "The National Credit Act (NCA) promotes fair, transparent credit markets and guards against reckless "
            "lending and unsustainable debt across the credit cycle (order -> delivery -> invoice -> settlement)."
        ),
        hints={
            "tier_1": "Think of why South Africa regulates credit agreements between lenders/suppliers and buyers.",
            "tier_2": "The NCA promotes responsible, transparent lending and prevents over-indebtedness.",
            "tier_3": "Select 'To protect borrowers from reckless lending, promote transparent credit agreements, and prevent over-indebtedness'.",
        },
        learning_objective_id="lo_c2_nca_purpose",
        concept_id="national_credit_act",
        misconception_tags=["thinks_nca_bans_business_credit"],
    )


def arch_03_source_documents_invoice_vs_cheque_vs_debit_note(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    amt = rng.choice([1250, 2400, 3150])
    prompt = (
        f"After ordering stock on credit from {supplier}, a shop receives the goods plus an itemized bill for {_fmt_zar(amt)}.\n\n"
        f"Which exact source document triggers the initial entry in the Creditors Journal (CJ)?"
    )
    correct = "Original invoice received from the supplier"
    distractors = [
        "Duplicate sales invoice issued by our shop to a customer",
        "Cash register roll (CRR) printed at the till",
        "Cheque counterfoil / EFT payment receipt sent later",
    ]
    return _mcq(
        rng,
        subskill="03_source_documents_invoice_vs_cheque_vs_debit_note",
        title="Source Document for Creditors Journal",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "When buying on credit, the supplier keeps the duplicate and gives our business the ORIGINAL invoice — "
            "which is recorded in the Creditors Journal (CJ)."
        ),
        hints={
            "tier_1": "Distinguish an invoice RECEIVED from a supplier vs one ISSUED to a customer.",
            "tier_2": "Suppliers give the buyer the original invoice.",
            "tier_3": "Select 'Original invoice received from the supplier'.",
        },
        learning_objective_id="lo_c2_source_doc_cj",
        concept_id="cj_original_invoice",
        misconception_tags=["confuses_original_and_duplicate_invoice"],
    )


def arch_04_cpj_allocation_cheque_payment_to_creditor(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    cheque_no = rng.randint(410, 690)
    amt = rng.choice([2450, 3800, 5120])
    prompt = (
        f"A bookkeeper issues Cheque/EFT No. {cheque_no} for {_fmt_zar(amt)} to settle an account owing to {supplier}.\n\n"
        f"In the Cash Payments Journal (CPJ), which TWO monetary analysis columns must record {_fmt_zar(amt)}?"
    )
    correct = "Bank column and Creditors control column"
    distractors = [
        "Bank column and Debtors control column",
        "Analysis of receipts and Sales column",
        "Creditors control column and Trading stock column",
    ]
    return _mcq(
        rng,
        subskill="04_cpj_allocation_cheque_payment_to_creditor",
        title="Allocating Creditor Payments in CPJ",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Paying a creditor reduces Bank cash (`Bank` column in CPJ) and reduces the liability owed (`Creditors control` column in CPJ)."
        ),
        hints={
            "tier_1": "Notice which asset went down (cash in Bank) and which liability went down (Creditors control).",
            "tier_2": "A settlement payment is NOT a new purchase of Trading stock — the stock was already recorded in CJ!",
            "tier_3": "Select 'Bank column and Creditors control column'.",
        },
        learning_objective_id="lo_c2_cpj_allocation",
        concept_id="cpj_creditor_payment_columns",
        misconception_tags=["allocates_creditor_payment_to_trading_stock"],
    )


def arch_05_cpj_payments_to_creditors_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    s1, s2 = rng.sample(SUPPLIER_NAMES, 2)
    p1 = rng.choice([1458, 2240, 3150])
    p2 = rng.choice([964, 1850, 2600])
    tot = p1 + p2
    c1_no = rng.randint(701, 740)
    c2_no = c1_no + 1

    headers = ["Doc. no.", "Day", "Name of payee", "Fol.", "Bank (R)", "Creditors control (R)", "Audit"]
    raw_rows = [
        [
            {"type": "given", "value": str(c1_no)},
            {"type": "given", "value": "04"},
            {"type": "given", "value": s1},
            {"type": "given", "value": "C1"},
            {"type": "given", "value": _fmt_zar(p1)},
            {"type": "required", "expected": _fmt_zar(p1)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": str(c2_no)},
            {"type": "given", "value": "21"},
            {"type": "given", "value": s2},
            {"type": "given", "value": "C2"},
            {"type": "required", "expected": _fmt_zar(p2)},
            {"type": "given", "value": _fmt_zar(p2)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Totals"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(tot)},
            {"type": "required", "expected": _fmt_zar(tot)},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c5": f"Enter creditor settlement amount {_fmt_zar(p1)}.",
        "r1_c4": f"Enter Bank outflow matching Creditors control ({_fmt_zar(p2)}).",
        "r2_c4": f"Sum Bank column: {_fmt_zar(p1)} + {_fmt_zar(p2)}.",
        "r2_c5": f"Sum Creditors control column: {_fmt_zar(p1)} + {_fmt_zar(p2)}.",
    }
    derivations = [
        f"Day 04 ({s1}): Bank = {_fmt_zar(p1)}; Creditors control = {_fmt_zar(p1)}.",
        f"Day 21 ({s2}): Bank = {_fmt_zar(p2)}; Creditors control = {_fmt_zar(p2)}.",
        f"Totals = {_fmt_zar(p1)} + {_fmt_zar(p2)} = {_fmt_zar(tot)} in both Bank and Creditors control.",
    ]
    return _table_q(
        rng,
        subskill="05_cpj_payments_to_creditors_2d_table",
        title="CPJ Creditor Settlements Table",
        prompt=(
            f"Complete the Cash Payments Journal (CPJ) extract of {trader} recording payments to creditors {s1} "
            f"(Cheque {c1_no}, {_fmt_zar(p1)}) and {s2} (Cheque {c2_no}, {_fmt_zar(p2)}). Leave shaded cells and 'Audit' blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Each cheque payment enters both Bank and Creditors control for the exact same Rand amount.",
            "tier_2": "Sum both rows down Bank and Creditors control.",
            "tier_3": f"r0_c5={_fmt_zar(p1)}; r1_c4={_fmt_zar(p2)}; Totals={_fmt_zar(tot)}.",
        },
        learning_objective_id="lo_c2_cpj_2d_table",
        concept_id="cpj_creditor_payments_table",
        misconception_tags=["mismatches_bank_and_creditors_control", "fills_must_be_empty_cell"],
        journal_type="cpj",
    )


def arch_06_invoice_trade_discount_calculation(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    supplier = rng.choice(SUPPLIER_NAMES)
    gross_goods = rng.choice([1600, 2000, 2400])
    disc_pct = rng.choice([2.5, 5.0])
    net_goods = round(gross_goods * (1 - disc_pct / 100.0), 2)
    packs = rng.randint(4, 6)
    pack_price = rng.choice([50.0, 55.0])
    stationery = packs * pack_price
    rolls = rng.randint(6, 10)
    pack_mat = rolls * 5.0
    total_inv = round(net_goods + stationery + pack_mat, 2)

    prompt = (
        f"{trader} receives an original invoice from {supplier} for:\n"
        f"- Goods: {_fmt_zar(gross_goods)} less {_fmt_comma(disc_pct, 1)}% trade discount\n"
        f"- {packs} packs of paper at {_fmt_zar(pack_price)} each\n"
        f"- {rolls} rolls of packing material at R5 each\n\n"
        f"Calculate the total discounted invoice amount to record in Creditors control."
    )
    return _typed(
        rng,
        subskill="06_invoice_trade_discount_calculation",
        title="Net Invoice Calculation with Trade Discount",
        prompt=prompt,
        sample_answer=(
            f"Net goods = {_fmt_zar(gross_goods)} - {_fmt_comma(disc_pct, 1)}% = {_fmt_zar(net_goods, 2)}\n"
            f"Paper = {packs} x {_fmt_zar(pack_price)} = {_fmt_zar(stationery, 2)}\n"
            f"Packing material = {rolls} x R5 = {_fmt_zar(pack_mat, 2)}\n"
            f"Total invoice = {_fmt_zar(total_inv, 2)}"
        ),
        marking_points=[
            f"Net goods after {_fmt_comma(disc_pct, 1)}% discount = {_fmt_zar(net_goods, 2)} [1]",
            f"Stationery ({_fmt_zar(stationery, 2)}) + Packing material ({_fmt_zar(pack_mat, 2)}) [1]",
            f"Invoice total = {_fmt_zar(total_inv, 2)} [1]",
        ],
        hints={
            "tier_1": "First deduct the trade discount percentage from the goods amount ONLY.",
            "tier_2": "Next compute packs of paper + rolls of packing material.",
            "tier_3": f"{_fmt_zar(net_goods, 2)} + {_fmt_zar(stationery, 2)} + {_fmt_zar(pack_mat, 2)} = {_fmt_zar(total_inv, 2)}.",
        },
        learning_objective_id="lo_c2_invoice_discount_calc",
        concept_id="trade_discount_invoice",
        misconception_tags=["applies_trade_discount_to_entire_invoice"],
        marks=3,
        correct_answer=_fmt_zar(total_inv, 2),
        correct_value=float(total_inv),
        worked_solution=f"Net goods={net_goods}; Stationery={stationery}; Packing={pack_mat}; Total={_fmt_zar(total_inv, 2)}",
    )


def arch_07_source_invoice_to_cj_entry_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    supplier = rng.choice(SUPPLIER_NAMES)
    doc_no = rng.randint(231, 265)
    stock_amt = rng.choice([1800, 1920, 2400])
    stat_amt = rng.choice([260, 286, 340])
    pack_amt = rng.choice([45, 60, 90])
    total = stock_amt + stat_amt + pack_amt

    headers = ["Doc. no.", "Day", "Creditors", "Creditors control (R)", "Trading stock (R)", "Sundry Amount (R)", "Sundry Details"]
    raw_rows = [
        [
            {"type": "given", "value": str(doc_no)},
            {"type": "given", "value": "03"},
            {"type": "given", "value": supplier},
            {"type": "required", "expected": _fmt_zar(total)},
            {"type": "required", "expected": _fmt_zar(stock_amt)},
            {"type": "given", "value": _fmt_zar(stat_amt)},
            {"type": "given", "value": "Stationery"},
        ],
        [
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(pack_amt)},
            {"type": "required", "expected": "Packing material"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Sum all invoice items: {_fmt_zar(stock_amt)} + {_fmt_zar(stat_amt)} + {_fmt_zar(pack_amt)}.",
        "r0_c4": f"Goods bought for resale go into Trading stock ({_fmt_zar(stock_amt)}).",
        "r1_c6": "Enter exact sundry account name: 'Packing material'.",
    }
    derivations = [
        f"Creditors control = {_fmt_zar(stock_amt)} + {_fmt_zar(stat_amt)} + {_fmt_zar(pack_amt)} = {_fmt_zar(total)}",
        f"Trading stock = {_fmt_zar(stock_amt)}; Sundry row 2 Details = 'Packing material'.",
    ]
    return _table_q(
        rng,
        subskill="07_source_invoice_to_cj_entry_2d_table",
        title="Recording Original Invoice in CJ (2D Table)",
        prompt=(
            f"Enter Invoice {doc_no} from {supplier} in the Creditors Journal of {trader}: Trading goods {_fmt_zar(stock_amt)}, "
            f"Stationery {_fmt_zar(stat_amt)}, and Packing material {_fmt_zar(pack_amt)}. Leave shaded sub-row cells empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Creditors control receives the combined invoice total; Trading stock gets goods for resale only.",
            "tier_2": "Use the second Sundry line to label the remaining R-amount as 'Packing material'.",
            "tier_3": f"Creditors control={_fmt_zar(total)}; Trading stock={_fmt_zar(stock_amt)}; Details='Packing material'.",
        },
        learning_objective_id="lo_c2_cj_entry_table",
        concept_id="cj_invoice_recording_table",
        misconception_tags=["double_counts_sundry_into_trading_stock", "fills_must_be_empty_cell"],
        journal_type="cj",
    )


def arch_08_posting_cj_to_creditors_ledger_credit_side(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    inv_amt = rng.choice([1989, 2423, 3550])
    prompt = (
        f"A bookkeeper posts Invoice no. 64 for {_fmt_zar(inv_amt)} from the Creditors Journal (CJ) to {supplier}'s "
        f"individual Creditors Ledger account.\n\n"
        f"Which column of the Creditors Ledger receives this invoice, and how does the balance change?"
    )
    correct = f"Credit (+) column — increasing the liability balance owed by {_fmt_zar(inv_amt)}"
    distractors = [
        f"Debit (-) column — decreasing the liability balance owed by {_fmt_zar(inv_amt)}",
        f"Debit (+) column — treating the supplier as a customer asset",
        f"Balance column only — leaving both Debit and Credit empty",
    ]
    return _mcq(
        rng,
        subskill="08_posting_cj_to_creditors_ledger_credit_side",
        title="Posting CJ Invoices to Creditors Ledger",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Creditors are liabilities (normal Credit balance). Every credit purchase invoice from CJ posts to the Credit (+) "
            f"column and ADDS {_fmt_zar(inv_amt)} to the amount owed."
        ),
        hints={
            "tier_1": "Creditors are liabilities: do liabilities increase on the Debit or Credit side?",
            "tier_2": "Buying more goods on credit increases what we owe the supplier.",
            "tier_3": f"Select 'Credit (+) column — increasing the liability balance owed by {_fmt_zar(inv_amt)}'.",
        },
        learning_objective_id="lo_c2_cj_credit_post",
        concept_id="cj_to_creditors_ledger",
        misconception_tags=["debits_cj_invoice_like_debtors_ledger"],
    )


def arch_09_posting_cpj_to_creditors_ledger_debit_side(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    pay_amt = rng.choice([964, 1458, 2800])
    prompt = (
        f"A bookkeeper posts Cheque no. 707 for {_fmt_zar(pay_amt)} from the Cash Payments Journal (CPJ) to "
        f"{supplier}'s Creditors Ledger account.\n\n"
        f"Which column of the Creditors Ledger receives this payment, and how does the balance change?"
    )
    correct = f"Debit (-) column — subtracting {_fmt_zar(pay_amt)} from the balance owed to {supplier}"
    distractors = [
        f"Credit (+) column — adding {_fmt_zar(pay_amt)} to the balance owed to {supplier}",
        f"Credit (-) column — increasing assets in the Creditors Ledger",
        f"Debit (+) column — because paying debt makes us owe more money",
    ]
    return _mcq(
        rng,
        subskill="09_posting_cpj_to_creditors_ledger_debit_side",
        title="Posting CPJ Payments to Creditors Ledger",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Paying {supplier} reduces our liability. In the Creditors Ledger, cheque/EFT payments from CPJ post to "
            f"the Debit (-) column and subtract {_fmt_zar(pay_amt)} from the balance."
        ),
        hints={
            "tier_1": "Does paying off a supplier make our debt bigger or smaller?",
            "tier_2": "Liabilities decrease on the Debit (-) side.",
            "tier_3": f"Select 'Debit (-) column — subtracting {_fmt_zar(pay_amt)} from the balance owed to {supplier}'.",
        },
        learning_objective_id="lo_c2_cpj_debit_post",
        concept_id="cpj_to_creditors_ledger",
        misconception_tags=["credits_creditor_payments"],
    )


def arch_10_creditors_ledger_vs_general_ledger_timing(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    n_tx = rng.randint(12, 28)
    prompt = (
        f"{trader} processed {n_tx} credit invoices and payments across four suppliers this month.\n\n"
        f"Explain the key operational difference between updating the CREDITORS LEDGER versus posting to CREDITORS "
        f"CONTROL in the GENERAL LEDGER."
    )
    return _typed(
        rng,
        subskill="10_creditors_ledger_vs_general_ledger_timing",
        title="Creditors Ledger vs General Ledger Creditors Control",
        prompt=prompt,
        sample_answer=(
            f"1. Creditors Ledger (individual supplier accounts C1, C2...): Updated immediately as each of the {n_tx} "
            "transactions occurs, showing the exact running balance owed to a specific supplier after every invoice, return, or payment.\n"
            "2. General Ledger (Creditors Control account): Posted only once at month-end using column totals from CJ, CAJ, and CPJ, showing only the combined closing balance owed to all creditors."
        ),
        marking_points=[
            "Creditors Ledger updates continuously/daily per individual supplier with running balances [1]",
            "General Ledger Creditors Control posts monthly journal totals at month-end showing the aggregate balance [1]",
        ],
        hints={
            "tier_1": "Compare frequency of posting (daily vs month-end) and level of detail (per supplier vs aggregate total).",
            "tier_2": "Bookkeepers check a supplier's Creditors Ledger before writing a cheque; General Ledger summarizes month-end totals.",
            "tier_3": "Contrast individual running balances posted daily (Creditors Ledger) against month-end summary totals (General Ledger).",
        },
        learning_objective_id="lo_c2_cl_vs_gl_timing",
        concept_id="creditors_vs_general_ledger",
        misconception_tags=["thinks_general_ledger_tracks_daily_invoices_individually"],
        marks=2,
    )


def arch_11_double_entry_credit_purchase_of_trading_stock(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    amt = rng.choice([4500, 6800, 8200])
    prompt = (
        f"{trader} posts the monthly Creditors Journal (CJ) total for Trading stock bought on credit ({_fmt_zar(amt)}) "
        f"to the General Ledger.\n\n"
        f"Which General Ledger double entry accurately records buying Trading stock on credit?"
    )
    correct = "Debit Trading stock (Asset increases) and Credit Creditors control (Liability increases)"
    distractors = [
        "Debit Creditors control (Liability increases) and Credit Trading stock (Asset decreases)",
        "Debit Bank (Asset increases) and Credit Sales (Income increases)",
        "Debit Trading stock (Asset increases) and Credit Bank (Asset decreases)",
    ]
    return _mcq(
        rng,
        subskill="11_double_entry_credit_purchase_of_trading_stock",
        title="Double Entry: Credit Purchase of Trading Stock",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Assets (Trading stock) increase on the Debit side (+{_fmt_zar(amt)}), while Liabilities (Creditors control) "
            f"increase on the Credit side (+{_fmt_zar(amt)})."
        ),
        hints={
            "tier_1": "Did Bank cash change yet? No—the purchase was on credit!",
            "tier_2": "Trading stock is an Asset (+ on Debit); Creditors control is a Liability (+ on Credit).",
            "tier_3": "Select 'Debit Trading stock (Asset increases) and Credit Creditors control (Liability increases)'.",
        },
        learning_objective_id="lo_c2_double_entry_stock",
        concept_id="double_entry_credit_stock",
        misconception_tags=["credits_bank_for_credit_purchase"],
    )


def arch_12_double_entry_credit_purchase_of_expense_stationery(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    amt = rng.choice([380, 520, 740])
    prompt = (
        f"{trader} purchases Stationery worth {_fmt_zar(amt)} on credit via the Creditors Journal.\n\n"
        f"Identify the General Ledger account DEBITED, the account CREDITED, and explain the effect on Owner's Equity "
        f"and Liabilities."
    )
    return _typed(
        rng,
        subskill="12_double_entry_credit_purchase_of_expense_stationery",
        title="Double Entry: Credit Purchase of Stationery Expense",
        prompt=prompt,
        sample_answer=(
            f"Debit: Stationery ({_fmt_zar(amt)}) — an expense that decreases Owner's Equity.\n"
            f"Credit: Creditors control ({_fmt_zar(amt)}) — a Current Liability that increases because debt to a supplier rose."
        ),
        marking_points=[
            "Account Debited: Stationery (Expense decreases Owner's Equity) [1]",
            "Account Credited: Creditors control (Liability increases) [1]",
        ],
        hints={
            "tier_1": "Stationery is an expense (debited because expenses decrease Owner's Equity).",
            "tier_2": "Creditors control increases on the Credit side because our supplier debt rose.",
            "tier_3": "Debit Stationery (OE decreases); Credit Creditors control (Liability increases).",
        },
        learning_objective_id="lo_c2_double_entry_expense",
        concept_id="double_entry_credit_expense",
        misconception_tags=["treats_stationery_as_noncurrent_asset"],
        marks=2,
    )


def arch_13_double_entry_payment_to_creditor(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    amt = rng.choice([5400, 7200, 9600])
    prompt = (
        f"At month-end, {trader} posts the CPJ Creditors control column total ({_fmt_zar(amt)}) to the General Ledger.\n\n"
        f"Which General Ledger entry accurately records payments made to creditors?"
    )
    correct = "Debit Creditors control (Liability decreases) and Credit Bank (Asset decreases)"
    distractors = [
        "Debit Bank (Asset increases) and Credit Creditors control (Liability increases)",
        "Debit Trading stock (Asset increases) and Credit Bank (Asset decreases)",
        "Debit Creditors control (Asset increases) and Credit Debtors control (Asset decreases)",
    ]
    return _mcq(
        rng,
        subskill="13_double_entry_payment_to_creditor",
        title="Double Entry: Payment to Creditors",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Paying {_fmt_zar(amt)} to creditors decreases our Liability (`Debit Creditors control`) and decreases cash "
            f"in our Asset account (`Credit Bank`)."
        ),
        hints={
            "tier_1": "Cash in Bank goes down (Asset decreases -> Credit). Supplier debt goes down (Liability decreases -> Debit).",
            "tier_2": "Remember Bank is always CREDITED in CPJ postings.",
            "tier_3": "Select 'Debit Creditors control (Liability decreases) and Credit Bank (Asset decreases)'.",
        },
        learning_objective_id="lo_c2_double_entry_payment",
        concept_id="double_entry_creditor_payment",
        misconception_tags=["debits_bank_on_cpj_payment"],
    )


def arch_14_three_settlement_methods_for_creditors(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    prompt = (
        f"A bookkeeper reviewing {supplier}'s account wants to understand the three standard ways South African "
        f"businesses settle a creditor's account.\n\n"
        f"Which option accurately lists ALL THREE settlement methods?"
    )
    correct = (
        "Settling last month's rendered balance on the 1st of the new month, settling in full up to date, or paying in part (instalment)"
    )
    distractors = [
        "Paying double the invoice secretly, ignoring statements forever, or transferring debt to employees",
        "Issuing cash register rolls only, deleting opening balances, or cancelling invoices without returns",
        "Wait 10 years, trade only with debtors, or convert invoices into equity shares automatically",
    ]
    return _mcq(
        rng,
        subskill="14_three_settlement_methods_for_creditors",
        title="Three Ways to Settle Creditor Accounts",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Businesses settle creditors either by paying the previous month's balance on the 1st, paying the full "
            "balance owed up to today's date, or making a partial payment."
        ),
        hints={
            "tier_1": "Think about whether you pay ONLY last month's balance, EVERYTHING owed up to today, or PART of the debt.",
            "tier_2": "All three are real-world settlement schedules used by bookkeepers.",
            "tier_3": "Select 'Settling last month's rendered balance on the 1st of the new month, settling in full up to date, or paying in part (instalment)'.",
        },
        learning_objective_id="lo_c2_settlement_methods",
        concept_id="creditor_settlement_methods",
        misconception_tags=["assumes_only_full_payment_is_valid"],
    )


def arch_15_calculating_settlement_up_to_date_amount(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    bal_open = rng.choice([2100, 2900, 3600])
    inv1 = rng.choice([1400, 1750, 2150])
    inv2 = rng.choice([450, 620, 840])
    total_due = bal_open + inv1 + inv2
    prompt = (
        f"On 1 November, Thierry's Furnishers owed {supplier} {_fmt_zar(bal_open)} (account rendered). On 3 November, "
        f"stock worth {_fmt_zar(inv1)} was bought on credit, and on 15 November another credit invoice for {_fmt_zar(inv2)} "
        f"was received. On 6 November, packing material worth R500 was bought for CASH by cheque.\n\n"
        f"Calculate the cheque amount needed on 25 November to settle {supplier}'s account IN FULL UP TO DATE."
    )
    return _typed(
        rng,
        subskill="15_calculating_settlement_up_to_date_amount",
        title="Settling a Creditor Account in Full Up to Date",
        prompt=prompt,
        sample_answer=(
            f"Note: The R500 cash purchase on 6 Nov is already paid and NOT added to the Creditors Ledger.\n"
            f"Full settlement up to date = {_fmt_zar(bal_open)} + {_fmt_zar(inv1)} + {_fmt_zar(inv2)} = {_fmt_zar(total_due)}."
        ),
        marking_points=[
            "Excludes the R500 cash purchase because it was already paid immediately [1]",
            f"Sums opening balance ({_fmt_zar(bal_open)}) + credit invoices ({_fmt_zar(inv1)} + {_fmt_zar(inv2)}) = {_fmt_zar(total_due)} [2]",
        ],
        hints={
            "tier_1": "Watch out for the R500 cash purchase — does a cash purchase create supplier debt?",
            "tier_2": "Add ONLY opening rendered balance + credit invoices.",
            "tier_3": f"{_fmt_zar(bal_open)} + {_fmt_zar(inv1)} + {_fmt_zar(inv2)} = {_fmt_zar(total_due)}.",
        },
        learning_objective_id="lo_c2_settle_in_full_calc",
        concept_id="settlement_up_to_date",
        misconception_tags=["adds_cash_purchase_into_creditor_balance"],
        marks=3,
        correct_answer=_fmt_zar(total_due),
        correct_value=float(total_due),
        worked_solution=f"Settlement = {bal_open} + {inv1} + {inv2} = {_fmt_zar(total_due)} (R500 cash excluded)",
    )


def arch_16_cash_transaction_excluded_from_creditors_ledger(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    cash_amt = rng.choice([1850, 2400, 3258])
    prompt = (
        f"On 6 November, a business buys packing material from {supplier} worth {_fmt_zar(cash_amt)} and pays immediately "
        f"by cheque/EFT.\n\n"
        f"Why is this {_fmt_zar(cash_amt)} transaction OMITTED from {supplier}'s Creditors Ledger account?"
    )
    correct = (
        f"It is a cash transaction already settled immediately in the CPJ, so no creditor debt is created"
    )
    distractors = [
        f"Packing material is exempt from all bookkeeping entries in every journal",
        f"Creditors Ledger records only cash transactions and ignores invoices",
        f"The business must enter it twice in the Debtors Ledger instead",
    ]
    return _mcq(
        rng,
        subskill="16_cash_transaction_excluded_from_creditors_ledger",
        title="Excluding Cash Purchases from Creditors Ledger",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Because the {_fmt_zar(cash_amt)} was paid immediately (recorded straight in CPJ -> Bank & Packing material), "
            f"no amount is owed to {supplier}, so nothing goes into CJ or the Creditors Ledger."
        ),
        hints={
            "tier_1": "Ask whether buying by cheque/immediate EFT leaves any unpaid debt.",
            "tier_2": "Creditors Ledger tracks ONLY credit purchases (CJ), returns (CAJ), and payments against credit accounts (CPJ).",
            "tier_3": "Select 'It is a cash transaction already settled immediately in the CPJ, so no creditor debt is created'.",
        },
        learning_objective_id="lo_c2_cash_excluded_cl",
        concept_id="cash_vs_credit_exclusion",
        misconception_tags=["posts_cash_purchases_to_creditors_ledger"],
    )


def arch_17_posting_rules_summary_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    headers = ["Subsidiary Journal", "Source Document", "Creditors Ledger Column", "Effect on Balance", "Flag"]
    raw_rows = [
        [
            {"type": "given", "value": "Creditors Journal (CJ)"},
            {"type": "given", "value": "Original invoice"},
            {"type": "required", "expected": "Credit (+)"},
            {"type": "required", "expected": "Add to balance"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Cash Payments Journal (CPJ)"},
            {"type": "given", "value": "Cheque counterfoil"},
            {"type": "required", "expected": "Debit (-)"},
            {"type": "given", "value": "Subtract from balance"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Creditors Allowance Journal (CAJ)"},
            {"type": "required", "expected": "Debit note"},
            {"type": "given", "value": "Debit (-)"},
            {"type": "required", "expected": "Subtract from balance"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact string: 'Credit (+)'.",
        "r0_c3": "Exact string: 'Add to balance'.",
        "r1_c2": "Exact string: 'Debit (-)'.",
        "r2_c1": "Exact document: 'Debit note'.",
        "r2_c3": "Exact string: 'Subtract from balance'.",
    }
    derivations = [
        "CJ (Original invoice) -> Credit (+) -> Add to balance.",
        "CPJ (Cheque counterfoil) -> Debit (-) -> Subtract from balance.",
        "CAJ (Debit note) -> Debit (-) -> Subtract from balance.",
    ]
    return _table_q(
        rng,
        subskill="17_posting_rules_summary_2d_table",
        title="Creditors Ledger Posting Rules Schedule",
        prompt=(
            f"For {trader}'s trainee bookkeeper, complete the Creditors Ledger posting guide using these exact entries: "
            f"'Credit (+)', 'Debit (-)', 'Debit note', 'Add to balance', and 'Subtract from balance'. Leave 'Flag' blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Invoices increase what we owe (+ Credit); Cheques and Debit notes decrease what we owe (- Debit).",
            "tier_2": "Use the exact short strings listed in the prompt.",
            "tier_3": "r0_c2='Credit (+)', r0_c3='Add to balance', r1_c2='Debit (-)', r2_c1='Debit note', r2_c3='Subtract from balance'.",
        },
        learning_objective_id="lo_c2_posting_rules_table",
        concept_id="creditors_posting_rules_table",
        misconception_tags=["confuses_debit_and_credit_notes", "fills_must_be_empty_cell"],
    )


def arch_18_three_column_creditors_ledger_opening_plus_cj_2d_table(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    open_bal = rng.choice([2115, 2450, 3120])
    inv1 = rng.choice([1470, 1890, 2423])
    inv2 = rng.choice([980, 1340, 1650])
    b2 = open_bal + inv1
    b3 = b2 + inv2

    headers = ["Date", "Details / Doc no.", "Fol.", "Debit (-)", "Credit (+)", "Balance (R)"]
    raw_rows = [
        [
            {"type": "given", "value": "Jul 01"},
            {"type": "given", "value": "Account rendered"},
            {"type": "given", "value": "b/d"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(open_bal)},
        ],
        [
            {"type": "given", "value": "Jul 15"},
            {"type": "given", "value": "Invoice no. 63"},
            {"type": "given", "value": "CJ"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(inv1)},
            {"type": "required", "expected": _fmt_zar(b2)},
        ],
        [
            {"type": "given", "value": "Jul 28"},
            {"type": "given", "value": "Invoice no. 71"},
            {"type": "required", "expected": "CJ"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(inv2)},
            {"type": "required", "expected": _fmt_zar(b3)},
        ],
    ]
    cell_hints = {
        "r1_c5": f"Add {_fmt_zar(open_bal)} + {_fmt_zar(inv1)}.",
        "r2_c2": "Folio for credit purchase invoice is 'CJ'.",
        "r2_c5": f"Add {_fmt_zar(b2)} + {_fmt_zar(inv2)}.",
    }
    derivations = [
        f"Jul 15: Balance = {_fmt_zar(open_bal)} + {_fmt_zar(inv1)} = {_fmt_zar(b2)}.",
        f"Jul 28: Folio = CJ; Balance = {_fmt_zar(b2)} + {_fmt_zar(inv2)} = {_fmt_zar(b3)}.",
    ]
    return _table_q(
        rng,
        subskill="18_three_column_creditors_ledger_opening_plus_cj_2d_table",
        title=f"Creditors Ledger ({supplier}) — Running Credit Balances",
        prompt=(
            f"Complete the 3-column Creditors Ledger for {supplier} following two credit purchases (Jul 15: {_fmt_zar(inv1)}; "
            f"Jul 28: {_fmt_zar(inv2)}). Leave empty Debit (-) cells blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Each Credit (+) invoice adds to the running balance.",
            "tier_2": "Remember the journal folio for Invoices is CJ.",
            "tier_3": f"Jul 15 Bal={_fmt_zar(b2)}; Jul 28 Fol='CJ', Bal={_fmt_zar(b3)}.",
        },
        learning_objective_id="lo_c2_cl_running_credit",
        concept_id="creditors_ledger_cj_running_balance",
        misconception_tags=["subtracts_cj_invoices_from_balance", "fills_must_be_empty_cell"],
    )


def arch_19_three_column_creditors_ledger_with_cpj_payment_2d_table(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    open_bal = rng.choice([2314, 2850, 3420])
    inv_amt = rng.choice([1470, 1650, 1980])
    pay_amt = rng.choice([964, 1200, 1500])
    b2 = open_bal + inv_amt
    b3 = b2 - pay_amt

    headers = ["Date", "Details / Doc no.", "Fol.", "Debit (-)", "Credit (+)", "Balance (R)"]
    raw_rows = [
        [
            {"type": "given", "value": "Jul 01"},
            {"type": "given", "value": "Account rendered"},
            {"type": "given", "value": "b/d"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(open_bal)},
        ],
        [
            {"type": "given", "value": "Jul 15"},
            {"type": "given", "value": "Invoice no. 62"},
            {"type": "given", "value": "CJ"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(inv_amt)},
            {"type": "required", "expected": _fmt_zar(b2)},
        ],
        [
            {"type": "given", "value": "Jul 21"},
            {"type": "given", "value": "Cheque no. 707"},
            {"type": "given", "value": "CPJ"},
            {"type": "required", "expected": _fmt_zar(pay_amt)},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(b3)},
        ],
    ]
    cell_hints = {
        "r1_c5": f"{_fmt_zar(open_bal)} + {_fmt_zar(inv_amt)} = {_fmt_zar(b2)}.",
        "r2_c3": f"Enter cheque payment amount {_fmt_zar(pay_amt)} in Debit (-).",
        "r2_c5": f"Subtract {_fmt_zar(pay_amt)} from {_fmt_zar(b2)}.",
    }
    derivations = [
        f"Jul 15 (CJ Credit +): {_fmt_zar(open_bal)} + {_fmt_zar(inv_amt)} = {_fmt_zar(b2)}.",
        f"Jul 21 (CPJ Debit -): {_fmt_zar(b2)} - {_fmt_zar(pay_amt)} = {_fmt_zar(b3)}.",
    ]
    return _table_q(
        rng,
        subskill="19_three_column_creditors_ledger_with_cpj_payment_2d_table",
        title=f"Creditors Ledger ({supplier}) — Invoice & Cheque Payment",
        prompt=(
            f"Record Invoice 62 ({_fmt_zar(inv_amt)}) and Cheque 707 ({_fmt_zar(pay_amt)}) in {supplier}'s 3-column "
            f"Creditors Ledger. Leave blank Debit/Credit cells empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Invoice adds in Credit (+); Cheque subtracts in Debit (-).",
            "tier_2": "Update Balance row by row.",
            "tier_3": f"Jul 15 Bal={_fmt_zar(b2)}; Jul 21 Debit={_fmt_zar(pay_amt)}, Bal={_fmt_zar(b3)}.",
        },
        learning_objective_id="lo_c2_cl_cj_cpj_table",
        concept_id="creditors_ledger_cj_cpj_table",
        misconception_tags=["adds_cpj_cheque_instead_of_subtracts", "fills_must_be_empty_cell"],
    )


def arch_20_three_column_creditors_ledger_with_caj_return_2d_table(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    open_bal = rng.randint(10, 22) * 100
    pur_amt = rng.randint(18, 36) * 100
    ret_amt = rng.randint(3, 6) * 100
    pay_amt = rng.randint(10, 18) * 100
    b2 = open_bal + pur_amt
    b3 = b2 - ret_amt
    b4 = b3 - pay_amt

    headers = ["Date", "Details / Doc no.", "Fol.", "Debit (-)", "Credit (+)", "Balance (R)"]
    raw_rows = [
        [
            {"type": "given", "value": "Sep 01"},
            {"type": "given", "value": "Account rendered"},
            {"type": "given", "value": "b/d"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(open_bal)},
        ],
        [
            {"type": "given", "value": "Sep 08"},
            {"type": "given", "value": "Invoice 214"},
            {"type": "given", "value": "CJ"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(pur_amt)},
            {"type": "required", "expected": _fmt_zar(b2)},
        ],
        [
            {"type": "given", "value": "Sep 16"},
            {"type": "given", "value": "Debit Note 54"},
            {"type": "given", "value": "CAJ"},
            {"type": "required", "expected": _fmt_zar(ret_amt)},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(b3)},
        ],
        [
            {"type": "given", "value": "Sep 25"},
            {"type": "given", "value": "Cheque 518"},
            {"type": "given", "value": "CPJ"},
            {"type": "given", "value": _fmt_zar(pay_amt)},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(b4)},
        ],
    ]
    cell_hints = {
        "r1_c5": f"{_fmt_zar(open_bal)} + {_fmt_zar(pur_amt)} = {_fmt_zar(b2)}.",
        "r2_c3": f"Debit Note return from CAJ goes in Debit (-): {_fmt_zar(ret_amt)}.",
        "r2_c5": f"{_fmt_zar(b2)} - {_fmt_zar(ret_amt)} = {_fmt_zar(b3)}.",
        "r3_c5": f"{_fmt_zar(b3)} - {_fmt_zar(pay_amt)} = {_fmt_zar(b4)}.",
    }
    derivations = [
        f"Sep 08 (CJ): {_fmt_zar(open_bal)} + {_fmt_zar(pur_amt)} = {_fmt_zar(b2)}.",
        f"Sep 16 (CAJ Debit -): {_fmt_zar(b2)} - {_fmt_zar(ret_amt)} = {_fmt_zar(b3)}.",
        f"Sep 25 (CPJ Debit -): {_fmt_zar(b3)} - {_fmt_zar(pay_amt)} = {_fmt_zar(b4)}.",
    ]
    return _table_q(
        rng,
        subskill="20_three_column_creditors_ledger_with_caj_return_2d_table",
        title=f"Creditors Ledger ({supplier}) — CJ, CAJ & CPJ",
        prompt=(
            f"Complete {supplier}'s 3-column Creditors Ledger including a credit purchase ({_fmt_zar(pur_amt)}), damaged "
            f"stock return on Debit Note 54 ({_fmt_zar(ret_amt)}), and Cheque 518 ({_fmt_zar(pay_amt)}). Leave blank cells empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "CJ invoices go in Credit (+); BOTH CAJ returns and CPJ payments go in Debit (-).",
            "tier_2": "Compute running balance step by step down to Sep 25.",
            "tier_3": f"Sep 08={_fmt_zar(b2)}; Sep 16 Debit={_fmt_zar(ret_amt)}, Bal={_fmt_zar(b3)}; Sep 25={_fmt_zar(b4)}.",
        },
        learning_objective_id="lo_c2_cl_cj_caj_cpj_table",
        concept_id="creditors_ledger_full_account",
        misconception_tags=["credits_debit_note_return", "fills_must_be_empty_cell"],
    )


def arch_21_identifying_creditors_ledger_error_debit_credit_reversal(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    open_bal = rng.choice([2000, 2500, 3200])
    pay_amt = rng.choice([800, 1100, 1400])
    wrong_bal = open_bal + pay_amt
    correct_bal = open_bal - pay_amt
    diff = wrong_bal - correct_bal

    prompt = (
        f"A trainee bookkeeper opens {supplier}'s Creditors Ledger with a balance of {_fmt_zar(open_bal)} and records "
        f"Cheque 402 ({_fmt_zar(pay_amt)}, CPJ) mistakenly in the CREDIT (+) column instead of DEBIT (-), producing an "
        f"incorrect balance of {_fmt_zar(wrong_bal)}.\n\n"
        f"Calculate the CORRECT closing balance after fixing the reversal error."
    )
    return _typed(
        rng,
        subskill="21_identifying_creditors_ledger_error_debit_credit_reversal",
        title="Correcting a Creditors Ledger Reversal Error",
        prompt=prompt,
        sample_answer=(
            f"Cheque payments decrease a creditor's balance (Debit -), not increase it.\n"
            f"Correct balance = {_fmt_zar(open_bal)} - {_fmt_zar(pay_amt)} = {_fmt_zar(correct_bal)} "
            f"(the error overstated the balance by {_fmt_zar(diff)})."
        ),
        marking_points=[
            f"Identifies cheque CPJ must be debited (-) rather than credited (+) [1]",
            f"Correct closing balance = {_fmt_zar(open_bal)} - {_fmt_zar(pay_amt)} = {_fmt_zar(correct_bal)} [2]",
        ],
        hints={
            "tier_1": "Return to the opening balance before the wrongly posted cheque.",
            "tier_2": f"Subtract {_fmt_zar(pay_amt)} from {_fmt_zar(open_bal)}.",
            "tier_3": f"{_fmt_zar(open_bal)} - {_fmt_zar(pay_amt)} = {_fmt_zar(correct_bal)}.",
        },
        learning_objective_id="lo_c2_cl_error_correction",
        concept_id="creditors_ledger_reversal_error",
        misconception_tags=["only_subtracts_pay_once_from_wrong_bal"],
        marks=3,
        correct_answer=_fmt_zar(correct_bal),
        correct_value=float(correct_bal),
        worked_solution=f"Correct balance = {open_bal} - {pay_amt} = {_fmt_zar(correct_bal)}",
    )


def arch_22_accounting_equation_credit_purchase_stock_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    stock_amt = rng.choice([1800, 2400, 3200])
    equip_amt = rng.choice([4500, 6200, 7800])

    headers = ["Credit Transaction", "Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"type": "given", "value": f"Bought trading stock on credit, {_fmt_zar(stock_amt)}"},
            {"type": "given", "value": "Trading stock"},
            {"type": "required", "expected": "Creditors control"},
            {"type": "required", "expected": f"+{stock_amt}"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"+{stock_amt}"},
        ],
        [
            {"type": "given", "value": f"Bought equipment on credit, {_fmt_zar(equip_amt)}"},
            {"type": "required", "expected": "Equipment"},
            {"type": "given", "value": "Creditors control"},
            {"type": "required", "expected": f"+{equip_amt}"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"+{equip_amt}"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact account: 'Creditors control'.",
        "r0_c3": f"Trading stock increases Assets: '+{stock_amt}'.",
        "r0_c5": f"Debt owed to supplier increases Liabilities: '+{stock_amt}'.",
        "r1_c1": "Exact asset account: 'Equipment'.",
        "r1_c3": f"Equipment increases Assets: '+{equip_amt}'.",
        "r1_c5": f"Debt owed increases Liabilities: '+{equip_amt}'.",
    }
    derivations = [
        f"Stock on credit: A (+{stock_amt}) = OE (0) + L (+{stock_amt}).",
        f"Equipment on credit: A (+{equip_amt}) = OE (0) + L (+{equip_amt}).",
    ]
    return _table_q(
        rng,
        subskill="22_accounting_equation_credit_purchase_stock_2d_table",
        title="Accounting Equation: Credit Purchases of Assets",
        prompt=(
            f"Complete the Accounting Equation (A = OE + L) for two credit asset purchases by {trader}. "
            f"Enter exact signed numbers like '+{stock_amt}'."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Buying stock or equipment on credit adds an Asset and adds a Liability (Creditors control).",
            "tier_2": "Owner's Equity stays 0 on both purchases.",
            "tier_3": f"Row 1: Creditors control, +{stock_amt}, +{stock_amt}; Row 2: Equipment, +{equip_amt}, +{equip_amt}.",
        },
        learning_objective_id="lo_c2_eq_credit_assets",
        concept_id="accounting_equation_credit_assets",
        misconception_tags=["affects_owners_equity_for_asset_purchase"],
        journal_type="accounting_equation",
    )


def arch_23_accounting_equation_credit_expense_and_payment_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    stat_amt = rng.choice([280, 380, 490])
    pay_amt = rng.choice([1500, 2200, 2900])

    headers = ["Transaction", "Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"type": "given", "value": f"Bought stationery on credit, {_fmt_zar(stat_amt)}"},
            {"type": "given", "value": "Stationery"},
            {"type": "given", "value": "Creditors control"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"-{stat_amt}"},
            {"type": "required", "expected": f"+{stat_amt}"},
        ],
        [
            {"type": "given", "value": f"Paid creditor by EFT/cheque, {_fmt_zar(pay_amt)}"},
            {"type": "required", "expected": "Creditors control"},
            {"type": "given", "value": "Bank"},
            {"type": "required", "expected": f"-{pay_amt}"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"-{pay_amt}"},
        ],
    ]
    cell_hints = {
        "r0_c4": f"Stationery is an expense reducing Owner's Equity: '-{stat_amt}'.",
        "r0_c5": f"Creditors control increases Liabilities: '+{stat_amt}'.",
        "r1_c1": "Account Debited on payment: 'Creditors control'.",
        "r1_c3": f"Bank decreases Assets: '-{pay_amt}'.",
        "r1_c5": f"Creditors control decreases Liabilities: '-{pay_amt}'.",
    }
    derivations = [
        f"Stationery on credit: A (0) = OE (-{stat_amt}) + L (+{stat_amt}).",
        f"Cheque payment: A (-{pay_amt}) = OE (0) + L (-{pay_amt}).",
    ]
    return _table_q(
        rng,
        subskill="23_accounting_equation_credit_expense_and_payment_2d_table",
        title="Accounting Equation: Credit Expense & Settlement",
        prompt=(
            f"Complete the Accounting Equation analysis for {trader}: (1) Stationery bought on credit ({_fmt_zar(stat_amt)}) "
            f"and (2) EFT payment to a creditor ({_fmt_zar(pay_amt)}). Use exact signed values like '-{stat_amt}' or '+{stat_amt}'."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "An expense bought on credit cuts OE and raises Liabilities (A=0). Paying a creditor cuts Bank and Liabilities (OE=0).",
            "tier_2": "Verify A = OE + L holds for every row.",
            "tier_3": f"Row 1: OE=-{stat_amt}, L=+{stat_amt}; Row 2: Debited='Creditors control', A=-{pay_amt}, L=-{pay_amt}.",
        },
        learning_objective_id="lo_c2_eq_expense_payment",
        concept_id="accounting_equation_expense_settlement",
        misconception_tags=["leaves_stationery_as_asset_positive"],
        journal_type="accounting_equation",
    )


def arch_24_creditors_balance_movement_bar_graph(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.choice([3200, 3800, 4400])
    c2 = rng.choice([5400, 6200, 7100])
    c3 = rng.choice([2100, 2600, 3100])
    tot = c1 + c2 + c3

    svg = _svg_bar_chart(
        title="Closing Creditors Balances by Supplier (R)",
        y_label="Balance Owed (R)",
        bars=[
            ("C1 Makro", float(c1), "#1D4ED8"),
            ("C2 Mega", float(c2), "#DC2626"),
            ("C3 PaperCo", float(c3), "#0F766E"),
        ],
        max_val=float(c2 + 1200),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below showing month-end closing balances owed to three creditors: "
        f"C1 Makro ({_fmt_zar(c1)}), C2 Mega ({_fmt_zar(c2)}), and C3 PaperCo ({_fmt_zar(c3)}).\n\n"
        f"Calculate the total closing Creditors Control balance owed across all three suppliers."
    )
    return _typed(
        rng,
        subskill="24_creditors_balance_movement_bar_graph",
        title="Creditors Balances Summary (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Total Creditors Control = {_fmt_zar(c1)} + {_fmt_zar(c2)} + {_fmt_zar(c3)} = {_fmt_zar(tot)}.",
        marking_points=[
            f"Reads C1 ({_fmt_zar(c1)}), C2 ({_fmt_zar(c2)}), and C3 ({_fmt_zar(c3)}) accurately [1]",
            f"Sums all three supplier balances = {_fmt_zar(tot)} [2]",
        ],
        hints={
            "tier_1": "Read the exact Rand amount above each of the three bars.",
            "tier_2": "Add all three individual creditor balances to reconcile Creditors Control.",
            "tier_3": f"{_fmt_zar(c1)} + {_fmt_zar(c2)} + {_fmt_zar(c3)} = {_fmt_zar(tot)}.",
        },
        learning_objective_id="lo_c2_creditors_bar_graph",
        concept_id="creditors_balance_graph",
        misconception_tags=["omits_smallest_supplier_bar"],
        marks=3,
        correct_answer=_fmt_zar(tot),
        correct_value=float(tot),
        diagram_spec={"kind": "inline_svg", "title": "Closing Creditors Balances", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Total = {c1} + {c2} + {c3} = {_fmt_zar(tot)}",
    )


def arch_25_creditors_accounting_cycle_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    inv_amt = rng.choice([4200, 5600, 6800])
    svg = _svg_linear_flow(
        title=f"Credit Purchase Flow ({supplier})",
        stages=[
            ("1. SOURCE DOC", f"Original Invoice ({_fmt_zar(inv_amt)})", "#1D4ED8"),
            ("2. JOURNAL (CJ)", "Record invoice in Creditors Journal", "#D97706"),
            ("3. LEDGERS", "Credit C1 daily; GL Control month-end", "#15803D"),
        ],
    )
    prompt = (
        f"Refer to the flowchart below showing how a {_fmt_zar(inv_amt)} credit purchase from {supplier} moves through "
        f"the accounting cycle.\n\n"
        f"Explain what happens in Stage 2 (Creditors Journal) and Stage 3 (Creditors Ledger vs General Ledger Control)."
    )
    return _typed(
        rng,
        subskill="25_creditors_accounting_cycle_flow_diagram",
        title="Credit Purchase Accounting Cycle (Flowchart)",
        prompt=prompt,
        sample_answer=(
            f"Stage 2 (CJ): Bookkeeper records the {_fmt_zar(inv_amt)} Original Invoice into the Creditors Journal under "
            "Creditors control and the matching Trading stock or Sundry expense column.\n"
            "Stage 3 (Ledgers): The individual supplier account in the Creditors Ledger is credited immediately to update "
            "what we owe today, while the General Ledger Creditors Control account receives the combined monthly CJ total at month-end."
        ),
        marking_points=[
            "Stage 2 records the Original Invoice in CJ across Creditors control and asset/expense columns [1]",
            "Stage 3 credits the individual Creditors Ledger daily and posts the CJ monthly total to General Ledger Creditors Control [2]",
        ],
        hints={
            "tier_1": "Read Stage 2 and Stage 3 along the arrows from left to right.",
            "tier_2": "Mention journal columns in Stage 2 and daily individual vs monthly summary posting in Stage 3.",
            "tier_3": "CJ records the invoice; Creditors Ledger credits supplier daily while GL Creditors Control posts monthly total.",
        },
        learning_objective_id="lo_c2_accounting_cycle_flow",
        concept_id="creditors_accounting_cycle",
        misconception_tags=["reverses_journal_and_ledger_order"],
        marks=3,
        diagram_spec={"kind": "inline_svg", "title": "Credit Purchase Accounting Cycle", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25 = {
    "01_credit_transaction_and_creditor_current_liability": arch_01_credit_transaction_and_creditor_current_liability,
    "02_national_credit_act_purpose_and_credit_cycle": arch_02_national_credit_act_purpose_and_credit_cycle,
    "03_source_documents_invoice_vs_cheque_vs_debit_note": arch_03_source_documents_invoice_vs_cheque_vs_debit_note,
    "04_cpj_allocation_cheque_payment_to_creditor": arch_04_cpj_allocation_cheque_payment_to_creditor,
    "05_cpj_payments_to_creditors_2d_table": arch_05_cpj_payments_to_creditors_2d_table,
    "06_invoice_trade_discount_calculation": arch_06_invoice_trade_discount_calculation,
    "07_source_invoice_to_cj_entry_2d_table": arch_07_source_invoice_to_cj_entry_2d_table,
    "08_posting_cj_to_creditors_ledger_credit_side": arch_08_posting_cj_to_creditors_ledger_credit_side,
    "09_posting_cpj_to_creditors_ledger_debit_side": arch_09_posting_cpj_to_creditors_ledger_debit_side,
    "10_creditors_ledger_vs_general_ledger_timing": arch_10_creditors_ledger_vs_general_ledger_timing,
    "11_double_entry_credit_purchase_of_trading_stock": arch_11_double_entry_credit_purchase_of_trading_stock,
    "12_double_entry_credit_purchase_of_expense_stationery": arch_12_double_entry_credit_purchase_of_expense_stationery,
    "13_double_entry_payment_to_creditor": arch_13_double_entry_payment_to_creditor,
    "14_three_settlement_methods_for_creditors": arch_14_three_settlement_methods_for_creditors,
    "15_calculating_settlement_up_to_date_amount": arch_15_calculating_settlement_up_to_date_amount,
    "16_cash_transaction_excluded_from_creditors_ledger": arch_16_cash_transaction_excluded_from_creditors_ledger,
    "17_posting_rules_summary_2d_table": arch_17_posting_rules_summary_2d_table,
    "18_three_column_creditors_ledger_opening_plus_cj_2d_table": arch_18_three_column_creditors_ledger_opening_plus_cj_2d_table,
    "19_three_column_creditors_ledger_with_cpj_payment_2d_table": arch_19_three_column_creditors_ledger_with_cpj_payment_2d_table,
    "20_three_column_creditors_ledger_with_caj_return_2d_table": arch_20_three_column_creditors_ledger_with_caj_return_2d_table,
    "21_identifying_creditors_ledger_error_debit_credit_reversal": arch_21_identifying_creditors_ledger_error_debit_credit_reversal,
    "22_accounting_equation_credit_purchase_stock_2d_table": arch_22_accounting_equation_credit_purchase_stock_2d_table,
    "23_accounting_equation_credit_expense_and_payment_2d_table": arch_23_accounting_equation_credit_expense_and_payment_2d_table,
    "24_creditors_balance_movement_bar_graph": arch_24_creditors_balance_movement_bar_graph,
    "25_creditors_accounting_cycle_flow_diagram": arch_25_creditors_accounting_cycle_flow_diagram,
}
