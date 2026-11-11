"""Grade 7 EMS: Term 3 - Businesses Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "formal_informal_classification",
    "service_business_classification",
    "households_producers_explanation",
    "informal_business_advantages",
    "socio_economic_shocks_on_business",
    "epidemics_impact"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_formal_informal_classification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    examples = [
        ("operates a registered accounting consultancy with a formal business registration number, pays VAT and company tax, and leases permanent office suites", "Formal business", "Registered with SARS/CIPC, pays taxes, operates from fixed commercial premises"),
        ("sells fresh fruit, snacks, and phone cards from a temporary street-corner wooden stall, keeps no formal written accounts, and is not registered with SARS", "Informal business", "Unregistered with authorities, cash-based, operates without fixed legal structures"),
        ("runs a licensed pharmacy chain with 15 branches, employs 60 registered pharmacists, and complies with national labour regulations", "Formal business", "Legally registered company adhering to official regulations and payroll taxes"),
        ("cuts grass and prunes garden hedges for neighborhood homes using personal hand tools, receiving cash payments daily without formal invoices", "Informal business", "Unregistered micro-enterprise, cash transactions, zero formal regulatory paperwork")
    ]
    biz_desc, biz_type, rationale = rng.choice(examples)
    prompt = (
        f"In {area}, {person} {biz_desc}.\n\n"
        f"Is this business classified as a **formal business** or an **informal business**, and what is the defining characteristic?"
    )
    correct_opt = f"{biz_type}, because it is {rationale.lower()}."
    alt_type = "Informal business" if biz_type == "Formal business" else "Formal business"
    options = [
        correct_opt,
        f"{alt_type}, because all small businesses in South Africa are legally exempt from registration",
        f"{alt_type}, because any business that makes a cash profit is automatically formal",
        "Neither, because individual businesses cannot be classified by formal economic status"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Classification standards from Curriculum Reference:\n"
        f"- Formal business: Legally registered with government bodies (CIPC, SARS), pays corporate and employment taxes, operates from fixed commercial premises, and complies with labour laws.\n"
        f"- Informal business: Not legally registered, operates mainly in cash, keeps minimal formal records, and has no legal protection.\n\n"
        f"Step 2: Conclusion:\n"
        f"{person}'s venture is a {biz_type} because it is {rationale.lower()}."
    )
    return {
        "id": f"g7_ems_bus_class_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "formal_informal_classification",
        "question_family_id": "formal_informal_classification",
        "curriculum_reference": "Term 3 > Businesses > Formal and informal businesses",
        "hints": {
            "tier_1": "Check whether the business is officially registered with SARS and has fixed formal premises.",
            "tier_2": "Formal businesses are registered and pay tax; informal businesses operate without official registration.",
            "tier_3": f"This business is classified as a {biz_type}."
        },
        "misconception_tags": ["formal_informal_tax_confusion"]
    }


def _build_service_business_classification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    types = [
        ("Trading business", "buys packaged clothing from wholesalers and sells them directly to retail shoppers at a markup"),
        ("Manufacturing business", "purchases raw pine timber, cuts and assembles dining tables and chairs for sale"),
        ("Service business", "provides professional electrical installation, maintenance, and wiring repairs for homeowners")
    ]
    chosen_type, chosen_desc = rng.choice(types)
    prompt = (
        f"In {area}, {person} operates an enterprise that {chosen_desc}.\n\n"
        f"Into which business type does this enterprise fall?"
    )
    correct_opt = chosen_type
    options = ["Trading business", "Manufacturing business", "Service business", "Extraction syndicate"]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand the three primary types of businesses:\n"
        "- Trading business: Buys finished goods and resells them at a higher price without altering them.\n"
        "- Manufacturing business: Converts raw materials into new finished physical products.\n"
        "- Service business: Provides specialised labour, skills, or intellectual expertise rather than tangible goods.\n\n"
        f"Step 2: Conclusion:\n"
        f"Because this enterprise {chosen_desc}, it is a {chosen_type}."
    )
    return {
        "id": f"g7_ems_bus_type_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "service_business_classification",
        "question_family_id": "service_business_classification",
        "curriculum_reference": "Term 3 > Businesses > Types of businesses: Trading, manufacturing, service",
        "hints": {
            "tier_1": "Is the business making goods from raw materials, buying and reselling goods, or providing a skill?",
            "tier_2": "Trading = buying and selling; Manufacturing = making new goods; Service = offering skills/work.",
            "tier_3": f"This business is classified as a {chosen_type}."
        },
        "misconception_tags": ["trading_vs_service_confusion"]
    }


def _build_households_producers_explanation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"In {area}, households interact daily with formal and informal businesses. "
        f"Explain the dual role of **households** as both consumers and producers in the economic cycle. (4 marks)"
    )
    sample_answer = (
        "Households act as consumers because they spend their earned income to purchase finished goods and services "
        "produced by businesses to satisfy their personal needs and wants. Simultaneously, households act as producers "
        "because household members supply the essential factors of production—namely their labour, skills, entrepreneurial ideas, "
        "and capital—to businesses, without which businesses cannot produce output."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Households as consumers: Spend wages/income to buy goods and services to satisfy needs and wants (2 marks).\n"
        "2. Households as producers: Provide the factors of production (labour, skills, land, capital) to businesses (2 marks)."
    )
    return {
        "id": f"g7_ems_bus_house_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "households_producers_explanation",
        "question_family_id": "households_producers_explanation",
        "diagram_spec": {
        "diagram_role": "context","kind": "circular_flow", "title": "Two-Sector Economic Circular Flow (Households & Businesses)"},
        "curriculum_reference": "Term 3 > Businesses > Role of households as producers and consumers",
        "hints": {
            "tier_1": "Households buy goods (consumers) and supply their work/labour to businesses (producers).",
            "tier_2": "Explain what households buy from businesses and what households provide to businesses.",
            "tier_3": "Consumers buy products; producers supply factors of production like labour."
        },
        "misconception_tags": ["household_role_omission"]
    }


def _build_informal_business_advantages(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"{person} decides to open an informal spaza shop in {area} rather than registering a formal company immediately.\n\n"
        f"Which statement correctly identifies ONE key advantage and ONE key disadvantage of running an **informal business**?"
    )
    correct_opt = "Advantage: Low startup costs and minimal legal bureaucracy | Disadvantage: No legal protection and difficult access to commercial bank loans"
    options = [
        correct_opt,
        "Advantage: Guaranteed multi-million Rand government contracts | Disadvantage: Compulsory corporate tax audits every week",
        "Advantage: Unlimited legal liability protection | Disadvantage: Forbidden from trading with cash",
        "Advantage: Automatic listing on the Johannesburg Stock Exchange | Disadvantage: Cannot hire family members"
    ]
    rng.shuffle(options)
    sol = (
        "Analysis of Informal Business Pros and Cons:\n"
        "- Advantages: Very low startup capital needed, flexible operating hours, zero costly legal registration fees, direct cash flow.\n"
        "- Disadvantages: No formal bank loan access (lack of credit history), vulnerable to municipal confiscation or crime, no worker benefits, no legal entity status.\n\n"
        "Conclusion: Low startup costs is an advantage, while lack of legal protection and loan access is a disadvantage."
    )
    return {
        "id": f"g7_ems_bus_adv_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "informal_business_advantages",
        "question_family_id": "informal_business_advantages",
        "curriculum_reference": "Term 3 > Businesses > Advantages and disadvantages of informal businesses",
        "hints": {
            "tier_1": "Think about why informal businesses are easy to start, but hard to grow through commercial bank loans.",
            "tier_2": "Informal businesses have low barriers to entry but lack formal legal protections.",
            "tier_3": "Low startup cost is the advantage; difficulty obtaining loans is the disadvantage."
        },
        "misconception_tags": ["informal_business_privilege_misconception"]
    }


def _build_epidemics_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    intros = [
        f"In {area}, small enterprises like {person}'s business frequently cope with socioeconomic and environmental shocks.",
        f"Community health workers and local chamber leaders in {area} recently conducted a risk assessment for local employers like {person}.",
        f"A local business forum in {area} reviewed operational challenges faced by {person}'s enterprise during severe weather and disease outbreaks."
    ]
    intro = rng.choice(intros)
    prompt = (
        f"{intro} Explain how widespread health epidemics (such as HIV/AIDS or tuberculosis) and natural disasters (like floods) "
        f"impact workforce productivity and business continuity in South Africa. (4 marks)"
    )
    sample_answer = (
        "Health epidemics lead to increased worker absenteeism, fatigue, and lost production hours as employees fall ill "
        "or take time off to care for sick relatives. This forces businesses to incur higher training costs to replace skilled workers. "
        "Natural disasters damage infrastructure, destroy stock and transport links, and interrupt water and electricity supply, "
        "causing temporary or permanent business closures and lost sales."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Impact of epidemics: Increased absenteeism, loss of experienced labour, reduced productivity, and retraining costs (2 marks).\n"
        "2. Impact of disasters: Physical destruction of premises/stock, supply chain disruption, and loss of trading revenue (2 marks)."
    )
    return {
        "id": f"g7_ems_bus_epid_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "epidemics_impact",
        "question_family_id": "epidemics_impact",
        "curriculum_reference": "Term 3 > Businesses > Effect of natural disasters and health epidemics on businesses",
        "hints": {
            "tier_1": "Discuss worker sickness/absenteeism and physical destruction of stock/premises.",
            "tier_2": "Epidemics cause absenteeism and lost skills; disasters destroy infrastructure and halt production.",
            "tier_3": "Address both lost labour hours and damage to physical business operations."
        },
        "misconception_tags": ["vague_epidemic_answer"]
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()

    builders = {
        "formal_informal_classification": _build_formal_informal_classification,
        "service_business_classification": _build_service_business_classification,
        "households_producers_explanation": _build_households_producers_explanation,
        "informal_business_advantages": _build_informal_business_advantages,
        "epidemics_impact": _build_epidemics_impact
    }

    if target in builders:
        return [builders[target](rng) for _ in range(count)]

    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]

    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
