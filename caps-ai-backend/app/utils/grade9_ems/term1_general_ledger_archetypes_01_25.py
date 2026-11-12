"""Grade 9 EMS - General Ledger & Trial Balance (Sole Trader): Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 2/03. General ledger and Trial balance (sole trader).md

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "General ledger and Trial balance (sole trader)"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term1_general_ledger"

TRADER_SUFFIXES = [
    "Traders",
    "Stores",
    "Hardware",
    "Dresses",
    "Outfitter",
    "General Dealer",
    "Suppliers",
    "Wholesalers",
]

MONTH_YEARS = [
    ("March", "2025", "31", "Mar", "April", "01"),
    ("May", "2025", "31", "May", "June", "01"),
    ("July", "2025", "31", "Jul", "August", "01"),
    ("September", "2025", "30", "Sep", "October", "01"),
    ("October", "2025", "31", "Oct", "November", "01"),
]


def _fmt_r(amount: int | float) -> str:
    """Format Rand amounts cleanly with space thousands separator and comma decimal."""
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _trader_name(rng: random.Random, sc: Dict[str, Any]) -> str:
    return f"{sc['entrepreneur']} {rng.choice(TRADER_SUFFIXES)}"


def _cell(coord: str, value: str, ctype: str, editable: bool) -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "cell_id": coord,
        "value": value,
        "type": ctype,
        "editable": editable,
    }


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
    marks: int = 2,
    hints: Dict[str, str],
    misconception_tags: List[str],
    term: int = 1,
    caps_weight: int = 35,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct_text] + list(distractors)
    rng.shuffle(options)
    c_idx = options.index(correct_text)
    letter = chr(65 + c_idx)
    ans_full = f"{letter}. {correct_text}"
    worked = f"**{ans_full}** [{marks} marks]\n\n{explanation}"
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_gl_{subskill}",
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
                {"id": "mp_1", "desc": f"Selects {letter}: {correct_text}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "general_ledger", "sole_trader"],
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
    marks: int = 3,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
    qtype: str = "math_short",
    term: int = 1,
    caps_weight: int = 35,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_gl_{subskill}",
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
        "diagnostic_tags": ["accounting", "general_ledger", "sole_trader"],
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
    term: int = 1,
    caps_weight: int = 35,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_gl_{subskill}",
        "question_type": "table_completion",
        "modality": "ledger",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
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
        "diagnostic_tags": ["accounting", "general_ledger", "ledger_table"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _t_account_svg(
    account_title: str,
    dr_lines: List[tuple[str, str, str]],
    cr_lines: List[tuple[str, str, str]],
    accent: str = "#1d4ed8",
) -> str:
    """Render an authentic South African General Ledger T-account inline SVG."""
    dr_y = 66
    dr_svg: List[str] = []
    for dt, det, amt in dr_lines:
        dr_svg.append(
            f'<text x="18" y="{dr_y}" font-size="10.5" fill="#1e293b">{dt}</text>'
            f'<text x="68" y="{dr_y}" font-size="10.5" fill="#1e293b">{det}</text>'
            f'<text x="248" y="{dr_y}" font-size="10.5" font-weight="bold" text-anchor="end" fill="#0f172a">{amt}</text>'
        )
        dr_y += 20
    cr_y = 66
    cr_svg: List[str] = []
    for dt, det, amt in cr_lines:
        cr_svg.append(
            f'<text x="272" y="{cr_y}" font-size="10.5" fill="#1e293b">{dt}</text>'
            f'<text x="322" y="{cr_y}" font-size="10.5" fill="#1e293b">{det}</text>'
            f'<text x="502" y="{cr_y}" font-size="10.5" font-weight="bold" text-anchor="end" fill="#0f172a">{amt}</text>'
        )
        cr_y += 20
    h = max(145, max(dr_y, cr_y) + 20)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 {h}" width="520" height="{h}">'
        f'<rect x="4" y="4" width="512" height="{h - 8}" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="18" y="24" font-size="11" font-weight="bold" fill="{accent}">Dr</text>'
        f'<text x="260" y="24" font-size="12.5" font-weight="bold" text-anchor="middle" fill="#0f172a">{account_title}</text>'
        f'<text x="502" y="24" font-size="11" font-weight="bold" text-anchor="end" fill="{accent}">Cr</text>'
        f'<line x1="12" y1="32" x2="508" y2="32" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="260" y1="32" x2="260" y2="{h - 12}" stroke="#0f172a" stroke-width="2"/>'
        '<text x="18" y="47" font-size="9.5" fill="#64748b">Date</text>'
        '<text x="68" y="47" font-size="9.5" fill="#64748b">Details</text>'
        '<text x="248" y="47" font-size="9.5" text-anchor="end" fill="#64748b">Amount</text>'
        '<text x="272" y="47" font-size="9.5" fill="#64748b">Date</text>'
        '<text x="322" y="47" font-size="9.5" fill="#64748b">Details</text>'
        '<text x="502" y="47" font-size="9.5" text-anchor="end" fill="#64748b">Amount</text>'
        + "".join(dr_svg)
        + "".join(cr_svg)
        + "</svg>"
    )


def arch_01_general_ledger_heading_and_date_rules(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    cases = [
        (
            "overall main heading of the General Ledger",
            f"'General Ledger of {biz}' — containing ONLY the business name, NEVER the month or date.",
            [
                f"'General Ledger of {biz} on {last_d} {m_name} {yr}' — every ledger heading must carry the closing date.",
                f"'Trial Balance of {biz} for {yr}' — omitting any business owner identifier.",
                f"'Cash Receipts Ledger of {sc['entrepreneur']}' — listing only the month name without Dr/Cr.",
            ],
        ),
        (
            "dates recorded when posting CRJ and CPJ analysis column totals versus Sundry items",
            f"Analysis column totals are posted on the last day of the month ({last_d} {m_name}), while each Sundry entry is posted on the exact transaction day.",
            [
                f"Both analysis column totals and individual Sundry entries are always posted on Day 01 of {m_name}.",
                "Sundry accounts are summed and posted once on the last day of the month, while Sales is posted daily.",
                "No dates are ever written in General Ledger Date columns because journals already store dates.",
            ],
        ),
    ]
    focus, correct, distractors = rng.choice(cases)
    prompt = (
        f"When opening the General Ledger for **{biz}** in **{m_name} {yr}**, "
        f"which standard rule applies to the **{focus}**?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_01",
        subskill="01_general_ledger_heading_and_date_rules",
        title="General Ledger Heading & Posting Date Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Standard General Ledger convention: **{correct}**",
        hints={
            "tier_1": "Unlike a Trial Balance ('on <date>'), the General Ledger accumulates across months.",
            "tier_2": f"Ledger heading = 'General Ledger of {biz}' (no date); column totals go on day {last_d}, Sundry items on their transaction date.",
            "tier_3": correct,
        },
        misconception_tags=["putting_date_in_general_ledger_heading"],
    )


def arch_02_analysis_total_vs_sundry_individual_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cap_amt = rng.randint(15, 45) * 1000
    rent_amt = rng.randint(3, 9) * 500
    sundry_tot = cap_amt + rent_amt

    prompt = (
        f"In **{biz}**'s CRJ, the `Sundry Accounts` column shows Capital ({_fmt_r(cap_amt)}) on Day 04 and Rent Income ({_fmt_r(rent_amt)}) on Day 21, summing to **{_fmt_r(sundry_tot)}**.\n\n"
        f"Why is the Sundry total **{_fmt_r(sundry_tot)}** NEVER posted directly to a single General Ledger account?"
    )
    correct = f"Because Sundry mixes unrelated accounts (Capital and Rent Income), so each item ({_fmt_r(cap_amt)} and {_fmt_r(rent_amt)}) must be posted individually to its own ledger account on its transaction date."
    distractors = [
        f"Because Sundry items are omitted from the Trial Balance completely once Total Receipts reaches Bank.",
        f"Because {_fmt_r(sundry_tot)} must be posted as one lump sum into Cost of Sales instead.",
        f"Because Sundry accounts belong only in the Cash Payments Journal.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_02",
        subskill="02_analysis_total_vs_sundry_individual_posting",
        title="Why Sundry Column Totals Are Never Posted",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The **Sundry Accounts** column is a shared catch-all for different accounts (here **Capital {_fmt_r(cap_amt)}** and **Rent Income {_fmt_r(rent_amt)}**). "
            f"Posting {_fmt_r(sundry_tot)} as a single entry would corrupt individual ledger balances, whereas `{_fmt_r(sundry_tot)}` is ALREADY included inside `Bank Total Receipts`!"
        ),
        hints={
            "tier_1": "Check whether items in Sundry Accounts belong to the same T-account or different T-accounts.",
            "tier_2": "Each Sundry entry posts individually on its own date; the column total is strictly for cross-checking Bank.",
            "tier_3": correct,
        },
        misconception_tags=["posting_sundry_column_total_as_one_account"],
    )


def arch_03_dead_clic_classification_trading_sole_trader_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    pool = [
        ("Trading Stock", "Balance Sheet", "Debit"),
        ("Bank (Favourable)", "Balance Sheet", "Debit"),
        ("Capital", "Balance Sheet", "Credit"),
        ("Drawings", "Balance Sheet", "Debit"),
        ("Sales", "Nominal", "Credit"),
        ("Cost of Sales", "Nominal", "Debit"),
        ("Wages", "Nominal", "Debit"),
        ("Rent Income", "Nominal", "Credit"),
    ]
    chosen = rng.sample(pool, 5)
    headers = ["Ledger Account", "Section (`Balance Sheet` / `Nominal`)", "Increase Side (`Debit` / `Credit`)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Ledger Account | Section | Increase Side |", "| --- | --- | --- |"]

    for i, (acc, sec, side) in enumerate(chosen):
        correct_map[f"t0_r{i}_c1"] = sec
        correct_map[f"t0_r{i}_c2"] = side
        cell_hints[f"t0_r{i}_c1"] = "Assets, Equity & Liabilities -> Balance Sheet; Incomes & Expenses -> Nominal."
        cell_hints[f"t0_r{i}_c2"] = "DEAD (Drawings, Expenses, Assets -> Debit); CLIC (Capital, Liabilities, Income -> Credit)."
        rows.append([
            _cell(f"t0_r{i}_c0", acc, "given", False),
            _cell(f"t0_r{i}_c1", "", "required", True),
            _cell(f"t0_r{i}_c2", "", "required", True),
        ])
        md_lines.append(f"| {acc} | **{sec}** | **{side}** |")

    prompt = (
        f"Classify each sole-trader General Ledger account of **{biz}** below by **Section** (`Balance Sheet` or `Nominal`) "
        f"and **Increase Side** (`Debit` or `Credit`)."
    )
    sample = "; ".join(f"{acc}: {sec}, {side}" for acc, sec, side in chosen)
    worked = "**Sole-Trader DEAD/CLIC & Section Classification** [10 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_gl_03",
        subskill="03_dead_clic_classification_trading_sole_trader_table",
        title="Classify Trading Accounts: Section & Increase Side",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=10,
        hints={
            "tier_1": "Balance Sheet = Assets, Capital, Drawings, Liabilities; Nominal = Incomes & Expenses.",
            "tier_2": "Apply DEAD (Debit increases Drawings, Expenses, Assets) and CLIC (Credit increases Capital, Liabilities, Income).",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"{acc}: {sec}, {side}", "marks": 2, "editable": True} for i, (acc, sec, side) in enumerate(chosen)],
        misconception_tags=["dead_clic_rule_inversion", "balance_sheet_vs_nominal_confusion"],
    )


def arch_04_folio_referencing_journals_and_ledger(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    jnl_no = rng.randint(1, 9)
    acc_pair = rng.choice([
        ("Trading Stock", "B6", f"CPJ{jnl_no}", "below the Trading Stock column total"),
        ("Equipment", "B5", f"CPJ{jnl_no}", "in the Sundry folio column next to Equipment"),
        ("Sales", "N1", f"CRJ{jnl_no}", "below the Sales column total"),
        ("Rent Income", "N3", f"CRJ{jnl_no}", "in the Sundry folio column next to Rent Income"),
    ])
    acc_name, ledger_fol, jnl_fol, placement = acc_pair

    prompt = (
        f"While posting **{biz}**'s **{jnl_fol}** into General Ledger account **{acc_name} ({ledger_fol})**, "
        f"how must cross-referencing **folio codes** be recorded in BOTH books?"
    )
    correct = f"Write '{jnl_fol}' in the Fol. column of {acc_name} ({ledger_fol}), and write '{ledger_fol}' {placement} in the journal."
    distractors = [
        f"Write '{ledger_fol}' inside {acc_name} itself and leave the journal folio column empty.",
        f"Write the Rand amount in the Fol. column of both the journal and the General Ledger.",
        f"Use 'CRJ' inside Balance Sheet accounts and 'CPJ' inside Nominal accounts regardless of source.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_04",
        subskill="04_folio_referencing_journals_and_ledger",
        title="Cross-Referencing Folios: Journals & General Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Folio cross-referencing creates an audit trail: the General Ledger (`{acc_name} {ledger_fol}`) records where the entry came from (`{jnl_fol}`), "
            f"while the journal records `{ledger_fol}` {placement} to show posting is complete."
        ),
        hints={
            "tier_1": "Each book points to the OTHER book's page/code!",
            "tier_2": f"Ledger points back to journal ({jnl_fol}); journal points forward to ledger ({ledger_fol}).",
            "tier_3": correct,
        },
        misconception_tags=["reversing_journal_and_ledger_folios"],
    )


def arch_05_crj_total_receipts_to_bank_details_rule(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales = rng.randint(15, 45) * 500
    cap = rng.randint(10, 40) * 1000
    tot_rec = sales + cap

    prompt = (
        f"On the last day of the month, **{biz}** posts its CRJ `Bank` total of **{_fmt_r(tot_rec)}** "
        f"(composed of Sales {_fmt_r(sales)} + Capital {_fmt_r(cap)}) to the Debit side of the **Bank (B7)** General Ledger account.\n\n"
        f"Why must the **`Details`** column of **Bank** say **`Total receipts`** instead of `Sales`?"
    )
    correct = f"Because {_fmt_r(tot_rec)} is a combined total containing multiple contra accounts (Sales AND Capital/Sundry items), not Sales alone."
    distractors = [
        "Because Sales is an expense account that only appears in the Cash Payments Journal.",
        "Because Total receipts represents Cost of Sales deducted from Bank at month-end.",
        "Because Bank is always credited with Sales on the Debit side.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_05",
        subskill="05_crj_total_receipts_to_bank_details_rule",
        title="Why Bank Shows 'Total receipts' Instead of 'Sales'",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"We cannot write `Sales` in the Bank account details for **{_fmt_r(tot_rec)}** because `Total receipts` includes "
            f"other receipts such as **Capital ({_fmt_r(cap)})** alongside **Sales ({_fmt_r(sales)})**."
        ),
        hints={
            "tier_1": "Notice that Bank's {_fmt_r(tot_rec)} total is the sum of BOTH Sales and Sundry accounts.",
            "tier_2": "Writing 'Sales' would wrongly imply all cash received came purely from selling merchandise.",
            "tier_3": correct,
        },
        misconception_tags=["writing_sales_as_bank_total_detail"],
    )


def arch_06_crj_sales_contra_posting_rule(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    sales_tot = rng.randint(18, 65) * 500
    cos_tot = sales_tot * 100 // 125
    jnl = f"CRJ{rng.randint(1, 6)}"

    prompt = (
        f"**{biz}**'s Cash Receipts Journal (**{jnl}**) shows month-end totals for **{m_name} {yr}**: "
        f"`Sales = {_fmt_r(sales_tot)}` and `Cost of Sales = {_fmt_r(cos_tot)}`.\n\n"
        f"How is **`Sales (N1)`** posted in the General Ledger?"
    )
    correct = f"Credit Sales (N1) on {last_d} {m_name} with Details 'Bank', Folio '{jnl}', Amount {_fmt_r(sales_tot)}."
    distractors = [
        f"Debit Sales (N1) on {last_d} {m_name} with Details 'Total receipts', Amount {_fmt_r(sales_tot)}.",
        f"Credit Sales (N1) with {_fmt_r(sales_tot - cos_tot)} (net Gross Profit only) and omit Cost of Sales.",
        f"Credit Sales (N1) with {_fmt_r(cos_tot)} under Details 'Trading Stock'.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_06",
        subskill="06_crj_sales_contra_posting_rule",
        title="Posting CRJ Sales Column Total to Sales (N1)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Sales (N1)** is an Income account (CLIC -> Credit increases). Because cash received went to Debit Bank, "
            f"**Sales** is Credited on **{last_d} {m_name}** with contra account **`Bank`**, folio **`{jnl}`**, and full Selling Price **{_fmt_r(sales_tot)}**."
        ),
        hints={
            "tier_1": "Apply CLIC to Sales (Income) and identify the contra account where cash was debited.",
            "tier_2": f"Credit Sales on month-end ({last_d} {m_name}) -> Details: Bank -> {jnl} -> {_fmt_r(sales_tot)}.",
            "tier_3": correct,
        },
        misconception_tags=["crj_posting_side_reversal"],
    )


def arch_07_crj_cost_of_sales_to_trading_stock_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    cos_tot = rng.randint(14, 52) * 250
    jnl = f"CRJ{rng.randint(1, 6)}"

    prompt = (
        f"At the end of **{m_name} {yr}**, **{biz}**'s **{jnl}** shows a **`Cost of Sales`** column total of **{_fmt_r(cos_tot)}**.\n\n"
        f"Which General Ledger double-entry posts this **{_fmt_r(cos_tot)}** accurately?"
    )
    correct = f"Debit Cost of Sales (N2) [Details: Trading Stock, {jnl}] {_fmt_r(cos_tot)} AND Credit Trading Stock (B6) [Details: Cost of Sales, {jnl}] {_fmt_r(cos_tot)}."
    distractors = [
        f"Debit Bank (B7) {_fmt_r(cos_tot)} and Credit Cost of Sales (N2) [Details: Bank] {_fmt_r(cos_tot)}.",
        f"Debit Trading Stock (B6) {_fmt_r(cos_tot)} and Credit Sales (N1) {_fmt_r(cos_tot)}.",
        f"Credit Cost of Sales (N2) {_fmt_r(cos_tot)} and Credit Trading Stock (B6) {_fmt_r(cos_tot)} simultaneously.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_07",
        subskill="07_crj_cost_of_sales_to_trading_stock_posting",
        title="Posting CRJ Cost of Sales & Trading Stock Double Entry",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Cost of Sales** is a non-cash item and NEVER touches `Bank`. "
            f"On **{last_d} {m_name}**, Debit **Cost of Sales** (expense increasing -> DEAD, `Details: Trading Stock`) "
            f"and Credit **Trading Stock** (inventory asset decreasing, `Details: Cost of Sales`) with **{_fmt_r(cos_tot)}**."
        ),
        hints={
            "tier_1": "Cost of Sales never enters Bank; think which asset leaves the shop when goods are sold.",
            "tier_2": "Expense Cost of Sales increases (Dr); Asset Trading Stock decreases (Cr).",
            "tier_3": correct,
        },
        misconception_tags=["posting_cost_of_sales_to_bank"],
    )


def arch_08_crj_sundry_capital_and_rent_income_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _, _, _ = rng.choice(MONTH_YEARS)
    day = rng.randint(4, 24)
    is_cap = rng.choice([True, False])
    acc, fol, amt = ("Capital", "B1", rng.randint(25, 95) * 1000) if is_cap else ("Rent Income", "N3", rng.randint(4, 15) * 500)
    jnl = f"CRJ{rng.randint(1, 5)}"

    prompt = (
        f"On **{day:02d} {m_name} {yr}**, **{biz}**'s **{jnl}** Sundry Accounts column records **{_fmt_r(amt)}** for **{acc} ({fol})**.\n\n"
        f"Which exact entry appears inside the **{acc} ({fol})** General Ledger T-account?"
    )
    correct = f"Credit side: Date {day:02d} {m_name}, Details 'Bank', Fol. '{jnl}', Amount {_fmt_r(amt)}."
    distractors = [
        f"Credit side: Date 30/31 {m_name} (month-end), Details 'Total receipts', Fol. '{jnl}', Amount {_fmt_r(amt)}.",
        f"Debit side: Date {day:02d} {m_name}, Details 'Bank', Fol. '{jnl}', Amount {_fmt_r(amt)}.",
        f"Credit side: Date {day:02d} {m_name}, Details 'Sundry Accounts', Fol. '{jnl}', Amount {_fmt_r(amt)}.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_08",
        subskill="08_crj_sundry_capital_and_rent_income_posting",
        title="Posting Individual CRJ Sundry Entries",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Sundry CRJ entries are posted on the **exact transaction day (`{day:02d} {m_name}`)** to the **Credit side** (CLIC), "
            f"with contra Details **`Bank`** (never `'Sundry Accounts'` and never summed at month-end)."
        ),
        hints={
            "tier_1": "Check three things: Side (CLIC -> Credit), Date (transaction day for Sundry!), Details (contra account 'Bank').",
            "tier_2": f"Credit {acc} on {day:02d} {m_name} with Details: Bank and Fol: {jnl}.",
            "tier_3": correct,
        },
        misconception_tags=["posting_sundry_on_month_end_date", "writing_sundry_as_ledger_detail"],
    )


def arch_09_crj_full_posting_summary_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    markup = rng.choice([25, 50])
    cos_tot = rng.randint(12, 36) * 200
    sales_tot = cos_tot * (100 + markup) // 100
    cap_amt = rng.randint(25, 75) * 1000
    rent_amt = rng.randint(3, 10) * 500
    bank_tot = sales_tot + cap_amt + rent_amt

    headers = ["Account Debited / Credited", "Date (Day)", "Details (Contra Account)", "Side (`Debit` / `Credit`)", "Amount (R)"]
    specs = [
        ("Bank (B7)", last_d, "Total receipts", "Debit", str(bank_tot)),
        ("Sales (N1)", last_d, "Bank", "Credit", str(sales_tot)),
        ("Cost of Sales (N2)", last_d, "Trading Stock", "Debit", str(cos_tot)),
        ("Trading Stock (B6)", last_d, "Cost of Sales", "Credit", str(cos_tot)),
        ("Capital (B1) — Day 03", "03", "Bank", "Credit", str(cap_amt)),
        ("Rent Income (N3) — Day 19", "19", "Bank", "Credit", str(rent_amt)),
    ]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Ledger Account | Date (Day) | Details | Side | Amount (R) |", "| --- | --- | --- | --- | --- |"]

    for i, (acc, dy, det, side, amt) in enumerate(specs):
        # Test Details, Side, Amount on key postings, keep Date given on some and required on others for crisp practice
        date_ed = i in (0, 4)
        if date_ed:
            correct_map[f"t0_r{i}_c1"] = dy
            cell_hints[f"t0_r{i}_c1"] = "Totals post on month-end day; Sundry items post on transaction day."
        correct_map[f"t0_r{i}_c2"] = det
        correct_map[f"t0_r{i}_c3"] = side
        correct_map[f"t0_r{i}_c4"] = amt
        cell_hints[f"t0_r{i}_c2"] = f"Contra ledger/journal wording for {acc} (e.g. 'Total receipts', 'Bank', 'Trading Stock', 'Cost of Sales')."
        cell_hints[f"t0_r{i}_c3"] = f"Apply DEAD/CLIC to {acc}."
        cell_hints[f"t0_r{i}_c4"] = f"Enter digits without spaces or R ({amt})."
        rows.append([
            _cell(f"t0_r{i}_c0", acc, "given", False),
            _cell(f"t0_r{i}_c1", "" if date_ed else dy, "required" if date_ed else "given", date_ed),
            _cell(f"t0_r{i}_c2", "", "required", True),
            _cell(f"t0_r{i}_c3", "", "required", True),
            _cell(f"t0_r{i}_c4", "", "required", True),
        ])
        dy_md = f"**{dy}**" if date_ed else dy
        md_lines.append(f"| {acc} | {dy_md} | **{det}** | **{side}** | **{_fmt_r(int(amt))}** |")

    prompt = (
        f"The completed **CRJ** of **{biz}** for **{m_name} {yr}** (31/{last_d} month-end) reports:\n"
        f"- **Bank column total:** {_fmt_r(bank_tot)}\n"
        f"- **Sales column total:** {_fmt_r(sales_tot)}\n"
        f"- **Cost of Sales column total:** {_fmt_r(cos_tot)}\n"
        f"- **Sundry Accounts:** Day 03 Capital {_fmt_r(cap_amt)}; Day 19 Rent Income {_fmt_r(rent_amt)}\n\n"
        f"Complete the General Ledger posting table below (amounts without spaces or R)."
    )
    sample = f"Bank Dr {bank_tot} (Total receipts); Sales Cr {sales_tot}; COS Dr / Stock Cr {cos_tot}; Capital Cr {cap_amt}; Rent Cr {rent_amt}"
    worked = f"**CRJ to General Ledger Posting Memorandum** [12 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_gl_09",
        subskill="09_crj_full_posting_summary_table",
        title="Post Completed CRJ to General Ledger Accounts",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=12,
        hints={
            "tier_1": "Post Bank Dr Total receipts, credit all cash source accounts, and pair Cost of Sales Dr with Trading Stock Cr.",
            "tier_2": f"Month-end day = {last_d}; Capital posts on Day 03; Cost of Sales ({cos_tot}) pairs Dr Cost of Sales / Cr Trading Stock.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Bank Dr Total receipts {bank_tot} on Day {last_d}", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Sales Cr Bank {sales_tot}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"COS Dr Trading Stock & Stock Cr COS {cos_tot}", "marks": 4, "editable": True},
            {"id": "mp_4", "desc": f"Sundry Capital ({cap_amt}) on Day 03 & Rent ({rent_amt}) on Day 19", "marks": 3, "editable": True},
        ],
        misconception_tags=["crj_posting_side_reversal", "posting_cost_of_sales_to_bank"],
    )


def arch_10_cpj_total_payments_to_bank_credit_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    tot_pay = rng.randint(20, 75) * 500
    jnl = f"CPJ{rng.randint(1, 8)}"

    prompt = (
        f"At the end of **{m_name} {yr}**, **{biz}**'s **{jnl}** `Bank` column totals **{_fmt_r(tot_pay)}**.\n\n"
        f"How is **{_fmt_r(tot_pay)}** posted to the **Bank (B7)** General Ledger account, and why?"
    )
    correct = f"Credited to Bank (B7) on {last_d} {m_name} with Details 'Total payments' and Fol. '{jnl}' because cash outflows decrease the Bank asset."
    distractors = [
        f"Debited to Bank (B7) on {last_d} {m_name} with Details 'Total payments' because Bank is always debited.",
        f"Credited to Bank (B7) as separate individual lines for Trading Stock, Wages, and Stationery.",
        f"Posted to Cost of Sales instead of Bank because inventory was bought.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_10",
        subskill="10_cpj_total_payments_to_bank_credit_posting",
        title="Posting CPJ Total Payments to Bank (B7)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Money paid out in **{jnl}** decreases **Bank** (an Asset -> decreases on the **Credit** side). "
            f"On **{last_d} {m_name}**, Credit **Bank (B7)** with **`Total payments`**, **`{jnl}`**, and **{_fmt_r(tot_pay)}**."
        ),
        hints={
            "tier_1": "Cash leaving the business bank account decreases Assets (DEAD -> Credit decreases Assets).",
            "tier_2": f"Credit Bank on {last_d} {m_name} with Details: Total payments ({jnl}).",
            "tier_3": correct,
        },
        misconception_tags=["debiting_cpj_bank_payments"],
    )


def arch_11_cpj_trading_stock_purchases_debit_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    stock_pur = rng.randint(16, 65) * 400
    jnl = f"CPJ{rng.randint(1, 7)}"

    prompt = (
        f"During **{m_name} {yr}**, **{biz}** purchased merchandise for resale throughout the month, giving a **`Trading Stock`** column total of **{_fmt_r(stock_pur)}** in **{jnl}**.\n\n"
        f"Record the correct General Ledger posting into **Trading Stock (B6)**."
    )
    correct = f"Debit Trading Stock (B6) on {last_d} {m_name} with Details 'Bank', Fol. '{jnl}', Amount {_fmt_r(stock_pur)} (Asset increases)."
    distractors = [
        f"Credit Trading Stock (B6) on {last_d} {m_name} with Details 'Cost of Sales', Amount {_fmt_r(stock_pur)}.",
        f"Debit Cost of Sales (N2) directly on {last_d} {m_name} instead of Trading Stock.",
        f"Debit Trading Stock (B6) with Details 'Purchases' on Day 01 of the month.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_11",
        subskill="11_cpj_trading_stock_purchases_debit_posting",
        title="Posting CPJ Trading Stock Column Total",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Buying stock increases **Trading Stock (B6)** (an Asset -> Debit increases under DEAD). "
            f"Because the analysis column total is posted at month-end against **Bank**, write **{last_d} {m_name} | Bank | {jnl} | {_fmt_r(stock_pur)}** on the **Debit** side."
        ),
        hints={
            "tier_1": "Trading Stock is an Asset bought for resale; check which side increases Assets (DEAD).",
            "tier_2": f"Debit Trading Stock on {last_d} {m_name} with contra Details 'Bank' and {jnl}.",
            "tier_3": correct,
        },
        misconception_tags=["posting_stock_purchases_to_cost_of_sales"],
    )


def arch_12_cpj_expenses_wages_stationery_packing_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    acc, fol, amt = rng.choice([
        ("Wages", "N4", rng.randint(6, 20) * 350),
        ("Stationery", "N7", rng.randint(4, 15) * 150),
        ("Packing Material", "N5", rng.randint(5, 18) * 120),
    ])
    jnl = f"CPJ{rng.randint(1, 6)}"

    prompt = (
        f"At month-end (**{last_d} {m_name} {yr}**), **{biz}**'s **{jnl}** shows a **`{acc}`** analysis column total of **{_fmt_r(amt)}**.\n\n"
        f"Which entry posts **{acc} ({fol})** to the General Ledger?"
    )
    correct = f"Debit {acc} ({fol}) on {last_d} {m_name} with Details 'Bank', Fol. '{jnl}', Amount {_fmt_r(amt)} (Expense increases on Debit, reducing Owner's Equity)."
    distractors = [
        f"Credit {acc} ({fol}) on {last_d} {m_name} with Details 'Bank', Amount {_fmt_r(amt)}.",
        f"Debit Bank (B7) with Details '{acc}', Amount {_fmt_r(amt)}.",
        f"Post each individual cheque separately on {last_d} {m_name} using Details 'Total payments'.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_12",
        subskill="12_cpj_expenses_wages_stationery_packing_posting",
        title=f"Posting CPJ Expense Column ({acc}) to Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**{acc}** is a Nominal Expense account (DEAD -> **Debit**). Because it is a dedicated analysis column total, "
            f"post **{_fmt_r(amt)}** on **{last_d} {m_name}** with Details **`Bank`** and Fol. **`{jnl}`**."
        ),
        hints={
            "tier_1": f"Remember DEAD: Expenses ({acc}) increase on the Debit side and reduce Owner's Equity.",
            "tier_2": f"Post analysis column total on {last_d} {m_name} -> Debit {acc}, Details: Bank.",
            "tier_3": correct,
        },
        misconception_tags=["crediting_expense_accounts_on_payment"],
    )


def arch_13_cpj_sundry_drawings_and_equipment_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _, _, _ = rng.choice(MONTH_YEARS)
    day = rng.randint(5, 25)
    choice_item = rng.choice([
        ("Drawings", "B2", rng.randint(6, 24) * 250, "owner cash withdrawal"),
        ("Equipment", "B5", rng.randint(15, 55) * 400, "cash register & shelving"),
        ("Trading Licence", "N9", rng.randint(4, 15) * 100, "annual municipal business licence"),
    ])
    acc, fol, amt, desc = choice_item
    jnl = f"CPJ{rng.randint(1, 5)}"

    prompt = (
        f"On **{day:02d} {m_name} {yr}**, **{biz}** paid **{_fmt_r(amt)}** for **{desc}** (recorded in **Sundry Accounts** of **{jnl}**).\n\n"
        f"State the exact **Side**, **Date**, and **Details** in the **{acc} ({fol})** General Ledger account."
    )
    correct = f"Debit side | Date: {day:02d} {m_name} | Details: Bank | Fol: {jnl} | Amount: {_fmt_r(amt)}"
    distractors = [
        f"Credit side | Date: {day:02d} {m_name} | Details: Bank | Fol: {jnl} | Amount: {_fmt_r(amt)}",
        f"Debit side | Date: 30/31 {m_name} (month-end) | Details: Total payments | Fol: {jnl} | Amount: {_fmt_r(amt)}",
        f"Debit side | Date: {day:02d} {m_name} | Details: Sundry Accounts | Fol: {jnl} | Amount: {_fmt_r(amt)}",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_13",
        subskill="13_cpj_sundry_drawings_and_equipment_posting",
        title="Posting Individual CPJ Sundry Entries",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"All CPJ contra entries are **Debited** (since Bank was Credited). Because **{acc}** sits in Sundry Accounts, "
            f"post on the **exact transaction day (`{day:02d} {m_name}`)** with Details **`Bank`**."
        ),
        hints={
            "tier_1": "Since CPJ Bank is Credited, every other account posted from the CPJ is Debited.",
            "tier_2": f"Sundry items use their transaction date ({day:02d} {m_name}) and contra account 'Bank'.",
            "tier_3": correct,
        },
        misconception_tags=["posting_sundry_on_month_end_date", "writing_sundry_as_ledger_detail"],
    )


def arch_14_cpj_full_posting_summary_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, _, _, _ = rng.choice(MONTH_YEARS)
    stock_amt = rng.randint(14, 48) * 500
    wages_amt = rng.randint(6, 18) * 300
    equip_amt = rng.randint(8, 28) * 500
    draw_amt = rng.randint(4, 14) * 250
    bank_tot = stock_amt + wages_amt + equip_amt + draw_amt

    headers = ["General Ledger Account", "Date (Day)", "Details (Contra Account)", "Side (`Debit` / `Credit`)", "Amount (R)"]
    specs = [
        ("Bank (B7)", last_d, "Total payments", "Credit", str(bank_tot)),
        ("Trading Stock (B6)", last_d, "Bank", "Debit", str(stock_amt)),
        ("Wages (N4)", last_d, "Bank", "Debit", str(wages_amt)),
        ("Equipment (B5) — Day 08", "08", "Bank", "Debit", str(equip_amt)),
        ("Drawings (B2) — Day 23", "23", "Bank", "Debit", str(draw_amt)),
    ]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| General Ledger Account | Date (Day) | Details | Side | Amount (R) |", "| --- | --- | --- | --- | --- |"]

    for i, (acc, dy, det, side, amt) in enumerate(specs):
        date_ed = i in (0, 3)
        if date_ed:
            correct_map[f"t0_r{i}_c1"] = dy
            cell_hints[f"t0_r{i}_c1"] = "Totals post on month-end day; Sundry items post on exact transaction day."
        correct_map[f"t0_r{i}_c2"] = det
        correct_map[f"t0_r{i}_c3"] = side
        correct_map[f"t0_r{i}_c4"] = amt
        cell_hints[f"t0_r{i}_c2"] = "Bank uses 'Total payments'; contra accounts use 'Bank'."
        cell_hints[f"t0_r{i}_c3"] = "CPJ Bank decreases on Credit; contra assets, expenses & drawings Debit."
        cell_hints[f"t0_r{i}_c4"] = f"Enter numeric Rand amount without spaces or R ({amt})."
        rows.append([
            _cell(f"t0_r{i}_c0", acc, "given", False),
            _cell(f"t0_r{i}_c1", "" if date_ed else dy, "required" if date_ed else "given", date_ed),
            _cell(f"t0_r{i}_c2", "", "required", True),
            _cell(f"t0_r{i}_c3", "", "required", True),
            _cell(f"t0_r{i}_c4", "", "required", True),
        ])
        dy_md = f"**{dy}**" if date_ed else dy
        md_lines.append(f"| {acc} | {dy_md} | **{det}** | **{side}** | **{_fmt_r(int(amt))}** |")

    prompt = (
        f"The completed **CPJ** of **{biz}** for **{m_name} {yr}** (month-end Day {last_d}) reports:\n"
        f"- **Bank column total:** {_fmt_r(bank_tot)}\n"
        f"- **Trading Stock column total:** {_fmt_r(stock_amt)}\n"
        f"- **Wages column total:** {_fmt_r(wages_amt)}\n"
        f"- **Sundry Accounts:** Day 08 Equipment {_fmt_r(equip_amt)}; Day 23 Drawings {_fmt_r(draw_amt)}\n\n"
        f"Complete the General Ledger posting table below (enter amounts without spaces or R)."
    )
    sample = f"Bank Cr {bank_tot} (Total payments); Trading Stock Dr {stock_amt}; Wages Dr {wages_amt}; Equipment Dr {equip_amt} (08); Drawings Dr {draw_amt} (23)"
    worked = f"**CPJ to General Ledger Posting Memorandum** [10 marks]\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_gl_14",
        subskill="14_cpj_full_posting_summary_table",
        title="Post Completed CPJ to General Ledger Accounts",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=10,
        hints={
            "tier_1": "Credit Bank with Total payments on month-end; Debit each asset, expense, and Drawings contra account.",
            "tier_2": f"Bank Cr = {bank_tot}; Equipment posts on Day 08, Drawings on Day 23.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"{specs[i][0]}: {specs[i][3]} {specs[i][4]}", "marks": 2, "editable": True} for i in range(5)],
        misconception_tags=["debiting_cpj_bank_payments", "posting_sundry_on_month_end_date"],
    )


def arch_15_bank_t_account_balancing_favourable_debit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, m_abbr, next_m, _ = rng.choice(MONTH_YEARS)
    open_bal = rng.randint(15, 45) * 1000
    crj_tot = rng.randint(25, 65) * 500
    tot_dr = open_bal + crj_tot
    cpj_tot = rng.randint(12, 35) * 500
    if cpj_tot >= tot_dr - 2000:
        cpj_tot = tot_dr - 5000
    close_bal = tot_dr - cpj_tot

    headers = ["Dr Date", "Dr Details", "Dr Fol.", "Dr Amount (R)", "Cr Date", "Cr Details", "Cr Fol.", "Cr Amount (R)"]
    rows = [
        [
            _cell("t0_r0_c0", f"{m_abbr} 01", "given", False),
            _cell("t0_r0_c1", "Balance", "given", False),
            _cell("t0_r0_c2", "b/d", "given", False),
            _cell("t0_r0_c3", str(open_bal), "given", False),
            _cell("t0_r0_c4", f"{m_abbr} {last_d}", "given", False),
            _cell("t0_r0_c5", "", "required", True),
            _cell("t0_r0_c6", "CPJ1", "given", False),
            _cell("t0_r0_c7", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", f"{m_abbr} {last_d}", "given", False),
            _cell("t0_r1_c1", "", "required", True),
            _cell("t0_r1_c2", "CRJ1", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", f"{m_abbr} {last_d}", "given", False),
            _cell("t0_r1_c5", "Balance", "given", False),
            _cell("t0_r1_c6", "c/d", "given", False),
            _cell("t0_r1_c7", "", "required", True),
        ],
        [
            _cell("t0_r2_c0", "", "given", False),
            _cell("t0_r2_c1", "Total", "given", False),
            _cell("t0_r2_c2", "", "given", False),
            _cell("t0_r2_c3", "", "required", True),
            _cell("t0_r2_c4", "", "given", False),
            _cell("t0_r2_c5", "Total", "given", False),
            _cell("t0_r2_c6", "", "given", False),
            _cell("t0_r2_c7", "", "required", True),
        ],
        [
            _cell("t0_r3_c0", f"{next_m[:3]} 01", "given", False),
            _cell("t0_r3_c1", "Balance", "given", False),
            _cell("t0_r3_c2", "b/d", "given", False),
            _cell("t0_r3_c3", "", "required", True),
            _cell("t0_r3_c4", "", "given", False),
            _cell("t0_r3_c5", "", "given", False),
            _cell("t0_r3_c6", "", "given", False),
            _cell("t0_r3_c7", "", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c5": "Total payments",
        "t0_r0_c7": str(cpj_tot),
        "t0_r1_c1": "Total receipts",
        "t0_r1_c3": str(crj_tot),
        "t0_r1_c7": str(close_bal),
        "t0_r2_c3": str(tot_dr),
        "t0_r2_c7": str(tot_dr),
        "t0_r3_c3": str(close_bal),
    }
    cell_hints = {
        "t0_r0_c5": "Credit Bank details for CPJ1: Total payments.",
        "t0_r0_c7": f"CPJ total payments = {cpj_tot}.",
        "t0_r1_c1": "Debit Bank details for CRJ1: Total receipts.",
        "t0_r1_c3": f"CRJ total receipts = {crj_tot}.",
        "t0_r1_c7": f"Balance c/d = {tot_dr} - {cpj_tot} = {close_bal}.",
        "t0_r2_c3": f"Larger side total = {open_bal} + {crj_tot} = {tot_dr}.",
        "t0_r2_c7": f"Both sides must balance to {tot_dr}.",
        "t0_r3_c3": f"Bring Balance b/d down on the Debit side ({close_bal}).",
    }
    prompt = (
        f"Complete and balance the **Bank (B7)** General Ledger T-account for **{biz}** for **{m_name} {yr}** "
        f"(enter digits without spaces or R):\n"
        f"- **Opening Debit balance (`{m_abbr} 01`):** {_fmt_r(open_bal)}\n"
        f"- **CRJ1 Total Receipts:** {_fmt_r(crj_tot)}\n"
        f"- **CPJ1 Total Payments:** {_fmt_r(cpj_tot)}"
    )
    md = (
        "| Dr Date | Dr Details | Fol. | Dr Amount | Cr Date | Cr Details | Fol. | Cr Amount |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {m_abbr} 01 | Balance | b/d | {open_bal} | {m_abbr} {last_d} | **Total payments** | CPJ1 | **{cpj_tot}** |\n"
        f"| {m_abbr} {last_d} | **Total receipts** | CRJ1 | **{crj_tot}** | {m_abbr} {last_d} | Balance | c/d | **{close_bal}** |\n"
        f"| | Total | | **{tot_dr}** | | Total | | **{tot_dr}** |\n"
        f"| {next_m[:3]} 01 | Balance | b/d | **{close_bal}** | | | | |"
    )
    sample = f"Dr Total receipts {crj_tot}; Cr Total payments {cpj_tot}; Total {tot_dr}; Balance c/d & b/d = {close_bal}"
    worked = f"**Bank (B7) Balanced T-Account Memorandum** [8 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_15",
        subskill="15_bank_t_account_balancing_favourable_debit",
        title="Balance Bank (B7) T-Account (Favourable Debit Balance)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Receipts increase Debit; Payments decrease Credit; Balance c/d closes the smaller side and opens as b/d on the larger side.",
            "tier_2": f"Dr total = {open_bal} + {crj_tot} = {tot_dr}; Closing Balance = {tot_dr} - {cpj_tot} = {close_bal}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total receipts Dr {crj_tot} & Total payments Cr {cpj_tot}", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Balance c/d and b/d = {close_bal}, Totals = {tot_dr}", "marks": 4, "editable": True},
        ],
        misconception_tags=["putting_balance_bd_on_smaller_side", "reversing_crj_cpj_sides_in_bank"],
    )


def arch_16_bank_t_account_overdraft_reversal_credit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _, next_m, _ = rng.choice(MONTH_YEARS)
    open_dr = rng.randint(8, 22) * 1000
    crj_tot = rng.randint(10, 28) * 500
    tot_dr = open_dr + crj_tot
    overdraft = rng.randint(4, 18) * 500
    cpj_tot = tot_dr + overdraft

    expected = str(overdraft)
    prompt = (
        f"On 01 {m_name} {yr}, **{biz}** opened with a favourable Bank balance of **{_fmt_r(open_bal := open_dr)}**. "
        f"During {m_name}, **CRJ Total receipts = {_fmt_r(crj_tot)}** and **CPJ Total payments = {_fmt_r(cpj_tot)}**.\n\n"
        f"Calculate the **Bank Overdraft** closing balance (`Balance b/d` on the Credit side on 01 {next_m}).\n"
        f"*(Enter positive digits without spaces or R.)*"
    )
    worked = (
        f"**Bank Overdraft Calculation** [3 marks]\n\n"
        f"- Debit side (Available Cash): `{_fmt_r(open_bal)} + {_fmt_r(crj_tot)} = {_fmt_r(tot_dr)}`\n"
        f"- Credit side (Total Payments): `{_fmt_r(cpj_tot)}`\n"
        f"- Credit side exceeds Debit side -> **Bank Overdraft** = `{_fmt_r(cpj_tot)} - {_fmt_r(tot_dr)} = {_fmt_r(overdraft)}`\n"
        f"- (`Balance c/d` sits on Debit side; `Balance b/d` opens on Credit side on 01 {next_m}) -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_16",
        subskill="16_bank_t_account_overdraft_reversal_credit",
        title="Bank Overdraft Closing Balance Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "When CPJ total payments exceed (Opening Debit + CRJ receipts), the larger total is on the Credit side.",
            "tier_2": f"Overdraft = {_fmt_r(cpj_tot)} - ({_fmt_r(open_bal)} + {_fmt_r(crj_tot)}).",
            "tier_3": f"Bank Overdraft = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Totals Debit cash = {_fmt_r(tot_dr)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Subtracts from {_fmt_r(cpj_tot)} to find Credit Overdraft = {_fmt_r(overdraft)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_bank_always_has_debit_balance"],
    )


def arch_17_bank_t_account_starting_in_overdraft(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _, next_m, _ = rng.choice(MONTH_YEARS)
    open_od = rng.randint(10, 28) * 500
    cpj_tot = rng.randint(8, 24) * 500
    crj_tot = open_od + cpj_tot + rng.randint(6, 25) * 500
    close_fav = crj_tot - (open_od + cpj_tot)
    expected = str(close_fav)

    prompt = (
        f"On 01 {m_name} {yr}, **{biz}** begins in **Bank Overdraft** (`Balance b/d` on the **Credit** side = **{_fmt_r(open_od)}**). "
        f"During {m_name}, **CRJ Total receipts = {_fmt_r(crj_tot)}** and **CPJ Total payments = {_fmt_r(cpj_tot)}**.\n\n"
        f"Calculate the new favourable **Debit closing balance (`Balance b/d` on 01 {next_m})**.\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Recovery from Bank Overdraft** [3 marks]\n\n"
        f"- Debit side (`CRJ Total receipts`): `{_fmt_r(crj_tot)}`\n"
        f"- Credit side (`Opening Overdraft + CPJ payments`): `{_fmt_r(open_od)} + {_fmt_r(cpj_tot)} = {_fmt_r(open_od + cpj_tot)}`\n"
        f"- Closing favourable Debit balance: `{_fmt_r(crj_tot)} - {_fmt_r(open_od + cpj_tot)} = {_fmt_r(close_fav)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_17",
        subskill="17_bank_t_account_starting_in_overdraft",
        title="Bank T-Account Starting with Credit Overdraft",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "An opening overdraft starts on the Credit side alongside CPJ Total payments!",
            "tier_2": f"Favourable Closing Balance = {_fmt_r(crj_tot)} - ({_fmt_r(open_od)} + {_fmt_r(cpj_tot)}).",
            "tier_3": f"Closing Debit balance = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Places opening overdraft ({_fmt_r(open_od)}) on Credit side with CPJ", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Net favourable Debit balance = {_fmt_r(close_fav)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_opening_overdraft_to_debit_receipts"],
    )


def arch_18_trading_stock_t_account_complete_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, m_abbr, next_m, _ = rng.choice(MONTH_YEARS)
    open_stock = rng.randint(15, 55) * 500
    pur_stock = rng.randint(12, 42) * 500
    tot_avail = open_stock + pur_stock
    cos = rng.randint(10, 35) * 500
    if cos >= tot_avail - 2000:
        cos = tot_avail - 6000
    close_stock = tot_avail - cos

    headers = ["Dr Date", "Dr Details", "Dr Fol.", "Dr Amount (R)", "Cr Date", "Cr Details", "Cr Fol.", "Cr Amount (R)"]
    rows = [
        [
            _cell("t0_r0_c0", f"{m_abbr} 01", "given", False),
            _cell("t0_r0_c1", "Balance", "given", False),
            _cell("t0_r0_c2", "b/d", "given", False),
            _cell("t0_r0_c3", str(open_stock), "given", False),
            _cell("t0_r0_c4", f"{m_abbr} {last_d}", "given", False),
            _cell("t0_r0_c5", "", "required", True),
            _cell("t0_r0_c6", "CRJ1", "given", False),
            _cell("t0_r0_c7", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", f"{m_abbr} {last_d}", "given", False),
            _cell("t0_r1_c1", "", "required", True),
            _cell("t0_r1_c2", "CPJ1", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", f"{m_abbr} {last_d}", "given", False),
            _cell("t0_r1_c5", "Balance", "given", False),
            _cell("t0_r1_c6", "c/d", "given", False),
            _cell("t0_r1_c7", "", "required", True),
        ],
        [
            _cell("t0_r2_c0", "", "given", False),
            _cell("t0_r2_c1", "Total", "given", False),
            _cell("t0_r2_c2", "", "given", False),
            _cell("t0_r2_c3", "", "required", True),
            _cell("t0_r2_c4", "", "given", False),
            _cell("t0_r2_c5", "Total", "given", False),
            _cell("t0_r2_c6", "", "given", False),
            _cell("t0_r2_c7", "", "required", True),
        ],
        [
            _cell("t0_r3_c0", f"{next_m[:3]} 01", "given", False),
            _cell("t0_r3_c1", "Balance", "given", False),
            _cell("t0_r3_c2", "b/d", "given", False),
            _cell("t0_r3_c3", "", "required", True),
            _cell("t0_r3_c4", "", "given", False),
            _cell("t0_r3_c5", "", "given", False),
            _cell("t0_r3_c6", "", "given", False),
            _cell("t0_r3_c7", "", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c5": "Cost of Sales",
        "t0_r0_c7": str(cos),
        "t0_r1_c1": "Bank",
        "t0_r1_c3": str(pur_stock),
        "t0_r1_c7": str(close_stock),
        "t0_r2_c3": str(tot_avail),
        "t0_r2_c7": str(tot_avail),
        "t0_r3_c3": str(close_stock),
    }
    cell_hints = {
        "t0_r0_c5": "Contra account for stock sold from CRJ1: Cost of Sales.",
        "t0_r0_c7": f"Cost of Sales amount = {cos}.",
        "t0_r1_c1": "Contra account for stock purchased from CPJ1: Bank.",
        "t0_r1_c3": f"CPJ Trading Stock purchases = {pur_stock}.",
        "t0_r1_c7": f"Closing stock c/d = {tot_avail} - {cos} = {close_stock}.",
        "t0_r2_c3": f"Debit total = {open_stock} + {pur_stock} = {tot_avail}.",
        "t0_r2_c7": f"Total = {tot_avail}.",
        "t0_r3_c3": f"Opening next-month stock Balance b/d = {close_stock}.",
    }
    prompt = (
        f"Post and balance the **Trading Stock (B6)** T-account of **{biz}** for **{m_name} {yr}** "
        f"(enter digits without spaces or R):\n"
        f"- **Opening Stock (`{m_abbr} 01`):** {_fmt_r(open_stock)}\n"
        f"- **CPJ1 Trading Stock column total:** {_fmt_r(pur_stock)}\n"
        f"- **CRJ1 Cost of Sales column total:** {_fmt_r(cos)}"
    )
    md = (
        "| Dr Date | Dr Details | Fol. | Dr Amount | Cr Date | Cr Details | Fol. | Cr Amount |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {m_abbr} 01 | Balance | b/d | {open_stock} | {m_abbr} {last_d} | **Cost of Sales** | CRJ1 | **{cos}** |\n"
        f"| {m_abbr} {last_d} | **Bank** | CPJ1 | **{pur_stock}** | {m_abbr} {last_d} | Balance | c/d | **{close_stock}** |\n"
        f"| | Total | | **{tot_avail}** | | Total | | **{tot_avail}** |\n"
        f"| {next_m[:3]} 01 | Balance | b/d | **{close_stock}** | | | | |"
    )
    sample = f"Dr Bank {pur_stock}; Cr Cost of Sales {cos}; Total {tot_avail}; Closing Balance c/d & b/d = {close_stock}"
    worked = f"**Trading Stock (B6) Balanced T-Account Memorandum** [8 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_18",
        subskill="18_trading_stock_t_account_complete_table",
        title="Post & Balance Trading Stock (B6) T-Account",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Stock purchases (CPJ Bank) Debit Trading Stock; stock sold (CRJ Cost of Sales) Credits Trading Stock.",
            "tier_2": f"Closing stock = {open_stock} + {pur_stock} - {cos} = {close_stock}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr Bank {pur_stock} & Cr Cost of Sales {cos}", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Balance c/d & b/d = {close_stock}, Totals = {tot_avail}", "marks": 4, "editable": True},
        ],
        misconception_tags=["putting_sales_instead_of_cost_of_sales_in_trading_stock"],
    )


def arch_19_trading_stock_missing_purchases_or_cos_solve(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    open_s = rng.randint(18, 48) * 500
    pur_s = rng.randint(12, 36) * 500
    cos_s = rng.randint(10, 32) * 500
    while cos_s >= open_s + pur_s - 3000:
        cos_s -= 4000
    close_s = open_s + pur_s - cos_s
    ask_pur = rng.choice([True, False])

    if ask_pur:
        expected = str(pur_s)
        prompt = (
            f"The **Trading Stock (B6)** ledger of **{biz}** shows:\n"
            f"- Opening Balance b/d: **{_fmt_r(open_s)}**\n"
            f"- CRJ Cost of Sales (Credit): **{_fmt_r(cos_s)}**\n"
            f"- Closing Balance b/d: **{_fmt_r(close_s)}**\n\n"
            f"Calculate the missing **CPJ Trading Stock purchases (`Bank`)** for the month.\n*(Enter digits without spaces or R.)*"
        )
        worked = (
            f"**Solve Missing Stock Purchases** [3 marks]\n\n"
            f"`Opening ({_fmt_r(open_s)}) + Purchases = Cost of Sales ({_fmt_r(cos_s)}) + Closing ({_fmt_r(close_s)})`\n"
            f"`Purchases = {_fmt_r(cos_s + close_s)} - {_fmt_r(open_s)} = {_fmt_r(pur_s)}` -> Answer: `{expected}`"
        )
        t2 = f"Total Credit side = {_fmt_r(cos_s + close_s)}; subtract Opening Balance ({_fmt_r(open_s)})."
    else:
        expected = str(cos_s)
        prompt = (
            f"The **Trading Stock (B6)** ledger of **{biz}** shows:\n"
            f"- Opening Balance b/d: **{_fmt_r(open_s)}**\n"
            f"- CPJ Cash Purchases (`Bank` Debit): **{_fmt_r(pur_s)}**\n"
            f"- Closing Balance b/d: **{_fmt_r(close_s)}**\n\n"
            f"Calculate the **CRJ Cost of Sales** credited out during the month.\n*(Enter digits without spaces or R.)*"
        )
        worked = (
            f"**Solve Missing Cost of Sales from Trading Stock** [3 marks]\n\n"
            f"`Total Stock Available (Dr) = {_fmt_r(open_s)} + {_fmt_r(pur_s)} = {_fmt_r(open_s + pur_s)}`\n"
            f"`Cost of Sales = Total Available - Closing Stock = {_fmt_r(open_s + pur_s)} - {_fmt_r(close_s)} = {_fmt_r(cos_s)}` -> Answer: `{expected}`"
        )
        t2 = f"Total Debit available = {_fmt_r(open_s + pur_s)}; subtract Closing Stock ({_fmt_r(close_s)})."

    return _build_short(
        rng,
        qid_prefix="g9_gl_19",
        subskill="19_trading_stock_missing_purchases_or_cos_solve",
        title="Solve Missing Movement in Trading Stock T-Account",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "In Trading Stock (B6), Total Debits (Opening + Purchases) always equal Total Credits (Cost of Sales + Closing).",
            "tier_2": t2,
            "tier_3": f"Answer: {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correctly balances T-account sides to find {expected}", "marks": 3, "editable": True},
        ],
        misconception_tags=["putting_sales_instead_of_cost_of_sales_in_trading_stock"],
    )


def arch_20_capital_and_drawings_t_accounts_effect_on_equity(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cap_open = rng.randint(150, 320) * 1000
    cap_add = rng.randint(25, 85) * 1000
    draw_open = rng.randint(3, 12) * 500
    draw_add = rng.randint(2, 10) * 400
    cap_tot = cap_open + cap_add
    draw_tot = draw_open + draw_add
    net_eq = cap_tot - draw_tot

    headers = ["Account", "Opening b/d (R)", "Monthly Movement (Journal)", "Closing Balance (R)", "Normal Side (`Debit` / `Credit`)"]
    rows = [
        [
            _cell("t0_r0_c0", "Capital (B1)", "given", False),
            _cell("t0_r0_c1", str(cap_open), "given", False),
            _cell("t0_r0_c2", f"+{cap_add} (CRJ Bank)", "given", False),
            _cell("t0_r0_c3", "", "required", True),
            _cell("t0_r0_c4", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "Drawings (B2)", "given", False),
            _cell("t0_r1_c1", str(draw_open), "given", False),
            _cell("t0_r1_c2", f"+{draw_add} (CPJ Bank)", "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
        ],
        [
            _cell("t0_r2_c0", "Net Owner's Capital (Capital - Drawings)", "given", False),
            _cell("t0_r2_c1", "-", "given", False),
            _cell("t0_r2_c2", "-", "given", False),
            _cell("t0_r2_c3", "", "required", True),
            _cell("t0_r2_c4", "Credit", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c3": str(cap_tot),
        "t0_r0_c4": "Credit",
        "t0_r1_c3": str(draw_tot),
        "t0_r1_c4": "Debit",
        "t0_r2_c3": str(net_eq),
    }
    cell_hints = {
        "t0_r0_c3": f"Capital closing = {cap_open} + {cap_add} = {cap_tot}.",
        "t0_r0_c4": "Capital belongs to CLIC -> Credit.",
        "t0_r1_c3": f"Drawings closing = {draw_open} + {draw_add} = {draw_tot}.",
        "t0_r1_c4": "Drawings belongs to DEAD -> Debit.",
        "t0_r2_c3": f"Net Owner's Capital = {cap_tot} - {draw_tot} = {net_eq}.",
    }
    prompt = (
        f"Update the **Capital (B1)** and **Drawings (B2)** ledger summaries for **{biz}** and determine Net Owner's Capital "
        f"(enter digits without spaces or R)."
    )
    md = (
        "| Account | Opening b/d | Monthly Movement | Closing Balance | Normal Side |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| Capital (B1) | {_fmt_r(cap_open)} | +{_fmt_r(cap_add)} (CRJ Bank) | **{_fmt_r(cap_tot)}** | **Credit** |\n"
        f"| Drawings (B2) | {_fmt_r(draw_open)} | +{_fmt_r(draw_add)} (CPJ Bank) | **{_fmt_r(draw_tot)}** | **Debit** |\n"
        f"| Net Owner's Capital | - | - | **{_fmt_r(net_eq)}** | Credit |"
    )
    sample = f"Capital Cr {cap_tot}; Drawings Dr {draw_tot}; Net Owner's Capital {net_eq}"
    worked = f"**Capital & Drawings Ledger Memorandum** [5 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_20",
        subskill="20_capital_and_drawings_t_accounts_effect_on_equity",
        title="Capital & Drawings General Ledger Summary",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Capital increases on Credit; Drawings increase on Debit and reduce Net Owner's Capital.",
            "tier_2": f"Capital = {cap_tot}; Drawings = {draw_tot}; Net = {cap_tot} - {draw_tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Capital {cap_tot} Credit", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Drawings {draw_tot} Debit", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Net Capital {net_eq}", "marks": 1, "editable": True},
        ],
        misconception_tags=["adding_drawings_to_capital"],
    )


def arch_21_fixed_asset_t_account_equipment_and_vehicles(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    acc, fol = rng.choice([("Equipment", "B5"), ("Vehicles", "B4"), ("Land and Buildings", "B3")])
    open_b = rng.randint(25, 95) * 1000
    add_1 = rng.randint(6, 28) * 500
    add_2 = rng.randint(4, 16) * 500
    total_b = open_b + add_1 + add_2
    expected = str(total_b)

    prompt = (
        f"In **{biz}**'s General Ledger, **{acc} ({fol})** opens on the **Debit** side with **{_fmt_r(open_b)}**. "
        f"During the month, two CPJ Sundry entries record new purchases (`Details: Bank`) of **{_fmt_r(add_1)}** and **{_fmt_r(add_2)}**.\n\n"
        f"Calculate the closing **Debit balance** of **{acc} ({fol})**.\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Fixed Asset ({acc}) Closing Balance** [2 marks]\n\n"
        f"- Opening Balance b/d (Dr): `{_fmt_r(open_b)}`\n"
        f"- Add CPJ Bank purchases (Dr): `+{_fmt_r(add_1)} + {_fmt_r(add_2)}`\n"
        f"- Closing Debit Balance = `{_fmt_r(total_b)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_21",
        subskill="21_fixed_asset_t_account_equipment_and_vehicles",
        title=f"Update Fixed Asset T-Account ({acc})",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": f"{acc} is an Asset (DEAD -> Debit increases).",
            "tier_2": f"Sum all Debit entries: {_fmt_r(open_b)} + {_fmt_r(add_1)} + {_fmt_r(add_2)}.",
            "tier_3": f"Closing balance = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sums Debit asset balance = {_fmt_r(total_b)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_asset_purchases_from_balance"],
    )


def arch_22_visual_t_account_balancing_interpretation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, last_d, m_abbr, _, _ = rng.choice(MONTH_YEARS)
    open_b = rng.randint(18, 48) * 500
    pur_b = rng.randint(10, 32) * 500
    cos_b = rng.randint(8, 28) * 500
    close_b = open_b + pur_b - cos_b
    expected = str(close_b)

    svg = _t_account_svg(
        f"Trading Stock (B6) — {biz}",
        [
            (f"{m_abbr} 01", "Balance b/d", f"{open_b:,}".replace(",", " ")),
            (f"{m_abbr} {last_d}", "Bank (CPJ1)", f"{pur_b:,}".replace(",", " ")),
        ],
        [
            (f"{m_abbr} {last_d}", "Cost of Sales (CRJ1)", f"{cos_b:,}".replace(",", " ")),
            (f"{m_abbr} {last_d}", "Balance c/d", "?"),
        ],
    )
    prompt = (
        f"Inspect the **Trading Stock (B6)** T-account illustrated above for **{biz}** (**{m_name} {yr}**).\n\n"
        f"Calculate the missing **`Balance c/d`** marked **`?`** on the Credit side.\n"
        f"*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**T-Account Missing Balance c/d** [3 marks]\n\n"
        f"- Debit Total = `{_fmt_r(open_b)} + {_fmt_r(pur_b)} = {_fmt_r(open_b + pur_b)}`\n"
        f"- Subtract Credit Cost of Sales = `{_fmt_r(open_b + pur_b)} - {_fmt_r(cos_b)} = {_fmt_r(close_b)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_22",
        subskill="22_visual_t_account_balancing_interpretation",
        title="Calculate Missing T-Account Balance c/d",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Add the Debit column total, then subtract the Credit side entry.",
            "tier_2": f"Balance c/d = ({_fmt_r(open_b)} + {_fmt_r(pur_b)}) - {_fmt_r(cos_b)}.",
            "tier_3": f"Balance c/d = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Derives Balance c/d = {_fmt_r(close_b)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["t_account_balancing_arithmetic_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_23_visual_crj_to_trading_stock_and_cos_diagram(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cos_amt = rng.randint(12, 44) * 500
    sp_amt = cos_amt * 150 // 100
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 165" width="580" height="165">'
        '<rect x="4" y="4" width="572" height="157" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="290" y="24" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">CRJ Cost of Sales Posting — {biz}</text>'
        '<rect x="18" y="42" width="165" height="92" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>'
        '<text x="100" y="64" font-size="11" font-weight="bold" text-anchor="middle" fill="#075985">CRJ Cost of Sales Col.</text>'
        f'<text x="100" y="88" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{_fmt_r(cos_amt)}</text>'
        f'<text x="100" y="110" font-size="9.5" text-anchor="middle" fill="#475569">(Sales col: {_fmt_r(sp_amt)})</text>'
        '<rect x="220" y="42" width="160" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        f'<text x="300" y="61" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#92400e">Dr Cost of Sales (N2)</text>'
        f'<text x="300" y="77" font-size="10" text-anchor="middle" fill="#0f172a">Details: ? | {_fmt_r(cos_amt)}</text>'
        '<rect x="400" y="42" width="162" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        f'<text x="481" y="61" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#166534">Cr Trading Stock (B6)</text>'
        f'<text x="481" y="77" font-size="10" text-anchor="middle" fill="#0f172a">Details: ? | {_fmt_r(cos_amt)}</text>'
        '<text x="390" y="116" font-size="10.5" font-style="italic" text-anchor="middle" fill="#475569">Note: Bank T-account is NOT touched by Cost of Sales.</text>'
        '</svg>'
    )
    prompt = (
        f"Study the CRJ Cost of Sales posting flow above for **{biz}** (**Cost of Sales = {_fmt_r(cos_amt)}**).\n\n"
        f"Which pair of **`Details`** labels correctly replaces the two **`?`** placeholders in **Cost of Sales (N2)** and **Trading Stock (B6)**?"
    )
    correct = "Debit Cost of Sales writes Details 'Trading Stock'; Credit Trading Stock writes Details 'Cost of Sales'."
    distractors = [
        "Debit Cost of Sales writes Details 'Bank'; Credit Trading Stock writes Details 'Sales'.",
        "Both accounts write 'Total receipts' in Details because the figure originates in the CRJ.",
        "Debit Cost of Sales writes 'Cost of Sales' and Credit Trading Stock writes 'Trading Stock'.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_gl_23",
        subskill="23_visual_crj_to_trading_stock_and_cos_diagram",
        title="Contra Details in Cost of Sales & Trading Stock",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The contra-detail rule requires writing the **name of the opposite account**: inside **Cost of Sales (Dr {_fmt_r(cos_amt)})** write **`Trading Stock`**, "
            f"and inside **Trading Stock (Cr {_fmt_r(cos_amt)})** write **`Cost of Sales`**."
        ),
        hints={
            "tier_1": "Each ledger entry writes the name of the OTHER account involved in the double entry.",
            "tier_2": "Cost of Sales <-> Trading Stock (never Bank, never Sales).",
            "tier_3": correct,
        },
        misconception_tags=["posting_cost_of_sales_to_bank"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_24_nominal_account_totaling_sales_and_cost_of_sales(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales_open = rng.randint(20, 60) * 500
    sales_crj = rng.randint(15, 45) * 500
    cos_open = sales_open * 100 // 125
    cos_crj = sales_crj * 100 // 125
    sales_tot = sales_open + sales_crj
    cos_tot = cos_open + cos_crj
    gp = sales_tot - cos_tot

    headers = ["Nominal Account", "Opening b/d (R)", "Current Month CRJ (R)", "Closing Total (R)", "Column (`Debit` / `Credit`)"]
    rows = [
        [
            _cell("t0_r0_c0", "Sales (N1)", "given", False),
            _cell("t0_r0_c1", str(sales_open), "given", False),
            _cell("t0_r0_c2", str(sales_crj), "given", False),
            _cell("t0_r0_c3", "", "required", True),
            _cell("t0_r0_c4", "", "required", True),
        ],
        [
            _cell("t0_r1_c0", "Cost of Sales (N2)", "given", False),
            _cell("t0_r1_c1", str(cos_open), "given", False),
            _cell("t0_r1_c2", str(cos_crj), "given", False),
            _cell("t0_r1_c3", "", "required", True),
            _cell("t0_r1_c4", "", "required", True),
        ],
        [
            _cell("t0_r2_c0", "Cumulative Gross Profit", "given", False),
            _cell("t0_r2_c1", "-", "given", False),
            _cell("t0_r2_c2", "-", "given", False),
            _cell("t0_r2_c3", "", "required", True),
            _cell("t0_r2_c4", "Sales - Cost of Sales", "given", False),
        ],
    ]
    correct_map = {
        "t0_r0_c3": str(sales_tot),
        "t0_r0_c4": "Credit",
        "t0_r1_c3": str(cos_tot),
        "t0_r1_c4": "Debit",
        "t0_r2_c3": str(gp),
    }
    cell_hints = {
        "t0_r0_c3": f"Total Sales = {sales_open} + {sales_crj} = {sales_tot}.",
        "t0_r0_c4": "Sales is Income (Credit).",
        "t0_r1_c3": f"Total Cost of Sales = {cos_open} + {cos_crj} = {cos_tot}.",
        "t0_r1_c4": "Cost of Sales is Expense (Debit).",
        "t0_r2_c3": f"Gross Profit = {sales_tot} - {cos_tot} = {gp}.",
    }
    prompt = (
        f"Total the **Sales (N1)** and **Cost of Sales (N2)** Nominal ledger accounts for **{biz}** "
        f"and compute the cumulative Gross Profit (enter digits without spaces or R)."
    )
    md = (
        "| Nominal Account | Opening b/d | Current Month CRJ | Closing Total | Side |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| Sales (N1) | {_fmt_r(sales_open)} | {_fmt_r(sales_crj)} | **{_fmt_r(sales_tot)}** | **Credit** |\n"
        f"| Cost of Sales (N2) | {_fmt_r(cos_open)} | {_fmt_r(cos_crj)} | **{_fmt_r(cos_tot)}** | **Debit** |\n"
        f"| Cumulative Gross Profit | - | - | **{_fmt_r(gp)}** | Sales - Cost of Sales |"
    )
    sample = f"Sales Cr {sales_tot}; Cost of Sales Dr {cos_tot}; Gross Profit = {gp}"
    worked = f"**Nominal Trading Accounts Memorandum** [5 marks]\n\n{md}"
    return _build_table(
        rng,
        qid_prefix="g9_gl_24",
        subskill="24_nominal_account_totaling_sales_and_cost_of_sales",
        title="Total Nominal Trading Accounts & Gross Profit",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Nominal accounts simply add opening b/d plus current month CRJ entries on their active side.",
            "tier_2": f"Sales Cr = {sales_tot}; Cost of Sales Dr = {cos_tot}; Gross Profit = {sales_tot} - {cos_tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sales total {sales_tot} Credit", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Cost of Sales total {cos_tot} Debit", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Gross Profit = {gp}", "marks": 1, "editable": True},
        ],
        misconception_tags=["crj_posting_side_reversal"],
    )


def arch_25_nominal_expense_accounts_multi_sundry_postings(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    acc, fol = rng.choice([("Stationery", "N7"), ("Water and Electricity", "N11"), ("Vehicle Expense", "N14")])
    open_b = rng.randint(8, 25) * 100
    p1 = rng.randint(2, 9) * 50
    p2 = rng.randint(3, 12) * 50
    tot = open_b + p1 + p2
    expected = str(tot)

    prompt = (
        f"In **{biz}**'s General Ledger, **{acc} ({fol})** has an opening Debit balance (`b/d`) of **{_fmt_r(open_b)}**. "
        f"Two individual CPJ Sundry payments are posted on the 6th (**{_fmt_r(p1)}**) and 18th (**{_fmt_r(p2)}**).\n\n"
        f"Calculate the new cumulative **Debit total** of **{acc} ({fol})**.\n*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**Cumulative Nominal Expense Total ({acc})** [2 marks]\n\n"
        f"- Opening b/d (Dr): `{_fmt_r(open_b)}`\n"
        f"- Day 06 CPJ (`Bank`): `+{_fmt_r(p1)}`\n"
        f"- Day 18 CPJ (`Bank`): `+{_fmt_r(p2)}`\n"
        f"- Total Debit balance = `{_fmt_r(tot)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_gl_25",
        subskill="25_nominal_expense_accounts_multi_sundry_postings",
        title=f"Total Multi-Entry Nominal Expense ({acc})",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Each dated Sundry CPJ expense adds onto the Debit side.",
            "tier_2": f"Sum {_fmt_r(open_b)} + {_fmt_r(p1)} + {_fmt_r(p2)}.",
            "tier_3": f"Total = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Accurate cumulative Debit total = {_fmt_r(tot)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_opening_nominal_balance"],
    )


BUILDERS_01_25 = {
    "01_general_ledger_heading_and_date_rules": arch_01_general_ledger_heading_and_date_rules,
    "02_analysis_total_vs_sundry_individual_posting": arch_02_analysis_total_vs_sundry_individual_posting,
    "03_dead_clic_classification_trading_sole_trader_table": arch_03_dead_clic_classification_trading_sole_trader_table,
    "04_folio_referencing_journals_and_ledger": arch_04_folio_referencing_journals_and_ledger,
    "05_crj_total_receipts_to_bank_details_rule": arch_05_crj_total_receipts_to_bank_details_rule,
    "06_crj_sales_contra_posting_rule": arch_06_crj_sales_contra_posting_rule,
    "07_crj_cost_of_sales_to_trading_stock_posting": arch_07_crj_cost_of_sales_to_trading_stock_posting,
    "08_crj_sundry_capital_and_rent_income_posting": arch_08_crj_sundry_capital_and_rent_income_posting,
    "09_crj_full_posting_summary_table": arch_09_crj_full_posting_summary_table,
    "10_cpj_total_payments_to_bank_credit_posting": arch_10_cpj_total_payments_to_bank_credit_posting,
    "11_cpj_trading_stock_purchases_debit_posting": arch_11_cpj_trading_stock_purchases_debit_posting,
    "12_cpj_expenses_wages_stationery_packing_posting": arch_12_cpj_expenses_wages_stationery_packing_posting,
    "13_cpj_sundry_drawings_and_equipment_posting": arch_13_cpj_sundry_drawings_and_equipment_posting,
    "14_cpj_full_posting_summary_table": arch_14_cpj_full_posting_summary_table,
    "15_bank_t_account_balancing_favourable_debit": arch_15_bank_t_account_balancing_favourable_debit,
    "16_bank_t_account_overdraft_reversal_credit": arch_16_bank_t_account_overdraft_reversal_credit,
    "17_bank_t_account_starting_in_overdraft": arch_17_bank_t_account_starting_in_overdraft,
    "18_trading_stock_t_account_complete_table": arch_18_trading_stock_t_account_complete_table,
    "19_trading_stock_missing_purchases_or_cos_solve": arch_19_trading_stock_missing_purchases_or_cos_solve,
    "20_capital_and_drawings_t_accounts_effect_on_equity": arch_20_capital_and_drawings_t_accounts_effect_on_equity,
    "21_fixed_asset_t_account_equipment_and_vehicles": arch_21_fixed_asset_t_account_equipment_and_vehicles,
    "22_visual_t_account_balancing_interpretation": arch_22_visual_t_account_balancing_interpretation,
    "23_visual_crj_to_trading_stock_and_cos_diagram": arch_23_visual_crj_to_trading_stock_and_cos_diagram,
    "24_nominal_account_totaling_sales_and_cost_of_sales": arch_24_nominal_account_totaling_sales_and_cost_of_sales,
    "25_nominal_expense_accounts_multi_sundry_postings": arch_25_nominal_expense_accounts_multi_sundry_postings,
}
