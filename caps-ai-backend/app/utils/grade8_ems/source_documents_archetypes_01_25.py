"""Grade 8 EMS — Source Documents Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/02. Source documents.md.
Uses inline_svg (diagram_role="context") for all authentic SA commercial source document plates.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import AREAS, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario

TOPIC_NAME = "Source documents"
TOPIC_KEY = "grade8_ems_source_documents"
LO = "g8_ems_source_docs"
TERM = 2
CAPS_WEIGHT_PERCENT = 20

_BANKS = ["FNB", "Absa", "Standard Bank", "Nedbank", "Capitec Business"]


def get_ems_scenario(rng: Optional[random.Random] = None) -> Dict[str, Any]:
    s = _raw_ems_scenario(rng)
    first = str(s["entrepreneur"]).split()[0]
    s["business"] = f"{first}'s {s['business_type'].title()}"
    return s


def fmt_r(amount: int | float) -> str:
    """Format an integer or float Rand amount using SA space thousands separator."""
    if isinstance(amount, float) and not amount.is_integer():
        whole = int(amount)
        cents = round((amount - whole) * 100)
        whole_str = f"{whole:,}".replace(",", " ")
        return f"R{whole_str},{cents:02d}"
    return f"R{int(round(amount)):,}".replace(",", " ")


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    misconception_tags: Optional[List[str]] = None,
    duration_mins: int = 4,
) -> Dict[str, Any]:
    out = dict(item)
    hints = out.get("hints") or {
        "tier_1": "Check who pays vs who receives and which copy stays with the business.",
        "tier_2": "CRJ uses Duplicate Receipts, Deposit Slip Duplicates, CRR; CPJ uses Counterfoils, EFT Proofs, Cash Invoices.",
        "tier_3": str(out.get("correct_answer") or out.get("sample_answer") or ""),
    }
    out["hints"] = hints
    out["hint_sections"] = out.get("hint_sections") or [
        hints.get("tier_1", ""),
        hints.get("tier_2", ""),
        hints.get("tier_3", ""),
    ]
    out.update({
        "topic": TOPIC_NAME,
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_source_documents",
        "grade": 8,
        "subject": "Economic and Management Sciences",
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT_PERCENT,
        "suggested_duration_mins": out.get("suggested_duration_mins", duration_mins),
        "subskill": subskill,
        "archetype": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": subskill,
        "concept_group": "source_documents",
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 2 > Source Documents",
        "misconception_tags": misconception_tags or ["source_document_confusion"],
        "diagnostic_tags": ["source_documents", "financial_literacy", "grade8_ems"],
    })
    return out


def _make_mcq(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    options: List[str],
    correct_ans: str,
    explanation: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    shuffled = list(options)
    rng.shuffle(shuffled)
    c_idx = shuffled.index(correct_ans)
    letter = chr(65 + c_idx)
    full_ans = f"{letter}. {correct_ans}"
    worked = f"**{full_ans}** [{marks} marks]\n\n**Explanation:**\n- {explanation}"
    payload: Dict[str, Any] = {
        "id": f"g8_ems_sd_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "options": shuffled,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "expected_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct_ans}", "marks": marks, "editable": True}
            ],
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=3,
    )


def _make_typed(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    correct_ans: str,
    steps: List[str],
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    marks: int = 3,
    acceptable_answers: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    steps_md = "\n".join(f"- {s}" for s in steps)
    worked = f"**Answer:** {correct_ans} [{marks} marks]\n\n**Step-by-Step Working:**\n{steps_md}"
    payload: Dict[str, Any] = {
        "id": f"g8_ems_sd_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "typed",
        "modality": "math",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "expected_answer": correct_ans,
        "acceptable_answers": acceptable_answers or [correct_ans],
        "sample_answer": correct_ans,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{idx + 1}", "desc": st, "marks": 1, "editable": True}
                for idx, st in enumerate(steps[:marks])
            ],
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=4,
    )


def _make_rubric(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    sample_answer: str,
    marking_points: List[str],
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    marks: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    pts_md = "\n".join(f"- {p} [1 mark]" for p in marking_points)
    worked = f"**Model Answer** [{marks} marks]\n\n{sample_answer}\n\n**Marking Breakdown:**\n{pts_md}"
    payload: Dict[str, Any] = {
        "id": f"g8_ems_sd_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "short_answer",
        "modality": "semantic",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": sample_answer,
        "expected_answer": sample_answer,
        "sample_answer": sample_answer,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "marking_points": marking_points,
        "guidelines": marking_points,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{idx + 1}", "desc": p, "marks": 1, "editable": True}
                for idx, p in enumerate(marking_points)
            ],
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=5,
    )


def _make_table(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    journal_type: str,
    headers: List[str],
    table_rows: List[List[Tuple[str, str, bool]]],
    cell_hints: Dict[str, str],
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    worked_notes: str = "",
) -> Dict[str, Any]:
    ui_rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    md_rows: List[List[str]] = []

    for r_idx, row in enumerate(table_rows):
        ui_row: List[Dict[str, Any]] = []
        md_row: List[str] = []
        for c_idx, (val, ctype, editable) in enumerate(row):
            coord = f"t0_r{r_idx}_c{c_idx}"
            ui_row.append({
                "coordinate": coord,
                "value": val if not editable else "",
                "type": ctype,
                "editable": editable,
                "prefilled": not editable,
            })
            if editable:
                correct_map[coord] = val
            md_row.append(f"**{val}**" if editable and val else (val or "-"))
        ui_rows.append(ui_row)
        md_rows.append(md_row)

    header_line = "| " + " | ".join(headers) + " |"
    sep_line = "| " + " | ".join("---" for _ in headers) + " |"
    body_lines = ["| " + " | ".join(r) + " |" for r in md_rows]
    md_table = "\n".join([header_line, sep_line] + body_lines)

    marks = max(2, len(correct_map))
    worked = f"**Completed Table** [{marks} marks]\n\n{md_table}"
    if worked_notes:
        worked += f"\n\n**Notes:**\n{worked_notes}"

    payload: Dict[str, Any] = {
        "id": f"g8_ems_sd_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "headers": headers,
        "rows": ui_rows,
        "journal": {
            "journal_type": journal_type,
            "headers": headers,
            "rows": ui_rows,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{k}", "desc": f"Cell {k}: {v}", "marks": 1, "editable": True}
                for k, v in list(correct_map.items())[:marks]
            ],
        },
        "sample_answer": worked,
        "ideal_answer": worked,
        "expected_answer": worked,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "hints": hints,
    }
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=6,
    )


def svg_doc_plate(doc_title: str, doc_meta: str, fields: List[Tuple[str, str]], footer: str = "DUPLICATE AUDIT RECORD") -> str:
    """Render an authentic South African Paper & Ink commercial source document SVG."""
    row_h = 23
    h = 98 + len(fields) * row_h
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 {h}" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">',
        f'<rect x="4" y="4" width="532" height="{h - 8}" rx="6" fill="#FFFEF9" stroke="#1E293B" stroke-width="1.8"/>',
        f'<rect x="4" y="4" width="532" height="44" rx="6" fill="#0F172A"/>',
        f'<rect x="4" y="34" width="532" height="14" fill="#0F172A"/>',
        f'<text x="18" y="24" font-size="13" font-weight="bold" fill="#FFFFFF">{_xml_escape(doc_title)}</text>',
        f'<text x="522" y="24" font-size="11" font-weight="bold" text-anchor="end" fill="#FDE68A">{_xml_escape(doc_meta)}</text>',
        '<text x="18" y="40" font-size="9.5" fill="#CBD5E1">OFFICIAL BUSINESS SOURCE DOCUMENT</text>',
    ]
    for i, (lbl, val) in enumerate(fields):
        y = 70 + i * row_h
        bg = "#F8FAFC" if i % 2 == 0 else "#FFFEF9"
        lines.append(f'<rect x="14" y="{y - 15}" width="512" height="21" fill="{bg}" stroke="#E2E8F0" stroke-width="0.6"/>')
        lines.append(f'<text x="22" y="{y}" font-size="11" font-weight="bold" fill="#334155">{_xml_escape(lbl)}:</text>')
        lines.append(f'<text x="516" y="{y}" font-size="11.5" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(val)}</text>')
    fy = h - 18
    lines.append(f'<line x1="14" y1="{fy - 14}" x2="526" y2="{fy - 14}" stroke="#94A3B8" stroke-dasharray="4 3"/>')
    lines.append(f'<text x="270" y="{fy}" font-size="10" font-weight="bold" text-anchor="middle" fill="#13519C">{_xml_escape(footer)}</text>')
    lines.append("</svg>")
    return "".join(lines)


# =============================================================================
# ARCHETYPES 01 – 25
# =============================================================================

def _b01_no_source_doc_no_entry_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(6, 25) * 100
    prompt = (
        f"A new cashier at {s['business']} in {s['area']} claims: 'I remember paying {fmt_r(amt)} cash for cleaning soap this morning, so just enter it into the CPJ without any receipt or till slip.' "
        f"What fundamental accounting principle applies?"
    )
    ans = "No source document, no entry in the books — every journal entry must be backed by written proof"
    opts = [
        "No source document, no entry in the books — every journal entry must be backed by written proof",
        "Verbal claims by employees are recorded directly in the General Ledger Bank account",
        "Amounts under R5 000 do not require receipts or slips in South African accounting",
        "Cash purchases can be guessed at month-end from the Trial Balance",
    ]
    exp = f"Golden rule of bookkeeping: 'No source document, no entry in the books!' Without a slip, invoice, or voucher proving the {fmt_r(amt)} outflow, no legitimate entry can be audited."
    return _make_mcq(
        rng,
        subskill="01_no_source_doc_no_entry_rule",
        title="Golden Rule: No Source Document, No Entry",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think about what prevents fake expenses or theft from entering the journals.",
            "tier_2": "Recall the golden rule: 'No source document, no entry in the books.'",
            "tier_3": ans,
        },
        misconception_tags=["allows_unverified_journal_entries"],
        question_family_id="no_doc_no_entry",
    )


def _b02_essential_fields_on_source_doc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    doc_no = rng.randint(101, 499)
    prompt = (
        f"When auditing source document #{doc_no} at {s['business']}, which complete set of details MUST appear on a valid source document before it can be entered into CRJ or CPJ?"
    )
    ans = "Date, sequential Document Number, Names of parties, Description/Reason, Exact Rand Amount, and Authorisation/Reference"
    opts = [
        "Date, sequential Document Number, Names of parties, Description/Reason, Exact Rand Amount, and Authorisation/Reference",
        "Only the cashier's nickname and a rough estimated price",
        "Only the customer's home address and favourite colour",
        "Only the business logo with no date or document number",
    ]
    exp = f"Document #{doc_no} must record Date, sequential Number, Parties, Reason, Amount, and Authorisation so {s['business']} maintains a verifiable audit trail."
    return _make_mcq(
        rng,
        subskill="02_essential_fields_on_source_doc",
        title="Mandatory Fields on Source Documents",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask: What facts does the bookkeeper need to write Date, Doc No, Details, and Amount in a journal?",
            "tier_2": "Every valid document carries Date, Number, Parties, Description, Amount, and Authorisation.",
            "tier_3": ans,
        },
        misconception_tags=["omits_doc_number_or_date_audit_fields"],
        question_family_id="source_doc_fields",
    )


def _b03_receipt_original_vs_duplicate(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    payer = rng.choice(NAMES)
    amt = rng.randint(8, 35) * 100
    prompt = (
        f"{payer} pays {fmt_r(amt)} cash to {s['business']} for rent/services, and the receptionist writes out a Receipt in the pre-numbered receipt book. "
        f"Who receives the ORIGINAL receipt and what does {s['business']} keep to write up the CRJ?"
    )
    ans = f"{payer} receives the ORIGINAL receipt; {s['business']} keeps the DUPLICATE receipt inside the book"
    opts = [
        f"{payer} receives the ORIGINAL receipt; {s['business']} keeps the DUPLICATE receipt inside the book",
        f"{s['business']} keeps the ORIGINAL receipt; {payer} gets nothing",
        f"Both copies are torn out and handed to {payer}",
        f"{payer} receives the DUPLICATE receipt; {s['business']} records from memory",
    ]
    exp = f"When issuing a Receipt for {fmt_r(amt)}, the payer ({payer}) always gets the Original proof of payment, while {s['business']} retains the Duplicate receipt in its book as the CRJ source document."
    return _make_mcq(
        rng,
        subskill="03_receipt_original_vs_duplicate",
        title="Receipt: Original vs Duplicate Copy",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice who made the payment and needs proof vs who needs a permanent book copy.",
            "tier_2": "Customer/Payer = Original Receipt; Business = Duplicate Receipt (for CRJ).",
            "tier_3": ans,
        },
        misconception_tags=["thinks_business_keeps_original_receipt"],
        question_family_id="receipt_original_duplicate",
    )


def _b04_visual_receipt_plate_reading(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rec_no = rng.randint(204, 899)
    day = rng.randint(3, 25)
    amt = rng.randint(12, 48) * 100
    payer = s["entrepreneur"] if rng.random() < 0.5 else rng.choice(NAMES)
    reason = "Capital contribution" if payer == s["entrepreneur"] else "Rent Income for storeroom"
    expected_acct = "Capital" if payer == s["entrepreneur"] else "Rent Income"
    svg = svg_doc_plate(
        f"DUPLICATE CASH RECEIPT — {s['business']}",
        f"Receipt No. R{rec_no}",
        [
            ("Date", f"{day:02d} May 2026"),
            ("Received From", payer),
            ("Amount in Rands", fmt_r(amt)),
            ("For / Being", reason),
        ],
        footer=f"ISSUED BY {s['business'].upper()} — RETAINED FOR CRJ",
    )
    prompt = (
        f"Inspect Duplicate Cash Receipt No. R{rec_no} issued by {s['business']}. "
        f"Into which Subsidiary Journal and General Ledger Credit account must {fmt_r(amt)} be recorded?"
    )
    ans = f"Cash Receipts Journal (CRJ) — Credit {expected_acct}"
    opts = [
        f"Cash Receipts Journal (CRJ) — Credit {expected_acct}",
        f"Cash Payments Journal (CPJ) — Debit {expected_acct}",
        "Cash Payments Journal (CPJ) — Credit Bank",
        f"Cash Receipts Journal (CRJ) — Credit Drawings",
    ]
    exp = f"Duplicate Receipt R{rec_no} for {fmt_r(amt)} ({reason}) shows cash received by {s['business']} -> CRJ -> Dr Bank, Cr {expected_acct}."
    return _make_mcq(
        rng,
        subskill="04_visual_receipt_plate_reading",
        title="Reading a Duplicate Cash Receipt",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look at 'DUPLICATE CASH RECEIPT' and 'For / Being' on the document.",
            "tier_2": "Duplicate receipts always go into CRJ, crediting the specific reason account.",
            "tier_3": ans,
        },
        misconception_tags=["puts_duplicate_receipt_in_cpj"],
        question_family_id="visual_receipt_plate",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b05_visual_receipt_missing_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rec_no = rng.randint(510, 950)
    months = rng.choice([2, 3, 4])
    monthly_rent = rng.randint(15, 35) * 100
    total = months * monthly_rent
    tenant = rng.choice(NAMES)
    ans = fmt_r(total)
    svg = svg_doc_plate(
        f"DUPLICATE CASH RECEIPT — {s['business']}",
        f"Receipt No. R{rec_no}",
        [
            ("Received From", tenant),
            ("Being", f"{months} months office rent @ {fmt_r(monthly_rent)}/month"),
            ("Payment Method", "Cash / EFT verified"),
            ("Total Amount Received", "R ???"),
        ],
    )
    prompt = (
        f"Examine Duplicate Cash Receipt No. R{rec_no} from {tenant} to {s['business']}. "
        f"Calculate the missing Total Amount Received (`R ???`) that must be entered in the CRJ."
    )
    steps = [
        f"Monthly rent = {fmt_r(monthly_rent)}; Number of months = {months}.",
        f"Total Received = {months} x {fmt_r(monthly_rent)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="05_visual_receipt_missing_calc",
        title="Calculate Missing Total on Cash Receipt",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total}", str(total)],
        steps=steps,
        hints={
            "tier_1": "Read the 'Being' line carefully to see the monthly rate and number of months.",
            "tier_2": f"Multiply {months} months by {fmt_r(monthly_rent)}.",
            "tier_3": f"Total Received = {ans}.",
        },
        misconception_tags=["enters_one_month_instead_of_total_receipt"],
        question_family_id="visual_receipt_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b06_deposit_slip_original_vs_duplicate(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    amt = rng.randint(4, 18) * 1000
    prompt = (
        f"{s['entrepreneur']} takes {fmt_r(amt)} in cash takings from {s['business']} to {bank} and fills out a Bank Deposit Slip in duplicate. "
        f"Which copy does the bank teller keep, and which copy does {s['entrepreneur']} bring back for the business files?"
    )
    ans = f"The bank teller keeps the ORIGINAL deposit slip; {s['entrepreneur']} brings back the bank-stamped DUPLICATE deposit slip"
    opts = [
        f"The bank teller keeps the ORIGINAL deposit slip; {s['entrepreneur']} brings back the bank-stamped DUPLICATE deposit slip",
        f"{s['entrepreneur']} keeps the ORIGINAL deposit slip; the bank teller keeps nothing",
        f"Both slips are shredded once coins are counted at {bank}",
        f"The bank teller keeps the DUPLICATE and hands back an unsigned blank cheque",
    ]
    exp = f"At {bank}, the teller retains the Original deposit slip as the bank's record, stamps the Duplicate copy, and returns that stamped Duplicate ({fmt_r(amt)}) to {s['business']} as proof of banking."
    return _make_mcq(
        rng,
        subskill="06_deposit_slip_original_vs_duplicate",
        title="Bank Deposit Slip: Original vs Stamped Duplicate",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Just like a receipt, the teller needs the original authorisation while the depositor keeps stamped proof.",
            "tier_2": "Bank keeps Original; Business brings back the Stamped Duplicate Deposit Slip.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_depositor_keeps_original_deposit_slip"],
        question_family_id="deposit_slip_flow",
    )


def _b07_visual_deposit_slip_total_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    slip_no = rng.randint(1100, 9800)
    notes = rng.randint(15, 45) * 100
    coins = rng.randint(2, 9) * 50
    total = notes + coins
    ans = fmt_r(total)
    svg = svg_doc_plate(
        f"{bank} — STAMPED DUPLICATE DEPOSIT SLIP",
        f"Slip #{slip_no}",
        [
            ("Credit Account Name", s["business"]),
            ("Bank Notes Deposited", fmt_r(notes)),
            ("Coins Deposited", fmt_r(coins)),
            ("Total Banked", "R ???"),
        ],
        footer=f"TELLER STAMPED COPY — RETAINED BY {s['business'].upper()}",
    )
    prompt = (
        f"Inspect {bank} Deposit Slip #{slip_no} for {s['business']}. "
        f"Calculate the Total Banked (`R ???`) deposited into the business bank account."
    )
    steps = [
        f"Bank Notes = {fmt_r(notes)}; Coins = {fmt_r(coins)}.",
        f"Total Banked = {fmt_r(notes)} + {fmt_r(coins)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="07_visual_deposit_slip_total_calc",
        title="Calculate Bank Deposit Slip Total",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total}", str(total)],
        steps=steps,
        hints={
            "tier_1": "Add Notes Deposited and Coins Deposited together.",
            "tier_2": f"{fmt_r(notes)} + {fmt_r(coins)}.",
            "tier_3": f"Total Banked = {ans}.",
        },
        misconception_tags=["subtracts_coins_or_omits_coins_on_deposit_slip"],
        question_family_id="visual_deposit_slip",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b08_cash_register_roll_vs_till_slip(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    num_cust = rng.randint(18, 55)
    prompt = (
        f"{s['business']} serves {num_cust} cash customers per day. Every customer gets a small paper till slip at checkout, "
        f"while at closing time the bookkeeper prints the internal Cash Register Roll (CRR) summary. "
        f"Which copy is used as the business's CRJ source document?"
    )
    ans = "The internal Cash Register Roll (CRR) retained by the business showing the total cash takings"
    opts = [
        "The internal Cash Register Roll (CRR) retained by the business showing the total cash takings",
        "Only the very last customer's individual till slip",
        "A blank cheque counterfoil from the chequebook",
        "A verbal estimate telephoned to the bank manager",
    ]
    exp = f"Customers receive their individual Till Slips, while {s['business']} retains the Cash Register Roll (CRR) audit tape ({num_cust} transactions summed) to record daily cash takings in the CRJ."
    return _make_mcq(
        rng,
        subskill="08_cash_register_roll_vs_till_slip",
        title="Till Slip vs Cash Register Roll (CRR)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice customers walk away with their individual Till Slips.",
            "tier_2": "The business reads its internal CRR (Cash Register Roll) at day-end for CRJ.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_customer_till_slip_with_crr"],
        question_family_id="crr_vs_till_slip",
    )


def _b09_visual_crr_till_slip_audit(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    crr_no = rng.randint(201, 699)
    item1 = rng.randint(4, 14) * 50
    item2 = rng.randint(3, 10) * 50
    item3 = rng.randint(2, 8) * 50
    daily_tot = item1 + item2 + item3
    ans = fmt_r(daily_tot)
    svg = svg_doc_plate(
        f"CASH REGISTER ROLL (CRR) — {s['business']}",
        f"Z-Total CRR #{crr_no}",
        [
            ("Service Job 1 (Cash)", fmt_r(item1)),
            ("Service Job 2 (Cash)", fmt_r(item2)),
            ("Service Job 3 (Cash)", fmt_r(item3)),
            ("Z-TOTAL DAILY TAKINGS", "R ???"),
        ],
        footer="INTERNAL AUDIT TAPE — POST TO CRJ (CURRENT INCOME)",
    )
    prompt = (
        f"Inspect Cash Register Roll (CRR) #{crr_no} at day-end for {s['business']}. "
        f"Calculate the Z-Total Daily Takings (`R ???`) to enter under Analysis of Receipts and Current Income in the CRJ."
    )
    steps = [
        f"Sum all cash service jobs recorded on CRR #{crr_no}: {fmt_r(item1)} + {fmt_r(item2)} + {fmt_r(item3)}.",
        f"Z-Total Daily Takings = {ans} (posted in CRJ as Current Income).",
    ]
    return _make_typed(
        rng,
        subskill="09_visual_crr_till_slip_audit",
        title="Calculate Daily Cash Register Roll Total",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{daily_tot}", str(daily_tot)],
        steps=steps,
        hints={
            "tier_1": "Add all three cash service jobs listed on the internal audit tape.",
            "tier_2": f"{fmt_r(item1)} + {fmt_r(item2)} + {fmt_r(item3)}.",
            "tier_3": f"Daily Total = {ans}.",
        },
        misconception_tags=["misses_items_when_summing_crr"],
        question_family_id="visual_crr_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b10_cheque_parties_drawer_drawee_payee(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(15, 50) * 100
    role_ask = rng.choice(["Drawer", "Drawee", "Payee"])
    prompt = (
        f"{s['business']} banks with {bank} and issues a cheque of {fmt_r(amt)} to pay {sup} for stationery supplies. "
        f"Identify the **{role_ask}** on this cheque:"
    )
    if role_ask == "Drawer":
        ans = f"{s['business']} (the account holder writing and signing the payment instruction)"
    elif role_ask == "Drawee":
        ans = f"{bank} (the bank ordered to pay the funds out of the account)"
    else:
        ans = f"{sup} (the supplier receiving the {fmt_r(amt)} payment)"
    opts = [
        f"{s['business']} (the account holder writing and signing the payment instruction)",
        f"{bank} (the bank ordered to pay the funds out of the account)",
        f"{sup} (the supplier receiving the {fmt_r(amt)} payment)",
        "SARS (the national tax authority)",
    ]
    exp = f"On a cheque, Drawer = {s['business']} (payer), Drawee = {bank} (paying bank), and Payee = {sup} (recipient)."
    return _make_mcq(
        rng,
        subskill="10_cheque_parties_drawer_drawee_payee",
        title="Three Parties to a Cheque",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Remember: '-er' draws/writes it; '-ee' bank holds it or supplier is paid.",
            "tier_2": "Drawer = payer; Drawee = bank; Payee = recipient.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_drawer_drawee_and_payee"],
        question_family_id="cheque_parties",
    )


def _b11_cheque_vs_counterfoil_retention(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    chq_no = rng.randint(101, 599)
    amt = rng.randint(12, 48) * 100
    prompt = (
        f"After completing Cheque No. {chq_no} for {fmt_r(amt)} payable to {sup}, {s['entrepreneur']} tears out the main cheque for {sup}. "
        f"What part stays bound inside {s['business']}'s book as the CPJ source document?"
    )
    ans = f"The Cheque Counterfoil (stub) for Cheque No. {chq_no}"
    opts = [
        f"The Cheque Counterfoil (stub) for Cheque No. {chq_no}",
        f"The Cash Register Roll (CRR)",
        f"A Duplicate Cash Receipt",
        f"The Original Cheque handed back by {sup}",
    ]
    exp = f"While {sup} receives the cheque to bank, {s['business']} retains the bound Cheque Counterfoil ({chq_no}, {fmt_r(amt)}) to write up the CPJ."
    return _make_mcq(
        rng,
        subskill="11_cheque_vs_counterfoil_retention",
        title="Cheque vs Cheque Counterfoil",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "What paper stub stays attached inside the book when a cheque is torn out?",
            "tier_2": "The Cheque Counterfoil stays with the business for CPJ entries.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_cheque_counterfoil_with_receipt"],
        question_family_id="cheque_counterfoil_rule",
    )


def _b12_visual_cheque_counterfoil_plate(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    chq_no = rng.randint(310, 790)
    bf = rng.randint(25, 60) * 1000
    paid = rng.randint(3, 12) * 1000
    cf = bf - paid
    sup = rng.choice(SUPPLIERS)
    ans = fmt_r(cf)
    svg = svg_doc_plate(
        f"CHEQUE COUNTERFOIL — {s['business']}",
        f"Counterfoil No. {chq_no}",
        [
            ("Brought Forward Balance", fmt_r(bf)),
            ("Pay To", sup),
            ("For", "Trading Equipment / Supplies"),
            ("This Cheque Amount", fmt_r(paid)),
            ("Balance Carried Forward", "R ???"),
        ],
        footer=f"CPJ SOURCE DOCUMENT — STUB NO. {chq_no}",
    )
    prompt = (
        f"Examine Cheque Counterfoil No. {chq_no} of {s['business']} (paid to {sup}). "
        f"Calculate the Balance Carried Forward (`R ???`) remaining on the counterfoil after paying {fmt_r(paid)}."
    )
    steps = [
        f"Brought Forward Balance = {fmt_r(bf)}.",
        f"Subtract This Cheque Amount ({fmt_r(paid)}): {fmt_r(bf)} - {fmt_r(paid)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="12_visual_cheque_counterfoil_plate",
        title="Cheque Counterfoil Balance Calculation",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{cf}", str(cf)],
        steps=steps,
        hints={
            "tier_1": "Subtract the cheque payment from the Brought Forward balance.",
            "tier_2": f"{fmt_r(bf)} - {fmt_r(paid)}.",
            "tier_3": f"Balance Carried Forward = {ans}.",
        },
        misconception_tags=["adds_cheque_payment_to_brought_forward_balance"],
        question_family_id="visual_counterfoil_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b13_crossed_cheque_security_rules(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 1000
    prompt = (
        f"When issuing a high-value cheque of {fmt_r(amt)}, {s['entrepreneur']} draws two parallel lines (`//`) across the face and writes 'Account Payee Only'. "
        f"Why does crossing a cheque increase security?"
    )
    ans = "It prevents the cheque from being cashed over a bank counter — funds may ONLY be paid into a verified bank account"
    opts = [
        "It prevents the cheque from being cashed over a bank counter — funds may ONLY be paid into a verified bank account",
        "It cancels the cheque immediately so no supplier can ever deposit it",
        "It doubles the Rand amount printed on the cheque face",
        "It excuses the business from entering the payment in the CPJ",
    ]
    exp = f"Crossing a {fmt_r(amt)} cheque restricts payout to an actual bank account (cannot be cashed directly over the counter), protecting {s['business']} if lost or stolen."
    return _make_mcq(
        rng,
        subskill="13_crossed_cheque_security_rules",
        title="Security Purpose of Crossing a Cheque",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Consider the difference between handing notes over a counter vs transferring into a named bank account.",
            "tier_2": "A crossed cheque must be deposited into a bank account, creating a traceable path.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_crossing_lines_void_a_cheque"],
        question_family_id="crossed_cheque",
    )


def _b14_stale_post_dated_and_rd_cheques(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 65) * 100
    case = rng.choice(["stale", "post_dated", "rd"])
    if case == "stale":
        prompt = (
            f"A supplier brings a {fmt_r(amt)} cheque issued by {s['business']} 8 months ago to the bank, and the bank refuses to honour it. "
            f"What is a cheque older than 6 months called?"
        )
        ans = "A stale cheque"
        exp = f"In banking practice, a cheque dated more than 6 months earlier (8 months here, {fmt_r(amt)}) is a stale cheque."
    elif case == "post_dated":
        prompt = (
            f"On 10 May, a customer gives {s['business']} a {fmt_r(amt)} cheque dated 30 June, meaning it cannot be deposited until 30 June. "
            f"What kind of cheque is this?"
        )
        ans = "A post-dated cheque"
        exp = f"A cheque carrying a future date (30 June when handed over on 10 May) is a post-dated cheque."
    else:
        prompt = (
            f"{s['business']} deposits a customer's {fmt_r(amt)} cheque, but 3 days later the bank returns it unpaid stamped 'R/D' because the customer lacked funds. "
            f"What does 'R/D' stand for?"
        )
        ans = "Refer to Drawer (dishonoured cheque due to insufficient funds)"
        exp = f"'R/D' stands for Refer to Drawer — the payer's account lacked funds for the {fmt_r(amt)} cheque."
    opts = [
        "A stale cheque",
        "A post-dated cheque",
        "Refer to Drawer (dishonoured cheque due to insufficient funds)",
        "A bearer cash deposit",
    ]
    return _make_mcq(
        rng,
        subskill="14_stale_post_dated_and_rd_cheques",
        title="Stale, Post-Dated & R/D Cheques",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Match: >6 months = stale; future date = post-dated; bounced/insufficient funds = R/D.",
            "tier_2": f"Case involves {case.replace('_', '-')}.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_stale_and_post_dated_cheques"],
        question_family_id="special_cheque_terms",
    )


def _b15_cash_invoice_definition_e_and_oe(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    inv_no = rng.randint(401, 999)
    prompt = (
        f"At the bottom of Cash Invoice #{inv_no} from {sup} to {s['business']}, the letters 'E&OE' are printed. "
        f"What does 'E&OE' stand for and why is it printed?"
    )
    ans = "Errors and Omissions Excepted — protects the seller's right to correct accidental calculation or listing mistakes later"
    opts = [
        "Errors and Omissions Excepted — protects the seller's right to correct accidental calculation or listing mistakes later",
        "Electronic Only Entry — bans customers from paying with notes and coins",
        "End of Enterprise — marks the liquidation date of the supplier",
        "Equal Owners Equity — proves Capital equals Total Liabilities",
    ]
    exp = f"On Invoice #{inv_no} from {sup}, 'E&OE' (Errors and Omissions Excepted) allows the seller to rectify clerical arithmetic or omission errors discovered after billing."
    return _make_mcq(
        rng,
        subskill="15_cash_invoice_definition_e_and_oe",
        title="Cash Invoice & Meaning of E&OE",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Expand each letter: E = Errors, & = and, O = Omissions, E = Excepted.",
            "tier_2": "It protects the issuer against honest clerical pricing/multiplication mistakes.",
            "tier_3": ans,
        },
        misconception_tags=["misinterprets_e_and_oe_abbreviation"],
        question_family_id="cash_invoice_e_and_oe",
    )


def _b16_visual_cash_invoice_plate_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    inv_no = rng.randint(201, 899)
    q1, p1 = rng.randint(4, 9), rng.randint(3, 8) * 50
    q2, p2 = rng.randint(2, 5), rng.randint(4, 9) * 100
    t1 = q1 * p1
    t2 = q2 * p2
    grand = t1 + t2
    ans = fmt_r(grand)
    svg = svg_doc_plate(
        f"CASH INVOICE — {sup}",
        f"Invoice No. INV-{inv_no}",
        [
            ("Buyer", s["business"]),
            (f"{q1} x Paper Reams @ {fmt_r(p1)}", fmt_r(t1)),
            (f"{q2} x Ink Toners @ {fmt_r(p2)}", f"{fmt_r(t2)} (verify)"),
            ("TOTAL PAYABLE (E&OE)", "R ???"),
        ],
        footer=f"PAID IN FULL — RETAIN FOR {s['business'].upper()} CPJ",
    )
    prompt = (
        f"Inspect Cash Invoice INV-{inv_no} from {sup} to {s['business']}. "
        f"Calculate the Total Payable (`R ???`) that {s['business']} must record in its Stationery column in the CPJ."
    )
    steps = [
        f"Line 1: {q1} x {fmt_r(p1)} = {fmt_r(t1)}.",
        f"Line 2: {q2} x {fmt_r(p2)} = {fmt_r(t2)}.",
        f"Total Payable = {fmt_r(t1)} + {fmt_r(t2)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="16_visual_cash_invoice_plate_calc",
        title="Calculate Cash Invoice Grand Total",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{grand}", str(grand)],
        steps=steps,
        hints={
            "tier_1": "Verify both line extensions (Qty x Unit Price) before summing.",
            "tier_2": f"Add {fmt_r(t1)} + {fmt_r(t2)}.",
            "tier_3": f"Total Payable = {ans}.",
        },
        misconception_tags=["forgets_quantity_multiplication_on_invoice"],
        question_family_id="visual_cash_invoice",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b17_eft_proof_of_payment_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(2, 14) * 1000
    prompt = (
        f"In South Africa, most businesses like {s['business']} have replaced paper cheques with Electronic Funds Transfers (EFT) to pay {sup} ({fmt_r(amt)}). "
        f"What document serves as the source document for an EFT payment?"
    )
    ans = "The printed or digital EFT Proof of Payment confirmation (showing Reference No., Date, Amount, and Beneficiary)"
    opts = [
        "The printed or digital EFT Proof of Payment confirmation (showing Reference No., Date, Amount, and Beneficiary)",
        "A blank deposit slip without a bank stamp",
        "The supplier's annual marketing brochure",
        "A petty cash coin count sheet",
    ]
    exp = f"An EFT Proof of Payment confirmation verifies that {fmt_r(amt)} was electronically transferred to {sup}, serving as the CPJ source document alongside the Bank Statement."
    return _make_mcq(
        rng,
        subskill="17_eft_proof_of_payment_purpose",
        title="EFT Proof of Payment as Source Document",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "What downloadable receipt does an online banking app generate immediately after transferring funds?",
            "tier_2": "The EFT Proof of Payment confirmation serves as the CPJ source document.",
            "tier_3": ans,
        },
        misconception_tags=["treats_eft_as_needing_no_source_document"],
        question_family_id="eft_source_doc",
    )


def _b18_visual_eft_confirmation_plate(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    ref_no = f"EFT-{rng.randint(10000, 99999)}"
    amt = rng.randint(15, 55) * 100
    exp_acct = rng.choice(["Water & Electricity", "Telephone", "Advertising"])
    svg = svg_doc_plate(
        f"{bank} — EFT PROOF OF PAYMENT",
        ref_no,
        [
            ("From Account", s["business"]),
            ("To Beneficiary", f"{s['area']} Municipal / Service Desk"),
            ("Payment Reference", f"{exp_acct} Account"),
            ("Amount Transferred", fmt_r(amt)),
        ],
        footer=f"IMMEDIATE DIGITAL PAYMENT — REFERENCE {ref_no}",
    )
    prompt = (
        f"Inspect {bank} EFT Proof of Payment {ref_no} made by {s['business']}. "
        f"How must this {fmt_r(amt)} payment be recorded in {s['business']}'s books?"
    )
    ans = f"In the Cash Payments Journal (CPJ) under {exp_acct} (Dr {exp_acct}, Cr Bank)"
    opts = [
        f"In the Cash Payments Journal (CPJ) under {exp_acct} (Dr {exp_acct}, Cr Bank)",
        f"In the Cash Receipts Journal (CRJ) under Current Income",
        f"In the General Ledger only as Creditors Control",
        "Do not record it because no paper cheque was written",
    ]
    exp = f"EFT {ref_no} proves {s['business']} paid {fmt_r(amt)} for {exp_acct}, so it enters CPJ -> Debit {exp_acct}, Credit Bank."
    return _make_mcq(
        rng,
        subskill="18_visual_eft_confirmation_plate",
        title="Interpreting an EFT Proof of Payment",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check 'From Account' (payer) and 'Payment Reference' on the EFT slip.",
            "tier_2": f"Money left {s['business']}'s bank -> CPJ under {exp_acct}.",
            "tier_3": ans,
        },
        misconception_tags=["omits_eft_from_cpj"],
        question_family_id="visual_eft_plate",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b19_bank_statement_purpose_items(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    amt = rng.randint(15, 45) * 100
    prompt = (
        f"{s['business']} receives its monthly Bank Statement from {bank}. Why does a deposit of {fmt_r(amt)} "
        f"show in the CREDIT (+) column on {bank}'s Bank Statement even though Bank is a DEBIT Asset in {s['business']}'s ledger?"
    )
    ans = f"Because from {bank}'s perspective, customer deposits are money {bank} owes back to {s['business']} (a Liability to the bank)"
    opts = [
        f"Because from {bank}'s perspective, customer deposits are money {bank} owes back to {s['business']} (a Liability to the bank)",
        f"Because {bank} made an arithmetic error when printing the statement",
        f"Because Bank Overdrafts and Bank balances always share the same Debit sign",
        f"Because {s['business']} must enter deposits in the CPJ instead of CRJ",
    ]
    exp = f"The Bank Statement reflects {bank}'s own ledger! When {s['business']} deposits {fmt_r(amt)}, {bank} owes that money to {s['business']} (Liability for {bank} -> Credit)."
    return _make_mcq(
        rng,
        subskill="19_bank_statement_purpose_items",
        title="Bank Statement Perspective (Mirror Image)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask whose books the Bank Statement is printed from: the business's or the bank's?",
            "tier_2": "Deposits into a bank are Liabilities to the bank (owed back to the customer), so the bank credits them.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_bank_statement_uses_business_dr_cr_orientation"],
        question_family_id="bank_statement_perspective",
    )


def _b20_visual_bank_statement_extract(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    open_b = rng.randint(12, 35) * 1000
    dep = rng.randint(6, 18) * 1000
    eft_out = rng.randint(4, 12) * 1000
    chg = rng.randint(2, 6) * 50
    close_b = open_b + dep - eft_out - chg
    ans = fmt_r(close_b)
    svg = svg_doc_plate(
        f"{bank} — MONTHLY BANK STATEMENT EXTRACT",
        s["business"],
        [
            ("Opening Balance (Credit)", fmt_r(open_b)),
            ("+ Customer EFT Deposit (Cr)", fmt_r(dep)),
            ("- Supplier EFT Payment (Dr)", fmt_r(eft_out)),
            ("- Monthly Bank Charges (Dr)", fmt_r(chg)),
            ("Closing Balance", "R ???"),
        ],
        footer="VERIFY AGAINST CRJ & CPJ BEFORE CLOSING MONTH",
    )
    prompt = (
        f"Inspect the {bank} Bank Statement Extract for {s['business']}. "
        f"Calculate the Closing Balance (`R ???`) after accounting for the deposit, supplier payment, and bank charges."
    )
    steps = [
        f"Start with Opening Balance ({fmt_r(open_b)}) + Deposit ({fmt_r(dep)}) = {fmt_r(open_b + dep)}.",
        f"Subtract EFT Payment ({fmt_r(eft_out)}) and Bank Charges ({fmt_r(chg)}): total deductions = {fmt_r(eft_out + chg)}.",
        f"Closing Balance = {fmt_r(open_b + dep)} - {fmt_r(eft_out + chg)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="20_visual_bank_statement_extract",
        title="Calculate Closing Balance on Bank Statement",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{close_b}", str(close_b)],
        steps=steps,
        hints={
            "tier_1": "Add Cr deposits to Opening Balance, and subtract Dr payments and bank charges.",
            "tier_2": f"{fmt_r(open_b)} + {fmt_r(dep)} - {fmt_r(eft_out)} - {fmt_r(chg)}.",
            "tier_3": f"Closing Balance = {ans}.",
        },
        misconception_tags=["forgets_to_deduct_bank_charges_on_statement"],
        question_family_id="visual_bank_statement",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b21_bank_charges_vs_interest_received(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    chg = rng.randint(15, 45) * 10
    intr = rng.randint(12, 38) * 10
    prompt = (
        f"Comparing {bank}'s Bank Statement to its journals, {s['business']} discovers unrecorded Bank Charges of {fmt_r(chg)} "
        f"and Interest Received of {fmt_r(intr)}. Into which journals must BOTH be entered?"
    )
    ans = f"Bank Charges ({fmt_r(chg)}) -> CPJ (Expense); Interest Received ({fmt_r(intr)}) -> CRJ (Income)"
    opts = [
        f"Bank Charges ({fmt_r(chg)}) -> CPJ (Expense); Interest Received ({fmt_r(intr)}) -> CRJ (Income)",
        f"Both Bank Charges and Interest Received -> CRJ",
        f"Bank Charges -> CRJ (Income); Interest Received -> CPJ (Expense)",
        f"Both are ignored because {bank} already deducted/added them",
    ]
    exp = f"Bank Charges ({fmt_r(chg)}) reduce the bank account (Expense -> CPJ), whereas Interest Received ({fmt_r(intr)}) increases the bank account (Income -> CRJ)."
    return _make_mcq(
        rng,
        subskill="21_bank_charges_vs_interest_received",
        title="Recording Bank Charges vs Interest Received",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Charges take money OUT of the account; Interest puts money INTO the account.",
            "tier_2": "Outflows (Bank Charges) -> CPJ; Inflows (Interest Received) -> CRJ.",
            "tier_3": ans,
        },
        misconception_tags=["ignores_bank_charges_or_puts_in_crj"],
        question_family_id="bank_stmt_adjustments",
    )


def _b22_petty_cash_voucher_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(35, 140)
    item = rng.choice(["postage stamps", "milk and tea bags for staff", "local parcel courier tip"])
    prompt = (
        f"The office administrator at {s['business']} spends {fmt_r(amt)} from the locked petty cash box to pay for {item} where no formal machine till slip is issued. "
        f"What internal source document MUST be completed and signed?"
    )
    ans = "A Petty Cash Voucher"
    opts = ["A Petty Cash Voucher", "A Bank Deposit Slip", "A Mortgage Bond Deed", "A Cash Register Z-Roll"]
    exp = f"A signed Petty Cash Voucher for {fmt_r(amt)} ({item}) creates an audit trail inside the petty cash box for minor outlays."
    return _make_mcq(
        rng,
        subskill="22_petty_cash_voucher_purpose",
        title="Petty Cash Voucher as Source Document",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Name the voucher tied specifically to small cash-box disbursements.",
            "tier_2": "Minor cash box payments without formal external receipts use a Petty Cash Voucher.",
            "tier_3": "A Petty Cash Voucher.",
        },
        misconception_tags=["omits_voucher_for_petty_cash_payments"],
        question_family_id="petty_cash_voucher",
    )


def _b23_credit_note_vs_debit_note(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(4, 18) * 100
    prompt = (
        f"{s['business']} returns damaged stationery worth {fmt_r(amt)} to {sup} and asks to reduce the amount owed. "
        f"Which source document does {sup} (the seller) issue to confirm it is reducing {s['business']}'s account by {fmt_r(amt)}?"
    )
    ans = "A Credit Note (reducing the buyer's debt)"
    opts = [
        "A Credit Note (reducing the buyer's debt)",
        "A Cash Register Roll",
        "A Bank Deposit Slip",
        "A Duplicate Wage Receipt",
    ]
    exp = f"When goods worth {fmt_r(amt)} are returned or overcharged on credit, the seller ({sup}) issues a Credit Note confirming the reduction in amount owed."
    return _make_mcq(
        rng,
        subskill="23_credit_note_vs_debit_note",
        title="Credit Note for Returns/Allowances",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think about the seller's document confirming a credit reduction for returned goods.",
            "tier_2": "Seller issues a Credit Note; buyer sends a Debit Note to request that allowance.",
            "tier_3": "A Credit Note.",
        },
        misconception_tags=["confuses_credit_note_with_deposit_slip"],
        question_family_id="credit_note_concept",
    )


def _b24_match_doc_to_holder_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("Receipt", "Customer / Payer", "Business (CRJ)"),
        ("Bank Deposit Slip", "Commercial Bank Teller", "Business (Stamped Duplicate)"),
        ("Cheque & Counterfoil", "Supplier / Payee (Cheque)", "Business (Counterfoil for CPJ)"),
        ("Cash Register Slip / CRR", "Customer (Till Slip)", "Business (Internal CRR for CRJ)"),
    ]
    rng.shuffle(pool)
    headers = ["Source Document Type", "Who Keeps Original?", "Who Keeps Duplicate / Audit Copy?"]
    table_rows = [[(d, "given", False), (orig, "required", True), (dup, "required", True)] for d, orig, dup in pool]
    cell_hints = {}
    for idx, (d, _, _) in enumerate(pool):
        cell_hints[f"t0_r{idx}_c1"] = f"Identify who receives the original {d}."
        cell_hints[f"t0_r{idx}_c2"] = f"Identify who retains the duplicate/stub of {d}."
    prompt = f"Complete the Original vs Duplicate holder table below for source documents handled by {s['business']}."
    return _make_table(
        rng,
        subskill="24_match_doc_to_holder_table",
        title="Source Document Holders (Original vs Duplicate)",
        prompt=prompt,
        journal_type="doc_holders_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Remember the Deposit Slip exception: the BANK teller keeps the original and stamps the duplicate for the business!",
            "tier_2": "Receipts -> Customer gets original; Bank Deposit Slip -> Teller keeps original; Cheque -> Payee gets cheque, business keeps counterfoil.",
            "tier_3": " | ".join(f"{d}: Orig={o}, Dup={du}" for d, o, du in pool),
        },
        misconception_tags=["mixes_original_and_duplicate_holders"],
        question_family_id="doc_holders_table",
    )


def _b25_match_transaction_to_source_doc_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    c_amt = rng.randint(20, 50) * 1000
    s_amt = rng.randint(15, 45) * 100
    t_amt = rng.randint(6, 18) * 100
    b_amt = rng.randint(15, 45) * 10
    rows_pool = [
        (f"Owner invests {fmt_r(c_amt)} Capital.", "Duplicate Receipt / Deposit Slip", "CRJ"),
        (f"Daily cash takings from customers, {fmt_r(s_amt)}.", "Cash Register Roll (CRR)", "CRJ"),
        (f"Paid Telephone bill via EFT, {fmt_r(t_amt)}.", "EFT Proof of Payment", "CPJ"),
        (f"Monthly Bank Charges on Bank Statement, {fmt_r(b_amt)}.", "Bank Statement", "CPJ"),
    ]
    rng.shuffle(rows_pool)
    headers = ["Business Transaction", "Source Document", "Journal (CRJ / CPJ)"]
    table_rows = [[(tx, "given", False), (sd, "required", True), (j, "required", True)] for tx, sd, j in rows_pool]
    cell_hints = {}
    for idx in range(len(rows_pool)):
        cell_hints[f"t0_r{idx}_c1"] = "Name the exact source document retained by the business."
        cell_hints[f"t0_r{idx}_c2"] = "CRJ for receipts, CPJ for payments."
    prompt = f"Match each transaction of {s['business']} in {s['area']} to its retained Source Document and Subsidiary Journal (`CRJ` or `CPJ`)."
    return _make_table(
        rng,
        subskill="25_match_transaction_to_source_doc_table",
        title="Transaction -> Source Document -> Journal Table",
        prompt=prompt,
        journal_type="tx_to_source_doc",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Cash inflows go to CRJ; EFT/bank charge outflows go to CPJ.",
            "tier_2": "Capital = Duplicate Receipt; Takings = CRR; EFT = EFT Proof; Bank Charges = Bank Statement.",
            "tier_3": " | ".join(f"{sd} ({j})" for _, sd, j in rows_pool),
        },
        misconception_tags=["mismatches_source_doc_to_journal"],
        question_family_id="tx_doc_table",
    )


ARCHETYPES_01_25 = {
    "01_no_source_doc_no_entry_rule": _b01_no_source_doc_no_entry_rule,
    "02_essential_fields_on_source_doc": _b02_essential_fields_on_source_doc,
    "03_receipt_original_vs_duplicate": _b03_receipt_original_vs_duplicate,
    "04_visual_receipt_plate_reading": _b04_visual_receipt_plate_reading,
    "05_visual_receipt_missing_calc": _b05_visual_receipt_missing_calc,
    "06_deposit_slip_original_vs_duplicate": _b06_deposit_slip_original_vs_duplicate,
    "07_visual_deposit_slip_total_calc": _b07_visual_deposit_slip_total_calc,
    "08_cash_register_roll_vs_till_slip": _b08_cash_register_roll_vs_till_slip,
    "09_visual_crr_till_slip_audit": _b09_visual_crr_till_slip_audit,
    "10_cheque_parties_drawer_drawee_payee": _b10_cheque_parties_drawer_drawee_payee,
    "11_cheque_vs_counterfoil_retention": _b11_cheque_vs_counterfoil_retention,
    "12_visual_cheque_counterfoil_plate": _b12_visual_cheque_counterfoil_plate,
    "13_crossed_cheque_security_rules": _b13_crossed_cheque_security_rules,
    "14_stale_post_dated_and_rd_cheques": _b14_stale_post_dated_and_rd_cheques,
    "15_cash_invoice_definition_e_and_oe": _b15_cash_invoice_definition_e_and_oe,
    "16_visual_cash_invoice_plate_calc": _b16_visual_cash_invoice_plate_calc,
    "17_eft_proof_of_payment_purpose": _b17_eft_proof_of_payment_purpose,
    "18_visual_eft_confirmation_plate": _b18_visual_eft_confirmation_plate,
    "19_bank_statement_purpose_items": _b19_bank_statement_purpose_items,
    "20_visual_bank_statement_extract": _b20_visual_bank_statement_extract,
    "21_bank_charges_vs_interest_received": _b21_bank_charges_vs_interest_received,
    "22_petty_cash_voucher_purpose": _b22_petty_cash_voucher_purpose,
    "23_credit_note_vs_debit_note": _b23_credit_note_vs_debit_note,
    "24_match_doc_to_holder_table": _b24_match_doc_to_holder_table,
    "25_match_transaction_to_source_doc_table": _b25_match_transaction_to_source_doc_table,
}
