"""Grade 9 EMS - Term 3 Functions of a Business: Archetypes 01 to 25.

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Functions of a business.md,
curriculum_docs/EMS_Gr9/Term 3/11-Functions of a Business.md, and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African business contexts.
"""
from __future__ import annotations

import html
import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario


def get_ems_scenario(rng: random.Random) -> Dict[str, Any]:
    d = dict(_raw_ems_scenario(rng))
    d["business"] = f"{d['entrepreneur']} {d['business_type']}"
    return d

TOPIC_NAME = "Functions of a business"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_business"
CURRICULUM_REF = "Term 3 > Entrepreneurship: Functions of a Business"


def _fmt_r(amount: int | float) -> str:
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _esc(text: str) -> str:
    return html.escape(str(text), quote=False)


def _make_cell(coord: str, value: str, cell_type: str = "given") -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "value": value,
        "type": cell_type,
        "editable": cell_type in ("required", "editable"),
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "concept_id": subskill,
        "concept_group": "business_functions",
        "learning_objective_id": f"lo_g9_bf_{subskill}",
        "curriculum_reference": CURRICULUM_REF,
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
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "hint_sections": {
            "1_nudge": hints.get("tier_1", ""),
            "2_concept": hints.get("tier_2", ""),
            "3_breakdown": hints.get("tier_3", ""),
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "business_functions", "south_africa"],
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "concept_id": subskill,
        "concept_group": "business_functions",
        "learning_objective_id": f"lo_g9_bf_{subskill}",
        "curriculum_reference": CURRICULUM_REF,
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
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "hint_sections": {
            "1_nudge": hints.get("tier_1", ""),
            "2_concept": hints.get("tier_2", ""),
            "3_breakdown": hints.get("tier_3", ""),
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "business_functions", "south_africa"],
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "concept_id": subskill,
        "concept_group": "business_functions",
        "learning_objective_id": f"lo_g9_bf_{subskill}",
        "curriculum_reference": CURRICULUM_REF,
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
        "expected_answer": sample_answer,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "hint_sections": {
            "1_nudge": hints.get("tier_1", ""),
            "2_concept": hints.get("tier_2", ""),
            "3_breakdown": hints.get("tier_3", ""),
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "business_functions", "classification_table", "south_africa"],
    }


def arch_01_business_function_definition_and_interdependence(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"As **{sc['business']}** expands in **{sc['area']}**, the owner separates tasks into specialised departments.\n\n"
        "Which statement **best** defines a **business function** and explains why all **eight functions** must work together?"
    )
    correct = "A specialised group of business activities contributing to a core objective; all eight functions depend on one another for information, resources, and overall success."
    distractors = [
        "A monthly public holiday event; each department operates in total secrecy without communicating.",
        "A government municipal tax levy collected solely from retail cashiers.",
        "A seasonal clearance sale handled strictly by external delivery couriers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_01",
        subskill="01_business_function_definition_and_interdependence",
        title="Definition & Interdependence of Business Functions",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"At **{sc['business']}**, a **business function** groups specialised tasks (such as Finance, Production, or HR); because Production needs Purchasing for materials and Finance for budgets, all eight are interdependent."
        ),
        hints={
            "tier_1": "Think of specialised departmental roles that depend on each other.",
            "tier_2": "A business function is a specific activity set working interdependently toward business goals.",
            "tier_3": correct,
        },
        misconception_tags=["viewing_business_departments_as_isolated_silos"],
    )


def arch_02_eight_business_functions_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Collecting, filing, storing, and sharing accurate office records", "Administration", "Information backbone"),
        ("Sourcing raw materials and trading stock at the best price and quality", "Purchasing", "Supply acquisition"),
        ("Acquiring capital, drafting budgets, and managing cash flow", "Financial", "Money & solvency management"),
        ("Recruiting, inducting, training, and looking after staff welfare", "Human Resources", "People management"),
        ("Converting raw inputs into finished goods under quality control", "Production", "Manufacturing & operations"),
        ("Conducting market research, pricing, promotion, and distribution", "Marketing", "Customer demand & sales"),
        ("Maintaining positive two-way goodwill with the public and media", "Public Relations", "Reputation & image"),
        ("Setting overall vision and planning, organising, leading, and controlling", "General Management", "Strategic leadership"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Business Activity", "Core Focus", "Business Function Name"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Business Activity | Core Focus | Business Function |", "| :--- | :--- | :--- |"]
    for idx, (act, fn_name, focus) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", act, "given"),
            _make_cell(f"t0_r{idx}_c1", focus, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = fn_name
        cell_hints[coord] = "Enter exact function: Administration, Purchasing, Marketing, Financial, Public Relations, Human Resources, Production, or General Management."
        memo_lines.append(f"| {act} | {focus} | {fn_name} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Eight Business Functions Classification ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bf_02",
        subskill="02_eight_business_functions_classification_table",
        title="Classifying the Eight Business Functions",
        prompt=(
            f"Match each operational activity at **{sc['business']}** in **{sc['area']}** to its exact **Business Function** in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Connect records -> Admin, money -> Financial, staff -> Human Resources, goods -> Production, goodwill -> PR.",
            "tier_2": "Use exact names: Administration, Purchasing, Marketing, Financial, Public Relations, Human Resources, Production, General Management.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Identifies {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_marketing_with_public_relations_or_purchasing"],
    )


def arch_03_general_management_polc_framework(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Senior executives at **{sc['business']}** in **{sc['area']}** oversee the **General Management** function using the four-part **POLC** cycle.\n\n"
        "What do the four management tasks in **POLC** stand for?"
    )
    correct = "Planning, Organising, Leading, and Controlling."
    distractors = [
        "Purchasing, Ordering, Lending, and Collecting.",
        "Packaging, Offloading, Labelling, and Consuming.",
        "Printing, Operating, Litigating, and Cancelling.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_03",
        subskill="03_general_management_polc_framework",
        title="General Management POLC Cycle",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "**General Management** coordinates all departments at **{0}** through **Planning** (setting goals), **Organising** (allocating resources), **Leading** (motivating staff), and **Controlling** (monitoring results against targets).".format(sc["business"])
        ),
        hints={
            "tier_1": "Think of the four pillars of management: setting plans, arranging teams, inspiring staff, checking results.",
            "tier_2": "P = Planning, O = Organising, L = Leading, C = Controlling.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_management_tasks_with_production_tasks"],
    )


