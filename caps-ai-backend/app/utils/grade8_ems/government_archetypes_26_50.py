"""Grade 8 EMS - Government: Archetypes 26 to 50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/01. Government.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES as PERSON_NAMES
from .government_archetypes_01_25 import _build_mcq, _build_short, _build_table, _fmt_r

BUSINESS_NAMES = [
    "Ubuntu Solar Services",
    "Kasi Fresh Logistics",
    "Mfula Civil Contractors",
    "Naledi Packaging Works",
    "Imbali Textile Works",
    "Vula Tech Supplies",
    "Mzansi Builders Hub",
    "Thabo & Sons Catering",
]


def _make_cell(coord: str, value: str, cell_type: str) -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "cell_id": coord,
        "value": value,
        "type": cell_type,
    }


def arch_26_smme_support_skills_and_startup_finance(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    area = rng.choice(AREAS)
    grant_amt = rng.choice([45000, 65000, 85000, 120000])
    prompt = (
        f"**{owner}** wants to launch **{biz}**, a small manufacturing SMME in **{area}**, "
        f"but needs **{_fmt_r(grant_amt)}** in start-up capital plus mentorship on bookkeeping and tax compliance.\n\n"
        f"Explain **two ways** the South African government actively supports SMMEs like **{biz}** and state **one national economic benefit** of doing so."
    )
    expected = (
        f"1) Providing start-up finance/development grants (such as {_fmt_r(grant_amt)}) and affordable credit.\n"
        "2) Offering skills training, business advice, and mentorship.\n"
        "Benefit: Small firms create jobs, reduce unemployment, and expand the tax base."
    )
    sol = (
        f"**Supporting SMMEs ({biz}) [3 marks]:**\n\n"
        f"1. **Financial Support:** Government agencies provide start-up finance, micro-loans, or grants (such as **{_fmt_r(grant_amt)}**) so entrepreneurs can purchase equipment and stock **[1]**.\n"
        "2. **Non-Financial Support:** Government supplies free **business advice, skills training, and mentorship** so new owners manage finances properly **[1]**.\n"
        "3. **Economic Benefit:** Thriving SMMEs **create jobs** in local communities, reduce poverty, and pay taxes back to the state **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_26",
        subskill="26_smme_support_skills_and_startup_finance",
        title="Government Support for SMMEs",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think of money help (finance) and knowledge help (skills/advice).",
            "tier_2": "State two types of support for start-ups and why growing SMMEs helps the country.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Start-up finance / grants / affordable loans", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Business advice / skills training / mentorship", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Creates local employment and grows economy/tax base", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_government_only_helps_large_corporates"],
    )


def arch_27_government_tenders_and_procurement_from_businesses(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    area = rng.choice(AREAS)
    item = rng.choice(["school desks and textbooks", "clinic surgical gloves and uniforms", "road resurfacing materials", "municipal solar streetlamps"])
    tender_val = rng.choice([240000, 380000, 520000, 680000])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 210" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="210" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Public Procurement Flow: {area}</text>'
        '<rect x="30" y="55" width="180" height="90" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="120" y="92" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Government</text>'
        '<text x="120" y="114" text-anchor="middle" font-size="11" fill="#1e40af">(Consumer of Goods)</text>'
        '<rect x="430" y="55" width="180" height="90" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="520" y="92" text-anchor="middle" font-size="13" font-weight="bold" fill="#14532d">{biz}</text>'
        '<text x="520" y="114" text-anchor="middle" font-size="11" fill="#166534">(Private Supplier)</text>'
        '<line x1="210" y1="80" x2="422" y2="80" stroke="#0284c7" stroke-width="2.5"/>'
        '<polygon points="422,75 430,80 422,85" fill="#0284c7"/>'
        f'<text x="320" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#0369a1">Tender Payment: {_fmt_r(tender_val)}</text>'
        '<line x1="430" y1="122" x2="218" y2="122" stroke="#15803d" stroke-width="2.5"/>'
        '<polygon points="218,117 210,122 218,127" fill="#15803d"/>'
        f'<text x="320" y="142" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">{item}</text>'
        '</svg>'
    )
    prompt = (
        f"Study the procurement diagram for **{area}**, where **Government** awards a **{_fmt_r(tender_val)}** contract to **{biz}** "
        f"to supply **{item}**.\n\n"
        f"Which statement **best** explains how this tender demonstrates the economic role of **Government as a Consumer**?"
    )
    correct = (
        f"Government acts as a consumer by purchasing {item} from {biz} for {_fmt_r(tender_val)}, "
        "injecting revenue into the private sector and supporting jobs."
    )
    distractors = [
        f"Government acts as a producer by manufacturing {item} inside Parliament and selling it to {biz}.",
        f"Businesses must donate {item} to municipalities free of charge without receiving tender payments.",
        "Government only buys goods from foreign governments and never awards tenders to South African suppliers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_27",
        subskill="27_government_tenders_and_procurement_from_businesses",
        title="Government Tenders & Procurement from Businesses",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"When **Government** spends **{_fmt_r(tender_val)}** via a competitive **tender** to buy **{item}** from **{biz}**, "
            "the state acts as a major **consumer** of business output, creating income and jobs."
        ),
        hints={
            "tier_1": "Look at which party pays money and receives goods/services in the diagram.",
            "tier_2": "Buying goods from private suppliers makes Government a consumer in that transaction.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_government_only_produces_never_consumes"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_28_physical_infrastructure_roads_ports_railways(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    corridor = rng.choice(["N3 highway to Durban Harbour", "N1 freight corridor to Cape Town Port", "Maputo corridor rail and highway", "N2 coastal route to Gqeberha port"])
    product = rng.choice(["fresh citrus fruit", "canned foods", "mining machinery parts", "woven textiles"])
    prompt = (
        f"**{biz}** transports **{product}** along the **{corridor}** for domestic retail and international export.\n\n"
        f"Identify this **category** of government-provided infrastructure and explain **one direct economic benefit** for businesses like **{biz}**."
    )
    expected = (
        "Physical (transport) infrastructure (roads, railways, harbours, airports). "
        f"Benefit: Reduces transport delays/costs so {biz} can move {product} reliably to markets and ports."
    )
    sol = (
        f"**Physical Infrastructure ({corridor}) [3 marks]:**\n\n"
        "1. **Category:** **Physical infrastructure** (roads, bridges, railways, harbours, and airports) **[1]**.\n"
        f"2. **Economic Benefit:** Reliable highways and ports lower transport costs and delivery times so **{biz}** can deliver **{product}** safely to customers and export markets **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_28",
        subskill="28_physical_infrastructure_roads_ports_railways",
        title="Physical Infrastructure for Business Logistics",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Roads, bridges, railways, and ports belong to one of three infrastructure groups.",
            "tier_2": "Physical infrastructure (not utility or service infrastructure) moves goods.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies Physical infrastructure", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Explains faster/cheaper movement of goods, inputs, or exports", "marks": 2, "editable": True},
        ],
        misconception_tags=["confusing_physical_with_utility_infrastructure"],
    )


def arch_29_service_infrastructure_police_fire_health(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    facility = rng.choice(["a 24-hour SAPS police station and fire brigade", "a public clinic and ambulance depot", "municipal emergency fire and rescue services"])
    prompt = (
        f"In **{area}**, government operates **{facility}** that protect both local residents and businesses like **{biz}**.\n\n"
        f"How is this type of infrastructure classified, and why could most individual businesses not operate profitably without it?"
    )
    correct = "Service infrastructure; it provides public safety, fire protection, and healthcare that keep workers healthy and business property secure."
    distractors = [
        "Utility infrastructure; it consists strictly of underground electricity cables and raw coal mines.",
        "Private retail inventory; citizens buy police protection per hour at supermarkets.",
        "Parliamentary legislation; it only applies inside the Constitutional Court building.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_29",
        subskill="29_service_infrastructure_police_fire_health",
        title="Service Infrastructure: Safety, Fire & Healthcare",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**{facility.capitalize()}** represents **service infrastructure**. Without safe streets, fire prevention, and healthy workers, businesses like **{biz}** face theft, damage, and absenteeism."
        ),
        hints={
            "tier_1": "Police, fire stations, hospitals, and schools form part of public services.",
            "tier_2": "Distinguish between Physical (roads), Utility (water/power), and Service (police/health) infrastructure.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_service_and_utility_infrastructure"],
    )


def arch_30_utility_infrastructure_electricity_water_sewerage(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    area = rng.choice(AREAS)
    utility_issue = rng.choice(["continuous 3-phase electricity and clean piped water", "reliable sewerage treatment and industrial power supply", "uninterrupted municipal water pressure and grid electricity"])
    prompt = (
        f"**{biz}** plans to open a food-processing factory in **{area}** and requires **{utility_issue}** before installing machinery.\n\n"
        f"Which category of infrastructure must government and SOEs supply here, and name **two examples** belonging to this category."
    )
    expected = "Utility infrastructure. Examples: electricity supply, clean water supply, sewerage/sanitation, and stormwater drainage."
    sol = (
        f"**Utility Infrastructure ({area}) [3 marks]:**\n\n"
        "1. **Category:** **Utility infrastructure** **[1]**.\n"
        f"2. **Two Examples:** Reliable **electricity**, **clean piped water**, **sewerage/sanitation**, or **drainage** required by **{biz}** to run machinery hygienically **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_30",
        subskill="30_utility_infrastructure_electricity_water_sewerage",
        title="Utility Infrastructure for Production & Households",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Power, water, and sanitation are basic utilities.",
            "tier_2": "State the category name (Utility infrastructure) plus two specific utility services.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Utility infrastructure", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Any two valid utility examples (electricity, water, sewerage/drainage)", "marks": 2, "editable": True},
        ],
        misconception_tags=["confusing_utility_with_physical_infrastructure"],
    )


def arch_31_natural_resource_protection_and_sustainability(rng: random.Random) -> Dict[str, Any]:
    resource = rng.choice(["freshwater river catchments and wetlands", "coastal rock-lobster and fish stocks", "indigenous forestry reserves", "mineral-rich soil and clean air quality"])
    area = rng.choice(AREAS)
    prompt = (
        f"Near **{area}**, factories and farms depend heavily on **{resource}**.\n\n"
        f"Why must the South African government enforce environmental regulations protecting **{resource}** instead of allowing unlimited extraction?"
    )
    correct = "To prevent irreversible depletion and pollution so that households and businesses can use natural resources sustainably now and in the future."
    distractors = [
        "To permanently shut down all agriculture, mining, and fishing across South Africa.",
        "Because natural resources automatically regenerate instantaneously no matter how polluted they become.",
        "Because municipalities use fishing quotas to pay the salaries of Parliamentarians.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_31",
        subskill="31_natural_resource_protection_and_sustainability",
        title="Protecting Natural Resources & Sustainability",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Government protects **{resource}** through environmental permits, quotas, and anti-pollution enforcement to preserve ecosystems for future generations and ongoing economic activity."
        ),
        hints={
            "tier_1": "What happens to businesses and communities tomorrow if water, forests, or fish are exhausted today?",
            "tier_2": "Regulation ensures sustainable use rather than depletion or pollution.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_environmental_role_of_government"],
    )


def arch_32_business_legislation_classification_table(rng: random.Random) -> Dict[str, Any]:
    case_firm = rng.choice(BUSINESS_NAMES)
    acts = [
        ("Labour Relations Act", "Workplace fairness, unfair dismissal protection, and bargaining", f"Employees at {case_firm} strike legally over unsafe shifts"),
        ("Competition Act", "Preventing monopolies, price-fixing, and cartels", "Two large suppliers secretly agree to charge identical bread prices"),
        ("Companies Act", "Rules for registering, auditing, and governing formal businesses", f"{case_firm} submits annual financial returns and registers its MOI"),
    ]
    rng.shuffle(acts)
    headers = ["Scenario in South Africa", "Legislation Applicable (Write Exact Act)", "Primary Group Protected"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Scenario in South Africa | Legislation Applicable | Primary Group Protected |", "| :--- | :--- | :--- |"]
    for idx, (act_name, _desc, scenario) in enumerate(acts):
        c1 = f"r{idx}c1"
        c2 = f"r{idx}c2"
        prot = "Workers and Employers" if "Labour" in act_name else ("Consumers and Rival Businesses" if "Competition" in act_name else "Shareholders, Creditors & Public")
        rows.append([
            _make_cell(f"r{idx}c0", scenario, "given"),
            _make_cell(c1, "", "required"),
            _make_cell(c2, prot, "given"),
        ])
        correct_map[c1] = act_name
        cell_hints[c1] = "Choose among: Labour Relations Act, Competition Act, or Companies Act."
        memo_lines.append(f"| {scenario} | {act_name} | {prot} |")

    worked = (
        f"**Completed Business Legislation Table ({case_firm}) [3 marks]:**\n\n"
        + "\n".join(memo_lines)
        + "\n\n- **Labour Relations Act:** governs employment, unions, and workplace disputes **[1]**.\n"
        "- **Competition Act:** stops cartels, price-fixing, and monopolies **[1]**.\n"
        "- **Companies Act:** governs company registration and corporate compliance **[1]**."
    )
    sample = "; ".join(f"{a[2]} -> {a[0]}" for a in acts)
    return _build_table(
        rng,
        qid_prefix="g8_gov_32",
        subskill="32_business_legislation_classification_table",
        title="South African Business Legislation Schedule",
        prompt=(
            f"Complete the compliance schedule for **{case_firm}** by entering the exact South African Act "
            "(**Labour Relations Act**, **Competition Act**, or **Companies Act**) governing each scenario."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Match worker disputes -> Labour; price-fixing -> Competition; registration/MOI -> Companies.",
            "tier_2": "Use exact names: Labour Relations Act, Competition Act, Companies Act.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Correct Act for row {i+1}: {acts[i][0]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["confusing_competition_act_with_companies_act"],
    )


def arch_33_labour_relations_act_worker_employer_balance(rng: random.Random) -> Dict[str, Any]:
    worker = rng.choice(PERSON_NAMES)
    biz = rng.choice(BUSINESS_NAMES)
    months = rng.choice([8, 14, 22, 30])
    prompt = (
        f"**{worker}** has worked at **{biz}** for **{months} months** with a clean disciplinary record, "
        f"and is dismissed immediately via text message with no warning or disciplinary hearing.\n\n"
        f"Which **Act** protects **{worker}**, and state **two ways** this legislation regulates fair treatment between employers and employees."
    )
    expected = (
        "The Labour Relations Act. 1) Prohibits unfair dismissal without due procedure; "
        "2) Sets guidelines for fair working conditions, collective bargaining, and peaceful dispute resolution."
    )
    sol = (
        f"**Labour Relations Act Case ({worker} at {biz}) [3 marks]:**\n\n"
        "1. **Legislation:** The **Labour Relations Act** **[1]**.\n"
        f"2. **Protections:** It prohibits **unfair dismissal** without a fair hearing **[1]**, and provides structured rules for **dispute resolution, union bargaining, and fair workplace practices** protecting both workers and employers **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_33",
        subskill="33_labour_relations_act_worker_employer_balance",
        title="Labour Relations Act: Fair Workplace Protection",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Which Act deals with employers, workers, dismissals, and trade unions?",
            "tier_2": "Name the Labour Relations Act and give two workplace protections it provides.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies Labour Relations Act", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Prevents unfair dismissal / requires fair hearing", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Establishes dispute resolution / fair working conditions / bargaining", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_labour_law_only_helps_employers"],
    )


def arch_34_competition_act_preventing_monopolies_and_price_fixing(rng: random.Random) -> Dict[str, Any]:
    product = rng.choice(["maize meal", "cement", "cooking oil", "school shoes"])
    price_a = rng.choice([28, 42, 65, 95])
    cartel_price = price_a + rng.choice([12, 18, 25])
    prompt = (
        f"Three dominant producers of **{product}** secretly agree to raise the wholesale price from **{_fmt_r(price_a)}** to **{_fmt_r(cartel_price)}** simultaneously "
        f"and threaten to block small competitors from accessing retail shelves.\n\n"
        f"Under South Africa's **Competition Act**, why is this agreement unlawful?"
    )
    correct = "It constitutes anti-competitive price-fixing and market abuse that harms consumers through inflated prices and crushes fair competition."
    distractors = [
        "It violates the Competition Act only because prices were raised on a Friday instead of Monday.",
        "Price-fixing is legal whenever large companies want higher profit margins.",
        "The Competition Act requires all rival firms in an industry to charge identical fixed prices.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_34",
        subskill="34_competition_act_preventing_monopolies_and_price_fixing",
        title="Competition Act: Stopping Price-Fixing & Monopolies",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Raising **{product}** prices from **{_fmt_r(price_a)}** to **{_fmt_r(cartel_price)}** via a cartel violates the **Competition Act**, "
            "which promotes fair competition so consumers enjoy fair prices and smaller businesses can compete."
        ),
        hints={
            "tier_1": "What happens to households and small rivals when big firms secretly fix prices together?",
            "tier_2": "Price-fixing and monopolistic exclusion are illegal under the Competition Act.",
            "tier_3": correct,
        },
        misconception_tags=["believing_price_fixing_is_legal_competition"],
    )


def arch_35_tax_revenue_collection_to_public_service_cycle(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    tax_collected = rng.choice([12000000, 18000000, 25000000, 32000000])
    prompt = (
        f"Residents and businesses in **{area}** contribute **{_fmt_r(tax_collected)}** in annual taxes to the state.\n\n"
        f"Trace the **three-step cycle** explaining how tax revenue collected from households and businesses returns to benefit society."
    )
    expected = (
        f"1) Households and businesses pay taxes (e.g. {_fmt_r(tax_collected)}) into National Treasury; "
        "2) Government allocates funds across National, Provincial, and Local budgets; "
        "3) Public services, infrastructure, and social grants are delivered back to households and firms."
    )
    sol = (
        f"**Tax-to-Service Cycle ({_fmt_r(tax_collected)}) [3 marks]:**\n\n"
        f"1. **Collection:** Households and businesses pay direct and indirect taxes into state revenue **[1]**.\n"
        "2. **Budget Allocation:** National Treasury allocates funds across National departments, Provinces, and Municipalities **[1]**.\n"
        "3. **Public Delivery:** Funds pay for schools, hospitals, roads, utilities, policing, and social grants that uplift citizens and enable business growth **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_35",
        subskill="35_tax_revenue_collection_to_public_service_cycle",
        title="From Tax Collection to Public Service Delivery",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Follow the Rand from taxpayer -> Treasury/spheres -> community services.",
            "tier_2": "Include collection, allocation across spheres, and delivery of services/grants.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Taxes collected from households and businesses", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Funds budgeted/distributed to spheres of government", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Returned as infrastructure, public services, and grants", "marks": 1, "editable": True},
        ],
        misconception_tags=["viewing_tax_as_money_lost_without_public_return"],
    )


def arch_36_circular_flow_with_government_role_diagram(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    tax_hh = rng.choice([450000, 620000, 810000])
    tender_amt = rng.choice([300000, 480000, 560000])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="250" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Three-Participant Economic Flow: {area}</text>'
        '<rect x="20" y="135" width="175" height="80" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="107" y="168" text-anchor="middle" font-size="13" font-weight="bold" fill="#78350f">Households</text>'
        '<text x="107" y="190" text-anchor="middle" font-size="11" fill="#92400e">(Labour &amp; Taxpayers)</text>'
        '<rect x="252" y="42" width="176" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="340" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Government</text>'
        '<text x="340" y="96" text-anchor="middle" font-size="11" fill="#1e40af">(Public Goods &amp; Regulator)</text>'
        '<rect x="485" y="135" width="175" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="572" y="168" text-anchor="middle" font-size="13" font-weight="bold" fill="#14532d">{biz}</text>'
        '<text x="572" y="190" text-anchor="middle" font-size="11" fill="#166534">(Businesses)</text>'
        '<line x1="150" y1="135" x2="252" y2="95" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="165" y="102" text-anchor="middle" font-size="10" font-weight="bold" fill="#0369a1">Taxes {_fmt_r(tax_hh)}</text>'
        '<line x1="428" y1="88" x2="530" y2="135" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="515" y="100" text-anchor="middle" font-size="10" font-weight="bold" fill="#15803d">Tender {_fmt_r(tender_amt)}</text>'
        '<line x1="195" y1="175" x2="485" y2="175" stroke="#475569" stroke-width="2"/>'
        '<text x="340" y="195" text-anchor="middle" font-size="11" fill="#334155">Labour &amp; Wages / Goods &amp; Spending</text>'
        '</svg>'
    )
    prompt = (
        f"Study the economic flow diagram for **{area}** showing **Households**, **Government**, and **{biz}**. "
        f"Households pay **{_fmt_r(tax_hh)}** in taxes while Government awards a **{_fmt_r(tender_amt)}** infrastructure tender to **{biz}**.\n\n"
        f"Using the diagram, state **what Government receives from Households** and **what Government supplies in return** to both Households and **{biz}**."
    )
    expected = (
        f"From Households: Taxes ({_fmt_r(tax_hh)}) and civil-servant labour. "
        f"In return to Households & {biz}: Public services, infrastructure, social grants, laws/regulation, and tender payments ({_fmt_r(tender_amt)})."
    )
    sol = (
        f"**Government in the Circular Flow ({area}) [4 marks]:**\n\n"
        f"1. **Received from Households:** Tax payments (**{_fmt_r(tax_hh)}**) **[1]** and **labour** from civil servants **[1]**.\n"
        f"2. **Supplied in Return:** **Public infrastructure/services & grants** for households and businesses **[1]**, plus **legislation and tender spending ({_fmt_r(tender_amt)})** paid to suppliers such as **{biz}** **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_36",
        subskill="36_circular_flow_with_government_role_diagram",
        title="Circular Flow: Households, Businesses & Government",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Look at the arrow between Households and Government, then Government and Businesses.",
            "tier_2": "Include taxes + labour going IN to Government, and public goods/tenders/grants coming OUT.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Taxes from households", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Labour / skills from civil servants", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Public goods, utilities, or social grants returned", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Tender spending / regulatory framework for businesses", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_government_from_circular_flow"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_37_sphere_responsibility_five_scenario_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pool = [
        ("Passing the National Budget and national tax laws", "National"),
        (f"Collecting weekly household refuse in {area}", "Local"),
        ("Managing provincial public hospitals and ambulance fleets", "Provincial"),
        ("Commanding the South African National Defence Force", "National"),
        (f"Fixing burst municipal water mains in {area}", "Local"),
        ("Running public provincial secondary schools", "Provincial"),
        ("Operating municipal traffic lights and street lighting", "Local"),
    ]
    chosen = rng.sample(pool, 5)
    headers = ["Public Task / Service", "Responsible Sphere (National / Provincial / Local)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Public Task / Service | Responsible Sphere |", "| :--- | :--- |"]
    for idx, (task, sphere) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([
            _make_cell(f"r{idx}c0", task, "given"),
            _make_cell(c1, "", "required"),
        ])
        correct_map[c1] = sphere
        cell_hints[c1] = "Enter National, Provincial, or Local."
        memo_lines.append(f"| {task} | {sphere} |")

    worked = "**Completed Sphere Responsibility Table [5 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{t} -> {s}" for t, s in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_gov_37",
        subskill="37_sphere_responsibility_five_scenario_table",
        title="Five-Scenario Sphere Classification Audit",
        prompt=f"Classify each public task affecting residents in **{area}** under the correct South African government sphere: **National**, **Provincial**, or **Local**.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Defence & national laws = National; schools & hospitals = Provincial; water, refuse, streetlights = Local.",
            "tier_2": "Type exactly: National, Provincial, or Local.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]} -> {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(5)
        ],
        misconception_tags=["mixing_municipal_and_national_responsibilities"],
    )


def arch_38_municipal_utility_rate_and_budget_calculation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    rates = rng.choice([4200000, 5600000, 6800000, 7400000])
    water_elec = rng.choice([3100000, 4400000, 5200000])
    equitable_grant = rng.choice([2500000, 3200000, 4100000])
    total_rev = rates + water_elec + equitable_grant
    operating_cost = rng.choice([7100000, 8200000, 8900000])
    if operating_cost >= total_rev:
        operating_cost = total_rev - 1500000
    surplus_capex = total_rev - operating_cost

    prompt = (
        f"The local municipality serving **{area}** records these annual figures:\n"
        f"- Property rates collected: **{_fmt_r(rates)}**\n"
        f"- Water and electricity service tariffs: **{_fmt_r(water_elec)}**\n"
        f"- Equitable share grant transferred from National Government: **{_fmt_r(equitable_grant)}**\n"
        f"- Salaries and routine maintenance costs: **{_fmt_r(operating_cost)}**\n\n"
        f"Calculate **(a)** the municipality's **total revenue**, and **(b)** how much money remains for **upgrading clinics and paving streets**."
    )
    expected = f"(a) Total revenue = {_fmt_r(total_rev)}; (b) Remaining funds for upgrades = {_fmt_r(surplus_capex)}"
    sol = (
        f"**Municipal Revenue & Capital Budget ({area}) [4 marks]:**\n\n"
        f"**(a) Total Revenue:**\n"
        f"$${_fmt_r(rates)} + {_fmt_r(water_elec)} + {_fmt_r(equitable_grant)} = {_fmt_r(total_rev)}$$ **[2]**\n\n"
        f"**(b) Remaining Capital Upgrade Funds:**\n"
        f"$${_fmt_r(total_rev)} - {_fmt_r(operating_cost)} = {_fmt_r(surplus_capex)}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_38",
        subskill="38_municipal_utility_rate_and_budget_calculation",
        title="Municipal Revenue & Infrastructure Surplus Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Add all three municipal income streams first (rates + tariffs + national transfer).",
            "tier_2": "Subtract salaries/maintenance from total revenue to find the upgrade balance.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct addition of revenue streams = {_fmt_r(total_rev)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Correct subtraction of operating costs = {_fmt_r(surplus_capex)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_national_grant_from_municipal_revenue"],
        qtype="calculation",
    )


def arch_39_economic_flow_producer_vs_consumer_summary_table(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    area = rng.choice(AREAS)
    rows = [
        [_make_cell("r0c0", f"Households ({area})", "given"), _make_cell("r0c1", "", "required"), _make_cell("r0c2", "", "required")],
        [_make_cell("r1c0", f"Businesses ({biz})", "given"), _make_cell("r1c1", "", "required"), _make_cell("r1c2", "", "required")],
        [_make_cell("r2c0", "Government", "given"), _make_cell("r2c1", "", "required"), _make_cell("r2c2", "", "required")],
    ]
    correct_map = {
        "r0c1": "Labour",
        "r0c2": "Goods, services and utilities",
        "r1c1": "Goods and services",
        "r1c2": "Labour, raw materials and utilities",
        "r2c1": "Public goods, utilities and infrastructure",
        "r2c2": "Civil-servant labour and business tenders",
    }
    cell_hints = {
        "r0c1": "What do workers offer to earn wages?",
        "r0c2": "What do families buy from shops and municipalities?",
        "r1c1": f"What does {biz} sell to customers and the state?",
        "r1c2": f"What inputs does {biz} hire or buy to produce?",
        "r2c1": "What does the state deliver to society?",
        "r2c2": "What does the state hire and buy via procurement?",
    }
    worked = (
        f"**Completed Economic Participants Matrix ({area} & {biz}) [6 marks]:**\n\n"
        "| Participant | Produces / Supplies | Consumes / Uses |\n"
        "| :--- | :--- | :--- |\n"
        f"| Households ({area}) | Labour | Goods, services and utilities |\n"
        f"| Businesses ({biz}) | Goods and services | Labour, raw materials and utilities |\n"
        "| Government | Public goods, utilities and infrastructure | Civil-servant labour and business tenders |"
    )
    sample = "Households produce Labour / consume Goods & utilities; Businesses produce Goods & services / consume Labour & materials; Government produces Public goods & infrastructure / consumes Labour & tenders."
    return _build_table(
        rng,
        qid_prefix="g8_gov_39",
        subskill="39_economic_flow_producer_vs_consumer_summary_table",
        title="Producer vs Consumer Matrix Across All 3 Participants",
        prompt=f"Complete the summary matrix showing what **Households in {area}**, **{biz}**, and **Government** each **produce** and **consume** in the South African economy.",
        headers=["Economic Participant", "Produces / Supplies", "Consumes / Purchases"],
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Every participant plays BOTH roles: supplier (producer) and user (consumer).",
            "tier_2": "Households supply labour; Businesses supply goods/services; Government supplies infrastructure/public goods.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Household producer and consumer roles", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Business producer and consumer roles", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Government producer and consumer roles", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_households_only_as_consumers"],
    )


def arch_40_direct_vs_indirect_government_economic_intervention(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    direct_item = rng.choice(["paying child-support social grants and subsidising brown bread", "operating Eskom power stations and Transnet rail lines"])
    indirect_item = rng.choice(["enforcing the Competition Act and upgrading highways", "providing SMME advisory clinics and passing workplace safety laws"])
    prompt = (
        f"In **{area}**, the state supports economic activity in two distinct ways:\n"
        f"- **Action 1:** {direct_item}\n"
        f"- **Action 2:** {indirect_item}\n\n"
        f"Which option accurately distinguishes **direct** from **indirect** government support?"
    )
    correct = "Action 1 is direct assistance/production through payments or SOEs; Action 2 is indirect support by creating infrastructure and fair rules."
    distractors = [
        "Both Action 1 and Action 2 are illegal under the Companies Act.",
        "Action 2 is direct cash distribution to households while Action 1 only affects parliamentarians.",
        "Neither action requires tax revenue or government employees.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_40",
        subskill="40_direct_vs_indirect_government_economic_intervention",
        title="Direct vs Indirect Government Economic Support",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Government intervenes **directly** via SOEs, grants, and food subsidies, and **indirectly** by maintaining infrastructure and passing fair business laws."
        ),
        hints={
            "tier_1": "Paying grants/subsidies or running an SOE puts public money/goods directly into hands; laws and roads create the environment.",
            "tier_2": "Action 1 = Direct; Action 2 = Indirect.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_direct_subsidies_with_regulatory_environment"],
    )


def arch_41_export_support_trade_and_business_competitiveness(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(BUSINESS_NAMES)
    port = rng.choice(["Durban Harbour", "Port of Cape Town", "Ngqura Container Terminal", "Richards Bay Harbour"])
    good = rng.choice(["bottled Rooibos tea", "solar water heaters", "automotive components", "citrus fruit"])
    prompt = (
        f"**{biz}** plans to export **{good}** through **{port}** to overseas buyers.\n\n"
        f"Give **two concrete ways** government infrastructure and trade/SMME support help **{biz}** become internationally competitive."
    )
    expected = (
        f"1) Upgrading physical infrastructure (harbours like {port}, freight rail, highways) lowers shipping delays and costs. "
        "2) Export advice, trade agreements, and start-up finance help local firms scale up production."
    )
    sol = (
        f"**Government Support for Exporting Firms ({biz}) [3 marks]:**\n\n"
        f"1. **Efficient Ports & Corridors:** Maintaining **{port}**, railways, and highways reduces export delays and logistics costs **[1.5]**.\n"
        "2. **Business Advice, Skills & Finance:** Trade facilitation, market advice, and finance help local companies reach international quality and volume standards **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_41",
        subskill="41_export_support_trade_and_business_competitiveness",
        title="How Government Boosts Export Competitiveness",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": f"Think about how goods physically reach {port} and what knowledge/funding exporters need.",
            "tier_2": "Combine port/transport infrastructure with trade advice/finance.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Port, rail, and road infrastructure reducing logistics cost/delay", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Business/trade advice or start-up finance", "marks": 1, "editable": True},
        ],
        misconception_tags=["ignoring_infrastructure_impact_on_exports"],
    )


def arch_42_service_delivery_failure_economic_consequences(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    failure = rng.choice(["three-day municipal water outage and uncollected refuse", "collapsed bridge and severe potholes on the main delivery road", "prolonged municipal substation failure causing blackouts"])
    prompt = (
        f"**{area}** experiences a **{failure}**, directly affecting local residents and **{biz}**.\n\n"
        f"Explain **one consequence for households** and **two consequences for businesses** like **{biz}**."
    )
    expected = (
        f"Households: health/sanitation risks and extra cost buying emergency water/fuel. "
        f"Businesses ({biz}): lost output/sales, damaged stock/equipment, higher costs, and potential job losses."
    )
    sol = (
        f"**Economic Impact of Service Delivery Failure ({area}) [3 marks]:**\n\n"
        "1. **For Households:** Reduced dignity/health risks and higher living costs to replace basic utilities **[1]**.\n"
        f"2. **For {biz}:** Production halts or delayed deliveries reduce revenue **[1]**, while spoiled stock/repair costs may force staff layoffs **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_42",
        subskill="42_service_delivery_failure_economic_consequences",
        title="Economic Impact of Municipal Service Failure",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Separate the harm to families at home from the financial/operational harm to firms.",
            "tier_2": "Consider health/cost for households, and lost sales/spoiled stock/jobs for businesses.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Valid consequence for households (health, cost, lost wages)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "First valid consequence for business (halted production/lost revenue)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Second valid consequence for business (higher cost/spoiled stock/job cuts)", "marks": 1, "editable": True},
        ],
        misconception_tags=["underestimating_business_losses_from_municipal_outages"],
    )


def arch_43_rural_vs_urban_infrastructure_equity(rng: random.Random) -> Dict[str, Any]:
    rural_town = rng.choice(["Lusikisiki", "Giyani", "Nongoma", "Springbok"])
    urban_city = rng.choice(["Sandton", "Cape Town", "Umhlanga"])
    prompt = (
        f"Families in **{urban_city}** enjoy tarred roads and indoor piped water, while many households near **{rural_town}** still walk far to fetch water and face gravel roads.\n\n"
        f"Why must National and Provincial funding prioritise infrastructure in underdeveloped areas like **{rural_town}**?"
    )
    correct = "To address inequality so rural residents enjoy constitutional access to safe water, healthcare, education, and local economic opportunity."
    distractors = [
        "Because rural towns pay 90% of corporate income tax while cities pay zero taxes.",
        "Because Local Government in cities is prohibited from collecting property rates.",
        "So that rural residents must relocate permanently to metropolitan skyscrapers.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_43",
        subskill="43_rural_vs_urban_infrastructure_equity",
        title="Bridging Rural-Urban Infrastructure Inequality",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Targeted National and Provincial transfers narrow South Africa's **economic diversity and inequality gap**, helping towns like **{rural_town}** gain basic utilities, clinics, and roads."
        ),
        hints={
            "tier_1": "Think of the unequal access between wealthy urban suburbs and poorer rural municipalities.",
            "tier_2": "Redistributing funding promotes basic constitutional rights and rural job growth.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_municipalities_keep_all_national_taxes"],
    )


def arch_44_intergovernmental_disaster_and_crisis_coordination(rng: random.Random) -> Dict[str, Any]:
    province = rng.choice(["KwaZulu-Natal", "Eastern Cape", "Western Cape", "Limpopo"])
    disaster = rng.choice(["severe coastal flooding", "a destructive wildfire", "widespread agricultural drought"])
    prompt = (
        f"When **{disaster}** strikes districts in **{province}**, explain how **all three spheres of government** (Local, Provincial, and National) cooperate to respond."
    )
    expected = (
        "Local municipalities provide immediate rescue, shelter, and repair local water/roads; "
        f"{province} Provincial government coordinates provincial hospitals, schools, and regional roads; "
        "National Government releases emergency funds, SANDF/SAPS support, and national relief coordination."
    )
    sol = (
        f"**Coordinated Disaster Response ({province}) [3 marks]:**\n\n"
        "1. **Local Municipality:** Immediate fire/rescue response, emergency water/shelter, and repairing local streets/pipes **[1]**.\n"
        f"2. **Provincial Government ({province}):** Mobilising provincial clinics/hospitals, ambulances, schools, and regional roads **[1]**.\n"
        "3. **National Government:** Releasing national **emergency disaster funding** and deploying national security/SANDF/SAPS logistical support **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_44",
        subskill="44_intergovernmental_disaster_and_crisis_coordination",
        title="Three-Sphere Disaster Coordination",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Give one distinct crisis duty for Local, one for Provincial, and one for National.",
            "tier_2": "Local = immediate water/rescue; Provincial = hospitals/regional roads; National = emergency money & SANDF.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Local sphere immediate rescue/utilities", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Provincial sphere hospitals/regional relief", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "National sphere emergency funding / national security forces", "marks": 1, "editable": True},
        ],
        misconception_tags=["believing_only_one_sphere_acts_in_disasters"],
    )


def arch_45_separation_of_powers_checks_and_balances(rng: random.Random) -> Dict[str, Any]:
    case_action = rng.choice([
        "the President attempts to imprison a journalist without a court trial",
        "a Cabinet Minister tries to rewrite a statute passed by Parliament without parliamentary vote",
        "the Executive refuses to obey an order issued by the Constitutional Court",
    ])
    prompt = (
        f"Suppose **{case_action}**.\n\n"
        f"How does the constitutional principle of **separation of powers** among National government's three branches prevent abuse of state power here?"
    )
    correct = "The Legislative (makes laws), Executive (administers laws), and Judicial (independent courts enforcing the Constitution) branches check and balance one another."
    distractors = [
        "The Mayor of the nearest city overrules the Constitutional Court using municipal by-laws.",
        "All three branches merge into one single Cabinet Minister during any dispute.",
        "Parliament personally sentences citizens to prison without involving any judges.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_45",
        subskill="45_separation_of_powers_checks_and_balances",
        title="Separation of Powers: Checks & Balances",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Under the **separation of powers**, **Parliament** (Legislative) makes laws, the **President & Cabinet** (Executive) govern, and **independent Courts** (Judicial) strike down unconstitutional acts."
        ),
        hints={
            "tier_1": "Think about why Parliament, Cabinet, and the Courts are kept independent of each other.",
            "tier_2": "Each branch limits excess power by the other two branches.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_executive_controls_courts"],
    )


def arch_46_public_goods_vs_private_goods_comparison(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pub_good = rng.choice(["streetlights along residential roads", "national defence and neighbourhood SAPS policing", "public storm-water drainage canals"])
    priv_good = rng.choice(["a smartphone or loaf of artisan bread", "a pair of running shoes", "a private cinema ticket"])
    prompt = (
        f"In **{area}**, households buy **{priv_good}** from retail businesses, whereas government supplies **{pub_good}** out of tax revenue.\n\n"
        f"Explain **why private businesses generally do not supply {pub_good}** for profit, and why Government funds them instead."
    )
    expected = (
        f"Once {pub_good} exists, everyone benefits without easily paying per use (non-profit/essential public good). "
        "Therefore private firms cannot charge each passer-by profitably, so Government provides it non-profit out of taxes."
    )
    sol = (
        f"**Why Government Supplies Public Goods ({area}) [3 marks]:**\n\n"
        f"1. **No Easy Profit / Direct Fee:** Unlike **{priv_good}**, businesses cannot easily restrict **{pub_good}** only to paying buyers or charge per minute **[1.5]**.\n"
        "2. **Collective Benefit:** Government provides essential public goods **non-profit** using tax revenue so every household and business stays safe and productive **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_46",
        subskill="46_public_goods_vs_private_goods_comparison",
        title="Why Public Goods Are Funded via Taxation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Can a shop owner sell one streetlight beam only to people who swipe a bank card on the pavement?",
            "tier_2": "Mention that private companies seek profit and cannot easily charge per individual user for public goods.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Explains difficulty charging individual users / low commercial profit incentive", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Government funds essential public goods non-profit from taxes", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_every_essential_service_can_be_profitable_privately"],
    )


def arch_47_government_tender_multiplier_and_employment_calc(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    tender_val = rng.choice([1200000, 1500000, 1800000, 2400000])
    mat_pct = rng.choice([45, 50, 55, 60])
    workers = rng.choice([20, 25, 30])
    material_spend = tender_val * mat_pct // 100
    wage_pool = tender_val - material_spend
    wage_per_worker = wage_pool // workers
    # Ensure exact integer division cleanly:
    while wage_pool % workers != 0:
        workers += 1
        wage_per_worker = wage_pool // workers

    prompt = (
        f"A municipality near **{area}** awards a **{_fmt_r(tender_val)}** pavement-repair tender to **{biz}**.\n"
        f"**{mat_pct}%** of the contract pays for local bricks and cement, while the remainder funds wages equally for **{workers}** local workers.\n\n"
        f"Calculate:\n"
        f"(a) The amount spent on local **materials**;\n"
        f"(b) The total **wage pool** paid to workers;\n"
        f"(c) The total wage **earned per local worker**."
    )
    expected = (
        f"(a) Materials = {_fmt_r(material_spend)}; "
        f"(b) Wage pool = {_fmt_r(wage_pool)}; "
        f"(c) Wage per worker = {_fmt_r(wage_per_worker)}"
    )
    sol = (
        f"**Local Tender Multiplier Breakdown ({biz}) [4 marks]:**\n\n"
        f"**(a) Local Materials ({mat_pct}%):**\n"
        f"$${_fmt_r(tender_val)} \\times {mat_pct}\\% = {_fmt_r(material_spend)}$$ **[1]**\n\n"
        f"**(b) Total Wage Pool:**\n"
        f"$${_fmt_r(tender_val)} - {_fmt_r(material_spend)} = {_fmt_r(wage_pool)}$$ **[1]**\n\n"
        f"**(c) Earnings per Worker ({workers} workers):**\n"
        f"$${_fmt_r(wage_pool)} \\div {workers} = {_fmt_r(wage_per_worker)}$$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_47",
        subskill="47_government_tender_multiplier_and_employment_calc",
        title="Public Tender Economic Impact Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Start by taking {mat_pct}% of {_fmt_r(tender_val)} for bricks and cement.",
            "tier_2": f"Subtract materials from {_fmt_r(tender_val)} to get total wages, then divide by {workers}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Materials = {_fmt_r(material_spend)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Wage pool = {_fmt_r(wage_pool)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Wage per worker = {_fmt_r(wage_per_worker)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["percentage_split_arithmetic_error"],
        qtype="calculation",
    )


def arch_48_civic_tax_compliance_and_municipal_rates_duty(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pct_unpaid = rng.choice([28, 35, 42])
    prompt = (
        f"In **{area}**, **{pct_unpaid}%** of property owners stop paying municipal water tariffs and property rates.\n\n"
        f"Explain why widespread non-payment of rates and taxes eventually harms **even the residents and businesses** who refused to pay."
    )
    expected = (
        f"When {pct_unpaid}% do not pay rates/tariffs, municipal revenue drops sharply, leaving no funds to buy bulk water, "
        "maintain roads, clear refuse, or service electricity transformers—causing service collapses that hurt everyone."
    )
    sol = (
        f"**Civic Responsibility & Municipal Sustainability ({area}) [3 marks]:**\n\n"
        f"1. **Revenue Collapse:** When **{pct_unpaid}%** of ratepayers withhold tariffs, the municipality loses cash needed for bulk water/electricity purchases **[1]**.\n"
        "2. **Infrastructure Deterioration:** Roads develop potholes, refuse piles up, and substations fail without maintenance **[1]**.\n"
        "3. **Shared Harm:** Declining services drive away customers and jobs, lowering living standards for all residents **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_48",
        subskill="48_civic_tax_compliance_and_municipal_rates_duty",
        title="Tax & Municipal Rates Compliance Responsibility",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Where does a municipality get the money to buy bulk electricity/water and fix roads?",
            "tier_2": "Connect unpaid rates -> budget shortfall -> broken utilities -> harm to local families and businesses.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Loss of municipal revenue for bulk utilities", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Degradation of roads, refuse collection, and power maintenance", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Harm to households and local business survival/employment", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_municipal_services_cost_nothing_to_provide"],
    )


def arch_49_sphere_and_branch_misallocation_audit(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    errors = [
        ("The Ward Councillor writes new national criminal laws for all 9 provinces.", "Parliament (Legislative)"),
        (f"The Chief Justice collects refuse and sweeps streets in {area}.", "Local Municipality"),
        ("A Municipal Mayor leads the provincial hospital budget in the legislature.", "Premier and MECs (Provincial)"),
        ("Parliament sends police officers directly to arrest jaywalkers in town.", "Executive / SAPS / Local"),
    ]
    chosen = rng.sample(errors, 3)
    headers = ["Incorrect Briefing Statement", "Correct Authority / Body Responsible"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Incorrect Briefing Statement | Correct Authority / Body Responsible |", "| :--- | :--- |"]
    for idx, (stmt, fix) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([
            _make_cell(f"r{idx}c0", stmt, "given"),
            _make_cell(c1, "", "required"),
        ])
        correct_map[c1] = fix
        cell_hints[c1] = "Name the actual SA institution, sphere, or branch responsible."
        memo_lines.append(f"| {stmt} | {fix} |")

    worked = "**Completed Governance Audit Schedule [3 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{s} -> {f}" for s, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_gov_49",
        subskill="49_sphere_and_branch_misallocation_audit",
        title="Governance Role Misallocation Audit",
        prompt=f"Each statement from a community flyer in **{area}** names the wrong authority. Enter the **correct South African authority, sphere, or branch** responsible in each row.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=3,
        hints={
            "tier_1": "Check whether the task belongs to Parliament, Premier/MECs, Local Municipality, or SAPS/Executive.",
            "tier_2": "Match lawmaking -> Parliament; hospitals -> Provincial; refuse -> Local Municipality.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Corrected authority row {i+1}: {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["confusing_national_branches_with_local_councils"],
    )


def arch_50_holistic_sa_government_economic_ecosystem_synthesis(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(BUSINESS_NAMES)
    owner = rng.choice(PERSON_NAMES)
    grant_val = rng.choice([90000, 140000, 180000])
    prompt = (
        f"**Case Study ({area}):**\n"
        f"**{owner}** receives **{_fmt_r(grant_val)}** in government SMME support to launch **{biz}**, hiring 12 local workers.\n"
        f"Workers commute on paved provincial/municipal roads, use clean municipal water, pay income taxes, and are protected by national labour laws, while **{biz}** later wins a municipal clinic supply tender.\n\n"
        f"Synthesise this case by answering all three parts:\n"
        f"1. Identify **two distinct infrastructure categories** supporting **{biz}** and its workers.\n"
        f"2. Name **two spheres of government** involved and give **one specific action** each performs in the case.\n"
        f"3. Explain how **Government acts as both Producer and Consumer** in **{biz}**'s ecosystem."
    )
    expected = (
        "1) Physical infrastructure (roads) and Utility/Service infrastructure (municipal water / clinic).\n"
        "2) Local Municipality (water, local roads, clinic tender) and Provincial/National (SMME finance, provincial roads, labour law).\n"
        "3) Producer: provides roads, water, clinic services, SMME finance, and laws; Consumer: hires civil servants and purchases supplies from "
        f"{biz} via the tender."
    )
    sol = (
        f"**Holistic Government Ecosystem Synthesis ({biz}, {area}) [6 marks]:**\n\n"
        "1. **Infrastructure Categories [2 marks]:**\n"
        "   - **Physical infrastructure:** paved roads for worker transport **[1]**.\n"
        "   - **Utility / Service infrastructure:** clean municipal water (**utility**) and public clinic (**service**) **[1]**.\n"
        "2. **Two Spheres & Specific Actions [2 marks]:**\n"
        "   - **Local Municipality:** supplies clean water, local streets, and awards the clinic supply tender **[1]**.\n"
        "   - **National / Provincial Government:** enforces labour laws, provides SMME start-up grant, and maintains provincial arterial roads **[1]**.\n"
        "3. **Dual Economic Role [2 marks]:**\n"
        "   - **Producer:** delivers infrastructure, clean water, healthcare, labour protection, and SMME support **[1]**.\n"
        f"   - **Consumer:** buys goods/services from **{biz}** via the clinic tender and employs public-sector workers **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_50",
        subskill="50_holistic_sa_government_economic_ecosystem_synthesis",
        title="Holistic SA Government & Economy Case Synthesis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Work carefully through the 3 numbered prompts using exact EMS categories.",
            "tier_2": "Pair roads (physical) + water/clinic (utility/service); cite two spheres; show Producer + Consumer roles.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Identifies two valid infrastructure types from case", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Names two spheres with accurate case actions", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Explains Government as both Producer and Consumer", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_multi_sphere_interdependence"],
        qtype="extended_response",
    )


BUILDERS_26_50 = {
    "26_smme_support_skills_and_startup_finance": arch_26_smme_support_skills_and_startup_finance,
    "27_government_tenders_and_procurement_from_businesses": arch_27_government_tenders_and_procurement_from_businesses,
    "28_physical_infrastructure_roads_ports_railways": arch_28_physical_infrastructure_roads_ports_railways,
    "29_service_infrastructure_police_fire_health": arch_29_service_infrastructure_police_fire_health,
    "30_utility_infrastructure_electricity_water_sewerage": arch_30_utility_infrastructure_electricity_water_sewerage,
    "31_natural_resource_protection_and_sustainability": arch_31_natural_resource_protection_and_sustainability,
    "32_business_legislation_classification_table": arch_32_business_legislation_classification_table,
    "33_labour_relations_act_worker_employer_balance": arch_33_labour_relations_act_worker_employer_balance,
    "34_competition_act_preventing_monopolies_and_price_fixing": arch_34_competition_act_preventing_monopolies_and_price_fixing,
    "35_tax_revenue_collection_to_public_service_cycle": arch_35_tax_revenue_collection_to_public_service_cycle,
    "36_circular_flow_with_government_role_diagram": arch_36_circular_flow_with_government_role_diagram,
    "37_sphere_responsibility_five_scenario_table": arch_37_sphere_responsibility_five_scenario_table,
    "38_municipal_utility_rate_and_budget_calculation": arch_38_municipal_utility_rate_and_budget_calculation,
    "39_economic_flow_producer_vs_consumer_summary_table": arch_39_economic_flow_producer_vs_consumer_summary_table,
    "40_direct_vs_indirect_government_economic_intervention": arch_40_direct_vs_indirect_government_economic_intervention,
    "41_export_support_trade_and_business_competitiveness": arch_41_export_support_trade_and_business_competitiveness,
    "42_service_delivery_failure_economic_consequences": arch_42_service_delivery_failure_economic_consequences,
    "43_rural_vs_urban_infrastructure_equity": arch_43_rural_vs_urban_infrastructure_equity,
    "44_intergovernmental_disaster_and_crisis_coordination": arch_44_intergovernmental_disaster_and_crisis_coordination,
    "45_separation_of_powers_checks_and_balances": arch_45_separation_of_powers_checks_and_balances,
    "46_public_goods_vs_private_goods_comparison": arch_46_public_goods_vs_private_goods_comparison,
    "47_government_tender_multiplier_and_employment_calc": arch_47_government_tender_multiplier_and_employment_calc,
    "48_civic_tax_compliance_and_municipal_rates_duty": arch_48_civic_tax_compliance_and_municipal_rates_duty,
    "49_sphere_and_branch_misallocation_audit": arch_49_sphere_and_branch_misallocation_audit,
    "50_holistic_sa_government_economic_ecosystem_synthesis": arch_50_holistic_sa_government_economic_ecosystem_synthesis,
}
