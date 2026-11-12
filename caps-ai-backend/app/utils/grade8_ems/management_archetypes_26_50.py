"""Grade 8 EMS - Levels and functions of management: Archetypes 26 to 50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 3/02. Levels and functions of management.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES as PERSON_NAMES
from .management_archetypes_01_25 import (
    BUSINESS_NAMES,
    _build_mcq,
    _build_short,
    _build_table,
    _fmt_r,
    _make_cell,
)


def arch_26_good_manager_punctuality_and_organisation(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"At **{biz}**, **{mgr}** arrives 15 minutes early every day, prepares clear schedules, and never misses client deadlines.\n\n"
        "Why are **punctuality and personal organisation** critical traits of an effective manager?"
    )
    correct = "They set a professional standard for employees to copy, keep operations running on schedule, and build supplier and customer confidence."
    distractors = [
        "They guarantee a business pays zero corporate income tax.",
        "They allow the manager to abolish all planning and financial controlling.",
        "They automatically turn an informal tuckshop into a JSE Public Company.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_26",
        subskill="26_good_manager_punctuality_and_organisation",
        title="Good Manager Trait: Punctuality & Organisation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"When **{mgr}** models punctuality and neat preparation at **{biz}**, staff arrive on time, rosters stay smooth, and clients trust delivery promises."
        ),
        hints={
            "tier_1": "Think of how a punctual, organised boss shapes team habits and customer reliability.",
            "tier_2": "Sets an example for staff + keeps schedules reliable for clients.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_punctuality_applies_only_to_junior_staff"],
    )


def arch_27_good_manager_qualified_and_industry_knowledge(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    mgr = rng.choice(PERSON_NAMES)
    sector = rng.choice(["solar electrical engineering", "food safety and commercial baking", "financial bookkeeping and stock control"])
    prompt = (
        f"**{mgr}** manages a technical team specialising in **{sector}** in **{area}** and holds both formal qualifications and practical trade experience.\n\n"
        f"Give **two operational reasons** why being **well-qualified and knowledgeable** helps **{mgr}** manage effectively."
    )
    expected = (
        f"1) Enables accurate planning, cost estimating, and quality control of {sector} work; "
        "2) Earns staff respect so the manager can train apprentices and solve complex technical problems cleanly."
    )
    sol = (
        f"**Value of Managerial Qualifications & Knowledge ({mgr}) [3 marks]:**\n\n"
        f"1. **Sound Decisions & Quality Control:** Knowledge of **{sector}** helps spot errors early, quote accurately, and uphold safety standards **[1.5]**.\n"
        "2. **Staff Coaching & Credibility:** Qualified managers earn team respect and effectively mentor lower-level staff **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_27",
        subskill="27_good_manager_qualified_and_industry_knowledge",
        title="Why Good Managers Are Qualified & Knowledgeable",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Think about technical problem-solving and guiding trainees in {sector}.",
            "tier_2": "Mention smarter quality/budget decisions AND earning respect to train staff.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Enables sound planning, quality/safety checks, and problem-solving", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Builds team credibility and supports staff training/mentorship", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["thinking_managers_need_zero_technical_understanding"],
    )


def arch_28_good_manager_positive_attitude_and_extra_effort(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    peak = rng.choice(["back-to-school stationery rush", "December holiday catering surge", "unexpected machinery breakdown"])
    prompt = (
        f"During a high-pressure **{peak}** at **{biz}**, **{mgr}** stays calm with a **positive attitude** and **puts in extra effort** alongside the shift team until orders go out.\n\n"
        "Explain **two ways** this attitude lifts team resilience under stress."
    )
    expected = (
        "1) A calm, positive attitude prevents panic and keeps workers focused on constructive solutions; "
        "2) Seeing the manager work extra hours inspires mutual solidarity and pride rather than resentment."
    )
    sol = (
        f"**Positive Attitude & Extra Effort ({mgr} at {biz}) [3 marks]:**\n\n"
        "1. **Calm Problem-Solving:** Optimism reduces workplace panic during peak pressure so workers stay focused on quality **[1.5]**.\n"
        "2. **Shared Commitment:** When staff see leadership sacrificing alongside them, morale and teamwork stay strong **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_28",
        subskill="28_good_manager_positive_attitude_and_extra_effort",
        title="Positive Attitude & Extra Effort in Crisis Peaks",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Compare a calm, hardworking leader against a panicking boss during rush periods.",
            "tier_2": "Cover reduced stress/focus AND staff willingness to pull together.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Keeps team calm and focused under deadline pressure", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Visible extra effort inspires team solidarity and loyalty", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["underestimating_emotional_impact_of_manager_attitude"],
    )


def arch_29_chain_of_command_and_communication_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    ceo = rng.choice(PERSON_NAMES)
    mid = rng.choice([n for n in PERSON_NAMES if n != ceo])
    sup = rng.choice([n for n in PERSON_NAMES if n not in (ceo, mid)])
    biz = rng.choice(BUSINESS_NAMES)
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 245" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="245" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="22" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Chain of Command &amp; Two-Way Flow: {biz}</text>'
        '<rect x="190" y="38" width="260" height="44" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="320" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">Top: {ceo} (CEO)</text>'
        '<rect x="170" y="106" width="300" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="320" y="133" text-anchor="middle" font-size="12" font-weight="bold" fill="#14532d">Middle: {mid} (Operations Mgr)</text>'
        '<rect x="150" y="174" width="340" height="44" rx="6" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>'
        f'<text x="320" y="201" text-anchor="middle" font-size="12" font-weight="bold" fill="#9a3412">Lower: {sup} (Shift Supervisor)</text>'
        '<line x1="255" y1="82" x2="255" y2="106" stroke="#2563eb" stroke-width="2"/>'
        '<line x1="255" y1="150" x2="255" y2="174" stroke="#2563eb" stroke-width="2"/>'
        '<text x="118" y="130" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">Goals &amp; Policies v</text>'
        '<line x1="385" y1="174" x2="385" y2="150" stroke="#dc2626" stroke-width="2"/>'
        '<line x1="385" y1="106" x2="385" y2="82" stroke="#dc2626" stroke-width="2"/>'
        '<text x="530" y="130" text-anchor="middle" font-size="10" font-weight="bold" fill="#b91c1c">^ Daily Feedback</text>'
        '</svg>'
    )
    prompt = (
        f"Study the communication flow diagram for **{biz}** linking **{ceo}** (CEO), **{mid}** (Operations Manager), and **{sup}** (Shift Supervisor).\n\n"
        f"(a) Explain what moves **downward** from **{ceo}** through **{mid}** to **{sup}**;\n"
        f"(b) Explain why **upward feedback** from **{sup}** back to **{ceo}** is essential for **Controlling**."
    )
    expected = (
        f"(a) Downward: Strategic goals, company policies, departmental budgets, and task instructions. "
        f"(b) Upward: Frontline output figures, machine/stock faults, and customer feedback alert {ceo} and {mid} to variances so corrective steps happen promptly."
    )
    sol = (
        f"**Two-Way Chain of Command ({biz}) [4 marks]:**\n\n"
        f"**(a) Downward Communication ({ceo} -> {mid} -> {sup}) [2 marks]:**\n"
        "Conveys long-term strategy, policies, departmental targets, budgets, and operational standards **[2]**.\n\n"
        f"**(b) Upward Feedback ({sup} -> {mid} -> {ceo}) [2 marks]:**\n"
        f"Supplies actual daily performance reports, customer complaints, and bottlenecks from **{sup}** so **{mid}** and **{ceo}** can exercise **Controlling** and adjust targets **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_29",
        subskill="29_chain_of_command_and_communication_flow_diagram",
        title="Chain of Command & Two-Way Communication Diagram",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Read the downward blue arrows (left) and upward red arrows (right).",
            "tier_2": "Goals/policies go down; actual floor results/problems go up for Controlling.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Downward carries goals, policies, budgets, and instructions", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Upward delivers actual floor results/problems enabling Controlling", "marks": 2, "editable": True},
        ],
        misconception_tags=["thinking_communication_only_flows_downward"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_30_delegation_vs_abdication_of_responsibility(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    sub = rng.choice([n for n in PERSON_NAMES if n != mgr])
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"At **{biz}**, manager **{mgr}** delegates weekly inventory counting to assistant **{sub}**, and later an audit uncovers major stock errors.\n\n"
        "In sound management practice, who carries **final accountability** for the accuracy of the inventory?"
    )
    correct = f"{mgr} retains ultimate accountability for oversight and checking, even though {sub} is responsible for carrying out the delegated task properly."
    distractors = [
        f"Only {sub}, because delegation erases 100% of a manager's oversight duties.",
        "Neither person, because stock counts belong only to Parliament.",
        "Only customers who bought goods on Tuesday.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_30",
        subskill="30_delegation_vs_abdication_of_responsibility",
        title="Delegation vs Final Accountability",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Effective **delegation** passes task execution authority to **{sub}**, but **{mgr}** cannot abdicate overall supervisory **accountability**."
        ),
        hints={
            "tier_1": "Does delegating a task mean a manager stops checking or owning the outcome?",
            "tier_2": "Authority/task is delegated, but ultimate accountability stays with the manager.",
            "tier_3": correct,
        },
        misconception_tags=["believing_delegation_removes_manager_accountability"],
    )


def arch_31_comparing_time_horizons_and_scope_table(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Top Management", "Long-term (3 - 5+ years)", "Whole enterprise strategy and policies"),
        ("Middle Management", "Medium-term (Months to 1 year)", "Specific functional department (e.g. Finance / Marketing)"),
        ("Lower Management", "Short-term (Daily to weekly)", "Frontline team/shift operational supervision"),
    ]
    rng.shuffle(pool)
    headers = ["Management Level", "Typical Time Horizon", "Organisational Scope"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Management Level | Typical Time Horizon | Organisational Scope |", "| :--- | :--- | :--- |"]
    for idx, (lvl, hor, scope) in enumerate(pool):
        c1 = f"r{idx}c1"
        c2 = f"r{idx}c2"
        rows.append([
            _make_cell(f"r{idx}c0", lvl, "given"),
            _make_cell(c1, "", "required"),
            _make_cell(c2, "", "required"),
        ])
        correct_map[c1] = hor
        correct_map[c2] = scope
        cell_hints[c1] = "Long-term (3 - 5+ years), Medium-term (Months to 1 year), or Short-term (Daily to weekly)."
        cell_hints[c2] = "Whole enterprise, Specific department, or Frontline team/shift."
        memo_lines.append(f"| {lvl} | {hor} | {scope} |")

    worked = "**Completed Management Horizon & Scope Table [6 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{l}: {h} | {s}" for l, h, s in pool)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_31",
        subskill="31_comparing_time_horizons_and_scope_table",
        title="Time Horizons & Organisational Scope by Level",
        prompt="Complete each row contrasting **Top**, **Middle**, and **Lower** management by entering their **Time Horizon** and **Organisational Scope**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Top looks furthest ahead across the entire firm; Lower runs daily frontline work.",
            "tier_2": "Match Top->Long-term/Whole firm, Middle->Medium-term/Department, Lower->Short-term/Frontline shift.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{pool[i][0]}: {pool[i][1]} & {pool[i][2]}", "marks": 2, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["mixing_time_horizons_of_middle_and_lower_managers"],
    )


def arch_32_managing_across_business_functions_overview(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    func_pair = rng.choice([
        ("Marketing, Production, Finance, and Human Resources", "departmental heads coordinating under Middle Management"),
        ("Administration, Marketing, Purchasing, and Finance", "functional units aligned to Top Management's goals"),
    ])
    prompt = (
        f"Inside **{biz}**, specialists lead **{func_pair[0]}**.\n\n"
        "Where do these functional department heads sit in the management hierarchy, and how do they link business functions together?"
    )
    correct = "They serve as Middle-level managers translating corporate strategy into functional targets and coordinating workflows across departments."
    distractors = [
        "They are external SARS tax inspectors auditing private households.",
        "They work independently with zero communication with Top or Lower managers.",
        "They act strictly as Lower-level receptionists sweeping floors.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_32",
        subskill="32_managing_across_business_functions_overview",
        title="Coordinating Functional Departments via Middle Management",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Functional heads (**{func_pair[0]}**) represent **Middle Management**, aligning specialized teams toward Top Management's enterprise objectives."
        ),
        hints={
            "tier_1": "Marketing, Finance, HR, and Production heads each run one department.",
            "tier_2": "Departmental heads = Middle Management coordinating specialised functions.",
            "tier_3": correct,
        },
        misconception_tags=["treating_departmental_managers_as_non_managers"],
    )


def arch_33_marketing_manager_polc_application(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    product = rng.choice(["eco-friendly cleaning refills", "solar rechargeable lamps", "fortified sorghum cereal"])
    prompt = (
        f"**{mgr}** is the Marketing Manager at **{biz}** launching **{product}** across three provinces.\n\n"
        "Describe **one concrete marketing action** for each of **Planning**, **Organising**, **Leading**, and **Controlling** during this launch."
    )
    expected = (
        f"Planning: Set a quarterly sales target for {product} and choose promotional channels. "
        "Organising: Assign sales reps to provinces and allocate promo budgets/stands. "
        "Leading: Brief, coach, and motivate sales reps to hit launch targets. "
        "Controlling: Track weekly sales against targets and adjust ads where sales lag."
    )
    sol = (
        f"**POLC Applied to Marketing Launch ({product}) [4 marks]:**\n\n"
        f"- **Planning:** Research buyers, set target sales volumes for **{product}**, and decide launch steps **[1]**.\n"
        "- **Organising:** Assign regional sales teams, allocate promotional budgets, and distribute display samples **[1]**.\n"
        "- **Leading:** Coach, inspire, and communicate launch enthusiasm to sales representatives **[1]**.\n"
        "- **Controlling:** Compare actual weekly sales against budgeted targets and adjust promotions if sales underperform **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_33",
        subskill="33_marketing_manager_polc_application",
        title="Applying POLC to a Marketing Launch",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Write one crisp action starting with Goals (P), Teams/Budget (O), Motivating Reps (L), and Checking Sales (C).",
            "tier_2": "Cover all 4 POLC letters specifically in the marketing context.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Valid Marketing Planning action", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Valid Marketing Organising action", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Valid Marketing Leading action", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Valid Marketing Controlling action", "marks": 1, "editable": True},
        ],
        misconception_tags=["describing_general_polc_definitions_without_marketing_context"],
    )


def arch_34_production_manager_quality_and_safety_control(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    total_units = rng.choice([2000, 2500, 4000])
    max_defect_pct = 2
    max_allowed = total_units * max_defect_pct // 100
    actual_defects = max_allowed + rng.choice([25, 35, 45])

    prompt = (
        f"**{biz}** manufactures **{total_units:,} bottled packs** today. Its quality-control standard permits at most **{max_defect_pct}% defective units**.\n"
        f"During inspection, supervisors count **{actual_defects} defective packs**.\n\n"
        "(a) Calculate the **maximum allowed defective packs** under standard;\n"
        "(b) Did today's shift **pass or fail** quality control, and what **Controlling step** must the Production Manager take immediately?"
    )
    expected = (
        f"(a) Max allowed = {max_allowed} packs. "
        f"(b) Failed ({actual_defects} > {max_allowed}); halt/inspect sealing machinery, retrain operators, and remove faulty packs."
    )
    sol = (
        f"**Production Quality Control Audit ({biz}) [4 marks]:**\n\n"
        f"**(a) Maximum Allowed Defects ({max_defect_pct}%):**\n"
        f"$${total_units:,} \\times {max_defect_pct}\\% = {max_allowed}\\text{{ packs}}$$ **[2]**\n\n"
        "**(b) Inspection Verdict & Corrective Action:**\n"
        f"- **Verdict:** **Failed** quality standard (**{actual_defects} defects** exceeds the limit of **{max_allowed}**) **[1]**.\n"
        "- **Corrective Action:** Inspect/recalibrate packaging machines immediately, retrain shift workers, and quarantine faulty units **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_34",
        subskill="34_production_manager_quality_and_safety_control",
        title="Production Quality Control Threshold Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Compute {max_defect_pct}% of {total_units:,} first.",
            "tier_2": f"Compare actual ({actual_defects}) to limit ({max_allowed}) and prescribe corrective action.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Max allowed defects = {max_allowed}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Concludes FAIL (actual exceeds limit)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Concrete corrective fix (machine calibration/training)", "marks": 1, "editable": True},
        ],
        misconception_tags=["computing_20_percent_instead_of_2_percent"],
        qtype="calculation",
    )


def arch_35_finance_manager_cash_budget_and_controlling(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    bud_sales = rng.choice([300000, 360000, 420000])
    bud_exp = rng.choice([210000, 240000, 270000])
    bud_profit = bud_sales - bud_exp

    act_sales = bud_sales - rng.choice([20000, 30000])
    act_exp = bud_exp + rng.choice([15000, 25000])
    act_profit = act_sales - act_exp
    profit_gap = bud_profit - act_profit

    prompt = (
        f"The Finance Manager at **{biz}** reviews quarterly performance:\n"
        f"- **Budgeted:** Sales **{_fmt_r(bud_sales)}**, Expenses **{_fmt_r(bud_exp)}**\n"
        f"- **Actual:** Sales **{_fmt_r(act_sales)}**, Expenses **{_fmt_r(act_exp)}**\n\n"
        "(a) Calculate **budgeted profit** and **actual profit**;\n"
        "(b) By how much did actual profit **fall short** of the planned target?"
    )
    expected = (
        f"(a) Budgeted profit = {_fmt_r(bud_profit)}; Actual profit = {_fmt_r(act_profit)}; "
        f"(b) Shortfall = {_fmt_r(profit_gap)}"
    )
    sol = (
        f"**Financial Control Profit Variance ({biz}) [4 marks]:**\n\n"
        "**(a) Budgeted vs Actual Profit:**\n"
        f"- **Budgeted Profit:** ${_fmt_r(bud_sales)} - {_fmt_r(bud_exp)} = {_fmt_r(bud_profit)}$ **[1]**\n"
        f"- **Actual Profit:** ${_fmt_r(act_sales)} - {_fmt_r(act_exp)} = {_fmt_r(act_profit)}$ **[1]**\n\n"
        "**(b) Profit Shortfall:**\n"
        f"$${_fmt_r(bud_profit)} - {_fmt_r(act_profit)} = {_fmt_r(profit_gap)}$$ *(lower sales combined with overspent expenses)* **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_35",
        subskill="35_finance_manager_cash_budget_and_controlling",
        title="Financial Controlling: Budgeted vs Actual Profit",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Profit = Sales minus Expenses for each column separately.",
            "tier_2": "Subtract Actual Profit from Budgeted Profit to get the shortfall.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Budgeted profit = {_fmt_r(bud_profit)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Actual profit = {_fmt_r(act_profit)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Profit shortfall = {_fmt_r(profit_gap)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["comparing_sales_only_while_ignoring_higher_expenses"],
        qtype="calculation",
    )


def arch_36_hr_manager_training_and_staff_retention(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"**{biz}** in **{area}** loses 40% of newly hired staff within 6 months because workers feel undertrained and unsupported.\n\n"
        "State **two HR management actions** (reflecting good management traits and **Leading/Organising**) that will improve **staff retention**."
    )
    expected = (
        "1) Provide structured onboarding and skills training so new hires feel confident and competent (Organising/Training); "
        "2) Hold regular supportive check-ins, listen with strong people skills, and recognise achievements to keep employees happy (Leading)."
    )
    sol = (
        f"**HR Retention Strategy ({biz}) [3 marks]:**\n\n"
        "1. **Structured Induction & Skills Training (Organising):** Pair new hires with mentors and clear checklists so expectations are clear **[1.5]**.\n"
        "2. **People Skills, Fair Support & Recognition (Leading):** Keep staff happy through supportive feedback, fair workloads, and recognition **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_36",
        subskill="36_hr_manager_training_and_staff_retention",
        title="HR Management: Onboarding, Training & Retention",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of why new hires quit (poor training & low support) and solve both.",
            "tier_2": "Pair structured training/onboarding with supportive people-focused leadership.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Structured induction / skills training / mentorship", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Supportive communication, people skills, and recognition", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_money_alone_explains_early_staff_turnover"],
    )


def arch_37_departmental_staffing_and_shift_scheduling_calc(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    shifts_per_day = 2
    staff_per_shift = rng.choice([6, 8, 9])
    hourly_wage = rng.choice([45, 50, 60])
    hours_per_shift = 8
    daily_staff_shifts = shifts_per_day * staff_per_shift
    daily_wage_bill = daily_staff_shifts * hours_per_shift * hourly_wage

    prompt = (
        f"When **Organising** daily operations for a retail hub in **{area}**, the manager schedules **{shifts_per_day} shifts per day** (8 hours each), "
        f"requiring **{staff_per_shift} workers on duty per shift** at **{_fmt_r(hourly_wage)} per hour**.\n\n"
        "Calculate:\n"
        "(a) Total **worker-shifts worked per day**;\n"
        "(b) The **total daily wage bill** to budget for."
    )
    expected = f"(a) {daily_staff_shifts} worker-shifts/day; (b) Daily wage bill = {_fmt_r(daily_wage_bill)}"
    sol = (
        f"**Shift Staffing & Wage Budget ({area}) [3 marks]:**\n\n"
        f"**(a) Daily Worker-Shifts:** ${shifts_per_day} \\times {staff_per_shift} = {daily_staff_shifts}\\text{{ worker-shifts}}$ **[1]**\n\n"
        "**(b) Total Daily Wage Cost:**\n"
        f"$${daily_staff_shifts} \\times {hours_per_shift}\\text{{ hours}} \\times {_fmt_r(hourly_wage)} = {_fmt_r(daily_wage_bill)}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_37",
        subskill="37_departmental_staffing_and_shift_scheduling_calc",
        title="Organising Shifts & Calculating Daily Wage Budgets",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Multiply {shifts_per_day} shifts x {staff_per_shift} workers for total shifts.",
            "tier_2": f"Multiply daily worker-shifts x {hours_per_shift} hours x {_fmt_r(hourly_wage)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Daily worker-shifts = {daily_staff_shifts}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Daily wage bill = {_fmt_r(daily_wage_bill)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_to_multiply_by_8_hours_per_shift"],
        qtype="calculation",
    )


def arch_38_comparing_autocratic_democratic_permissive_table(rng: random.Random) -> Dict[str, Any]:
    styles = [
        ("Autocratic", "None (manager dictates alone)", "Genuine crises / urgent safety compliance"),
        ("Democratic", "High (shared discussion & ideas)", "Routine team improvements & problem-solving"),
        ("Permissive (Free-rein)", "Full operational autonomy", "Highly skilled, self-motivated experts"),
    ]
    rng.shuffle(styles)
    headers = ["Management Style", "Employee Participation Level", "Best Workplace Situation"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Management Style | Employee Participation | Best Situation |", "| :--- | :--- | :--- |"]
    for idx, (st, part, sit) in enumerate(styles):
        c1 = f"r{idx}c1"
        c2 = f"r{idx}c2"
        rows.append([
            _make_cell(f"r{idx}c0", st, "given"),
            _make_cell(c1, "", "required"),
            _make_cell(c2, "", "required"),
        ])
        correct_map[c1] = part
        correct_map[c2] = sit
        cell_hints[c1] = "State None, High participation, or Full autonomy."
        cell_hints[c2] = "Crises/safety, Routine team decisions, or Skilled specialists."
        memo_lines.append(f"| {st} | {part} | {sit} |")

    worked = "**Completed Management Styles Comparison [6 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{st}: {p} | {s}" for st, p, s in styles)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_38",
        subskill="38_comparing_autocratic_democratic_permissive_table",
        title="Comparison Matrix: Three Management Styles",
        prompt="Compare **Autocratic**, **Democratic**, and **Permissive (Free-rein)** styles by completing their **Employee Participation Level** and **Best Workplace Situation**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Autocratic = manager decides alone; Democratic = team input; Permissive = expert autonomy.",
            "tier_2": "Fill participation level and ideal context concisely per row.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{styles[i][0]}: {styles[i][1]} & {styles[i][2]}", "marks": 2, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["mixing_democratic_and_permissive_involvement"],
    )


def arch_39_blended_adaptive_leadership_by_situation(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"During one week at **{biz}**, manager **{mgr}** gives sharp, unquestioned commands when a chemical drum leaks (**Monday**), "
        "runs a brainstorming session with cashiers on queue flow (**Wednesday**), and lets a senior web designer choose their own design software (**Friday**).\n\n"
        f"Does **{mgr}** show inconsistency or adaptive management skill? Identify all three styles used and justify your view."
    )
    expected = (
        f"Adaptive skill: Monday = Autocratic (urgent safety), Wednesday = Democratic (staff buy-in & ideas), Friday = Permissive (expert autonomy). "
        "Great managers match style to urgency and team skill level."
    )
    sol = (
        f"**Adaptive Situational Management ({mgr} at {biz}) [4 marks]:**\n\n"
        "- **Assessment:** Shows **adaptability**, not inconsistency **[1]**.\n"
        "- **Monday (Safety Leak):** **Autocratic** — fast command protects lives without debate **[1]**.\n"
        "- **Wednesday (Queue Flow):** **Democratic** — gathers valuable frontline ideas and morale **[1]**.\n"
        "- **Friday (Senior Web Designer):** **Permissive / Laissez-faire** — empowers skilled specialist autonomy **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_39",
        subskill="39_blended_adaptive_leadership_by_situation",
        title="Adaptive Leadership: Matching Style to Context",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Identify which style fits Monday, Wednesday, and Friday respectively.",
            "tier_2": "Explain why matching style to risk/skill proves strong adaptive leadership.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Concludes adaptive leadership skill", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Monday = Autocratic (safety speed)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Wednesday = Democratic (staff participation)", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Friday = Permissive (expert autonomy)", "marks": 1, "editable": True},
        ],
        misconception_tags=["believing_a_manager_must_use_only_one_style_forever"],
    )


def arch_40_ethical_conduct_and_setting_good_example(rng: random.Random) -> Dict[str, Any]:
    mgr = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"One of the nine good-manager characteristics is **setting a good example** and staying **trustworthy**.\n\n"
        f"If **{mgr}** quietly asks staff at **{biz}** to alter expiry dates on stock to hide losses, how does this breach good management?"
    )
    correct = "It destroys trustworthiness, sets an unethical example for employees to imitate, endangers customers, and invites legal liability."
    distractors = [
        "It qualifies as effective Controlling because costs appear lower temporarily.",
        "It exemplifies Democratic participation because staff joined in.",
        "It has zero risk because managers never bear responsibility for shopfloor ethics.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_40",
        subskill="40_ethical_conduct_and_setting_good_example",
        title="Ethical Leadership & Setting a Good Example",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Unethical orders from **{mgr}** destroy **trustworthiness** and **good role-modelling**, damaging staff culture, customer safety, and **{biz}**'s survival."
        ),
        hints={
            "tier_1": "Ask: What happens to trust, ethics, and reputation when a boss models dishonesty?",
            "tier_2": "Violates trustworthiness and setting a good example.",
            "tier_3": correct,
        },
        misconception_tags=["equating_short_term_deception_with_clever_controlling"],
    )


def arch_41_conflict_resolution_and_people_skills_case(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.choice(PERSON_NAMES)
    w2 = rng.choice([n for n in PERSON_NAMES if n != w1])
    mgr = rng.choice([n for n in PERSON_NAMES if n not in (w1, w2)])
    prompt = (
        f"Two cashiers, **{w1}** and **{w2}**, argue loudly near customers over unfair weekend shift rotations.\n\n"
        f"Explain **two constructive steps** manager **{mgr}** should take using **good people skills** and **Organising/Controlling** to resolve the dispute fairly."
    )
    expected = (
        f"1) Move {w1} and {w2} away from customers to a private office and listen calmly to both sides objectively (people skills & trustworthiness); "
        "2) Review and publish a transparent, fair rotating weekend roster so shifts are equal and auditable going forward (Organising)."
    )
    sol = (
        f"**Fair Workplace Conflict Resolution ({mgr}) [3 marks]:**\n\n"
        f"1. **Private Active Listening (People Skills):** Speak calmly with **{w1}** and **{w2}** privately away from shoppers, listening fairly without bias **[1.5]**.\n"
        "2. **Transparent Roster Fix (Organising):** Create a written rotating weekend schedule checked regularly so workloads stay demonstrably fair **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_41",
        subskill="41_conflict_resolution_and_people_skills_case",
        title="Applying People Skills to Resolve Shift Conflict",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Separate how you calm the two people now from how you prevent unfair rosters next week.",
            "tier_2": "Combine private unbiased listening with a transparent rotating roster system.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Private, calm, unbiased listening to both workers", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Transparent, fair rotating schedule to prevent repeat disputes", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["disciplining_staff_publicly_in_front_of_customers"],
    )


def arch_42_productivity_efficiency_output_per_worker_calc(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    workers = rng.choice([10, 12, 15])
    old_total = workers * rng.choice([20, 25])
    old_per = old_total // workers
    gain_pct = rng.choice([20, 25])
    new_per = old_per + (old_per * gain_pct // 100)
    new_total = workers * new_per

    prompt = (
        f"At **{biz}**, **{workers} packers** previously packed **{old_total} parcels per day**.\n"
        f"After Lower Management improves workstation organisation (**Organising**) and coaches teams (**Leading**), total daily output rises to **{new_total} parcels per day** with the same **{workers} workers**.\n\n"
        "(a) Calculate output **per worker** before and after the change;\n"
        "(b) Calculate the **percentage increase** in labour productivity."
    )
    expected = (
        f"(a) Before = {old_per} parcels/worker; After = {new_per} parcels/worker; "
        f"(b) Productivity gain = {gain_pct}%"
    )
    sol = (
        f"**Productivity Improvement Calculation ({biz}) [4 marks]:**\n\n"
        "**(a) Output per Worker:**\n"
        f"- **Before:** ${old_total} \\div {workers} = {old_per}\\text{{ parcels/worker}}$ **[1]**\n"
        f"- **After:** ${new_total} \\div {workers} = {new_per}\\text{{ parcels/worker}}$ **[1]**\n\n"
        "**(b) Percentage Productivity Gain:**\n"
        f"$$\\frac{{{new_per} - {old_per}}}{{{old_per}}} \\times 100\\% = \\frac{{{new_per - old_per}}}{{{old_per}}} \\times 100\\% = {gain_pct}\\%$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_42",
        subskill="42_productivity_efficiency_output_per_worker_calc",
        title="Measuring Managerial Productivity Gains",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Divide total output before and after by {workers} workers.",
            "tier_2": "Percentage increase = (New - Old) / Old x 100%.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Before = {old_per}, After = {new_per}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Percentage productivity gain = {gain_pct}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_to_divide_output_by_number_of_workers"],
        qtype="calculation",
    )


def arch_43_overtime_cost_control_and_planning_calc(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    base_rate = rng.choice([60, 80, 100])
    ot_rate = base_rate * 3 // 2  # 1,5x overtime
    ot_hours = rng.choice([40, 50, 60])
    extra_ot_cost = ot_hours * ot_rate
    normal_cost = ot_hours * base_rate
    penalty_premium = extra_ot_cost - normal_cost

    prompt = (
        f"Because a manager at **{biz}** neglected advance **Planning** of stock levels, workers had to work **{ot_hours} urgent overtime hours** "
        f"at **{_fmt_r(ot_rate)}/hour** instead of the normal wage rate of **{_fmt_r(base_rate)}/hour**.\n\n"
        "(a) Calculate the **total overtime wage bill** paid;\n"
        "(b) Calculate the **extra avoidable premium cost** caused purely by poor planning."
    )
    expected = f"(a) Overtime bill = {_fmt_r(extra_ot_cost)}; (b) Extra avoidable premium = {_fmt_r(penalty_premium)}"
    sol = (
        f"**Avoidable Overtime Cost of Poor Planning ({biz}) [3 marks]:**\n\n"
        f"**(a) Total Overtime Cost:** ${ot_hours} \\times {_fmt_r(ot_rate)} = {_fmt_r(extra_ot_cost)}$ **[1.5]**\n\n"
        "**(b) Avoidable Overtime Premium:**\n"
        f"$$({_fmt_r(ot_rate)} - {_fmt_r(base_rate)}) \\times {ot_hours} = {_fmt_r(ot_rate - base_rate)} \\times {ot_hours} = {_fmt_r(penalty_premium)}$$ **[1.5]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_43",
        subskill="43_overtime_cost_control_and_planning_calc",
        title="Financial Cost of Poor Advance Planning (Overtime)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Multiply {ot_hours} hours by the overtime rate ({_fmt_r(ot_rate)}).",
            "tier_2": "Subtract normal-rate pay for those same hours to isolate the extra penalty.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total overtime bill = {_fmt_r(extra_ot_cost)}", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": f"Avoidable extra premium = {_fmt_r(penalty_premium)}", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["reporting_total_overtime_as_premium_without_subtracting_normal_rate"],
        qtype="calculation",
    )


def arch_44_feedback_loop_bottom_up_to_top_management(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    prompt = (
        f"Frontline cashiers at **{biz}**'s **{area}** store notice customers repeatedly abandoning long queues because barcode scanners freeze.\n\n"
        "Why must **Top Management** maintain open **upward feedback channels** from Lower managers and frontline staff?"
    )
    correct = "Frontline supervisors spot operational faults and shifting customer needs first; listening upward lets executives fix root causes and improve strategic decisions."
    distractors = [
        "So Top executives can immediately blame cashiers for faulty barcode hardware.",
        "Because Top managers legally belong inside the Lower management pyramid tier.",
        "To eliminate the need for Middle Management departments completely.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_44",
        subskill="44_feedback_loop_bottom_up_to_top_management",
        title="Value of Upward Operational Feedback",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Upward feedback from **{area}**'s floor team alerts Middle and Top leaders to urgent scanner bottlenecks before sales drop further."
        ),
        hints={
            "tier_1": "Who hears customer complaints and sees malfunctioning tools first each morning?",
            "tier_2": "Upward information connects shopfloor reality to executive fixes.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_top_executives_never_need_frontline_input"],
    )


def arch_45_management_level_and_polc_matrix_table(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("CEO sets a 5-year goal to open 10 solar plants nationwide", "Top", "Planning"),
        ("HR Manager divides recruiting staff into interview panels and assigns budgets", "Middle", "Organising"),
        ("Shift Foreman inspects daily stitched uniforms and fixes machine tension errors", "Lower", "Controlling"),
    ]
    rng.shuffle(items)
    headers = ["Business Scenario", "Management Level (Top / Middle / Lower)", "Management Task (Planning / Organising / Leading / Controlling)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Business Scenario | Management Level | Management Task |", "| :--- | :--- | :--- |"]
    for idx, (scen, lvl, task) in enumerate(items):
        c1 = f"r{idx}c1"
        c2 = f"r{idx}c2"
        rows.append([
            _make_cell(f"r{idx}c0", scen, "given"),
            _make_cell(c1, "", "required"),
            _make_cell(c2, "", "required"),
        ])
        correct_map[c1] = lvl
        correct_map[c2] = task
        cell_hints[c1] = "Top, Middle, or Lower."
        cell_hints[c2] = "Planning, Organising, Leading, or Controlling."
        memo_lines.append(f"| {scen} | {lvl} | {task} |")

    worked = "**Completed Dual Level & POLC Matrix [6 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{s} -> {l}, {t}" for s, l, t in items)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_45",
        subskill="45_management_level_and_polc_matrix_table",
        title="Dual Audit: Management Level & POLC Function",
        prompt="Identify **both** the **Management Level** (**Top**, **Middle**, or **Lower**) and the **POLC Management Task** (**Planning**, **Organising**, **Leading**, or **Controlling**) in each scenario.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Match scope/person (CEO/HR/Foreman) to Level, and activity (goals/dividing resources/inspecting errors) to POLC.",
            "tier_2": "Keep both columns concise using exact labels.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{items[i][0]} -> {items[i][1]} / {items[i][2]}", "marks": 2, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["swapping_level_and_task_columns"],
    )


def arch_46_poor_management_warning_signs_and_fixes(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    symptom = rng.choice(["high employee resignation rates, missed supplier deadlines, and repeated budget overspending", "frequent customer complaints, idle equipment, and unpaid overtime surges"])
    prompt = (
        f"A quarterly review at **{biz}** shows **{symptom}**.\n\n"
        "Diagnose **two distinct management breakdowns** (citing POLC functions or management traits) causing these warning signs and recommend a specific fix for each."
    )
    expected = (
        "1) Weak Planning & Controlling: missed deadlines and budget overruns arise from poor forecasting and failing to monitor variances; fix with clear target schedules and weekly variance reviews. "
        "2) Weak Leading & People Skills: staff turnover/complaints come from autocratic neglect or unmotivated teams; fix with supportive coaching and democratic listening."
    )
    sol = (
        f"**Management Failure Diagnosis ({biz}) [4 marks]:**\n\n"
        "1. **Deadlines & Cost Overruns (Planning / Controlling Gap):** Caused by unclear timelines and unmonitored spending; **Fix:** introduce realistic budgets and weekly variance checks **[2]**.\n"
        "2. **High Turnover & Complaints (Leading / People-Skills Gap):** Staff leave when unsupported or unheard; **Fix:** build regular recognition, coaching, and two-way communication **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_46",
        subskill="46_poor_management_warning_signs_and_fixes",
        title="Diagnosing & Fixing Poor Management Symptoms",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Link each business symptom back to either Planning/Organising/Controlling or Leading/People skills.",
            "tier_2": "Give two root causes paired with concrete corrective remedies.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Diagnosis 1 + fix targeting Planning/Organising/Controlling", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Diagnosis 2 + fix targeting Leading/People Skills/Traits", "marks": 2, "editable": True},
        ],
        misconception_tags=["blaming_workers_alone_for_systemic_management_failures"],
    )


def arch_47_entrepreneur_transitioning_from_doing_to_managing(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    area = rng.choice(AREAS)
    staff = rng.choice([14, 18, 22])
    prompt = (
        f"**{founder}** started a craft bakery in **{area}** baking everything alone. Five years later, **{founder}** employs **{staff} staff**, "
        "yet still tries to mix dough, drive every delivery, and handle every till personally — leaving staff standing idle waiting for instructions.\n\n"
        "Which management shift must **{0}** make immediately so the growing enterprise succeeds?".format(founder)
    )
    correct = "Transition from doing all manual work personally to Planning, Organising (delegating clear roles to supervisors), Leading, and Controlling team performance."
    distractors = [
        "Fire all 18 employees so there is nobody to delegate to.",
        "Switch to an extreme permissive style where nobody receives training or targets.",
        "Convert the bakery into a national government ministry.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_mgt_47",
        subskill="47_entrepreneur_transitioning_from_doing_to_managing",
        title="Entrepreneur Shift: From Sole Worker to Manager",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"As an enterprise scales to **{staff} staff**, **{founder}** must delegate daily execution and invest energy in **Planning, Organising, Leading, and Controlling**."
        ),
        hints={
            "tier_1": "Why are staff standing idle while the founder tries to do every physical chore alone?",
            "tier_2": "Effective scaling requires delegation (Organising) and active management (POLC).",
            "tier_3": correct,
        },
        misconception_tags=["thinking_great_founders_never_delegate_technical_work"],
    )


def arch_48_team_incentive_bonus_and_leading_motivation_calc(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    target = rng.choice([1000, 1200, 1500])
    extra = rng.choice([200, 300, 400])
    actual = target + extra
    bonus_per_unit = rng.choice([15, 20, 25])
    workers = rng.choice([10, 12, 15])
    # ensure integer division nicely:
    total_bonus = extra * bonus_per_unit
    while total_bonus % workers != 0:
        workers += 1
    each_bonus = total_bonus // workers

    prompt = (
        f"To **Lead** and motivate staff at **{biz}**, management promises a team bonus of **{_fmt_r(bonus_per_unit)}** for every pack produced **above** the monthly target of **{target:,} packs**. "
        f"This month, the **{workers}-person team** produces **{actual:,} packs**.\n\n"
        "(a) Calculate the **number of bonus-qualifying packs** above target;\n"
        "(b) Calculate the **total team bonus pool** and the **equal payout per worker**."
    )
    expected = (
        f"(a) {extra} packs above target; "
        f"(b) Team bonus pool = {_fmt_r(total_bonus)}; Payout per worker = {_fmt_r(each_bonus)}"
    )
    sol = (
        f"**Motivating Team Incentive Calculation ({biz}) [4 marks]:**\n\n"
        f"**(a) Packs Above Target:** ${actual:,} - {target:,} = {extra}\\text{{ packs}}$ **[1]**\n\n"
        "**(b) Team Bonus Pool & Per-Worker Payout:**\n"
        f"- **Total bonus pool:** ${extra} \\times {_fmt_r(bonus_per_unit)} = {_fmt_r(total_bonus)}$ **[1.5]**\n"
        f"- **Each worker ({workers} staff):** ${_fmt_r(total_bonus)} \\div {workers} = {_fmt_r(each_bonus)}$ **[1.5]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_48",
        subskill="48_team_incentive_bonus_and_leading_motivation_calc",
        title="Leading Through Performance Bonuses Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "First subtract target from actual units to find ONLY the surplus units.",
            "tier_2": f"Multiply surplus units by {_fmt_r(bonus_per_unit)}, then divide equally by {workers}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Extra packs = {extra}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total bonus pool = {_fmt_r(total_bonus)}", "marks": 1.5, "editable": True},
            {"id": "mp_3", "desc": f"Per-worker payout = {_fmt_r(each_bonus)}", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["paying_bonus_on_entire_output_instead_of_surplus_above_target"],
        qtype="calculation",
    )


def arch_49_management_misconception_error_audit_table(rng: random.Random) -> Dict[str, Any]:
    myths = [
        ("Shift supervisors and floor foremen belong to Top Management.", "Lower (First-line) Management supervising daily operations"),
        ("Democratic management means workers do anything they wish without manager oversight.", "Managers collaborate and participate WITH staff while keeping clear goals"),
        ("Controlling only means punishing employees after rules are broken.", "Measuring performance against standards and taking constructive corrective steps"),
        ("Permissive (laissez-faire) style works best for untrained beginners on day one.", "Works best with skilled, experienced specialists; beginners need structured direction"),
    ]
    chosen = rng.sample(myths, 3)
    headers = ["Incorrect Management Myth", "Factual EMS Correction"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Incorrect Management Myth | Factual EMS Correction |", "| :--- | :--- |"]
    for idx, (myth, fix) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", myth, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = fix
        cell_hints[c1] = "State the accurate management fact correcting this claim."
        memo_lines.append(f"| {myth} | {fix} |")

    worked = "**Completed Management Misconception Audit [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{m} -> {f}" for m, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_mgt_49",
        subskill="49_management_misconception_error_audit_table",
        title="Management Concepts Misconception Audit",
        prompt="Identify the error in each statement and write the **accurate management fact** in column 2.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Check levels (Top/Middle/Lower), styles (Democratic/Permissive), and POLC (Controlling).",
            "tier_2": "Write concise factual corrections.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Correction row {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["confusing_democratic_style_with_lack_of_leadership"],
    )


def arch_50_comprehensive_management_pyramid_polc_and_style_synthesis(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    ceo = rng.choice(PERSON_NAMES)
    prod_mgr = rng.choice([n for n in PERSON_NAMES if n != ceo])
    sup = rng.choice([n for n in PERSON_NAMES if n not in (ceo, prod_mgr)])
    defect_pct = rng.choice([6, 8, 9])

    prompt = (
        f"**Management Case Study ({biz}, {area}):**\n"
        f"- **{ceo}** (CEO) sets a 5-year objective to supply renewable hardware across Southern Africa.\n"
        f"- **{prod_mgr}** (Production Manager) breaks that vision into quarterly factory budgets, equipment needs, and team structures.\n"
        f"- **{sup}** (Floor Supervisor) manages 12 assembly technicians daily. Recently, defects jumped to **{defect_pct}%** while **{sup}** has been barking strict autocratic orders nonstop.\n\n"
        "Answer all three parts:\n"
        f"1. Classify **{ceo}**, **{prod_mgr}**, and **{sup}** into their exact **management levels**.\n"
        f"2. Identify which **two POLC tasks** must fix the **{defect_pct}% defect spike** and give one specific action for each.\n"
        f"3. Recommend why shifting toward a **democratic style** plus **two good-manager traits** will help **{sup}** lift quality."
    )
    expected = (
        f"1) {ceo} = Top Management; {prod_mgr} = Middle Management; {sup} = Lower Management. "
        f"2) Controlling (measure defects vs standard & fix root cause/machinery) + Organising or Leading (retrain staff/adjust workstations/coach clearly). "
        "3) Democratic participation invites technicians' practical insight into why defects happen and boosts morale; traits like people skills, taking responsibility, and positive attitude build trust and ownership."
    )
    sol = (
        f"**Comprehensive Management Case Synthesis ({biz}) [6 marks]:**\n\n"
        "1. **Management Levels [2 marks]:**\n"
        f"   - **{ceo}** (CEO): **Top Management**; **{prod_mgr}** (Production Mgr): **Middle Management**; **{sup}** (Floor Supervisor): **Lower (First-line) Management** **[2]**.\n"
        f"2. **POLC Fix for {defect_pct}% Defects [2 marks]:**\n"
        "   - **Controlling:** Compare daily defects against quality targets, inspect faulty tools/processes, and apply corrective steps **[1]**.\n"
        "   - **Organising / Leading:** Reallocate assembly bottlenecks and coach/motivate technicians calmly **[1]**.\n"
        "3. **Style Shift & Good-Manager Traits [2 marks]:**\n"
        "   - Shifting to **Democratic (participatory)** gathers technicians' hands-on insight into root errors and lifts buy-in **[1]**.\n"
        "   - Demonstrating **good people skills, taking responsibility, and keeping employees happy/valued** rebuilds team quality **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_mgt_50",
        subskill="50_comprehensive_management_pyramid_polc_and_style_synthesis",
        title="Comprehensive Management Levels, POLC & Style Synthesis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Work through the 3 parts systematically: (1) Levels, (2) POLC fixes, (3) Democratic style + 2 traits.",
            "tier_2": f"Map {ceo}/{prod_mgr}/{sup} cleanly, pair Controlling + Leading/Organising, and show why participation solves hidden defects.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "All 3 managers mapped to Top, Middle, and Lower levels", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Two valid POLC tasks with specific quality actions", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Democratic style benefit + two good-manager characteristics", "marks": 2, "editable": True},
        ],
        misconception_tags=["relying_on_harsher_autocratic_shouting_to_solve_quality_defects"],
        qtype="extended_response",
    )


BUILDERS_26_50 = {
    "26_good_manager_punctuality_and_organisation": arch_26_good_manager_punctuality_and_organisation,
    "27_good_manager_qualified_and_industry_knowledge": arch_27_good_manager_qualified_and_industry_knowledge,
    "28_good_manager_positive_attitude_and_extra_effort": arch_28_good_manager_positive_attitude_and_extra_effort,
    "29_chain_of_command_and_communication_flow_diagram": arch_29_chain_of_command_and_communication_flow_diagram,
    "30_delegation_vs_abdication_of_responsibility": arch_30_delegation_vs_abdication_of_responsibility,
    "31_comparing_time_horizons_and_scope_table": arch_31_comparing_time_horizons_and_scope_table,
    "32_managing_across_business_functions_overview": arch_32_managing_across_business_functions_overview,
    "33_marketing_manager_polc_application": arch_33_marketing_manager_polc_application,
    "34_production_manager_quality_and_safety_control": arch_34_production_manager_quality_and_safety_control,
    "35_finance_manager_cash_budget_and_controlling": arch_35_finance_manager_cash_budget_and_controlling,
    "36_hr_manager_training_and_staff_retention": arch_36_hr_manager_training_and_staff_retention,
    "37_departmental_staffing_and_shift_scheduling_calc": arch_37_departmental_staffing_and_shift_scheduling_calc,
    "38_comparing_autocratic_democratic_permissive_table": arch_38_comparing_autocratic_democratic_permissive_table,
    "39_blended_adaptive_leadership_by_situation": arch_39_blended_adaptive_leadership_by_situation,
    "40_ethical_conduct_and_setting_good_example": arch_40_ethical_conduct_and_setting_good_example,
    "41_conflict_resolution_and_people_skills_case": arch_41_conflict_resolution_and_people_skills_case,
    "42_productivity_efficiency_output_per_worker_calc": arch_42_productivity_efficiency_output_per_worker_calc,
    "43_overtime_cost_control_and_planning_calc": arch_43_overtime_cost_control_and_planning_calc,
    "44_feedback_loop_bottom_up_to_top_management": arch_44_feedback_loop_bottom_up_to_top_management,
    "45_management_level_and_polc_matrix_table": arch_45_management_level_and_polc_matrix_table,
    "46_poor_management_warning_signs_and_fixes": arch_46_poor_management_warning_signs_and_fixes,
    "47_entrepreneur_transitioning_from_doing_to_managing": arch_47_entrepreneur_transitioning_from_doing_to_managing,
    "48_team_incentive_bonus_and_leading_motivation_calc": arch_48_team_incentive_bonus_and_leading_motivation_calc,
    "49_management_misconception_error_audit_table": arch_49_management_misconception_error_audit_table,
    "50_comprehensive_management_pyramid_polc_and_style_synthesis": arch_50_comprehensive_management_pyramid_polc_and_style_synthesis,
}
