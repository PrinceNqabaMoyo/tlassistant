"""Grade 8 EMS — The Accounting Cycle Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/01. the accounting cycle.md.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import AREAS, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario


def get_ems_scenario(rng: Optional[random.Random] = None) -> Dict[str, Any]:
    s = _raw_ems_scenario(rng)
    first = str(s["entrepreneur"]).split()[0]
    s["business"] = f"{first}'s {s['business_type'].title()}"
    return s

TOPIC_NAME = "the accounting cycle"
TOPIC_KEY = "grade8_ems_accounting_cycle"
LO = "g8_ems_acct_cycle"
TERM = 2
CAPS_WEIGHT_PERCENT = 20

_BANKS = ["FNB", "Absa", "Standard Bank", "Nedbank", "Capitec Business"]


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
        "tier_1": "Trace the step in chronological order: Transaction -> Source Doc -> Journal -> Ledger -> Trial Balance -> Financial Statements.",
        "tier_2": "Remember CRJ records cash received and CPJ records cash paid.",
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
        "subtopic_id": "term2_accounting_cycle",
        "grade": 8,
        "subject": "Economic and Management Sciences",
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT_PERCENT,
        "suggested_duration_mins": out.get("suggested_duration_mins", duration_mins),
        "subskill": subskill,
        "archetype": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": subskill,
        "concept_group": "accounting_cycle",
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 2 > The Accounting Cycle",
        "misconception_tags": misconception_tags or ["accounting_cycle_sequence_error"],
        "diagnostic_tags": ["accounting_cycle", "financial_literacy", "grade8_ems"],
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
        "id": f"g8_ems_cy_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_cy_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_cy_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_cy_{subskill}_{rng.randint(100000, 999999)}",
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


def _svg_cycle_flow(biz: str, highlight_idx: int) -> str:
    """Render Paper & Ink 6-stage accounting cycle flow with dynamic highlight and ??? on next step."""
    stages = [
        "1. Transaction",
        "2. Source Doc",
        "3. Journals",
        "4. General Ledger",
        "5. Trial Balance",
        "6. Fin. Statements",
    ]
    next_idx = (highlight_idx + 1) if highlight_idx < 5 else 0
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 175" width="100%" style="max-width:560px;font-family:Arial,sans-serif;">',
        '<rect x="4" y="4" width="552" height="167" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>',
        '<rect x="4" y="4" width="552" height="32" rx="8" fill="#13519C"/>',
        '<rect x="4" y="24" width="552" height="12" fill="#13519C"/>',
        f'<text x="20" y="25" font-size="12" font-weight="bold" fill="#FFFFFF">{_xml_escape(biz)} — Accounting Cycle Sequence</text>',
    ]
    coords = [(18, 52), (198, 52), (378, 52), (378, 112), (198, 112), (18, 112)]
    for i, st in enumerate(stages):
        x, y = coords[i]
        label = f"Step {i + 1}: ???" if i == next_idx else st
        if i == highlight_idx:
            fill, stroke, txt = "#DBEAFE", "#1D4ED8", "#1E3A8A"
        elif i == next_idx:
            fill, stroke, txt = "#FEF3C7", "#D97706", "#92400E"
        else:
            fill, stroke, txt = "#F8FAFC", "#64748B", "#1E293B"
        lines.append(f'<rect x="{x}" y="{y}" width="164" height="40" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        lines.append(f'<text x="{x + 82}" y="{y + 24}" font-size="11" font-weight="bold" text-anchor="middle" fill="{txt}">{_xml_escape(label)}</text>')
    lines.extend([
        '<line x1="184" y1="72" x2="196" y2="72" stroke="#334155" stroke-width="2"/>',
        '<line x1="364" y1="72" x2="376" y2="72" stroke="#334155" stroke-width="2"/>',
        '<line x1="460" y1="94" x2="460" y2="110" stroke="#334155" stroke-width="2"/>',
        '<line x1="376" y1="132" x2="364" y2="132" stroke="#334155" stroke-width="2"/>',
        '<line x1="196" y1="132" x2="184" y2="132" stroke="#334155" stroke-width="2"/>',
        '</svg>',
    ])
    return "".join(lines)


def _svg_t_account(acct_name: str, dr_entry: str, dr_amt: str, cr_entry: str, cr_amt: str) -> str:
    """Render a crisp Paper & Ink General Ledger T-account SVG."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 155" width="100%" style="max-width:520px;font-family:Arial,sans-serif;">'
        '<rect x="4" y="4" width="512" height="147" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>'
        '<text x="20" y="28" font-size="12" font-weight="bold" fill="#1D4ED8">Dr</text>'
        f'<text x="260" y="28" font-size="13" font-weight="bold" text-anchor="middle" fill="#0F172A">{_xml_escape(acct_name)}</text>'
        '<text x="500" y="28" font-size="12" font-weight="bold" text-anchor="end" fill="#B91C1C">Cr</text>'
        '<line x1="14" y1="38" x2="506" y2="38" stroke="#0F172A" stroke-width="2"/>'
        '<line x1="260" y1="38" x2="260" y2="138" stroke="#0F172A" stroke-width="2"/>'
        f'<text x="24" y="64" font-size="11" fill="#1E293B">{_xml_escape(dr_entry)}</text>'
        f'<text x="248" y="64" font-size="11" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(dr_amt)}</text>'
        f'<text x="272" y="64" font-size="11" fill="#1E293B">{_xml_escape(cr_entry)}</text>'
        f'<text x="496" y="64" font-size="11" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(cr_amt)}</text>'
        '<text x="260" y="130" font-size="9" text-anchor="middle" fill="#64748B">General Ledger T-Account Format (Left = Debit | Right = Credit)</text>'
        '</svg>'
    )