def arch_04_three_levels_of_management_hierarchy_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    top_n = rng.choice([2, 3, 4])
    mid_n = rng.choice([6, 8, 10])
    low_n = rng.choice([14, 18, 22])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 245" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="245" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Management Levels at {_esc(sc["business"])} ({_esc(sc["area"])})</text>'
        '<polygon points="320,42 225,95 415,95" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="320" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">Top Management</text>'
        f'<text x="320" y="90" text-anchor="middle" font-size="9.5" fill="#1e40af">CEO / MD ({top_n})</text>'
        '<polygon points="225,98 415,98 475,152 165,152" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="320" y="122" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">Middle Management</text>'
        f'<text x="320" y="140" text-anchor="middle" font-size="10" fill="#92400e">Department Heads ({mid_n}) — Tactical Plans</text>'
        '<polygon points="165,155 475,155 540,212 100,212" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="320" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">Lower Management</text>'
        f'<text x="320" y="198" text-anchor="middle" font-size="10" fill="#166534">Supervisors / Foremen ({low_n}) — Daily Operations</text>'
        '</svg>'
    )
    prompt = (
        f"Study the management hierarchy pyramid for **{sc['business']}** in **{sc['area']}** showing **{top_n} Top**, **{mid_n} Middle**, and **{low_n} Lower** managers.\n\n"
        "Compare the **decision scope** of **Top Management** (strategic) with **Lower Management** (operational), giving **one** example decision for each level."
    )
    expected = (
        f"Top Management ({top_n} executives like CEO/MD) makes long-term strategic decisions affecting the whole business (e.g. expanding to another province); "
        f"Lower Management ({low_n} supervisors/foremen) makes short-term daily operational decisions (e.g. assigning daily shift rosters and checking machine safety)."
    )
    sol = (
        f"**Management Hierarchy at {sc['business']} [4 marks]:**\n\n"
        f"1. **Top Management ({top_n} executives):** Sets **long-term strategic vision and policies** for the entire enterprise (e.g., opening a new regional branch) **[2]**.\n"
        f"2. **Lower Management ({low_n} supervisors):** Oversees **daily short-term operational tasks** on the floor (e.g., supervising shift targets and daily stock counts) **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_04",
        subskill="04_three_levels_of_management_hierarchy_svg",
        title="Three Levels of Management Hierarchy",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Top = long-term whole company; Middle = departmental tactics; Lower = daily floor supervision.",
            "tier_2": "Give decision scope + one concrete example for Top and Lower Management.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Top management: long-term strategic company-wide decisions + example", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Lower management: daily operational / shift supervision + example", "marks": 2, "editable": True},
        ],
        misconception_tags=["confusing_strategic_top_decisions_with_daily_supervision"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_05_planning_and_organising_in_general_management(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    target_rev = rng.choice([450000, 600000, 750000])
    prompt = (
        f"**{sc['entrepreneur']}** aims to reach **{_fmt_r(target_rev)}** in quarterly turnover at **{sc['business']}** in **{sc['area']}**.\n\n"
        "Distinguish clearly between **Planning** and **Organising** as management tasks to achieve this target."
    )
    expected = (
        f"Planning decides in advance WHAT goals to achieve ({_fmt_r(target_rev)}) and HOW to reach them; "
        "Organising arranges and allocates people, capital, tasks, and resources into structured roles so the plan can be executed."
    )
    sol = (
        f"**Planning vs Organising at {sc['business']} [4 marks]:**\n\n"
        f"1. **Planning:** Formulating goals (reaching **{_fmt_r(target_rev)}**), forecasting needs, and choosing action steps beforehand **[2]**.\n"
        "2. **Organising:** Dividing work into departments, delegating authority, and allocating staff, machinery, and budgets efficiently **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_05",
        subskill="05_planning_and_organising_in_general_management",
        title="General Management: Planning vs Organising",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Planning happens first (goals & strategy); Organising arranges staff and resources next.",
            "tier_2": "Planning = deciding goals/steps; Organising = assigning people, tasks & resources.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Planning: setting goals and action steps in advance", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Organising: allocating staff, roles, and resources", "marks": 2, "editable": True},
        ],
        misconception_tags=["treating_planning_and_organising_as_identical"],
    )


def arch_06_leading_and_controlling_in_general_management(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    target_units = rng.choice([1200, 1500, 1800])
    actual_units = target_units - rng.choice([180, 240])
    prompt = (
        f"At **{sc['business']}** in **{sc['area']}**, monthly output was planned at **{target_units} units**, but actual production reached **{actual_units} units**.\n\n"
        "1. Which POLC management task compares **{actual_units}** against **{target_units}** and corrects the shortfall?\n"
        "2. Explain how **Leading** helps staff close that output gap without lowering morale."
    )
    expected = (
        f"1. Controlling (comparing {actual_units} vs {target_units} and taking corrective action). "
        "2. Leading motivates, guides, and communicates clearly with workers so they feel valued and inspired to lift output."
    )
    sol = (
        f"**Leading & Controlling ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Controlling:** Measures actual output (**{actual_units}**) against the standard (**{target_units}**), identifies causes of the **{target_units - actual_units}-unit** variance, and applies corrective steps **[2]**.\n"
        "2. **Leading:** Motivates staff through clear direction, supportive feedback, teamwork, and recognition to boost commitment **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_06",
        subskill="06_leading_and_controlling_in_general_management",
        title="General Management: Leading & Controlling",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Checking numbers against targets is Control; inspiring people is Leading.",
            "tier_2": "1. Controlling (measure vs standard + correct); 2. Leading (motivate, guide, communicate).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Controlling: comparing actual vs target & correcting", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Leading: motivating, directing, and communicating with staff", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_controlling_purely_as_punishment"],
    )


def arch_07_administration_function_information_lifecycle(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Every morning at **{sc['business']}** in **{sc['area']}**, office staff receive supplier invoices, capture sales orders, and file contracts.\n\n"
        "What is the **primary responsibility** of the **Administration function**?"
    )
    correct = "To collect, process, store, retrieve, and distribute reliable internal and external business information so every department can operate smoothly."
    distractors = [
        "To borrow long-term expansion capital from commercial investment banks.",
        "To design billboard campaigns and discount coupons for retail shoppers.",
        "To weld steel components on the manufacturing assembly line.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_07",
        subskill="07_administration_function_information_lifecycle",
        title="Administration Function & Information Handling",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The **Administration function** handles data capture, filing, clerical correspondence, and digital record systems so managers at **{sc['business']}** always have accurate facts."
        ),
        hints={
            "tier_1": "Think about paperwork, digital databases, and accurate records.",
            "tier_2": "Administration manages the collection, processing, filing, and distribution of information.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_administration_with_finance_or_hr"],
    )


