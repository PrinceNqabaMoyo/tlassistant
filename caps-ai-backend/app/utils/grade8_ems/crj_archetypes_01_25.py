"""Grade 8 EMS - Cash Receipts Journal (Service Business): Archetypes 01 to 25.

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/
03. Cash receipts journal for a services business 1.md and 2.md.
Zero-LLM, 100% deterministic, South African Rand (R) contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "Cash receipts journal for a services business 1"
SUBTOPIC_ID = "term2_crj"

CRJ_HEADERS = [
    "Doc No",
    "Day",
    "Details",
    "Fol.",
    "Analysis of Receipts",
    "Bank",
    "Current Income",
    "Sundry Amount",
    "Sundry Details",
]

_MONTHS = [
    ("March 2025", "March"),
    ("April 2025", "April"),
    ("May 2025", "May"),
    ("June 2025", "June"),
    ("July 2025", "July"),
    ("August 2025", "August"),
    ("September 2025", "September"),
]

_BANKS = ["First National Bank", "Standard Bank", "Nedbank", "Absa Bank", "Capitec Business"]

_TENANTS = ["T. Ndlovu", "M. van der Merwe", "R. Delport", "K. Mokoena", "S. Naidoo", "P. Botha"]

_SERVICE_DESCS = [
    ("hair styling services", "Hair Studio"),
    ("electrical repairs", "Electrical Services"),
    ("plumbing call-out services", "Plumbing Solutions"),
    ("car wash & valeting services", "Auto Shine"),
    ("gardening & landscaping services", "Green Thumb Services"),
    ("tailoring & alteration services", "Stitch Craft"),
    ("computer repair services", "TechFix Workshop"),
]


def _fmt_r(amount: int | float) -> str:
    """Format Rand amounts cleanly with space thousands separator."""
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _biz_ctx(rng: random.Random) -> Dict[str, Any]:
    """Build deterministic South African service business context."""
    sc = get_ems_scenario(rng)
    svc_desc, suffix = rng.choice(_SERVICE_DESCS)
    month_full, month_short = rng.choice(_MONTHS)
    surname = sc["entrepreneur"].split()[-1]
    biz_name = f"{surname} {suffix}"
    return {
        **sc,
        "biz_name": biz_name,
        "svc_desc": svc_desc,
        "month_full": month_full,
        "month_short": month_short,
        "bank_name": rng.choice(_BANKS),
        "tenant": rng.choice(_TENANTS),
        "crj_no": f"CRJ{rng.randint(1, 9)}",
    }


def _cell(
    r_i: int,
    c_i: int,
    expected: str,
    *,
    editable: bool = True,
    is_money: bool = False,
) -> Dict[str, Any]:
    """Create a normalized 2D ledger cell dictionary."""
    return {
        "cell_id": f"r{r_i}_c{c_i}",
        "value": "" if editable else expected,
        "expected": expected,
        "editable": editable,
        "prefilled": not editable,
        "required": editable and expected != "",
        "must_be_empty": editable and expected == "",
        "type": "currency" if is_money else "text",
    }


def _md_table(headers: List[str], str_rows: List[List[str]]) -> str:
    """Render a clean Markdown table for worked solutions and sample answers."""
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = ["| " + " | ".join(cell if cell != "" else "—" for cell in r) + " |" for r in str_rows]
    return "\n".join([head, sep] + body)


def _crj_flow_svg(biz_name: str, crj_no: str, n_receipts: int, bank_total: int, ci_total: int, sun_total: int) -> str:
    """Context SVG showing how multiple daily receipts consolidate into General Ledger totals."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 210" width="640" height="210">'
        '<rect width="640" height="210" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="320" y="26" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{biz_name} — {crj_no} Summary Flow</text>'
        '<rect x="20" y="48" width="175" height="126" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="107" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e40af">Source Documents</text>'
        f'<text x="107" y="96" font-size="11" text-anchor="middle" fill="#1e293b">{n_receipts} cash receipts</text>'
        '<text x="107" y="116" font-size="11" text-anchor="middle" fill="#1e293b">Receipts, CRR &amp; BS</text>'
        '<text x="107" y="142" font-size="11" font-weight="bold" text-anchor="middle" fill="#1d4ed8">Recorded daily</text>'
        '<path d="M200 110 L234 110" stroke="#475569" stroke-width="2" marker-end="url(#arr)"/>'
        '<rect x="238" y="48" width="170" height="126" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>'
        f'<text x="323" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#065f46">{crj_no} Totals</text>'
        f'<text x="323" y="98" font-size="11" text-anchor="middle" fill="#0f172a">Bank: {_fmt_r(bank_total)}</text>'
        f'<text x="323" y="120" font-size="11" text-anchor="middle" fill="#0f172a">Current Income: {_fmt_r(ci_total)}</text>'
        f'<text x="323" y="142" font-size="11" text-anchor="middle" fill="#0f172a">Sundry: {_fmt_r(sun_total)}</text>'
        '<path d="M412 110 L446 110" stroke="#475569" stroke-width="2"/>'
        '<rect x="450" y="48" width="170" height="126" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>'
        '<text x="535" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#854d0e">General Ledger</text>'
        '<text x="535" y="98" font-size="11" text-anchor="middle" fill="#1e293b">1 monthly Bank Dr</text>'
        '<text x="535" y="120" font-size="11" text-anchor="middle" fill="#1e293b">1 Current Income Cr</text>'
        '<text x="535" y="142" font-size="11" text-anchor="middle" fill="#1e293b">Sundry items posted Cr</text>'
        '</svg>'
    )