# =============================================================================
# ARCHETYPES 01 – 25
# =============================================================================

def _b01_accounting_cycle_definition_period(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    months = 12
    start_month = rng.choice(["March", "January", "July"])
    prompt = (
        f"{s['business']} in {s['area']} follows a {months}-month financial year starting every {start_month}. "
        f"Which statement accurately defines the Accounting Cycle?"
    )
    ans = "A recurring step-by-step sequence of recording, classifying, and summarising financial transactions throughout a financial period"
    opts = [
        "A recurring step-by-step sequence of recording, classifying, and summarising financial transactions throughout a financial period",
        "A one-time process completed only when a business shuts down permanently",
        "A marketing campaign used to recruit seasonal retail employees",
        "An optional personal shopping list prepared before visiting wholesalers",
    ]
    exp = f"The accounting cycle repeats every financial year ({months} months from {start_month}) at {s['business']} to transform daily transactions into final financial statements."
    return _make_mcq(
        rng,
        subskill="01_accounting_cycle_definition_period",
        title="Accounting Cycle Definition",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice the word 'cycle' — it repeats every accounting period.",
            "tier_2": "It covers recording, classifying, and reporting transactions from start to end of each financial year.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_accounting_cycle_happens_once"],
        question_family_id="cycle_definition",
    )


def _b02_stage_1_financial_transactions(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 75) * 100
    prompt = (
        f"Every accounting cycle at {s['business']} begins at Step 1. Which event initiates Step 1 (a financial transaction)?"
    )
    ans = f"Receiving {fmt_r(amt)} cash from a client for repair services performed in {s['area']}"
    opts = [
        f"Receiving {fmt_r(amt)} cash from a client for repair services performed in {s['area']}",
        "Updating the shop's social media profile picture before opening",
        "Checking the weather forecast for weekend foot traffic",
        "Cleaning dust off the display counters inside the office",
    ]
    exp = f"Step 1 of the cycle is a monetary transaction involving the exchange of goods/services for money ({fmt_r(amt)})."
    return _make_mcq(
        rng,
        subskill="02_stage_1_financial_transactions",
        title="Stage 1: Financial Transactions",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for the event where money, goods, or services are exchanged in Rands.",
            "tier_2": "Step 1 starts with an actual financial transaction.",
            "tier_3": ans,
        },
        misconception_tags=["includes_non_financial_events_as_stage_1"],
        question_family_id="stage_1_transactions",
    )


def _b03_stage_2_source_documents_origin(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(8, 35) * 100
    doc = rng.choice(["duplicate receipt", "cash register slip", "bank deposit slip"])
    prompt = (
        f"Immediately after {s['business']} receives {fmt_r(amt)} from a customer, the clerk completes a {doc}. "
        f"What role does completing this source document play in Stage 2 of the accounting cycle?"
    )
    ans = "It provides original written proof (date, amount, parties) required before any journal entry can be made"
    opts = [
        "It provides original written proof (date, amount, parties) required before any journal entry can be made",
        "It replaces the Balance Sheet at the end of the financial year",
        "It automatically pays all supplier liabilities without bank approval",
        "It deletes the transaction from the General Ledger",
    ]
    exp = f"In Stage 2, the {doc} for {fmt_r(amt)} serves as verifiable audit evidence ('no source document, no entry') to post accurately into the journals."
    return _make_mcq(
        rng,
        subskill="03_stage_2_source_documents_origin",
        title="Stage 2: Source Documents Role",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Why can't a bookkeeper make up journal entries from memory?",
            "tier_2": "Source documents are original written proof verifying date, amount, and transaction details.",
            "tier_3": ans,
        },
        misconception_tags=["skips_source_documents_before_journals"],
        question_family_id="stage_2_source_docs",
    )


def _b04_stage_3_subsidiary_journals_crj_cpj(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    num_docs = rng.randint(18, 45)
    prompt = (
        f"At the end of the week, {s['entrepreneur']} has {num_docs} receipts, cash till slips, and EFT payment advices at {s['business']}. "
        f"In Stage 3 of the accounting cycle, where are these similar daily source documents recorded chronologically BEFORE reaching the General Ledger?"
    )
    ans = "Subsidiary Journals (Cash Receipts Journal and Cash Payments Journal)"
    opts = [
        "Subsidiary Journals (Cash Receipts Journal and Cash Payments Journal)",
        "The Trial Balance summary sheet",
        "The annual Balance Sheet immediately",
        "A personal household shopping notebook",
    ]
    exp = f"All {num_docs} cash inflows and outflows are grouped first into Subsidiary Journals (CRJ and CPJ) during Stage 3 so only monthly totals post to the General Ledger."
    return _make_mcq(
        rng,
        subskill="04_stage_3_subsidiary_journals_crj_cpj",
        title="Stage 3: Subsidiary Journals",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Which books of first entry group similar daily cash receipts and payments together?",
            "tier_2": "Receipts go to CRJ and payments go to CPJ in Stage 3.",
            "tier_3": ans,
        },
        misconception_tags=["posts_source_docs_straight_to_trial_balance"],
        question_family_id="stage_3_journals",
    )


