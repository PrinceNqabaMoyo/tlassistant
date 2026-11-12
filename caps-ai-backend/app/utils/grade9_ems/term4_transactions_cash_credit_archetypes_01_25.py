"""Grade 9 EMS — Transactions (Cash and Credit): Archetypes 01-25.
100% Aligned with South African National Curriculum Standards (Term 4: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Transactions (Cash and Credit).md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Formatting & Contract Helpers
# ---------------------------------------------------------------------------

def _fmt_zar(amount: float) -> str:
    """Format a Rand amount cleanly with space thousands and comma cents if non-integer."""
    rounded = round(float(amount), 2)
    neg = rounded < 0
    val = abs(rounded)
    whole = int(round(val * 100)) // 100
    cents = int(round(val * 100)) % 100
    whole_str = f"{whole:,}".replace(",", " ")
    if cents == 0:
        res = f"R {whole_str}"
    else:
        res = f"R {whole_str},{cents:02d}"
    return f"-{res}" if neg else res


def _fmt_cell_amt(amount: float) -> str:
    """Format cell currency value without 'R ' prefix, space thousands and 2 decimals."""
    rounded = round(float(amount), 2)
    cents_total = int(round(abs(rounded) * 100))
    whole = cents_total // 100
    cents = cents_total % 100
    whole_str = f"{whole:,}".replace(",", " ")
    prefix = "-" if rounded < 0 else ""
    return f"{prefix}{whole_str}.{cents:02d}"


def _base_contract(
    *,
    subskill: str,
    qtype: str,
    prompt: str,
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    sample_answer: str,
    marking_schema: Dict[str, Any],
    duration_mins: int = 5,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "topic_id": "grade9_ems",
        "subtopic_id": "term4_transactions_cash_credit",
        "subskill": subskill,
        "mode": f"elementary_{subskill}",
        "term": 4,
        "caps_weight_percent": 40.0,
        "suggested_duration_mins": duration_mins,
        "type": qtype,
        "question_type": qtype,
        "question": prompt,
        "question_text": prompt,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "worked_solution": worked_solution,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
    }
    if extra:
        q.update(extra)
    return q


def _mcq(
    rng: random.Random,
    *,
    subskill: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    duration_mins: int = 3,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + list(distractors)
    rng.shuffle(options)
    extra: Dict[str, Any] = {
        "options": options,
        "correct_answer": correct,
        "answer": correct,
    }
    if diagram_spec:
        extra["diagram_spec"] = diagram_spec
    return _base_contract(
        subskill=subskill,
        qtype="mcq",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=worked_solution,
        sample_answer=f"{correct}\n\n{worked_solution}",
        marking_schema={"total_marks": 2, "rules": [{"step": "Correct option selected", "marks": 2}]},
        duration_mins=duration_mins,
        extra=extra,
    )


def _typed(
    *,
    subskill: str,
    prompt: str,
    correct_answer: str,
    accepted_answers: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    marks: int = 4,
    duration_mins: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    extra: Dict[str, Any] = {
        "correct_answer": correct_answer,
        "answer": correct_answer,
        "accepted_answers": accepted_answers,
    }
    if diagram_spec:
        extra["diagram_spec"] = diagram_spec
    return _base_contract(
        subskill=subskill,
        qtype="typed",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=worked_solution,
        sample_answer=f"Answer: {correct_answer}\n\n{worked_solution}",
        marking_schema={"total_marks": marks, "rules": [{"step": "Accurate calculation / response", "marks": marks}]},
        duration_mins=duration_mins,
        extra=extra,
    )


def _table_q(
    *,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    raw_rows: List[List[Dict[str, Any]]],
    cell_hints: Dict[str, str],
    derivations: List[str],
    hints: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    journal_type: str = "subsidiary_journal",
    transactions: Optional[List[Dict[str, Any]]] = None,
    duration_mins: int = 7,
) -> Dict[str, Any]:
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    has_must_be_empty = False

    for r_idx, row in enumerate(raw_rows):
        out_row: List[Dict[str, Any]] = []
        for c_idx, cell in enumerate(row):
            cell_id = f"r{r_idx}_c{c_idx}"
            status = cell.get("status", "given")
            val = str(cell.get("value", ""))
            editable = status in ("required", "must_be_empty")
            if status == "must_be_empty":
                has_must_be_empty = True
            if editable:
                correct_map[cell_id] = "" if status == "must_be_empty" else val
            out_row.append({
                "id": cell_id,
                "coordinate": cell_id,
                "value": val,
                "status": status,
                "editable": editable,
            })
        rows.append(out_row)

    md_header = "| " + " | ".join(headers) + " |"
    md_sep = "| " + " | ".join("---" for _ in headers) + " |"
    md_body = ["| " + " | ".join(str(c.get("value", "")) for c in row) + " |" for row in raw_rows]
    md_table = "\n".join([md_header, md_sep] + md_body)
    deriv_text = "\n".join(f"- {d}" for d in derivations)
    full_solution = f"### {title}\n\n{md_table}\n\n**Step-by-step workings:**\n{deriv_text}"

    req_count = sum(1 for r in raw_rows for c in r if c.get("status") == "required")
    total_marks = max(2, req_count)
    deductions = [{"rule": "must_be_empty_filled", "penalty": -1}] if has_must_be_empty else []

    return _base_contract(
        subskill=subskill,
        qtype="accounting_table",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=full_solution,
        sample_answer=full_solution,
        marking_schema={
            "total_marks": total_marks,
            "deductions": deductions,
            "rules": [{"step": f"Correctly complete {req_count} required ledger/journal cells", "marks": total_marks}],
        },
        duration_mins=duration_mins,
        extra={
            "title": title,
            "headers": headers,
            "columns": headers,
            "rows": rows,
            "journal": {
                "journal_type": journal_type,
                "headers": headers,
                "rows": rows,
            },
            "transactions": transactions or [],
            "correct_map": correct_map,
            "cell_hints": cell_hints,
            "deductions": deductions,
            "answer": correct_map,
            "correct_answer": correct_map,
        },
    )


def _svg_bar_chart(title: str, subtitle: str, bars: List[Tuple[str, float, str]]) -> Dict[str, Any]:
    max_val = max((v for _, v, _ in bars), default=1.0) or 1.0
    width, height = 620, 290
    base_y, chart_h = 225, 145
    bar_w = 78
    gap = max(24, (500 - len(bars) * bar_w) // max(1, len(bars) + 1))
    x0 = 75
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">',
        f'<text x="310" y="26" text-anchor="middle" font-size="15" font-weight="bold" fill="#0f172a">{title}</text>',
        f'<text x="310" y="45" text-anchor="middle" font-size="11.5" fill="#475569">{subtitle}</text>',
        f'<line x1="65" y1="65" x2="65" y2="{base_y}" stroke="#334155" stroke-width="1.5"/>',
        f'<line x1="65" y1="{base_y}" x2="585" y2="{base_y}" stroke="#334155" stroke-width="1.5"/>',
    ]
    for frac in (0.25, 0.5, 0.75, 1.0):
        gy = round(base_y - chart_h * frac, 1)
        gval = int(round(max_val * frac))
        parts.append(f'<line x1="65" y1="{gy}" x2="585" y2="{gy}" stroke="#e2e8f0" stroke-dasharray="4,3"/>')
        parts.append(f'<text x="59" y="{gy + 4}" text-anchor="end" font-size="10" fill="#64748b">R {gval:,}</text>'.replace(",", " "))

    cx = x0
    for label, val, color in bars:
        bh = round((val / max_val) * chart_h, 1)
        by = round(base_y - bh, 1)
        parts.append(f'<rect x="{cx}" y="{by}" width="{bar_w}" height="{bh}" rx="4" fill="{color}"/>')
        parts.append(f'<text x="{cx + bar_w / 2}" y="{by - 6}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{_fmt_zar(val)}</text>')
        parts.append(f'<text x="{cx + bar_w / 2}" y="{base_y + 18}" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{label}</text>')
        cx += bar_w + gap
    parts.append("</svg>")
    return {"kind": "inline_svg", "title": title, "svg": "".join(parts), "diagram_role": "context"}


def _svg_cycle_flow(title: str, boxes: List[Tuple[str, str, str]]) -> Dict[str, Any]:
    width, height = 680, 175
    box_w, box_h = 138, 78
    gap = 24
    start_x = 24
    y = 58
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">',
        f'<text x="340" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="#0f172a">{title}</text>',
    ]
    for i, (head, sub, bg) in enumerate(boxes):
        bx = start_x + i * (box_w + gap)
        parts.append(f'<rect x="{bx}" y="{y}" width="{box_w}" height="{box_h}" rx="8" fill="{bg}" stroke="#334155" stroke-width="1.5"/>')
        parts.append(f'<text x="{bx + box_w / 2}" y="{y + 28}" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">{head}</text>')
        parts.append(f'<text x="{bx + box_w / 2}" y="{y + 52}" text-anchor="middle" font-size="10.5" fill="#334155">{sub}</text>')
        if i < len(boxes) - 1:
            ax1 = bx + box_w + 3
            ax2 = bx + box_w + gap - 4
            ay = y + box_h / 2
            parts.append(f'<line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" stroke="#1e293b" stroke-width="2"/>')
            parts.append(f'<polygon points="{ax2},{ay-5} {ax2+6},{ay} {ax2},{ay+5}" fill="#1e293b"/>')
    parts.append("</svg>")
    return {"kind": "inline_svg", "title": title, "svg": "".join(parts), "diagram_role": "context"}


_BIZ_NAMES = ["Slamet Stores", "Nani Traders", "Valley Wholesalers", "Viwe Enterprises", "Baxter Outfitters", "Mahlangu Hardware"]
_DEBTOR_NAMES = ["T Baxter", "J Domingo", "L Zoar", "A Khonjwayo", "A Kelby", "S Davids", "N Petersen"]
_CREDITOR_NAMES = ["Mountifield Ltd", "Cekiso Suppliers", "Boyd Traders", "W Hugo", "H Bosman", "Lebo Suppliers", "E Carlse"]


# ---------------------------------------------------------------------------
# Archetypes 01 - 12
# ---------------------------------------------------------------------------

def _b01_source_documents_to_journals_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    r_num = rng.randint(40, 99)
    chq_num = rng.randint(110, 290)
    dup_inv = rng.randint(301, 499)
    orig_inv = rng.randint(500, 699)
    dn_num = rng.randint(20, 75)

    headers = ["Source Document", "Journal", "Primary Ledger Effect"]
    raw_rows = [
        [
            {"value": f"Duplicate receipt no. {r_num} (issued to debtor)", "status": "given"},
            {"value": "CRJ", "status": "required"},
            {"value": "Dr Bank / Cr Debtors control", "status": "required"},
        ],
        [
            {"value": f"Cheque counterfoil / EFT proof no. {chq_num}", "status": "given"},
            {"value": "CPJ", "status": "required"},
            {"value": "Cr Bank", "status": "given"},
        ],
        [
            {"value": f"Duplicate invoice no. {dup_inv} (issued to credit customer)", "status": "given"},
            {"value": "DJ", "status": "required"},
            {"value": "Dr Debtors control / Cr Sales", "status": "required"},
        ],
        [
            {"value": f"Original invoice no. {orig_inv} (received from supplier)", "status": "given"},
            {"value": "CJ", "status": "required"},
            {"value": "Cr Creditors control", "status": "required"},
        ],
        [
            {"value": f"Debit note no. {dn_num} (goods returned to supplier)", "status": "given"},
            {"value": "CAJ", "status": "required"},
            {"value": "Dr Creditors control", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Money received from a customer uses the Cash Receipts Journal (CRJ).",
        "r0_c2": "Bank increases (Dr) and Debtors control decreases (Cr).",
        "r1_c1": "Payments by cheque or EFT are entered in the Cash Payments Journal (CPJ).",
        "r2_c1": "Duplicate invoice issued to a debtor belongs in the Debtors Journal (DJ).",
        "r2_c2": "Debtor owes more (Dr Debtors control) and Sales income increases (Cr Sales).",
        "r3_c1": "Original invoice from a creditor belongs in the Creditors Journal (CJ).",
        "r3_c2": "Liability owed increases: Credit Creditors control.",
        "r4_c1": "Returns to suppliers on credit use the Creditors Allowances Journal (CAJ).",
    }
    derivations = [
        "Duplicate receipt issued & Cash register roll -> CRJ (Dr Bank, Cr Debtors control / Sales).",
        "Cheque counterfoil / EFT / Bank statement D/O -> CPJ (Cr Bank).",
        "Duplicate invoice issued -> DJ (Dr Debtors control, Cr Sales; plus Dr Cost of sales, Cr Trading stock).",
        "Original invoice received -> CJ (Cr Creditors control).",
        "Original debit note issued for supplier returns -> CAJ (Dr Creditors control).",
    ]
    return _table_q(
        subskill="01_source_documents_to_journals_matching_2d_table",
        title=f"{biz} — Source Documents and Subsidiary Journals",
        prompt=f"Complete the classification schedule for {biz} by entering the correct subsidiary journal code (`CRJ`, `CPJ`, `DJ`, `CJ`, `CAJ`) and primary General Ledger effect for each source document.",
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Ask who issued or received the document: duplicate documents issued stay in CRJ or DJ; original invoices received go to CJ.",
            "Cash flowing in = CRJ; cash flowing out = CPJ; returns to a supplier = CAJ.",
            "Check each cell: r0_c1=CRJ, r1_c1=CPJ, r2_c1=DJ, r3_c1=CJ, r4_c1=CAJ.",
        ],
        learning_objective_id="EMS9-T4-TXN-01",
        concept_id="source_document_journal_mapping",
        misconception_tags=["confused_duplicate_vs_original_invoice", "misrouted_credit_return_journal"],
    )


def _b02_keyword_cues_cash_vs_credit_mcq(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    partner = rng.choice(_CREDITOR_NAMES)
    amt = rng.randrange(1200, 5600, 200)
    scenarios = [
        (
            f"Bought packing material on account from {partner} for {_fmt_zar(amt)}; received original invoice.",
            "Creditors Journal (CJ)",
            ["Debtors Journal (DJ)", "Cash Payments Journal (CPJ)", "Cash Receipts Journal (CRJ)"],
            "'On account' combined with buying goods and receiving an original invoice indicates a credit purchase recorded in the CJ.",
        ),
        (
            f"Sold trading stock on credit to {rng.choice(_DEBTOR_NAMES)} for {_fmt_zar(amt)} and issued a duplicate invoice.",
            "Debtors Journal (DJ)",
            ["Creditors Journal (CJ)", "Cash Receipts Journal (CRJ)", "Cash Payments Journal (CPJ)"],
            "Selling trading stock on credit with a duplicate invoice increases Debtors Control and Sales in the DJ.",
        ),
        (
            f"Settled our overdue account with {partner} via EFT for {_fmt_zar(amt)}.",
            "Cash Payments Journal (CPJ)",
            ["Creditors Journal (CJ)", "Cash Receipts Journal (CRJ)", "Debtors Journal (DJ)"],
            "Any cash/EFT/cheque payment leaving Bank—even to settle an old creditor balance—goes into the CPJ.",
        ),
        (
            f"Received {_fmt_zar(amt)} from a credit customer in part settlement of their account; issued a duplicate receipt.",
            "Cash Receipts Journal (CRJ)",
            ["Debtors Journal (DJ)", "Cash Payments Journal (CPJ)", "Creditors Journal (CJ)"],
            "Cash received from a debtor with a duplicate receipt increases Bank and reduces Debtors Control in the CRJ.",
        ),
    ]
    tx, correct, dist, reason = rng.choice(scenarios)
    return _mcq(
        rng,
        subskill="02_keyword_cues_cash_vs_credit_transactions_mcq",
        prompt=f"{biz} recorded the following transaction:\n\n\"{tx}\"\n\nIn which subsidiary journal must this transaction be recorded?",
        correct=correct,
        distractors=dist,
        learning_objective_id="EMS9-T4-TXN-02",
        concept_id="cash_vs_credit_keyword_cues",
        misconception_tags=["cash_settlement_misclassified_as_credit_journal", "buyer_vs_seller_confusion"],
        hints=[
            "Look for whether cash/EFT moved immediately or if payment will happen later ('on account' / 'on credit').",
            "Only credit sales go in DJ and only credit purchases go in CJ; subsequent settlements use CRJ or CPJ.",
            reason,
        ],
        worked_solution=reason,
    )


def _b03_owner_vs_customer_invoice_perspective_mcq(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    supplier = rng.choice(_CREDITOR_NAMES)
    inv_no = rng.randint(210, 490)
    amt = rng.randrange(1500, 6500, 250)
    is_original = rng.choice([True, False])
    if is_original:
        prompt = (
            f"{biz} receives original invoice no. {inv_no} from {supplier} for merchandise valued at {_fmt_zar(amt)}. "
            "Why is this entered in the Creditors Journal (CJ) rather than the Debtors Journal (DJ)?"
        )
        correct = f"Because {biz} is the buyer purchasing on credit and received the supplier's original invoice."
        dist = [
            f"Because {biz} sold stock to {supplier} on credit.",
            f"Because {biz} issued a duplicate cheque to {supplier}.",
            "Because original invoices are always recorded as cash sales in the CRJ.",
        ]
        sol = "A supplier keeps the duplicate and hands the original invoice to the buyer. Receiving an original invoice means the business owes a creditor -> CJ."
    else:
        debtor = rng.choice(_DEBTOR_NAMES)
        prompt = (
            f"{biz} issues duplicate invoice no. {inv_no} to {debtor} for goods worth {_fmt_zar(amt)}. "
            "Why does this belong in the Debtors Journal (DJ)?"
        )
        correct = f"Because {biz} is the seller granting credit and retains the duplicate invoice while the customer takes the original."
        dist = [
            f"Because {biz} owes {debtor} money for credit purchases.",
            "Because all duplicate documents represent cash payments from Bank.",
            "Because the customer paid cash over the counter immediately.",
        ]
        sol = "When a business sells on credit, it gives the original invoice to the customer and files the duplicate invoice -> DJ."
    return _mcq(
        rng,
        subskill="03_owner_vs_customer_invoice_perspective_mcq",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="EMS9-T4-TXN-03",
        concept_id="invoice_issuer_vs_recipient",
        misconception_tags=["original_vs_duplicate_invoice_reversal"],
        hints=[
            "Remember the golden rule: the seller keeps the duplicate invoice and hands the original to the buyer.",
            "Identify whether the business is buying on credit (CJ) or selling on credit (DJ).",
            sol,
        ],
        worked_solution=sol,
    )


def _b04_accounting_cycle_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    crj_tot = rng.randrange(24000, 48000, 1000)
    dj_tot = rng.randrange(9000, 22000, 500)
    svg_spec = _svg_cycle_flow(
        "Integrated Cash & Credit Posting Cycle",
        [
            ("1. Source Docs", "Receipts / Invoices", "#e0f2fe"),
            ("2. Journals", f"CRJ/CPJ | DJ {_fmt_zar(dj_tot)}", "#dcfce7"),
            ("3. Sub-Ledgers", "Debtors & Creditors (Daily)", "#fef3c7"),
            ("4. Control & TB", f"Bank/GL (Month-end CRJ {_fmt_zar(crj_tot)})", "#f3e8ff"),
        ],
    )
    return _mcq(
        rng,
        subskill="04_subsidiary_journals_to_accounting_cycle_flow_diagram",
        prompt="Refer to the flowchart below. At what frequency are individual credit transactions posted from the DJ and CJ to the Debtors and Creditors Ledgers versus column totals to the General Ledger?",
        correct="Individual invoices/receipts/payments post daily to the Debtors/Creditors Ledgers; journal column totals post at month-end to the General Ledger.",
        distractors=[
            "Column totals post daily to the Debtors Ledger while individual invoices wait until year-end for the General Ledger.",
            "Both individual items and column totals are posted only once a year after the Trial Balance is drawn up.",
            "General Ledger control accounts are updated daily directly from source documents without using subsidiary journals.",
        ],
        learning_objective_id="EMS9-T4-TXN-04",
        concept_id="daily_subsidiary_vs_month_end_general_ledger",
        misconception_tags=["wrong_posting_frequency_subsidiary_vs_control"],
        hints=[
            "Follow Step 3 (Sub-Ledgers) vs Step 4 (Control & TB) in the flowchart.",
            "Businesses must know how much each customer owes or each supplier is owed every day, whereas summary control accounts use month-end column totals.",
            "Step 3 updates Debtors & Creditors Ledgers daily; Step 4 posts column totals to the General Ledger at month-end.",
        ],
        worked_solution="Individual customer and supplier transactions are posted daily to keep running balances accurate, while subsidiary journal column totals are posted to the General Ledger at month-end.",
        diagram_spec=svg_spec,
    )


def _b05_markup_selling_price_and_cost_of_sales(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    markup, cp_unit = rng.choice([(25, 40), (25, 80), (50, 60), (50, 120), (60, 50), (100, 75), (80, 50)])
    qty = rng.randint(15, 45)
    cos = cp_unit * qty
    sales = int(round(cos * (100 + markup) / 100))
    ask_cos = rng.choice([True, False])
    if ask_cos:
        prompt = (
            f"{biz} marks up all trading stock at {markup}% on cost price. "
            f"Cash sales on the cash register roll total {_fmt_zar(sales)}. "
            "Calculate the Cost of sales (Rand value) for the CRJ."
        )
        ans = str(cos)
        accepted = [ans, _fmt_cell_amt(cos), _fmt_zar(cos), f"R{cos}", f"R {cos}"]
        sol = f"Cost of sales = Selling price × 100 / (100 + mark-up%) = {_fmt_zar(sales)} × 100 / {100 + markup} = {_fmt_zar(cos)}."
    else:
        prompt = (
            f"{biz} marks up trading stock at {markup}% on cost price. "
            f"If the cost price of goods sold on credit is {_fmt_zar(cos)}, calculate the Selling price (Sales) for the DJ."
        )
        ans = str(sales)
        accepted = [ans, _fmt_cell_amt(sales), _fmt_zar(sales), f"R{sales}", f"R {sales}"]
        sol = f"Selling price = Cost of sales × (100 + mark-up%) / 100 = {_fmt_zar(cos)} × {100 + markup} / 100 = {_fmt_zar(sales)}."
    return _typed(
        subskill="05_markup_selling_price_and_cost_of_sales_calculation",
        prompt=prompt,
        correct_answer=_fmt_zar(int(ans)),
        accepted_answers=accepted,
        learning_objective_id="EMS9-T4-TXN-05",
        concept_id="markup_cost_to_sales_conversion",
        misconception_tags=["subtracted_markup_percent_from_selling_price"],
        hints=[
            f"Remember Cost Price = 100% and Selling Price = {100 + markup}%.",
            f"Divide by {100 + markup} to get 1% when solving Cost of sales from Selling price.",
            sol,
        ],
        worked_solution=sol,
    )


def _b06_calculating_profit_pct_from_opening_balances(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    markup = rng.choice([25, 38, 40, 50, 60])
    open_cos = rng.randrange(20000, 90000, 2000)
    open_sales = int(round(open_cos * (100 + markup) / 100))
    crj_cos = rng.randrange(2500, 8500, 500)
    crj_sales = int(round(crj_cos * (100 + markup) / 100))
    profit = open_sales - open_cos
    sol = (
        f"1. Opening Gross Profit = {_fmt_zar(open_sales)} - {_fmt_zar(open_cos)} = {_fmt_zar(profit)}.\n"
        f"2. Mark-up % = ({_fmt_zar(profit)} / {_fmt_zar(open_cos)}) × 100 = {markup}%.\n"
        f"3. Missing CRJ Sales = ({100 + markup} / 100) × {_fmt_zar(crj_cos)} = {_fmt_zar(crj_sales)}."
    )
    return _typed(
        subskill="06_calculating_profit_percentage_from_opening_balances",
        prompt=(
            f"In the General Ledger of {biz}, the opening balances on 1 June are:\n"
            f"- Sales: {_fmt_zar(open_sales)}\n"
            f"- Cost of sales: {_fmt_zar(open_cos)}\n\n"
            f"Assuming a constant mark-up percentage on cost, if the CRJ Cost of sales total for June is {_fmt_zar(crj_cos)}, calculate the missing CRJ Sales amount."
        ),
        correct_answer=_fmt_zar(crj_sales),
        accepted_answers=[str(crj_sales), _fmt_zar(crj_sales), _fmt_cell_amt(crj_sales), f"R{crj_sales}"],
        learning_objective_id="EMS9-T4-TXN-06",
        concept_id="derive_markup_from_ledger_balances",
        misconception_tags=["divided_profit_by_selling_price_instead_of_cost"],
        hints=[
            "First find Gross Profit = Opening Sales - Opening Cost of sales.",
            "Calculate Mark-up % = (Profit / Opening Cost of sales) × 100.",
            f"Mark-up is {markup}%, so Sales = {100 + markup}% × {_fmt_zar(crj_cos)}.",
        ],
        worked_solution=sol,
        marks=5,
        duration_mins=6,
    )


def _b07_crj_analysis_of_receipts_banking_rule_mcq(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    debtor = rng.choice(_DEBTOR_NAMES)
    r1 = rng.randrange(400, 1400, 100)
    r2 = rng.randrange(1200, 3200, 100)
    tot = r1 + r2
    day = rng.randint(5, 22)
    return _mcq(
        rng,
        subskill="07_crj_analysis_of_receipts_banking_rule_mcq",
        prompt=(
            f"On day {day}, {biz} receives {_fmt_zar(r1)} cash from debtor {debtor} (receipt no. 88) "
            f"and {_fmt_zar(r2)} from cash sales (CRR) before banking all cash at the end of the day. "
            "How must `Analysis of receipts` and `Bank` be completed in the CRJ?"
        ),
        correct=f"Enter {_fmt_zar(r1)} and {_fmt_zar(r2)} on separate lines in `Analysis of receipts`, and enter the single combined deposit {_fmt_zar(tot)} in `Bank` on the second line.",
        distractors=[
            f"Enter {_fmt_zar(r1)} and {_fmt_zar(r2)} individually in `Bank` and leave `Analysis of receipts` blank.",
            f"Add {_fmt_zar(r1)} and {_fmt_zar(r2)} together into one combined row in `Analysis of receipts` and repeat {_fmt_zar(tot)} in `Sales`.",
            f"Record only {_fmt_zar(r2)} in `Analysis of receipts` because receipts from debtors do not enter the cash till.",
        ],
        learning_objective_id="EMS9-T4-TXN-07",
        concept_id="crj_daily_banking_subtotal_rule",
        misconception_tags=["double_counted_bank_deposit", "skipped_analysis_of_receipts"],
        hints=[
            "The Analysis of receipts column acts like the cash till accumulating all cash received during one day.",
            "Only ONE total deposit slip goes into the Bank column at the end of that day.",
            f"Line 1 Analysis = {_fmt_zar(r1)} (Bank blank); Line 2 Analysis = {_fmt_zar(r2)} -> Bank = {_fmt_zar(tot)}.",
        ],
        worked_solution=f"Individual cash receipts on day {day} are listed in `Analysis of receipts` ({_fmt_zar(r1)} + {_fmt_zar(r2)}), and their combined total ({_fmt_zar(tot)}) is banked once on the final line of day {day}.",
    )


def _b08_crj_multi_transaction_entry_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    owner = biz.split()[0]
    debtor = rng.choice(_DEBTOR_NAMES)
    cap_amt = rng.randrange(20000, 45000, 5000)
    deb_amt = rng.randrange(800, 2400, 100)
    cos_amt = rng.randrange(900, 2200, 100)
    sales_amt = int(cos_amt * 1.5)  # exact 50% mark-up
    bank_day2 = deb_amt + sales_amt
    tot_bank = cap_amt + bank_day2

    headers = ["Doc", "Day", "Details", "Analysis", "Bank", "Sales", "Cost of sales", "Debtors control", "Sundry Amount", "Sundry Details"]
    raw_rows = [
        [
            {"value": "01", "status": "given"},
            {"value": "02", "status": "given"},
            {"value": owner, "status": "given"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(cap_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(cap_amt), "status": "required"},
            {"value": "Capital", "status": "required"},
        ],
        [
            {"value": "02", "status": "given"},
            {"value": "10", "status": "given"},
            {"value": debtor, "status": "given"},
            {"value": _fmt_cell_amt(deb_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(deb_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "CRR", "status": "given"},
            {"value": "10", "status": "given"},
            {"value": "Sales", "status": "given"},
            {"value": _fmt_cell_amt(sales_amt), "status": "given"},
            {"value": _fmt_cell_amt(bank_day2), "status": "required"},
            {"value": _fmt_cell_amt(sales_amt), "status": "required"},
            {"value": _fmt_cell_amt(cos_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "Total", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(tot_bank), "status": "required"},
            {"value": _fmt_cell_amt(sales_amt), "status": "required"},
            {"value": _fmt_cell_amt(cos_amt), "status": "given"},
            {"value": _fmt_cell_amt(deb_amt), "status": "required"},
            {"value": _fmt_cell_amt(cap_amt), "status": "given"},
            {"value": "", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c3": "Direct EFT/deposit by owner skips Analysis of receipts (leave blank).",
        "r0_c4": f"Direct capital deposit enters Bank directly: {_fmt_cell_amt(cap_amt)}.",
        "r0_c8": f"Capital has no dedicated analysis column, so enter {_fmt_cell_amt(cap_amt)} in Sundry Amount.",
        "r0_c9": "Specify the General Ledger account: Capital.",
        "r1_c3": f"Debtor cash receipt on Day 10 goes into Analysis first: {_fmt_cell_amt(deb_amt)}.",
        "r1_c4": "Wait until the last cash receipt of Day 10 before banking (leave blank here).",
        "r1_c7": f"Allocate debtor collection to Debtors control: {_fmt_cell_amt(deb_amt)}.",
        "r2_c4": f"Sum all Day 10 receipts ({_fmt_cell_amt(deb_amt)} + {_fmt_cell_amt(sales_amt)}) into Bank: {_fmt_cell_amt(bank_day2)}.",
        "r2_c5": f"Enter Cash sales amount: {_fmt_cell_amt(sales_amt)}.",
        "r2_c6": f"50% mark-up on cost: {_fmt_cell_amt(sales_amt)} × 100 / 150 = {_fmt_cell_amt(cos_amt)}.",
        "r3_c4": f"Sum Bank column = {_fmt_cell_amt(cap_amt)} + {_fmt_cell_amt(bank_day2)} = {_fmt_cell_amt(tot_bank)}.",
        "r3_c5": f"Total Sales = {_fmt_cell_amt(sales_amt)}.",
        "r3_c7": f"Total Debtors control = {_fmt_cell_amt(deb_amt)}.",
    }
    derivations = [
        f"Day 02: Owner {owner} deposits {_fmt_zar(cap_amt)} directly into Bank -> Bank +{_fmt_cell_amt(cap_amt)}, Sundry (Capital) +{_fmt_cell_amt(cap_amt)}.",
        f"Day 10 (Receipt 02): Received {_fmt_zar(deb_amt)} from {debtor} in till (`Analysis`), allocated to `Debtors control`.",
        f"Day 10 (CRR): Cash sales {_fmt_zar(sales_amt)} (Cost = {_fmt_zar(sales_amt)} × 100/150 = {_fmt_zar(cos_amt)}); total banked for Day 10 = {_fmt_zar(deb_amt)} + {_fmt_zar(sales_amt)} = {_fmt_zar(bank_day2)}.",
        f"Cross-cast check: Bank ({_fmt_cell_amt(tot_bank)}) = Sales ({_fmt_cell_amt(sales_amt)}) + Debtors control ({_fmt_cell_amt(deb_amt)}) + Sundry ({_fmt_cell_amt(cap_amt)}).",
    ]
    prompt = (
        f"Complete the Cash Receipts Journal (CRJ) of {biz} for the following transactions (mark-up is 50% on cost):\n"
        f"- Day 02: Owner {owner} deposits {_fmt_zar(cap_amt)} directly into the business bank account as capital (Receipt 01).\n"
        f"- Day 10: Received {_fmt_zar(deb_amt)} cash from debtor {debtor} on account (Receipt 02).\n"
        f"- Day 10: Cash sales per CRR total {_fmt_zar(sales_amt)}.\n"
        "Enter amounts formatted like `12 500.00` and leave non-applicable cells empty."
    )
    return _table_q(
        subskill="08_crj_multi_transaction_entry_2d_table",
        title=f"Cash Receipts Journal (CRJ) — {biz}",
        prompt=prompt,
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Direct bank deposits skip `Analysis`; same-day cash receipts sit in `Analysis` and bank together on the final line of the day.",
            "Remember Cost of sales is NOT added when cross-casting Bank = Sales + Debtors control + Sundry.",
            f"Day 10 Bank = {_fmt_cell_amt(bank_day2)}; Total Bank = {_fmt_cell_amt(tot_bank)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-08",
        concept_id="crj_2d_journal_entry_and_crosscast",
        misconception_tags=["included_cost_of_sales_in_bank_crosscast", "banked_each_cash_receipt_separately"],
        journal_type="crj",
        duration_mins=9,
    )


def _b09_crj_missing_debtors_control_total(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    sales_tot = rng.randrange(12000, 36000, 1000)
    deb_tot = rng.randrange(4500, 14500, 500)
    rent_tot = rng.randrange(3000, 9000, 500)
    bank_tot = sales_tot + deb_tot + rent_tot
    cos_tot = int(round(sales_tot * 0.6))
    sol = (
        f"In the CRJ, Bank total = Sales + Debtors control + Sundry accounts (Cost of sales is excluded).\n"
        f"Debtors control = {_fmt_zar(bank_tot)} - {_fmt_zar(sales_tot)} - {_fmt_zar(rent_tot)} = {_fmt_zar(deb_tot)}."
    )
    return _typed(
        subskill="09_crj_missing_debtors_control_total_deduction",
        prompt=(
            f"At month-end, the CRJ column totals of {biz} show:\n"
            f"- Bank: {_fmt_zar(bank_tot)}\n"
            f"- Sales: {_fmt_zar(sales_tot)}\n"
            f"- Cost of sales: {_fmt_zar(cos_tot)}\n"
            f"- Sundry accounts (Rent income): {_fmt_zar(rent_tot)}\n\n"
            "Calculate the missing `Debtors control` column total."
        ),
        correct_answer=_fmt_zar(deb_tot),
        accepted_answers=[str(deb_tot), _fmt_zar(deb_tot), _fmt_cell_amt(deb_tot), f"R{deb_tot}"],
        learning_objective_id="EMS9-T4-TXN-09",
        concept_id="crj_horizontal_cross_cast_deduction",
        misconception_tags=["subtracted_cost_of_sales_when_balancing_crj"],
        hints=[
            "Which CRJ money columns actually represent cash flowing into Bank?",
            "Cost of sales is an inventory memo column in the CRJ — do NOT subtract it from Bank.",
            sol,
        ],
        worked_solution=sol,
    )


def _b10_crj_current_income_vs_sales_mcq(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(["Cyclone Cycles", "Shero Repair Centre", "Baxter Shoe Repairs", "Cape Auto Care"])
    fee = rng.randrange(350, 950, 50)
    return _mcq(
        rng,
        subskill="10_crj_current_income_vs_sales_distinction_mcq",
        prompt=f"{biz} receives {_fmt_zar(fee)} cash for repairs/services rendered to a walk-in client. Which CRJ column(s) receive the {_fmt_zar(fee)} entry, and why is Cost of sales left blank?",
        correct="Enter it in `Current income` (or Sundry) and leave `Cost of sales` blank, because services rendered do not sell physical trading stock.",
        distractors=[
            "Enter it in `Sales` and estimate a 50% `Cost of sales` figure.",
            "Enter it in `Debtors control` because the client received service on credit.",
            "Enter it in `Trading stock` Cr in the CPJ because tools were used.",
        ],
        learning_objective_id="EMS9-T4-TXN-10",
        concept_id="current_income_service_vs_trading_sales",
        misconception_tags=["assigned_cost_of_sales_to_service_fee"],
        hints=[
            "Did any physical merchandise leave the storeroom when a repair/service was performed?",
            "Service fees go to Current income and only trading goods sold trigger Cost of sales.",
            "Services earn Current income with zero Cost of sales entry.",
        ],
        worked_solution=f"Cash received for services rendered ({_fmt_zar(fee)}) is credited to `Current income` and has no physical inventory cost, so `Cost of sales` stays empty.",
    )


def _b11_cpj_cash_payments_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    cred = rng.choice(_CREDITOR_NAMES)
    p_cred = rng.randrange(1500, 4500, 100)
    p_stock = rng.randrange(2000, 5200, 200)
    p_wages = rng.randrange(900, 2100, 100)
    p_water = rng.randrange(450, 950, 50)
    tot_bank = p_cred + p_stock + p_wages + p_water

    headers = ["Doc", "Day", "Payee", "Bank", "Trading stock", "Creditors control", "Wages", "Sundry Amount", "Sundry Details"]
    raw_rows = [
        [
            {"value": "107", "status": "given"},
            {"value": "04", "status": "given"},
            {"value": cred, "status": "given"},
            {"value": _fmt_cell_amt(p_cred), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(p_cred), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "108", "status": "given"},
            {"value": "12", "status": "given"},
            {"value": "Cash", "status": "given"},
            {"value": _fmt_cell_amt(p_wages), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(p_wages), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "109", "status": "given"},
            {"value": "18", "status": "given"},
            {"value": "Metro Wholesalers", "status": "given"},
            {"value": _fmt_cell_amt(p_stock), "status": "given"},
            {"value": _fmt_cell_amt(p_stock), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "110", "status": "given"},
            {"value": "25", "status": "given"},
            {"value": "Municipality", "status": "given"},
            {"value": _fmt_cell_amt(p_water), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(p_water), "status": "required"},
            {"value": "Water and electricity", "status": "required"},
        ],
        [
            {"value": "Total", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_bank), "status": "required"},
            {"value": _fmt_cell_amt(p_stock), "status": "given"},
            {"value": _fmt_cell_amt(p_cred), "status": "given"},
            {"value": _fmt_cell_amt(p_wages), "status": "given"},
            {"value": _fmt_cell_amt(p_water), "status": "given"},
            {"value": "", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Payment to creditor reduces Bank by {_fmt_cell_amt(p_cred)}.",
        "r0_c5": f"Settles supplier account: Creditors control = {_fmt_cell_amt(p_cred)}.",
        "r1_c3": f"Cash cheque for wages: Bank = {_fmt_cell_amt(p_wages)}.",
        "r1_c6": f"Wages has its own analysis column: {_fmt_cell_amt(p_wages)}.",
        "r2_c4": f"Cash stock purchase enters Trading stock column: {_fmt_cell_amt(p_stock)}.",
        "r3_c3": f"Municipal payment reduces Bank by {_fmt_cell_amt(p_water)}.",
        "r3_c7": "Water & electricity has no dedicated column, so enter in Sundry Amount.",
        "r3_c8": "Enter account name: Water and electricity.",
        "r4_c3": f"Sum all Bank payments = {_fmt_cell_amt(tot_bank)}.",
    }
    derivations = [
        f"Day 04: Paid creditor {cred} {_fmt_zar(p_cred)} -> Bank & Creditors control.",
        f"Day 12: Cashed cheque for weekly wages {_fmt_zar(p_wages)} -> Bank & Wages.",
        f"Day 18: Bought trading stock cash {_fmt_zar(p_stock)} -> Bank & Trading stock.",
        f"Day 25: Paid Municipality {_fmt_zar(p_water)} -> Bank & Sundry (Water and electricity).",
        f"Total Bank = {_fmt_zar(p_cred)} + {_fmt_zar(p_wages)} + {_fmt_zar(p_stock)} + {_fmt_zar(p_water)} = {_fmt_zar(tot_bank)}.",
    ]
    return _table_q(
        subskill="11_cpj_cash_payments_and_bank_columns_2d_table",
        title=f"Cash Payments Journal (CPJ) — {biz}",
        prompt=(
            f"Record the following payments of {biz} in the CPJ:\n"
            f"- Doc 107 (Day 04): Paid creditor {cred} {_fmt_zar(p_cred)} on account.\n"
            f"- Doc 108 (Day 12): Cash cheque for wages, {_fmt_zar(p_wages)}.\n"
            f"- Doc 109 (Day 18): Bought trading stock cash from Metro Wholesalers, {_fmt_zar(p_stock)}.\n"
            f"- Doc 110 (Day 25): Paid Municipality {_fmt_zar(p_water)} for water and electricity."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Every cheque/EFT payment enters Bank first, then splits into the matching analysis column or Sundry accounts.",
            "Remember Water and electricity does not have its own column in this CPJ, so use Sundry accounts.",
            f"Total Bank must equal {_fmt_cell_amt(tot_bank)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-11",
        concept_id="cpj_multi_column_entry",
        misconception_tags=["put_cash_stock_in_creditors_control", "forgot_sundry_account_label"],
        journal_type="cpj",
        duration_mins=8,
    )


def _b12_cpj_split_payment_vehicle_and_fuel_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    veh = rng.randrange(95000, 185000, 5000)
    fuel = rng.randrange(600, 1500, 100)
    total = veh + fuel
    headers = ["Doc", "Day", "Payee", "Bank", "Sundry Amount", "Fol", "Sundry Details"]
    raw_rows = [
        [
            {"value": "41", "status": "given"},
            {"value": "09", "status": "given"},
            {"value": "Mbeki Motors", "status": "given"},
            {"value": _fmt_cell_amt(total), "status": "required"},
            {"value": _fmt_cell_amt(veh), "status": "required"},
            {"value": "B4", "status": "given"},
            {"value": "Vehicles", "status": "required"},
        ],
        [
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(fuel), "status": "required"},
            {"value": "N4", "status": "given"},
            {"value": "Fuel", "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Single cheque/EFT total paid out of Bank = {_fmt_cell_amt(veh)} + {_fmt_cell_amt(fuel)} = {_fmt_cell_amt(total)}.",
        "r0_c4": f"Vehicle capital asset portion = {_fmt_cell_amt(veh)}.",
        "r0_c6": "Asset account name: Vehicles.",
        "r1_c3": "Do NOT enter Bank twice for the same cheque (leave Bank empty on line 2).",
        "r1_c4": f"Operating expense portion = {_fmt_cell_amt(fuel)}.",
        "r1_c6": "Expense account name: Fuel.",
    }
    derivations = [
        f"Total paid on Doc 41 = {_fmt_zar(veh)} (Vehicles) + {_fmt_zar(fuel)} (Fuel) = {_fmt_zar(total)}.",
        "Line 1 carries the full Bank amount and the first Sundry item (`Vehicles`, B4).",
        "Line 2 records ONLY the second Sundry item (`Fuel`, N4), leaving Bank blank so it is not double-counted.",
    ]
    return _table_q(
        subskill="12_cpj_split_payment_vehicle_and_fuel_2d_table",
        title=f"CPJ Split Cheque Entry — {biz}",
        prompt=(
            f"{biz} bought a delivery bakkie from Mbeki Motors for {_fmt_zar(veh)} and a full tank of petrol/fuel costing {_fmt_zar(fuel)}, "
            f"paying the total by a single EFT/cheque (Doc 41 on Day 09). Complete both lines of the CPJ."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "One payment document means ONLY ONE entry in the Bank column on the first line.",
            "Put Vehicles and Fuel on two separate lines inside Sundry accounts.",
            f"Bank = {_fmt_cell_amt(total)}; Sundry lines = {_fmt_cell_amt(veh)} (Vehicles) and {_fmt_cell_amt(fuel)} (Fuel).",
        ],
        learning_objective_id="EMS9-T4-TXN-12",
        concept_id="cpj_split_sundry_lines",
        misconception_tags=["repeated_bank_amount_on_second_sundry_line", "combined_asset_and_expense_into_vehicles"],
        journal_type="cpj",
    )


# ---------------------------------------------------------------------------
# Archetypes 13 - 25
# ---------------------------------------------------------------------------

def _b13_cpj_drawings_and_cash_float_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    owner = biz.split()[0]
    float_amt = rng.randrange(200, 600, 100)
    draw_amt = rng.randrange(350, 950, 50)
    tot = float_amt + draw_amt
    headers = ["Doc", "Day", "Payee", "Bank", "Sundry Amount", "Fol", "Sundry Details"]
    raw_rows = [
        [
            {"value": "185", "status": "given"},
            {"value": "07", "status": "given"},
            {"value": "Cash", "status": "given"},
            {"value": _fmt_cell_amt(tot), "status": "required"},
            {"value": _fmt_cell_amt(float_amt), "status": "required"},
            {"value": "B10", "status": "given"},
            {"value": "Cash float", "status": "required"},
        ],
        [
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(draw_amt), "status": "required"},
            {"value": "B2", "status": "given"},
            {"value": "Drawings", "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Total cash withdrawn = {_fmt_cell_amt(float_amt)} + {_fmt_cell_amt(draw_amt)} = {_fmt_cell_amt(tot)}.",
        "r0_c4": f"Cash placed in the cash register till: {_fmt_cell_amt(float_amt)}.",
        "r0_c6": "Register change fund is called `Cash float` (B10).",
        "r1_c4": f"Owner's private cash taken: {_fmt_cell_amt(draw_amt)}.",
        "r1_c6": "Owner taking cash for personal use goes to `Drawings` (B2), never Salaries.",
    }
    derivations = [
        f"Total cash cheque 185 = {_fmt_zar(float_amt)} + {_fmt_zar(draw_amt)} = {_fmt_zar(tot)}.",
        "Putting cash in the till increases asset `Cash float` (B10).",
        "Cash taken by owner for personal expenses increases `Drawings` (B2) and reduces Equity.",
    ]
    return _table_q(
        subskill="13_cpj_personal_drawings_and_cash_float_2d_table",
        title=f"CPJ Cash Cheque Split (Cash Float & Drawings) — {biz}",
        prompt=(
            f"On Day 07, {biz} cashed cheque no. 185 for {_fmt_zar(tot)}: {_fmt_zar(float_amt)} was placed in the cash register till as change, "
            f"and owner {owner} took the remaining {_fmt_zar(draw_amt)} for personal weekend use. Complete the CPJ entry."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Money placed in the register for change is an Asset called Cash float.",
            "Personal use by the owner is always recorded under Drawings, not Wages.",
            f"Bank = {_fmt_cell_amt(tot)}; Cash float = {_fmt_cell_amt(float_amt)}; Drawings = {_fmt_cell_amt(draw_amt)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-13",
        concept_id="cash_float_and_owner_drawings_cpj",
        misconception_tags=["recorded_drawings_as_wages", "expensed_cash_float"],
        journal_type="cpj",
    )


def _b14_cpj_direct_debit_order_entry_typed(rng: random.Random) -> Dict[str, Any]:
    insurer = rng.choice(["Tamson Insurers", "Santam Commercial", "Mzansi Cover", "OutSure Business"])
    amt = rng.randrange(480, 1280, 40)
    sol = f"A monthly debit order (`D/O`) appears on the bank statement, so it is recorded in the CPJ with `D/O` in Doc no., {_fmt_zar(amt)} in Bank, and {_fmt_zar(amt)} in Sundry accounts (`Insurance`)."
    return _typed(
        subskill="14_cpj_direct_debit_order_entry_typed",
        prompt=(
            f"At month-end, the bank statement shows a direct debit order (`D/O`) paid to {insurer} for {_fmt_zar(amt)} monthly business insurance. "
            "Which subsidiary journal records this, and which General Ledger account is debited?"
        ),
        correct_answer="CPJ; Insurance",
        accepted_answers=["CPJ; Insurance", "CPJ - Insurance", "CPJ, Insurance", "Cash Payments Journal; Insurance"],
        learning_objective_id="EMS9-T4-TXN-14",
        concept_id="debit_order_cpj_recording",
        misconception_tags=["omitted_bank_statement_debit_order"],
        hints=[
            "Money left the Bank account automatically via debit order -> cash payment.",
            "Answer in the format `Journal; Account debited` (e.g., `CPJ; Insurance`).",
            sol,
        ],
        worked_solution=sol,
    )


def _b15_dj_credit_sales_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    d1, d2, d3 = rng.sample(_DEBTOR_NAMES, 3)
    markup = rng.choice([25, 50, 60])
    cos1 = rng.randrange(400, 1200, 100)
    cos2 = rng.randrange(600, 1800, 100)
    cos3 = rng.randrange(500, 1500, 100)
    s1 = int(round(cos1 * (100 + markup) / 100))
    s2 = int(round(cos2 * (100 + markup) / 100))
    s3 = int(round(cos3 * (100 + markup) / 100))
    tot_s = s1 + s2 + s3
    tot_c = cos1 + cos2 + cos3

    headers = ["Doc no.", "Day", "Debtor", "Fol.", "Sales", "Cost of sales"]
    raw_rows = [
        [
            {"value": "321", "status": "given"},
            {"value": "07", "status": "given"},
            {"value": d1, "status": "given"},
            {"value": "D1", "status": "given"},
            {"value": _fmt_cell_amt(s1), "status": "required"},
            {"value": _fmt_cell_amt(cos1), "status": "required"},
        ],
        [
            {"value": "322", "status": "given"},
            {"value": "14", "status": "given"},
            {"value": d2, "status": "given"},
            {"value": "D2", "status": "given"},
            {"value": _fmt_cell_amt(s2), "status": "given"},
            {"value": _fmt_cell_amt(cos2), "status": "required"},
        ],
        [
            {"value": "323", "status": "given"},
            {"value": "22", "status": "given"},
            {"value": d3, "status": "given"},
            {"value": "D3", "status": "given"},
            {"value": _fmt_cell_amt(s3), "status": "required"},
            {"value": _fmt_cell_amt(cos3), "status": "given"},
        ],
        [
            {"value": "Total", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "B7/N1 | N2/B6", "status": "given"},
            {"value": _fmt_cell_amt(tot_s), "status": "required"},
            {"value": _fmt_cell_amt(tot_c), "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c4": f"Selling price = Cost {_fmt_cell_amt(cos1)} × {100 + markup}/100 = {_fmt_cell_amt(s1)}.",
        "r0_c5": f"Cost price given: {_fmt_cell_amt(cos1)}.",
        "r1_c5": f"Cost = Selling {_fmt_cell_amt(s2)} × 100/{100 + markup} = {_fmt_cell_amt(cos2)}.",
        "r2_c4": f"Selling price = Cost {_fmt_cell_amt(cos3)} × {100 + markup}/100 = {_fmt_cell_amt(s3)}.",
        "r3_c4": f"Total credit sales = {_fmt_cell_amt(tot_s)}.",
        "r3_c5": f"Total cost of credit sales = {_fmt_cell_amt(tot_c)}.",
    }
    derivations = [
        f"Inv 321 ({d1}): Cost = {_fmt_zar(cos1)} -> Sales ({markup}% mark-up) = {_fmt_zar(s1)}.",
        f"Inv 322 ({d2}): Sales = {_fmt_zar(s2)} -> Cost = {_fmt_zar(s2)} × 100/{100 + markup} = {_fmt_zar(cos2)}.",
        f"Inv 323 ({d3}): Cost = {_fmt_zar(cos3)} -> Sales = {_fmt_zar(s3)}.",
        f"Totals: Sales = {_fmt_zar(tot_s)} (Dr B7 Debtors control / Cr N1 Sales); Cost of sales = {_fmt_zar(tot_c)} (Dr N2 Cost of sales / Cr B6 Trading stock).",
    ]
    return _table_q(
        subskill="15_dj_credit_sales_and_cost_of_sales_2d_table",
        title=f"Debtors Journal (DJ) — {biz} (Mark-up {markup}%)",
        prompt=(
            f"Complete the Debtors Journal of {biz} (consistent mark-up of {markup}% on cost):\n"
            f"- Inv 321 (Day 07) to {d1}: Cost price {_fmt_zar(cos1)}.\n"
            f"- Inv 322 (Day 14) to {d2}: Selling price {_fmt_zar(s2)}.\n"
            f"- Inv 323 (Day 22) to {d3}: Cost price {_fmt_zar(cos3)}."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            f"To convert Cost to Sales, multiply by {(100 + markup) / 100:.2f}.",
            f"To convert Sales back to Cost, multiply by 100 / {100 + markup}.",
            f"Totals: Sales = {_fmt_cell_amt(tot_s)}, Cost of sales = {_fmt_cell_amt(tot_c)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-15",
        concept_id="dj_credit_sales_and_cost_calculation",
        misconception_tags=["used_wrong_markup_denominator", "forgot_total_row_sum"],
        journal_type="dj",
        duration_mins=7,
    )


def _b16_dj_dual_double_entry_mcq(rng: random.Random) -> Dict[str, Any]:
    s_amt = rng.randrange(1500, 4500, 300)
    c_amt = int(round(s_amt * 2 / 3))
    return _mcq(
        rng,
        subskill="16_dj_dual_double_entry_explanation_mcq",
        prompt=(
            f"At month-end, the Debtors Journal totals show Sales of {_fmt_zar(s_amt)} and Cost of sales of {_fmt_zar(c_amt)}. "
            "Which pair of double entries is posted to the General Ledger?"
        ),
        correct=f"1) Dr Debtors control & Cr Sales ({_fmt_zar(s_amt)});  2) Dr Cost of sales & Cr Trading stock ({_fmt_zar(c_amt)}).",
        distractors=[
            f"1) Dr Bank & Cr Sales ({_fmt_zar(s_amt)});  2) Dr Trading stock & Cr Cost of sales ({_fmt_zar(c_amt)}).",
            f"1) Dr Sales & Cr Debtors control ({_fmt_zar(s_amt)});  2) Dr Cost of sales & Cr Creditors control ({_fmt_zar(c_amt)}).",
            f"Only one entry: Dr Debtors control ({_fmt_zar(s_amt)}) & Cr Trading stock ({_fmt_zar(c_amt)}).",
        ],
        learning_objective_id="EMS9-T4-TXN-16",
        concept_id="dj_dual_double_entry_rule",
        misconception_tags=["debited_bank_for_credit_sale", "reversed_trading_stock_and_cost_of_sales"],
        hints=[
            "Credit sales do NOT touch Bank; they increase Debtors control (Asset + Dr) and Sales (Income + Cr).",
            "At the same time, inventory leaves the shelves, so Cost of sales is debited and Trading stock is credited.",
            "Dr Debtors control / Cr Sales at selling price; Dr Cost of sales / Cr Trading stock at cost price.",
        ],
        worked_solution=f"Credit sales require TWO double entries: record the revenue owed (Dr Debtors control, Cr Sales for {_fmt_zar(s_amt)}) and record inventory cost leaving stock (Dr Cost of sales, Cr Trading stock for {_fmt_zar(c_amt)}).",
    )


def _b17_cj_credit_purchases_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    c1, c2 = rng.sample(_CREDITOR_NAMES, 2)
    stock1 = rng.randrange(1800, 4200, 100)
    stat1 = rng.randrange(250, 650, 50)
    tot1 = stock1 + stat1
    equip2 = rng.randrange(2400, 6200, 200)
    adv2 = rng.randrange(300, 900, 50)
    tot2 = equip2 + adv2
    tot_cc = tot1 + tot2
    tot_sundry = tot2

    headers = ["Doc", "Day", "Creditor", "Creditors control", "Trading stock", "Stationery", "Sundry Amount", "Sundry Details"]
    raw_rows = [
        [
            {"value": "304", "status": "given"},
            {"value": "06", "status": "given"},
            {"value": c1, "status": "given"},
            {"value": _fmt_cell_amt(tot1), "status": "required"},
            {"value": _fmt_cell_amt(stock1), "status": "required"},
            {"value": _fmt_cell_amt(stat1), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "305", "status": "given"},
            {"value": "19", "status": "given"},
            {"value": c2, "status": "given"},
            {"value": _fmt_cell_amt(tot2), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(equip2), "status": "required"},
            {"value": "Equipment", "status": "required"},
        ],
        [
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(adv2), "status": "required"},
            {"value": "Advertising", "status": "required"},
        ],
        [
            {"value": "Total", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_cc), "status": "required"},
            {"value": _fmt_cell_amt(stock1), "status": "given"},
            {"value": _fmt_cell_amt(stat1), "status": "given"},
            {"value": _fmt_cell_amt(tot_sundry), "status": "required"},
            {"value": "", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Total invoice owed to {c1} = {_fmt_cell_amt(stock1)} + {_fmt_cell_amt(stat1)} = {_fmt_cell_amt(tot1)}.",
        "r0_c4": f"Stock bought on credit: {_fmt_cell_amt(stock1)}.",
        "r0_c5": f"Stationery bought on credit: {_fmt_cell_amt(stat1)}.",
        "r1_c3": f"Total invoice owed to {c2} = {_fmt_cell_amt(equip2)} + {_fmt_cell_amt(adv2)} = {_fmt_cell_amt(tot2)}.",
        "r1_c6": f"First sundry item (Equipment): {_fmt_cell_amt(equip2)}.",
        "r1_c7": "Enter account name: Equipment.",
        "r2_c6": f"Second sundry item (Advertising): {_fmt_cell_amt(adv2)}.",
        "r2_c7": "Enter account name: Advertising.",
        "r3_c3": f"Total Creditors control = {_fmt_cell_amt(tot1)} + {_fmt_cell_amt(tot2)} = {_fmt_cell_amt(tot_cc)}.",
        "r3_c6": f"Total Sundry accounts = {_fmt_cell_amt(tot_sundry)}.",
    }
    derivations = [
        f"Inv 304 ({c1}): {_fmt_zar(stock1)} (Trading stock) + {_fmt_zar(stat1)} (Stationery) = {_fmt_zar(tot1)} in Creditors control.",
        f"Inv 305 ({c2}): {_fmt_zar(equip2)} (Equipment) + {_fmt_zar(adv2)} (Advertising) = {_fmt_zar(tot2)} in Creditors control; split across two Sundry lines.",
        f"Column cross-cast: {_fmt_zar(tot_cc)} = {_fmt_zar(stock1)} + {_fmt_zar(stat1)} + {_fmt_zar(tot_sundry)}.",
    ]
    return _table_q(
        subskill="17_cj_credit_purchases_multi_column_2d_table",
        title=f"Creditors Journal (CJ) — {biz}",
        prompt=(
            f"Record these credit purchases of {biz} in the CJ:\n"
            f"- Inv 304 (Day 06) from {c1}: Trading stock {_fmt_zar(stock1)} and Stationery {_fmt_zar(stat1)}.\n"
            f"- Inv 305 (Day 19) from {c2}: Equipment {_fmt_zar(equip2)} and Advertising flyers {_fmt_zar(adv2)}."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Creditors control gets the full invoice total on line 1; never repeat Creditors control on line 2 of a split invoice.",
            "Equipment and Advertising lack dedicated columns in this CJ, so put them in Sundry accounts.",
            f"Total Creditors control = {_fmt_cell_amt(tot_cc)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-17",
        concept_id="cj_multi_column_credit_purchases",
        misconception_tags=["repeated_creditors_control_on_split_line", "put_equipment_in_trading_stock"],
        journal_type="cj",
        duration_mins=8,
    )


def _b18_cj_invoice_with_trade_discount_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    sup = rng.choice(_CREDITOR_NAMES)
    disc_pct = rng.choice([10, 20])
    gross_stock = rng.randrange(2000, 6000, 200)
    gross_stat = rng.randrange(400, 1200, 100)
    net_stock = gross_stock * (100 - disc_pct) / 100
    net_stat = gross_stat * (100 - disc_pct) / 100
    net_tot = net_stock + net_stat

    headers = ["Doc", "Day", "Creditor", "Creditors control", "Trading stock", "Stationery"]
    raw_rows = [
        [
            {"value": "412", "status": "given"},
            {"value": "15", "status": "given"},
            {"value": sup, "status": "given"},
            {"value": _fmt_cell_amt(net_tot), "status": "required"},
            {"value": _fmt_cell_amt(net_stock), "status": "required"},
            {"value": _fmt_cell_amt(net_stat), "status": "required"},
        ]
    ]
    cell_hints = {
        "r0_c3": f"Net invoice = ({_fmt_cell_amt(gross_stock)} + {_fmt_cell_amt(gross_stat)}) × (100 - {disc_pct})% = {_fmt_cell_amt(net_tot)}.",
        "r0_c4": f"Net trading stock = {_fmt_cell_amt(gross_stock)} × {100 - disc_pct}% = {_fmt_cell_amt(net_stock)}.",
        "r0_c5": f"Net stationery = {_fmt_cell_amt(gross_stat)} × {100 - disc_pct}% = {_fmt_cell_amt(net_stat)}.",
    }
    derivations = [
        f"Trade discount is deducted BEFORE recording in the CJ (never recorded separately).",
        f"Net Trading stock = {_fmt_zar(gross_stock)} - {disc_pct}% = {_fmt_zar(net_stock)}.",
        f"Net Stationery = {_fmt_zar(gross_stat)} - {disc_pct}% = {_fmt_zar(net_stat)}.",
        f"Total Creditors control = {_fmt_zar(net_tot)}.",
    ]
    return _table_q(
        subskill="18_cj_invoice_with_trade_discount_calculation_2d_table",
        title=f"CJ Entry After Trade Discount — {biz}",
        prompt=(
            f"{biz} received original invoice no. 412 (Day 15) from {sup} for Trading stock listed at {_fmt_zar(gross_stock)} "
            f"and Stationery listed at {_fmt_zar(gross_stat)}, less {disc_pct}% trade discount on the entire invoice. "
            "Record the net amounts in the CJ."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Trade discount is subtracted immediately from list prices before any journal entry is made.",
            f"Multiply each listed amount by {(100 - disc_pct) / 100:.2f}.",
            f"Creditors control = {_fmt_cell_amt(net_tot)}; Stock = {_fmt_cell_amt(net_stock)}; Stationery = {_fmt_cell_amt(net_stat)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-18",
        concept_id="trade_discount_net_invoice_cj",
        misconception_tags=["entered_gross_list_price_ignoring_trade_discount"],
        journal_type="cj",
    )


def _b19_cj_missing_stationery_column_cross_cast(rng: random.Random) -> Dict[str, Any]:
    stock = rng.randrange(40000, 95000, 1000)
    equip = rng.randrange(12000, 28000, 500)
    pack = rng.randrange(8000, 18000, 500)
    stat = rng.randrange(6500, 14500, 500)
    tot_cc = stock + stat + equip + pack
    sol = f"Missing Stationery total = {_fmt_zar(tot_cc)} - {_fmt_zar(stock)} - {_fmt_zar(equip)} - {_fmt_zar(pack)} = {_fmt_zar(stat)}."
    return _typed(
        subskill="19_cj_missing_stationery_column_cross_cast",
        prompt=(
            f"The Creditors Journal totals at month-end show:\n"
            f"- Creditors control: {_fmt_zar(tot_cc)}\n"
            f"- Trading stock: {_fmt_zar(stock)}\n"
            f"- Sundry (Equipment): {_fmt_zar(equip)}\n"
            f"- Sundry (Packing material): {_fmt_zar(pack)}\n\n"
            "Calculate the missing `Stationery` column total."
        ),
        correct_answer=_fmt_zar(stat),
        accepted_answers=[str(stat), _fmt_zar(stat), _fmt_cell_amt(stat), f"R{stat}"],
        learning_objective_id="EMS9-T4-TXN-19",
        concept_id="cj_column_cross_cast",
        misconception_tags=["added_instead_of_subtracted_sundry_items"],
        hints=[
            "In the CJ, Creditors control must equal the sum of all debit analysis columns plus Sundry items.",
            f"Subtract Trading stock ({_fmt_zar(stock)}) and both Sundry amounts from Creditors control.",
            sol,
        ],
        worked_solution=sol,
    )


def _b20_caj_and_daj_allowances_mcq(rng: random.Random) -> Dict[str, Any]:
    amt = rng.randrange(350, 1450, 50)
    is_caj = rng.choice([True, False])
    if is_caj:
        return _mcq(
            rng,
            subskill="20_caj_and_daj_allowances_and_returns_mcq",
            prompt=f"Goods worth {_fmt_zar(amt)} bought on credit are damaged, so the business issues a Debit Note and returns them to the supplier. Which journal and General Ledger effect apply?",
            correct="Creditors Allowances Journal (CAJ); Dr Creditors control / Cr Trading stock.",
            distractors=[
                "Debtors Allowances Journal (DAJ); Dr Debtors allowances / Cr Debtors control.",
                "Creditors Journal (CJ); Dr Trading stock / Cr Creditors control.",
                "Cash Receipts Journal (CRJ); Dr Bank / Cr Creditors control.",
            ],
            learning_objective_id="EMS9-T4-TXN-20",
            concept_id="caj_vs_daj_credit_returns",
            misconception_tags=["confused_debit_note_with_credit_note"],
            hints=[
                "Debit Note = returning goods to a supplier (reducing what we owe).",
                "Reducing a Creditor liability means Dr Creditors control in the CAJ.",
                "CAJ records debit notes for supplier returns: Dr Creditors control / Cr Trading stock.",
            ],
            worked_solution="Returning damaged credit purchases uses a Debit Note recorded in the Creditors Allowances Journal (CAJ), debiting Creditors control and crediting Trading stock.",
        )
    return _mcq(
        rng,
        subskill="20_caj_and_daj_allowances_and_returns_mcq",
        prompt=f"A credit customer returns damaged trading stock sold on credit for {_fmt_zar(amt)}. We issue a Credit Note. Which journal records this?",
        correct="Debtors Allowances Journal (DAJ), which credits Debtors control (plus reverses Cost of sales and restores Trading stock).",
        distractors=[
            "Creditors Allowances Journal (CAJ), which debits Creditors control.",
            "Debtors Journal (DJ), which increases Sales and Debtors control.",
            "Cash Payments Journal (CPJ), because a refund reduces Bank immediately.",
        ],
        learning_objective_id="EMS9-T4-TXN-20",
        concept_id="caj_vs_daj_credit_returns",
        misconception_tags=["confused_credit_note_with_debit_note"],
        hints=[
            "Credit Note = customer returning credit sales to us.",
            "Customer owes us LESS, so Debtors control is credited in the DAJ.",
            "DAJ records credit notes for customer returns (Dr Debtors allowances, Cr Debtors control, plus stock restoration).",
        ],
        worked_solution="Customer returns on credit use a Credit Note recorded in the Debtors Allowances Journal (DAJ).",
    )


def _b21_journals_brought_down_totals_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    bd_bank = rng.randrange(30000, 75000, 2500)
    bd_stock = rng.randrange(15000, 35000, 1000)
    bd_wages = rng.randrange(8000, 18000, 500)
    bd_cred = bd_bank - bd_stock - bd_wages
    p_stock = rng.randrange(4000, 12000, 500)
    p_wages = rng.randrange(2500, 6500, 250)
    p_cred = rng.randrange(1500, 4500, 250)

    headers = ["Doc", "Day", "Payee", "Bank", "Trading stock", "Wages", "Creditors control"]
    raw_rows = [
        [
            {"value": "", "status": "given"},
            {"value": "29", "status": "given"},
            {"value": "Total b/d", "status": "given"},
            {"value": _fmt_cell_amt(bd_bank), "status": "given"},
            {"value": _fmt_cell_amt(bd_stock), "status": "given"},
            {"value": _fmt_cell_amt(bd_wages), "status": "given"},
            {"value": _fmt_cell_amt(bd_cred), "status": "given"},
        ],
        [
            {"value": "201", "status": "given"},
            {"value": "30", "status": "given"},
            {"value": "Ride Traders", "status": "given"},
            {"value": _fmt_cell_amt(p_stock), "status": "required"},
            {"value": _fmt_cell_amt(p_stock), "status": "given"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "202", "status": "given"},
            {"value": "30", "status": "given"},
            {"value": "Cash", "status": "given"},
            {"value": _fmt_cell_amt(p_wages), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(p_wages), "status": "given"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "203", "status": "given"},
            {"value": "30", "status": "given"},
            {"value": "Slipstream Stores", "status": "given"},
            {"value": _fmt_cell_amt(p_cred), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(p_cred), "status": "given"},
        ],
        [
            {"value": "Total", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bd_bank + p_stock + p_wages + p_cred), "status": "required"},
            {"value": _fmt_cell_amt(bd_stock + p_stock), "status": "required"},
            {"value": _fmt_cell_amt(bd_wages + p_wages), "status": "required"},
            {"value": _fmt_cell_amt(bd_cred + p_cred), "status": "required"},
        ],
    ]
    cell_hints = {
        "r1_c3": f"Cheque 201 for Trading stock: Bank = {_fmt_cell_amt(p_stock)}.",
        "r2_c3": f"Cheque 202 for Wages: Bank = {_fmt_cell_amt(p_wages)}.",
        "r3_c3": f"Cheque 203 to creditor: Bank = {_fmt_cell_amt(p_cred)}.",
        "r4_c3": f"Closing Bank total = {_fmt_cell_amt(bd_bank)} + {_fmt_cell_amt(p_stock + p_wages + p_cred)} = {_fmt_cell_amt(bd_bank + p_stock + p_wages + p_cred)}.",
        "r4_c4": f"Total Trading stock = {_fmt_cell_amt(bd_stock + p_stock)}.",
        "r4_c5": f"Total Wages = {_fmt_cell_amt(bd_wages + p_wages)}.",
        "r4_c6": f"Total Creditors control = {_fmt_cell_amt(bd_cred + p_cred)}.",
    }
    derivations = [
        f"Start with totals b/d (Bank {_fmt_zar(bd_bank)}) and add the three Day 30 payments.",
        f"Closing Bank = {_fmt_zar(bd_bank + p_stock + p_wages + p_cred)}.",
        f"Verify cross-cast: Stock ({_fmt_zar(bd_stock + p_stock)}) + Wages ({_fmt_zar(bd_wages + p_wages)}) + Creditors ({_fmt_zar(bd_cred + p_cred)}) = Bank.",
    ]
    return _table_q(
        subskill="21_journals_brought_down_totals_completion_2d_table",
        title=f"CPJ Brought-Down Totals Completion — {biz}",
        prompt=f"The CPJ of {biz} shows column totals brought down (`Total b/d`) up to Day 29. Complete Day 30 Bank entries and calculate the final month-end totals.",
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Copy each Day 30 payment amount into Bank on its row.",
            "Add Total b/d plus the Day 30 rows down each column.",
            f"Final Bank total = {_fmt_cell_amt(bd_bank + p_stock + p_wages + p_cred)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-21",
        concept_id="journal_totals_brought_down",
        misconception_tags=["ignored_brought_down_total", "crosscast_mismatch"],
        journal_type="cpj",
        duration_mins=6,
    )


def _b22_integrated_four_journals_routing_2d_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    d_name = rng.choice(_DEBTOR_NAMES)
    c_name = rng.choice(_CREDITOR_NAMES)
    amt_sale = rng.randrange(1200, 3600, 200)
    amt_cred = rng.randrange(1500, 4500, 300)
    amt_rent = rng.randrange(2200, 5000, 200)
    amt_pay = rng.randrange(1000, 3000, 200)

    headers = ["Transaction", "Source Document", "Journal", "Account Debited", "Account Credited"]
    raw_rows = [
        [
            {"value": f"1. Cash sales per till ({_fmt_zar(amt_sale)})", "status": "given"},
            {"value": "Cash register roll", "status": "required"},
            {"value": "CRJ", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": "Sales", "status": "required"},
        ],
        [
            {"value": f"2. Sold goods on credit to {d_name} ({_fmt_zar(amt_sale)})", "status": "given"},
            {"value": "Duplicate invoice", "status": "required"},
            {"value": "DJ", "status": "required"},
            {"value": "Debtors control", "status": "required"},
            {"value": "Sales", "status": "given"},
        ],
        [
            {"value": f"3. Bought equipment on credit from {c_name} ({_fmt_zar(amt_cred)})", "status": "given"},
            {"value": "Original invoice", "status": "required"},
            {"value": "CJ", "status": "required"},
            {"value": "Equipment", "status": "required"},
            {"value": "Creditors control", "status": "required"},
        ],
        [
            {"value": f"4. Paid {c_name} {_fmt_zar(amt_pay)} by EFT on account", "status": "given"},
            {"value": "Cheque counterfoil / EFT", "status": "given"},
            {"value": "CPJ", "status": "required"},
            {"value": "Creditors control", "status": "required"},
            {"value": "Bank", "status": "given"},
        ],
        [
            {"value": f"5. Received {_fmt_zar(amt_rent)} rent from tenant", "status": "given"},
            {"value": "Duplicate receipt", "status": "required"},
            {"value": "CRJ", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": "Rent income", "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Cash sales generate a `Cash register roll`.",
        "r0_c2": "Cash received goes to `CRJ`.",
        "r0_c4": "Revenue account credited: `Sales`.",
        "r1_c1": "Credit sale uses a `Duplicate invoice`.",
        "r1_c2": "Credit sales journal = `DJ`.",
        "r1_c3": "Asset increased: `Debtors control`.",
        "r2_c1": "Supplier credit invoice = `Original invoice`.",
        "r2_c2": "Credit purchases journal = `CJ`.",
        "r2_c3": "Asset bought: `Equipment`.",
        "r2_c4": "Liability increased: `Creditors control`.",
        "r3_c2": "Payments belong in `CPJ`.",
        "r3_c3": "Liability decreased: `Creditors control`.",
        "r4_c1": "Receipts for rent/debtors use a `Duplicate receipt`.",
        "r4_c2": "Cash received belongs in `CRJ`.",
        "r4_c4": "Income account credited: `Rent income`.",
    }
    derivations = [
        "1. Cash sales -> Cash register roll | CRJ | Dr Bank, Cr Sales (plus Dr Cost of sales, Cr Trading stock).",
        "2. Credit sale -> Duplicate invoice | DJ | Dr Debtors control, Cr Sales.",
        "3. Credit equipment purchase -> Original invoice | CJ | Dr Equipment, Cr Creditors control.",
        "4. EFT payment to creditor -> EFT / Cheque counterfoil | CPJ | Dr Creditors control, Cr Bank.",
        "5. Cash rent received -> Duplicate receipt | CRJ | Dr Bank, Cr Rent income.",
    ]
    return _table_q(
        subskill="22_integrated_four_journals_routing_2d_table",
        title=f"Master Journal & Account Routing — {biz}",
        prompt=f"Classify the five mixed cash and credit transactions of {biz} by completing the Source Document, Journal (`CRJ`, `CPJ`, `DJ`, `CJ`), Account Debited, and Account Credited.",
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Separate cash receipts (CRJ), cash payments (CPJ), credit sales (DJ), and credit purchases (CJ).",
            "Remember duplicate invoices belong to DJ while original invoices belong to CJ.",
            "Rent received credits `Rent income`; equipment bought on credit debits `Equipment`.",
        ],
        learning_objective_id="EMS9-T4-TXN-22",
        concept_id="integrated_four_journal_routing",
        misconception_tags=["mixed_up_dj_and_cj", "debited_creditor_in_cj"],
        duration_mins=8,
    )


def _b23_cash_vs_credit_sales_proportion_bar_graph(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    cash_sales = rng.randrange(12000, 36000, 4000)
    credit_sales = rng.randrange(8000, 28000, 4000)
    # Force clean ratio
    total_sales = cash_sales + credit_sales
    pct_credit = round(credit_sales * 100 / total_sales, 1)
    cash_purch = rng.randrange(10000, 26000, 2000)
    cred_purch = rng.randrange(8000, 24000, 2000)
    svg = _svg_bar_chart(
        f"{biz} — Monthly Cash vs Credit Activity",
        "Comparison across Subsidiary Journals",
        [
            ("CRJ Cash Sales", float(cash_sales), "#0284c7"),
            ("DJ Credit Sales", float(credit_sales), "#16a34a"),
            ("CPJ Stock Cash", float(cash_purch), "#d97706"),
            ("CJ Stock Credit", float(cred_purch), "#7c3aed"),
        ],
    )
    sol = f"Total Sales = {_fmt_zar(cash_sales)} (CRJ) + {_fmt_zar(credit_sales)} (DJ) = {_fmt_zar(total_sales)}. Credit Sales % = ({credit_sales} / {total_sales}) × 100 = {pct_credit}%."
    ans = f"{pct_credit}%"
    return _typed(
        subskill="23_cash_vs_credit_sales_proportion_bar_graph",
        prompt=f"Refer to the bar graph below for {biz}. Calculate Credit Sales (`DJ`) as a percentage of Total Sales (CRJ Cash Sales + DJ Credit Sales), rounded to 1 decimal place.",
        correct_answer=ans,
        accepted_answers=[ans, f"{pct_credit}", f"{int(pct_credit)}%" if pct_credit == int(pct_credit) else ans],
        learning_objective_id="EMS9-T4-TXN-23",
        concept_id="cash_vs_credit_sales_proportion",
        misconception_tags=["included_purchases_in_total_sales_denominator"],
        hints=[
            "Read ONLY the CRJ Cash Sales and DJ Credit Sales bars to find Total Sales.",
            f"Divide DJ Credit Sales ({_fmt_zar(credit_sales)}) by Total Sales ({_fmt_zar(total_sales)}), then multiply by 100.",
            sol,
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b24_owner_capital_percentage_increase(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([20, 25, 50])
    orig = rng.randrange(12000, 48000, 4000)
    new_cap = int(round(orig * (100 + pct) / 100))
    added = new_cap - orig
    sol = (
        f"Original capital = 100%; new capital = {100 + pct}% = {_fmt_zar(new_cap)}.\n"
        f"Original capital = {_fmt_zar(new_cap)} × 100 / {100 + pct} = {_fmt_zar(orig)}.\n"
        f"Extra capital contributed = {_fmt_zar(new_cap)} - {_fmt_zar(orig)} = {_fmt_zar(added)}."
    )
    return _typed(
        subskill="24_owner_capital_percentage_increase_calculation",
        prompt=(
            f"The owner increased his capital contribution by {pct}% *to* {_fmt_zar(new_cap)}. "
            "Calculate the exact additional Rand amount deposited in the CRJ to reach this new total."
        ),
        correct_answer=_fmt_zar(added),
        accepted_answers=[str(added), _fmt_zar(added), _fmt_cell_amt(added), f"R{added}"],
        learning_objective_id="EMS9-T4-TXN-24",
        concept_id="reverse_percentage_capital_contribution",
        misconception_tags=["took_percentage_of_new_capital_instead_of_original"],
        hints=[
            f"Notice the word 'to': {_fmt_zar(new_cap)} already includes the {pct}% increase, so it equals {100 + pct}%.",
            f"Divide {_fmt_zar(new_cap)} by {100 + pct} and multiply by {pct} to get the increase.",
            sol,
        ],
        worked_solution=sol,
    )


def _b25_personal_vs_business_split_equity_effect(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    owner = biz.split()[0]
    bus_tel = rng.randrange(300, 900, 50)
    pers_tel = rng.randrange(150, 450, 50)
    tot = bus_tel + pers_tel
    return _mcq(
        rng,
        subskill="25_personal_vs_business_split_equity_effect",
        prompt=(
            f"{biz} paid Telkom {_fmt_zar(tot)} by EFT/cheque: {_fmt_zar(bus_tel)} was for the business telephone account, "
            f"and {_fmt_zar(pers_tel)} was for owner {owner}'s private home telephone. How is this recorded in the CPJ?"
        ),
        correct=f"Bank decreases by {_fmt_zar(tot)}; Sundry accounts split into `Telephone` ({_fmt_zar(bus_tel)}) and `Drawings` ({_fmt_zar(pers_tel)}).",
        distractors=[
            f"Bank decreases by {_fmt_zar(tot)} and the entire {_fmt_zar(tot)} is debited to `Telephone`.",
            f"Only {_fmt_zar(bus_tel)} is recorded in the CPJ because personal expenses are ignored by the bank account.",
            f"Bank decreases by {_fmt_zar(tot)} and the {_fmt_zar(pers_tel)} is debited to `Creditors control`.",
        ],
        learning_objective_id="EMS9-T4-TXN-25",
        concept_id="business_entity_concept_drawings_split",
        misconception_tags=["expensed_owner_personal_bill", "omitted_personal_portion_from_bank"],
        hints=[
            "The full amount left the business bank account, so Bank must decrease by the total paid.",
            "Under the Business Entity concept, private expenses paid with business money are Drawings.",
            f"Split CPJ Sundry accounts into Telephone ({_fmt_zar(bus_tel)}) and Drawings ({_fmt_zar(pers_tel)}).",
        ],
        worked_solution=f"Because the full {_fmt_zar(tot)} left the business bank account, Bank is credited with {_fmt_zar(tot)}, while Sundry accounts debit `Telephone` ({_fmt_zar(bus_tel)}) and `Drawings` ({_fmt_zar(pers_tel)}).",
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_source_documents_to_journals_matching_2d_table": _b01_source_documents_to_journals_2d,
    "02_keyword_cues_cash_vs_credit_transactions_mcq": _b02_keyword_cues_cash_vs_credit_mcq,
    "03_owner_vs_customer_invoice_perspective_mcq": _b03_owner_vs_customer_invoice_perspective_mcq,
    "04_subsidiary_journals_to_accounting_cycle_flow_diagram": _b04_accounting_cycle_flow_diagram,
    "05_markup_selling_price_and_cost_of_sales_calculation": _b05_markup_selling_price_and_cost_of_sales,
    "06_calculating_profit_percentage_from_opening_balances": _b06_calculating_profit_pct_from_opening_balances,
    "07_crj_analysis_of_receipts_banking_rule_mcq": _b07_crj_analysis_of_receipts_banking_rule_mcq,
    "08_crj_multi_transaction_entry_2d_table": _b08_crj_multi_transaction_entry_2d_table,
    "09_crj_missing_debtors_control_total_deduction": _b09_crj_missing_debtors_control_total,
    "10_crj_current_income_vs_sales_distinction_mcq": _b10_crj_current_income_vs_sales_mcq,
    "11_cpj_cash_payments_and_bank_columns_2d_table": _b11_cpj_cash_payments_2d_table,
    "12_cpj_split_payment_vehicle_and_fuel_2d_table": _b12_cpj_split_payment_vehicle_and_fuel_2d_table,
    "13_cpj_personal_drawings_and_cash_float_2d_table": _b13_cpj_drawings_and_cash_float_2d_table,
    "14_cpj_direct_debit_order_entry_typed": _b14_cpj_direct_debit_order_entry_typed,
    "15_dj_credit_sales_and_cost_of_sales_2d_table": _b15_dj_credit_sales_2d_table,
    "16_dj_dual_double_entry_explanation_mcq": _b16_dj_dual_double_entry_mcq,
    "17_cj_credit_purchases_multi_column_2d_table": _b17_cj_credit_purchases_2d_table,
    "18_cj_invoice_with_trade_discount_calculation_2d_table": _b18_cj_invoice_with_trade_discount_2d_table,
    "19_cj_missing_stationery_column_cross_cast": _b19_cj_missing_stationery_column_cross_cast,
    "20_caj_and_daj_allowances_and_returns_mcq": _b20_caj_and_daj_allowances_mcq,
    "21_journals_brought_down_totals_completion_2d_table": _b21_journals_brought_down_totals_2d_table,
    "22_integrated_four_journals_routing_2d_table": _b22_integrated_four_journals_routing_2d_table,
    "23_cash_vs_credit_sales_proportion_bar_graph": _b23_cash_vs_credit_sales_proportion_bar_graph,
    "24_owner_capital_percentage_increase_calculation": _b24_owner_capital_percentage_increase,
    "25_personal_vs_business_split_equity_effect": _b25_personal_vs_business_split_equity_effect,
}
