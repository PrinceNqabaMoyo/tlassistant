"""Grade 7 Economic and Management Sciences - Term 2: Income and Expenses (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/EMS_Gr7/Term 2/02. Income and Expenses.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, get_ems_scenario


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
        "id": f"g7_ems_ie_{subskill[:2]}_{rng.randint(100000, 999999)}",
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
        "caps_weight_percent": 30,
        "suggested_duration_mins": max(2, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": f"Select: {correct}"},
        "marking_points": [correct],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}],
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_income_and_expenses",
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
        "id": f"g7_ems_ie_{subskill[:2]}_{rng.randint(100000, 999999)}",
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
        "caps_weight_percent": 30,
        "suggested_duration_mins": max(2, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": f"Expected answer: {disp}"},
        "marking_points": [disp],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_formula", "desc": f"Correct formula ({formula})", "marks": 1, "editable": True},
                {"id": "mp_final", "desc": f"Accurate calculated result: {disp}", "marks": max(1, marks - 1), "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_income_and_expenses",
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
        "id": f"g7_ems_ie_{subskill[:2]}_{rng.randint(100000, 999999)}",
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
        "caps_weight_percent": 30,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": sample_answer},
        "guidelines": [f"Cover {len(marking_points)} core marking points clearly."],
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
        "subtopic_id": "term2_income_and_expenses",
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
        "id": f"g7_ems_ie_{subskill[:2]}_{rng.randint(100000, 999999)}",
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
        "caps_weight_percent": 30,
        "suggested_duration_mins": max(4, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": "Complete each highlighted cell following the exact format shown."},
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
        "subtopic_id": "term2_income_and_expenses",
    }


def _svg_net_worth_stack(person: str, assets: int, liab: int) -> str:
    """Seed-varied stacked bar chart comparing Assets vs Liabilities + Net Worth."""
    nw = assets - liab
    max_v = max(assets, liab, 1)
    h_a = 136
    h_l = max(18, int(round((liab / max_v) * 136)))
    y_a = 178 - h_a
    y_l = 178 - h_l
    h_nw = max(16, h_a - h_l) if nw >= 0 else max(18, int(round((abs(nw) / max_v) * 136)))
    y_nw = y_a if nw >= 0 else y_l
    nw_label = f"Net Worth: {_fmt_r(nw)}" if nw >= 0 else f"Deficit: {_fmt_r(nw)}"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 230" width="540" height="230">'
        '<rect width="540" height="230" fill="#f8fafc" rx="8"/>'
        f'<text x="270" y="24" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0f172a">{person}: Statement of Net Worth Visual</text>'
        '<line x1="60" y1="178" x2="480" y2="178" stroke="#64748b" stroke-width="2"/>'
        f'<rect x="105" y="{y_a}" width="110" height="{h_a}" fill="#0284c7" rx="4"/>'
        f'<text x="160" y="{y_a + h_a // 2}" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#ffffff">{_fmt_r(assets)}</text>'
        '<text x="160" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Total Assets</text>'
        f'<rect x="305" y="{y_l}" width="110" height="{h_l}" fill="#e11d48" rx="4"/>'
        f'<text x="360" y="{y_l + h_l // 2 + 4}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#ffffff">{_fmt_r(liab)}</text>'
        f'<rect x="305" y="{y_nw}" width="110" height="{h_nw}" fill="#16a34a" rx="4" opacity="0.88"/>'
        f'<text x="360" y="{y_nw - 8}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#166534">Net Worth = ?</text>'
        '<text x="360" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Liabilities + Net Worth</text>'
        f'<text x="270" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#475569">Check: {nw_label.split(":")[0]} = Total Assets - Total Liabilities</text>'
        "</svg>"
    )


def _svg_liquidity_spectrum(person: str, a_cash: int, a_ut: int, a_house: int) -> str:
    """Seed-varied liquidity continuum from instant cash to illiquid property."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 190" width="560" height="190">'
        '<rect width="560" height="190" fill="#f8fafc" rx="8"/>'
        f'<text x="280" y="24" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{person}: Asset Liquidity Conversion Spectrum</text>'
        '<line x1="45" y1="88" x2="515" y2="88" stroke="#0284c7" stroke-width="4"/>'
        '<polygon points="515,82 528,88 515,94" fill="#0284c7"/>'
        '<text x="45" y="64" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#15803d">Fastest to Cash (Hours)</text>'
        '<text x="515" y="64" text-anchor="end" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#b91c1c">Slowest to Cash (Months)</text>'
        f'<rect x="38" y="106" width="135" height="54" fill="#dcfce7" stroke="#16a34a" rx="6"/>'
        f'<text x="105" y="127" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#14532d">Bank Savings</text>'
        f'<text x="105" y="147" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#166534">{_fmt_r(a_cash)}</text>'
        f'<rect x="212" y="106" width="135" height="54" fill="#e0f2fe" stroke="#0284c7" rx="6"/>'
        f'<text x="280" y="127" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#0c4a6e">Unit Trust / Policy</text>'
        f'<text x="280" y="147" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#0369a1">{_fmt_r(a_ut)}</text>'
        f'<rect x="386" y="106" width="135" height="54" fill="#fee2e2" stroke="#dc2626" rx="6"/>'
        f'<text x="453" y="127" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#7f1d1d">Residential House</text>'
        f'<text x="453" y="147" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#991b1b">{_fmt_r(a_house)}</text>'
        "</svg>"
    )