def _b05_stage_4_general_ledger_posting(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    crj_tot = rng.randint(25, 65) * 1000
    prompt = (
        f"At month-end, {s['business']} totals its Cash Receipts Journal (Bank total {fmt_r(crj_tot)}) and prepares to enter the totals into T-accounts. "
        f"What is this Stage 4 book called?"
    )
    ans = "The General Ledger"
    opts = ["The General Ledger", "The Source Document File", "The Cash Budget", "The Stock Take Sheet"]
    exp = f"Posting monthly column totals (like Bank {fmt_r(crj_tot)}) and sundry items into individual T-accounts happens in the General Ledger (Stage 4)."
    return _make_mcq(
        rng,
        subskill="05_stage_4_general_ledger_posting",
        title="Stage 4: General Ledger",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Which book holds a separate T-account for every Asset, Liability, Capital, Income, and Expense?",
            "tier_2": "Journals post at month-end into the General Ledger.",
            "tier_3": "Correct answer: The General Ledger.",
        },
        misconception_tags=["confuses_journals_with_general_ledger"],
        question_family_id="stage_4_ledger",
    )


def _b06_stage_5_trial_balance_check(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    tot = rng.randint(120, 280) * 1000
    prompt = (
        f"After balancing every General Ledger T-account for {s['business']}, the bookkeeper lists all Debit balances and Credit balances side-by-side and confirms both columns equal {fmt_r(tot)}. "
        f"What Stage 5 accounting schedule is being prepared, and why?"
    )
    ans = "The Trial Balance — to verify arithmetic accuracy that Total Debits equal Total Credits"
    opts = [
        "The Trial Balance — to verify arithmetic accuracy that Total Debits equal Total Credits",
        "The Cash Receipts Journal — to record new customer cash receipts",
        "A Bank Deposit Slip — to deposit coins into the commercial bank",
        "The Income Statement — only listing Operating Expenses",
    ]
    exp = f"The Trial Balance lists all General Ledger balances to verify double-entry accuracy (Debit total {fmt_r(tot)} = Credit total {fmt_r(tot)}) before compiling Financial Statements."
    return _make_mcq(
        rng,
        subskill="06_stage_5_trial_balance_check",
        title="Stage 5: Purpose of the Trial Balance",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice both Debit and Credit columns must match before drafting statements.",
            "tier_2": "A Trial Balance tests mathematical equality of Debits and Credits.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_trial_balance_with_balance_sheet"],
        question_family_id="stage_5_trial_balance",
    )


def _b07_stage_6_financial_statements_prep(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    profit = rng.randint(25, 85) * 1000
    assets = rng.randint(140, 300) * 1000
    prompt = (
        f"At the close of Stage 6 for {s['business']} in {s['area']}, {s['entrepreneur']} reviews two final reports: "
        f"one showing a Net Profit of {fmt_r(profit)}, and another showing Total Assets of {fmt_r(assets)} balancing OE + L. "
        f"Name these two Financial Statements:"
    )
    ans = "Income Statement (profit/loss) and Balance Sheet (Assets, Owner's Equity, and Liabilities)"
    opts = [
        "Income Statement (profit/loss) and Balance Sheet (Assets, Owner's Equity, and Liabilities)",
        "Cash Receipts Journal and Cash Payments Journal",
        "Cheque Counterfoil Book and Bank Deposit Register",
        "Daily Price List and Quotation File",
    ]
    exp = f"Stage 6 produces the Income Statement (reporting Net Profit of {fmt_r(profit)}) and the Balance Sheet (reporting Assets of {fmt_r(assets)} = OE + L)."
    return _make_mcq(
        rng,
        subskill="07_stage_6_financial_statements_prep",
        title="Stage 6: Financial Statements",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Which statement calculates Profit/Loss and which shows A = OE + L?",
            "tier_2": "Income Statement (Income - Expenses) + Balance Sheet (A = OE + L).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_journals_with_financial_statements"],
        question_family_id="stage_6_statements",
    )


