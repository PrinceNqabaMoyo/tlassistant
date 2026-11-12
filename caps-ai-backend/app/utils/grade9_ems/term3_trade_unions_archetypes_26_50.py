"""Grade 9 EMS - Term 3 Trade Unions: Archetypes 26 to 50.

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 1/01. Trade Unions.md,
curriculum_docs/EMS_Gr9/Term 3/8-Trade unions.md, and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African labour relations contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES

from .term3_trade_unions_archetypes_01_25 import (
    _build_mcq,
    _build_short,
    _build_table,
    _esc,
    _fmt_r,
    _make_cell,
    get_ems_scenario,
)


def arch_26_forms_of_industrial_action_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Workers stop working completely and withhold labour after LRA notice", "Strike", "Complete collective stoppage"),
        ("Workers deliberately work slower than normal to reduce factory output", "Go-slow", "Intentional slowdown on duty"),
        ("Workers follow every rule literally and refuse all voluntary overtime", "Work-to-rule", "Strict minimum compliance"),
        ("Workers stand peacefully outside company gates holding placards", "Picketing", "Lawful public awareness"),
        ("Management closes factory gates to block workers during a dispute", "Lock-out", "Employer industrial action"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Workplace Action", "Key Feature", "Form of Industrial Action"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Workplace Action | Key Feature | Form of Industrial Action |", "| :--- | :--- | :--- |"]
    for idx, (desc, label, feat) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", desc, "given"),
            _make_cell(f"t0_r{idx}_c1", feat, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = label
        cell_hints[coord] = "Choose: Strike, Go-slow, Work-to-rule, Picketing, or Lock-out."
        memo_lines.append(f"| {desc} | {feat} | {label} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Forms of Industrial Action at {sc['business']} [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_tu_26",
        subskill="26_forms_of_industrial_action_classification_table",
        title="Forms of Industrial Action Matrix",
        prompt=(
            f"Classify four industrial action scenarios reported around **{sc['business']}** in **{sc['area']}**.\n\n"
            "Enter the exact form (**Strike**, **Go-slow**, **Work-to-rule**, **Picketing**, or **Lock-out**) in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Distinguish total stoppage (strike), slower pace (go-slow), placard protest (picketing), strict rules (work-to-rule), and employer closure (lock-out).",
            "tier_2": "Use exact terms: Strike, Go-slow, Work-to-rule, Picketing, Lock-out.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Identifies {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_go_slow_with_lockout_or_strike"],
    )


def arch_27_picket_rules_and_non_intimidation_duty(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"During a protected dispute at **{sc['business']}** in **{sc['area']}**, union members stage a **picket** outside the entrance.\n\n"
        "Which boundary separates a **lawful peaceful picket** from **illegal conduct**?"
    )
    correct = "Demonstrators may carry placards and persuade visitors peacefully outside designated gates without blocking access, vandalising property, or intimidating non-strikers."
    distractors = [
        "Picketers may lock supervisors inside warehouse offices until wage increases are signed.",
        "Picketers may burn supplier delivery trucks on public municipal roads.",
        "Picketers must physically remove all replacement goods from customer shopping trolleys.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_27",
        subskill="27_picket_rules_and_non_intimidation_duty",
        title="Peaceful Picketing vs Illegal Intimidation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Section 69 of the LRA permits peaceful picketing outside **{sc['business']}** only to express support non-violently; blocking doors, damage, and intimidation break the law."
        ),
        hints={
            "tier_1": "Picketing protects peaceful expression while forbidding violence or intimidation.",
            "tier_2": "Peaceful placards outside gates = lawful; damage/intimidation/blockades = unlawful.",
            "tier_3": correct,
        },
        misconception_tags=["equating_strike_rights_with_right_to_damage_property"],
    )


def arch_28_employer_lockout_defensive_industrial_action(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"After talks break down at **{sc['business']}** in **{sc['area']}**, management locks the plant gates and refuses employees entry until the union accepts its offer.\n\n"
        "1. What is this employer action called?\n"
        "2. State **one** reason an employer uses a **lock-out** during collective bargaining."
    )
    expected = (
        "1. A lock-out; "
        "2. To compel the union/employees to accept management's demands, or to protect factory equipment and prevent sabotage during partial go-slows."
    )
    sol = (
        f"**Employer Lock-out ({sc['business']}) [3 marks]:**\n\n"
        "1. **Term:** **Lock-out** **[1]**.\n"
        "2. **Reason:** Compels the union to negotiate/accept employer proposals via economic pressure (no work, no pay), or protects machinery/operations from disruptive go-slows **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_28",
        subskill="28_employer_lockout_defensive_industrial_action",
        title="Employer Lock-Out Mechanism",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Notice management — not employees — is closing the gates.",
            "tier_2": "Called a lock-out; used to protect operations or pressure union acceptance.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Lock-out", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Pressures union to settle / protects premises from go-slows", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_only_workers_take_industrial_action"],
    )


def arch_29_secret_ballot_requirement_before_strikes(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    voters = rng.choice([140, 210, 320])
    prompt = (
        f"Before calling **{voters} members** at **{sc['business']}** out on strike, union leaders organise an anonymous **secret ballot**.\n\n"
        "Why is holding a **secret ballot** an essential union **responsibility**?"
    )
    correct = "It ensures the strike reflects genuine democratic majority support without peer pressure or open intimidation at meetings."
    distractors = [
        "It reveals each dissenting member's name to supervisors for overtime cancellation.",
        "It replaces the legal requirement to notify the employer 48 hours beforehand.",
        "It pays striking members their full regular wages out of municipal rates.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_29",
        subskill="29_secret_ballot_requirement_before_strikes",
        title="Secret Ballot Accountability",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **secret ballot** across all **{voters}** members protects internal union democracy so workers vote freely without intimidation."
        ),
        hints={
            "tier_1": "Why vote privately on paper instead of raising hands in front of everyone?",
            "tier_2": "Secret ballots prevent peer intimidation and verify true majority consent.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_internal_union_democracy"],
    )


def arch_30_unprotected_wildcat_strike_consequences(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Workers at **{sc['business']}** in **{sc['area']}** launch an **unprotected (wildcat) strike**, ignoring CCMA procedures.\n\n"
        "Explain **two** legal or financial risks workers face during an unprotected strike."
    )
    expected = (
        "1. Workers lose LRA dismissal protection and may be fairly dismissed after due warning/ultimatum; "
        "2. Employees lose wages ('no work, no pay') and the union/workers may face court interdicts or damage claims."
    )
    sol = (
        f"**Risks of Unprotected Strikes ({sc['business']}) [4 marks]:**\n\n"
        "1. **Fair Dismissal Risk:** Unlike protected strikes, employees can be **dismissed** for breach of contract after fair ultimatums **[2]**.\n"
        "2. **Loss of Income & Interdicts:** Employers enforce **no work, no pay**, and the Labour Court can interdict the stoppage or order **compensation for losses** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_30",
        subskill="30_unprotected_wildcat_strike_consequences",
        title="Consequences of Unprotected Strikes",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Without LRA protection, job security and pay protections drop away.",
            "tier_2": "Mention (1) risk of dismissal and (2) no-work-no-pay / court interdict or damages.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Loss of job protection / fair dismissal risk", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "No work no pay / Labour Court interdict or civil damages", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_striking_workers_can_never_be_dismissed"],
    )


def arch_31_no_work_no_pay_principle_and_wage_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    daily_wage = rng.choice([320, 360, 420, 480])
    strike_days = rng.choice([4, 5, 6, 8])
    monthly_days = 22
    gross_monthly = daily_wage * monthly_days
    deduction = daily_wage * strike_days
    net_pay = gross_monthly - deduction
    prompt = (
        f"**{worker}** earns **{_fmt_r(daily_wage)} per day** across a **{monthly_days}-working-day month** at **{sc['business']}** in **{sc['area']}**.\n"
        f"During a protected strike lasting **{strike_days} working days**, the employer applies South Africa's **no work, no pay** rule.\n\n"
        "Calculate:\n"
        f"1. **{worker}**'s normal gross monthly wage before the strike.\n"
        "2. The total wage deduction for the strike days.\n"
        f"3. **{worker}**'s actual wage received for that month."
    )
    expected = (
        f"1. Normal gross wage = {_fmt_r(gross_monthly)}; "
        f"2. Strike deduction = {_fmt_r(deduction)}; "
        f"3. Actual wage received = {_fmt_r(net_pay)}."
    )
    sol = (
        f"**No Work, No Pay Calculation ({worker}) [4 marks]:**\n\n"
        f"1. **Normal Monthly Wage:** ${monthly_days} \\times {_fmt_r(daily_wage)} = {_fmt_r(gross_monthly)}$ **[1]**\n"
        f"2. **Strike Deduction:** ${strike_days} \\times {_fmt_r(daily_wage)} = {_fmt_r(deduction)}$ **[1]**\n"
        f"3. **Actual Wage Received:** ${_fmt_r(gross_monthly)} - {_fmt_r(deduction)} = {_fmt_r(net_pay)}$ **[2]**\n\n"
        "*(Even in a protected strike, employers are not obliged to pay wages for unworked strike days.)*"
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_31",
        subskill="31_no_work_no_pay_principle_and_wage_calculation",
        title="No Work, No Pay Wage Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Multiply daily wage by working days; deduct unworked strike days.",
            "tier_2": f"Gross = {monthly_days} x {daily_wage}; Deduction = {strike_days} x {daily_wage}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Gross monthly wage {_fmt_r(gross_monthly)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Strike deduction {_fmt_r(deduction)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Actual wage {_fmt_r(net_pay)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_employers_must_pay_wages_during_protected_strikes"],
    )


def arch_32_wage_increase_percentage_and_payroll_cost_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    workers = rng.choice([40, 50, 80])
    base_wage = rng.choice([7000, 8000, 9000])
    union_pct = rng.choice([9, 10, 11])
    offer_pct = rng.choice([5, 6, 7])
    union_inc = int(base_wage * union_pct / 100)
    offer_inc = int(base_wage * offer_pct / 100)
    diff_per_worker = union_inc - offer_inc
    monthly_gap = diff_per_worker * workers
    prompt = (
        f"At **{sc['business']}** in **{sc['area']}**, **{workers} workers** each currently earn **{_fmt_r(base_wage)} per month**.\n"
        f"During bargaining, the trade union demands a **{union_pct}%** wage increase, while management offers **{offer_pct}%**.\n\n"
        "Calculate:\n"
        "1. The Rand monthly increase per worker under each proposal.\n"
        f"2. The total monthly payroll cost gap between the union's demand and management's offer across all **{workers} workers**."
    )
    expected = (
        f"1. Union demand: {_fmt_r(union_inc)}/worker; Employer offer: {_fmt_r(offer_inc)}/worker; "
        f"2. Monthly payroll gap across {workers} workers = {_fmt_r(monthly_gap)}."
    )
    sol = (
        f"**Collective Bargaining Payroll Comparison ({sc['business']}) [5 marks]:**\n\n"
        f"1. **Union Demand ({union_pct}%):** $\\frac{{{union_pct}}}{{100}} \\times {_fmt_r(base_wage)} = {_fmt_r(union_inc)}$ per worker **[1]**\n"
        f"   **Employer Offer ({offer_pct}%):** $\\frac{{{offer_pct}}}{{100}} \\times {_fmt_r(base_wage)} = {_fmt_r(offer_inc)}$ per worker **[1]**\n"
        f"2. **Difference per Worker:** ${_fmt_r(union_inc)} - {_fmt_r(offer_inc)} = {_fmt_r(diff_per_worker)}$ **[1]**\n"
        f"3. **Total Monthly Payroll Gap:** ${workers} \\times {_fmt_r(diff_per_worker)} = {_fmt_r(monthly_gap)}$ per month **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_32",
        subskill="32_wage_increase_percentage_and_payroll_cost_calc",
        title="Wage Bargaining Payroll Cost Analysis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=5,
        hints={
            "tier_1": "Find each percentage of the base wage first, then multiply the per-worker gap by total workers.",
            "tier_2": f"{union_pct}% - {offer_pct}% = {union_pct - offer_pct}% of {_fmt_r(base_wage)} x {workers} workers.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Union {_fmt_r(union_inc)} and Offer {_fmt_r(offer_inc)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Per-worker difference {_fmt_r(diff_per_worker)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Total payroll gap {_fmt_r(monthly_gap)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_to_multiply_wage_gap_by_headcount"],
    )


def arch_33_lost_output_and_productivity_cost_during_strike_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    normal_rev = rng.choice([80000, 100000, 120000])
    strike_rev = rng.choice([20000, 25000, 30000])
    lost_per_day = normal_rev - strike_rev
    days = rng.choice([4, 5, 6])
    total_lost = lost_per_day * days
    strike_h = int(140 * (strike_rev / normal_rev))
    strike_y = 185 - strike_h
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 240" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="240" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Daily Production Revenue: {_esc(sc["business"])} ({days}-Day Strike)</text>'
        '<line x1="90" y1="185" x2="430" y2="185" stroke="#475569" stroke-width="2"/>'
        '<line x1="90" y1="40" x2="90" y2="185" stroke="#475569" stroke-width="2"/>'
        '<rect x="140" y="45" width="90" height="140" rx="4" fill="#16a34a"/>'
        f'<text x="185" y="38" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">{_fmt_r(normal_rev)}</text>'
        '<text x="185" y="204" text-anchor="middle" font-size="11" fill="#1e293b">Normal Day</text>'
        f'<rect x="285" y="{strike_y}" width="90" height="{strike_h}" rx="4" fill="#ef4444"/>'
        f'<text x="330" y="{strike_y - 7}" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">{_fmt_r(strike_rev)}</text>'
        '<text x="330" y="204" text-anchor="middle" font-size="11" fill="#1e293b">Strike Day</text>'
        '<rect x="445" y="55" width="175" height="110" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="532" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">Dispute Impact Summary</text>'
        f'<text x="532" y="102" text-anchor="middle" font-size="11" fill="#334155">Normal/day: {_fmt_r(normal_rev)}</text>'
        f'<text x="532" y="122" text-anchor="middle" font-size="11" fill="#334155">Strike/day: {_fmt_r(strike_rev)}</text>'
        f'<text x="532" y="144" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">Duration: {days} days</text>'
        '</svg>'
    )
    prompt = (
        f"Study the production revenue bar chart for **{sc['business']}** in **{sc['area']}** comparing normal daily revenue (**{_fmt_r(normal_rev)}**) "
        f"with revenue during a **{days}-day** industrial stoppage (**{_fmt_r(strike_rev)}/day**).\n\n"
        f"1. Calculate the **total revenue lost** over the **{days}-day** stoppage.\n"
        "2. State **one** negative consequence of such production losses for workers or local customers."
    )
    expected = (
        f"1. Daily loss = {_fmt_r(lost_per_day)}; Total {days}-day lost revenue = {_fmt_r(total_lost)}. "
        "2. Cancelled customer orders, delayed deliveries, or potential job losses if the firm loses competitiveness."
    )
    sol = (
        f"**Strike Production & Revenue Loss ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Daily Lost Revenue:** ${_fmt_r(normal_rev)} - {_fmt_r(strike_rev)} = {_fmt_r(lost_per_day)}$ **[1]**\n"
        f"   **Total Lost Revenue ({days} days):** ${days} \\times {_fmt_r(lost_per_day)} = {_fmt_r(total_lost)}$ **[1]**\n"
        "2. **Consequence:** Lost customer contracts, product shortages for consumers, reduced profitability, and heightened risk of future retrenchments **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_33",
        subskill="33_lost_output_and_productivity_cost_during_strike_svg",
        title="Lost Output & Revenue During Industrial Action",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Subtract strike-day revenue from normal-day revenue, then multiply by the strike duration.",
            "tier_2": f"({_fmt_r(normal_rev)} - {_fmt_r(strike_rev)}) x {days} days + explain downstream business/job risk.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Daily loss {_fmt_r(lost_per_day)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total {days}-day loss {_fmt_r(total_lost)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Valid downstream impact (lost orders, shortages, job cuts)", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_to_subtract_partial_strike_output"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_34_reasonable_vs_unreasonable_wage_demands_tradeoff(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pct = rng.choice([35, 42, 50])
    prompt = (
        f"A trade union at **{sc['business']}** demands an immediate **{pct}% wage increase** even though factory productivity and sales stayed flat.\n\n"
        "Why is making **reasonable wage demands** a key **union responsibility**?"
    )
    correct = "Unsustainable wage hikes far above productivity force employers to raise prices (inflation), automate tasks, retrench staff, or close down."
    distractors = [
        "Employers automatically print South African Rand notes whenever payroll increases.",
        "Higher labour costs always force competitors to cut their own retail prices.",
        "Government refunds 100% of private company wage increases via VAT rebates.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_34",
        subskill="34_reasonable_vs_unreasonable_wage_demands_tradeoff",
        title="Reasonable Wage Demands & Job Sustainability",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **{pct}%** rise without output growth threatens **{sc['business']}**'s survival, triggering higher prices, mechanisation, or **retrenchments** that harm workers long-term."
        ),
        hints={
            "tier_1": "What happens to costs, prices, and employment if wages soar without matching productivity?",
            "tier_2": "Excessive wage demands risk business closure, inflation, and job losses.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_wage_productivity_and_employment_tradeoff"],
    )


def arch_35_retrenchment_consultation_section_189_process(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    affected = rng.choice([15, 22, 30])
    prompt = (
        f"Due to falling orders in **{sc['area']}**, **{sc['business']}** considers **retrenching {affected} workers** for operational reasons.\n\n"
        "Describe **two** legal duties management has toward the trade union during retrenchment consultations and **one** alternative unions often propose to save jobs."
    )
    expected = (
        "Duties: Consult meaningfully in writing with the union beforehand and apply fair objective selection criteria (e.g. LIFO) plus statutory severance pay. "
        "Alternative: Short-time work, voluntary unpaid leave, redeployment, or temporary overtime freezes."
    )
    sol = (
        f"**Fair Retrenchment Process ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Consultation & Fairness:** Management must issue written notice and **consult meaningfully** with the union over reasons and **{affected}** positions **[1]**, applying fair criteria (such as LIFO) and paying **severance pay** **[1]**.\n"
        "2. **Job-Saving Alternative:** Working **short-time** (reduced hours), **retraining/redeployment** to other branches, or halting overtime instead of dismissing staff **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_35",
        subskill="35_retrenchment_consultation_section_189_process",
        title="Retrenchment Consultation & Alternatives",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Under the LRA (Section 189), employers cannot just fire operational staff overnight.",
            "tier_2": "Include written consultation, fair selection/severance pay, and alternatives like short-time or redeployment.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Prior written consultation with union", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Fair objective criteria / severance pay", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Valid alternative (short-time, redeployment, overtime freeze)", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_employers_need_not_consult_before_retrenchment"],
    )


def arch_36_disciplinary_hearings_and_fair_dismissal_procedure(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    emp = rng.choice(NAMES)
    prompt = (
        f"Management at **{sc['business']}** accuses **{emp}** of repeated lateness and wants immediate dismissal without a hearing.\n\n"
        "How does the **Labour Relations Act** protect **{emp}** against **unfair dismissal**?"
    )
    correct = "Management must prove a valid fair reason (substantive fairness) AND hold a formal disciplinary hearing where the employee can be represented by a shop steward or colleague (procedural fairness)."
    distractors = [
        "Management may dismiss any worker verbally on the spot without keeping written records.",
        "Only company shareholders may appeal disciplinary decisions at the Reserve Bank.",
        "Trade union members are exempt from all workplace attendance rules forever.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_36",
        subskill="36_disciplinary_hearings_and_fair_dismissal_procedure",
        title="Fair Dismissal & Disciplinary Representation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Under the LRA, dismissing **{emp}** requires both **substantive fairness** (a valid reason) and **procedural fairness** (prior notice, disciplinary hearing, shop steward representation)."
        ),
        hints={
            "tier_1": "Look for both a fair reason AND a fair hearing procedure.",
            "tier_2": "LRA requires substantive + procedural fairness and representation rights.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_employers_have_unilateral_spot_dismissal_power"],
    )


def arch_37_minimum_wage_policy_and_employment_effects(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    hourly_rate = rng.choice([27, 29, 31])
    prompt = (
        f"Imagine South Africa's **National Minimum Wage** sits around **{_fmt_r(hourly_rate)} per hour** for small employers in **{area}**.\n\n"
        "State **one** economic **benefit** of a statutory minimum wage for low-income workers and **one** potential **challenge** for struggling micro-enterprises."
    )
    expected = (
        "Benefit: Protects vulnerable workers from poverty-level exploitation and boosts household purchasing power. "
        "Challenge: Increases labour costs for small businesses, potentially slowing new hiring if turnover does not rise."
    )
    sol = (
        f"**Minimum Wage Analysis ({area} at {_fmt_r(hourly_rate)}/hr) [4 marks]:**\n\n"
        "- **Benefit for Workers:** Prevents extreme wage exploitation, improves living standards, and raises local consumer spending **[2]**.\n"
        "- **Challenge for Small Firms:** Raises fixed/operating payroll expenses, which may discourage small firms from hiring extra unskilled staff if profits are tight **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_37",
        subskill="37_minimum_wage_policy_and_employment_effects",
        title="National Minimum Wage: Benefits vs Trade-Offs",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Weigh poverty protection against higher payroll costs for small employers.",
            "tier_2": "Benefit = worker dignity/spending; Challenge = higher small-business cost/slower hiring.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Benefit: prevents exploitation / lifts worker income & demand", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Challenge: higher payroll cost / hiring restraint for small firms", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_minimum_wage_with_zero_business_cost_effect"],
    )


def arch_38_workplace_health_and_safety_union_oversight(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    hazard = rng.choice(["faulty ventilation and missing dust masks", "unguarded cutting machinery", "leaking chemical storage drums"])
    prompt = (
        f"Workers at **{sc['business']}** notice **{hazard}** and report it to their union health-and-safety representative.\n\n"
        "Why is monitoring **occupational health and safety** a vital union function?"
    )
    correct = "It prevents workplace injuries and occupational illness by enforcing safe equipment, protective gear, and legal safety inspections."
    distractors = [
        "It increases company electricity exports during winter peak hours.",
        "It replaces annual financial audits with environmental rainfall logs.",
        "It forces workers to purchase their own industrial steel-toe machinery parts.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_38",
        subskill="38_workplace_health_and_safety_union_oversight",
        title="Workplace Health & Safety Oversight",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Unions inspect **personal protective equipment (PPE)** and hazards like **{hazard}** so workers at **{sc['business']}** return home safely and firms avoid costly accidents."
        ),
        hints={
            "tier_1": "Think of injuries, PPE, and safe working conditions.",
            "tier_2": "Safety oversight enforces protective gear and safe procedures to prevent harm.",
            "tier_3": correct,
        },
        misconception_tags=["limiting_unions_solely_to_wage_bargaining"],
    )


def arch_39_union_subscriptions_percentage_dues_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    members = rng.choice([80, 120, 150])
    monthly_pay = rng.choice([8000, 9000, 10000])
    dues_pct = rng.choice([1, 2])
    dues_per_member = int(monthly_pay * dues_pct / 100)
    monthly_total = dues_per_member * members
    annual_total = monthly_total * 12
    prompt = (
        f"At **{sc['business']}** in **{sc['area']}**, **{members} union members** earn **{_fmt_r(monthly_pay)} per month** each.\n"
        f"Each member pays a union subscription equal to **{dues_pct}% of monthly pay**.\n\n"
        "Calculate:\n"
        "1. The monthly subscription paid by **one** member.\n"
        f"2. The **total annual dues** collected from all **{members} members** (over 12 months)."
    )
    expected = (
        f"1. Monthly subscription per member = {_fmt_r(dues_per_member)}; "
        f"2. Total monthly dues = {_fmt_r(monthly_total)}; Total annual dues = {_fmt_r(annual_total)}."
    )
    sol = (
        f"**Union Subscription Revenue ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Monthly Fee per Member:** $\\frac{{{dues_pct}}}{{100}} \\times {_fmt_r(monthly_pay)} = {_fmt_r(dues_per_member)}$ **[1]**\n"
        f"2. **Total Monthly Dues:** ${members} \\times {_fmt_r(dues_per_member)} = {_fmt_r(monthly_total)}$ **[1]**\n"
        f"3. **Total Annual Dues:** $12 \\times {_fmt_r(monthly_total)} = {_fmt_r(annual_total)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_39",
        subskill="39_union_subscriptions_percentage_dues_calculation",
        title="Calculating Union Membership Subscriptions",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Find 1 member's monthly fee first, then multiply by total members and 12 months.",
            "tier_2": f"{dues_pct}% of {_fmt_r(monthly_pay)} x {members} x 12 months.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Per-member fee {_fmt_r(dues_per_member)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Monthly branch total {_fmt_r(monthly_total)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Annual total {_fmt_r(annual_total)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_12_months_in_annual_dues_calc"],
    )


def arch_40_benefits_of_trade_unions_to_businesses(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Management at **{sc['business']}** in **{sc['area']}** recognises that constructive engagement with a trade union can also **benefit the business**.\n\n"
        "Which option describes a **positive effect** of well-run trade unions on a business?"
    )
    correct = "They create a structured single channel for management-worker communication, improving morale, staff retention, and negotiated dispute resolution."
    distractors = [
        "They guarantee zero raw material delivery costs from overseas suppliers.",
        "They automatically exempt the business from paying municipal rates and VAT.",
        "They eliminate the need for managers to monitor product quality standards.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_40",
        subskill="40_benefits_of_trade_unions_to_businesses",
        title="Positive Effects of Trade Unions on Businesses",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Working with an organised union lets **{sc['business']}** resolve grievances early through shop stewards instead of facing sudden wildcat walkouts, boosting productivity and retention."
        ),
        hints={
            "tier_1": "How does speaking to one elected team help management better than unorganised chaos?",
            "tier_2": "Structured communication, higher worker morale, lower staff turnover, fewer wildcat stoppages.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_unions_have_zero_benefits_for_employers"],
    )


def arch_41_challenges_posed_by_unions_to_businesses(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"During tense labour relations at **{sc['business']}** in **{sc['area']}**, prolonged industrial action threatens operations.\n\n"
        "Explain **two** negative impacts or operational challenges militant or protracted union disputes can create for a business."
    )
    expected = (
        "1. Lost output, missed customer orders, and reputational damage during prolonged strikes or go-slows; "
        "2. Steeply rising labour costs that reduce profits or deter future expansion and investment."
    )
    sol = (
        f"**Operational Challenges for {sc['business']} [4 marks]:**\n\n"
        "1. **Lost Output & Reliability:** Strikes and go-slows halt production, causing missed deadlines, lost clients, and lower revenue **[2]**.\n"
        "2. **Cost & Investment Pressure:** Unaffordable wage settlements squeeze cash flow, lowering retained profits and discouraging owners from expanding operations **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_41",
        subskill="41_challenges_posed_by_unions_to_businesses",
        title="Challenges Posed by Labour Disputes to Business",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Consider production stoppages and rising payroll expenses.",
            "tier_2": "Mention (1) disrupted production/lost clients and (2) higher labour costs/reduced investment.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Production stoppages / missed orders / lost clients", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Higher wage costs squeezing profit or deterring investment", "marks": 2, "editable": True},
        ],
        misconception_tags=["overlooking_business_cost_and_output_risks_of_strikes"],
    )


def arch_42_economic_effects_of_strikes_on_gdp_and_communities(rng: random.Random) -> Dict[str, Any]:
    sector = rng.choice(["freight rail and ports", "automotive manufacturing", "gold and platinum mining"])
    area = rng.choice(AREAS)
    prompt = (
        f"A multi-week strike hits **{sector}** around **{area}**.\n\n"
        "Explain **two** broader economic effects a protracted sector-wide strike has on the **South African economy and surrounding communities**."
    )
    expected = (
        "1. Exports and GDP output fall, damaging foreign investor confidence and supplier businesses; "
        "2. Local household incomes drop (no work, no pay), hurting neighbourhood shops and community livelihoods."
    )
    sol = (
        f"**Macro & Community Impact ({sector} around {area}) [4 marks]:**\n\n"
        "1. **National Output & Investment:** Disrupted supply chains reduce exports and **GDP growth**, making foreign investors cautious about funding local projects **[2]**.\n"
        "2. **Community Livelihoods:** Striking families lose pay, shrinking spending at local spaza shops, taxis, and supermarkets around **{area}** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_42",
        subskill="42_economic_effects_of_strikes_on_gdp_and_communities",
        title="Macroeconomic & Community Impact of Strikes",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Look beyond the factory fence to national exports/GDP and nearby households/shops.",
            "tier_2": "Explain impact on (1) GDP/exports/investors and (2) community household spending.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Lower GDP/exports or weakened investor confidence", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Reduced worker income and lower local community spending", "marks": 2, "editable": True},
        ],
        misconception_tags=["ignoring_ripple_effects_beyond_a_single_firm"],
    )


def arch_43_sustainable_growth_and_skills_development(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Trade unions in **{area}** partner with SETAs and employers to fund artisan **skills development** and productivity programmes.\n\n"
        "How does **skills training** support **sustainable economic growth**?"
    )
    correct = "More skilled workers produce higher-quality output more efficiently, enabling businesses to grow profitably and sustain higher real wages without causing inflation."
    distractors = [
        "Skills training allows factories to pay lower wages even as productivity doubles.",
        "Skills training eliminates the need for raw materials in manufacturing.",
        "Skills training lowers employment by encouraging workers to retire at age twenty-five.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_43",
        subskill="43_sustainable_growth_and_skills_development",
        title="Skills Development & Sustainable Growth",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Investing in **skills development** increases **labour productivity** (output per worker), allowing firms to pay better real wages sustainably while remaining globally competitive."
        ),
        hints={
            "tier_1": "Link worker skills -> higher productivity -> sustainable wages & business growth.",
            "tier_2": "Higher skill raises output quality/efficiency so wages and profits grow together.",
            "tier_3": correct,
        },
        misconception_tags=["separating_productivity_growth_from_sustainable_wages"],
    )


def arch_44_equitable_wealth_distribution_and_consumer_spending(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Economists studying households around **{area}** note that fair collective bargaining contributes to **equitable wealth distribution**.\n\n"
        "Explain how **fair wages** secured through responsible bargaining stimulate broader **local economic development**."
    )
    expected = (
        "Fair wages narrow extreme income inequality, enabling working households to spend more on food, housing, schooling, and local businesses, which boosts production and jobs."
    )
    sol = (
        f"**Fair Wages & Equitable Growth ({area}) [3 marks]:**\n\n"
        "- **Inequality Reduction:** Prevents profits from flowing solely to top owners while workers remain in poverty **[1]**.\n"
        "- **Multiplier Demand:** Workers spend higher disposable income at local shops, builders, and clinics in **{area}**, growing aggregate demand and creating jobs **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_44",
        subskill="44_equitable_wealth_distribution_and_consumer_spending",
        title="Equitable Wealth Distribution & Demand",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "What do working families do with fairer wages inside their community?",
            "tier_2": "Explain reduced inequality plus increased consumer spending supporting local businesses.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Narrows income inequality / shares wealth fairly", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Boosts household consumption and local business growth", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_wages_solely_as_cost_without_demand_effect"],
    )


def arch_45_peaceful_industrial_dialogue_and_investor_confidence(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    invest_amt = rng.choice([4500000, 6000000, 8500000])
    new_jobs = rng.choice([35, 50, 65])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 205" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="205" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Industrial Dialogue &amp; Sustainable Growth: {_esc(sc["area"])}</text>'
        '<rect x="20" y="60" width="142" height="82" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="91" y="92" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1e3a8a">Constructive Talks</text>'
        '<text x="91" y="112" text-anchor="middle" font-size="10" fill="#1e40af">Union &amp; Management</text>'
        '<text x="91" y="127" text-anchor="middle" font-size="10" fill="#1e40af">reach fair agreement</text>'
        '<line x1="162" y1="101" x2="188" y2="101" stroke="#334155" stroke-width="2"/>'
        '<polygon points="188,96 198,101 188,106" fill="#334155"/>'
        '<rect x="198" y="60" width="142" height="82" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="269" y="92" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#78350f">Workplace Stability</text>'
        '<text x="269" y="112" text-anchor="middle" font-size="10" fill="#92400e">Zero wildcat stops;</text>'
        '<text x="269" y="127" text-anchor="middle" font-size="10" fill="#92400e">reliable deliveries</text>'
        '<line x1="340" y1="101" x2="366" y2="101" stroke="#334155" stroke-width="2"/>'
        '<polygon points="366,96 376,101 366,106" fill="#334155"/>'
        '<rect x="376" y="60" width="142" height="82" rx="8" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>'
        '<text x="447" y="92" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#312e81">Investor Trust</text>'
        f'<text x="447" y="112" text-anchor="middle" font-size="10" fill="#3730a3">{_fmt_r(invest_amt)} new</text>'
        '<text x="447" y="127" text-anchor="middle" font-size="10" fill="#3730a3">plant capital</text>'
        '<line x1="518" y1="101" x2="544" y2="101" stroke="#334155" stroke-width="2"/>'
        '<polygon points="544,96 554,101 544,106" fill="#334155"/>'
        '<rect x="554" y="60" width="110" height="82" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="609" y="92" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#14532d">Growth</text>'
        f'<text x="609" y="112" text-anchor="middle" font-size="10" fill="#166534">+{new_jobs} permanent</text>'
        '<text x="609" y="127" text-anchor="middle" font-size="10" fill="#166534">jobs created</text>'
        '<text x="340" y="178" text-anchor="middle" font-size="11" fill="#475569">Predictable labour relations attract investment and protect long-term employment.</text>'
        '</svg>'
    )
    prompt = (
        f"Study the causal diagram illustrating **Industrial Dialogue & Sustainable Growth** around **{sc['area']}** "
        f"where **{_fmt_r(invest_amt)}** of expansion capital creates **{new_jobs} permanent jobs**.\n\n"
        f"Explain how **constructive union-management dialogue** connects to **investor trust** and the creation of those **{new_jobs} jobs**."
    )
    expected = (
        f"Constructive dialogue prevents disruptive strikes and creates workplace stability, giving investors confidence to commit {_fmt_r(invest_amt)} in plant expansion and create {new_jobs} permanent jobs."
    )
    sol = (
        f"**Industrial Dialogue & Growth ({sc['area']}) [3 marks]:**\n\n"
        "1. **Workplace Stability:** Peaceful negotiation resolves disputes early so production and customer orders continue reliably **[1]**.\n"
        f"2. **Investor Confidence & Jobs:** Predictable operations encourage investors to inject **{_fmt_r(invest_amt)}** locally rather than relocating, generating **{new_jobs} sustainable jobs** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_45",
        subskill="45_peaceful_industrial_dialogue_and_investor_confidence",
        title="Peaceful Dialogue & Investor Confidence",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Trace the four stages from left to right in the causal diagram.",
            "tier_2": "Dialogue -> stability -> investor capital -> sustainable job creation.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dialogue brings workplace stability / predictable operations", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Stability attracts investment capital and creates permanent jobs", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_investment_is_unaffected_by_labour_stability"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_46_employer_vs_employee_rights_balance_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Expect workers to perform agreed duties honestly during working hours", "Employer", "Management productivity right"),
        ("Receive fair wages on time in safe, non-discriminatory conditions", "Employee", "Section 23 fair labour right"),
        ("Protect company premises and implement lawful lock-outs during deadlocks", "Employer", "Employer operational right"),
        ("Form or join a trade union and participate in lawful protected strikes", "Employee", "Freedom of association right"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Workplace Right / Entitlement", "Legal Basis", "Primary Holder (Employer vs Employee)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Workplace Right | Legal Basis | Primary Holder |", "| :--- | :--- | :--- |"]
    for idx, (right, holder, basis) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", right, "given"),
            _make_cell(f"t0_r{idx}_c1", basis, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = holder
        cell_hints[coord] = "Enter exact word: Employer or Employee."
        memo_lines.append(f"| {right} | {basis} | {holder} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Balancing Employer & Employee Rights ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_tu_46",
        subskill="46_employer_vs_employee_rights_balance_table",
        title="Balancing Employer vs Employee Rights",
        prompt=(
            f"Under South African labour law, workplace harmony at **{sc['business']}** requires balancing mutual rights.\n\n"
            "Identify whether each entitlement belongs primarily to the **Employer** or the **Employee** in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Distinguish duties owed to business owners (Employer) vs workers (Employee).",
            "tier_2": "Write exact words: Employer or Employee.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Identifies {chosen[i][1]} right", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["assuming_labour_law_grants_rights_only_to_one_party"],
    )


def arch_47_case_study_sa_mining_wage_deadlock_resolution(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    union = rng.choice(["NUM", "SATAWU", "FAWU"])
    demand = rng.choice([12, 14, 15])
    offer = rng.choice([6, 7, 8])
    prompt = (
        f"Workers affiliated with **{union}** at **{sc['business']}** in **{sc['area']}** demand a **{demand}%** pay increase, while management offers **{offer}%** citing rising electricity tariffs.\n\n"
        f"1. Suggest **one** lawful institution where **{union}** and **{sc['business']}** should refer their deadlock before striking.\n"
        f"2. Advise **{union}** on **one** responsibility its members must uphold if a strike proceeds, and state **one** compromise strategy both sides could consider."
    )
    expected = (
        f"1. Refer to the CCMA (or sector Bargaining Council) for conciliation. "
        "2. Keep any strike peaceful/lawful (no intimidation, secret ballot); compromise via a multi-year staged settlement, productivity bonus, or mediated midpoint increase."
    )
    sol = (
        f"**Case Study Resolution ({union} & {sc['business']}) [5 marks]:**\n\n"
        "1. **Dispute Body:** Refer the deadlock to the **CCMA** (or applicable sector **Bargaining Council**) for conciliation **[1]**.\n"
        f"2. **Union Responsibility:** Conduct a **secret ballot**, give **48h written notice**, and keep pickets **peaceful without intimidation or vandalism** **[2]**.\n"
        f"3. **Compromise Strategy:** Agree on a phased multi-year increase (e.g. near the midpoint between {offer}% and {demand}%) paired with **productivity-linked bonuses** or training allowances **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_47",
        subskill="47_case_study_sa_mining_wage_deadlock_resolution",
        title="Case Study: Resolving a SA Wage Deadlock",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=5,
        hints={
            "tier_1": "Apply the CCMA referral rule, union duty of peaceful conduct, and realistic bargaining compromises.",
            "tier_2": "Include (1) CCMA/Bargaining Council, (2) peaceful strike/secret ballot/48h notice, (3) productivity bonus or staged midpoint.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "CCMA or Bargaining Council referral", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Peaceful non-violent conduct / secret ballot / 48h notice", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Constructive compromise (midpoint / multi-year / productivity bonus)", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_deadlocks_have_only_strike_as_outcome"],
    )


def arch_48_essential_services_strike_prohibition_and_arbitration(rng: random.Random) -> Dict[str, Any]:
    service = rng.choice(["emergency hospital paramedics", "municipal firefighting crews", "police operational officers", "potable water supply technicians"])
    area = rng.choice(AREAS)
    prompt = (
        f"In **{area}**, **{service}** provide an **essential service** whose interruption threatens public life, health, or safety.\n\n"
        "How does South Africa's **Labour Relations Act** treat disputes involving **essential service workers**?"
    )
    correct = "Essential service workers may belong to trade unions, but are legally prohibited from striking and must resolve deadlocks through binding CCMA arbitration."
    distractors = [
        "Essential service workers are banned from joining any trade union or earning overtime.",
        "Essential service workers may strike immediately without notice whenever budgets change.",
        "Municipal mayors must personally perform emergency surgery during hospital wage talks.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_tu_48",
        subskill="48_essential_services_strike_prohibition_and_arbitration",
        title="Essential Services & Compulsory Arbitration",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Because interrupting **{service}** in **{area}** endangers lives, the LRA prohibits strikes in designated essential services and mandates **binding arbitration** instead."
        ),
        hints={
            "tier_1": "Public safety prevents strikes here, so how are deadlocks settled fairly?",
            "tier_2": "May join unions, cannot strike, settled via compulsory binding arbitration.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_essential_service_workers_have_no_union_rights_or_can_strike"],
    )


def arch_49_informal_and_seasonal_farm_worker_unionisation(rng: random.Random) -> Dict[str, Any]:
    crop = rng.choice(["citrus orchards", "table grape farms", "sugarcane plantations"])
    area = rng.choice(AREAS)
    prompt = (
        f"Seasonal labourers working on **{crop}** near **{area}** often have lower union membership rates than urban factory workers.\n\n"
        "Give **two** practical challenges trade unions face when organising **seasonal agricultural or informal workers**."
    )
    expected = (
        "1. Workers are geographically scattered on remote private farms, making union access difficult; "
        "2. Short-term seasonal contracts and fear of not being rehired discourage workers from joining."
    )
    sol = (
        f"**Union Organising Hurdles ({crop} near {area}) [4 marks]:**\n\n"
        "1. **Geographic Isolation:** Workers are dispersed across remote private properties where union organisers struggle to hold meetings **[2]**.\n"
        "2. **Job Insecurity:** Temporary seasonal contracts make low-income earners afraid employers will not renew their next season's work if they join **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_49",
        subskill="49_informal_and_seasonal_farm_worker_unionisation",
        title="Organising Seasonal & Rural Workers",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare an urban 500-person factory with scattered short-term seasonal farm work.",
            "tier_2": "Mention physical dispersion/access limits and seasonal contract insecurity.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Remote dispersion / limited access on farms", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Temporary contracts / fear of non-renewal or victimisation", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_all_sectors_organise_with_equal_ease"],
    )


def arch_50_holistic_sa_labour_relations_sustainable_economy_synthesis(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Using **{sc['business']}** in **{sc['area']}** as a South African case example, evaluate how responsible trade unions contribute to a **sustainable economy**:\n\n"
        "1. Identify the **constitutional clause** and **primary statute** governing union rights and dispute settlement.\n"
        "2. Explain **one** role unions perform for worker welfare AND **one** responsibility unions owe to business survival.\n"
        "3. State how balancing worker rights with productivity supports **long-term national economic growth**."
    )
    expected = (
        "1. Constitution Section 23 and the Labour Relations Act (LRA). "
        "2. Role: collective bargaining for fair pay/safety; Responsibility: realistic wage demands and peaceful lawful action. "
        "3. Higher skills and workplace stability protect jobs, attract investment, and distribute wealth fairly."
    )
    sol = (
        f"**Holistic SA Labour Relations Synthesis ({sc['business']}) [6 marks]:**\n\n"
        "1. **Legal Framework:** **Section 23** of the South African Constitution **[1]** and the **Labour Relations Act (LRA)** (supported by the CCMA) **[1]**.\n"
        f"2. **Role vs Responsibility:** Unions **negotiate fair wages, safety, and training** for workers at **{sc['business']}** **[1]**, while upholding the **responsibility** to keep demands sustainable, hold secret ballots, and act peacefully **[1]**.\n"
        "3. **Sustainable Growth:** Fair pay lifts local consumer demand while workplace stability, upskilling, and profitability encourage investment and job creation across South Africa **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_tu_50",
        subskill="50_holistic_sa_labour_relations_sustainable_economy_synthesis",
        title="Holistic SA Trade Unions & Sustainable Growth",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Link legal foundation (Sec 23 + LRA) -> role/responsibility -> productivity & growth.",
            "tier_2": "Cover (1) Sec 23 & LRA, (2) bargaining/welfare role + realistic/peaceful responsibility, (3) investment/demand/jobs.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Constitution Section 23", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Labour Relations Act (LRA)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Valid union role (bargaining, legal aid, safety)", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Valid union responsibility (peaceful action, realistic demands)", "marks": 1, "editable": True},
            {"id": "mp_5", "desc": "Links balanced relations to investment, productivity, and jobs", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_labour_relations_as_purely_adversarial_zero_sum"],
    )


BUILDERS_26_50 = {
    "26_forms_of_industrial_action_classification_table": arch_26_forms_of_industrial_action_classification_table,
    "27_picket_rules_and_non_intimidation_duty": arch_27_picket_rules_and_non_intimidation_duty,
    "28_employer_lockout_defensive_industrial_action": arch_28_employer_lockout_defensive_industrial_action,
    "29_secret_ballot_requirement_before_strikes": arch_29_secret_ballot_requirement_before_strikes,
    "30_unprotected_wildcat_strike_consequences": arch_30_unprotected_wildcat_strike_consequences,
    "31_no_work_no_pay_principle_and_wage_calculation": arch_31_no_work_no_pay_principle_and_wage_calculation,
    "32_wage_increase_percentage_and_payroll_cost_calc": arch_32_wage_increase_percentage_and_payroll_cost_calc,
    "33_lost_output_and_productivity_cost_during_strike_svg": arch_33_lost_output_and_productivity_cost_during_strike_svg,
    "34_reasonable_vs_unreasonable_wage_demands_tradeoff": arch_34_reasonable_vs_unreasonable_wage_demands_tradeoff,
    "35_retrenchment_consultation_section_189_process": arch_35_retrenchment_consultation_section_189_process,
    "36_disciplinary_hearings_and_fair_dismissal_procedure": arch_36_disciplinary_hearings_and_fair_dismissal_procedure,
    "37_minimum_wage_policy_and_employment_effects": arch_37_minimum_wage_policy_and_employment_effects,
    "38_workplace_health_and_safety_union_oversight": arch_38_workplace_health_and_safety_union_oversight,
    "39_union_subscriptions_percentage_dues_calculation": arch_39_union_subscriptions_percentage_dues_calculation,
    "40_benefits_of_trade_unions_to_businesses": arch_40_benefits_of_trade_unions_to_businesses,
    "41_challenges_posed_by_unions_to_businesses": arch_41_challenges_posed_by_unions_to_businesses,
    "42_economic_effects_of_strikes_on_gdp_and_communities": arch_42_economic_effects_of_strikes_on_gdp_and_communities,
    "43_sustainable_growth_and_skills_development": arch_43_sustainable_growth_and_skills_development,
    "44_equitable_wealth_distribution_and_consumer_spending": arch_44_equitable_wealth_distribution_and_consumer_spending,
    "45_peaceful_industrial_dialogue_and_investor_confidence": arch_45_peaceful_industrial_dialogue_and_investor_confidence,
    "46_employer_vs_employee_rights_balance_table": arch_46_employer_vs_employee_rights_balance_table,
    "47_case_study_sa_mining_wage_deadlock_resolution": arch_47_case_study_sa_mining_wage_deadlock_resolution,
    "48_essential_services_strike_prohibition_and_arbitration": arch_48_essential_services_strike_prohibition_and_arbitration,
    "49_informal_and_seasonal_farm_worker_unionisation": arch_49_informal_and_seasonal_farm_worker_unionisation,
    "50_holistic_sa_labour_relations_sustainable_economy_synthesis": arch_50_holistic_sa_labour_relations_sustainable_economy_synthesis,
}