def arch_08_administration_importance_for_decision_making(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Why would poor filing or lost electronic records inside **{sc['business']}**'s **Administration department** cripple other functions in **{sc['area']}**?\n\n"
        "Give **two** specific consequences of administrative disorganisation for other departments."
    )
    expected = (
        "1. Finance cannot verify invoices, chase overdue debtors, or file accurate VAT/SARS returns; "
        "2. General Management makes flawed decisions using outdated sales or stock figures (and legal POPIA compliance risks arise)."
    )
    sol = (
        f"**Importance of Administration ({sc['business']}) [4 marks]:**\n\n"
        "1. **Financial & Tax Delays:** Missing invoices/receipts prevent Finance from paying suppliers on time, collecting debts, or submitting accurate **SARS tax returns** **[2]**.\n"
        "2. **Weak Decisions & POPIA Risk:** Managers lack reliable stock/customer metrics, while sloppy record storage risks breaching **POPIA** privacy laws **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_08",
        subskill="08_administration_importance_for_decision_making",
        title="Why Effective Administration Matters",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Consider what Finance, Purchasing, and Management do when paperwork goes missing.",
            "tier_2": "Mention broken billing/tax compliance and poor management decisions / POPIA breaches.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Disrupts billing, supplier payments, or SARS tax records", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Flawed management decisions or POPIA data privacy risk", "marks": 2, "editable": True},
        ],
        misconception_tags=["treating_administration_as_unimportant_paperwork"],
    )


def arch_09_purchasing_function_right_inputs_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    supplier = rng.choice(SUPPLIERS)
    prompt = (
        f"The **Purchasing department** at **{sc['business']}** places recurring inventory orders with **{supplier}**.\n\n"
        "Which combination summarises the **five rights** of an effective **Purchasing function**?"
    )
    correct = "Buying the right quality, in the right quantity, at the right time, at the right price, from the right reliable supplier."
    distractors = [
        "Always choosing the cheapest unverified item regardless of quality or delivery delays.",
        "Selling finished products directly to retail walk-in shoppers at clearance prices.",
        "Printing quarterly balance sheets without verifying stock levels.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_09",
        subskill="09_purchasing_function_right_inputs_definition",
        title="Purchasing Function: The Five Rights",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Ordering from **{supplier}** successfully requires balancing **right quality**, **quantity**, **time**, **price**, and **supplier** — not simply buying the cheapest defective batch."
        ),
        hints={
            "tier_1": "Purchasing balances quality, quantity, delivery timing, cost, and supplier reliability.",
            "tier_2": "Five rights: right quality, quantity, time, price, and supplier.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_purchasing_only_means_finding_lowest_price"],
    )


def arch_10_purchasing_cash_vs_credit_buying_and_stock_control(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    supplier = rng.choice(SUPPLIERS)
    order_val = rng.choice([45000, 62000, 80000])
    prompt = (
        f"**{sc['business']}** needs **{_fmt_r(order_val)}** of raw materials from **{supplier}** in **{sc['area']}**.\n\n"
        "1. State **one** advantage for **{sc['business']}** of buying from **{supplier}** on **30-day credit** instead of paying cash upfront.\n"
        "2. Explain **one** danger of holding **excessively high stock** (overstocking) in the storeroom."
    )
    expected = (
        f"1. Buying on credit lets {sc['business']} keep cash on hand and sell finished goods before paying {supplier}. "
        "2. Overstocking ties up working capital, raises storage/insurance costs, and risks stock going stale, obsolete, or stolen."
    )
    sol = (
        f"**Purchasing Terms & Stock Control ({_fmt_r(order_val)}) [4 marks]:**\n\n"
        f"1. **Credit Buying Advantage:** Improves short-term cash flow because **{sc['business']}** can manufacture and sell stock to customers before the **{_fmt_r(order_val)}** invoice falls due **[2]**.\n"
        "2. **Danger of Overstocking:** Ties up cash (working capital), increases warehouse rent/insurance, and risks expiry, damage, or theft **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_10",
        subskill="10_purchasing_cash_vs_credit_buying_and_stock_control",
        title="Credit Purchasing & Stock Control Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Think of cash flow timing on 30-day terms, and storage costs/spoilage on excess stock.",
            "tier_2": "1. Preserves cash until sales occur; 2. Ties up cash / storage costs / spoilage or obsolescence.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Preserves working capital / sell before paying supplier", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Overstocking ties up cash, storage cost, spoilage/obsolescence", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_more_inventory_is_always_better"],
    )


