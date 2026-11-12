"""Grade 9 EMS - Term 3 Trade Unions: Archetypes 01 to 25.

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 1/01. Trade Unions.md,
curriculum_docs/EMS_Gr9/Term 3/8-Trade unions.md, and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African labour relations contexts.
"""
from __future__ import annotations

import html
import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, get_ems_scenario as _raw_ems_scenario


def get_ems_scenario(rng: random.Random) -> Dict[str, Any]:
    d = dict(_raw_ems_scenario(rng))
    d["business"] = f"{d['entrepreneur']} {d['business_type']}"
    return d

TOPIC_NAME = "Trade unions"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_trade_unions"
CURRICULUM_REF = "Term 3 > The Economy: Trade Unions"


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
        "concept_group": "trade_unions",
        "learning_objective_id": f"lo_g9_tu_{subskill}",
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
        "diagnostic_tags": ["economy", "trade_unions", "labour_relations", "south_africa"],
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
        "concept_group": "trade_unions",
        "learning_objective_id": f"lo_g9_tu_{subskill}",
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
        "diagnostic_tags": ["economy", "trade_unions", "labour_relations", "south_africa"],
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
        "concept_group": "trade_unions",
        "learning_objective_id": f"lo_g9_tu_{subskill}",
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
        "diagnostic_tags": ["economy", "trade_unions", "classification_table", "south_africa"],
    }


def arch_01_trade_union_definition_and_core_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sector = rng.choice(["manufacturing", "mining", "commercial retail", "transport logistics"])
    prompt = (
        f"Workers at **{sc['business']}** in **{sc['area']}** ({sector} sector) want a stronger voice when discussing wages and working hours.\n\n"
        "Which definition **best** describes a **trade union**?"
    )
    correct = "An organised association of workers formed to protect and promote their shared workplace rights, fair wages, and safe conditions."
    distractors = [
        "A government tax agency that collects corporate income tax from factory owners.",
        "An employers' cartel formed to fix product selling prices across competing retailers.",
        "A private bank department that approves business start-up loans for entrepreneurs.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_01",
        subskill="01_trade_union_definition_and_core_purpose",
        title="Definition & Core Purpose of Trade Unions",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **trade union** represents employees collectively so workers at **{sc['business']}** can negotiate wages, benefits, and workplace safety instead of bargaining alone against employers."
        ),
        hints={
            "tier_1": "Think about why employees band together in an organisation.",
            "tier_2": "A trade union protects and advances workers' rights, pay, and conditions.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_trade_union_with_employer_association"],
    )


def arch_02_union_membership_voluntary_dues_and_strength(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    dues = rng.choice([75, 95, 110, 130])
    prompt = (
        f"At a factory in **{area}**, employees pay **{_fmt_r(dues)}** per month in union subscriptions.\n\n"
        "Why does paying regular membership fees strengthen a trade union's effectiveness?"
    )
    correct = "Subscriptions fund legal advice, member training, administrative staff, and full-time negotiators so workers have collective strength."
    distractors = [
        "Subscriptions allow the union to pay monthly dividends like listed company shares.",
        "Subscriptions replace the employer's legal duty to pay workers any salaries.",
        "Subscriptions exempt workers from following workplace safety regulations.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_02",
        subskill="02_union_membership_voluntary_dues_and_strength",
        title="Union Subscriptions & Collective Strength",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Monthly dues (**{_fmt_r(dues)}**) keep the union financially independent, paying for skilled negotiators, CCMA legal representation, and member education."
        ),
        hints={
            "tier_1": "How does a union afford lawyers, offices, and organisers without relying on employers?",
            "tier_2": "Member subscriptions fund union operations, training, and legal support.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_union_dues_are_taxes"],
    )


