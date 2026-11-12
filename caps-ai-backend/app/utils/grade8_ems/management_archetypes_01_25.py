"""Grade 8 EMS - Levels and functions of management: Archetypes 01 to 25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 3/02. Levels and functions of management.md
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
    "Mzansi Builders Hub",
    "Karabo Foods Catering",
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
        "topic": "Levels and functions of management",
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_management",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_mgt_{subskill}",
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
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "management", "south_africa"],
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
        "topic": "Levels and functions of management",
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_management",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_mgt_{subskill}",
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
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "management", "south_africa"],
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
        "topic": "Levels and functions of management",
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_management",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_mgt_{subskill}",
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
        "term": 3,
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
        "diagnostic_tags": ["entrepreneurship", "management", "south_africa"],
    }


def arch_01_definition_and_purpose_of_management(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    area = rng.choice(AREAS)
    prompt = (
        f"As **{biz}** in **{area}** expands its staff and delivery fleet, why does the enterprise rely on effective **management**?"
    )
    correct = "To coordinate people, finances, and physical resources through planning, organising, leading, and controlling so business goals are met efficiently."
    distractors = [
        "To prevent workers from ever knowing their daily job responsibilities.",
        "To eliminate the need for budgeting, equipment, or customer service.",
        "To convert every private business into a municipal tax office.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_01",
        subskill="01_definition_and_purpose_of_management",
        title="Definition & Purpose of Business Management",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Management** ensures **{biz}** uses staff, money, and materials harmoniously via **Planning, Organising, Leading, and Controlling** to reach objectives efficiently."
        ),
        hints={
            "tier_1": "What keeps employees, budgets, and stock pulling in the same direction?",
            "tier_2": "Management coordinates human and material resources to reach goals efficiently.",
            "tier_3": correct,
        },
        misconception_tags=["equating_management_solely_with_punishing_workers"],
    )


def arch_02_three_levels_of_management_pyramid_diagram(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    top_n = rng.choice([2, 3, 4])
    mid_n = rng.choice([6, 8, 10])
    low_n = rng.choice([16, 20, 24])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="230" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Management Pyramid: {biz}</text>'
        '<polygon points="320,42 225,95 415,95" fill="#1d4ed8" stroke="#1e3a8a" stroke-width="2"/>'
        f'<text x="320" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Top ({top_n} Execs)</text>'
        '<polygon points="225,98 415,98 475,152 165,152" fill="#16a34a" stroke="#14532d" stroke-width="2"/>'
        f'<text x="320" y="130" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">Middle Management ({mid_n} Dept Heads)</text>'
        '<polygon points="165,155 475,155 540,210 100,210" fill="#ea580c" stroke="#9a3412" stroke-width="2"/>'
        f'<text x="320" y="188" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">Lower / First-Line Management ({low_n} Supervisors)</text>'
        '</svg>'
    )
    prompt = (
        f"Examine the management hierarchy pyramid for **{biz}** showing **{top_n} top executives**, **{mid_n} middle managers**, and **{low_n} lower supervisors**.\n\n"
        f"(a) Explain why there are far fewer managers at the **Top** ({top_n}) than at the **Lower** level ({low_n});\n"
        "(b) State the primary decision-horizon focus of **Top** versus **Lower** management."
    )
    expected = (
        f"(a) A few Top leaders set overall direction for the whole company, while many Lower managers ({low_n}) directly supervise daily frontline teams across shifts/sections. "
        "(b) Top focuses on long-term strategic decisions (years ahead); Lower focuses on short-term day-to-day operational tasks."
    )
    sol = (
        f"**Management Pyramid Analysis ({biz}) [4 marks]:**\n\n"
        f"**(a) Pyramid Shape ({top_n} vs {low_n}):** Few executives (**{top_n}**) guide overall corporate direction, whereas many supervisors (**{low_n}**) are needed on the floor to oversee small teams daily **[2]**.\n\n"
        "**(b) Decision Time Horizons:**\n"
        "- **Top Management:** Long-term **strategic** planning and policy (several years ahead) **[1]**.\n"
        "- **Lower Management:** Short-term **operational** scheduling and daily output checks **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_02",
        subskill="02_three_levels_of_management_pyramid_diagram",
        title="The Three-Tier Management Hierarchy Pyramid",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Look at the width of each triangle layer from top to bottom.",
            "tier_2": "Explain hands-on supervision density (why bottom is widest) and long-term vs daily time horizons.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Explains why lower tier has more supervisors (direct daily team oversight)", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Top = long-term strategic focus; Lower = daily/short-term operational focus", "marks": 2, "editable": True},
        ],
        misconception_tags=["inverting_the_management_pyramid"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_03_top_management_titles_and_strategic_horizon(rng: random.Random) -> Dict[str, Any]:
    leader = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{leader}** serves as Chief Executive Officer (**CEO**) alongside the Board of Directors of **{biz}**.\n\n"
        "Which responsibility belongs strictly to **Top-level Management**?"
    )
    correct = "Setting long-term strategic vision, approving overall company policy, and deciding on 5-year national expansion for the entire business."
    distractors = [
        "Unlocking the delivery storeroom at 07:00 and checking staff time-cards daily.",
        "Operating a single cash register during the lunch rush.",
        "Assigning hourly tea-break slots for six warehouse packers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_03",
        subskill="03_top_management_titles_and_strategic_horizon",
        title="Top Management: Titles & Strategic Decisions",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Top-level management** (CEO **{leader}**, Managing Director, Board) carries responsibility for the whole enterprise's **long-term strategy** and policies."
        ),
        hints={
            "tier_1": "Match the CEO / Board role with company-wide, multi-year decisions.",
            "tier_2": "Top management = strategic long-term goals and corporate policy.",
            "tier_3": correct,
        },
        misconception_tags=["assigning_hourly_rostering_to_top_management"],
    )


def arch_04_middle_management_departmental_bridging_role(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    dept = rng.choice(["Marketing Department", "Human Resources Department", "Finance Department", "Production Department"])
    biz = rng.choice(BUSINESS_NAMES)
    goal = rng.choice(["growing national sales by 15% this year", "reducing factory waste over the next 4 quarters"])
    prompt = (
        f"**{mgr}** heads the **{dept}** at **{biz}**. Top management sets the broad corporate target of **{goal}**.\n\n"
        f"Identify **{mgr}**'s management level and explain **two key duties** connecting Top executives with Lower-level supervisors."
    )
    expected = (
        f"Middle-level (departmental) management. 1) Translates Top management's long-term goal into concrete medium-term goals for the {dept}; "
        "2) Allocates departmental budgets/resources and coordinates/supports Lower-level supervisors."
    )
    sol = (
        f"**Middle Management Bridging Role ({mgr}, {dept}) [3 marks]:**\n\n"
        "1. **Level:** **Middle-level management** (Departmental Manager) **[1]**.\n"
        f"2. **Translating Strategy into Action:** Converts Top management's target (**{goal}**) into medium-term departmental targets and campaigns **[1]**.\n"
        "3. **Supporting Lower Management:** Guides shift supervisors and monitors departmental performance back to Top executives **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_04",
        subskill="04_middle_management_departmental_bridging_role",
        title="Middle Management: Departmental Bridging Role",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Marketing, Finance, HR, and Production Heads sit between CEO and Floor Supervisors.",
            "tier_2": "Name Middle management plus translating strategic targets and supervising lower managers.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies Middle-level management", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Converts long-term strategy into departmental targets", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Leads/supports lower supervisors and coordinates across department", "marks": 1, "editable": True},
        ],
        misconception_tags=["treating_departmental_heads_as_lower_level_foremen"],
    )


def arch_05_lower_first_line_management_operational_tasks(rng: random.Random) -> Dict[str, Any]:
    sup = rng.choice(PERSON_NAMES)
    area = rng.choice(AREAS)
    setting = rng.choice(["packaging shift foreman", "supermarket floor supervisor", "kitchen shift team leader"])
    prompt = (
        f"**{sup}** works as a **{setting}** at a branch in **{area}**.\n\n"
        "Which set of daily actions belongs specifically to **Lower-level (First-line) Management**?"
    )
    correct = "Allocating daily work rosters to frontline staff, monitoring immediate product/service quality, and solving day-to-day floor problems."
    distractors = [
        "Signing a 10-year international merger with overseas shareholders.",
        "Listing company shares on the JSE via a Prospectus.",
        "Determining national tax policy for the Ministry of Finance.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_05",
        subskill="05_lower_first_line_management_operational_tasks",
        title="Lower (First-Line) Management: Operational Duties",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"As a **{setting}**, **{sup}** performs **lower-level (operational) management** by supervising frontline employees daily and ensuring smooth routine work."
        ),
        hints={
            "tier_1": "Lower management works directly alongside frontline workers every single day.",
            "tier_2": "Focus on daily schedules, routine safety/quality, and hands-on supervision.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_first_line_supervisors_with_board_directors"],
    )


def arch_06_management_levels_classification_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    pool = [
        (f"Chief Executive Officer (CEO) signing a 5-year expansion pact for {biz}", "Top"),
        ("Human Resources Manager drafting quarterly hiring targets for staff", "Middle"),
        ("Warehouse Shift Supervisor checking daily packing accuracy", "Lower"),
        ("Marketing Manager coordinating seasonal provincial radio adverts", "Middle"),
        ("Board of Directors approving overall company sustainability policy", "Top"),
        ("Bakery Floor Foreman assigning morning oven cleaning duties", "Lower"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Management Role / Activity", "Management Level (Top / Middle / Lower)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Management Role / Activity | Management Level |", "| :--- | :--- |"]
    for idx, (act, lvl) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", act, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = lvl
        cell_hints[c1] = "Write exactly: Top, Middle, or Lower."
        memo_lines.append(f"| {act} | {lvl} |")

    worked = f"**Completed Management Level Schedule ({biz}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{a} -> {l}" for a, l in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_06",
        subskill="06_management_levels_classification_table",
        title="Classify Decisions by Management Level",
        prompt=f"Classify each role or action inside **{biz}** as **Top**, **Middle**, or **Lower** management.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Company-wide 5-year/policy = Top; Departmental quarterly = Middle; Daily shift/floor = Lower.",
            "tier_2": "Enter exactly: Top, Middle, or Lower.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]} -> {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["mixing_middle_departmental_with_top_executive_roles"],
    )


def arch_07_polc_four_management_tasks_overview(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"Every effective manager at **{biz}** executes four core functions often remembered by **POLC**.\n\n"
        "What are the **four basic tasks of management**?"
    )
    correct = "Planning, Organising, Leading, and Controlling."
    distractors = [
        "Purchasing, Outsourcing, Liquidating, and Competing.",
        "Advertising, Taxation, Borrowing, and Retrenching.",
        "Autocratic, Democratic, Permissive, and Laissez-faire.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_07",
        subskill="07_polc_four_management_tasks_overview",
        title="Four Core Functions of Management (POLC)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The four foundational management tasks are **Planning**, **Organising**, **Leading**, and **Controlling** (**POLC**) — distinct from the 3 management styles."
        ),
        hints={
            "tier_1": "Expand the acronym P - O - L - C.",
            "tier_2": "Do NOT confuse management TASKS (POLC) with management STYLES (autocratic/democratic/permissive).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_management_tasks_polc_with_management_styles"],
    )


def arch_08_planning_task_definition_and_forecasting(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    goal = rng.choice(["launching a second delivery branch in six months", "doubling school stationery output before January"])
    prompt = (
        f"Before committing cash or hiring staff for **{goal}**, **{mgr}** at **{biz}** sits down to decide ahead what targets to achieve, "
        "which exact steps must happen first, and what budget and timeline are needed.\n\n"
        "Name this management task and explain **two reasons** why skipping it leads to business failure."
    )
    expected = (
        "Planning. 1) Without clear goals and forecasts, staff waste money and time on uncoordinated tasks; "
        "2) Businesses fail to anticipate shortages, bottlenecks, or cash-flow crises early."
    )
    sol = (
        f"**The Planning Function ({mgr} at {biz}) [3 marks]:**\n\n"
        "1. **Management Task:** **Planning** (deciding ahead what must be done, when, and how) **[1]**.\n"
        "2. **Two Reasons Planning Prevents Failure:**\n"
        "   - Sets clear targets and avoids wasted time, duplicated work, and overspending **[1]**.\n"
        "   - Anticipates supply shortages, deadlines, and cash requirements before crises hit **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_08",
        subskill="08_planning_task_definition_and_forecasting",
        title="Planning Function: Setting Goals & Deciding Ahead",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Which of P-O-L-C means thinking and deciding ahead before acting?",
            "tier_2": "Name Planning, then give two problems caused when a manager rushes in with no foresight.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies Planning", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Reason 1: clear direction / avoids waste of resources", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Reason 2: anticipates risks, bottlenecks, or cash needs early", "marks": 1, "editable": True},
        ],
        misconception_tags=["equating_planning_with_reacting_after_crises"],
    )


def arch_09_planning_vs_budget_forecast_calculation(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    base_units = rng.choice([2000, 2500, 3000])
    growth_pct = rng.choice([10, 20, 25])
    extra_units = base_units * growth_pct // 100
    target_units = base_units + extra_units
    unit_cost = rng.choice([40, 50, 60])
    total_budget = target_units * unit_cost

    prompt = (
        f"During annual **Planning**, **{biz}** sold **{base_units:,} unit packs** last year and sets a strategic target to grow output by **{growth_pct}%** next year. "
        f"Production cost is projected at **{_fmt_r(unit_cost)} per unit**.\n\n"
        "Calculate:\n"
        "(a) The **planned production target (in units)** for next year;\n"
        "(b) The **total planned production cost budget** required."
    )
    expected = f"(a) Planned output = {target_units:,} units; (b) Production budget = {_fmt_r(total_budget)}"
    sol = (
        f"**Planning Production Targets & Cost Budget ({biz}) [4 marks]:**\n\n"
        f"**(a) Target Output (+{growth_pct}%):**\n"
        f"$${base_units:,} + ({base_units:,} \\times {growth_pct}\\%) = {base_units:,} + {extra_units:,} = {target_units:,}\\text{{ units}}$$ **[2]**\n\n"
        f"**(b) Planned Production Budget (@ {_fmt_r(unit_cost)}/unit):**\n"
        f"$${target_units:,} \\times {_fmt_r(unit_cost)} = {_fmt_r(total_budget)}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_09",
        subskill="09_planning_vs_budget_forecast_calculation",
        title="Quantitative Planning: Output Target & Cost Forecast",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Increase {base_units:,} by {growth_pct}% first.",
            "tier_2": f"Multiply the new unit target by {_fmt_r(unit_cost)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Target output = {target_units:,} units", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Planned budget = {_fmt_r(total_budget)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_to_add_growth_units_to_baseline"],
        qtype="calculation",
    )


def arch_10_organising_task_delegation_and_resource_allocation(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"After goals are finalised at **{biz}**, **{mgr}** groups tasks into Procurement, Packing, and Delivery teams, "
        "assigns exactly who reports to whom, and allocates delivery vans and equipment to each group.\n\n"
        "Which management function is **{0}** performing?".format(mgr)
    )
    correct = "Organising — dividing work, assigning clear authority/responsibility, and allocating resources to put goals into action."
    distractors = [
        "Controlling — disciplining workers after an annual audit variance.",
        "Autocratic dictating — shouting at customers without any structure.",
        "Liquidation — shutting down the company and selling off its vans.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_10",
        subskill="10_organising_task_delegation_and_resource_allocation",
        title="Organising: Dividing Work & Allocating Resources",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Deciding **who does what** and matching workers with vans, tools, and budgets is **Organising**."
        ),
        hints={
            "tier_1": "Notice: grouping teams, assigning responsibilities, and distributing tools/vans.",
            "tier_2": "Putting structure, roles, and resources in place = Organising.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_organising_with_leading_or_controlling"],
    )


def arch_11_span_of_control_and_organising_ratio_calculation(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    max_span = rng.choice([8, 10, 12])
    total_workers = max_span * rng.choice([5, 6, 8])
    needed_sups = total_workers // max_span

    prompt = (
        f"While **Organising** a new assembly plant for **{biz}**, HR policy requires that each Lower-level supervisor oversees at most **{max_span} workers** (the **span of control**) to maintain safety and quality.\n\n"
        f"If the plant hires **{total_workers} frontline workers**:\n"
        "(a) How many **lower-level supervisors** must be appointed?\n"
        "(b) Why can making one supervisor's span of control too wide (e.g., 50 workers) harm quality?"
    )
    expected = (
        f"(a) {needed_sups} supervisors ({total_workers} / {max_span}). "
        "(b) One supervisor cannot properly coach, inspect work, or prevent safety/quality mistakes across 50 workers simultaneously."
    )
    sol = (
        f"**Organising Span of Control ({biz}) [3 marks]:**\n\n"
        f"**(a) Supervisors Required:** ${total_workers} \\div {max_span} = {needed_sups}\\text{{ supervisors}}$ **[2]**\n\n"
        "**(b) Excessive Span Risk:** Too many direct reports overstretch supervision, causing miscommunication, slower coaching, and lower product quality **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_11",
        subskill="11_span_of_control_and_organising_ratio_calculation",
        title="Organising Span of Control & Staffing Ratio",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Divide total workers by the maximum workers per supervisor.",
            "tier_2": "Explain why one supervisor managing dozens of staff loses oversight quality.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct count = {needed_sups} supervisors", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Explains diluted supervision, quality errors, or weak coaching", "marks": 1, "editable": True},
        ],
        misconception_tags=["multiplying_workers_by_span_instead_of_dividing"],
        qtype="calculation",
    )


def arch_12_leading_task_communication_and_staff_motivation(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    issue = rng.choice(["high absenteeism and slow customer service", "falling morale after a busy holiday peak"])
    prompt = (
        f"**{biz}** faces **{issue}**. Even though shifts and budgets are well-planned and organised, staff feel disconnected and unmotivated. "
        f"**{mgr}** steps in to hold encouraging briefings, clarify team goals, listen to concerns, and recognise top performers.\n\n"
        f"Identify the **management task** **{mgr}** is applying and give **two practical outcomes** of effective leadership on staff performance."
    )
    expected = (
        "Leading. Outcomes: 1) Higher staff motivation, enthusiasm, and morale; "
        "2) Better teamwork, communication, productivity, and lower absenteeism."
    )
    sol = (
        f"**The Leading Function ({mgr} at {biz}) [3 marks]:**\n\n"
        "1. **Management Task:** **Leading** (guiding, inspiring, communicating, and motivating staff) **[1]**.\n"
        "2. **Two Performance Outcomes:**\n"
        "   - Raises **employee morale, loyalty, and willingness to put in effort** **[1]**.\n"
        "   - Improves **clear communication, teamwork, and productivity**, lowering absenteeism **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_12",
        subskill="12_leading_task_communication_and_staff_motivation",
        title="Leading Function: Communication & Motivation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Notice motivating, communicating, encouraging, and guiding people.",
            "tier_2": "Name Leading and link it to higher morale and stronger productivity/teamwork.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies Leading", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Higher employee morale/motivation", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Better teamwork, communication, and productivity", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_leading_only_means_giving_commands"],
    )


def arch_13_controlling_task_standards_and_corrective_action(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    metric = rng.choice(["daily defective brick rate", "monthly delivery fuel expense", "weekly customer wait time"])
    prompt = (
        f"Every Friday, **{mgr}** at **{biz}** compares the **actual {metric}** against pre-set quality benchmarks, "
        "identifies shortfalls, and immediately adjusts staff training or equipment maintenance to bring results back on track.\n\n"
        f"Which management function is **{mgr}** exercising?"
    )
    correct = "Controlling — monitoring actual performance against set standards and taking corrective action when deviations occur."
    distractors = [
        "Permissive non-interference — allowing defects to grow indefinitely without review.",
        "Incorporation — filing an initial MOI document with CIPC.",
        "Organising — choosing which colour stationery folders to buy before opening.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_13",
        subskill="13_controlling_task_standards_and_corrective_action",
        title="Controlling: Standards, Monitoring & Corrective Action",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Comparing **actual performance** against **standards/targets** and applying **corrective steps** defines the **Controlling** task."
        ),
        hints={
            "tier_1": "Look for measuring results, comparing against targets, and fixing deviations.",
            "tier_2": "Monitor -> Compare -> Correct = Controlling.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_controlling_with_autocratic_bullying"],
    )


def arch_14_controlling_variance_calculation_actual_vs_budget(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    budget_cost = rng.choice([20000, 25000, 40000])
    overrun_pct = rng.choice([10, 15, 20])
    variance = budget_cost * overrun_pct // 100
    actual_cost = budget_cost + variance

    prompt = (
        f"During monthly **Controlling**, **{biz}** budgeted **{_fmt_r(budget_cost)}** for packaging materials, "
        f"but actual invoices totalled **{_fmt_r(actual_cost)}**.\n\n"
        "(a) Calculate the **Rand overspending variance** and the **percentage overrun** above budget;\n"
        "(b) Suggest **one realistic corrective action** management can take next month."
    )
    expected = (
        f"(a) Variance = {_fmt_r(variance)} overspent ({overrun_pct}% over budget). "
        "(b) Negotiate bulk supplier discounts, reduce packaging waste/damage on the floor, or check alternative suppliers."
    )
    sol = (
        f"**Controlling Variance Analysis ({biz}) [4 marks]:**\n\n"
        "**(a) Variance & Percentage Overrun:**\n"
        f"- **Overspend variance:** ${_fmt_r(actual_cost)} - {_fmt_r(budget_cost)} = {_fmt_r(variance)}$ **[1]**\n"
        f"- **Percentage overrun:** $\\frac{{{_fmt_r(variance)}}}{{{_fmt_r(budget_cost)}}} \\times 100\\% = {overrun_pct}\\%$ **[2]**\n\n"
        "**(b) Corrective Action:** Tighten stock waste controls on the packing line or compare bulk quotes from competing suppliers **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_14",
        subskill="14_controlling_variance_calculation_actual_vs_budget",
        title="Controlling Cost Variances: Budget vs Actual",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Subtract budgeted amount from actual spend, then divide the difference by the budgeted amount x 100.",
            "tier_2": "Give a practical operational fix to bring packaging expenses back on target.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Rand variance = {_fmt_r(variance)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Percentage overrun = {overrun_pct}%", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Sensible corrective cost-control measure", "marks": 1, "editable": True},
        ],
        misconception_tags=["dividing_variance_by_actual_instead_of_budget"],
        qtype="calculation",
    )


def arch_15_polc_management_tasks_scenario_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    pool = [
        (f"Setting next year's revenue goal of R2 million for {biz}", "Planning"),
        ("Allocating work shifts, cashiers, and stockrooms to each supervisor", "Organising"),
        ("Holding Monday morning briefings to coach and inspire delivery drivers", "Leading"),
        ("Inspecting Friday quality logs to fix delayed customer orders", "Controlling"),
    ]
    rng.shuffle(pool)
    headers = ["Management Action", "Management Task (Planning / Organising / Leading / Controlling)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Management Action | Management Task |", "| :--- | :--- |"]
    for idx, (act, task) in enumerate(pool):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", act, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = task
        cell_hints[c1] = "Enter: Planning, Organising, Leading, or Controlling."
        memo_lines.append(f"| {act} | {task} |")

    worked = f"**Completed POLC Function Schedule ({biz}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{a} -> {t}" for a, t in pool)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_15",
        subskill="15_polc_management_tasks_scenario_table",
        title="Match Actions to Management Functions (POLC)",
        prompt=f"Classify each action carried out at **{biz}** under the correct management function: **Planning**, **Organising**, **Leading**, or **Controlling**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Goals ahead = Planning; shifts/resources = Organising; inspiring staff = Leading; checking logs/fixing = Controlling.",
            "tier_2": "Type exactly: Planning, Organising, Leading, or Controlling.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{pool[i][0]} -> {pool[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_organising_shifts_with_controlling"],
    )


def arch_16_polc_interdependence_why_all_four_matter(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{founder}** drafts brilliant growth goals for **{biz}** (**Planning**) and divides duties cleanly (**Organising**), "
        "but never communicates with workers or monitors stock waste and expenses (**skipping Leading and Controlling**).\n\n"
        f"Predict **two specific operational problems** **{biz}** will suffer because management skipped **Leading** and **Controlling**."
    )
    expected = (
        "1) Skipped Leading: Workers lack direction, motivation, and morale, hurting productivity and customer care. "
        "2) Skipped Controlling: Errors, overspending, and stock losses go unnoticed until serious financial losses occur."
    )
    sol = (
        f"**Consequences of Neglecting Leading & Controlling ({biz}) [4 marks]:**\n\n"
        "1. **Without Leading:** Staff feel unvalued, poorly guided, and demotivated, leading to slow service and conflict **[2]**.\n"
        "2. **Without Controlling:** Cost overruns, stock shrinkage, and quality defects remain uncorrected, eroding profits **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_16",
        subskill="16_polc_interdependence_why_all_four_matter",
        title="Interdependence of All Four POLC Tasks",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Separate the staff-motivation problem (missing Leading) from the error/cost-leak problem (missing Controlling).",
            "tier_2": "Show one concrete consequence for each neglected function.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Missing Leading -> low morale, weak teamwork, unclear daily motivation", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Missing Controlling -> unmonitored waste, errors, and budget losses", "marks": 2, "editable": True},
        ],
        misconception_tags=["thinking_planning_alone_guarantees_execution"],
    )


def arch_17_management_styles_three_types_overview(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Business owners across **{area}** differ in how much say they give employees over decisions.\n\n"
        "Which option lists the **three core management styles** taught in Grade 8 Entrepreneurship?"
    )
    correct = "Autocratic (directive), Democratic (participatory), and Permissive (free-rein / laissez-faire)."
    distractors = [
        "Top, Middle, and Lower management.",
        "Planning, Organising, and Controlling.",
        "Sole trader, Partnership, and Close Corporation.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_17",
        subskill="17_management_styles_three_types_overview",
        title="The Three Management Styles Overview",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "The three management **styles** are **Autocratic** (manager dictates alone), **Democratic** (participatory with staff), and **Permissive / Laissez-faire** (broad delegation)."
        ),
        hints={
            "tier_1": "Do not mix up levels (Top/Middle/Lower) or tasks (POLC) with leadership STYLES.",
            "tier_2": "Autocratic, Democratic, Permissive (laissez-faire).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_management_levels_with_management_styles"],
    )


def arch_18_autocratic_style_features_pros_and_cons(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{mgr}** uses an **autocratic management style** at **{biz}** — deciding everything unilaterally and ordering workers what to do without input.\n\n"
        "(a) State **one genuine situation** where an autocratic style works well;\n"
        "(b) Give **two negative consequences** if **{0}** uses it every single day during normal trading.".format(mgr)
    )
    expected = (
        "(a) Genuine emergencies (fire/chemical spill), urgent crisis decisions, or strict repetitive safety tasks needing instant obedience. "
        "(b) 1) Low staff morale/resentment because voices are ignored; 2) High absenteeism/staff turnover and missed creative worker ideas."
    )
    sol = (
        f"**Evaluating the Autocratic Style ({mgr} at {biz}) [4 marks]:**\n\n"
        "**(a) When Useful [2 marks]:**\n"
        "During **urgent crises or safety emergencies** requiring instant action without debate, or with completely untrained staff needing strict step-by-step instructions **[2]**.\n\n"
        "**(b) Daily Disadvantages [2 marks]:**\n"
        "1. Workers feel distrusted and resentful, lowering morale **[1]**.\n"
        "2. Business loses creative improvements from experienced staff and suffers higher turnover **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_18",
        subskill="18_autocratic_style_features_pros_and_cons",
        title="Autocratic Management Style: When Valid & Risks",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "When is instant zero-debate command actually helpful (e.g. a fire or crisis), versus daily office morale?",
            "tier_2": "Pair crisis speed/safety with daily demotivation and lost employee ideas.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Valid situation: urgent crisis/emergency or strict safety compliance", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Consequence 1: low morale / resentment", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Consequence 2: higher staff turnover or missed worker ideas", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_autocratic_management_is_always_wrong_even_in_emergencies"],
    )


def arch_19_democratic_participatory_style_features_and_buy_in(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"Before redesigning customer service at **{biz}**, **{mgr}** holds open workshops where cashiers, packers, and drivers share practical ideas and vote on solutions.\n\n"
        "Why is this **democratic (participatory)** management style particularly effective for improving long-term staff commitment?"
    )
    correct = "Employees who participate in shaping decisions feel respected and motivated, take stronger ownership of outcomes, and contribute valuable frontline insights."
    distractors = [
        "Employees no longer need to arrive on time or perform any work.",
        "Managers pass 100% of legal accountability to customers.",
        "It forces every decision to take zero seconds without listening to workers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_19",
        subskill="19_democratic_participatory_style_features_and_buy_in",
        title="Democratic (Participatory) Style & Employee Buy-In",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Through **democratic/participatory** leadership, **{mgr}** builds employee buy-in, unlocks practical shopfloor solutions, and strengthens team commitment at **{biz}**."
        ),
        hints={
            "tier_1": "How do staff behave when their manager listens to and involves them?",
            "tier_2": "Higher motivation, ownership of decisions, and richer frontline ideas.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_democratic_input_with_zero_management_direction"],
    )


def arch_20_permissive_laissez_faire_free_rein_delegation(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    team = rng.choice(["senior software engineers", "qualified architectural designers", "experienced laboratory pharmacists"])
    prompt = (
        f"**{mgr}** leads a team of **{team}**, sets only the final project deadline, and grants them full freedom to decide **how** to complete their work (**permissive / free-rein / laissez-faire style**).\n\n"
        f"(a) Why can this delegation style succeed with **{team}**?\n"
        "(b) Why would using this same style fail badly with **newly hired, untrained teenagers on their first day**?"
    )
    expected = (
        f"(a) Skilled experts ({team}) possess deep expertise, self-discipline, and creativity, flourishing with autonomy. "
        "(b) Inexperienced newcomers lack skills and structure, causing confusion, errors, missed deadlines, and safety lapses."
    )
    sol = (
        f"**Permissive / Free-Rein (Laissez-Faire) Style ({team}) [4 marks]:**\n\n"
        f"**(a) Success with Experts [2 marks]:** Experienced specialists (**{team}**) already know technical standards, stay self-motivated, and innovate best without micromanagement **[2]**.\n\n"
        "**(b) Failure with Untrained Beginners [2 marks]:** Brand-new untrained workers need clear training, checklists, and guidance; total freedom leads to mistakes, wasted stock, and missed targets **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_20",
        subskill="20_permissive_laissez_faire_free_rein_delegation",
        title="Permissive (Free-Rein / Laissez-Faire) Delegation Style",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare self-directed experts against brand-new untrained beginners.",
            "tier_2": "Explain autonomy/creativity for specialists vs confusion/errors for beginners.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Experts are skilled, self-motivated, and thrive with freedom", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Beginners lack experience/direction causing errors and delays", "marks": 2, "editable": True},
        ],
        misconception_tags=["thinking_permissive_style_works_for_every_skill_level"],
    )


def arch_21_management_styles_situational_matching_table(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("A warehouse fire alarm sounds and staff need immediate evacuation orders", "Autocratic"),
        ("Marketing staff brainstorm fresh community ideas for a new product launch", "Democratic"),
        ("Senior software developers choose their own coding workflow to hit a target", "Permissive"),
        ("Urgent safety recall where a strict mandatory checklist must be followed immediately", "Autocratic"),
    ]
    chosen = rng.sample(cases, 3)
    headers = ["Workplace Situation", "Most Appropriate Management Style (Autocratic / Democratic / Permissive)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Workplace Situation | Most Appropriate Management Style |", "| :--- | :--- |"]
    for idx, (sit, style) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", sit, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = style
        cell_hints[c1] = "Enter: Autocratic, Democratic, or Permissive."
        memo_lines.append(f"| {sit} | {style} |")

    worked = "**Completed Situational Management Style Table [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{s} -> {st}" for s, st in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_21",
        subskill="21_management_styles_situational_matching_table",
        title="Situational Management Style Selection",
        prompt="Select the most appropriate management style (**Autocratic**, **Democratic**, or **Permissive**) for each South African workplace situation.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Crisis/strict safety = Autocratic; group brainstorming = Democratic; senior experts deciding how = Permissive.",
            "tier_2": "Use exact names: Autocratic, Democratic, or Permissive.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]} -> {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["recommending_permissive_style_during_fire_evacuation"],
    )


def arch_22_characteristics_of_a_good_manager_nine_traits(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{biz}** in **{area}** is interviewing candidates to lead a 20-person branch.\n\n"
        "Which trait combination **accurately** reflects the curriculum's **characteristics of a good manager**?"
    )
    correct = "Qualified, trustworthy, punctual and organised, takes responsibility, has good people skills, sets a good example, and keeps a positive attitude."
    distractors = [
        "Arrives late whenever possible, blames junior staff for errors, and avoids extra effort.",
        "Keeps secrets from the team, refuses qualification training, and discourages happy employees.",
        "Never communicates goals, delegates zero responsibility, and shouts at customers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_22",
        subskill="22_characteristics_of_a_good_manager_nine_traits",
        title="Core Characteristics of a Good Manager",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "A good manager is **qualified, trustworthy, punctual & organised, hardworking (extra effort), positive, takes responsibility, sets a good example, has good people skills, and keeps employees happy**."
        ),
        hints={
            "tier_1": "Eliminate traits showing lateness, blame-shifting, or poor communication.",
            "tier_2": "Look for accountability, people skills, punctuality, trustworthiness, and positive example.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_fear_and_blame_make_an_effective_manager"],
    )


def arch_23_good_manager_taking_responsibility_vs_blaming_staff(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    order_val = rng.choice([35000, 50000, 75000])
    prompt = (
        f"A major **{_fmt_r(order_val)}** client order at **{biz}** ships late because **{mgr}** approved an unrealistic delivery schedule without checking van availability. "
        f"Instead of blaming the drivers, **{mgr}** steps up, apologises to the client, takes responsibility, and fixes the dispatch checklist.\n\n"
        "Explain **two positive effects** when a manager **takes responsibility** and **sets a good example**."
    )
    expected = (
        "1) Builds trust and psychological safety so employees report problems early instead of hiding mistakes; "
        "2) Staff mirror the manager's honesty, discipline, and accountability, raising long-term team performance and client trust."
    )
    sol = (
        f"**Accountability & Leading by Example ({mgr}, {_fmt_r(order_val)} Order) [3 marks]:**\n\n"
        "1. **Trust & Open Problem-Solving:** Staff trust **{0}** rather than fearing unfair blame, so bottlenecks are flagged early **[1.5]**.\n".format(mgr)
        + "2. **Role-Model Culture & Client Confidence:** Workers copy honest, solution-focused habits, while clients regain trust in **{0}** **[1.5]**.".format(biz)
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_23",
        subskill="23_good_manager_taking_responsibility_vs_blaming_staff",
        title="Good Manager Trait: Taking Responsibility & Role-Modelling",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of how workers feel toward a boss who owns mistakes instead of scapegoating.",
            "tier_2": "Connect honesty/accountability -> trust + workers copying a good example.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Builds workplace trust and honest early problem reporting", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Staff mirror good example / client confidence restored", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["thinking_admitting_mistakes_weakens_authority"],
    )


def arch_24_good_manager_people_skills_and_keeping_staff_happy(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{mgr}** consistently listens respectfully to staff, recognises hard work, resolves conflicts calmly, and keeps employees happy and motivated at **{biz}**.\n\n"
        "Give **two measurable business benefits** of strong **people skills** and **high employee morale**."
    )
    expected = (
        "1) Lower absenteeism and staff turnover (saving hiring and retraining costs); "
        "2) Higher productivity, better teamwork, and friendlier service that retains loyal customers."
    )
    sol = (
        f"**Business Value of People Skills & Staff Morale ({biz}) [3 marks]:**\n\n"
        "1. **Lower Staff Turnover & Absenteeism:** Happy, respected staff stay longer, cutting expensive recruitment and retraining costs **[1.5]**.\n"
        "2. **Higher Productivity & Customer Care:** Motivated teams work faster, make fewer errors, and treat customers warmly, lifting repeat sales **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_24",
        subskill="24_good_manager_people_skills_and_keeping_staff_happy",
        title="People Skills, Employee Happiness & Productivity",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think about attendance, staff retention, productivity, and customer service.",
            "tier_2": "Link happy workers to lower turnover/absenteeism and better customer/output quality.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Lower absenteeism and staff turnover (lower hiring costs)", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Higher productivity and better customer service", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["viewing_employee_morale_as_unrelated_to_profits"],
    )


def arch_25_management_traits_matching_scenario_table(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    traits = [
        (f"{mgr} always opens briefings sharply at 07:30 with well-prepared agendas", "Punctual and organised"),
        (f"{mgr} protects confidential payroll records and keeps promises made to staff", "Trustworthy"),
        (f"{mgr} stays an extra hour without complaint to finish an urgent client audit", "Willing to put in extra effort"),
        (f"{mgr} owns up when a roster mistake happened and corrects it promptly", "Takes responsibility"),
    ]
    chosen = rng.sample(traits, 3)
    headers = ["Observed Manager Behaviour", "Matching Good-Manager Characteristic"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Observed Manager Behaviour | Characteristic |", "| :--- | :--- |"]
    for idx, (behav, trait) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", behav, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = trait
        cell_hints[c1] = "Choose: Punctual and organised, Trustworthy, Willing to put in extra effort, or Takes responsibility."
        memo_lines.append(f"| {behav} | {trait} |")

    worked = "**Completed Good-Manager Characteristics Schedule [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{b} -> {t}" for b, t in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_25",
        subskill="25_management_traits_matching_scenario_table",
        title="Good-Manager Traits Behaviour Audit",
        prompt=(
            "Match each workplace behaviour to the exact good-manager trait: "
            "**Punctual and organised**, **Trustworthy**, **Willing to put in extra effort**, or **Takes responsibility**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "07:30 agendas = Punctual & organised; confidentiality/promises = Trustworthy; extra hour = Extra effort; owning errors = Responsibility.",
            "tier_2": "Use the exact trait wording supplied in the prompt.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Matches row {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["confusing_trustworthy_with_takes_responsibility"],
    )


BUILDERS_01_25 = {
    "01_definition_and_purpose_of_management": arch_01_definition_and_purpose_of_management,
    "02_three_levels_of_management_pyramid_diagram": arch_02_three_levels_of_management_pyramid_diagram,
    "03_top_management_titles_and_strategic_horizon": arch_03_top_management_titles_and_strategic_horizon,
    "04_middle_management_departmental_bridging_role": arch_04_middle_management_departmental_bridging_role,
    "05_lower_first_line_management_operational_tasks": arch_05_lower_first_line_management_operational_tasks,
    "06_management_levels_classification_table": arch_06_management_levels_classification_table,
    "07_polc_four_management_tasks_overview": arch_07_polc_four_management_tasks_overview,
    "08_planning_task_definition_and_forecasting": arch_08_planning_task_definition_and_forecasting,
    "09_planning_vs_budget_forecast_calculation": arch_09_planning_vs_budget_forecast_calculation,
    "10_organising_task_delegation_and_resource_allocation": arch_10_organising_task_delegation_and_resource_allocation,
    "11_span_of_control_and_organising_ratio_calculation": arch_11_span_of_control_and_organising_ratio_calculation,
    "12_leading_task_communication_and_staff_motivation": arch_12_leading_task_communication_and_staff_motivation,
    "13_controlling_task_standards_and_corrective_action": arch_13_controlling_task_standards_and_corrective_action,
    "14_controlling_variance_calculation_actual_vs_budget": arch_14_controlling_variance_calculation_actual_vs_budget,
    "15_polc_management_tasks_scenario_table": arch_15_polc_management_tasks_scenario_table,
    "16_polc_interdependence_why_all_four_matter": arch_16_polc_interdependence_why_all_four_matter,
    "17_management_styles_three_types_overview": arch_17_management_styles_three_types_overview,
    "18_autocratic_style_features_pros_and_cons": arch_18_autocratic_style_features_pros_and_cons,
    "19_democratic_participatory_style_features_and_buy_in": arch_19_democratic_participatory_style_features_and_buy_in,
    "20_permissive_laissez_faire_free_rein_delegation": arch_20_permissive_laissez_faire_free_rein_delegation,
    "21_management_styles_situational_matching_table": arch_21_management_styles_situational_matching_table,
    "22_characteristics_of_a_good_manager_nine_traits": arch_22_characteristics_of_a_good_manager_nine_traits,
    "23_good_manager_taking_responsibility_vs_blaming_staff": arch_23_good_manager_taking_responsibility_vs_blaming_staff,
    "24_good_manager_people_skills_and_keeping_staff_happy": arch_24_good_manager_people_skills_and_keeping_staff_happy,
    "25_management_traits_matching_scenario_table": arch_25_management_traits_matching_scenario_table,
}
