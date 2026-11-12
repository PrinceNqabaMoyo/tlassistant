"""Grade 9 EMS - Credit Transactions (Debtors 2): Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Debtors 2).md
- curriculum_docs/EMS_Gr9/Term 3/9-Credit transactions Debtors (2).md

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "Credit transactions (Debtors 2)"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_debtors_ledger"
CURRICULUM_REFERENCE = "Term 3 > Financial Literacy: Credit Transactions (Debtors 2)"

TRADER_SUFFIXES = [
    "Traders",
    "Stores",
    "Suppliers",
    "Hardware",
    "Wholesalers",
    "Outfitters",
    "Superette",
    "Stationers",
    "Boutique",
    "Distributors",
]

MONTH_DATA = [
    ("August", "2026", "31", "Sep", "1"),
    ("September", "2026", "30", "Oct", "1"),
    ("October", "2026", "31", "Nov", "1"),
    ("November", "2026", "30", "Dec", "1"),
    ("May", "2026", "31", "Jun", "1"),
]

DEBTOR_POOL = [
    ("S. Moore", "D1"),
    ("E. Klopper", "D2"),
    ("P. Ciel", "D3"),
    ("M. Gama", "D4"),
    ("S. Mdaka", "D5"),
    ("J. Tanner", "D6"),
    ("A. Falck", "D7"),
    ("D. Nyathi", "D8"),
]


def fmt_r(amount: int | float) -> str:
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
    return {"1_nudge": hints["tier_1"], "2_concept": hints["tier_2"], "3_breakdown": hints["tier_3"]}


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
        "learning_objective_id": f"lo_g9_dl_{subskill}",
        "concept_id": subskill,
        "concept_group": "debtors_2",
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
        "term": 3,
        "caps_weight_percent": 40,
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
        "diagnostic_tags": ["accounting", "debtors_ledger", "general_ledger"],
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
        "learning_objective_id": f"lo_g9_dl_{subskill}",
        "concept_id": subskill,
        "concept_group": "debtors_2",
        "question_type": "math_short",
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
        "term": 3,
        "caps_weight_percent": 40,
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
        "diagnostic_tags": ["accounting", "debtors_ledger", "general_ledger"],
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
    journal_type: str = "debtors_ledger",
    transactions: Optional[List[str]] = None,
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
        "learning_objective_id": f"lo_g9_dl_{subskill}",
        "concept_id": subskill,
        "concept_group": "debtors_2",
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
        "term": 3,
        "caps_weight_percent": 40,
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
        "diagnostic_tags": ["accounting", "debtors_ledger", "tabular"],
    }
    if transactions:
        q["transactions"] = transactions
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def make_grid_rows(
    data_rows: List[List[str]],
    given_coords: set[Tuple[int, int]] | None = None,
) -> Tuple[List[List[Dict[str, Any]]], Dict[str, str]]:
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


def arch_01_debtors_ledger_vs_general_ledger_purpose(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    n_debtors = rng.randint(18, 45)

    prompt = (
        f"**{biz}** has **{n_debtors}** active credit customers.\n\n"
        "Why does the bookkeeper keep a separate **Debtors Ledger** alongside the **Debtors Control** account in the General Ledger?"
    )
    correct = "The Debtors Ledger tracks each individual debtor's balance on a daily basis, while Debtors Control in the General Ledger summarises the combined total owed by all debtors."
    distractors = [
        "The Debtors Ledger records cash sales, while Debtors Control records monthly salaries paid out in the CPJ.",
        "Debtors Control tracks individual invoice items, while the Debtors Ledger records Capital only.",
        "They duplicate identical bank statements so that Sales and Cost of Sales stay equal.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_01",
        subskill="01_debtors_ledger_vs_general_ledger_purpose",
        title="Subsidiary Debtors Ledger vs General Ledger Control",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Keeping all individual customer accounts inside the General Ledger would clutter it. "
            "Instead, each customer gets an individual **Debtors Ledger (`D1`, `D2`, ...)** account, "
            "while **Debtors Control (`B6`)** holds the overall control total."
        ),
        hints={
            "tier_1": "Think of individual customer detail versus one combined summary control account.",
            "tier_2": "Debtors Ledger = individual accounts (daily); Debtors Control = General Ledger summary (monthly).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_debtors_ledger_and_debtors_control"],
    )


def arch_02_debtors_ledger_3col_column_rules_dr_cr_balance(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL)

    prompt = (
        f"In the 3-column **Debtors Ledger** account of **{debtor} ({fol})** at **{biz}**, "
        "which columns show `Debit (+)` and `Credit (-)` effects, and why?"
    )
    correct = "Debtors are Current Assets: Debit (+) INCREASES what the debtor owes (e.g. DJ credit sales), while Credit (-) DECREASES what they owe (CRJ receipts and DAJ returns)."
    distractors = [
        "Debtors are Liabilities: Credit (+) increases what they owe and Debit (-) decreases their balance.",
        "Both DJ invoices and CRJ receipts enter the Debit (+) column so the running balance always rises.",
        "Debit (+) reduces the balance when cash is paid, and Credit (-) increases the balance on credit sales.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_02",
        subskill="02_debtors_ledger_3col_column_rules_dr_cr_balance",
        title="3-Column Debtors Ledger Debit (+) and Credit (-) Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "A debtor is an **Asset**. Asset accounts increase on the **Debit (+)** side (`Balance = Prev + Debit`) "
            "and decrease on the **Credit (-)** side (`Balance = Prev - Credit`)."
        ),
        hints={
            "tier_1": "Remember the accounting classification of Debtors (Assets vs Liabilities).",
            "tier_2": "Assets carry Debit (+) to increase and Credit (-) to decrease.",
            "tier_3": correct,
        },
        misconception_tags=["reversing_debit_and_credit_in_debtors_ledger"],
    )


def arch_03_debtors_ledger_source_mapping_dj_daj_crj_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    rows_spec = [
        ("DJ (Debtors Journal)", "Duplicate Invoice", "Debit (+)", "Add to Balance"),
        ("DAJ (Debtors Allowance)", "Duplicate Credit Note", "Credit (-)", "Subtract from Balance"),
        ("CRJ (Cash Receipts Journal)", "Duplicate Receipt", "Credit (-)", "Subtract from Balance"),
    ]
    rng.shuffle(rows_spec)
    headers = ["Journal", "Source Document", "Debtors Ledger Column", "Effect on Running Balance"]
    given = {(i, 0) for i in range(3)}
    rows, correct_map = make_grid_rows([list(r) for r in rows_spec], given_coords=given)
    cell_hints = {
        f"t0_r{i}_c1": f"Source doc for {r[0]} is {r[1]}." for i, r in enumerate(rows_spec)
    }
    cell_hints.update({
        f"t0_r{i}_c2": f"{r[0]} enters {r[2]}." for i, r in enumerate(rows_spec)
    })
    cell_hints.update({
        f"t0_r{i}_c3": f"Effect: {r[3]}." for i, r in enumerate(rows_spec)
    })
    prompt = "Complete the **Debtors Ledger Source Mapping** table linking each journal to its source document, column, and balance effect."
    md_rows = "\n".join(f"| {a} | **{b}** | **{c}** | **{d}** |" for a, b, c, d in rows_spec)
    worked = "**Debtors Ledger Source & Posting Rules** [6 marks]\n\n| Journal | Source Doc | Column | Effect |\n| --- | --- | --- | --- |\n" + md_rows
    return build_table(
        rng,
        qid="g9_dl_03",
        subskill="03_debtors_ledger_source_mapping_dj_daj_crj_table",
        title="Map Journals to Debtors Ledger Columns & Effects",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"{a}->{c} ({d})" for a, _, c, d in rows_spec),
        marks=6,
        hints={
            "tier_1": "Credit sales increase debt (Debit +); returns & payments reduce debt (Credit -).",
            "tier_2": "Pair DJ->Invoice->Debit(+), DAJ->Credit Note->Credit(-), CRJ->Receipt->Credit(-).",
            "tier_3": "; ".join(f"{a}: {b} | {c} | {d}" for a, b, c, d in rows_spec),
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{r[0]} mapped cleanly", "marks": 2, "editable": True}
            for i, r in enumerate(rows_spec)
        ],
        misconception_tags=["confusing_dj_daj_crj_ledger_columns"],
        journal_type="mapping_table",
    )


def arch_04_account_rendered_balance_bd_meaning(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL)
    bal = rng.randint(18, 85) * 100
    m_name, yr, _, _, _ = rng.choice(MONTH_DATA)

    prompt = (
        f"On **1 {m_name} {yr}**, the opening line of **{debtor} ({fol})**'s Debtors Ledger account at **{biz}** reads:\n"
        f"`Date: 1 | Details: Account rendered | Fol: b/d | Balance: {fmt_r(bal)}`.\n\n"
        "What does **`Account rendered`** (`b/d`) signify?"
    )
    correct = f"The unpaid balance ({fmt_r(bal)}) brought down from the previous month's statement already rendered to {debtor}."
    distractors = [
        f"A brand-new credit sale of {fmt_r(bal)} made on 1 {m_name} using Duplicate Invoice 1.",
        f"Cash of {fmt_r(bal)} already paid by {debtor} on the 1st of the month in the CRJ.",
        f"A damaged-stock allowance granted to {debtor} in the Debtors Allowance Journal.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_04",
        subskill="04_account_rendered_balance_bd_meaning",
        title="Meaning of Account Rendered (b/d) in Debtors Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "`Account rendered` (`b/d` — brought down) records the **opening balance owed from the prior month**; "
            "because it was billed earlier, it enters directly in the `Balance` column without repeating Debit/Credit."
        ),
        hints={
            "tier_1": "Notice it sits only in the Balance column on Day 1.",
            "tier_2": "`b/d` means brought down from the previous month's closing statement.",
            "tier_3": correct,
        },
        misconception_tags=["treating_opening_balance_as_new_credit_sale"],
    )


def arch_05_debtors_ledger_single_credit_sale_row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    m_name, yr, _, _, _ = rng.choice(MONTH_DATA)
    open_bal = rng.randint(15, 45) * 100
    inv = rng.randint(201, 490)
    sale = rng.randint(8, 26) * 100
    new_bal = open_bal + sale
    day = rng.randint(3, 18)

    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(open_bal)],
        [str(day), f"Invoice {inv}", "DJ", str(sale), "", str(new_bal)],
    ]
    given = {(0, j) for j in range(6)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c0": f"Transaction day is {day}.",
        "t0_r1_c1": f"Write 'Invoice {inv}'.",
        "t0_r1_c2": "Folio from Debtors Journal is 'DJ'.",
        "t0_r1_c3": f"Credit sale enters Debit (+) = {sale}.",
        "t0_r1_c4": "Leave Credit (-) EMPTY on a credit sale.",
        "t0_r1_c5": f"New Balance = {open_bal} + {sale} = {new_bal}.",
    }
    prompt = (
        f"Post the Day {day} credit sale on **Duplicate Invoice {inv}** (**{fmt_r(sale)}**) into the 3-column Debtors Ledger of "
        f"**{debtor} ({fol})** at **{biz}** for **{m_name} {yr}** *(leave unused Credit cell empty; digits only)*."
    )
    worked = (
        f"**Debtors Ledger: {debtor} ({fol}) — Credit Sale Posting** [4 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Account rendered | b/d | | | {open_bal} |\n"
        f"| **{day}** | **Invoice {inv}** | **DJ** | **{sale}** | | **{new_bal}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_05",
        subskill="05_debtors_ledger_single_credit_sale_row_table",
        title="Post Single Credit Sale (DJ) to Debtors Ledger",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Day {day} Invoice {inv} | DJ | Dr {sale} | Bal {new_bal}",
        marks=4,
        hints={
            "tier_1": "Invoices from the DJ go into Debit (+) and ADD to the running balance.",
            "tier_2": f"Details: Invoice {inv}; Fol: DJ; Debit: {sale}; Balance: {open_bal} + {sale}.",
            "tier_3": f"New running balance = {new_bal}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Day {day}, Invoice {inv}, Fol DJ", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Debit (+) = {sale} and Credit empty", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Running Balance = {new_bal}", "marks": 2, "editable": True},
        ],
        misconception_tags=["entering_credit_sale_in_credit_column"],
    )


def arch_06_debtors_ledger_single_credit_note_row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    m_name, yr, _, _, _ = rng.choice(MONTH_DATA)
    bal1 = rng.randint(25, 60) * 100
    cn = rng.randint(25, 79)
    ret = rng.randint(3, 9) * 100
    bal2 = bal1 - ret
    day = rng.randint(8, 22)

    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["5", "Invoice 104", "DJ", str(bal1), "", str(bal1)],
        [str(day), f"Credit Note {cn}", "DAJ", "", str(ret), str(bal2)],
    ]
    given = {(0, j) for j in range(6)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c1": f"Write 'Credit Note {cn}'.",
        "t0_r1_c2": "Folio from Debtors Allowance Journal is 'DAJ'.",
        "t0_r1_c3": "Leave Debit (+) EMPTY.",
        "t0_r1_c4": f"Credit Note enters Credit (-) = {ret}.",
        "t0_r1_c5": f"New Balance = {bal1} - {ret} = {bal2}.",
    }
    prompt = (
        f"On **Day {day} {m_name} {yr}**, **{biz}** issues **Duplicate Credit Note {cn}** for **{fmt_r(ret)}** "
        f"to **{debtor} ({fol})** for damaged stock returned.\n\n"
        "Post Row 2 into the Debtors Ledger below *(leave unused Debit cell empty; digits only)*."
    )
    worked = (
        f"**Debtors Ledger: Credit Note Posting (DAJ)** [4 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 5 | Invoice 104 | DJ | {bal1} | | {bal1} |\n"
        f"| **{day}** | **Credit Note {cn}** | **DAJ** | | **{ret}** | **{bal2}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_06",
        subskill="06_debtors_ledger_single_credit_note_row_table",
        title="Post Single Credit Note (DAJ) to Debtors Ledger",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Day {day} Credit Note {cn} | DAJ | Cr {ret} | Bal {bal2}",
        marks=4,
        hints={
            "tier_1": "Credit Notes reduce what a debtor owes, so they enter Credit (-).",
            "tier_2": f"Details: Credit Note {cn}; Fol: DAJ; Credit: {ret}; Subtract from {bal1}.",
            "tier_3": f"New Balance = {bal1} - {ret} = {bal2}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Credit Note {cn}, Fol DAJ", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Credit (-) = {ret} and Debit empty", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Balance reduced to {bal2}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_credit_note_to_balance_instead_of_subtracting"],
    )


def arch_07_debtors_ledger_single_receipt_row_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    bal1 = rng.randint(30, 75) * 100
    rec = rng.randint(501, 690)
    paid = rng.randint(12, 28) * 100
    bal2 = bal1 - paid
    day = rng.randint(15, 28)

    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(bal1)],
        [str(day), f"Receipt {rec}", "CRJ", "", str(paid), str(bal2)],
    ]
    given = {(0, j) for j in range(6)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c1": f"Write 'Receipt {rec}'.",
        "t0_r1_c2": "Cash receipts come from 'CRJ'.",
        "t0_r1_c4": f"Payment received reduces debtor balance in Credit (-) = {paid}.",
        "t0_r1_c5": f"Balance = {bal1} - {paid} = {bal2}.",
    }
    prompt = (
        f"On **Day {day}**, **{biz}** receives **{fmt_r(paid)}** from **{debtor} ({fol})** in part settlement of account "
        f"and issues **Duplicate Receipt {rec}**.\n\n"
        "Complete Row 2 in the Debtors Ledger below."
    )
    worked = (
        "**Debtors Ledger: Cash Receipt Posting (CRJ)** [4 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Account rendered | b/d | | | {bal1} |\n"
        f"| **{day}** | **Receipt {rec}** | **CRJ** | | **{paid}** | **{bal2}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_07",
        subskill="07_debtors_ledger_single_receipt_row_table",
        title="Post Single Receipt (CRJ) to Debtors Ledger",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Day {day} Receipt {rec} | CRJ | Cr {paid} | Bal {bal2}",
        marks=4,
        hints={
            "tier_1": "When a debtor pays cash/EFT, their debt goes down -> Credit (-) column.",
            "tier_2": f"Details: Receipt {rec}; Fol: CRJ; Credit: {paid}.",
            "tier_3": f"Closing Balance = {bal1} - {paid} = {bal2}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Receipt {rec}, Fol CRJ, Cr {paid}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Balance = {bal2}", "marks": 2, "editable": True},
        ],
        misconception_tags=["debiting_receipts_in_debtors_ledger"],
    )


def arch_08_debtors_ledger_full_account_d1_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, _, _, _ = rng.choice(MONTH_DATA)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    open_bal = rng.randint(10, 28) * 100
    sale = rng.randint(12, 34) * 100
    ret = rng.randint(2, 6) * 100
    rec = rng.randint(8, 20) * 100
    b2 = open_bal + sale
    b3 = b2 - ret
    b4 = b3 - rec
    inv_no = rng.randint(101, 240)
    cn_no = rng.randint(31, 69)
    rec_no = rng.randint(81, 140)

    txns = [
        f"Day 1: Account rendered balance brought forward: {fmt_r(open_bal)}.",
        f"Day 10: Sold goods on credit to {debtor}, {fmt_r(sale)}. Issued duplicate invoice {inv_no} (DJ).",
        f"Day 16: Issued Credit Note {cn_no} to {debtor} for damaged goods returned, {fmt_r(ret)} (DAJ).",
        f"Day 25: Received {fmt_r(rec)} from {debtor} in partial settlement; issued duplicate receipt {rec_no} (CRJ).",
    ]
    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(open_bal)],
        ["10", f"Invoice {inv_no}", "DJ", str(sale), "", str(b2)],
        ["16", f"Credit Note {cn_no}", "DAJ", "", str(ret), str(b3)],
        ["25", f"Receipt {rec_no}", "CRJ", "", str(rec), str(b4)],
    ]
    given = {(0, 0), (0, 1), (0, 2), (0, 5)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c3": f"DJ sale increases debt in Debit (+) = {sale}.",
        "t0_r1_c5": f"Balance = {open_bal} + {sale} = {b2}.",
        "t0_r2_c4": f"DAJ credit note reduces debt in Credit (-) = {ret}.",
        "t0_r2_c5": f"Balance = {b2} - {ret} = {b3}.",
        "t0_r3_c4": f"CRJ receipt reduces debt in Credit (-) = {rec}.",
        "t0_r3_c5": f"Final balance = {b3} - {rec} = {b4}.",
    }
    prompt = (
        f"Complete the 3-column **Debtors Ledger** account for **{debtor} ({fol})** in the books of **{biz}** for **{m_name} {yr}**.\n"
        "*(Enter digits without spaces or R; leave unused Dr/Cr cells blank.)*"
    )
    worked = (
        f"**Debtors Ledger of {biz} — {debtor} ({fol})** [16 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Account rendered | b/d | | | {open_bal} |\n"
        f"| 10 | Invoice {inv_no} | DJ | {sale} | | {b2} |\n"
        f"| 16 | Credit Note {cn_no} | DAJ | | {ret} | {b3} |\n"
        f"| 25 | Receipt {rec_no} | CRJ | | {rec} | **{b4}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_08",
        subskill="08_debtors_ledger_full_account_d1_table",
        title="Complete Full 3-Column Debtors Ledger Account",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Closing balance for {debtor}: R{b4:,} (Debit balance).",
        marks=16,
        hints={
            "tier_1": "Debits (+) increase debtor debt; Credits (-) reduce debtor debt.",
            "tier_2": f"DJ Inv {inv_no} -> Dr {sale}; DAJ CN {cn_no} -> Cr {ret}; CRJ Rec {rec_no} -> Cr {rec}.",
            "tier_3": f"Running balances: {open_bal} -> {b2} -> {b3} -> {b4}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Day 10 Invoice {inv_no} (DJ) Dr {sale}, Bal {b2}", "marks": 5, "editable": True},
            {"id": "mp_2", "desc": f"Day 16 Credit Note {cn_no} (DAJ) Cr {ret}, Bal {b3}", "marks": 5, "editable": True},
            {"id": "mp_3", "desc": f"Day 25 Receipt {rec_no} (CRJ) Cr {rec}, Bal {b4}", "marks": 6, "editable": True},
        ],
        misconception_tags=["putting_returns_or_payments_on_debit_side"],
        transactions=txns,
    )


def arch_09_debtors_ledger_settlement_first_of_month_pattern(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    open_bal = rng.randint(18, 52) * 100
    inv1 = rng.randint(10, 24) * 100
    rec_no = rng.randint(510, 599)
    inv_no = rng.randint(41, 88)
    b_after_pay = 0
    b_final = inv1

    txns = [
        f"Day 01: Account rendered opening balance owed by {debtor}: {fmt_r(open_bal)}.",
        f"Day 01: {debtor} settles last month's account in full on the 1st of the month (Receipt {rec_no}, CRJ).",
        f"Day 14: Sold goods on credit to {debtor} for {fmt_r(inv1)} (Invoice {inv_no}, DJ).",
    ]
    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(open_bal)],
        ["1", f"Receipt {rec_no}", "CRJ", "", str(open_bal), str(b_after_pay)],
        ["14", f"Invoice {inv_no}", "DJ", str(inv1), "", str(b_final)],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, j) for j in range(6)})
    cell_hints = {
        "t0_r1_c4": f"Paying prior month's full balance on Day 1 credits the full {open_bal}.",
        "t0_r1_c5": "After paying the opening balance in full, Balance becomes 0.",
        "t0_r2_c3": f"New credit sale on Day 14 debits {inv1}.",
        "t0_r2_c5": f"Balance rises from 0 to {b_final}.",
    }
    prompt = (
        f"Record **{debtor} ({fol})**'s **first-of-the-month settlement** and subsequent credit purchase in the Debtors Ledger of **{biz}**."
    )
    worked = (
        "**Debtors Ledger — 1st-of-Month Full Settlement Pattern** [6 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Account rendered | b/d | | | {open_bal} |\n"
        f"| 1 | Receipt {rec_no} | CRJ | | {open_bal} | 0 |\n"
        f"| 14 | Invoice {inv_no} | DJ | {inv1} | | **{b_final}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_09",
        subskill="09_debtors_ledger_settlement_first_of_month_pattern",
        title="1st-of-Month Settlement in Debtors Ledger",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Day 1 Cr {open_bal} -> Bal 0; Day 14 Dr {inv1} -> Bal {b_final}",
        marks=6,
        hints={
            "tier_1": "When a debtor settles the previous month's account on the 1st, Credit the entire b/d balance to bring Balance to 0.",
            "tier_2": f"Row 2 credits {open_bal} -> Bal 0; Row 3 debits {inv1} -> Bal {b_final}.",
            "tier_3": f"Balances: {open_bal} -> 0 -> {b_final}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Day 1 Receipt {rec_no} CRJ Cr {open_bal}, Bal 0", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Day 14 Invoice {inv_no} DJ Dr {inv1}, Bal {b_final}", "marks": 3, "editable": True},
        ],
        misconception_tags=["carrying_forward_settled_balance_after_payment"],
        transactions=txns,
    )


def arch_10_debtors_ledger_settlement_in_full_up_to_date_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    open_bal = rng.randint(15, 35) * 100
    s1 = rng.randint(10, 22) * 100
    s2 = rng.randint(8, 18) * 100
    b2 = open_bal + s1
    b3 = b2 + s2
    inv1, inv2, rec_no = rng.randint(701, 740), rng.randint(741, 780), rng.randint(601, 680)

    txns = [
        f"Day 01: Account rendered opening balance: {fmt_r(open_bal)}.",
        f"Day 06: Invoice {inv1} for goods sold on credit, {fmt_r(s1)} (DJ).",
        f"Day 15: Invoice {inv2} for goods sold on credit, {fmt_r(s2)} (DJ).",
        f"Day 24: {debtor} pays the full balance owing UP TO DATE (Receipt {rec_no}, CRJ).",
    ]
    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(open_bal)],
        ["6", f"Invoice {inv1}", "DJ", str(s1), "", str(b2)],
        ["15", f"Invoice {inv2}", "DJ", str(s2), "", str(b3)],
        ["24", f"Receipt {rec_no}", "CRJ", "", str(b3), "0"],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, j) for j in range(6)})
    cell_hints = {
        "t0_r1_c5": f"Balance = {open_bal} + {s1} = {b2}.",
        "t0_r2_c5": f"Total owed before Day 24 payment = {b2} + {s2} = {b3}.",
        "t0_r3_c4": f"Settling in full up to date means paying the full {b3}!",
        "t0_r3_c5": "Full settlement leaves closing Balance = 0.",
    }
    prompt = (
        f"Complete the Debtors Ledger account for **{debtor} ({fol})** at **{biz}** when the debtor settles **in full up to date** on Day 24."
    )
    worked = (
        "**Debtors Ledger — Settlement in Full Up to Date** [8 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Account rendered | b/d | | | {open_bal} |\n"
        f"| 6 | Invoice {inv1} | DJ | {s1} | | {b2} |\n"
        f"| 15 | Invoice {inv2} | DJ | {s2} | | {b3} |\n"
        f"| 24 | Receipt {rec_no} | CRJ | | **{b3}** | **0** |"
    )
    return build_table(
        rng,
        qid="g9_dl_10",
        subskill="10_debtors_ledger_settlement_in_full_up_to_date_table",
        title="Settlement in Full Up to Date in Debtors Ledger",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Full payment on Day 24 = {b3}; Closing Balance = 0.",
        marks=8,
        hints={
            "tier_1": "First update the running balance after BOTH invoices, then pay that entire up-to-date total on Day 24.",
            "tier_2": f"Day 15 Balance = {open_bal} + {s1} + {s2} = {b3}.",
            "tier_3": f"Receipt {rec_no} credits {b3}, leaving Balance 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Day 6 & Day 15 DJ debits bringing balance to {b3}", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Day 24 Receipt {rec_no} credits {b3}, Balance 0", "marks": 4, "editable": True},
        ],
        misconception_tags=["paying_opening_balance_only_when_up_to_date_requested"],
        transactions=txns,
    )


def arch_11_debtors_ledger_part_settlement_with_allowance_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[4:])
    b0 = rng.randint(20, 48) * 100
    paid1 = rng.randint(8, 16) * 100
    b1 = b0 - paid1
    inv1 = rng.randint(10, 22) * 100
    b2 = b1 + inv1
    ret1 = rng.randint(2, 5) * 100
    b3 = b2 - ret1

    headers = ["Date", "Details", "Fol", "Debit (+)", "Credit (-)", "Balance"]
    data_rows = [
        ["1", "Account rendered", "b/d", "", "", str(b0)],
        ["4", "Receipt 555", "CRJ", "", str(paid1), str(b1)],
        ["12", "Invoice 804", "DJ", str(inv1), "", str(b2)],
        ["19", "Credit Note 42", "DAJ", "", str(ret1), str(b3)],
    ]
    given = {(i, 0) for i in range(4)} | {(i, 1) for i in range(4)} | {(i, 2) for i in range(4)} | {(0, 5)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c4": f"Receipt 555 (CRJ) -> Credit (-) = {paid1}.",
        "t0_r1_c5": f"Balance = {b0} - {paid1} = {b1}.",
        "t0_r2_c3": f"Invoice 804 (DJ) -> Debit (+) = {inv1}.",
        "t0_r2_c5": f"Balance = {b1} + {inv1} = {b2}.",
        "t0_r3_c4": f"Credit Note 42 (DAJ) -> Credit (-) = {ret1}.",
        "t0_r3_c5": f"Closing Balance = {b2} - {ret1} = {b3}.",
    }
    prompt = (
        f"Complete the Debit (+), Credit (-), and Balance columns of **{debtor} ({fol})**'s Debtors Ledger account at **{biz}**.\n"
        "*(Enter digits only; leave unused Debit/Credit cells blank.)*"
    )
    worked = (
        f"**Debtors Ledger Running Balance ({debtor})** [6 marks]\n\n"
        "| Date | Details | Fol | Debit (+) | Credit (-) | Balance |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Account rendered | b/d | | | {b0} |\n"
        f"| 4 | Receipt 555 | CRJ | | {paid1} | {b1} |\n"
        f"| 12 | Invoice 804 | DJ | {inv1} | | {b2} |\n"
        f"| 19 | Credit Note 42 | DAJ | | {ret1} | **{b3}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_11",
        subskill="11_debtors_ledger_part_settlement_with_allowance_table",
        title="Calculate Running Balances Across CRJ, DJ & DAJ",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Balances: {b0} -> {b1} -> {b2} -> {b3}",
        marks=6,
        hints={
            "tier_1": "Track the folio carefully: CRJ & DAJ enter Credit (-); DJ enters Debit (+).",
            "tier_2": f"Day 4: {b0}-{paid1}={b1}; Day 12: +{inv1}={b2}; Day 19: -{ret1}={b3}.",
            "tier_3": f"Closing Balance = {b3}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Day 4 Cr {paid1} -> Bal {b1}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Day 12 Dr {inv1} -> Bal {b2}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Day 19 Cr {ret1} -> Bal {b3}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_crj_receipt_instead_of_subtracting"],
    )


def arch_12_debtors_ledger_reverse_to_dj_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 2)
    markup = rng.choice([25, 50])
    cp1, cp2, cp3 = rng.randint(6, 14) * 100, rng.randint(8, 18) * 100, rng.randint(10, 20) * 100
    sp1, sp2, sp3 = [c * (100 + markup) // 100 for c in (cp1, cp2, cp3)]
    inv0 = rng.randint(901, 930)
    receipt_amt = rng.randint(5, 12) * 100

    prompt = (
        f"Study these extracts from the **Debtors Ledger** of **{biz}** (profit mark-up is **{markup}% on cost**):\n\n"
        f"**{debtors[0][0]} ({debtors[0][1]}):**\n"
        f"- Day 03: Invoice {inv0} (DJ) — Debit (+) {fmt_r(sp1)}\n"
        f"- Day 08: Receipt 655 (CRJ) — Credit (-) {fmt_r(receipt_amt)}\n"
        f"- Day 20: Invoice {inv0 + 2} (DJ) — Debit (+) {fmt_r(sp3)}\n\n"
        f"**{debtors[1][0]} ({debtors[1][1]}):**\n"
        f"- Day 11: Invoice {inv0 + 1} (DJ) — Debit (+) {fmt_r(sp2)}\n\n"
        "Reconstruct the **Debtors Journal (DJ)** in strict chronological order *(exclude receipts; digits only)*."
    )
    headers = ["Doc No", "Day", "Debtor", "Fol", "Sales", "Cost of Sales"]
    data_rows = [
        [str(inv0), "3", debtors[0][0], debtors[0][1], str(sp1), str(cp1)],
        [str(inv0 + 1), "11", debtors[1][0], debtors[1][1], str(sp2), str(cp2)],
        [str(inv0 + 2), "20", debtors[0][0], debtors[0][1], str(sp3), str(cp3)],
    ]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c5": f"CoS = {sp1} × 100 / {100 + markup} = {cp1}.",
        "t0_r1_c0": f"Second chronological invoice is {inv0 + 1} (Day 11, {debtors[1][0]}).",
        "t0_r1_c5": f"CoS = {sp2} × 100 / {100 + markup} = {cp2}.",
        "t0_r2_c5": f"CoS = {sp3} × 100 / {100 + markup} = {cp3}.",
    }
    worked = (
        f"**Reconstructed Debtors Journal ({markup}% mark-up)** [9 marks]\n\n"
        "| Doc No | Day | Debtor | Fol | Sales | Cost of Sales |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| {inv0} | 3 | {debtors[0][0]} | {debtors[0][1]} | {sp1} | {cp1} |\n"
        f"| {inv0+1} | 11 | {debtors[1][0]} | {debtors[1][1]} | {sp2} | {cp2} |\n"
        f"| {inv0+2} | 20 | {debtors[0][0]} | {debtors[0][1]} | {sp3} | {cp3} |"
    )
    return build_table(
        rng,
        qid="g9_dl_12",
        subskill="12_debtors_ledger_reverse_to_dj_table",
        title="Reconstruct Debtors Journal from Debtors Ledger",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Inv {inv0} ({sp1}/{cp1}), Inv {inv0+1} ({sp2}/{cp2}), Inv {inv0+2} ({sp3}/{cp3})",
        marks=9,
        hints={
            "tier_1": "Extract ONLY Invoice (DJ) rows from all debtor accounts, sort by date, and compute Cost of Sales.",
            "tier_2": f"Ignore Day 08 Receipt 655 (CRJ). Order Days 3, 11, 20; CoS = SP × 100/{100 + markup}.",
            "tier_3": f"Inv {inv0}: {sp1}/{cp1}; Inv {inv0+1}: {sp2}/{cp2}; Inv {inv0+2}: {sp3}/{cp3}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Excludes CRJ receipt & sorts Days 3, 11, 20", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Accurate Sales & CoS ({cp1}, {cp2}, {cp3})", "marks": 6, "editable": True},
        ],
        misconception_tags=["including_crj_receipts_when_rebuilding_dj"],
        journal_type="dj",
    )


def arch_13_debtors_ledger_find_missing_transaction_amount_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL)
    b0 = rng.randint(30, 75) * 100
    paid = rng.randint(12, 24) * 100
    b_after = b0 - paid

    prompt = (
        f"In the Debtors Ledger account of **{debtor} ({fol})** at **{biz}**, ink smudged one amount:\n"
        f"- **Day 01 (b/d):** Balance = **{fmt_r(b0)}**\n"
        f"- **Day 14 (Receipt 771, CRJ):** Balance drops to **{fmt_r(b_after)}**\n\n"
        "Calculate the missing **Credit (-)** receipt amount on Day 14 [2].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Deduce Missing Credit (-) Receipt** [2 marks]\n\n"
        f"`Receipt = Previous Balance ({fmt_r(b0)}) - New Balance ({fmt_r(b_after)}) = {fmt_r(paid)}` -> Answer: `{paid}`"
    )
    return build_short(
        rng,
        qid="g9_dl_13",
        subskill="13_debtors_ledger_find_missing_transaction_amount_calc",
        title="Deduce Missing Debtors Ledger Transaction Value",
        prompt=prompt,
        expected_answer=str(paid),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "When a receipt lowers the balance, Credit (-) equals Previous Balance minus New Balance.",
            "tier_2": f"Calculate {b0} - {b_after}.",
            "tier_3": f"Missing receipt amount = {paid}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Missing Credit = {paid}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_balances_to_find_missing_payment"],
    )


def arch_14_debtors_ledger_folio_and_date_ordering_error_fix(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL)
    b0 = rng.randint(15, 35) * 100
    amt = rng.randint(5, 12) * 100
    wrong_bal = b0 + amt
    right_bal = b0 - amt

    prompt = (
        f"A bookkeeper at **{biz}** posted Receipt 305 (**{fmt_r(amt)}** from **{debtor}**, folio `{fol}`) "
        f"into the **Debit (+)** column by mistake, turning a {fmt_r(b0)} balance into **{fmt_r(wrong_bal)}**.\n\n"
        f"What is the **corrected** balance owed by **{debtor}**, and how is the ledger entry fixed?"
    )
    correct = f"Move {fmt_r(amt)} from Debit (+) to Credit (-) with folio CRJ so the balance becomes {fmt_r(right_bal)}."
    distractors = [
        f"Keep {fmt_r(amt)} in Debit (+) and change the opening balance to {fmt_r(wrong_bal + amt)}.",
        f"Move {fmt_r(amt)} to Credit (-) and add it to {fmt_r(b0)} to get {fmt_r(wrong_bal)}.",
        f"Delete the opening balance {fmt_r(b0)} so the debtor owes only {fmt_r(amt)}.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_14",
        subskill="14_debtors_ledger_folio_and_date_ordering_error_fix",
        title="Correct Misposted Debit/Credit in Debtors Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Payments received (`CRJ`) **decrease** what a debtor owes. Moving {fmt_r(amt)} to **Credit (-)** "
            f"changes the balance to `{fmt_r(b0)} - {fmt_r(amt)} = {fmt_r(right_bal)}`."
        ),
        hints={
            "tier_1": "Cash paid by a debtor lowers their debt, not increases it.",
            "tier_2": f"Credit {fmt_r(amt)} instead of Debiting it: {b0} - {amt} = {right_bal}.",
            "tier_3": correct,
        },
        misconception_tags=["putting_receipts_on_debit_side_of_debtors_ledger"],
    )


def arch_15_debtors_list_compile_from_3_accounts_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, _, _ = rng.choice(MONTH_DATA)
    debtors = pick_debtors(rng, 3)
    b1 = rng.randint(25, 65) * 100
    b2 = rng.randint(18, 52) * 100
    b3 = rng.randint(12, 40) * 100
    tot = b1 + b2 + b3

    headers = ["Debtor", "Fol", "Closing Balance (R)"]
    data_rows = [
        [debtors[0][0], debtors[0][1], str(b1)],
        [debtors[1][0], debtors[1][1], str(b2)],
        [debtors[2][0], debtors[2][1], str(b3)],
        ["Debtors Control (Total)", "B6", str(tot)],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(i, 0) for i in range(4)} | {(i, 1) for i in range(4)})
    cell_hints = {
        "t0_r0_c2": f"Final balance of {debtors[0][0]} = {b1}.",
        "t0_r1_c2": f"Final balance of {debtors[1][0]} = {b2}.",
        "t0_r2_c2": f"Final balance of {debtors[2][0]} = {b3}.",
        "t0_r3_c2": f"Sum all three individual debtor balances = {tot}.",
    }
    prompt = (
        f"On **{end_d} {m_name} {yr}**, the final balances of **{biz}**'s three Debtors Ledger accounts are:\n"
        f"- **{debtors[0][0]} ({debtors[0][1]}):** {fmt_r(b1)}\n"
        f"- **{debtors[1][0]} ({debtors[1][1]}):** {fmt_r(b2)}\n"
        f"- **{debtors[2][0]} ({debtors[2][1]}):** {fmt_r(b3)}\n\n"
        "Compile the **Debtors List** and calculate the **Debtors Control** total *(digits only)*."
    )
    worked = (
        f"**Debtors List of {biz} on {end_d} {m_name} {yr}** [4 marks]\n\n"
        "| Debtor | Fol | Amount (R) |\n| --- | --- | --- |\n"
        f"| {debtors[0][0]} | {debtors[0][1]} | {b1} |\n"
        f"| {debtors[1][0]} | {debtors[1][1]} | {b2} |\n"
        f"| {debtors[2][0]} | {debtors[2][1]} | {b3} |\n"
        f"| **Debtors Control** | **B6** | **{tot}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_15",
        subskill="15_debtors_list_compile_from_3_accounts_table",
        title="Compile Debtors List & Debtors Control Total",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Total Debtors List = {tot}",
        marks=4,
        hints={
            "tier_1": "List each debtor's closing balance and sum them to match Debtors Control (B6).",
            "tier_2": f"Total = {b1} + {b2} + {b3}.",
            "tier_3": f"Debtors Control Total = {tot}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Individual debtor balances entered", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Total Debtors Control = {tot}", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_debtors_from_debtors_list"],
        journal_type="debtors_list",
    )


def arch_16_debtors_list_missing_debtor_opening_balance_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtors = pick_debtors(rng, 4)
    b1 = rng.randint(6, 16) * 1000 + rng.choice([240, 560, 960])
    b2 = rng.randint(2, 6) * 1000 + rng.choice([44, 120, 480])
    b3 = rng.randint(1, 4) * 1000 + rng.choice([280, 640, 820])
    b4 = rng.randint(2, 5) * 1000 + rng.choice([152, 412, 652])
    tot = b1 + b2 + b3 + b4

    prompt = (
        f"On 1 September, **{biz}**'s General Ledger **Debtors Control** balance is **{fmt_r(tot)}**.\n\n"
        "From the **Debtors Ledger**, three balances are known while the fourth (`D1`) is missing:\n"
        f"- **{debtors[0][0]} (D1):** `R?`\n"
        f"- **{debtors[1][0]} (D2):** {fmt_r(b2)}\n"
        f"- **{debtors[2][0]} (D3):** {fmt_r(b3)}\n"
        f"- **{debtors[3][0]} (D4):** {fmt_r(b4)}\n\n"
        f"Calculate the missing balance owed by **{debtors[0][0]} (D1)** [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Reconciling Missing Debtor Balance from Debtors Control** [3 marks]\n\n"
        f"$$\\text{{{debtors[0][0]}}} = \\text{{Debtors Control}} - (D2 + D3 + D4)$$\n"
        f"$$= {tot} - ({b2} + {b3} + {b4}) = {tot} - {b2 + b3 + b4} = {b1}$$\n"
        f"Answer: `{b1}`"
    )
    return build_short(
        rng,
        qid="g9_dl_16",
        subskill="16_debtors_list_missing_debtor_opening_balance_calc",
        title="Find Missing Debtor Balance from Control Account",
        prompt=prompt,
        expected_answer=str(b1),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "The Debtors Control total equals the sum of ALL individual Debtors Ledger balances.",
            "tier_2": f"Sum D2 + D3 + D4 = {b2 + b3 + b4}, then subtract from {tot}.",
            "tier_3": f"{debtors[0][0]} (D1) = {b1}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Sums known debtors = {b2 + b3 + b4}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Missing balance = {b1}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_debtors_list_must_equal_control"],
    )


def arch_17_reconcile_debtors_list_to_debtors_control_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    tot = rng.randint(15, 45) * 1000

    prompt = (
        f"At month-end, the **Debtors Control (B6)** balance in **{biz}**'s General Ledger is **{fmt_r(tot)}**.\n\n"
        f"Why **must** the total of the **Debtors List** compiled from the Debtors Ledger equal **{fmt_r(tot)}**?"
    )
    correct = "Because Debtors Control is posted from the same monthly DJ, DAJ, and CRJ totals whose individual transactions are posted daily to the individual Debtors Ledger accounts (acting as an internal accuracy check)."
    distractors = [
        "Because every cash sale on the Cash Register Roll is divided equally among all individual debtors.",
        "Because Debtors List adds Bank cash and Trading Stock totals to match Capital.",
        "Because Credit Notes are posted ONLY to Debtors Control and skipped in the Debtors Ledger.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_17",
        subskill="17_reconcile_debtors_list_to_debtors_control_rule",
        title="Why Debtors List Reconciles to Debtors Control",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Individual lines from the **DJ, DAJ, and CRJ** enter the **Debtors Ledger** daily, while the exact column **totals** "
            "from those same journals enter **Debtors Control (`B6`)** at month-end — so both must reconcile."
        ),
        hints={
            "tier_1": "Both records summarise the exact same credit-sales, returns, and receipts data.",
            "tier_2": "Daily individual postings (DL) must add up to monthly column-total postings (Debtors Control).",
            "tier_3": correct,
        },
        misconception_tags=["not_understanding_control_account_reconciliation"],
    )


def arch_18_diagnose_debtors_list_vs_control_discrepancy_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    list_tot = rng.randint(18, 42) * 1000
    omitted_inv = rng.randint(4, 15) * 100
    ctrl_tot = list_tot + omitted_inv
    debtor, fol = rng.choice(DEBTOR_POOL[:4])

    prompt = (
        f"**{biz}**'s month-end **Debtors Control** account shows **{fmt_r(ctrl_tot)}**, "
        f"but the **Debtors List** totals only **{fmt_r(list_tot)}**.\n\n"
        f"What single omitted posting in **{debtor} ({fol})**'s individual Debtors Ledger account explains this discrepancy?"
    )
    correct = f"A credit sale invoice of {fmt_r(omitted_inv)} was included in the DJ total (posted to Debtors Control) but omitted from {debtor}'s Debit (+) column in the Debtors Ledger."
    distractors = [
        f"A receipt of {fmt_r(omitted_inv)} from {debtor} was omitted from Debtors Control but posted to {debtor}'s Debit (+) column.",
        f"A cash sale of {fmt_r(omitted_inv)} was left out of the Cash Payments Journal.",
        f"A Credit Note of {fmt_r(omitted_inv)} was posted ONLY to {debtor}'s Debit (+) column.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_18",
        subskill="18_diagnose_debtors_list_vs_control_discrepancy_calc",
        title="Diagnose Debtors List vs Control Discrepancy",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Debtors Control (`{fmt_r(ctrl_tot)}`) is **{fmt_r(omitted_inv)} higher** than the Debtors List (`{fmt_r(list_tot)}`). "
            f"That happens when a DJ credit sale of **{fmt_r(omitted_inv)}** increased Debtors Control but was missed in {debtor}'s Debtors Ledger account."
        ),
        hints={
            "tier_1": f"Find the exact difference: {fmt_r(ctrl_tot)} - {fmt_r(list_tot)} = {fmt_r(omitted_inv)}.",
            "tier_2": "If the Debtors List is LOWER by that amount, an invoice debit to a customer's DL was missed (or a receipt doubled).",
            "tier_3": correct,
        },
        misconception_tags=["misdiagnosing_control_vs_list_variance"],
    )


def arch_19_general_ledger_classification_debtors_accounts(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    cases = [
        ("Debtors Control (B6)", "Current Asset", "Balance Sheet Section", "Debit"),
        ("Trading Stock (B5)", "Current Asset", "Balance Sheet Section", "Debit"),
        ("Sales (N1)", "Income", "Nominal Accounts Section", "Credit"),
        ("Cost of Sales (N2)", "Expense", "Nominal Accounts Section", "Debit"),
        ("Debtors Allowance (N3)", "Income Contra (Reduces Sales)", "Nominal Accounts Section", "Debit"),
    ]
    picked = rng.sample(cases, 3)
    headers = ["General Ledger Account", "Account Element", "GL Section", "Normal Side (Debit / Credit)"]
    given = {(i, 0) for i in range(3)}
    rows, correct_map = make_grid_rows([list(c) for c in picked], given_coords=given)
    cell_hints = {
        f"t0_r{i}_c1": f"{c[0]} is a(n) {c[1]}." for i, c in enumerate(picked)
    }
    cell_hints.update({
        f"t0_r{i}_c3": f"Normal balance side: {c[3]}." for i, c in enumerate(picked)
    })
    prompt = "Classify each General Ledger account by **Account Element**, **GL Section**, and **Normal Side (`Debit` or `Credit`)**."
    md_rows = "\n".join(f"| {a} | {b} | {c} | **{d}** |" for a, b, c, d in picked)
    worked = "**General Ledger Classification** [6 marks]\n\n| Account | Element | Section | Normal Side |\n| --- | --- | --- | --- |\n" + md_rows
    return build_table(
        rng,
        qid="g9_dl_19",
        subskill="19_general_ledger_classification_debtors_accounts",
        title="Classify General Ledger Accounts (B/S vs Nominal)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer="; ".join(f"{a}: {b}, {d}" for a, b, _, d in picked),
        marks=6,
        hints={
            "tier_1": "B accounts belong in Balance Sheet (Assets/OE/Liabilities); N accounts belong in Nominal (Income/Expenses).",
            "tier_2": "Expenses & Assets increase on Debit; Income increases on Credit (Debtors Allowance is contra-income -> Debit).",
            "tier_3": "; ".join(f"{a} -> {b} | {c} | {d}" for a, b, c, d in picked),
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{c[0]} classified completely", "marks": 2, "editable": True}
            for i, c in enumerate(picked)
        ],
        misconception_tags=["treating_cost_of_sales_as_asset_or_trading_stock_as_expense"],
        journal_type="classification_table",
    )


def arch_20_posting_dj_selling_price_double_entry_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    tot_sales = rng.randint(18, 55) * 1000

    prompt = (
        f"At month-end, the **Sales** column total in **{biz}**'s Debtors Journal (DJ) is **{fmt_r(tot_sales)}**.\n\n"
        "Which General Ledger double entry posts the **selling-price** total of the Debtors Journal?"
    )
    correct = f"Debit Debtors Control (asset increases) {fmt_r(tot_sales)}; Credit Sales (income increases OE) {fmt_r(tot_sales)}."
    distractors = [
        f"Debit Bank {fmt_r(tot_sales)}; Credit Debtors Control {fmt_r(tot_sales)}.",
        f"Debit Sales {fmt_r(tot_sales)}; Credit Trading Stock {fmt_r(tot_sales)}.",
        f"Debit Cost of Sales {fmt_r(tot_sales)}; Credit Debtors Control {fmt_r(tot_sales)}.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_20",
        subskill="20_posting_dj_selling_price_double_entry_rule",
        title="Posting DJ Selling Price Total to General Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Posting the DJ **Sales** total of {fmt_r(tot_sales)} increases the asset **Debtors Control** (Debit) "
            "and increases income **Sales** (Credit)."
        ),
        hints={
            "tier_1": "No cash enters Bank during a credit sale; Debtors owe the business instead.",
            "tier_2": "Debtor asset goes up (Dr Debtors Control); Income goes up (Cr Sales).",
            "tier_3": correct,
        },
        misconception_tags=["debiting_bank_instead_of_debtors_control_for_dj"],
    )


def arch_21_posting_dj_cost_price_double_entry_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    tot_cos = rng.randint(12, 36) * 1000

    prompt = (
        f"At month-end, the **Cost of Sales** column total in **{biz}**'s Debtors Journal (DJ) is **{fmt_r(tot_cos)}**.\n\n"
        "Which General Ledger double entry posts this **cost-price** total from the DJ?"
    )
    correct = f"Debit Cost of Sales (expense decreases OE) {fmt_r(tot_cos)}; Credit Trading Stock (asset decreases) {fmt_r(tot_cos)}."
    distractors = [
        f"Debit Trading Stock {fmt_r(tot_cos)}; Credit Cost of Sales {fmt_r(tot_cos)}.",
        f"Debit Debtors Control {fmt_r(tot_cos)}; Credit Cost of Sales {fmt_r(tot_cos)}.",
        f"Debit Sales {fmt_r(tot_cos)}; Credit Bank {fmt_r(tot_cos)}.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_21",
        subskill="21_posting_dj_cost_price_double_entry_rule",
        title="Posting DJ Cost of Sales Total to General Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"When goods leave the shelves, **Trading Stock** (Asset) decreases on the **Credit** side "
            f"and **Cost of Sales** (Expense) increases on the **Debit** side by **{fmt_r(tot_cos)}**."
        ),
        hints={
            "tier_1": "Which asset drops when goods are handed to credit customers, and which expense records that cost?",
            "tier_2": "Cost of Sales (Expense) = Debit; Trading Stock (Asset) = Credit.",
            "tier_3": correct,
        },
        misconception_tags=["reversing_cost_of_sales_and_trading_stock"],
    )


def arch_22_posting_crj_debtors_receipts_double_entry_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    tot_rec = rng.randint(14, 48) * 1000

    prompt = (
        f"In **{biz}**'s Cash Receipts Journal (CRJ), the month-end total of the **Debtors Control** column is **{fmt_r(tot_rec)}**.\n\n"
        "How is this **Debtors Control** column total posted to the General Ledger?"
    )
    correct = f"Debtors Control (B6) is CREDITED with {fmt_r(tot_rec)} (details: Bank / CRJ), while Bank (B7) is DEBITED as part of Total Receipts."
    distractors = [
        f"Debtors Control (B6) is DEBITED with {fmt_r(tot_rec)} and Sales (N1) is CREDITED.",
        f"Cost of Sales (N2) is CREDITED with {fmt_r(tot_rec)} and Trading Stock (B5) is DEBITED.",
        f"Creditors Control is DEBITED with {fmt_r(tot_rec)} and Bank is CREDITED.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_22",
        subskill="22_posting_crj_debtors_receipts_double_entry_rule",
        title="Posting CRJ Debtors Receipts to General Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Money received from debtors increases **Bank** (Debit) and decreases the **Debtors Control** asset "
            f"on the **Credit** side (`Bank | CRJ | {fmt_r(tot_rec)}`)."
        ),
        hints={
            "tier_1": "Cash paid by debtors reduces what they owe and increases Bank.",
            "tier_2": "Debit Bank (inside Total Receipts); Credit Debtors Control (Details: Bank).",
            "tier_3": correct,
        },
        misconception_tags=["debiting_debtors_control_on_cash_collection"],
    )


def arch_23_posting_daj_selling_and_cost_price_double_entry_rule(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sp_ret = rng.randint(24, 60) * 100
    cp_ret = sp_ret * 100 // 150

    prompt = (
        f"The **Debtors Allowance Journal (DAJ)** of **{biz}** closes with:\n"
        f"- **Debtors Allowance column:** {fmt_r(sp_ret)}\n"
        f"- **Cost of Sales column:** {fmt_r(cp_ret)}\n\n"
        "Which pair of General Ledger double entries correctly posts BOTH columns?"
    )
    correct = f"1) Dr Debtors Allowance / Cr Debtors Control ({fmt_r(sp_ret)}); 2) Dr Trading Stock / Cr Cost of Sales ({fmt_r(cp_ret)})."
    distractors = [
        f"1) Dr Debtors Control / Cr Debtors Allowance ({fmt_r(sp_ret)}); 2) Dr Cost of Sales / Cr Trading Stock ({fmt_r(cp_ret)}).",
        f"1) Dr Bank / Cr Debtors Control ({fmt_r(sp_ret)}); 2) Dr Sales / Cr Trading Stock ({fmt_r(cp_ret)}).",
        f"1) Dr Debtors Allowance / Cr Sales ({fmt_r(sp_ret)}); ignore Cost of Sales ({fmt_r(cp_ret)}).",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_23",
        subskill="23_posting_daj_selling_and_cost_price_double_entry_rule",
        title="Posting Both Columns of DAJ to General Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "DAJ **reverses** a credit sale: `Debtors Control` decreases (Credit), `Debtors Allowance` increases (Debit), "
            "`Trading Stock` rises back up (Debit), and `Cost of Sales` decreases (Credit)."
        ),
        hints={
            "tier_1": "DAJ reverses the exact double entries made when the goods were sold in the DJ.",
            "tier_2": "Debtors Allowance (Dr) vs Debtors Control (Cr); Trading Stock (Dr) vs Cost of Sales (Cr).",
            "tier_3": correct,
        },
        misconception_tags=["posting_daj_with_same_sides_as_dj"],
    )


def arch_24_complete_debtors_control_t_account_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, next_m, next_d = rng.choice(MONTH_DATA)
    open_bal = rng.randint(14, 28) * 1000
    dj_sales = rng.randint(12, 30) * 1000
    crj_bank = rng.randint(10, 22) * 1000
    daj_ret = rng.randint(1, 4) * 1000
    tot_dr = open_bal + dj_sales
    cd_bal = tot_dr - crj_bank - daj_ret

    headers = ["Dr Date", "Dr Details", "Dr Fol", "Dr Amount", "Cr Date", "Cr Details", "Cr Fol", "Cr Amount"]
    data_rows = [
        [f"{m_name[:3]} 1", "Balance", "b/d", str(open_bal), f"{m_name[:3]} {end_d}", "Bank", "CRJ", str(crj_bank)],
        [f"{m_name[:3]} {end_d}", "Sales", "DJ", str(dj_sales), f"{m_name[:3]} {end_d}", "Debtors allowance", "DAJ", str(daj_ret)],
        ["", "", "", "", f"{m_name[:3]} {end_d}", "Balance", "c/d", str(cd_bal)],
        ["", "", "TOTAL", str(tot_dr), "", "", "TOTAL", str(tot_dr)],
        [f"{next_m} {next_d}", "Balance", "b/d", str(cd_bal), "", "", "", ""],
    ]
    given = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (4, 7)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c1": "Contra account for DJ total on Dr side is 'Sales'.",
        "t0_r1_c3": f"DJ Sales total = {dj_sales}.",
        "t0_r0_c5": "Contra account for CRJ receipts on Cr side is 'Bank'.",
        "t0_r0_c7": f"CRJ Debtors Control total = {crj_bank}.",
        "t0_r1_c7": f"DAJ Debtors Allowance total = {daj_ret}.",
        "t0_r2_c7": f"Balance c/d = {tot_dr} - ({crj_bank} + {daj_ret}) = {cd_bal}.",
        "t0_r4_c3": f"Next month Balance b/d on Dr side = {cd_bal}.",
    }
    prompt = (
        f"Complete and balance the General Ledger **Debtors Control (`B6`)** T-account of **{biz}** for **{m_name} {yr}**.\n"
        f"- **1 {m_name}:** Opening Balance (`b/d`) = {fmt_r(open_bal)}\n"
        f"- **DJ Total (`Sales`):** {fmt_r(dj_sales)}\n"
        f"- **CRJ Total (`Debtors Control`):** {fmt_r(crj_bank)}\n"
        f"- **DAJ Total (`Debtors Allowance`):** {fmt_r(daj_ret)}\n"
        "*(Enter digits without spaces or R.)*"
    )
    worked = (
        f"**General Ledger: Debtors Control (B6)** [10 marks]\n\n"
        "| Dr Date | Details | Fol | Dr Amount | Cr Date | Details | Fol | Cr Amount |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| {m_name[:3]} 1 | Balance | b/d | {open_bal} | {m_name[:3]} {end_d} | Bank | CRJ | {crj_bank} |\n"
        f"| {m_name[:3]} {end_d} | Sales | DJ | {dj_sales} | {m_name[:3]} {end_d} | Debtors allowance | DAJ | {daj_ret} |\n"
        f"| | | | | {m_name[:3]} {end_d} | Balance | c/d | **{cd_bal}** |\n"
        f"| | | **TOTAL** | **{tot_dr}** | | | **TOTAL** | **{tot_dr}** |\n"
        f"| {next_m} {next_d} | Balance | b/d | **{cd_bal}** | | | | |"
    )
    return build_table(
        rng,
        qid="g9_dl_24",
        subskill="24_complete_debtors_control_t_account_table",
        title="Complete & Balance Debtors Control (B6) T-Account",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Total={tot_dr}; Cr Bank={crj_bank}, DAJ={daj_ret}; Closing Balance b/d={cd_bal}",
        marks=10,
        hints={
            "tier_1": "Balance b/d and Sales (DJ) enter Debit; Bank (CRJ) and Debtors allowance (DAJ) enter Credit.",
            "tier_2": f"Dr total = {open_bal} + {dj_sales} = {tot_dr}; subtract {crj_bank} + {daj_ret} for c/d.",
            "tier_3": f"Balance c/d and next-month b/d = {cd_bal}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr Sales (DJ) {dj_sales}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Cr Bank (CRJ) {crj_bank} & DAJ {daj_ret}", "marks": 4, "editable": True},
            {"id": "mp_3", "desc": f"Balanced c/d & b/d = {cd_bal} (Total {tot_dr})", "marks": 4, "editable": True},
        ],
        misconception_tags=["putting_crj_bank_receipts_on_debit_side_of_debtors_control"],
        journal_type="t_account",
    )


def arch_25_reconstruct_debtors_control_from_3_debtors_ledgers_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, next_m, next_d = rng.choice(MONTH_DATA)
    debtors = pick_debtors(rng, 3)

    b1, b2, b3 = [rng.randint(4, 12) * 1000 for _ in range(3)]
    inv1, inv2, inv3 = [rng.randint(3, 9) * 1000 for _ in range(3)]
    rec1, rec2, rec3 = [rng.randint(2, 7) * 1000 for _ in range(3)]

    tot_open = b1 + b2 + b3
    tot_sales = inv1 + inv2 + inv3
    tot_bank = rec1 + rec2 + rec3
    tot_dr = tot_open + tot_sales
    closing = tot_dr - tot_bank

    prompt = (
        f"The bookkeeper at **{biz}** misplaced the General Ledger **Debtors Control (`B6`)** page, "
        "but still has all three individual **Debtors Ledger** accounts:\n\n"
        f"- **{debtors[0][0]} (D1):** Opening b/d {fmt_r(b1)}; DJ Invoice {fmt_r(inv1)}; CRJ Receipt {fmt_r(rec1)}\n"
        f"- **{debtors[1][0]} (D2):** Opening b/d {fmt_r(b2)}; DJ Invoice {fmt_r(inv2)}; CRJ Receipt {fmt_r(rec2)}\n"
        f"- **{debtors[2][0]} (D3):** Opening b/d {fmt_r(b3)}; DJ Invoice {fmt_r(inv3)}; CRJ Receipt {fmt_r(rec3)}\n\n"
        f"Recreate the missing **Debtors Control (`B6`)** account for **{m_name} {yr}** in the table below *(digits only)*."
    )
    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    data_rows = [
        ["Balance", "b/d", str(tot_open), "Bank", "CRJ", str(tot_bank)],
        ["Sales", "DJ", str(tot_sales), "Balance", "c/d", str(closing)],
        ["TOTAL", "", str(tot_dr), "TOTAL", "", str(tot_dr)],
        ["Balance", "b/d", str(closing), "", "", ""],
    ]
    given = {(2, 0), (2, 1), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r0_c2": f"Sum all opening balances: {b1} + {b2} + {b3} = {tot_open}.",
        "t0_r1_c2": f"Sum all DJ invoices: {inv1} + {inv2} + {inv3} = {tot_sales}.",
        "t0_r0_c5": f"Sum all CRJ receipts: {rec1} + {rec2} + {rec3} = {tot_bank}.",
        "t0_r1_c5": f"Closing Balance c/d = {tot_dr} - {tot_bank} = {closing}.",
    }
    worked = (
        f"**Recreated Debtors Control (B6) from Debtors Ledger** [10 marks]\n\n"
        f"- Opening b/d = `{b1} + {b2} + {b3} = {tot_open}`\n"
        f"- Sales (DJ) = `{inv1} + {inv2} + {inv3} = {tot_sales}`\n"
        f"- Bank (CRJ) = `{rec1} + {rec2} + {rec3} = {tot_bank}`\n"
        f"- Balance c/d & b/d = `{tot_dr} - {tot_bank} = {closing}`\n\n"
        "| Dr Details | Fol | Dr Amount | Cr Details | Fol | Cr Amount |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| Balance | b/d | {tot_open} | Bank | CRJ | {tot_bank} |\n"
        f"| Sales | DJ | {tot_sales} | Balance | c/d | **{closing}** |\n"
        f"| **TOTAL** | | **{tot_dr}** | **TOTAL** | | **{tot_dr}** |\n"
        f"| Balance | b/d | **{closing}** | | | |"
    )
    return build_table(
        rng,
        qid="g9_dl_25",
        subskill="25_reconstruct_debtors_control_from_3_debtors_ledgers_table",
        title="Recreate Debtors Control from Individual Ledgers",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr b/d={tot_open}, Sales={tot_sales}; Cr Bank={tot_bank}, c/d={closing}",
        marks=10,
        hints={
            "tier_1": "Sum all opening balances for b/d, all DJ invoices for Sales, and all CRJ receipts for Bank.",
            "tier_2": f"Opening={tot_open}; Sales={tot_sales}; Bank={tot_bank}.",
            "tier_3": f"Total={tot_dr}; Closing Balance={closing}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Totals b/d ({tot_open}), Sales ({tot_sales}), Bank ({tot_bank})", "marks": 6, "editable": True},
            {"id": "mp_2", "desc": f"Balanced c/d & b/d = {closing}", "marks": 4, "editable": True},
        ],
        misconception_tags=["omitting_one_debtors_account_when_rebuilding_control"],
        journal_type="t_account",
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_debtors_ledger_vs_general_ledger_purpose": arch_01_debtors_ledger_vs_general_ledger_purpose,
    "02_debtors_ledger_3col_column_rules_dr_cr_balance": arch_02_debtors_ledger_3col_column_rules_dr_cr_balance,
    "03_debtors_ledger_source_mapping_dj_daj_crj_table": arch_03_debtors_ledger_source_mapping_dj_daj_crj_table,
    "04_account_rendered_balance_bd_meaning": arch_04_account_rendered_balance_bd_meaning,
    "05_debtors_ledger_single_credit_sale_row_table": arch_05_debtors_ledger_single_credit_sale_row_table,
    "06_debtors_ledger_single_credit_note_row_table": arch_06_debtors_ledger_single_credit_note_row_table,
    "07_debtors_ledger_single_receipt_row_table": arch_07_debtors_ledger_single_receipt_row_table,
    "08_debtors_ledger_full_account_d1_table": arch_08_debtors_ledger_full_account_d1_table,
    "09_debtors_ledger_settlement_first_of_month_pattern": arch_09_debtors_ledger_settlement_first_of_month_pattern,
    "10_debtors_ledger_settlement_in_full_up_to_date_table": arch_10_debtors_ledger_settlement_in_full_up_to_date_table,
    "11_debtors_ledger_part_settlement_with_allowance_table": arch_11_debtors_ledger_part_settlement_with_allowance_table,
    "12_debtors_ledger_reverse_to_dj_table": arch_12_debtors_ledger_reverse_to_dj_table,
    "13_debtors_ledger_find_missing_transaction_amount_calc": arch_13_debtors_ledger_find_missing_transaction_amount_calc,
    "14_debtors_ledger_folio_and_date_ordering_error_fix": arch_14_debtors_ledger_folio_and_date_ordering_error_fix,
    "15_debtors_list_compile_from_3_accounts_table": arch_15_debtors_list_compile_from_3_accounts_table,
    "16_debtors_list_missing_debtor_opening_balance_calc": arch_16_debtors_list_missing_debtor_opening_balance_calc,
    "17_reconcile_debtors_list_to_debtors_control_rule": arch_17_reconcile_debtors_list_to_debtors_control_rule,
    "18_diagnose_debtors_list_vs_control_discrepancy_calc": arch_18_diagnose_debtors_list_vs_control_discrepancy_calc,
    "19_general_ledger_classification_debtors_accounts": arch_19_general_ledger_classification_debtors_accounts,
    "20_posting_dj_selling_price_double_entry_rule": arch_20_posting_dj_selling_price_double_entry_rule,
    "21_posting_dj_cost_price_double_entry_rule": arch_21_posting_dj_cost_price_double_entry_rule,
    "22_posting_crj_debtors_receipts_double_entry_rule": arch_22_posting_crj_debtors_receipts_double_entry_rule,
    "23_posting_daj_selling_and_cost_price_double_entry_rule": arch_23_posting_daj_selling_and_cost_price_double_entry_rule,
    "24_complete_debtors_control_t_account_table": arch_24_complete_debtors_control_t_account_table,
    "25_reconstruct_debtors_control_from_3_debtors_ledgers_table": arch_25_reconstruct_debtors_control_from_3_debtors_ledgers_table,
}
