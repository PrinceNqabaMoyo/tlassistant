"""Grade 8 EMS - The National Budget: Archetypes 01 to 25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/02. The National Budget.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, NAMES as PERSON_NAMES

BUSINESS_NAMES = [
    "Ubuntu Solar Services",
    "Kasi Fresh Logistics",
    "Mfula Civil Contractors",
    "Naledi Packaging Works",
    "Imbali Textile Works",
    "Vula Tech Supplies",
    "Mzansi Retailers",
    "Karabo Foods Holdings",
]


def _fmt_r(amount: int | float) -> str:
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _make_cell(coord: str, value: str, cell_type: str) -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "cell_id": coord,
        "value": value,
        "type": cell_type,
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
        "topic": "The National Budget",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_national_budget",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_bud_{subskill}",
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
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["economy", "national_budget", "south_africa"],
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
    qtype: str = "short_answer",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "The National Budget",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_national_budget",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_bud_{subskill}",
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
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["economy", "national_budget", "south_africa"],
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
) -> Dict[str, Any]:
    return {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "The National Budget",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_national_budget",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_bud_{subskill}",
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
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["economy", "national_budget", "south_africa"],
    }


def arch_01_definition_and_purpose_of_national_budget(rng: random.Random) -> Dict[str, Any]:
    year = rng.choice([2024, 2025, 2026])
    area = rng.choice(AREAS)
    prompt = (
        f"During a civic economics workshop in **{area}**, a speaker summarises South Africa's **{year}/{year + 1} National Budget**.\n\n"
        "Which option **most accurately** defines the **National Budget**?"
    )
    correct = "An annual financial plan setting out expected government revenue (money flowing in) and planned public expenditure (money flowing out) for the country."
    distractors = [
        "A private retail balance sheet recording only supermarket sales profits in Gauteng.",
        "A list of international holidays when municipal offices close for maintenance.",
        "A voluntary household shopping receipt issued to shoppers at month-end.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_01",
        subskill="01_definition_and_purpose_of_national_budget",
        title="Definition & Purpose of the National Budget",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The **National Budget** ({year}/{year + 1}) is the country's formal annual financial plan estimating "
            "**revenue** (taxes, fees, borrowing) and allocating **expenditure** across public services."
        ),
        hints={
            "tier_1": "Every budget compares two sides: money expected to come in and planned money going out.",
            "tier_2": "A National Budget plans state revenue and expenditure for the whole country over a year.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_national_budget_with_business_profit_statement"],
    )


def arch_02_minister_of_finance_and_national_treasury_roles(rng: random.Random) -> Dict[str, Any]:
    year = rng.choice([2024, 2025, 2026])
    sector = rng.choice(["rural primary health clinics", "public transport upgrades", "school textbook procurement"])
    prompt = (
        f"Ahead of the **{year}** South African Budget Speech deciding allocations for **{sector}**, two institutions lead national financial planning.\n\n"
        "Name the **national department** responsible for managing South Africa's public finances and the **Cabinet member** who presents and leads National Budget decisions."
    )
    expected = "National Treasury manages the state's finances, and the Minister of Finance leads and presents National Budget decisions to Parliament."
    sol = (
        f"**National Budget Leadership ({year}) [2 marks]:**\n\n"
        "1. **National Treasury:** The national government department responsible for drafting, managing, and monitoring public finances **[1]**.\n"
        f"2. **Minister of Finance:** The Cabinet Minister (such as Minister Enoch Godongwana) who makes key fiscal recommendations and tables the Budget before Parliament for **{sector}** and all sectors **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_02",
        subskill="02_minister_of_finance_and_national_treasury_roles",
        title="National Treasury & Minister of Finance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=2,
        hints={
            "tier_1": "Which department looks after the national purse, and which Cabinet Minister reads the February Budget Speech?",
            "tier_2": "Name National Treasury and the Minister of Finance.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies National Treasury", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Identifies the Minister of Finance", "marks": 1, "editable": True},
        ],
        misconception_tags=["confusing_sars_with_national_treasury"],
    )


def arch_03_sars_tax_collection_and_fiscal_year_schedule(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{biz}** in **{area}** deducts employee tax and pays corporate taxes on behalf of the state.\n\n"
        "Which South African authority collects national tax revenue, and when does South Africa's government **financial (fiscal) year** run?"
    )
    correct = "South African Revenue Service (SARS); financial year runs from 1 April to 31 March of the following year."
    distractors = [
        "South African Broadcasting Corporation (SABC); runs from 1 July to 30 June.",
        "Municipal Traffic Department; runs strictly from 1 January to 30 June.",
        "Constitutional Court Registrar; runs once every five years.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_03",
        subskill="03_sars_tax_collection_and_fiscal_year_schedule",
        title="SARS Tax Collection & Fiscal Year",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"National taxes paid by **{biz}** and households are collected by **SARS** (South African Revenue Service) "
            "for the national fiscal year running **1 April to 31 March**."
        ),
        hints={
            "tier_1": "SARS collects national taxes, while the Budget Speech in February precedes the new April start.",
            "tier_2": "SARS; 1 April to 31 March.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_government_fiscal_year_matches_calendar_year"],
    )


def arch_04_budget_revenue_vs_expenditure_sides(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Personal income tax (PAYE) collected from teachers and engineers", "Revenue"),
        ("Building new RDP low-cost houses for qualifying families", "Expenditure"),
        ("15% Value Added Tax (VAT) paid at supermarket checkouts", "Revenue"),
        ("Paying monthly old-age and child-support social grants", "Expenditure"),
        ("Excise (sin) taxes collected on tobacco and alcohol sales", "Revenue"),
        ("Paying salaries of public hospital doctors and nurses", "Expenditure"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["National Budget Item", "Budget Side (Revenue or Expenditure)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| National Budget Item | Budget Side |", "| :--- | :--- |"]
    for idx, (item, side) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", item, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = side
        cell_hints[c1] = "Write Revenue (inflow) or Expenditure (outflow)."
        memo_lines.append(f"| {item} | {side} |")

    worked = "**Completed Revenue vs Expenditure Schedule [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{item} -> {side}" for item, side in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_bud_04",
        subskill="04_budget_revenue_vs_expenditure_sides",
        title="Budget Revenue vs Expenditure Classification",
        prompt="Classify each National Budget transaction below as either **Revenue** (money flowing into the state) or **Expenditure** (money spent by the state).",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Taxes and fees flowing into SARS are Revenue; state payments for housing, salaries, and grants are Expenditure.",
            "tier_2": "Enter exactly 'Revenue' or 'Expenditure'.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Correct side for row {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["reversing_tax_inflows_and_grant_outflows"],
    )


def arch_05_direct_tax_definition_and_incidence(rng: random.Random) -> Dict[str, Any]:
    worker = rng.choice(PERSON_NAMES)
    salary = rng.choice([22000, 28500, 34000])
    prompt = (
        f"**{worker}** earns **{_fmt_r(salary)}** per month as a hospital technician, and income tax is deducted directly from **{worker}**'s earnings for SARS.\n\n"
        "Why is Personal Income Tax (PAYE) classified as a **direct tax**?"
    )
    correct = "The tax burden falls directly on the person earning the income and cannot be shifted onto someone else."
    distractors = [
        "Retail supermarkets collect income tax on every loaf of bread sold.",
        "Taxpayers voluntarily choose how many cents per Rand they want to donate.",
        "Only state-owned enterprises pay direct taxes while households never do.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_05",
        subskill="05_direct_tax_definition_and_incidence",
        title="Direct Tax Incidence & Definition",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **direct tax** (such as **{worker}**'s PAYE on **{_fmt_r(salary)}** or corporate income tax) "
            "is levied straight on income/profit and **cannot be shifted** to another party."
        ),
        hints={
            "tier_1": f"Can {worker} force a local shop customer to pay {worker}'s income tax instead?",
            "tier_2": "Direct taxes stay on the earner; indirect taxes can be passed on via prices.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_income_tax_can_be_shifted_like_vat"],
    )


def arch_06_indirect_tax_definition_and_shifting(rng: random.Random) -> Dict[str, Any]:
    shop = rng.choice(BUSINESS_NAMES)
    tax_example = rng.choice(["15% Value Added Tax (VAT)", "the fuel levy on petrol", "excise (sin) tax on bottled beverages"])
    prompt = (
        f"**{shop}** includes **{tax_example}** in the shelf price paid by retail customers, then pays that collected tax over to SARS.\n\n"
        "Define an **indirect tax** and explain how the intermediary (**shifting**) mechanism works in this transaction."
    )
    expected = (
        "An indirect tax is collected from consumers via an intermediary (like a retailer/producer) and shifted onto the final buyer through the selling price. "
        f"Customers pay {tax_example} inside {shop}'s price, and {shop} remits it to SARS."
    )
    sol = (
        f"**Indirect Tax Mechanism ({shop}) [3 marks]:**\n\n"
        "1. **Definition:** A tax paid indirectly to government through an intermediary business rather than straight from personal income **[1]**.\n"
        f"2. **Shifting Mechanism:** **{shop}** adds **{tax_example}** into the selling price paid by shoppers **[1]** and subsequently transfers that tax to **SARS** **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_06",
        subskill="06_indirect_tax_definition_and_shifting",
        title="Indirect Taxes & Tax Shifting via Retailers",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Notice two parties: the shopper paying at the till and {shop} passing the tax to SARS.",
            "tier_2": "State that indirect taxes are embedded in goods/services prices and remitted by intermediaries.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Collected via an intermediary rather than directly on income", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Shifted into final price paid by consumer", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Retailer/producer remits tax to SARS", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_shopkeepers_keep_vat_revenue_for_themselves"],
    )


def arch_07_direct_vs_indirect_taxes_classification_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    tax_pool = [
        ("Personal Income Tax (PAYE) on monthly salaries", "Direct Tax"),
        (f"Company Income Tax paid on {biz}'s annual profit", "Direct Tax"),
        ("15% Value Added Tax (VAT) on retail furniture", "Indirect Tax"),
        ("Excise (sin) tax on cigarettes and spirits", "Indirect Tax"),
        ("General Fuel Levy included per litre of petrol", "Indirect Tax"),
    ]
    rng.shuffle(tax_pool)
    headers = ["Tax Type in South Africa", "Category (Direct Tax or Indirect Tax)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Tax Type in South Africa | Category |", "| :--- | :--- |"]
    for idx, (name, cat) in enumerate(tax_pool):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", name, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = cat
        cell_hints[c1] = "Enter 'Direct Tax' or 'Indirect Tax'."
        memo_lines.append(f"| {name} | {cat} |")

    worked = "**Completed Direct vs Indirect Tax Classification [5 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{n} -> {c}" for n, c in tax_pool)
    return _build_table(
        rng,
        qid_prefix="g8_bud_07",
        subskill="07_direct_vs_indirect_taxes_classification_table",
        title="Classify Direct vs Indirect Taxes Schedule",
        prompt="Classify each South African tax in the schedule as a **Direct Tax** or an **Indirect Tax**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Income and profit taxes are Direct; taxes on spending (VAT, sin tax, fuel levy) are Indirect.",
            "tier_2": "Type exactly: 'Direct Tax' or 'Indirect Tax'.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{tax_pool[i][0]} -> {tax_pool[i][1]}", "marks": 1, "editable": True}
            for i in range(5)
        ],
        misconception_tags=["classifying_fuel_levy_or_vat_as_direct_tax"],
    )


def arch_08_paye_personal_income_tax_bracket_calculation(rng: random.Random) -> Dict[str, Any]:
    worker = rng.choice(PERSON_NAMES)
    gross_monthly = rng.choice([18000, 24000, 30000, 36000])
    eff_rate = rng.choice([18, 20, 22])
    paye_monthly = gross_monthly * eff_rate // 100
    net_monthly = gross_monthly - paye_monthly
    annual_tax = paye_monthly * 12

    prompt = (
        f"**{worker}** earns a gross monthly salary of **{_fmt_r(gross_monthly)}**, with an effective PAYE income tax rate of **{eff_rate}%**.\n\n"
        "Calculate:\n"
        "(a) **Monthly PAYE** deducted and paid to SARS;\n"
        f"(b) **{worker}**'s **monthly net take-home pay**;\n"
        "(c) **Total annual income tax** collected by SARS over 12 months."
    )
    expected = f"(a) Monthly PAYE = {_fmt_r(paye_monthly)}; (b) Net monthly pay = {_fmt_r(net_monthly)}; (c) Annual PAYE = {_fmt_r(annual_tax)}"
    sol = (
        f"**PAYE Income Tax Calculation ({worker}) [4 marks]:**\n\n"
        f"**(a) Monthly PAYE ({eff_rate}%):**\n"
        f"$${_fmt_r(gross_monthly)} \\times {eff_rate}\\% = {_fmt_r(paye_monthly)}$$ **[1]**\n\n"
        "**(b) Monthly Net Take-Home Pay:**\n"
        f"$${_fmt_r(gross_monthly)} - {_fmt_r(paye_monthly)} = {_fmt_r(net_monthly)}$$ **[1]**\n\n"
        "**(c) Annual PAYE Collected (12 months):**\n"
        f"$${_fmt_r(paye_monthly)} \\times 12 = {_fmt_r(annual_tax)}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_08",
        subskill="08_paye_personal_income_tax_bracket_calculation",
        title="PAYE Personal Income Tax & Take-Home Pay",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Compute {eff_rate}% of {_fmt_r(gross_monthly)} first.",
            "tier_2": "Subtract monthly PAYE from gross salary for net pay; multiply monthly PAYE by 12 for annual revenue.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Monthly PAYE = {_fmt_r(paye_monthly)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Net monthly pay = {_fmt_r(net_monthly)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Annual PAYE = {_fmt_r(annual_tax)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_paye_instead_of_deducting_from_gross"],
        qtype="calculation",
    )


def arch_09_corporate_business_income_tax_calculation(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    profit = rng.choice([800000, 1200000, 1500000, 2000000])
    cit_rate = 27
    tax_due = profit * cit_rate // 100
    retained = profit - tax_due

    prompt = (
        f"**{biz}** records an annual taxable profit of **{_fmt_r(profit)}**. "
        f"Under South Africa's **{cit_rate}%** Corporate Income Tax rate:\n\n"
        "(a) Calculate the **business income tax** payable to SARS;\n"
        f"(b) Calculate **{biz}**'s **after-tax profit** remaining for owners or reinvestment."
    )
    expected = f"(a) Corporate tax = {_fmt_r(tax_due)}; (b) After-tax profit = {_fmt_r(retained)}"
    sol = (
        f"**Corporate Income Tax ({biz}) [3 marks]:**\n\n"
        f"**(a) Tax Payable ({cit_rate}%):**\n"
        f"$${_fmt_r(profit)} \\times 27\\% = {_fmt_r(tax_due)}$$ **[2]**\n\n"
        "**(b) After-Tax Profit:**\n"
        f"$${_fmt_r(profit)} - {_fmt_r(tax_due)} = {_fmt_r(retained)}$$ **[1]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_09",
        subskill="09_corporate_business_income_tax_calculation",
        title="Corporate Income Tax (Direct Business Tax)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Multiply taxable profit by 0,27 (27%).",
            "tier_2": "Subtract tax payable from pre-tax profit to get after-tax profit.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Corporate tax = {_fmt_r(tax_due)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"After-tax profit = {_fmt_r(retained)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["taxing_total_turnover_instead_of_profit"],
        qtype="calculation",
    )


def arch_10_vat_15_percent_forward_calculation(rng: random.Random) -> Dict[str, Any]:
    shop = rng.choice(BUSINESS_NAMES)
    item = rng.choice(["an office printer", "a workshop drill", "a delivery bicycle", "a microwave oven"])
    excl = rng.choice([1200, 1600, 2400, 3200, 4800])
    vat_amt = excl * 15 // 100
    incl = excl + vat_amt

    prompt = (
        f"**{shop}** prices **{item}** at **{_fmt_r(excl)}** **excluding VAT**. "
        "South Africa's standard VAT rate is **15%**.\n\n"
        "Calculate:\n"
        "(a) The **15% VAT amount** added at the till;\n"
        "(b) The **final VAT-inclusive price** paid by the consumer."
    )
    expected = f"(a) VAT = {_fmt_r(vat_amt)}; (b) VAT-inclusive price = {_fmt_r(incl)}"
    sol = (
        f"**Forward 15% VAT Calculation ({shop}) [3 marks]:**\n\n"
        "**(a) 15% VAT Amount:**\n"
        f"$${_fmt_r(excl)} \\times 15\\% = {_fmt_r(vat_amt)}$$ **[2]**\n\n"
        "**(b) VAT-Inclusive Price:**\n"
        f"$${_fmt_r(excl)} + {_fmt_r(vat_amt)} = {_fmt_r(incl)}$$ **[1]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_10",
        subskill="10_vat_15_percent_forward_calculation",
        title="Calculating 15% VAT & VAT-Inclusive Price",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Find 15% of the VAT-exclusive price (10% + half of 10%).",
            "tier_2": f"VAT = 0,15 x {_fmt_r(excl)}; add VAT to get the till total.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"15% VAT = {_fmt_r(vat_amt)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"VAT-inclusive total = {_fmt_r(incl)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["using_outdated_14_percent_vat_rate"],
        qtype="calculation",
    )


def arch_11_vat_15_percent_reverse_extraction(rng: random.Random) -> Dict[str, Any]:
    shop = rng.choice(BUSINESS_NAMES)
    base_excl = rng.choice([800, 1400, 2000, 2600])
    vat_portion = base_excl * 15 // 100
    incl_total = base_excl + vat_portion

    prompt = (
        f"A receipt from **{shop}** shows a **VAT-inclusive total** of **{_fmt_r(incl_total)}** (standard 15% VAT is already inside this price).\n\n"
        "Calculate:\n"
        "(a) The **original VAT-exclusive price** (divide by $1{,}15$);\n"
        "(b) The exact **VAT portion** remitted to SARS ($\\times \\frac{15}{115}$)."
    )
    expected = f"(a) VAT-exclusive price = {_fmt_r(base_excl)}; (b) VAT portion = {_fmt_r(vat_portion)}"
    sol = (
        f"**Extracting VAT from a VAT-Inclusive Receipt ({shop}) [4 marks]:**\n\n"
        "**(a) VAT-Exclusive Price (100%):**\n"
        f"$${_fmt_r(incl_total)} \\div 1{{,}}15 = {_fmt_r(base_excl)}$$ **[2]**\n\n"
        "**(b) VAT Portion (15%):**\n"
        f"$${_fmt_r(incl_total)} - {_fmt_r(base_excl)} = {_fmt_r(vat_portion)}$$ *(or ${_fmt_r(incl_total)} \\times \\frac{{15}}{{115}}$)* **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_11",
        subskill="11_vat_15_percent_reverse_extraction",
        title="Extracting 15% VAT from a VAT-Inclusive Total",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "A VAT-inclusive amount equals 115% of the base price, not 100%!",
            "tier_2": f"Do NOT take 15% of {_fmt_r(incl_total)}. Divide {_fmt_r(incl_total)} by 1,15 first.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Divides by 1,15 -> Base = {_fmt_r(base_excl)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"VAT extracted = {_fmt_r(vat_portion)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["multiplying_vat_inclusive_price_by_15_percent"],
        qtype="calculation",
    )


def arch_12_vat_zero_rated_basic_foodstuffs_equity(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    basket = rng.choice(["brown bread, maize meal, fresh milk, and dried beans", "brown bread, rice, eggs, and cooking oil"])
    prompt = (
        f"When families in **{area}** buy basic staples such as **{basket}**, the till slip displays **0% VAT**.\n\n"
        "Why does the National Budget zero-rate essential basic foodstuffs?"
    )
    correct = "To make essential nutrition more affordable for low-income households and reduce inequality because poorer families spend a larger share of income on food."
    distractors = [
        "Because supermarkets refuse to install tills capable of multiplying by 15%.",
        "Because brown bread and milk are luxury imports consumed only by tourists.",
        "So that SARS collects higher personal income tax from bakers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_12",
        subskill="12_vat_zero_rated_basic_foodstuffs_equity",
        title="Zero-Rated Basic Foods & Reducing Inequality",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Zero-rating essentials (**{basket}**) shields vulnerable households in **{area}** from indirect VAT costs on daily food, directly lowering poverty and food insecurity."
        ),
        hints={
            "tier_1": "Who suffers most if 15% tax is added to bread, maize meal, and milk?",
            "tier_2": "Zero-rating essential foods reduces the burden on poorer households.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_all_grocery_items_attract_15_percent_vat"],
    )


def arch_13_sin_tax_excise_purpose_and_price_impact(rng: random.Random) -> Dict[str, Any]:
    product = rng.choice(["a carton of cigarettes", "a bottle of spirits", "bottled alcoholic cider"])
    pre_tax = rng.choice([80, 110, 140])
    sin_tax = rng.choice([25, 35, 45])
    new_price = pre_tax + sin_tax
    prompt = (
        f"In the National Budget Speech, the Minister raises the **sin (excise) tax** on **{product}** by **{_fmt_r(sin_tax)}** above its previous retail price of **{_fmt_r(pre_tax)}**.\n\n"
        f"(a) Calculate the **new shelf price** of {product};\n"
        "(b) State **two distinct reasons** why government levies sin taxes on tobacco and alcohol."
    )
    expected = (
        f"(a) New price = {_fmt_r(new_price)}. "
        "1) Raises indirect tax revenue for the National Budget; 2) Discourages harmful consumption to protect public health."
    )
    sol = (
        f"**Sin (Excise) Tax Analysis ({product}) [3 marks]:**\n\n"
        f"**(a) New Shelf Price:** ${_fmt_r(pre_tax)} + {_fmt_r(sin_tax)} = {_fmt_r(new_price)}$ **[1]**\n\n"
        "**(b) Two Government Reasons [2 marks]:**\n"
        "1. **Revenue Generation:** Raises substantial indirect tax revenue for public hospitals and state spending **[1]**.\n"
        "2. **Health Deterrent:** Higher prices discourage excessive consumption of addictive/harmful products **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_13",
        subskill="13_sin_tax_excise_purpose_and_price_impact",
        title="Sin (Excise) Tax Calculation & Dual Purpose",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Sin tax increases the price and tries to nudge health behaviour while raising state cash.",
            "tier_2": "Add the tax for the new price; give one budget reason and one public-health reason.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"New price = {_fmt_r(new_price)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Raises tax revenue for the state", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Discourages harmful consumption / reduces health burden", "marks": 1, "editable": True},
        ],
        misconception_tags=["believing_sin_tax_is_a_direct_income_tax"],
    )


def arch_14_fuel_levy_and_road_accident_fund_mechanism(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    litres = rng.choice([200, 350, 500, 600])
    gen_fuel_cents = 396  # R3,96/L
    raf_cents = 218       # R2,18/L
    tot_gen = round(litres * (gen_fuel_cents / 100), 2)
    tot_raf = round(litres * (raf_cents / 100), 2)
    tot_levies = round(tot_gen + tot_raf, 2)

    prompt = (
        f"Delivery vans operated by **{biz}** purchase **{litres} litres** of diesel this week. "
        "Each litre includes a **R3,96** General Fuel Levy and a **R2,18** Road Accident Fund (RAF) levy.\n\n"
        "Calculate the **total indirect fuel taxes** paid on these **{litres} litres**, and briefly state what the **RAF levy** funds."
    )
    expected = (
        f"Total fuel levies = {_fmt_r(tot_levies)} (General Fuel Levy {_fmt_r(tot_gen)} + RAF {_fmt_r(tot_raf)}). "
        "The RAF levy funds compensation/medical support for road accident victims."
    )
    sol = (
        f"**Fuel Levy & RAF Calculation ({biz}) [4 marks]:**\n\n"
        f"- **Combined levy per litre:** $R3{{,}}96 + R2{{,}}18 = R6{{,}}14$ **[1]**\n"
        f"- **Total indirect fuel tax ({litres} L):** ${litres} \\times R6{{,}}14 = {_fmt_r(tot_levies)}$ *(General Fuel Levy: {_fmt_r(tot_gen)} + RAF: {_fmt_r(tot_raf)})* **[2]**\n"
        "- **Purpose of RAF:** Covers medical, rehabilitation, and income-loss claims for victims of road crashes **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_14",
        subskill="14_fuel_levy_and_road_accident_fund_mechanism",
        title="Fuel Levy & Road Accident Fund (RAF) Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Add R3,96 and R2,18 per litre first, then multiply by litres purchased.",
            "tier_2": "Total levy per litre = R6,14. Explain RAF protects road crash victims.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Combined levy per litre R6,14", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total fuel taxes = {_fmt_r(tot_levies)}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "RAF compensates/supports road accident victims", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_fuel_levy_goes_to_private_garages"],
        qtype="calculation",
    )


def arch_15_government_borrowing_bonds_and_interest_cost(rng: random.Random) -> Dict[str, Any]:
    borrowed_bn = rng.choice([120, 150, 200, 250])  # R million to keep arithmetic crisp for Gr8: let's use R million!
    interest_pct = rng.choice([8, 9, 10])
    annual_interest = borrowed_bn * interest_pct // 100
    prompt = (
        f"Suppose National Government borrows **{_fmt_r(borrowed_bn * 1000000)}** via government bonds at **{interest_pct}%** annual interest to cover a revenue shortfall.\n\n"
        "(a) Calculate the **annual interest cost** government must pay on this debt;\n"
        "(b) Why must government be careful not to borrow excessively year after year?"
    )
    expected = (
        f"(a) Annual interest = {_fmt_r(annual_interest * 1000000)}. "
        "(b) High debt interest consumes tax revenue needed for schools, clinics, roads, and grants."
    )
    sol = (
        "**Government Borrowing & Interest Burden [3 marks]:**\n\n"
        f"**(a) Annual Interest Cost ({interest_pct}%):**\n"
        f"$${_fmt_r(borrowed_bn * 1000000)} \\times {interest_pct}\\% = {_fmt_r(annual_interest * 1000000)}$$ **[2]**\n\n"
        "**(b) Fiscal Risk:** Escalating interest payments take up future tax revenue, leaving less money for hospitals, education, housing, and infrastructure **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_15",
        subskill="15_government_borrowing_bonds_and_interest_cost",
        title="State Borrowing & Annual Debt Interest Burden",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Loans must be repaid WITH interest!",
            "tier_2": f"Calculate {interest_pct}% of {_fmt_r(borrowed_bn * 1000000)} and link rising debt costs to squeezed social budgets.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Interest = {_fmt_r(annual_interest * 1000000)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Interest reduces future budget available for public services", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_government_borrowing_is_free_money"],
        qtype="calculation",
    )


def arch_16_non_tax_revenue_fees_interest_donations(rng: random.Random) -> Dict[str, Any]:
    extra = rng.choice(["passport and vehicle licence fees", "interest earned on state deposits and international donor grants", "customs harbour charges and state dividends"])
    prompt = (
        f"Besides direct and indirect taxes, National Treasury records inflows from **{extra}**.\n\n"
        "Where do these inflows fit in South Africa's National Budget structure?"
    )
    correct = "They form non-tax government revenue (interest, charges, and donations) alongside tax receipts to finance public expenditure."
    distractors = [
        "They are counted as government expenditure alongside school and hospital salaries.",
        "They are donated directly to private JSE-listed shareholders.",
        "They cannot legally be recorded in National Treasury accounts.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_16",
        subskill="16_non_tax_revenue_fees_interest_donations",
        title="Non-Tax State Revenue: Fees, Interest & Donations",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"While taxes are the main income stream, **interest, user charges, administrative fees, and donations** ({extra}) "
            "are valid **non-tax revenue sources** in the National Budget."
        ),
        hints={
            "tier_1": "Are fees, interest earned, and grants received money coming IN or going OUT?",
            "tier_2": "All money flowing in (other than loans) represents revenue — here specifically non-tax revenue.",
            "tier_3": correct,
        },
        misconception_tags=["believing_taxes_are_the_only_source_of_budget_revenue"],
    )


def arch_17_budget_deficit_vs_budget_surplus_calculation(rng: random.Random) -> Dict[str, Any]:
    direct_tax = rng.choice([720000, 810000, 880000])
    indirect_tax = rng.choice([540000, 590000, 620000])
    non_tax = rng.choice([40000, 50000, 60000])
    tot_rev = direct_tax + indirect_tax + non_tax
    deficit_val = rng.choice([120000, 150000, 180000])
    tot_exp = tot_rev + deficit_val

    rows = [
        [_make_cell("r0c0", "Direct Taxes (PAYE & Corporate)", "given"), _make_cell("r0c1", _fmt_r(direct_tax), "given")],
        [_make_cell("r1c0", "Indirect Taxes (VAT, Fuel, Excise)", "given"), _make_cell("r1c1", _fmt_r(indirect_tax), "given")],
        [_make_cell("r2c0", "Interest, Charges & Donations", "given"), _make_cell("r2c1", _fmt_r(non_tax), "given")],
        [_make_cell("r3c0", "Total Revenue", "given"), _make_cell("r3c1", "", "required")],
        [_make_cell("r4c0", "Total Planned Expenditure", "given"), _make_cell("r4c1", _fmt_r(tot_exp), "given")],
        [_make_cell("r5c0", "Budget Balance (State Deficit Amount)", "given"), _make_cell("r5c1", "", "required")],
    ]
    correct_map = {
        "r3c1": _fmt_r(tot_rev),
        "r5c1": _fmt_r(deficit_val),
    }
    cell_hints = {
        "r3c1": "Sum Direct Taxes + Indirect Taxes + Interest/Charges.",
        "r5c1": "Find Total Expenditure minus Total Revenue (the borrowing shortfall).",
    }
    worked = (
        "**Completed Budget Balance Summary (R million scale shown) [4 marks]:**\n\n"
        "| Budget Line Item | Amount |\n"
        "| :--- | :--- |\n"
        f"| Direct Taxes | {_fmt_r(direct_tax)} |\n"
        f"| Indirect Taxes | {_fmt_r(indirect_tax)} |\n"
        f"| Interest, Charges & Donations | {_fmt_r(non_tax)} |\n"
        f"| **Total Revenue** | **{_fmt_r(tot_rev)}** |\n"
        f"| Total Planned Expenditure | {_fmt_r(tot_exp)} |\n"
        f"| **Budget Deficit (Borrowing Required)** | **{_fmt_r(deficit_val)}** |\n\n"
        f"- **Total Revenue:** ${_fmt_r(direct_tax)} + {_fmt_r(indirect_tax)} + {_fmt_r(non_tax)} = {_fmt_r(tot_rev)}$ **[2]**.\n"
        f"- **Budget Deficit:** Since expenditure ({_fmt_r(tot_exp)}) exceeds revenue ({_fmt_r(tot_rev)}), government has a **deficit of {_fmt_r(deficit_val)}** **[2]**."
    )
    sample = f"Total Revenue = {_fmt_r(tot_rev)}; Budget Deficit = {_fmt_r(deficit_val)}"
    return _build_table(
        rng,
        qid_prefix="g8_bud_17",
        subskill="17_budget_deficit_vs_budget_surplus_calculation",
        title="Budget Balance: Revenue Total & Deficit Calculation",
        prompt="Complete the fiscal summary table (in R thousands) by calculating **Total Revenue** and the **Budget Deficit** that must be funded via borrowing.",
        headers=["Budget Line Item", "Amount (R '000)"],
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Add the three revenue lines first.",
            "tier_2": "Deficit = Planned Expenditure - Total Revenue.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Revenue = {_fmt_r(tot_rev)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Budget Deficit = {_fmt_r(deficit_val)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_expenditure_wrong_way_for_deficit"],
    )


def arch_18_education_spending_allocation_and_growth_impact(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    edu_pct = rng.choice([19, 20, 21])
    total_spend_bn = rng.choice([2100, 2200, 2400])  # using clean integers in R millions or billions
    edu_amt_bn = round(total_spend_bn * edu_pct / 100, 1)
    prompt = (
        f"Education typically forms the largest single functional allocation in South Africa's National Budget — suppose **{edu_pct}%** of a **{_fmt_r(total_spend_bn)} billion** national expenditure plan.\n\n"
        f"List **two concrete educational resources** funded for learners in **{area}** and explain **one long-term economic growth benefit** of prioritising education."
    )
    expected = (
        "Resources: Teacher salaries, public schools/classrooms, textbooks/stationery, and school nutrition programmes. "
        "Growth benefit: Skilled, literate workers earn higher incomes, improve business productivity, and widen future tax revenue."
    )
    sol = (
        f"**Education Budget Priority ({edu_pct}% = R{str(edu_amt_bn).replace('.', ',')} billion) [3 marks]:**\n\n"
        f"1. **Funded Resources ({area}):** Public school buildings, qualified teachers, textbooks, and national school feeding programmes **[2]**.\n"
        "2. **Economic Growth Benefit:** Better-educated citizens acquire scarce skills, raise workplace productivity, earn higher wages, and strengthen long-term tax collection **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_18",
        subskill="18_education_spending_allocation_and_growth_impact",
        title="Education Expenditure & Long-Term Growth",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of what a public school needs daily and why educated adults lift an entire economy.",
            "tier_2": "Give two tangible school inputs + one economic productivity/jobs link.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Two valid education inputs (teachers, schools, books, nutrition)", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Skilled workforce boosts productivity, employment, and tax base", "marks": 1, "editable": True},
        ],
        misconception_tags=["viewing_education_spending_as_non_productive_consumption"],
    )


def arch_19_health_expenditure_free_child_and_clinic_care(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    service = rng.choice(["free primary clinic visits and childhood immunisations", "free maternal and infant care plus HIV/TB medication"])
    prompt = (
        f"In **{area}**, the public Health budget funds **{service}**.\n\n"
        "How does public healthcare spending directly support **reducing economic inequalities** as well as economic growth?"
    )
    correct = "It ensures low-income families receive essential medical care without going bankrupt, keeping parents and children healthy enough to attend school and work."
    distractors = [
        "It bans all private pharmacies and doctors from treating insured patients.",
        "It charges tourists double VAT on medicine at national airports.",
        "It pays clinic staff strictly from municipal parking fines.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_19",
        subskill="19_health_expenditure_free_child_and_clinic_care",
        title="Health Budget: Free Clinic Care & Inequality Reduction",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Funding **{service}** in **{area}** prevents poor households from losing income to catastrophic medical bills while maintaining a healthy workforce and student body."
        ),
        hints={
            "tier_1": "What happens when a poor household can access clinics and infant care free of charge?",
            "tier_2": "Connect free healthcare to reduced poverty/inequality and healthier learners/workers.",
            "tier_3": correct,
        },
        misconception_tags=["overlooking_health_spending_as_inequality_reducer"],
    )


def arch_20_housing_expenditure_rdp_low_cost_settlements(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    units = rng.choice([450, 620, 850, 1100])
    cost_per_unit = rng.choice([140000, 160000, 180000])
    total_cost = units * cost_per_unit
    prompt = (
        f"Government allocates **{_fmt_r(total_cost)}** to construct **{units}** formal low-cost (**RDP**) houses with piped water and sanitation near **{area}**.\n\n"
        "State **two social or economic benefits** of RDP housing expenditure for both recipient households and the surrounding local economy."
    )
    expected = (
        "1) Provides safe shelter, dignity, clean sanitation, and an asset for low-income families to narrow inequality; "
        "2) Creates local construction jobs and boosts demand for brickmakers, plumbers, and suppliers."
    )
    sol = (
        f"**RDP Housing Allocation ({units} units @ {_fmt_r(cost_per_unit)} = {_fmt_r(total_cost)}) [3 marks]:**\n\n"
        f"1. **For Recipient Households ({area}):** Safe, weatherproof shelter with sanitation improves family health, safety, and dignity, reducing inequality **[1.5]**.\n"
        "2. **For Local Economy:** Construction contracts create jobs for local builders and boost sales for hardware and material suppliers **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_20",
        subskill="20_housing_expenditure_rdp_low_cost_settlements",
        title="RDP Housing Budget: Social & Local Economic Impact",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of BOTH who lives in the finished homes and who gets hired to build them.",
            "tier_2": "Mention family shelter/inequality reduction AND construction employment/materials demand.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Safe shelter, health/dignity, and inequality reduction for poor families", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Creates local construction jobs and boosts suppliers", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["ignoring_job_creation_effects_of_housing_budgets"],
    )


def arch_21_social_welfare_grants_and_hivaids_family_support(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    grant_type = rng.choice(["old-age pension, child-support, and disability grants", "foster-care, old-age, and child-support grants"])
    prompt = (
        f"In communities across **{area}**, grandparents caring for orphaned grandchildren (including families affected by HIV/AIDS) often rely on **{grant_type}**.\n\n"
        "Explain **two critical roles** that the **Social Welfare / Social Protection** budget plays for these households and local shopkeepers."
    )
    expected = (
        "1) Grants relieve extreme poverty by helping caregivers buy food, school uniforms, and transport; "
        "2) Because grant money is spent immediately in local spazas/shops, it sustains rural and township retail trade."
    )
    sol = (
        f"**Social Welfare Grants Impact ({area}) [3 marks]:**\n\n"
        "1. **Protecting Vulnerable Households:** Social grants support pensioners, persons with disabilities, and extended families raising children/orphans with money for nutrition and schooling **[2]**.\n"
        "2. **Local Retail Circulation:** Cash grants are spent quickly at nearby shops and markets, supporting local traders and food producers **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_21",
        subskill="21_social_welfare_grants_and_hivaids_family_support",
        title="Social Welfare Grants & Extended-Family Support",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of how elderly/orphaned households survive and where they spend that grant money.",
            "tier_2": "Address basic household food/care first, then spending circulation in local shops.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Supports vulnerable elderly, disabled, orphans, and extended-family caregivers", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Cash spent locally supports small shops and rural economies", "marks": 1, "editable": True},
        ],
        misconception_tags=["viewing_social_grants_as_leaking_out_of_local_economy"],
    )


def arch_22_transport_infrastructure_roads_rail_ports_raf(rng: random.Random) -> Dict[str, Any]:
    corridor = rng.choice(["roads, bridges, and commuter rail", "regional airports, harbours, and freight rail"])
    prompt = (
        f"In the National Budget, the **Transport** vote funds **{corridor}**, alongside the Road Accident Fund (RAF).\n\n"
        "Why is efficient transport expenditure essential for **both** commuters and businesses?"
    )
    correct = "Workers reach jobs safely and affordably while businesses move raw materials and finished exports efficiently with lower logistics costs."
    distractors = [
        "Transport spending applies only to private luxury yachts inside national parks.",
        "Harbours and bridges eliminate the need for any electricity or clean water.",
        "The Transport vote collects personal income tax directly at highway toll gates.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_22",
        subskill="22_transport_infrastructure_roads_rail_ports_raf",
        title="Transport Budget: Mobility, Logistics & Exports",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Investing in **{corridor}** links workers reliably to employment and enables factories, farms, and exporters to transport goods reliably."
        ),
        hints={
            "tier_1": "Ask how both employees and cargo move across a large country like South Africa.",
            "tier_2": "Connect commuter mobility for workers with freight/export efficiency for businesses.",
            "tier_3": correct,
        },
        misconception_tags=["separating_transport_spending_from_business_productivity"],
    )


def arch_23_safety_security_and_justice_budget_pillars(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    institutions = rng.choice(["SAPS police stations, local magistrates' courts, and correctional centres", "the South African Police Service (SAPS), SANDF, courts, and prisons"])
    prompt = (
        f"The National Budget allocates billions annually to **Safety, Security and Justice**, funding **{institutions}** serving **{area}** and the nation.\n\n"
        "Give **two economic reasons** (not just policing reasons) why funding Safety & Security is crucial for business investment and employment."
    )
    expected = (
        "1) Lower crime and protected property encourage local and foreign investors to open shops and factories (creating jobs); "
        "2) Courts enforce contracts and property rights fairly while public safety lowers business security/insurance costs."
    )
    sol = (
        f"**Economic Case for Safety, Security & Justice ({area}) [3 marks]:**\n\n"
        "1. **Investor Confidence & Jobs:** Low crime and peaceful borders encourage businesses to invest, expand branches, and employ more workers **[1.5]**.\n"
        "2. **Contract Enforcement & Lower Costs:** Independent courts protect legal agreements and lower theft/security costs for SMMEs **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_23",
        subskill="23_safety_security_and_justice_budget_pillars",
        title="Safety, Security & Justice: Economic Importance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Would a business build a new factory where crime is unchecked and courts fail to enforce contracts?",
            "tier_2": "Link security + justice to investor confidence, job creation, and lower business risk.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Builds investor confidence to expand businesses and jobs", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Courts protect property/contracts and reduce theft losses", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["viewing_security_spending_as_unrelated_to_economy"],
    )


def arch_24_budget_functional_expenditure_matching_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pairs = [
        (f"Recruiting additional nurses and stocking clinic medicine in {area}", "Health"),
        ("Providing monthly child-support and disability grants to vulnerable families", "Social Welfare"),
        ("Equipping SAPS patrol vehicles and funding regional courts", "Safety and Security"),
        ("Printing Grade 8 textbooks and paying public school teachers", "Education"),
        ("Upgrading national freight rail bridges and harbour cranes", "Transport"),
    ]
    chosen = rng.sample(pairs, 4)
    headers = ["Public Spending Need", "National Budget Sector (Education / Health / Social Welfare / Safety and Security / Transport)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Public Spending Need | National Budget Sector |", "| :--- | :--- |"]
    for idx, (need, sec) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", need, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = sec
        cell_hints[c1] = "Enter exact vote name: Education, Health, Social Welfare, Safety and Security, or Transport."
        memo_lines.append(f"| {need} | {sec} |")

    worked = "**Completed Expenditure Sector Matching [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{n} -> {s}" for n, s in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_bud_24",
        subskill="24_budget_functional_expenditure_matching_table",
        title="National Budget Expenditure Sector Audit",
        prompt="Match each real public need to the exact **National Budget expenditure category**: **Education**, **Health**, **Social Welfare**, **Safety and Security**, or **Transport**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Check whether each item funds clinics, grants, policing/courts, schools, or roads/ports.",
            "tier_2": "Use exact category names from the prompt list.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Correct sector row {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["mixing_social_welfare_grants_with_health_spending"],
    )


def arch_25_national_budget_sector_bar_chart_diagram(rng: random.Random) -> Dict[str, Any]:
    year = rng.choice([2025, 2026])
    edu = rng.choice([440, 480, 520])
    health = rng.choice([260, 280, 300])
    social = rng.choice([340, 360, 380])
    safety = rng.choice([220, 240, 250])
    total_4 = edu + health + social + safety
    diff_edu_safety = edu - safety

    max_v = max(edu, health, social, safety)
    h_edu = int(120 * edu / max_v)
    h_soc = int(120 * social / max_v)
    h_hea = int(120 * health / max_v)
    h_saf = int(120 * safety / max_v)

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="230" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{year} Budget Expenditure Extract (R billion)</text>'
        '<line x1="60" y1="180" x2="590" y2="180" stroke="#475569" stroke-width="2"/>'
        f'<rect x="95" y="{180 - h_edu}" width="75" height="{h_edu}" fill="#2563eb" rx="4"/>'
        f'<text x="132" y="{172 - h_edu}" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">R{edu} bn</text>'
        '<text x="132" y="198" text-anchor="middle" font-size="11" fill="#0f172a">Education</text>'
        f'<rect x="220" y="{180 - h_soc}" width="75" height="{h_soc}" fill="#16a34a" rx="4"/>'
        f'<text x="257" y="{172 - h_soc}" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">R{social} bn</text>'
        '<text x="257" y="198" text-anchor="middle" font-size="11" fill="#0f172a">Social Grants</text>'
        f'<rect x="345" y="{180 - h_hea}" width="75" height="{h_hea}" fill="#ea580c" rx="4"/>'
        f'<text x="382" y="{172 - h_hea}" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c2d12">R{health} bn</text>'
        '<text x="382" y="198" text-anchor="middle" font-size="11" fill="#0f172a">Health</text>'
        f'<rect x="470" y="{180 - h_saf}" width="75" height="{h_saf}" fill="#7c3aed" rx="4"/>'
        f'<text x="507" y="{172 - h_saf}" text-anchor="middle" font-size="11" font-weight="bold" fill="#4c1d95">R{safety} bn</text>'
        '<text x="507" y="198" text-anchor="middle" font-size="11" fill="#0f172a">Safety &amp; Justice</text>'
        '</svg>'
    )
    prompt = (
        f"Study the **{year}** National Budget expenditure bar chart showing planned spending across four key sectors "
        f"(Education R{edu} bn, Social Grants R{social} bn, Health R{health} bn, Safety & Justice R{safety} bn).\n\n"
        "(a) Calculate the **combined total spending** on all four sectors;\n"
        "(b) By how much does **Education** spending exceed **Safety & Justice** spending?"
    )
    expected = f"(a) Combined total = R{total_4} bn; (b) Education exceeds Safety & Justice by R{diff_edu_safety} bn"
    sol = (
        f"**Budget Bar Chart Analysis ({year}) [3 marks]:**\n\n"
        f"**(a) Combined Spending (4 sectors):**\n"
        f"$$R{edu}\\text{{ bn}} + R{social}\\text{{ bn}} + R{health}\\text{{ bn}} + R{safety}\\text{{ bn}} = R{total_4}\\text{{ bn}}$$ **[2]**\n\n"
        "**(b) Difference (Education minus Safety & Justice):**\n"
        f"$$R{edu}\\text{{ bn}} - R{safety}\\text{{ bn}} = R{diff_edu_safety}\\text{{ bn}}$$ **[1]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_25",
        subskill="25_national_budget_sector_bar_chart_diagram",
        title="Reading & Calculating Budget Expenditure Bar Charts",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Read all four bar values carefully from the chart.",
            "tier_2": "Sum all 4 bars for (a); subtract Safety & Justice from Education for (b).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Combined total = R{total_4} bn", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Education - Safety & Justice = R{diff_edu_safety} bn", "marks": 1, "editable": True},
        ],
        misconception_tags=["misreading_bar_chart_totals"],
        qtype="calculation",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25 = {
    "01_definition_and_purpose_of_national_budget": arch_01_definition_and_purpose_of_national_budget,
    "02_minister_of_finance_and_national_treasury_roles": arch_02_minister_of_finance_and_national_treasury_roles,
    "03_sars_tax_collection_and_fiscal_year_schedule": arch_03_sars_tax_collection_and_fiscal_year_schedule,
    "04_budget_revenue_vs_expenditure_sides": arch_04_budget_revenue_vs_expenditure_sides,
    "05_direct_tax_definition_and_incidence": arch_05_direct_tax_definition_and_incidence,
    "06_indirect_tax_definition_and_shifting": arch_06_indirect_tax_definition_and_shifting,
    "07_direct_vs_indirect_taxes_classification_table": arch_07_direct_vs_indirect_taxes_classification_table,
    "08_paye_personal_income_tax_bracket_calculation": arch_08_paye_personal_income_tax_bracket_calculation,
    "09_corporate_business_income_tax_calculation": arch_09_corporate_business_income_tax_calculation,
    "10_vat_15_percent_forward_calculation": arch_10_vat_15_percent_forward_calculation,
    "11_vat_15_percent_reverse_extraction": arch_11_vat_15_percent_reverse_extraction,
    "12_vat_zero_rated_basic_foodstuffs_equity": arch_12_vat_zero_rated_basic_foodstuffs_equity,
    "13_sin_tax_excise_purpose_and_price_impact": arch_13_sin_tax_excise_purpose_and_price_impact,
    "14_fuel_levy_and_road_accident_fund_mechanism": arch_14_fuel_levy_and_road_accident_fund_mechanism,
    "15_government_borrowing_bonds_and_interest_cost": arch_15_government_borrowing_bonds_and_interest_cost,
    "16_non_tax_revenue_fees_interest_donations": arch_16_non_tax_revenue_fees_interest_donations,
    "17_budget_deficit_vs_budget_surplus_calculation": arch_17_budget_deficit_vs_budget_surplus_calculation,
    "18_education_spending_allocation_and_growth_impact": arch_18_education_spending_allocation_and_growth_impact,
    "19_health_expenditure_free_child_and_clinic_care": arch_19_health_expenditure_free_child_and_clinic_care,
    "20_housing_expenditure_rdp_low_cost_settlements": arch_20_housing_expenditure_rdp_low_cost_settlements,
    "21_social_welfare_grants_and_hivaids_family_support": arch_21_social_welfare_grants_and_hivaids_family_support,
    "22_transport_infrastructure_roads_rail_ports_raf": arch_22_transport_infrastructure_roads_rail_ports_raf,
    "23_safety_security_and_justice_budget_pillars": arch_23_safety_security_and_justice_budget_pillars,
    "24_budget_functional_expenditure_matching_table": arch_24_budget_functional_expenditure_matching_table,
    "25_national_budget_sector_bar_chart_diagram": arch_25_national_budget_sector_bar_chart_diagram,
}
