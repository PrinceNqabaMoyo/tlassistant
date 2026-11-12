"""
Grade 7 EMS — Term 1: Businesses — Semantic Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md
and curriculum_docs/EMS_Gr7/Term 1/4-Businesses.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term1_businesses_archetypes_01_25 import (
    _escape,
    _fmt_rand,
    _mcq,
    _pick_person,
    _pick_place,
    _pick_two_people,
    _q,
    _svg_bars,
    _svg_three_boxes,
    _svg_wrap,
    _table_q,
)


# ---------------------------------------------------------------------------
# Archetypes 26 – 50
# ---------------------------------------------------------------------------

def _b26(rng: random.Random) -> Dict[str, Any]:
    region_workers = rng.choice([100000, 150000, 200000, 250000])
    agri_workers = (region_workers * 8) // 100
    diag = _svg_bars(
        f"SA Agriculture Economic Shares (Sample Workforce: {region_workers})",
        [
            ("Agro-Industrial Share of GDP (%)", 12, "#16a34a"),
            ("Formal Jobs in Agriculture (%)", 8, "#0284c7"),
            ("Direct Primary Farm GDP (%)", 3, "#ca8a04"),
        ],
        unit_prefix="",
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the agricultural contribution diagram noting that although primary farming accounts for roughly "
        f"2,5%–3% of direct GDP, the wider agro-industrial sector contributes 12% of GDP and 8% of South Africa's formal jobs. "
        f"In a province with {region_workers} formal workers, calculate how many formal jobs depend on agriculture (8%)."
    )
    worked = (
        f"1. **Job share [1]:** 8% of {region_workers} formal workers.\n"
        f"2. **Calculation [1]:** (8 / 100) x {region_workers} = **{agri_workers} formal jobs** (highlighting why farm droughts threaten wide employment)."
    )
    return _q(
        rng,
        "26_sa_agriculture_gdp_employment_data",
        prompt,
        f"{agri_workers} jobs",
        worked,
        "South African agriculture anchors much larger agro-industrial manufacturing and formal employment than direct farm GDP alone suggests.",
        {
            "tier_1": "Use the 8% formal jobs share shown in the diagram.",
            "tier_2": f"Calculate 8% of {region_workers}.",
            "tier_3": f"Compute (8 / 100) x {region_workers} = {agri_workers} jobs.",
        },
        ["uses_12_percent_agro_gdp_instead_of_8_percent_employment"],
        [
            {"criterion": f"Selects 8% formal employment share for {region_workers}", "marks": 1},
            {"criterion": f"Calculates {agri_workers} formal jobs", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b27(rng: random.Random) -> Dict[str, Any]:
    decade = rng.choice(["early 1990s regional maize droughts", "dry El Nino summer maize harvests"])
    prompt = (
        f"Historical South African EMS studies highlight how {decade} devastated summer-rainfall maize harvests across "
        f"southern Africa, whereas the Western Cape's wheat sector continued supplying grain. Explain why regional climate "
        f"diversity helped stabilise South African and SADC food supplies."
    )
    sample = (
        f"South Africa spans both summer-rainfall maize zones (vulnerable during {decade}) and a distinct winter-rainfall "
        f"Mediterranean zone in the Western Cape where reliable winter wheat could still be harvested and transported to "
        f"prevent severe regional famine across SADC neighbours."
    )
    worked = (
        f"1. **Summer vs winter rainfall contrast [1.5]:** Summer drought devastated northern/central maize belts, while Western Cape winter rains sustained wheat harvests.\n"
        f"2. **SADC food stability [1.5]:** Surplus commercial grain helped supply neighbouring Southern African countries during shortages."
    )
    return _q(
        rng,
        "27_drought_maize_1990s_vs_western_cape",
        prompt,
        sample,
        worked,
        "Different seasonal rainfall zones buffered national food security when severe droughts struck summer grain regions.",
        {
            "tier_1": "Think about WHEN rain falls in inland maize areas versus the Western Cape.",
            "tier_2": "Contrast summer-rainfall maize vulnerability against winter-rainfall wheat stability.",
            "tier_3": "Explain that winter wheat in the Western Cape buffered grain supplies for SA and SADC neighbours.",
        },
        ["thinks_all_south_african_provinces_share_identical_rain_seasons"],
        [
            {"criterion": "Contrasts summer-rainfall maize drought against Western Cape winter rainfall", "marks": 1},
            {"criterion": "Explains food-security buffer for South Africa and SADC", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b28(rng: random.Random) -> Dict[str, Any]:
    farmer = _pick_person(rng)
    normal_t = rng.choice([120, 150, 180])
    drought_t = rng.choice([50, 70, 90])
    price_per_t = rng.choice([3000, 3500, 4000])
    loss_t = normal_t - drought_t
    loss_r = loss_t * price_per_t
    prompt = (
        f"Severe drought cuts {farmer}'s annual maize harvest from {normal_t} tonnes down to {drought_t} tonnes. "
        f"If maize trades at {_fmt_rand(price_per_t)} per tonne, calculate the total Rand farm revenue lost due to drought."
    )
    worked = (
        f"1. **Lost harvest tonnage [1]:** {normal_t} - {drought_t} = {loss_t} tonnes.\n"
        f"2. **Lost Rand revenue [1]:** {loss_t} tonnes x {_fmt_rand(price_per_t)} = **{_fmt_rand(loss_r)}**."
    )
    return _q(
        rng,
        "28_drought_crop_revenue_loss_calculation",
        prompt,
        _fmt_rand(loss_r),
        worked,
        "Droughts cut farm output sharply, slashing revenue needed to repay loans and retain farm workers.",
        {
            "tier_1": "Subtract drought tonnage from normal tonnage first.",
            "tier_2": f"Multiply lost tonnes by {_fmt_rand(price_per_t)}/tonne.",
            "tier_3": f"Compute ({normal_t} - {drought_t}) x {price_per_t} = {_fmt_rand(loss_r)}.",
        },
        ["multiplies_drought_tonnage_instead_of_lost_tonnage"],
        [
            {"criterion": f"Lost tonnage = {loss_t} tonnes", "marks": 1},
            {"criterion": f"Lost Rand revenue = {_fmt_rand(loss_r)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b29(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    formal_name, informal_name = _pick_two_people(rng)
    prompt = (
        f"After flash floods strike {town}, both {formal_name}'s insured formal supermarket and {informal_name}'s uninsured "
        f"street vegetable stall lose stock. Explain TWO reasons why {formal_name}'s formal supermarket usually recovers "
        f"faster than {informal_name}'s informal stall."
    )
    sample = (
        f"(1) {formal_name}'s registered business holds commercial insurance and cash/bank credit facilities to rebuild stock quickly, "
        f"whereas {informal_name} lacks insurance and bank loans; (2) {formal_name} operates from durable brick premises with supplier "
        f"credit contracts, while {informal_name}'s family cash reserve is wiped out immediately."
    )
    worked = (
        f"1. **Insurance & bank credit [1.5]:** Formal insurance payouts and bank overdrafts help {formal_name} restock; {informal_name} absorbs 100% of cash loss personally.\n"
        f"2. **Resilient premises & supplier credit [1.5]:** Formal brick stores and wholesale credit terms speed recovery compared with uninsured street stalls in {town}."
    )
    return _q(
        rng,
        "29_formal_vs_informal_disaster_recovery",
        prompt,
        sample,
        worked,
        "Access to insurance, bank bridge finance, and supplier credit determines disaster resilience across the formal/informal divide.",
        {
            "tier_1": "Think of financial safety nets like short-term insurance, bank overdrafts, and wholesale supplier credit.",
            "tier_2": f"Contrast {formal_name}'s insured formal firm against {informal_name}'s cash-only street stall.",
            "tier_3": "State formal insurance/bank credit access and supplier terms/stronger premises versus uninsured total cash loss.",
        },
        ["thinks_informal_traders_always_receive_commercial_insurance_payouts"],
        [
            {"criterion": "Explains formal insurance / bank finance vs zero informal cover", "marks": 1},
            {"criterion": "Explains stronger premises / supplier credit / financial reserves", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b30(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"In EMS studies of businesses in {town}, which two widespread health epidemics are specifically examined for their "
        f"long-term socio-economic impact on South African workplaces and households?"
    )
    return _mcq(
        rng,
        "30_health_epidemics_hiv_tb_definition",
        prompt,
        "HIV/Aids and Tuberculosis (TB)",
        ["Temporary mild sunburn and tooth decay", "Seasonal pollen hay-fever and hiccups", "Broken wrists from weekend soccer"],
        "Grade 7 EMS specifically examines HIV/Aids and Tuberculosis (TB) as serious South African health epidemics lowering workplace productivity, raising medical costs, and reducing household spending.",
        {
            "tier_1": "Think of the major infectious and chronic epidemics documented across South African communities.",
            "tier_2": "Eliminate minor temporary injuries or mild allergies.",
            "tier_3": "Select 'HIV/Aids and Tuberculosis (TB)'.",
        },
        ["trivialises_major_socioeconomic_health_epidemics"],
    )


def _b31(rng: random.Random) -> Dict[str, Any]:
    firm = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Severe illness from an epidemic spreads among employees at {firm}'s clothing factory in {town}. "
        f"Explain THREE negative operational impacts this health epidemic has on {firm}'s business."
    )
    sample = (
        f"(1) Increased worker absenteeism lowers daily output and misses client delivery deadlines; "
        f"(2) loss of experienced skilled workers through chronic illness or death forces {firm} to spend money recruiting "
        f"and retraining replacements; and (3) rising sick-leave, medical, and insurance costs squeeze profits."
    )
    worked = (
        f"1. **Absenteeism & lower productivity [1]:** Ill workers (or staff caring for sick relatives) miss shifts, cutting output.\n"
        f"2. **Loss of skills & retraining cost [1]:** Replacing experienced machinists/supervisors slows production in {town}.\n"
        f"3. **Higher workplace costs [1]:** Overtime pay, temporary cover, and employee medical support raise expenses."
    )
    return _q(
        rng,
        "31_epidemics_productivity_absenteeism",
        prompt,
        sample,
        worked,
        "Health epidemics undermine labour supply, institutional skill memory, and operating margins simultaneously.",
        {
            "tier_1": "Think about attendance, experienced skills, and extra money spent replacing/supporting sick workers.",
            "tier_2": "Connect missing shifts -> lost production, lost skills -> retraining cost, sick leave -> higher expenses.",
            "tier_3": "Explain higher absenteeism, skill loss/retraining expenses, and higher payroll/medical operating costs.",
        },
        ["misses_training_and_skill_loss_costs"],
        [
            {"criterion": "Higher absenteeism / lower output and productivity", "marks": 1},
            {"criterion": "Loss of skilled staff and high recruitment/training costs", "marks": 1},
            {"criterion": "Higher sick-leave, overtime, or medical benefit expenses", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b32(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    shop = rng.choice(["a local furniture and appliance retailer", "a community clothing and stationery store"])
    prompt = (
        f"During a severe epidemic in {town}, breadwinners fall ill and households redirect scarce money toward clinics, "
        f"medicine, and funerals. Explain how this shift in household spending affects {shop} nearby."
    )
    sample = (
        f"As households spend larger shares of scarce income on medicine, care, and funerals — while earning lower wages due to illness — "
        f"demand for non-urgent goods from {shop} drops sharply, lowering sales, forcing discounts or staff layoffs, and threatening closure."
    )
    worked = (
        f"1. **Spending diversion [1.5]:** Families cut back non-medical purchases ({shop}) to afford healthcare and family support.\n"
        f"2. **Business revenue contraction [1.5]:** Falling household income plus lower retail demand shrink store sales and threaten jobs in {town}."
    )
    return _q(
        rng,
        "32_epidemics_household_demand_shift",
        prompt,
        sample,
        worked,
        "Epidemics hit businesses on the demand side as sick households reallocate shrinking incomes toward urgent medical survival.",
        {
            "tier_1": "Consider both sides of the wallet: less earned wage AND urgent medical expenses.",
            "tier_2": f"Ask what happens to sales at {shop} when neighbours spend every spare Rand on clinics and funerals.",
            "tier_3": "Explain spending diversion to healthcare and lower household earnings shrinking retail store revenue.",
        },
        ["thinks_epidemics_only_affect_sick_staff_never_customer_sales"],
        [
            {"criterion": "Explains household budget diversion to medicine/care/funerals", "marks": 1},
            {"criterion": f"Explains falling customer sales and profit pressure at {shop}", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b33(rng: random.Random) -> Dict[str, Any]:
    manager = _pick_person(rng)
    absent = rng.randint(4, 9)
    days = rng.choice([3, 4, 5])
    units_per_shift = rng.choice([20, 25, 30])
    unit_val = rng.choice([40, 50, 60])
    lost_units = absent * days * units_per_shift
    lost_r = lost_units * unit_val
    prompt = (
        f"During a seasonal flu and TB wave at {manager}'s workshop, {absent} skilled workers each miss {days} shifts. "
        f"Each worker normally produces {units_per_shift} units per shift worth {_fmt_rand(unit_val)} each. "
        f"Calculate the total Rand value of production lost during this period."
    )
    worked = (
        f"1. **Lost shifts [1]:** {absent} workers x {days} days = {absent * days} missed shifts.\n"
        f"2. **Lost units [1]:** {absent * days} x {units_per_shift} = {lost_units} units.\n"
        f"3. **Lost Rand value [1]:** {lost_units} x {_fmt_rand(unit_val)} = **{_fmt_rand(lost_r)}**."
    )
    return _q(
        rng,
        "33_absenteeism_cost_calculation",
        prompt,
        _fmt_rand(lost_r),
        worked,
        "High employee absenteeism rapidly multiplies into steep lost physical production and revenue losses.",
        {
            "tier_1": "Compute total missed worker-shifts first (absent workers x days missed).",
            "tier_2": f"Multiply missed shifts by {units_per_shift} units/shift, then multiply by {_fmt_rand(unit_val)}.",
            "tier_3": f"Compute {absent} x {days} x {units_per_shift} x {unit_val} = {_fmt_rand(lost_r)}.",
        },
        ["forgets_one_multiplier_in_chain"],
        [
            {"criterion": f"Missed shifts = {absent * days} and lost units = {lost_units}", "marks": 2},
            {"criterion": f"Lost Rand value = {_fmt_rand(lost_r)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b34(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    prompt = (
        f"Unlike salaried formal employees, {trader} operates an informal one-person fruit stall in {town}. "
        f"Explain TWO reasons why prolonged illness hits an informal sole trader harder than a salaried formal employee."
    )
    sample = (
        f"(1) Zero paid sick leave or UIF: whenever {trader} stays home sick or cares for family, the stall earns R0 daily income; "
        f"(2) zero employer medical aid forces out-of-pocket medical payments, draining working stock capital so {trader} may be unable to restock."
    )
    worked = (
        f"1. **Immediate total income stop [1.5]:** No paid sick leave or co-workers to run the stall — closed stall = zero earnings.\n"
        f"2. **Stock capital drained by medical costs [1.5]:** Without medical aid, {trader} uses daily trading cash for treatment, risking permanent stall collapse."
    )
    return _q(
        rng,
        "34_epidemics_affecting_informal_traders",
        prompt,
        sample,
        worked,
        "Lack of paid sick leave, medical aid, and backup staff leaves informal sole traders exposed to rapid poverty when illness strikes.",
        {
            "tier_1": "Ask what happens to daily cash income and next week's vegetable stock money when a solo vendor gets sick.",
            "tier_2": "Contrast paid sick leave + medical aid in formal employment against R0 earnings + out-of-pocket bills.",
            "tier_3": "Explain zero paid sick leave (R0 when closed) and lack of medical aid draining trading capital.",
        },
        ["assumes_informal_vendors_receive_paid_sick_leave"],
        [
            {"criterion": "Explains zero paid sick leave / R0 daily revenue when closed", "marks": 1},
            {"criterion": "Explains lack of medical aid draining trading stock capital", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b35(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each external shock experienced by businesses in {town} as either a **Natural Disaster Impact** or a "
        f"**Health Epidemic Impact**."
    )
    row_specs = [
        {"cells": ["River burst banks and ruined R80 000 of stored supermarket dry goods", None], "expected": ["Natural Disaster Impact"], "cell_hints": ["Flooding directly destroys physical inventory."]},
        {"cells": ["Chronic worker illness leaves four factory sewing lines unstaffed", None], "expected": ["Health Epidemic Impact"], "cell_hints": ["Widespread employee sickness causing absenteeism."]},
        {"cells": ["Earthquake cracks bridge roads, stopping delivery trucks for two weeks", None], "expected": ["Natural Disaster Impact"], "cell_hints": ["Geological shock breaking transport infrastructure."]},
        {"cells": ["Households divert grocery money toward clinic bills and funerals", None], "expected": ["Health Epidemic Impact"], "cell_hints": ["Widespread community illness reshaping spending priorities."]},
    ]
    return _table_q(
        rng,
        "35_disaster_vs_epidemic_impacts_table",
        prompt,
        ["Business Disruption", "Shock Category"],
        row_specs,
        "Natural disasters destroy physical infrastructure and inventory suddenly, whereas health epidemics erode workforce capacity and household spending power over time.",
        {
            "tier_1": "Separate physical weather/earth emergencies from community-wide illness disruptions.",
            "tier_2": "Flooded stock & broken bridges->Natural Disaster; unstaffed shifts & clinic-bill diversions->Health Epidemic.",
            "tier_3": "Fill in Natural Disaster Impact or Health Epidemic Impact.",
        },
        ["confuses_epidemic_absenteeism_with_natural_disasters"],
    )


def _b36(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Knowing that hailstorms and electrical surges occasionally strike {town}, {owner}'s formal hardware business "
        f"pays a monthly premium to transfer major physical asset risk. Which proactive tool is {owner} using?"
    )
    return _mcq(
        rng,
        "36_insurance_and_emergency_reserves",
        prompt,
        "Commercial property and stock insurance",
        ["Unregistered street bartering", "Zero emergency cash reserves", "Dropping all safety locks"],
        "Commercial short-term insurance protects registered businesses against catastrophic flood, fire, hail, or theft losses by paying compensation to rebuild.",
        {
            "tier_1": "Name the monthly financial contract where an insurer compensates a firm after fire, flood, or theft.",
            "tier_2": "Informal stalls typically cannot afford or qualify for this protection, whereas formal firms rely on it.",
            "tier_3": "Select 'Commercial property and stock insurance'.",
        },
        ["assumes_government_automatically_replaces_every_private_shop_free"],
    )


def _b37(rng: random.Random) -> Dict[str, Any]:
    founder = _pick_person(rng)
    biz = rng.choice(["mobile car-detailing company", "artisan leather sandal workshop", "corporate lunch caterer"])
    prompt = (
        f"{founder} wants to convert an informal {biz} into a registered **formal** South African business. "
        f"Which combination of official registrations is required?"
    )
    return _mcq(
        rng,
        "37_business_registration_steps_cipc",
        prompt,
        "Register the business entity (CIPC), register for taxes (SARS), and obtain municipal safety/trading permits",
        [
            "Only print colourful flyers without keeping books or paying taxes",
            "Barter three cattle at the nearest post office without paperwork",
            "Close the bank account and operate strictly with loose cash under a tree",
        ],
        "Formalising in South Africa requires legal entity registration (CIPC), tax/UIF registration with SARS, and compliance with municipal health/zoning bylaws.",
        {
            "tier_1": "Think of the three levels of formal compliance: company register, national tax authority, and local municipal permits.",
            "tier_2": "Eliminate options avoiding tax registration, accounting records, or bank accounts.",
            "tier_3": "Select the option combining CIPC, SARS, and municipal trading/safety permits.",
        },
        ["thinks_social_media_page_alone_makes_a_business_formal"],
    )


def _b38(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    city = _pick_place(rng, rural=False)
    prompt = (
        f"{owner} runs a successful informal catering business in {city} and has been invited to tender for daily office lunches "
        f"at a large local hospital — provided {owner} formalises first. Advise {owner} on TWO major **benefits** of "
        f"formalising and TWO new **responsibilities** {owner} must prepare for."
    )
    sample = (
        f"Benefits: (1) Eligibility to win large formal contracts/tenders (like the hospital in {city}) and (2) access to "
        f"commercial bank credit/insurance to expand kitchen capacity. "
        f"Responsibilities: (1) Keeping formal accounting records and paying SARS taxes, and (2) complying with strict HACCP food hygiene, municipal licences, and labour contracts."
    )
    worked = (
        f"1. **Two benefits [2]:** (a) Qualification for high-value corporate/public tenders; (b) Access to bank expansion loans and insurance.\n"
        f"2. **Two responsibilities [2]:** (a) Formal bookkeeping and SARS tax filing; (b) HACCP hygiene inspections, municipal permits, and formal staff compliance."
    )
    return _q(
        rng,
        "38_transition_informal_to_formal_case",
        prompt,
        sample,
        worked,
        "Transitioning from informal to formal status unlocks institutional buyers and credit while demanding tax, accounting, and safety compliance.",
        {
            "tier_1": "Balance both sides clearly: two opportunities unlocked vs two legal/cost duties added.",
            "tier_2": f"Think of why the hospital contract in {city} requires formal status (hygiene + tax clearance).",
            "tier_3": "State tenders + bank loans/insurance as benefits; SARS bookkeeping + HACCP/labour compliance as duties.",
        },
        ["lists_only_benefits_ignoring_tax_and_hygiene_duties"],
        [
            {"criterion": "Benefit 1 & 2: Tender eligibility and bank credit/insurance access", "marks": 2},
            {"criterion": "Responsibility 1 & 2: Bookkeeping/SARS tax and HACCP/labour compliance", "marks": 2},
        ],
        cognitive_level="Problem Solving",
        marks=4,
    )


def _b39(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    formal_jobs = rng.choice([25, 35, 45])
    informal_jobs = rng.choice([75, 65, 55])
    total = formal_jobs + informal_jobs
    inf_pct = round(100 * informal_jobs / total)
    diag = _svg_bars(
        f"Local Employment Survey — {town} ({total} Jobs)",
        [
            ("Formal Registered Firms", formal_jobs, "#2563eb"),
            ("Informal Micro-Enterprises", informal_jobs, "#d97706"),
        ],
        unit_prefix="",
        unit_suffix=" jobs",
    )
    prompt = (
        f"Refer to the employment survey diagram for {town} counting {formal_jobs} formal jobs and {informal_jobs} informal jobs "
        f"(total {total} working residents). Calculate what percentage of surveyed workers depend on **informal micro-enterprises**, "
        f"and explain why municipalities should support safe trading stalls for them."
    )
    worked = (
        f"1. **Informal percentage [1]:** ({informal_jobs} / {total}) x 100 = **{inf_pct}%**.\n"
        f"2. **Municipal support reason [2]:** Supporting the majority {inf_pct}% workforce with sheltered stalls, clean water, and waste bins reduces poverty, keeps streets hygienic, and nurtures future formal businesses."
    )
    return _q(
        rng,
        "39_small_business_employment_creation",
        prompt,
        f"{inf_pct}%",
        worked,
        "Supporting informal traders with clean stalls, water, and training boosts local household income and public hygiene simultaneously.",
        {
            "tier_1": "Divide informal jobs by total jobs and multiply by 100, then explain the community case for safe stalls.",
            "tier_2": f"Compute ({informal_jobs} / {total}) x 100 and relate to hygiene, shelter, and livelihoods in {town}.",
            "tier_3": f"State {inf_pct}% and explain poverty reduction, cleaner markets, and stepping-stone enterprise growth.",
        },
        ["calculates_formal_percentage_instead_of_informal_percentage"],
        [
            {"criterion": f"Calculates informal share = {inf_pct}%", "marks": 1},
            {"criterion": "Explains economic/hygiene case for safe municipal trading support", "marks": 2},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b40(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    vendor = _pick_person(rng)
    prompt = (
        f"Health inspectors visit both licensed sit-down restaurants and busy street-food stalls run by {vendor} in {town}. "
        f"State TWO specific food-hygiene practices all food businesses must follow and explain how failing these practices "
        f"harms both consumers and the business."
    )
    sample = (
        "Hygiene practices: (1) keeping perishable meat/dairy cold at safe temperatures and (2) washing hands/utensils with clean "
        "running water while storing food away from pests. Failing these causes food poisoning among customers, destroys customer "
        "reputation, and triggers health-inspector closures or fines."
    )
    worked = (
        "1. **Two hygiene rules [2]:** Clean water & utensil sanitising, cold-chain refrigeration, pest control, or separated raw/cooked prep (any two).\n"
        f"2. **Consequences of failure [1]:** Customer illness/food poisoning plus lost trust, fines, or forced closure for {vendor} in {town}."
    )
    return _q(
        rng,
        "40_consumer_protection_unsafe_food",
        prompt,
        sample,
        worked,
        "Food safety rules protect consumers from illness and safeguard businesses against reputation collapse and shutdown.",
        {
            "tier_1": "Think about temperature control, clean water, and protecting food from flies/dust.",
            "tier_2": "Include one harm to the consumer (illness) and one harm to the stall/restaurant (lost buyers/closure).",
            "tier_3": "State two concrete food hygiene rules plus customer food poisoning and business closure/reputation loss.",
        },
        ["thinks_street_food_sellers_do_not_need_clean_water_or_cold_storage"],
        [
            {"criterion": "Hygiene rule 1 & 2 (cold chain, clean water, pest/contamination control)", "marks": 2},
            {"criterion": "Consumer illness + business shutdown/reputation loss", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b41(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    hours = rng.choice([4, 5, 6])
    litres_hr = 2
    fuel_price = rng.choice([22, 24, 25])
    days = 20
    total_fuel_r = hours * litres_hr * fuel_price * days
    prompt = (
        f"Power disruptions force {owner}'s small bakery to run a backup diesel generator for {hours} hours per day over "
        f"{days} trading days this month. The generator burns {litres_hr} litres of fuel per hour at {_fmt_rand(fuel_price)}/litre. "
        f"Calculate the extra Rand fuel expense {owner} must pay this month."
    )
    daily_l = hours * litres_hr
    daily_cost = daily_l * fuel_price
    worked = (
        f"1. **Fuel used per day [1]:** {hours} hrs x {litres_hr} L/hr = {daily_l} L/day.\n"
        f"2. **Daily fuel cost [1]:** {daily_l} L x {_fmt_rand(fuel_price)} = {_fmt_rand(daily_cost)}/day.\n"
        f"3. **20-day monthly cost [1]:** {_fmt_rand(daily_cost)} x {days} = **{_fmt_rand(total_fuel_r)}**."
    )
    return _q(
        rng,
        "41_loadshedding_infrastructure_shock_cost",
        prompt,
        _fmt_rand(total_fuel_r),
        worked,
        "Utility breakdowns force small formal and informal businesses into steep backup energy expenses that squeeze net profits.",
        {
            "tier_1": "Find litres burned per day first, then cost per day, then multiply by 20 days.",
            "tier_2": f"Compute {hours} x {litres_hr} x {fuel_price} x {days}.",
            "tier_3": f"Calculate {_fmt_rand(daily_cost)} x {days} = {_fmt_rand(total_fuel_r)}.",
        },
        ["forgets_litres_per_hour_or_trading_days"],
        [
            {"criterion": f"Daily fuel usage = {daily_l} L", "marks": 1},
            {"criterion": f"Daily fuel cost = {_fmt_rand(daily_cost)}", "marks": 1},
            {"criterion": f"Monthly fuel expense = {_fmt_rand(total_fuel_r)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b42(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Compare typical customer features in {town} by matching each feature to **Formal Supermarket** or "
        f"**Informal Spaza / Hawker**."
    )
    row_specs = [
        {"cells": ["Accepts bank cards, loyalty apps, and issues printed VAT receipts", None], "expected": ["Formal Supermarket"], "cell_hints": ["Uses formal banking terminals and SARS VAT systems."]},
        {"cells": ["Sells single unwrapped biscuits, one candle, or tiny daily packs on cash", None], "expected": ["Informal Spaza / Hawker"], "cell_hints": ["Breaks bulk into tiny affordable units for daily cash earners."]},
        {"cells": ["Files audited annual financial statements and registered PAYE payroll", None], "expected": ["Formal Supermarket"], "cell_hints": ["Large registered employer under statutory tax rules."]},
        {"cells": ["Sets up right beside morning commuter queues with zero lease lock-in", None], "expected": ["Informal Spaza / Hawker"], "cell_hints": ["Highly mobile and close to commuter foot traffic."]},
    ]
    return _table_q(
        rng,
        "42_informal_tuckshop_vs_formal_supermarket",
        prompt,
        ["Operating Feature", "Business Format"],
        row_specs,
        "Formal supermarkets offer scale, digital payments, and VAT compliance, whereas informal spaza stalls excel at proximity and tiny affordable daily portions.",
        {
            "tier_1": "Look for VAT receipts & card machines vs broken-bulk single units & taxi-rank mobility.",
            "tier_2": "VAT/PAYE belong to Formal Supermarket; single loose items and commuter stalls belong to Informal Spaza / Hawker.",
            "tier_3": "Fill in Formal Supermarket or Informal Spaza / Hawker.",
        },
        ["confuses_informal_broken_bulk_convenience_with_formal_supermarkets"],
    )


def _b43(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    raw_r = rng.choice([2000, 2600, 3200])
    sales_r = rng.choice([4800, 5800, 6800])
    margin = sales_r - raw_r
    diag = _svg_three_boxes(
        f"{owner}'s Timber Workshop Flow",
        [
            ("Inputs Bought", "Pine planks, glue, labour", f"Cost: {_fmt_rand(raw_r)}"),
            ("Transformation", "Cutting, sanding, assembly", "Workshop value-add"),
            ("Consumer Outputs", "Sturdy study tables sold", f"Sales: {_fmt_rand(sales_r)}"),
        ],
    )
    prompt = (
        f"Refer to the workshop flow diagram for {owner}'s business spending {_fmt_rand(raw_r)} on inputs and selling tables "
        f"for {_fmt_rand(sales_r)}. Define **inputs**, **transformation process**, and **outputs**, and calculate the "
        f"Rand value added ({_fmt_rand(sales_r)} minus {_fmt_rand(raw_r)})."
    )
    sample = (
        f"Inputs are the productive resources bought ({_fmt_rand(raw_r)}: pine planks, glue, labour). "
        f"Transformation is the workshop cutting, sanding, and assembly that adds value. "
        f"Outputs are the finished sturdy tables sold to consumers for {_fmt_rand(sales_r)}. "
        f"Value added = {_fmt_rand(sales_r)} - {_fmt_rand(raw_r)} = **{_fmt_rand(margin)}**."
    )
    worked = (
        f"1. **Inputs / Transformation / Outputs [3]:** Resources bought ({_fmt_rand(raw_r)}) -> physical woodworking conversion -> finished tables sold ({_fmt_rand(sales_r)}).\n"
        f"2. **Value added [1]:** {_fmt_rand(sales_r)} - {_fmt_rand(raw_r)} = **{_fmt_rand(margin)}**."
    )
    return _q(
        rng,
        "43_primary_secondary_tertiary_business_flow",
        prompt,
        sample,
        worked,
        "Every enterprise takes productive inputs, transforms them efficiently, and delivers higher-value outputs to buyers.",
        {
            "tier_1": "Read all three boxes left to right, then subtract the left box cost from the right box sales.",
            "tier_2": f"Define inputs ({_fmt_rand(raw_r)}), transformation, and outputs ({_fmt_rand(sales_r)}), plus the difference.",
            "tier_3": f"Compute {_fmt_rand(sales_r)} - {_fmt_rand(raw_r)} = {_fmt_rand(margin)} alongside the three definitions.",
        },
        ["confuses_gross_sales_with_value_added"],
        [
            {"criterion": "Correctly defines inputs, transformation, and outputs using diagram", "marks": 3},
            {"criterion": f"Calculates value added = {_fmt_rand(margin)}", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=4,
        diagram_spec=diag,
    )


def _b44(rng: random.Random) -> Dict[str, Any]:
    hawker = _pick_person(rng)
    gross_sales = rng.choice([680, 740, 820])
    stock_cost = rng.choice([410, 440, 480])
    taxi_cost = rng.choice([50, 60, 70])
    net_profit = gross_sales - stock_cost - taxi_cost
    prompt = (
        f"An informal fresh-produce hawker, {hawker}, collects {_fmt_rand(gross_sales)} in cash sales today. "
        f"{hawker} spent {_fmt_rand(stock_cost)} at the morning market for stock and paid {_fmt_rand(taxi_cost)} in transport fares. "
        f"Calculate {hawker}'s net Rand profit for the day."
    )
    worked = (
        f"1. **Total daily expenses [1]:** {_fmt_rand(stock_cost)} + {_fmt_rand(taxi_cost)} = {_fmt_rand(stock_cost + taxi_cost)}.\n"
        f"2. **Net daily profit [1]:** {_fmt_rand(gross_sales)} - {_fmt_rand(stock_cost + taxi_cost)} = **{_fmt_rand(net_profit)}**."
    )
    return _q(
        rng,
        "44_profit_margin_informal_hawker",
        prompt,
        _fmt_rand(net_profit),
        worked,
        "Informal hawkers must deduct transport and market stall fees alongside stock purchases to know true daily earnings.",
        {
            "tier_1": "Add both expenses (stock + taxi fare) before subtracting from cash sales.",
            "tier_2": f"Subtract ({_fmt_rand(stock_cost)} + {_fmt_rand(taxi_cost)}) from {_fmt_rand(gross_sales)}.",
            "tier_3": f"Compute {_fmt_rand(gross_sales)} - {_fmt_rand(stock_cost + taxi_cost)} = {_fmt_rand(net_profit)}.",
        },
        ["forgets_to_deduct_taxi_transport_fare"],
        [
            {"criterion": f"Total expenses = {_fmt_rand(stock_cost + taxi_cost)}", "marks": 1},
            {"criterion": f"Net profit = {_fmt_rand(net_profit)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b45(rng: random.Random) -> Dict[str, Any]:
    worker = _pick_person(rng)
    prompt = (
        f"{worker} compares working at a registered formal factory against operating an independent informal stall. "
        f"Which employment protection applies specifically to workers in registered **formal** businesses?"
    )
    return _mcq(
        rng,
        "45_fixed_vs_working_hours_flexibility",
        prompt,
        "Statutory UIF cover, minimum wage protection, written contracts, and paid annual/sick leave",
        [
            "Complete exemption from income tax and workplace safety laws",
            "Right to close the entire factory arbitrarily whenever sunny weather arrives",
            "Zero record of hours worked, wages paid, or pension deductions",
        ],
        "Formal registered employers must comply with South African labour laws providing written contracts, minimum wages, UIF unemployment protection, and statutory leave.",
        {
            "tier_1": "Look for legal worker protections enforced inside registered formal workplaces.",
            "tier_2": "Informal self-employed traders lack UIF and paid sick leave; registered firms must provide them.",
            "tier_3": "Select the option mentioning UIF, minimum wages, contracts, and paid leave.",
        },
        ["confuses_informal_flexibility_with_statutory_uif_rights"],
    )


def _b46(rng: random.Random) -> Dict[str, Any]:
    partner = rng.choice(["Botswana, Namibia, and Lesotho", "Zimbabwe, Mozambique, and Eswatini"])
    tonnes = rng.choice([250000, 400000, 550000])
    prompt = (
        f"During dry agricultural seasons, commercial South African farms export grain surpluses (for example over "
        f"{tonnes} tonnes across SADC routes into {partner}). Explain TWO economic reasons why strong South African "
        f"commercial farming matters to the wider SADC region."
    )
    sample = (
        f"(1) Cross-border food exports into {partner} prevent regional hunger and stabilise food prices when local rains fail; "
        f"(2) regional export earnings sustain commercial farming jobs, agro-processing factories, and cross-border freight businesses in South Africa."
    )
    worked = (
        f"1. **Regional food security [1.5]:** Commercial grain surpluses cushion {partner} against drought-induced shortages.\n"
        f"2. **Export income & SADC trade jobs [1.5]:** Sustains farm revenue, rail/road logistics, and regional manufacturing partnerships."
    )
    return _q(
        rng,
        "46_sadc_regional_agricultural_trade",
        prompt,
        sample,
        worked,
        "Productive South African agriculture anchors regional food security and cross-border trade across Southern Africa.",
        {
            "tier_1": "Consider both the importing SADC countries and South Africa's export farmers/truckers.",
            "tier_2": f"Think about nutrition stability in {partner} plus revenue/jobs for farms and transport.",
            "tier_3": "Explain regional food security during dry years and export income/jobs across farms and logistics.",
        },
        ["treats_sa_farming_as_isolated_from_sadc_neighbours"],
        [
            {"criterion": f"Explains SADC food security buffer in {partner}", "marks": 1},
            {"criterion": "Explains export earnings and agro-logistics jobs", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b47(rng: random.Random) -> Dict[str, Any]:
    firm = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        f"{firm}'s formal engineering workshop in {town} provides protective safety helmets, ventilated welding bays, "
        f"and fair regulated wages. Explain TWO long-term business benefits of maintaining ethical workplace safety and fair pay."
    )
    sample = (
        f"(1) Fewer workplace injuries, sick days, and compensation lawsuits save operating expenses and keep production steady; "
        f"(2) fair pay and safe conditions boost worker loyalty, productivity, and {firm}'s reputation with corporate clients."
    )
    worked = (
        f"1. **Lower accident & turnover disruption [1.5]:** Healthy, uninjured staff work consistently without costly shutdowns or legal claims.\n"
        f"2. **Higher morale & client reputation [1.5]:** Motivated employees deliver higher quality, attracting repeat formal contracts in {town}."
    )
    return _q(
        rng,
        "47_ethical_labour_and_safety_compliance",
        prompt,
        sample,
        worked,
        "Workplace safety and fair remuneration strengthen productivity, reduce injury losses, and enhance corporate credibility.",
        {
            "tier_1": "Ask how safety gear and fair wages save the owner money or win customers in the long run.",
            "tier_2": "Think of fewer accidents/absenteeism AND higher worker retention/reputation.",
            "tier_3": "State lower injury/legal disruption and stronger worker productivity + business reputation.",
        },
        ["assumes_safety_spending_only_reduces_company_profit"],
        [
            {"criterion": "Fewer injuries, absenteeism, or legal liability costs", "marks": 1},
            {"criterion": "Higher worker morale/retention and stronger corporate reputation", "marks": 2},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b48(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    prompt = (
        f"{owner} runs a neighbourhood pharmacy and clinic supply shop in {town} in a district facing occasional storms "
        f"and power/water cuts. Recommend THREE practical continuity measures {owner} can put in place beforehand to keep "
        f"essential medicines safe and serve customers during disruptions."
    )
    sample = (
        "(1) Maintain backup solar/battery or generator power for vaccine fridges and till systems; "
        "(2) store medicines on raised waterproof shelves alongside emergency rainwater/clean water tanks; and "
        "(3) keep emergency cash reserves, short-term stock insurance, and multiple backup wholesale suppliers."
    )
    worked = (
        "1. **Backup power & cold storage [1]:** Battery/solar/generator backup protects temperature-sensitive medicines.\n"
        "2. **Water & flood protection [1]:** Raised waterproof shelving plus emergency clean water tank storage.\n"
        "3. **Financial & supply resilience [1]:** Cash reserve, commercial insurance, and secondary delivery routes/suppliers."
    )
    return _q(
        rng,
        "48_disaster_continuity_planning_strategy",
        prompt,
        sample,
        worked,
        "Advance preparedness across backup utilities, physical protection, insurance, and supplier diversification minimises disaster downtime.",
        {
            "tier_1": "Think across three practical pillars: power for medicine fridges, water/flood protection, and money/suppliers.",
            "tier_2": f"Avoid vague advice — name concrete tools {owner} can install or arrange before a storm hits {town}.",
            "tier_3": "Recommend backup power, raised waterproof shelves / water tank, and insurance + backup suppliers.",
        },
        ["gives_reactive_advice_only_after_stock_is_already_ruined"],
        [
            {"criterion": "Backup electricity/cold-chain measure", "marks": 1},
            {"criterion": "Physical stock protection / water backup measure", "marks": 1},
            {"criterion": "Financial reserve, insurance, or backup supplier measure", "marks": 1},
        ],
        cognitive_level="Problem Solving",
        marks=3,
    )


def _b49(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Audit each external force affecting businesses in {town} into its exact environmental category: "
        f"**Formal Support Policy**, **Natural Disaster**, **Health Epidemic**, or **Market Competition**."
    )
    row_specs = [
        {"cells": ["BBBEE supplier-development grants training township caterers", None], "expected": ["Formal Support Policy"], "cell_hints": ["Deliberate policy bridging informal firms into formal corporate supply chains."]},
        {"cells": ["Prolonged regional drought slashing maize supply", None], "expected": ["Natural Disaster"], "cell_hints": ["Extreme uncontrollable weather shock hitting agricultural inputs."]},
        {"cells": ["Rising HIV/Aids and TB absenteeism straining workshop productivity", None], "expected": ["Health Epidemic"], "cell_hints": ["Widespread community illness reducing workforce availability."]},
        {"cells": ["Three new fast-food takeaways opening on the same taxi-rank corner", None], "expected": ["Market Competition"], "cell_hints": ["Rival businesses competing for the same local consumer spending."]},
    ]
    return _table_q(
        rng,
        "49_business_environment_audit_table",
        prompt,
        ["External Business Force", "Category"],
        row_specs,
        "Enterprises monitor policies (BBBEE), natural disasters, community health epidemics, and local market rivals to stay resilient.",
        {
            "tier_1": "Match government growth policy, climate hazard, worker disease impact, and commercial rivalry.",
            "tier_2": "BBBEE->Formal Support Policy, drought->Natural Disaster, HIV/TB->Health Epidemic, rival takeaways->Market Competition.",
            "tier_3": "Fill in the exact four category labels cleanly.",
        },
        ["confuses_market_competition_with_natural_disasters"],
    )


def _b50(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    learner = _pick_person(rng)
    prompt = (
        f"Write a structured Term 1 synthesis report for {learner} evaluating businesses in {town} across THREE headings: "
        f"(1) How **formal and informal** trading, manufacturing, and service businesses complement each other; "
        f"(2) Why businesses act as **both producers and consumers**; and "
        f"(3) How **natural disasters and health epidemics** threaten business survival and how firms build resilience."
    )
    sample = (
        f"1. **Formal & informal complementarity:** Formal firms supply bulk manufactured/utility goods, pay SARS taxes, and anchor "
        f"large jobs, while informal stalls create entry-level livelihoods and convenient broken-bulk access near commuters in {town}.\n"
        f"2. **Dual role:** Every firm buys raw inputs, utilities, and labour as a consumer, then sells goods/services as a producer.\n"
        f"3. **Shocks & resilience:** Floods/droughts ruin assets and transport while HIV/TB raise absenteeism and cut customer demand; "
        f"insurance, safety standards (HACCP), backup utilities, and formalisation strengthen survival."
    )
    worked = (
        f"1. **Formal vs informal roles [2]:** Scale, tax, and tender reach vs low-capital survival jobs and local convenience across trading/manufacturing/services.\n"
        f"2. **Producer & consumer cycle [1]:** Buying inputs/labour while supplying consumer goods/services.\n"
        f"3. **Disaster/epidemic shock & resilience [2]:** Stock/supply loss and productivity/demand drops mitigated by insurance, hygiene standards, reserves, and preparedness."
    )
    return _q(
        rng,
        "50_businesses_term_synthesis_evaluation",
        prompt,
        sample,
        worked,
        "South Africa's commercial ecosystem depends on resilient formal and informal firms navigating input/output chains and external shocks.",
        {
            "tier_1": "Organise your answer cleanly into the three numbered headings in the question.",
            "tier_2": "Include concrete SA examples across formal/informal sectors, dual consumer-producer roles, and disaster/epidemic resilience.",
            "tier_3": "Cover formal+informal complementarity, buying inputs vs selling outputs, and shocks (floods/droughts + HIV/TB) with resilience steps.",
        },
        ["omits_either_epidemics_or_formal_informal_roles"],
        [
            {"criterion": "Explains formal & informal complementarity across trading/manufacturing/services", "marks": 2},
            {"criterion": "Explains businesses as both producers and consumers", "marks": 1},
            {"criterion": "Evaluates disaster + epidemic impacts and practical resilience steps", "marks": 2},
        ],
        cognitive_level="Problem Solving",
        marks=5,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_sa_agriculture_gdp_employment_data": _b26,
    "27_drought_maize_1990s_vs_western_cape": _b27,
    "28_drought_crop_revenue_loss_calculation": _b28,
    "29_formal_vs_informal_disaster_recovery": _b29,
    "30_health_epidemics_hiv_tb_definition": _b30,
    "31_epidemics_productivity_absenteeism": _b31,
    "32_epidemics_household_demand_shift": _b32,
    "33_absenteeism_cost_calculation": _b33,
    "34_epidemics_affecting_informal_traders": _b34,
    "35_disaster_vs_epidemic_impacts_table": _b35,
    "36_insurance_and_emergency_reserves": _b36,
    "37_business_registration_steps_cipc": _b37,
    "38_transition_informal_to_formal_case": _b38,
    "39_small_business_employment_creation": _b39,
    "40_consumer_protection_unsafe_food": _b40,
    "41_loadshedding_infrastructure_shock_cost": _b41,
    "42_informal_tuckshop_vs_formal_supermarket": _b42,
    "43_primary_secondary_tertiary_business_flow": _b43,
    "44_profit_margin_informal_hawker": _b44,
    "45_fixed_vs_working_hours_flexibility": _b45,
    "46_sadc_regional_agricultural_trade": _b46,
    "47_ethical_labour_and_safety_compliance": _b47,
    "48_disaster_continuity_planning_strategy": _b48,
    "49_business_environment_audit_table": _b49,
    "50_businesses_term_synthesis_evaluation": _b50,
}