def arch_11_production_function_input_process_output_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    raw_kg = rng.choice([250, 400, 500])
    out_units = rng.choice([800, 1200, 1600])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 215" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="215" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Production System: {_esc(sc["business"])} ({_esc(sc["area"])})</text>'
        '<rect x="24" y="55" width="165" height="90" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="106" y="83" text-anchor="middle" font-size="12" font-weight="bold" fill="#78350f">1. INPUTS</text>'
        f'<text x="106" y="104" text-anchor="middle" font-size="10.5" fill="#92400e">{raw_kg} kg Raw Material</text>'
        '<text x="106" y="121" text-anchor="middle" font-size="10.5" fill="#92400e">Labour, Power, Machines</text>'
        '<line x1="189" y1="100" x2="232" y2="100" stroke="#334155" stroke-width="2"/>'
        '<polygon points="232,95 242,100 232,105" fill="#334155"/>'
        '<rect x="242" y="55" width="190" height="90" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="337" y="83" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">2. TRANSFORMATION</text>'
        '<text x="337" y="104" text-anchor="middle" font-size="10.5" fill="#1e40af">Blending, Shaping &amp; Baking</text>'
        '<text x="337" y="121" text-anchor="middle" font-size="10.5" fill="#1e40af">SABS / Quality Inspection</text>'
        '<line x1="432" y1="100" x2="475" y2="100" stroke="#334155" stroke-width="2"/>'
        '<polygon points="475,95 485,100 475,105" fill="#334155"/>'
        '<rect x="485" y="55" width="170" height="90" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="570" y="83" text-anchor="middle" font-size="12" font-weight="bold" fill="#14532d">3. OUTPUTS</text>'
        f'<text x="570" y="104" text-anchor="middle" font-size="10.5" fill="#166534">{out_units} Finished Units</text>'
        '<text x="570" y="121" text-anchor="middle" font-size="10.5" fill="#166534">Packaged for Sale</text>'
        '<text x="340" y="182" text-anchor="middle" font-size="11" fill="#475569">Quality control checks at every stage prevent defective goods from reaching customers.</text>'
        '</svg>'
    )
    prompt = (
        f"Examine the Production workflow diagram for **{sc['business']}** converting **{raw_kg} kg** of raw material into **{out_units} finished units**.\n\n"
        "1. Describe what happens in the **Transformation** stage.\n"
        "2. Why does the **Production function** run **quality control** inspections during processing rather than only after delivery?"
    )
    expected = (
        f"1. Raw materials ({raw_kg} kg), labour, energy, and machinery combine through shaping/assembly to add value and create {out_units} finished goods. "
        "2. Early quality control catches defects before wasted materials accumulate, lowering scrap costs and protecting brand trust."
    )
    sol = (
        f"**Production Workflow ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Transformation Stage:** Combines raw inputs (**{raw_kg} kg**), factory labour, electricity, and machinery to add value into **{out_units} finished units** **[2]**.\n"
        "2. **In-Process Quality Control:** Stops faulty units early before extra labour/packaging is wasted, cutting rework costs and preventing customer recalls **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_11",
        subskill="11_production_function_input_process_output_svg",
        title="Production Input-Process-Output Workflow",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Read Stage 2 and the footer note on quality inspections.",
            "tier_2": "Transformation = combining inputs via labour/machinery to add value; QC cuts waste & protects reputation.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Combines inputs (raw materials, labour, machines) to create finished outputs", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Quality control stops defects early, reducing waste and customer returns", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_quality_control_from_production_role"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_12_production_quality_control_and_unit_cost_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    units = rng.choice([400, 500, 800])
    mat_cost = rng.choice([12000, 16000, 20000])
    labour_cost = rng.choice([8000, 10000, 12000])
    overhead = rng.choice([4000, 6000, 8000])
    total_cost = mat_cost + labour_cost + overhead
    unit_cost = total_cost / units
    prompt = (
        f"The Production manager at **{sc['business']}** in **{sc['area']}** records these weekly manufacturing costs to produce **{units} units**:\n"
        f"- Raw materials: **{_fmt_r(mat_cost)}**\n"
        f"- Direct factory labour: **{_fmt_r(labour_cost)}**\n"
        f"- Factory overheads (electricity & maintenance): **{_fmt_r(overhead)}**\n\n"
        "Calculate the **total production cost** and the **production cost per unit**."
    )
    expected = f"Total production cost = {_fmt_r(total_cost)}; Production cost per unit = {_fmt_r(unit_cost)}."
    sol = (
        f"**Weekly Production Costing ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Total Production Cost:** ${_fmt_r(mat_cost)} + {_fmt_r(labour_cost)} + {_fmt_r(overhead)} = {_fmt_r(total_cost)}$ **[2]**\n"
        f"2. **Unit Production Cost:** $\\frac{{{_fmt_r(total_cost)}}}{{{units}}} = {_fmt_r(unit_cost)}$ per unit **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_12",
        subskill="12_production_quality_control_and_unit_cost_calc",
        title="Calculating Total & Unit Production Cost",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Add materials + direct labour + factory overheads, then divide by units produced.",
            "tier_2": f"Total = {_fmt_r(total_cost)}; divide by {units} units.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total production cost {_fmt_r(total_cost)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Unit cost {_fmt_r(unit_cost)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_factory_overheads_from_unit_production_cost"],
    )


def arch_13_marketing_function_four_ps_overview(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** launches a new consumer line in **{sc['area']}** and needs the **Marketing function** to drive sustainable sales.\n\n"
        "What are the core elements of the **Marketing Mix (4 Ps)** managed by Marketing?"
    )
    correct = "Product, Price, Place (distribution), and Promotion (advertising/selling)."
    distractors = [
        "Payroll, Purchasing, Production, and Petty Cash.",
        "Planning, Policing, Printing, and Patenting.",
        "Profit, Property, Procurement, and Packaging only.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_13",
        subskill="13_marketing_function_four_ps_overview",
        title="Marketing Function & The 4 Ps",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"At **{sc['business']}**, Marketing identifies customer needs via research and combines **Product**, **Price**, **Place**, and **Promotion** so goods reach buyers profitably."
        ),
        hints={
            "tier_1": "Remember the four P words connecting goods, value, location, and persuasion.",
            "tier_2": "Product, Price, Place, and Promotion.",
            "tier_3": correct,
        },
        misconception_tags=["equating_marketing_solely_with_advertising"],
    )


