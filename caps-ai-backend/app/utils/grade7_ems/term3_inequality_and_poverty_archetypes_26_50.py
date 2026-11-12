"""Grade 7 EMS — Inequality and Poverty: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards (Term 3: The Economy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 4/02. Inequality and poverty.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

from .term3_inequality_and_poverty_archetypes_01_25 import (
    _fmt_comma,
    _fmt_zar,
    _mcq,
    _svg_bar_chart,
    _svg_cycle_flow,
    _table_q,
    _typed,
)


def arch_26_urban_vs_rural_service_access_bar_graph(rng: random.Random) -> Dict[str, Any]:
    urban_area = rng.choice(URBAN_AREAS)
    rural_area = rng.choice(RURAL_AREAS)
    urban_water = rng.randint(88, 96)
    rural_water = rng.randint(36, 52)
    urban_elec = rng.randint(85, 95)
    rural_elec = rng.randint(48, 64)
    gap = urban_water - rural_water

    svg = _svg_bar_chart(
        title="Household Piped Water & Electricity Access (%)",
        y_label="Share of Households (%)",
        bars=[
            ("Urban Water", float(urban_water), "#1D4ED8"),
            ("Rural Water", float(rural_water), "#F59E0B"),
            ("Urban Elec", float(urban_elec), "#0F766E"),
            ("Rural Elec", float(rural_elec), "#DC2626"),
        ],
        max_val=100.0,
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the bar graph below comparing household access to piped water and electricity between "
        f"{urban_area} (urban) and {rural_area} (rural).\n\n"
        f"Calculate the percentage-point gap between Urban Water access ({urban_water}%) and Rural Water access ({rural_water}%)."
    )
    return _typed(
        rng,
        subskill="26_urban_vs_rural_service_access_bar_graph",
        title="Urban vs Rural Basic Service Gap (Bar Graph)",
        prompt=prompt,
        sample_answer=(
            f"Piped water access gap = {urban_water}% - {rural_water}% = {gap} percentage points.\n"
            f"This shows severe spatial inequality between {urban_area} and {rural_area} in basic municipal service delivery."
        ),
        marking_points=[
            f"Read Urban Water ({urban_water}%) and Rural Water ({rural_water}%) from the bar graph [1]",
            f"Correctly calculate gap = {urban_water} - {rural_water} = {gap} percentage points [2]",
        ],
        hints={
            "tier_1": "Locate the first two bars representing Urban Water and Rural Water.",
            "tier_2": "Subtract the rural piped water percentage from the urban piped water percentage.",
            "tier_3": f"{urban_water}% - {rural_water}% = {gap} percentage points.",
        },
        learning_objective_id="lo_ineq_urban_rural_service_gap",
        concept_id="service_delivery_gap",
        misconception_tags=["misreads_bar_graph_values", "adds_instead_of_subtracts"],
        marks=3,
        correct_answer=f"{gap} percentage points",
        correct_value=float(gap),
        diagram_spec={"kind": "inline_svg", "title": "Urban vs Rural Service Access", "svg": svg, "diagram_role": "context"},
        worked_solution=(
            f"Step 1: Urban Water = {urban_water}%\n"
            f"Step 2: Rural Water = {rural_water}%\n"
            f"Step 3: Percentage-point gap = {urban_water} - {rural_water} = {gap}%"
        ),
    )


def arch_27_rural_poverty_intervention_strategies(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    budget_m = rng.randint(12, 48)
    prompt = (
        f"Provincial planners allocate R{budget_m} million to reduce deep structural poverty in {rural_area}, where "
        f"most families lack tarred roads, irrigation water, and market links.\n\n"
        f"Which intervention BEST addresses rural poverty sustainably?"
    )
    correct = (
        "Building rural roads and water infrastructure alongside training, credit, and market access for small-scale farmers"
    )
    distractors = [
        "Banning all agricultural activity in the district so residents must move to metropolitan cities",
        "Issuing high-interest consumer store credit cards to rural households",
        "Closing rural primary schools to concentrate funding solely on urban shopping malls",
    ]
    return _mcq(
        rng,
        subskill="27_rural_poverty_intervention_strategies",
        title="Sustainable Rural Poverty Interventions",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"In {rural_area}, upgrading roads, irrigation water, agricultural skills, and market access raises farm "
            f"output and local non-farm jobs, breaking rural isolation sustainably."
        ),
        hints={
            "tier_1": "Think about what helps rural households produce food and sell surpluses profitably.",
            "tier_2": "Infrastructure (roads, water) plus training and market access create lasting livelihoods.",
            "tier_3": "Select the option combining infrastructure, small-scale farming support, credit, and market access.",
        },
        learning_objective_id="lo_ineq_rural_interventions",
        concept_id="rural_poverty_interventions",
        misconception_tags=["confuses_debt_with_development"],
    )


def arch_28_empowering_rural_women_and_youth(rng: random.Random) -> Dict[str, Any]:
    learner = rng.choice(NAMES)
    rural_area = rng.choice(RURAL_AREAS)
    women_share = rng.randint(58, 72)
    prompt = (
        f"In {rural_area}, {learner} notices that {women_share}% of households rely on women for farming, fetching "
        f"water, and childcare while young adults struggle to find local jobs.\n\n"
        f"Explain THREE ways empowering rural women and youth helps reduce rural poverty."
    )
    return _typed(
        rng,
        subskill="28_empowering_rural_women_and_youth",
        title="Empowering Rural Women and Youth",
        prompt=prompt,
        sample_answer=(
            "1. Skills training and agricultural extension help women and youth increase crop yields and start micro-enterprises.\n"
            "2. Access to micro-credit, land rights, and cooperatives enables them to buy seeds, tools, and equipment.\n"
            "3. Clean water and safe transport reduce unpaid time spent fetching water/wood, freeing hours for schooling and paid work."
        ),
        marking_points=[
            "Providing skills training/education raises productivity and enterprise creation [1]",
            "Providing access to finance, land, and cooperatives grows household income [1]",
            "Providing basic services (water/transport) frees time for education and income-earning work [1]",
        ],
        hints={
            "tier_1": "Consider education, access to finance/resources, and time saved by basic infrastructure.",
            "tier_2": "Link skills + finance + clean water/childcare directly to higher household earnings.",
            "tier_3": "Give three clear mechanisms: training/skills, access to credit/land, and infrastructure freeing productive time.",
        },
        learning_objective_id="lo_ineq_empower_women_youth",
        concept_id="rural_empowerment",
        misconception_tags=["omits_economic_link_to_empowerment"],
        marks=3,
    )


def arch_29_urban_poverty_intervention_strategies(rng: random.Random) -> Dict[str, Any]:
    urban_area = rng.choice(URBAN_AREAS)
    families = rng.randint(450, 1200)
    prompt = (
        f"Rapid migration into {urban_area} has left {families} households living in crowded informal shacks far from "
        f"industrial parks, facing poor sanitation and unsafe electricity connections.\n\n"
        f"Which municipal package is MOST effective for reducing urban poverty?"
    )
    correct = (
        "Upgrading informal settlements with formal housing, clean water, sanitation, safe electricity, and affordable public transport to jobs"
    )
    distractors = [
        "Demolishing informal settlements without providing alternative housing or basic services",
        "Removing bus and train subsidies so commuters spend most of their wages on transport",
        "Restricting urban clinics to private medical-aid members only",
    ]
    return _mcq(
        rng,
        subskill="29_urban_poverty_intervention_strategies",
        title="Urban Poverty Reduction Measures",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Formalising settlements in {urban_area} with water, sanitation, safe electricity, and affordable commuter "
            f"transport protects health and connects workers to employment hubs."
        ),
        hints={
            "tier_1": "Focus on dignity, public health, and physical access to workplaces.",
            "tier_2": "Removing transport or housing increases poverty; upgrading services and transport reduces it.",
            "tier_3": "Choose formal housing, basic services (water/sanitation/electricity), and affordable transport.",
        },
        learning_objective_id="lo_ineq_urban_interventions",
        concept_id="urban_poverty_interventions",
        misconception_tags=["favors_punitive_urban_policy"],
    )


def arch_30_sustainable_job_definition_and_meaning(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    months = rng.randint(2, 4)
    wage = rng.randint(3200, 5400)
    prompt = (
        f"{name} from {area} is comparing a {months}-month once-off clean-up stipend with a permanent manufacturing "
        f"apprenticeship paying {_fmt_zar(wage)} per month.\n\n"
        f"What BEST defines a sustainable job?"
    )
    correct = (
        "Long-lasting, secure employment that provides ongoing income, safe working conditions, and opportunities to grow skills over time"
    )
    distractors = [
        "Any cash payment earned for a single weekend of casual labour with no future work",
        "Borrowing money every month from informal lenders to cover rent and groceries",
        "Short-term relief work guaranteed to terminate permanently after a few weeks",
    ]
    return _mcq(
        rng,
        subskill="30_sustainable_job_definition_and_meaning",
        title="Meaning of a Sustainable Job",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Sustainable jobs are durable and reliable over the long term, allowing households to budget, save, educate "
            "children, and exit poverty permanently."
        ),
        hints={
            "tier_1": "Look for words linked to long-term stability rather than temporary relief.",
            "tier_2": "A sustainable job keeps existing beyond a short contract and supports ongoing living standards.",
            "tier_3": "Select the option emphasizing long-lasting, secure employment, ongoing income, and skill development.",
        },
        learning_objective_id="lo_ineq_sustainable_job_def",
        concept_id="sustainable_jobs",
        misconception_tags=["confuses_casual_work_with_sustainable_jobs"],
    )


def arch_31_job_longevity_and_security_for_poverty_reduction(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    wage = rng.randint(4200, 6800)
    contract_weeks = rng.randint(4, 8)
    prompt = (
        f"{name} supports three dependants on a {contract_weeks}-week casual contract earning {_fmt_zar(wage)} per month, "
        f"after which income stops completely for several months.\n\n"
        f"Explain TWO reasons why job longevity and security are essential for lifting families permanently out of poverty."
    )
    return _typed(
        rng,
        subskill="31_job_longevity_and_security_for_poverty_reduction",
        title="Why Job Longevity and Security Matter",
        prompt=prompt,
        sample_answer=(
            f"1. Steady year-round income of {_fmt_zar(wage)}/month prevents households from falling back into debt during unemployed months.\n"
            "2. Job security lets families afford ongoing school fees, nutritious food, housing, and emergency savings over many years."
        ),
        marking_points=[
            "Continuous income prevents recurring poverty cycles and harmful debt during idle months [1]",
            "Predictable long-term earnings enable education investment, healthcare, housing stability, and savings [1]",
        ],
        hints={
            "tier_1": "Think about what happens to bills and school fees when a short contract ends.",
            "tier_2": "Contrast temporary relief with multi-year household budgeting and savings.",
            "tier_3": "State two points: avoiding debt relapse between contracts, and enabling ongoing education, housing, and savings.",
        },
        learning_objective_id="lo_ineq_job_longevity",
        concept_id="job_longevity_security",
        misconception_tags=["ignores_income_continuity"],
        marks=2,
    )


def arch_32_job_security_impact_on_worker_motivation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    workers = rng.randint(25, 80)
    prompt = (
        f"A packaging business in {area} converts {workers} precarious day-labour roles into permanent contracts with "
        f"fair leave, safety gear, and clear performance bonuses.\n\n"
        f"How does stronger job security typically affect employees and the workplace?"
    )
    correct = (
        "Higher worker motivation, lower absenteeism, stronger loyalty, and higher output quality"
    )
    distractors = [
        "Workers immediately stop caring about quality because they can never learn new skills",
        "Employee turnover skyrockets as secure workers abandon stable incomes",
        "Customer service worsens because staff no longer cooperate as a team",
    ]
    return _mcq(
        rng,
        subskill="32_job_security_impact_on_worker_motivation",
        title="Job Security and Worker Motivation",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "When employees feel secure and valued, stress drops and commitment rises—boosting motivation, skill mastery, "
            "and overall business productivity."
        ),
        hints={
            "tier_1": "How do people perform when they know their job and income are stable and safe?",
            "tier_2": "Security encourages long-term loyalty and investment in doing the job well.",
            "tier_3": "Choose higher motivation, lower absenteeism, stronger loyalty, and better output quality.",
        },
        learning_objective_id="lo_ineq_job_security_motivation",
        concept_id="worker_motivation",
        misconception_tags=["assumes_security_causes_laziness"],
    )


def arch_33_business_sustainability_and_job_stability(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    staff = rng.randint(15, 45)
    prompt = (
        f"A local textile cooperative in {area} employs {staff} workers. Explain why the long-term financial and "
        f"operational sustainability of the business itself is necessary to keep those {staff} jobs secure."
    )
    return _typed(
        rng,
        subskill="33_business_sustainability_and_job_stability",
        title="Business Sustainability and Job Stability",
        prompt=prompt,
        sample_answer=(
            f"If the business fails to make consistent profits, manage costs, and satisfy customers, it will close and "
            f"all {staff} jobs will disappear. Sustainable businesses survive downturns, reinvest profits, and preserve "
            f"stable wages over the long run."
        ),
        marking_points=[
            "Only profitable, well-managed businesses stay open to keep paying salaries [1]",
            "Sustainable enterprises reinvest in equipment/markets, protecting and expanding jobs [1]",
        ],
        hints={
            "tier_1": "Can an unprofitable business that runs out of cash keep paying salaries?",
            "tier_2": "Connect business survival and profitability directly to employee job stability.",
            "tier_3": "Explain that business failure destroys all jobs, whereas profitable reinvestment sustains wages long-term.",
        },
        learning_objective_id="lo_ineq_business_sustainability",
        concept_id="business_sustainability",
        misconception_tags=["separates_business_viability_from_jobs"],
        marks=2,
    )


def arch_34_epwp_purpose_and_2004_launch(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    unemployed_target = rng.randint(300, 950)
    prompt = (
        f"South Africa launched the Expanded Public Works Programme (EPWP) in 2004, now recruiting {unemployed_target} "
        f"unemployed residents around {area}.\n\n"
        f"What is the PRIMARY objective of the EPWP?"
    )
    correct = (
        "To provide poverty and income relief through temporary labour-intensive work on community assets while equipping participants with practical skills"
    )
    distractors = [
        "To replace all private-sector companies with state-owned luxury retail stores",
        "To lend foreign currency exclusively to multinational mining corporations",
        "To abolish municipal tariffs for high-income commercial property owners",
    ]
    return _mcq(
        rng,
        subskill="34_epwp_purpose_and_2004_launch",
        title="EPWP Launch (2004) and Core Purpose",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Launched in 2004, the EPWP uses government budgets on labour-intensive infrastructure, social, and "
            "environmental projects to pay stipends, reduce poverty, and train workers."
        ),
        hints={
            "tier_1": "Focus on why government funds labour-intensive public projects for unemployed people.",
            "tier_2": "EPWP combines short-term income relief, useful public infrastructure/services, and training.",
            "tier_3": "Select the option combining poverty/income relief, community work, and skills training.",
        },
        learning_objective_id="lo_ineq_epwp_purpose",
        concept_id="epwp_programme",
        misconception_tags=["confuses_epwp_with_corporate_subsidy"],
    )


def arch_35_epwp_stipend_and_payroll_budget_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    daily_rate = rng.choice([120, 140, 150, 160])
    w1_days = rng.randint(15, 22)
    w2_days = rng.randint(16, 22)
    w1_pay = daily_rate * w1_days
    w2_pay = daily_rate * w2_days
    total_pay = w1_pay + w2_pay

    headers = ["EPWP Team", "Days Worked", "Daily Stipend (R)", "Total Monthly Pay (R)", "Audit Flag"]
    raw_rows = [
        [
            {"type": "given", "value": "Road Maintenance Crew"},
            {"type": "given", "value": str(w1_days)},
            {"type": "given", "value": f"R{daily_rate}"},
            {"type": "required", "expected": _fmt_zar(w1_pay)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Alien Plant Clearing Crew"},
            {"type": "given", "value": str(w2_days)},
            {"type": "given", "value": f"R{daily_rate}"},
            {"type": "required", "expected": _fmt_zar(w2_pay)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Combined Project Payroll"},
            {"type": "given", "value": str(w1_days + w2_days)},
            {"type": "given", "value": "-"},
            {"type": "required", "expected": _fmt_zar(total_pay)},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Multiply {w1_days} days by R{daily_rate}.",
        "r1_c3": f"Multiply {w2_days} days by R{daily_rate}.",
        "r2_c3": "Add the Total Monthly Pay of both crews.",
    }
    derivations = [
        f"Road Crew Pay = {w1_days} x R{daily_rate} = {_fmt_zar(w1_pay)}",
        f"Clearing Crew Pay = {w2_days} x R{daily_rate} = {_fmt_zar(w2_pay)}",
        f"Combined Project Payroll = {_fmt_zar(w1_pay)} + {_fmt_zar(w2_pay)} = {_fmt_zar(total_pay)}",
        "Leave every cell in 'Audit Flag' completely blank.",
    ]
    return _table_q(
        rng,
        subskill="35_epwp_stipend_and_payroll_budget_table",
        title="EPWP Project Payroll Schedule",
        prompt=(
            f"Complete the EPWP monthly stipend schedule for a municipal project in {area} at a uniform daily stipend of "
            f"R{daily_rate}. Leave the 'Audit Flag' column empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Use Daily Stipend x Days Worked to calculate each crew's total pay.",
            "tier_2": "Sum both crew totals to complete Combined Project Payroll.",
            "tier_3": f"Road Crew = {_fmt_zar(w1_pay)}; Clearing Crew = {_fmt_zar(w2_pay)}; Combined = {_fmt_zar(total_pay)}.",
        },
        learning_objective_id="lo_ineq_epwp_payroll_table",
        concept_id="epwp_payroll",
        misconception_tags=["miscomputes_daily_stipend_total", "fills_must_be_empty_cell"],
    )


def arch_36_working_for_water_programme(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    hectares = rng.randint(180, 520)
    prompt = (
        f"Teams from the Working for Water initiative clear {hectares} hectares of thirsty alien invader trees along a "
        f"river catchment near {rural_area}.\n\n"
        f"Which pair of benefits does Working for Water achieve at the same time?"
    )
    correct = (
        "Increases scarce water flow and restores native ecosystems while creating rural jobs and training"
    )
    distractors = [
        "Drains local rivers faster while replacing human workers with heavy mining trucks",
        "Imports more invasive eucalyptus species to dry out community boreholes",
        "Restricts drinking water exclusively to industrial factories in distant provinces",
    ]
    return _mcq(
        rng,
        subskill="36_working_for_water_programme",
        title="Working for Water Environmental Jobs",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Clearing {hectares} ha of water-guzzling invasive alien plants restores catchment water yield and biodiversity "
            f"while employing and training rural residents near {rural_area}."
        ),
        hints={
            "tier_1": "Think of both the environmental benefit (water) and the social benefit (work).",
            "tier_2": "Invasive alien plants consume far more water than indigenous fynbos or grassland.",
            "tier_3": "Choose increasing scarce water flow / ecosystem health while creating rural jobs and training.",
        },
        learning_objective_id="lo_ineq_working_for_water",
        concept_id="working_for_water",
        misconception_tags=["ignores_environmental_employment_link"],
    )


def arch_37_epwp_roads_healthcare_and_ecd_jobs(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    ecd_workers = rng.randint(18, 42)
    road_workers = rng.randint(30, 75)
    prompt = (
        f"In {area}, public works funding employs {road_workers} residents to pave feeder roads and {ecd_workers} residents "
        f"as Early Childhood Development (ECD) assistants and home-based care aides.\n\n"
        f"Explain TWO distinct ways these projects help break long-term poverty beyond simply paying weekly stipends."
    )
    return _typed(
        rng,
        subskill="37_epwp_roads_healthcare_and_ecd_jobs",
        title="Community Assets in EPWP Roads & Social Sectors",
        prompt=prompt,
        sample_answer=(
            "1. Paved roads improve clinic, school, and market access for the entire community.\n"
            "2. ECD and home-based care services prepare young children for Grade 1, protect household health, and allow parents to seek work while workers gain accredited caregiving/construction skills."
        ),
        marking_points=[
            "Better feeder roads lower transport costs and connect the whole community to markets, schools, and clinics [1]",
            "ECD/care roles improve child school-readiness and community health while transferring accredited skills to workers [1]",
        ],
        hints={
            "tier_1": "Look at what the roads and ECD/health services leave behind for the community.",
            "tier_2": "Focus on lasting public infrastructure + better early childhood health/learning + worker skills.",
            "tier_3": "Mention improved physical access via roads and stronger child readiness/health/skills from ECD & care work.",
        },
        learning_objective_id="lo_ineq_epwp_community_assets",
        concept_id="epwp_social_infrastructure",
        misconception_tags=["treats_epwp_as_pure_cash_grant"],
        marks=2,
    )


def arch_38_epwp_sector_job_distribution_bar_graph(rng: random.Random) -> Dict[str, Any]:
    infra = rng.randint(36, 48)
    enviro = rng.randint(18, 26)
    social = rng.randint(16, 24)
    non_state = 100 - (infra + enviro + social)
    total_opportunities = rng.choice([20000, 40000, 50000])
    infra_jobs = int(round(total_opportunities * infra / 100.0))

    svg = _svg_bar_chart(
        title="EPWP Work Opportunities by Sector (%)",
        y_label="Share (%)",
        bars=[
            ("Infrastructure", float(infra), "#1D4ED8"),
            ("Environment", float(enviro), "#15803D"),
            ("Social/ECD", float(social), "#D97706"),
            ("Non-State", float(non_state), "#7C3AED"),
        ],
        max_val=60.0,
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the bar graph below displaying the percentage split of {total_opportunities:,}".replace(",", " ")
        + " EPWP work opportunities across four sectors.\n\n"
        f"Calculate how many work opportunities were created in the Infrastructure sector ({infra}%)."
    )
    return _typed(
        rng,
        subskill="38_epwp_sector_job_distribution_bar_graph",
        title="EPWP Sector Distribution Analysis (Bar Graph)",
        prompt=prompt,
        sample_answer=(
            f"Infrastructure share = {infra}%\n"
            f"Work opportunities = {infra}% of {total_opportunities:,} = {infra_jobs:,}".replace(",", " ")
        ),
        marking_points=[
            f"Read Infrastructure percentage ({infra}%) from the bar graph [1]",
            f"Calculate {infra}% x {total_opportunities} = {infra_jobs} work opportunities [2]",
        ],
        hints={
            "tier_1": "Read the height of the Infrastructure bar first.",
            "tier_2": f"Convert {infra}% to {infra}/100 and multiply by {total_opportunities:,}.".replace(",", " "),
            "tier_3": f"{infra}/100 x {total_opportunities} = {infra_jobs}.",
        },
        learning_objective_id="lo_ineq_epwp_sector_share",
        concept_id="epwp_sector_analysis",
        misconception_tags=["forgets_divide_percentage_by_100"],
        marks=3,
        correct_answer=str(infra_jobs),
        correct_value=float(infra_jobs),
        diagram_spec={"kind": "inline_svg", "title": "EPWP Work Opportunities by Sector", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Infrastructure jobs = ({infra} / 100) x {total_opportunities} = {infra_jobs}",
    )


def arch_39_un_millennium_development_goals_overview(rng: random.Random) -> Dict[str, Any]:
    year_target = 2015
    nations = rng.randint(185, 193)
    prompt = (
        f"At the turn of the millennium, {nations} United Nations member countries adopted the Millennium Development "
        f"Goals (MDGs) with a target date of {year_target}.\n\n"
        f"Which goal stood as Goal 1 of the UN Millennium Development Goals?"
    )
    correct = "Eradicating extreme poverty and hunger worldwide"
    distractors = [
        "Eliminating all income taxes for high-earning international investors",
        "Replacing rural primary education exclusively with paid online universities",
        "Promoting luxury urban consumption above basic clean water provision",
    ]
    return _mcq(
        rng,
        subskill="39_un_millennium_development_goals_overview",
        title="UN Millennium Development Goals (MDGs)",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "UN MDG Goal 1 focused directly on eradicating extreme poverty and hunger, alongside universal primary "
            "education, gender equality, lower child mortality, and environmental sustainability."
        ),
        hints={
            "tier_1": "Remember the central global challenge linking food security and income deprivation.",
            "tier_2": "All eight MDGs prioritised human dignity—starting with extreme poverty and hunger.",
            "tier_3": "Select 'Eradicating extreme poverty and hunger worldwide'.",
        },
        learning_objective_id="lo_ineq_un_mdgs",
        concept_id="millennium_development_goals",
        misconception_tags=["confuses_mdgs_with_tax_cuts"],
    )


def arch_40_private_urban_vs_public_rural_healthcare(rng: random.Random) -> Dict[str, Any]:
    urban_area = rng.choice(URBAN_AREAS)
    rural_area = rng.choice(RURAL_AREAS)
    distance_km = rng.randint(25, 65)
    prompt = (
        f"Residents in affluent suburbs of {urban_area} use medical-aid private hospitals minutes from home, whereas "
        f"families in {rural_area} travel {distance_km} km to reach an under-staffed public clinic.\n\n"
        f"Explain TWO ways unequal healthcare access deepens economic inequality between households."
    )
    return _typed(
        rng,
        subskill="40_private_urban_vs_public_rural_healthcare",
        title="Healthcare Access Inequality & Economic Impact",
        prompt=prompt,
        sample_answer=(
            f"1. High travel costs over {distance_km} km and long clinic queues eat into low rural incomes and cost days of missed wages.\n"
            "2. Untreated or delayed illnesses lower children's school attendance and adults' productivity, locking families into low earnings."
        ),
        marking_points=[
            "Long travel distances and clinic delays increase out-of-pocket costs and lost working hours [1]",
            "Poorer health reduces school attendance, work capacity, and earning potential [1]",
        ],
        hints={
            "tier_1": "Think about both the financial cost of travelling far to clinics and what illness does to school/work.",
            "tier_2": "Health inequality feeds directly back into lost wages and missed school days.",
            "tier_3": "Give two impacts: extra travel/lost-wage costs, and poorer health reducing education and productivity.",
        },
        learning_objective_id="lo_ineq_healthcare_gap",
        concept_id="healthcare_inequality",
        misconception_tags=["treats_healthcare_as_separate_from_economy"],
        marks=2,
    )


def arch_41_poor_quality_education_summary_table(rng: random.Random) -> Dict[str, Any]:
    class_size = rng.randint(52, 74)
    area = rng.choice(AREAS)
    headers = ["Classroom Barrier", "Immediate Effect", "Long-Term Economic Consequence", "Audit Check"]
    raw_rows = [
        [
            {"type": "given", "value": f"Overcrowded class ({class_size} learners)"},
            {"type": "required", "expected": "Little individual teacher attention"},
            {"type": "given", "value": "Weak literacy and numeracy"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "No science labs or textbooks"},
            {"type": "given", "value": "Theory memorised without practice"},
            {"type": "required", "expected": "Exclusion from technical careers"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Lack of qualified specialist teachers"},
            {"type": "required", "expected": "High failure and dropout rates"},
            {"type": "given", "value": "Persistently high youth unemployment"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Exact phrase: 'Little individual teacher attention'.",
        "r1_c2": "Exact phrase: 'Exclusion from technical careers'.",
        "r2_c1": "Exact phrase: 'High failure and dropout rates'.",
    }
    derivations = [
        f"Class of {class_size} learners -> Little individual teacher attention -> Weak literacy/numeracy.",
        "No labs/textbooks -> Theory without practice -> Exclusion from technical careers.",
        "Lack of specialist teachers -> High failure and dropout rates -> Youth unemployment.",
        "Leave 'Audit Check' blank.",
    ]
    return _table_q(
        rng,
        subskill="41_poor_quality_education_summary_table",
        title="Education Quality Barriers Matrix",
        prompt=(
            f"Complete the Education Quality Matrix for schools surveyed in {area} using these exact completions: "
            f"'Little individual teacher attention', 'Exclusion from technical careers', and 'High failure and dropout rates'. "
            f"Leave 'Audit Check' blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Match each school barrier to whether the missing cell is an Immediate Effect or Long-Term Economic Consequence.",
            "tier_2": "Large classes limit individual attention; no science labs block technical careers; weak teaching raises dropouts.",
            "tier_3": "Fill r0_c1='Little individual teacher attention', r1_c2='Exclusion from technical careers', r2_c1='High failure and dropout rates'.",
        },
        learning_objective_id="lo_ineq_education_matrix",
        concept_id="education_quality_matrix",
        misconception_tags=["swaps_immediate_and_long_term_effects"],
    )


def arch_42_progressive_tax_and_social_grant_budget_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    rural_area = rng.choice(RURAL_AREAS)
    grant_inc = rng.choice([2000, 2150, 2300])
    casual_inc = rng.choice([750, 900, 1050])
    total_inc = grant_inc + casual_inc
    food_exp = rng.choice([1450, 1550, 1650])
    elec_exp = rng.choice([350, 420, 480])
    trans_exp = rng.choice([320, 380, 440])
    total_exp = food_exp + elec_exp + trans_exp
    balance = total_inc - total_exp

    headers = ["Household Budget Item", "Income (R)", "Essential Expense (R)", "Verification"]
    raw_rows = [
        [
            {"type": "given", "value": "Social Grants (Old Age & Child Support)"},
            {"type": "given", "value": _fmt_zar(grant_inc)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Casual Gardening Income"},
            {"type": "given", "value": _fmt_zar(casual_inc)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Total Monthly Household Income"},
            {"type": "required", "expected": _fmt_zar(total_inc)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Basic Food, Electricity & Clinic Transport"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(total_exp)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Remaining Buffer / Savings"},
            {"type": "required", "expected": _fmt_zar(balance)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r2_c1": f"Add {_fmt_zar(grant_inc)} and {_fmt_zar(casual_inc)}.",
        "r4_c1": f"Subtract essential expenses ({_fmt_zar(total_exp)}) from Total Monthly Household Income.",
    }
    derivations = [
        f"Total Income = {_fmt_zar(grant_inc)} + {_fmt_zar(casual_inc)} = {_fmt_zar(total_inc)}",
        f"Food ({_fmt_zar(food_exp)}) + Electricity ({_fmt_zar(elec_exp)}) + Transport ({_fmt_zar(trans_exp)}) = {_fmt_zar(total_exp)}",
        f"Remaining Buffer = {_fmt_zar(total_inc)} - {_fmt_zar(total_exp)} = {_fmt_zar(balance)}",
    ]
    return _table_q(
        rng,
        subskill="42_progressive_tax_and_social_grant_budget_table",
        title="Social Grant Household Cash Buffer Table",
        prompt=(
            f"In {rural_area}, {name}'s household receives {_fmt_zar(grant_inc)} in social grants plus {_fmt_zar(casual_inc)} "
            f"from casual gardening. Essential monthly bills total {_fmt_zar(total_exp)} (food {_fmt_zar(food_exp)}, "
            f"electricity {_fmt_zar(elec_exp)}, transport {_fmt_zar(trans_exp)}). Complete the two required cells and leave shaded columns empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "First total both income sources in the Income column.",
            "tier_2": "Next subtract Total Essential Expenses from Total Monthly Household Income.",
            "tier_3": f"Total Income = {_fmt_zar(total_inc)}; Remaining Buffer = {_fmt_zar(balance)}.",
        },
        learning_objective_id="lo_ineq_grant_household_budget",
        concept_id="social_grant_budget",
        misconception_tags=["forgets_to_subtract_expenses", "fills_must_be_empty_cell"],
    )


def arch_43_rural_vs_urban_monthly_income_gap_bar_graph(rng: random.Random) -> Dict[str, Any]:
    metro = rng.choice([12500, 14000, 15500])
    town = rng.choice([7200, 8000, 8800])
    rural = rng.choice([2800, 3200, 3600])
    gap = metro - rural

    svg = _svg_bar_chart(
        title="Median Monthly Household Income by Area (R)",
        y_label="Monthly Income (R)",
        bars=[
            ("Urban Metro", float(metro), "#1D4ED8"),
            ("Small Town", float(town), "#0284C7"),
            ("Deep Rural", float(rural), "#DC2626"),
        ],
        max_val=16000.0,
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below comparing median monthly household incomes across South African settlement types: "
        f"Urban Metro ({_fmt_zar(metro)}), Small Town ({_fmt_zar(town)}), and Deep Rural ({_fmt_zar(rural)}).\n\n"
        f"Calculate the monthly Rand income gap between an Urban Metro household and a Deep Rural household."
    )
    return _typed(
        rng,
        subskill="43_rural_vs_urban_monthly_income_gap_bar_graph",
        title="Urban vs Rural Household Income Gap (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Monthly income gap = {_fmt_zar(metro)} - {_fmt_zar(rural)} = {_fmt_zar(gap)}",
        marking_points=[
            f"Read Urban Metro ({_fmt_zar(metro)}) and Deep Rural ({_fmt_zar(rural)}) from the bar graph [1]",
            f"Compute gap = {_fmt_zar(metro)} - {_fmt_zar(rural)} = {_fmt_zar(gap)} [2]",
        ],
        hints={
            "tier_1": "Compare the tallest bar (Urban Metro) against the shortest bar (Deep Rural).",
            "tier_2": f"Subtract {_fmt_zar(rural)} from {_fmt_zar(metro)}.",
            "tier_3": f"{_fmt_zar(metro)} - {_fmt_zar(rural)} = {_fmt_zar(gap)}.",
        },
        learning_objective_id="lo_ineq_income_gap_graph",
        concept_id="income_disparity_graph",
        misconception_tags=["picks_small_town_instead_of_deep_rural"],
        marks=3,
        correct_answer=_fmt_zar(gap),
        correct_value=float(gap),
        diagram_spec={"kind": "inline_svg", "title": "Median Monthly Household Income", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Gap = {_fmt_zar(metro)} - {_fmt_zar(rural)} = {_fmt_zar(gap)}",
    )


def arch_44_skills_shortage_sector_impact_schedule(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["Scarce Skill Sector", "Economic Bottleneck Caused", "Targeted Policy Fix", "Extra"]
    raw_rows = [
        [
            {"type": "given", "value": "Civil & Electrical Engineering"},
            {"type": "required", "expected": "Delayed water, road & power projects"},
            {"type": "given", "value": "SETA apprenticeships & university bursaries"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Medical & Nursing Staff"},
            {"type": "given", "value": "Overloaded rural public clinics"},
            {"type": "required", "expected": "Rural health scholarships & retention"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Maths & Science Teachers"},
            {"type": "required", "expected": "Fewer university-ready STEM graduates"},
            {"type": "given", "value": "Funza Lushaka teacher training grants"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Exact phrase: 'Delayed water, road & power projects'.",
        "r1_c2": "Exact phrase: 'Rural health scholarships & retention'.",
        "r2_c1": "Exact phrase: 'Fewer university-ready STEM graduates'.",
    }
    derivations = [
        "Engineering shortage -> Delayed water, road & power projects.",
        "Medical shortage -> Overloaded rural public clinics -> Rural health scholarships & retention.",
        "Teacher shortage -> Fewer university-ready STEM graduates.",
    ]
    return _table_q(
        rng,
        subskill="44_skills_shortage_sector_impact_schedule",
        title="Skills Shortage Bottlenecks & Fixes Schedule",
        prompt=(
            f"District planners in {area} need to align skills shortages with economic bottlenecks and solutions. "
            f"Fill in the blanks using these exact phrases: 'Delayed water, road & power projects', "
            f"'Rural health scholarships & retention', and 'Fewer university-ready STEM graduates'. Leave 'Extra' blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Link engineering to infrastructure, medicine to clinics, and teachers to STEM learners.",
            "tier_2": "Check whether the blank sits in 'Economic Bottleneck Caused' or 'Targeted Policy Fix'.",
            "tier_3": "r0_c1='Delayed water, road & power projects'; r1_c2='Rural health scholarships & retention'; r2_c1='Fewer university-ready STEM graduates'.",
        },
        learning_objective_id="lo_ineq_skills_bottlenecks_table",
        concept_id="skills_shortage_table",
        misconception_tags=["mismatch_sector_to_bottleneck"],
    )


def arch_45_epwp_worker_skills_transfer_calculation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    cohort = rng.choice([200, 300, 400, 500])
    pct = rng.choice([25, 30, 35, 40])
    placed = int(round(cohort * pct / 100.0))
    prompt = (
        f"In {area}, {cohort} unemployed youths complete an EPWP plumbing and solar-geyser installation project coupled "
        f"with accredited artisan training. If {pct}% of participants secure permanent private-sector jobs after "
        f"graduating, how many youths move into permanent employment?"
    )
    return _typed(
        rng,
        subskill="45_epwp_worker_skills_transfer_calculation",
        title="EPWP Training-to-Employment Transition",
        prompt=prompt,
        sample_answer=f"Permanent jobs secured = {pct}% x {cohort} = {placed} youths.",
        marking_points=[
            f"Set up percentage calculation: ({pct} / 100) x {cohort} [1]",
            f"Correctly evaluate = {placed} youths [1]",
        ],
        hints={
            "tier_1": "Convert the percentage placed into a fraction out of 100.",
            "tier_2": f"Calculate ({pct} / 100) x {cohort}.",
            "tier_3": f"{pct}% of {cohort} = {placed} youths.",
        },
        learning_objective_id="lo_ineq_epwp_placement_calc",
        concept_id="epwp_skills_transition",
        misconception_tags=["adds_percentage_instead_of_multiplying"],
        marks=2,
        correct_answer=f"{placed} youths",
        correct_value=float(placed),
        worked_solution=f"({pct} / 100) x {cohort} = {placed} youths",
    )


def arch_46_environmental_sustainability_and_poverty_link(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    households = rng.randint(140, 380)
    prompt = (
        f"Acid mine drainage and illegal dumping contaminate the main stream relied upon by {households} subsistence "
        f"farming households near {rural_area}.\n\n"
        f"Why do environmental pollution and land degradation worsen rural poverty fastest?"
    )
    correct = (
        "Low-income families directly depend on clean water, fertile soil, and grazing land for daily food and cannot afford private substitutes"
    )
    distractors = [
        "Rural households receive higher farm prices whenever rivers turn acidic and crops fail",
        "Polluted water automatically converts dry farmland into wealthy industrial cities",
        "Only wealthy urban residents suffer from damaged grazing land and soil erosion",
    ]
    return _mcq(
        rng,
        subskill="46_environmental_sustainability_and_poverty_link",
        title="Environmental Degradation and Rural Poverty",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"In {rural_area}, {households} families rely directly on clean water and soil for survival; unlike wealthier "
            f"households, they cannot afford bottled water or imported groceries when local ecosystems collapse."
        ),
        hints={
            "tier_1": "Compare who can afford alternatives when rivers or soil are ruined.",
            "tier_2": "Subsistence households depend directly on local ecosystems for water, food, and livestock.",
            "tier_3": "Select the option explaining direct dependence on water/soil and inability to buy substitutes.",
        },
        learning_objective_id="lo_ineq_env_poverty",
        concept_id="environmental_poverty_link",
        misconception_tags=["ignores_ecosystem_dependence"],
    )


def arch_47_fiscal_redistribution_tax_to_grant_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    tax_b = rng.randint(180, 260)
    svg = _svg_cycle_flow(
        title="Progressive Tax & Social Redistribution Flow",
        nodes=[
            f"1. Progressive Tax (R{tax_b}B collected)",
            "2. National Treasury Budget Allocation",
            "3. Public Schools, Clinics & Grants",
            "4. Healthier Skilled Workers Grow GDP",
        ],
        accent_color="#0F766E",
    )
    prompt = (
        f"Refer to the flowchart below showing how R{tax_b} billion in progressive taxation circulates through the South "
        f"African economy.\n\n"
        f"Explain how Step 3 (public schools, clinics, and social grants) leads to Step 4 (healthier, skilled workers growing GDP)."
    )
    return _typed(
        rng,
        subskill="47_fiscal_redistribution_tax_to_grant_flow_diagram",
        title="Fiscal Redistribution Cycle (Flowchart)",
        prompt=prompt,
        sample_answer=(
            f"Redistributing part of the R{tax_b}B tax revenue into nutrition, healthcare, and quality schooling equips "
            f"children from low-income families to stay healthy, graduate, enter skilled jobs, earn higher incomes, and "
            f"contribute taxes that grow national GDP."
        ),
        marking_points=[
            "Public clinics and grants protect nutrition and health so learners stay in school [1]",
            "Public education builds scarce skills, raising employment, productivity, and future tax revenue (GDP growth) [2]",
        ],
        hints={
            "tier_1": "Follow the arrow from Box 3 to Box 4 in the flowchart.",
            "tier_2": "Healthy, educated young people become more productive workers and taxpayers.",
            "tier_3": "Explain that clinics/grants support schooling, schooling builds skills, and skilled workers expand GDP.",
        },
        learning_objective_id="lo_ineq_fiscal_flow_diagram",
        concept_id="fiscal_redistribution_cycle",
        misconception_tags=["views_social_spending_as_pure_loss"],
        marks=3,
        diagram_spec={"kind": "inline_svg", "title": "Progressive Tax Redistribution Flow", "svg": svg, "diagram_role": "context"},
    )


def arch_48_legislation_reforms_matching_matrix(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["South African Law / Initiative", "Year / Milestone", "Core Redress Mechanism", "Notes"]
    raw_rows = [
        [
            {"type": "given", "value": "Employment Equity Act"},
            {"type": "given", "value": "1998"},
            {"type": "required", "expected": "Fair workplace representation"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Skills Development Act"},
            {"type": "given", "value": "1998"},
            {"type": "required", "expected": "SETA levies and learnerships"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Expanded Public Works Programme"},
            {"type": "given", "value": "2004"},
            {"type": "required", "expected": "Temporary jobs and training"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact phrase: 'Fair workplace representation'.",
        "r1_c2": "Exact phrase: 'SETA levies and learnerships'.",
        "r2_c2": "Exact phrase: 'Temporary jobs and training'.",
    }
    derivations = [
        "Employment Equity Act (1998) -> Fair workplace representation.",
        "Skills Development Act (1998) -> SETA levies and learnerships.",
        "EPWP (2004) -> Temporary jobs and training.",
    ]
    return _table_q(
        rng,
        subskill="48_legislation_reforms_matching_matrix",
        title="Post-1994 Economic Redress Policy Matrix",
        prompt=(
            f"For a civic economics workshop in {area}, match each South African policy to its redress mechanism using these "
            f"exact phrases: 'Fair workplace representation', 'SETA levies and learnerships', and 'Temporary jobs and training'. "
            f"Leave 'Notes' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Distinguish workplace anti-discrimination (Employment Equity) from training levies (Skills Act) and public works (EPWP).",
            "tier_2": "Match each of the three provided exact strings to its corresponding statute/programme.",
            "tier_3": "r0_c2='Fair workplace representation'; r1_c2='SETA levies and learnerships'; r2_c2='Temporary jobs and training'.",
        },
        learning_objective_id="lo_ineq_redress_legislation_table",
        concept_id="redress_legislation",
        misconception_tags=["mixes_up_1998_acts_and_epwp"],
    )


def arch_49_small_business_vs_grant_dependency_sustainability(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    grant = rng.choice([2100, 2200, 2300])
    prompt = (
        f"{name}'s community group in {area} debates whether {_fmt_zar(grant)} monthly social grants alone can lift "
        f"families permanently out of poverty, or if micro-enterprise support and artisan training are also needed.\n\n"
        f"Evaluate why combining social grants with small-business support and skills training is more sustainable than grants alone."
    )
    return _typed(
        rng,
        subskill="49_small_business_vs_grant_dependency_sustainability",
        title="Social Grants Plus Entrepreneurship Sustainability",
        prompt=prompt,
        sample_answer=(
            f"Social grants ({_fmt_zar(grant)}/month) prevent immediate hunger, but cannot raise household income above subsistence "
            "or absorb rising unemployment. Adding artisan skills and SMME support enables households to build profitable "
            "businesses, create additional jobs, and achieve independent long-term prosperity."
        ),
        marking_points=[
            "Grants meet urgent basic survival needs (food/schooling) immediately [1]",
            "Grants alone are limited by state tax budgets and keep households near subsistence [1]",
            "Skills + SMME support create self-sustaining income, savings, and additional local employment [1]",
        ],
        hints={
            "tier_1": "Acknowledge both the immediate safety net of grants AND the long-term ceiling if no jobs exist.",
            "tier_2": "Show how grants stabilize survival while skills and small businesses create independent growth.",
            "tier_3": "Include all three points: short-term hunger relief, fiscal/income limits of grants alone, and wealth/job creation via SMMEs.",
        },
        learning_objective_id="lo_ineq_grants_vs_smme",
        concept_id="smme_sustainability",
        misconception_tags=["dismisses_social_grants_or_enterprise"],
        marks=3,
    )


def arch_50_integrated_anti_poverty_strategy_synthesis(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    urban_area = rng.choice(URBAN_AREAS)
    budget_bn = rng.randint(25, 65)
    prompt = (
        f"National Treasury sets aside R{budget_bn} billion for an integrated anti-poverty strategy spanning rural "
        f"{rural_area} and urban townships near {urban_area}.\n\n"
        f"Design a FOUR-pillar response explaining how (1) quality education, (2) accredited skills training, "
        f"(3) sustainable job creation, and (4) basic municipal infrastructure reinforce one another."
    )
    return _typed(
        rng,
        subskill="50_integrated_anti_poverty_strategy_synthesis",
        title="Integrated Four-Pillar Anti-Poverty Strategy",
        prompt=prompt,
        sample_answer=(
            f"1. Quality education builds strong literacy, maths, and science foundations for learners in {rural_area} and {urban_area}.\n"
            "2. Accredited skills training (learnerships/SETAs) converts school leavers into scarce-skill technicians and managers.\n"
            "3. Sustainable jobs in viable private firms and EPWP transition programmes provide steady, secure household incomes.\n"
            f"4. Clean water, electricity, clinics, and transport from the R{budget_bn}B budget protect health and connect workers to markets."
        ),
        marking_points=[
            "Pillar 1 — Quality education builds foundational literacy and numeracy [1]",
            "Pillar 2 — Accredited skills training bridges school to scarce technical/business roles [1]",
            "Pillar 3 — Sustainable private and public jobs generate durable wages above the poverty line [1]",
            "Pillar 4 — Water, power, health, and transport infrastructure safeguard health and market access [1]",
        ],
        hints={
            "tier_1": "Address every one of the four numbered pillars explicitly.",
            "tier_2": "Explain what each pillar contributes AND how it supports the next pillar.",
            "tier_3": "Write four clear points linking schooling -> accredited skills -> sustainable jobs -> water/power/transport infrastructure.",
        },
        learning_objective_id="lo_ineq_integrated_strategy",
        concept_id="integrated_anti_poverty_strategy",
        misconception_tags=["omits_one_or_more_pillars"],
        marks=4,
    )


BUILDERS_26_50 = {
    "26_urban_vs_rural_service_access_bar_graph": arch_26_urban_vs_rural_service_access_bar_graph,
    "27_rural_poverty_intervention_strategies": arch_27_rural_poverty_intervention_strategies,
    "28_empowering_rural_women_and_youth": arch_28_empowering_rural_women_and_youth,
    "29_urban_poverty_intervention_strategies": arch_29_urban_poverty_intervention_strategies,
    "30_sustainable_job_definition_and_meaning": arch_30_sustainable_job_definition_and_meaning,
    "31_job_longevity_and_security_for_poverty_reduction": arch_31_job_longevity_and_security_for_poverty_reduction,
    "32_job_security_impact_on_worker_motivation": arch_32_job_security_impact_on_worker_motivation,
    "33_business_sustainability_and_job_stability": arch_33_business_sustainability_and_job_stability,
    "34_epwp_purpose_and_2004_launch": arch_34_epwp_purpose_and_2004_launch,
    "35_epwp_stipend_and_payroll_budget_table": arch_35_epwp_stipend_and_payroll_budget_table,
    "36_working_for_water_programme": arch_36_working_for_water_programme,
    "37_epwp_roads_healthcare_and_ecd_jobs": arch_37_epwp_roads_healthcare_and_ecd_jobs,
    "38_epwp_sector_job_distribution_bar_graph": arch_38_epwp_sector_job_distribution_bar_graph,
    "39_un_millennium_development_goals_overview": arch_39_un_millennium_development_goals_overview,
    "40_private_urban_vs_public_rural_healthcare": arch_40_private_urban_vs_public_rural_healthcare,
    "41_poor_quality_education_summary_table": arch_41_poor_quality_education_summary_table,
    "42_progressive_tax_and_social_grant_budget_table": arch_42_progressive_tax_and_social_grant_budget_table,
    "43_rural_vs_urban_monthly_income_gap_bar_graph": arch_43_rural_vs_urban_monthly_income_gap_bar_graph,
    "44_skills_shortage_sector_impact_schedule": arch_44_skills_shortage_sector_impact_schedule,
    "45_epwp_worker_skills_transfer_calculation": arch_45_epwp_worker_skills_transfer_calculation,
    "46_environmental_sustainability_and_poverty_link": arch_46_environmental_sustainability_and_poverty_link,
    "47_fiscal_redistribution_tax_to_grant_flow_diagram": arch_47_fiscal_redistribution_tax_to_grant_flow_diagram,
    "48_legislation_reforms_matching_matrix": arch_48_legislation_reforms_matching_matrix,
    "49_small_business_vs_grant_dependency_sustainability": arch_49_small_business_vs_grant_dependency_sustainability,
    "50_integrated_anti_poverty_strategy_synthesis": arch_50_integrated_anti_poverty_strategy_synthesis,
}