def _b08_cycle_sequence_next_step(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    stage_names = [
        "Transactions occur",
        "Source Documents",
        "Subsidiary Journals (CRJ/CPJ)",
        "General Ledger",
        "Trial Balance",
        "Financial Statements",
    ]
    highlight_idx = rng.choice([1, 2, 3, 4])
    next_name = stage_names[highlight_idx + 1]
    svg = _svg_cycle_flow(s["business"], highlight_idx)
    prompt = (
        f"Examine the Accounting Cycle sequence schematic for {s['business']}. "
        f"After completing '{stage_names[highlight_idx]}', what is the exact next stage marked '???'?"
    )
    distractors = [st for idx, st in enumerate(stage_names) if idx != highlight_idx + 1][:3]
    opts = [next_name] + distractors
    exp = f"In chronological order, '{stage_names[highlight_idx]}' is followed directly by '{next_name}'."
    return _make_mcq(
        rng,
        subskill="08_cycle_sequence_next_step",
        title="Next Stage in the Accounting Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=next_name,
        explanation=exp,
        hints={
            "tier_1": "Follow the arrows chronologically starting from Step 1 (Transactions).",
            "tier_2": "Sequence: Transactions -> Source Doc -> Journals -> General Ledger -> Trial Balance -> Financial Statements.",
            "tier_3": f"Next stage: {next_name}.",
        },
        misconception_tags=["reverses_ledger_and_trial_balance_order"],
        question_family_id="cycle_next_stage",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b09_cycle_sequence_ordering_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    ordered = [
        ("Stage 1", "Transactions occur (cash/credit exchange)"),
        ("Stage 2", "Source Documents completed as proof"),
        ("Stage 3", "Subsidiary Journals (CRJ and CPJ) written up"),
        ("Stage 4", "General Ledger T-accounts posted"),
        ("Stage 5", "Trial Balance drafted to verify Dr = Cr"),
        ("Stage 6", "Financial Statements (Income Statement & Balance Sheet)"),
    ]
    shift = rng.choice([0, 1])
    window = ordered[shift:shift + 4]
    headers = ["Chronological Stage", "Accounting Cycle Activity"]
    table_rows = [[(stage, "given", False), (act, "required", True)] for stage, act in window]
    cell_hints = {
        f"t0_r{i}_c1": f"State what happens during {st}." for i, (st, _) in enumerate(window)
    }
    prompt = (
        f"Complete the Accounting Cycle sequence table below for {s['business']} in {s['area']} "
        f"by matching each numbered stage to its exact bookkeeping activity "
        f"(choose from: Source Documents completed, Subsidiary Journals written up, General Ledger posted, Trial Balance drafted, Financial Statements prepared, Transactions occur)."
    )
    return _make_table(
        rng,
        subskill="09_cycle_sequence_ordering_table",
        title="Accounting Cycle Stage Ordering Table",
        prompt=prompt,
        journal_type="cycle_sequence",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Move step by step from the original transaction through books of first entry to final reports.",
            "tier_2": "Order: 1. Transactions -> 2. Source Docs -> 3. Journals -> 4. General Ledger -> 5. Trial Balance -> 6. Financial Statements.",
            "tier_3": " | ".join(f"{st}: {a}" for st, a in window),
        },
        misconception_tags=["scrambles_accounting_cycle_order"],
        question_family_id="cycle_order_table",
    )


def _b10_crj_purpose_and_entries(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(2, 18) * 1000
    cases = [
        (f"{s['entrepreneur']} deposits {fmt_r(amt)} into the business bank account as Capital", "Owner cash capital contribution"),
        (f"{s['business']} receives {fmt_r(amt)} cash for plumbing/salon services rendered today", "Cash fees received"),
        (f"{s['business']} receives {fmt_r(amt)} EFT from a tenant for sub-letting spare office space", "Rent income received"),
    ]
    tx, reason = rng.choice(cases)
    prompt = f"{tx}. Which Subsidiary Journal must record this transaction?"
    ans = "Cash Receipts Journal (CRJ)"
    opts = [
        "Cash Receipts Journal (CRJ)",
        "Cash Payments Journal (CPJ)",
        "Creditors Ledger Only",
        "Asset Disposal Register Only",
    ]
    exp = f"Because cash/EFT flows INTO the business bank account ({reason}, {fmt_r(amt)}), it is recorded in the Cash Receipts Journal (CRJ)."
    return _make_mcq(
        rng,
        subskill="10_crj_purpose_and_entries",
        title="Cash Receipts Journal (CRJ) Transactions",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask: Did the business RECEIVE money into Bank/Till, or PAY money out?",
            "tier_2": "All cash and EFT money received enters the Cash Receipts Journal (CRJ).",
            "tier_3": "Correct journal: Cash Receipts Journal (CRJ).",
        },
        misconception_tags=["records_receipts_in_cpj"],
        question_family_id="crj_routing",
    )


def _b11_cpj_purpose_and_entries(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 95) * 100
    cases = [
        f"Paid {fmt_r(amt)} via EFT to the municipality for Water and Electricity",
        f"Bought stationery for {fmt_r(amt)} and paid immediately by business debit card",
        f"{s['entrepreneur']} withdrew {fmt_r(amt)} cash from business bank for personal use (Drawings)",
        f"Paid weekly staff wages of {fmt_r(amt)} out of the business bank account",
    ]
    tx = rng.choice(cases)
    prompt = f"At {s['business']} in {s['area']}, the following happened: {tx}. Which Subsidiary Journal records this?"
    ans = "Cash Payments Journal (CPJ)"
    opts = [
        "Cash Payments Journal (CPJ)",
        "Cash Receipts Journal (CRJ)",
        "Trial Balance Debit Slip",
        "Sales Returns Journal",
    ]
    exp = f"Money left the business Bank account ({fmt_r(amt)}), so it must be recorded in the Cash Payments Journal (CPJ)."
    return _make_mcq(
        rng,
        subskill="11_cpj_purpose_and_entries",
        title="Cash Payments Journal (CPJ) Transactions",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Track the direction of cash: is Bank receiving money or paying money out?",
            "tier_2": "Every cash, card, or EFT outflow (expenses, cash assets, drawings) enters the CPJ.",
            "tier_3": "Correct journal: Cash Payments Journal (CPJ).",
        },
        misconception_tags=["records_payments_in_crj"],
        question_family_id="cpj_routing",
    )


def _b12_crj_vs_cpj_routing_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    c_amt = rng.randint(25, 65) * 1000
    s_amt = rng.randint(18, 48) * 100
    w_amt = rng.randint(12, 32) * 100
    e_amt = rng.randint(4, 15) * 1000

    pool = [
        (f"Owner deposits {fmt_r(c_amt)} as Capital.", "CRJ", "Increase (+)"),
        (f"Cash received for services rendered, {fmt_r(s_amt)}.", "CRJ", "Increase (+)"),
        (f"Paid weekly wages via EFT, {fmt_r(w_amt)}.", "CPJ", "Decrease (-)"),
        (f"Bought workshop equipment cash/EFT, {fmt_r(e_amt)}.", "CPJ", "Decrease (-)"),
    ]
    rng.shuffle(pool)
    headers = ["Transaction", "Journal (CRJ / CPJ)", "Effect on Bank"]
    table_rows = [[(tx, "given", False), (j, "required", True), (eff, "required", True)] for tx, j, eff in pool]
    cell_hints = {}
    for idx, (_, j, eff) in enumerate(pool):
        cell_hints[f"t0_r{idx}_c1"] = "CRJ if cash is received; CPJ if cash is paid."
        cell_hints[f"t0_r{idx}_c2"] = "Bank increases (+) on receipts and decreases (-) on payments."

    prompt = f"Classify each transaction of {s['business']} into the correct Subsidiary Journal (CRJ or CPJ) and its Effect on Bank (`Increase (+)` or `Decrease (-)`)."
    return _make_table(
        rng,
        subskill="12_crj_vs_cpj_routing_table",
        title="CRJ vs CPJ Routing Table",
        prompt=prompt,
        journal_type="journal_routing",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Cash/EFT coming IN -> CRJ (+); Cash/EFT going OUT -> CPJ (-).",
            "tier_2": "Fill CRJ or CPJ in column 2 and Increase (+) or Decrease (-) in column 3.",
            "tier_3": " | ".join(f"Row {i+1}: {j}, {eff}" for i, (_, j, eff) in enumerate(pool)),
        },
        misconception_tags=["swaps_crj_and_cpj_direction"],
        question_family_id="crj_cpj_table",
    )


