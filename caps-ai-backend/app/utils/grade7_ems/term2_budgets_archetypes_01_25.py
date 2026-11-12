"""Grade 7 Economic and Management Sciences - Term 2: Budgets (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/EMS_Gr7/Term 2/03. Budgets.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, NAMES, get_ems_scenario


def _fmt_r(val: int | float) -> str:
    """Format Rand amounts cleanly with space thousands separator."""
    if isinstance(val, float) and not val.is_integer():
        sign = "-" if val < 0 else ""
        abs_v = abs(val)
        whole, dec = f"{abs_v:.2f}".split(".")
        whole_fmt = f"{int(whole):,}".replace(",", " ")
        return f"{sign}R{whole_fmt},{dec}"
    sign = "-" if val < 0 else ""
    return f"{sign}R{abs(int(val)):,}".replace(",", " ")


def _make_mcq(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    sol: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    opts = [correct] + distractors[:3]
    rng.shuffle(opts)
    idx = opts.index(correct)
    item: Dict[str, Any] = {
        "id": f"g7_ems_bg_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "options": opts,
        "correct_index": str(idx),
        "correct_answer": correct,
        "sample_answer": correct,
        "ideal_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "solution": sol,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(2, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": f"Select: {correct}"},
        "marking_points": [correct],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}],
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_budgets",
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _make_calc(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    val: int | float,
    formula: str,
    sol: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 3,
    unit: str = "R",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    is_int = isinstance(val, int) or float(val).is_integer()
    clean_num = str(int(val)) if is_int else f"{val:.2f}".rstrip("0").rstrip(".")
    disp = _fmt_r(val) if unit == "R" else f"{clean_num} {unit}".strip()
    item: Dict[str, Any] = {
        "id": f"g7_ems_bg_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "calc",
        "modality": "math",
        "solution_type": "calculation",
        "prompt": prompt,
        "question": prompt,
        "formula": formula,
        "unit": unit,
        "correct_answer": clean_num,
        "expected_answer": clean_num,
        "sample_answer": disp,
        "ideal_answer": disp,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "solution": sol,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(2, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": f"Expected answer: {disp}"},
        "marking_points": [disp],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_formula", "desc": f"Correct formula ({formula})", "marks": 1, "editable": True},
                {"id": "mp_final", "desc": f"Accurate result: {disp}", "marks": max(1, marks - 1), "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_budgets",
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _make_typed(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    marking_points: List[str],
    key_concepts: List[str],
    sample_answer: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    item: Dict[str, Any] = {
        "id": f"g7_ems_bg_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "typed",
        "modality": "semantic",
        "solution_type": "marking_points",
        "prompt": prompt,
        "question": prompt,
        "marking_points": marking_points,
        "key_concepts": key_concepts,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "correct_answer": sample_answer,
        "worked_solution": sample_answer,
        "explanation": sample_answer,
        "canonical_solution": sample_answer,
        "solution": sample_answer,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": sample_answer},
        "guidelines": [f"Address {len(marking_points)} distinct points clearly."],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{i + 1}", "desc": mp, "marks": 1, "concepts": key_concepts[:3], "editable": True}
                for i, mp in enumerate(marking_points)
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_budgets",
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _make_ledger(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    md_memo: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 5,
) -> Dict[str, Any]:
    return {
        "id": f"g7_ems_bg_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "tables": [{"headers": headers, "rows": rows}],
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "sample_answer": md_memo,
        "ideal_answer": md_memo,
        "correct_answer": md_memo,
        "worked_solution": md_memo,
        "explanation": md_memo,
        "canonical_solution": md_memo,
        "solution": md_memo,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(4, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": "Complete all highlighted table cells carefully."},
        "marking_points": [f"{k} -> {v}" for k, v in correct_map.items()],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"cell_{i + 1}", "desc": f"Cell {k}: {v}", "marks": 1, "editable": True}
                for i, (k, v) in enumerate(correct_map.items())
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_budgets",
    }


def _svg_personal_allocation(person: str, inc: int, fixed: int, var: int) -> str:
    """Seed-varied horizontal allocation bar visual for a personal budget."""
    sav = inc - fixed - var
    w_tot = 440
    w_fix = max(55, int(round((fixed / max(inc, 1)) * w_tot)))
    w_var = max(55, int(round((var / max(inc, 1)) * w_tot)))
    w_sav = max(35, w_tot - w_fix - w_var)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 190" width="540" height="190">'
        '<rect width="540" height="190" fill="#f8fafc" rx="8"/>'
        f'<text x="270" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{person}: Monthly Budget Allocation (Income {_fmt_r(inc)})</text>'
        f'<rect x="50" y="58" width="{w_fix}" height="50" fill="#0284c7" rx="3"/>'
        f'<text x="{50 + w_fix // 2}" y="87" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#ffffff">Fixed {_fmt_r(fixed)}</text>'
        f'<rect x="{50 + w_fix}" y="58" width="{w_var}" height="50" fill="#f59e0b" rx="3"/>'
        f'<text x="{50 + w_fix + w_var // 2}" y="87" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Var {_fmt_r(var)}</text>'
        f'<rect x="{50 + w_fix + w_var}" y="58" width="{w_sav}" height="50" fill="#16a34a" rx="3"/>'
        f'<text x="{50 + w_fix + w_var + w_sav // 2}" y="87" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#ffffff">Save ?</text>'
        f'<text x="270" y="138" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#334155">Total Expenses = Fixed ({_fmt_r(fixed)}) + Variable ({_fmt_r(var)}) | Remaining Savings = {_fmt_r(sav)}</text>'
        '<text x="270" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#475569">Formula: Planned Savings = Total Net Income - Total Expenses</text>'
        "</svg>"
    )


def _svg_four_month_cashflow(person: str, inc: int, e1: int, e2: int, e3: int, e4: int) -> str:
    """Seed-varied 4-month paired Income vs Expense bar chart."""
    months = [("Jan", e1), ("Feb", e2), ("Mar", e3), ("Apr", e4)]
    max_v = max(inc, e1, e2, e3, e4, 1)
    bars = []
    for idx, (m_lbl, exp) in enumerate(months):
        x0 = 62 + idx * 110
        h_i = max(22, int(round((inc / max_v) * 112)))
        h_e = max(22, int(round((exp / max_v) * 112)))
        bars.append(
            f'<rect x="{x0}" y="{166 - h_i}" width="32" height="{h_i}" fill="#0284c7" rx="3"/>'
            f'<rect x="{x0 + 36}" y="{166 - h_e}" width="32" height="{h_e}" fill="#e11d48" rx="3"/>'
            f'<text x="{x0 + 34}" y="184" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e293b">{m_lbl}</text>'
            f'<text x="{x0 + 52}" y="{160 - h_e}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#9f1239">{_fmt_r(exp)}</text>'
        )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 218" width="540" height="218">'
        '<rect width="540" height="218" fill="#f8fafc" rx="8"/>'
        f'<text x="270" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{person}: 4-Month Budget (Blue Income {_fmt_r(inc)} vs Red Expenses)</text>'
        '<line x1="45" y1="166" x2="500" y2="166" stroke="#64748b" stroke-width="2"/>'
        + "".join(bars)
        + "</svg>"
    )


def build_01_budget_definition_future_earnings_expenses(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    period = rng.choice(["July", "the next 3 months", "next financial year"])
    prompt = (
        f"{name} sits down to draw up a personal budget for {period} in {rng.choice(AREAS)}. "
        f"What is the accurate EMS definition of a budget?"
    )
    correct = "A written financial schedule of expected future income and planned expenses over a specific future period."
    distractors = [
        "A list of cash receipts showing goods already bought six months ago.",
        "A legal court document declaring personal bankruptcy after overspending.",
        "An estimate of historical building depreciation owned by a municipality.",
    ]
    sol = f"A budget is forward-looking: it plans **expected future earnings and expected expenses** for {period} so {name} can spend, save, or borrow wisely."
    return _make_mcq(
        rng, "01_budget_definition_future_earnings_expenses", "Budget Definition", prompt,
        correct, distractors, sol,
        "Ask whether a budget looks backward at history or forward at future income and spending.",
        "It estimates future earnings and planned expenses over a chosen time period.",
        ["ems_confuses_budget_with_history"],
    )


def build_02_three_financial_choices_spend_save_borrow(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    goal = rng.choice(["buying a second-hand scooter", "paying university registration fees", "upgrading home solar panels"])
    prompt = (
        f"When planning {goal}, how does compiling a budget guide {name}'s key financial decisions?"
    )
    correct = "It shows realistically how much money can be spent, how much should be saved, and whether borrowing is affordable."
    distractors = [
        "It guarantees banks must lend unlimited money interest-free regardless of income.",
        "It eliminates all living costs such as municipal water, electricity, and groceries.",
        "It replaces the need to ever earn a salary or keep bank statements.",
    ]
    sol = "According to the curriculum, budgeting clarifies three linked financial actions: **what to spend, what to save, and what/whether to borrow**."
    return _make_mcq(
        rng, "02_three_financial_choices_spend_save_borrow", "Spend, Save & Borrow Purpose", prompt,
        correct, distractors, sol,
        "Recall the three action verbs budgets help us decide.",
        "Think: Spend, Save, and Borrow.",
        ["ems_narrow_budget_purpose"],
    )


def build_03_budget_vs_historical_financial_records(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} keeps both a shoebox of last year's supplier invoices for {sc['business_type']} and a new monthly budget for next quarter. "
        f"Explain two differences between historical financial records and a budget."
    )
    mps = [
        "Time orientation: Financial records track past completed transactions; a budget forecasts expected future inflows and outflows.",
        "Flexibility & purpose: Records prove actual past cash movements and profit; budgets guide planning, targets, and spending control before money is spent.",
        "Corrective link: Past records supply realistic cost figures used to make accurate future budget estimates.",
    ]
    sample = (
        "1. **Past vs Future**: Past invoices record actual completed spending; a budget estimates future expected income and expenses.\n"
        "2. **Proof vs Planning**: Past records verify history for SARS/tracking, while a budget sets targets beforehand to control cash flow."
    )
    return _make_typed(
        rng, "03_budget_vs_historical_financial_records", "Budget vs Historical Records", prompt,
        mps, ["past", "future", "forecast", "actual", "control"], sample,
        "Compare the time direction (already happened vs planned ahead) and how managers use each document.",
        "Note also how last year's actual figures help refine this year's budget.",
        ["ems_conflates_budget_and_ledger_history"],
    )


def build_04_budget_tracking_affordability_awareness(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    small_amt = rng.choice([25, 35, 45])
    days = rng.choice([20, 22])
    tot = small_amt * days
    prompt = (
        f"Without writing down expenses, {name} buys takeaway lunches costing {_fmt_r(small_amt)} on {days} workdays per month ({_fmt_r(tot)} total) "
        f"and then struggles to pay rent. Explain how a personal budget helps prevent this shortfall."
    )
    mps = [
        f"Reveals hidden cumulative small leaks ({days} × {_fmt_r(small_amt)} = {_fmt_r(tot)}/month).",
        "Forces essential priorities (rent, electricity, transport) to be allocated before discretionary treats.",
        "Provides exact affordability limits showing how much can safely be spent each week.",
    ]
    sample = (
        f"Writing a budget forces {name} to add up frequent small costs ({_fmt_r(tot)}/month) alongside essential rent, "
        "making affordability limits visible before overspending happens."
    )
    return _make_typed(
        rng, "04_budget_tracking_affordability_awareness", "Budgeting Reveals Hidden Spending", prompt,
        mps, ["affordability", "cumulative", "priorities", "essentials", "tracking"], sample,
        "Consider why small daily purchases become invisible unless totalled monthly.",
        "Explain prioritising necessities (rent) over impulse wants.",
        ["ems_ignores_small_recurring_leaks"],
    )


def build_05_new_business_three_budgeting_steps(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} is opening a brand-new {sc['business_type']} in {sc['area']} with zero past trading history of its own. "
        f"Which three-step budgeting sequence should {sc['entrepreneur']} follow?"
    )
    correct = "Research similar existing businesses, make careful income/cost estimates, and revise the budget once real figures arrive."
    distractors = [
        "Guess random numbers once, lock them permanently, and refuse all adjustments.",
        "Wait five full years before estimating monthly rent, electricity, or stock costs.",
        "Copy a household grocery receipt directly and skip calculating projected revenue.",
    ]
    sol = "New businesses start by (1) **researching similar businesses**, (2) **making careful estimates**, and (3) **revising as real actual figures emerge**."
    return _make_mcq(
        rng, "05_new_business_three_budgeting_steps", "Three New-Business Budgeting Steps", prompt,
        correct, distractors, sol,
        "Since a start-up has no past books yet, where can it get benchmarks and what must happen later?",
        "Sequence: Research -> Careful estimates -> Revise with actual results.",
        ["ems_treats_budget_as_unchangeable"],
    )


def build_06_net_take_home_pay_after_salary_deductions(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    gross = rng.randrange(14000, 26000, 1000)
    tax = rng.randrange(1600, 3200, 200)
    med = rng.randrange(1200, 2400, 200)
    pens = rng.randrange(800, 1600, 200)
    net_pay = gross - tax - med - pens
    prompt = (
        f"{name} earns a gross salary of {_fmt_r(gross)} per month. Before reaching {name}'s bank account, monthly deductions are "
        f"PAYE Income Tax {_fmt_r(tax)}, Medical Aid {_fmt_r(med)}, and Pension Fund {_fmt_r(pens)}. "
        f"Calculate {name}'s monthly take-home pay available for the personal budget (numbers only)."
    )
    sol = f"Net Take-home Salary = {_fmt_r(gross)} - ({_fmt_r(tax)} + {_fmt_r(med)} + {_fmt_r(pens)}) = **{_fmt_r(net_pay)}**"
    return _make_calc(
        rng, "06_net_take_home_pay_after_salary_deductions", "Net Take-Home Salary for Budget", prompt,
        net_pay, "Net Salary = Gross Salary - Total Deductions", sol,
        "Always budget using Net Take-Home Pay after tax, medical aid, and pension deductions.",
        f"{gross} - {tax + med + pens} = {net_pay}.",
        ["ems_budgets_using_gross_salary"], marks=3,
    )


def build_07_personal_budget_total_income_and_expenses_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    rent = rng.randrange(3200, 5600, 400)
    food = rng.randrange(1800, 3000, 200)
    util = rng.randrange(600, 1200, 100)
    transp = rng.randrange(700, 1500, 100)
    cell = rng.randrange(250, 550, 50)
    tot_exp = rent + food + util + transp + cell
    prompt = (
        f"{name} budgets monthly expenses: Rent {_fmt_r(rent)}, Groceries {_fmt_r(food)}, Water & Electricity {_fmt_r(util)}, "
        f"Transport {_fmt_r(transp)}, and Cellphone/Data {_fmt_r(cell)}. Calculate Total Budgeted Expenses (numbers only)."
    )
    sol = f"Total Expenses = {_fmt_r(rent)} + {_fmt_r(food)} + {_fmt_r(util)} + {_fmt_r(transp)} + {_fmt_r(cell)} = **{_fmt_r(tot_exp)}**"
    return _make_calc(
        rng, "07_personal_budget_total_income_and_expenses_calc", "Total Budgeted Expenses Calculation", prompt,
        tot_exp, "Total Expenses = Sum of all Expense Line Items", sol,
        "Add all five monthly expense items carefully.",
        f"Sum = {tot_exp}.",
        ["ems_expense_summation_error"], marks=3,
    )


def build_08_personal_budget_monthly_savings_surplus_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    sal = rng.randrange(12000, 21000, 1000)
    tutor = rng.randrange(1000, 3000, 500)
    tot_inc = sal + tutor
    tot_exp = rng.randrange(9000, sal - 500, 500)
    savings = tot_inc - tot_exp
    prompt = (
        f"{name} budgets monthly income from Net Salary ({_fmt_r(sal)}) plus weekend tutoring ({_fmt_r(tutor)}), "
        f"and plans total monthly expenses of {_fmt_r(tot_exp)}. Calculate {name}'s budgeted monthly Savings/Surplus (numbers only)."
    )
    sol = (
        f"Total Income = {_fmt_r(sal)} + {_fmt_r(tutor)} = {_fmt_r(tot_inc)}\n"
        f"Budgeted Savings = Total Income - Total Expenses = {_fmt_r(tot_inc)} - {_fmt_r(tot_exp)} = **{_fmt_r(savings)}**"
    )
    return _make_calc(
        rng, "08_personal_budget_monthly_savings_surplus_calc", "Personal Budget Savings Surplus", prompt,
        savings, "Savings = Total Budgeted Income - Total Budgeted Expenses", sol,
        "Sum all budgeted income sources before subtracting total planned expenses.",
        f"{tot_inc} - {tot_exp} = {savings}.",
        ["ems_forgets_secondary_income_stream"], marks=4,
    )


def build_09_personal_budget_deficit_identification_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    inc = rng.randrange(8500, 13500, 500)
    exp = inc + rng.randrange(1000, 3500, 500)
    diff = inc - exp
    prompt = (
        f"{name}'s monthly take-home income is {_fmt_r(inc)}, while planned household expenses add up to {_fmt_r(exp)}. "
        f"Calculate the monthly budget shortfall/deficit, keeping the negative sign (numbers only)."
    )
    sol = f"Budget Result = Income - Expenses = {_fmt_r(inc)} - {_fmt_r(exp)} = **{_fmt_r(diff)}** (Deficit)"
    return _make_calc(
        rng, "09_personal_budget_deficit_identification_calc", "Budget Deficit Calculation", prompt,
        diff, "Budget Surplus/Deficit = Income - Expenses", sol,
        "When expenses exceed income, Income - Expenses produces a negative deficit.",
        f"{inc} - {exp} = {diff}.",
        ["ems_drops_deficit_negative_sign"], marks=3,
    )


def build_10_priya_style_personal_budget_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    net_sal = rng.randrange(13500, 19500, 500)
    rent = rng.randrange(3600, 4800, 200)
    car = rng.randrange(1800, 2600, 200)
    elec = rng.randrange(600, 1000, 100)
    groc = rng.randrange(2200, 3200, 200)
    ins = rng.randrange(500, 900, 100)
    tot_exp = rent + car + elec + groc + ins
    savings = net_sal - tot_exp
    headers = ["Personal Budget Item", "Category", "Budget (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Net monthly salary", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Income", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(net_sal), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Flat rent", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(rent), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Car instalment", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(car), "editable": False, "prefilled": True}],
        [{"cell_id": "r3_c0", "value": "Electricity & water", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": str(elec), "editable": False, "prefilled": True}],
        [{"cell_id": "r4_c0", "value": "Groceries", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": str(groc), "editable": False, "prefilled": True}],
        [{"cell_id": "r5_c0", "value": "Insurance", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": str(ins), "editable": False, "prefilled": True}],
        [{"cell_id": "r6_c0", "value": "Total Expenses", "editable": False, "prefilled": True},
         {"cell_id": "r6_c1", "value": "Subtotal", "editable": False, "prefilled": True},
         {"cell_id": "r6_c2", "value": "", "editable": True, "expected": str(tot_exp)}],
        [{"cell_id": "r7_c0", "value": "Planned Monthly Savings", "editable": False, "prefilled": True},
         {"cell_id": "r7_c1", "value": "", "editable": True, "expected": "Surplus"},
         {"cell_id": "r7_c2", "value": "", "editable": True, "expected": str(savings)}],
    ]
    cmap = {"r6_c2": str(tot_exp), "r7_c1": "Surplus", "r7_c2": str(savings)}
    chints = {
        "r6_c2": "Add all 5 expense items (digits only).",
        "r7_c1": "Enter 'Surplus' or 'Deficit'.",
        "r7_c2": "Subtract Total Expenses from Net Monthly Salary.",
    }
    md_memo = (
        f"| Personal Budget Item | Category | Budget (R) |\n|---|---|---:|\n"
        f"| Net monthly salary | Income | {net_sal} |\n| Flat rent | Expense | {rent} |\n"
        f"| Car instalment | Expense | {car} |\n| Electricity & water | Expense | {elec} |\n"
        f"| Groceries | Expense | {groc} |\n| Insurance | Expense | {ins} |\n"
        f"| **Total Expenses** | Subtotal | **{tot_exp}** |\n| **Planned Monthly Savings** | **Surplus** | **{savings}** |"
    )
    prompt = f"Complete {name}'s monthly Personal Budget table below (enter plain numbers without 'R' or spaces)."
    return _make_ledger(
        rng, "10_priya_style_personal_budget_table", "Personal Budget Table Completion",
        prompt, headers, rows, cmap, chints, md_memo,
        "Sum all 5 expense lines first, then subtract from net salary.",
        f"Total Expenses = {tot_exp}; Savings = {net_sal} - {tot_exp} = {savings} (Surplus).",
        ["ems_personal_budget_table_error"], marks=6,
    )


def build_11_personal_budget_allocation_bar_visual(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    inc = rng.randrange(12000, 22000, 1000)
    fixed = rng.randrange(5000, 8000, 500)
    var = rng.randrange(2500, 4500, 500)
    sav = inc - fixed - var
    svg = _svg_personal_allocation(name, inc, fixed, var)
    prompt = (
        f"Inspect {name}'s monthly income allocation bar: Total Net Income is {_fmt_r(inc)}, divided into Fixed Expenses ({_fmt_r(fixed)}), "
        f"Variable Expenses ({_fmt_r(var)}), and Planned Savings. Calculate {name}'s Planned Savings (numbers only)."
    )
    sol = f"Planned Savings = {_fmt_r(inc)} - ({_fmt_r(fixed)} + {_fmt_r(var)}) = **{_fmt_r(sav)}**."
    return _make_calc(
        rng, "11_personal_budget_allocation_bar_visual", "Budget Allocation Bar Visual", prompt,
        sav, "Savings = Net Income - (Fixed Expenses + Variable Expenses)", sol,
        "The full bar equals Net Income; subtract both blue Fixed and amber Variable segments.",
        f"{inc} - ({fixed} + {var}) = {sav}.",
        ["ems_budget_bar_subtraction_error"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_12_fixed_vs_variable_personal_expenses_classify(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    rent = rng.randrange(3000, 5500, 500)
    q_fixed = rng.choice([True, False])
    if q_fixed:
        prompt = f"In {name}'s household budget, which item is a **Fixed Expense** that stays constant every month regardless of short-term choices?"
        correct = f"Monthly apartment lease rent of {_fmt_r(rent)}"
        distractors = [
            "Weekend cinema and restaurant outings",
            "Holiday petrol refills for spontaneous road trips",
            "Impulse clothing and snack purchases",
        ]
        sol = f"**{correct}** is contractually fixed at the same amount each month."
    else:
        prompt = f"In {name}'s household budget, which item is a **Variable Expense** that fluctuates from month to month depending on usage?"
        correct = "Electricity units and discretionary groceries/entertainment"
        distractors = [
            f"Fixed monthly flat rent of {_fmt_r(rent)}",
            "A fixed 36-month car instalment contract",
            "Fixed monthly funeral policy premium",
        ]
        sol = f"**{correct}** changes each month depending on household consumption and choices, making it easier to trim in a tight month."
    return _make_mcq(
        rng, "12_fixed_vs_variable_personal_expenses_classify", "Fixed vs Variable Personal Expenses", prompt,
        correct, distractors, sol,
        "Ask whether a signed contract fixes the Rand amount each month or whether personal usage changes it.",
        "Rent/bond instalments = Fixed; electricity/entertainment/takeaways = Variable.",
        ["ems_confuses_fixed_and_variable_expenses"],
    )


def build_13_personal_fixed_variable_budget_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    r_amt = rng.randrange(3500, 5500, 500)
    c_amt = rng.randrange(1500, 2500, 250)
    e_amt = rng.randrange(400, 900, 100)
    g_amt = rng.randrange(1800, 3000, 200)
    headers = ["Household Expense Item", "Amount (R)", "Fixed or Variable", "Priority (Essential or Want)"]
    rows_meta = [
        ("Contractual home rent", r_amt, "Fixed", "Essential"),
        ("Fixed car loan instalment", c_amt, "Fixed", "Essential"),
        ("Weekend restaurant takeaways", e_amt, "Variable", "Want"),
        ("Electricity & groceries", g_amt, "Variable", "Essential"),
    ]
    rows: List[List[Dict[str, Any]]] = []
    cmap: Dict[str, str] = {}
    chints: Dict[str, str] = {}
    md_lines = [f"| {' | '.join(headers)} |", "|---|---:|---|---|"]
    for i, (item, amt, fv, pr) in enumerate(rows_meta):
        c2, c3 = f"r{i}_c2", f"r{i}_c3"
        cmap[c2], cmap[c3] = fv, pr
        chints[c2] = "Enter 'Fixed' or 'Variable'."
        chints[c3] = "Enter 'Essential' or 'Want'."
        rows.append([
            {"cell_id": f"r{i}_c0", "value": item, "editable": False, "prefilled": True},
            {"cell_id": f"r{i}_c1", "value": _fmt_r(amt), "editable": False, "prefilled": True},
            {"cell_id": c2, "value": "", "editable": True, "expected": fv},
            {"cell_id": c3, "value": "", "editable": True, "expected": pr},
        ])
        md_lines.append(f"| {item} | {_fmt_r(amt)} | {fv} | {pr} |")
    prompt = f"Classify {name}'s four expenses below using **Fixed**/**Variable** and **Essential**/**Want**."
    return _make_ledger(
        rng, "13_personal_fixed_variable_budget_table", "Fixed/Variable & Essential/Want Table",
        prompt, headers, rows, cmap, chints, "\n".join(md_lines),
        "Fixed = constant contractual amount; Variable = changes with use/behaviour.",
        "Note that variable food/electricity can still be Essential, unlike takeaways (Want).",
        ["ems_variable_equals_want_fallacy"], marks=8,
    )


def build_14_correcting_personal_budget_deficit_spending_cuts(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    deficit = rng.randrange(700, 1800, 100)
    prompt = (
        f"{name}'s monthly budget currently ends in a deficit of -{_fmt_r(deficit)} after paying rent, transport, groceries, "
        f"restaurant outings, and streaming subscriptions. Describe two practical, realistic budget adjustments to remove the deficit."
    )
    mps = [
        f"Target non-essential variable wants first (e.g., trim restaurant outings and extra streaming by at least {_fmt_r(deficit)}).",
        "Leave contractual essentials like rent and work transport intact until income grows or lease ends.",
        "Consider realistic side-income boosts (overtime/weekend tutoring) alongside variable spending cuts.",
    ]
    sample = (
        f"1. **Cut Discretionary Variable Wants**: Reduce takeaways, dining out, and non-essential subscriptions by {_fmt_r(deficit)}+ per month.\n"
        "2. **Protect Contractual Essentials / Boost Income**: Keep rent and work travel secure while seeking extra weekend income if needed."
    )
    return _make_typed(
        rng, "14_correcting_personal_budget_deficit_spending_cuts", "Correcting a Personal Budget Deficit", prompt,
        mps, ["variable", "wants", "essentials", "cut", "income"], sample,
        "Which costs can be cut immediately vs which are locked in by contracts or survival needs?",
        "Target discretionary wants before cutting rent or food.",
        ["ems_cuts_essentials_before_wants"],
    )


def build_15_emergency_savings_separate_from_goal_purchase(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    car_goal = rng.randrange(35000, 75000, 5000)
    emerg = rng.randrange(6000, 14000, 2000)
    prompt = (
        f"{name} wants to buy a used car costing {_fmt_r(car_goal)} and currently holds {_fmt_r(emerg)} in emergency savings. "
        f"Why does EMS advise keeping emergency savings separate from the car-purchase fund?"
    )
    correct = "So unexpected medical bills, home repairs, or job shocks never force costly high-interest borrowing or derail essentials."
    distractors = [
        "Because South African banks forbid holding more than one savings goal simultaneously.",
        "So all emergency reserves get spent automatically on flashy car accessories.",
        "Because emergency cash reduces a person's personal net worth immediately.",
    ]
    sol = f"Keeping {_fmt_r(emerg)} untouched as an emergency buffer ensures unexpected crises don't wipe out {name}'s financial safety net or force emergency loans."
    return _make_mcq(
        rng, "15_emergency_savings_separate_from_goal_purchase", "Protecting Emergency Savings", prompt,
        correct, distractors, sol,
        "Think about what happens if your fridge breaks or someone falls ill the day after spending every Rand on a car.",
        "Dedicated emergency buffers avoid high-interest crisis debt.",
        ["ems_raids_emergency_fund_for_wants"],
    )


def build_16_personal_budget_impact_on_net_worth(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    surplus = rng.randrange(1200, 3200, 200)
    prompt = (
        f"By sticking strictly to a monthly personal budget, {name} consistently saves {_fmt_r(surplus)} each month and avoids store-card debt. "
        f"Explain how disciplined budgeting improves {name}'s **Statement of Net Worth** over a full year."
    )
    mps = [
        f"Increases Assets: Monthly savings ({_fmt_r(surplus)} × 12 = {_fmt_r(surplus * 12)}) raise bank balances or investments.",
        "Reduces or avoids Liabilities: Spending within income limits stops credit-card and store-account debt from growing.",
        "Raises Net Worth: Since Net Worth = Total Assets - Total Liabilities, higher assets and lower debt expand long-term Net Worth.",
    ]
    sample = (
        f"Consistent budgeting generates {_fmt_r(surplus * 12)}/year in new savings (**Assets rise**) while preventing unnecessary credit debt (**Liabilities stay low**), "
        "directly raising Net Worth (Assets - Liabilities)."
    )
    return _make_typed(
        rng, "16_personal_budget_impact_on_net_worth", "How Budgeting Builds Net Worth", prompt,
        mps, ["assets", "liabilities", "net worth", "savings", "debt"], sample,
        "Connect monthly surplus/deficit directly to the Net Worth equation (Assets - Liabilities).",
        "Higher savings builds Assets; avoiding credit keeps Liabilities low.",
        ["ems_disconnects_budget_and_net_worth"],
    )


def build_17_months_required_to_reach_savings_goal_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    sav_mo = rng.randrange(800, 2400, 200)
    months = rng.choice([6, 8, 9, 10, 12])
    target = sav_mo * months
    prompt = (
        f"From a monthly personal budget, {name} reliably saves {_fmt_r(sav_mo)} every month toward a laptop and printer package costing {_fmt_r(target)}. "
        f"Assuming no interest, how many months will it take {name} to buy the equipment in cash (numbers only)?"
    )
    sol = f"Months Needed = Goal Amount / Monthly Budgeted Savings = {_fmt_r(target)} / {_fmt_r(sav_mo)} = **{months} months**"
    return _make_calc(
        rng, "17_months_required_to_reach_savings_goal_calc", "Months to Reach Savings Goal", prompt,
        months, "Months = Target Cost / Monthly Savings", sol,
        "Divide the total Rand target by the fixed monthly surplus saved.",
        f"{target} ÷ {sav_mo} = {months}.",
        ["ems_goal_timeline_division_error"], marks=3, unit="months",
    )


def build_18_annualising_monthly_budget_surplus_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    m_inc = rng.randrange(11000, 17000, 1000)
    m_exp = rng.randrange(8500, m_inc - 500, 500)
    m_surp = m_inc - m_exp
    yr_surp = m_surp * 12
    prompt = (
        f"{name} earns {_fmt_r(m_inc)} net per month and budgets monthly expenses of {_fmt_r(m_exp)}. "
        f"If {name} follows this exact budget for 12 months, calculate the total annual savings surplus (numbers only)."
    )
    sol = (
        f"Monthly Surplus = {_fmt_r(m_inc)} - {_fmt_r(m_exp)} = {_fmt_r(m_surp)}\n"
        f"Annual Surplus (12 months) = {_fmt_r(m_surp)} × 12 = **{_fmt_r(yr_surp)}**"
    )
    return _make_calc(
        rng, "18_annualising_monthly_budget_surplus_calc", "Annual Budget Surplus Projection", prompt,
        yr_surp, "Annual Surplus = (Monthly Income - Monthly Expenses) × 12", sol,
        "Find one month's surplus first, then multiply by 12 months.",
        f"Monthly = {m_surp}; 12 × {m_surp} = {yr_surp}.",
        ["ems_forgets_12_month_multiplier"], marks=3,
    )


def build_19_four_month_budget_cashflow_bars_visual(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    inc = rng.randrange(12000, 16000, 1000)
    e1 = inc - rng.randrange(1500, 2500, 500)
    e2 = inc - rng.randrange(1000, 2000, 500)
    e3 = inc + rng.randrange(1500, 3500, 500)
    e4 = inc - rng.randrange(1000, 2500, 500)
    net_mar = inc - e3
    svg = _svg_four_month_cashflow(name, inc, e1, e2, e3, e4)
    prompt = (
        f"Compare {name}'s 4-month budget summary where monthly Net Income stays fixed at {_fmt_r(inc)}, while expenses are "
        f"Jan {_fmt_r(e1)}, Feb {_fmt_r(e2)}, Mar {_fmt_r(e3)}, and Apr {_fmt_r(e4)}. "
        f"Calculate the March budget balance (Net Income minus March Expenses, keeping the negative sign; numbers only)."
    )
    sol = f"In March, red expenses ({_fmt_r(e3)}) exceed blue income ({_fmt_r(inc)}): {_fmt_r(inc)} - {_fmt_r(e3)} = **{_fmt_r(net_mar)}** (deficit)."
    return _make_calc(
        rng, "19_four_month_budget_cashflow_bars_visual", "4-Month Budget Deficit Visual", prompt,
        net_mar, "March Balance = Income - March Expenses", sol,
        "Notice which single month shows the red Expense bar rising higher than the blue Income bar.",
        f"{inc} - {e3} = {net_mar}.",
        ["ems_misreads_grouped_bar_deficit"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_20_monthly_sinking_fund_for_annual_expense_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    m_set = rng.randrange(250, 750, 50)
    annual = m_set * 12
    prompt = (
        f"{name} knows school uniforms and stationary at the start of next year will cost {_fmt_r(annual)}. "
        f"How much must {name} set aside every month over 12 months in the personal budget to pay this cash without borrowing (numbers only)?"
    )
    sol = f"Monthly Budget Provision = {_fmt_r(annual)} ÷ 12 months = **{_fmt_r(m_set)}**"
    return _make_calc(
        rng, "20_monthly_sinking_fund_for_annual_expense_calc", "Monthly Provision for Annual Cost", prompt,
        m_set, "Monthly Provision = Annual Cost ÷ 12", sol,
        "Spread the once-a-year expense evenly across 12 monthly budgets.",
        f"{annual} ÷ 12 = {m_set}.",
        ["ems_fails_to_smooth_irregular_expenses"], marks=3,
    )


def build_21_household_budget_reallocation_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    inc = rng.randrange(14000, 18000, 1000)
    rent = 5000
    groc = 3000
    tr = 1500
    old_want = inc - rent - groc - tr + 600  # deliberately creates -600 deficit
    cut = 900
    new_want = old_want - cut
    new_sav = inc - (rent + groc + tr + new_want)
    headers = ["Line Item", "Original Budget (R)", "Adjustment", "Revised Budget (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Net Monthly Income", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": str(inc), "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": "No change", "editable": False, "prefilled": True},
         {"cell_id": "r0_c3", "value": str(inc), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Essentials (Rent + Groceries + Transport)", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": str(rent + groc + tr), "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": "Protected", "editable": False, "prefilled": True},
         {"cell_id": "r1_c3", "value": str(rent + groc + tr), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Entertainment & Takeaways", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": str(old_want), "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": f"-{cut}", "editable": False, "prefilled": True},
         {"cell_id": "r2_c3", "value": "", "editable": True, "expected": str(new_want)}],
        [{"cell_id": "r3_c0", "value": "Revised Total Expenses", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": str(rent + groc + tr + old_want), "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": f"-{cut}", "editable": False, "prefilled": True},
         {"cell_id": "r3_c3", "value": "", "editable": True, "expected": str(rent + groc + tr + new_want)}],
        [{"cell_id": "r4_c0", "value": "Revised Monthly Balance", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "-600", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": "", "editable": True, "expected": "Surplus"},
         {"cell_id": "r4_c3", "value": "", "editable": True, "expected": str(new_sav)}],
    ]
    cmap = {
        "r2_c3": str(new_want),
        "r3_c3": str(rent + groc + tr + new_want),
        "r4_c2": "Surplus",
        "r4_c3": str(new_sav),
    }
    chints = {
        "r2_c3": f"Subtract {cut} from original Entertainment & Takeaways (digits only).",
        "r3_c3": "Add Revised Essentials + Revised Entertainment.",
        "r4_c2": "Enter 'Surplus' or 'Deficit'.",
        "r4_c3": "Subtract Revised Total Expenses from Net Monthly Income.",
    }
    md_memo = (
        f"| Line Item | Original | Adjustment | Revised |\n|---|---:|---|---:|\n"
        f"| Net Income | {inc} | No change | {inc} |\n"
        f"| Essentials | {rent + groc + tr} | Protected | {rent + groc + tr} |\n"
        f"| Entertainment & Takeaways | {old_want} | -{cut} | **{new_want}** |\n"
        f"| Revised Total Expenses | {rent + groc + tr + old_want} | -{cut} | **{rent + groc + tr + new_want}** |\n"
        f"| Revised Monthly Balance | -600 | **Surplus** | **{new_sav}** |"
    )
    prompt = f"Revise {name}'s household budget table below to turn a -R600 deficit into positive savings (plain integers without 'R')."
    return _make_ledger(
        rng, "21_household_budget_reallocation_table", "Revised Household Budget Table",
        prompt, headers, rows, cmap, chints, md_memo,
        "Apply the -900 adjustment to Entertainment & Takeaways first.",
        f"New wants = {new_want}; Revised expenses = {rent + groc + tr + new_want}; New surplus = {new_sav}.",
        ["ems_budget_reallocation_arithmetic_error"], marks=8,
    )


def build_22_credit_instalment_vs_cash_budget_affordability(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    cash_p = rng.randrange(4000, 7000, 500)
    inst = rng.randrange(350, 550, 50)
    months = 18
    tot_credit = inst * months
    extra = tot_credit - cash_p
    prompt = (
        f"{name} sees a fridge priced at {_fmt_r(cash_p)} cash OR {_fmt_r(inst)}/month over {months} months on credit ({_fmt_r(tot_credit)} total). "
        f"Calculate how much extra {name} pays in total credit costs/interest compared to saving and buying cash (numbers only)."
    )
    sol = (
        f"Total Credit Paid = {_fmt_r(inst)} × {months} = {_fmt_r(tot_credit)}\n"
        f"Extra Credit Cost = {_fmt_r(tot_credit)} - {_fmt_r(cash_p)} = **{_fmt_r(extra)}**"
    )
    return _make_calc(
        rng, "22_credit_instalment_vs_cash_budget_affordability", "Credit Instalment vs Cash Price Cost", prompt,
        extra, "Extra Cost = (Monthly Instalment × Months) - Cash Price", sol,
        "Multiply monthly instalment by 18 first, then subtract the cash price.",
        f"{tot_credit} - {cash_p} = {extra}.",
        ["ems_compares_monthly_instalment_to_cash_price"], marks=3,
    )


def build_23_utility_tariff_spike_budget_impact_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    old_elec = rng.randrange(600, 1200, 100)
    pct = rng.choice([15, 20, 25])
    increase = (old_elec * pct) // 100
    new_elec = old_elec + increase
    prompt = (
        f"{name} budgeted {_fmt_r(old_elec)}/month for electricity. Municipal tariffs increase by {pct}%. "
        f"Calculate the new updated monthly electricity figure {name} must enter into next month's budget (numbers only)."
    )
    sol = f"New Electricity Budget = {_fmt_r(old_elec)} + ({pct}% × {_fmt_r(old_elec)}) = {_fmt_r(old_elec)} + {_fmt_r(increase)} = **{_fmt_r(new_elec)}**"
    return _make_calc(
        rng, "23_utility_tariff_spike_budget_impact_calc", "Adjusting Budget for Tariff Increase", prompt,
        new_elec, "New Amount = Old Budget + (% Increase × Old Budget)", sol,
        "Calculate the percentage increase and add it onto the previous electricity budget.",
        f"{pct}% of {old_elec} = {increase}; new budget = {new_elec}.",
        ["ems_forgets_to_add_increase_to_base"], marks=3,
    )


def build_24_comparing_personal_vs_business_budget_scope(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} prepares both a **personal household budget** and an **operating budget for {sc['business_type']}**. "
        f"Identify two differences in structure, items, and purpose between a personal budget and a business operating budget."
    )
    mps = [
        "Personal budgets focus on household net salary/wages and living expenses (food, rent, utilities) to plan personal savings.",
        "Business budgets forecast trading Sales/Current Income, Cost of Sales, staff wages, marketing, and business tax to target Net Profit.",
        "Business budgets often include 3-column Actual vs Budget vs Variance monitoring to guide stock reinvestment and cost control.",
    ]
    sample = (
        "- **Income & Expense Items**: Personal budgets track net salary and family living costs; business budgets track Sales/Current Income, inventory stock, wages, and business overheads.\n"
        "- **Main Goal**: Personal budgets target household savings and avoiding consumer debt; business budgets track **Net Profit/Loss**, variance control, and growth reinvestment."
    )
    return _make_typed(
        rng, "24_comparing_personal_vs_business_budget_scope", "Personal vs Business Budget Comparison", prompt,
        mps, ["personal", "business", "profit", "savings", "variance"], sample,
        "Compare the typical revenue sources, expense items, and bottom-line objective of each budget.",
        "Household ends at Savings; Business ends at Net Profit/Loss (A - B).",
        ["ems_treats_business_and_personal_budgets_identically"],
    )


def build_25_impulse_spending_tracking_diary_strategy(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    days = rng.choice([7, 14, 30])
    prompt = (
        f"{name} finds that estimated groceries and entertainment in a personal budget never match actual bank balances after {days} days. "
        f"Which practical habit best improves budget accuracy?"
    )
    correct = "Record every actual cash and card outlay daily in a spending diary or app and adjust next month's budget lines realistically."
    distractors = [
        "Throw away till slips immediately so overspending causes less stress.",
        "Increase budgeted income artificially on paper without earning extra money.",
        "Cancel rent and municipal electricity payments to boost weekend entertainment.",
    ]
    sol = f"Keeping an actual spending diary over {days} days exposes where estimates fell short so {name} can revise future budgets accurately."
    return _make_mcq(
        rng, "25_impulse_spending_tracking_diary_strategy", "Tracking Actual Spending Against Budget", prompt,
        correct, distractors, sol,
        "How do you replace guesses with reliable personal expense numbers?",
        "Track real till slips/EFTs and update the budget.",
        ["ems_ignores_budget_monitoring"],
    )


BUILDERS_01_25 = {
    "01_budget_definition_future_earnings_expenses": build_01_budget_definition_future_earnings_expenses,
    "02_three_financial_choices_spend_save_borrow": build_02_three_financial_choices_spend_save_borrow,
    "03_budget_vs_historical_financial_records": build_03_budget_vs_historical_financial_records,
    "04_budget_tracking_affordability_awareness": build_04_budget_tracking_affordability_awareness,
    "05_new_business_three_budgeting_steps": build_05_new_business_three_budgeting_steps,
    "06_net_take_home_pay_after_salary_deductions": build_06_net_take_home_pay_after_salary_deductions,
    "07_personal_budget_total_income_and_expenses_calc": build_07_personal_budget_total_income_and_expenses_calc,
    "08_personal_budget_monthly_savings_surplus_calc": build_08_personal_budget_monthly_savings_surplus_calc,
    "09_personal_budget_deficit_identification_calc": build_09_personal_budget_deficit_identification_calc,
    "10_priya_style_personal_budget_table": build_10_priya_style_personal_budget_table,
    "11_personal_budget_allocation_bar_visual": build_11_personal_budget_allocation_bar_visual,
    "12_fixed_vs_variable_personal_expenses_classify": build_12_fixed_vs_variable_personal_expenses_classify,
    "13_personal_fixed_variable_budget_table": build_13_personal_fixed_variable_budget_table,
    "14_correcting_personal_budget_deficit_spending_cuts": build_14_correcting_personal_budget_deficit_spending_cuts,
    "15_emergency_savings_separate_from_goal_purchase": build_15_emergency_savings_separate_from_goal_purchase,
    "16_personal_budget_impact_on_net_worth": build_16_personal_budget_impact_on_net_worth,
    "17_months_required_to_reach_savings_goal_calc": build_17_months_required_to_reach_savings_goal_calc,
    "18_annualising_monthly_budget_surplus_calc": build_18_annualising_monthly_budget_surplus_calc,
    "19_four_month_budget_cashflow_bars_visual": build_19_four_month_budget_cashflow_bars_visual,
    "20_monthly_sinking_fund_for_annual_expense_calc": build_20_monthly_sinking_fund_for_annual_expense_calc,
    "21_household_budget_reallocation_table": build_21_household_budget_reallocation_table,
    "22_credit_instalment_vs_cash_budget_affordability": build_22_credit_instalment_vs_cash_budget_affordability,
    "23_utility_tariff_spike_budget_impact_calc": build_23_utility_tariff_spike_budget_impact_calc,
    "24_comparing_personal_vs_business_budget_scope": build_24_comparing_personal_vs_business_budget_scope,
    "25_impulse_spending_tracking_diary_strategy": build_25_impulse_spending_tracking_diary_strategy,
}
