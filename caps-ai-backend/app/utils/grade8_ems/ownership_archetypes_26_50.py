"""Grade 8 EMS - Forms of ownership: Archetypes 26 to 50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 3/01. Forms of ownership.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES as PERSON_NAMES
from .ownership_archetypes_01_25 import (
    _build_mcq,
    _build_short,
    _build_table,
    _fmt_r,
    _make_cell,
)


def arch_26_smme_definition_and_ownership_types(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(["a 4-person solar repair workshop", "a small urban bakery with 8 staff", "a local upholstery and curtain studio"])
    prompt = (
        f"In **{area}**, an entrepreneur runs **{biz}**.\n\n"
        "What does the abbreviation **SMME** stand for in South African economics, and which forms of ownership do most SMMEs start as?"
    )
    correct = "Small, Medium and Micro Enterprises; they commonly start as sole traders or partnerships before potentially growing into CCs or Private Companies."
    distractors = [
        "State Monopoly Municipal Enterprises; owned strictly by national Cabinet Ministers.",
        "Stock Market Mining Exchanges; restricted exclusively to Public Companies (Ltd) on the JSE.",
        "South African Tax Ministries; responsible only for collecting 15% VAT.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_26",
        subskill="26_smme_definition_and_ownership_types",
        title="SMME Meaning & Common Ownership Forms",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**SMME** stands for **Small, Medium and Micro Enterprises** ({biz} in **{area}**). Most begin simply as **sole traders** or **partnerships**."
        ),
        hints={
            "tier_1": "Expand S - M - M - E carefully and identify small starter ownership structures.",
            "tier_2": "Small, Medium and Micro Enterprises -> mainly sole traders and partnerships initially.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_smme_with_state_owned_enterprise"],
    )


def arch_27_smme_role_in_sustainable_job_creation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    smme_count = rng.choice([15, 25, 40])
    workers_each = rng.choice([4, 5, 6])
    tot_jobs = smme_count * workers_each
    prompt = (
        f"In a growing business hub in **{area}**, **{smme_count} local SMMEs** each employ an average of **{workers_each} staff**.\n\n"
        f"(a) Calculate the **total jobs created** in this hub;\n"
        "(b) Give **two reasons** why SMMEs play a vital role in **sustainable job creation** across South Africa."
    )
    expected = (
        f"(a) Total jobs = {tot_jobs}. "
        "(b) 1) SMMEs absorb entry-level and lower-skilled jobseekers while teaching practical skills on the job; "
        "2) As SMMEs grow into CCs/companies, higher turnover and competitiveness support long-term employment."
    )
    sol = (
        f"**SMME Sustainable Job Creation ({area}) [4 marks]:**\n\n"
        f"**(a) Direct Local Jobs:** ${smme_count} \\times {workers_each} = {tot_jobs}\\text{{ jobs}}$ **[1]**\n\n"
        "**(b) Why SMMEs Drive Sustainable Employment [3 marks]:**\n"
        "1. They create accessible local jobs that alleviate unemployment and transfer practical **on-the-job skills** to youth **[1.5]**.\n"
        "2. Thriving SMMEs reinvest locally, improve competitiveness, and evolve into CCs or Private Companies employing more permanent staff **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_27",
        subskill="27_smme_role_in_sustainable_job_creation",
        title="SMMEs & Sustainable Job Creation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Multiply SMMEs by workers per firm first.",
            "tier_2": "Connect SMMEs to entry-level employment, hands-on training, and long-term business scaling.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total jobs = {tot_jobs}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Entry-level jobs and practical workplace skill development", "marks": 1.5, "editable": True},
            {"id": "mp_3", "desc": "Growth into larger CCs/companies builds lasting competitiveness", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_only_jse_giants_create_jobs"],
    )


def arch_28_smme_skills_transfer_and_youth_employment(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    area = rng.choice(AREAS)
    craft = rng.choice(["welding and gate fabrication", "solar panel installation", "commercial baking and food safety"])
    prompt = (
        f"**{owner}** runs a medium-sized workshop in **{area}** specialising in **{craft}** and trains apprentices lacking formal university degrees.\n\n"
        "How does this SMME directly help reduce South Africa's **skills shortage**?"
    )
    correct = "Small and medium firms train workers in practical, hands-on industry skills, building confidence and readiness for permanent employment or launching new enterprises."
    distractors = [
        "SMMEs forbid inexperienced youth from entering the workplace until age 45.",
        "Only public companies listed on international exchanges may train apprentices.",
        "Practical skills training increases unemployment by forcing workers out of cities.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_28",
        subskill="28_smme_skills_transfer_and_youth_employment",
        title="How SMMEs Address South Africa's Skills Shortage",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"SMMEs like **{owner}'s** workshop in **{area}** provide hands-on mentoring in **{craft}**, directly equipping young workers with marketable skills."
        ),
        hints={
            "tier_1": "Notice the apprentices gain real practical experience on the job.",
            "tier_2": "SMMEs train semi-skilled workers and build future entrepreneurs.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_informal_and_smme_training_value"],
    )


def arch_29_business_growth_progression_sole_to_company(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    area = rng.choice(AREAS)
    prompt = (
        f"**{founder}** started in **{area}** selling homemade jams from one kitchen table (Sole trader), "
        f"later opened a regional factory with 4 investors (**`(Pty) Ltd`**), and 15 years later lists nationally on the JSE (**`Ltd`**).\n\n"
        "Explain **two business reasons** why expanding enterprises upgrade their ownership form along this path."
    )
    expected = (
        "1) To attract far larger expansion capital from additional shareholders/public investors; "
        "2) To gain limited liability and separate legal entity protection plus continuity of existence as financial risk grows."
    )
    sol = (
        f"**Ownership Growth Trajectory ({founder}) [3 marks]:**\n\n"
        "1. **Expanding Capital Access:** Transitioning from personal savings (Sole trader) to private equity (`(Pty) Ltd`) and public JSE capital (`Ltd`) funds major factory expansion **[1.5]**.\n"
        "2. **Risk Shield & Continuity:** Gaining **limited liability**, **separate legal personality**, and **continuity** protects founders as debts and staff headcounts scale up **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_29",
        subskill="29_business_growth_progression_sole_to_company",
        title="Why Growing Businesses Upgrade Their Ownership Form",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Compare money available and personal risk as a firm expands from kitchen to national factory.",
            "tier_2": "Mention raising larger capital AND gaining limited liability / continuity.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Ability to raise larger capital from private or public shareholders", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Secures limited liability, separate legal entity, and continuity", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["thinking_legal_form_never_changes_once_started"],
    )


def arch_30_tax_implications_sole_trader_vs_company(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    biz = rng.choice(["Vula Packaging (Pty) Ltd", "Kasi Engineering Ltd"])
    prompt = (
        f"Compare how income tax applies to **{owner}** (a sole trader) versus **{biz}** (a registered company).\n\n"
        "Which statement correctly explains the **tax implication** difference?"
    )
    correct = f"A sole trader's profit is taxed directly as {owner}'s personal income, whereas {biz} is a separate legal taxpayer taxed at corporate income tax rates."
    distractors = [
        f"Both {owner} and {biz} pay zero income tax in South Africa.",
        f"Sole traders pay 27% corporate tax while companies pay personal PAYE tax only.",
        "Only partnerships must register for tax while Public Companies are tax-free.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_30",
        subskill="30_tax_implications_sole_trader_vs_company",
        title="Tax Treatment: Sole Trader vs Registered Company",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Because a sole trader is NOT a separate legal entity, profit is taxed in **{owner}**'s personal hands. "
            f"Because **{biz}** IS a separate juristic person, it pays corporate tax as its own entity."
        ),
        hints={
            "tier_1": "Link separate legal entity status directly to who SARS taxes.",
            "tier_2": "Sole trader -> personal income tax; Company -> separate corporate tax entity.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_companies_pay_tax_under_personal_id_numbers"],
    )


def arch_31_profit_distribution_across_ownership_forms_table(rng: random.Random) -> Dict[str, Any]:
    rows_pool = [
        ("Sole trader", "100% retained by the single owner"),
        ("Partnership", "Shared among partners per the Partnership Agreement"),
        ("Close Corporation (CC)", "Distributed to members based on member's interest percentage"),
        ("Private / Public Company", "Declared as dividends per share to shareholders (after retaining reserves)"),
    ]
    chosen = rng.sample(rows_pool, 3)
    headers = ["Form of Ownership", "How Net Profit Is Distributed to Owners"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Form of Ownership | Profit Distribution Method |", "| :--- | :--- |"]
    for idx, (form, dist) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", form, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = dist
        cell_hints[c1] = "Explain who receives profit and according to what rule (owner, agreement, member interest, or dividends)."
        memo_lines.append(f"| {form} | {dist} |")

    worked = "**Completed Profit Distribution Schedule [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{f} -> {d}" for f, d in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_31",
        subskill="31_profit_distribution_across_ownership_forms_table",
        title="Comparing Profit Distribution Across Ownership Forms",
        prompt="Complete the schedule explaining how after-tax profit is distributed across each form of ownership listed.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Sole trader takes all; partners follow an agreement; company shareholders receive dividends.",
            "tier_2": "Mention partnership agreement, member interest, or dividends per share.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["thinking_shareholders_withdraw_company_cash_arbitrarily"],
    )


def arch_32_raising_capital_ability_ranking_table(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Sole trader", "Owner's personal savings and modest personal bank loans (Smallest capital pool)"),
        ("Partnership", "Pooled capital and loans of 2 to 20 partners"),
        ("Private Company (Pty) Ltd", "Private equity from invited shareholders (no JSE public sales)"),
        ("Public Company (Ltd)", "Massive equity raised publicly via Prospectus and JSE share issues (Largest capital pool)"),
    ]
    chosen = rng.sample(pool, 3)
    headers = ["Primary Capital-Raising Source", "Matching Ownership Form"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Primary Capital-Raising Source | Matching Ownership Form |", "| :--- | :--- |"]
    for idx, (form, src) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", src, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = form
        cell_hints[c1] = "Enter exact form: Sole trader, Partnership, Private Company (Pty) Ltd, or Public Company (Ltd)."
        memo_lines.append(f"| {src} | {form} |")

    worked = "**Completed Capital Access Matching [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{s} -> {f}" for f, s in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_32",
        subskill="32_raising_capital_ability_ranking_table",
        title="Capital-Raising Capacity Across Ownership Forms",
        prompt=(
            "Match each capital-raising mechanism to the correct form of ownership: "
            "**Sole trader**, **Partnership**, **Private Company (Pty) Ltd**, or **Public Company (Ltd)**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Personal savings = smallest; JSE public issue = largest.",
            "tier_2": "Use exact names provided in the prompt.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][1]} -> {chosen[i][0]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["thinking_sole_traders_issue_jse_shares"],
    )


def arch_33_decision_making_speed_vs_corporate_governance(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(["flour and yeast", "solar inverters", "timber planks"])
    discount_pct = rng.choice([18, 22, 25])
    prompt = (
        f"A supplier offers a sudden 24-hour **{discount_pct}% clearance discount** on **{supplier}**.\n\n"
        "Compare how quickly a **sole trader** can approve this purchase compared to a **Public Company (`Ltd`)**, explaining **why**."
    )
    expected = (
        f"A sole trader can decide immediately alone and grab the {discount_pct}% discount, "
        "whereas a Public Company follows slower formal governance/procurement approvals by managers, directors, or board committees."
    )
    sol = (
        f"**Decision Speed Comparison ({discount_pct}% Offer) [3 marks]:**\n\n"
        f"1. **Sole Trader:** Can approve the **{supplier}** purchase on the spot because one single owner holds full authority **[1.5]**.\n"
        "2. **Public Company (Ltd):** Much slower due to strict corporate governance, multi-level procurement rules, and board/management accountability **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_33",
        subskill="33_decision_making_speed_vs_corporate_governance",
        title="Decision Speed: Sole Trader vs Public Company",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Compare consulting 1 person against multi-tier corporate governance.",
            "tier_2": "Explain instant solo authority vs slower board/committee governance.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Sole trader decides fast without consulting partners/boards", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Public company slower due to formal corporate governance & procedures", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_large_companies_make_decisions_faster_than_solo_owners"],
    )


def arch_34_sustainable_use_of_renewable_resources(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    resource = rng.choice(["coastal fishing stocks", "commercial timber forests", "freshwater river irrigation"])
    prompt = (
        f"A partnership and a large `(Pty) Ltd` company near **{area}** both depend on **{resource}**.\n\n"
        "What does **sustainable use of renewable natural resources** require from **all forms of business ownership**?"
    )
    correct = "Harvesting or consuming renewable resources responsibly at rates that allow nature to regenerate so future generations can still use them."
    distractors = [
        "Depleting forests and rivers as quickly as possible before rival firms arrive.",
        "Only allowing Public Companies (Ltd) to use solar energy while banning SMMEs from recycling water.",
        "Replacing all renewable water and timber permanently with coal and diesel.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_34",
        subskill="34_sustainable_use_of_renewable_resources",
        title="Sustainable Use of Renewable Resources Across Firms",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Sustainable stewardship of **{resource}** requires every firm — sole trader to public corporation — to harvest no faster than natural regeneration."
        ),
        hints={
            "tier_1": "Renewable resources can run out if overused or polluted faster than they replenish.",
            "tier_2": "Use at a rate allowing natural regeneration for future business and households.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_renewable_resources_never_need_conservation"],
    )


def arch_35_non_renewable_resources_and_alternative_innovation(rng: random.Random) -> Dict[str, Any]:
    firm = rng.choice(["Horizon Metals (Pty) Ltd", "Vula Transport Ltd", "Cape Ceramics CC"])
    non_ren = rng.choice(["coal-fired grid electricity", "crude diesel fuel", "finite mineral deposits"])
    prompt = (
        f"**{firm}** relies heavily on **{non_ren}** — a **non-renewable resource** that cannot be replenished once exhausted.\n\n"
        "Give **two proactive steps** businesses of any ownership form must take regarding **non-renewable resources** to secure future economic activity."
    )
    expected = (
        f"1) Reduce waste and improve energy/material efficiency when using {non_ren}; "
        "2) Invest in and adopt renewable alternatives (such as solar energy, electric fleets, or recycled inputs)."
    )
    sol = (
        f"**Managing Non-Renewable Resources ({firm}) [3 marks]:**\n\n"
        f"1. **Conservation & Efficiency:** Minimise unnecessary waste of **{non_ren}** and recycle usable materials wherever possible **[1.5]**.\n"
        "2. **Developing Renewable Alternatives:** Transition processes toward clean, sustainable substitutes such as **solar power, biogas, or recycled materials** to protect future operations **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_35",
        subskill="35_non_renewable_resources_and_alternative_innovation",
        title="Conserving Non-Renewable Resources & Alternatives",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Once coal, oil, or finite minerals run out, what two things keep a firm operating sustainably?",
            "tier_2": "Combine efficiency/waste reduction with developing renewable alternatives.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Conserves scarce non-renewable inputs / reduces waste", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Develops or switches to renewable alternatives (e.g. solar)", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["ignoring_need_to_replace_non_renewable_inputs"],
    )


def arch_36_large_company_ecological_footprint_vs_smme(rng: random.Random) -> Dict[str, Any]:
    pub = rng.choice(["Mzansi Manufacturing Ltd", "Karoo Beverages Ltd"])
    area = rng.choice(AREAS)
    prompt = (
        f"Compare the resource consumption of **{pub}** (a large national Public Company) against a single neighbourhood sole trader tailor in **{area}**.\n\n"
        f"Why does **{pub}** carry an especially major responsibility for sustainable resource use, and name **one advantage** large companies have when adopting green technology?"
    )
    expected = (
        f"{pub} operates large factories and fleets consuming massive volumes of water, electricity, and raw materials, so its environmental harm would be vast if unchecked. "
        f"Advantage: Large companies can raise significant capital (e.g. from shareholders/retained profits) to fund solar plants, water-recycling systems, and cleaner machinery."
    )
    sol = (
        f"**Resource Footprint: Large Corporations vs SMMEs ({pub}) [3 marks]:**\n\n"
        f"1. **Scale of Consumption:** **{pub}** uses vastly more electricity, water, fuel, and packaging than a tiny local tailor, magnifying ecological impact **[1.5]**.\n"
        "2. **Capital Advantage:** Large companies can access greater **shareholder capital** to install solar arrays, water-treatment plants, and low-waste production lines **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_36",
        subskill="36_large_company_ecological_footprint_vs_smme",
        title="Resource Responsibility: Large Companies vs SMMEs",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of BOTH factory consumption volume AND access to green-investment capital.",
            "tier_2": "Large firms consume far more resources but have greater capital to adopt cleaner alternatives.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Large companies consume far greater resource quantities", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Stronger capital access lets large companies fund green technology/alternatives", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["thinking_only_small_firms_need_environmental_care"],
    )


def arch_37_public_sector_soe_vs_public_company_distinction(rng: random.Random) -> Dict[str, Any]:
    pub_co = rng.choice(["Shoprite Holdings Ltd", "Pick n Pay Stores Ltd", "MTN Group Ltd"])
    soe = rng.choice(["Eskom SOC Ltd", "Transnet SOC Ltd"])
    prompt = (
        f"Learners often confuse **{pub_co}** (a JSE-listed **Public Company**) with **{soe}** (a **State-Owned Enterprise**).\n\n"
        f"Which distinction between **{pub_co}** and **{soe}** is **accurate**?"
    )
    correct = f"{pub_co} is owned by private/public JSE shareholders aiming to earn dividends, whereas {soe} is controlled by the South African government to deliver strategic state services."
    distractors = [
        f"{pub_co} is owned by Parliament and distributes free groceries paid from national taxes.",
        f"{soe} trades shares freely to private shoppers who become Minister of Finance.",
        "Both entities are informal sole traders without separate legal personality.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_37",
        subskill="37_public_sector_soe_vs_public_company_distinction",
        title="Distinguishing Public Company (Ltd) from SOEs",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"'Public' in **Public Company** (**{pub_co}**) means the general public may buy its shares on the **JSE** — it is still a private-sector profit business, NOT owned by the state like **{soe}**."
        ),
        hints={
            "tier_1": "Careful: 'Public Company' does NOT mean 'owned by Government'!",
            "tier_2": "Public Company = shares open to public investors on JSE; SOE = owned by Government.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_public_company_means_government_owned"],
    )


def arch_38_sole_trader_income_statement_to_owner_drawings_calc(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    open_cap = rng.choice([80000, 100000, 120000])
    net_profit = rng.choice([75000, 95000, 110000])
    drawings = rng.choice([45000, 55000, 60000])
    closing_cap = open_cap + net_profit - drawings

    prompt = (
        f"**{owner}** starts the year as a sole trader with **{_fmt_r(open_cap)}** Owner's Equity (Capital). "
        f"During the year, the business earns a **net profit of {_fmt_r(net_profit)}**, and **{owner}** withdraws **{_fmt_r(drawings)}** in **Drawings** for family expenses.\n\n"
        f"Calculate **{owner}**'s **closing Owner's Equity (Capital)** at year-end."
    )
    expected = f"Closing Owner's Equity = {_fmt_r(closing_cap)}"
    sol = (
        f"**Sole Trader Closing Capital ({owner}) [3 marks]:**\n\n"
        f"$$\\text{{Closing Capital}} = \\text{{Opening Capital}} + \\text{{Net Profit}} - \\text{{Drawings}}$$\n"
        f"$$= {_fmt_r(open_cap)} + {_fmt_r(net_profit)} - {_fmt_r(drawings)} = {_fmt_r(closing_cap)}$$ **[3]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_38",
        subskill="38_sole_trader_income_statement_to_owner_drawings_calc",
        title="Sole Trader Profit, Drawings & Closing Equity",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Net profit INCREASES owner's capital; personal drawings DECREASE owner's capital.",
            "tier_2": f"Compute {_fmt_r(open_cap)} + {_fmt_r(net_profit)} - {_fmt_r(drawings)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Adds Net Profit to Opening Capital", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Subtracts Drawings correctly", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Final Closing Equity = {_fmt_r(closing_cap)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["adding_drawings_instead_of_subtracting_from_capital"],
        qtype="calculation",
    )


def arch_39_private_company_shareholder_voting_percentage_calc(rng: random.Random) -> Dict[str, Any]:
    holder = rng.choice(PERSON_NAMES)
    co = rng.choice(["Vula Solar (Pty) Ltd", "Imbali Foods (Pty) Ltd", "Naledi Print (Pty) Ltd"])
    tot_shares = rng.choice([10000, 20000, 50000])
    pct = rng.choice([25, 30, 40])
    held_shares = tot_shares * pct // 100
    div_pool = rng.choice([100000, 200000])
    holder_div = div_pool * pct // 100

    prompt = (
        f"**{co}** has **{tot_shares:,} issued shares** in total, and **{holder}** owns **{held_shares:,} shares**.\n\n"
        f"(a) Calculate **{holder}**'s **percentage ownership / voting stake** in **{co}**;\n"
        f"(b) If **{co}** declares **{_fmt_r(div_pool)}** in total dividends, how much does **{holder}** receive?"
    )
    expected = f"(a) Voting stake = {pct}%; (b) Dividend payout = {_fmt_r(holder_div)}"
    sol = (
        f"**Shareholder Ownership & Dividend Stake ({co}) [4 marks]:**\n\n"
        f"**(a) Ownership / Voting Percentage:**\n"
        f"$$\\frac{{{held_shares:,}}}{{{tot_shares:,}}} \\times 100\\% = {pct}\\%$$ **[2]**\n\n"
        f"**(b) {holder}'s Dividend Payout ({pct}%):**\n"
        f"$${_fmt_r(div_pool)} \\times {pct}\\% = {_fmt_r(holder_div)}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_39",
        subskill="39_private_company_shareholder_voting_percentage_calc",
        title="Shareholder Voting Percentage & Dividend Share",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Divide {held_shares:,} by {tot_shares:,} and multiply by 100 for the percentage.",
            "tier_2": f"Apply that exact percentage to {_fmt_r(div_pool)} total dividends.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Percentage stake = {pct}%", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Dividend payout = {_fmt_r(holder_div)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["inverting_fraction_total_over_held_shares"],
        qtype="calculation",
    )


def arch_40_converting_partnership_to_pty_ltd_scenario(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(PERSON_NAMES)
    p2 = rng.choice([n for n in PERSON_NAMES if n != p1])
    contract_val = rng.choice([2500000, 3500000, 4800000])
    prompt = (
        f"**{p1}** and **{p2}** currently run a civil contracting **partnership**, and they have been invited to tender for a risky **{_fmt_r(contract_val)}** bridge contract requiring heavy machinery loans.\n\n"
        f"Advise why converting their partnership into a **Private Company `(Pty) Ltd`** protects their family homes AND ensures **continuity**."
    )
    expected = (
        "1) Limited liability & separate legal entity: If the contract fails, creditors claim only company assets, protecting both founders' family homes/personal wealth. "
        "2) Continuity of existence: Unlike a partnership, the (Pty) Ltd will not dissolve if a partner retires or dies mid-contract."
    )
    sol = (
        f"**Why Convert from Partnership to (Pty) Ltd ({_fmt_r(contract_val)} Contract) [4 marks]:**\n\n"
        "1. **Limited Liability Shield:** In a partnership, personal homes can be seized if the contract fails; registering a **`(Pty) Ltd`** creates a **separate legal entity** capping liability to company capital **[2]**.\n"
        "2. **Continuity of Contracts:** A **`(Pty) Ltd`** keeps executing multi-year contracts seamlessly even if one shareholder exits or passes away, whereas a partnership would dissolve **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_40",
        subskill="40_converting_partnership_to_pty_ltd_scenario",
        title="Advisory Case: Converting a Partnership to (Pty) Ltd",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Think of TWO critical risks of partnerships when signing huge multi-million Rand loans: liability and continuity.",
            "tier_2": "Explain separate legal entity / limited liability protecting homes + continuity of existence.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Limited liability & separate legal entity protect personal homes", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Continuity prevents forced dissolution mid-contract", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_partnerships_carry_corporate_liability_protection"],
    )


def arch_41_cipc_compliance_and_annual_audit_requirement(rng: random.Random) -> Dict[str, Any]:
    co = rng.choice(["Vula Power Ltd", "Naledi Foods (Pty) Ltd"])
    prompt = (
        f"**{co}** is required by the Companies Act to keep formal accounting records, compile financial statements, and undergo review/audit processes.\n\n"
        "Why does law enforce stricter financial reporting and audit accountability on companies than on an informal sole trader?"
    )
    correct = "To protect shareholders, creditors, and the public by ensuring transparent financial health because limited liability prevents creditors from claiming owners' personal wealth."
    distractors = [
        "So that company managers can hide business profits from SARS completely.",
        "Because sole traders are forbidden from owning a calculator or cash register.",
        "To prevent shareholders from ever receiving any annual dividends.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_41",
        subskill="41_cipc_compliance_and_annual_audit_requirement",
        title="Why Companies Need Financial Accountability & Audits",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Because **{co}** enjoys **limited liability** (and public companies accept public savings), transparent **financial/audited statements** protect investors, suppliers, and lenders."
        ),
        hints={
            "tier_1": "If creditors cannot touch owners' personal houses, what assurance do lenders and outside shareholders need?",
            "tier_2": "Audited statements verify transparent financial truth and deter fraud.",
            "tier_3": correct,
        },
        misconception_tags=["viewing_audits_as_unnecessary_red_tape_with_no_creditor_protection"],
    )


def arch_42_economic_growth_exports_and_smme_competitiveness(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    product = rng.choice(["bottled marula skincare oils", "hand-crafted leather boots", "solar water pumps"])
    prompt = (
        f"A small enterprise in **{area}** producing **{product}** starts as a sole trader, hires and trains 10 workers, "
        f"converts into a **`(Pty) Ltd`**, and secures export orders overseas.\n\n"
        "Explain **two macroeconomic benefits** for South Africa when growing SMMEs achieve higher **competitiveness** and expand internationally."
    )
    expected = (
        "1) Higher foreign export earnings bring money into South Africa, expanding business turnover and sustainable local jobs; "
        "2) Larger formal businesses invest in better skills/technology and widen the SARS tax base."
    )
    sol = (
        f"**SMME Competitiveness & Export Growth ({area}) [3 marks]:**\n\n"
        "1. **Foreign Earnings & Sustainable Jobs:** Exporting increases company turnover and finances permanent jobs across South Africa **[1.5]**.\n"
        "2. **Innovation, Skills & Tax Revenue:** Competitive firms train workers, adopt better productivity tools, and pay corporate/PAYE taxes **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_42",
        subskill="42_economic_growth_exports_and_smme_competitiveness",
        title="SMME Competitiveness, Exports & Economic Growth",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of jobs, foreign export income, skills, and taxes.",
            "tier_2": "Give two distinct national economic benefits of globally competitive local firms.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Higher turnover/exports fund sustainable employment", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Drives skills development, competitiveness, or higher tax revenue", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["assuming_only_domestic_sales_matter_for_growth"],
    )


def arch_43_choosing_best_ownership_form_case_studies_table(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("One hairdresser starting quickly with R4 000 savings and keeping all decisions simple", "Sole trader"),
        ("Three qualified physiotherapists combining skills without listing on any stock exchange", "Partnership"),
        ("Four software developers wanting limited liability and private shareholders only", "Private Company (Pty) Ltd"),
        ("A mining conglomerate needing R5 billion from public investors on the JSE", "Public Company (Ltd)"),
    ]
    chosen = rng.sample(cases, 3)
    headers = ["Entrepreneurial Scenario", "Most Suitable Ownership Form"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Entrepreneurial Scenario | Most Suitable Ownership Form |", "| :--- | :--- |"]
    for idx, (scen, form) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", scen, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = form
        cell_hints[c1] = "Choose: Sole trader, Partnership, Private Company (Pty) Ltd, or Public Company (Ltd)."
        memo_lines.append(f"| {scen} | {form} |")

    worked = "**Completed Ownership Advisory Table [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{s} -> {f}" for s, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_43",
        subskill="43_choosing_best_ownership_form_case_studies_table",
        title="Recommending the Best Ownership Form",
        prompt=(
            "Recommend the most suitable form of ownership for each scenario: "
            "**Sole trader**, **Partnership**, **Private Company (Pty) Ltd**, or **Public Company (Ltd)**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Check owner count, need for limited liability, and whether JSE public money is required.",
            "tier_2": "Use exact names provided in the prompt.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]} -> {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["recommending_public_company_for_micro_tuckshop"],
    )


def arch_44_close_corporation_legacy_status_and_conversion_option(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    cc_name = rng.choice(["Zain Hardware CC", "Palesa Catering CC"])
    prompt = (
        f"**{founder}** buys a member's interest in an existing Close Corporation, **{cc_name}**, while a friend wants to register a **brand-new CC** from scratch today.\n\n"
        "Under current South African law (Companies Act 71 of 2008), which statement is **correct**?"
    )
    correct = f"Existing CCs like {cc_name} continue operating with limited liability (or may convert into a (Pty) Ltd), while brand-new CCs can no longer be registered."
    distractors = [
        "Every existing CC in South Africa was immediately declared illegal and shut down overnight.",
        "Anyone can register a brand-new CC today and list its shares directly on the JSE.",
        "CCs were converted automatically into partnerships with unlimited liability.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_44",
        subskill="44_close_corporation_legacy_status_and_conversion_option",
        title="Close Corporations Today: Existing CCs vs New Entities",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Since the Companies Act transition, **no new Close Corporations** are registered, but existing ones like **{cc_name}** remain valid legal entities with limited liability and can convert to **`(Pty) Ltd`** if they expand."
        ),
        hints={
            "tier_1": "Existing CCs did not vanish, even though CIPC stopped registering brand-new CCs.",
            "tier_2": "Existing CCs keep trading (with option to convert to `(Pty) Ltd`); no new CCs can be formed.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_existing_ccs_lost_legal_validity"],
    )


def arch_45_capital_to_liability_break_even_risk_diagram(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    invested = rng.choice([100000, 150000, 200000])
    debt_left = invested + rng.choice([300000, 400000, 500000])
    personal_risk = debt_left - invested
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 200" width="100%" height="auto">'
        '<rect x="0" y="0" width="650" height="200" fill="#f8fafc" rx="10"/>'
        f'<text x="325" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{owner}: Debt Impact After Business Failure (Debt {_fmt_r(debt_left)})</text>'
        '<rect x="30" y="50" width="275" height="115" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        '<text x="167" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">Scenario A: Sole Trader</text>'
        f'<text x="167" y="102" text-anchor="middle" font-size="11" fill="#7f1d1d">Invested Capital Lost: {_fmt_r(invested)}</text>'
        f'<text x="167" y="128" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">Personal Assets Seized: {_fmt_r(personal_risk)}</text>'
        '<rect x="345" y="50" width="275" height="115" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="482" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#14532d">Scenario B: Private Co (Pty) Ltd</text>'
        f'<text x="482" y="102" text-anchor="middle" font-size="11" fill="#166534">Invested Shares Lost: {_fmt_r(invested)}</text>'
        '<text x="482" y="128" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">Personal Assets Seized: R0</text>'
        '</svg>'
    )
    prompt = (
        f"Study the risk comparison diagram for **{owner}**, whose enterprise fails owing **{_fmt_r(debt_left)}** after **{owner}** invested **{_fmt_r(invested)}**.\n\n"
        f"(a) In **Scenario A (Sole Trader)**, how much extra personal wealth is claimed from **{owner}**?\n"
        "(b) Why is personal loss capped at **R0** above invested shares in **Scenario B (`(Pty) Ltd`)**?"
    )
    expected = (
        f"(a) {_fmt_r(personal_risk)} in personal assets seized. "
        f"(b) Because a (Pty) Ltd is a separate legal entity giving {owner} limited liability — max loss equals the {_fmt_r(invested)} invested."
    )
    sol = (
        f"**Liability Exposure Comparison ({owner}) [3 marks]:**\n\n"
        f"**(a) Scenario A Personal Loss (Sole Trader):** ${_fmt_r(debt_left)} - {_fmt_r(invested)} = {_fmt_r(personal_risk)}$ seized from **{owner}**'s personal assets **[1]**.\n\n"
        f"**(b) Scenario B Protection (`(Pty) Ltd`):** Because a company is a **separate legal entity** with **limited liability**, **{owner}** loses only the **{_fmt_r(invested)}** invested in shares and **R0** from personal property **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_45",
        subskill="45_capital_to_liability_break_even_risk_diagram",
        title="Comparing Personal Loss Under Failure: Sole Trader vs (Pty) Ltd",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Read the bottom line of each box in the risk comparison diagram.",
            "tier_2": f"Scenario A loses {_fmt_r(personal_risk)} personally; Scenario B stops at {_fmt_r(invested)} due to limited liability.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Personal wealth seized = {_fmt_r(personal_risk)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Explains separate legal entity and limited liability protect personal assets", "marks": 2, "editable": True},
        ],
        misconception_tags=["thinking_shareholders_lose_zero_even_on_initial_share_capital"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_46_franchise_vs_independent_ownership_entity_note(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    franchisee = rng.choice(PERSON_NAMES)
    prompt = (
        f"**{franchisee}** buys the rights to operate a branded fast-food franchise outlet in **{area}**.\n\n"
        "In South African business law, does buying a **franchise** automatically create a separate form of ownership on its own?"
    )
    correct = f"No — franchising is a licensing arrangement; {franchisee} must still register and run the outlet using a legal ownership form such as a Sole trader, Partnership, CC, or (Pty) Ltd."
    distractors = [
        "Yes — every franchise outlet in South Africa is owned directly by the Minister of Finance.",
        "Yes — franchisees enjoy limited liability automatically without registering any legal entity.",
        "No — franchisees are prohibited from hiring South African workers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_46",
        subskill="46_franchise_vs_independent_ownership_entity_note",
        title="Franchises & Legal Form of Ownership",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A franchise contract governs branding and operating systems, while **{franchisee}** still picks a legal ownership structure (typically **`(Pty) Ltd`**, **CC**, **Partnership**, or **Sole trader**)."
        ),
        hints={
            "tier_1": "Notice that a franchise still needs a CIPC company, CC, partnership, or sole owner behind the counter.",
            "tier_2": "Franchise = business model/licence, not a separate ownership type.",
            "tier_3": correct,
        },
        misconception_tags=["treating_franchise_as_a_sixth_statutory_ownership_form"],
    )


def arch_47_corporate_social_and_environmental_sustainability_calc(rng: random.Random) -> Dict[str, Any]:
    co = rng.choice(["Ubuntu Textiles (Pty) Ltd", "Bafana Bottlers Ltd", "Mfula Timber CC"])
    solar_cost = rng.choice([600000, 900000, 1200000])
    annual_saving = solar_cost // rng.choice([3, 4, 5])
    payback_yrs = solar_cost // annual_saving

    prompt = (
        f"To shift away from non-renewable coal electricity toward **sustainable renewable energy**, **{co}** invests **{_fmt_r(solar_cost)}** in rooftop solar panels, "
        f"saving **{_fmt_r(annual_saving)}** per year on power costs.\n\n"
        "(a) How many **years** will it take for electricity savings to pay back the **{_fmt_r(solar_cost)}** investment?\n"
        "(b) State **one environmental benefit** and **one long-term financial benefit** of this transition."
    )
    expected = (
        f"(a) Payback period = {payback_yrs} years. "
        "(b) Environmental: lowers fossil-fuel emissions and reliance on non-renewable coal; Financial: cuts ongoing utility expenses and insulates the business from power hikes."
    )
    sol = (
        f"**Renewable Investment Sustainability ({co}) [4 marks]:**\n\n"
        f"**(a) Payback Period:**\n"
        f"$${_fmt_r(solar_cost)} \\div {_fmt_r(annual_saving)} = {payback_yrs}\\text{{ years}}$$ **[2]**\n\n"
        "**(b) Environmental & Financial Benefits [2 marks]:**\n"
        "1. **Environmental:** Uses renewable sunlight instead of finite coal, reducing pollution **[1]**.\n"
        "2. **Financial:** After year " + str(payback_yrs) + ", clean electricity savings improve net profitability and resilience **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_47",
        subskill="47_corporate_social_and_environmental_sustainability_calc",
        title="Renewable Energy Payback & Business Sustainability",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Divide installation cost by annual electricity savings.",
            "tier_2": "Give both a non-renewable conservation benefit and a business cost-saving benefit.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Payback = {payback_yrs} years", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Environmental benefit (replaces non-renewable fossil energy)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Financial benefit (lower long-term electricity costs)", "marks": 1, "editable": True},
        ],
        misconception_tags=["viewing_green_investments_purely_as_unrecoverable_cost"],
        qtype="calculation",
    )


def arch_48_partnership_dispute_without_written_agreement(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(PERSON_NAMES)
    p2 = rng.choice([n for n in PERSON_NAMES if n != p1])
    prompt = (
        f"**{p1}** contributed 80% of the money and works 60 hours a week, while partner **{p2}** works 15 hours a week. "
        "They started with only a **verbal handshake** and never signed a written **Partnership Agreement**.\n\n"
        "Identify **two serious disputes** likely to arise here and explain why a **written Partnership Agreement** prevents them."
    )
    expected = (
        "Disputes: 1) Disagreement over how profits/losses should be split (80:20 vs 50:50); "
        "2) Conflict over workload, decision authority, or exit buyout terms. "
        "Prevention: A written Partnership Agreement sets clear legally binding ratios, duties, and exit procedures upfront."
    )
    sol = (
        f"**Importance of a Written Partnership Agreement ({p1} & {p2}) [3 marks]:**\n\n"
        "1. **Profit-Split Dispute:** Without written terms, partners clash over whether profits follow capital (80%), hours worked, or equal shares **[1]**.\n"
        "2. **Workload & Exit Conflict:** Unequal work hours and unclear withdrawal rules cause breakdown **[1]**.\n"
        "3. **Written Agreement Protection:** Recording profit ratios, duties, authority limits, and dissolution rules upfront avoids costly court disputes **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_48",
        subskill="48_partnership_dispute_without_written_agreement",
        title="Risks of Verbal vs Written Partnership Agreements",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Look at the uneven money and work hours in the prompt.",
            "tier_2": "Identify two conflict areas (profit split, duties/exit) and explain how a written contract clarifies rules upfront.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Profit/loss sharing dispute", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Workload / decision / exit conflict", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Written Partnership Agreement defines clear binding rules upfront", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_verbal_trust_is_enough_between_partners"],
    )


def arch_49_ownership_misconception_error_audit_table(rng: random.Random) -> Dict[str, Any]:
    myths = [
        ("Coca-Cola South Africa (Pty) Ltd sells shares freely to ordinary citizens on the JSE.", "(Pty) Ltd is a Private Company; its shares CANNOT be sold publicly on the JSE"),
        ("A Public Company (Ltd) is owned by the South African government.", "Owned by private/public shareholders; government firms are State-Owned Enterprises (SOEs)"),
        ("Sole traders have limited liability so their houses are safe if the business fails.", "Sole traders have UNLIMITED liability putting personal assets at risk"),
        ("A partnership continues unchanged automatically when one partner dies.", "No continuity; original partnership dissolves when a partner dies or exits"),
    ]
    chosen = rng.sample(myths, 3)
    headers = ["Incorrect Ownership Myth", "Factual Correction"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Incorrect Ownership Myth | Factual Correction |", "| :--- | :--- |"]
    for idx, (myth, fix) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", myth, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = fix
        cell_hints[c1] = "State the exact legal/ownership correction."
        memo_lines.append(f"| {myth} | {fix} |")

    worked = "**Completed Ownership Misconception Audit [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{m} -> {f}" for m, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_49",
        subskill="49_ownership_misconception_error_audit_table",
        title="Forms of Ownership Misconception Audit",
        prompt="Identify the error in each statement and write the **accurate ownership fact** in the right column.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Check `(Pty) Ltd` vs `Ltd`, Public Company vs SOE, liability, and continuity.",
            "tier_2": "Write concise factual corrections.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Corrects myth {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["confusing_public_company_with_state_ownership"],
    )


def arch_50_holistic_entrepreneurship_ownership_and_sustainability_synthesis(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    founder = rng.choice(PERSON_NAMES)
    staff = rng.choice([12, 18, 24])
    prompt = (
        f"**Entrepreneurship Case Study ({area}):**\n"
        f"**{founder}** started a recycling and eco-brick workshop 6 years ago as a **sole trader**. Today, the business employs **{staff} youth**, "
        f"supplies large construction retailers, and needs **R12 million** in investor equity to scale nationally while reducing diesel and coal-grid dependence.\n\n"
        "Answer all three parts:\n"
        f"1. Recommend whether **{founder}** should convert into a **`(Pty) Ltd`** or a **`Ltd`** right now, giving **two legal/capital reasons** (liability, continuity, share rules).\n"
        f"2. Explain **two ways** SMMEs growing like **{founder}'s workshop** promote **sustainable job creation** and close South Africa's **skills shortage**.\n"
        "3. Suggest **two practical steps** the factory must take to ensure **sustainable use of renewable and non-renewable resources**."
    )
    expected = (
        "1) Convert to (Pty) Ltd (if raising R12m from invited private investors with restricted share trading, MOI, limited liability, separate legal entity, and continuity) — OR Ltd if seeking public JSE capital via Prospectus. "
        f"2) Employs and upskills {staff} local youth on the job; higher turnover and competitiveness help the firm scale sustainable permanent jobs. "
        "3) Conserve water/renewable inputs responsibly; reduce diesel/coal waste and invest in solar/recycled raw materials."
    )
    sol = (
        f"**Entrepreneurship, Ownership & Sustainability Synthesis ({founder}) [6 marks]:**\n\n"
        "1. **Recommended Ownership Upgrade (`(Pty) Ltd`) [2 marks]:**\n"
        "   - Converts via an **MOI** into a **`(Pty) Ltd`** (ideal for R12m private investor equity before public JSE listing), securing **separate legal entity status, limited liability, and continuity of existence** **[2]**.\n"
        f"2. **SMME Job Creation & Skills Transfer ({staff} youth) [2 marks]:**\n"
        "   - Creates local employment and transfers **hands-on technical/business skills**, alleviating the skills shortage **[1]**.\n"
        "   - Stronger competitiveness and turnover sustain permanent career growth **[1]**.\n"
        "3. **Resource Sustainability [2 marks]:**\n"
        "   - Harvest/use **renewable inputs** (water/bio-materials) responsibly without depletion **[1]**.\n"
        "   - Cut reliance on **non-renewable** coal/diesel via efficiency and **solar/recycled alternatives** **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_50",
        subskill="50_holistic_entrepreneurship_ownership_and_sustainability_synthesis",
        title="Holistic Forms of Ownership & Sustainability Case Synthesis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Break your answer into 3 parts: (1) Legal Form/Capital/Liability, (2) SMME Jobs & Skills, (3) Renewable & Non-Renewable Resources.",
            "tier_2": "Highlight `(Pty) Ltd` (or `Ltd` for JSE), hands-on skills transfer, and clean resource alternatives.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Recommends suitable corporate form with 2 legal/capital reasons", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Explains SMME sustainable job creation and skills transfer", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Identifies sustainable use of renewable and non-renewable alternatives", "marks": 2, "editable": True},
        ],
        misconception_tags=["ignoring_link_between_ownership_growth_and_sustainability"],
        qtype="extended_response",
    )


BUILDERS_26_50 = {
    "26_smme_definition_and_ownership_types": arch_26_smme_definition_and_ownership_types,
    "27_smme_role_in_sustainable_job_creation": arch_27_smme_role_in_sustainable_job_creation,
    "28_smme_skills_transfer_and_youth_employment": arch_28_smme_skills_transfer_and_youth_employment,
    "29_business_growth_progression_sole_to_company": arch_29_business_growth_progression_sole_to_company,
    "30_tax_implications_sole_trader_vs_company": arch_30_tax_implications_sole_trader_vs_company,
    "31_profit_distribution_across_ownership_forms_table": arch_31_profit_distribution_across_ownership_forms_table,
    "32_raising_capital_ability_ranking_table": arch_32_raising_capital_ability_ranking_table,
    "33_decision_making_speed_vs_corporate_governance": arch_33_decision_making_speed_vs_corporate_governance,
    "34_sustainable_use_of_renewable_resources": arch_34_sustainable_use_of_renewable_resources,
    "35_non_renewable_resources_and_alternative_innovation": arch_35_non_renewable_resources_and_alternative_innovation,
    "36_large_company_ecological_footprint_vs_smme": arch_36_large_company_ecological_footprint_vs_smme,
    "37_public_sector_soe_vs_public_company_distinction": arch_37_public_sector_soe_vs_public_company_distinction,
    "38_sole_trader_income_statement_to_owner_drawings_calc": arch_38_sole_trader_income_statement_to_owner_drawings_calc,
    "39_private_company_shareholder_voting_percentage_calc": arch_39_private_company_shareholder_voting_percentage_calc,
    "40_converting_partnership_to_pty_ltd_scenario": arch_40_converting_partnership_to_pty_ltd_scenario,
    "41_cipc_compliance_and_annual_audit_requirement": arch_41_cipc_compliance_and_annual_audit_requirement,
    "42_economic_growth_exports_and_smme_competitiveness": arch_42_economic_growth_exports_and_smme_competitiveness,
    "43_choosing_best_ownership_form_case_studies_table": arch_43_choosing_best_ownership_form_case_studies_table,
    "44_close_corporation_legacy_status_and_conversion_option": arch_44_close_corporation_legacy_status_and_conversion_option,
    "45_capital_to_liability_break_even_risk_diagram": arch_45_capital_to_liability_break_even_risk_diagram,
    "46_franchise_vs_independent_ownership_entity_note": arch_46_franchise_vs_independent_ownership_entity_note,
    "47_corporate_social_and_environmental_sustainability_calc": arch_47_corporate_social_and_environmental_sustainability_calc,
    "48_partnership_dispute_without_written_agreement": arch_48_partnership_dispute_without_written_agreement,
    "49_ownership_misconception_error_audit_table": arch_49_ownership_misconception_error_audit_table,
    "50_holistic_entrepreneurship_ownership_and_sustainability_synthesis": arch_50_holistic_entrepreneurship_ownership_and_sustainability_synthesis,
}