def _b13_why_journals_precede_ledger(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    tx_count = rng.randint(150, 350)
    prompt = (
        f"{s['business']} in {s['area']} processes around {tx_count} cash receipts and payments each month. "
        f"Explain TWO practical bookkeeping reasons why {s['business']} summarises daily transactions in CRJ and CPJ before posting to the General Ledger rather than posting every single receipt individually into the Bank T-account."
    )
    sample = (
        f"1. Prevents overcrowding in the General Ledger: Summarising {tx_count} transactions in journals allows just ONE monthly Bank total from CRJ and ONE from CPJ to be posted.\n"
        "2. Division of labour and chronological tracking: Multiple clerks can record daily receipts (CRJ) and payments (CPJ) separately while preserving a daily audit trail."
    )
    pts = [
        f"Prevents cluttering the General Ledger Bank account by posting consolidated monthly totals instead of {tx_count} separate lines.",
        "Allows division of duties (different clerks maintaining CRJ and CPJ) and easier chronological tracking.",
    ]
    return _make_rubric(
        rng,
        subskill="13_why_journals_precede_ledger",
        title="Why Subsidiary Journals Precede the General Ledger",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Imagine writing 250 single lines inside one small Bank T-account every month.",
            "tier_2": "Focus on monthly summary totals preventing ledger clutter AND allowing division of work.",
            "tier_3": sample,
        },
        misconception_tags=["misses_monthly_summary_posting_efficiency"],
        question_family_id="journals_before_ledger",
        marks=2,
    )


def _b14_importance_of_subsidiary_journals(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    prompt = (
        f"State THREE management and control benefits {owner} gains by keeping separate Cash Receipts (CRJ) and Cash Payments (CPJ) journals at {s['business']}."
    )
    sample = (
        "1. Effective cash management: Shows total monthly cash inflows vs outflows clearly so shortfalls can be spotted early.\n"
        "2. Fraud & error control: Total Bank column and cross-casting Analysis columns detect missing cash or arithmetic mistakes quickly.\n"
        "3. Informed decision-making: Column analysis reveals top income streams and largest expense categories for budgeting."
    )
    pts = [
        "Tracks cash inflows vs outflows for cash-flow planning.",
        "Detects errors and prevents cash fraud via totals and cross-casting.",
        "Supports management decisions and budgeting using grouped income/expense columns.",
    ]
    return _make_rubric(
        rng,
        subskill="14_importance_of_subsidiary_journals",
        title="Importance of CRJ and CPJ",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about cash flow tracking, spotting errors/fraud, and planning expenses.",
            "tier_2": "Cover cash management, error/fraud control, and decision-making.",
            "tier_3": sample,
        },
        misconception_tags=["treats_journals_as_purely_academic"],
        question_family_id="importance_of_journals",
        marks=3,
    )


def _b15_double_entry_principle_basics(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 19) * 1000
    prompt = (
        f"When {s['business']} buys equipment for {fmt_r(amt)} cash, Equipment is debited with {fmt_r(amt)} and Bank is credited with {fmt_r(amt)}. "
        f"What fundamental accounting principle does this illustrate?"
    )
    ans = "The Double-Entry Principle — every transaction requires an equal Debit entry and Credit entry in at least two accounts"
    opts = [
        "The Double-Entry Principle — every transaction requires an equal Debit entry and Credit entry in at least two accounts",
        "The Single-Entry Shortcut — only cash increases need to be written down",
        "The Cash-Only Rule — credit sales are ignored until next year",
        "The Cost Recovery Rule — expenses must always exceed capital",
    ]
    exp = f"Under the Double-Entry Principle, every financial transaction ({fmt_r(amt)}) affects at least two General Ledger accounts with equal Debit and Credit totals."
    return _make_mcq(
        rng,
        subskill="15_double_entry_principle_basics",
        title="Double-Entry Principle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice there are TWO opposite sides posted for the exact same Rand amount.",
            "tier_2": "For every Debit, there is an equal Credit -> Double-Entry Principle.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_second_entry_of_transaction"],
        question_family_id="double_entry_rule",
    )