def arch_03_major_sa_trade_unions_and_sectors_matching_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pool = [
        ("SADTU", "South African Democratic Teachers' Union", "Public and private school educators"),
        ("NUM", "National Union of Mineworkers", "Gold, platinum, and coal mining"),
        ("FAWU", "Food and Allied Workers Union", "Agriculture, beverage, and food processing"),
        ("DENOSA", "Democratic Nursing Organisation of South Africa", "Hospitals and public clinic nurses"),
        ("POPCRU", "Police and Prisons Civil Rights Union", "Police, correctional, and traffic officers"),
        ("NEHAWU", "National Education, Health and Allied Workers' Union", "Public administration, health, and universities"),
        ("SACTWU", "Southern African Clothing and Textile Workers' Union", "Garment, textile, and footwear manufacturing"),
        ("SATAWU", "South African Transport and Allied Workers Union", "Rail, freight, port, and bus transport"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Economic Sector / Workforce", "Full Union Name", "Union Acronym"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Economic Sector / Workforce | Full Union Name | Union Acronym |", "| :--- | :--- | :--- |"]
    for idx, (acronym, full_name, sector) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", sector, "given"),
            _make_cell(f"t0_r{idx}_c1", full_name, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = acronym
        cell_hints[coord] = f"Take the official acronym matching '{full_name}'."
        memo_lines.append(f"| {sector} | {full_name} | {acronym} |")

    worked = f"**South African Trade Unions Matched to Sectors ({area}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{s} -> {a}" for a, _f, s in chosen)
    return _build_table(
        rng,
        qid_prefix="g9_tu_03",
        subskill="03_major_sa_trade_unions_and_sectors_matching_table",
        title="Major South African Trade Unions by Sector",
        prompt=(
            f"Career advisors in **{area}** are mapping major South African trade unions by economic sector.\n\n"
            "Enter the correct **Union Acronym** in the third column for each listed sector and union name."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Use the capital initials of the full union name given in column 2.",
            "tier_2": "Examples include SADTU (teachers), NUM (mineworkers), FAWU (food), DENOSA (nursing).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Row {i+1}: {chosen[i][0]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["mismatching_sa_unions_to_sectors"],
    )


def arch_04_cosatu_and_sa_union_federations(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    month = rng.choice(["March", "June", "September"])
    prompt = (
        f"During a {month} workplace summit in **{area}**, shop stewards refer to South Africa's largest trade union federation, **COSATU**.\n\n"
        "What does **COSATU** stand for, and what is the role of a trade union federation?"
    )
    correct = "Congress of South African Trade Unions; it unites many sector unions into one national body to strengthen policy advocacy."
    distractors = [
        "Council of South African Tax Units; it audits annual corporate income taxes.",
        "Committee of Southern African Traders; it regulates import customs duties.",
        "Coalition of Small Artisan Employers; it recruits apprentices for private mines.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_04",
        subskill="04_cosatu_and_sa_union_federations",
        title="COSATU & Union Federations",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Founded in **1985**, **COSATU** (*Congress of South African Trade Unions*) brings affiliate unions from mining, retail, education, and public service together under a unified national voice."
        ),
        hints={
            "tier_1": "The 'C' stands for Congress, and a federation groups multiple individual unions.",
            "tier_2": "COSATU = Congress of South African Trade Unions, uniting affiliate unions nationally.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_cosatu_name_or_role"],
    )


def arch_05_four_worker_categories_classification_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pool = [
        ("Cleaner sweeping warehouses and packing boxes", "General workers", "Unskilled / basic manual tasks"),
        ("Qualified electrician wiring factory machinery", "Tradesmen", "Certified craft or artisan skill"),
        ("Assembly-line welder operating factory presses", "Blue-collar workers", "Manual industrial/technical work"),
        ("Payroll clerk and financial accountant in an office", "White-collar workers", "Administrative, clerical, or professional work"),
        ("Farm labourer harvesting seasonal fruit crates", "General workers", "Entry-level physical duties"),
        ("Licensed plumber repairing municipal pipelines", "Tradesmen", "Apprenticeship-trained skilled trade"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Employee Role at Workplace", "Skill / Task Focus", "Worker Group (General / Tradesmen / Blue-collar / White-collar)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Employee Role | Skill / Task Focus | Worker Group |", "| :--- | :--- | :--- |"]
    for idx, (role, cat, focus) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", role, "given"),
            _make_cell(f"t0_r{idx}_c1", focus, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = cat
        cell_hints[coord] = "Enter exact group: General workers, Tradesmen, Blue-collar workers, or White-collar workers."
        memo_lines.append(f"| {role} | {focus} | {cat} |")

    worked = f"**Classification of Worker Groups ({area}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{r} -> {c}" for r, c, _f in chosen)
    return _build_table(
        rng,
        qid_prefix="g9_tu_05",
        subskill="05_four_worker_categories_classification_table",
        title="Classifying the Four Types of Workers",
        prompt=(
            f"Classify four employees working across **{area}** into the four recognised trade union worker groups: "
            "**General workers**, **Tradesmen**, **Blue-collar workers**, or **White-collar workers**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Separate office staff (white-collar), factory/mine manual staff (blue-collar), certified artisans (tradesmen), and unskilled helpers (general).",
            "tier_2": "Use exact names: General workers, Tradesmen, Blue-collar workers, White-collar workers.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Categorises '{chosen[i][0][:32]}...' as {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_blue_collar_with_white_collar_workers"],
    )


def arch_06_general_workers_vs_skilled_tradesmen_distinction(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    trade = rng.choice(["certified boiler-maker", "qualified millwright", "licensed diesel mechanic"])
    prompt = (
        f"On a construction site in **{area}**, management employs **general labourers** alongside a **{trade}**.\n\n"
        "What distinguishes **tradesmen (artisans)** from **general workers**?"
    )
    correct = "Tradesmen hold formal technical qualifications or completed apprenticeships in a specialised craft, whereas general workers perform tasks requiring minimal formal training."
    distractors = [
        "Tradesmen work exclusively in executive boardrooms while general workers only manage computers.",
        "General workers earn higher salaries because they hold university engineering degrees.",
        "Tradesmen are prohibited by law from joining any South African trade union.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_06",
        subskill="06_general_workers_vs_skilled_tradesmen_distinction",
        title="General Workers vs Tradesmen",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **{trade}** undergoes structured technical schooling and trade testing (artisan qualification), whereas **general workers** perform entry-level manual support duties."
        ),
        hints={
            "tier_1": "Focus on formal apprenticeship, trade certificates, and specialised craft skills.",
            "tier_2": "Tradesmen are certified skilled artisans; general workers perform unskilled or semi-skilled tasks.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_general_workers_with_certified_tradesmen"],
    )


def arch_07_blue_collar_vs_white_collar_workers(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Inside **{sc['business']}** in **{sc['area']}**, both **blue-collar** and **white-collar** employees belong to unions.\n\n"
        "Compare **blue-collar workers** and **white-collar workers** by giving **one** workplace difference and **one** South African example of each group."
    )
    expected = (
        "Blue-collar workers perform manual/physical industrial work (e.g. mineworkers, factory machine operators) often paid hourly/weekly wages; "
        "white-collar workers perform office, administrative, or professional work (e.g. bank clerks, teachers, nurses) usually paid monthly salaries."
    )
    sol = (
        f"**Comparison at {sc['business']} ({sc['area']}) [4 marks]:**\n\n"
        "- **Blue-collar workers:** Perform physical, manual, or operational labour in factories, mines, or transport **[1]** — e.g., **factory assembly operator / mineworker** **[1]**.\n"
        "- **White-collar workers:** Perform office, clerical, administrative, or professional service work **[1]** — e.g., **bookkeeper / teacher / nurse** **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_07",
        subskill="07_blue_collar_vs_white_collar_workers",
        title="Blue-Collar vs White-Collar Workers",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Contrast factory/manual labour with office/professional roles.",
            "tier_2": "Give one defining work environment for each group plus one clear job example.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Defines blue-collar as manual/industrial labour", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Valid blue-collar example (miner, driver, factory operator)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Defines white-collar as office/clerical/professional work", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Valid white-collar example (accountant, teacher, clerk)", "marks": 1, "editable": True},
        ],
        misconception_tags=["confusing_blue_collar_with_white_collar_workers"],
    )


def arch_08_early_sa_labour_history_1922_to_1946(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(["Johannesburg", "Witwatersrand", "Benoni", "Krugersdorp"])
    event = rng.choice(["1922 miners' strike", "1946 African Mine Workers' strike"])
    prompt = (
        f"Historical archives from **{area}** document South Africa's early industrial conflicts, including the **{event}**.\n\n"
        "What drove early South African mine and factory workers to form unions between **1920 and 1946**?"
    )
    correct = "Harsh working conditions, low pay, unsafe underground shifts, and employers cutting wages or replacing skilled workers with cheaper unrepresented labour."
    distractors = [
        "Employers voluntarily offered four-day paid weekends and workers opposed extra leave.",
        "Government banned all private mining companies from exporting gold before 1950.",
        "International software companies demanded automated digital payroll systems in 1922.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_08",
        subskill="08_early_sa_labour_history_1922_to_1946",
        title="Early SA Labour History (1922–1946)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"During the early industrial era on the **{area}** mines (notably the **1922** and **1946** strikes), dangerous conditions, low wages, and wage cuts led workers to organise collective action."
        ),
        hints={
            "tier_1": "Why would miners risk confrontation during the 1920s–1940s?",
            "tier_2": "Focus on hazardous underground work, low wages, and job/pay cuts.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_economic_causes_of_early_sa_strikes"],
    )


def arch_09_apartheid_labour_restrictions_migrant_labour_impact(rng: random.Random) -> Dict[str, Any]:
    homeland = rng.choice(["Transkei", "Ciskei", "KwaZulu", "Lebowa"])
    area = rng.choice(["Johannesburg", "Durban", "Cape Town", "Gqeberha"])
    prompt = (
        f"During apartheid, workers travelling from **{homeland}** to industrial centres such as **{area}** faced **migrant labour** controls and racial job reservation.\n\n"
        "Explain **two** ways apartheid labour laws suppressed black workers' rights before the 1979 reforms."
    )
    expected = (
        "Black unions were denied legal recognition/collective bargaining status, and job reservation / pass laws forced black migrant workers into low-paid manual jobs separated from their families."
    )
    sol = (
        f"**Impact of Apartheid Labour Restrictions ({homeland} to {area}) [4 marks]:**\n\n"
        "1. **Exclusion from Legal Bargaining:** Black trade unions were not legally recognised as employees' bargaining bodies under early Industrial Conciliation laws, making strikes illegal **[2]**.\n"
        "2. **Job Reservation & Migrant Control:** Skilled jobs were reserved by race while pass laws restricted migrant workers to single-sex hostels and low-wage manual work **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_09",
        subskill="09_apartheid_labour_restrictions_migrant_labour_impact",
        title="Apartheid Labour Laws & Migrant Labour",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Consider union recognition and movement/job restrictions (pass laws & job reservation).",
            "tier_2": "Mention (1) lack of legal union/strike recognition and (2) migrant pass controls or racial job reservation.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Unrecognised black unions / illegal strike prohibition", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Job reservation or migrant labour / pass law restrictions", "marks": 2, "editable": True},
        ],
        misconception_tags=["overlooking_apartheid_union_exclusion"],
    )


def arch_10_eighties_union_mobilisation_stay_aways_and_cosatu(rng: random.Random) -> Dict[str, Any]:
    township = rng.choice(["Soweto", "Khayelitsha", "Umlazi", "Mamelodi"])
    prompt = (
        f"In the **1980s**, workers in townships like **{township}** joined nationwide **stay-aways** alongside **COSATU**.\n\n"
        "Why did trade unions play both a workplace and political role during the 1980s?"
    )
    correct = "Because disenfranchised workers lacked parliamentary representation, unions combined wage bargaining with civic pressure for democracy and non-racial labour laws."
    distractors = [
        "Because every worker was already guaranteed equal voting rights and high minimum wages by 1980.",
        "Because unions aimed to privatise municipal clinics and close down factories permanently.",
        "Because employers requested stay-aways to avoid paying electricity tariffs.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_10",
        subskill="10_eighties_union_mobilisation_stay_aways_and_cosatu",
        title="1980s Stay-Aways & Democratic Struggle",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"In the 1980s, communities such as **{township}** used organised stay-aways and **COSATU** alliances because workers could not separate shop-floor exploitation from lack of political rights."
        ),
        hints={
            "tier_1": "Think about why workplace grievances connected to national political exclusion in the 1980s.",
            "tier_2": "Unions became a democratic voice against both unfair labour treatment and apartheid laws.",
            "tier_3": correct,
        },
        misconception_tags=["separating_1980s_union_history_from_political_rights"],
    )


