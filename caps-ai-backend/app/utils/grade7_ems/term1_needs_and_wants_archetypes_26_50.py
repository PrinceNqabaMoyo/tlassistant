"""
Grade 7 EMS — Term 1: Needs and Wants — Semantic Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 1/02. Needs and Wants.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term1_needs_and_wants_archetypes_01_25 import (
    _escape,
    _fmt_rand,
    _mcq,
    _pick_person,
    _pick_place,
    _pick_two_people,
    _q,
    _svg_bars,
    _svg_wrap,
    _table_q,
)


def _svg_chain(title: str, nodes: List[tuple[str, str]]) -> Dict[str, Any]:
    parts: List[str] = []
    for idx, (head, sub) in enumerate(nodes):
        x = 22 + idx * 120
        parts.append(f'<rect x="{x}" y="54" width="110" height="76" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>')
        parts.append(f'<text x="{x + 55}" y="82" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#1e3a8a">{_escape(head)}</text>')
        parts.append(f'<text x="{x + 55}" y="106" text-anchor="middle" font-family="Arial, sans-serif" font-size="10.5" fill="#334155">{_escape(sub)}</text>')
        if idx < len(nodes) - 1:
            parts.append(f'<line x1="{x + 110}" y1="92" x2="{x + 120}" y2="92" stroke="#0f766e" stroke-width="2"/>')
    return _svg_wrap(640, 150, title, "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 26 – 50
# ---------------------------------------------------------------------------

def _b26(rng: random.Random) -> Dict[str, Any]:
    firm = _pick_place(rng, rural=False)
    prompt = (
        f"Businesses in {firm} pay an economic reward for each factor of production they hire. "
        f"Match each factor of production to its exact economic remuneration."
    )
    row_specs = [
        {"cells": ["Natural Resources (Land)", None], "expected": ["Rent"], "cell_hints": ["Return paid for the use of land, water, or mineral sites."]},
        {"cells": ["Labour", None], "expected": ["Wages / Salaries"], "cell_hints": ["Income earned by workers for physical or mental effort."]},
        {"cells": ["Capital", None], "expected": ["Interest"], "cell_hints": ["Return paid for borrowed or invested financial/physical capital."]},
        {"cells": ["Entrepreneurship", None], "expected": ["Profit"], "cell_hints": ["Surplus reward earned for taking business risk."]},
    ]
    return _table_q(
        rng,
        "26_factors_of_production_remuneration_table",
        prompt,
        ["Factor of Production", "Remuneration (Reward)"],
        row_specs,
        "Each factor earns its distinct income: Land -> Rent, Labour -> Wages/Salaries, Capital -> Interest, and Entrepreneurship -> Profit.",
        {
            "tier_1": "Link each productive input to the income word used in EMS.",
            "tier_2": "Workers earn wages, landowners receive rent, lenders earn interest, and entrepreneurs earn profit.",
            "tier_3": "Fill in Rent, Wages / Salaries, Interest, and Profit.",
        },
        ["swaps_interest_and_profit_remuneration"],
    )


def _b27(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    shop = rng.choice(["a fresh fruit and grain corner shop", "a local primary healthcare pharmacy", "a warm winter uniform tailor"])
    prompt = (
        f"In {town}, {owner} opens {shop} to satisfy local residents' everyday needs while earning a sustainable profit. "
        f"Explain TWO mutually beneficial outcomes when businesses meet genuine community needs."
    )
    sample = (
        f"(1) Community households gain reliable local access to essential goods ({shop}) without costly travel; "
        f"(2) {owner}'s business earns revenue to pay worker wages, buy local supplies, and stay sustainable."
    )
    worked = (
        f"1. **Benefit to households [1]:** Convenient access to needed goods/services in {town} saves transport cost and raises living standards.\n"
        f"2. **Benefit to owner & economy [2]:** Satisfying demand generates revenue and profit for {owner}, supporting jobs and local economic growth."
    )
    return _q(
        rng,
        "27_business_meets_community_needs",
        prompt,
        sample,
        worked,
        "Successful businesses align private profit motives with solving real needs in their surrounding community.",
        {
            "tier_1": "Consider both sides of the transaction: what residents gain and what the business gains.",
            "tier_2": f"Think about convenience/survival for {town} residents and income/jobs created by {owner}.",
            "tier_3": "Explain mutual gain: accessible essentials for families and sustainable income/employment for the business.",
        },
        ["assumes_business_profit_hurts_communities"],
        [
            {"criterion": f"Benefit to community households in {town}", "marks": 1},
            {"criterion": f"Benefit to {owner}'s business/local employment", "marks": 2},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b28(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    service = rng.choice(["free public clinics, streetlights, and community policing", "tarred residential roads, sanitation pipes, and public primary schools"])
    prompt = (
        f"Private companies seldom build {service} for poor households in {town} on their own. "
        f"Why must government step in to provide these essential community needs?"
    )
    return _mcq(
        rng,
        "28_government_public_goods_provision",
        prompt,
        "Public infrastructure has high upfront costs and serves low-income residents who cannot pay commercial profits",
        [
            "Businesses are legally barred from owning concrete mixers or water pipes",
            "Government prints unlimited free money so public buildings cost zero resources",
            "Municipal streetlights produce gold coins whenever switched on at night",
        ],
        "Public goods such as roads, clinics, sanitation, and policing benefit everyone non-exclusively and require tax funding rather than commercial profit margins.",
        {
            "tier_1": "Ask whether every resident in a community could afford private commercial fees for streetlights or public policing.",
            "tier_2": "Recall why tax-funded public provision guarantees universal access to essential infrastructure.",
            "tier_3": "Select the option explaining high infrastructure costs and universal access without profit barriers.",
        },
        ["assumes_private_firms_provide_all_public_roads_free"],
    )


def _b29(rng: random.Random) -> Dict[str, Any]:
    muni = _pick_place(rng, rural=True)
    water_m = rng.choice([18, 22, 26])
    clinic_m = rng.choice([12, 15, 19])
    monument_m = rng.choice([8, 10, 12])
    diag = _svg_bars(
        f"{muni} Municipal Draft Projects (R Million)",
        [
            ("Clean Water Pipeline", water_m, "#0284c7"),
            ("Community Health Clinic", clinic_m, "#16a34a"),
            ("Decorative Flag Plaza", monument_m, "#f59e0b"),
        ],
        unit_prefix="R",
        unit_suffix="m",
    )
    prompt = (
        f"Refer to the municipal allocation diagram for {muni}: Clean Water Pipeline (R{water_m}m), "
        f"Community Health Clinic (R{clinic_m}m), and Decorative Flag Plaza (R{monument_m}m). "
        f"If funds are severely scarce, justify which two projects should be approved first and explain why."
    )
    sample = (
        f"Approve the **Clean Water Pipeline** (R{water_m}m) and **Community Health Clinic** (R{clinic_m}m) first, "
        f"because safe drinking water and healthcare satisfy primary survival needs across {muni}, whereas the Decorative Flag Plaza "
        f"(R{monument_m}m) is a non-essential secondary want that must wait."
    )
    worked = (
        f"1. **Approved priority projects [2]:** Clean Water Pipeline (R{water_m}m) and Community Health Clinic (R{clinic_m}m).\n"
        f"2. **Economic justification [1]:** Scarce public tax money must satisfy urgent primary survival and health needs before decorative municipal wants (R{monument_m}m)."
    )
    return _q(
        rng,
        "29_municipal_service_delivery_priorities",
        prompt,
        sample,
        worked,
        "Municipal budgeting applies needs-over-wants prioritisation under resource scarcity.",
        {
            "tier_1": "Apply the rule: primary survival needs come before secondary or decorative desires.",
            "tier_2": "Identify which two projects in the diagram directly protect human health and survival.",
            "tier_3": f"Prioritise the Water Pipeline (R{water_m}m) and Clinic (R{clinic_m}m), deferring the Flag Plaza (R{monument_m}m).",
        },
        ["funds_cosmetic_projects_over_water_and_clinics"],
        [
            {"criterion": f"Selects Water Pipeline (R{water_m}m) and Health Clinic (R{clinic_m}m)", "marks": 2},
            {"criterion": "Justifies primary survival needs priority over non-essential plaza", "marks": 1},
        ],
        cognitive_level="Problem Solving",
        marks=3,
        diagram_spec=diag,
    )


def _b30(rng: random.Random) -> Dict[str, Any]:
    area = _pick_place(rng, rural=True)
    issue = rng.choice(["burst sewage pipes and uncollected rubbish", "dry taps and unlit potholes roads", "overcrowded classrooms and closed clinics"])
    prompt = (
        f"Residents of {area} face prolonged service delivery failures such as {issue}. "
        f"Analyse ONE health impact on families and ONE negative economic impact on local small businesses."
    )
    sample = (
        f"Health impact: {issue.capitalize()} increases disease outbreaks, contaminated drinking water, and stress for households. "
        f"Business impact: Shops suffer lost trading hours, damaged delivery vehicles, higher private security/generator costs, and reduced customer foot traffic."
    )
    worked = (
        f"1. **Family health/safety impact [1]:** Exposure to illness, sanitation hazards, or physical danger lowers household wellbeing and misses school/work days.\n"
        f"2. **Small business impact [2]:** Higher operating costs (repairs, water/power backups) and disrupted customer access reduce revenue and threaten jobs in {area}."
    )
    return _q(
        rng,
        "30_service_delivery_protests_causes",
        prompt,
        sample,
        worked,
        "Unmet municipal service delivery harms public health and raises operating costs across local enterprises.",
        {
            "tier_1": "Separate the personal household effect (health/safety) from the business effect (costs/customers).",
            "tier_2": f"Think about what happens to shop owners when {issue} persists for weeks.",
            "tier_3": "State one public health risk and one commercial impact such as higher costs or lost sales.",
        },
        ["ignores_economic_cost_to_local_enterprises"],
        [
            {"criterion": "Identifies clear health or safety impact on families", "marks": 1},
            {"criterion": "Explains negative cost or revenue impact on local small businesses", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b31(rng: random.Random) -> Dict[str, Any]:
    rural_town = _pick_place(rng, rural=True)
    city = _pick_place(rng, rural=False)
    prompt = (
        f"Compare typical urgent infrastructure needs in rural {rural_town} versus urban {city} by classifying each "
        f"need into **Rural Priority** or **Urban Metro Priority**."
    )
    row_specs = [
        {"cells": ["Community boreholes, solar clinics, and all-weather gravel feeder roads", None], "expected": ["Rural Priority"], "cell_hints": ["Essential where homes are dispersed far from city water mains."]},
        {"cells": ["High-capacity commuter trains and multi-lane storm-water drains", None], "expected": ["Urban Metro Priority"], "cell_hints": ["Needed where dense populations commute across paved city suburbs."]},
        {"cells": ["Rural agricultural irrigation dams and village mobile network towers", None], "expected": ["Rural Priority"], "cell_hints": ["Supports farming livelihoods and isolated settlements."]},
        {"cells": ["High-density municipal waste recycling hubs and traffic-light grids", None], "expected": ["Urban Metro Priority"], "cell_hints": ["Addresses crowded city streets and industrial waste volumes."]},
    ]
    return _table_q(
        rng,
        "31_rural_vs_urban_community_needs",
        prompt,
        ["Community Infrastructure Need", "Settlement Context"],
        row_specs,
        "Although primary survival needs remain identical, specific community infrastructure differs between dispersed rural areas and dense urban centres.",
        {
            "tier_1": "Match dispersed farming/village needs against dense city commuter/housing needs.",
            "tier_2": "Boreholes and irrigation suit rural settlements; commuter rail and city waste hubs suit dense metros.",
            "tier_3": "Use exact labels: 'Rural Priority' or 'Urban Metro Priority'.",
        },
        ["assumes_rural_and_urban_infrastructure_priorities_are_identical"],
    )


def _b32(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Free State maize belt", "KwaZulu-Natal sugar & vegetable valley", "Limpopo citrus orchards"])
    fertile_pct = rng.choice([12, 13, 14])
    yield_t = rng.randint(4, 8)
    diag = _svg_bars(
        f"South African Land Resource Limits ({region})",
        [
            ("Arable Farmland Share (%)", fertile_pct, "#16a34a"),
            ("Dry / Non-Arable Share (%)", 100 - fertile_pct, "#d97706"),
        ],
        unit_prefix="",
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the land-use diagram noting that only about {fertile_pct}% of South African land is naturally arable "
        f"(producing around {yield_t} tonnes/ha when irrigated). Explain why conserving fertile agricultural soil and water "
        f"is crucial for South Africa's national food security."
    )
    sample = (
        f"Because arable land is severely scarce (only {fertile_pct}%), soil erosion, pollution, or unplanned urban sprawl "
        f"permanently shrinks food output ({yield_t} tonnes/ha), driving up staple food prices and threatening nutrition for millions."
    )
    worked = (
        f"1. **Resource scarcity [1]:** Only {fertile_pct}% of land can grow staple crops productively.\n"
        f"2. **Food security link [2]:** Protecting topsoil and water sustains domestic harvests ({yield_t} tonnes/ha), keeping staple foods affordable and preventing hunger or expensive imports."
    )
    return _q(
        rng,
        "32_agricultural_food_security_land",
        prompt,
        sample,
        worked,
        "Soil and water conservation preserves scarce natural capital essential for feeding the nation.",
        {
            "tier_1": f"Notice from the diagram how tiny the {fertile_pct}% arable farmland bar is.",
            "tier_2": "Connect losing arable farmland directly to food availability and household food prices.",
            "tier_3": "Explain that scarce fertile land means losing farms threatens domestic food supply and affordability.",
        },
        ["overlooks_scarcity_of_south_african_arable_land"],
        [
            {"criterion": f"Notes extreme scarcity of arable land ({fertile_pct}%)", "marks": 1},
            {"criterion": "Connects soil/water conservation to staple food supply and price stability", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b33(rng: random.Random) -> Dict[str, Any]:
    farmer = _pick_person(rng)
    hectares = rng.randint(20, 45)
    normal_t = rng.randint(5, 7)
    drought_t = rng.randint(2, 3)
    loss_tonnes = hectares * (normal_t - drought_t)
    prompt = (
        f"{farmer} farms maize on {hectares} hectares of scarce fertile land. In a good rainfall season, yield is "
        f"{normal_t} tonnes per hectare, but drought cuts yield to {drought_t} tonnes per hectare. "
        f"Calculate the total maize harvest lost in tonnes across {farmer}'s farm."
    )
    worked = (
        f"1. **Yield drop per hectare [1]:** {normal_t} - {drought_t} = {normal_t - drought_t} tonnes/ha.\n"
        f"2. **Total farm loss [1]:** {hectares} ha x {normal_t - drought_t} tonnes/ha = **{loss_tonnes} tonnes**."
    )
    return _q(
        rng,
        "33_arable_land_crop_yield_calculation",
        prompt,
        f"{loss_tonnes} tonnes",
        worked,
        "Rainfall scarcity directly reduces physical agricultural output per hectare, shrinking food supply.",
        {
            "tier_1": "Find how many tonnes were lost on each single hectare first.",
            "tier_2": f"Multiply the per-hectare drop by {hectares} hectares.",
            "tier_3": f"Compute {hectares} x ({normal_t} - {drought_t}) = {loss_tonnes} tonnes.",
        },
        ["forgets_to_multiply_per_hectare_loss_by_hectares"],
        [
            {"criterion": f"Yield loss per hectare = {normal_t - drought_t} tonnes", "marks": 1},
            {"criterion": f"Total harvest loss = {loss_tonnes} tonnes", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b34(rng: random.Random) -> Dict[str, Any]:
    province = rng.choice(["Mpumalanga coal fields", "Northern Cape solar parks", "Limpopo platinum belt"])
    resource = rng.choice(["coal and gold ore", "crude oil and natural gas"])
    prompt = (
        f"While studying resource sustainability near {province}, learners examine finite minerals such as {resource} "
        f"that take millions of years to form and cannot be replaced once mined. How are these classified?"
    )
    return _mcq(
        rng,
        "34_renewable_vs_nonrenewable_resources",
        prompt,
        "Non-renewable natural resources",
        ["Unlimited consumer wants", "Infinite renewable solar flows", "Manufactured machinery capital"],
        "Non-renewable resources exist in fixed geological deposits and cannot replenish within a human lifetime once extracted.",
        {
            "tier_1": "Ask whether humans can regrow coal or platinum ore on a farm within a few years.",
            "tier_2": "Distinguish finite geological minerals from replenishing solar/wind flows.",
            "tier_3": "Select 'Non-renewable natural resources'.",
        },
        ["thinks_coal_and_minerals_regrow_rapidly"],
    )


def _b35(rng: random.Random) -> Dict[str, Any]:
    school = _pick_place(rng, rural=False)
    leader = _pick_person(rng)
    prompt = (
        f"At a school eco-club in {school}, {leader} warns that wasteful consumption drains scarce water and electricity "
        f"needed by future South Africans. Suggest THREE practical ways households or businesses can use scarce resources more sustainably."
    )
    sample = (
        "(1) Fix leaking taps and harvest rainwater to conserve scarce fresh water; "
        "(2) Switch to energy-efficient LED bulbs and solar water heaters to cut electricity waste; and "
        "(3) Reuse, repair, and recycle packaging/materials to reduce raw material depletion and landfill waste."
    )
    worked = (
        "1. **Water conservation [1]:** Repair dripping taps, collect rainwater in JoJo tanks, and irrigate gardens during cool hours.\n"
        "2. **Energy efficiency [1]:** Turn off unused appliances, install LEDs, or use solar power where affordable.\n"
        "3. **Waste reduction [1]:** Reuse, repair, and recycle paper, glass, metal, and plastics."
    )
    return _q(
        rng,
        "35_sustainable_resource_management",
        prompt,
        sample,
        worked,
        "Sustainable resource habits meet today's needs without exhausting natural resources for future generations.",
        {
            "tier_1": "Think of concrete actions covering water, electricity, and physical materials.",
            "tier_2": "Consider leaks/rainwater, LED/switching off power, and recycling/reusing.",
            "tier_3": "Give three clear practical habits covering water saving, energy conservation, and reuse/recycling.",
        },
        ["gives_vague_answers_like_be_good_to_nature"],
        [
            {"criterion": "Concrete water conservation practice", "marks": 1},
            {"criterion": "Concrete energy efficiency / saving practice", "marks": 1},
            {"criterion": "Concrete material reuse, repair, or recycling practice", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b36(rng: random.Random) -> Dict[str, Any]:
    shopper = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    pair = rng.choice(["pure 24-carat gold rings and diamond earrings", "imported designer perfume and first-class air tickets", "luxury sports coupe and designer handbags"])
    prompt = (
        f"In an upscale boutique in {town}, {shopper} sees {pair}. Why are these classified as luxury wants "
        f"rather than primary needs?"
    )
    return _mcq(
        rng,
        "36_luxury_wants_vs_basic_necessities",
        prompt,
        "People can stay healthy and survive completely without them; they serve status and indulgence",
        [
            "Doctors prescribe imported perfume as mandatory daily hydration",
            "Government distributes luxury diamond jewellery as monthly social grants",
            "Luxury goods cost less than tap water and staple maize meal",
        ],
        "Luxury wants go far beyond basic physical survival or functional everyday comfort, reflecting high prestige or indulgence desires.",
        {
            "tier_1": "Test whether human health or safety fails without designer luxury items.",
            "tier_2": "Separate high-cost status consumption from basic survival needs.",
            "tier_3": "Choose the statement highlighting survival without them and status/indulgence.",
        },
        ["rationalises_status_symbols_as_basic_needs"],
    )


def _b37(rng: random.Random) -> Dict[str, Any]:
    parent = _pick_person(rng)
    budget = rng.choice([700, 800, 900])
    water = rng.choice([180, 210])
    groceries = rng.choice([380, 420])
    data = rng.choice([160, 190])
    cinema = rng.choice([220, 260])
    total_all = water + groceries + data + cinema
    shortfall = total_all - budget
    prompt = (
        f"{parent} has {_fmt_rand(budget)} for the week and faces four items: municipal water bill ({_fmt_rand(water)}), "
        f"basic food groceries ({_fmt_rand(groceries)}), homework data ({_fmt_rand(data)}), and cinema outing ({_fmt_rand(cinema)}). "
        f"Calculate the Rand shortfall if {parent} tried to pay for all four items."
    )
    worked = (
        f"1. **Total cost of all four items [1]:** {_fmt_rand(water)} + {_fmt_rand(groceries)} + {_fmt_rand(data)} + {_fmt_rand(cinema)} = {_fmt_rand(total_all)}.\n"
        f"2. **Rand shortfall [1]:** {_fmt_rand(total_all)} - {_fmt_rand(budget)} = **{_fmt_rand(shortfall)}** (meaning cinema outings are cut first so water and groceries are paid)."
    )
    return _q(
        rng,
        "37_utility_and_priority_ranking",
        prompt,
        _fmt_rand(shortfall),
        worked,
        "Calculating budget shortfalls clarifies why luxury wants must be deferred until primary survival bills are settled.",
        {
            "tier_1": "Add all four listed Rand amounts together first.",
            "tier_2": f"Subtract {parent}'s {_fmt_rand(budget)} budget from the combined total.",
            "tier_3": f"Compute {_fmt_rand(total_all)} - {_fmt_rand(budget)} = {_fmt_rand(shortfall)}.",
        },
        ["omits_one_item_when_totalling_expenses"],
        [
            {"criterion": f"Sums all four items = {_fmt_rand(total_all)}", "marks": 1},
            {"criterion": f"Calculates shortfall = {_fmt_rand(shortfall)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b38(rng: random.Random) -> Dict[str, Any]:
    earner = _pick_person(rng)
    income = rng.choice([4000, 5000, 6000, 8000])
    pct_needs = rng.choice([65, 70, 75, 80])
    needs_amt = (income * pct_needs) // 100
    prompt = (
        f"{earner}'s household earns {_fmt_rand(income)} per month and spends {_fmt_rand(needs_amt)} on basic survival "
        f"needs (rent, electricity, water, and staple food). What percentage of household income is consumed by basic needs?"
    )
    worked = (
        f"1. **Share formula [1]:** (Basic needs / Monthly income) x 100.\n"
        f"2. **Calculation [1]:** ({_fmt_rand(needs_amt)} / {_fmt_rand(income)}) x 100 = **{pct_needs}%**."
    )
    return _q(
        rng,
        "38_household_income_vs_wants_ratio",
        prompt,
        f"{pct_needs}%",
        worked,
        "Lower- and middle-income households often devote the vast majority of income to basic survival needs before wants.",
        {
            "tier_1": "Divide basic needs spending by total monthly household income.",
            "tier_2": f"Compute ({needs_amt} / {income}) x 100.",
            "tier_3": f"Express the fraction as a whole percentage: {pct_needs}%.",
        },
        ["divides_income_by_needs_instead_of_needs_by_income"],
        [
            {"criterion": f"Correct ratio {needs_amt} / {income}", "marks": 1},
            {"criterion": f"Correct percentage {pct_needs}%", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b39(rng: random.Random) -> Dict[str, Any]:
    grandparent, learner = _pick_two_people(rng)
    tech = rng.choice(["reliable home electricity and internet access", "a basic mobile phone for safety and banking"])
    prompt = (
        f"{grandparent} recalls when {tech} felt like a rare luxury, whereas today {learner} relies on it for school "
        f"assignments and family communication. Explain why some former wants evolve into practical secondary needs over time."
    )
    sample = (
        f"As society and technology advance, schoolwork, job applications, banking, and safety increasingly depend on "
        f"{tech}. Without it, citizens like {learner} risk exclusion from education and employment, shifting it from "
        f"an optional luxury into a modern secondary need."
    )
    worked = (
        f"1. **Social & technological shift [1]:** Schools, employers, and banks digitise core services.\n"
        f"2. **Risk of exclusion [2]:** Access to {tech} becomes essential for learning and participating in modern economic life rather than pure entertainment."
    )
    return _q(
        rng,
        "39_needs_evolution_with_technology",
        prompt,
        sample,
        worked,
        "While basic biological needs never change, modern secondary needs evolve alongside schooling, work, and public infrastructure.",
        {
            "tier_1": "Compare how learners submitted assignments 40 years ago versus today.",
            "tier_2": f"Consider whether lacking {tech} today harms education or safety, not just fun.",
            "tier_3": "Explain that digital schooling, banking, and work make former luxuries practical modern secondary needs.",
        },
        ["claims_needs_never_evolve_beyond_stone_age"],
        [
            {"criterion": "Explains societal/technological shift in schools and workplaces", "marks": 1},
            {"criterion": f"Links {tech} to equal educational/economic participation", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b40(rng: random.Random) -> Dict[str, Any]:
    student = _pick_person(rng)
    prompt = (
        f"Before focusing on school clubs or creative hobbies, {student} ensures hunger, clean water, and safe shelter "
        f"are taken care of first. Which progression of human needs does this demonstrate?"
    )
    return _mcq(
        rng,
        "40_maslow_basic_to_higher_hierarchy",
        prompt,
        "Primary physical survival needs must be met first before higher social and self-development needs take priority",
        [
            "Entertainment and designer fashion must always be bought before drinking water",
            "Human survival improves when air and food are replaced by luxury wants",
            "National military spending satisfies individual hunger faster than groceries",
        ],
        "In human needs hierarchies, immediate physiological survival and safety sit at the foundation; once secured, social, educational, and self-fulfilment needs follow.",
        {
            "tier_1": "Think of the priority order between biological survival and social or creative hobbies.",
            "tier_2": "Foundational food, water, and shelter come first; belonging and hobbies build on top.",
            "tier_3": "Select the option stating primary survival needs precede higher social/development needs.",
        },
        ["reverses_survival_and_self_actualisation_order"],
    )


def _b41(rng: random.Random) -> Dict[str, Any]:
    founder = _pick_person(rng)
    suburb = _pick_place(rng, rural=False)
    votes_repair = rng.randint(42, 68)
    votes_bread = rng.randint(25, 38)
    votes_candy = rng.randint(8, 16)
    diag = _svg_bars(
        f"{suburb} Unmet Needs Poll ({founder})",
        [
            ("After-School Shoe & Bag Repair", votes_repair, "#16a34a"),
            ("Early-Morning Warm Bread", votes_bread, "#0284c7"),
            ("Novelty Cotton Candy", votes_candy, "#f59e0b"),
        ],
        unit_prefix="",
        unit_suffix=" votes",
    )
    prompt = (
        f"Refer to the neighbourhood survey diagram collected by {founder} in {suburb} showing unmet requests: "
        f"Shoe & Bag Repair ({votes_repair} votes), Warm Bread ({votes_bread} votes), and Cotton Candy ({votes_candy} votes). "
        f"Which service should {founder} launch first, and why does it represent the strongest entrepreneurial opportunity?"
    )
    sample = (
        f"{founder} should launch **After-School Shoe & Bag Repair** first because it recorded the highest unmet community demand "
        f"({votes_repair} votes vs {votes_bread} and {votes_candy}) and solves an everyday practical family need that saves households money."
    )
    worked = (
        f"1. **Best choice [1]:** **After-School Shoe & Bag Repair** ({votes_repair} votes).\n"
        f"2. **Entrepreneurial reasoning [2]:** Highest verified customer demand in {suburb} and addresses a recurring practical household need rather than an optional sugary want ({votes_candy} votes)."
    )
    return _q(
        rng,
        "41_entrepreneur_spots_unmet_need",
        prompt,
        sample,
        worked,
        "Successful entrepreneurs spot high-demand unmet local needs rather than guessing low-priority novelty wants.",
        {
            "tier_1": "Look for the option with both the highest survey count and genuine practical usefulness.",
            "tier_2": f"Compare {votes_repair} votes, {votes_bread} votes, and {votes_candy} votes in the diagram.",
            "tier_3": f"Recommend Shoe & Bag Repair ({votes_repair} votes) based on peak demand and recurring household utility.",
        },
        ["picks_novelty_want_despite_lowest_demand"],
        [
            {"criterion": f"Selects Shoe & Bag Repair ({votes_repair} votes)", "marks": 1},
            {"criterion": "Justifies with highest demand and practical community need", "marks": 2},
        ],
        cognitive_level="Problem Solving",
        marks=3,
        diagram_spec=diag,
    )


def _b42(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each essential service in {town} according to whether it is typically supplied by **Government**, "
        f"**Private Business**, or **Both Government and Private**."
    )
    row_specs = [
        {"cells": ["National policing, courts, and municipal street lighting", None], "expected": ["Government"], "cell_hints": ["Core sovereign and non-exclusive public safety functions."]},
        {"cells": ["Branded sportswear, bakery pastries, and private hair salons", None], "expected": ["Private Business"], "cell_hints": ["Competitive retail consumer goods and personal services."]},
        {"cells": ["School education and medical clinic/hospital care in South Africa", None], "expected": ["Both Government and Private"], "cell_hints": ["Exists as free/subsidised public schools/clinics alongside fee-paying private providers."]},
        {"cells": ["National border defence and traffic regulation laws", None], "expected": ["Government"], "cell_hints": ["Exclusive state authority functions."]},
    ]
    return _table_q(
        rng,
        "42_public_vs_private_provision_table",
        prompt,
        ["Good or Service", "Typical Provider"],
        row_specs,
        "Mixed economies like South Africa combine public tax-funded government infrastructure, competitive private businesses, and dual sectors such as health and education.",
        {
            "tier_1": "Ask which items must be tax-funded for all citizens, which are commercial retail, and which exist in both public and private versions.",
            "tier_2": "Policing/defence belong to Government; sportswear/salons to Private Business; schools/hospitals exist in Both.",
            "tier_3": "Fill in Government, Private Business, and Both Government and Private.",
        },
        ["thinks_clinics_and_schools_are_only_private_or_only_public"],
    )


def _b43(rng: random.Random) -> Dict[str, Any]:
    family = _pick_person(rng)
    old_basket = rng.choice([400, 500, 600, 800])
    inc_pct = rng.choice([10, 15, 20])
    extra_cost = (old_basket * inc_pct) // 100
    new_basket = old_basket + extra_cost
    prompt = (
        f"Due to inflation, the price of {family}'s weekly basic food basket rises by {inc_pct}% from {_fmt_rand(old_basket)}. "
        f"Calculate the **new weekly cost** of the food basket in Rands."
    )
    worked = (
        f"1. **Price increase [1]:** {inc_pct}% of {_fmt_rand(old_basket)} = {_fmt_rand(extra_cost)}.\n"
        f"2. **New weekly cost [1]:** {_fmt_rand(old_basket)} + {_fmt_rand(extra_cost)} = **{_fmt_rand(new_basket)}** "
        f"(reducing money left for secondary wants)."
    )
    return _q(
        rng,
        "43_inflation_impact_on_basic_needs",
        prompt,
        _fmt_rand(new_basket),
        worked,
        "Rising prices on staple food squeeze fixed household budgets, leaving fewer Rands for secondary needs and wants.",
        {
            "tier_1": f"First calculate {inc_pct}% of {_fmt_rand(old_basket)}.",
            "tier_2": "Add the Rand price increase onto the original food basket cost.",
            "tier_3": f"Compute {_fmt_rand(old_basket)} + {_fmt_rand(extra_cost)} = {_fmt_rand(new_basket)}.",
        },
        ["reports_only_the_increase_not_the_new_total"],
        [
            {"criterion": f"Calculates increase = {_fmt_rand(extra_cost)}", "marks": 1},
            {"criterion": f"Calculates new basket total = {_fmt_rand(new_basket)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b44(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    coop = rng.choice(["a community vegetable garden sharing tools and borehole water", "a neighbour grocery stokvel buying bulk maize and cooking oil together"])
    members = rng.randint(10, 24)
    prompt = (
        f"In {town}, {members} households form {coop}. Explain TWO economic ways that Ubuntu and community cooperation "
        f"help families cope with scarce money and resources."
    )
    sample = (
        f"(1) Pooling money or inputs among {members} families cuts unit costs through bulk buying or shared capital tools, "
        f"and (2) shared skills and mutual support build food security and cushion individual households against sudden shortages."
    )
    worked = (
        f"1. **Cost sharing / bulk savings [1]:** {members} families split costs of expensive equipment or bulk staples, stretching scarce Rands further.\n"
        f"2. **Mutual resilience [1]:** Sharing labour, knowledge, and surpluses protects vulnerable households during tough months."
    )
    return _q(
        rng,
        "44_sharing_and_community_ubuntu",
        prompt,
        sample,
        worked,
        "Community cooperation like stokvels and shared gardens turns scarce individual inputs into stronger collective capacity.",
        {
            "tier_1": f"Think about why {members} households working together pay less per item than one person buying alone.",
            "tier_2": "Focus on bulk discounts, sharing expensive tools, and mutual crisis support.",
            "tier_3": "State two economic benefits: lower unit/tool costs through pooling, and improved resilience/food security.",
        },
        ["overlooks_bulk_and_cost_sharing_economies"],
        [
            {"criterion": "Explains cost reduction / bulk buying or shared tools", "marks": 1},
            {"criterion": "Explains collective resilience / mutual support against scarcity", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b45(rng: random.Random) -> Dict[str, Any]:
    health_b = rng.choice([240, 260, 280])
    edu_b = rng.choice([410, 440, 460])
    trans_b = rng.choice([120, 140, 150])
    total_b = health_b + edu_b + trans_b
    shift_b = rng.choice([20, 30])
    diag = _svg_bars(
        "Sample National Need Allocations (R Billion)",
        [
            ("Public Education", edu_b, "#2563eb"),
            ("Public Healthcare", health_b, "#16a34a"),
            ("Public Transport", trans_b, "#0d9488"),
        ],
        unit_prefix="R",
        unit_suffix="bn",
    )
    prompt = (
        f"Refer to the national budget diagram showing allocations for Public Education (R{edu_b}bn), Public Healthcare "
        f"(R{health_b}bn), and Public Transport (R{trans_b}bn). Calculate the combined Rand total across all three, "
        f"and state the opportunity cost if government shifts R{shift_b}bn from Public Transport into Public Healthcare."
    )
    worked = (
        f"1. **Combined allocation [1]:** R{edu_b}bn + R{health_b}bn + R{trans_b}bn = **R{total_b}bn**.\n"
        f"2. **Opportunity cost [1]:** Shifting R{shift_b}bn means Public Transport receives R{shift_b}bn less (foregone rail/bus upgrades = **R{shift_b}bn in transport**)."
    )
    return _q(
        rng,
        "45_government_budget_tradeoff_country",
        prompt,
        f"R{total_b}bn; R{shift_b}bn foregone in Public Transport",
        worked,
        "Even national treasuries face scarcity and opportunity cost: raising one priority department requires reducing or taxing elsewhere.",
        {
            "tier_1": "Add the three sector bars in R billions, then identify which sector loses R funding when R moves to Healthcare.",
            "tier_2": f"Sum R{edu_b}bn + R{health_b}bn + R{trans_b}bn and state the foregone transport value.",
            "tier_3": f"Give R{total_b}bn total and state R{shift_b}bn foregone in Public Transport.",
        },
        ["assumes_government_can_spend_without_tradeoffs"],
        [
            {"criterion": f"Calculates combined total = R{total_b}bn", "marks": 1},
            {"criterion": f"Identifies opportunity cost: R{shift_b}bn foregone in Public Transport", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Complex Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b46(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    crop = rng.choice(["fresh tomatoes", "avocados", "green peppers", "potatoes"])
    prompt = (
        f"After severe hail damages farms around {town}, supply of {crop} drops sharply while household demand stays high. "
        f"What normally happens to the market price of scarce {crop}?"
    )
    return _mcq(
        rng,
        "46_scarcity_price_signal_supply",
        prompt,
        "The price rises because limited supply cannot satisfy every buyer at the old price",
        [
            "The price drops immediately to zero because crops are smaller",
            "Shopkeepers give away remaining stock free until shelves empty in one minute",
            "Demand triples the harvest overnight without rain or planting",
        ],
        "Greater relative scarcity pushes prices upward, rationing limited stock toward higher-priority buyers and signalling farmers to plant more.",
        {
            "tier_1": "Think of what happens when 100 shoppers want a basket of goods and only 20 baskets arrive at market.",
            "tier_2": "Recall how scarcity affects market prices when demand exceeds supply.",
            "tier_3": "Choose the answer explaining why prices increase.",
        },
        ["thinks_shortage_causes_prices_to_drop"],
    )


def _b47(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    ad = rng.choice(["a flashy 'must-have' energy drink advert", "a limited-time social media sneaker drop"])
    prompt = (
        f"{learner} notices how {ad} tries to convince teenagers that an expensive want is actually an urgent need. "
        f"Recommend TWO practical smart-spending habits that protect a Grade 7 learner's budget from persuasive marketing."
    )
    sample = (
        "(1) Write a shopping list in advance distinguishing needs from wants and stick strictly to it; and "
        "(2) apply a 48-hour cooling-off rule before buying advertised non-essentials while comparing prices across stores."
    )
    worked = (
        "1. **Planned list & budget [1]:** Separate survival/school needs from wants before entering a shop or online store.\n"
        "2. **Cooling-off & price check [1]:** Wait 24–48 hours before impulse purchases and question advertising claims."
    )
    return _q(
        rng,
        "47_consumer_rights_vs_want_advertising",
        prompt,
        sample,
        worked,
        "Critical consumer literacy helps learners resist impulse buying driven by persuasive marketing.",
        {
            "tier_1": "Think of two habits that stop shoppers from making quick emotional purchases triggered by ads.",
            "tier_2": "Consider pre-written needs/wants budgets and waiting periods before spending.",
            "tier_3": "State two concrete habits: pre-shopping needs-first list/budget and a cooling-off pause / price comparison.",
        },
        ["confuses_advertising_claims_with_real_needs"],
        [
            {"criterion": "Habit 1: Needs-first shopping list / written budget limit", "marks": 1},
            {"criterion": "Habit 2: Cooling-off delay / comparing prices / questioning ads", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b48(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    disaster = rng.choice(["severe river flooding", "a sudden coastal cyclone"])
    prompt = (
        f"When {disaster} strikes {town}, homes and roads are damaged. Identify TWO urgent **immediate primary needs** "
        f"that disaster relief teams must deliver in the first 48 hours, and ONE **medium-term community recovery need**."
    )
    sample = (
        "Immediate primary needs (first 48 hours): (1) safe bottled drinking water and ready-to-eat nutritious food, and "
        "(2) dry emergency shelter, blankets, and medical first aid. Medium-term recovery need: repairing municipal pipes, bridges, electricity lines, and schools."
    )
    worked = (
        f"1. **Immediate primary need 1 [1]:** Clean drinking water / emergency food parcels.\n"
        f"2. **Immediate primary need 2 [1]:** Dry shelter, warm blankets, or emergency healthcare.\n"
        f"3. **Medium-term recovery need [1]:** Rebuilding water/sanitation pipes, roads, or schools in {town}."
    )
    return _q(
        rng,
        "48_disaster_disrupts_basic_needs",
        prompt,
        sample,
        worked,
        "Natural disasters instantly return community priorities to raw physiological survival before infrastructure restoration begins.",
        {
            "tier_1": "Separate life-saving basics needed tonight from infrastructure rebuilt over weeks.",
            "tier_2": "Think of water/food/shelter/medicine first, then bridges, clinics, and electricity grids.",
            "tier_3": "List two 48-hour survival needs and one infrastructure repair priority.",
        },
        ["prioritises_wifi_or_entertainment_during_emergency_rescue"],
        [
            {"criterion": "Immediate survival need 1 (water / food)", "marks": 1},
            {"criterion": "Immediate survival need 2 (emergency shelter / medical care)", "marks": 1},
            {"criterion": "Medium-term community recovery need (pipes / roads / schools)", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b49(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    cap = rng.choice([15000, 22000, 30000])
    diag = _svg_chain(
        f"Economic Resource Chain — {town}",
        [
            ("1. Wants vs Limits", "Basic economic problem"),
            ("2. Choice", "Prioritise needs first"),
            ("3. Factors", f"Capital {_fmt_rand(cap)} + Labour"),
            ("4. Production", "Goods & services"),
            ("5. Satisfaction", "Community needs met"),
        ],
    )
    prompt = (
        f"Refer to the five-step economic chain diagram for {town} (including {_fmt_rand(cap)} capital invested). "
        f"Trace how scarcity at Step 1 leads through Step 3 (factors of production) to Step 5 (satisfying community needs)."
    )
    sample = (
        f"Because unlimited wants clash with scarce resources at Step 1, households and planners make prioritisation choices "
        f"(Step 2). Producers then combine natural resources, labour, entrepreneurship, and {_fmt_rand(cap)} capital (Step 3) "
        f"to manufacture essential goods and services (Step 4) that satisfy priority community needs (Step 5)."
    )
    worked = (
        f"1. **Scarcity -> Choice [1]:** Limited inputs force {town} to select priority needs over optional wants.\n"
        f"2. **Factors -> Output -> Needs [2]:** Entrepreneurs combine land, labour, and {_fmt_rand(cap)} capital to produce goods/services that relieve community shortages."
    )
    return _q(
        rng,
        "49_needs_wants_resource_chain_diagram",
        prompt,
        sample,
        worked,
        "Economics links unlimited human wants, scarce productive inputs, entrepreneur choices, and final need satisfaction in one logical chain.",
        {
            "tier_1": "Follow the sequence from Step 1 through Step 5 in the diagram.",
            "tier_2": f"Mention how {_fmt_rand(cap)} capital works alongside land, labour, and entrepreneurship at Step 3.",
            "tier_3": "Explain scarcity -> choice -> factors of production -> goods/services -> satisfied needs.",
        },
        ["disconnects_factors_of_production_from_need_satisfaction"],
        [
            {"criterion": "Connects scarcity (Step 1) to forced choice (Step 2)", "marks": 1},
            {"criterion": f"Explains combining {_fmt_rand(cap)} capital + other factors to satisfy needs (Steps 3–5)", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b50(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    budget = rng.choice([2800, 3500, 4200])
    prompt = (
        f"Write a structured mini-essay for {learner} in {town} explaining how the basic economic problem operates "
        f"simultaneously at **Individual/Family** (e.g. a {_fmt_rand(budget)} monthly budget), **Community**, and **Country** "
        f"levels, making sure to incorporate **primary needs**, **unlimited wants**, **scarcity**, and **opportunity cost**."
    )
    sample = (
        f"Every tier of society faces scarcity because wants are unlimited while resources are limited. "
        f"At the family level in {town}, a {_fmt_rand(budget)} budget must fund primary needs (water, staple food, shelter) first; "
        f"the opportunity cost of extra groceries may be giving up new sneakers. At the community level, scarce municipal taxes "
        f"force choices between clinics and parks. At the country level, national government weighs healthcare and education against "
        f"transport spending, always incurring opportunity cost."
    )
    worked = (
        f"1. **Individual/Family ({_fmt_rand(budget)}) [2]:** Prioritises primary survival needs ahead of unlimited wants; names a clear opportunity cost.\n"
        f"2. **Community level [1]:** Municipalities allocate scarce local funds toward shared clinics, sanitation, and water.\n"
        f"3. **Country level [1]:** National treasury balances education, healthcare, defence, and food security under scarcity."
    )
    return _q(
        rng,
        "50_economic_problem_synthesis_essay",
        prompt,
        sample,
        worked,
        "Across households, towns, and nations, unlimited wants and finite resources make prioritisation and opportunity cost unavoidable.",
        {
            "tier_1": "Structure your answer cleanly into three paragraphs/points: Household, Community, and Country.",
            "tier_2": f"Weave all four key terms explicitly into your {_fmt_rand(budget)} and {town} examples.",
            "tier_3": "Cover family primary needs vs opportunity cost, community infrastructure choices, and national budget priorities.",
        },
        ["answers_only_individual_level_omitting_community_and_country"],
        [
            {"criterion": f"Household level ({_fmt_rand(budget)}): primary needs, wants, opportunity cost", "marks": 2},
            {"criterion": f"Community level in {town}: shared service priorities", "marks": 1},
            {"criterion": "Country level: national allocation tradeoffs under scarcity", "marks": 1},
        ],
        cognitive_level="Problem Solving",
        marks=4,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_factors_of_production_remuneration_table": _b26,
    "27_business_meets_community_needs": _b27,
    "28_government_public_goods_provision": _b28,
    "29_municipal_service_delivery_priorities": _b29,
    "30_service_delivery_protests_causes": _b30,
    "31_rural_vs_urban_community_needs": _b31,
    "32_agricultural_food_security_land": _b32,
    "33_arable_land_crop_yield_calculation": _b33,
    "34_renewable_vs_nonrenewable_resources": _b34,
    "35_sustainable_resource_management": _b35,
    "36_luxury_wants_vs_basic_necessities": _b36,
    "37_utility_and_priority_ranking": _b37,
    "38_household_income_vs_wants_ratio": _b38,
    "39_needs_evolution_with_technology": _b39,
    "40_maslow_basic_to_higher_hierarchy": _b40,
    "41_entrepreneur_spots_unmet_need": _b41,
    "42_public_vs_private_provision_table": _b42,
    "43_inflation_impact_on_basic_needs": _b43,
    "44_sharing_and_community_ubuntu": _b44,
    "45_government_budget_tradeoff_country": _b45,
    "46_scarcity_price_signal_supply": _b46,
    "47_consumer_rights_vs_want_advertising": _b47,
    "48_disaster_disrupts_basic_needs": _b48,
    "49_needs_wants_resource_chain_diagram": _b49,
    "50_economic_problem_synthesis_essay": _b50,
}