def _b16_ledger_t_account_anatomy(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt_dr = rng.randint(15, 45) * 1000
    amt_cr = rng.randint(4, 12) * 1000
    svg = _svg_t_account("Bank (B3)", "Capital (CRJ)", fmt_r(amt_dr), "Total Payments (CPJ)", fmt_r(amt_cr))
    prompt = (
        f"Inspect the General Ledger T-account for {s['business']}. "
        f"Which entry appears on the DEBIT (left-hand) side and what does it represent?"
    )
    ans = f"Capital (CRJ) for {fmt_r(amt_dr)} — representing total cash inflows deposited into Bank"
    opts = [
        f"Capital (CRJ) for {fmt_r(amt_dr)} — representing total cash inflows deposited into Bank",
        f"Total Payments (CPJ) for {fmt_r(amt_cr)} — representing cash outflows",
        f"Only expenses paid in cash appear on the left side of Bank",
        f"Neither side shows cash because Bank is a Nominal account",
    ]
    exp = f"In a General Ledger T-account, the left side is Debit (Dr) and the right side is Credit (Cr). Here Dr shows Capital (CRJ) {fmt_r(amt_dr)}, increasing Bank."
    return _make_mcq(
        rng,
        subskill="16_ledger_t_account_anatomy",
        title="General Ledger T-Account Anatomy",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look at the left-hand side marked Dr vs the right-hand side marked Cr.",
            "tier_2": "Assets like Bank increase on the Debit (left) side when money is received.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_debit_left_and_credit_right_sides"],
        question_family_id="t_account_anatomy",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b17_balance_sheet_vs_nominal_sections(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(3, 18) * 1000
    ask_bs = rng.choice([True, False])
    if ask_bs:
        acct = rng.choice(["Vehicles", "Capital", "Bank", "Drawings", "Equipment"])
        prompt = (
            f"The bookkeeper of {s['business']} is indexing the General Ledger account '{acct}' (balance {fmt_r(amt)}). "
            f"Into which section of the General Ledger does '{acct}' belong?"
        )
        ans = "Balance Sheet Accounts Section (permanent Assets, Owner's Equity, or Liabilities accounts)"
        exp = f"{acct} ({fmt_r(amt)}) is an Asset/Owner's Equity account whose balance carries forward from year to year in the Balance Sheet Accounts Section."
    else:
        acct = rng.choice(["Current Income", "Rent Income", "Telephone", "Water & Electricity", "Stationery"])
        prompt = (
            f"The bookkeeper of {s['business']} is indexing the General Ledger account '{acct}' (total {fmt_r(amt)}). "
            f"Into which section of the General Ledger does '{acct}' belong?"
        )
        ans = "Nominal Accounts Section (Income and Expense accounts used to calculate Profit or Loss)"
        exp = f"{acct} ({fmt_r(amt)}) is an Income or Expense account, belonging to the Nominal Accounts Section."
    opts = [
        "Balance Sheet Accounts Section (permanent Assets, Owner's Equity, or Liabilities accounts)",
        "Nominal Accounts Section (Income and Expense accounts used to calculate Profit or Loss)",
        "Cash Receipts Journal Summary Page",
        "Municipal Tax Return Appendix",
    ]
    return _make_mcq(
        rng,
        subskill="17_balance_sheet_vs_nominal_sections",
        title="Balance Sheet vs Nominal Accounts Section",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Assets, Liabilities, Capital, and Drawings go in Balance Sheet Section; Income and Expenses go in Nominal Section.",
            "tier_2": f"Determine whether {acct} is A/L/OE or Income/Expense.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_balance_sheet_and_nominal_sections"],
        question_family_id="ledger_sections",
    )


def _b18_sort_accounts_ledger_sections_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("Capital", "Balance Sheet Section", "Owner's Equity"),
        ("Vehicles", "Balance Sheet Section", "Asset"),
        ("Current Income", "Nominal Section", "Income"),
        ("Wages", "Nominal Section", "Expense"),
        ("Bank", "Balance Sheet Section", "Asset"),
        ("Telephone", "Nominal Section", "Expense"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Account Name", "General Ledger Section", "Accounting Element"]
    table_rows = [[(a, "given", False), (sec, "required", True), (el, "required", True)] for a, sec, el in chosen]
    cell_hints = {
        f"t0_r{i}_c1": f"Write 'Balance Sheet Section' (A/OE/L) or 'Nominal Section' (Income/Expense) for {a}."
        for i, (a, _, _) in enumerate(chosen)
    }
    for i, (a, _, _) in enumerate(chosen):
        cell_hints[f"t0_r{i}_c2"] = f"Specify Asset, Liability, Owner's Equity, Income, or Expense for {a}."
    prompt = f"Sort each account of {s['business']} in {s['area']} into its General Ledger Section and Accounting Element."
    return _make_table(
        rng,
        subskill="18_sort_accounts_ledger_sections_table",
        title="General Ledger Sections Sorting Table",
        prompt=prompt,
        journal_type="ledger_sections",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Assets, OE, and Liabilities = Balance Sheet Section; Income and Expenses = Nominal Section.",
            "tier_2": "Classify every account by element first, then match to its ledger section.",
            "tier_3": " | ".join(f"{a}: {sec} ({el})" for a, sec, el in chosen),
        },
        misconception_tags=["puts_income_or_expenses_in_balance_sheet_section"],
        question_family_id="ledger_sections_table",
    )


def _b19_debit_credit_asset_increase_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    asset = rng.choice(["Vehicles", "Equipment", "Bank"])
    amt = rng.randint(12, 55) * 1000
    svg = _svg_t_account(asset, "Increase (+)", fmt_r(amt), "Decrease (-)", "R0")
    prompt = (
        f"Look at the General Ledger rule shown in the T-account for {asset} at {s['business']}. "
        f"When {asset} INCREASES by {fmt_r(amt)}, which side of the {asset} T-account is posted?"
    )
    ans = "Debit side (left-hand side)"
    opts = [
        "Debit side (left-hand side)",
        "Credit side (right-hand side)",
        "Neither side — only recorded in the Income Statement",
        "Credit side only if bought for cash",
    ]
    exp = f"{asset} is an Asset. All Assets increase on the Debit (left) side (+{fmt_r(amt)}) and decrease on the Credit (right) side."
    return _make_mcq(
        rng,
        subskill="19_debit_credit_asset_increase_rule",
        title="Debit/Credit Rule for Assets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Use the rule DEAD: Debits increase Expenses, Assets, and Drawings.",
            "tier_2": f"Since {asset} is an Asset, increases go on the left (Debit) side.",
            "tier_3": "Debit side (left-hand side).",
        },
        misconception_tags=["credits_asset_increase"],
        question_family_id="asset_dr_cr_rule",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b20_debit_credit_equity_income_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(8, 30) * 1000
    acct = rng.choice(["Capital (Owner's Equity)", "Current Income (Income)", "Rent Income (Income)"])
    prompt = (
        f"When {s['business']} records an increase of {fmt_r(amt)} in {acct}, which side of that General Ledger T-account must be posted?"
    )
    ans = "Credit side (right-hand side)"
    opts = [
        "Credit side (right-hand side)",
        "Debit side (left-hand side)",
        "Only noted in the Trial Balance",
        "Debited twice to match the bank deposit slip",
    ]
    exp = f"Under CLIC (Credit increases Liabilities, Income, and Capital/Owner's Equity), an increase in {acct} of {fmt_r(amt)} is posted to the Credit (right) side."
    return _make_mcq(
        rng,
        subskill="20_debit_credit_equity_income_rule",
        title="Debit/Credit Rule for Capital & Income",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Remember CLIC: Credits increase Liabilities, Income, and Capital.",
            "tier_2": "Capital and Income both grow on the Credit (right) side.",
            "tier_3": "Credit side (right-hand side).",
        },
        misconception_tags=["debits_income_or_capital_increase"],
        question_family_id="equity_income_cr_rule",
    )