def arch_14_marketing_mix_four_ps_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    items = [
        ("Offering eco-friendly refillable packaging with a 2-year warranty", "Product", "Features & quality"),
        ("Setting an introductory launch discount below competitor prices", "Price", "Pricing strategy"),
        ("Distributing through township spaza shops and an online store", "Place", "Distribution channel"),
        ("Running local community radio adverts and sampling stalls", "Promotion", "Customer communication"),
    ]
    rng.shuffle(items)
    headers = ["Marketing Decision at Business", "Focus", "Marketing Mix Element (Product / Price / Place / Promotion)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Marketing Decision | Focus | 4 Ps Element |", "| :--- | :--- | :--- |"]
    for idx, (dec, el, foc) in enumerate(items):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", dec, "given"),
            _make_cell(f"t0_r{idx}_c1", foc, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = el
        cell_hints[coord] = "Enter exact P: Product, Price, Place, or Promotion."
        memo_lines.append(f"| {dec} | {foc} | {el} |")

    sample = "; ".join(f"{i+1}: {items[i][1]}" for i in range(4))
    worked = f"**Marketing Mix (4 Ps) Schedule for {sc['business']} [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bf_14",
        subskill="14_marketing_mix_four_ps_classification_table",
        title="Marketing Mix (4 Ps) Application Matrix",
        prompt=(
            f"Classify four marketing actions taken by **{sc['business']}** in **{sc['area']}** into **Product**, **Price**, **Place**, or **Promotion**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Match item/design -> Product, Rand value -> Price, outlets/delivery -> Place, ads/samples -> Promotion.",
            "tier_2": "Use exact terms: Product, Price, Place, Promotion.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Classifies {items[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_place_distribution_with_promotion"],
    )


def arch_15_financial_function_capital_budgeting_and_cash_flow(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Before opening a second branch in **{sc['area']}**, managers at **{sc['business']}** consult the **Financial function**.\n\n"
        "Which set of duties belongs strictly to the **Financial function**?"
    )
    correct = "Raising own or borrowed capital, preparing cash budgets, investing surplus funds wisely, and tracking solvency and profitability."
    distractors = [
        "Interviewing factory welders and drafting workplace shift rosters.",
        "Hosting community fun runs and issuing press releases to local newspapers.",
        "Transporting perishable fruit from farms to supermarket shelves.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_15",
        subskill="15_financial_function_capital_budgeting_and_cash_flow",
        title="Core Duties of the Financial Function",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The **Financial function** secures start-up and expansion capital, draws up budgets, controls cash flow, and reports profit/loss statements for **{sc['business']}**."
        ),
        hints={
            "tier_1": "Look for money sourcing, budgets, investments, and financial statements.",
            "tier_2": "Finance manages capital raising, budgeting, cash flow, and solvency.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_financial_function_with_general_admin_or_marketing"],
    )


def arch_16_financial_own_vs_borrowed_capital_comparison(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    own_cap = rng.choice([120000, 180000, 240000])
    loan_cap = rng.choice([80000, 100000, 150000])
    prompt = (
        f"To launch **{sc['business']}** in **{sc['area']}**, **{sc['entrepreneur']}** invests **{_fmt_r(own_cap)}** from personal savings (**own capital**) "
        f"and takes a **{_fmt_r(loan_cap)}** bank loan (**borrowed capital**).\n\n"
        "Compare **own capital** and **borrowed capital** on **repayment obligation** and **cost (interest vs profit sharing)**."
    )
    expected = (
        f"Own capital ({_fmt_r(own_cap)}) carries no mandatory repayment date and no fixed interest expense (owners earn profit/dividends if successful). "
        f"Borrowed capital ({_fmt_r(loan_cap)}) must be repaid on agreed dates together with fixed interest regardless of profit."
    )
    sol = (
        f"**Own vs Borrowed Capital ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Own Capital ({_fmt_r(own_cap)}):** Permanent owner investment with **no mandatory repayment deadline** and **no interest cost**; return depends on net profits **[2]**.\n"
        f"2. **Borrowed Capital ({_fmt_r(loan_cap)}):** Must be **repaid to lenders on schedule** along with contractual **interest**, even during low-profit months **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_16",
        subskill="16_financial_own_vs_borrowed_capital_comparison",
        title="Own Capital vs Borrowed Capital",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Think: Who gets paid interest even if the firm has a slow month?",
            "tier_2": "Own = no repayment/no interest; Borrowed = fixed repayment + mandatory interest.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Own capital: no fixed repayment or interest obligation", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Borrowed capital: mandatory repayment plus contractual interest", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_bank_loans_only_require_interest_if_profitable"],
    )


def arch_17_human_resources_function_recruitment_to_retention(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** needs skilled technicians who stay loyal long-term.\n\n"
        "Which responsibilities sit within the **Human Resources (HR) function**?"
    )
    correct = "Workforce planning, recruiting, interviewing, inducting new staff, arranging training, managing leave/payroll benefits, and ensuring fair labour compliance."
    distractors = [
        "Evaluating competing wholesale fabric suppliers for seasonal discounts.",
        "Adjusting factory machine temperatures and packaging labels.",
        "Authorising bank overdrafts for municipal property tax payments.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_17",
        subskill="17_human_resources_function_recruitment_to_retention",
        title="Human Resources Lifecycle Functions",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The **Human Resources** department manages the full employee lifecycle at **{sc['business']}** — attracting, onboarding, training, motivating, and retaining productive staff."
        ),
        hints={
            "tier_1": "HR deals with people from recruitment through training and workplace welfare.",
            "tier_2": "Recruitment, selection, induction, training, benefits, and labour compliance.",
            "tier_3": correct,
        },
        misconception_tags=["limiting_hr_strictly_to_firing_staff"],
    )


