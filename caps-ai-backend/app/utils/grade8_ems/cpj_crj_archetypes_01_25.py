"""Grade 8 EMS - Cash Receipts Journal 2 & Cash Payments Journal: Archetypes 01 to 25.

Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/
03. Cash receipts journal for a services business 2.md and
04. Cash payments journal for a services business.md.
Zero-LLM, 100% deterministic, South African Rand (R) contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "Cash payments journal for a services business"
SUBTOPIC_ID = "term3_cpj_and_crj"

CPJ_HEADERS = [
    "Doc No",
    "Day",
    "Name of Payee",
    "Fol.",
    "Bank",
    "Wages",
    "Stationery",
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
_MUNICIPALITIES = ["City of Tshwane", "City of Cape Town", "eThekwini Municipality", "City Power Johannesburg", "Mangaung Metro"]
_LANDLORDS = ["Khumalo Properties", "Silver Oak Estates", "Protea Mall Rentals", "Ubuntu Business Park"]
_SERVICE_DESCS = [
    ("hairdressing services", "Hair Lounge"),
    ("electrical contracting", "Spark Electrical"),
    ("plumbing maintenance", "FlowFix Plumbers"),
    ("auto detailing services", "CleanRide Studio"),
    ("garden services", "Kirstenbosch Care"),
    ("tailoring & repairs", "ThreadWorks"),
    ("IT support services", "ByteCare Tech"),
]


def _fmt_r(amount: int | float) -> str:
    """Format Rand amounts cleanly with space thousands separator."""
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _biz_ctx(rng: random.Random) -> Dict[str, Any]:
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
        "municipality": rng.choice(_MUNICIPALITIES),
        "landlord": rng.choice(_LANDLORDS),
        "cpj_no": f"CPJ{rng.randint(1, 9)}",
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
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = ["| " + " | ".join(cell if cell != "" else "—" for cell in r) + " |" for r in str_rows]
    return "\n".join([head, sep] + body)


def _cpj_crj_flow_svg(biz_name: str, crj_tot: int, cpj_tot: int) -> str:
    """Context SVG comparing Cash In (CRJ) vs Cash Out (CPJ) and Net Bank Change."""
    net = crj_tot - cpj_tot
    sign = "+" if net >= 0 else "-"
    net_lbl = f"{sign}{_fmt_r(abs(net))}"
    net_col = "#047857" if net >= 0 else "#b91c1c"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 205" width="640" height="205">'
        '<rect width="640" height="205" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="320" y="26" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">{biz_name} — Cash Flow Journals Overview</text>'
        '<rect x="20" y="48" width="180" height="122" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>'
        '<text x="110" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#065f46">CRJ (Cash In)</text>'
        '<text x="110" y="96" font-size="11" text-anchor="middle" fill="#1e293b">Bank Debited (+)</text>'
        f'<text x="110" y="122" font-size="13" font-weight="bold" text-anchor="middle" fill="#047857">{_fmt_r(crj_tot)}</text>'
        '<text x="110" y="146" font-size="10" text-anchor="middle" fill="#475569">Receipts, CRR, BS</text>'
        '<rect x="230" y="48" width="180" height="122" rx="8" fill="#fff1f2" stroke="#e11d48" stroke-width="1.5"/>'
        '<text x="320" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#9f1239">CPJ (Cash Out)</text>'
        '<text x="320" y="96" font-size="11" text-anchor="middle" fill="#1e293b">Bank Credited (-)</text>'
        f'<text x="320" y="122" font-size="13" font-weight="bold" text-anchor="middle" fill="#be123c">{_fmt_r(cpj_tot)}</text>'
        '<text x="320" y="146" font-size="10" text-anchor="middle" fill="#475569">Cheque Stubs, EFT, BS</text>'
        '<rect x="440" y="48" width="180" height="122" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="530" y="72" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e40af">Net Bank Effect</text>'
        '<text x="530" y="98" font-size="11" text-anchor="middle" fill="#1e293b">CRJ - CPJ</text>'
        f'<text x="530" y="126" font-size="14" font-weight="bold" text-anchor="middle" fill="{net_col}">{net_lbl}</text>'
        '<text x="530" y="148" font-size="10" text-anchor="middle" fill="#475569">Monthly cash change</text>'
        '</svg>'
    )


def _cheque_counterfoil_svg(
    biz_name: str,
    cheque_no: str,
    date_str: str,
    payee: str,
    reason: str,
    amt: int,
    extra_line: str = "",
) -> str:
    """Context SVG rendering a parameterized South African Cheque Counterfoil / Payment Voucher."""
    h = 225 if not extra_line else 245
    extra_svg = (
        f'<text x="24" y="180" font-size="11" fill="#475569">Breakdown: <tspan font-weight="bold" fill="#0f172a">{extra_line}</tspan></text>'
        if extra_line else ""
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 {h}" width="580" height="{h}">'
        f'<rect width="580" height="{h}" rx="10" fill="#ffffff" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="0" y="0" width="580" height="42" rx="8" fill="#9f1239"/>'
        f'<text x="20" y="26" font-size="14" font-weight="bold" fill="#ffffff">CHEQUE COUNTERFOIL — {biz_name}</text>'
        f'<text x="560" y="26" font-size="14" font-weight="bold" text-anchor="end" fill="#fde047">No: {cheque_no}</text>'
        f'<text x="24" y="72" font-size="12" fill="#334155">Date: <tspan font-weight="bold" fill="#0f172a">{date_str}</tspan></text>'
        f'<text x="24" y="100" font-size="12" fill="#334155">To (Payee): <tspan font-weight="bold" fill="#0f172a">{payee}</tspan></text>'
        f'<text x="24" y="128" font-size="12" fill="#334155">For: <tspan font-weight="bold" fill="#0f172a">{reason}</tspan></text>'
        f'<text x="24" y="156" font-size="13" fill="#334155">Amount: <tspan font-weight="bold" fill="#be123c">{_fmt_r(amt)}</tspan></text>'
        f'{extra_svg}'
        f'<text x="556" y="{h - 14}" font-size="10" text-anchor="end" fill="#64748b">Retained in business cheque book for CPJ entry</text>'
        '</svg>'
    )


def _eft_advice_svg(
    bank_name: str,
    biz_name: str,
    ref_no: str,
    date_str: str,
    payee: str,
    amt: int,
    reason: str,
) -> str:
    """Context SVG rendering an online EFT payment confirmation slip."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 210" width="580" height="210">'
        '<rect width="580" height="210" rx="10" fill="#f8fafc" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<rect x="0" y="0" width="580" height="40" rx="8" fill="#1d4ed8"/>'
        f'<text x="20" y="25" font-size="13" font-weight="bold" fill="#ffffff">{bank_name} — EFT Payment Confirmation</text>'
        f'<text x="560" y="25" font-size="13" font-weight="bold" text-anchor="end" fill="#fde047">Ref: {ref_no}</text>'
        f'<text x="24" y="68" font-size="12" fill="#334155">From Account: <tspan font-weight="bold" fill="#0f172a">{biz_name}</tspan></text>'
        f'<text x="24" y="94" font-size="12" fill="#334155">Date Paid: <tspan font-weight="bold" fill="#0f172a">{date_str}</tspan></text>'
        f'<text x="24" y="120" font-size="12" fill="#334155">Beneficiary (Payee): <tspan font-weight="bold" fill="#0f172a">{payee}</tspan></text>'
        f'<text x="24" y="146" font-size="12" fill="#334155">Reference / Reason: <tspan font-weight="bold" fill="#0f172a">{reason}</tspan></text>'
        f'<text x="556" y="182" font-size="15" font-weight="bold" text-anchor="end" fill="#be123c">Paid: {_fmt_r(amt)}</text>'
        '</svg>'
    )