def _b21_debit_credit_expense_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 100
    exp_acct = rng.choice(["Telephone", "Stationery", "Wages", "Water & Electricity"])
    prompt = (
        f"{s['business']} pays {fmt_r(amt)} for {exp_acct} via EFT. "
        f"Why is the {exp_acct} T-account DEBITED while Bank is CREDITED?"
    )
    ans = f"Expenses increase on the Debit side (reducing Owner's Equity) while Bank (an Asset) decreases on the Credit side"
    opts = [
        f"Expenses increase on the Debit side (reducing Owner's Equity) while Bank (an Asset) decreases on the Credit side",
        f"Expenses are Liabilities so they decrease on the Debit side",
        f"Bank increases when money is paid out, so Bank is Credited",
        f"Expenses never enter the General Ledger",
    ]
    exp = f"{exp_acct} ({fmt_r(amt)}) is an Expense (DEAD -> Debit increases Expenses) and paying reduces Bank (Asset decreases on Credit)."
    return _make_mcq(
        rng,
        subskill="21_debit_credit_expense_rule",
        title="Debit/Credit Rule for Expenses",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check both halves: Expense increasing vs Asset (Bank) decreasing.",
            "tier_2": "Expenses increase on Debit; Assets (Bank) decrease on Credit.",
            "tier_3": ans,
        },
        misconception_tags=["credits_expense_payments"],
        question_family_id="expense_dr_rule",
    )


def _b22_trace_capital_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(40, 120) * 1000
    prompt = (
        f"Trace the transaction: '{s['entrepreneur']} deposits {fmt_r(amt)} as starting Capital into the bank account of {s['business']}.' "
        f"Which complete cycle chain (Source Doc -> Journal -> Ledger Accounts) is correct?"
    )
    ans = "Duplicate Receipt / Bank Deposit Slip -> CRJ -> Debit Bank, Credit Capital"
    opts = [
        "Duplicate Receipt / Bank Deposit Slip -> CRJ -> Debit Bank, Credit Capital",
        "Cheque Counterfoil / EFT -> CPJ -> Debit Capital, Credit Bank",
        "Cash Invoice -> CPJ -> Debit Equipment, Credit Creditors",
        "Bank Statement -> Trial Balance directly (skipping CRJ)",
    ]
    exp = f"Starting Capital of {fmt_r(amt)} received by {s['business']} produces a Duplicate Receipt (CRJ) and debits Bank (Asset +) while crediting Capital (OE +)."
    return _make_mcq(
        rng,
        subskill="22_trace_capital_through_cycle",
        title="Trace Capital Through the Accounting Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "The business RECEIVED money from the owner -> which journal and which account increases?",
            "tier_2": "Receipt/Deposit -> CRJ -> Dr Bank (Asset+), Cr Capital (OE+).",
            "tier_3": ans,
        },
        misconception_tags=["puts_capital_in_cpj_or_debits_capital"],
        question_family_id="trace_capital",
    )


def _b23_trace_vehicle_purchase_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(85, 210) * 1000
    dealer = rng.choice(SUPPLIERS)
    prompt = (
        f"Trace the transaction: '{s['business']} bought a delivery vehicle from {dealer} for {fmt_r(amt)} and paid via EFT.' "
        f"Which cycle chain is completely accurate?"
    )
    ans = "EFT Confirmation / Cash Invoice -> CPJ -> Debit Vehicles, Credit Bank"
    opts = [
        "EFT Confirmation / Cash Invoice -> CPJ -> Debit Vehicles, Credit Bank",
        "Duplicate Receipt -> CRJ -> Debit Bank, Credit Vehicles",
        "Cash Register Roll -> CRJ -> Debit Equipment, Credit Current Income",
        "EFT Confirmation -> CPJ -> Debit Operating Expenses, Credit Capital",
    ]
    exp = f"Paying {fmt_r(amt)} to {dealer} reduces Bank -> CPJ -> Debit Vehicles (Fixed Asset +) and Credit Bank (Current Asset -)."
    return _make_mcq(
        rng,
        subskill="23_trace_vehicle_purchase_through_cycle",
        title="Trace Vehicle Purchase Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash left Bank to buy a Fixed Asset (Vehicles).",
            "tier_2": "Payment -> CPJ -> Dr Vehicles (Asset +), Cr Bank (Asset -).",
            "tier_3": ans,
        },
        misconception_tags=["treats_vehicle_purchase_as_expense_or_crj"],
        question_family_id="trace_vehicle",
    )