def arch_18_human_resources_sa_labour_legislation_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    laws = [
        ("Sets maximum ordinary working hours (45h/week), overtime, and annual/sick leave", "BCEA", "Basic Conditions of Employment Act"),
        ("Eliminates unfair workplace discrimination and promotes equal opportunity", "EEA", "Employment Equity Act"),
        ("Governs union recognition, collective bargaining, and CCMA dispute steps", "LRA", "Labour Relations Act"),
        ("Funds workplace upskilling and SETA learnerships via a 1% payroll levy", "SDA", "Skills Development Act"),
    ]
    rng.shuffle(laws)
    headers = ["HR Compliance Focus", "Full Statute Name", "Law Acronym (BCEA / EEA / LRA / SDA)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| HR Compliance Focus | Full Statute Name | Acronym |", "| :--- | :--- | :--- |"]
    for idx, (focus, acr, full) in enumerate(laws):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", focus, "given"),
            _make_cell(f"t0_r{idx}_c1", full, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = acr
        cell_hints[coord] = "Enter exact acronym: BCEA, EEA, LRA, or SDA."
        memo_lines.append(f"| {focus} | {full} | {acr} |")

    sample = "; ".join(f"{i+1}: {laws[i][1]}" for i in range(4))
    worked = f"**South African HR Legislation Compliance ({area}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bf_18",
        subskill="18_human_resources_sa_labour_legislation_table",
        title="HR Compliance: Key South African Labour Laws",
        prompt=(
            f"An HR officer in **{area}** prepares a compliance checklist.\n\n"
            "Enter the exact acronym (**BCEA**, **EEA**, **LRA**, or **SDA**) in Column 3 for each statute."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Use the initials of each full statute listed in Column 2.",
            "tier_2": "BCEA (hours/leave), EEA (equity), LRA (unions/CCMA), SDA (training).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Matches {laws[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_bcea_working_hours_with_lra_union_rules"],
    )


def arch_19_public_relations_function_vs_advertising(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** sponsors a local youth literacy drive while also paying for weekly social-media product adverts.\n\n"
        "How does the **Public Relations (PR)** function differ from **Marketing advertising**?"
    )
    correct = "PR builds long-term public goodwill, stakeholder trust, and a positive brand image, whereas advertising pays to persuade buyers to purchase specific products or services."
    distractors = [
        "PR focuses strictly on cutting raw material transport expenses while advertising hires engineers.",
        "PR only communicates internally with payroll accountants whereas advertising handles bank loans.",
        "PR sets wholesale unit costs while advertising operates factory boilers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_19",
        subskill="19_public_relations_function_vs_advertising",
        title="Public Relations (PR) vs Paid Advertising",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Public Relations** manages **{sc['business']}**'s reputation with customers, media, and communities (two-way goodwill), whereas **advertising** is paid product promotion under Marketing."
        ),
        hints={
            "tier_1": "Separate overall company reputation/goodwill from direct product sales messages.",
            "tier_2": "PR builds long-term goodwill and trust; advertising sells specific offerings.",
            "tier_3": correct,
        },
        misconception_tags=["treating_public_relations_and_paid_advertising_as_identical"],
    )


def arch_20_publicity_crisis_communication_and_csr(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cause = rng.choice(["a school bursary fund", "river-bank clean-up volunteers", "community sports kits"])
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** supports **{cause}** as part of Corporate Social Responsibility (CSR), and handles media questions after a delivery truck breakdown.\n\n"
        "1. Define **publicity** in business.\n"
        "2. Explain **one** positive effect of CSR on public perception and **one** step PR must take when **negative publicity** hits."
    )
    expected = (
        "1. Publicity is free media/public information shared about a business (unlike paid ads, management cannot fully control it). "
        "2. CSR builds community loyalty/goodwill; during negative publicity, PR must respond promptly, honestly, and outline corrective action."
    )
    sol = (
        f"**Publicity & CSR ({sc['business']}) [4 marks]:**\n\n"
        "1. **Publicity:** Unpaid news, social posts, or word-of-mouth exposure about a business that can be either positive or negative **[1]**.\n"
        f"2. **CSR Goodwill:** Supporting **{cause}** demonstrates social care, strengthening customer loyalty and trust **[1]**.\n"
        "3. **Negative Publicity Response:** Communicate **promptly and transparently**, apologise if at fault, and announce concrete steps fixing the issue **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_20",
        subskill="20_publicity_crisis_communication_and_csr",
        title="Publicity, CSR & PR Crisis Handling",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Publicity is free media attention (unlike paid adverts); transparency restores trust.",
            "tier_2": "Define unpaid publicity + CSR goodwill benefit + honest rapid crisis response.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Defines publicity as unpaid media/public exposure", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "CSR builds goodwill and community loyalty", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Prompt, transparent communication + corrective action", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_silence_eliminates_negative_publicity"],
    )


def arch_21_purchasing_vs_production_vs_marketing_handoff(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prod = rng.choice(["leather school satchels", "organic fruit juice bottles", "wooden classroom desks"])
    prompt = (
        f"Follow the operational chain at **{sc['business']}** as it creates and sells **{prod}** in **{sc['area']}**.\n\n"
        "Which sequence accurately traces the core operational handoff across **Purchasing**, **Production**, and **Marketing**?"
    )
    correct = "Purchasing sources quality raw materials -> Production transforms inputs into finished products -> Marketing promotes, prices, and distributes them to customers."
    distractors = [
        "Marketing mines raw materials -> Purchasing advertises to shoppers -> Production approves bank loans.",
        "Production pays SARS payroll taxes -> Marketing hires machinists -> Purchasing files tax audits.",
        "Purchasing manufactures goods -> Marketing repairs conveyor belts -> Production delivers press releases.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_21",
        subskill="21_purchasing_vs_production_vs_marketing_handoff",
        title="Supply Chain Handoff: Purchasing -> Production -> Marketing",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Before **{sc['business']}** can sell **{prod}**, **Purchasing** acquires materials, **Production** manufactures the finished item, and **Marketing** delivers it to buyers."
        ),
        hints={
            "tier_1": "Trace an item from supplier delivery, through the factory, out to paying shoppers.",
            "tier_2": "Buy inputs (Purchasing) -> Make item (Production) -> Sell/deliver (Marketing).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_purchasing_buying_with_marketing_selling"],
    )


