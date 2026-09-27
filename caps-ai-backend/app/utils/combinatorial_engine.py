"""Fundile Learning - 4D Combinatorial Slot-Filling Engine
Enables near-infinite (> 80,000 permutations per subskill) deterministic question generation
for Business Studies, EMS, and conceptual Sciences.

Zero LLM dependencies. 100% pure deterministic Python. Cyclomatic complexity <= 12 per function.
Satisfies the Universal 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# DIMENSION 1: Authentic South African Economic Sectors & Enterprises (20)
# ============================================================================
SA_SECTORS: List[Dict[str, str]] = [
    {"sector": "Renewable Energy & Solar EPC", "province": "Northern Cape", "location": "Upington", "product": "commercial solar arrays"},
    {"sector": "Township FMCG & Spaza Retail", "province": "Gauteng", "location": "Soweto", "product": "daily grocery staples"},
    {"sector": "Automotive Component Manufacturing", "province": "Eastern Cape", "location": "Gqeberha", "product": "catalytic converters"},
    {"sector": "Citrus Farming & Cold-Chain Export", "province": "Limpopo", "location": "Tzaneen", "product": "navel oranges for export"},
    {"sector": "Fintech & Mobile Remittance", "province": "Western Cape", "location": "Cape Town", "product": "low-cost digital payment wallets"},
    {"sector": "Deep-Level Gold & Platinum Mining", "province": "North West", "location": "Rustenburg", "product": "refined platinum group metals"},
    {"sector": "Wine Viticulture & Ecotourism", "province": "Western Cape", "location": "Stellenbosch", "product": "estate wines and cellar tours"},
    {"sector": "Timber & Sustainable Forestry", "province": "Mpumalanga", "location": "Nelspruit", "product": "treated structural timber"},
    {"sector": "Harbour Container Logistics", "province": "KwaZulu-Natal", "location": "Durban", "product": "freight forwarding and drayage"},
    {"sector": "Textile & Workwear Apparel", "province": "KwaZulu-Natal", "location": "Newcastle", "product": "industrial protective overalls"},
    {"sector": "Poultry & Feed Milling", "province": "Free State", "location": "Parys", "product": "fresh broiler chicken packs"},
    {"sector": "Pharmaceutical & Generic Medicines", "province": "Gauteng", "location": "Midrand", "product": "chronic hypertension medication"},
    {"sector": "E-Commerce On-Demand Delivery", "province": "Gauteng", "location": "Johannesburg", "product": "same-day parcels by electric scooters"},
    {"sector": "Marine Fisheries & Cold Storage", "province": "Western Cape", "location": "Saldanha Bay", "product": "sustainably caught hake fillets"},
    {"sector": "Speciality Coffee Roasting", "province": "KwaZulu-Natal", "location": "Durban North", "product": "artisan single-origin beans"},
    {"sector": "Plastic Recycling & Extrusion", "province": "Gauteng", "location": "Germiston", "product": "recycled polymer pellets"},
    {"sector": "Dairy Farming & Processing", "province": "Eastern Cape", "location": "Tsitsikamma", "product": "pasteurised milk and gouda cheese"},
    {"sector": "Commercial Aviation & Cargo Handling", "province": "Gauteng", "location": "Kempton Park", "product": "cold-chain airfreight logistics"},
    {"sector": "Software Engineering & Cloud Services", "province": "Western Cape", "location": "Century City", "product": "enterprise ERP platforms"},
    {"sector": "Eco-Friendly Brick & Tile Manufacturing", "province": "Free State", "location": "Bloemfontein", "product": "compressed clay paving pavers"},
]

# ============================================================================
# DIMENSION 2: Forms of Ownership & Enterprise Scales (6)
# ============================================================================
ENTERPRISE_FORMS: List[Dict[str, Any]] = [
    {
        "form": "Sole Trader",
        "legal_personality": False,
        "liability": "unlimited personal liability",
        "taxation": "taxed at individual progressive income tax rates",
        "continuity": "no perpetual succession; ceases upon death or insolvency of owner",
        "capital_source": "owner's personal savings or informal loans",
        "suffix": "",
    },
    {
        "form": "Partnership",
        "legal_personality": False,
        "liability": "joint and several unlimited liability for partnership debts",
        "taxation": "partners taxed individually on their profit shares",
        "continuity": "dissolves upon retirement, death, or insolvency of any partner",
        "capital_source": "capital contributions of 2 to 20 partners",
        "suffix": "& Partners",
    },
    {
        "form": "Private Company",
        "legal_personality": True,
        "liability": "limited liability for shareholders",
        "taxation": "subject to standard corporate income tax (27%)",
        "continuity": "perpetual succession; existence unaffected by shareholder changes",
        "capital_source": "private equity from up to 50 private shareholders (no public shares)",
        "suffix": "(Pty) Ltd",
    },
    {
        "form": "Public Company",
        "legal_personality": True,
        "liability": "limited liability for all shareholders",
        "taxation": "subject to corporate income tax (27%) and dividends tax",
        "continuity": "full perpetual succession",
        "capital_source": "public share issuance on the Johannesburg Stock Exchange (JSE)",
        "suffix": "Ltd",
    },
    {
        "form": "State-Owned Company",
        "legal_personality": True,
        "liability": "state-backed limited liability",
        "taxation": "governed by Public Finance Management Act (PFMA)",
        "continuity": "perpetual succession under relevant government ministry",
        "capital_source": "government capital appropriations, public bonds, and tariffs",
        "suffix": "SOC Ltd",
    },
    {
        "form": "Close Corporation",
        "legal_personality": True,
        "liability": "limited liability for members (subject to reckless trading exemptions)",
        "taxation": "taxed as a corporate entity (27%)",
        "continuity": "perpetual succession; members hold percentage member's interest",
        "capital_source": "member contributions from 1 to 10 natural persons (closed to new regs)",
        "suffix": "CC",
    },
]

# ============================================================================
# DIMENSION 3: Macro & Market Economic Shocks / Events (15)
# ============================================================================
ECONOMIC_EVENTS: List[Dict[str, str]] = [
    {
        "event": "South African Reserve Bank (SARB) 75 basis-point repo rate hike",
        "environment": "macro",
        "pes_factor": "economic",
        "direct_impact": "commercial bank prime lending rates rise, increasing interest costs on overdrafts and dampening consumer credit demand",
        "strategic_response": "retire variable-rate short-term debt, offer cash settlement discounts, and negotiate fixed-rate supplier financing",
    },
    {
        "event": "Depreciation of the South African Rand against the US Dollar (R19,20/$)",
        "environment": "macro",
        "pes_factor": "economic",
        "direct_impact": "imported raw material and fuel costs rise significantly, squeezing gross profit margins for import-dependent firms",
        "strategic_response": "source substitute inputs from local Southern African suppliers and implement forward exchange contracts (FECs)",
    },
    {
        "event": "Implementation of Stage 4 Eskom load curtailment across industrial nodes",
        "environment": "macro",
        "pes_factor": "physical/technological",
        "direct_impact": "factory production runs are abruptly interrupted, reducing machinery utilization and increasing diesel generator expenses",
        "strategic_response": "invest in commercial rooftop solar PV arrays with battery backup, and reschedule shifts to off-peak tariff periods",
    },
    {
        "event": "Aggressive price-undercutting campaign launched by a new multinational entrant",
        "environment": "market",
        "pes_factor": "competition",
        "direct_impact": "existing market share is threatened as price-sensitive consumers switch to the subsidized entrant",
        "strategic_response": "differentiate through superior localized customer service, loyalty rewards, and targeted product quality guarantees",
    },
    {
        "event": "Prolonged port congestion and container berth delays at Durban harbour",
        "environment": "market",
        "pes_factor": "intermediaries/suppliers",
        "direct_impact": "crucial production components are stuck offshore, risking factory line shutdowns and delayed customer order fulfillment",
        "strategic_response": "increase safety buffer stock levels and diversify logistics routes through Maputo or Gqeberha ports",
    },
    {
        "event": "Bargaining council wage agreement mandating an 8.5% industry-wide minimum wage increase",
        "environment": "macro",
        "pes_factor": "socio-economic/legal",
        "direct_impact": "direct labour costs rise across the production and warehousing operations",
        "strategic_response": "up-skill workers through SETA accredited training to lift productivity, and automate repetitive manual packaging",
    },
    {
        "event": "Gazetting of updated Broad-Based Black Economic Empowerment (B-BBEE) sector codes",
        "environment": "macro",
        "pes_factor": "legal/political",
        "direct_impact": "suppliers with low B-BBEE recognition levels risk losing tenders from government and corporate clients",
        "strategic_response": "accelerate enterprise and supplier development (ESD) partnerships with black-owned emerging micro-enterprises",
    },
    {
        "event": "Consumer Protection Act (CPA) complaint regarding product return policies",
        "environment": "market",
        "pes_factor": "consumers/legal",
        "direct_impact": "dissatisfied consumers exercise statutory 6-month implied warranty rights, demanding full refunds on defective goods",
        "strategic_response": "tighten Total Quality Management (TQM) incoming inspection, and retrain retail staff on CPA section 55 and 56 compliance",
    },
    {
        "event": "Major domestic water supply quota reduction due to persistent provincial drought",
        "environment": "macro",
        "pes_factor": "environmental/physical",
        "direct_impact": "water-intensive industrial washing and cooling processes face severe volume restrictions and municipal penalty surcharges",
        "strategic_response": "commission on-site closed-loop greywater recycling plants and install high-efficiency rainwater retention tanks",
    },
    {
        "event": "Spike in national fuel levy and Road Accident Fund (RAF) fuel price surcharges",
        "environment": "macro",
        "pes_factor": "economic",
        "direct_impact": "fleet distribution and delivery costs jump, driving up operating expenses and carriage on sales",
        "strategic_response": "optimize fleet delivery routing using telematics GPS algorithms, and consolidate small customer shipments",
    },
    {
        "event": "National trade union declares a protected strike over annual bonus structuring",
        "environment": "market",
        "pes_factor": "trade unions/labour",
        "direct_impact": "factory floor operations cease for two weeks, resulting in unfulfilled supply contracts and lost revenue",
        "strategic_response": "engage in proactive collective bargaining via CCMA mediation and establish transparent performance-linked profit sharing",
    },
    {
        "event": "Launch of a disruptive direct-to-consumer mobile shopping application by an intermediary",
        "environment": "market",
        "pes_factor": "intermediaries",
        "direct_impact": "traditional brick-and-mortar retail distribution channels experience reduced footfall and inventory turnover",
        "strategic_response": "adopt an omnichannel strategy with seamless online ordering, in-store collection, and personalized digital coupons",
    },
    {
        "event": "Department of Employment and Labour gazettes revised occupational health inspection rules (COIDA)",
        "environment": "macro",
        "pes_factor": "legal",
        "direct_impact": "mandatory quarterly ergonomics and safety audits require documented standard operating procedures (SOPs)",
        "strategic_response": "appoint certified workplace safety representatives and conduct regular staff hazard identification and risk assessments (HIRA)",
    },
    {
        "event": "Wholesale supplier experiences unexpected corporate liquidation and freezes trade credit",
        "environment": "market",
        "pes_factor": "suppliers",
        "direct_impact": "essential raw material deliveries freeze immediately with outstanding supply invoices disputed",
        "strategic_response": "activate backup approved vendors and establish flexible 30-day revolving credit lines with alternative suppliers",
    },
    {
        "event": "Surge in cyber ransomware attacks targeting mid-tier South African commercial databases",
        "environment": "macro",
        "pes_factor": "technological",
        "direct_impact": "customer billing and proprietary stock records risk corruption or extortion under POPIA data protection rules",
        "strategic_response": "deploy multi-factor authentication (MFA), immutable encrypted off-site cloud backups, and regular staff phishing drills",
    },
]

# ============================================================================
# DIMENSION 4: Statutory & Theoretical Framework Probes (12)
# ============================================================================
STATUTORY_FRAMEWORKS: List[Dict[str, str]] = [
    {
        "framework": "Basic Conditions of Employment Act (BCEA)",
        "core_purpose": "sets minimum floors for working hours, overtime pay, annual/maternity leave, and termination notice periods",
        "misconception_tag": "bcea_vs_lra_confusion",
    },
    {
        "framework": "Labour Relations Act (LRA)",
        "core_purpose": "governs collective bargaining, formation of trade unions, workplace forums, dispute resolution via CCMA, and legal strike procedures",
        "misconception_tag": "lra_vs_bcea_confusion",
    },
    {
        "framework": "Employment Equity Act (EEA)",
        "core_purpose": "eliminates unfair discrimination in the workplace and requires affirmative action measures to ensure equitable demographic representation",
        "misconception_tag": "eea_vs_bbbee_confusion",
    },
    {
        "framework": "Broad-Based Black Economic Empowerment (B-BBEE) Act",
        "core_purpose": "promotes economic transformation through scorecard pillars: ownership, management control, skills development, enterprise development, and socio-economic development",
        "misconception_tag": "bbbee_vs_eea_confusion",
    },
    {
        "framework": "Consumer Protection Act (CPA)",
        "core_purpose": "protects consumer rights to fair value, good quality and safety, disclosure of information, and choice without deceptive marketing",
        "misconception_tag": "consumer_rights_inversion",
    },
    {
        "framework": "Compensation for Occupational Injuries and Diseases Act (COIDA)",
        "core_purpose": "provides statutory financial compensation for employees injured or contracted illnesses in the course of employment, replacing civil liability",
        "misconception_tag": "coida_vs_uif_confusion",
    },
    {
        "framework": "King IV Code of Corporate Governance",
        "core_purpose": "outlines principles of ethical leadership, transparency, accountability, and sustainable stakeholder inclusivity for governing bodies",
        "misconception_tag": "ethics_vs_legal_compliance_confusion",
    },
    {
        "framework": "Porter's Five Forces Model",
        "core_purpose": "analyzes market environment attractiveness via: threat of new entrants, bargaining power of buyers, bargaining power of suppliers, threat of substitutes, and competitive rivalry",
        "misconception_tag": "porters_vs_swot_confusion",
    },
    {
        "framework": "PESTLE Macro Environmental Framework",
        "core_purpose": "systematically identifies external challenges across Political, Economic, Social, Technological, Legal, and Environmental dimensions",
        "misconception_tag": "macro_vs_market_confusion",
    },
    {
        "framework": "Total Quality Management (TQM)",
        "core_purpose": "continuous enterprise-wide improvement aimed at zero defects, customer satisfaction, employee involvement, and reduced costs of quality",
        "misconception_tag": "quality_control_vs_assurance_confusion",
    },
    {
        "framework": "The Eight Business Functions",
        "core_purpose": "coordinates enterprise operations: General Management, Financial, Purchasing, Production, Marketing, Public Relations, Human Resources, and Administration",
        "misconception_tag": "business_function_misclassification",
    },
    {
        "framework": "Corporate Social Responsibility (CSR) & CSI",
        "core_purpose": "enterprise initiatives contributing positively to community development, education, environmental restoration, and socio-economic upliftment beyond profit",
        "misconception_tag": "csr_vs_commercial_marketing_confusion",
    },
]

try:
    from .sa_naming_engine import generate_sa_person, generate_sa_enterprise
except ImportError:
    from app.utils.sa_naming_engine import generate_sa_person, generate_sa_enterprise


# ============================================================================
# CORE GENERATION ENGINE: 4-Dimensional Permutation Factory
# ============================================================================

def sample_scenario(r: random.Random) -> Dict[str, Any]:
    """Generates an authentic South African business scenario with 4 dimensions."""
    sector = r.choice(SA_SECTORS)
    form = r.choice(ENTERPRISE_FORMS)
    event = r.choice(ECONOMIC_EVENTS)
    framework = r.choice(STATUTORY_FRAMEWORKS)

    founder_data = generate_sa_person(r)
    founder = founder_data["full_name"]
    first = founder_data["first_name"]
    surname = founder_data["surname"]

    naming_style = r.choice(["possessive", "surname_trade", "regional"])
    if naming_style == "possessive" or form["form"] == "Sole Trader":
        name_root = f"{first}'s {sector['sector'].split()[0]}"
    elif naming_style == "surname_trade":
        name_root = f"{surname} {sector['sector'].split()[0]}"
    else:
        name_root = f"{sector['location']} {sector['sector'].split()[0]}"

    business_name = f"{name_root} {form['suffix']}".strip()

    return {
        "founder": founder,
        "founder_data": founder_data,
        "business_name": business_name,
        "sector": sector,
        "form": form,
        "event": event,
        "framework": framework,
    }


def make_combinatorial_mcq(
    r: random.Random,
    *,
    subskill_id: str,
    term: int = 1,
    cognitive_level: int = 2,
    mode: str = "compound",
) -> Dict[str, Any]:
    """Emits an authentic exam-standard MCQ driven by the 4D grammar."""
    sc = sample_scenario(r)
    ev = sc["event"]
    fw = sc["framework"]
    fm = sc["form"]

    question_templates = [
        # Template 1: Environmental Classification
        {
            "prompt": (
                f"{sc['business_name']}, a {fm['form']} operating in {sc['sector']['location']} "
                f"({sc['sector']['province']}), is confronted by the following event:\n"
                f"\"{ev['event']}\".\n\n"
                f"Identify the business environment and primary environmental dimension of this challenge."
            ),
            "correct": f"The {ev['environment'].capitalize()} Environment ({ev['pes_factor'].capitalize()} dimension)",
            "distractors": [
                f"The Micro Environment (internal organizational resource)",
                f"The {'Market' if ev['environment'] == 'macro' else 'Macro'} Environment (solely within management control)",
                f"The Global Environment (completely immune to South African statutory standards)",
            ],
            "explanation": (
                f"This event represents a challenge in the {ev['environment']} environment because {sc['business_name']} "
                f"{'has zero direct control over macroeconomic conditions' if ev['environment'] == 'macro' else 'can only partially influence market stakeholders'}. "
                f"Direct impact: {ev['direct_impact']}."
            ),
            "tier1": f"Check whether {sc['business_name']} has direct internal control over this event.",
            "tier2": "The Micro environment is internal (full control); Market is external (influence only); Macro is external (no control).",
            "tier3": f"Classify this as {ev['environment'].capitalize()} Environment because the business has no direct control over {ev['pes_factor']}.",
            "misconception": "macro_vs_market_confusion",
        },
        # Template 2: Strategic Adaptation
        {
            "prompt": (
                f"{sc['founder']}, the managing executive of {sc['business_name']}, needs an effective, "
                f"curriculum-aligned strategic response to address:\n"
                f"\"{ev['event']}\".\n\n"
                f"Which ONE of the following represents the most viable business strategy?"
            ),
            "correct": ev["strategic_response"].capitalize(),
            "distractors": [
                "Ignore the challenge and immediately lower employee wages below the statutory minimum",
                "Liquidate the enterprise immediately without notifying creditors or commercial banks",
                "Increase selling prices by 200% while reducing product quality to inflate short-term cash",
            ],
            "explanation": (
                f"The correct strategic response is to {ev['strategic_response']}. "
                f"This addresses the core problem: {ev['direct_impact']}."
            ),
            "tier1": f"Look at how an enterprise in {sc['sector']['sector']} can mitigate {ev['pes_factor']} pressure.",
            "tier2": "Strategic management requires sustainable, lawful operational adjustments rather than unlawful shortcuts.",
            "tier3": f"Adopt the strategy: {ev['strategic_response']}.",
            "misconception": "inappropriate_strategic_response",
        },
        # Template 3: Form of Ownership & Legal Liability
        {
            "prompt": (
                f"{sc['business_name']} is currently registered as a {fm['form']}.\n\n"
                f"If the enterprise accrues substantial debts during the economic challenge, which statement "
                f"accurately describes the legal liability and continuity of {sc['founder']}?"
            ),
            "correct": f"The owners face {fm['liability']}, and the business has {fm['continuity']}.",
            "distractors": [
                f"The owners face {'limited liability' if not fm['legal_personality'] else 'unlimited personal liability'}, with guaranteed government bailouts.",
                "All debts are automatically transferred to the South African Department of Trade, Industry and Competition.",
                "The business ceases to exist automatically every time interest rates change.",
            ],
            "explanation": (
                f"For a {fm['form']}, the legal reality is {fm['liability']}. "
                f"Continuity principle: {fm['continuity']}."
            ),
            "tier1": f"Recall whether a {fm['form']} possesses separate legal personality from its owners.",
            "tier2": "Sole Traders and Partnerships have unlimited liability; Companies and Close Corporations enjoy separate legal personality.",
            "tier3": f"A {fm['form']} carries {fm['liability']}.",
            "misconception": "ownership_liability_inversion",
        },
        # Template 4: Statutory Compliance & Labour Law
        {
            "prompt": (
                f"In responding to staff scheduling during this period, {sc['business_name']} must strictly adhere to the {fw['framework']}.\n\n"
                f"What is the primary statutory purpose of the {fw['framework']} in South African commerce?"
            ),
            "correct": fw["core_purpose"].capitalize(),
            "distractors": [
                "To eliminate all taxes payable by commercial businesses to the South African Revenue Service (SARS)",
                "To grant businesses the legal authority to terminate contracts without procedural fairness",
                "To fix the national exchange rate between the South African Rand and foreign currencies",
            ],
            "explanation": (
                f"The primary purpose of the {fw['framework']} is that it {fw['core_purpose']}."
            ),
            "tier1": f"Identify the core focus area of {fw['framework']}.",
            "tier2": "Differentiate between BCEA (basic working conditions), LRA (collective bargaining), and EEA (affirmative action).",
            "tier3": f"The {fw['framework']} {fw['core_purpose']}.",
            "misconception": fw["misconception_tag"],
        },
    ]

    t = r.choice(question_templates)
    opts = [t["correct"]] + t["distractors"]
    r.shuffle(opts)
    correct_idx = opts.index(t["correct"])

    qid = f"g10_bs_comb_{r.randint(100000, 999999)}"

    return {
        "id": qid,
        "question_id": qid,
        "question_type": "mcq",
        "term": term,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "cognitive_level": cognitive_level,
        "mode": mode,
        "subskill_id": subskill_id,
        "prompt": t["prompt"],
        "options": opts,
        "correct_index": str(correct_idx),
        "explanation": t["explanation"],
        "marks": 2,
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct multiple choice option selection", "marks": 2, "editable": False}
            ],
            "deductions": [],
            "carry_forward_rule": "none"
        },
        "hints": {
            "tier_1": t["tier1"],
            "tier_2": t["tier2"],
            "tier_3": t["tier3"],
        },
        "misconception_tags": [t["misconception"]],
        "metadata": {
            "sector": sc["sector"]["sector"],
            "province": sc["sector"]["province"],
            "form": fm["form"],
            "framework": fw["framework"],
        }
    }


def make_combinatorial_drag_and_drop(
    r: random.Random,
    *,
    subskill_id: str,
    term: int = 1,
    mode: str = "compound",
) -> Dict[str, Any]:
    """Generates an interactive classification / sorting question (Modality 3)."""
    sc = sample_scenario(r)
    biz = sc["business_name"]
    ev = sc["event"]

    items = [
        {"id": "item_1", "text": f"{biz} vision, mission, and organizational culture", "target": "Micro Environment"},
        {"id": "item_2", "text": f"Aggressive local competitors and customer buying habits", "target": "Market Environment"},
        {"id": "item_3", "text": f"{ev['event']}", "target": f"{ev['environment'].capitalize()} Environment"},
        {"id": "item_4", "text": f"Production equipment, physical inventory, and staff morale", "target": "Micro Environment"},
    ]
    r.shuffle(items)

    qid = f"g10_bs_dnd_{r.randint(100000, 999999)}"

    return {
        "id": qid,
        "question_id": qid,
        "question_type": "drag_and_drop",
        "term": term,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "cognitive_level": 3,
        "mode": mode,
        "subskill_id": subskill_id,
        "prompt": (
            f"Classify the following elements of {biz} into their respective business environments "
            f"(Micro, Market, or Macro Environment)."
        ),
        "categories": ["Micro Environment", "Market Environment", "Macro Environment"],
        "items": items,
        "solution": {it["id"]: it["target"] for it in items},
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": f"Correct classification of item {i+1}", "marks": 1, "editable": True}
                for i in range(len(items))
            ],
            "deductions": [],
            "carry_forward_rule": "none"
        },
        "hints": {
            "tier_1": "Determine the degree of control the business has over each item.",
            "tier_2": "Micro = full internal control; Market = consumers/competitors/suppliers (influence only); Macro = national economy/laws (zero control).",
            "tier_3": "Internal assets and vision belong in Micro. Competitors belong in Market. External economic/legal forces belong in Macro.",
        },
        "misconception_tags": ["macro_vs_market_confusion", "micro_vs_market_confusion"],
    }


def make_combinatorial_cloze(
    r: random.Random,
    *,
    subskill_id: str,
    term: int = 1,
    mode: str = "compound",
) -> Dict[str, Any]:
    """Generates a contextual Cloze / sentence completion question (Modality 4)."""
    sc = sample_scenario(r)
    fm = sc["form"]
    fw = sc["framework"]

    blanks = [
        {"key": "blank_1", "correct": fm["liability"].split()[0], "label": "liability type (limited / unlimited)"},
        {"key": "blank_2", "correct": fw["framework"].split()[0], "label": "governing statutory legislation acronym"},
    ]

    qid = f"g10_bs_cloze_{r.randint(100000, 999999)}"

    return {
        "id": qid,
        "question_id": qid,
        "question_type": "cloze",
        "term": term,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "cognitive_level": 2,
        "mode": mode,
        "subskill_id": subskill_id,
        "prompt": (
            f"Complete the legal and regulatory evaluation for {sc['business_name']} by filling in the missing terms:\n\n"
            f"1. Because {sc['business_name']} operates as a {fm['form']}, its founders bear [blank_1] liability.\n"
            f"2. To safeguard basic workplace standards, human resource operations must comply with the [blank_2] framework."
        ),
        "blanks": blanks,
        "solution": {b["key"]: b["correct"] for b in blanks},
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate identification of liability status", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Accurate identification of legislation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Review the ownership rules for a {fm['form']} and labour regulations.",
            "tier_2": "Limited liability protects personal assets; unlimited liability places personal assets at risk.",
            "tier_3": f"Enter '{fm['liability'].split()[0]}' for blank 1, and '{fw['framework'].split()[0]}' for blank 2.",
        },
        "misconception_tags": ["ownership_liability_inversion", fw["misconception_tag"]],
    }


def generate_combinatorial_batch(
    *,
    subskill_id: str,
    term: int = 1,
    count: int = 5,
    seed: Optional[int] = None,
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    """Master batch generator for combinatorial semantic questions."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        # Rotate through modalities to ensure rich learning ergonomics
        modality_cycle = i % 3
        if modality_cycle == 0:
            questions.append(make_combinatorial_mcq(r, subskill_id=subskill_id, term=term, mode=mode))
        elif modality_cycle == 1:
            questions.append(make_combinatorial_drag_and_drop(r, subskill_id=subskill_id, term=term, mode=mode))
        else:
            questions.append(make_combinatorial_cloze(r, subskill_id=subskill_id, term=term, mode=mode))

    return questions