def _receipt_svg(
    biz_name: str,
    doc_no: str,
    date_str: str,
    received_from: str,
    amount: int,
    reason: str,
    signed_by: str,
) -> str:
    """Context SVG rendering a parameterized South African Duplicate Receipt slip."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 220" width="600" height="220">'
        '<rect width="600" height="220" rx="10" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="0" y="0" width="600" height="44" rx="8" fill="#1e3a8a"/>'
        f'<text x="20" y="28" font-size="15" font-weight="bold" fill="#ffffff">DUPLICATE RECEIPT — {biz_name}</text>'
        f'<text x="580" y="28" font-size="14" font-weight="bold" text-anchor="end" fill="#fde047">No: {doc_no}</text>'
        f'<text x="24" y="74" font-size="12" fill="#334155">Date: <tspan font-weight="bold" fill="#0f172a">{date_str}</tspan></text>'
        f'<text x="24" y="102" font-size="12" fill="#334155">Received from: <tspan font-weight="bold" fill="#0f172a">{received_from}</tspan></text>'
        f'<text x="24" y="130" font-size="12" fill="#334155">The sum of: <tspan font-weight="bold" fill="#0f172a">{_fmt_r(amount)}</tspan></text>'
        f'<text x="24" y="158" font-size="12" fill="#334155">Being payment for: <tspan font-weight="bold" fill="#0f172a">{reason}</tspan></text>'
        '<line x1="24" y1="184" x2="576" y2="184" stroke="#cbd5e1" stroke-width="1"/>'
        f'<text x="24" y="204" font-size="11" fill="#475569">Signed: {signed_by}</text>'
        f'<text x="576" y="204" font-size="13" font-weight="bold" text-anchor="end" fill="#047857">{_fmt_r(amount)}</text>'
        '</svg>'
    )


def _crr_slip_svg(biz_name: str, doc_no: str, date_str: str, items: List[Tuple[str, int]]) -> str:
    """Context SVG rendering a Cash Register Roll (till slip) with itemized service fees."""
    total = sum(a for _, a in items)
    rows_svg = []
    y = 84
    for label, amt in items:
        rows_svg.append(
            f'<text x="40" y="{y}" font-size="12" fill="#1e293b">{label}</text>'
            f'<text x="400" y="{y}" font-size="12" font-weight="bold" text-anchor="end" fill="#0f172a">{_fmt_r(amt)}</text>'
        )
        y += 24
    h = max(190, y + 54)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 {h}" width="440" height="{h}">'
        f'<rect width="440" height="{h}" rx="8" fill="#fefce8" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="220" y="28" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{biz_name}</text>'
        f'<text x="220" y="48" font-size="11" text-anchor="middle" fill="#475569">CASH REGISTER ROLL ({doc_no}) — {date_str}</text>'
        '<line x1="30" y1="60" x2="410" y2="60" stroke="#94a3b8" stroke-dasharray="4 3"/>'
        + "".join(rows_svg)
        + f'<line x1="30" y1="{y}" x2="410" y2="{y}" stroke="#0f172a" stroke-width="1.5"/>'
        + f'<text x="40" y="{y + 24}" font-size="13" font-weight="bold" fill="#0f172a">DAILY TILL TOTAL</text>'
        + f'<text x="400" y="{y + 24}" font-size="13" font-weight="bold" text-anchor="end" fill="#047857">{_fmt_r(total)}</text>'
        + '</svg>'
    )


def _bank_stmt_svg(
    bank_name: str,
    biz_name: str,
    month_full: str,
    entries: List[Tuple[str, str, int]],
) -> str:
    """Context SVG rendering a parameterized Bank Statement credit extract."""
    rows_svg = []
    y = 86
    for dt, desc, amt in entries:
        rows_svg.append(
            f'<text x="24" y="{y}" font-size="11" fill="#1e293b">{dt}</text>'
            f'<text x="95" y="{y}" font-size="11" fill="#1e293b">{desc}</text>'
            f'<text x="576" y="{y}" font-size="11" font-weight="bold" text-anchor="end" fill="#047857">+{_fmt_r(amt)}</text>'
        )
        y += 24
    h = max(170, y + 26)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {h}" width="600" height="{h}">'
        f'<rect width="600" height="{h}" rx="8" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>'
        '<rect x="0" y="0" width="600" height="42" rx="6" fill="#0f766e"/>'
        f'<text x="20" y="26" font-size="13" font-weight="bold" fill="#ffffff">{bank_name} — Account Statement ({month_full})</text>'
        f'<text x="24" y="62" font-size="11" font-weight="bold" fill="#475569">Account Holder: {biz_name}</text>'
        '<text x="576" y="62" font-size="11" font-weight="bold" text-anchor="end" fill="#475569">Credit (Deposit)</text>'
        '<line x1="20" y1="68" x2="580" y2="68" stroke="#cbd5e1"/>'
        + "".join(rows_svg)
        + '</svg>'
    )


def _build_mcq(
    rng: random.Random,
    *,
    qid_prefix: str,
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
    caps_weight: int = 25,
    diagram_spec: Optional[Dict[str, Any]] = None,
    topic_name: str = TOPIC_NAME,
    subtopic_id: str = SUBTOPIC_ID,
) -> Dict[str, Any]:
    options = [correct_text] + list(distractors)
    rng.shuffle(options)
    c_idx = options.index(correct_text)
    letter = chr(65 + c_idx)
    ans_full = f"{letter}. {correct_text}"
    worked = f"**{ans_full}** [{marks} marks]\n\n{explanation}"
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": topic_name,
        "topic_id": "grade8_ems",
        "subtopic_id": subtopic_id,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_crj_{subskill}",
        "question_type": "mcq",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans_full,
        "expected_answer": ans_full,
        "sample_answer": ans_full,
        "worked_solution": worked,
        "explanation": worked,
        "canonical_solution": worked,
        "marks": marks,
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "cash_receipts_journal", "service_business"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _build_short(
    rng: random.Random,
    *,
    qid_prefix: str,
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
    caps_weight: int = 25,
    diagram_spec: Optional[Dict[str, Any]] = None,
    topic_name: str = TOPIC_NAME,
    subtopic_id: str = SUBTOPIC_ID,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": topic_name,
        "topic_id": "grade8_ems",
        "subtopic_id": subtopic_id,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_crj_{subskill}",
        "question_type": qtype,
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "correct_answer": expected_answer,
        "expected_answer": expected_answer,
        "sample_answer": expected_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "cash_receipts_journal", "service_business"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _build_table(
    rng: random.Random,
    *,
    qid_prefix: str,
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
    qtype: str = "journal",
    journal_type: str = "crj",
    term: int = 2,
    caps_weight: int = 25,
    diagram_spec: Optional[Dict[str, Any]] = None,
    topic_name: str = TOPIC_NAME,
    subtopic_id: str = SUBTOPIC_ID,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": topic_name,
        "topic_id": "grade8_ems",
        "subtopic_id": subtopic_id,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_crj_{subskill}",
        "question_type": qtype,
        "modality": "ledger",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "journal": {
            "journal_type": journal_type,
            "headers": headers,
            "rows": rows,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "correct_answer": sample_answer,
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
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "cash_receipts_journal", "ledger_table"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _crj_journal_question(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    row_specs: List[Tuple[List[str], List[int], Dict[int, str]]],
    explanation_notes: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    diagram_spec: Optional[Dict[str, Any]] = None,
    topic_name: str = TOPIC_NAME,
    subtopic_id: str = SUBTOPIC_ID,
) -> Dict[str, Any]:
    """Build a 2D interactive CRJ table question from row specifications.

    Each item in `row_specs` is:
      (values_9_cols, prefilled_col_indices, custom_cell_hints_by_col)
    """
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    str_rows: List[List[str]] = []
    marking_points: List[Dict[str, Any]] = []
    money_cols = {4, 5, 6, 7}

    default_col_hints = {
        0: "Enter the source document code (e.g. R01, CRR, BS, or leave blank on a Totals row).",
        1: "Enter the day of the month as a number (or leave blank on a Totals row).",
        2: "Enter the name of the payer/source (or 'Services rendered' for CRR).",
        3: "Enter the folio reference only for Sundry items (e.g. B1, N2) or leave blank.",
        4: "Enter till/cash receipts here; leave blank for direct deposits or on a Totals row.",
        5: "Enter the daily deposit total banked on that day (or the Bank column total).",
        6: "Enter service fee income here; leave blank if the receipt belongs in Sundry.",
        7: "Enter non-service receipt amounts (Capital, Loan, Rent income, Interest) here.",
        8: "Name the General Ledger account for Sundry receipts (e.g. Capital, Rent income).",
    }

    mp_idx = 1
    for r_i, (vals, prefilled_cols, custom_hints) in enumerate(row_specs):
        str_rows.append(list(vals))
        row_cells: List[Dict[str, Any]] = []
        pref_set = set(prefilled_cols)
        for c_i, val in enumerate(vals):
            editable = c_i not in pref_set
            cell = _cell(r_i, c_i, val, editable=editable, is_money=(c_i in money_cols))
            row_cells.append(cell)
            if editable:
                cid = cell["cell_id"]
                correct_map[cid] = val
                cell_hints[cid] = custom_hints.get(c_i, default_col_hints[c_i])
                if val != "":
                    marking_points.append(
                        {
                            "id": f"mp_{mp_idx}",
                            "desc": f"Row {r_i + 1} {CRJ_HEADERS[c_i]}: {val}",
                            "marks": 1,
                            "editable": True,
                        }
                    )
                    mp_idx += 1
        rows.append(row_cells)

    if not marking_points:
        marking_points = [{"id": "mp_1", "desc": "Accurate journal entries completed", "marks": 2, "editable": True}]

    marks = sum(mp["marks"] for mp in marking_points)
    md = _md_table(CRJ_HEADERS, str_rows)
    worked = f"**Completed Cash Receipts Journal ({marks} marks)**\n\n{md}\n\n**Accounting Notes:**\n{explanation_notes}"
    return _build_table(
        rng,
        qid_prefix=qid_prefix,
        subskill=subskill,
        title=title,
        prompt=prompt,
        headers=CRJ_HEADERS,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=md,
        marks=marks,
        hints=hints,
        marking_points=marking_points,
        misconception_tags=misconception_tags,
        qtype="journal",
        journal_type="crj",
        diagram_spec=diagram_spec,
        topic_name=topic_name,
        subtopic_id=subtopic_id,
    )


# ---------------------------------------------------------------------------
# Archetypes 01 - 25
# ---------------------------------------------------------------------------

def build_01_crj_purpose_reducing_ledger_entries(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    n_rec = rng.randint(18, 42)
    ci_tot = rng.randint(8, 25) * 1000 + rng.choice([250, 500, 750])
    sun_tot = rng.randint(15, 60) * 1000
    bank_tot = ci_tot + sun_tot
    svg = _crj_flow_svg(ctx["biz_name"], ctx["crj_no"], n_rec, bank_tot, ci_tot, sun_tot)
    prompt = (
        f"Study the {ctx['crj_no']} summary flow diagram for {ctx['biz_name']} in {ctx['month_full']}, "
        f"showing {n_rec} cash receipts totalling {_fmt_r(bank_tot)} "
        f"(Current Income {_fmt_r(ci_tot)} and Sundry Accounts {_fmt_r(sun_tot)}). "
        f"Why does {ctx['entrepreneur']} record all {n_rec} receipts in the Cash Receipts Journal first instead of posting each receipt directly to the General Ledger?"
    )
    return _build_mcq(
        rng,
        qid_prefix="crj01",
        subskill="01_crj_purpose_reducing_ledger_entries",
        title="Purpose of the Cash Receipts Journal",
        prompt=prompt,
        correct_text=f"To group all {n_rec} cash receipts into a single book so only monthly totals are posted, reducing General Ledger clutter",
        distractors=[
            "To avoid having to issue duplicate receipts or keep till slips for customers",
            "To record both credit sales and cash payments on one combined page",
            "To replace the Bank column in the General Ledger permanently so no Bank account is needed",
        ],
        explanation=(
            f"A subsidiary journal collects all similar cash inflows ({n_rec} receipts totalling {_fmt_r(bank_tot)}) "
            f"in chronological order so only the monthly Bank total ({_fmt_r(bank_tot)}) and Current Income total ({_fmt_r(ci_tot)}) "
            f"are posted to the General Ledger."
        ),
        hints={
            "tier_1": "Think about what happens to the General Ledger if 40 individual daily receipts were posted separately.",
            "tier_2": "Subsidiary journals summarise daily transactions into monthly column totals.",
            "tier_3": "Posting one monthly Bank total and one Current Income total keeps the General Ledger concise and uncluttered.",
        },
        misconception_tags=["crj_purpose_misunderstood", "subsidiary_to_gl_confusion"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_02_crj_heading_three_required_elements(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    j_num = rng.randint(1, 12)
    prompt = (
        f"{ctx['entrepreneur']} owns {ctx['biz_name']} in {ctx['area']}. "
        f"The business is preparing its Cash Receipts Journal for {ctx['month_full']} — its {j_num}th journal since opening. "
        f"Complete the three mandatory heading items required at the top of a Cash Receipts Journal."
    )
    headers = ["Heading Requirement", "Entry for this Business"]
    items = [
        ("1. Name of Journal & Business", f"Cash Receipts Journal of {ctx['biz_name']}"),
        ("2. Month and Year", ctx["month_full"]),
        ("3. Journal Reference Number", f"CRJ{j_num}"),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    for r_i, (lbl, exp) in enumerate(items):
        str_rows.append([lbl, exp])
        c0 = _cell(r_i, 0, lbl, editable=False)
        c1 = _cell(r_i, 1, exp, editable=True)
        rows.append([c0, c1])
        cmap[c1["cell_id"]] = exp
        chints[c1["cell_id"]] = f"Include the exact {lbl.split('. ')[1].lower()} given in the scenario."
        mps.append({"id": f"mp_{r_i + 1}", "desc": f"{lbl}: {exp}", "marks": 1, "editable": True})
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj02",
        subskill="02_crj_heading_three_required_elements",
        title="Three Mandatory Elements of a CRJ Heading",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ Heading Summary (3 marks)**\n\n{md}",
        sample_answer=md,
        marks=3,
        hints={
            "tier_1": "Every CRJ heading states who owns the book, which period it covers, and its sequence code.",
            "tier_2": "Combine the journal title with the business name, then state the month/year and CRJ number.",
            "tier_3": f"Use 'Cash Receipts Journal of {ctx['biz_name']}', '{ctx['month_full']}', and 'CRJ{j_num}'.",
        },
        marking_points=mps,
        misconception_tags=["missing_journal_heading_elements", "missing_crj_number"],
        qtype="table_completion",
        journal_type="heading",
    )


def build_03_crj_journal_number_sequence_and_trading_month(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    j_num = rng.randint(4, 12)
    cap_amt = rng.randint(4, 15) * 10000
    prompt = (
        f"You inspect a journal headed 'Cash Receipts Journal of {ctx['biz_name']} for {ctx['month_full']} — CRJ{j_num}'. "
        f"On Day 03, {ctx['entrepreneur']} deposits {_fmt_r(cap_amt)} into the business bank account as Capital. "
        f"What does the journal number CRJ{j_num} tell you about this {_fmt_r(cap_amt)} Capital contribution?"
    )
    return _build_mcq(
        rng,
        qid_prefix="crj03",
        subskill="03_crj_journal_number_sequence_and_trading_month",
        title="Interpreting the CRJ Reference Number",
        prompt=prompt,
        correct_text=f"It is an additional Capital increase during month {j_num} of trading, not the initial start-up capital (which appears in CRJ1)",
        distractors=[
            f"It must be the business's very first transaction on opening day because CRJ{j_num} only tracks start-up funds",
            f"It means the bank loan of {_fmt_r(cap_amt)} was repaid over {j_num} instalments",
            "It shows the owner withdrew capital rather than depositing money into the business",
        ],
        explanation=(
            f"Each month of trading receives the next sequential journal number (CRJ1, CRJ2, ... CRJ{j_num}). "
            f"Because this is CRJ{j_num}, the business has already been operating for several months, so {_fmt_r(cap_amt)} increases existing Capital."
        ),
        hints={
            "tier_1": "Ask yourself which journal number is used in the very first month a business opens.",
            "tier_2": f"CRJ1 marks month 1 of operations; CRJ{j_num} is month {j_num} of operations.",
            "tier_3": f"Since CRJ{j_num} is after CRJ1, the {_fmt_r(cap_amt)} deposit increases existing Capital rather than starting the business from zero.",
        },
        misconception_tags=["crj_sequence_misread", "startup_vs_additional_capital_confusion"],
    )


def build_04_crj_cash_only_exclusion_of_credit_sales(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    cash_amt = rng.randint(12, 48) * 100
    credit_amt = rng.randint(15, 65) * 100
    pay_amt = rng.randint(8, 30) * 100
    personal_amt = rng.randint(5, 19) * 100
    variant = rng.choice(["exclude_credit_quote", "identify_crj_eligible"])
    if variant == "exclude_credit_quote":
        prompt = (
            f"{ctx['biz_name']} had four events during {ctx['month_full']}. "
            f"Which event must be RECORDED inside the Cash Receipts Journal ({ctx['crj_no']})?"
        )
        correct = f"Received {_fmt_r(cash_amt)} via EFT from a client for completed {ctx['svc_desc']}"
        distractors = [
            f"Issued a written quotation of {_fmt_r(credit_amt)} to a client who will decide next month",
            f"Paid {ctx['supplier']} {_fmt_r(pay_amt)} by EFT for business stationery",
            f"{ctx['entrepreneur']} spent {_fmt_r(personal_amt)} from a private account on household groceries",
        ]
        expl = "Only actual money received by the business (cash, card, or EFT inflow) enters the CRJ. Quotations, business payments (CPJ), and private spending are excluded."
    else:
        prompt = (
            f"On 14 {ctx['month_short']}, {ctx['biz_name']} completed several activities. "
            f"Which transaction should be EXCLUDED from the Cash Receipts Journal?"
        )
        correct = f"Paid {ctx['supplier']} {_fmt_r(pay_amt)} by business EFT for workshop consumables"
        distractors = [
            f"Banked {_fmt_r(cash_amt)} received from walk-in clients for {ctx['svc_desc']}",
            f"Tenant {ctx['tenant']} paid {_fmt_r(credit_amt)} directly into the business bank account for rent",
            f"{ctx['entrepreneur']} deposited {_fmt_r(personal_amt)} as additional Capital into the business bank account",
        ]
        expl = "Paying a supplier is a cash outflow recorded in the Cash Payments Journal (CPJ), never the CRJ."
    return _build_mcq(
        rng,
        qid_prefix="crj04",
        subskill="04_crj_cash_only_exclusion_of_credit_sales",
        title="Filtering Transactions for the CRJ",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=expl,
        hints={
            "tier_1": "The CRJ records ONLY money actually flowing INTO the business bank/till.",
            "tier_2": "Exclude quotations (no money moved yet), payments going out (CPJ), and private owner expenses.",
            "tier_3": "Match the option where the business receives actual cash or EFT inflow (or identify the one cash outflow if asked to exclude).",
        },
        misconception_tags=["payments_entered_in_crj", "non_cash_quotation_recorded"],
    )


def build_05_crj_source_doc_duplicate_receipt_purpose(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc_no = f"R{rng.randint(12, 89)}"
    day = rng.randint(2, 24)
    amt = rng.randint(25, 95) * 100
    reason_pair = rng.choice([
        (ctx["tenant"], f"Monthly workshop rent for {ctx['month_short']}", "a Duplicate Receipt because the original receipt was handed to the tenant"),
        (ctx["entrepreneur"], "Owner's capital contribution", "a Duplicate Receipt kept in the receipt book as proof of cash received from the owner"),
    ])
    payer, reason, reason_why = reason_pair
    svg = _receipt_svg(ctx["biz_name"], doc_no, f"{day:02d} {ctx['month_full']}", payer, amt, reason, ctx["entrepreneur"])
    prompt = (
        f"Examine the source document shown below for {ctx['biz_name']} on {day:02d} {ctx['month_full']} "
        f"(Document {doc_no}, amount {_fmt_r(amt)} from {payer}). "
        f"Why does {ctx['biz_name']} use a duplicate copy rather than the original copy to record this entry in {ctx['crj_no']}?"
    )
    return _build_mcq(
        rng,
        qid_prefix="crj05",
        subskill="05_crj_source_doc_duplicate_receipt_purpose",
        title="Duplicate Receipt as CRJ Source Document",
        prompt=prompt,
        correct_text=f"It uses {reason_why}",
        distractors=[
            "Because duplicate receipts are only prepared when the business pays cash to a supplier",
            "Because original receipts are sent to the Bank Statement department at year-end",
            "Because duplicate receipts are used to record daily till sales for walk-in service customers",
        ],
        explanation=(
            f"When money is received directly from a person like {payer} (Document {doc_no} for {_fmt_r(amt)}), "
            f"the original receipt goes to the payer and the business keeps the duplicate receipt to write up {ctx['crj_no']}."
        ),
        hints={
            "tier_1": "Think about who walks away with the original receipt when they hand over money.",
            "tier_2": "The person paying gets the original proof of payment; the business files the copy.",
            "tier_3": "Therefore the business enters the duplicate receipt into its CRJ.",
        },
        misconception_tags=["original_vs_duplicate_receipt_confusion"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_06_crj_source_doc_cash_register_roll_services(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = rng.randint(4, 26)
    doc_no = f"CRR{rng.randint(1, 9)}"
    a1, a2, a3 = rng.randint(4, 15) * 50, rng.randint(6, 18) * 50, rng.randint(5, 12) * 50
    total = a1 + a2 + a3
    svg = _crr_slip_svg(
        ctx["biz_name"],
        doc_no,
        f"{day:02d} {ctx['month_short']}",
        [("Morning client fee", a1), ("Afternoon client fee", a2), ("Late afternoon service", a3)],
    )
    prompt = (
        f"Inspect the till summary slip shown below for {ctx['biz_name']} on {day:02d} {ctx['month_short']} "
        f"({doc_no}, fees {_fmt_r(a1)}, {_fmt_r(a2)}, and {_fmt_r(a3)}). "
        f"Which source document code and amount should be recorded in {ctx['crj_no']} for {ctx['svc_desc']} on Day {day:02d}?"
    )
    return _build_mcq(
        rng,
        qid_prefix="crj06",
        subskill="06_crj_source_doc_cash_register_roll_services",
        title="Cash Register Roll (CRR) Till Total",
        prompt=prompt,
        correct_text=f"Doc No: CRR (Cash Register Roll) for the combined daily total of {_fmt_r(total)}",
        distractors=[
            f"Three separate Duplicate Receipt lines of {_fmt_r(a1)}, {_fmt_r(a2)}, and {_fmt_r(a3)}",
            f"Cheque counterfoil for {_fmt_r(total)} entered in the CPJ",
            f"Doc No: BS for {_fmt_r(a1 + a2)} only",
        ],
        explanation=(
            f"At day-end, the cash register prints one Cash Register Roll (CRR) summary totalling "
            f"{_fmt_r(a1)} + {_fmt_r(a2)} + {_fmt_r(a3)} = {_fmt_r(total)}, entered once into Current Income."
        ),
        hints={
            "tier_1": "Walk-in till customers are rung up on a cash register rather than issued individual handwritten receipts.",
            "tier_2": "Sum all three till amounts on the roll to get one daily service income figure.",
            "tier_3": f"Record Doc No 'CRR' and add {_fmt_r(a1)} + {_fmt_r(a2)} + {_fmt_r(a3)} = {_fmt_r(total)}.",
        },
        misconception_tags=["crr_vs_receipt_confusion", "separate_till_slip_posting"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_07_crj_source_doc_deposit_slip_and_bank_statement(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_amt = rng.randint(3, 9) * 10000
    s_amt = rng.randint(15, 45) * 100
    r_amt = rng.randint(20, 50) * 100
    i_amt = rng.randint(12, 45) * 10
    scenarios = [
        (f"{ctx['biz_name']} banks the day's cash receipts totalling {_fmt_r(s_amt + r_amt)} at {ctx['bank_name']}", "Duplicate deposit slip"),
        (f"Till fees of {_fmt_r(s_amt)} received from walk-in clients for {ctx['svc_desc']}", "Cash register roll (CRR)"),
        (f"Tenant {ctx['tenant']} pays {_fmt_r(r_amt)} rent cash at the counter and receives an original receipt", "Duplicate receipt"),
        (f"{ctx['bank_name']} credits {_fmt_r(i_amt)} interest directly onto the monthly account statement", "Bank statement"),
    ]
    rng.shuffle(scenarios)
    headers = ["Receipt Event", "Authoritative CRJ Source Document"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    for r_i, (ev, doc) in enumerate(scenarios):
        str_rows.append([ev, doc])
        c0 = _cell(r_i, 0, ev, editable=False)
        c1 = _cell(r_i, 1, doc, editable=True)
        rows.append([c0, c1])
        cmap[c1["cell_id"]] = doc
        chints[c1["cell_id"]] = "Choose from: Duplicate receipt, Cash register roll (CRR), Duplicate deposit slip, or Bank statement."
        mps.append({"id": f"mp_{r_i + 1}", "desc": f"{doc}", "marks": 1, "editable": True})
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj07",
        subskill="07_crj_source_doc_deposit_slip_and_bank_statement",
        title="Matching CRJ Events to Source Documents",
        prompt=f"Match each cash receipt event for {ctx['biz_name']} (Capital base {_fmt_r(c_amt)}) to its exact CRJ source document: Duplicate receipt, Cash register roll (CRR), Duplicate deposit slip, or Bank statement.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ Source Document Matching (4 marks)**\n\n{md}",
        sample_answer=md,
        marks=4,
        hints={
            "tier_1": "Each receipt channel leaves a different paper or digital trail.",
            "tier_2": "Walk-in till -> CRR; counter payment -> Duplicate receipt; cash banked -> Duplicate deposit slip; bank-initiated credit -> Bank statement.",
            "tier_3": "Fill each row with one of the four exact document names listed in the prompt.",
        },
        marking_points=mps,
        misconception_tags=["source_document_mismatch"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_08_crj_doc_no_abbreviation_conventions(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    num = rng.randint(15, 68)
    amt = rng.randint(10, 45) * 100
    cases = [
        ("BS", f"{ctx['bank_name']} notifies {ctx['biz_name']} via its monthly statement of a {_fmt_r(amt)} direct deposit or interest credit",
         ["CRR", f"R{num}", "CC01"],
         "BS stands for Bank Statement whenever an entry originates from the monthly bank statement."),
        ("CRR", f"End-of-day cash till tally of {_fmt_r(amt)} for {ctx['svc_desc']}",
         ["BS", f"R{num}", "DS01"],
         "CRR stands for Cash Register Roll."),
        (f"R{num}", f"Duplicate receipt number {num} issued for {_fmt_r(amt)} rent received from {ctx['tenant']}",
         ["BS", "CRR", f"C{num}"],
         f"Receipts are coded with 'R' followed by the receipt number (R{num})."),
    ]
    correct, desc, dists, expl = rng.choice(cases)
    return _build_mcq(
        rng,
        qid_prefix="crj08",
        subskill="08_crj_doc_no_abbreviation_conventions",
        title="Document Number Codes in the CRJ",
        prompt=f"What code should be entered in the 'Doc No' column of {ctx['crj_no']} for: {desc}?",
        correct_text=correct,
        distractors=dists,
        explanation=expl,
        hints={
            "tier_1": "Match the abbreviation to the initials of the source document.",
            "tier_2": "R# = Receipt, CRR = Cash Register Roll, BS = Bank Statement.",
            "tier_3": "Select the code whose letters match the transaction description above.",
        },
        misconception_tags=["doc_code_abbreviation_error"],
    )


def build_09_crj_column_sequence_identification(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    missing_pair = rng.choice([(4, 5, 6), (2, 4, 6), (4, 6, 7)])
    headers = ["Col Position", "CRJ Column Heading"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for idx, col_name in enumerate(CRJ_HEADERS):
        lbl = f"Column {idx + 1}"
        str_rows.append([lbl, col_name])
        editable = idx in missing_pair
        c0 = _cell(idx, 0, lbl, editable=False)
        c1 = _cell(idx, 1, col_name, editable=editable)
        rows.append([c0, c1])
        if editable:
            cmap[c1["cell_id"]] = col_name
            chints[c1["cell_id"]] = f"Recall the left-to-right CRJ sequence around {CRJ_HEADERS[max(0, idx - 1)]}."
            mps.append({"id": f"mp_{mp_i}", "desc": f"Column {idx + 1}: {col_name}", "marks": 1, "editable": True})
            mp_i += 1
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj09",
        subskill="09_crj_column_sequence_identification",
        title="Correct Layout & Column Sequence of the CRJ",
        prompt=f"{ctx['entrepreneur']} is setting up {ctx['crj_no']} for {ctx['biz_name']} in {ctx['month_full']}. Complete the 3 missing column headings in their standard left-to-right order.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**Standard CRJ Column Order (3 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "Identify columns moving from left (document details) to right (Analysis -> Bank -> Income -> Sundry).",
            "tier_2": "Remember 'Analysis of Receipts' sits directly before 'Bank', followed by 'Current Income' and 'Sundry'.",
            "tier_3": "Check the adjacent pre-filled columns and enter exact standard headings.",
        },
        marking_points=mps,
        misconception_tags=["crj_column_order_error"],
        qtype="table_completion",
        journal_type="structure",
    )


def build_10_crj_details_column_entry_rule(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc_no = f"R{rng.randint(10, 50)}"
    day = rng.randint(5, 25)
    amt = rng.randint(18, 55) * 100
    scenario = rng.choice([
        ("tenant", ctx["tenant"], f"Workshop rent for {ctx['month_short']}",
         f"{ctx['tenant']}", [f"Rent income", "Cash", f"Bank ({ctx['bank_name']})"],
         f"For a named receipt ({doc_no}), Details records WHO paid the money ({ctx['tenant']}); the account name 'Rent income' goes in Sundry Details."),
        ("crr", "Cash customers", f"{ctx['svc_desc']} till receipts",
         "Services rendered", [f"{ctx['entrepreneur']}", "Current income", "Cash register roll"],
         "For daily till receipts (CRR), South African Grade 8 convention writes 'Services rendered' (or 'Cash') in the Details column."),
    ])
    kind, payer, reason, correct, dists, expl = scenario
    svg = _receipt_svg(ctx["biz_name"], doc_no, f"{day:02d} {ctx['month_short']}", payer, amt, reason, ctx["entrepreneur"])
    return _build_mcq(
        rng,
        qid_prefix="crj10",
        subskill="10_crj_details_column_entry_rule",
        title="What to Write in the CRJ Details Column",
        prompt=(
            f"Inspect the source slip shown below for {ctx['biz_name']} on {day:02d} {ctx['month_short']} "
            f"({doc_no}, from {payer} for {reason}, {_fmt_r(amt)}). "
            f"What exact entry belongs in the 'Details' column of {ctx['crj_no']}?"
        ),
        correct_text=correct,
        distractors=dists,
        explanation=expl,
        hints={
            "tier_1": "Distinguish the 'Details' column (WHO paid or 'Services rendered') from the 'Sundry Details' column (WHICH ledger account).",
            "tier_2": "Named receipts record the payer's name in Details; till totals record 'Services rendered'.",
            "tier_3": "Match the payer/service convention stated in Tier 2 to this slip.",
        },
        misconception_tags=["details_vs_sundry_details_swap"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_11_crj_analysis_of_receipts_purpose_cash_till(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    r1 = rng.randint(12, 30) * 100
    r2 = rng.randint(14, 35) * 100
    day = rng.randint(3, 21)
    prompt = (
        f"On {day:02d} {ctx['month_short']}, {ctx['biz_name']} receives {_fmt_r(r1)} cash in the till for {ctx['svc_desc']} "
        f"and later the same day receives {_fmt_r(r2)} cash rent from {ctx['tenant']}. "
        f"Why does {ctx['entrepreneur']} record both amounts in 'Analysis of Receipts' before extending one total to 'Bank'?"
    )
    return _build_mcq(
        rng,
        qid_prefix="crj11",
        subskill="11_crj_analysis_of_receipts_purpose_cash_till",
        title="Purpose of the Analysis of Receipts Column",
        prompt=prompt,
        correct_text=f"To serve as a cash-till holding column that groups all physical cash received on Day {day:02d} into one single bank deposit of {_fmt_r(r1 + r2)}",
        distractors=[
            f"To double the Bank total so both {_fmt_r(r1)} and {_fmt_r(r2)} are counted twice in the General Ledger",
            "To post individual cash register slips separately into the Trial Balance",
            "To record credit sales that customers promise to pay next month",
        ],
        explanation=(
            f"'Analysis of Receipts' acts as the business's cash till for the day. "
            f"At day-end, all cash receipts on Day {day:02d} ({_fmt_r(r1)} + {_fmt_r(r2)}) are added together into ONE deposit of {_fmt_r(r1 + r2)} in the Bank column."
        ),
        hints={
            "tier_1": "Think about whether you walk to the bank five times a day or make one combined deposit at closing time.",
            "tier_2": "Analysis of Receipts tracks money inside the till before banking; Bank shows the single daily deposit.",
            "tier_3": f"One combined deposit of {_fmt_r(r1 + r2)} matches the single duplicate deposit slip stamped by the bank.",
        },
        misconception_tags=["analysis_of_receipts_posted_to_gl"],
    )


def build_12_crj_single_cash_service_receipt_row(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(2, 27):02d}"
    amt = _fmt_r(rng.randint(18, 64) * 100 + rng.choice([0, 50]))
    prompt = (
        f"Record the following single transaction in {ctx['crj_no']} for {ctx['biz_name']} ({ctx['month_full']}): "
        f"On Day {day}, cash received for {ctx['svc_desc']} according to the Cash Register Roll amounted to {amt} (banked immediately). "
        f"Leave columns that do not apply blank."
    )
    row_specs = [
        (["CRR", day, "Services rendered", "", amt, amt, amt, "", ""], [0, 1], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj12",
        subskill="12_crj_single_cash_service_receipt_row",
        title="Recording a Cash Register Roll Service Entry",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Till cash enters `Analysis of Receipts` ({amt}), is banked as {amt} in `Bank`, and classified under `Current Income` ({amt}).\n"
            f"- `Sundry Amount`, `Sundry Details`, and `Fol.` remain blank."
        ),
        hints={
            "tier_1": "Cash received at the till passes through Analysis of Receipts, then Bank, then Current Income.",
            "tier_2": "Use 'Services rendered' in Details and keep all Sundry columns empty.",
            "tier_3": f"Enter {amt} in Analysis of Receipts, Bank, and Current Income.",
        },
        misconception_tags=["crr_sundry_confusion", "missing_analysis_entry"],
    )


def build_13_crj_single_owner_capital_cash_vs_direct_deposit(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(1, 5):02d}"
    doc = f"R{rng.randint(1, 3):02d}"
    amt = _fmt_r(rng.randint(5, 16) * 10000)
    prompt = (
        f"On {day} {ctx['month_full']}, {ctx['entrepreneur']} deposited {amt} directly into {ctx['biz_name']}'s {ctx['bank_name']} account "
        f"as start-up Capital (Receipt {doc}, folio B1). "
        f"Record this direct deposit in {ctx['crj_no']}. Keep unused columns blank."
    )
    row_specs = [
        ([doc, day, ctx["entrepreneur"], "B1", "", amt, "", amt, "Capital"], [0, 1, 3], {
            4: "Direct deposits do NOT pass through the cash till — leave Analysis of Receipts blank!",
            6: "Capital is NOT trading service income — leave Current Income blank.",
            8: "Enter the exact General Ledger account name: Capital.",
        }),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj13",
        subskill="13_crj_single_owner_capital_cash_vs_direct_deposit",
        title="Recording Direct Deposit of Owner Capital",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Direct deposits go straight into the bank account, so `Analysis of Receipts` is left blank.\n"
            f"- Enter {amt} in `Bank` and `Sundry Amount`, with `Capital` in `Sundry Details`."
        ),
        hints={
            "tier_1": "Ask: did this money ever sit inside the business cash register till?",
            "tier_2": "Because it went directly into the bank, skip Analysis of Receipts and classify it under Sundry Accounts.",
            "tier_3": f"Leave Analysis of Receipts and Current Income blank; put {amt} in Bank and Sundry Amount ('Capital').",
        },
        misconception_tags=["direct_deposit_in_analysis", "capital_in_current_income"],
    )


def build_14_crj_direct_eft_deposit_analysis_rule(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(8, 25):02d}"
    amt = rng.randint(45, 95) * 100
    svg = _bank_stmt_svg(
        ctx["bank_name"],
        ctx["biz_name"],
        ctx["month_full"],
        [(f"{day} {ctx['month_short']}", f"EFT Credit — {ctx['tenant']} (Rent)", amt)],
    )
    prompt = (
        f"Inspect the Bank Statement extract below for {ctx['biz_name']} showing an EFT credit of {_fmt_r(amt)} "
        f"from {ctx['tenant']} on {day} {ctx['month_short']}. "
        f"How must the 'Analysis of Receipts' column be handled when recording this direct EFT deposit in {ctx['crj_no']}?"
    )
    return _build_mcq(
        rng,
        qid_prefix="crj14",
        subskill="14_crj_direct_eft_deposit_analysis_rule",
        title="Direct EFT Deposits & Analysis of Receipts",
        prompt=prompt,
        correct_text=f"Leave Analysis of Receipts blank and enter {_fmt_r(amt)} directly into the Bank column and Sundry Amount",
        distractors=[
            f"Enter {_fmt_r(amt)} in Analysis of Receipts first and then bank it at the end of the week",
            f"Enter {_fmt_r(amt)} only in Sundry Amount and skip the Bank column",
            f"Split {_fmt_r(amt)} equally between Current Income and Analysis of Receipts",
        ],
        explanation=(
            f"An EFT or direct deposit goes straight into {ctx['bank_name']} without touching the business till. "
            f"Therefore Analysis of Receipts stays blank and {_fmt_r(amt)} enters Bank and Sundry Amount (Rent income)."
        ),
        hints={
            "tier_1": "Analysis of Receipts tracks physical cash/till receipts waiting to be banked.",
            "tier_2": "Since an EFT lands straight in the bank, it never waits in the till.",
            "tier_3": f"Skip Analysis of Receipts; record {_fmt_r(amt)} directly in Bank and Sundry Amount.",
        },
        misconception_tags=["eft_recorded_in_analysis_of_receipts"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_15_crj_same_day_two_receipts_banking_rule(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(10, 26):02d}"
    r_no = f"R{rng.randint(14, 38)}"
    rent_amt = rng.randint(22, 48) * 100
    svc_amt = rng.randint(18, 42) * 100
    bank_sum = rent_amt + svc_amt
    prompt = (
        f"Record BOTH cash receipts received on Day {day} of {ctx['month_full']} for {ctx['biz_name']} in {ctx['crj_no']}:\n"
        f"1. Issued Receipt {r_no} to tenant {ctx['tenant']} for {_fmt_r(rent_amt)} cash rent (folio N2).\n"
        f"2. Cash Register Roll (CRR) for {ctx['svc_desc']} totalled {_fmt_r(svc_amt)}.\n"
        f"Both cash amounts were banked together at day-end. Leave non-applicable cells blank."
    )
    row_specs = [
        ([r_no, day, ctx["tenant"], "N2", _fmt_r(rent_amt), "", "", _fmt_r(rent_amt), "Rent income"], [0, 1, 3], {
            5: "Same-day receipts are banked together on the LAST line of that day — leave Bank blank here!",
        }),
        (["CRR", day, "Services rendered", "", _fmt_r(svc_amt), _fmt_r(bank_sum), _fmt_r(svc_amt), "", ""], [0, 1], {
            5: f"Add both cash receipts from Day {day}: {_fmt_r(rent_amt)} + {_fmt_r(svc_amt)}.",
        }),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj15",
        subskill="15_crj_same_day_two_receipts_banking_rule",
        title="Two Cash Receipts on the Same Day (Combined Deposit)",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Row 1 ({r_no}): Enter {_fmt_r(rent_amt)} in `Analysis of Receipts` and `Sundry Amount` (Rent income). Leave `Bank` blank.\n"
            f"- Row 2 (CRR): Enter {_fmt_r(svc_amt)} in `Analysis of Receipts` and `Current Income`, then bank ONE combined deposit of {_fmt_r(bank_sum)} in `Bank`."
        ),
        hints={
            "tier_1": "When two physical cash receipts happen on the same day, the business makes ONE deposit at closing time.",
            "tier_2": "Record each receipt in Analysis of Receipts, keep Bank blank on Row 1, and sum both into Bank on Row 2.",
            "tier_3": f"Row 2 Bank = {_fmt_r(rent_amt)} + {_fmt_r(svc_amt)} = {_fmt_r(bank_sum)}.",
        },
        misconception_tags=["same_day_banked_separately", "forgot_combined_deposit"],
    )


def build_16_crj_same_day_three_receipts_combined_deposit(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(8, 22):02d}"
    r1 = rng.randint(10, 28) * 100
    r2 = rng.randint(12, 34) * 100
    r3 = rng.randint(15, 39) * 100
    eft_prev = rng.randint(25, 55) * 100
    total_bank = r1 + r2 + r3
    svg = _crr_slip_svg(
        ctx["biz_name"],
        f"Day {day} Till",
        f"{day} {ctx['month_short']}",
        [(f"Receipt R11 ({ctx['tenant']})", r1), ("Receipt R12 (Donation)", r2), (f"CRR ({ctx['svc_desc']})", r3)],
    )
    prompt = (
        f"Inspect the till summary card below for {ctx['biz_name']} on {day} {ctx['month_short']}: "
        f"cash till receipts were {_fmt_r(r1)} (rent), {_fmt_r(r2)} (donation), and {_fmt_r(r3)} (services). "
        f"(Note: an unrelated {_fmt_r(eft_prev)} EFT arrived directly on Day {int(day) - 2:02d}.) "
        f"Calculate the SINGLE deposit amount entered in the Bank column on Day {day}."
    )
    ans = _fmt_r(total_bank)
    worked = (
        f"1. Include ONLY the physical cash receipts received on Day {day} in the till:\n"
        f"   {_fmt_r(r1)} + {_fmt_r(r2)} + {_fmt_r(r3)} = **{ans}**\n"
        f"2. Exclude the {_fmt_r(eft_prev)} direct EFT from Day {int(day) - 2:02d} (already banked on that earlier day)."
    )
    return _build_short(
        rng,
        qid_prefix="crj16",
        subskill="16_crj_same_day_three_receipts_combined_deposit",
        title="Combined Daily Deposit from Three Same-Day Receipts",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "Only group cash amounts received in the till on THAT exact day.",
            "tier_2": f"Ignore the earlier EFT on Day {int(day) - 2:02d}; sum the three receipts from Day {day}.",
            "tier_3": f"Compute {_fmt_r(r1)} + {_fmt_r(r2)} + {_fmt_r(r3)}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sums only Day {day} cash receipts ({_fmt_r(r1)} + {_fmt_r(r2)} + {_fmt_r(r3)})", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Final Bank deposit: {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["cross_day_receipts_summed", "arithmetic_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_17_crj_multi_day_separate_banking_comparison(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    d1 = rng.randint(4, 11)
    d2 = d1 + rng.randint(3, 7)
    a1 = _fmt_r(rng.randint(15, 40) * 100)
    a2 = _fmt_r(rng.randint(18, 45) * 100)
    prompt = (
        f"Record these two cash till entries on DIFFERENT days in {ctx['crj_no']} for {ctx['biz_name']} ({ctx['month_full']}):\n"
        f"- Day {d1:02d}: CRR cash services rendered, {a1}.\n"
        f"- Day {d2:02d}: CRR cash services rendered, {a2}.\n"
        f"Remember: receipts on different days are banked separately on their own days!"
    )
    row_specs = [
        (["CRR", f"{d1:02d}", "Services rendered", "", a1, a1, a1, "", ""], [0, 1], {
            5: f"Day {d1:02d} is banked on its own day ({a1}), NOT combined with Day {d2:02d}.",
        }),
        (["CRR", f"{d2:02d}", "Services rendered", "", a2, a2, a2, "", ""], [0, 1], {
            5: f"Bank Day {d2:02d}'s receipt separately as {a2}.",
        }),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj17",
        subskill="17_crj_multi_day_separate_banking_comparison",
        title="Separate Banking on Different Days",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Receipts are ONLY summed in `Bank` when they occur on the SAME day.\n"
            f"- Day {d1:02d} banks {a1} on Day {d1:02d}; Day {d2:02d} banks {a2} on Day {d2:02d}."
        ),
        hints={
            "tier_1": "Check the Day column carefully before combining deposits!",
            "tier_2": "Different days mean two separate trips to the bank, so each row populates Bank independently.",
            "tier_3": f"Row 1 Bank = {a1}; Row 2 Bank = {a2}.",
        },
        misconception_tags=["different_days_wrongly_summed"],
    )


def build_18_crj_current_income_vs_sundry_classification(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    a_svc = _fmt_r(rng.randint(20, 60) * 100)
    a_cap = _fmt_r(rng.randint(3, 8) * 10000)
    a_rent = _fmt_r(rng.randint(25, 50) * 100)
    a_loan = _fmt_r(rng.randint(2, 6) * 10000)
    items = [
        (f"Walk-in fees of {a_svc} for {ctx['svc_desc']}", "Current Income", "Current Income"),
        (f"{ctx['entrepreneur']} invests {a_cap} cash into the business", "Sundry Accounts", "Capital"),
        (f"Sub-letting spare office space to {ctx['tenant']} for {a_rent}", "Sundry Accounts", "Rent income"),
        (f"Receiving a {a_loan} business loan from {ctx['bank_name']}", "Sundry Accounts", f"Loan: {ctx['bank_name']}"),
    ]
    rng.shuffle(items)
    headers = ["Cash Receipt Description", "CRJ Allocation Column", "Exact Ledger Account Name"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (desc, col_choice, acct) in enumerate(items):
        str_rows.append([desc, col_choice, acct])
        c0 = _cell(r_i, 0, desc, editable=False)
        c1 = _cell(r_i, 1, col_choice, editable=True)
        c2 = _cell(r_i, 2, acct, editable=True)
        rows.append([c0, c1, c2])
        cmap[c1["cell_id"]] = col_choice
        cmap[c2["cell_id"]] = acct
        chints[c1["cell_id"]] = "Enter 'Current Income' (core services) or 'Sundry Accounts' (all other receipts)."
        chints[c2["cell_id"]] = "Name the exact account (e.g. Current Income, Capital, Rent income, or Loan: Bank)."
        mps.append({"id": f"mp_{mp_i}", "desc": f"Row {r_i + 1} Column: {col_choice}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 1}", "desc": f"Row {r_i + 1} Account: {acct}", "marks": 1, "editable": True})
        mp_i += 2
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj18",
        subskill="18_crj_current_income_vs_sundry_classification",
        title="Current Income vs Sundry Accounts Classification",
        prompt=f"Classify each receipt for {ctx['biz_name']} into either 'Current Income' or 'Sundry Accounts' and specify the exact General Ledger account name.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ Column & Account Classification (8 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "Only core day-to-day service revenue goes into Current Income.",
            "tier_2": "Capital, Rent income, and Bank Loans are infrequent/non-service receipts handled in Sundry Accounts.",
            "tier_3": f"Match Rent -> Rent income, Owner investment -> Capital, Loan -> Loan: {ctx['bank_name']}.",
        },
        marking_points=mps,
        misconception_tags=["rent_income_in_current_income", "loan_misclassified_as_income"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_19_crj_sundry_capital_contribution_entry(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(12, 24):02d}"
    doc = f"R{rng.randint(20, 49)}"
    amt = _fmt_r(rng.randint(15, 45) * 1000)
    prompt = (
        f"In {ctx['crj_no']} ({ctx['month_full']}), {ctx['entrepreneur']} increases Capital by transferring {amt} "
        f"directly into {ctx['biz_name']}'s bank account on Day {day} (Receipt {doc}, folio B1). "
        f"Complete the CRJ row."
    )
    row_specs = [
        ([doc, day, ctx["entrepreneur"], "B1", "", amt, "", amt, "Capital"], [0, 1, 3], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj19",
        subskill="19_crj_sundry_capital_contribution_entry",
        title="Additional Capital Contribution in the CRJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Owner capital transfers bypass `Analysis of Receipts`, increase `Bank` by {amt}, and post to `Capital` under Sundry Accounts.",
        hints={
            "tier_1": "Direct bank transfer -> skip Analysis of Receipts.",
            "tier_2": "Capital is an Owner's Equity account recorded in Sundry Accounts.",
            "tier_3": f"Enter {amt} in Bank and Sundry Amount, and write 'Capital' in Sundry Details.",
        },
        misconception_tags=["capital_in_analysis", "capital_in_current_income"],
    )


def build_20_crj_sundry_bank_loan_receipt_entry(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(5, 22):02d}"
    amt = _fmt_r(rng.randint(3, 12) * 10000)
    loan_acct = f"Loan: {ctx['bank_name']}"
    prompt = (
        f"On {day} {ctx['month_full']}, {ctx['bank_name']} approved and deposited a business loan of {amt} "
        f"directly into {ctx['biz_name']}'s current bank account (Bank Statement entry BS, folio B4). "
        f"Record this loan receipt in {ctx['crj_no']}."
    )
    row_specs = [
        (["BS", day, ctx["bank_name"], "B4", "", amt, "", amt, loan_acct], [0, 1, 3], {
            8: f"Name the specific liability account: {loan_acct}.",
        }),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj20",
        subskill="20_crj_sundry_bank_loan_receipt_entry",
        title="Recording a Bank Loan in the CRJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Bank loans arrive straight into the bank account via Bank Statement (`BS`), so `Analysis of Receipts` is blank.\n"
            f"- Credit `{loan_acct}` in `Sundry Accounts`, NOT `Current Income` (a loan is a liability, not earned revenue)."
        ),
        hints={
            "tier_1": "A loan is money deposited by the bank directly — never in the cash till, and never earned service income.",
            "tier_2": "Leave Analysis of Receipts and Current Income empty; record in Bank and Sundry.",
            "tier_3": f"Details = {ctx['bank_name']}; Bank = {amt}; Sundry Amount = {amt}; Sundry Details = {loan_acct}.",
        },
        misconception_tags=["loan_treated_as_current_income"],
    )


def build_21_crj_sundry_rent_income_tenant_entry(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(2, 18):02d}"
    doc = f"R{rng.randint(31, 79)}"
    amt = rng.randint(24, 65) * 100
    amt_str = _fmt_r(amt)
    svg = _receipt_svg(ctx["biz_name"], doc, f"{day} {ctx['month_short']}", ctx["tenant"], amt, f"Sub-let office rent ({ctx['month_short']})", ctx["entrepreneur"])
    prompt = (
        f"Inspect the duplicate receipt slip below issued to {ctx['tenant']} on {day} {ctx['month_short']} "
        f"for {amt_str} cash paid at the office (folio N2). Record this single cash receipt in {ctx['crj_no']} (assume no other receipts on Day {day})."
    )
    row_specs = [
        ([doc, day, ctx["tenant"], "N2", amt_str, amt_str, "", amt_str, "Rent income"], [0, 1, 3], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj21",
        subskill="21_crj_sundry_rent_income_tenant_entry",
        title="Recording Cash Rent Income from a Receipt Slip",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Because {ctx['tenant']} paid cash at the premises (Duplicate Receipt {doc}), {amt_str} enters `Analysis of Receipts` first and then `Bank`.\n"
            f"- Rent is non-core income, so allocate {amt_str} to `Sundry Amount` with `Rent income` in `Sundry Details`."
        ),
        hints={
            "tier_1": "Cash paid at the premises goes into Analysis of Receipts first; rent goes into Sundry Accounts.",
            "tier_2": "Write the tenant's name in Details and 'Rent income' in Sundry Details.",
            "tier_3": f"Enter {amt_str} in Analysis of Receipts, Bank, and Sundry Amount.",
        },
        misconception_tags=["rent_income_in_current_income", "cash_receipt_skipped_analysis"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_22_crj_sundry_interest_received_on_current_account(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(28, 30):02d}"
    amt = rng.randint(15, 85) * 10 + rng.choice([0, 5])
    amt_str = _fmt_r(amt)
    svg = _bank_stmt_svg(ctx["bank_name"], ctx["biz_name"], ctx["month_full"], [(f"{day} {ctx['month_short']}", "Interest on current account", amt)])
    prompt = (
        f"Examine the Bank Statement extract below from {ctx['bank_name']} showing {amt_str} interest credited on Day {day} {ctx['month_short']} (folio N3). "
        f"Record this entry in {ctx['crj_no']}."
    )
    row_specs = [
        (["BS", day, ctx["bank_name"], "N3", "", amt_str, "", amt_str, "Interest income"], [0, 1, 3], {
            8: "Record the income account as 'Interest income' (or 'Interest on current account').",
        }),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj22",
        subskill="22_crj_sundry_interest_received_on_current_account",
        title="Recording Bank Interest Income in the CRJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Bank interest is credited directly on the Bank Statement (`BS`), so leave `Analysis of Receipts` blank and allocate {amt_str} to `Sundry Amount` (`Interest income`).",
        hints={
            "tier_1": "Interest comes straight from the Bank Statement (BS) into your bank balance.",
            "tier_2": "Skip Analysis of Receipts; leave Current Income empty.",
            "tier_3": f"Details = {ctx['bank_name']}; Bank = {amt_str}; Sundry Amount = {amt_str}; Sundry Details = Interest income.",
        },
        misconception_tags=["interest_entered_in_analysis", "interest_in_current_income"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_23_crj_sundry_commission_or_donation_receipt(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(11, 25):02d}"
    doc = f"R{rng.randint(51, 88)}"
    amt = _fmt_r(rng.randint(8, 35) * 100)
    variant = rng.choice([
        (ctx["supplier"], "Commission income", "promotional referral commission"),
        (ctx["competitor"], "Donations received", "local youth enterprise grant"),
    ])
    payer, acct, desc = variant
    prompt = (
        f"On {day} {ctx['month_full']}, {ctx['biz_name']} received {amt} via direct EFT from {payer} for a {desc} "
        f"(Receipt {doc}, folio N4). Record this non-core receipt in {ctx['crj_no']}."
    )
    row_specs = [
        ([doc, day, payer, "N4", "", amt, "", amt, acct], [0, 1, 3], {}),
    ]
    return _crj_journal_question(
        rng,
        qid_prefix="crj23",
        subskill="23_crj_sundry_commission_or_donation_receipt",
        title="Miscellaneous Sundry Receipts (Commission / Grants)",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Non-core inflows ({desc}) go to `Sundry Accounts` under `{acct}`. Because payment was by EFT, `Analysis of Receipts` remains blank.",
        hints={
            "tier_1": "EFT inflows bypass the cash till, and non-service income goes to Sundry Accounts.",
            "tier_2": "Enter the payer in Details and the exact miscellaneous income account in Sundry Details.",
            "tier_3": f"Enter {amt} in Bank and Sundry Amount with '{acct}' in Sundry Details.",
        },
        misconception_tags=["misc_income_in_current_income"],
    )


def build_24_crj_folio_column_purpose_and_codes(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    b_fol = f"B{rng.randint(1, 5)}"
    n_fol = f"N{rng.randint(1, 6)}"
    variant = rng.choice([
        ("Sundry Accounts", f"{b_fol} or {n_fol}",
         "Each Sundry item belongs to a different General Ledger account, so each row posts individually and needs its own folio reference",
         [
             "Sundry items are never posted to the General Ledger at month-end",
             "Every Current Income till row must carry a separate page number on each day",
             "Folio codes show the VAT rate charged on each service",
         ]),
        ("B vs N codes", f"{b_fol} (Balance Sheet section) and {n_fol} (Nominal accounts section)",
         f"'{b_fol}' marks Balance Sheet section accounts (like Capital or Loan) whereas '{n_fol}' marks Nominal income accounts (like Rent income)",
         [
             f"'{b_fol}' always means Bank Statement and '{n_fol}' means Net Profit",
             f"'{b_fol}' stands for Business expense and '{n_fol}' stands for No entry needed",
             "Folio numbers are chosen randomly by the cashier every morning",
         ]),
    ])
    _, code_str, correct, dists = variant
    return _build_mcq(
        rng,
        qid_prefix="crj24",
        subskill="24_crj_folio_column_purpose_and_codes",
        title="Folio References in the CRJ",
        prompt=f"In {ctx['biz_name']}'s {ctx['crj_no']}, you notice folio references such as {code_str} written next to Sundry entries, while daily Current Income rows have blank folio cells. Why?",
        correct_text=correct,
        distractors=dists,
        explanation=(
            f"Daily `Current Income` rows are summed and posted once at month-end under the total row, "
            f"whereas `Sundry Accounts` rows go to distinct accounts (e.g. {b_fol} Balance Sheet section, {n_fol} Nominal section) so each row is referenced individually."
        ),
        hints={
            "tier_1": "Think about which column posts ONLY as a monthly total versus which column contains mixed accounts.",
            "tier_2": "B = Balance Sheet accounts (Capital, Loan, Bank); N = Nominal accounts (Current Income, Rent income).",
            "tier_3": "Individual sundry rows post separately to different GL accounts, so each row gets a B# or N# folio.",
        },
        misconception_tags=["folio_cross_reference_misunderstood"],
    )


def build_25_crj_column_selection_for_mixed_source_docs(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    a_cap = _fmt_r(rng.randint(4, 9) * 10000)
    a_svc1 = _fmt_r(rng.randint(15, 35) * 100)
    a_rent = _fmt_r(rng.randint(20, 45) * 100)
    a_int = _fmt_r(rng.randint(12, 36) * 10)
    headers = ["Transaction", "Analysis of Receipts?", "Bank?", "Current Income?", "Sundry Amount?"]
    rows_spec = [
        (f"Direct EFT Capital {a_cap}", "No", a_cap, "No", a_cap),
        (f"Till CRR Services {a_svc1} (only receipt that day)", a_svc1, a_svc1, a_svc1, "No"),
        (f"Cash Receipt Rent {a_rent} (only receipt that day)", a_rent, a_rent, "No", a_rent),
        (f"Bank Statement Interest {a_int}", "No", a_int, "No", a_int),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (tx, c1, c2, c3, c4) in enumerate(rows_spec):
        str_rows.append([tx, c1, c2, c3, c4])
        cells = [_cell(r_i, 0, tx, editable=False)]
        for c_i, val in enumerate([c1, c2, c3, c4], start=1):
            cell = _cell(r_i, c_i, val, editable=True)
            cells.append(cell)
            cmap[cell["cell_id"]] = val
            chints[cell["cell_id"]] = "Enter the exact Rand amount if used, or type 'No' if this column is blank."
            mps.append({"id": f"mp_{mp_i}", "desc": f"R{r_i + 1}C{c_i}: {val}", "marks": 1, "editable": True})
            mp_i += 1
        rows.append(cells)
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="crj25",
        subskill="25_crj_column_selection_for_mixed_source_docs",
        title="Amount Placement Across CRJ Money Columns",
        prompt=f"For each single receipt below at {ctx['biz_name']}, enter either the exact Rand amount placed in each CRJ column OR 'No' if that column stays blank.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CRJ Column Placement Drill (16 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "Test two questions on every receipt: (1) Did cash touch the till? (2) Is it core services or Sundry?",
            "tier_2": "Direct EFT / Bank Statement credits skip Analysis of Receipts ('No').",
            "tier_3": "Every transaction ALWAYS enters the Bank column.",
        },
        marking_points=mps,
        misconception_tags=["column_allocation_confusion"],
        qtype="table_completion",
        journal_type="classification",
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_crj_purpose_reducing_ledger_entries": build_01_crj_purpose_reducing_ledger_entries,
    "02_crj_heading_three_required_elements": build_02_crj_heading_three_required_elements,
    "03_crj_journal_number_sequence_and_trading_month": build_03_crj_journal_number_sequence_and_trading_month,
    "04_crj_cash_only_exclusion_of_credit_sales": build_04_crj_cash_only_exclusion_of_credit_sales,
    "05_crj_source_doc_duplicate_receipt_purpose": build_05_crj_source_doc_duplicate_receipt_purpose,
    "06_crj_source_doc_cash_register_roll_services": build_06_crj_source_doc_cash_register_roll_services,
    "07_crj_source_doc_deposit_slip_and_bank_statement": build_07_crj_source_doc_deposit_slip_and_bank_statement,
    "08_crj_doc_no_abbreviation_conventions": build_08_crj_doc_no_abbreviation_conventions,
    "09_crj_column_sequence_identification": build_09_crj_column_sequence_identification,
    "10_crj_details_column_entry_rule": build_10_crj_details_column_entry_rule,
    "11_crj_analysis_of_receipts_purpose_cash_till": build_11_crj_analysis_of_receipts_purpose_cash_till,
    "12_crj_single_cash_service_receipt_row": build_12_crj_single_cash_service_receipt_row,
    "13_crj_single_owner_capital_cash_vs_direct_deposit": build_13_crj_single_owner_capital_cash_vs_direct_deposit,
    "14_crj_direct_eft_deposit_analysis_rule": build_14_crj_direct_eft_deposit_analysis_rule,
    "15_crj_same_day_two_receipts_banking_rule": build_15_crj_same_day_two_receipts_banking_rule,
    "16_crj_same_day_three_receipts_combined_deposit": build_16_crj_same_day_three_receipts_combined_deposit,
    "17_crj_multi_day_separate_banking_comparison": build_17_crj_multi_day_separate_banking_comparison,
    "18_crj_current_income_vs_sundry_classification": build_18_crj_current_income_vs_sundry_classification,
    "19_crj_sundry_capital_contribution_entry": build_19_crj_sundry_capital_contribution_entry,
    "20_crj_sundry_bank_loan_receipt_entry": build_20_crj_sundry_bank_loan_receipt_entry,
    "21_crj_sundry_rent_income_tenant_entry": build_21_crj_sundry_rent_income_tenant_entry,
    "22_crj_sundry_interest_received_on_current_account": build_22_crj_sundry_interest_received_on_current_account,
    "23_crj_sundry_commission_or_donation_receipt": build_23_crj_sundry_commission_or_donation_receipt,
    "24_crj_folio_column_purpose_and_codes": build_24_crj_folio_column_purpose_and_codes,
    "25_crj_column_selection_for_mixed_source_docs": build_25_crj_column_selection_for_mixed_source_docs,
}