def arch_11_post_1994_labour_law_transformation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Since **1994**, employers in **{area}** operate under South Africa's democratic labour dispensation.\n\n"
        "State **two** major improvements for workers brought about by post-1994 labour reforms."
    )
    expected = (
        "All workers gained equal constitutional protection regardless of race/gender, and democratic labour laws (like the LRA and BCEA) legalised union membership, collective bargaining, and regulated working hours."
    )
    sol = (
        f"**Post-1994 Labour Transformation ({area}) [4 marks]:**\n\n"
        "1. **Equal Constitutional Rights:** Racial job reservation ended; all workers gained equal protection against unfair discrimination **[2]**.\n"
        "2. **Legal Bargaining & Fair Standards:** The Labour Relations Act and Basic Conditions of Employment Act legally protected union membership, strikes, leave, and overtime **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_11",
        subskill="11_post_1994_labour_law_transformation",
        title="Post-1994 Labour Law Transformation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "What changed after 1994 regarding equality and union rights?",
            "tier_2": "Mention ending racial discrimination plus legal protection under the Constitution/LRA/BCEA.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Equal rights / end of racial job reservation", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Legal protection for union bargaining, LRA/BCEA hours and leave", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_labour_laws_existed_unchanged_before_1994"],
    )


def arch_12_primary_sector_mining_farm_worker_exploitation(rng: random.Random) -> Dict[str, Any]:
    sector_ex = rng.choice(["platinum mines in Rustenburg", "wine and fruit farms in Paarl", "coal mines in Emalahleni"])
    prompt = (
        f"Historically, trade union formation in South Africa concentrated strongly in primary sector industries such as **{sector_ex}**.\n\n"
        "Which factor **primarily** explains why primary sector workers urgently needed union protection?"
    )
    correct = "Remote workplaces, physically hazardous duties, low wages, and reliance on employer-controlled accommodation left individual workers vulnerable to exploitation."
    distractors = [
        "Primary sector labourers mostly worked remotely from home offices with six-figure salaries.",
        "Mining and agricultural employers were forbidden from hiring more than two workers.",
        "Primary sector farms produced software licences that required zero manual labour.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_12",
        subskill="12_primary_sector_mining_farm_worker_exploitation",
        title="Primary Sector Vulnerability & Unionisation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Workers on **{sector_ex}** faced dangerous conditions, low pay, and dependence on employer housing/hostels, making collective union representation vital."
        ),
        hints={
            "tier_1": "Think about the physical risks and living dependence in mines and remote farms.",
            "tier_2": "Hazardous conditions, low pay, and isolated/employer housing increased vulnerability.",
            "tier_3": correct,
        },
        misconception_tags=["misunderstanding_primary_sector_working_conditions"],
    )


