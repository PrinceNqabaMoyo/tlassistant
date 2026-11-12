"""Grade 8 EMS — Factors of Production Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 4/03. Factors of production.md.
Covers Entrepreneurship qualities & SA Labour Legislation (LRA, BCEA, OHSA, COIDA, EEA, CCMA).
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import NAMES, SUPPLIERS
from app.utils.grade8_ems.factors_of_production_archetypes_01_25 import (
    _BANKS,
    _make_mcq,
    _make_rubric,
    _make_table,
    _make_typed,
    fmt_r,
    get_ems_scenario,
    svg_factor_card,
)


def _b26_entrepreneur_seven_qualities_id(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    trait = rng.choice([
        ("Calculated risk-taker", "researches customer demand and starts with manageable capital despite uncertainty"),
        ("Perseverant and hardworking", "keeps improving the venture even after slow initial trading months"),
        ("Creative and innovative", "invents fresh packaging and eco-friendly products to stand out from competitors"),
        ("Good planner and organiser", "schedules supplier deliveries, rosters, and monthly cash budgets cleanly"),
    ])
    prompt = (
        f"In {s['area']}, {owner} launches {s['business']} and demonstrates this habit: {owner} {trait[1]}. "
        f"Which entrepreneurial quality does this illustrate?"
    )
    ans = trait[0]
    opts = [
        "Calculated risk-taker",
        "Perseverant and hardworking",
        "Creative and innovative",
        "Good planner and organiser",
    ]
    exp = f"An entrepreneur who {trait[1]} displays the quality of being '{trait[0]}'."
    return _make_mcq(
        rng,
        subskill="26_entrepreneur_seven_qualities_id",
        title="Key Qualities of Entrepreneurs",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Match the exact behaviour in the sentence to one of the 7 entrepreneurial qualities.",
            "tier_2": "Consider risk-taking, perseverance, creativity, and planning/organising.",
            "tier_3": f"Quality shown: {ans}.",
        },
        misconception_tags=["confuses_entrepreneurial_qualities"],
        question_family_id="entrepreneur_qualities",
    )


def _b27_calculated_vs_reckless_risk(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    loan = rng.randint(50, 150) * 1000
    prompt = (
        f"Entrepreneur A in {s['area']} borrows {fmt_r(loan)} without surveying customers, keeping no cash reserve, and ignoring hygiene permits. "
        f"Entrepreneur B surveys 80 local households, writes a cash budget, and insures stock before borrowing {fmt_r(loan)}. "
        f"Explain TWO differences between Entrepreneur B's **calculated risk** and Entrepreneur A's **reckless risk**."
    )
    sample = (
        f"1. Research & planning: Entrepreneur B validates demand and prepares a cash budget to manage {fmt_r(loan)} debt repayments, whereas Entrepreneur A guesses blindly.\n"
        "2. Risk mitigation: Entrepreneur B maintains emergency savings, legal permits, and insurance to survive setbacks rather than risking total collapse."
    )
    pts = [
        "Calculated risk relies on market research and cash-flow/budget planning before investing.",
        "Calculated risk uses safeguards (savings buffer, permits, insurance) unlike blind reckless gambling.",
    ]
    return _make_rubric(
        rng,
        subskill="27_calculated_vs_reckless_risk",
        title="Calculated vs Reckless Entrepreneurial Risk",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Compare how the two entrepreneurs prepare, research, and protect against failure.",
            "tier_2": "Focus on market research/budgeting AND risk-mitigation reserves/insurance.",
            "tier_3": sample,
        },
        misconception_tags=["equates_entrepreneurship_with_reckless_gambling"],
        question_family_id="calculated_risk_rubric",
        marks=2,
    )


def _b28_entrepreneurial_profit_loss_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rev = rng.randint(60, 120) * 1000
    rent = rng.randint(6, 14) * 1000
    wages = rng.randint(15, 32) * 1000
    interest = rng.randint(2, 6) * 1000
    profit = rev - (rent + wages + interest)
    ans = fmt_r(profit)
    svg = svg_factor_card(
        f"{s['business']} — Factor Payments & Profit",
        f"Entrepreneur: {s['entrepreneur']} ({s['area']})",
        [
            ("Total Monthly Revenue", fmt_r(rev)),
            ("Rent Paid (Natural Resources / Premises)", fmt_r(rent)),
            ("Salaries & Wages Paid (Labour)", fmt_r(wages)),
            ("Interest Paid (Borrowed Capital)", fmt_r(interest)),
            ("Entrepreneurial Profit Remaining", "R ???"),
        ],
    )
    prompt = (
        f"Inspect the Factor Payments summary for {s['business']}. "
        f"Calculate the remaining **Entrepreneurial Profit** (`R ???`) left for {s['entrepreneur']} after paying Rent, Labour, and Capital Interest."
    )
    steps = [
        f"Total Factor Costs = Rent ({fmt_r(rent)}) + Salaries/Wages ({fmt_r(wages)}) + Interest ({fmt_r(interest)}) = {fmt_r(rent + wages + interest)}.",
        f"Entrepreneurial Profit = Revenue ({fmt_r(rev)}) - Factor Costs ({fmt_r(rent + wages + interest)}) = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="28_entrepreneurial_profit_loss_calc",
        title="Calculate Entrepreneurial Profit Reward",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{profit}", str(profit)],
        steps=steps,
        hints={
            "tier_1": "Profit is the residual left after paying Rent, Labour, and Capital Interest.",
            "tier_2": f"{fmt_r(rev)} - ({fmt_r(rent)} + {fmt_r(wages)} + {fmt_r(interest)}).",
            "tier_3": f"Entrepreneurial Profit = {ans}.",
        },
        misconception_tags=["forgets_to_deduct_interest_or_rent_before_profit"],
        question_family_id="entrepreneur_profit_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b29_lra_labour_relations_act_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    staff = rng.randint(15, 60)
    prompt = (
        f"Workers among the {staff} employees at {s['business']} in {s['area']} wish to join a registered trade union, elect shop stewards, and engage in peaceful collective bargaining over annual wage increases. "
        f"Which South African Act primarily governs trade unions, collective bargaining, strikes, and fair dismissal rules?"
    )
    ans = "Labour Relations Act (LRA)"
    opts = [
        "Labour Relations Act (LRA)",
        "Occupational Health and Safety Act (OHSA)",
        "Compensation for Occupational Injuries and Diseases Act (COIDA)",
        "National Building Regulations Act",
    ]
    exp = f"The Labour Relations Act (LRA) protects employees' rights to belong to trade unions, bargain collectively, follow fair dismissal rules, and resolve workplace disputes."
    return _make_mcq(
        rng,
        subskill="29_lra_labour_relations_act_purpose",
        title="Labour Relations Act (LRA)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for the law covering employer-employee *relations*, trade unions, and collective bargaining.",
            "tier_2": "Trade unions, strikes, and collective bargaining fall under the Labour Relations Act (LRA).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_lra_and_bcea"],
        question_family_id="lra_purpose",
    )


def _b30_bcea_working_hours_overtime(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    norm_hrs = 45
    max_ot = 10
    prompt = (
        f"Under South Africa's **Basic Conditions of Employment Act (BCEA)**, {s['business']} schedules full-time staff shifts. "
        f"What are the statutory BCEA maximum ordinary working hours per week, maximum overtime hours per week, and minimum overtime pay rate?"
    )
    ans = f"Max {norm_hrs} ordinary hours/week, max {max_ot} hours/week overtime, paid at least 1,5 times the normal wage rate"
    opts = [
        f"Max {norm_hrs} ordinary hours/week, max {max_ot} hours/week overtime, paid at least 1,5 times the normal wage rate",
        "Max 60 ordinary hours/week with unpaid mandatory overtime",
        "Max 30 ordinary hours/week and 30 hours overtime at half rate",
        "Unlimited working hours whenever sales orders increase",
    ]
    exp = f"The BCEA protects employees from overwork by capping ordinary hours at {norm_hrs}/week and overtime at {max_ot}/week (paid at 1,5x normal rate or time off)."
    return _make_mcq(
        rng,
        subskill="30_bcea_working_hours_overtime",
        title="BCEA Working Hours & Overtime Rules",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Recall the standard BCEA weekly hour cap (45 hours) and overtime rate (1,5x).",
            "tier_2": "45 ordinary hrs + max 10 hrs overtime/week at 1,5x normal hourly wage.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_bcea_allows_60_hour_ordinary_weeks"],
        question_family_id="bcea_hours_overtime",
    )


def _b31_bcea_sick_leave_36_month_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    days_off = rng.choice([3, 4])
    prompt = (
        f"{worker}, a full-time employee at {s['business']} in {s['area']}, falls ill and stays off work for {days_off} consecutive working days (more than 2 days in a row). "
        f"Under the **BCEA sick leave rule** (over a 36-month cycle), what can {s['business']} lawfully require before paying sick leave?"
    )
    ans = f"A valid medical certificate signed by a registered medical practitioner because absence exceeded 2 consecutive days"
    opts = [
        f"A valid medical certificate signed by a registered medical practitioner because absence exceeded 2 consecutive days",
        "Immediate permanent dismissal with zero warning",
        "Zero documentation even if absent for 14 consecutive days",
        "Forfeiture of all 36 months of annual vacation leave",
    ]
    exp = f"Under the BCEA, employees get 6 weeks (30 or 36 days) of paid sick leave per 36-month cycle, but a medical certificate is required whenever absent for MORE than 2 consecutive days ({days_off} days here) or more than twice in 8 weeks."
    return _make_mcq(
        rng,
        subskill="31_bcea_sick_leave_36_month_rule",
        title="BCEA Sick Leave & Medical Certificate Rule",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check the BCEA rule triggered when someone misses MORE than 2 consecutive days.",
            "tier_2": "Absence > 2 consecutive days requires a valid medical certificate.",
            "tier_3": ans,
        },
        misconception_tags=["ignores_bcea_2_day_medical_certificate_threshold"],
        question_family_id="bcea_sick_leave_rule",
    )


def _b32_bcea_sick_leave_case_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    used = rng.randint(4, 14)
    entitlement = 30
    remaining = entitlement - used
    ans = f"{remaining} days"
    prompt = (
        f"{worker} works a standard 5-day week at {s['business']}. Under the BCEA, a 5-day-week employee is entitled to {entitlement} paid sick-leave days "
        f"in a 36-month sick-leave cycle. If {worker} has taken {used} verified paid sick days so far in the cycle, how many paid sick-leave days remain?"
    )
    steps = [
        f"Total 36-month BCEA sick leave entitlement (5-day week) = {entitlement} days.",
        f"Subtract days already used ({used}): {entitlement} - {used} = {ans} remaining.",
    ]
    return _make_typed(
        rng,
        subskill="32_bcea_sick_leave_case_calc",
        title="BCEA 36-Month Sick Leave Balance",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, str(remaining)],
        steps=steps,
        hints={
            "tier_1": "Subtract sick days already used from the 30-day 36-month cycle entitlement.",
            "tier_2": f"{entitlement} - {used}.",
            "tier_3": f"Remaining paid sick days = {ans}.",
        },
        misconception_tags=["multiplies_30_days_per_year_instead_of_36_months"],
        question_family_id="bcea_sick_leave_calc",
    )


def _b33_bcea_annual_and_family_leave(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    prompt = (
        f"{worker} has worked full-time for {s['business']} for 12 months. Under South Africa's **BCEA**, "
        f"what minimum **annual leave** AND **family responsibility leave** is {worker} entitled to per leave cycle?"
    )
    ans = "At least 21 consecutive days' paid annual leave AND 3 days' paid family responsibility leave per year"
    opts = [
        "At least 21 consecutive days' paid annual leave AND 3 days' paid family responsibility leave per year",
        "Only 5 days' unpaid annual leave and 0 family leave days",
        "60 paid annual leave days plus unlimited unpaid weekend leave",
        "Annual leave applies only to company directors, not general workers",
    ]
    exp = f"Under the BCEA, full-time staff ({worker}) qualify for at least 21 consecutive days of paid annual leave per year plus 3 paid days of family responsibility leave (for birth, sick child, or close family bereavement)."
    return _make_mcq(
        rng,
        subskill="33_bcea_annual_and_family_leave",
        title="BCEA Annual & Family Responsibility Leave",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Recall the standard SA paid annual vacation minimum (21 consecutive days) and family leave (3 days).",
            "tier_2": "BCEA grants 21 consecutive days annual leave + 3 days family responsibility leave.",
            "tier_3": ans,
        },
        misconception_tags=["underestimates_bcea_annual_leave_entitlement"],
        question_family_id="bcea_annual_family_leave",
    )


def _b34_ohsa_occupational_health_safety(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    workers = rng.randint(5, 18)
    prompt = (
        f"Inside {s['business']}'s workshop in {s['area']}, {workers} workers cut metal and grind steel. "
        f"Which law legally requires {s['entrepreneur']} to fit machine safety guards, maintain clean ventilation, and provide free PPE (goggles, ear muffs, steel-toe boots)?"
    )
    ans = "Occupational Health and Safety Act (OHSA)"
    opts = [
        "Occupational Health and Safety Act (OHSA)",
        "Employment Equity Act (EEA)",
        "Labour Relations Act (LRA)",
        "Consumer Price Index Rules",
    ]
    exp = f"The Occupational Health and Safety Act (OHSA) obliges employers to maintain hazard-free workplaces and supply safety gear (PPE) for all {workers} workshop workers."
    return _make_mcq(
        rng,
        subskill="34_ohsa_occupational_health_safety",
        title="Occupational Health and Safety Act (OHSA)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice safety guards, ventilation, and protective PPE.",
            "tier_2": "Physical workplace hazards and PPE fall under OHSA.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_ohsa_safety_with_coida_compensation"],
        question_family_id="ohsa_purpose",
    )


def _b35_coida_workplace_injury_compensation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    med_cost = rng.randint(6, 22) * 1000
    prompt = (
        f"Despite safety training, {worker} slips on a wet loading bay at {s['business']} while carrying goods on duty and breaks an arm, requiring {fmt_r(med_cost)} in hospital care and 3 weeks off work. "
        f"Which South African Act provides no-fault medical cover and wage compensation for employees injured on duty?"
    )
    ans = "Compensation for Occupational Injuries and Diseases Act (COIDA)"
    opts = [
        "Compensation for Occupational Injuries and Diseases Act (COIDA)",
        "Employment Equity Act (EEA)",
        "Johannesburg Stock Exchange Listing Act",
        "Municipal Rates Rebate Act",
    ]
    exp = f"COIDA covers hospital bills ({fmt_r(med_cost)}) and disability/wage compensation for workers injured on duty or contracting workplace illnesses."
    return _make_mcq(
        rng,
        subskill="35_coida_workplace_injury_compensation",
        title="COIDA Workplace Injury Compensation",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "OHSA prevents accidents BEFORE they happen; which Act pays medical/injury compensation AFTER an on-duty injury?",
            "tier_2": "COIDA = Compensation for Occupational Injuries and Diseases Act.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_ohsa_prevention_with_coida_compensation"],
        question_family_id="coida_purpose",
    )


def _b36_eea_employment_equity_anti_discrimination(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sal = rng.randint(10, 22) * 1000
    prompt = (
        f"Two candidates in {s['area']} hold identical qualifications and apply for a {fmt_r(sal)}/month supervisor job at {s['business']}. "
        f"Refusing to interview or pay a candidate fairly based on gender, race, disability, religion, or pregnancy violates which Act?"
    )
    ans = "Employment Equity Act (EEA)"
    opts = [
        "Employment Equity Act (EEA)",
        "Compensation for Occupational Injuries and Diseases Act (COIDA)",
        "Occupational Health and Safety Act (OHSA)",
        "Municipal Traffic Ordinance",
    ]
    exp = f"The Employment Equity Act (EEA) forbids unfair workplace discrimination in hiring, pay ({fmt_r(sal)}/month), and promotion, while advancing workplace equality."
    return _make_mcq(
        rng,
        subskill="36_eea_employment_equity_anti_discrimination",
        title="Employment Equity Act (EEA)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for the law protecting equal treatment and banning discrimination.",
            "tier_2": "Anti-discrimination & equal employment fairness = Employment Equity Act (EEA).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_eea_with_ohsa_or_coida"],
        question_family_id="eea_purpose",
    )


def _b37_ccma_dispute_resolution_role(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    yrs = rng.randint(2, 7)
    prompt = (
        f"After {yrs} years of loyal service at {s['business']}, {worker} is dismissed without a disciplinary hearing or valid reason. "
        f"To which independent South African statutory body can {worker} refer this unfair dismissal dispute free of charge for conciliation and arbitration?"
    )
    ans = "CCMA (Commission for Conciliation, Mediation and Arbitration)"
    opts = [
        "CCMA (Commission for Conciliation, Mediation and Arbitration)",
        "Johannesburg Stock Exchange (JSE)",
        "South African Revenue Service (SARS)",
        "A private retail bank branch",
    ]
    exp = f"The CCMA handles unfair dismissal and workplace disputes outside expensive courts through conciliation and arbitration."
    return _make_mcq(
        rng,
        subskill="37_ccma_dispute_resolution_role",
        title="Role of the CCMA in Labour Disputes",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Recall the national commission where workers refer unfair dismissal cases.",
            "tier_2": "CCMA = Commission for Conciliation, Mediation and Arbitration.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_ccma_with_sars_or_jse"],
        question_family_id="ccma_role",
    )


def _b38_sa_labour_laws_matching_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("LRA (Labour Relations Act)", "Governs trade unions, collective bargaining & fair dismissal procedures"),
        ("BCEA (Basic Conditions of Employment Act)", "Sets max hours (45h), overtime (1,5x), annual & sick leave minimums"),
        ("OHSA (Occupational Health and Safety Act)", "Mandates safe machinery, hazard control & employer-supplied PPE"),
        ("COIDA", "Compensates medical costs/lost wages from on-duty injuries or diseases"),
        ("EEA (Employment Equity Act)", "Prohibits unfair workplace discrimination & promotes equal opportunity"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["South African Labour Act", "Core Workplace Protection"]
    table_rows = [[(act, "given", False), (prot, "required", True)] for act, prot in chosen]
    cell_hints = {f"t0_r{i}_c1": f"State the primary purpose of {act}." for i, (act, _) in enumerate(chosen)}
    prompt = f"Match each South African Labour Act below to its core workplace protection at {s['business']}."
    return _make_table(
        rng,
        subskill="38_sa_labour_laws_matching_table",
        title="South African Labour Laws Matching Table",
        prompt=prompt,
        journal_type="labour_laws_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Distinguish unions (LRA), hours/leave (BCEA), physical PPE (OHSA), injury payouts (COIDA), discrimination (EEA).",
            "tier_2": "Write concise key duties next to each Act.",
            "tier_3": " | ".join(f"{a}: {p}" for a, p in chosen),
        },
        misconception_tags=["swaps_ohsa_and_coida_or_lra_and_bcea"],
        question_family_id="labour_laws_table",
    )


def _b39_fair_vs_unfair_dismissal_procedure(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    prompt = (
        f"During a busy Friday at {s['business']}, a manager loses patience and shouts at {worker}: 'Pack your bag right now and never come back!' "
        f"Why would the CCMA rule this dismissal **procedurally unfair**?"
    )
    ans = "Because the employer gave no valid investigation, written notice, opportunity to state a defence, or formal disciplinary hearing"
    opts = [
        "Because the employer gave no valid investigation, written notice, opportunity to state a defence, or formal disciplinary hearing",
        "Because employers are legally banned from dismissing workers even after proven theft and fair hearings",
        "Because dismissals may only occur on Mondays via bank EFT",
        "Because only the Johannesburg Stock Exchange may terminate staff",
    ]
    exp = f"Under the LRA, dismissal requires BOTH a fair reason (substantive fairness) AND a proper disciplinary hearing where {worker} can respond (procedural fairness)."
    return _make_mcq(
        rng,
        subskill="39_fair_vs_unfair_dismissal_procedure",
        title="Procedural Fairness in Dismissal",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "What steps must occur BEFORE a dismissal is legally fair?",
            "tier_2": "Investigation, notice, fair hearing, and right to defend/representation are required.",
            "tier_3": ans,
        },
        misconception_tags=["believes_bosses_can_fire_on_the_spot_without_hearing"],
        question_family_id="fair_dismissal_procedure",
    )


def _b40_grievance_procedure_workplace_steps(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    prompt = (
        f"{worker} notices a recurring payroll error and unsafe ladder at {s['business']} in {s['area']}. "
        f"What is the proper chronological **workplace grievance procedure** before escalating externally?"
    )
    ans = "1. Report informally to immediate supervisor -> 2. Lodge formal written grievance -> 3. Management/HR hearing -> 4. Refer to Trade Union or CCMA if unresolved"
    opts = [
        "1. Report informally to immediate supervisor -> 2. Lodge formal written grievance -> 3. Management/HR hearing -> 4. Refer to Trade Union or CCMA if unresolved",
        "1. Immediately break workshop equipment -> 2. Refuse all communication -> 3. Demand cash damages",
        "1. Post confidential payroll details online -> 2. Skip management entirely",
        "1. Appeal directly to the local municipal water office",
    ]
    exp = f"An orderly grievance procedure escalates internally first (supervisor -> written grievance -> management hearing) and only moves externally (Union/CCMA) if unresolved."
    return _make_mcq(
        rng,
        subskill="40_grievance_procedure_workplace_steps",
        title="Proper Workplace Grievance Procedure",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Start internally at the closest supervisor before escalating upwards.",
            "tier_2": "Informal supervisor discussion -> Written grievance -> Management hearing -> Union / CCMA.",
            "tier_3": ans,
        },
        misconception_tags=["skips_internal_grievance_steps"],
        question_family_id="grievance_procedure",
    )


def _b41_fair_employment_practices_audit_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    hrs = rng.choice([52, 56])
    headers = ["Workplace Scenario", "Fair or Unfair?", "Applicable SA Act"]
    table_rows = [
        [(f"Employer forces staff to work {hrs} ordinary hrs/week with no overtime pay.", "given", False), ("Unfair", "required", True), ("BCEA", "required", True)],
        [("Workshop provides free safety goggles, gloves & fire training.", "given", False), ("Fair", "required", True), ("OHSA", "required", True)],
        [("Applicant rejected solely because of gender despite top scores.", "given", False), ("Unfair", "required", True), ("EEA", "required", True)],
        [("Manager holds fair hearing with union steward present before warning.", "given", False), ("Fair", "required", True), ("LRA", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Unfair", "t0_r0_c2": "BCEA",
        "t0_r1_c1": "Fair", "t0_r1_c2": "OHSA",
        "t0_r2_c1": "Unfair", "t0_r2_c2": "EEA",
        "t0_r3_c1": "Fair", "t0_r3_c2": "LRA",
    }
    prompt = f"Audit each workplace scenario from {s['area']} as `Fair` or `Unfair` and name the governing South African Act (`BCEA`, `OHSA`, `EEA`, or `LRA`)."
    return _make_table(
        rng,
        subskill="41_fair_employment_practices_audit_table",
        title="Fair Employment Practices Audit Table",
        prompt=prompt,
        journal_type="employment_audit_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Check working hours (BCEA), physical PPE (OHSA), discrimination (EEA), and disciplinary fairness (LRA).",
            "tier_2": "Row 1 Unfair/BCEA | Row 2 Fair/OHSA | Row 3 Unfair/EEA | Row 4 Fair/LRA.",
            "tier_3": "Complete Fair/Unfair and the exact Act acronym for all 4 rows.",
        },
        misconception_tags=["misidentifies_governing_labour_act"],
        question_family_id="employment_audit_table",
    )


def _b42_impact_of_unfair_practices_on_business(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    prompt = (
        f"Suppose {s['business']} in {s['area']} routinely ignores safety rules, pays late, and shouts at employees. "
        f"Explain FOUR damaging consequences that **unfair employment practices** eventually bring onto the business itself."
    )
    sample = (
        "1. Low morale & falling productivity: Demotivated workers produce careless defects and slow output.\n"
        "2. High absenteeism & staff turnover: Experienced employees quit, forcing constant costly hiring and re-training.\n"
        "3. Industrial action & strikes: Angry workers strike or go-slow, halting revenue completely.\n"
        "4. CCMA fines & reputation damage: Unfair dismissals lead to costly CCMA compensation awards and customer boycotts."
    )
    pts = [
        "Lower morale, reduced productivity, and poor product quality.",
        "Higher absenteeism and costly turnover of experienced staff.",
        "Workplace conflict, strikes, or go-slows disrupting operations.",
        "CCMA legal penalties/fines and damaged business reputation.",
    ]
    return _make_rubric(
        rng,
        subskill="42_impact_of_unfair_practices_on_business",
        title="Business Damage from Unfair Labour Practices",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about worker motivation, staff quitting, strikes, and CCMA legal penalties.",
            "tier_2": "Cover morale/productivity, staff turnover, strikes, and CCMA fines/reputation.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_mistreating_staff_permanently_boosts_profit"],
        question_family_id="unfair_practices_impact",
    )


def _b43_benefits_of_fair_employment_practices(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    retention_yrs = rng.randint(5, 10)
    prompt = (
        f"{s['business']} pays fair wages on time, invests in staff training, and complies strictly with BCEA and OHSA, keeping skilled workers for {retention_yrs}+ years. "
        f"Explain THREE competitive advantages fair employment practices create for {s['business']}."
    )
    sample = (
        f"1. Higher productivity & quality: Loyal, safe, well-treated staff work accurately and care about customer satisfaction.\n"
        f"2. Retained Human Capital ({retention_yrs}+ yrs): Keeping experienced employees avoids repeated recruitment and training expenses.\n"
        "3. Industrial peace & positive brand: Zero unexpected strikes and a respected reputation attract top talent and ethical customers."
    )
    pts = [
        "Boosts worker morale, product quality, and customer service.",
        f"Retains skilled Human Capital ({retention_yrs}+ yrs) and cuts hiring/training turnover costs.",
        "Promotes industrial harmony (fewer disputes/strikes) and enhances brand reputation.",
    ]
    return _make_rubric(
        rng,
        subskill="43_benefits_of_fair_employment_practices",
        title="Competitive Benefits of Fair Labour Practices",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think of the positive opposites of strikes and high turnover.",
            "tier_2": "Discuss quality/productivity, retained Human Capital, and industrial harmony/brand goodwill.",
            "tier_3": sample,
        },
        misconception_tags=["views_labour_compliance_strictly_as_wasted_cost"],
        question_family_id="fair_practices_benefits",
        marks=3,
    )


def _b44_trade_unions_role_and_collective_bargaining(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    members = rng.randint(25, 80)
    prompt = (
        f"Inside an industrial factory near {s['area']}, {members} machine operators belong to a registered Trade Union. "
        f"Explain TWO ways a Trade Union protects its members and ONE way orderly collective bargaining also benefits the employer."
    )
    sample = (
        f"For members: (1) Collective bargaining power negotiates better wages, medical benefits, and safe OHSA conditions for all {members} workers together; "
        "(2) Shop stewards represent members fairly during disciplinary hearings and CCMA disputes.\n"
        "For employer: Structured negotiations with ONE recognised union streamline wage agreements and avoid chaotic wildcat work stoppages."
    )
    pts = [
        f"Member benefit 1: Collective bargaining for fairer wages/benefits/safety across all {members} workers.",
        "Member benefit 2: Legal/shop-steward representation during grievances and disciplinary hearings.",
        "Employer benefit: Predictable structured wage negotiations and reduced unexpected wildcat stoppages.",
    ]
    return _make_rubric(
        rng,
        subskill="44_trade_unions_role_and_collective_bargaining",
        title="Trade Unions & Collective Bargaining",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Show strength in numbers for workers, disciplinary representation, and structured dialogue for management.",
            "tier_2": "Give two worker protections and one management stability benefit.",
            "tier_3": sample,
        },
        misconception_tags=["views_trade_unions_as_purely_adversarial"],
        question_family_id="trade_unions_rubric",
        marks=3,
    )


def _b45_combine_4_factors_case_calculation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    units = rng.choice([200, 250, 300])
    price = rng.randint(120, 180)
    rev = units * price
    rent = rng.randint(4, 9) * 1000
    wages = rng.randint(8, 16) * 1000
    interest = rng.randint(1, 3) * 1000
    materials = rng.randint(5, 10) * 1000
    total_cost = rent + wages + interest + materials
    profit = rev - total_cost
    ans = fmt_r(profit)
    prompt = (
        f"{s['entrepreneur']} manufactures and sells {units} jackets at {fmt_r(price)} each in {s['area']}. "
        f"Monthly factor & input costs are: Factory Rent {fmt_r(rent)}, Seamstress Wages {fmt_r(wages)}, "
        f"Loan Interest {fmt_r(interest)}, and Raw Materials {fmt_r(materials)}. "
        f"Calculate {s['entrepreneur']}'s Entrepreneurial Profit."
    )
    steps = [
        f"Total Sales Revenue = {units} x {fmt_r(price)} = {fmt_r(rev)}.",
        f"Total Costs = {fmt_r(rent)} + {fmt_r(wages)} + {fmt_r(interest)} + {fmt_r(materials)} = {fmt_r(total_cost)}.",
        f"Entrepreneurial Profit = {fmt_r(rev)} - {fmt_r(total_cost)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="45_combine_4_factors_case_calculation",
        title="Four-Factor Costing & Profit Calculation",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{profit}", str(profit)],
        steps=steps,
        hints={
            "tier_1": "First compute Total Revenue (units x price), then add ALL four cost categories.",
            "tier_2": f"{fmt_r(rev)} - {fmt_r(total_cost)}.",
            "tier_3": f"Entrepreneurial Profit = {ans}.",
        },
        misconception_tags=["omits_raw_materials_or_interest_when_computing_profit"],
        question_family_id="four_factors_profit_calc",
    )


def _b46_spot_labour_law_misconceptions(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cost = rng.randint(250, 650)
    statements = [
        (
            f"A manager at {s['business']} tells workshop staff: 'Under the OHSA, workers must buy their own {fmt_r(cost)} safety helmets and goggles out of their weekly wages.' Evaluate this claim.",
            "False — under the Occupational Health and Safety Act (OHSA), the employer must provide mandatory PPE free of charge",
            f"Employers are legally responsible under OHSA to supply mandatory Personal Protective Equipment ({fmt_r(cost)} gear) free to workers, never deducting it from wages.",
        ),
        (
            f"A supervisor at {s['business']} tells staff: 'If you are sick for 4 consecutive working days, BCEA forbids us from ever asking for a doctor's certificate.' Evaluate this claim.",
            "False — under BCEA, an employer may require a valid medical certificate whenever absence exceeds 2 consecutive days",
            "BCEA allows employers to request a valid medical certificate if an employee is off sick for MORE than 2 consecutive days or more than twice in 8 weeks.",
        ),
    ]
    prompt, ans, exp = rng.choice(statements)
    opts = [
        ans,
        "True — employers face zero safety or sick-leave verification rules under SA law",
        "True — PPE costs must always come from the employee's annual leave allowance",
        "False — COIDA cancels all sick leave after 12 months",
    ]
    return _make_mcq(
        rng,
        subskill="46_spot_labour_law_misconceptions",
        title="Labour Law Statement Audit (True/False)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Test the manager's claim directly against OHSA and BCEA statutory rules.",
            "tier_2": "Employers supply PPE free (OHSA) and may ask for medical certificates after > 2 sick days (BCEA).",
            "tier_3": ans,
        },
        misconception_tags=["accepts_illegal_ppe_deduction_or_sick_leave_myth"],
        question_family_id="labour_law_audit",
    )


def _b47_rural_vs_urban_factor_constraints(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    prompt = (
        f"Compare factor-of-production conditions for an entrepreneur starting an agro-processing venture in {s['rural_area']} (rural) "
        f"versus an urban industrial park in {s['urban_area']}. Contrast TWO advantages or constraints across Land, Labour, and Capital."
    )
    sample = (
        f"1. Natural Resources / Land & Rent: {s['rural_area']} offers affordable spacious land and raw farm produce close by, whereas {s['urban_area']} has higher industrial rents.\n"
        f"2. Skilled Labour & Infrastructure (Capital): {s['urban_area']} offers larger pools of scarce ICT/engineering skills, high-speed internet, and reliable transport, whereas {s['rural_area']} often faces higher logistics costs and scarcer technical specialists."
    )
    pts = [
        f"Contrasts Land/Rent access: affordable open land & raw inputs in {s['rural_area']} vs pricey premises in {s['urban_area']}.",
        f"Contrasts Labour/Capital infrastructure: wider scarce-skills & logistics/connectivity in {s['urban_area']} vs higher transport/skills gaps in {s['rural_area']}.",
    ]
    return _make_rubric(
        rng,
        subskill="47_rural_vs_urban_factor_constraints",
        title="Rural vs Urban Factor Conditions in SA",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Weigh rural land/raw produce access against urban infrastructure and scarce skilled specialists.",
            "tier_2": "Compare Land/Rent AND Skilled Labour/Logistics across rural vs urban SA regions.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_rural_and_urban_factor_availability_are_identical"],
        question_family_id="rural_urban_factors",
        marks=2,
    )


def _b48_sustainable_production_capital_labour_balance(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cost_mach = rng.randint(90, 220) * 1000
    prompt = (
        f"{s['business']} invests {fmt_r(cost_mach)} in automated packaging machinery (Physical Capital) that speeds up output, "
        f"potentially making 4 manual packers redundant. Advise {s['entrepreneur']} on TWO socially responsible, LRA-compliant ways to balance new Physical Capital with existing Labour."
    )
    sample = (
        "1. Reskilling & redeployment: Train the 4 packers to become semi-skilled machine operators, quality checkers, or dispatch coordinators instead of dismissing them.\n"
        "2. LRA consultation & fair process: Consult affected staff/union early on expansion plans so increased output funds new marketing/delivery roles."
    )
    pts = [
        "Upskills and redeploys existing manual workers into machine operation, quality control, or expanded dispatch roles.",
        "Consults workers/unions transparently under LRA fairness rather than sudden retrenchment.",
    ]
    return _make_rubric(
        rng,
        subskill="48_sustainable_production_capital_labour_balance",
        title="Balancing Automation Capital & Workforce",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about investing in Human Capital (retraining) alongside Physical Capital (machines).",
            "tier_2": "Focus on reskilling/redeployment + transparent LRA consultation.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_new_machinery_always_requires_retrenchments"],
        question_family_id="capital_labour_balance_rubric",
        marks=2,
    )


def _b49_case_study_labour_dispute_ccma(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    hrs = rng.choice([54, 58])
    prompt = (
        f"Workers at a workshop near {s['area']} work {hrs} hours/week at flat pay with zero overtime multiplier, receive no safety boots near heavy cutters, "
        f"and two workers who complained were fired immediately without a hearing. "
        f"Identify: (a) TWO South African Labour Acts breached, (b) the statutory dispute body where fired staff can seek relief, and (c) ONE corrective action management must take."
    )
    sample = (
        f"(a) Breached Acts: **BCEA** ({hrs} hrs/week & unpaid overtime rate violation) and **OHSA** (no protective safety boots near dangerous equipment) — plus **LRA** (unfair dismissal without a hearing).\n"
        "(b) Dispute body: **CCMA** (Commission for Conciliation, Mediation and Arbitration).\n"
        "(c) Corrective step: Immediately cap shifts at 45 hrs + 1,5x overtime, issue free OHSA PPE, and reinstate/hold fair disciplinary procedures."
    )
    pts = [
        "Identifies BCEA breach (excess hours / missing 1,5x overtime) and OHSA breach (missing PPE).",
        "Identifies LRA breach / names CCMA as dispute resolution body.",
        "Proposes concrete corrective compliance action (PPE, lawful shift hours, fair hearings).",
    ]
    return _make_rubric(
        rng,
        subskill="49_case_study_labour_dispute_ccma",
        title="Case Study: Labour Law Breaches & CCMA Relief",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Link hours/overtime -> BCEA, safety boots -> OHSA, firing without hearing -> LRA/CCMA.",
            "tier_2": "Name specific breached Acts, state CCMA, and prescribe corrective workplace compliance.",
            "tier_3": sample,
        },
        misconception_tags=["omits_ccma_or_mixes_up_bcea_and_ohsa_violations"],
        question_family_id="labour_case_study_ccma",
        marks=4,
    )


def _b50_comprehensive_factors_capstone(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rev = rng.randint(80, 150) * 1000
    rent = rng.randint(8, 15) * 1000
    wages = rng.randint(22, 42) * 1000
    interest = rng.randint(3, 8) * 1000
    profit = rev - (rent + wages + interest)
    svg = svg_factor_card(
        f"{s['business']} — Annual Production & Labour Snapshot",
        f"Entrepreneur: {s['entrepreneur']} ({s['area']})",
        [
            ("Monthly Sales Output Revenue", fmt_r(rev)),
            ("Workshop Premises Rent (Natural Resources)", fmt_r(rent)),
            ("Skilled & Semi-skilled Payroll (Labour)", fmt_r(wages)),
            ("Machinery Loan Interest (Borrowed Capital)", fmt_r(interest)),
            ("Safety & Hours Audit", "PPE Supplied | 42 hrs/week"),
        ],
    )
    prompt = (
        f"Inspect the Production & Labour Snapshot for {s['business']}. "
        f"(a) Calculate {s['entrepreneur']}'s monthly Entrepreneurial Profit. "
        f"(b) Verify whether the 42 hrs/week schedule and free PPE satisfy **BCEA** and **OHSA**. "
        f"(c) State ONE long-term benefit of continuing to invest in worker training (Human Capital)."
    )
    sample = (
        f"(a) Entrepreneurial Profit = {fmt_r(rev)} - ({fmt_r(rent)} + {fmt_r(wages)} + {fmt_r(interest)}) = {fmt_r(profit)}.\n"
        "(b) Yes: 42 hours/week sits safely below the BCEA maximum of 45 ordinary hours/week, and free PPE complies with OHSA safety obligations.\n"
        "(c) Training builds Human Capital, raising output per worker, reducing defects, and improving staff loyalty."
    )
    pts = [
        f"Calculates Entrepreneurial Profit accurately as {fmt_r(profit)}.",
        "Verifies 42 hrs/week <= 45h BCEA limit AND free PPE meets OHSA compliance.",
        "Identifies productivity, quality, or retention gains from Human Capital training.",
    ]
    return _make_rubric(
        rng,
        subskill="50_comprehensive_factors_capstone",
        title="Comprehensive Factors of Production & Labour Capstone",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Compute Revenue - (Rent + Wages + Interest), check BCEA 45h & OHSA PPE rules, and explain Human Capital.",
            "tier_2": f"Profit = {fmt_r(profit)}; 42h <= 45h BCEA; PPE meets OHSA.",
            "tier_3": sample,
        },
        misconception_tags=["misses_profit_cost_deduction_or_statutory_compliance"],
        question_family_id="factors_capstone",
        marks=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


ARCHETYPES_26_50 = {
    "26_entrepreneur_seven_qualities_id": _b26_entrepreneur_seven_qualities_id,
    "27_calculated_vs_reckless_risk": _b27_calculated_vs_reckless_risk,
    "28_entrepreneurial_profit_loss_calc": _b28_entrepreneurial_profit_loss_calc,
    "29_lra_labour_relations_act_purpose": _b29_lra_labour_relations_act_purpose,
    "30_bcea_working_hours_overtime": _b30_bcea_working_hours_overtime,
    "31_bcea_sick_leave_36_month_rule": _b31_bcea_sick_leave_36_month_rule,
    "32_bcea_sick_leave_case_calc": _b32_bcea_sick_leave_case_calc,
    "33_bcea_annual_and_family_leave": _b33_bcea_annual_and_family_leave,
    "34_ohsa_occupational_health_safety": _b34_ohsa_occupational_health_safety,
    "35_coida_workplace_injury_compensation": _b35_coida_workplace_injury_compensation,
    "36_eea_employment_equity_anti_discrimination": _b36_eea_employment_equity_anti_discrimination,
    "37_ccma_dispute_resolution_role": _b37_ccma_dispute_resolution_role,
    "38_sa_labour_laws_matching_table": _b38_sa_labour_laws_matching_table,
    "39_fair_vs_unfair_dismissal_procedure": _b39_fair_vs_unfair_dismissal_procedure,
    "40_grievance_procedure_workplace_steps": _b40_grievance_procedure_workplace_steps,
    "41_fair_employment_practices_audit_table": _b41_fair_employment_practices_audit_table,
    "42_impact_of_unfair_practices_on_business": _b42_impact_of_unfair_practices_on_business,
    "43_benefits_of_fair_employment_practices": _b43_benefits_of_fair_employment_practices,
    "44_trade_unions_role_and_collective_bargaining": _b44_trade_unions_role_and_collective_bargaining,
    "45_combine_4_factors_case_calculation": _b45_combine_4_factors_case_calculation,
    "46_spot_labour_law_misconceptions": _b46_spot_labour_law_misconceptions,
    "47_rural_vs_urban_factor_constraints": _b47_rural_vs_urban_factor_constraints,
    "48_sustainable_production_capital_labour_balance": _b48_sustainable_production_capital_labour_balance,
    "49_case_study_labour_dispute_ccma": _b49_case_study_labour_dispute_ccma,
    "50_comprehensive_factors_capstone": _b50_comprehensive_factors_capstone,
}