def build_01_personal_income_definition_wealth(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    sal = rng.randrange(9500, 18500, 500)
    int_inc = rng.randrange(250, 950, 50)
    house_val = rng.randrange(450000, 850000, 50000)
    prompt = (
        f"{name} lives in {area}, earns a monthly salary of {_fmt_r(sal)}, receives {_fmt_r(int_inc)} in bank interest, "
        f"and inherited a house valued at {_fmt_r(house_val)}. What is the correct EMS definition of {name}'s personal income?"
    )
    correct = "Total money earned or received by an individual from all sources such as work, capital interest, and rental."
    distractors = [
        "Only the total market value of houses, cars, and jewellery owned at year-end.",
        "Total unpaid household store accounts and bank mortgage bonds still owed.",
        "Only physical banknotes kept inside a wallet before paying living expenses.",
    ]
    sol = f"Personal income is the total inflow of earnings from all sources ({_fmt_r(sal)} salary + {_fmt_r(int_inc)} interest). The {_fmt_r(house_val)} house is wealth (an asset), not monthly income."
    return _make_mcq(
        rng, "01_personal_income_definition_wealth", "Personal Income Definition", prompt,
        correct, distractors, sol,
        "Distinguish money flowing in (income) from things you already own (wealth/assets).",
        "Include salary, wages, interest, rent, and dividends — not property value itself.",
        ["ems_confuses_income_and_wealth"],
    )


def build_02_three_personal_income_sources_classification(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    cases = [
        ("earns monthly interest on a fixed deposit and dividends on shares", "Capital (investments and savings)", "Work (labour/salary)"),
        ("leases out an extra garden cottage for monthly rent", "Land and property", "Capital (bank interest)"),
        ("works 40 hours a week as a clinic receptionist for a wage", "Work (selling labour or skill)", "Land and property"),
    ]
    desc, correct, alt = rng.choice(cases)
    amt = rng.randrange(1800, 7500, 200)
    prompt = (
        f"Personal income comes from three main sources: work, capital, or land. "
        f"If {name} {desc} generating {_fmt_r(amt)} per month, which source of personal income is this?"
    )
    all_opts = ["Work (selling labour or skill)", "Capital (investments and savings)", "Land and property", "Long-term debt financing"]
    distractors = [o for o in all_opts if o != correct][:3]
    sol = f"Receiving {_fmt_r(amt)} when {name} {desc} classifies under **{correct}** among the three personal income sources."
    return _make_mcq(
        rng, "02_three_personal_income_sources_classification", "Three Sources of Personal Income", prompt,
        correct, distractors, sol,
        "Ask whether the cash comes from human effort (Work), invested money (Capital), or physical land/buildings (Land).",
        "Wages/salaries/commission = Work; interest/dividends = Capital; rental = Land.",
        ["ems_income_source_misclassification"],
    )


def build_03_salary_wage_commission_comparison(rng: random.Random) -> Dict[str, Any]:
    n1, n2, n3 = rng.sample(NAMES, 3)
    sal = rng.randrange(14000, 22000, 1000)
    hr_rate = rng.randrange(65, 110, 5)
    comm_pct = rng.choice([6, 8, 10])
    prompt = (
        f"Compare three work-based remuneration methods in {rng.choice(AREAS)}: {n1} receives a fixed salary of {_fmt_r(sal)}/month, "
        f"{n2} earns a wage of {_fmt_r(hr_rate)}/hour, and {n3} earns {comm_pct}% commission on appliance sales. "
        f"Explain clearly how a salary, a wage, and commission differ."
    )
    mps = [
        "Salary is a fixed regular monthly sum paid regardless of exact daily hours worked.",
        "Wage is calculated directly per hour worked or unit produced and often paid weekly or fortnightly.",
        "Commission is a percentage reward tied directly to total sales value achieved.",
        "Uses the given scenario contexts accurately to distinguish predictable vs performance-based earnings.",
    ]
    sample = (
        f"1. **Salary**: {n1} receives a fixed regular amount ({_fmt_r(sal)} monthly) usually paid to permanent staff.\n"
        f"2. **Wage**: {n2} is paid per hour worked ({_fmt_r(hr_rate)}/hr), often weekly, so earnings fluctuate with hours.\n"
        f"3. **Commission**: {n3} earns {comm_pct}% of sales made, rewarding higher sales performance."
    )
    return _make_typed(
        rng, "03_salary_wage_commission_comparison", "Salary vs Wage vs Commission", prompt,
        mps, ["salary", "wage", "commission", "fixed", "hourly", "sales percentage"], sample,
        "Focus on the calculation basis: fixed month vs hours worked vs sales percentage.",
        "Include payment predictability and frequency for full marks.",
        ["ems_salary_vs_wage_confusion"],
    )


def build_04_gross_wage_commission_income_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    retainer = rng.randrange(3000, 6500, 500)
    sales_val = rng.randrange(25000, 55000, 5000)
    rate = rng.choice([4, 5, 6, 8])
    comm = (sales_val * rate) // 100
    total = retainer + comm
    prompt = (
        f"{name} works at a sports shop earning a basic monthly retainer of {_fmt_r(retainer)} plus {rate}% commission on all sales. "
        f"During May, {name} sells goods worth {_fmt_r(sales_val)}. Calculate {name}'s total personal income for May (enter numbers only)."
    )
    sol = (
        f"Commission = {rate}% × {_fmt_r(sales_val)} = {_fmt_r(comm)}\n"
        f"Total Personal Income = {_fmt_r(retainer)} + {_fmt_r(comm)} = **{_fmt_r(total)}**"
    )
    return _make_calc(
        rng, "04_gross_wage_commission_income_calc", "Basic Pay + Commission Calculation", prompt,
        total, "Total Income = Retainer + (Commission Rate × Sales)", sol,
        f"First compute {rate}% of {_fmt_r(sales_val)}, then add the {_fmt_r(retainer)} retainer.",
        f"{sales_val} × {rate}/100 = {comm}; add {retainer}.",
        ["ems_commission_calculation_error"],
    )


def build_05_personal_expenses_definition_examples(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    w = rng.randrange(350, 750, 50)
    f = rng.randrange(1800, 3200, 100)
    a = rng.randrange(150, 350, 50)
    prompt = (
        f"{name} pays {_fmt_r(w)} for municipal water and electricity, {_fmt_r(f)} for groceries, and {_fmt_r(a)} for airtime each month. "
        f"Why are these classified as personal expenses rather than assets?"
    )
    correct = "They are day-to-day living costs consumed without leaving behind an item of lasting monetary value."
    distractors = [
        "They increase personal net worth by creating long-term tangible investments.",
        "They are repayments of shareholder dividends owed to municipal workers.",
        "They represent cash still owed to a bank over more than one year.",
    ]
    sol = f"Payments for water/electricity ({_fmt_r(w)}), food ({_fmt_r(f)}), and airtime ({_fmt_r(a)}) are consumed for living and decrease cash without creating a resaleable asset."
    return _make_mcq(
        rng, "05_personal_expenses_definition_examples", "Personal Expenses Definition", prompt,
        correct, distractors, sol,
        "Ask whether anything with lasting resale value remains once groceries or electricity are used.",
        "Personal expenses cover daily living needs and reduce wealth rather than building assets.",
        ["ems_expense_vs_asset_confusion"],
    )


def build_06_personal_vs_business_expense_distinction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    b_amt = rng.randrange(1200, 3600, 200)
    p_amt = rng.randrange(900, 2400, 100)
    prompt = (
        f"{sc['entrepreneur']} owns {sc['business_type']} in {sc['area']}. In June, {sc['entrepreneur']} paid {_fmt_r(b_amt)} for shop packaging bags "
        f"and {_fmt_r(p_amt)} for family groceries at home. Explain why these two expenses must be recorded separately."
    )
    mps = [
        f"The {_fmt_r(b_amt)} packaging cost is a business expense incurred to operate {sc['business_type']}.",
        f"The {_fmt_r(p_amt)} family groceries cost is a personal household expense unrelated to earning business income.",
        "Mixing personal and business expenses distorts true business profit and makes budgeting inaccurate.",
        "Under the business entity principle, owner household spending must be kept separate from business records.",
    ]
    sample = (
        f"- **Business Expense ({_fmt_r(b_amt)})**: Packaging is required directly to run {sc['business_type']}.\n"
        f"- **Personal Expense ({_fmt_r(p_amt)})**: Family groceries are private household consumption.\n"
        "- **Why separate**: Keeping them separate reveals whether the business is genuinely profitable and prevents draining business cash."
    )
    return _make_typed(
        rng, "06_personal_vs_business_expense_distinction", "Separating Personal & Business Expenses", prompt,
        mps, ["business expense", "personal expense", "profit", "separate", "entity"], sample,
        "Identify which outflow keeps the business running vs feeds the owner's household.",
        "Explain how mixing the two hides real business profit.",
        ["ems_business_personal_mixing"],
    )


def build_07_ethics_financial_worth_vs_human_worth(rng: random.Random) -> Dict[str, Any]:
    n1, n2 = rng.sample(NAMES, 2)
    nw1 = rng.randrange(450000, 950000, 50000)
    nw2 = rng.randrange(-45000, -10000, 5000)
    prompt = (
        f"A Statement of Net Worth shows {n1} has a Net Worth of {_fmt_r(nw1)}, while {n2} (a newly qualified community nurse with student debt) "
        f"has a Net Worth of {_fmt_r(nw2)}. Using EMS principles on personal worth vs financial net worth, evaluate whether {n1} is a better or more valuable human being than {n2}."
    )
    mps = [
        f"No — Net Worth ({_fmt_r(nw1)} vs {_fmt_r(nw2)}) only measures financial wealth (Assets minus Liabilities) at one moment.",
        "A person's human value, character, compassion, ethics, and community contribution cannot be measured in Rands.",
        "Negative net worth often reflects temporary early-career debt such as student loans rather than personal failure.",
        "Concluding superiority from monetary wealth confuses accounting balance sheets with human dignity.",
    ]
    sample = (
        f"**No.** Financial net worth ({_fmt_r(nw1)} vs {_fmt_r(nw2)}) strictly measures monetary Assets minus Liabilities on a given date. "
        "It does **not** measure a person's kindness, work ethic, dignity, or value to society."
    )
    return _make_typed(
        rng, "07_ethics_financial_worth_vs_human_worth", "Financial Net Worth vs Human Value", prompt,
        mps, ["net worth", "financial", "human worth", "dignity", "not equal"], sample,
        "Separate an accounting measurement (Rands) from moral and human value.",
        "Note why someone starting out in a caring profession may temporarily carry debt.",
        ["ems_equates_wealth_with_human_worth"],
    )


def build_08_statement_of_net_worth_balance_sheet_alias(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    day = rng.choice(["28 February 2025", "30 June 2025", "31 December 2025"])
    prompt = (
        f"{name} draws up a Statement of Net Worth on {day}. Why is a Statement of Net Worth also called a Personal Balance Sheet?"
    )
    correct = "Because it shows a snapshot of a person's assets, liabilities, and resulting net worth at one specific point in time."
    distractors = [
        "Because it tracks weekly grocery prices over an entire five-year period.",
        "Because it only records cash deposited into a bank cheque account without debts.",
        "Because banks require all employees to publish their salaries in newspapers.",
    ]
    sol = f"Just like a business balance sheet, a Statement of Net Worth summarizes **Assets = Liabilities + Net Worth** (or Assets - Liabilities = Net Worth) at one date ({day})."
    return _make_mcq(
        rng, "08_statement_of_net_worth_balance_sheet_alias", "Statement of Net Worth / Balance Sheet", prompt,
        correct, distractors, sol,
        "Think about the two sides that balance at a point in time: what you own vs what you owe.",
        "It gives a snapshot on a specific date, not cash flows across a whole year.",
        ["ems_statement_period_confusion"],
    )


def build_09_current_assets_short_term_liquidity(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    amt = rng.randrange(4000, 18000, 500)
    opts_pool = [
        (f"Cash in a bank savings account ({_fmt_r(amt)})", "A residential house owned in town"),
        (f"A short-term fixed deposit maturing in 3 months ({_fmt_r(amt)})", "Bedroom furniture and a dining table"),
        (f"Cash on hand plus a loan owed back to {name} ({_fmt_r(amt)})", "Gold jewellery and oil paintings"),
    ]
    correct, non_curr = rng.choice(opts_pool)
    prompt = (
        f"Current (liquid) assets can be converted into cash quickly without losing significant value. "
        f"Which item belonging to {name} is a **Current Asset**?"
    )
    distractors = [
        non_curr,
        f"An unpaid clothing store credit bill of {_fmt_r(amt)}",
        "A 20-year mortgage bond owed to a commercial bank",
    ]
    sol = f"**{correct}** is a current/liquid asset because it is cash or easily turned into cash within a short period."
    return _make_mcq(
        rng, "09_current_assets_short_term_liquidity", "Current / Liquid Assets", prompt,
        correct, distractors, sol,
        "Current assets are cash or financial claims easily converted to cash; liabilities are debts.",
        "Houses, furniture, and jewellery are tangible non-current assets, not current assets.",
        ["ems_current_vs_noncurrent_asset"],
    )


def build_10_non_current_assets_tangible_long_term(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    val = rng.randrange(12000, 85000, 1000)
    items = [
        f"A family delivery car valued at {_fmt_r(val)}",
        f"Solid oak household furniture worth {_fmt_r(val)}",
        f"Gold jewellery and camera equipment worth {_fmt_r(val)}",
    ]
    correct = rng.choice(items)
    prompt = (
        f"Non-current (fixed/tangible) assets are long-term physical items kept for ongoing use rather than instant cash conversion. "
        f"Which item owned by {name} is a **Non-current Asset**?"
    )
    distractors = [
        f"Cash withdrawn at an ATM ({_fmt_r(val // 10)})",
        f"An overdue municipal electricity bill of {_fmt_r(val // 12)}",
        f"Money held in an everyday cheque account ({_fmt_r(val // 5)})",
    ]
    sol = f"**{correct}** is a tangible non-current asset kept for long-term use."
    return _make_mcq(
        rng, "10_non_current_assets_tangible_long_term", "Non-Current (Tangible) Assets", prompt,
        correct, distractors, sol,
        "Look for long-lasting physical possessions you use, not cash or unpaid bills.",
        "Vehicles, property, furniture, electronics, and jewellery are non-current assets.",
        ["ems_noncurrent_asset_error"],
    )


def build_11_personal_assets_liabilities_classification_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    a1 = rng.randrange(450000, 750000, 25000)
    a2 = rng.randrange(4500, 14500, 500)
    l1 = rng.randrange(1500, 6500, 500)
    l2 = rng.randrange(180000, 320000, 10000)
    headers = ["Personal Item", "Amount (R)", "Asset or Liability", "Current or Non-current"]
    items = [
        ("Township home owned", a1, "Asset", "Non-current"),
        ("Bank savings balance", a2, "Asset", "Current"),
        ("Clothing store account owing", l1, "Liability", "Current"),
        ("20-year mortgage bond owing", l2, "Liability", "Non-current"),
    ]
    rows: List[List[Dict[str, Any]]] = []
    cmap: Dict[str, str] = {}
    chints: Dict[str, str] = {}
    md_lines = [f"| {' | '.join(headers)} |", "|---|---:|---|---|"]
    for r_i, (desc, amt, kind, term_t) in enumerate(items):
        cid_k = f"r{r_i}_c2"
        cid_t = f"r{r_i}_c3"
        cmap[cid_k] = kind
        cmap[cid_t] = term_t
        chints[cid_k] = "Enter 'Asset' (owned) or 'Liability' (owed)."
        chints[cid_t] = "Enter 'Current' (< 1 year/liquid) or 'Non-current' (long-term)."
        rows.append([
            {"cell_id": f"r{r_i}_c0", "value": desc, "editable": False, "prefilled": True},
            {"cell_id": f"r{r_i}_c1", "value": _fmt_r(amt), "editable": False, "prefilled": True},
            {"cell_id": cid_k, "value": "", "editable": True, "expected": kind},
            {"cell_id": cid_t, "value": "", "editable": True, "expected": term_t},
        ])
        md_lines.append(f"| {desc} | {_fmt_r(amt)} | {kind} | {term_t} |")
    prompt = (
        f"Complete the personal classification schedule below for {name}. For each item, fill in exact values: "
        f"**Asset** or **Liability** in column 3, and **Current** or **Non-current** in column 4."
    )
    return _make_ledger(
        rng, "11_personal_assets_liabilities_classification_table", "Assets & Liabilities Classification Schedule",
        prompt, headers, rows, cmap, chints, "\n".join(md_lines),
        "Assets = things owned; Liabilities = debts owed to others.",
        "Current = cash/liquid assets or debts due within 1 year; Non-current = houses or multi-year bonds.",
        ["ems_classification_table_error"], marks=8,
    )


def build_12_current_vs_long_term_liabilities_split(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    amt = rng.randrange(25000, 95000, 5000)
    q_current = rng.choice([True, False])
    if q_current:
        prompt = f"{name} owes several debts. Which of the following is a **Current Liability** (due within 12 months)?"
        correct = f"A credit card bill of {_fmt_r(amt // 10)} due at the end of this month"
        distractors = [
            f"A 20-year home mortgage bond of {_fmt_r(amt * 5)}",
            f"A 5-year vehicle instalment loan of {_fmt_r(amt)}",
            f"Personal cash saved in a wallet ({_fmt_r(amt // 20)})",
        ]
        sol = f"**{correct}** must be settled within one year, making it a current (short-term) liability."
    else:
        prompt = f"{name} reviews household debts. Which item is a **Long-term Liability** (settled over more than 1 year)?"
        correct = f"A 48-month car finance loan with {_fmt_r(amt)} still owing"
        distractors = [
            f"This month's unpaid water account of {_fmt_r(amt // 25)}",
            f"A 30-day pharmacy store account of {_fmt_r(amt // 30)}",
            f"A bank savings account balance of {_fmt_r(amt // 5)}",
        ]
        sol = f"**{correct}** is repaid over multiple years (> 12 months), making it a long-term liability."
    return _make_mcq(
        rng, "12_current_vs_long_term_liabilities_split", "Current vs Long-Term Liabilities", prompt,
        correct, distractors, sol,
        "Use the 12-month timeframe rule: within 1 year = Current; more than 1 year = Long-term.",
        "Do not confuse bank savings (an asset) with debt (a liability).",
        ["ems_liability_timeframe_error"],
    )


def build_13_net_worth_equation_surplus_deficit_concept(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    liab = rng.randrange(120000, 260000, 10000)
    assets = liab - rng.randrange(20000, 60000, 5000)
    nw = assets - liab
    prompt = (
        f"Using the fundamental Net Worth equation, {name} finds Total Assets = {_fmt_r(assets)} and Total Liabilities = {_fmt_r(liab)} "
        f"(giving {_fmt_r(nw)}). Which statement is correct?"
    )
    correct = f"Net Worth = Total Assets - Total Liabilities, and {name} currently has a net worth deficit because debts exceed assets."
    distractors = [
        f"Net Worth = Total Assets + Total Liabilities, and {name} currently has a financial surplus.",
        f"Net Worth = Total Liabilities - Total Assets, meaning {name} holds extra spare cash.",
        f"Net Worth ignores liabilities whenever assets exceed {_fmt_r(assets // 2)}.",
    ]
    sol = f"Formula: Net Worth = Assets ({_fmt_r(assets)}) - Liabilities ({_fmt_r(liab)}) = **{_fmt_r(nw)}** (< R0 = deficit)."
    return _make_mcq(
        rng, "13_net_worth_equation_surplus_deficit_concept", "Net Worth Equation & Deficit Concept", prompt,
        correct, distractors, sol,
        "Net Worth subtracts what you owe from what you own.",
        "When Liabilities > Assets, Assets - Liabilities is negative (a deficit).",
        ["ems_adds_assets_and_liabilities"],
    )


def build_14_remaining_loan_balance_from_paid_portion(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    flat_val = rng.randrange(500000, 900000, 50000)
    flat_paid = flat_val - rng.randrange(150000, 300000, 20000)
    car_val = rng.randrange(70000, 130000, 10000)
    car_owed = rng.randrange(15000, 40000, 5000)
    bank = rng.randrange(15000, 55000, 5000)
    flat_owed = flat_val - flat_paid
    tot_a = flat_val + car_val + bank
    tot_l = flat_owed + car_owed
    nw = tot_a - tot_l
    prompt = (
        f"{name} owns a flat worth {_fmt_r(flat_val)} of which {_fmt_r(flat_paid)} has already been paid off, a car worth {_fmt_r(car_val)} "
        f"with {_fmt_r(car_owed)} still owed, and {_fmt_r(bank)} in the bank. Calculate {name}'s **Net Worth** (numbers only)."
    )
    sol = (
        f"1. Bond still owing on flat = {_fmt_r(flat_val)} - {_fmt_r(flat_paid)} = {_fmt_r(flat_owed)}\n"
        f"2. Total Assets = {_fmt_r(flat_val)} + {_fmt_r(car_val)} + {_fmt_r(bank)} = {_fmt_r(tot_a)}\n"
        f"3. Total Liabilities = {_fmt_r(flat_owed)} + {_fmt_r(car_owed)} = {_fmt_r(tot_l)}\n"
        f"4. Net Worth = {_fmt_r(tot_a)} - {_fmt_r(tot_l)} = **{_fmt_r(nw)}**"
    )
    return _make_calc(
        rng, "14_remaining_loan_balance_from_paid_portion", "Bond Paid vs Remaining Net Worth", prompt,
        nw, "Net Worth = Total Assets - (Bond Owing + Car Loan)", sol,
        "Watch carefully: amount 'paid off' is NOT the liability — subtract paid off from property value first!",
        f"Flat owing = {flat_val - flat_paid}; Total Assets = {tot_a}; Total Liabilities = {tot_l}.",
        ["ems_uses_paid_amount_as_liability"], marks=5,
    )


def build_15_net_worth_surplus_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    house = rng.randrange(650000, 1400000, 50000)
    veh = rng.randrange(120000, 260000, 10000)
    furn = rng.randrange(60000, 140000, 10000)
    sav = rng.randrange(20000, 80000, 5000)
    bond = rng.randrange(250000, 500000, 25000)
    card = rng.randrange(4000, 18000, 1000)
    tot_a = house + veh + furn + sav
    tot_l = bond + card
    nw = tot_a - tot_l
    prompt = (
        f"{name} lists assets: House {_fmt_r(house)}, Vehicles {_fmt_r(veh)}, Furniture {_fmt_r(furn)}, Savings {_fmt_r(sav)}; "
        f"and liabilities: Mortgage bond {_fmt_r(bond)}, Credit card {_fmt_r(card)}. "
        f"Calculate {name}'s positive Net Worth (numbers only)."
    )
    sol = (
        f"Total Assets = {_fmt_r(house)} + {_fmt_r(veh)} + {_fmt_r(furn)} + {_fmt_r(sav)} = {_fmt_r(tot_a)}\n"
        f"Total Liabilities = {_fmt_r(bond)} + {_fmt_r(card)} = {_fmt_r(tot_l)}\n"
        f"Net Worth = {_fmt_r(tot_a)} - {_fmt_r(tot_l)} = **{_fmt_r(nw)}**"
    )
    return _make_calc(
        rng, "15_net_worth_surplus_calculation", "Net Worth Surplus Calculation", prompt,
        nw, "Net Worth = Total Assets - Total Liabilities", sol,
        "Sum all 4 assets first, then sum the 2 liabilities.",
        f"{tot_a} - {tot_l} = {nw}.",
        ["ems_net_worth_arithmetic_error"], marks=4,
    )


def build_16_net_worth_deficit_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    house = rng.randrange(400000, 650000, 25000)
    furn = rng.randrange(30000, 80000, 5000)
    bond = house + rng.randrange(40000, 110000, 10000)
    loan = rng.randrange(45000, 95000, 5000)
    tot_a = house + furn
    tot_l = bond + loan
    nw = tot_a - tot_l
    prompt = (
        f"{name}'s assets are a small house ({_fmt_r(house)}) and furniture ({_fmt_r(furn)}), while liabilities total "
        f"mortgage bond ({_fmt_r(bond)}) and personal loan ({_fmt_r(loan)}). Calculate {name}'s Net Worth, including the minus sign if negative (numbers only)."
    )
    sol = (
        f"Total Assets = {_fmt_r(house)} + {_fmt_r(furn)} = {_fmt_r(tot_a)}\n"
        f"Total Liabilities = {_fmt_r(bond)} + {_fmt_r(loan)} = {_fmt_r(tot_l)}\n"
        f"Net Worth = {_fmt_r(tot_a)} - {_fmt_r(tot_l)} = **{_fmt_r(nw)}** (Deficit)"
    )
    return _make_calc(
        rng, "16_net_worth_deficit_calculation", "Net Worth Deficit Calculation", prompt,
        nw, "Net Worth = Total Assets - Total Liabilities", sol,
        "Subtract Total Liabilities from Total Assets even when Liabilities are larger.",
        f"{tot_a} - {tot_l} = {nw} (negative net worth).",
        ["ems_drops_negative_sign_net_worth"], marks=4,
    )


def build_17_asset_liability_net_worth_stacked_bar_visual(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    assets = rng.randrange(380000, 760000, 20000)
    liab = rng.randrange(120000, 280000, 15000)
    nw = assets - liab
    svg = _svg_net_worth_stack(name, assets, liab)
    prompt = (
        f"Refer to {name}'s stacked bar balance summary: Total Assets are {_fmt_r(assets)} and Total Liabilities are {_fmt_r(liab)}. "
        f"Calculate the missing green Net Worth block needed to balance Total Assets (numbers only)."
    )
    sol = f"Missing Net Worth block = Total Assets ({_fmt_r(assets)}) - Total Liabilities ({_fmt_r(liab)}) = **{_fmt_r(nw)}**."
    return _make_calc(
        rng, "17_asset_liability_net_worth_stacked_bar_visual", "Net Worth Stacked Bar Balance", prompt,
        nw, "Net Worth = Total Assets - Total Liabilities", sol,
        "Notice both tall bars reach the exact same Total Assets height.",
        f"Subtract the red Liabilities bar ({_fmt_r(liab)}) from Total Assets ({_fmt_r(assets)}).",
        ["ems_balance_bar_reading_error"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_18_missing_asset_or_liability_reverse_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    known_a = rng.randrange(220000, 420000, 20000)
    sav = rng.randrange(18000, 65000, 2000)
    tot_l = rng.randrange(90000, 175000, 5000)
    nw = (known_a + sav) - tot_l
    prompt = (
        f"{name}'s confirmed Net Worth is {_fmt_r(nw)} and Total Liabilities are {_fmt_r(tot_l)}. Listed physical assets equal {_fmt_r(known_a)}, "
        f"excluding one undisclosed bank savings account. Find the balance in that bank savings account (numbers only)."
    )
    sol = (
        f"Total Assets = Net Worth + Total Liabilities = {_fmt_r(nw)} + {_fmt_r(tot_l)} = {_fmt_r(known_a + sav)}\n"
        f"Bank Savings = {_fmt_r(known_a + sav)} - {_fmt_r(known_a)} = **{_fmt_r(sav)}**"
    )
    return _make_calc(
        rng, "18_missing_asset_or_liability_reverse_calc", "Reverse Missing Asset Calculation", prompt,
        sav, "Missing Asset = (Net Worth + Liabilities) - Known Assets", sol,
        "Rearrange Net Worth = Assets - Liabilities to get Total Assets = Net Worth + Liabilities first.",
        f"{nw} + {tot_l} - {known_a} = {sav}.",
        ["ems_reverse_net_worth_error"], marks=4,
    )


def build_19_household_room_inventory_statement_net_worth_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    bed = rng.randrange(2500, 4500, 500)
    desk = rng.randrange(1200, 2800, 200)
    phone = rng.randrange(2400, 4800, 300)
    tot_a = bed + desk + phone
    owe_parent = rng.randrange(600, 1500, 100)
    nw = tot_a - owe_parent
    headers = ["Personal Inventory / Debt Item", "Classification", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Bed and mattress", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Asset", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(bed), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Study desk and chair", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Asset", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(desk), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Smartphone", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Asset", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(phone), "editable": False, "prefilled": True}],
        [{"cell_id": "r3_c0", "value": "Total Assets", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Subtotal", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": "", "editable": True, "expected": str(tot_a)}],
        [{"cell_id": "r4_c0", "value": "Amount owed to sister", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "", "editable": True, "expected": "Liability"},
         {"cell_id": "r4_c2", "value": str(owe_parent), "editable": False, "prefilled": True}],
        [{"cell_id": "r5_c0", "value": "Personal Net Worth", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Surplus", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": "", "editable": True, "expected": str(nw)}],
    ]
    cmap = {"r3_c2": str(tot_a), "r4_c1": "Liability", "r5_c2": str(nw)}
    chints = {
        "r3_c2": "Add bed + desk + smartphone values (digits only).",
        "r4_c1": "Enter 'Liability'.",
        "r5_c2": "Subtract Total Liabilities from Total Assets (digits only).",
    }
    md_memo = (
        f"| Personal Inventory / Debt Item | Classification | Amount (R) |\n|---|---|---:|\n"
        f"| Bed and mattress | Asset | {bed} |\n| Study desk and chair | Asset | {desk} |\n"
        f"| Smartphone | Asset | {phone} |\n| **Total Assets** | Subtotal | **{tot_a}** |\n"
        f"| Amount owed to sister | Liability | {owe_parent} |\n| **Personal Net Worth** | Surplus | **{nw}** |"
    )
    prompt = f"Complete {name}'s bedroom inventory Statement of Net Worth below (enter numeric totals without 'R' or spaces)."
    return _make_ledger(
        rng, "19_household_room_inventory_statement_net_worth_table", "Room Inventory Net Worth Schedule",
        prompt, headers, rows, cmap, chints, md_memo,
        "Sum all three room assets before subtracting the personal debt.",
        f"Total Assets = {bed} + {desk} + {phone}; Net Worth = Total Assets - {owe_parent}.",
        ["ems_inventory_net_worth_table_error"], marks=6,
    )


def build_20_fractional_instalment_debt_net_worth_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    cash = rng.randrange(40, 120, 10)
    bike = rng.randrange(400, 900, 50)
    unit_p = rng.randrange(150, 300, 25)
    audio = unit_p * 3
    owed_audio = unit_p  # 1/3 still owing
    sav = rng.randrange(300, 750, 50)
    store_owe = rng.randrange(40, 100, 10)
    tot_a = cash + bike + audio + sav
    tot_l = owed_audio + store_owe
    nw = tot_a - tot_l
    prompt = (
        f"{name} owns {_fmt_r(cash)} cash, a bicycle worth {_fmt_r(bike)}, an audio system worth {_fmt_r(audio)} "
        f"(with two-thirds paid off and one-third still owing), and {_fmt_r(sav)} in savings, while also owing {_fmt_r(store_owe)} to a cousin. "
        f"Calculate {name}'s Net Worth (numbers only)."
    )
    sol = (
        f"1. Amount still owing on audio system = 1/3 × {_fmt_r(audio)} = {_fmt_r(owed_audio)}\n"
        f"2. Total Assets = {_fmt_r(cash)} + {_fmt_r(bike)} + {_fmt_r(audio)} + {_fmt_r(sav)} = {_fmt_r(tot_a)}\n"
        f"3. Total Liabilities = {_fmt_r(owed_audio)} + {_fmt_r(store_owe)} = {_fmt_r(tot_l)}\n"
        f"4. Net Worth = {_fmt_r(tot_a)} - {_fmt_r(tot_l)} = **{_fmt_r(nw)}**"
    )
    return _make_calc(
        rng, "20_fractional_instalment_debt_net_worth_calc", "Fractional Instalment Net Worth", prompt,
        nw, "Net Worth = Sum of full Asset values - (1/3 owing + Cousin Loan)", sol,
        "List the full value of the audio system under Assets, and only the unpaid 1/3 under Liabilities.",
        f"1/3 of {audio} = {owed_audio}; Total Assets = {tot_a}; Total Liabilities = {tot_l}.",
        ["ems_fractional_debt_misread"], marks=5,
    )


def build_21_complete_donovan_statement_net_worth_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    flat_val = rng.randrange(540000, 720000, 30000)
    flat_paid = flat_val - rng.randrange(180000, 270000, 30000)
    car_val = rng.randrange(75000, 115000, 5000)
    car_owed = rng.randrange(15000, 35000, 5000)
    bank = rng.randrange(25000, 55000, 5000)
    bond_owed = flat_val - flat_paid
    tot_a = flat_val + car_val + bank
    tot_l = bond_owed + car_owed
    nw = tot_a - tot_l
    headers = ["Statement Line Item", "Section", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": f"Flat (market value {_fmt_r(flat_val)}, {_fmt_r(flat_paid)} paid)", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Asset", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(flat_val), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Motor car", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Asset", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(car_val), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Money in bank", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Asset", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(bank), "editable": False, "prefilled": True}],
        [{"cell_id": "r3_c0", "value": "Total Assets", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Subtotal", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": "", "editable": True, "expected": str(tot_a)}],
        [{"cell_id": "r4_c0", "value": "Remaining mortgage bond owing on flat", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "Liability", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": "", "editable": True, "expected": str(bond_owed)}],
        [{"cell_id": "r5_c0", "value": "Car finance still owing", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Liability", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": str(car_owed), "editable": False, "prefilled": True}],
        [{"cell_id": "r6_c0", "value": "Total Liabilities", "editable": False, "prefilled": True},
         {"cell_id": "r6_c1", "value": "Subtotal", "editable": False, "prefilled": True},
         {"cell_id": "r6_c2", "value": "", "editable": True, "expected": str(tot_l)}],
        [{"cell_id": "r7_c0", "value": "Net Worth", "editable": False, "prefilled": True},
         {"cell_id": "r7_c1", "value": "Owner Wealth", "editable": False, "prefilled": True},
         {"cell_id": "r7_c2", "value": "", "editable": True, "expected": str(nw)}],
    ]
    cmap = {"r3_c2": str(tot_a), "r4_c2": str(bond_owed), "r6_c2": str(tot_l), "r7_c2": str(nw)}
    chints = {
        "r3_c2": "Add Flat market value + Motor car + Money in bank.",
        "r4_c2": f"Remaining bond = {_fmt_r(flat_val)} - {_fmt_r(flat_paid)}.",
        "r6_c2": "Add Remaining bond + Car finance owing.",
        "r7_c2": "Subtract Total Liabilities from Total Assets.",
    }
    md_memo = (
        f"| Statement Line Item | Section | Amount (R) |\n|---|---|---:|\n"
        f"| Flat | Asset | {flat_val} |\n| Motor car | Asset | {car_val} |\n| Money in bank | Asset | {bank} |\n"
        f"| **Total Assets** | Subtotal | **{tot_a}** |\n"
        f"| Remaining bond owing | Liability | {bond_owed} |\n| Car finance owing | Liability | {car_owed} |\n"
        f"| **Total Liabilities** | Subtotal | **{tot_l}** |\n"
        f"| **Net Worth** | Owner Wealth | **{nw}** |"
    )
    prompt = f"Complete {name}'s Statement of Net Worth below (enter clean integer amounts without 'R' or spaces)."
    return _make_ledger(
        rng, "21_complete_donovan_statement_net_worth_table", "Complete Statement of Net Worth",
        prompt, headers, rows, cmap, chints, md_memo,
        "Market value goes in Assets; unpaid balance goes in Liabilities.",
        f"Bond owing = {flat_val} - {flat_paid} = {bond_owed}.",
        ["ems_statement_net_worth_table_error"], marks=8,
    )


def build_22_debt_repayment_vs_cash_asset_impact_on_net_worth(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    pay = rng.randrange(3000, 9000, 1000)
    prompt = (
        f"{name} uses {_fmt_r(pay)} from a bank savings account to pay off {_fmt_r(pay)} owed on a clothing store account. "
        f"Explain the exact effect on {name}'s Total Assets, Total Liabilities, and overall Net Worth."
    )
    mps = [
        f"Total Assets decrease by {_fmt_r(pay)} because cash in the bank savings account decreases.",
        f"Total Liabilities decrease by {_fmt_r(pay)} because the store debt owed is settled.",
        "Overall Net Worth remains unchanged because Assets and Liabilities drop by the exact same amount.",
        "Liquidity drops slightly, while monthly interest or debt stress is reduced going forward.",
    ]
    sample = (
        f"- **Assets**: Decrease by {_fmt_r(pay)} (bank balance drops).\n"
        f"- **Liabilities**: Decrease by {_fmt_r(pay)} (store account settled).\n"
        f"- **Net Worth**: **Unchanged**, because Assets - Liabilities shifts by (-{_fmt_r(pay)}) - (-{_fmt_r(pay)}) = R0."
    )
    return _make_typed(
        rng, "22_debt_repayment_vs_cash_asset_impact_on_net_worth", "Debt Repayment Effect on Net Worth", prompt,
        mps, ["assets decrease", "liabilities decrease", "net worth unchanged"], sample,
        "Check both sides of Net Worth = Assets - Liabilities when paying cash toward debt.",
        "Both Assets and Liabilities decrease equally, leaving Net Worth identical immediately.",
        ["ems_thinks_debt_repayment_drops_net_worth"],
    )


def build_23_depreciation_vs_appreciation_effect_on_net_worth(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    pct = rng.choice([8, 10, 12])
    prompt = (
        f"{name} wants to grow long-term Net Worth in {rng.choice(AREAS)}. Compare buying a {pct}% appreciating asset (a small house/plot) "
        f"versus taking a loan to buy a rapidly depreciating item like electronics or luxury clothes."
    )
    mps = [
        "Property/land generally appreciates (grows in market value) over time, lifting Total Assets and Net Worth.",
        "Electronics or luxury consumer goods depreciate rapidly in resale value while the loan liability remains.",
        "Borrowing for depreciating consumer items leaves Liabilities higher than Asset value, risking a net worth deficit.",
        "Long-term wealth grows faster when financing productive or appreciating assets rather than consumption.",
    ]
    sample = (
        f"- **Appreciating Asset (Property)**: Growing value (+{pct}%/yr) builds equity as the bond shrinks, increasing Net Worth.\n"
        "- **Depreciating Loan Purchase**: Resale value falls sharply while full loan debt plus interest stays, shrinking or creating a negative Net Worth."
    )
    return _make_typed(
        rng, "23_depreciation_vs_appreciation_effect_on_net_worth", "Appreciating vs Depreciating Assets", prompt,
        mps, ["appreciate", "depreciate", "loan", "net worth", "asset"], sample,
        "Track how asset market value changes over 3–5 years compared to the remaining debt.",
        "Contrast growing property value against shrinking electronics resale value.",
        ["ems_consumer_debt_net_worth_blindspot"],
    )


def build_24_passive_vs_active_personal_income_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    s_amt = rng.randrange(11000, 19000, 1000)
    r_amt = rng.randrange(2500, 5000, 500)
    i_amt = rng.randrange(400, 1100, 100)
    w_amt = rng.randrange(1600, 3200, 200)
    headers = ["Income Stream", "Monthly Amount", "Active or Passive", "Income Source"]
    items = [
        ("Full-time teaching salary", s_amt, "Active", "Work"),
        ("Rental from backyard cottage", r_amt, "Passive", "Land"),
        ("Fixed deposit bank interest", i_amt, "Passive", "Capital"),
        ("Weekend baking wages", w_amt, "Active", "Work"),
    ]
    rows: List[List[Dict[str, Any]]] = []
    cmap: Dict[str, str] = {}
    chints: Dict[str, str] = {}
    md_lines = [f"| {' | '.join(headers)} |", "|---|---:|---|---|"]
    for i, (stream, amt, ap, src) in enumerate(items):
        c2, c3 = f"r{i}_c2", f"r{i}_c3"
        cmap[c2], cmap[c3] = ap, src
        chints[c2] = "Enter 'Active' or 'Passive'."
        chints[c3] = "Enter 'Work', 'Capital', or 'Land'."
        rows.append([
            {"cell_id": f"r{i}_c0", "value": stream, "editable": False, "prefilled": True},
            {"cell_id": f"r{i}_c1", "value": _fmt_r(amt), "editable": False, "prefilled": True},
            {"cell_id": c2, "value": "", "editable": True, "expected": ap},
            {"cell_id": c3, "value": "", "editable": True, "expected": src},
        ])
        md_lines.append(f"| {stream} | {_fmt_r(amt)} | {ap} | {src} |")
    prompt = (
        f"Classify {name}'s four monthly income streams in the schedule below: enter **Active** or **Passive** in column 3, "
        f"and **Work**, **Capital**, or **Land** in column 4."
    )
    return _make_ledger(
        rng, "24_passive_vs_active_personal_income_table", "Active vs Passive Income Sources Schedule",
        prompt, headers, rows, cmap, chints, "\n".join(md_lines),
        "Active income requires direct hours/labour; Passive income flows from property or invested money.",
        "Use exact terms: Active/Passive and Work/Capital/Land.",
        ["ems_passive_income_misclassification"], marks=8,
    )


def build_25_personal_asset_liquidity_spectrum_visual(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    a_cash = rng.randrange(6000, 18000, 1000)
    a_ut = rng.randrange(25000, 65000, 5000)
    a_house = rng.randrange(480000, 880000, 20000)
    svg = _svg_liquidity_spectrum(name, a_cash, a_ut, a_house)
    prompt = (
        f"Based on {name}'s asset liquidity spectrum showing Bank Savings ({_fmt_r(a_cash)}), Unit Trust/Policy ({_fmt_r(a_ut)}), "
        f"and a Residential House ({_fmt_r(a_house)}), which statement correctly contrasts Current and Non-current Assets?"
    )
    correct = f"Bank Savings ({_fmt_r(a_cash)}) is the most liquid current asset; the Residential House ({_fmt_r(a_house)}) is a non-current asset taking months to sell."
    distractors = [
        f"The Residential House ({_fmt_r(a_house)}) converts to cash fastest because its Rand value is highest.",
        f"All three items are liabilities because {name} cannot spend property directly at a supermarket.",
        f"Unit trusts ({_fmt_r(a_ut)}) are always physical non-current assets kept inside a garage.",
    ]
    sol = f"Liquidity measures how quickly an asset turns into cash: Bank Savings ({_fmt_r(a_cash)}) is fastest (current), whereas a House ({_fmt_r(a_house)}) is a slow-to-sell tangible non-current asset."
    return _make_mcq(
        rng, "25_personal_asset_liquidity_spectrum_visual", "Asset Liquidity Spectrum Analysis", prompt,
        correct, distractors, sol,
        "Higher Rand value does NOT mean faster cash conversion.",
        "Current assets sit on the left (fastest to cash); tangible property sits on the right (months).",
        ["ems_equates_high_value_with_liquidity"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25 = {
    "01_personal_income_definition_wealth": build_01_personal_income_definition_wealth,
    "02_three_personal_income_sources_classification": build_02_three_personal_income_sources_classification,
    "03_salary_wage_commission_comparison": build_03_salary_wage_commission_comparison,
    "04_gross_wage_commission_income_calc": build_04_gross_wage_commission_income_calc,
    "05_personal_expenses_definition_examples": build_05_personal_expenses_definition_examples,
    "06_personal_vs_business_expense_distinction": build_06_personal_vs_business_expense_distinction,
    "07_ethics_financial_worth_vs_human_worth": build_07_ethics_financial_worth_vs_human_worth,
    "08_statement_of_net_worth_balance_sheet_alias": build_08_statement_of_net_worth_balance_sheet_alias,
    "09_current_assets_short_term_liquidity": build_09_current_assets_short_term_liquidity,
    "10_non_current_assets_tangible_long_term": build_10_non_current_assets_tangible_long_term,
    "11_personal_assets_liabilities_classification_table": build_11_personal_assets_liabilities_classification_table,
    "12_current_vs_long_term_liabilities_split": build_12_current_vs_long_term_liabilities_split,
    "13_net_worth_equation_surplus_deficit_concept": build_13_net_worth_equation_surplus_deficit_concept,
    "14_remaining_loan_balance_from_paid_portion": build_14_remaining_loan_balance_from_paid_portion,
    "15_net_worth_surplus_calculation": build_15_net_worth_surplus_calculation,
    "16_net_worth_deficit_calculation": build_16_net_worth_deficit_calculation,
    "17_asset_liability_net_worth_stacked_bar_visual": build_17_asset_liability_net_worth_stacked_bar_visual,
    "18_missing_asset_or_liability_reverse_calc": build_18_missing_asset_or_liability_reverse_calc,
    "19_household_room_inventory_statement_net_worth_table": build_19_household_room_inventory_statement_net_worth_table,
    "20_fractional_instalment_debt_net_worth_calc": build_20_fractional_instalment_debt_net_worth_calc,
    "21_complete_donovan_statement_net_worth_table": build_21_complete_donovan_statement_net_worth_table,
    "22_debt_repayment_vs_cash_asset_impact_on_net_worth": build_22_debt_repayment_vs_cash_asset_impact_on_net_worth,
    "23_depreciation_vs_appreciation_effect_on_net_worth": build_23_depreciation_vs_appreciation_effect_on_net_worth,
    "24_passive_vs_active_personal_income_table": build_24_passive_vs_active_personal_income_table,
    "25_personal_asset_liquidity_spectrum_visual": build_25_personal_asset_liquidity_spectrum_visual,
}