def arch_13_constitution_section_23_labour_rights(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Employees at **{sc['business']}** in **{sc['area']}** invoke **Section 23 of the Constitution of South Africa** during a workplace meeting.\n\n"
        "Which right is **explicitly guaranteed** to workers under **Section 23**?"
    )
    correct = "Every worker has the right to fair labour practices, to form and join a trade union, to bargain collectively, and to participate in a lawful strike."
    distractors = [
        "Every worker has the right to seize business machinery without court authorisation.",
        "Employers have the right to fire any employee solely for attending a union meeting.",
        "Government sets identical flat salaries for every private retail manager nationwide.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_13",
        subskill="13_constitution_section_23_labour_rights",
        title="Constitution Section 23 Labour Rights",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "**Section 23** of South Africa's Constitution enshrines fair labour practices, freedom to form/join unions, collective bargaining, and the right to strike."
        ),
        hints={
            "tier_1": "Section 23 is the supreme constitutional clause protecting workers and unions.",
            "tier_2": "Look for fair labour practices, union membership, bargaining, and lawful strikes.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_section_23_with_company_policy"],
    )


def arch_14_freedom_of_association_and_closed_shop_limits(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    prompt = (
        f"At **{sc['business']}** in **{sc['area']}**, **{worker}** chooses NOT to join the local trade union, while colleagues try to pressure **{worker}**.\n\n"
        "1. What constitutional principle protects **{worker}**'s choice to join or not join a union?\n"
        "2. State **one** duty trade unions have toward non-members during recruitment drives."
    )
    expected = (
        "1. Freedom of association (Constitution Section 23 / LRA); "
        "2. Unions must persuade peacefully and must never intimidate, threaten, or force workers into joining."
    )
    sol = (
        f"**Freedom of Association ({sc['business']}) [3 marks]:**\n\n"
        f"1. **Principle:** **Freedom of association** protects **{worker}**'s voluntary right to join, or decline to join, a trade union without victimisation **[1]**.\n"
        "2. **Union Responsibility:** Unions may recruit via information and persuasion, but may **never use intimidation, violence, or coercion** against non-members **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_14",
        subskill="14_freedom_of_association_and_closed_shop_limits",
        title="Freedom of Association & Non-Intimidation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Joining a union must be voluntary, not forced.",
            "tier_2": "Name Freedom of Association and state that coercion/intimidation is forbidden.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Freedom of association", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Unions must not intimidate or force workers to join", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_union_membership_can_be_enforced_by_intimidation"],
    )