def arch_22_admin_and_finance_record_keeping_link(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Explain how the **Administration function** and the **Financial function** depend closely on each other at **{sc['business']}** in **{sc['area']}**.\n\n"
        "Give **two** specific examples of documents or tasks linking Administration directly to Finance."
    )
    expected = (
        "1. Administration captures, files, and verifies source documents (invoices, receipts, EFT proofs, credit notes) that Finance needs for journals and ledgers; "
        "2. Administration maintains employee attendance/time-sheets and VAT records used by Finance to run payroll and pay SARS accurately."
    )
    sol = (
        f"**Admin & Finance Synergy ({sc['business']}) [4 marks]:**\n\n"
        "1. **Source Documents for Accounting:** Administration receives, checks, and files invoices, bank deposit slips, and customer statements so **Finance** can record accurate ledger balances **[2]**.\n"
        "2. **Payroll & Statutory Filings:** Accurate attendance logs and tax documentation organised by Administration enable **Finance** to pay staff and **SARS VAT/PAYE** on schedule **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_22",
        subskill="22_admin_and_finance_record_keeping_link",
        title="Link Between Administration & Financial Functions",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Finance relies on clean paperwork from Admin to prepare ledgers, budgets, and tax filings.",
            "tier_2": "Give two examples: invoices/receipts for ledgers and timesheets/tax records for payroll & SARS.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Admin captures/files invoices & receipts used in Financial ledgers", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Admin organizes timesheets / tax records for payroll & SARS compliance", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_finance_operates_without_administrative_records"],
    )


def arch_23_management_span_of_control_and_delegation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    staff = rng.choice([18, 25, 32])
    prompt = (
        f"As **{sc['business']}** grows to **{staff} staff** in **{sc['area']}**, the owner can no longer supervise every invoice and delivery alone, so **delegation** begins.\n\n"
        "What happens to a manager's **accountability** when a task is delegated to a supervisor?"
    )
    correct = "The supervisor receives authority to execute the task, while the manager still retains ultimate accountability for the outcome."
    distractors = [
        "The manager permanently escapes all responsibility if the department fails.",
        "Employees no longer receive monthly wages once a duty is delegated.",
        "Only external customers decide who gets promoted in the department.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bf_23",
        subskill="23_management_span_of_control_and_delegation",
        title="Delegation, Authority & Accountability",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Effective managers at **{sc['business']}** delegate **tasks and authority** to free time for strategy across **{staff}** staff, yet remain **accountable** for final results."
        ),
        hints={
            "tier_1": "You can hand over authority to do a task, but can a boss wash their hands of final results?",
            "tier_2": "Authority is delegated down; ultimate accountability remains with the manager.",
            "tier_3": correct,
        },
        misconception_tags=["believing_delegation_removes_manager_accountability"],
    )


