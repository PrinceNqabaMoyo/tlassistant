"""Grade 7 EMS — Savings: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards (Term 4: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 4/01. Savings.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term4_savings"
TOPIC_NAME = "Savings"
CURRICULUM_REF = "Term 4 > Financial Literacy: Savings"
BANKS_SA = ["Standard Bank", "First National Bank (FNB)", "Nedbank", "Absa", "Capitec"]


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
        "grade": 7,
        "subject": "Economic and Management Sciences",
        "term": 4,
        "caps_weight_percent": 20,
        "suggested_duration_mins": duration_mins,
        "curriculum_reference": CURRICULUM_REF,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "concept_group": "savings_and_banking",
        "marks": marks,
        "total_marks": marks,
        "misconception_tags": misconception_tags,
        "diagnostic_tags": diagnostic_tags or ["savings_and_banking"],
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
        "id": f"g7_ems_sav_{subskill[:12]}_{rng.randint(100000, 999999)}",
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
        "id": f"g7_ems_sav_{subskill[:12]}_{rng.randint(100000, 999999)}",
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
                ui_row.append({"id": cell_id, "type": "given", "value": val, "label": headers[c_idx]})
                md_cells.append(val)
            elif ctype == "required":
                exp = str(cell["expected"])
                ui_row.append({"id": cell_id, "type": "required", "value": "", "expected": exp, "label": headers[c_idx]})
                correct_map[cell_id] = exp
                marking_points.append({"id": f"mp_{mp_idx}", "desc": f"{headers[c_idx]} (Row {r_idx + 1}): {exp}", "marks": 1, "editable": True})
                mp_idx += 1
                md_cells.append(f"**{exp}**")
            else:
                has_must_be_empty = True
                ui_row.append({"id": cell_id, "type": "must_be_empty", "value": "", "expected": "", "label": headers[c_idx]})
                correct_map[cell_id] = ""
                md_cells.append("*(blank)*")
        rows.append(ui_row)
        md_rows.append("| " + " | ".join(md_cells) + " |")

    marks = max(1, len(marking_points))
    md_table = "\n".join(md_rows)
    deriv_text = "\n".join(f"- {d}" for d in derivations)
    memo = f"{md_table}\n\n**Derivations & Rules:**\n{deriv_text}"
    deductions = [{"rule": "must_be_empty_filled", "penalty": -1}] if has_must_be_empty else []

    return {
        **_base_meta(subskill, learning_objective_id, concept_id, marks, max(4, marks), misconception_tags),
        "id": f"g7_ems_sav_tbl_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
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


def _svg_cycle_flow(
    title: str,
    nodes: List[str],
    accent_color: str = "#1D4ED8",
) -> str:
    w, h = 640, 260
    coords = [(115, 65), (525, 65), (525, 195), (115, 195)]
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:640px;background:#FFFFFF;font-family:Arial,sans-serif;">',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#FAF8F3" stroke="#CBD5E1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">{title}</text>',
        '<defs><marker id="arr_sav" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#334155"/></marker></defs>',
        '<line x1="215" y1="65" x2="418" y2="65" stroke="#334155" stroke-width="2" marker-end="url(#arr_sav)"/>',
        '<line x1="525" y1="95" x2="525" y2="160" stroke="#334155" stroke-width="2" marker-end="url(#arr_sav)"/>',
        '<line x1="425" y1="195" x2="222" y2="195" stroke="#334155" stroke-width="2" marker-end="url(#arr_sav)"/>',
        '<line x1="115" y1="165" x2="115" y2="100" stroke="#334155" stroke-width="2" marker-end="url(#arr_sav)"/>',
    ]
    for i, (cx, cy) in enumerate(coords):
        text = nodes[i]
        part1 = text[:28]
        part2 = text[28:56].strip()
        lines.append(f'<rect x="{cx-95}" y="{cy-26}" width="190" height="52" rx="8" fill="#EFF6FF" stroke="{accent_color}" stroke-width="2"/>')
        if part2:
            lines.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">{part1}</text>')
            lines.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">{part2}</text>')
        else:
            lines.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0F172A">{part1}</text>')
    lines.append("</svg>")
    return "".join(lines)


def arch_01_personal_savings_definition(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    allowance = rng.choice([250, 300, 400, 500])
    prompt = (
        f"{name} earns {_fmt_zar(allowance)} per month from weekend tutoring and sets aside a fixed portion instead of "
        f"spending all of it on snacks and airtime.\n\n"
        f"Which economic definition BEST captures PERSONAL SAVINGS?"
    )
    correct = "Income left over after subtracting expenses, set aside safely for future needs, goals, or emergencies"
    distractors = [
        "Borrowing extra money from a store credit card whenever income runs out",
        "Spending every Rand earned immediately before prices can change",
        "Taxes paid to municipal councils for water and refuse removal",
    ]
    return _mcq(
        rng,
        subskill="01_personal_savings_definition",
        title="Definition of Personal Savings",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Personal savings equal Income minus Expenses kept aside for future security rather than consumed right away."
        ),
        hints={
            "tier_1": "Think of the formula linking Income, Expenses, and Savings.",
            "tier_2": "Savings represent unspent income preserved for future needs or emergencies.",
            "tier_3": "Select 'Income left over after subtracting expenses, set aside safely for future needs, goals, or emergencies'.",
        },
        learning_objective_id="lo_sav_definition",
        concept_id="personal_savings_def",
        misconception_tags=["confuses_savings_with_credit"],
    )


def arch_02_personal_savings_monthly_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    income = rng.choice([5400, 6200, 7500, 8400])
    expenses = rng.choice([4100, 4650, 5200, 5800])
    monthly_sav = income - expenses
    months = rng.choice([4, 6, 8])
    total_sav = monthly_sav * months
    prompt = (
        f"{name} receives a monthly net salary of {_fmt_zar(income)} and pays {_fmt_zar(expenses)} for rent, food, "
        f"and transport.\n\n"
        f"If {name} saves the full remaining monthly surplus every month for {months} months (excluding interest), "
        f"how much money will {name} accumulate?"
    )
    return _typed(
        rng,
        subskill="02_personal_savings_monthly_calculation",
        title="Calculating Monthly and Multi-Month Savings",
        prompt=prompt,
        sample_answer=(
            f"Monthly savings = {_fmt_zar(income)} - {_fmt_zar(expenses)} = {_fmt_zar(monthly_sav)}\n"
            f"Accumulated over {months} months = {_fmt_zar(monthly_sav)} x {months} = {_fmt_zar(total_sav)}"
        ),
        marking_points=[
            f"Compute monthly savings: {_fmt_zar(income)} - {_fmt_zar(expenses)} = {_fmt_zar(monthly_sav)} [1]",
            f"Multiply by {months} months = {_fmt_zar(total_sav)} [2]",
        ],
        hints={
            "tier_1": "Step 1: Find Monthly Savings = Income - Expenses.",
            "tier_2": f"Step 2: Multiply that monthly surplus by {months} months.",
            "tier_3": f"Monthly = {_fmt_zar(monthly_sav)}; Total = {_fmt_zar(monthly_sav)} x {months} = {_fmt_zar(total_sav)}.",
        },
        learning_objective_id="lo_sav_monthly_calc",
        concept_id="monthly_savings_calc",
        misconception_tags=["forgets_to_multiply_by_months"],
        marks=3,
        correct_answer=_fmt_zar(total_sav),
        correct_value=float(total_sav),
        worked_solution=f"Monthly = {income - expenses}; Total ({months}m) = {_fmt_zar(total_sav)}",
    )


def arch_03_personal_savings_budget_ledger_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    wages = rng.choice([3600, 4200, 4800])
    tutor = rng.choice([600, 800, 1000])
    tot_inc = wages + tutor
    groceries = rng.choice([1800, 2000, 2200])
    transport = rng.choice([700, 850, 950])
    tot_exp = groceries + transport
    savings = tot_inc - tot_exp

    headers = ["Personal Budget Line", "Monthly Amount (R)", "Category Summary (R)", "Review Flag"]
    raw_rows = [
        [
            {"type": "given", "value": "Part-Time Wages"},
            {"type": "given", "value": _fmt_zar(wages)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Weekend Tutoring Income"},
            {"type": "given", "value": _fmt_zar(tutor)},
            {"type": "required", "expected": _fmt_zar(tot_inc)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Groceries & Utilities"},
            {"type": "given", "value": _fmt_zar(groceries)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Taxi & Data Expenses"},
            {"type": "given", "value": _fmt_zar(transport)},
            {"type": "required", "expected": _fmt_zar(tot_exp)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Net Monthly Savings Surplus"},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(savings)},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r1_c2": f"Add wages ({_fmt_zar(wages)}) and tutoring ({_fmt_zar(tutor)}).",
        "r3_c2": f"Add groceries ({_fmt_zar(groceries)}) and transport ({_fmt_zar(transport)}).",
        "r4_c2": "Subtract Total Expenses from Total Income.",
    }
    derivations = [
        f"Total Income = {_fmt_zar(wages)} + {_fmt_zar(tutor)} = {_fmt_zar(tot_inc)}",
        f"Total Expenses = {_fmt_zar(groceries)} + {_fmt_zar(transport)} = {_fmt_zar(tot_exp)}",
        f"Monthly Savings = {_fmt_zar(tot_inc)} - {_fmt_zar(tot_exp)} = {_fmt_zar(savings)}",
    ]
    return _table_q(
        rng,
        subskill="03_personal_savings_budget_ledger_table",
        title="Household Monthly Savings Budget Ledger",
        prompt=(
            f"Complete {name}'s monthly personal savings schedule in {area} by computing Total Income, Total Expenses, "
            f"and Net Monthly Savings Surplus. Leave shaded cells and 'Review Flag' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "First group the two income rows and two expense rows separately.",
            "tier_2": "Monthly Savings Surplus = Total Income - Total Expenses.",
            "tier_3": f"Total Income={_fmt_zar(tot_inc)}; Total Expenses={_fmt_zar(tot_exp)}; Savings={_fmt_zar(savings)}.",
        },
        learning_objective_id="lo_sav_budget_ledger",
        concept_id="savings_budget_table",
        misconception_tags=["adds_expenses_to_income", "fills_must_be_empty_cell"],
    )


def arch_04_purpose_saving_avoiding_high_interest_credit(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    item = rng.choice(["winter school blazer", "study tablet", "hiking jacket"])
    cash_price = rng.choice([1200, 1800, 2400])
    prompt = (
        f"{name} wants a {item} priced at {_fmt_zar(cash_price)} and considers using a retail store credit card "
        f"charging 22% annual interest instead of saving cash for three months.\n\n"
        f"What is the PRIMARY financial benefit of saving cash before buying?"
    )
    correct = (
        "You avoid expensive store-card interest fees and keep more money while earning interest on your savings"
    )
    distractors = [
        "Store credit cards pay cash bonuses to buyers who miss monthly instalments",
        "Paying in cash forces shops to double the price tag at the till",
        "Interest-bearing debt increases household net worth faster than saving",
    ]
    return _mcq(
        rng,
        subskill="04_purpose_saving_avoiding_high_interest_credit",
        title="Saving Cash vs High-Interest Store Credit",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Buying a {_fmt_zar(cash_price)} {item} with saved cash avoids 22% credit-card interest charges and keeps "
            f"{name} debt-free."
        ),
        hints={
            "tier_1": "Compare earning interest in a savings account against paying 22% interest on store credit.",
            "tier_2": "Saving beforehand turns interest from an expense into a reward.",
            "tier_3": "Select 'You avoid expensive store-card interest fees and keep more money while earning interest on your savings'.",
        },
        learning_objective_id="lo_sav_avoid_debt",
        concept_id="avoiding_high_interest_credit",
        misconception_tags=["underestimates_store_card_interest_cost"],
    )


def arch_05_cash_vs_credit_purchase_cost_bar_graph(rng: random.Random) -> Dict[str, Any]:
    cash_price = rng.choice([3000, 3600, 4200])
    credit_total = int(round(cash_price * rng.choice([1.25, 1.30, 1.35])))
    extra_paid = credit_total - cash_price

    svg = _svg_bar_chart(
        title="Total Cost: Saved Cash vs 12-Month Store Credit (R)",
        y_label="Total Rand Paid (R)",
        bars=[
            ("Saved Cash", float(cash_price), "#15803D"),
            ("Store Credit", float(credit_total), "#DC2626"),
        ],
        max_val=float(max(6000, credit_total + 600)),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below comparing buying a study laptop with Saved Cash ({_fmt_zar(cash_price)}) versus "
        f"12-Month Store Credit ({_fmt_zar(credit_total)}).\n\n"
        f"Calculate how much extra Rand is wasted on interest and fees by buying on Store Credit instead of saving cash."
    )
    return _typed(
        rng,
        subskill="05_cash_vs_credit_purchase_cost_bar_graph",
        title="Cash Savings vs Store Credit Penalty (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Extra interest/fees paid = {_fmt_zar(credit_total)} - {_fmt_zar(cash_price)} = {_fmt_zar(extra_paid)}.",
        marking_points=[
            f"Read Store Credit ({_fmt_zar(credit_total)}) and Saved Cash ({_fmt_zar(cash_price)}) correctly [1]",
            f"Compute savings = {_fmt_zar(credit_total)} - {_fmt_zar(cash_price)} = {_fmt_zar(extra_paid)} [2]",
        ],
        hints={
            "tier_1": "Find the difference between the red Store Credit bar and the green Saved Cash bar.",
            "tier_2": f"Subtract {_fmt_zar(cash_price)} from {_fmt_zar(credit_total)}.",
            "tier_3": f"{_fmt_zar(credit_total)} - {_fmt_zar(cash_price)} = {_fmt_zar(extra_paid)}.",
        },
        learning_objective_id="lo_sav_cash_vs_credit_graph",
        concept_id="cash_vs_credit_bar_graph",
        misconception_tags=["adds_both_bars_together"],
        marks=3,
        correct_answer=_fmt_zar(extra_paid),
        correct_value=float(extra_paid),
        diagram_spec={"kind": "inline_svg", "title": "Cash vs Store Credit Total Cost", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Interest penalty saved = {credit_total} - {cash_price} = {_fmt_zar(extra_paid)}",
    )


def arch_06_purpose_saving_short_medium_long_term_goals(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    goal = rng.choice([
        ("saving over 18 years to buy a family home and fund retirement", "Long-term goal (over 5 years)"),
        ("saving for 3 months to buy running shoes for school athletics", "Short-term goal (under 1 year)"),
    ])
    desc, correct = goal
    if "Long-term" in correct:
        distractors = [
            "Short-term goal (under 6 months)",
            "Daily petty-cash impulse purchase",
            "Overdraft emergency penalty",
        ]
    else:
        distractors = [
            "Long-term retirement pension fund (30+ years)",
            "Decade-long commercial factory mortgage",
            "Multi-generational infrastructure bond",
        ]
    prompt = (
        f"{name} sets a financial target of {desc}.\n\n"
        f"How is this savings goal classified by time horizon?"
    )
    return _mcq(
        rng,
        subskill="06_purpose_saving_short_medium_long_term_goals",
        title="Classifying Short- vs Long-Term Savings Goals",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Goals under 1 year (shoes, books) are short-term; 1–5 year goals (appliances, car deposit) are medium-term; "
            "and 5+ year goals (housing, university fees, retirement) are long-term."
        ),
        hints={
            "tier_1": "Check how many months or years are required to reach the goal.",
            "tier_2": "Under 1 year = short-term; 1–5 years = medium-term; 5+ years = long-term.",
            "tier_3": f"Select '{correct}'.",
        },
        learning_objective_id="lo_sav_goal_horizons",
        concept_id="savings_goal_horizons",
        misconception_tags=["confuses_short_and_long_term_goals"],
    )


def arch_07_purpose_saving_emergency_fund(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    cost = rng.choice([1800, 2400, 3200])
    prompt = (
        f"A burst household geyser in {area} unexpectedly requires {_fmt_zar(cost)} in urgent plumbing repairs.\n\n"
        f"Explain TWO reasons why having a dedicated emergency savings fund helps {name}'s household handle shocks "
        f"like this better than borrowing urgently."
    )
    return _typed(
        rng,
        subskill="07_purpose_saving_emergency_fund",
        title="Role of an Emergency Savings Fund",
        prompt=prompt,
        sample_answer=(
            f"1. Immediate liquidity: {name} can pay the {_fmt_zar(cost)} repair right away without delaying essential water and electricity.\n"
            "2. Debt protection: The family avoids expensive short-term payday/informal loans and high interest repayments in future months."
        ),
        marking_points=[
            f"Provides instant cash ({_fmt_zar(cost)}) to resolve urgent household emergencies immediately [1]",
            "Prevents trapping the household in high-interest emergency debt [1]",
        ],
        hints={
            "tier_1": "Think about speed of payment AND avoiding emergency loans.",
            "tier_2": "Emergency reserves give peace of mind without crippling interest charges.",
            "tier_3": "State two points: instant payment for urgent repairs, and avoiding expensive emergency debt.",
        },
        learning_objective_id="lo_sav_emergency_fund",
        concept_id="emergency_fund",
        misconception_tags=["relies_on_credit_for_emergencies"],
        marks=2,
    )


def arch_08_purpose_saving_inflation_and_purchasing_power(rng: random.Random) -> Dict[str, Any]:
    infl = rng.choice(["6%", "7%"])
    prompt = (
        f"When consumer price inflation averages {infl} per year, groceries and school textbooks cost more next year "
        f"than they cost today.\n\n"
        f"Why is keeping idle banknotes hidden in a tin box worse against inflation than placing them in an interest-bearing savings product?"
    )
    correct = (
        "Hidden cash earns 0% interest and loses purchasing power every year, whereas bank interest helps savings keep pace with rising prices"
    )
    distractors = [
        "Banknotes locked inside a tin box automatically multiply in number every winter",
        "Inflation lowers all food and textbook prices whenever cash stays at home",
        "Savings accounts deduct 50% of principal balances monthly to fight inflation",
    ]
    return _mcq(
        rng,
        subskill="08_purpose_saving_inflation_and_purchasing_power",
        title="Inflation and Protecting Purchasing Power",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"At {infl} inflation, cash stuffed at home buys less every year. Earning competitive interest in a bank "
            f"account or money market fund offsets or beats inflation."
        ),
        hints={
            "tier_1": "What happens to the buying power of R100 hidden under a mattress when prices rise?",
            "tier_2": "0% return loses value to inflation; earning interest defends real purchasing power.",
            "tier_3": "Select the option explaining hidden cash earns 0% and loses purchasing power while interest helps offset inflation.",
        },
        learning_objective_id="lo_sav_inflation_protection",
        concept_id="inflation_purchasing_power",
        misconception_tags=["thinks_cash_at_home_keeps_constant_value"],
    )


def arch_09_purpose_saving_education_and_retirement(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    years_ed = rng.randint(10, 12)
    prompt = (
        f"{name}'s parents save small amounts monthly for {years_ed} years toward university fees, while {name}'s "
        f"older cousin contributes to a workplace retirement fund.\n\n"
        f"Explain TWO distinct benefits of long-term saving for (1) further education and (2) retirement."
    )
    return _typed(
        rng,
        subskill="09_purpose_saving_education_and_retirement",
        title="Saving for Education and Retirement",
        prompt=prompt,
        sample_answer=(
            f"1. Education savings ({years_ed} years): Avoids heavy student debt and equips young people with scarce skills for higher lifelong earnings.\n"
            "2. Retirement savings: Replaces monthly salary after stopping work so elderly citizens live independently with dignity rather than relying solely on grants or family."
        ),
        marking_points=[
            "Education savings cover tuition/books without crushing debt and expand future career earnings [1]",
            "Retirement savings preserve financial independence and living standards after leaving the workforce [1]",
        ],
        hints={
            "tier_1": "Explain one long-term benefit for youth education AND one for post-work old age.",
            "tier_2": "Focus on avoiding student debt/raising skills, and maintaining independent income in old age.",
            "tier_3": "Cover both education (debt-free skills/higher income) and retirement (independent post-work income).",
        },
        learning_objective_id="lo_sav_edu_and_retirement",
        concept_id="education_retirement_savings",
        misconception_tags=["omits_either_education_or_retirement"],
        marks=2,
    )


def arch_10_savings_growth_over_time_bar_graph(rng: random.Random) -> Dict[str, Any]:
    y1 = rng.choice([2400, 3000, 3600])
    y2 = int(round(y1 * 2 + 180))
    y3 = int(round(y1 * 3 + 480))
    y4 = int(round(y1 * 4 + 920))
    gain = y4 - y1

    svg = _svg_bar_chart(
        title="Cumulative Savings Balance Over 4 Years (R)",
        y_label="Total Balance (R)",
        bars=[
            ("Year 1", float(y1), "#93C5FD"),
            ("Year 2", float(y2), "#60A5FA"),
            ("Year 3", float(y3), "#2563EB"),
            ("Year 4", float(y4), "#15803D"),
        ],
        max_val=float(y4 + 2000),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below showing a learner's interest-bearing savings balance at the end of Year 1 "
        f"({_fmt_zar(y1)}), Year 2 ({_fmt_zar(y2)}), Year 3 ({_fmt_zar(y3)}), and Year 4 ({_fmt_zar(y4)}).\n\n"
        f"Calculate the total Rand growth in the account from Year 1 to Year 4."
    )
    return _typed(
        rng,
        subskill="10_savings_growth_over_time_bar_graph",
        title="Savings Growth Over Four Years (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Total growth (Year 1 to Year 4) = {_fmt_zar(y4)} - {_fmt_zar(y1)} = {_fmt_zar(gain)}.",
        marking_points=[
            f"Read Year 4 ({_fmt_zar(y4)}) and Year 1 ({_fmt_zar(y1)}) correctly [1]",
            f"Subtract {_fmt_zar(y1)} from {_fmt_zar(y4)} = {_fmt_zar(gain)} [2]",
        ],
        hints={
            "tier_1": "Locate the final green Year 4 bar and the first light-blue Year 1 bar.",
            "tier_2": f"Subtract {_fmt_zar(y1)} from {_fmt_zar(y4)}.",
            "tier_3": f"{_fmt_zar(y4)} - {_fmt_zar(y1)} = {_fmt_zar(gain)}.",
        },
        learning_objective_id="lo_sav_growth_bar_graph",
        concept_id="savings_growth_graph",
        misconception_tags=["subtracts_year_3_instead_of_year_1"],
        marks=3,
        correct_answer=_fmt_zar(gain),
        correct_value=float(gain),
        diagram_spec={"kind": "inline_svg", "title": "Cumulative Savings Balance Over 4 Years", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Growth = {y4} - {y1} = {_fmt_zar(gain)}",
    )


def arch_11_history_of_money_and_earliest_temple_banks(rng: random.Random) -> Dict[str, Any]:
    year_hint = rng.choice(["around 2000 BCE in ancient Mesopotamia", "four thousand years ago in ancient Babylon"])
    prompt = (
        f"Before modern commercial banking existed, merchants {year_hint} needed a secure place to store grain, silver, "
        f"and valuable trade goods.\n\n"
        f"Where did the earliest recorded banking activities begin?"
    )
    correct = "Ancient temples, where priests safeguarded grain and precious metals and issued early loans"
    distractors = [
        "Electronic smartphone apps running on solar Wi-Fi networks",
        "Automated plastic ATM kiosks along railway lines",
        "Stock exchanges trading digital cryptocurrencies in the 21st century",
    ]
    return _mcq(
        rng,
        subskill="11_history_of_money_and_earliest_temple_banks",
        title="Origins of Early Temple Banking",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Ancient temples around 2000 BCE were heavily guarded, respected public buildings where merchants deposited "
            "grain and metals — marking the earliest origins of safekeeping and lending."
        ),
        hints={
            "tier_1": "Think of the most heavily guarded, trusted buildings in ancient towns around 2000 BCE.",
            "tier_2": "Long before electronic banking or wooden benches in Italy, priests guarded grain and gold in temples.",
            "tier_3": "Select 'Ancient temples, where priests safeguarded grain and precious metals and issued early loans'.",
        },
        learning_objective_id="lo_sav_history_temples",
        concept_id="history_of_banking_temples",
        misconception_tags=["anachronistic_banking_timeline"],
    )


def arch_12_commodity_vs_representative_money_and_cheques(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"During an EMS heritage project in {area}, learners examine why societies shifted from gold coins to paper "
        f"banknotes/cheques and why Italian moneychangers used wooden benches (`banchi`).\n\n"
        f"Distinguish COMMODITY money from REPRESENTATIVE money, and explain where the English word 'bank' originates."
    )
    return _typed(
        rng,
        subskill="12_commodity_vs_representative_money_and_cheques",
        title="Commodity vs Representative Money & Origin of 'Bank'",
        prompt=prompt,
        sample_answer=(
            "1. Commodity money (e.g. cattle, salt, gold/silver coins) has intrinsic value in itself.\n"
            "2. Representative money (early paper receipts, banknotes, cheques) has little material value of its own but represents a claim to deposits/value held safely.\n"
            "3. Origin of 'bank': From the Italian word 'banco' / 'banchi' — the wooden benches/tables where 14th-century Italian merchants exchanged money."
        ),
        marking_points=[
            "Defines commodity money as items with intrinsic value (cattle, gold/silver) [1]",
            "Defines representative money (notes/cheques) as tokens representing value held securely [1]",
            "Traces 'bank' to Italian 'banco'/'banchi' (merchant benches in 14th-century Italy) [1]",
        ],
        hints={
            "tier_1": "Ask whether the object itself has value (gold) versus being a paper claim to deposits (cheque/note).",
            "tier_2": "Recall the Italian word 'banco' from 14th-century marketplace benches.",
            "tier_3": "Define commodity vs representative money and link 'bank' to Italian 'banco' benches.",
        },
        learning_objective_id="lo_sav_commodity_vs_rep_money",
        concept_id="money_history_types",
        misconception_tags=["confuses_commodity_with_representative_money"],
        marks=3,
    )


def arch_13_role_of_banks_safe_storage_and_security(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    bank = rng.choice(BANKS_SA)
    cash_amt = rng.choice([2500, 3800, 4600])
    prompt = (
        f"{name} keeps {_fmt_zar(cash_amt)} inside a bedroom drawer instead of depositing it at {bank}.\n\n"
        f"Which THREE risks are avoided by keeping money safely in a formal bank?"
    )
    correct = "Theft, physical damage (fire/flood), and losing value from temptation to spend cash impulsively with 0% interest"
    distractors = [
        "Guaranteed doubling of banknotes overnight inside the bedroom drawer",
        "Eliminating all income taxes and municipal rates permanently",
        "Preventing the South African Reserve Bank from issuing coins",
    ]
    return _mcq(
        rng,
        subskill="13_role_of_banks_safe_storage_and_security",
        title="Banks as Safe Custodians of Money",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Storing {_fmt_zar(cash_amt)} at {bank} protects it against theft, fire/flood damage, and impulse cash "
            f"spending while paying interest."
        ),
        hints={
            "tier_1": "Think about what can physically happen to paper notes in a house.",
            "tier_2": "Banks guard deposits in secure vaults/records and pay interest instead of leaving cash exposed.",
            "tier_3": "Select 'Theft, physical damage (fire/flood), and losing value from temptation to spend cash impulsively with 0% interest'.",
        },
        learning_objective_id="lo_sav_safe_storage",
        concept_id="bank_safe_storage",
        misconception_tags=["believes_mattress_cash_is_safer"],
    )


def arch_14_role_of_banks_interest_paid_vs_charged(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    sav_rate = rng.choice([4.5, 5.0, 5.5])
    loan_rate = rng.choice([11.5, 12.0, 13.0])
    spread = round(loan_rate - sav_rate, 1)
    prompt = (
        f"{bank} pays savers {_fmt_comma(sav_rate, 1)}% annual interest on savings deposits and charges borrowers "
        f"{_fmt_comma(loan_rate, 1)}% annual interest on business loans.\n\n"
        f"Calculate the bank's interest-rate spread (the percentage-point difference between loan interest charged and deposit interest paid)."
    )
    return _typed(
        rng,
        subskill="14_role_of_banks_interest_paid_vs_charged",
        title="Bank Interest Spread: Deposits vs Loans",
        prompt=prompt,
        sample_answer=(
            f"Interest spread = {_fmt_comma(loan_rate, 1)}% - {_fmt_comma(sav_rate, 1)}% = {_fmt_comma(spread, 1)} percentage points.\n"
            f"This spread covers {bank}'s staff, buildings, security systems, and operating profit."
        ),
        marking_points=[
            f"Subtract deposit rate ({_fmt_comma(sav_rate, 1)}%) from lending rate ({_fmt_comma(loan_rate, 1)}%) [1]",
            f"Correct spread = {_fmt_comma(spread, 1)} percentage points [1]",
        ],
        hints={
            "tier_1": "Banks charge borrowers a higher interest rate than they pay savers.",
            "tier_2": f"Subtract {_fmt_comma(sav_rate, 1)}% from {_fmt_comma(loan_rate, 1)}%.",
            "tier_3": f"{_fmt_comma(loan_rate, 1)}% - {_fmt_comma(sav_rate, 1)}% = {_fmt_comma(spread, 1)} percentage points.",
        },
        learning_objective_id="lo_sav_interest_spread",
        concept_id="bank_interest_spread",
        misconception_tags=["adds_deposit_and_loan_rates"],
        marks=2,
        correct_answer=f"{_fmt_comma(spread, 1)} percentage points",
        correct_value=float(spread),
        worked_solution=f"Spread = {loan_rate} - {sav_rate} = {_fmt_comma(spread, 1)}%",
    )


def arch_15_financial_intermediation_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    pool_m = rng.randint(15, 45)
    svg = _svg_cycle_flow(
        title=f"Financial Intermediation Cycle ({bank})",
        nodes=[
            f"1. Households Deposit R{pool_m}M Savings",
            "2. Bank Pools Deposits Safely",
            "3. Bank Lends Capital to Businesses",
            "4. Businesses Grow GDP & Pay Wages",
        ],
        accent_color="#1D4ED8",
    )
    prompt = (
        f"Refer to the flowchart below showing how {bank} acts as a financial intermediary for R{pool_m} million in "
        f"community deposits.\n\n"
        f"Explain how Steps 2 and 3 turn idle household savings into new factory jobs and economic growth in Step 4."
    )
    return _typed(
        rng,
        subskill="15_financial_intermediation_flow_diagram",
        title="Banks as Financial Intermediaries (Flowchart)",
        prompt=prompt,
        sample_answer=(
            f"Instead of small R{pool_m}M deposits sitting idle in separate drawers, {bank} pools them safely in Step 2 "
            f"and lends investment capital to businesses in Step 3. Entrepreneurs buy machinery and stock, creating jobs "
            f"and wages in Step 4 that flow back into household deposits."
        ),
        marking_points=[
            "Explains pooling of many small household deposits into usable investment sums [1]",
            "Explains lending funds to productive businesses to buy capital equipment and expand [1]",
            "Links business investment to job creation, household wages, and GDP growth [1]",
        ],
        hints={
            "tier_1": "Trace the arrows from Box 1 through Box 2 and Box 3 down to Box 4.",
            "tier_2": "A financial intermediary connects people with surplus money (savers) to entrepreneurs needing capital.",
            "tier_3": "Explain pooling deposits -> lending to businesses -> building machinery/jobs -> higher wages & GDP.",
        },
        learning_objective_id="lo_sav_intermediation_flow",
        concept_id="financial_intermediation",
        misconception_tags=["thinks_banks_keep_all_cash_locked_unused"],
        marks=3,
        diagram_spec={"kind": "inline_svg", "title": "Financial Intermediation Cycle", "svg": svg, "diagram_role": "context"},
    )


def arch_16_banks_capital_investment_and_gdp_growth(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    loan_m = rng.randint(4, 15)
    prompt = (
        f"A commercial bank channels R{loan_m} million from household savings into expanding a citrus juice processing "
        f"plant in {area}.\n\n"
        f"How does this bank lending stimulate South Africa's economic growth (GDP)?"
    )
    correct = (
        "It enables businesses to buy new capital machinery, expand output, and create sustainable employment and wages"
    )
    distractors = [
        "It forces every local household to hide banknotes permanently away from commerce",
        "It prevents factories from upgrading equipment or paying employees",
        "It removes the business from the Primary, Secondary, and Tertiary sectors",
    ]
    return _mcq(
        rng,
        subskill="16_banks_capital_investment_and_gdp_growth",
        title="Bank Capital Investment and GDP Growth",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Lending R{loan_m} million turns idle savings into productive factory equipment and jobs, expanding total "
            f"goods and services produced (GDP)."
        ),
        hints={
            "tier_1": "Think of what a factory buys with a business expansion loan.",
            "tier_2": "New machinery + expanded production + new staff directly raise GDP.",
            "tier_3": "Select 'It enables businesses to buy new capital machinery, expand output, and create sustainable employment and wages'.",
        },
        learning_objective_id="lo_sav_capital_gdp",
        concept_id="bank_capital_investment",
        misconception_tags=["ignores_investment_multiplier_of_savings"],
    )


def arch_17_banks_international_trade_and_surety(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    export_val = rng.choice([250000, 420000, 680000])
    prompt = (
        f"A textile exporter near {area} ships a {_fmt_zar(export_val)} order to buyers in Europe and imports sewing "
        f"spare parts priced in euros.\n\n"
        f"Explain TWO services commercial banks provide to support safe international trade."
    )
    return _typed(
        rng,
        subskill="17_banks_international_trade_and_surety",
        title="Banks in International Trade & Financial Surety",
        prompt=prompt,
        sample_answer=(
            "1. Foreign exchange (forex) conversion: Converting Rand into euros/dollars (and converting export earnings back into Rand).\n"
            f"2. Financial surety & international payments: Acting as a trusted guarantor (e.g. letters of credit/surety) so exporters ship safely knowing {_fmt_zar(export_val)} will be paid securely across borders."
        ),
        marking_points=[
            "Foreign currency exchange (converting Rand to euros/dollars and back) [1]",
            "Providing surety/payment guarantees and cross-border wire transfers so trading partners trust delivery/payment [1]",
        ],
        hints={
            "tier_1": "Think about different currencies (Rand vs euros) AND trust between distant buyers and sellers.",
            "tier_2": "Banks convert foreign exchange AND stand as financial surety/guarantors for cross-border payments.",
            "tier_3": "State foreign currency conversion (forex) and acting as surety/guaranteeing cross-border settlement.",
        },
        learning_objective_id="lo_sav_international_trade_banks",
        concept_id="banks_international_trade",
        misconception_tags=["forgets_forex_or_surety_role"],
        marks=2,
    )


def arch_18_bank_accounts_savings_vs_cheque_comparison(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    prompt = (
        f"A Grade 7 learner compares an everyday Savings account against an adult Cheque (Current) account at {bank}.\n\n"
        f"Which statement ACCUARATELY contrasts a Savings account and a Cheque account?"
        .replace("ACCUARATELY", "ACCURATELY")
    )
    correct = (
        "A savings account earns interest on positive balances with lower fees and no overdraft, whereas a cheque account supports frequent everyday payments, debit orders, and optional overdraft facilities"
    )
    distractors = [
        "Only savings accounts offer unlimited business overdraft loans without any positive balance",
        "Cheque accounts cannot be linked to debit cards or electronic EFT salary payments",
        "Savings accounts prohibit withdrawals for 30 years unless approved by Parliament",
    ]
    return _mcq(
        rng,
        subskill="18_bank_accounts_savings_vs_cheque_comparison",
        title="Savings Account vs Cheque (Current) Account",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Savings accounts encourage setting money aside with positive-balance interest and no overdraft debt, while "
            "cheque/current accounts manage high-frequency transactions, salary deposits, debit orders, and overdraft credit."
        ),
        hints={
            "tier_1": "Which account is built for daily transactional flow + overdraft vs safely growing positive savings?",
            "tier_2": "Savings accounts do NOT normally provide overdraft debt.",
            "tier_3": "Select the option contrasting savings (interest on positive funds, lower fees, no overdraft) vs cheque (frequent payments/overdraft).",
        },
        learning_objective_id="lo_sav_savings_vs_cheque",
        concept_id="savings_vs_cheque_account",
        misconception_tags=["thinks_savings_accounts_include_overdrafts"],
    )


def arch_19_bank_investment_products_fixed_money_market_unit_trusts(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    principal = rng.choice([15000, 25000, 40000])
    prompt = (
        f"A family with {_fmt_zar(principal)} in spare savings visits {bank} and is offered three investment options: "
        f"(1) Fixed Deposit, (2) Money Market account, and (3) Unit Trusts.\n\n"
        f"Briefly explain what EACH of these three bank investment products does."
    )
    return _typed(
        rng,
        subskill="19_bank_investment_products_fixed_money_market_unit_trusts",
        title="Fixed Deposits, Money Market & Unit Trusts",
        prompt=prompt,
        sample_answer=(
            f"1. Fixed Deposit: Locks the {_fmt_zar(principal)} away for an agreed period (e.g. 6–24 months) at a fixed higher interest rate.\n"
            "2. Money Market account: Requires a higher minimum balance and pays tiered interest while allowing relatively quick withdrawals.\n"
            "3. Unit Trusts: Pools money from many investors to buy a diversified portfolio of company shares, bonds, and property managed by professionals."
        ),
        marking_points=[
            "Fixed Deposit: locks funds for a fixed term at a guaranteed higher interest rate [1]",
            "Money Market: pays higher liquid interest in exchange for a larger minimum balance [1]",
            "Unit Trusts: pools investor funds into professionally managed shares/bonds/assets [1]",
        ],
        hints={
            "tier_1": "Identify what distinguishes locking money away (Fixed), liquid higher-balance interest (Money Market), and pooled shares (Unit Trust).",
            "tier_2": "Give one accurate sentence per product.",
            "tier_3": "Fixed Deposit (locked term/rate), Money Market (higher minimum/liquid rate), Unit Trusts (pooled diversified shares/bonds).",
        },
        learning_objective_id="lo_sav_investment_products",
        concept_id="bank_investment_products",
        misconception_tags=["confuses_unit_trust_with_fixed_deposit"],
        marks=3,
    )


def arch_20_bank_loans_home_short_term_credit_cards(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    house_price = rng.choice([650000, 850000, 950000])
    prompt = (
        f"A household applies to {bank} to buy a {_fmt_zar(house_price)} home repayable over 20 years using the "
        f"property as security.\n\n"
        f"Which type of bank loan is designed specifically for purchasing residential property over many years?"
    )
    correct = "A home loan (mortgage bond)"
    distractors = [
        "A 30-day revolving store loyalty voucher",
        "A small-change petty-cash tin",
        "A stokvel year-end grocery hamper",
    ]
    return _mcq(
        rng,
        subskill="20_bank_loans_home_short_term_credit_cards",
        title="Home Loans vs Short-Term Credit",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"A home loan (mortgage bond) provides long-term finance (typically 20 years) secured against the {_fmt_zar(house_price)} property."
        ),
        hints={
            "tier_1": "Think of the 20-year loan specifically secured by a house or land.",
            "tier_2": "Unlike short-term personal loans or credit cards, property loans are mortgage bonds.",
            "tier_3": "Select 'A home loan (mortgage bond)'.",
        },
        learning_objective_id="lo_sav_bank_loan_types",
        concept_id="home_loans_vs_short_term",
        misconception_tags=["confuses_mortgage_with_credit_card"],
    )


def arch_21_modern_banking_channels_atm_eft_cellphone_internet(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    amt = rng.choice([450, 750, 1200])
    prompt = (
        f"Without standing in a branch queue at {bank}, a customer sends {_fmt_zar(amt)} instantly from her phone "
        f"directly into a supplier's bank account.\n\n"
        f"Which banking service enables direct digital transfers from one bank account to another via internet or cellphone banking?"
    )
    correct = "Electronic Funds Transfer (EFT)"
    distractors = [
        "Physical barter of livestock",
        "Postage-stamp coin mailing",
        "Underground safety-deposit safe rental",
    ]
    return _mcq(
        rng,
        subskill="21_modern_banking_channels_atm_eft_cellphone_internet",
        title="EFT, ATM, Cellphone & Internet Banking",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"An EFT moves {_fmt_zar(amt)} electronically between bank accounts via cellphone or internet banking without handling physical cash."
        ),
        hints={
            "tier_1": "Match the letters E-F-T to moving money digitally between accounts.",
            "tier_2": "Cellphone and internet banking execute Electronic Funds Transfers (EFTs).",
            "tier_3": "Select 'Electronic Funds Transfer (EFT)'.",
        },
        learning_objective_id="lo_sav_digital_banking",
        concept_id="eft_modern_banking",
        misconception_tags=["confuses_eft_with_atm_cash_withdrawal"],
    )


def arch_22_sa_major_commercial_banks_and_post_office(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Learners in {area} list accessible South African institutions where citizens can open formal savings accounts, "
        f"including major retail banks and rural branches.\n\n"
        f"Which group correctly lists South African commercial/retail banking savings providers?"
    )
    correct = "Capitec, Standard Bank, Nedbank, Absa, First National Bank (FNB), and the South African Post Office (Postbank)"
    distractors = [
        "Only European central banks that ban South African Rand deposits",
        "Clothing wholesalers and local taxi associations acting as reserve banks",
        "Unregistered loan sharks charging 100% weekly cash interest",
    ]
    return _mcq(
        rng,
        subskill="22_sa_major_commercial_banks_and_post_office",
        title="South African Retail Banks & Postbank",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "South Africa's major formal retail savings providers are Capitec, Standard Bank, Nedbank, Absa, FNB, and "
            "widely accessible Post Office / Postbank outlets."
        ),
        hints={
            "tier_1": "Identify regulated South African banks plus the national Post Office savings network.",
            "tier_2": "Exclude unregistered lenders and foreign banks that do not take retail Rand deposits.",
            "tier_3": "Select 'Capitec, Standard Bank, Nedbank, Absa, First National Bank (FNB), and the South African Post Office (Postbank)'.",
        },
        learning_objective_id="lo_sav_sa_banks_list",
        concept_id="sa_commercial_banks",
        misconception_tags=["includes_informal_lenders_as_banks"],
    )


def arch_23_islamic_sharia_banking_interest_free_principles(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    sharia_bank = rng.choice(["Al Baraka Bank", "Absa Islamic Banking", "FNB Islamic Banking"])
    prompt = (
        f"In {area}, customers choose {sharia_bank} rather than conventional interest-bearing accounts.\n\n"
        f"Explain TWO core principles of Islamic (Sharia-compliant) banking in South Africa."
    )
    return _typed(
        rng,
        subskill="23_islamic_sharia_banking_interest_free_principles",
        title="Islamic Banking Principles in South Africa",
        prompt=prompt,
        sample_answer=(
            f"1. Prohibition of interest (riba): {sharia_bank} neither pays nor charges conventional interest on deposits or loans.\n"
            "2. Profit-and-risk sharing & ethical asset backing: Returns come from real trade, asset leasing/mark-up, and shared investment profits rather than money-on-money interest, avoiding harmful industries."
        ),
        marking_points=[
            "Explains prohibition of paying or charging interest (riba) [1]",
            "Explains profit/risk-sharing or real asset-backed trade/ethical investment principles [1]",
        ],
        hints={
            "tier_1": "What does Sharia law forbid regarding interest, and how does the bank earn returns fairly instead?",
            "tier_2": "Banks like Al Baraka, Absa Islamic, and FNB Islamic replace interest with profit-sharing and asset trade.",
            "tier_3": "Mention zero interest (no riba) AND profit/risk sharing backed by real ethical assets.",
        },
        learning_objective_id="lo_sav_islamic_banking",
        concept_id="islamic_banking_sa",
        misconception_tags=["thinks_islamic_banks_give_free_money"],
        marks=2,
    )


def arch_24_opening_under16_savings_account_requirements(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    age = rng.randint(12, 15)
    bank = rng.choice(BANKS_SA)
    prompt = (
        f"{name}, aged {age}, visits {bank} with a parent to open a youth savings account.\n\n"
        f"Which set of documents and requirements is needed for a South African learner under 16 to open a savings account?"
    )
    correct = (
        "Parent or legal guardian present with their ID, proof of residential address, the child's birth certificate, and a small minimum opening deposit (e.g. R10) scanned electronically"
    )
    distractors = [
        "Only a handwritten school timetable and an unregistered R5 000 credit limit",
        "A university degree certificate and three years of company tax audits",
        "An unaccompanied child bringing no birth certificate or guardian identification",
    ]
    return _mcq(
        rng,
        subskill="24_opening_under16_savings_account_requirements",
        title="Opening a Savings Account Under Age 16",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Under South African FICA rules, a {age}-year-old needs a parent/guardian with ID, proof of address, the "
            f"learner's birth certificate, and an opening deposit (often R10), captured electronically."
        ),
        hints={
            "tier_1": "Learners under 16 cannot sign bank contracts alone without adult/FICA verification.",
            "tier_2": "Think of Guardian ID + Proof of Address + Child's Birth Certificate + R10 minimum deposit.",
            "tier_3": "Select the option listing guardian presence/ID, proof of address, child's birth certificate, and small minimum deposit.",
        },
        learning_objective_id="lo_sav_under16_account",
        concept_id="opening_savings_account_under16",
        misconception_tags=["assumes_child_needs_passport_or_salary_slip"],
    )


def arch_25_under16_bank_account_checklist_table(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    name = rng.choice(NAMES)
    headers = ["Account Requirement", "Who / What Supplies It", "Verification Purpose", "Check"]
    raw_rows = [
        [
            {"type": "given", "value": "Parent / Guardian ID"},
            {"type": "given", "value": "Accompanying adult"},
            {"type": "required", "expected": "Confirms legal guardian identity"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Child's Birth Certificate"},
            {"type": "given", "value": f"{name}'s family"},
            {"type": "required", "expected": "Proves child age and parentage"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Proof of Address & R10"},
            {"type": "given", "value": "Utility bill & opening cash"},
            {"type": "required", "expected": "Verifies residence and activates account"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact phrase: 'Confirms legal guardian identity'.",
        "r1_c2": "Exact phrase: 'Proves child age and parentage'.",
        "r2_c2": "Exact phrase: 'Verifies residence and activates account'.",
    }
    derivations = [
        "Parent/Guardian ID -> Confirms legal guardian identity.",
        "Child's Birth Certificate -> Proves child age and parentage.",
        "Proof of Address & R10 -> Verifies residence and activates account.",
    ]
    return _table_q(
        rng,
        subskill="25_under16_bank_account_checklist_table",
        title="Under-16 Savings Account Verification Checklist",
        prompt=(
            f"Before visiting {bank}, {name}'s guardian checks off the three mandatory FICA items. Complete the Verification "
            f"Purpose column using these exact phrases: 'Confirms legal guardian identity', 'Proves child age and parentage', "
            f"and 'Verifies residence and activates account'. Leave 'Check' blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Match each document to what it legally confirms.",
            "tier_2": "ID confirms guardian, birth certificate proves child age/parentage, utility bill & R10 verify address/activate.",
            "tier_3": "Fill r0_c2, r1_c2, and r2_c2 with the three exact checklist descriptions.",
        },
        learning_objective_id="lo_sav_under16_table",
        concept_id="under16_fica_checklist",
        misconception_tags=["swaps_id_and_proof_of_address_purpose", "fills_must_be_empty_cell"],
    )


BUILDERS_01_25 = {
    "01_personal_savings_definition": arch_01_personal_savings_definition,
    "02_personal_savings_monthly_calculation": arch_02_personal_savings_monthly_calculation,
    "03_personal_savings_budget_ledger_table": arch_03_personal_savings_budget_ledger_table,
    "04_purpose_saving_avoiding_high_interest_credit": arch_04_purpose_saving_avoiding_high_interest_credit,
    "05_cash_vs_credit_purchase_cost_bar_graph": arch_05_cash_vs_credit_purchase_cost_bar_graph,
    "06_purpose_saving_short_medium_long_term_goals": arch_06_purpose_saving_short_medium_long_term_goals,
    "07_purpose_saving_emergency_fund": arch_07_purpose_saving_emergency_fund,
    "08_purpose_saving_inflation_and_purchasing_power": arch_08_purpose_saving_inflation_and_purchasing_power,
    "09_purpose_saving_education_and_retirement": arch_09_purpose_saving_education_and_retirement,
    "10_savings_growth_over_time_bar_graph": arch_10_savings_growth_over_time_bar_graph,
    "11_history_of_money_and_earliest_temple_banks": arch_11_history_of_money_and_earliest_temple_banks,
    "12_commodity_vs_representative_money_and_cheques": arch_12_commodity_vs_representative_money_and_cheques,
    "13_role_of_banks_safe_storage_and_security": arch_13_role_of_banks_safe_storage_and_security,
    "14_role_of_banks_interest_paid_vs_charged": arch_14_role_of_banks_interest_paid_vs_charged,
    "15_financial_intermediation_flow_diagram": arch_15_financial_intermediation_flow_diagram,
    "16_banks_capital_investment_and_gdp_growth": arch_16_banks_capital_investment_and_gdp_growth,
    "17_banks_international_trade_and_surety": arch_17_banks_international_trade_and_surety,
    "18_bank_accounts_savings_vs_cheque_comparison": arch_18_bank_accounts_savings_vs_cheque_comparison,
    "19_bank_investment_products_fixed_money_market_unit_trusts": arch_19_bank_investment_products_fixed_money_market_unit_trusts,
    "20_bank_loans_home_short_term_credit_cards": arch_20_bank_loans_home_short_term_credit_cards,
    "21_modern_banking_channels_atm_eft_cellphone_internet": arch_21_modern_banking_channels_atm_eft_cellphone_internet,
    "22_sa_major_commercial_banks_and_post_office": arch_22_sa_major_commercial_banks_and_post_office,
    "23_islamic_sharia_banking_interest_free_principles": arch_23_islamic_sharia_banking_interest_free_principles,
    "24_opening_under16_savings_account_requirements": arch_24_opening_under16_savings_account_requirements,
    "25_under16_bank_account_checklist_table": arch_25_under16_bank_account_checklist_table,
}