def arch_15_labour_relations_act_lra_objectives(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"When HR managers and union officials in **{area}** clash over a collective agreement, they consult the **Labour Relations Act (LRA) 66 of 1995**.\n\n"
        "Which option captures the **core objectives** of the **LRA**?"
    )
    correct = "To promote economic development, social justice, workplace democracy, and orderly resolution of labour disputes between employers and unions."
    distractors = [
        "To eliminate all trade unions so companies never experience industrial disputes.",
        "To replace municipal water billing with provincial payroll levies.",
        "To set fixed retail bread and fuel prices for grocery chains.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_15",
        subskill="15_labour_relations_act_lra_objectives",
        title="Labour Relations Act (LRA) Objectives",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The **LRA** gives practical effect to Section 23 by promoting orderly collective bargaining, workplace democracy, social justice, and peaceful dispute resolution via the CCMA."
        ),
        hints={
            "tier_1": "The LRA balances economic growth with fair worker rights and dispute resolution.",
            "tier_2": "Look for social justice, workplace democracy, and structured dispute resolution.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_lra_with_tax_or_price_regulation"],
    )


def arch_16_international_labour_organisation_ilo_alignment(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"South Africa's labour statutes in places from Polokwane to **{area}** align with conventions of the **International Labour Organisation (ILO)**.\n\n"
        "Which workplace standard does the **ILO** uphold globally?"
    )
    correct = "Decent work, elimination of forced and child labour, freedom of association, and non-discrimination at work."
    distractors = [
        "Abolishing paid annual leave across all developing countries.",
        "Setting global supermarket exchange rates for imported electronics.",
        "Banning employers from using automated factory equipment.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_16",
        subskill="16_international_labour_organisation_ilo_alignment",
        title="International Labour Organisation (ILO) Standards",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The **ILO** (a UN tripartite agency of governments, employers, and unions) sets international labour conventions promoting decent work, safety, and core human rights."
        ),
        hints={
            "tier_1": "What global body safeguards workers' human rights and decent work standards?",
            "tier_2": "ILO champions decent work, no child/forced labour, and freedom of association.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_ilo_with_trade_tariffs"],
    )


def arch_17_roles_vs_responsibilities_classification_table(rng: random.Random) -> Dict[str, Any]:
    items_pool = [
        ("Organise lawful industrial action and strikes", "Role", "A recognised power/function to mobilise members collectively"),
        ("Ensure that industrial action remains lawful and peaceful", "Responsibility", "Legal and ethical duty to avoid violence or property damage"),
        ("Negotiate wages and working conditions via collective bargaining", "Role", "Core representative function of a union"),
        ("Make realistic wage demands that do not bankrupt the business", "Responsibility", "Duty to safeguard sustainable employment"),
        ("Provide legal advice and representation at CCMA hearings", "Role", "Core service unions deliver to protect members"),
        ("Hold a secret ballot before calling members out on strike", "Responsibility", "Democratic duty ensuring true majority consent"),
        ("Recruit and educate members about workplace safety and rights", "Role", "Function that builds an informed collective voice"),
        ("Never intimidate or force non-members into joining the union", "Responsibility", "Constitutional duty respecting freedom of association"),
    ]
    selected = rng.sample(items_pool, 4)
    sector = rng.choice([
        "the South African mining and energy sector",
        "commercial retail and transport logistics",
        "heavy manufacturing and assembly industries",
        "public education and healthcare services",
    ])
    headers = ["No.", "Trade Union Action / Practice", "Category (Role vs Responsibility)", "Justification"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| No. | Trade Union Action / Practice | Role vs Responsibility | Justification |", "| :--- | :--- | :--- | :--- |"]
    for idx, (action, cat, reason) in enumerate(selected):
        c_cat = f"t0_r{idx}_c2"
        correct_map[c_cat] = cat
        cell_hints[c_cat] = f"Is '{action}' a power/function (Role) or a legal/ethical duty (Responsibility)?"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", str(idx + 1), "given"),
            _make_cell(f"t0_r{idx}_c1", action, "given"),
            _make_cell(c_cat, "", "required"),
            _make_cell(f"t0_r{idx}_c3", reason, "given"),
        ])
        memo_lines.append(f"| {idx + 1} | {action} | {cat} | {reason} |")

    sample = "; ".join(f"{i+1}: {selected[i][1]}" for i in range(4))
    worked = f"**Trade Union Roles vs Responsibilities ({sector}) [8 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_tu_17",
        subskill="17_roles_vs_responsibilities_classification_table",
        title="Trade Union Roles vs Responsibilities",
        prompt=(
            f"In **{sector}**, distinguish between the **Roles** (powers/functions) and **Responsibilities** (duties/obligations) of trade unions.\n\n"
            "Enter **Role** or **Responsibility** in Column 3 for each action."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "A Role is what a union does to empower members; a Responsibility is a duty to act lawfully and fairly.",
            "tier_2": "Write exact labels: Role or Responsibility.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Categorises '{selected[i][0][:30]}...' as {selected[i][1]}", "marks": 2, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confused_union_role_with_responsibility"],
    )


