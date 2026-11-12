"""Grade 8 EMS - General Ledger & Trial Balance of a Service Business: Archetypes 01 to 25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/01. General ledger and Trial balance of a service business.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African Rand (R) contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import get_ems_scenario


def _fmt_r(amount: int | float) -> str:
    """Format Rand amounts cleanly with space thousands separator."""
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


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
    caps_weight: int = 25,
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
        "topic": "General ledger and Trial balance of a service business",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_general_ledger",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_gl_{subskill}",
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
        "diagnostic_tags": ["accounting", "general_ledger", "service_business"],
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
    caps_weight: int = 25,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "General ledger and Trial balance of a service business",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_general_ledger",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_gl_{subskill}",
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
        "diagnostic_tags": ["accounting", "general_ledger", "service_business"],
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
    caps_weight: int = 25,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "General ledger and Trial balance of a service business",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_general_ledger",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_gl_{subskill}",
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


def _t_account_svg(account_title: str, dr_lines: List[tuple], cr_lines: List[tuple], accent: str = "#1d4ed8") -> str:
    dr_y = 66
    dr_svg = []
    for dt, det, amt in dr_lines:
        dr_svg.append(
            f'<text x="20" y="{dr_y}" font-size="11" fill="#1e293b">{dt}</text>'
            f'<text x="58" y="{dr_y}" font-size="11" fill="#1e293b">{det}</text>'
            f'<text x="245" y="{dr_y}" font-size="11" font-weight="bold" text-anchor="end" fill="#0f172a">{amt}</text>'
        )
        dr_y += 20
    cr_y = 66
    cr_svg = []
    for dt, det, amt in cr_lines:
        cr_svg.append(
            f'<text x="275" y="{cr_y}" font-size="11" fill="#1e293b">{dt}</text>'
            f'<text x="313" y="{cr_y}" font-size="11" fill="#1e293b">{det}</text>'
            f'<text x="505" y="{cr_y}" font-size="11" font-weight="bold" text-anchor="end" fill="#0f172a">{amt}</text>'
        )
        cr_y += 20
    h = max(135, max(dr_y, cr_y) + 20)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 {h}" width="520" height="{h}">'
        f'<rect x="4" y="4" width="512" height="{h-8}" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="20" y="24" font-size="11" font-weight="bold" fill="{accent}">Dr</text>'
        f'<text x="260" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">{account_title}</text>'
        f'<text x="500" y="24" font-size="11" font-weight="bold" text-anchor="end" fill="{accent}">Cr</text>'
        f'<line x1="12" y1="32" x2="508" y2="32" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="260" y1="32" x2="260" y2="{h-12}" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="20" y="47" font-size="10" fill="#64748b">Date</text>'
        f'<text x="58" y="47" font-size="10" fill="#64748b">Details</text>'
        f'<text x="245" y="47" font-size="10" text-anchor="end" fill="#64748b">Amount (R)</text>'
        f'<text x="275" y="47" font-size="10" fill="#64748b">Date</text>'
        f'<text x="313" y="47" font-size="10" fill="#64748b">Details</text>'
        f'<text x="505" y="47" font-size="10" text-anchor="end" fill="#64748b">Amount (R)</text>'
        + "".join(dr_svg) + "".join(cr_svg) + "</svg>"
    )


def arch_01_accounting_cycle_stage_sequencing(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    stages = [
        ("Stage 2 (after Source Documents)", "Subsidiary Journals (CRJ and CPJ)", "records daily transactions sorted by cash receipts and cash payments", ["General Ledger", "Trial Balance", "Income Statement"]),
        ("Stage 3 (after Subsidiary Journals)", "General Ledger", "groups transactions into individual T-accounts after monthly journal totals are posted", ["Source Documents", "Trial Balance", "Cheque Counterfoil"]),
        ("Stage 4 (after General Ledger)", "Trial Balance", "lists final T-account balances to prove Total Debits equal Total Credits before financial statements", ["Subsidiary Journals", "Bank Reconciliation Statement", "Till Slip Summary"]),
    ]
    stage_label, correct, desc, wrongs = rng.choice(stages)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 95" width="560" height="95">'
        f'<rect width="560" height="95" fill="#ffffff"/>'
        f'<text x="280" y="18" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{sc["entrepreneur"]} Accounting Cycle Flow</text>'
        f'<rect x="10" y="34" width="115" height="42" rx="5" fill="#eff6ff" stroke="#1d4ed8"/><text x="67" y="59" font-size="10" text-anchor="middle" fill="#1e3a8a">Source Docs</text>'
        f'<line x1="125" y1="55" x2="145" y2="55" stroke="#334155" stroke-width="2"/>'
        f'<rect x="148" y="34" width="120" height="42" rx="5" fill="#f0fdf4" stroke="#15803d"/><text x="208" y="59" font-size="10" text-anchor="middle" fill="#14532d">{"?" if "Journals" in correct else "Journals (CRJ/CPJ)"}</text>'
        f'<line x1="268" y1="55" x2="288" y2="55" stroke="#334155" stroke-width="2"/>'
        f'<rect x="291" y="34" width="120" height="42" rx="5" fill="#fefce8" stroke="#ca8a04"/><text x="351" y="59" font-size="10" text-anchor="middle" fill="#713f12">{"?" if "Ledger" in correct else "General Ledger"}</text>'
        f'<line x1="411" y1="55" x2="431" y2="55" stroke="#334155" stroke-width="2"/>'
        f'<rect x="434" y="34" width="115" height="42" rx="5" fill="#faf5ff" stroke="#7e22ce"/><text x="491" y="59" font-size="10" text-anchor="middle" fill="#581c87">{"?" if "Trial" in correct else "Trial Balance"}</text>'
        f'</svg>'
    )
    prompt = (
        f"Look at the accounting cycle diagram for **{sc['entrepreneur']}'s {sc['business_type']}** in {sc['area']}.\n\n"
        f"Which accounting record belongs in **{stage_label}**, where it {desc}?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_01",
        subskill="01_accounting_cycle_stage_sequencing",
        title="Accounting Cycle Sequence",
        prompt=prompt,
        correct_text=correct,
        distractors=wrongs,
        explanation=f"The Grade 8 accounting sequence flows: Source Documents -> Subsidiary Journals (CRJ and CPJ) -> General Ledger -> Trial Balance -> Financial Statements. Therefore, {stage_label} is **{correct}**.",
        hints={
            "tier_1": "Follow the chronological sequence from source documents to checking accuracy.",
            "tier_2": "Journals summarize documents; the Ledger groups accounts; the Trial Balance checks equality.",
            "tier_3": f"Correct answer: {correct}.",
        },
        misconception_tags=["accounting_cycle_order_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_02_general_ledger_purpose_and_journal_link(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(15, 65) * 100
    prompt = (
        f"**{sc['entrepreneur']}** runs a **{sc['business_type']}** in {sc['area']} and completed monthly CRJ and CPJ totals of {_fmt_r(amt)}.\n\n"
        f"What is the primary purpose of **posting** these journal totals into the **General Ledger**?"
    )
    correct = "To sort and group all transactions belonging to each specific account (such as Bank, Wages, or Current Income) in one organised T-account."
    distractors = [
        "To serve as the primary daily cash register slip handed to retail walk-in customers.",
        "To calculate employee PAYE income tax brackets on behalf of SARS at year-end.",
        "To replace source documents so receipts and cheque counterfoils can be discarded immediately.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_02",
        subskill="02_general_ledger_purpose_and_journal_link",
        title="Purpose of the General Ledger",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="The CRJ and CPJ record receipts and payments chronologically like diaries, while the **General Ledger** acts as the central filing cabinet sorting every transaction into dedicated T-accounts.",
        hints={
            "tier_1": "Think of journals as chronological diaries and the General Ledger as an organised filing cabinet.",
            "tier_2": "Each individual account collects all debit and credit movements affecting that single account.",
            "tier_3": "It sorts and groups all activity related to each single account into one place.",
        },
        misconception_tags=["confusing_journals_with_general_ledger"],
    )


def arch_03_double_entry_principle_duality(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(4, 24) * 250
    prompt = (
        f"During May, **{sc['entrepreneur']}'s {sc['business_type']}** in {sc['area']} recorded a single business transaction worth **{_fmt_r(amt)}**.\n\n"
        f"According to the **double-entry principle**, how must {_fmt_r(amt)} be recorded in the General Ledger?"
    )
    correct = f"As one debit entry of {_fmt_r(amt)} in one account and an equal credit entry of {_fmt_r(amt)} in a corresponding contra account."
    distractors = [
        f"As two separate debit entries of {_fmt_r(amt)} in the same Bank T-account.",
        f"Only once on the debit side of the Cash Receipts Journal without affecting any other account.",
        f"As {_fmt_r(amt / 2)} on the debit side and {_fmt_r(amt / 2)} on the credit side of Bank.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_03",
        subskill="03_double_entry_principle_duality",
        title="Double-Entry Principle",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"The double-entry principle requires every transaction's monetary value ({_fmt_r(amt)}) to have two equal and opposite entries: one Debit and one Credit across at least two ledger accounts.",
        hints={
            "tier_1": "Every transaction affects at least two accounts equally and oppositely.",
            "tier_2": "Total debits recorded for any transaction must equal total credits.",
            "tier_3": f"Debit one account with {_fmt_r(amt)} and Credit the contra account with {_fmt_r(amt)}.",
        },
        misconception_tags=["single_entry_misconception"],
    )


def arch_04_t_account_structure_debit_credit_sides(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    acc = rng.choice(["Bank (B4)", "Capital (B1)", "Wages (N3)", "Current Income (N1)"])
    amt = rng.randint(12, 48) * 100
    svg = _t_account_svg(acc, [("May 5", "Contra Entry", f"{amt:,}".replace(",", " "))], [])
    prompt = (
        f"Inspect the General Ledger T-account layout for **{acc}** at **{sc['entrepreneur']}'s {sc['business_type']}**.\n\n"
        f"Which directional rule is **correct** for the standard South African General Ledger T-account format shown?"
    )
    correct = "The left-hand side is the Debit (Dr) side, the right-hand side is the Credit (Cr) side, and the account heading contains only the account name (never the month or date)."
    distractors = [
        "The left-hand side is the Credit (Cr) side, and the date of opening must appear in the main account heading.",
        "Debit always means positive profit and Credit always means a loss regardless of account type.",
        "Only Assets are drawn as T-accounts; Expenses and Incomes do not have Debit or Credit sides.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_04",
        subskill="04_t_account_structure_debit_credit_sides",
        title="T-Account Structure & Heading Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="In a standard General Ledger T-account, **Debit (Dr)** is strictly the left side, **Credit (Cr)** is strictly the right side, and the heading shows the account name and folio code only—dates go in the Date column.",
        hints={
            "tier_1": "Recall what 'Dr' and 'Cr' stand for spatially on a capital 'T'.",
            "tier_2": "Dr is left, Cr is right; headings show only the account title (not dates).",
            "tier_3": "Left = Dr, Right = Cr, heading contains account name only.",
        },
        misconception_tags=["debit_credit_side_reversal", "date_in_heading_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_05_balance_sheet_vs_nominal_sections(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Vehicles", "Balance Sheet Accounts Section", "Non-Current Asset representing long-term resources owned by the business"),
        ("Equipment", "Balance Sheet Accounts Section", "Non-Current Asset owned for ongoing business operations"),
        ("Land and Buildings", "Balance Sheet Accounts Section", "Fixed property asset carrying forward from month to month"),
        ("Drawings", "Balance Sheet Accounts Section", "Owner's Equity account tracking cash or goods taken by the owner"),
        ("Capital", "Balance Sheet Accounts Section", "Owner's Equity investment permanently retained in the business"),
        ("Cash Float", "Balance Sheet Accounts Section", "Current Asset holding change inside the till"),
        ("Consumable goods", "Nominal Accounts Section", "Operating expense incurred during service delivery"),
        ("Water and Electricity", "Nominal Accounts Section", "Monthly utility expense used to calculate profit"),
        ("Material Cost", "Nominal Accounts Section", "Direct service-delivery expense belonging in profit calculation"),
        ("Rent Income", "Nominal Accounts Section", "Revenue earned by renting out spare business space"),
    ]
    acc, sec, reason = rng.choice(pool)
    other_sec = "Nominal Accounts Section" if "Balance" in sec else "Balance Sheet Accounts Section"
    prompt = (
        f"While organising the General Ledger for **{sc['entrepreneur']}'s {sc['business_type']}**, "
        f"the bookkeeper must file the **{acc}** account into the correct ledger section.\n\n"
        f"Into which section of the General Ledger should **{acc}** be placed, and why?"
    )
    correct = f"{sec}, because {acc} is a {reason}."
    distractors = [
        f"{other_sec}, because {acc} is an account created solely inside the Cash Receipts Journal.",
        f"{other_sec}, because {acc} is closed off to the petty cash voucher box every Friday.",
        f"Subsidiary Trial Journal Section, because service businesses separate {acc} from the ledger.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_05",
        subskill="05_balance_sheet_vs_nominal_sections",
        title="Balance Sheet vs Nominal Accounts Section",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"The General Ledger separates permanent accounts (**Balance Sheet Section**: Assets, Owner's Equity, Liabilities) from temporary profit-calculating accounts (**Nominal Section**: Income and Expenses). Thus **{acc}** belongs in the **{sec}**.",
        hints={
            "tier_1": "Ask: Is this an Asset/Liability/Equity (Balance Sheet) or an Income/Expense (Nominal)?",
            "tier_2": f"{acc} represents a {reason[:38]}...",
            "tier_3": f"Place {acc} in the {sec}.",
        },
        misconception_tags=["nominal_vs_balance_sheet_confusion"],
    )


def arch_06_folio_numbering_system_b_and_n(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    num = rng.randint(1, 6)
    acc_choice = rng.choice([
        ("Capital", f"B{num}", "Balance Sheet Accounts Section"),
        ("Bank", f"B{num}", "Balance Sheet Accounts Section"),
        ("Equipment", f"B{num}", "Balance Sheet Accounts Section"),
        ("Current Income", f"N{num}", "Nominal Accounts Section"),
        ("Wages", f"N{num}", "Nominal Accounts Section"),
        ("Telephone", f"N{num}", "Nominal Accounts Section"),
    ])
    acc_name, folio, sec = acc_choice
    prompt = (
        f"In the General Ledger index of **{sc['entrepreneur']}'s {sc['business_type']}**, the account **{acc_name}** is assigned folio number **{folio}**.\n\n"
        f"State which General Ledger section the prefix letter in **{folio}** identifies, and explain where this folio number is cross-referenced in the CRJ or CPJ."
    )
    expected = f"{sec}; entered in the journal's Folio column (for Sundry items) or directly beneath the special column total."
    sol = (
        f"**{expected}** [3 marks]\n\n"
        f"**Working & Rationale:**\n"
        f"1. **Folio Prefix:** `{folio[0]}` in **{folio}** designates the **{sec}** [1 mark].\n"
        f"2. **Sundry Column Cross-Reference:** If {acc_name} is posted from Sundry Accounts, **{folio}** is written in the journal's Folio column beside that row [1 mark].\n"
        f"3. **Special Column Total:** If {acc_name} has a dedicated journal column, **{folio}** is written immediately below the monthly column total [1 mark]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_06",
        subskill="06_folio_numbering_system_b_and_n",
        title="Ledger Folio Prefix & Cross-Referencing",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        qtype="short_answer",
        hints={
            "tier_1": "Prefix 'B' stands for Balance Sheet section; 'N' stands for Nominal accounts section.",
            "tier_2": "Folio codes go in the journal Fol column for Sundry entries, or below column totals for special columns.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Identifies {sec} from folio {folio}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Explains Sundry Fol column entry", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Explains folio written beneath special column total", "marks": 1, "editable": True},
        ],
        misconception_tags=["folio_prefix_confusion"],
    )


def arch_07_dead_mnemonic_debit_increase_accounts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cases = [
        ("Drawings", "the owner withdraws cash for personal use", "Drawings increases Owner's Equity reduction on the Debit side"),
        ("Expenses (e.g. Telephone)", "the business pays its monthly phone account", "Expenses reduce Owner's Equity and always increase on the Debit side"),
        ("Assets (e.g. Equipment)", "the business buys new salon chairs for cash", "Assets are resources owned and always increase on the Debit side"),
    ]
    cat, ctx, why = rng.choice(cases)
    prompt = (
        f"At **{sc['entrepreneur']}'s {sc['business_type']}** in {sc['area']}, {ctx}.\n\n"
        f"Using the **DEAD** mnemonic, why is the **{cat}** account entered on the **left-hand** side of its T-account when it increases?"
    )
    correct = f"Because DEAD stands for Drawings, Expenses, Assets (and Debtors), all of which have normal Debit balances and increase on the Debit (left) side ({why})."
    distractors = [
        f"Because {cat} belongs to CLIC and increases on the Credit side whenever money leaves the business.",
        f"Because all accounts in the Nominal Section are strictly credited when they increase.",
        f"Because cash receipts from customers require every asset and expense to be credited together.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_07",
        subskill="07_dead_mnemonic_debit_increase_accounts",
        title="DEAD Mnemonic Debit Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**DEAD** = **D**ebit **D**rawings, **E**xpenses, **A**ssets, and **D**ebtors to increase them. Decreases in any DEAD account are recorded on the Credit side.",
        hints={
            "tier_1": "Expand each letter of D-E-A-D.",
            "tier_2": "Drawings, Expenses, Assets, Debtors increase on the Debit side.",
            "tier_3": f"{cat} belongs to DEAD and increases on the Debit side.",
        },
        misconception_tags=["dead_clic_rule_inversion"],
    )


def arch_08_clic_mnemonic_credit_increase_accounts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cases = [
        ("Capital", f"{sc['entrepreneur']} invests personal savings into the business bank account", "owner's capital claim"),
        ("Liabilities (Loan)", f"{sc['entrepreneur']} obtains a business loan from a local bank", "obligation owed to an external lender"),
        ("Income (Current Income)", f"{sc['entrepreneur']} earns service fees from customers", "revenue increasing Owner's Equity"),
    ]
    cat, ctx, why = rng.choice(cases)
    prompt = (
        f"Suppose **{ctx}**.\n\n"
        f"Applying the **CLIC** rule in the General Ledger, on which side does **{cat}** increase, and what does the mnemonic **CLIC** represent?"
    )
    correct = f"Credit side; CLIC represents Capital, Liabilities, Income (and Creditors), all of which increase on the Credit side ({why})."
    distractors = [
        "Debit side; CLIC represents Cash, Ledgers, Inventory, and Cost accounts increasing on the left.",
        "Credit side only if Cash Payments Journal payments exceed Cash Receipts Journal deposits.",
        "Debit side; all increases in Equity and Revenue are always recorded on the left-hand side.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_08",
        subskill="08_clic_mnemonic_credit_increase_accounts",
        title="CLIC Mnemonic Credit Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**CLIC** = **C**redit **C**reditors, **L**iabilities, **I**ncome, and **C**apital to increase them. Therefore **{cat}** increases on the Credit (right-hand) side.",
        hints={
            "tier_1": "Expand each letter of C-L-I-C.",
            "tier_2": "Capital, Liabilities, Income, Creditors increase on the Credit side.",
            "tier_3": f"{cat} increases on the Credit side under CLIC.",
        },
        misconception_tags=["dead_clic_rule_inversion"],
    )


def arch_09_account_normal_balance_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Bank", "Balance Sheet", "DEAD", "Debit"),
        ("Capital", "Balance Sheet", "CLIC", "Credit"),
        ("Current Income", "Nominal", "CLIC", "Credit"),
        ("Wages", "Nominal", "DEAD", "Debit"),
        ("Drawings", "Balance Sheet", "DEAD", "Debit"),
        ("Equipment", "Balance Sheet", "DEAD", "Debit"),
        ("Rent Income", "Nominal", "CLIC", "Credit"),
        ("Consumable goods", "Nominal", "DEAD", "Debit"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Account Name", "Ledger Section (Balance Sheet / Nominal)", "Rule Group (DEAD / CLIC)", "Normal Balance (Debit / Credit)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_rows = ["| Account Name | Ledger Section | Rule Group | Normal Balance |", "| --- | --- | --- | --- |"]

    for idx, (name, sec, rule, bal) in enumerate(chosen):
        correct_map[f"t0_r{idx}_c1"] = sec
        correct_map[f"t0_r{idx}_c2"] = rule
        correct_map[f"t0_r{idx}_c3"] = bal
        cell_hints[f"t0_r{idx}_c1"] = f"Permanent Assets/Equity/Liabilities go in Balance Sheet; temporary Income/Expenses go in Nominal."
        cell_hints[f"t0_r{idx}_c2"] = f"Apply DEAD (Drawings, Expenses, Assets) or CLIC (Capital, Liabilities, Income) to {name}."
        cell_hints[f"t0_r{idx}_c3"] = f"{rule} accounts carry a {bal} balance."
        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "cell_id": f"t0_r{idx}_c0", "value": name, "type": "given", "editable": False},
            {"coordinate": f"t0_r{idx}_c1", "cell_id": f"t0_r{idx}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c2", "cell_id": f"t0_r{idx}_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c3", "cell_id": f"t0_r{idx}_c3", "value": "", "type": "required", "editable": True},
        ])
        md_rows.append(f"| {name} | **{sec}** | **{rule}** | **{bal}** |")

    worked = f"**Completed General Ledger Classification** [12 marks]:\n\n" + "\n".join(md_rows)
    sample = "; ".join(f"{n}: {s}/{r}/{b}" for n, s, r, b in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_gl_09",
        subskill="09_account_normal_balance_classification_table",
        title="Ledger Section & DEAD CLIC Classification Table",
        prompt=(
            f"Classify each General Ledger account for **{sc['entrepreneur']}'s {sc['business_type']}** by entering its "
            f"**Ledger Section** (`Balance Sheet` or `Nominal`), **Rule Group** (`DEAD` or `CLIC`), and **Normal Balance** (`Debit` or `Credit`)."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=12,
        hints={
            "tier_1": "Separate Balance Sheet accounts (Assets, Equity, Liabilities) from Nominal accounts (Income, Expenses).",
            "tier_2": "DEAD accounts have Debit normal balances; CLIC accounts have Credit normal balances.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Correct classification for {c[0]}", "marks": 3, "editable": True} for i, c in enumerate(chosen)],
        misconception_tags=["dead_clic_rule_inversion", "nominal_vs_balance_sheet_confusion"],
    )


def arch_10_bank_account_asset_receipts_and_payments(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    open_bal = rng.randint(6, 20) * 1000
    receipts = rng.randint(5, 18) * 500
    payments = rng.randint(4, 15) * 400
    closing = open_bal + receipts - payments
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** begins 1 May with a Debit Bank balance of **{_fmt_r(open_bal)}**. "
        f"During May, the business receives **{_fmt_r(receipts)}** (cash receipts) and pays **{_fmt_r(payments)}** (cash payments).\n\n"
        f"Calculate the new Bank balance (in Rand) at 31 May after posting both entries to the Bank T-account."
    )
    ans = _fmt_r(closing)
    sol = (
        f"**{ans}** (Debit balance) [3 marks]\n\n"
        f"**Working:**\n"
        f"Bank is an **Asset** (DEAD): receipts increase Bank on the **Debit** side; payments decrease Bank on the **Credit** side.\n"
        f"$$\\text{{New Balance}} = {open_bal} + {receipts} - {payments} = {closing}\\text{{ (R{closing:,})}}$$".replace(",", " ")
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_10",
        subskill="10_bank_account_asset_receipts_and_payments",
        title="Bank Asset T-Account Receipts & Payments",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Add cash received to the opening Debit balance, then subtract cash paid out.",
            "tier_2": f"Compute {open_bal} + {receipts} - {payments}.",
            "tier_3": f"Closing Bank balance = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Adds receipts ({_fmt_r(receipts)}) on Debit side", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Subtracts payments ({_fmt_r(payments)}) on Credit side", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Correct final Bank balance {ans}", "marks": 1, "editable": True},
        ],
        misconception_tags=["bank_receipt_credit_error"],
    )


def arch_11_capital_contribution_double_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(15, 95) * 1000
    prompt = (
        f"**{sc['entrepreneur']}** deposits **{_fmt_r(amt)}** of personal funds directly into the business bank account as a **capital contribution** to start **{sc['business_type']}** in {sc['area']}.\n\n"
        f"Which account is **Debited**, which account is **Credited**, and what is the effect on the Accounting Equation ($A = OE + L$)?"
    )
    correct = f"Debit Bank ({_fmt_r(amt)}), Credit Capital ({_fmt_r(amt)}); Assets increase by +{_fmt_r(amt)} and Owner's Equity increases by +{_fmt_r(amt)}."
    distractors = [
        f"Debit Capital ({_fmt_r(amt)}), Credit Bank ({_fmt_r(amt)}); Assets increase by +{_fmt_r(amt)} and Liabilities increase by +{_fmt_r(amt)}.",
        f"Debit Bank ({_fmt_r(amt)}), Credit Current Income ({_fmt_r(amt)}); Assets increase by +{_fmt_r(amt)} and Owner's Equity decreases.",
        f"Debit Drawings ({_fmt_r(amt)}), Credit Capital ({_fmt_r(amt)}); no net effect on Assets.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_11",
        subskill="11_capital_contribution_double_entry",
        title="Capital Contribution Double-Entry",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"1. **Bank** (Asset, DEAD) increases -> **Debit Bank** (+{_fmt_r(amt)} to Assets).\n2. **Capital** (Owner's Equity, CLIC) increases -> **Credit Capital** (+{_fmt_r(amt)} to Owner's Equity).",
        hints={
            "tier_1": "Cash entered the business bank account (Asset +), funded by the owner (Capital +).",
            "tier_2": "Asset increases on Debit (DEAD); Capital increases on Credit (CLIC).",
            "tier_3": f"Dr Bank {_fmt_r(amt)}, Cr Capital {_fmt_r(amt)}; +A, +OE.",
        },
        misconception_tags=["debit_capital_misconception"],
    )


def arch_12_drawings_owner_withdrawal_double_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(8, 36) * 250
    purpose = rng.choice(["pay personal home electricity", "fund a family holiday", "buy personal groceries"])
    prompt = (
        f"**{sc['entrepreneur']}** withdraws **{_fmt_r(amt)}** from the business bank account to {purpose}.\n\n"
        f"State the **Account Debited**, **Account Credited**, and the effect on **Assets (A)** and **Owner's Equity (OE)**."
    )
    expected = f"Account Debited: Drawings ({_fmt_r(amt)}); Account Credited: Bank ({_fmt_r(amt)}); Effect: A = -{_fmt_r(amt)}, OE = -{_fmt_r(amt)}"
    sol = (
        f"**{expected}** [4 marks]\n\n"
        f"**Analysis:**\n"
        f"- **Drawings** (DEAD) increases when the owner withdraws business funds for personal use -> **Debit Drawings** (reduces Owner's Equity by {_fmt_r(amt)}).\n"
        f"- **Bank** (Asset, DEAD) decreases when cash leaves the business -> **Credit Bank** (reduces Assets by {_fmt_r(amt)})."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_12",
        subskill="12_drawings_owner_withdrawal_double_entry",
        title="Owner Drawings Double-Entry",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        qtype="short_answer",
        hints={
            "tier_1": "Personal withdrawals by the owner are recorded in the Drawings account, never Wages or Expenses.",
            "tier_2": "Drawings increases on Debit (DEAD), decreasing OE; Bank decreases on Credit, decreasing A.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Debit Drawings", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Credit Bank", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Assets decrease by {_fmt_r(amt)}", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Owner's Equity decreases by {_fmt_r(amt)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["classifying_drawings_as_expense", "drawings_credit_error"],
    )


def arch_13_service_fee_current_income_double_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(5, 45) * 150
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** receives **{_fmt_r(amt)}** cash from clients for services rendered.\n\n"
        f"Identify the correct General Ledger double-entry and accounting equation impact."
    )
    correct = f"Debit Bank, Credit Current Income with {_fmt_r(amt)}; Assets +{_fmt_r(amt)} and Owner's Equity +{_fmt_r(amt)}."
    distractors = [
        f"Debit Current Income, Credit Bank with {_fmt_r(amt)}; Assets -{_fmt_r(amt)} and Owner's Equity -{_fmt_r(amt)}.",
        f"Debit Bank, Credit Capital with {_fmt_r(amt)}; Assets +{_fmt_r(amt)} and Liabilities +{_fmt_r(amt)}.",
        f"Debit Services Rendered, Credit Sales with {_fmt_r(amt)}; Assets +{_fmt_r(amt)} and Liabilities +{_fmt_r(amt)}.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_13",
        subskill="13_service_fee_current_income_double_entry",
        title="Current Income Double-Entry",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Cash received from services increases **Bank** (Asset -> Debit) and increases **Current Income** (Income, CLIC -> Credit), increasing both Assets and Owner's Equity by {_fmt_r(amt)}.",
        hints={
            "tier_1": "Cash increases Bank (Debit), and service fees earned go to Current Income.",
            "tier_2": "Current Income increases Owner's Equity on the Credit side (CLIC).",
            "tier_3": f"Dr Bank, Cr Current Income; A +{_fmt_r(amt)}, OE +{_fmt_r(amt)}.",
        },
        misconception_tags=["crediting_bank_on_receipt"],
    )


def arch_14_rent_income_received_double_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(2, 9) * 800
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** rents out spare floor space to a tenant and receives **{_fmt_r(amt)}** into the business bank account.\n\n"
        f"Why is the **Rent Income** ledger account **Credited** with {_fmt_r(amt)}?"
    )
    correct = "Because Rent Income is an Income account under CLIC; crediting increases Income and raises Owner's Equity while Bank (Asset) is debited."
    distractors = [
        "Because Rent Income is an operating Expense under DEAD that reduces the business's bank balance.",
        "Because rental deposits are always owed back to SARS as an indirect liability.",
        "Because every transaction involving property is recorded on the Credit side of Current Income.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_14",
        subskill="14_rent_income_received_double_entry",
        title="Rent Income Credit Rationale",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"Receiving rent increases **Bank** (Asset -> Debit {_fmt_r(amt)}) and increases **Rent Income** (Income, CLIC -> Credit {_fmt_r(amt)}). Note that Rent Income uses its own Nominal account rather than Current Income.",
        hints={
            "tier_1": "Receiving rent means the business earns income (CLIC), not paying an expense.",
            "tier_2": "Income accounts increase on the Credit side and raise Owner's Equity.",
            "tier_3": "Rent Income is an Income account under CLIC, so Credit increases it.",
        },
        misconception_tags=["confusing_rent_income_and_rent_expense"],
    )


def arch_15_expense_payment_wages_or_telephone_double_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    expense = rng.choice(["Wages", "Stationery", "Telephone", "Water and Electricity", "Consumable goods"])
    amt = rng.randint(4, 25) * 120
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** pays **{_fmt_r(amt)}** from the business bank account for **{expense}**.\n\n"
        f"Which T-account entry and Owner's Equity effect apply to **{expense}**?"
    )
    correct = f"Debit {expense} ({_fmt_r(amt)}) because Expenses increase on Debit (DEAD), and Credit Bank ({_fmt_r(amt)}); Owner's Equity decreases by -{_fmt_r(amt)}."
    distractors = [
        f"Credit {expense} ({_fmt_r(amt)}) and Debit Bank ({_fmt_r(amt)}); Owner's Equity increases by +{_fmt_r(amt)}.",
        f"Debit {expense} ({_fmt_r(amt)}) and Credit Capital ({_fmt_r(amt)}); Assets remain completely unchanged.",
        f"Credit {expense} ({_fmt_r(amt)}) because paying money out means credits on both accounts.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_15",
        subskill="15_expense_payment_wages_or_telephone_double_entry",
        title="Expense Payment Double-Entry",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**{expense}** is an **Expense** (DEAD -> Debit increases it) that lowers net profit and Owner's Equity (-{_fmt_r(amt)}), while **Bank** (Asset) decreases via Credit (-{_fmt_r(amt)}).",
        hints={
            "tier_1": f"Money was paid out (Bank Credit) for an operating cost ({expense}).",
            "tier_2": "Expenses fall under DEAD (increase on Debit) and decrease Owner's Equity.",
            "tier_3": f"Dr {expense}, Cr Bank; OE -{_fmt_r(amt)}.",
        },
        misconception_tags=["crediting_expenses_when_paid"],
    )


def arch_16_asset_purchase_equipment_or_vehicle_double_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    asset = rng.choice(["Equipment", "Vehicles"])
    amt = rng.randint(12, 60) * 500
    prompt = (
        f"**{sc['entrepreneur']}'s {sc['business_type']}** buys **{asset}** from {sc['supplier']} for **{_fmt_r(amt)}** paid via EFT.\n\n"
        f"1. Name the Account Debited and Account Credited.\n"
        f"2. What is the **net effect** on Total Assets ($A$) and Total Owner's Equity ($OE$)?"
    )
    expected = f"Debit {asset} ({_fmt_r(amt)}), Credit Bank ({_fmt_r(amt)}); Net effect: A = 0 (+{_fmt_r(amt)} and -{_fmt_r(amt)}), OE = 0"
    sol = (
        f"**{expected}** [4 marks]\n\n"
        f"**Analysis:**\n"
        f"1. **Debit {asset}** (+{_fmt_r(amt)} Non-Current Asset) and **Credit Bank** (-{_fmt_r(amt)} Current Asset) [2 marks].\n"
        f"2. Total **Assets** have **no net change (0)** because one asset ({asset}) increased by {_fmt_r(amt)} while another asset (Bank) decreased by {_fmt_r(amt)}. **Owner's Equity** is unaffected (0) [2 marks]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_16",
        subskill="16_asset_purchase_equipment_or_vehicle_double_entry",
        title="Cash Purchase of Non-Current Assets",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        qtype="short_answer",
        hints={
            "tier_1": f"Both {asset} and Bank are Assets.",
            "tier_2": f"One Asset increases (+{_fmt_r(amt)}) and another decreases (-{_fmt_r(amt)}); Owner's Equity does not change.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Debit {asset}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Credit Bank", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Assets net effect is 0 (+amt / -amt)", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Owner's Equity unaffected (0)", "marks": 1, "editable": True},
        ],
        misconception_tags=["treating_asset_purchase_as_expense"],
    )


def arch_17_loan_received_and_repayment_liability_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(10, 50) * 1000
    is_receive = rng.choice([True, False])
    if is_receive:
        prompt = f"**{sc['entrepreneur']}'s {sc['business_type']}** receives a business loan of **{_fmt_r(amt)}** directly into its Bank account from Mzanzi Bank.\n\nWhich entry and Accounting Equation impact is correct?"
        correct = f"Debit Bank ({_fmt_r(amt)}), Credit Loan ({_fmt_r(amt)}); Assets +{_fmt_r(amt)} and Liabilities +{_fmt_r(amt)}."
        distractors = [
            f"Debit Loan ({_fmt_r(amt)}), Credit Bank ({_fmt_r(amt)}); Assets +{_fmt_r(amt)} and Owner's Equity +{_fmt_r(amt)}.",
            f"Debit Bank ({_fmt_r(amt)}), Credit Current Income ({_fmt_r(amt)}); Owner's Equity +{_fmt_r(amt)}.",
            f"Debit Capital ({_fmt_r(amt)}), Credit Loan ({_fmt_r(amt)}); Liabilities -{_fmt_r(amt)}.",
        ]
    else:
        prompt = f"**{sc['entrepreneur']}'s {sc['business_type']}** pays **{_fmt_r(amt)}** from Bank as a capital repayment on an existing **Loan**.\n\nWhich entry and Accounting Equation impact is correct?"
        correct = f"Debit Loan ({_fmt_r(amt)}), Credit Bank ({_fmt_r(amt)}); Assets -{_fmt_r(amt)} and Liabilities -{_fmt_r(amt)}."
        distractors = [
            f"Debit Bank ({_fmt_r(amt)}), Credit Loan ({_fmt_r(amt)}); Assets -{_fmt_r(amt)} and Liabilities +{_fmt_r(amt)}.",
            f"Debit Wages ({_fmt_r(amt)}), Credit Bank ({_fmt_r(amt)}); Owner's Equity -{_fmt_r(amt)}.",
            f"Debit Loan ({_fmt_r(amt)}), Credit Capital ({_fmt_r(amt)}); Owner's Equity -{_fmt_r(amt)}.",
        ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_17",
        subskill="17_loan_received_and_repayment_liability_entry",
        title="Loan Liability Double-Entry",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="Loan is a **Liability** (CLIC): it increases on the **Credit** side when borrowed and decreases on the **Debit** side when repaid.",
        hints={
            "tier_1": "Loan is a Liability (CLIC): Credit increases debt, Debit decreases debt.",
            "tier_2": "A loan does not affect Owner's Equity (not income, not expense).",
            "tier_3": correct,
        },
        misconception_tags=["treating_loan_as_income_or_expense"],
    )


def arch_18_owners_equity_formula_capital_profit_drawings(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    capital = rng.randint(40, 120) * 1000
    income = rng.randint(25, 70) * 1000
    expenses = rng.randint(10, 24) * 1000
    drawings = rng.randint(3, 12) * 1000
    profit = income - expenses
    oe = capital + profit - drawings
    prompt = (
        f"Calculate the final **Owner's Equity** for **{sc['entrepreneur']}'s {sc['business_type']}** using the ledger totals below:\n"
        f"- Capital: **{_fmt_r(capital)}**\n"
        f"- Total Income: **{_fmt_r(income)}**\n"
        f"- Total Expenses: **{_fmt_r(expenses)}**\n"
        f"- Drawings: **{_fmt_r(drawings)}**\n\n"
        f"Enter the closing Owner's Equity in Rand."
    )
    ans = _fmt_r(oe)
    sol = (
        f"**{ans}** [4 marks]\n\n"
        f"**Working:**\n"
        f"1. **Net Profit** = $\\text{{Income}} - \\text{{Expenses}} = {income} - {expenses} = {profit}$ [1 mark]\n"
        f"2. **Owner's Equity** = $\\text{{Capital}} + \\text{{Profit}} - \\text{{Drawings}}$ [1 mark]\n"
        f"   $$= {capital} + {profit} - {drawings} = {oe}$$ [2 marks]"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_18",
        subskill="18_owners_equity_formula_capital_profit_drawings",
        title="Owner's Equity Calculation",
        prompt=prompt,
        expected_answer=ans,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "First find Net Profit = Income - Expenses.",
            "tier_2": "Owner's Equity = Capital + Net Profit - Drawings.",
            "tier_3": f"Closing Owner's Equity = {ans}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Profit calculated: {_fmt_r(profit)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Applies Capital + Profit - Drawings", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Final Owner's Equity: {ans}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_drawings_to_owners_equity"],
    )


def arch_19_accounting_equation_a_equals_oe_plus_l(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    c_amt = rng.randint(20, 60) * 1000
    s_amt = rng.randint(5, 18) * 500
    e_amt = rng.randint(2, 9) * 300
    eq_items = [
        (f"{sc['entrepreneur']} invested {_fmt_r(c_amt)} capital into the business bank account.", "Bank", "Capital", f"+{c_amt}", f"+{c_amt}", "0"),
        (f"Received {_fmt_r(s_amt)} cash for services rendered.", "Bank", "Current Income", f"+{s_amt}", f"+{s_amt}", "0"),
        (f"Paid {_fmt_r(e_amt)} via EFT for weekly wages.", "Wages", "Bank", f"-{e_amt}", f"-{e_amt}", "0"),
    ]
    headers = ["Transaction", "Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Transaction | Account Debited | Account Credited | A | OE | L |", "| --- | --- | --- | --- | --- | --- |"]

    for r_i, (desc, dr, cr, a_v, oe_v, l_v) in enumerate(eq_items):
        correct_map[f"t0_r{r_i}_c1"] = dr
        correct_map[f"t0_r{r_i}_c2"] = cr
        correct_map[f"t0_r{r_i}_c3"] = a_v
        correct_map[f"t0_r{r_i}_c4"] = oe_v
        correct_map[f"t0_r{r_i}_c5"] = l_v
        cell_hints[f"t0_r{r_i}_c1"] = f"Identify which account receives the Debit entry under DEAD CLIC."
        cell_hints[f"t0_r{r_i}_c2"] = f"Identify which account receives the Credit entry under DEAD CLIC."
        cell_hints[f"t0_r{r_i}_c3"] = f"Show +amount or -amount effect on Assets ({a_v})."
        cell_hints[f"t0_r{r_i}_c4"] = f"Show +amount or -amount effect on Owner's Equity ({oe_v})."
        cell_hints[f"t0_r{r_i}_c5"] = "If no external debt changed, enter 0."
        rows.append([
            {"coordinate": f"t0_r{r_i}_c0", "cell_id": f"t0_r{r_i}_c0", "value": desc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{r_i}_c1", "cell_id": f"t0_r{r_i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{r_i}_c2", "cell_id": f"t0_r{r_i}_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{r_i}_c3", "cell_id": f"t0_r{r_i}_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{r_i}_c4", "cell_id": f"t0_r{r_i}_c4", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{r_i}_c5", "cell_id": f"t0_r{r_i}_c5", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {desc} | **{dr}** | **{cr}** | **{a_v}** | **{oe_v}** | **{l_v}** |")

    worked = "**Accounting Equation Schedule Memorandum** [15 marks]:\n\n" + "\n".join(md_lines)
    sample = f"Row1: Bank/Capital (+{c_amt}); Row2: Bank/Current Income (+{s_amt}); Row3: Wages/Bank (-{e_amt})"
    return _build_table(
        rng,
        qid_prefix="g8_gl_19",
        subskill="19_accounting_equation_a_equals_oe_plus_l",
        title="Accounting Equation Analysis Table",
        prompt=f"Complete the Accounting Equation analysis table for **{sc['entrepreneur']}'s {sc['business_type']}** (`A = OE + L`), showing `+`/`-` effects with amounts or `0` where unaffected.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=15,
        hints={
            "tier_1": "Check whether Bank increases (+A) or decreases (-A), and identify the matching contra account.",
            "tier_2": "Capital and Current Income increase OE; Expenses (Wages) decrease OE.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Transaction {i+1} double entry and A=OE+L signs", "marks": 5, "editable": True} for i in range(3)],
        misconception_tags=["wrong_sign_on_expense_oe_effect"],
    )


def arch_20_contra_account_cross_referencing_details(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(15, 75) * 100
    case = rng.choice([
        ("Capital", "Bank", f"{sc['entrepreneur']} invested {_fmt_r(amt)} capital into the business bank account", "Credit side of Capital", "Bank"),
        ("Wages", "Bank", f"paid {_fmt_r(amt)} wages from Bank", "Debit side of Wages", "Bank"),
        ("Bank", "Rent Income", f"received {_fmt_r(amt)} rent income into Bank", "Debit side of Bank", "Rent Income"),
        ("Bank", "Drawings", f"{sc['entrepreneur']} withdrew {_fmt_r(amt)} from Bank for personal use", "Credit side of Bank", "Drawings"),
    ])
    target_acc, contra_acc, tx, side_desc, expected_det = case
    prompt = (
        f"A transaction occurred at **{sc['entrepreneur']}'s {sc['business_type']}**: **{tx}**.\n\n"
        f"When recording this entry on the **{side_desc}** T-account, what exact account name must be written in the **Details** column?"
    )
    wrongs = [target_acc, f"{target_acc} Cash", "Balance b/d"]
    if target_acc == expected_det:
        wrongs = ["Balance c/d", "Cash Flow", "Owner Details"]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_20",
        subskill="20_contra_account_cross_referencing_details",
        title="Contra Account Details Cross-Reference",
        prompt=prompt,
        correct_text=expected_det,
        distractors=wrongs,
        explanation=f"In double-entry General Ledger cross-referencing, you **never** write the account's own name (`{target_acc}`) in its Details column; you always write the name of the **contra account** (`{expected_det}`).",
        hints={
            "tier_1": "Never write the T-account's own heading in its Details column.",
            "tier_2": f"Write the other (contra) account affected by the {_fmt_r(amt)} transaction.",
            "tier_3": f"Details must state: {expected_det}.",
        },
        misconception_tags=["writing_self_account_in_details"],
    )


def arch_21_crj_total_posting_bank_and_current_income(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cur_inc = rng.randint(18, 52) * 500
    sundry_cap = rng.randint(10, 30) * 1000
    bank_tot = cur_inc + sundry_cap
    prompt = (
        f"At the end of June, the **Cash Receipts Journal (CRJ)** of **{sc['entrepreneur']}'s {sc['business_type']}** shows column totals:\n"
        f"- **Bank column total:** {_fmt_r(bank_tot)}\n"
        f"- **Current Income column total:** {_fmt_r(cur_inc)}\n\n"
        f"How are these two dedicated column totals posted to the General Ledger?"
    )
    correct = f"On 30 June, Debit Bank with {_fmt_r(bank_tot)} (Total Receipts CRJ) and Credit Current Income with {_fmt_r(cur_inc)} (Bank CRJ)."
    distractors = [
        f"On 30 June, Credit Bank with {_fmt_r(bank_tot)} and Debit Current Income with {_fmt_r(cur_inc)}.",
        f"Post every daily receipt slip individually to Bank instead of using the {_fmt_r(bank_tot)} monthly total.",
        f"Post {_fmt_r(bank_tot)} to Current Income Debit and leave Bank out of the General Ledger.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_21",
        subskill="21_crj_total_posting_bank_and_current_income",
        title="Posting CRJ Column Totals",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"CRJ dedicated column totals are posted on the **last day of the month** (30 June): Bank increases on the **Debit** side ({_fmt_r(bank_tot)}), and Current Income increases on the **Credit** side ({_fmt_r(cur_inc)}).",
        hints={
            "tier_1": "CRJ increases Bank (Debit) and records earned Income (Credit).",
            "tier_2": "Dedicated CRJ column totals are posted once at month-end.",
            "tier_3": correct,
        },
        misconception_tags=["crj_posting_side_reversal"],
    )


def arch_22_cpj_total_posting_bank_and_special_columns(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    wages = rng.randint(8, 22) * 500
    stat = rng.randint(1, 6) * 400
    sundry_eq = rng.randint(4, 15) * 500
    bank_tot = wages + stat + sundry_eq
    prompt = (
        f"At 31 July, the **Cash Payments Journal (CPJ)** of **{sc['entrepreneur']}'s {sc['business_type']}** has the following totals:\n"
        f"- **Bank column total:** {_fmt_r(bank_tot)}\n"
        f"- **Wages column total:** {_fmt_r(wages)}\n"
        f"- **Stationery column total:** {_fmt_r(stat)}\n\n"
        f"On which date and which side are these three special column totals posted in the General Ledger?"
    )
    expected = f"31 July (month-end): Bank Credited ({_fmt_r(bank_tot)}); Wages Debited ({_fmt_r(wages)}); Stationery Debited ({_fmt_r(stat)})"
    sol = (
        f"**{expected}** [4 marks]\n\n"
        f"**Posting Breakdown:**\n"
        f"- **Date:** 31 July (last day of the month for all dedicated column totals) [1 mark].\n"
        f"- **Bank:** **Credit** {_fmt_r(bank_tot)} (payments decrease the Asset Bank) [1 mark].\n"
        f"- **Wages:** **Debit** {_fmt_r(wages)} (Expense increases on Debit) [1 mark].\n"
        f"- **Stationery:** **Debit** {_fmt_r(stat)} (Expense increases on Debit) [1 mark]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gl_22",
        subskill="22_cpj_total_posting_bank_and_special_columns",
        title="Posting CPJ Special Column Totals",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        qtype="short_answer",
        hints={
            "tier_1": "CPJ records payments, so Bank decreases (Credit).",
            "tier_2": "Expenses like Wages and Stationery increase on Debit; special column totals post at month-end.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Month-end posting date (31 July)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Bank Credited {_fmt_r(bank_tot)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Wages Debited {_fmt_r(wages)}", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Stationery Debited {_fmt_r(stat)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["cpj_debit_bank_error"],
    )


def arch_23_sundry_accounts_individual_posting_dates(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap_amt = rng.randint(15, 45) * 1000
    rent_amt = rng.randint(2, 7) * 500
    d1, d2 = rng.randint(2, 9), rng.randint(14, 26)
    prompt = (
        f"In the CRJ of **{sc['entrepreneur']}'s {sc['business_type']}** for August, the **Sundry Accounts** column contains two entries:\n"
        f"- August {d1}: Capital, {_fmt_r(cap_amt)}\n"
        f"- August {d2}: Rent Income, {_fmt_r(rent_amt)}\n\n"
        f"Why must the Sundry Accounts column total (**{_fmt_r(cap_amt + rent_amt)}**) **NOT** be posted as one lump sum at month-end?"
    )
    correct = f"Because the Sundry column contains different unrelated accounts (Capital on Aug {d1} and Rent Income on Aug {d2}); each item must be posted individually on its specific transaction date."
    distractors = [
        f"Because Sundry entries are posted only once a year when the auditor visits on December 31.",
        f"Because the {_fmt_r(cap_amt + rent_amt)} total belongs solely on the Debit side of the Wages account.",
        f"Because Capital and Rent Income are already included inside the Current Income column total.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_23",
        subskill="23_sundry_accounts_individual_posting_dates",
        title="Sundry Accounts Individual Posting Rule",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="The **Sundry Accounts** column acts as a catch-all for miscellaneous accounts without dedicated columns. Therefore you never post the Sundry total; each line is posted **individually on the specific date of the transaction**.",
        hints={
            "tier_1": "Notice that Capital (Equity) and Rent Income (Income) are completely different T-accounts.",
            "tier_2": "Sundry entries must be posted individually on each transaction's actual day.",
            "tier_3": correct,
        },
        misconception_tags=["posting_sundry_column_total_error"],
    )


def arch_24_journal_column_to_ledger_posting_rules_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    spec_cpj = rng.choice(["CPJ - Wages", "CPJ - Stationery", "CPJ - Consumable goods"])
    items = [
        ("CRJ - Bank", "Debit", "Monthly total", "Month-end"),
        ("CRJ - Current Income", "Credit", "Monthly total", "Month-end"),
        ("CRJ - Sundry Accounts", "Credit", "Individual amounts", "Transaction date"),
        ("CPJ - Bank", "Credit", "Monthly total", "Month-end"),
        (spec_cpj, "Debit", "Monthly total", "Month-end"),
        ("CPJ - Sundry Accounts", "Debit", "Individual amounts", "Transaction date"),
    ]
    rng.shuffle(items)
    selected = items[:4]
    headers = ["Journal Column", "Ledger Side (Debit / Credit)", "Amount Posted (Monthly total / Individual amounts)", "Posting Date (Month-end / Transaction date)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Journal Column | Ledger Side | Amount Posted | Posting Date |", "| --- | --- | --- | --- |"]

    for idx, (col, side, amt_type, pdate) in enumerate(selected):
        correct_map[f"t0_r{idx}_c1"] = side
        correct_map[f"t0_r{idx}_c2"] = amt_type
        correct_map[f"t0_r{idx}_c3"] = pdate
        cell_hints[f"t0_r{idx}_c1"] = f"Determine whether {col} increases Assets/Expenses (Debit) or Equity/Income or decreases Bank (Credit)."
        cell_hints[f"t0_r{idx}_c2"] = "Special columns post 'Monthly total'; Sundry columns post 'Individual amounts'."
        cell_hints[f"t0_r{idx}_c3"] = "Special column totals use 'Month-end'; Sundry items use 'Transaction date'."
        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "cell_id": f"t0_r{idx}_c0", "value": col, "type": "given", "editable": False},
            {"coordinate": f"t0_r{idx}_c1", "cell_id": f"t0_r{idx}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c2", "cell_id": f"t0_r{idx}_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c3", "cell_id": f"t0_r{idx}_c3", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {col} | **{side}** | **{amt_type}** | **{pdate}** |")

    worked = "**Summary of CRJ & CPJ Posting Rules** [12 marks]:\n\n" + "\n".join(md_lines)
    sample = "; ".join(f"{c}: {s}/{a}/{d}" for c, s, a, d in selected)
    return _build_table(
        rng,
        qid_prefix="g8_gl_24",
        subskill="24_journal_column_to_ledger_posting_rules_table",
        title="CRJ & CPJ to General Ledger Posting Rules Table",
        prompt=f"Complete the posting rule schedule for **{sc['entrepreneur']}'s {sc['business_type']}** indicating the **Ledger Side**, **Amount Posted**, and **Posting Date** for each journal column.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=12,
        hints={
            "tier_1": "Dedicated columns post totals at month-end; Sundry posts individual lines on transaction dates.",
            "tier_2": "CRJ Bank -> Dr; CRJ Income -> Cr; CPJ Bank -> Cr; CPJ Expenses -> Dr.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Rule for {selected[i][0]}", "marks": 3, "editable": True} for i in range(4)],
        misconception_tags=["posting_sundry_column_total_error", "cpj_debit_bank_error"],
    )


def arch_25_reconstructing_transaction_from_ledger_posting(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(6, 48) * 250
    day = rng.randint(4, 27)
    amt_str = f"{amt:,}".replace(",", " ")
    case = rng.choice([
        ("Equipment", [(f"Sep {day}", "Bank (CPJ)", amt_str)], [], f"{sc['entrepreneur']} purchased Equipment for {_fmt_r(amt)} cash/EFT via the CPJ on {day} September."),
        ("Rent Income", [], [(f"Sep {day}", "Bank (CRJ)", amt_str)], f"The business received {_fmt_r(amt)} rent income from a tenant into Bank via the CRJ on {day} September."),
        ("Drawings", [(f"Sep {day}", "Bank (CPJ)", amt_str)], [], f"{sc['entrepreneur']} withdrew {_fmt_r(amt)} from the business bank account for personal use on {day} September."),
    ])
    acc_name, dr_l, cr_l, correct = case
    svg = _t_account_svg(f"{acc_name}", dr_l, cr_l, accent="#0f766e")
    distractors = [
        f"{sc['entrepreneur']} invested {_fmt_r(amt)} additional personal Capital on {day} September.",
        f"The business earned {_fmt_r(amt)} from routine service fees recorded in Current Income on {day} September.",
        f"The business repaid {_fmt_r(amt)} toward an external bank Loan on {day} September.",
    ]
    prompt = (
        f"Examine the General Ledger T-account diagram for **{acc_name}** showing an entry of **R{amt_str}** on **Sep {day}**.\n\n"
        f"Which original business transaction occurred at **{sc['entrepreneur']}'s {sc['business_type']}**?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g8_gl_25",
        subskill="25_reconstructing_transaction_from_ledger_posting",
        title="Reconstructing Transaction from T-Account",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"The **{acc_name}** T-account shows **{amt_str}** with contra account **Bank** on **Sep {day}**, meaning: {correct}",
        hints={
            "tier_1": "Read the account heading, the Debit vs Credit side, and the contra account name.",
            "tier_2": f"Contra account Bank shows cash moved in ({'CRJ' if cr_l else 'CPJ'}) affecting {acc_name}.",
            "tier_3": correct,
        },
        misconception_tags=["contra_account_interpretation_error"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25 = {
    "01_accounting_cycle_stage_sequencing": arch_01_accounting_cycle_stage_sequencing,
    "02_general_ledger_purpose_and_journal_link": arch_02_general_ledger_purpose_and_journal_link,
    "03_double_entry_principle_duality": arch_03_double_entry_principle_duality,
    "04_t_account_structure_debit_credit_sides": arch_04_t_account_structure_debit_credit_sides,
    "05_balance_sheet_vs_nominal_sections": arch_05_balance_sheet_vs_nominal_sections,
    "06_folio_numbering_system_b_and_n": arch_06_folio_numbering_system_b_and_n,
    "07_dead_mnemonic_debit_increase_accounts": arch_07_dead_mnemonic_debit_increase_accounts,
    "08_clic_mnemonic_credit_increase_accounts": arch_08_clic_mnemonic_credit_increase_accounts,
    "09_account_normal_balance_classification_table": arch_09_account_normal_balance_classification_table,
    "10_bank_account_asset_receipts_and_payments": arch_10_bank_account_asset_receipts_and_payments,
    "11_capital_contribution_double_entry": arch_11_capital_contribution_double_entry,
    "12_drawings_owner_withdrawal_double_entry": arch_12_drawings_owner_withdrawal_double_entry,
    "13_service_fee_current_income_double_entry": arch_13_service_fee_current_income_double_entry,
    "14_rent_income_received_double_entry": arch_14_rent_income_received_double_entry,
    "15_expense_payment_wages_or_telephone_double_entry": arch_15_expense_payment_wages_or_telephone_double_entry,
    "16_asset_purchase_equipment_or_vehicle_double_entry": arch_16_asset_purchase_equipment_or_vehicle_double_entry,
    "17_loan_received_and_repayment_liability_entry": arch_17_loan_received_and_repayment_liability_entry,
    "18_owners_equity_formula_capital_profit_drawings": arch_18_owners_equity_formula_capital_profit_drawings,
    "19_accounting_equation_a_equals_oe_plus_l": arch_19_accounting_equation_a_equals_oe_plus_l,
    "20_contra_account_cross_referencing_details": arch_20_contra_account_cross_referencing_details,
    "21_crj_total_posting_bank_and_current_income": arch_21_crj_total_posting_bank_and_current_income,
    "22_cpj_total_posting_bank_and_special_columns": arch_22_cpj_total_posting_bank_and_special_columns,
    "23_sundry_accounts_individual_posting_dates": arch_23_sundry_accounts_individual_posting_dates,
    "24_journal_column_to_ledger_posting_rules_table": arch_24_journal_column_to_ledger_posting_rules_table,
    "25_reconstructing_transaction_from_ledger_posting": arch_25_reconstructing_transaction_from_ledger_posting,
}
