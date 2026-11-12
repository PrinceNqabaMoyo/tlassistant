"""Grade 8 EMS — Accounting Concepts Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/01. Accounting concepts.md.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario


def get_ems_scenario(rng: Optional[random.Random] = None) -> Dict[str, Any]:
    s = _raw_ems_scenario(rng)
    first = str(s["entrepreneur"]).split()[0]
    s["business"] = f"{first}'s {s['business_type'].title()}"
    return s

TOPIC_NAME = "Accounting concepts"
TOPIC_KEY = "grade8_ems_accounting_basics"
LO = "g8_ems_acct_concepts"
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
        "tier_1": "Identify the accounting element involved before choosing an answer.",
        "tier_2": "Recall: Assets = Owner's Equity + Liabilities (A = OE + L).",
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
        "subtopic_id": "term1_accounting_basics",
        "grade": 8,
        "subject": "Economic and Management Sciences",
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT_PERCENT,
        "suggested_duration_mins": out.get("suggested_duration_mins", duration_mins),
        "subskill": subskill,
        "archetype": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": subskill,
        "concept_group": "accounting_concepts",
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 2 > Accounting Concepts",
        "misconception_tags": misconception_tags or ["accounting_element_confusion"],
        "diagnostic_tags": ["accounting", "financial_literacy", "grade8_ems"],
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
        "id": f"g8_ems_ac_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_ac_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "typed",
        "modality": "math",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "expected_answer": correct_ans,
        "acceptable_answers": acceptable_answers or [correct_ans],
        "sample_answer": f"{correct_ans}",
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
        "id": f"g8_ems_ac_{subskill}_{rng.randint(100000, 999999)}",
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
    """Build a 2D table_completion payload + full Markdown table memo."""
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
        "id": f"g8_ems_ac_{subskill}_{rng.randint(100000, 999999)}",
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


def _svg_ledger_card(title: str, subtitle: str, rows: List[Tuple[str, str]]) -> str:
    """Render a crisp Paper & Ink accounting summary card SVG with XML escaping."""
    row_height = 24
    height = 78 + len(rows) * row_height
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 {height}" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">',
        f'<rect x="4" y="4" width="532" height="{height - 8}" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>',
        f'<rect x="4" y="4" width="532" height="44" rx="8" fill="#13519C"/>',
        f'<rect x="4" y="34" width="532" height="14" fill="#13519C"/>',
        f'<text x="20" y="24" font-size="13" font-weight="bold" fill="#FFFFFF">{_xml_escape(title)}</text>',
        f'<text x="20" y="40" font-size="10" fill="#DBEAFE">{_xml_escape(subtitle)}</text>',
    ]
    for idx, (label, val) in enumerate(rows):
        y = 70 + idx * row_height
        bg = "#F8FAFC" if idx % 2 == 0 else "#FFFFFF"
        lines.append(f'<rect x="14" y="{y - 15}" width="512" height="22" fill="{bg}" rx="3"/>')
        lines.append(f'<text x="22" y="{y}" font-size="12" fill="#1E293B">{_xml_escape(label)}</text>')
        lines.append(f'<text x="516" y="{y}" font-size="12" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(val)}</text>')
    lines.append("</svg>")
    return "".join(lines)


# =============================================================================
# ARCHETYPES 01 – 25
# =============================================================================

def _b01_capital_definition_contribution(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    biz = s["business"]
    cash_cap = rng.randint(15, 65) * 1000
    equip_cap = rng.randint(5, 25) * 1000
    cases = [
        (
            f"{owner} opens {biz} in {s['area']} by depositing {fmt_r(cash_cap)} of personal savings into the business bank account and bringing in personal equipment worth {fmt_r(equip_cap)}. What accounting term describes the owner's total contribution ({fmt_r(cash_cap + equip_cap)}) to start the business?",
            "Capital",
            f"Capital refers to the money and/or assets contributed by the owner ({owner}) to start or expand a business, totalling {fmt_r(cash_cap + equip_cap)}.",
            ["Capital", "Current Liabilities", "Drawings", "Current Income"],
        ),
        (
            f"To expand {biz} in {s['area']}, {owner} transfers {fmt_r(cash_cap)} from a personal savings account into the business bank account. In the books of {biz}, this contribution is recorded as:",
            "Capital",
            f"Any money or resources invested by the owner into the enterprise increases Capital ({fmt_r(cash_cap)}).",
            ["Capital", "Operational Expenses", "Sales Revenue", "Bank Overdraft"],
        ),
    ]
    prompt, ans, exp, opts = rng.choice(cases)
    return _make_mcq(
        rng,
        subskill="01_capital_definition_contribution",
        title="Capital Contribution",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think about resources put INTO the business by the owner to start or grow it.",
            "tier_2": "Capital is the owner's investment; Drawings is what the owner takes out for personal use.",
            "tier_3": f"The contribution is Capital ({ans}).",
        },
        misconception_tags=["confuses_capital_and_income"],
        question_family_id="capital_contribution",
    )


def _b02_own_vs_borrowed_capital(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    bank = rng.choice(_BANKS)
    own_amt = rng.randint(20, 50) * 1000
    loan_amt = rng.randint(15, 45) * 1000
    scenario_type = rng.choice(["borrowed", "own"])
    if scenario_type == "borrowed":
        prompt = (
            f"{owner} needs {fmt_r(own_amt + loan_amt)} to open {s['business']} in {s['area']}. "
            f"{owner} uses {fmt_r(own_amt)} from personal savings and obtains a {fmt_r(loan_amt)} loan from {bank} that must be repaid with interest. "
            f"How is the {fmt_r(loan_amt)} from {bank} classified?"
        )
        ans = "Borrowed capital (a liability)"
        exp = f"Funds obtained from external institutions such as {bank} ({fmt_r(loan_amt)}) carry a legal obligation to repay with interest and are classified as borrowed capital (a liability)."
    else:
        prompt = (
            f"{owner} starts {s['business']} in {s['area']} using {fmt_r(own_amt)} from personal savings and an inheritance, without taking any bank loans. "
            f"How is this {fmt_r(own_amt)} funding classified?"
        )
        ans = "Own capital (owner's equity)"
        exp = f"Personal savings and inheritances invested by the owner ({fmt_r(own_amt)}) do not have to be repaid to outsiders and are classified as own capital."
    opts = [
        "Borrowed capital (a liability)",
        "Own capital (owner's equity)",
        "Drawings by the owner",
        "Current operating income",
    ]
    return _make_mcq(
        rng,
        subskill="02_own_vs_borrowed_capital",
        title="Own vs Borrowed Capital",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check whether the funds come from the owner personally or from an outside lender.",
            "tier_2": "Borrowed capital (loans) must be repaid with interest; own capital comes from the owner's own wealth.",
            "tier_3": f"Correct classification: {ans}.",
        },
        misconception_tags=["confuses_own_and_borrowed_capital"],
        question_family_id="capital_sources",
    )


def _b03_owners_equity_net_worth_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    cap = rng.randint(40, 120) * 1000
    profit = rng.randint(12, 45) * 1000
    drawings = rng.randint(3, 10) * 1000
    oe = cap + profit - drawings
    ans = fmt_r(oe)
    prompt = (
        f"At the start of the financial year, {owner} had Capital of {fmt_r(cap)} in {s['business']}. "
        f"During the year the business earned a Net Profit of {fmt_r(profit)}, while {owner} withdrew {fmt_r(drawings)} for personal household use. "
        f"Calculate {owner}'s closing Owner's Equity (in Rands)."
    )
    steps = [
        f"Formula: Owner's Equity = Capital + Net Profit - Drawings",
        f"Substitute values: {fmt_r(cap)} + {fmt_r(profit)} - {fmt_r(drawings)}",
        f"Closing Owner's Equity = {ans}",
    ]
    return _make_typed(
        rng,
        subskill="03_owners_equity_net_worth_calc",
        title="Calculate Closing Owner's Equity",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{oe}", str(oe)],
        steps=steps,
        hints={
            "tier_1": "Net Profit increases Owner's Equity; Drawings decrease Owner's Equity.",
            "tier_2": "Use: Owner's Equity = Capital + Net Profit - Drawings.",
            "tier_3": f"{fmt_r(cap)} + {fmt_r(profit)} - {fmt_r(drawings)} = {ans}.",
        },
        misconception_tags=["adds_drawings_instead_of_subtracting"],
        question_family_id="owners_equity_calc",
    )


def _b04_drawings_cash_and_goods_impact(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    amt = rng.randint(6, 28) * 100
    variant = rng.choice(["cash", "stock"])
    if variant == "cash":
        prompt = (
            f"{owner} takes {fmt_r(amt)} cash out of the cash register of {s['business']} to buy groceries for home use. "
            f"How does this transaction affect the accounting elements of {s['business']}?"
        )
    else:
        prompt = (
            f"{owner} takes trading goods worth {fmt_r(amt)} (at cost price) from {s['business']} as a birthday gift for a family member. "
            f"In the accounting records of {s['business']}, how must this withdrawal be classified?"
        )
    ans = "As Drawings, which decreases Owner's Equity"
    opts = [
        "As Drawings, which decreases Owner's Equity",
        "As an Operating Expense, which reduces Net Profit",
        "As Additional Capital invested by the owner",
        "As a Current Liability owed to the owner",
    ]
    exp = f"Any cash or goods worth {fmt_r(amt)} taken by {owner} for personal use is Drawings. Drawings reduce Owner's Equity directly and are NOT a business expense."
    return _make_mcq(
        rng,
        subskill="04_drawings_cash_and_goods_impact",
        title="Drawings Concept & Impact",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": f"Ask: Was this {fmt_r(amt)} spent to generate business income, or taken for the owner's personal family use?",
            "tier_2": "Personal withdrawals by the owner are always Drawings, never a business expense.",
            "tier_3": "Drawings decrease Assets (Cash/Stock) and decrease Owner's Equity.",
        },
        misconception_tags=["treats_drawings_as_expense"],
        question_family_id="drawings_impact",
    )


def _b05_fixed_non_current_assets_id(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    val = rng.randint(45, 220) * 1000
    fixed_choices = [
        ("delivery van", "Vehicles"),
        ("workshop building", "Land and Buildings"),
        ("industrial sewing machines and office computers", "Equipment"),
    ]
    item_desc, acct_name = rng.choice(fixed_choices)
    prompt = (
        f"{owner}'s business in {s['area']} purchases a {item_desc} for {fmt_r(val)} to use in daily operations for the next 5 to 10 years. "
        f"Which classification best describes {acct_name}?"
    )
    ans = "Fixed (Non-current) Asset"
    opts = [
        "Fixed (Non-current) Asset",
        "Current Asset",
        "Long-term Liability",
        "Operating Expense",
    ]
    exp = f"{acct_name} worth {fmt_r(val)} are bought to be kept and used for longer than 12 months (not for resale), making them Fixed (Non-current) Assets."
    return _make_mcq(
        rng,
        subskill="05_fixed_non_current_assets_id",
        title="Fixed (Non-current) Assets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "How long does the business intend to keep and use this asset?",
            "tier_2": "Long-term tangible assets used for > 1 year (Land & Buildings, Vehicles, Equipment) are Fixed Assets.",
            "tier_3": f"{acct_name} are classified as Fixed (Non-current) Assets.",
        },
        misconception_tags=["classifies_fixed_assets_as_expenses"],
        question_family_id="fixed_assets",
    )


def _b06_current_assets_id(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 24) * 1000
    sets = [
        ("Trading Stock, Bank, Debtors Control, Petty Cash", "All items are converted into cash or used up within 12 months."),
        ("Cash Float, Bank, Trading Stock, Debtors Control", "Cash and near-cash items expected to circulate within one accounting year are Current Assets."),
    ]
    correct_list, reason = rng.choice(sets)
    prompt = (
        f"{s['business']} in {s['area']} has total short-term resources valued at {fmt_r(amt)}. "
        f"Which group contains ONLY Current Assets?"
    )
    opts = [
        correct_list,
        "Vehicles, Land and Buildings, Equipment, Mortgage Bond",
        "Bank, Creditors Control, Bank Overdraft, Salaries",
        "Trading Stock, Equipment, Water and Electricity, Rent Income",
    ]
    return _make_mcq(
        rng,
        subskill="06_current_assets_id",
        title="Current Assets Identification",
        prompt=prompt,
        options=opts,
        correct_ans=correct_list,
        explanation=f"{correct_list} are all Current Assets. {reason}",
        hints={
            "tier_1": "Eliminate any list containing Fixed Assets (Vehicles, Equipment) or Liabilities (Creditors, Overdraft).",
            "tier_2": "Current Assets include Trading Stock, Debtors Control, Bank, Cash Float, and Petty Cash.",
            "tier_3": f"The correct Current Assets list is: {correct_list}.",
        },
        misconception_tags=["confuses_fixed_and_current_assets"],
        question_family_id="current_assets",
    )


def _b07_cash_float_vs_petty_cash(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    float_amt = rng.randint(3, 12) * 100
    petty_amt = rng.randint(2, 8) * 100
    ask_float = rng.choice([True, False])
    if ask_float:
        prompt = (
            f"Every morning before {s['business']} opens in {s['area']}, the cashier places {fmt_r(float_amt)} in coins and small notes inside the till solely to give change to cash customers. "
            f"What is this {fmt_r(float_amt)} fund called?"
        )
        ans = "Cash Float"
        exp = f"Cash Float ({fmt_r(float_amt)}) is the cash kept in the till specifically to provide change to customers. Both Cash Float and Petty Cash are Current Assets."
    else:
        prompt = (
            f"The receptionist at {s['business']} keeps {fmt_r(petty_amt)} inside a locked tin box to pay for minor day-to-day items such as tea, milk, and postage stamps without writing cheques or doing EFTs. "
            f"What is this {fmt_r(petty_amt)} fund called?"
        )
        ans = "Petty Cash"
        exp = f"Petty Cash ({fmt_r(petty_amt)}) is small cash kept on hand for minor everyday business payments. It is classified as a Current Asset."
    opts = ["Cash Float", "Petty Cash", "Creditors Control", "Current Income"]
    return _make_mcq(
        rng,
        subskill="07_cash_float_vs_petty_cash",
        title="Cash Float vs Petty Cash",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Compare: giving change at the cash register vs paying for minor office items like stamps and milk.",
            "tier_2": "Till change = Cash Float; minor expense tin = Petty Cash.",
            "tier_3": f"Correct term: {ans}.",
        },
        misconception_tags=["confuses_cash_float_and_petty_cash"],
        question_family_id="cash_funds",
    )


def _b08_debtors_control_current_asset(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    customer = rng.choice(NAMES)
    amt = rng.randint(15, 85) * 100
    prompt = (
        f"{s['business']} sells goods on credit worth {fmt_r(amt)} to a regular customer, {customer}, who promises to pay within 30 days. "
        f"In the books of {s['business']}, how is the {fmt_r(amt)} owed by {customer} (Debtors Control) classified?"
    )
    ans = "Current Asset — money owed TO the business, receivable within 12 months"
    opts = [
        "Current Asset — money owed TO the business, receivable within 12 months",
        "Current Liability — money the business owes to suppliers",
        "Operating Expense — cash lost by the business",
        "Fixed Asset — long-term investment held for more than a year",
    ]
    exp = f"Customers who buy on credit ({customer}) are Debtors. Because they owe {fmt_r(amt)} to the business and settle within ~30 days, Debtors Control is a Current Asset."
    return _make_mcq(
        rng,
        subskill="08_debtors_control_current_asset",
        title="Debtors as Current Assets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think: Does the business expect to RECEIVE this cash or PAY it out?",
            "tier_2": "Debtors owe money TO the business -> a short-term receivable -> Current Asset.",
            "tier_3": f"Debtors Control ({fmt_r(amt)}) is a Current Asset.",
        },
        misconception_tags=["confuses_debtors_and_creditors"],
        question_family_id="debtors_asset",
    )


def _b09_financial_investments_as_assets(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    amt = rng.randint(25, 90) * 1000
    years = rng.choice([2, 3, 5])
    prompt = (
        f"{s['business']} invests surplus cash of {fmt_r(amt)} in a {years}-year Fixed Deposit account at {bank} to earn annual interest. "
        f"How is this Fixed Deposit classified in the Balance Sheet?"
    )
    ans = "Financial Asset (Non-current Asset)"
    opts = [
        "Financial Asset (Non-current Asset)",
        "Long-term Liability",
        "Operational Expense",
        "Drawings by Owner",
    ]
    exp = f"A {years}-year Fixed Deposit of {fmt_r(amt)} at {bank} belongs to the business and earns interest over more than one year, making it a Financial (Non-current) Asset."
    return _make_mcq(
        rng,
        subskill="09_financial_investments_as_assets",
        title="Financial Assets (Fixed Deposits)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "The business owns the money deposited at the bank and receives interest — it does not owe money.",
            "tier_2": "Fixed Deposits maturing after 12 months are classified under Financial / Non-current Assets.",
            "tier_3": "Correct classification: Financial Asset (Non-current Asset).",
        },
        misconception_tags=["confuses_fixed_deposit_with_liability"],
        question_family_id="financial_assets",
    )


def _b10_total_assets_calculation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    veh = rng.randint(90, 220) * 1000
    equip = rng.randint(20, 65) * 1000
    stock = rng.randint(15, 45) * 1000
    bank = rng.randint(8, 35) * 1000
    cred = rng.randint(10, 30) * 1000
    rent_exp = rng.randint(4, 12) * 1000
    total_assets = veh + equip + stock + bank
    ans = fmt_r(total_assets)

    card_svg = _svg_ledger_card(
        f"{s['business']} — Account Balances",
        f"Owner: {s['entrepreneur']} ({s['area']})",
        [
            ("Vehicles", fmt_r(veh)),
            ("Equipment", fmt_r(equip)),
            ("Trading Stock", fmt_r(stock)),
            ("Bank (favourable)", fmt_r(bank)),
            ("Creditors Control", fmt_r(cred)),
            ("Rent Expense", fmt_r(rent_exp)),
        ],
    )
    prompt = (
        f"Inspect the Account Balances summary provided for {s['business']}. "
        f"Calculate the Total Assets of {s['business']} (exclude Liabilities and Expenses)."
    )
    steps = [
        f"Identify Assets only: Vehicles ({fmt_r(veh)}) + Equipment ({fmt_r(equip)}) + Trading Stock ({fmt_r(stock)}) + Bank ({fmt_r(bank)}).",
        f"Exclude Creditors Control ({fmt_r(cred)}, Current Liability) and Rent Expense ({fmt_r(rent_exp)}, Expense).",
        f"Total Assets = {fmt_r(veh)} + {fmt_r(equip)} + {fmt_r(stock)} + {fmt_r(bank)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="10_total_assets_calculation",
        title="Calculate Total Assets",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total_assets}", str(total_assets)],
        steps=steps,
        hints={
            "tier_1": "First sort every item into Assets, Liabilities, or Expenses.",
            "tier_2": "Add Fixed Assets (Vehicles + Equipment) and Current Assets (Trading Stock + Bank).",
            "tier_3": f"Total Assets = {fmt_r(veh + equip)} + {fmt_r(stock + bank)} = {ans}.",
        },
        misconception_tags=["includes_liabilities_or_expenses_in_assets"],
        question_family_id="total_assets_calc",
        marks=4,
        diagram_spec={"kind": "inline_svg", "svg": card_svg, "diagram_role": "context"},
    )


def _b11_long_term_liabilities_id(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    amt = rng.randint(180, 650) * 1000
    years = rng.choice([5, 10, 15, 20])
    prompt = (
        f"To purchase business premises in {s['area']}, {s['business']} signs a {years}-year Mortgage Bond of {fmt_r(amt)} with {bank}. "
        f"How is this {fmt_r(amt)} Mortgage Bond classified?"
    )
    ans = "Long-term (Non-current) Liability"
    opts = [
        "Long-term (Non-current) Liability",
        "Current Liability",
        "Fixed (Non-current) Asset",
        "Owner's Equity",
    ]
    exp = f"A Mortgage Bond of {fmt_r(amt)} repayable to {bank} over {years} years (longer than 12 months) is a Long-term (Non-current) Liability. (Note: the property itself is Land & Buildings, a Fixed Asset, while the loan is a Liability.)"
    return _make_mcq(
        rng,
        subskill="11_long_term_liabilities_id",
        title="Long-term Liabilities",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Separate the loan owed to the bank from the building bought with the loan.",
            "tier_2": "Debts repaid over more than 12 months (Mortgage Bond, Long-term Bank Loan) are Long-term Liabilities.",
            "tier_3": "Mortgage Bond = Long-term (Non-current) Liability.",
        },
        misconception_tags=["confuses_mortgage_with_land_asset"],
        question_family_id="long_term_liabilities",
    )


def _b12_current_liabilities_id(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(3, 18) * 1000
    item_variant = rng.choice([
        ("Creditors Control", f"owes {sup} {fmt_r(amt)} for inventory bought on 30-day credit"),
        ("Bank Overdraft", f"has an unfavourable balance of {fmt_r(amt)} that must be cleared within the next few months"),
        ("Clothing store credit account (6 months)", f"has a short-term retail credit balance of {fmt_r(amt)} payable within 6 months"),
    ])
    label, desc = item_variant
    prompt = (
        f"{s['business']} in {s['area']} {desc}. How is '{label}' classified in accounting?"
    )
    ans = "Current Liability"
    opts = [
        "Current Liability",
        "Current Asset",
        "Long-term Liability",
        "Operational Expense",
    ]
    exp = f"{label} ({fmt_r(amt)}) represents a short-term debt that must be settled within 12 months, so it is a Current Liability."
    return _make_mcq(
        rng,
        subskill="12_current_liabilities_id",
        title="Current Liabilities",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Is this an obligation owed to outside parties, and is it due within 12 months?",
            "tier_2": "Debts due within one year (Creditors Control, Bank Overdraft, 6-month accounts) are Current Liabilities.",
            "tier_3": f"{label} is a Current Liability.",
        },
        misconception_tags=["confuses_current_and_long_term_liabilities"],
        question_family_id="current_liabilities",
    )


def _b13_bank_vs_bank_overdraft_distinction(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    pos_amt = rng.randint(9, 25) * 1000
    neg_amt = rng.randint(4, 14) * 1000
    prompt = (
        f"In January, {s['business']} had a positive balance of {fmt_r(pos_amt)} at {bank}. "
        f"By March, after paying urgent supplier invoices, the business withdrew more than it had in its account and recorded a Bank Overdraft of {fmt_r(neg_amt)}. "
        f"Compare how the January balance and the March Bank Overdraft are classified:"
    )
    ans = "January Bank = Current Asset; March Bank Overdraft = Current Liability"
    opts = [
        "January Bank = Current Asset; March Bank Overdraft = Current Liability",
        "Both January Bank and March Bank Overdraft = Current Assets",
        "January Bank = Owner's Equity; March Bank Overdraft = Operating Expense",
        "January Bank = Current Liability; March Bank Overdraft = Fixed Asset",
    ]
    exp = f"A positive Bank balance ({fmt_r(pos_amt)}) belongs to the business (Current Asset), whereas a Bank Overdraft ({fmt_r(neg_amt)}) is money owed back to {bank} on short notice (Current Liability)."
    return _make_mcq(
        rng,
        subskill="13_bank_vs_bank_overdraft_distinction",
        title="Bank Balance vs Bank Overdraft",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Positive bank cash = business owns the money; Overdraft = business owes the bank.",
            "tier_2": "Money owned short-term = Current Asset; money owed short-term = Current Liability.",
            "tier_3": "Positive Bank = Current Asset; Bank Overdraft = Current Liability.",
        },
        misconception_tags=["classifies_bank_overdraft_as_asset"],
        question_family_id="bank_vs_overdraft",
    )


def _b14_creditors_vs_debtors_misconception(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    cust = rng.choice(NAMES)
    amt_sup = rng.randint(5, 19) * 1000
    amt_cust = rng.randint(2, 9) * 1000
    prompt = (
        f"{s['business']} bought goods on credit for {fmt_r(amt_sup)} from {sup} and also sold goods on credit for {fmt_r(amt_cust)} to {cust}. "
        f"Which statement accurately pairs the two accounts in the records of {s['business']}?"
    )
    ans = f"{sup} is a Creditor (Current Liability) and {cust} is a Debtor (Current Asset)"
    opts = [
        f"{sup} is a Creditor (Current Liability) and {cust} is a Debtor (Current Asset)",
        f"{sup} is a Debtor (Current Asset) and {cust} is a Creditor (Current Liability)",
        f"Both {sup} and {cust} are Operating Expenses",
        f"Both {sup} and {cust} are Current Assets",
    ]
    exp = f"{s['business']} owes {fmt_r(amt_sup)} to {sup} (Creditor = Current Liability), whereas {cust} owes {fmt_r(amt_cust)} to {s['business']} (Debtor = Current Asset)."
    return _make_mcq(
        rng,
        subskill="14_creditors_vs_debtors_misconception",
        title="Creditors vs Debtors",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Supplier you owe = Creditor; Customer who owes you = Debtor.",
            "tier_2": "Creditors = Liabilities (you pay them); Debtors = Assets (they pay you).",
            "tier_3": ans,
        },
        misconception_tags=["swaps_debtors_and_creditors"],
        question_family_id="creditors_vs_debtors",
    )


def _b15_total_liabilities_calculation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    loan = rng.randint(50, 140) * 1000
    cred = rng.randint(8, 25) * 1000
    overdraft = rng.randint(3, 12) * 1000
    debtors = rng.randint(4, 15) * 1000
    equip = rng.randint(15, 40) * 1000
    total_liab = loan + cred + overdraft
    ans = fmt_r(total_liab)
    prompt = (
        f"{s['business']} in {s['area']} lists these balances: Bank Loan (5-year) {fmt_r(loan)}, Creditors Control {fmt_r(cred)}, "
        f"Bank Overdraft {fmt_r(overdraft)}, Debtors Control {fmt_r(debtors)}, and Equipment {fmt_r(equip)}. "
        f"Calculate Total Liabilities."
    )
    steps = [
        f"Identify Liabilities (debts owed): Bank Loan ({fmt_r(loan)}) + Creditors Control ({fmt_r(cred)}) + Bank Overdraft ({fmt_r(overdraft)}).",
        f"Exclude Assets: Debtors Control ({fmt_r(debtors)}) and Equipment ({fmt_r(equip)}).",
        f"Total Liabilities = {fmt_r(loan)} + {fmt_r(cred)} + {fmt_r(overdraft)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="15_total_liabilities_calculation",
        title="Calculate Total Liabilities",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total_liab}", str(total_liab)],
        steps=steps,
        hints={
            "tier_1": "Only include amounts the business OWES to outside lenders or suppliers.",
            "tier_2": "Add Long-term Bank Loan + Creditors Control + Bank Overdraft (do not add Debtors or Equipment).",
            "tier_3": f"Total Liabilities = {ans}.",
        },
        misconception_tags=["includes_debtors_or_assets_in_liabilities"],
        question_family_id="total_liabilities_calc",
    )


def _b16_service_vs_trading_income(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(NAMES)
    area = rng.choice(AREAS)
    amt = rng.randint(12, 48) * 100
    svc_biz = rng.choice([
        ("plumbing repair service", "Current Income"),
        ("hair and beauty salon", "Current Income"),
        ("auto mechanical workshop", "Current Income"),
    ])
    prompt = (
        f"{owner} runs a {svc_biz[0]} in {area} and receives {fmt_r(amt)} cash from clients for services rendered today. "
        f"Which income account should be credited in the books?"
    )
    ans = "Current Income"
    opts = ["Current Income", "Sales", "Creditors Control", "Capital"]
    exp = f"Service enterprises earn revenue by providing skills/labour rather than reselling physical goods, so fees earned ({fmt_r(amt)}) are recorded as Current Income (whereas trading shops use Sales)."
    return _make_mcq(
        rng,
        subskill="16_service_vs_trading_income",
        title="Service Income vs Sales",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Does this business sell physical stock or provide a skilled service?",
            "tier_2": "Service businesses record service fees as Current Income; retail shops record goods sold as Sales.",
            "tier_3": "Correct account: Current Income.",
        },
        misconception_tags=["confuses_current_income_and_sales"],
        question_family_id="income_accounts",
    )


def _b17_operating_expenses_classification(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(8, 35) * 100
    exp_item = rng.choice(["Water and Electricity", "Telephone and Internet", "Wages", "Stationery", "Advertising"])
    prompt = (
        f"{s['business']} pays {fmt_r(amt)} for {exp_item} needed to operate during the month. "
        f"How does {exp_item} affect Owner's Equity?"
    )
    ans = "It is an Operating Expense, which decreases Owner's Equity"
    opts = [
        "It is an Operating Expense, which decreases Owner's Equity",
        "It is a Current Asset, which increases Owner's Equity",
        "It is a Long-term Liability, which increases Assets",
        "It is Capital invested by the owner",
    ]
    exp = f"Day-to-day running costs like {exp_item} ({fmt_r(amt)}) are consumed immediately, reduce profit, and therefore decrease Owner's Equity."
    return _make_mcq(
        rng,
        subskill="17_operating_expenses_classification",
        title="Operating Expenses & Equity Effect",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Are day-to-day running bills kept for future years, or used up immediately?",
            "tier_2": "Expenses reduce profit and therefore decrease Owner's Equity.",
            "tier_3": f"{exp_item} is an Operating Expense that decreases Owner's Equity.",
        },
        misconception_tags=["thinks_expenses_increase_equity"],
        question_family_id="operating_expenses",
    )


def _b18_asset_vs_expense_confusion(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    print_amt = rng.randint(4, 15) * 100
    printer_amt = rng.randint(4, 12) * 1000
    prompt = (
        f"{s['business']} buys a laser printer for {fmt_r(printer_amt)} (expected to last 4 years) and printer paper cartridges for {fmt_r(print_amt)} (used up this month). "
        f"Classify BOTH purchases correctly:"
    )
    ans = f"Printer ({fmt_r(printer_amt)}) = Fixed Asset (Equipment); Paper cartridges ({fmt_r(print_amt)}) = Expense (Stationery)"
    opts = [
        f"Printer ({fmt_r(printer_amt)}) = Fixed Asset (Equipment); Paper cartridges ({fmt_r(print_amt)}) = Expense (Stationery)",
        f"Both the printer and paper cartridges are Operating Expenses",
        f"Both the printer and paper cartridges are Current Assets",
        f"Printer ({fmt_r(printer_amt)}) = Expense; Paper cartridges ({fmt_r(print_amt)}) = Fixed Asset",
    ]
    exp = f"The laser printer ({fmt_r(printer_amt)}) provides lasting value over 4 years (Fixed Asset: Equipment), whereas the paper cartridges ({fmt_r(print_amt)}) are consumed immediately in operations (Expense: Stationery)."
    return _make_mcq(
        rng,
        subskill="18_asset_vs_expense_confusion",
        title="Asset vs Expense Distinction",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Compare lasting possessions (> 1 year) vs consumable supplies used up quickly.",
            "tier_2": "Printer -> Equipment (Fixed Asset); Paper -> Stationery (Expense).",
            "tier_3": ans,
        },
        misconception_tags=["treats_equipment_purchase_as_expense"],
        question_family_id="asset_vs_expense",
    )


def _b19_profit_calculation_basic(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    curr_inc = rng.randint(35, 85) * 1000
    rent_inc = rng.randint(4, 12) * 1000
    wages = rng.randint(12, 22) * 1000
    elec = rng.randint(2, 6) * 1000
    stat = rng.randint(1, 3) * 1000
    tot_inc = curr_inc + rent_inc
    tot_exp = wages + elec + stat
    profit = tot_inc - tot_exp
    ans = fmt_r(profit)

    card_svg = _svg_ledger_card(
        f"{s['business']} — Monthly Summary",
        f"Owner: {s['entrepreneur']} ({s['area']})",
        [
            ("Current Income", fmt_r(curr_inc)),
            ("Rent Income", fmt_r(rent_inc)),
            ("Wages Expense", fmt_r(wages)),
            ("Water & Electricity", fmt_r(elec)),
            ("Stationery Expense", fmt_r(stat)),
        ],
    )
    prompt = (
        f"Examine the Monthly Summary record provided for {s['business']}. "
        f"Calculate the Net Profit earned by {s['entrepreneur']} for the month."
    )
    steps = [
        f"Total Income = Current Income ({fmt_r(curr_inc)}) + Rent Income ({fmt_r(rent_inc)}) = {fmt_r(tot_inc)}.",
        f"Total Expenses = Wages ({fmt_r(wages)}) + Water & Electricity ({fmt_r(elec)}) + Stationery ({fmt_r(stat)}) = {fmt_r(tot_exp)}.",
        f"Net Profit = Total Income - Total Expenses = {fmt_r(tot_inc)} - {fmt_r(tot_exp)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="19_profit_calculation_basic",
        title="Calculate Net Profit",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{profit}", str(profit)],
        steps=steps,
        hints={
            "tier_1": "Group all Income items together and all Expense items together first.",
            "tier_2": "Net Profit = Total Income - Total Expenses.",
            "tier_3": f"{fmt_r(tot_inc)} - {fmt_r(tot_exp)} = {ans}.",
        },
        misconception_tags=["adds_expenses_to_income_for_profit"],
        question_family_id="profit_calc",
        marks=4,
        diagram_spec={"kind": "inline_svg", "svg": card_svg, "diagram_role": "context"},
    )


def _b20_loss_calculation_basic(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    inc = rng.randint(14, 28) * 1000
    exp_rent = rng.randint(8, 14) * 1000
    exp_wages = rng.randint(9, 16) * 1000
    exp_util = rng.randint(2, 5) * 1000
    tot_exp = exp_rent + exp_wages + exp_util
    loss = tot_exp - inc
    ans = fmt_r(loss)
    prompt = (
        f"During its opening month in {s['area']}, {s['business']} earned Total Income of {fmt_r(inc)}, "
        f"while incurring Rent Expense of {fmt_r(exp_rent)}, Wages of {fmt_r(exp_wages)}, and Utilities of {fmt_r(exp_util)}. "
        f"Calculate the Net Loss (enter the positive Rand amount of the loss)."
    )
    steps = [
        f"Total Expenses = {fmt_r(exp_rent)} + {fmt_r(exp_wages)} + {fmt_r(exp_util)} = {fmt_r(tot_exp)}.",
        f"Since Total Expenses ({fmt_r(tot_exp)}) > Total Income ({fmt_r(inc)}), the business made a Net Loss.",
        f"Net Loss = {fmt_r(tot_exp)} - {fmt_r(inc)} = {ans} (this decreases Owner's Equity).",
    ]
    return _make_typed(
        rng,
        subskill="20_loss_calculation_basic",
        title="Calculate Net Loss",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{loss}", str(loss), f"-{ans}"],
        steps=steps,
        hints={
            "tier_1": "Sum all three expense amounts and compare with Total Income.",
            "tier_2": "When Expenses exceed Income: Net Loss = Total Expenses - Total Income.",
            "tier_3": f"Total Expenses ({fmt_r(tot_exp)}) - Income ({fmt_r(inc)}) = {ans} Net Loss.",
        },
        misconception_tags=["confuses_profit_and_loss_direction"],
        question_family_id="loss_calc",
    )


def _b21_missing_income_or_expense_reverse(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    tot_inc = rng.randint(38, 95) * 1000
    profit = rng.randint(8, 25) * 1000
    tot_exp = tot_inc - profit
    ans = fmt_r(tot_exp)
    prompt = (
        f"At the end of the quarter, {s['business']} in {s['area']} earned Total Income of {fmt_r(tot_inc)} and achieved a Net Profit of {fmt_r(profit)}. "
        f"What were the Total Expenses for the quarter?"
    )
    steps = [
        f"Start with: Net Profit = Total Income - Total Expenses.",
        f"Rearrange: Total Expenses = Total Income - Net Profit.",
        f"Total Expenses = {fmt_r(tot_inc)} - {fmt_r(profit)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="21_missing_income_or_expense_reverse",
        title="Solve for Missing Total Expenses",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{tot_exp}", str(tot_exp)],
        steps=steps,
        hints={
            "tier_1": "Income covers both Expenses and Profit.",
            "tier_2": "Total Expenses = Total Income - Net Profit.",
            "tier_3": f"{fmt_r(tot_inc)} - {fmt_r(profit)} = {ans}.",
        },
        misconception_tags=["adds_profit_to_income_to_find_expenses"],
        question_family_id="reverse_profit_formula",
    )


def _b22_accounting_equation_missing_term(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    oe = rng.randint(60, 180) * 1000
    liab = rng.randint(15, 70) * 1000
    assets = oe + liab
    solve_for = rng.choice(["A", "L", "OE"])
    if solve_for == "A":
        ans = fmt_r(assets)
        prompt = f"{s['business']} has Owner's Equity of {fmt_r(oe)} and Liabilities of {fmt_r(liab)}. Using the Accounting Equation (A = OE + L), calculate Total Assets."
        steps = [f"A = OE + L", f"A = {fmt_r(oe)} + {fmt_r(liab)} = {ans}"]
        acc = [ans, f"R{assets}", str(assets)]
    elif solve_for == "L":
        ans = fmt_r(liab)
        prompt = f"{s['business']} holds Total Assets of {fmt_r(assets)} and Owner's Equity of {fmt_r(oe)}. Using A = OE + L, calculate Total Liabilities."
        steps = [f"L = A - OE", f"L = {fmt_r(assets)} - {fmt_r(oe)} = {ans}"]
        acc = [ans, f"R{liab}", str(liab)]
    else:
        ans = fmt_r(oe)
        prompt = f"{s['business']} has Total Assets of {fmt_r(assets)} and Total Liabilities of {fmt_r(liab)}. Calculate Owner's Equity (Net Worth)."
        steps = [f"OE = A - L", f"OE = {fmt_r(assets)} - {fmt_r(liab)} = {ans}"]
        acc = [ans, f"R{oe}", str(oe)]

    return _make_typed(
        rng,
        subskill="22_accounting_equation_missing_term",
        title="Accounting Equation Calculation",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=acc,
        steps=steps,
        hints={
            "tier_1": "Write down A = OE + L first.",
            "tier_2": "If solving for OE or L, subtract the known right-hand side term from Total Assets.",
            "tier_3": steps[-1],
        },
        misconception_tags=["reverses_accounting_equation_signs"],
        question_family_id="accounting_equation_numeric",
    )


def _b23_classify_accounts_table_drill(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("Vehicles", "Asset", "Fixed Asset"),
        ("Trading Stock", "Asset", "Current Asset"),
        ("Creditors Control", "Liability", "Current Liability"),
        ("Mortgage Bond", "Liability", "Long-term Liability"),
        ("Capital", "Owner's Equity", "Owner's Equity"),
        ("Current Income", "Income", "Operating Income"),
        ("Water & Electricity", "Expense", "Operating Expense"),
        ("Debtors Control", "Asset", "Current Asset"),
        ("Bank Overdraft", "Liability", "Current Liability"),
        ("Drawings", "Owner's Equity", "Reduces Owner's Equity"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Account Name", "Main Accounting Element", "Sub-classification"]
    table_rows = []
    cell_hints = {}
    for idx, (acct, elem, sub) in enumerate(chosen):
        table_rows.append([
            (acct, "given", False),
            (elem, "required", True),
            (sub, "required", True),
        ])
        cell_hints[f"t0_r{idx}_c1"] = f"Choose Asset, Liability, Owner's Equity, Income, or Expense for {acct}."
        cell_hints[f"t0_r{idx}_c2"] = f"Specify whether {acct} is Fixed/Current, Long-term/Current, etc."

    prompt = (
        f"Classify each account of {s['business']} in {s['area']} into its Main Accounting Element "
        f"(Asset, Liability, Owner's Equity, Income, or Expense) and its specific Sub-classification in the table below."
    )
    return _make_table(
        rng,
        subskill="23_classify_accounts_table_drill",
        title="Account Element Classification Table",
        prompt=prompt,
        journal_type="account_classification",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Assets are owned; Liabilities are owed; OE is owner's stake; Income & Expenses affect profit.",
            "tier_2": "Distinguish long-term (> 1 year) from short-term (<= 1 year) for Assets and Liabilities.",
            "tier_3": "; ".join(f"{a}: {e} ({sub})" for a, e, sub in chosen),
        },
        misconception_tags=["misclassifies_main_accounting_element"],
        question_family_id="classification_table",
    )


def _b24_accounting_equation_table_effect(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    cap_amt = rng.randint(30, 80) * 1000
    equip_amt = rng.randint(6, 18) * 1000
    exp_amt = rng.randint(8, 25) * 100
    headers = ["Transaction", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    tx1 = f"{owner} deposits {fmt_r(cap_amt)} as initial Capital."
    tx2 = f"Bought workshop equipment on credit for {fmt_r(equip_amt)}."
    tx3 = f"Paid monthly telephone bill of {fmt_r(exp_amt)} via EFT."

    c_str = f"+{fmt_r(cap_amt)}"
    e_str = f"+{fmt_r(equip_amt)}"
    x_str = f"-{fmt_r(exp_amt)}"
    table_rows = [
        [(tx1, "given", False), (c_str, "required", True), (c_str, "required", True), ("0", "required", True)],
        [(tx2, "given", False), (e_str, "required", True), ("0", "required", True), (e_str, "required", True)],
        [(tx3, "given", False), (x_str, "required", True), (x_str, "required", True), ("0", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": f"Bank (Asset) increases by {fmt_r(cap_amt)} -> +{fmt_r(cap_amt)}.",
        "t0_r0_c2": f"Capital increases Owner's Equity -> +{fmt_r(cap_amt)}.",
        "t0_r0_c3": "No liability created -> 0.",
        "t0_r1_c1": f"Equipment (Asset) increases -> +{fmt_r(equip_amt)}.",
        "t0_r1_c2": "Equipment purchase on credit does not change OE -> 0.",
        "t0_r1_c3": f"Creditors Control (Liability) increases -> +{fmt_r(equip_amt)}.",
        "t0_r2_c1": f"Bank (Asset) decreases -> -{fmt_r(exp_amt)}.",
        "t0_r2_c2": f"Telephone (Expense) reduces Owner's Equity -> -{fmt_r(exp_amt)}.",
        "t0_r2_c3": "Paid immediately via EFT, so Liabilities unchanged -> 0.",
    }
    prompt = (
        f"Complete the Accounting Equation table (A = OE + L) below for {s['business']} in {s['area']}. "
        f"Use +R..., -R..., or 0 in every cell so that each row remains balanced."
    )
    return _make_table(
        rng,
        subskill="24_accounting_equation_table_effect",
        title="Accounting Equation Table Drill",
        prompt=prompt,
        journal_type="accounting_equation",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Check the left side (A) equals the sum of the right side (OE + L) on every row.",
            "tier_2": "Capital (+A, +OE), Credit purchase (+A, +L), Cash expense (-A, -OE).",
            "tier_3": f"Row 1: {c_str}, {c_str}, 0 | Row 2: {e_str}, 0, {e_str} | Row 3: {x_str}, {x_str}, 0.",
        },
        misconception_tags=["unbalanced_accounting_equation_row"],
        question_family_id="equation_table_drill",
    )


def _b25_transaction_to_equity_impact(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 1000
    cases = [
        (
            f"{s['business']} buys a delivery motorcycle for {fmt_r(amt)} and pays immediately via EFT from the business bank account. What is the overall effect on Total Assets?",
            "Zero overall change in Total Assets (+Asset Vehicles and -Asset Bank cancel out)",
            [
                "Zero overall change in Total Assets (+Asset Vehicles and -Asset Bank cancel out)",
                f"Total Assets increase by {fmt_r(amt)}",
                f"Total Assets decrease by {fmt_r(amt)}",
                f"Owner's Equity decreases by {fmt_r(amt)}",
            ],
            f"Vehicles (+{fmt_r(amt)}) increases Assets while Bank (-{fmt_r(amt)}) decreases Assets by the exact same amount, leaving Total Assets unchanged.",
        ),
        (
            f"{s['business']} receives {fmt_r(amt)} rent income from a tenant occupying spare office space. What is the effect on A = OE + L?",
            f"Assets increase by {fmt_r(amt)} and Owner's Equity increases by {fmt_r(amt)}",
            [
                f"Assets increase by {fmt_r(amt)} and Owner's Equity increases by {fmt_r(amt)}",
                f"Assets increase by {fmt_r(amt)} and Liabilities increase by {fmt_r(amt)}",
                f"Owner's Equity decreases by {fmt_r(amt)} and Liabilities decrease by {fmt_r(amt)}",
                "No effect on Assets or Owner's Equity",
            ],
            f"Bank (Asset) increases by {fmt_r(amt)}, and Rent Income increases profit and therefore Owner's Equity by {fmt_r(amt)}.",
        ),
    ]
    prompt, ans, opts, exp = rng.choice(cases)
    return _make_mcq(
        rng,
        subskill="25_transaction_to_equity_impact",
        title="Single Transaction Equation Effect",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Identify both accounts affected by the transaction before judging the net effect.",
            "tier_2": "Swapping cash for equipment changes Asset composition only (net 0 change); earning income raises both A and OE.",
            "tier_3": ans,
        },
        misconception_tags=["misses_asset_swap_net_zero"],
        question_family_id="transaction_equation_mcq",
    )


ARCHETYPES_01_25 = {
    "01_capital_definition_contribution": _b01_capital_definition_contribution,
    "02_own_vs_borrowed_capital": _b02_own_vs_borrowed_capital,
    "03_owners_equity_net_worth_calc": _b03_owners_equity_net_worth_calc,
    "04_drawings_cash_and_goods_impact": _b04_drawings_cash_and_goods_impact,
    "05_fixed_non_current_assets_id": _b05_fixed_non_current_assets_id,
    "06_current_assets_id": _b06_current_assets_id,
    "07_cash_float_vs_petty_cash": _b07_cash_float_vs_petty_cash,
    "08_debtors_control_current_asset": _b08_debtors_control_current_asset,
    "09_financial_investments_as_assets": _b09_financial_investments_as_assets,
    "10_total_assets_calculation": _b10_total_assets_calculation,
    "11_long_term_liabilities_id": _b11_long_term_liabilities_id,
    "12_current_liabilities_id": _b12_current_liabilities_id,
    "13_bank_vs_bank_overdraft_distinction": _b13_bank_vs_bank_overdraft_distinction,
    "14_creditors_vs_debtors_misconception": _b14_creditors_vs_debtors_misconception,
    "15_total_liabilities_calculation": _b15_total_liabilities_calculation,
    "16_service_vs_trading_income": _b16_service_vs_trading_income,
    "17_operating_expenses_classification": _b17_operating_expenses_classification,
    "18_asset_vs_expense_confusion": _b18_asset_vs_expense_confusion,
    "19_profit_calculation_basic": _b19_profit_calculation_basic,
    "20_loss_calculation_basic": _b20_loss_calculation_basic,
    "21_missing_income_or_expense_reverse": _b21_missing_income_or_expense_reverse,
    "22_accounting_equation_missing_term": _b22_accounting_equation_missing_term,
    "23_classify_accounts_table_drill": _b23_classify_accounts_table_drill,
    "24_accounting_equation_table_effect": _b24_accounting_equation_table_effect,
    "25_transaction_to_equity_impact": _b25_transaction_to_equity_impact,
}