def arch_18_collective_bargaining_purpose_and_process(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pct = rng.choice([6, 7, 8])
    prompt = (
        f"Union representatives and management at **{sc['business']}** in **{sc['area']}** begin annual talks over a **{pct}%** wage adjustment and shift allowances.\n\n"
        "1. Define **collective bargaining**.\n"
        "2. Explain **one** advantage of collective bargaining over individual salary negotiations for employees."
    )
    expected = (
        "1. Collective bargaining is formal negotiation between employer representatives and a trade union representing a group of workers over wages and conditions of service. "
        "2. Workers gain stronger combined bargaining power and uniform, legally binding agreements."
    )
    sol = (
        f"**Collective Bargaining at {sc['business']} ({pct}% talk) [4 marks]:**\n\n"
        "1. **Definition:** Formal negotiation between **a trade union (representing workers collectively)** and **an employer / employers' body** to reach agreement on wages, hours, and conditions of employment **[2]**.\n"
        f"2. **Advantage:** Prevents employers from undercutting isolated workers at **{sc['business']}**, delivering fair standard terms backed by collective strength **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_18",
        subskill="18_collective_bargaining_purpose_and_process",
        title="Collective Bargaining Purpose & Advantage",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare one worker negotiating alone with many workers speaking through one union team.",
            "tier_2": "Collective bargaining = group negotiations between union and employer; gives stronger unity & fair standards.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Defines union-employer group negotiation over wages/conditions", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Advantage: greater bargaining power / uniform protection", "marks": 2, "editable": True},
        ],
        misconception_tags=["confusing_collective_bargaining_with_individual_contracts"],
    )


def arch_19_union_lobbying_government_on_labour_policy(rng: random.Random) -> Dict[str, Any]:
    issue = rng.choice(["national minimum wage adjustments", "stronger mine safety regulations", "UIF maternity and retrenchment benefits"])
    area = rng.choice(AREAS)
    prompt = (
        f"Trade union delegations from **{area}** meet cabinet officials to lobby for **{issue}**.\n\n"
        "What does **lobbying government** allow trade unions to achieve?"
    )
    correct = "To influence national legislation and socioeconomic policies so laws better protect all workers across South Africa."
    distractors = [
        "To appoint private corporate CEOs to sit as judges in municipal traffic courts.",
        "To secretly cancel employee pay-as-you-earn income tax deductions for managers.",
        "To replace the South African Reserve Bank in setting commercial bank interest rates.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_19",
        subskill="19_union_lobbying_government_on_labour_policy",
        title="Union Lobbying on National Policy",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Through bodies like **NEDLAC** and parliamentary submissions, unions **lobby government** on **{issue}** to shape protective national laws beyond one single workplace."
        ),
        hints={
            "tier_1": "Lobbying goes beyond one company to influence lawmakers.",
            "tier_2": "Unions persuade government to enact worker-friendly legislation and social protections.",
            "tier_3": correct,
        },
        misconception_tags=["limiting_union_role_strictly_to_one_factory"],
    )


def arch_20_worker_education_training_and_legal_representation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    count = rng.choice([24, 35, 48])
    prompt = (
        f"A regional union educates **{count}** members employed at **{sc['business']}** in **{sc['area']}** about workplace rights and offers legal help.\n\n"
        "Identify **two** practical non-wage services trade unions provide to their members."
    )
    expected = (
        "1. Skills training and worker rights/financial literacy workshops; "
        "2. Legal advice and representation in disciplinary hearings, retrenchments, or CCMA disputes."
    )
    sol = (
        f"**Non-Wage Union Services ({count} members at {sc['business']}) [4 marks]:**\n\n"
        "1. **Education & Skills Development:** Running workshops on workplace laws, safety, and technical upskilling **[2]**.\n"
        "2. **Legal Advice & Representation:** Advising workers on contracts and representing members in disciplinary inquiries and **CCMA** cases **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_20",
        subskill="20_worker_education_training_and_legal_representation",
        title="Worker Education & Legal Support Services",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Unions do more than negotiate pay — think of training and legal aid.",
            "tier_2": "Mention (1) education/skills training and (2) legal representation at hearings/CCMA.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Education / skills training / rights awareness", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Legal advice / disciplinary or CCMA representation", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_unions_as_only_negotiating_salaries"],
    )


def arch_21_shop_steward_workplace_representation_role(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    name = rng.choice(NAMES)
    prompt = (
        f"Workers at **{sc['business']}** in **{sc['area']}** elect fellow employee **{name}** as their **shop steward**.\n\n"
        "What is **{name}**'s main duty as a shop steward on the factory or office floor?"
    )
    correct = "To represent co-workers in day-to-day grievances, monitor compliance with labour agreements, and accompany members in disciplinary inquiries."
    distractors = [
        "To resign from the company immediately and act as an external Supreme Court judge.",
        "To sign corporate dividend cheques and approve annual marketing budgets for shareholders.",
        "To discipline fellow employees by imposing unilateral salary deductions without management.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_21",
        subskill="21_shop_steward_workplace_representation_role",
        title="Role of the Elected Shop Steward",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"As an elected co-worker, **{name}** serves as the workplace bridge between members and management at **{sc['business']}**, protecting fair procedures."
        ),
        hints={
            "tier_1": "A shop steward works on-site alongside fellow union members.",
            "tier_2": "Shop stewards handle day-to-day grievances, safety monitoring, and disciplinary representation.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_shop_steward_with_company_manager"],
    )