def _b24_trace_services_rendered_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 65) * 100
    prompt = (
        f"Trace the transaction: '{s['business']} received {fmt_r(amt)} cash from clients for services rendered today.' "
        f"Select the accurate Source Document -> Journal -> General Ledger sequence."
    )
    ans = "Cash Register Roll (CRR) / Duplicate Receipt -> CRJ -> Debit Bank, Credit Current Income"
    opts = [
        "Cash Register Roll (CRR) / Duplicate Receipt -> CRJ -> Debit Bank, Credit Current Income",
        "Bank Deposit Slip -> CPJ -> Debit Current Income, Credit Bank",
        "EFT Payment Advice -> CPJ -> Debit Bank, Credit Sales",
        "Cheque Counterfoil -> CRJ -> Debit Wages, Credit Bank",
    ]
    exp = f"Cash received for services ({fmt_r(amt)}) is backed by CRR/Duplicate Receipt -> CRJ -> Dr Bank, Cr Current Income."
    return _make_mcq(
        rng,
        subskill="24_trace_services_rendered_through_cycle",
        title="Trace Services Rendered Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash received by a service enterprise enters the CRJ.",
            "tier_2": "CRR / Duplicate Receipt -> CRJ -> Dr Bank (+), Cr Current Income (+).",
            "tier_3": ans,
        },
        misconception_tags=["credits_sales_for_service_business_or_uses_cpj"],
        question_family_id="trace_services",
    )


def _b25_trace_telephone_payment_through_cycle(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(6, 22) * 100
    prompt = (
        f"Trace the transaction: '{s['business']} paid the monthly Telephone bill of {fmt_r(amt)} via EFT.' "
        f"Identify the exact Source Document -> Journal -> Ledger posting."
    )
    ans = "EFT Proof of Payment / Bank Statement -> CPJ -> Debit Telephone, Credit Bank"
    opts = [
        "EFT Proof of Payment / Bank Statement -> CPJ -> Debit Telephone, Credit Bank",
        "Duplicate Receipt -> CRJ -> Debit Bank, Credit Telephone",
        "Cash Register Roll -> CPJ -> Debit Bank, Credit Capital",
        "Deposit Slip -> CRJ -> Debit Telephone, Credit Drawings",
    ]
    exp = f"Paying Telephone ({fmt_r(amt)}) via EFT produces an EFT Confirmation -> CPJ -> Debit Telephone (Expense + / OE -) and Credit Bank (Asset -)."
    return _make_mcq(
        rng,
        subskill="25_trace_telephone_payment_through_cycle",
        title="Trace Expense Payment Through Cycle",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Cash left the business bank account for a monthly expense.",
            "tier_2": "EFT Proof -> CPJ -> Dr Telephone (Expense), Cr Bank (Asset -).",
            "tier_3": ans,
        },
        misconception_tags=["swaps_telephone_and_bank_dr_cr"],
        question_family_id="trace_telephone",
    )


ARCHETYPES_01_25 = {
    "01_accounting_cycle_definition_period": _b01_accounting_cycle_definition_period,
    "02_stage_1_financial_transactions": _b02_stage_1_financial_transactions,
    "03_stage_2_source_documents_origin": _b03_stage_2_source_documents_origin,
    "04_stage_3_subsidiary_journals_crj_cpj": _b04_stage_3_subsidiary_journals_crj_cpj,
    "05_stage_4_general_ledger_posting": _b05_stage_4_general_ledger_posting,
    "06_stage_5_trial_balance_check": _b06_stage_5_trial_balance_check,
    "07_stage_6_financial_statements_prep": _b07_stage_6_financial_statements_prep,
    "08_cycle_sequence_next_step": _b08_cycle_sequence_next_step,
    "09_cycle_sequence_ordering_table": _b09_cycle_sequence_ordering_table,
    "10_crj_purpose_and_entries": _b10_crj_purpose_and_entries,
    "11_cpj_purpose_and_entries": _b11_cpj_purpose_and_entries,
    "12_crj_vs_cpj_routing_table": _b12_crj_vs_cpj_routing_table,
    "13_why_journals_precede_ledger": _b13_why_journals_precede_ledger,
    "14_importance_of_subsidiary_journals": _b14_importance_of_subsidiary_journals,
    "15_double_entry_principle_basics": _b15_double_entry_principle_basics,
    "16_ledger_t_account_anatomy": _b16_ledger_t_account_anatomy,
    "17_balance_sheet_vs_nominal_sections": _b17_balance_sheet_vs_nominal_sections,
    "18_sort_accounts_ledger_sections_table": _b18_sort_accounts_ledger_sections_table,
    "19_debit_credit_asset_increase_rule": _b19_debit_credit_asset_increase_rule,
    "20_debit_credit_equity_income_rule": _b20_debit_credit_equity_income_rule,
    "21_debit_credit_expense_rule": _b21_debit_credit_expense_rule,
    "22_trace_capital_through_cycle": _b22_trace_capital_through_cycle,
    "23_trace_vehicle_purchase_through_cycle": _b23_trace_vehicle_purchase_through_cycle,
    "24_trace_services_rendered_through_cycle": _b24_trace_services_rendered_through_cycle,
    "25_trace_telephone_payment_through_cycle": _b25_trace_telephone_payment_through_cycle,
}