def arch_24_eight_functions_organisational_ecosystem_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    staff_total = rng.choice([48, 64, 80])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 265" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="265" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{_esc(sc["business"])} ({staff_total} Staff): 8-Function Ecosystem</text>'
        '<line x1="340" y1="138" x2="105" y2="68" stroke="#64748b" stroke-width="1.8"/>'
        '<line x1="340" y1="138" x2="265" y2="68" stroke="#64748b" stroke-width="1.8"/>'
        '<line x1="340" y1="138" x2="415" y2="68" stroke="#64748b" stroke-width="1.8"/>'
        '<line x1="340" y1="138" x2="575" y2="68" stroke="#64748b" stroke-width="1.8"/>'
        '<line x1="340" y1="138" x2="135" y2="215" stroke="#64748b" stroke-width="1.8"/>'
        '<line x1="340" y1="138" x2="340" y2="215" stroke="#64748b" stroke-width="1.8"/>'
        '<line x1="340" y1="138" x2="545" y2="215" stroke="#64748b" stroke-width="1.8"/>'
        '<rect x="242" y="114" width="196" height="48" rx="8" fill="#1e3a8a" stroke="#1d4ed8" stroke-width="2"/>'
        '<text x="340" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">General Management</text>'
        '<text x="340" y="151" text-anchor="middle" font-size="10" fill="#dbeafe">Strategic Hub (POLC)</text>'
        '<rect x="35" y="42" width="140" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        '<text x="105" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">Purchasing</text>'
        '<rect x="195" y="42" width="140" height="44" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="265" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">Production</text>'
        '<rect x="345" y="42" width="140" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        '<text x="415" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">Marketing</text>'
        '<rect x="505" y="42" width="140" height="44" rx="6" fill="#fae8ff" stroke="#a21caf" stroke-width="1.5"/>'
        '<text x="575" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#701a75">Public Relations</text>'
        '<rect x="65" y="192" width="145" height="44" rx="6" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.5"/>'
        '<text x="137" y="218" text-anchor="middle" font-size="11" font-weight="bold" fill="#312e81">Administration</text>'
        '<rect x="268" y="192" width="145" height="44" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>'
        '<text x="340" y="218" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">Financial</text>'
        '<rect x="472" y="192" width="145" height="44" rx="6" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5"/>'
        '<text x="544" y="218" text-anchor="middle" font-size="11" font-weight="bold" fill="#134e4a">Human Resources</text>'
        '</svg>'
    )
    prompt = (
        f"Study the organisational ecosystem diagram for **{sc['business']}** (**{staff_total} staff**) placing **General Management** at the hub of the other seven functions.\n\n"
        f"1. Why is **General Management** shown connecting all seven specialist functions in **{sc['area']}**?\n"
        "2. Trace how a decision to launch a new eco-product requires **four** different functions shown in the diagram to cooperate."
    )
    expected = (
        f"1. General Management coordinates, aligns goals, and controls budgets/workflows across all departments at {sc['business']}. "
        "2. Finance funds the budget -> Purchasing sources eco-materials -> Production manufactures the line -> Marketing promotes & sells it (with HR training and Admin tracking orders)."
    )
    sol = (
        f"**8-Function Coordination ({sc['business']}, {staff_total} staff) [5 marks]:**\n\n"
        "1. **Central Coordination:** **General Management** sets overarching goals and ensures every specialist department works in sync rather than at cross-purposes **[2]**.\n"
        "2. **Four-Function Cooperation Example:** **Financial** allocates launch funds; **Purchasing** buys sustainable materials; **Production** manufactures safe goods; **Marketing** promotes and distributes to buyers (supported by **HR**, **Admin**, and **PR**) **[3]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_24",
        subskill="24_eight_functions_organisational_ecosystem_svg",
        title="Eight-Function Organisational Ecosystem",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=5,
        hints={
            "tier_1": "Look at how General Management sits at the centre linking every box.",
            "tier_2": "Explain central coordination plus concrete duties from 4 named specialist functions.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "General Management coordinates goals across all departments", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Accurate linked actions across 4 named specialist functions", "marks": 3, "editable": True},
        ],
        misconception_tags=["viewing_general_management_as_unrelated_to_specialist_units"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_25_ntuli_beauty_style_scenario_function_identification(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(NAMES)
    area = rng.choice(AREAS)
    biz = f"{founder} Care Solutions"
    prompt = (
        f"**{biz}** in **{area}** manufactures natural skincare products and faces three urgent tasks:\n"
        "- Task A: Secure a **R150 000** commercial loan and tighten overdue debtor collections.\n"
        "- Task B: Appoint **three** qualified sales representatives and run labour-law induction.\n"
        "- Task C: Negotiate reliable glass-jar bulk deliveries from a KwaZulu-Natal supplier.\n\n"
        "Name the **exact business function** responsible for **Task A**, **Task B**, and **Task C**."
    )
    expected = "Task A: Financial function; Task B: Human Resources function; Task C: Purchasing function."
    sol = (
        f"**Scenario Function Matching ({biz}) [3 marks]:**\n\n"
        "- **Task A (loan & debtor cash collections):** **Financial function** **[1]**.\n"
        "- **Task B (hiring reps & induction):** **Human Resources function** **[1]**.\n"
        "- **Task C (glass-jar supplier bulk order):** **Purchasing function** **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bf_25",
        subskill="25_ntuli_beauty_style_scenario_function_identification",
        title="Case Scenario: Matching Operational Tasks to Functions",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Loan/cash = money; hiring/induction = people; jar supplier = buying inputs.",
            "tier_2": "Financial (A), Human Resources (B), Purchasing (C).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Task A: Financial", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Task B: Human Resources", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Task C: Purchasing", "marks": 1, "editable": True},
        ],
        misconception_tags=["confusing_purchasing_inputs_with_marketing_sales"],
    )


BUILDERS_01_25 = {
    "01_business_function_definition_and_interdependence": arch_01_business_function_definition_and_interdependence,
    "02_eight_business_functions_classification_table": arch_02_eight_business_functions_classification_table,
    "03_general_management_polc_framework": arch_03_general_management_polc_framework,
    "04_three_levels_of_management_hierarchy_svg": arch_04_three_levels_of_management_hierarchy_svg,
    "05_planning_and_organising_in_general_management": arch_05_planning_and_organising_in_general_management,
    "06_leading_and_controlling_in_general_management": arch_06_leading_and_controlling_in_general_management,
    "07_administration_function_information_lifecycle": arch_07_administration_function_information_lifecycle,
    "08_administration_importance_for_decision_making": arch_08_administration_importance_for_decision_making,
    "09_purchasing_function_right_inputs_definition": arch_09_purchasing_function_right_inputs_definition,
    "10_purchasing_cash_vs_credit_buying_and_stock_control": arch_10_purchasing_cash_vs_credit_buying_and_stock_control,
    "11_production_function_input_process_output_svg": arch_11_production_function_input_process_output_svg,
    "12_production_quality_control_and_unit_cost_calc": arch_12_production_quality_control_and_unit_cost_calc,
    "13_marketing_function_four_ps_overview": arch_13_marketing_function_four_ps_overview,
    "14_marketing_mix_four_ps_classification_table": arch_14_marketing_mix_four_ps_classification_table,
    "15_financial_function_capital_budgeting_and_cash_flow": arch_15_financial_function_capital_budgeting_and_cash_flow,
    "16_financial_own_vs_borrowed_capital_comparison": arch_16_financial_own_vs_borrowed_capital_comparison,
    "17_human_resources_function_recruitment_to_retention": arch_17_human_resources_function_recruitment_to_retention,
    "18_human_resources_sa_labour_legislation_table": arch_18_human_resources_sa_labour_legislation_table,
    "19_public_relations_function_vs_advertising": arch_19_public_relations_function_vs_advertising,
    "20_publicity_crisis_communication_and_csr": arch_20_publicity_crisis_communication_and_csr,
    "21_purchasing_vs_production_vs_marketing_handoff": arch_21_purchasing_vs_production_vs_marketing_handoff,
    "22_admin_and_finance_record_keeping_link": arch_22_admin_and_finance_record_keeping_link,
    "23_management_span_of_control_and_delegation": arch_23_management_span_of_control_and_delegation,
    "24_eight_functions_organisational_ecosystem_svg": arch_24_eight_functions_organisational_ecosystem_svg,
    "25_ntuli_beauty_style_scenario_function_identification": arch_25_ntuli_beauty_style_scenario_function_identification,
}