def arch_22_bargaining_councils_sector_wide_agreements(rng: random.Random) -> Dict[str, Any]:
    sector = rng.choice(["Motor Industry", "Metal and Engineering", "Clothing Manufacturing"])
    area = rng.choice(AREAS)
    prompt = (
        f"Employers' organisations and trade unions across South Africa's **{sector}** meet through a statutory **Bargaining Council** affecting firms in **{area}**.\n\n"
        "Why do sectors use **Bargaining Councils** instead of forcing every small firm to negotiate separately?"
    )
    correct = "They establish uniform minimum wages and employment conditions across an entire industry, reducing workplace conflict and unfair wage undercutting."
    distractors = [
        "They set fixed selling prices for retail customers buying imported vehicles.",
        "They abolish minimum wage floors whenever company profits rise.",
        "They collect municipal property rates from commercial landlords.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_22",
        subskill="22_bargaining_councils_sector_wide_agreements",
        title="Bargaining Councils in Industry",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **Bargaining Council** in the **{sector}** sets standardised industry-wide terms through collective agreements and resolves sector disputes efficiently."
        ),
        hints={
            "tier_1": "Think of negotiations covering an entire sector rather than just one company.",
            "tier_2": "Bargaining Councils create industry-wide agreements on wages and prevent unfair undercutting.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_bargaining_council_with_ccma_court"],
    )


def arch_23_workplace_forums_joint_decision_making(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    staff = rng.choice([120, 185, 240])
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** employs **{staff} full-time workers** (over 100 employees) and sets up a **workplace forum** under the LRA.\n\n"
        "State the main purpose of a **workplace forum** and give **two** non-wage operational matters management consults the forum on."
    )
    expected = (
        "Purpose: To promote non-adversarial worker participation and cooperation on operational workplace issues (rather than wage bargaining). "
        "Matters: restructuring/new technology, shift schedules, retrenchment criteria, or health and safety training."
    )
    sol = (
        f"**Workplace Forum at {sc['business']} ({staff} staff) [4 marks]:**\n\n"
        "1. **Purpose:** Encourages joint problem-solving, consultation, and efficiency between management and staff outside confrontational wage bargaining **[2]**.\n"
        "2. **Consultative Matters (any two):** Introduction of **new machinery/technology**, **workplace restructuring**, **training/grading policies**, or **shift & safety rosters** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_23",
        subskill="23_workplace_forums_joint_decision_making",
        title="Workplace Forums & Consultation (>100 Staff)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Workplace forums (>100 employees) focus on cooperation and operational efficiency rather than wages.",
            "tier_2": "State cooperative consultation + two non-wage topics like new tech, restructuring, or training.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Promotes worker participation / cooperative efficiency on non-wage issues", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Two valid matters (restructuring, new tech, training, safety/shifts)", "marks": 2, "editable": True},
        ],
        misconception_tags=["confusing_workplace_forum_with_wage_strike_committee"],
    )


def arch_24_ccma_and_lra_dispute_escalation_diagram(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    union_short = rng.choice(["NUM", "FAWU", "SATAWU", "SACTWU"])
    notice_hrs = 48
    conciliation_days = 30
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="220" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">LRA Dispute Resolution Path: {_esc(sc["business"])} &amp; {union_short}</text>'
        '<rect x="18" y="65" width="142" height="82" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="89" y="96" text-anchor="middle" font-size="12" font-weight="bold" fill="#78350f">1. Deadlock</text>'
        '<text x="89" y="116" text-anchor="middle" font-size="10" fill="#92400e">Bargaining talks</text>'
        '<text x="89" y="131" text-anchor="middle" font-size="10" fill="#92400e">reach impasse</text>'
        '<line x1="160" y1="106" x2="188" y2="106" stroke="#334155" stroke-width="2"/>'
        '<polygon points="188,101 198,106 188,111" fill="#334155"/>'
        '<rect x="198" y="65" width="145" height="82" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="270" y="96" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">2. CCMA</text>'
        f'<text x="270" y="116" text-anchor="middle" font-size="10" fill="#1e40af">Conciliation ({conciliation_days} days)</text>'
        '<text x="270" y="131" text-anchor="middle" font-size="10" fill="#1e40af">Independent mediator</text>'
        '<line x1="343" y1="106" x2="371" y2="106" stroke="#334155" stroke-width="2"/>'
        '<polygon points="371,101 381,106 371,111" fill="#334155"/>'
        '<rect x="381" y="65" width="138" height="82" rx="8" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>'
        '<text x="450" y="96" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">3. Certificate</text>'
        '<text x="450" y="116" text-anchor="middle" font-size="10" fill="#3730a3">Non-resolution issued</text>'
        f'<text x="450" y="131" text-anchor="middle" font-size="10" fill="#3730a3">+ {notice_hrs}h written notice</text>'
        '<line x1="519" y1="106" x2="544" y2="106" stroke="#334155" stroke-width="2"/>'
        '<polygon points="544,101 554,106 544,111" fill="#334155"/>'
        '<rect x="554" y="65" width="110" height="82" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="609" y="96" text-anchor="middle" font-size="12" font-weight="bold" fill="#14532d">4. Protected</text>'
        '<text x="609" y="116" text-anchor="middle" font-size="10" fill="#166534">Lawful strike or</text>'
        '<text x="609" y="131" text-anchor="middle" font-size="10" fill="#166534">CCMA arbitration</text>'
        '<text x="340" y="190" text-anchor="middle" font-size="11" fill="#475569">Skipping Steps 2 &amp; 3 makes industrial action UNPROTECTED under the LRA.</text>'
        '</svg>'
    )
    prompt = (
        f"Study the Labour Relations Act (LRA) dispute resolution flowchart for **{sc['business']}** and **{union_short}** in **{sc['area']}**.\n\n"
        f"Using the diagram, explain the **two statutory steps** {union_short} must complete between **Deadlock (Step 1)** and a **Protected Strike (Step 4)**, "
        f"stating the **30 days** conciliation window and **48 hours** written notice rule."
    )
    expected = (
        f"1. Refer the deadlock to the CCMA (or Bargaining Council) for conciliation within {conciliation_days} days; "
        f"2. Obtain a Certificate of Non-Resolution and give the employer {notice_hrs} hours' written notice before striking."
    )
    sol = (
        f"**LRA Dispute Steps ({sc['business']} & {union_short}) [4 marks]:**\n\n"
        f"1. **CCMA Conciliation (Step 2):** Refer the dispute to the independent **CCMA** (up to **{conciliation_days} days**) to attempt mediated settlement **[2]**.\n"
        f"2. **Certificate & Notice (Step 3):** If unresolved, obtain a **Certificate of Non-Resolution** **[1]** and serve at least **{notice_hrs} hours' written notice** on **{sc['business']}** before striking **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_24",
        subskill="24_ccma_and_lra_dispute_escalation_diagram",
        title="CCMA & LRA Dispute Escalation Flowchart",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Read Boxes 2 and 3 between Deadlock and Protected action in the flowchart.",
            "tier_2": "Include CCMA conciliation (30 days), Certificate of Non-Resolution, and 48h written notice.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "CCMA conciliation (30 days)", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Certificate of Non-Resolution", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "48 hours written notice before strike", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_strikes_start_immediately_without_ccma"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_25_protected_vs_unprotected_strike_requirements(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Union members at **{sc['business']}** in **{sc['area']}** walk out of work without consulting the **CCMA** or giving notice.\n\n"
        "Why is this walkout classified as an **unprotected strike** under South African labour law?"
    )
    correct = "Workers bypassed mandatory CCMA conciliation, failed to obtain a certificate of non-resolution, and failed to give 48 hours' written notice."
    distractors = [
        "Workers wore civilian clothing instead of safety boots during lunch hour.",
        "Only blue-collar workers participated while white-collar staff remained on leave.",
        "The strike lasted fewer than ten working days during the summer holidays.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_25",
        subskill="25_protected_vs_unprotected_strike_requirements",
        title="Protected vs Unprotected Strikes",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"For a strike at **{sc['business']}** to be legally **protected**, the dispute must first go to the **CCMA**, receive a non-resolution certificate, and serve **48 hours' written notice** (7 days if the State is employer)."
        ),
        hints={
            "tier_1": "Check the legal procedural prerequisites set by the LRA before striking.",
            "tier_2": "Protected strikes require CCMA referral, non-resolution certificate, and 48h written notice.",
            "tier_3": correct,
        },
        misconception_tags=["believing_all_worker_walkouts_are_automatically_protected"],
    )


