"""Grade 8 EMS - The National Budget: Archetypes 26 to 50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/02. The National Budget.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES as PERSON_NAMES
from .national_budget_archetypes_01_25 import (
    BUSINESS_NAMES,
    _build_mcq,
    _build_short,
    _build_table,
    _fmt_r,
    _make_cell,
)


def arch_26_emergency_fund_contingency_reserve_purpose(rng: random.Random) -> Dict[str, Any]:
    crisis = rng.choice([
        "a sudden coastal storm damaging bridges and schools",
        "an unexpected outbreak requiring urgent medical supplies",
        "a sharp global fuel shock and severe agricultural drought",
    ])
    reserve_bn = rng.choice([8, 10, 12, 15])
    prompt = (
        f"South Africa's National Budget includes an unallocated **Emergency Fund (Contingency Reserve)** of **R{reserve_bn} billion** "
        f"to cover unforeseen events such as **{crisis}**.\n\n"
        "Why does National Treasury keep this reserve separate from ordinary departmental spending?"
    )
    correct = "To respond rapidly to unpredictable disasters, epidemics, or economic shocks without having to abruptly shut down schools, hospitals, or social grants."
    distractors = [
        "To fund annual overseas holiday flights for municipal councillors.",
        "Because departments are legally forbidden from spending money on water or roads during normal months.",
        "To lend money interest-free to profitable international luxury brands.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_26",
        subskill="26_emergency_fund_contingency_reserve_purpose",
        title="Purpose of the Budget Emergency Fund",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Setting aside **R{reserve_bn} billion** in the **Emergency Fund (Contingency Reserve)** gives government rapid disaster-relief funds "
            f"when events like **{crisis}** hit unexpectedly."
        ),
        hints={
            "tier_1": "What happens if an unplanned disaster strikes mid-year and zero reserve money exists?",
            "tier_2": "A contingency reserve cushions emergencies without disrupting essential ongoing services.",
            "tier_3": correct,
        },
        misconception_tags=["viewing_contingency_reserves_as_wasted_idle_cash"],
    )


def arch_27_japanese_2011_tsunami_supply_chain_and_reserve_lesson(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    loss_usd = rng.choice([250, 300])
    prompt = (
        f"In 2011, a massive earthquake and tsunami hit Japan, causing an estimated **US${loss_usd} billion** in damage (around 25 trillion yen) "
        f"and halting electronics and vehicle-part factories worldwide — affecting assembly suppliers even in regions like **{area}** and firms such as **{biz}**.\n\n"
        "Explain **two fiscal lessons** this global shock teaches South Africa's National Treasury when planning the **National Budget**."
    )
    expected = (
        f"1) South Africa must hold a strong Emergency Fund (Contingency Reserve) because natural disasters (like Japan's US${loss_usd} bn shock) strike unexpectedly; "
        "2) Global supply disruptions can slow local firms and tax collection, so fiscal buffers and diversified local industry are essential."
    )
    sol = (
        f"**Fiscal Lessons from the 2011 Japanese Tsunami (US${loss_usd} bn Case) [3 marks]:**\n\n"
        "1. **Dedicated Disaster Reserve:** Major disasters strike unexpectedly and cost billions, proving why South Africa budgets a ring-fenced **Emergency Fund** each year **[1.5]**.\n"
        f"2. **Global Interdependence & Tax Resilience:** Supply-chain delays hurt domestic businesses like **{biz}** and lower corporate/VAT tax receipts, so Treasury needs prudent reserves and diversified domestic capacity **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_27",
        subskill="27_japanese_2011_tsunami_supply_chain_and_reserve_lesson",
        title="Disaster Reserves & Global Supply-Chain Shocks",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Link the scale of the disaster cost to reserves, and factory shutdowns in Japan to SA supply/tax risk.",
            "tier_2": "Mention Emergency Fund preparedness and global supply-chain impact on domestic business/revenue.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Need for an Emergency Fund / Contingency Reserve for unexpected disasters", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Global supply disruption hits local firms/tax receipts so prudent buffers matter", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_foreign_disasters_cannot_affect_sa_budget"],
    )


def arch_28_fiscal_policy_growth_tax_base_virtuous_cycle_diagram(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    infra_spend = rng.choice([450, 600, 750])
    new_jobs = rng.choice([1200, 1600, 2000])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="220" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Growth &amp; Tax-Base Cycle: {area}</text>'
        '<rect x="20" y="55" width="145" height="75" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="92" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">1. Budget Investment</text>'
        f'<text x="92" y="106" text-anchor="middle" font-size="11" fill="#1e40af">Roads/SMMEs R{infra_spend}m</text>'
        '<line x1="165" y1="92" x2="195" y2="92" stroke="#334155" stroke-width="2"/>'
        '<rect x="195" y="55" width="145" height="75" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="267" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">2. Jobs Created</text>'
        f'<text x="267" y="106" text-anchor="middle" font-size="11" fill="#166534">+{new_jobs} Workers</text>'
        '<line x1="340" y1="92" x2="370" y2="92" stroke="#334155" stroke-width="2"/>'
        '<rect x="370" y="55" width="135" height="75" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="437" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">3. Wider Tax Base</text>'
        '<text x="437" y="106" text-anchor="middle" font-size="11" fill="#92400e">Wages + Spending</text>'
        '<line x1="505" y1="92" x2="535" y2="92" stroke="#334155" stroke-width="2"/>'
        '<rect x="535" y="55" width="125" height="75" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>'
        '<text x="597" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#4c1d95">4. Higher SARS</text>'
        '<text x="597" y="106" text-anchor="middle" font-size="11" fill="#5b21b6">PAYE + VAT Yield</text>'
        '<path d="M 597 130 Q 340 198 92 130" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="5,4"/>'
        '<text x="340" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">Reinvested into Future Services &amp; Redress</text>'
        '</svg>'
    )
    prompt = (
        f"Examine the fiscal growth diagram for **{area}**, where **R{infra_spend} million** in infrastructure and SMME support helps create **{new_jobs} new jobs**.\n\n"
        "Trace step-by-step how spending **R{0} million** on growth and job creation leads to **higher future government tax revenue** without raising tax rates.".format(infra_spend)
    )
    expected = (
        f"Budget investment (R{infra_spend}m in infrastructure/SMMEs) creates {new_jobs} jobs; "
        "newly employed workers earn wages (paying PAYE) and spend at local firms (generating VAT and corporate profit taxes), "
        "widening the tax base so SARS collects more revenue for future services."
    )
    sol = (
        f"**Virtuous Fiscal Growth & Tax-Base Cycle ({area}) [4 marks]:**\n\n"
        f"1. **Productive Investment:** Spending **R{infra_spend} million** on infrastructure and SMME finance enables firms to expand **[1]**.\n"
        f"2. **Employment & Income:** Creating **{new_jobs} jobs** shifts residents from unemployment into wage-earning households **[1]**.\n"
        "3. **Wider Tax Base:** More wage earners pay **PAYE**, spend more generating **15% VAT**, and boost business profits subject to **Corporate Income Tax** **[1]**.\n"
        "4. **Sustainable Future Funding:** Rising total SARS receipts fund additional clinics, schools, and infrastructure without punishing tax-rate hikes **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_28",
        subskill="28_fiscal_policy_growth_tax_base_virtuous_cycle_diagram",
        title="How Budget-Driven Growth Expands the Tax Base",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Follow steps 1 -> 2 -> 3 -> 4 in the flow diagram.",
            "tier_2": "Explain jobs -> wages & shopping -> more PAYE, VAT, and business tax -> larger future budget.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Public investment stimulates SMMEs and infrastructure activity", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Job creation gives households regular wages", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "More PAYE, VAT, and company tax widens the tax base", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Higher total tax yield funds future public services sustainably", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_higher_tax_revenue_only_comes_from_raising_tax_rates"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_29_subsidies_on_basic_goods_brown_bread_milk(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    family = rng.choice(PERSON_NAMES)
    unsub_loaf = rng.choice([18, 20, 22])
    subsidy_loaf = rng.choice([4, 5, 6])
    loaves_month = rng.choice([25, 30, 35])
    sub_price = unsub_loaf - subsidy_loaf
    monthly_saving = subsidy_loaf * loaves_month

    prompt = (
        f"To promote affordability for low-income households in **{area}**, government keeps brown bread VAT zero-rated and subsidises staple production.\n"
        f"Suppose the unsubsidised price of a loaf of brown bread is **{_fmt_r(unsub_loaf)}**, and a targeted subsidy lowers the shelf price by **{_fmt_r(subsidy_loaf)}** per loaf. "
        f"**{family}**'s household buys **{loaves_month} loaves** per month.\n\n"
        "Calculate:\n"
        "(a) The **subsidised price** per loaf;\n"
        f"(b) **{family}**'s **total monthly grocery saving** on bread."
    )
    expected = f"(a) Subsidised price = {_fmt_r(sub_price)} per loaf; (b) Monthly saving = {_fmt_r(monthly_saving)}"
    sol = (
        f"**Basic Food Subsidy Impact ({family}'s Household) [3 marks]:**\n\n"
        f"**(a) Subsidised Price per Loaf:** ${_fmt_r(unsub_loaf)} - {_fmt_r(subsidy_loaf)} = {_fmt_r(sub_price)}$ **[1]**\n\n"
        f"**(b) Monthly Household Saving ({loaves_month} loaves):** ${loaves_month} \\times {_fmt_r(subsidy_loaf)} = {_fmt_r(monthly_saving)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_29",
        subskill="29_subsidies_on_basic_goods_brown_bread_milk",
        title="Food Subsidies & Low-Income Household Relief",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "A subsidy lowers the price paid by the consumer.",
            "tier_2": f"Multiply the {_fmt_r(subsidy_loaf)} per-loaf saving by {loaves_month} loaves.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subsidised loaf price = {_fmt_r(sub_price)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Monthly household saving = {_fmt_r(monthly_saving)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_subsidy_to_price_instead_of_subtracting"],
        qtype="calculation",
    )


def arch_30_public_works_epwp_job_creation_calculation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    workers = rng.choice([40, 50, 60])
    daily_stipend = rng.choice([160, 180, 200])
    days = rng.choice([20, 22])
    total_wages = workers * daily_stipend * days
    project = rng.choice(["clearing invasive weeds and repairing storm drains", "maintaining school grounds and paving clinic walkways"])

    prompt = (
        f"Through an Expanded Public Works Programme (**EPWP**) budget allocation in **{area}**, **{workers} unemployed local residents** "
        f"are hired for **{days} workdays** this month at **{_fmt_r(daily_stipend)}** per day while **{project}**.\n\n"
        "(a) Calculate the **total monthly wages** injected into local households;\n"
        "(b) State **two economic/social benefits** of public works job creation for the community."
    )
    expected = (
        f"(a) Total monthly wages = {_fmt_r(total_wages)}. "
        f"(b) 1) Gives jobless households earned income and work skills; 2) Leaves lasting community assets ({project}) while boosting local shop spending."
    )
    sol = (
        f"**EPWP Public Works Calculation ({area}) [4 marks]:**\n\n"
        f"**(a) Total Wages Paid:** ${workers} \\times {days} \\times {_fmt_r(daily_stipend)} = {_fmt_r(total_wages)}$ **[2]**\n\n"
        "**(b) Two Community Benefits [2 marks]:**\n"
        "1. Provides earned income, dignity, and workplace experience to previously unemployed residents **[1]**.\n"
        f"2. Improves public community assets (**{project}**) while wages circulate at local businesses **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_30",
        subskill="30_public_works_epwp_job_creation_calculation",
        title="Public Works (EPWP) Budget & Wage Injection",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Multiply workers x days worked x daily wage rate.",
            "tier_2": "Give BOTH a household skills/income benefit and a community asset/retail spending benefit.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total monthly wages = {_fmt_r(total_wages)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Two valid benefits (household wages/skills + public asset/local spending)", "marks": 2, "editable": True},
        ],
        misconception_tags=["multiplying_workers_by_rate_but_forgetting_days"],
        qtype="calculation",
    )


def arch_31_reducing_economic_inequality_five_mechanisms_table(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("RDP Low-Cost Housing", "Provides safe formal homes and property assets for low-income families"),
        ("School Nutrition Programme", "Gives learners nutritious daily meals so hunger does not block learning"),
        ("Free Basic Water & Electricity", "Guarantees essential monthly survival lifeline quotas to indigent households"),
        ("Free Child & Maternal Healthcare", "Eliminates clinic fees for young children and pregnant mothers"),
        ("Social Security Grants", "Supplies monthly income support to elderly, disabled, and child caregivers"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Redress / Anti-Poverty Programme", "Core Inequality Barrier Addressed (Choose or Write Concisely)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Redress / Anti-Poverty Programme | Core Inequality Barrier Addressed |", "| :--- | :--- |"]
    for idx, (prog, barrier) in enumerate(chosen):
        c0 = f"r{idx}c0"
        c1 = f"r{idx}c1"
        rows.append([_make_cell(c0, "", "required"), _make_cell(c1, barrier, "given")])
        correct_map[c0] = prog
        cell_hints[c0] = "Match: RDP Low-Cost Housing, School Nutrition Programme, Free Basic Water & Electricity, Free Child & Maternal Healthcare, or Social Security Grants."
        memo_lines.append(f"| {prog} | {barrier} |")

    worked = "**Completed Inequality-Reduction Schedule [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{b} -> {p}" for p, b in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_bud_31",
        subskill="31_reducing_economic_inequality_five_mechanisms_table",
        title="Budget Programmes Reducing Economic Inequality",
        prompt=(
            "Match each household inequality barrier to the exact South African National Budget programme from this list: "
            "**RDP Low-Cost Housing**, **School Nutrition Programme**, **Free Basic Water & Electricity**, **Free Child & Maternal Healthcare**, or **Social Security Grants**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Read the household barrier in the right column and identify the matching public programme.",
            "tier_2": "Use exact programme names supplied in the prompt.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Matches row {i+1}: {chosen[i][0]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_rdp_housing_with_social_security_grants"],
    )


def arch_32_school_nutrition_programme_human_capital_benefit(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    learners = rng.choice([540, 720, 880])
    prompt = (
        f"At a primary school in **{area}**, **{learners} learners** receive a cooked meal every morning via the National School Nutrition Programme.\n\n"
        "How does funding school nutrition help reduce **both** immediate poverty and long-term income inequality?"
    )
    correct = "Hungry children can concentrate, attend school consistently, pass grades, and eventually qualify for higher-paying skilled jobs."
    distractors = [
        "It replaces the need to pay teachers' salaries across public schools.",
        "Meals are sold only to corporate executives at 15% VAT.",
        "Learners stop attending school once daily school meals are provided.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_32",
        subskill="32_school_nutrition_programme_human_capital_benefit",
        title="School Nutrition: Human Capital & Redress",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Feeding **{learners} learners** in **{area}** prevents malnutrition from forcing children out of class, lifting academic performance and breaking intergenerational poverty."
        ),
        hints={
            "tier_1": "Think of how hunger affects classroom concentration today and employment opportunities 10 years later.",
            "tier_2": "Link daily nutrition -> school attendance/learning -> future employability.",
            "tier_3": correct,
        },
        misconception_tags=["treating_school_feeding_as_unrelated_to_future_skills"],
    )


def arch_33_free_basic_water_and_electricity_poverty_alleviation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    free_kl = 6
    free_kwh = 50
    prompt = (
        f"Indigent (very low-income) registered households in **{area}** receive a monthly lifeline of **{free_kl} kilolitres of free basic water** "
        f"and **{free_kwh} kWh of free basic electricity** funded via National Budget transfers to municipalities.\n\n"
        "Give **two ways** this lifeline policy narrows living-standard inequality."
    )
    expected = (
        f"1) Guarantees basic hygiene, safe drinking water ({free_kl} kl), and lighting/cooking energy ({free_kwh} kWh) regardless of household cash income; "
        "2) Frees tiny household cash budgets to spend on nutritious food, transport, and school items."
    )
    sol = (
        f"**Free Basic Services Policy ({area}) [3 marks]:**\n\n"
        f"1. **Minimum Standard of Dignity & Health:** Every indigent family secures **{free_kl} kl** clean water for sanitation/drinking and **{free_kwh} kWh** electricity for safe lighting/study **[1.5]**.\n"
        "2. **Household Budget Relief:** Money saved on basic utilities stays available for food, clinic travel, and learners' school needs **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_33",
        subskill="33_free_basic_water_and_electricity_poverty_alleviation",
        title="Free Basic Water & Electricity Lifeline Policy",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Consider health/study conditions inside the home AND cash left over for food.",
            "tier_2": "Give one direct utility/health benefit and one household disposable-income benefit.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Ensures health, sanitation, and safe energy/lighting access", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Frees scarce household income for food and schooling", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_indigent_households_get_unlimited_free_power"],
    )


def arch_34_progressive_vs_regressive_tax_fairness(rng: random.Random) -> Dict[str, Any]:
    low_earner = rng.choice(PERSON_NAMES)
    high_earner = rng.choice([n for n in PERSON_NAMES if n != low_earner])
    prompt = (
        f"**{low_earner}** earns **R10 000** per month while **{high_earner}** earns **R80 000** per month. "
        "Under South Africa's **Personal Income Tax (PAYE)** system, higher income brackets pay a **higher percentage tax rate** than lower earners.\n\n"
        "Why is South Africa's personal income tax structure described as **progressive**, and how does it support equity?"
    )
    correct = "Higher earners pay a larger percentage share of their income than lower earners, collecting more from those with greater ability to pay to fund social services."
    distractors = [
        "Low earners pay 45% tax while high earners pay 5% tax.",
        "Everyone pays the exact same flat R5 000 Rand regardless of salary.",
        "Only retired pensioners pay PAYE while working executives are exempt.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_34",
        subskill="34_progressive_vs_regressive_tax_fairness",
        title="Progressive Income Tax & Ability to Pay",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Because **{high_earner}** pays a higher percentage rate on higher earnings than **{low_earner}**, PAYE is **progressive**, redistributing resources toward public services and grants."
        ),
        hints={
            "tier_1": "Notice how the tax RATE (%) rises as income rises.",
            "tier_2": "Progressive taxation matches tax burden to ability to pay.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_progressive_tax_with_flat_rate_vat"],
    )


def arch_35_tax_base_expansion_vs_increasing_tax_rates(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    new_firms = rng.choice([250, 400, 550])
    prompt = (
        f"Facing a revenue shortfall, one official suggests doubling VAT and PAYE rates, while a National Treasury economist advises helping **{new_firms} informal enterprises in {area}** formalise, hire workers, and register for tax.\n\n"
        "Explain why **widening the tax base** through growth and formalisation is usually healthier for the economy than sharply hiking tax rates."
    )
    expected = (
        f"Bringing {new_firms} new firms and employed workers into the tax net generates sustainable tax revenue from more taxpayers, "
        "whereas steep tax-rate hikes discourage work, shrink consumer spending, and push businesses out of compliance."
    )
    sol = (
        "**Widening the Tax Base vs Hiking Rates [3 marks]:**\n\n"
        f"1. **Broader Contribution:** Formalising **{new_firms} firms** creates more wage earners and profitable businesses paying PAYE, VAT, and CIT **[1.5]**.\n"
        "2. **Avoiding Economic Slowdown:** Steep tax-rate hikes drain household spending and business investment, whereas a growing tax base collects more sustainably **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_35",
        subskill="35_tax_base_expansion_vs_increasing_tax_rates",
        title="Widening the Tax Base vs Tax-Rate Hikes",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Compare collecting from MORE jobs/firms against squeezing EXISTING taxpayers harder.",
            "tier_2": "Highlight broader sustainable revenue vs risk of slowing consumer spending and investment.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "More jobs/formal businesses increase total taxpayer numbers", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Extreme tax hikes can hurt spending, jobs, or compliance", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["thinking_raising_tax_rates_always_raises_growth"],
    )


def arch_36_debt_servicing_crowding_out_social_spending(rng: random.Random) -> Dict[str, Any]:
    tot_budget = rng.choice([2000, 2200, 2500])  # R billion
    debt_pct = rng.choice([18, 20, 22])
    debt_cost = tot_budget * debt_pct // 100
    school_cost_m = 50  # R50m per modern public secondary school (0.05 bn = 50m -> clean R billion math using R million!)
    # Use clean R million figures:
    budget_m = rng.choice([10000, 12000, 15000])
    debt_m = budget_m * debt_pct // 100
    clinics_lost = debt_m // 25

    prompt = (
        f"Suppose a regional fiscal allocation totals **{_fmt_r(budget_m * 1000000)}**, and **{debt_pct}%** must be spent immediately on **interest servicing costs** on past government debt.\n\n"
        f"(a) Calculate the exact **debt-interest cost** in Rands;\n"
        "(b) If building and equipping one local primary clinic costs **R25 000 000**, calculate how many clinics equal that annual debt-interest bill."
    )
    expected = f"(a) Debt interest = {_fmt_r(debt_m * 1000000)}; (b) Equivalent to {clinics_lost} clinics"
    sol = (
        "**Debt-Servicing Opportunity Cost [4 marks]:**\n\n"
        f"**(a) Annual Debt Interest ({debt_pct}%):**\n"
        f"$${_fmt_r(budget_m * 1000000)} \\times {debt_pct}\\% = {_fmt_r(debt_m * 1000000)}$$ **[2]**\n\n"
        "**(b) Clinic Opportunity Cost (at R25 000 000 per clinic):**\n"
        f"$${_fmt_r(debt_m * 1000000)} \\div R25\\ 000\\ 000 = {clinics_lost}\\text{{ clinics}}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_36",
        subskill="36_debt_servicing_crowding_out_social_spending",
        title="Debt Servicing Opportunity Cost (Clinics Forgone)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Find {debt_pct}% of {_fmt_r(budget_m * 1000000)} first.",
            "tier_2": "Divide the debt interest amount by R25 000 000.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Debt interest = {_fmt_r(debt_m * 1000000)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Clinics forgone = {clinics_lost}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_millions_zeros_during_division"],
        qtype="calculation",
    )


def arch_37_multi_year_budget_comparison_growth_calc(rng: random.Random) -> Dict[str, Any]:
    sector = rng.choice(["Public Transport & Roads", "Community Health Clinics", "RDP Human Settlements"])
    yr1 = rng.choice([200, 250, 400, 500])  # R million
    pct_inc = rng.choice([8, 10, 12, 15])
    increase = yr1 * pct_inc // 100
    yr2 = yr1 + increase

    prompt = (
        f"Last financial year, the allocation for **{sector}** was **R{yr1} million**. "
        f"In the new National Budget, National Treasury increases this vote by **{pct_inc}%**.\n\n"
        "(a) Calculate the **Rand increase** in the budget;\n"
        f"(b) State the **new total allocation** for **{sector}**."
    )
    expected = f"(a) Increase = R{increase} million; (b) New allocation = R{yr2} million"
    sol = (
        f"**Year-on-Year Budget Change ({sector}) [3 marks]:**\n\n"
        f"**(a) Rand Increase ({pct_inc}%):**\n"
        f"$$R{yr1}\\text{{ m}} \\times {pct_inc}\\% = R{increase}\\text{{ million}}$$ **[2]**\n\n"
        "**(b) New Total Allocation:**\n"
        f"$$R{yr1}\\text{{ m}} + R{increase}\\text{{ m}} = R{yr2}\\text{{ million}}$$ **[1]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_37",
        subskill="37_multi_year_budget_comparison_growth_calc",
        title="Year-on-Year Sector Budget Increase",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Find {pct_inc}% of R{yr1} million.",
            "tier_2": "Add the Rand increase onto the original R{yr1} million baseline.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Increase = R{increase} million", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"New total = R{yr2} million", "marks": 1, "editable": True},
        ],
        misconception_tags=["reporting_increase_only_as_final_budget"],
        qtype="calculation",
    )


def arch_38_indirect_tax_household_monthly_burden_calc(rng: random.Random) -> Dict[str, Any]:
    person = rng.choice(PERSON_NAMES)
    zero_food = rng.choice([1200, 1500, 1800])  # 0% VAT
    vatable_goods = rng.choice([2000, 2400, 3000])  # excl VAT -> 15%
    vat_paid = vatable_goods * 15 // 100
    fuel_litres = rng.choice([50, 60, 80])
    fuel_tax_per_l = 6  # simplified exact integer levy R6/L
    fuel_tax_paid = fuel_litres * fuel_tax_per_l
    total_indirect = vat_paid + fuel_tax_paid

    prompt = (
        f"During one month, **{person}** buys:\n"
        f"- Zero-rated basic foods (brown bread, maize meal, milk): **{_fmt_r(zero_food)}** (0% VAT)\n"
        f"- Standard VAT-able household goods priced **{_fmt_r(vatable_goods)}** excluding **15% VAT**\n"
        f"- **{fuel_litres} litres** of petrol carrying **R{fuel_tax_per_l},00** per litre in combined fuel & RAF levies.\n\n"
        f"Calculate the **total indirect taxes** **{person}** pays to the state across these purchases."
    )
    expected = (
        f"Zero-rated food VAT = R0; 15% VAT on standard goods = {_fmt_r(vat_paid)}; "
        f"Fuel levies = {_fmt_r(fuel_tax_paid)}; Total indirect tax = {_fmt_r(total_indirect)}"
    )
    sol = (
        f"**Monthly Indirect Tax Burden ({person}) [4 marks]:**\n\n"
        f"1. **Zero-Rated Food ({_fmt_r(zero_food)}):** $0\\% \\text{{ VAT}} = R0$ **[1]**\n"
        f"2. **Standard 15% VAT Goods:** ${_fmt_r(vatable_goods)} \\times 15\\% = {_fmt_r(vat_paid)}$ **[1]**\n"
        f"3. **Fuel & RAF Levies ({fuel_litres} L):** ${fuel_litres} \\times R{fuel_tax_per_l} = {_fmt_r(fuel_tax_paid)}$ **[1]**\n"
        f"4. **Total Indirect Taxes Paid:** $R0 + {_fmt_r(vat_paid)} + {_fmt_r(fuel_tax_paid)} = {_fmt_r(total_indirect)}$ **[1]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_38",
        subskill="38_indirect_tax_household_monthly_burden_calc",
        title="Household Monthly Indirect Tax Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Remember brown bread, maize meal, and milk are 0% VAT — do NOT charge 15% on them!",
            "tier_2": f"Sum: 0 + (15% of {_fmt_r(vatable_goods)}) + ({fuel_litres} x R{fuel_tax_per_l}).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Applies 0% VAT to zero-rated basic foods", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"15% VAT = {_fmt_r(vat_paid)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Fuel levies = {_fmt_r(fuel_tax_paid)}", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Total indirect tax = {_fmt_r(total_indirect)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["charging_15_percent_vat_on_zero_rated_food_staples"],
        qtype="calculation",
    )


def arch_39_conditional_grants_to_provinces_and_municipalities(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    grant_purpose = rng.choice(["building new RDP low-cost houses and bulk water pipes", "buying antiretroviral HIV/AIDS clinic medication and upgrading classrooms"])
    prompt = (
        f"When National Treasury allocates a **conditional grant** to the province or municipality serving **{area}** "
        f"specifically for **{grant_purpose}**, what rule governs that money?"
    )
    correct = "The receiving province or municipality may only spend that grant on the specified national priority and must account for its exact usage."
    distractors = [
        "Local councillors may freely spend the hospital grant on luxury VIP sedans instead.",
        "Provinces collect their own 15% VAT separately from SARS.",
        "Unspent conditional grants become personal bonuses for municipal clerks.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_39",
        subskill="39_conditional_grants_to_provinces_and_municipalities",
        title="Conditional Grants & Ring-Fenced Accountability",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Conditional grants** transfer national tax revenue to provinces or municipalities with strict rules tying every Rand to **{grant_purpose}**."
        ),
        hints={
            "tier_1": "Notice the word 'conditional': conditions are attached to how the transfer is spent.",
            "tier_2": "Funds are ring-fenced for the national goal (clinics, schools, RDP housing) and audited.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_conditional_grants_can_be_repurposed_arbitrarily"],
    )


def arch_40_tax_evasion_vs_tax_avoidance_civic_impact(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    lost_tax = rng.choice([180000, 240000, 320000])
    prompt = (
        f"Investigators uncover that a smuggling ring hides cash sales from SARS, evading **{_fmt_r(lost_tax)}** in taxes, "
        f"while **{biz}** legally claims allowable depreciation deductions under SARS rules.\n\n"
        "Distinguish between **illegal tax evasion** and **legal tax avoidance**, and explain **how tax evasion damages the National Budget**."
    )
    expected = (
        "Tax evasion is breaking the law to hide income or fake deductions; tax avoidance is using lawful allowances permitted by tax legislation. "
        f"Evasion steals {_fmt_r(lost_tax)} from SARS revenue, shrinking funds for schools/hospitals or increasing national borrowing."
    )
    sol = (
        "**Tax Evasion vs Tax Avoidance [3 marks]:**\n\n"
        "1. **Tax Evasion (Illegal):** Deliberately concealing income, falsifying invoices, or smuggling to skip taxes due **[1]**.\n"
        f"2. **Tax Avoidance (Legal):** Lawful tax planning using genuine deductions allowed in law, as **{biz}** does **[1]**.\n"
        f"3. **Budget Harm:** Evading **{_fmt_r(lost_tax)}** cuts public revenue, forcing either cuts in social spending or costlier state borrowing **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_40",
        subskill="40_tax_evasion_vs_tax_avoidance_civic_impact",
        title="Tax Evasion vs Legal Tax Avoidance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "One breaks tax law; the other stays inside legal deductions.",
            "tier_2": "Explain both terms clearly, then show the revenue harm to public services/borrowing.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Tax evasion defined as illegal non-disclosure/fraud", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Tax avoidance defined as legal use of permitted deductions", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Explains revenue loss harms public services or widens deficit", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_tax_avoidance_and_tax_evasion_are_the_same"],
    )


def arch_41_fiscal_allocation_trade_offs_opportunity_cost(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    amt = rng.choice([50, 75, 100])
    opt_a = "building a new district clinic and maternity ward"
    opt_b = "resurfacing freight roads and stormwater bridges"
    prompt = (
        f"National Treasury has **R{amt} million** left in discretionary capital funds for **{area}**, which cannot fully pay for both **{opt_a}** and **{opt_b}** at the same time.\n\n"
        "Define **opportunity cost** in a National Budget decision and explain why the Minister of Finance must prioritise competing public needs."
    )
    expected = (
        f"Opportunity cost is the value of the next best alternative given up when choosing where to allocate limited budget funds "
        f"(e.g. choosing {opt_a} means postponing {opt_b}). Because tax revenue is scarce while needs are unlimited, priorities must be weighed carefully."
    )
    sol = (
        f"**Fiscal Opportunity Cost ({area}) [3 marks]:**\n\n"
        f"1. **Definition:** **Opportunity cost** is the benefit of the next best public project sacrificed when scarce funds choose another project (e.g., funding **{opt_a}** over **{opt_b}**) **[1.5]**.\n"
        "2. **Need for Prioritisation:** Government revenue is finite while social and economic needs exceed available funds, requiring careful cost-benefit choices **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_41",
        subskill="41_fiscal_allocation_trade_offs_opportunity_cost",
        title="Scarcity & Opportunity Cost in National Budgeting",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Because money is limited, choosing option A forces sacrificing option B.",
            "tier_2": "Define opportunity cost using the two given projects, then link to scarce state revenue.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Defines opportunity cost as next best alternative forgone", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Explains scarcity of revenue vs unlimited public needs", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_government_can_fund_every_project_simultaneously"],
    )


def arch_42_emergency_drought_or_flood_reallocation_calc(rng: random.Random) -> Dict[str, Any]:
    province = rng.choice(["Eastern Cape", "KwaZulu-Natal", "Free State", "Northern Cape"])
    damage_m = rng.choice([900, 1200, 1500])
    reserve_m = rng.choice([600, 800, 1000])
    gap_m = damage_m - reserve_m

    prompt = (
        f"Severe floods in **{province}** require **R{damage_m} million** in urgent road, school, and clinic repairs. "
        f"National Treasury releases **R{reserve_m} million** from its **Emergency Fund (Contingency Reserve)** and must reprioritise the remaining gap from non-essential departmental travel.\n\n"
        "(a) Calculate the **remaining shortfall** to be reprioritised;\n"
        "(b) Why is cutting non-essential travel better than cutting primary healthcare clinics?"
    )
    expected = (
        f"(a) Remaining shortfall = R{gap_m} million. "
        "(b) Trimming discretionary travel preserves essential life-saving health services and protects vulnerable households."
    )
    sol = (
        f"**Disaster Budget Reprioritisation ({province}) [3 marks]:**\n\n"
        f"**(a) Remaining Shortfall:** $R{damage_m}\\text{{ m}} - R{reserve_m}\\text{{ m}} = R{gap_m}\\text{{ million}}$ **[1]**\n\n"
        "**(b) Protecting Core Services:** Cutting administrative/non-essential travel preserves frontline hospitals, clinics, and schools during a crisis **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_42",
        subskill="42_emergency_drought_or_flood_reallocation_calc",
        title="Emergency Reserve Release & Mid-Year Reallocation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Subtract the Contingency Reserve released from total flood repair need.",
            "tier_2": "Explain why frontline health/schools take priority over discretionary admin perks.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Remaining shortfall = R{gap_m} million", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Protects essential frontline health/education over non-essential travel", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_emergency_reserve_to_damage_instead_of_subtracting"],
        qtype="calculation",
    )


def arch_43_rural_clinic_and_school_infrastructure_equity_budget(rng: random.Random) -> Dict[str, Any]:
    rural = rng.choice(["Lusikisiki", "Nongoma", "Giyani", "QwaQwa"])
    prompt = (
        f"Historically disadvantaged districts such as **{rural}** still face overcrowded mud classrooms and distant clinics.\n\n"
        "Which National Budget strategy directly reduces this regional infrastructure inequality?"
    )
    correct = "Allocating targeted conditional grants and national capital spending to build brick schools, clinics, piped water, and tarred access roads in underserved rural districts."
    distractors = [
        "Charging 30% VAT strictly on rural residents while exempting metropolitan malls.",
        "Closing all rural post offices and schools until local residents raise private loans.",
        "Cutting social welfare grants so elderly pensioners migrate abroad.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_43",
        subskill="43_rural_clinic_and_school_infrastructure_equity_budget",
        title="Redressing Rural Infrastructure Backlogs",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Directing capital grants toward classrooms, clinics, water, and roads in underserved regions like **{rural}** narrows South Africa's geographic inequality."
        ),
        hints={
            "tier_1": "Think of how national public investment remedies historic underdevelopment.",
            "tier_2": "Targeted capital expenditure builds essential rural facilities.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_rural_regions_must_self_fund_all_capital_backlogs"],
    )


def arch_44_revenue_and_expenditure_balancing_audit_table(rng: random.Random) -> Dict[str, Any]:
    # R billion clean numbers
    paye = rng.choice([680, 720, 760])
    vat = rng.choice([460, 490, 520])
    cit_other = rng.choice([360, 390, 420])
    tot_rev = paye + vat + cit_other

    soc_edu = rng.choice([740, 780, 820])
    health_sec = rng.choice([510, 540, 570])
    debt_int = rng.choice([370, 410, 440])
    tot_exp = soc_edu + health_sec + debt_int
    deficit = tot_exp - tot_rev

    rows = [
        [_make_cell("r0c0", f"Revenue: PAYE ({paye}) + VAT ({vat}) + Corporate/Excise ({cit_other})", "given"), _make_cell("r0c1", "", "required")],
        [_make_cell("r1c0", f"Expenditure: Edu/Social ({soc_edu}) + Health/Security ({health_sec}) + Interest ({debt_int})", "given"), _make_cell("r1c1", "", "required")],
        [_make_cell("r2c0", "Budget Deficit (Total Expenditure minus Total Revenue)", "given"), _make_cell("r2c1", "", "required")],
    ]
    correct_map = {
        "r0c1": f"R{tot_rev} bn",
        "r1c1": f"R{tot_exp} bn",
        "r2c1": f"R{deficit} bn",
    }
    cell_hints = {
        "r0c1": f"Add {paye} + {vat} + {cit_other} (format: R{tot_rev} bn).",
        "r1c1": f"Add {soc_edu} + {health_sec} + {debt_int} (format: R{tot_exp} bn).",
        "r2c1": "Subtract Total Revenue from Total Expenditure (format: R... bn).",
    }
    worked = (
        "**Completed National Fiscal Audit (R billion) [6 marks]:**\n\n"
        "| Budget Summary Line | Computed Total (R bn) |\n"
        "| :--- | :--- |\n"
        f"| Total Revenue | R{tot_rev} bn |\n"
        f"| Total Expenditure | R{tot_exp} bn |\n"
        f"| Budget Deficit (Borrowing Need) | R{deficit} bn |\n\n"
        f"- **Revenue:** ${paye} + {vat} + {cit_other} = R{tot_rev}\\text{{ bn}}$ **[2]**\n"
        f"- **Expenditure:** ${soc_edu} + {health_sec} + {debt_int} = R{tot_exp}\\text{{ bn}}$ **[2]**\n"
        f"- **Deficit:** $R{tot_exp}\\text{{ bn}} - R{tot_rev}\\text{{ bn}} = R{deficit}\\text{{ bn}}$ **[2]**"
    )
    sample = f"Total Revenue = R{tot_rev} bn; Total Expenditure = R{tot_exp} bn; Deficit = R{deficit} bn"
    return _build_table(
        rng,
        qid_prefix="g8_bud_44",
        subskill="44_revenue_and_expenditure_balancing_audit_table",
        title="National Budget Revenue, Expenditure & Deficit Audit",
        prompt="Compute **Total Revenue**, **Total Expenditure**, and the **Budget Deficit** in billions of Rands (enter amounts in the format **R1 500 bn** or **R1500 bn**).",
        headers=["Budget Component Summary (R billion)", "Total Amount (R... bn)"],
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Sum the three inflows for Total Revenue and the three outflows for Total Expenditure.",
            "tier_2": "Deficit = Total Expenditure - Total Revenue.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Revenue = R{tot_rev} bn", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Total Expenditure = R{tot_exp} bn", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Budget Deficit = R{deficit} bn", "marks": 2, "editable": True},
        ],
        misconception_tags=["mixing_debt_interest_into_revenue"],
    )


def arch_45_budget_pie_share_and_percentage_comparison_diagram(rng: random.Random) -> Dict[str, Any]:
    total_spend = rng.choice([2000, 2400])
    pct_direct = rng.choice([45, 50])
    pct_indirect = 35
    pct_borrow = 100 - pct_direct - pct_indirect
    amt_borrow = total_spend * pct_borrow // 100
    amt_direct = total_spend * pct_direct // 100
    amt_indirect = total_spend * pct_indirect // 100

    w_dir = int(520 * pct_direct / 100)
    w_ind = int(520 * pct_indirect / 100)
    w_bor = 520 - w_dir - w_ind

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 175" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="175" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Funding a R{total_spend} bn Budget: Revenue vs Borrowing Mix</text>'
        f'<rect x="60" y="55" width="{w_dir}" height="52" fill="#2563eb"/>'
        f'<text x="{60 + w_dir // 2}" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Direct Tax {pct_direct}%</text>'
        f'<rect x="{60 + w_dir}" y="55" width="{w_ind}" height="52" fill="#16a34a"/>'
        f'<text x="{60 + w_dir + w_ind // 2}" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Indirect Tax {pct_indirect}%</text>'
        f'<rect x="{60 + w_dir + w_ind}" y="55" width="{w_bor}" height="52" fill="#dc2626"/>'
        f'<text x="{60 + w_dir + w_ind + w_bor // 2}" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Borrow ?%</text>'
        f'<text x="320" y="142" text-anchor="middle" font-size="12" fill="#334155">Total Planned Expenditure = R{total_spend} billion</text>'
        '</svg>'
    )
    prompt = (
        f"Study the proportional funding bar diagram for a **R{total_spend} billion** National Budget: Direct Taxes cover **{pct_direct}%** "
        f"and Indirect Taxes cover **{pct_indirect}%**, while **Borrowing (State Debt)** makes up the remaining percentage.\n\n"
        "(a) What **percentage** of the budget is financed via **Borrowing**?\n"
        f"(b) Calculate the **exact Rand amount (in R billion)** covered by Borrowing out of **R{total_spend} billion**."
    )
    expected = f"(a) Borrowing = {pct_borrow}%; (b) Borrowing amount = R{amt_borrow} billion"
    sol = (
        f"**Proportional Funding Mix (R{total_spend} bn) [3 marks]:**\n\n"
        f"**(a) Borrowing Share (%):** $100\\% - ({pct_direct}\\% + {pct_indirect}\\%) = {pct_borrow}\\%$ **[1]**\n\n"
        f"**(b) Borrowing Amount:** $R{total_spend}\\text{{ bn}} \\times {pct_borrow}\\% = R{amt_borrow}\\text{{ billion}}$ "
        f"*(Check: Direct Tax R{amt_direct} bn + Indirect Tax R{amt_indirect} bn + Borrowing R{amt_borrow} bn = R{total_spend} bn)* **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_45",
        subskill="45_budget_pie_share_and_percentage_comparison_diagram",
        title="Budget Funding Mix: Taxes vs State Borrowing",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "All shares of the 100% funding bar must add up to 100%.",
            "tier_2": f"Find 100% - {pct_direct}% - {pct_indirect}%, then multiply by R{total_spend} billion.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Borrowing percentage = {pct_borrow}%", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Borrowing Rand value = R{amt_borrow} billion", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_borrowing_fills_gap_to_100_percent"],
        qtype="calculation",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_46_inflation_erosion_of_social_grants_and_adjustment(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    old_grant = rng.choice([2000, 2100, 2200])  # Old Age Pension scale
    inc_pct = rng.choice([5, 6, 8])
    inc_amt = old_grant * inc_pct // 100
    new_grant = old_grant + inc_amt

    prompt = (
        f"Because rising food prices erode pensioners' buying power in **{area}**, the Minister of Finance raises the monthly Old Age Grant "
        f"from **{_fmt_r(old_grant)}** by **{inc_pct}%**.\n\n"
        "(a) Calculate the **new monthly grant payout**;\n"
        "(b) Why must social grants be adjusted periodically for inflation?"
    )
    expected = (
        f"(a) New monthly grant = {_fmt_r(new_grant)} (increase of {_fmt_r(inc_amt)}). "
        "(b) Without adjustments, inflation lowers real purchasing power and pushes elderly/vulnerable recipients deeper into poverty."
    )
    sol = (
        f"**Social Grant Inflation Adjustment ({area}) [3 marks]:**\n\n"
        f"**(a) New Monthly Grant:** ${_fmt_r(old_grant)} + ({_fmt_r(old_grant)} \\times {inc_pct}\\%) = {_fmt_r(old_grant)} + {_fmt_r(inc_amt)} = {_fmt_r(new_grant)}$ **[2]**\n\n"
        "**(b) Purchasing Power Protection:** Inflation increases food, transport, and energy costs; periodic grant adjustments protect basic living standards **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_46",
        subskill="46_inflation_erosion_of_social_grants_and_adjustment",
        title="Inflation Adjustments to Social Grants",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Add {inc_pct}% of {_fmt_r(old_grant)} to {_fmt_r(old_grant)}.",
            "tier_2": "Connect rising grocery prices (inflation) to protecting vulnerable pensioners' real buying power.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"New monthly grant = {_fmt_r(new_grant)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Preserves real purchasing power against rising food/living prices", "marks": 1, "editable": True},
        ],
        misconception_tags=["computing_increase_without_adding_back_to_old_grant"],
        qtype="calculation",
    )


def arch_47_smme_tax_compliance_and_formalisation_incentive(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    area = rng.choice(AREAS)
    prompt = (
        f"**{owner}** runs **{biz}** informally in **{area}** and hesitates to register formally with CIPC and SARS.\n\n"
        "Give **one advantage to {0}** of becoming tax-compliant and **one benefit to the National Budget**.".format(biz)
    )
    expected = (
        f"For {biz}: Becomes eligible for government tenders, commercial bank loans, and formal corporate contracts. "
        "For National Budget: Adds sustainable tax receipts and formal employment data into SARS."
    )
    sol = (
        f"**SMME Formalisation & Tax Compliance ({biz}) [3 marks]:**\n\n"
        f"1. **Advantage to {biz}:** Tax clearance and formal registration allow bidding for government tenders, accessing bank credit, and supplying big retailers **[1.5]**.\n"
        "2. **Benefit to National Budget:** Formal businesses widen the tax base and create protected jobs contributing to SARS **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_47",
        subskill="47_smme_tax_compliance_and_formalisation_incentive",
        title="Why SMME Formalisation Helps Firms & the Budget",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Think about what {biz} gains (tenders, loans) AND what SARS gains.",
            "tier_2": "Pair tender/credit access for the SMME with wider revenue for the National Budget.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Firm gains access to government tenders, bank credit, or corporate buyers", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "National Budget gains broader, more reliable tax base", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["seeing_registration_only_as_a_cost_with_no_business_upside"],
    )


def arch_48_sin_tax_behavioural_shift_and_health_savings(rng: random.Random) -> Dict[str, Any]:
    tax_hike = rng.choice([7, 9, 12])
    prompt = (
        f"Suppose the Minister of Finance announces an above-inflation **{tax_hike}% sin tax increase** on cigarettes and high-alcohol products.\n\n"
        "How can higher sin taxes eventually help **reduce pressure on the public Health budget**?"
    )
    correct = "By raising retail prices to discourage heavy smoking and alcohol consumption, reducing preventable diseases treated in public hospitals."
    distractors = [
        "By making cigarettes zero-rated at supermarkets.",
        "By transferring hospital doctors into parliament to sell tobacco.",
        "Because higher cigarette taxes automatically repair municipal potholes.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_bud_48",
        subskill="48_sin_tax_behavioural_shift_and_health_savings",
        title="Sin Taxes & Long-Term Public Health Savings",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Raising sin taxes by **{tax_hike}%** acts as a price deterrent against harmful consumption while helping fund public health pressure."
        ),
        hints={
            "tier_1": "What happens to consumption and long-term clinic admissions when harmful products cost more?",
            "tier_2": "Discourages harmful habits -> fewer preventable illnesses in public hospitals.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_sin_taxes_never_affect_consumer_choices"],
    )


def arch_49_budget_misconception_error_correction_table(rng: random.Random) -> Dict[str, Any]:
    myths = [
        ("15% VAT is a direct tax because shoppers hand cash directly to till cashiers.", "Indirect Tax (collected via retailer intermediary and shifted to buyer)"),
        ("Government should abolish the Emergency Fund because disasters cannot happen in SA.", "Emergency Fund is vital for unexpected floods, epidemics, or economic shocks"),
        ("Brown bread and maize meal carry 15% VAT in South Africa.", "0% Zero-rated basic foods to protect low-income households"),
        ("The South African national financial year runs 1 January to 31 December.", "Runs 1 April to 31 March of the following year"),
    ]
    chosen = rng.sample(myths, 3)
    headers = ["Incorrect Budget Myth", "Factual National Budget Correction"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Incorrect Budget Myth | Factual National Budget Correction |", "| :--- | :--- |"]
    for idx, (myth, fix) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", myth, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = fix
        cell_hints[c1] = "Write the accurate National Budget fact correcting this misconception."
        memo_lines.append(f"| {myth} | {fix} |")

    worked = "**Completed National Budget Misconception Audit [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{m} -> {f}" for m, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_bud_49",
        subskill="49_budget_misconception_error_correction_table",
        title="National Budget Misconception Error Audit",
        prompt="Each statement in the table reflects a common misconception about South Africa's National Budget. State the **accurate factual correction** in column 2.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Identify why each statement is wrong: direct vs indirect, fiscal dates, zero-rated staples, or emergency reserves.",
            "tier_2": "Give a concise, factual correction for each statement.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Accurate correction row {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["accepting_budget_myths_about_vat_and_reserves"],
    )


def arch_50_comprehensive_national_budget_policy_synthesis(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    rev_bn = rng.choice([1750, 1850, 1950])
    exp_bn = rev_bn + rng.choice([250, 300])
    deficit_bn = exp_bn - rev_bn
    prompt = (
        f"**Budget Policy Case Study ({area} & National Treasury):**\n"
        f"In the current fiscal year, total expected revenue is **R{rev_bn} billion** while planned expenditure is **R{exp_bn} billion**, leaving a **R{deficit_bn} billion deficit**. "
        "At the same time, low-income families face rising food prices, youth unemployment remains high, and climate floods threaten provincial bridges.\n\n"
        "Advise the **Minister of Finance** by answering all three parts:\n"
        "1. Distinguish between **one Direct Tax** and **one Indirect Tax** used to collect revenue, and note **how the R{0} billion deficit is funded**.\n".format(deficit_bn)
        + "2. Recommend **two budget tools** that directly **reduce economic inequality** for vulnerable households.\n"
        "3. Explain **two budget strategies** (other than tax-rate hikes) to **grow the economy** and widen the tax base over time."
    )
    expected = (
        f"1) Direct: Personal Income Tax (PAYE) or Corporate Tax; Indirect: 15% VAT, sin tax, or fuel levy; Deficit (R{deficit_bn} bn) funded via government borrowing/bonds. "
        "2) Inequality tools: Social grants, RDP housing, school nutrition, free basic water/electricity, zero-rated basic food, free child healthcare. "
        "3) Growth strategies: Infrastructure construction, EPWP community jobs, SMME start-up finance & skills advice, plus maintaining an Emergency Fund against disasters."
    )
    sol = (
        f"**Ministerial National Budget Synthesis (Deficit R{deficit_bn} bn) [6 marks]:**\n\n"
        "1. **Revenue & Deficit Funding [2 marks]:**\n"
        "   - **Direct Tax:** Personal Income Tax (PAYE) or Company Tax (cannot be shifted) + **Indirect Tax:** 15% VAT, excise/sin tax, or fuel levy **[1]**.\n"
        f"   - **Deficit Funding:** Government bridges the **R{deficit_bn} billion** shortfall through **borrowing (state loans/bonds)**, incurring future interest costs **[1]**.\n"
        "2. **Reducing Economic Inequality [2 marks]:**\n"
        "   - **Two Redress Tools:** E.g. **Social security grants** & **zero-rated basic foods / RDP housing / school nutrition / free basic utilities / free child healthcare** **[2]**.\n"
        "3. **Driving Growth & Widening Tax Base [2 marks]:**\n"
        "   - **Two Growth Strategies:** Investing in **transport/utility infrastructure & EPWP job creation** **[1]** plus **SMME finance, training, and advice** so more firms and workers pay future taxes **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_bud_50",
        subskill="50_comprehensive_national_budget_policy_synthesis",
        title="Comprehensive National Budget Policy Advice Synthesis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Structure into 3 parts: Revenue/Borrowing, Inequality Redress, Growth & Tax-Base Expansion.",
            "tier_2": "Give exact tax examples + borrowing for deficit; 2 poverty tools; 2 growth/job strategies.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Direct tax, indirect tax, and deficit borrowing", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Two valid inequality-reduction programmes", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Two valid growth & tax-base expansion strategies", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_tradeoff_between_borrowing_and_growth"],
        qtype="extended_response",
    )


BUILDERS_26_50 = {
    "26_emergency_fund_contingency_reserve_purpose": arch_26_emergency_fund_contingency_reserve_purpose,
    "27_japanese_2011_tsunami_supply_chain_and_reserve_lesson": arch_27_japanese_2011_tsunami_supply_chain_and_reserve_lesson,
    "28_fiscal_policy_growth_tax_base_virtuous_cycle_diagram": arch_28_fiscal_policy_growth_tax_base_virtuous_cycle_diagram,
    "29_subsidies_on_basic_goods_brown_bread_milk": arch_29_subsidies_on_basic_goods_brown_bread_milk,
    "30_public_works_epwp_job_creation_calculation": arch_30_public_works_epwp_job_creation_calculation,
    "31_reducing_economic_inequality_five_mechanisms_table": arch_31_reducing_economic_inequality_five_mechanisms_table,
    "32_school_nutrition_programme_human_capital_benefit": arch_32_school_nutrition_programme_human_capital_benefit,
    "33_free_basic_water_and_electricity_poverty_alleviation": arch_33_free_basic_water_and_electricity_poverty_alleviation,
    "34_progressive_vs_regressive_tax_fairness": arch_34_progressive_vs_regressive_tax_fairness,
    "35_tax_base_expansion_vs_increasing_tax_rates": arch_35_tax_base_expansion_vs_increasing_tax_rates,
    "36_debt_servicing_crowding_out_social_spending": arch_36_debt_servicing_crowding_out_social_spending,
    "37_multi_year_budget_comparison_growth_calc": arch_37_multi_year_budget_comparison_growth_calc,
    "38_indirect_tax_household_monthly_burden_calc": arch_38_indirect_tax_household_monthly_burden_calc,
    "39_conditional_grants_to_provinces_and_municipalities": arch_39_conditional_grants_to_provinces_and_municipalities,
    "40_tax_evasion_vs_tax_avoidance_civic_impact": arch_40_tax_evasion_vs_tax_avoidance_civic_impact,
    "41_fiscal_allocation_trade_offs_opportunity_cost": arch_41_fiscal_allocation_trade_offs_opportunity_cost,
    "42_emergency_drought_or_flood_reallocation_calc": arch_42_emergency_drought_or_flood_reallocation_calc,
    "43_rural_clinic_and_school_infrastructure_equity_budget": arch_43_rural_clinic_and_school_infrastructure_equity_budget,
    "44_revenue_and_expenditure_balancing_audit_table": arch_44_revenue_and_expenditure_balancing_audit_table,
    "45_budget_pie_share_and_percentage_comparison_diagram": arch_45_budget_pie_share_and_percentage_comparison_diagram,
    "46_inflation_erosion_of_social_grants_and_adjustment": arch_46_inflation_erosion_of_social_grants_and_adjustment,
    "47_smme_tax_compliance_and_formalisation_incentive": arch_47_smme_tax_compliance_and_formalisation_incentive,
    "48_sin_tax_behavioural_shift_and_health_savings": arch_48_sin_tax_behavioural_shift_and_health_savings,
    "49_budget_misconception_error_correction_table": arch_49_budget_misconception_error_correction_table,
    "50_comprehensive_national_budget_policy_synthesis": arch_50_comprehensive_national_budget_policy_synthesis,
}