def _cpj_bank_stmt_svg(
    bank_name: str,
    biz_name: str,
    month_full: str,
    entries: List[Tuple[str, str, int]],
) -> str:
    """Context SVG rendering a Bank Statement debit extract (fees, debit orders)."""
    rows_svg = []
    y = 86
    for dt, desc, amt in entries:
        rows_svg.append(
            f'<text x="24" y="{y}" font-size="11" fill="#1e293b">{dt}</text>'
            f'<text x="96" y="{y}" font-size="11" fill="#1e293b">{desc}</text>'
            f'<text x="576" y="{y}" font-size="11" font-weight="bold" text-anchor="end" fill="#be123c">-{_fmt_r(amt)}</text>'
        )
        y += 24
    h = max(165, y + 24)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {h}" width="600" height="{h}">'
        f'<rect width="600" height="{h}" rx="8" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>'
        '<rect x="0" y="0" width="600" height="42" rx="6" fill="#0f766e"/>'
        f'<text x="20" y="26" font-size="13" font-weight="bold" fill="#ffffff">{bank_name} — Bank Statement ({month_full})</text>'
        f'<text x="24" y="62" font-size="11" font-weight="bold" fill="#475569">Account Holder: {biz_name}</text>'
        '<text x="576" y="62" font-size="11" font-weight="bold" text-anchor="end" fill="#475569">Debit (Deduction)</text>'
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
        "learning_objective_id": f"lo_g8_cpj_{subskill}",
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
        "diagnostic_tags": ["accounting", "cash_payments_journal", "service_business"],
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
        "learning_objective_id": f"lo_g8_cpj_{subskill}",
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
        "diagnostic_tags": ["accounting", "cash_payments_journal", "service_business"],
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
    journal_type: str = "cpj",
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
        "learning_objective_id": f"lo_g8_cpj_{subskill}",
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
        "diagnostic_tags": ["accounting", "cash_payments_journal", "ledger_table"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _cpj_journal_question(
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
    headers: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Build a 2D interactive CPJ table question."""
    hdrs = list(headers or CPJ_HEADERS)
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    str_rows: List[List[str]] = []
    marking_points: List[Dict[str, Any]] = []
    money_cols = {4, 5, 6, 7}

    default_col_hints = {
        0: "Enter payment document code (e.g. C01, EFT1, BS, or blank on Totals).",
        1: "Enter the day of the month (or blank on Totals).",
        2: "Enter the payee name ('Cash' for cash wages/float, or supplier/bank name).",
        3: "Enter folio reference for Sundry items (e.g. B2, N5) or leave blank.",
        4: "Enter the total cheque/EFT/BS amount paid from Bank.",
        5: f"Enter {hdrs[5]} expense here if applicable; otherwise leave blank.",
        6: f"Enter {hdrs[6]} expense here if applicable; otherwise leave blank.",
        7: "Enter non-column payment amounts (Equipment, Drawings, Rent, Loan, Bank charges) here.",
        8: "Name the Sundry General Ledger account (e.g. Equipment, Drawings, Bank charges).",
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
                            "desc": f"Row {r_i + 1} {hdrs[c_i]}: {val}",
                            "marks": 1,
                            "editable": True,
                        }
                    )
                    mp_idx += 1
        rows.append(row_cells)

    if not marking_points:
        marking_points = [{"id": "mp_1", "desc": "Accurate journal entries completed", "marks": 2, "editable": True}]

    marks = sum(mp["marks"] for mp in marking_points)
    md = _md_table(hdrs, str_rows)
    worked = f"**Completed Cash Payments Journal ({marks} marks)**\n\n{md}\n\n**Accounting Notes:**\n{explanation_notes}"
    return _build_table(
        rng,
        qid_prefix=qid_prefix,
        subskill=subskill,
        title=title,
        prompt=prompt,
        headers=hdrs,
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
        journal_type="cpj",
        diagram_spec=diagram_spec,
    )


# ---------------------------------------------------------------------------
# Archetypes 01 - 25
# ---------------------------------------------------------------------------

def build_01_cpj_purpose_cash_out_diary(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    crj_tot = rng.randint(25, 60) * 1000
    cpj_tot = rng.randint(12, 24) * 1000
    svg = _cpj_crj_flow_svg(ctx["biz_name"], crj_tot, cpj_tot)
    prompt = (
        f"Study the Cash Flow Journals overview diagram for {ctx['biz_name']} in {ctx['month_full']} "
        f"(CRJ receipts {_fmt_r(crj_tot)} vs CPJ payments {_fmt_r(cpj_tot)}). "
        f"What is the primary purpose of the Cash Payments Journal ({ctx['cpj_no']})?"
    )
    return _build_mcq(
        rng,
        qid_prefix="cpj01",
        subskill="01_cpj_purpose_cash_out_diary",
        title="Purpose of the Cash Payments Journal (Cash Out Diary)",
        prompt=prompt,
        correct_text=f"To record every actual cash, cheque, EFT, and bank debit outflow paid out by the business ({_fmt_r(cpj_tot)} total), summarising them before posting to the General Ledger",
        distractors=[
            f"To record cash received from customers and deposits into Bank ({_fmt_r(crj_tot)})",
            "To list supplier invoices bought strictly on 60-day credit with no cash paid",
            "To track personal household purchases paid out of the owner's private wallet",
        ],
        explanation=(
            f"The CPJ serves as the business's 'Cash Out' diary. Every rand flowing out of {ctx['biz_name']}'s bank account "
            f"(totalling {_fmt_r(cpj_tot)}) is classified in the CPJ before monthly column totals post to the General Ledger."
        ),
        hints={
            "tier_1": "Contrast the direction of money in CRJ ('Cash In') versus CPJ.",
            "tier_2": "Only actual money leaving the business bank account belongs in the CPJ.",
            "tier_3": "Match the option describing cash/cheque/EFT/bank-statement outflows summarised for the General Ledger.",
        },
        misconception_tags=["cpj_crj_direction_confused"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_02_cpj_heading_three_required_elements(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    j_num = rng.randint(2, 11)
    headers = ["Heading Field", "Required CPJ Entry"]
    items = [
        ("1. Journal Name & Business", f"Cash Payments Journal of {ctx['biz_name']}"),
        ("2. Month and Year", ctx["month_full"]),
        ("3. Journal Code", f"CPJ{j_num}"),
    ]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    for r_i, (lbl, exp) in enumerate(items):
        str_rows.append([lbl, exp])
        c0 = _cell(r_i, 0, lbl, editable=False)
        c1 = _cell(r_i, 1, exp, editable=True)
        rows.append([c0, c1])
        cmap[c1["cell_id"]] = exp
        chints[c1["cell_id"]] = f"State the exact {lbl.split('. ')[1].lower()} from the business scenario."
        mps.append({"id": f"mp_{r_i + 1}", "desc": f"{lbl}: {exp}", "marks": 1, "editable": True})
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj02",
        subskill="02_cpj_heading_three_required_elements",
        title="Three Mandatory Elements of a CPJ Heading",
        prompt=f"{ctx['biz_name']} is preparing its {j_num}th Cash Payments Journal for {ctx['month_full']}. Complete the three required heading fields.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CPJ Heading (3 marks)**\n\n{md}",
        sample_answer=md,
        marks=3,
        hints={
            "tier_1": "Every subsidiary journal heading needs the book & owner name, period, and sequential code.",
            "tier_2": "Remember to change 'Receipts' to 'Payments' and use 'CPJ' instead of 'CRJ'.",
            "tier_3": f"Cash Payments Journal of {ctx['biz_name']} | {ctx['month_full']} | CPJ{j_num}.",
        },
        marking_points=mps,
        misconception_tags=["cpj_heading_missing_fields"],
        qtype="table_completion",
        journal_type="heading",
    )


def build_03_cpj_cash_only_exclusion_of_credit_purchases(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt_paid = _fmt_r(rng.randint(12, 42) * 100)
    amt_credit = _fmt_r(rng.randint(25, 65) * 100)
    amt_rec = _fmt_r(rng.randint(15, 38) * 100)
    variant = rng.choice(["find_excluded", "find_included"])
    if variant == "find_excluded":
        prompt = f"Which event at {ctx['biz_name']} must NOT be recorded in the Cash Payments Journal ({ctx['cpj_no']})?"
        correct = f"Ordered equipment worth {amt_credit} from {ctx['supplier']} on 30 days' credit with no payment made yet"
        dists = [
            f"Paid {ctx['supplier']} {amt_paid} by EFT for stationery and cleaning supplies",
            f"Cashed a cheque for {amt_rec} to pay weekly staff wages",
            f"{ctx['bank_name']} deducted monthly service fees of {_fmt_r(285)} on the Bank Statement",
        ]
        expl = "Buying on credit (or ordering without paying) involves NO immediate cash outflow, so it stays out of the CPJ until actually paid."
    else:
        prompt = f"Which of these events at {ctx['biz_name']} MUST be entered in the Cash Payments Journal ({ctx['cpj_no']})?"
        correct = f"Paid {ctx['municipality']} {amt_paid} by business EFT for water and electricity"
        dists = [
            f"Received {amt_rec} from walk-in clients for {ctx['svc_desc']}",
            f"Received a price quotation of {amt_credit} from {ctx['supplier']} for new chairs",
            f"Tenant {ctx['landlord']} transferred rent into another unrelated person's account",
        ]
        expl = "Paying the municipal account via business EFT reduces the business's Bank balance, so it belongs in the CPJ."
    return _build_mcq(
        rng,
        qid_prefix="cpj03",
        subskill="03_cpj_cash_only_exclusion_of_credit_purchases",
        title="Cash-Only Scope of the CPJ",
        prompt=prompt,
        correct_text=correct,
        distractors=dists,
        explanation=expl,
        hints={
            "tier_1": "Ask: did real money leave the business bank account right now?",
            "tier_2": "Exclude credit orders/quotations (no money paid) and cash inflows (CRJ).",
            "tier_3": "Match the rule above to the exact transaction wording.",
        },
        misconception_tags=["credit_purchase_entered_in_cpj"],
    )


def build_04_cpj_source_doc_cheque_counterfoil_and_eft(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_no = f"C{rng.randint(101, 189)}"
    day = f"{rng.randint(3, 24):02d}"
    amt = rng.randint(18, 65) * 100
    svg = _cheque_counterfoil_svg(ctx["biz_name"], c_no, f"{day} {ctx['month_full']}", ctx["supplier"], "Stationery & printer ink", amt)
    prompt = (
        f"Inspect the source document stub below for {ctx['biz_name']} ({c_no}, {day} {ctx['month_full']}, paid to {ctx['supplier']}, {_fmt_r(amt)}). "
        f"Why does {ctx['biz_name']} use this Cheque Counterfoil (or an EFT payment confirmation) as the source document for {ctx['cpj_no']}?"
    )
    return _build_mcq(
        rng,
        qid_prefix="cpj04",
        subskill="04_cpj_source_doc_cheque_counterfoil_and_eft",
        title="Cheque Counterfoil & EFT Confirmation in the CPJ",
        prompt=prompt,
        correct_text=f"Because the original cheque goes to {ctx['supplier']}, leaving the counterfoil stub ({c_no}) in the business book as proof of what was paid and why",
        distractors=[
            "Because cheque counterfoils are issued only when cash customers pay for services rendered",
            "Because counterfoils act as the Cash Register Roll for daily till receipts",
            "Because counterfoils record unapproved supplier quotes before purchase",
        ],
        explanation=(
            f"Just as receipts keep a duplicate copy for inflows, cheque payments leave behind the Cheque Counterfoil ({c_no}), "
            f"and electronic payments leave an EFT confirmation slip containing date, payee, reason, and {_fmt_r(amt)}."
        ),
        hints={
            "tier_1": "When you tear out a cheque or submit an online transfer, what record stays inside the business?",
            "tier_2": "The payee gets the cheque/funds; the business retains the stub (counterfoil) or EFT slip.",
            "tier_3": f"The retained counterfoil ({c_no}) records payee, reason, date, and amount for CPJ entry.",
        },
        misconception_tags=["cheque_counterfoil_purpose_confused"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_05_cpj_source_doc_original_receipt_and_invoice(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(15, 45) * 100)
    return _build_mcq(
        rng,
        qid_prefix="cpj05",
        subskill="05_cpj_source_doc_original_receipt_and_invoice",
        title="Original Receipt / Cash Invoice (CPJ) vs Duplicate Receipt (CRJ)",
        prompt=(
            f"{ctx['biz_name']} pays {ctx['landlord']} {amt} for workshop rent and receives an Original Receipt at the counter. "
            f"Why does an ORIGINAL receipt/cash invoice go into the CPJ whereas a DUPLICATE receipt goes into the CRJ?"
        ),
        correct_text="When paying out money, the payer receives and files the original receipt/cash invoice (CPJ); when receiving money, the business hands out the original and files the duplicate (CRJ)",
        distractors=[
            "Original receipts are always thrown away and only duplicates exist in accounting",
            "Original receipts are exclusively for bank loans received by the business",
            "Duplicate receipts belong in the CPJ because cash leaves the till",
        ],
        explanation="Whoever pays the money keeps the ORIGINAL document (so Original Receipt / Cash Invoice supports the CPJ), while whoever receives the money issues the original and retains the DUPLICATE (supporting the CRJ).",
        hints={
            "tier_1": "Remember who walks away with the top (original) page of a receipt book.",
            "tier_2": "The party paying cash receives the original; the party receiving cash keeps the duplicate.",
            "tier_3": "Paying -> you receive Original Receipt/Invoice (CPJ); Receiving -> you keep Duplicate Receipt (CRJ).",
        },
        misconception_tags=["original_vs_duplicate_receipt_confusion"],
    )


def build_06_cpj_source_doc_bank_statement_charges_and_debit_orders(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    fee = rng.randint(18, 45) * 10 + 5
    d_order = rng.randint(12, 35) * 100
    svg = _cpj_bank_stmt_svg(
        ctx["bank_name"],
        ctx["biz_name"],
        ctx["month_full"],
        [
            (f"25 {ctx['month_short']}", "Debit order — Business Insurance", d_order),
            (f"30 {ctx['month_short']}", "Monthly bank service & card fees", fee),
        ],
    )
    prompt = (
        f"Inspect the Bank Statement debit extract below from {ctx['bank_name']} for {ctx['biz_name']} "
        f"(Insurance debit order {_fmt_r(d_order)} and Bank charges {_fmt_r(fee)}). "
        f"Which Doc No code and journal must be used to record these deductions?"
    )
    return _build_mcq(
        rng,
        qid_prefix="cpj06",
        subskill="06_cpj_source_doc_bank_statement_charges_and_debit_orders",
        title="Bank Statement Deductions in the CPJ",
        prompt=prompt,
        correct_text="Doc No: BS in the Cash Payments Journal (CPJ), because money was deducted from the business bank account",
        distractors=[
            "Doc No: BS in the Cash Receipts Journal (CRJ), because the bank statement always means cash in",
            "Doc No: CRR in the CPJ, because debit orders come from the cash register till",
            "Omit both deductions completely because no paper cheque was written",
        ],
        explanation=f"Bank charges ({_fmt_r(fee)}) and debit orders ({_fmt_r(d_order)}) reduce the Bank balance directly on the Bank Statement, so they are recorded as 'BS' in the CPJ.",
        hints={
            "tier_1": "Notice the minus sign and 'Deduction' header: money is leaving the business bank account.",
            "tier_2": "Every bank-statement cash outflow is coded 'BS' inside the Cash Payments Journal.",
            "tier_3": "Select Doc No 'BS' in the CPJ.",
        },
        misconception_tags=["bank_charges_entered_in_crj", "omitted_bank_statement_debits"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_07_cpj_source_doc_matching_table(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    items = [
        (f"Paid {ctx['supplier']} {_fmt_r(1450)} by cheque #42 for equipment", "Cheque counterfoil"),
        (f"Transferred {_fmt_r(3200)} online to {ctx['municipality']} for electricity", "EFT confirmation"),
        (f"Paid {_fmt_r(890)} cash/card at counter and got top copy of receipt", "Original receipt"),
        (f"{ctx['bank_name']} charged {_fmt_r(215)} monthly account fee on statement", "Bank statement"),
    ]
    rng.shuffle(items)
    headers = ["Payment Event", "CPJ Source Document"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    for r_i, (ev, doc) in enumerate(items):
        str_rows.append([ev, doc])
        c0 = _cell(r_i, 0, ev, editable=False)
        c1 = _cell(r_i, 1, doc, editable=True)
        rows.append([c0, c1])
        cmap[c1["cell_id"]] = doc
        chints[c1["cell_id"]] = "Choose: Cheque counterfoil, EFT confirmation, Original receipt, or Bank statement."
        mps.append({"id": f"mp_{r_i + 1}", "desc": doc, "marks": 1, "editable": True})
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj07",
        subskill="07_cpj_source_doc_matching_table",
        title="Matching CPJ Payments to Source Documents",
        prompt=f"Match each cash outflow at {ctx['biz_name']} to its exact CPJ source document: Cheque counterfoil, EFT confirmation, Original receipt, or Bank statement.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CPJ Source Document Matching (4 marks)**\n\n{md}",
        sample_answer=md,
        marks=4,
        hints={
            "tier_1": "Think about the document retained by the payer for each payment method.",
            "tier_2": "Cheque -> Cheque counterfoil; online bank payment -> EFT confirmation; counter receipt -> Original receipt; bank fee -> Bank statement.",
            "tier_3": "Match the exact labels provided in the prompt.",
        },
        marking_points=mps,
        misconception_tags=["cpj_source_document_mismatch"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_08_cpj_payee_rule_cash_for_wages_and_float(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_no = f"C{rng.randint(201, 250)}"
    day = f"{rng.randint(5, 25):02d}"
    amt = rng.randint(16, 48) * 100
    purpose = rng.choice(["Weekly staff wages", "Replenish till cash float"])
    svg = _cheque_counterfoil_svg(ctx["biz_name"], c_no, f"{day} {ctx['month_short']}", "Cash", purpose, amt)
    prompt = (
        f"Inspect the cheque counterfoil below ({c_no}, {day} {ctx['month_short']}, {_fmt_r(amt)} for {purpose}). "
        f"Why is 'Cash' written in the 'Name of Payee' column of {ctx['cpj_no']} instead of a specific staff member's or supplier's name?"
    )
    return _build_mcq(
        rng,
        qid_prefix="cpj08",
        subskill="08_cpj_payee_rule_cash_for_wages_and_float",
        title="Using 'Cash' as Name of Payee for Wages / Cash Float",
        prompt=prompt,
        correct_text="Because the cheque is drawn to withdraw physical cash at the bank (to distribute wages or keep as a till cash float), not paid directly to an external supplier",
        distractors=[
            "Because South African accounting forbids writing any employee's wages inside the CPJ",
            "Because 'Cash' means the business received money in the Cash Receipts Journal",
            "Because the payee's name is only ever entered under Sundry Details",
        ],
        explanation=f"When cash is drawn from the bank for {purpose.lower()} ({_fmt_r(amt)}), the cheque is payable to 'Cash', so 'Cash' is entered in `Name of Payee`.",
        hints={
            "tier_1": "Think about how the cashier withdraws physical banknotes from the bank for the till or weekly pay packets.",
            "tier_2": "A cheque made out to 'Cash' withdraws physical cash rather than paying an outside company.",
            "tier_3": "Therefore Name of Payee = 'Cash'.",
        },
        misconception_tags=["cash_payee_rule_misunderstood"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_09_cpj_bank_column_total_payment_credit_rule(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = rng.randint(25, 85) * 100
    return _build_mcq(
        rng,
        qid_prefix="cpj09",
        subskill="09_cpj_bank_column_total_payment_credit_rule",
        title="How the CPJ Bank Column Posts to the General Ledger",
        prompt=(
            f"At month-end, {ctx['biz_name']}'s {ctx['cpj_no']} has a total Bank column of {_fmt_r(amt)}. "
            f"Which side of the General Ledger Bank account receives this {_fmt_r(amt)} CPJ total, and why?"
        ),
        correct_text=f"Credit side of Bank (- Asset), because every CPJ entry represents money paid OUT of the business bank account",
        distractors=[
            f"Debit side of Bank (+ Asset), because Bank is always debited from every journal",
            "Debit side of Current Income, because expenses reduce income directly",
            "It is never posted to Bank because Analysis columns replace Bank",
        ],
        explanation=f"Bank is an Asset (increases Debit, decreases Credit). Since CPJ totals ({_fmt_r(amt)}) represent cash outflows, Total Payments are CREDITED to Bank.",
        hints={
            "tier_1": "Apply DEAD CLIC: Bank is an Asset. Does paying money increase or decrease Bank?",
            "tier_2": "Paying decreases an Asset, and Assets decrease on the Credit side.",
            "tier_3": "Credit Bank with the CPJ Bank column total.",
        },
        misconception_tags=["cpj_bank_debited_instead_of_credited"],
    )


def build_10_cpj_column_sequence_identification(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    missing_set = rng.choice([(2, 4, 5), (4, 6, 7), (2, 5, 8)])
    headers = ["Position", "CPJ Column Heading"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for idx, col in enumerate(CPJ_HEADERS):
        lbl = f"Column {idx + 1}"
        str_rows.append([lbl, col])
        editable = idx in missing_set
        c0 = _cell(idx, 0, lbl, editable=False)
        c1 = _cell(idx, 1, col, editable=editable)
        rows.append([c0, c1])
        if editable:
            cmap[c1["cell_id"]] = col
            chints[c1["cell_id"]] = f"Check standard CPJ order after {CPJ_HEADERS[max(0, idx - 1)]}."
            mps.append({"id": f"mp_{mp_i}", "desc": f"Column {idx + 1}: {col}", "marks": 1, "editable": True})
            mp_i += 1
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj10",
        subskill="10_cpj_column_sequence_identification",
        title="Standard Column Sequence of the CPJ",
        prompt=f"{ctx['entrepreneur']} is ruling up {ctx['cpj_no']} for {ctx['biz_name']} in {ctx['month_full']}. Complete the 3 missing column headings.",
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**Standard CPJ Column Layout (3 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "Notice there is NO 'Analysis of Receipts' column in a CPJ — it moves straight from Fol. to Bank.",
            "tier_2": "Sequence: Doc No, Day, Name of Payee, Fol., Bank, Wages, Stationery, Sundry Amount, Sundry Details.",
            "tier_3": "Fill in the exact missing column headings.",
        },
        marking_points=mps,
        misconception_tags=["cpj_column_order_error"],
        qtype="table_completion",
        journal_type="structure",
    )


def build_11_cpj_no_analysis_of_receipts_column_reason(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    amt = _fmt_r(rng.randint(15, 45) * 100)
    return _build_mcq(
        rng,
        qid_prefix="cpj11",
        subskill="11_cpj_no_analysis_of_receipts_column_reason",
        title="Why the CPJ Has No Analysis of Receipts Column",
        prompt=(
            f"When preparing {ctx['cpj_no']} for {ctx['biz_name']} (e.g. a cheque/EFT payment of {amt}), "
            f"why is there NO 'Analysis of Receipts' column like in the CRJ?"
        ),
        correct_text="Because payments leave the bank account individually per cheque/EFT/debit order, rather than being collected in a cash till awaiting one daily bank deposit",
        distractors=[
            "Because the CPJ never interacts with the business Bank account",
            "Because multiple supplier payments are held in the till for a week before entering Bank",
            "Because payments are always counted as income first",
        ],
        explanation="In the CRJ, till cash is held in Analysis of Receipts until banked once per day. In the CPJ, each cheque or EFT pays out of Bank immediately, so the amount goes straight into the Bank column.",
        hints={
            "tier_1": "Remember why Analysis of Receipts existed in the CRJ in the first place.",
            "tier_2": "Till receipts accumulate before ONE daily deposit; cheques and EFTs leave Bank one by one.",
            "tier_3": "Therefore each CPJ payment goes straight into Bank without needing a staging column.",
        },
        misconception_tags=["expected_analysis_column_in_cpj"],
    )


def build_12_cpj_dedicated_analysis_columns_selection(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    items = [
        (f"Weekly staff pay ({_fmt_r(2400)}) for {ctx['svc_desc']}", "Wages", "Analysis column"),
        (f"Printer paper & receipt books ({_fmt_r(680)}) from {ctx['supplier']}", "Stationery", "Analysis column"),
        (f"Buying a new computer ({_fmt_r(9500)}) once a year", "Equipment", "Sundry Accounts"),
        (f"Monthly business telephone & water account ({_fmt_r(1150)})", "Water & electricity", "Sundry Accounts"),
    ]
    rng.shuffle(items)
    headers = ["Payment Description", "General Ledger Account", "Dedicated Analysis or Sundry?"]
    rows, cmap, chints, str_rows, mps = [], {}, {}, [], []
    mp_i = 1
    for r_i, (desc, acct, kind) in enumerate(items):
        str_rows.append([desc, acct, kind])
        c0 = _cell(r_i, 0, desc, editable=False)
        c1 = _cell(r_i, 1, acct, editable=True)
        c2 = _cell(r_i, 2, kind, editable=True)
        rows.append([c0, c1, c2])
        cmap[c1["cell_id"]] = acct
        cmap[c2["cell_id"]] = kind
        chints[c1["cell_id"]] = "Name the exact account (Wages, Stationery, Equipment, or Water & electricity)."
        chints[c2["cell_id"]] = "Given standard CPJ columns Bank | Wages | Stationery | Sundry, choose 'Analysis column' or 'Sundry Accounts'."
        mps.append({"id": f"mp_{mp_i}", "desc": f"Account: {acct}", "marks": 1, "editable": True})
        mps.append({"id": f"mp_{mp_i + 1}", "desc": f"Classification: {kind}", "marks": 1, "editable": True})
        mp_i += 2
    md = _md_table(headers, str_rows)
    return _build_table(
        rng,
        qid_prefix="cpj12",
        subskill="12_cpj_dedicated_analysis_columns_selection",
        title="Dedicated Analysis Columns vs Sundry Accounts in CPJ",
        prompt=(
            f"{ctx['biz_name']}'s {ctx['cpj_no']} has dedicated analysis columns for **Wages** and **Stationery** (plus **Sundry Accounts**). "
            f"Classify each payment below by its General Ledger account and whether it uses an 'Analysis column' or 'Sundry Accounts'."
        ),
        headers=headers,
        rows=rows,
        correct_map=cmap,
        cell_hints=chints,
        worked_solution=f"**CPJ Analysis Column Selection (8 marks)**\n\n{md}",
        sample_answer=md,
        marks=len(mps),
        hints={
            "tier_1": "Frequent payments (Wages, Stationery) get their own columns; infrequent/other items use Sundry Accounts.",
            "tier_2": "Only items matching the dedicated column headings go into 'Analysis column'.",
            "tier_3": "Equipment and Water & electricity have no dedicated column here -> Sundry Accounts.",
        },
        marking_points=mps,
        misconception_tags=["analysis_vs_sundry_confusion"],
        qtype="table_completion",
        journal_type="classification",
    )


def build_13_cpj_single_wages_cash_cheque_row(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_no = f"C{rng.randint(10, 48)}"
    day = f"{rng.randint(5, 26):02d}"
    amt = _fmt_r(rng.randint(18, 46) * 100)
    prompt = (
        f"Record this single transaction in {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}): "
        f"On Day {day}, cashed cheque {c_no} for {amt} to pay weekly wages. Leave unused cells blank."
    )
    row_specs = [
        ([c_no, day, "Cash", "", amt, amt, "", "", ""], [0, 1], {
            2: "Remember the Payee rule for cash cheques drawn for wages!",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj13",
        subskill="13_cpj_single_wages_cash_cheque_row",
        title="Recording a Cash Cheque for Weekly Wages",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"- `Name of Payee` is `Cash`.\n- Enter {amt} in `Bank` and `Wages`; keep `Stationery`, `Fol.`, and `Sundry` blank.",
        hints={
            "tier_1": "Cash cheques for wages use a special payee word rather than 'Wages'.",
            "tier_2": "Write 'Cash' in Name of Payee, and use the dedicated Wages column.",
            "tier_3": f"Bank = {amt}, Wages = {amt}, all Stationery/Sundry cells blank.",
        },
        misconception_tags=["wages_written_as_payee", "wages_put_in_sundry"],
    )


def build_14_cpj_single_stationery_supplier_payment_row(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"EFT{rng.randint(11, 59)}"
    day = f"{rng.randint(3, 25):02d}"
    amt = _fmt_r(rng.randint(6, 28) * 100 + rng.choice([0, 50]))
    prompt = (
        f"Record this payment in {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}): "
        f"On Day {day}, paid {ctx['supplier']} {amt} via {doc} for invoice books, pens, and printer paper."
    )
    row_specs = [
        ([doc, day, ctx["supplier"], "", amt, "", amt, "", ""], [0, 1], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj14",
        subskill="14_cpj_single_stationery_supplier_payment_row",
        title="Recording a Stationery Payment in the CPJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Paper, pens, and receipt books are classified as `Stationery` ({amt}), paid to `{ctx['supplier']}`.",
        hints={
            "tier_1": "Identify who received the payment and which dedicated analysis column covers paper/pens.",
            "tier_2": f"Name of Payee = {ctx['supplier']}; analysis column = Stationery.",
            "tier_3": f"Enter {amt} in Bank and Stationery; leave Wages and Sundry blank.",
        },
        misconception_tags=["stationery_in_sundry"],
    )


def build_15_cpj_single_material_costs_or_consumables_row(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"C{rng.randint(31, 69)}"
    day = f"{rng.randint(4, 24):02d}"
    amt = _fmt_r(rng.randint(14, 42) * 100)
    custom_hdrs = ["Doc No", "Day", "Name of Payee", "Fol.", "Bank", "Material costs", "Stationery", "Sundry Amount", "Sundry Details"]
    prompt = (
        f"A service business uses the CPJ columns provided in the table (including **Material costs** and **Stationery**). "
        f"Record this payment for {ctx['biz_name']} ({ctx['month_full']}): "
        f"On Day {day}, paid {ctx['supplier']} {amt} (Cheque {doc}) for consumable supplies used directly in {ctx['svc_desc']}."
    )
    row_specs = [
        ([doc, day, ctx["supplier"], "", amt, amt, "", "", ""], [0, 1], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj15",
        subskill="15_cpj_single_material_costs_or_consumables_row",
        title="Recording Material Costs / Consumable Goods in CPJ",
        prompt=prompt,
        row_specs=row_specs,
        headers=custom_hdrs,
        explanation_notes=f"Service consumables used directly to deliver {ctx['svc_desc']} enter the `Material costs` analysis column ({amt}).",
        hints={
            "tier_1": "Consumable supplies used directly to perform services go to Material costs (not Stationery).",
            "tier_2": f"Name of Payee = {ctx['supplier']}; Bank = {amt}; Material costs = {amt}.",
            "tier_3": "Keep Stationery and Sundry columns blank.",
        },
        misconception_tags=["material_costs_confused_with_stationery"],
    )


def build_16_cpj_sundry_equipment_asset_purchase(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"EFT{rng.randint(20, 75)}"
    day = f"{rng.randint(2, 18):02d}"
    amt = _fmt_r(rng.randint(4, 18) * 1000)
    item = rng.choice(["a laptop and colour printer", "workshop tools and workbench", "two reception desks and salon chairs"])
    prompt = (
        f"Record this asset purchase in {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}): "
        f"On Day {day}, paid {ctx['supplier']} {amt} ({doc}) for {item} (folio B2)."
    )
    row_specs = [
        ([doc, day, ctx["supplier"], "B2", amt, "", "", amt, "Equipment"], [0, 1, 3], {
            8: "Enter the Balance Sheet asset account: Equipment.",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj16",
        subskill="16_cpj_sundry_equipment_asset_purchase",
        title="Recording an Equipment Purchase in Sundry Accounts",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Furniture, computers, and workshop machinery are long-term assets classified as `Equipment` in `Sundry Accounts` ({amt}).",
        hints={
            "tier_1": "Equipment is not Wages or Stationery — so which section handles it?",
            "tier_2": "Use Sundry Accounts and name the General Ledger asset account.",
            "tier_3": f"Bank = {amt}, Sundry Amount = {amt}, Sundry Details = Equipment.",
        },
        misconception_tags=["equipment_entered_in_stationery"],
    )


def build_17_cpj_sundry_vehicle_or_premises_repair_expense(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"C{rng.randint(41, 88)}"
    day = f"{rng.randint(8, 25):02d}"
    amt = _fmt_r(rng.randint(15, 55) * 100)
    choice = rng.choice([
        ("delivery scooter service & brake repair", "Repairs", "N6", "Repairs is an operating expense (keeping an existing asset working), NOT buying a new asset."),
        ("installing a solar inverter system in a delivery van", "Vehicles", "B3", "Major permanent vehicles/deliveries belong under Vehicles (or Equipment). Here paying a mechanic for maintenance is Repairs; let's test Repairs clearly!"),
    ])
    # Force clean Repairs variant with varied items for crisp curriculum alignment
    work_item = rng.choice(["repairing a broken air-conditioner", "servicing the workshop compressor", "fixing leaking workshop pipes"])
    prompt = (
        f"On Day {day} ({ctx['month_full']}), {ctx['biz_name']} paid {ctx['competitor']} {amt} by cheque {doc} for {work_item} (folio N6). "
        f"Record this maintenance payment in {ctx['cpj_no']}."
    )
    row_specs = [
        ([doc, day, ctx["competitor"], "N6", amt, "", "", amt, "Repairs"], [0, 1, 3], {
            8: "Maintenance of existing assets is recorded under 'Repairs' (not Equipment).",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj17",
        subskill="17_cpj_sundry_vehicle_or_premises_repair_expense",
        title="Recording Repairs & Maintenance vs Purchasing Assets",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Fixing existing workshop items ({work_item}) is an operating expense called `Repairs` in `Sundry Accounts` ({amt}), not a new asset purchase.",
        hints={
            "tier_1": "Ask: did the business acquire a brand-new asset, or restore an existing one?",
            "tier_2": "Fixing/servicing existing property or equipment uses the Repairs account in Sundry.",
            "tier_3": f"Bank = {amt}, Sundry Amount = {amt}, Sundry Details = Repairs.",
        },
        misconception_tags=["repairs_confused_with_equipment"],
    )


def build_18_cpj_sundry_water_and_electricity_municipal_payment(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    ref = f"EFT{rng.randint(301, 499)}"
    day = f"{rng.randint(14, 27):02d}"
    amt = rng.randint(12, 44) * 100
    amt_s = _fmt_r(amt)
    svg = _eft_advice_svg(ctx["bank_name"], ctx["biz_name"], ref, f"{day} {ctx['month_short']}", ctx["municipality"], amt, "Municipal Water & Electricity")
    prompt = (
        f"Inspect the EFT payment confirmation below for {ctx['biz_name']} ({ref}, {day} {ctx['month_short']}, paid to {ctx['municipality']}, {amt_s}). "
        f"Enter this payment into {ctx['cpj_no']} (folio N7)."
    )
    row_specs = [
        ([ref, day, ctx["municipality"], "N7", amt_s, "", "", amt_s, "Water and electricity"], [3], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj18",
        subskill="18_cpj_sundry_water_and_electricity_municipal_payment",
        title="Recording Municipal Water & Electricity from an EFT Slip",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Read `{ref}`, Day `{day}`, Payee `{ctx['municipality']}`, and Amount `{amt_s}` from the EFT confirmation into `Sundry Accounts` (`Water and electricity`).",
        hints={
            "tier_1": "Read the reference number, day, beneficiary, and amount directly from the EFT slip.",
            "tier_2": "Municipal utility bills belong in Sundry Accounts.",
            "tier_3": f"Bank = {amt_s}, Sundry Amount = {amt_s}, Sundry Details = Water and electricity.",
        },
        misconception_tags=["municipal_bill_misclassified"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_19_cpj_sundry_rent_expense_paid_to_landlord(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"EFT{rng.randint(12, 48)}"
    day = f"{rng.randint(1, 5):02d}"
    amt = _fmt_r(rng.randint(35, 85) * 100)
    prompt = (
        f"On Day {day} ({ctx['month_full']}), {ctx['biz_name']} paid {ctx['landlord']} {amt} via {doc} for the monthly shop lease (folio N4). "
        f"Record this entry in {ctx['cpj_no']} — be careful to distinguish Rent expense from Rent income!"
    )
    row_specs = [
        ([doc, day, ctx["landlord"], "N4", amt, "", "", amt, "Rent expense"], [0, 1, 3], {
            8: "Because the business is PAYING rent (CPJ), the account is 'Rent expense' (not Rent income).",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj19",
        subskill="19_cpj_sundry_rent_expense_paid_to_landlord",
        title="Recording Rent Expense in the CPJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Paying a landlord ({ctx['landlord']}) is recorded as `Rent expense` in the CPJ (`{amt}`), whereas receiving rent from a tenant is `Rent income` in the CRJ.",
        hints={
            "tier_1": "Is the business earning rent or paying rent in the CPJ?",
            "tier_2": "Paying rent creates an expense in Sundry Details.",
            "tier_3": f"Bank = {amt}, Sundry Amount = {amt}, Sundry Details = Rent expense.",
        },
        misconception_tags=["rent_expense_labeled_rent_income"],
    )


def build_20_cpj_sundry_bank_charges_bank_statement_entry(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(28, 30):02d}"
    fee = rng.randint(16, 48) * 10 + rng.choice([0, 5])
    fee_s = _fmt_r(fee)
    svg = _cpj_bank_stmt_svg(ctx["bank_name"], ctx["biz_name"], ctx["month_full"], [(f"{day} {ctx['month_short']}", "Monthly ledger & EFT fees", fee)])
    prompt = (
        f"Inspect the Bank Statement debit entry below from {ctx['bank_name']} ({day} {ctx['month_short']}, bank fees {fee_s}). "
        f"Record this deduction in {ctx['cpj_no']} (folio N8)."
    )
    row_specs = [
        (["BS", day, ctx["bank_name"], "N8", fee_s, "", "", fee_s, "Bank charges"], [3], {
            0: "Entries taken straight from the Bank Statement use 'BS'.",
            2: f"Name of Payee is the bank itself ({ctx['bank_name']}).",
            8: "Use the standard General Ledger expense account: Bank charges.",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj20",
        subskill="20_cpj_sundry_bank_charges_bank_statement_entry",
        title="Recording Bank Charges from the Bank Statement in CPJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Monthly bank fees on the statement use `Doc No = BS`, `Name of Payee = {ctx['bank_name']}`, and `Sundry Details = Bank charges` ({fee_s}).",
        hints={
            "tier_1": "Code Bank Statement deductions as BS and pay the bank.",
            "tier_2": f"Payee = {ctx['bank_name']}; Sundry Details = Bank charges.",
            "tier_3": f"Doc = BS, Day = {day}, Bank = {fee_s}, Sundry Amount = {fee_s}, Sundry Details = Bank charges.",
        },
        misconception_tags=["bank_charges_missing_or_in_crj"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_21_cpj_sundry_loan_repayment_and_interest(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    day = f"{rng.randint(25, 28):02d}"
    amt = _fmt_r(rng.randint(25, 65) * 100)
    loan_acct = f"Loan: {ctx['bank_name']}"
    prompt = (
        f"On Day {day} ({ctx['month_full']}), {ctx['bank_name']} processed a monthly debit order of {amt} "
        f"to repay part of {ctx['biz_name']}'s business loan (Bank Statement BS, folio B5). Record this repayment in {ctx['cpj_no']}."
    )
    row_specs = [
        (["BS", day, ctx["bank_name"], "B5", amt, "", "", amt, loan_acct], [0, 1, 3], {
            8: f"Name the specific liability account being reduced: {loan_acct}.",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj21",
        subskill="21_cpj_sundry_loan_repayment_and_interest",
        title="Recording a Bank Loan Repayment in the CPJ",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=f"Repaying a loan via debit order (`BS`) credits Bank ({amt}) and debits `{loan_acct}` in `Sundry Accounts`.",
        hints={
            "tier_1": "Debit orders appear on the Bank Statement (BS) and reduce the Loan liability account.",
            "tier_2": f"Payee = {ctx['bank_name']}; enter {amt} in Bank and Sundry Amount.",
            "tier_3": f"Sundry Details = {loan_acct}.",
        },
        misconception_tags=["loan_repayment_classified_as_expense"],
    )


def build_22_cpj_split_payment_two_analysis_columns(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"C{rng.randint(52, 89)}"
    day = f"{rng.randint(6, 23):02d}"
    mat = rng.randint(12, 32) * 100
    stat = rng.randint(4, 15) * 100
    tot = mat + stat
    custom_hdrs = ["Doc No", "Day", "Name of Payee", "Fol.", "Bank", "Material costs", "Stationery", "Sundry Amount", "Sundry Details"]
    prompt = (
        f"Record this single SPLIT cheque payment in {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}):\n"
        f"- On Day {day}, issued cheque {doc} to {ctx['supplier']} for {_fmt_r(tot)} in total: "
        f"{_fmt_r(mat)} for workshop material costs and {_fmt_r(stat)} for office stationery."
    )
    row_specs = [
        ([doc, day, ctx["supplier"], "", _fmt_r(tot), _fmt_r(mat), _fmt_r(stat), "", ""], [0, 1], {
            4: f"Only ONE cheque was written — enter the combined sum {_fmt_r(mat)} + {_fmt_r(stat)} in Bank.",
            5: f"Enter only the material costs portion ({_fmt_r(mat)}).",
            6: f"Enter only the stationery portion ({_fmt_r(stat)}).",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj22",
        subskill="22_cpj_split_payment_two_analysis_columns",
        title="Split Cheque Allocation Across Two Analysis Columns",
        prompt=prompt,
        row_specs=row_specs,
        headers=custom_hdrs,
        explanation_notes=(
            f"- One cheque ({doc}) appears on ONE line with the full payment {_fmt_r(tot)} in `Bank`.\n"
            f"- Split across `Material costs` ({_fmt_r(mat)}) and `Stationery` ({_fmt_r(stat)}): check `{_fmt_r(mat)} + {_fmt_r(stat)} = {_fmt_r(tot)}`."
        ),
        hints={
            "tier_1": "Never split one cheque into two Bank entries! Enter the total once in Bank and divide across the columns.",
            "tier_2": f"Bank = {_fmt_r(tot)}, Material costs = {_fmt_r(mat)}, Stationery = {_fmt_r(stat)}.",
            "tier_3": "Leave Sundry columns blank because both items already have dedicated analysis columns.",
        },
        misconception_tags=["split_cheque_duplicated_in_bank", "split_allocation_sum_mismatch"],
    )


def build_23_cpj_split_payment_analysis_and_sundry_account(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    doc = f"EFT{rng.randint(60, 99)}"
    day = f"{rng.randint(7, 24):02d}"
    stat = rng.randint(5, 16) * 100
    equip = rng.randint(25, 65) * 100
    tot = stat + equip
    prompt = (
        f"Record this single split EFT payment in {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}):\n"
        f"- On Day {day}, paid {ctx['supplier']} {_fmt_r(tot)} ({doc}) in one transfer for "
        f"{_fmt_r(stat)} stationery and {_fmt_r(equip)} office equipment (folio B2)."
    )
    row_specs = [
        ([doc, day, ctx["supplier"], "B2", _fmt_r(tot), "", _fmt_r(stat), _fmt_r(equip), "Equipment"], [0, 1, 3], {
            4: f"Sum both parts into Bank: {_fmt_r(stat)} + {_fmt_r(equip)}.",
            6: f"Stationery portion = {_fmt_r(stat)}.",
            7: f"Equipment portion = {_fmt_r(equip)}.",
        }),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj23",
        subskill="23_cpj_split_payment_analysis_and_sundry_account",
        title="Split EFT Across Stationery Analysis Column & Sundry Equipment",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Single EFT of {_fmt_r(tot)} goes into `Bank` once.\n"
            f"- Allocate {_fmt_r(stat)} to `Stationery` and {_fmt_r(equip)} to `Sundry Amount` (`Equipment`)."
        ),
        hints={
            "tier_1": "One payment goes into Bank once, then splits between Stationery (analysis column) and Equipment (Sundry).",
            "tier_2": f"Bank = {_fmt_r(tot)}, Stationery = {_fmt_r(stat)}, Sundry = {_fmt_r(equip)}.",
            "tier_3": "Name the Sundry account 'Equipment' and leave Wages blank.",
        },
        misconception_tags=["split_cheque_duplicated_in_bank", "equipment_in_stationery"],
    )


def build_24_cpj_owner_drawings_vs_staff_wages(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c1, c2 = f"C{rng.randint(15, 29)}", f"C{rng.randint(31, 49)}"
    w_amt = rng.randint(18, 42) * 100
    d_amt = rng.randint(12, 34) * 100
    tot_b = w_amt + d_amt
    prompt = (
        f"Record BOTH transactions in {ctx['cpj_no']} for {ctx['biz_name']} ({ctx['month_full']}) and balance the Totals row:\n"
        f"- Day 08: Cashed cheque {c1} for {_fmt_r(w_amt)} to pay assistant staff wages.\n"
        f"- Day 16: Issued cheque {c2} to {ctx['entrepreneur']} (or personal holiday/school fees) for {_fmt_r(d_amt)} for owner's personal use (fol. B6)."
    )
    row_specs = [
        ([c1, "08", "Cash", "", _fmt_r(w_amt), _fmt_r(w_amt), "", "", ""], [0, 1], {
            2: "Staff wages cashed at bank -> Name of Payee is 'Cash'.",
        }),
        ([c2, "16", ctx["entrepreneur"], "B6", _fmt_r(d_amt), "", "", _fmt_r(d_amt), "Drawings"], [0, 1, 3], {
            8: "Owner taking business funds for personal use -> 'Drawings'.",
        }),
        (["", "", "TOTALS", "", _fmt_r(tot_b), _fmt_r(w_amt), "", _fmt_r(d_amt), ""], [0, 1, 2, 3, 6, 8], {}),
    ]
    return _cpj_journal_question(
        rng,
        qid_prefix="cpj24",
        subskill="24_cpj_owner_drawings_vs_staff_wages",
        title="Distinguishing Staff Wages ('Cash') vs Owner Drawings",
        prompt=prompt,
        row_specs=row_specs,
        explanation_notes=(
            f"- Business staff pay enters `Wages` with Payee `Cash`.\n"
            f"- Owner personal withdrawals never enter `Wages`; they enter `Sundry Accounts` under `Drawings` (reduces Owner's Equity)."
        ),
        hints={
            "tier_1": "Keep business employee wages strictly separate from the owner's personal withdrawals.",
            "tier_2": "Row 1 uses Payee 'Cash' -> Wages; Row 2 uses owner name -> Sundry 'Drawings'.",
            "tier_3": f"Totals: Bank = {_fmt_r(tot_b)}, Wages = {_fmt_r(w_amt)}, Sundry = {_fmt_r(d_amt)}.",
        },
        misconception_tags=["drawings_classified_as_wages"],
    )


def build_25_cpj_multi_row_split_cheque_bank_sum_drill(rng: random.Random) -> Dict[str, Any]:
    ctx = _biz_ctx(rng)
    c_no = f"C{rng.randint(71, 99)}"
    day = f"{rng.randint(10, 26):02d}"
    a_stat = rng.randint(4, 14) * 100
    a_mat = rng.randint(12, 28) * 100
    a_equip = rng.randint(18, 45) * 100
    tot = a_stat + a_mat + a_equip
    svg = _cheque_counterfoil_svg(
        ctx["biz_name"],
        c_no,
        f"{day} {ctx['month_short']}",
        ctx["supplier"],
        "Split business invoice",
        tot,
        extra_line=f"Stationery {_fmt_r(a_stat)} + Material {_fmt_r(a_mat)} + Equipment {_fmt_r(a_equip)}",
    )
    prompt = (
        f"Inspect the cheque counterfoil stub below ({c_no}, {day} {ctx['month_short']}) paid by {ctx['biz_name']} to {ctx['supplier']} "
        f"covering Stationery ({_fmt_r(a_stat)}), Material costs ({_fmt_r(a_mat)}), and Equipment ({_fmt_r(a_equip)}). "
        f"How much is entered into the CPJ Bank column AND how much goes into Sundry Amount?"
    )
    ans = f"Bank: {_fmt_r(tot)}, Sundry Amount: {_fmt_r(a_equip)}"
    worked = (
        f"1. Total single cheque in `Bank` = {_fmt_r(a_stat)} + {_fmt_r(a_mat)} + {_fmt_r(a_equip)} = **{_fmt_r(tot)}**.\n"
        f"2. `Stationery` ({_fmt_r(a_stat)}) and `Material costs` ({_fmt_r(a_mat)}) have dedicated analysis columns, so ONLY `Equipment` (**{_fmt_r(a_equip)}**) goes to `Sundry Amount`."
    )
    return _build_short(
        rng,
        qid_prefix="cpj25",
        subskill="25_cpj_multi_row_split_cheque_bank_sum_drill",
        title="Split Cheque Bank Total & Sundry Allocation",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=worked,
        hints={
            "tier_1": "Bank always records the full combined cheque total; Sundry takes only items without dedicated columns.",
            "tier_2": f"Sum all three amounts for Bank; check whether Stationery and Material costs are analysis columns.",
            "tier_3": ans,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Bank amount = {_fmt_r(tot)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Sundry Amount (Equipment) = {_fmt_r(a_equip)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["split_allocation_sum_mismatch"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_cpj_purpose_cash_out_diary": build_01_cpj_purpose_cash_out_diary,
    "02_cpj_heading_three_required_elements": build_02_cpj_heading_three_required_elements,
    "03_cpj_cash_only_exclusion_of_credit_purchases": build_03_cpj_cash_only_exclusion_of_credit_purchases,
    "04_cpj_source_doc_cheque_counterfoil_and_eft": build_04_cpj_source_doc_cheque_counterfoil_and_eft,
    "05_cpj_source_doc_original_receipt_and_invoice": build_05_cpj_source_doc_original_receipt_and_invoice,
    "06_cpj_source_doc_bank_statement_charges_and_debit_orders": build_06_cpj_source_doc_bank_statement_charges_and_debit_orders,
    "07_cpj_source_doc_matching_table": build_07_cpj_source_doc_matching_table,
    "08_cpj_payee_rule_cash_for_wages_and_float": build_08_cpj_payee_rule_cash_for_wages_and_float,
    "09_cpj_bank_column_total_payment_credit_rule": build_09_cpj_bank_column_total_payment_credit_rule,
    "10_cpj_column_sequence_identification": build_10_cpj_column_sequence_identification,
    "11_cpj_no_analysis_of_receipts_column_reason": build_11_cpj_no_analysis_of_receipts_column_reason,
    "12_cpj_dedicated_analysis_columns_selection": build_12_cpj_dedicated_analysis_columns_selection,
    "13_cpj_single_wages_cash_cheque_row": build_13_cpj_single_wages_cash_cheque_row,
    "14_cpj_single_stationery_supplier_payment_row": build_14_cpj_single_stationery_supplier_payment_row,
    "15_cpj_single_material_costs_or_consumables_row": build_15_cpj_single_material_costs_or_consumables_row,
    "16_cpj_sundry_equipment_asset_purchase": build_16_cpj_sundry_equipment_asset_purchase,
    "17_cpj_sundry_vehicle_or_premises_repair_expense": build_17_cpj_sundry_vehicle_or_premises_repair_expense,
    "18_cpj_sundry_water_and_electricity_municipal_payment": build_18_cpj_sundry_water_and_electricity_municipal_payment,
    "19_cpj_sundry_rent_expense_paid_to_landlord": build_19_cpj_sundry_rent_expense_paid_to_landlord,
    "20_cpj_sundry_bank_charges_bank_statement_entry": build_20_cpj_sundry_bank_charges_bank_statement_entry,
    "21_cpj_sundry_loan_repayment_and_interest": build_21_cpj_sundry_loan_repayment_and_interest,
    "22_cpj_split_payment_two_analysis_columns": build_22_cpj_split_payment_two_analysis_columns,
    "23_cpj_split_payment_analysis_and_sundry_account": build_23_cpj_split_payment_analysis_and_sundry_account,
    "24_cpj_owner_drawings_vs_staff_wages": build_24_cpj_owner_drawings_vs_staff_wages,
    "25_cpj_multi_row_split_cheque_bank_sum_drill": build_25_cpj_multi_row_split_cheque_bank_sum_drill,
}