BUILDERS_01_25 = {
    "01_trade_union_definition_and_core_purpose": arch_01_trade_union_definition_and_core_purpose,
    "02_union_membership_voluntary_dues_and_strength": arch_02_union_membership_voluntary_dues_and_strength,
    "03_major_sa_trade_unions_and_sectors_matching_table": arch_03_major_sa_trade_unions_and_sectors_matching_table,
    "04_cosatu_and_sa_union_federations": arch_04_cosatu_and_sa_union_federations,
    "05_four_worker_categories_classification_table": arch_05_four_worker_categories_classification_table,
    "06_general_workers_vs_skilled_tradesmen_distinction": arch_06_general_workers_vs_skilled_tradesmen_distinction,
    "07_blue_collar_vs_white_collar_workers": arch_07_blue_collar_vs_white_collar_workers,
    "08_early_sa_labour_history_1922_to_1946": arch_08_early_sa_labour_history_1922_to_1946,
    "09_apartheid_labour_restrictions_migrant_labour_impact": arch_09_apartheid_labour_restrictions_migrant_labour_impact,
    "10_eighties_union_mobilisation_stay_aways_and_cosatu": arch_10_eighties_union_mobilisation_stay_aways_and_cosatu,
    "11_post_1994_labour_law_transformation": arch_11_post_1994_labour_law_transformation,
    "12_primary_sector_mining_farm_worker_exploitation": arch_12_primary_sector_mining_farm_worker_exploitation,
    "13_constitution_section_23_labour_rights": arch_13_constitution_section_23_labour_rights,
    "14_freedom_of_association_and_closed_shop_limits": arch_14_freedom_of_association_and_closed_shop_limits,
    "15_labour_relations_act_lra_objectives": arch_15_labour_relations_act_lra_objectives,
    "16_international_labour_organisation_ilo_alignment": arch_16_international_labour_organisation_ilo_alignment,
    "17_roles_vs_responsibilities_classification_table": arch_17_roles_vs_responsibilities_classification_table,
    "18_collective_bargaining_purpose_and_process": arch_18_collective_bargaining_purpose_and_process,
    "19_union_lobbying_government_on_labour_policy": arch_19_union_lobbying_government_on_labour_policy,
    "20_worker_education_training_and_legal_representation": arch_20_worker_education_training_and_legal_representation,
    "21_shop_steward_workplace_representation_role": arch_21_shop_steward_workplace_representation_role,
    "22_bargaining_councils_sector_wide_agreements": arch_22_bargaining_councils_sector_wide_agreements,
    "23_workplace_forums_joint_decision_making": arch_23_workplace_forums_joint_decision_making,
    "24_ccma_and_lra_dispute_escalation_diagram": arch_24_ccma_and_lra_dispute_escalation_diagram,
    "25_protected_vs_unprotected_strike_requirements": arch_25_protected_vs_unprotected_strike_requirements,
}
