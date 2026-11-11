"""Grade 7 EMS: Term 1 - Goods and Services Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 1/03. Goods and Service.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "goods_services_classification",
    "producer_consumer_roles",
    "recycling_benefits",
    "sector_classification",
    "household_roles_essay",
    "recycling_discussion"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 1/03. Goods and Service.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _with_metadata(item: Dict[str, Any], *, question_family_id: str, **kwargs: Any) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": "grade7_ems",
        "subtopic_id": "term1_goods_and_services",
        "subskill": question_family_id,
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 1 > Goods and Services",
        "difficulty_band": item.get("difficulties", ["easy", "medium"]),
    })
    return enriched


def _build_goods_services_classification(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]

    services = [
        ("a haircut and styling at a local hair salon", "hair salon service"),
        ("plumbing repair on a leaking municipal water pipe", "trade repair service"),
        ("commuter minibus taxi transport to school", "public passenger transport"),
        ("a consultation with a registered medical doctor", "healthcare service")
    ]
    goods = [
        "a loaf of fresh brown bread",
        "a pair of durable school shoes",
        "a plastic bucket for water storage",
        "a math exercise workbook"
    ]
    target_serv, serv_type = rng.choice(services)
    distract_goods = rng.sample(goods, 3)

    prompt = (
        f"{person} is shopping in {area} and spends money on various necessities. "
        f"Which of the following purchases represents a **SERVICE** rather than a physical good?"
    )
    correct_opt = target_serv.capitalize()
    options = [correct_opt] + [g.capitalize() for g in distract_goods]
    rng.shuffle(options)

    sol = (
        f"Step 1: Distinguish between goods and services:\n"
        f"- Goods are tangible physical items that can be touched, stored, and owned (e.g. bread, shoes, books).\n"
        f"- Services are intangible activities, skills, or actions performed by individuals to satisfy a need.\n\n"
        f"Step 2: Identify the intangible activity:\n"
        f"{target_serv.capitalize()} is an intangible service ({serv_type}).\n\n"
        f"Conclusion: {correct_opt}."
    )
    return _with_metadata({
        "id": f"g7_ems_goods_serv_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "diagram_spec": {
        "diagram_role": "context",
            "kind": "circular_flow",
            "title": "Two-Sector Economic Circular Flow (Households & Businesses)"
        },
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "hints": {
            "tier_1": "Can you hold this item in your hand and take it home? If yes, it is a good. If no, it is a service.",
            "tier_2": "Look for the intangible action or skill performed by someone.",
            "tier_3": f"Correct service: {correct_opt}."
        }
    }, question_family_id="goods_services_classification")


def _build_producer_consumer_roles(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    producer_name = scenario["entrepreneur"]
    area = scenario["area"]

    crops = ["maize", "potatoes", "sunflower seeds", "sugarcane", "cabbages"]
    crop = rng.choice(crops)
    buyers = [
        ("a community bakery", "milling the harvest into bread flour"),
        ("a food processing plant", "canning vegetables for retail stores"),
        ("a regional dairy depot", "processing animal feed"),
        ("a wholesale fruit and veg market", "supplying local street vendors")
    ]
    buyer_name, purpose = rng.choice(buyers)

    prompt = (
        f"{producer_name} farms land near {area}, harvests {crop}, and sells the harvest to {buyer_name} for {purpose}.\n\n"
        f"In this economic transaction, {producer_name} acts as the ______ and {buyer_name} acts as the ______."
    )
    correct_opt = "producer; consumer"
    options = [
        "producer; consumer",
        "consumer; producer",
        "retailer; wholesaler",
        "employee; employer"
    ]
    rng.shuffle(options)

    sol = (
        f"Step 1: Define producer and consumer roles:\n"
        f"- The **producer** is the person or enterprise that grows, manufactures, or supplies goods ({producer_name} cultivating {crop}).\n"
        f"- The **consumer** is the person or business that buys and uses goods or raw materials to satisfy needs ({buyer_name}).\n\n"
        f"Conclusion: {producer_name} is the producer; {buyer_name} is the consumer."
    )
    return _with_metadata({
        "id": f"g7_ems_prod_cons_{rng.randint(100000, 999999)}",
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
        "hints": {
            "tier_1": "Who makes or supplies the product, and who purchases or consumes it?",
            "tier_2": f"{producer_name} produces {crop}. {buyer_name} buys it.",
            "tier_3": "Correct roles: producer; consumer."
        }
    }, question_family_id="producer_consumer_roles")


def _build_recycling_benefits(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]
    materials = ["glass beverage bottles", "cardboard packing boxes", "scrap aluminium beverage cans", "plastic containers"]
    mat = rng.choice(materials)

    prompt = (
        f"{person} organizes an environmental youth initiative in {area} to collect and sort discarded {mat}.\n\n"
        f"Why is it economically and environmentally vital for households and businesses in South Africa to recycle such goods?"
    )
    correct_opt = "To reduce waste in municipal landfill sites, conserve natural resources, and protect the environment."
    distractors = [
        "To make raw materials scarce so that retail prices increase drastically.",
        "To replace all primary sector mining activities with plastic manufacturing.",
        "To ensure households spend more money on packaging disposal fees."
    ]
    options = [correct_opt] + distractors
    rng.shuffle(options)

    sol = (
        f"Economic and Environmental Benefits of Recycling:\n"
        f"1. Reduces the volume of waste sent to overflowing municipal landfill sites.\n"
        f"2. Conserves scarce natural resources by reusing materials instead of extracting new ones.\n"
        f"3. Lowers production costs and saves energy.\n"
        f"4. Creates green jobs for waste reclaimers and collectors in {area}.\n\n"
        f"Conclusion: {correct_opt}"
    )
    return _with_metadata({
        "id": f"g7_ems_recyc_ben_{rng.randint(100000, 999999)}",
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
        "hints": {
            "tier_1": "Think about what happens to garbage when it is reused instead of dumped in landfills.",
            "tier_2": "Recycling conserves resources and cuts pollution.",
            "tier_3": f"Correct: {correct_opt}"
        }
    }, question_family_id="recycling_benefits")


def _build_sector_classification(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    area = scenario["area"]

    sectors = [
        ("tertiary (services)", "A commercial retail bank providing loans and accounts", "A deep-level gold mine extracting raw ore", "A motor vehicle assembly factory", "A commercial timber plantation"),
        ("primary (raw material extraction)", "A commercial citrus fruit farm harvesting oranges", "A clothing factory sewing school uniforms", "An insurance brokerage firm", "A furniture showroom shop"),
        ("secondary (manufacturing / processing)", "A furniture manufacturing workshop building desks", "A commercial cattle ranch raising livestock", "A private security guard company", "A wholesale grocery distribution warehouse")
    ]
    target_sec, correct_biz, d1, d2, d3 = rng.choice(sectors)

    prompt = (
        f"Enterprises across {area} operate in different spheres of production. "
        f"Which of the following enterprises operates in the **{target_sec}** sector?"
    )
    correct_opt = correct_biz
    options = [correct_biz, d1, d2, d3]
    rng.shuffle(options)

    sol = (
        f"Economic Sectors Breakdown:\n"
        f"- Primary Sector: Extraction and harvesting of raw natural resources (farming, mining, fishing, forestry).\n"
        f"- Secondary Sector: Manufacturing, processing, and construction that transforms raw materials into finished goods.\n"
        f"- Tertiary Sector: Commercial and professional services provided to consumers and businesses (banking, transport, retail, healthcare).\n\n"
        f"The business operating in the {target_sec} sector is: {correct_biz}."
    )
    return _with_metadata({
        "id": f"g7_ems_sec_class_{rng.randint(100000, 999999)}",
        "diagram_spec": {
        "diagram_role": "context",
            "kind": "production_chain",
            "raw": "Natural Resource",
            "primary": "Primary Extraction Sector",
            "secondary": "Secondary Manufacturing Sector",
            "tertiary": "Tertiary Services / Retail",
            "product": "Finished Consumer Good"
        },
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
        "hints": {
            "tier_1": "Primary = raw resources; Secondary = factory making things; Tertiary = services.",
            "tier_2": f"Target sector: {target_sec}.",
            "tier_3": f"Correct business: {correct_biz}."
        }
    }, question_family_id="sector_classification")


def _build_household_roles_essay(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    family_name = scenario["entrepreneur"]
    area = scenario["area"]
    occupations = [
        ("registered staff nurse at a provincial clinic", "providing healthcare labour"),
        ("diesel mechanic repairing delivery trucks", "providing mechanical repair labour"),
        ("primary school educator teaching mathematics", "providing educational labour"),
        ("carpenter building roof trusses", "providing construction labour")
    ]
    job, labour_desc = rng.choice(occupations)

    prompt = (
        f"In {area}, a parent in the {family_name} household works as a {job} ({labour_desc}) to earn a monthly wage, "
        f"while the family buys groceries, electricity, and clothing from local retailers.\n\n"
        f"Explain how this household functions as both a **producer** and a **consumer** in the economy. Provide an example for each role. (4 marks)"
    )
    sample_ans = (
        f"The household is a producer because its members provide productive labour ({job}) to businesses or the state to produce goods and services. "
        f"The household is a consumer because it uses its earned income to purchase goods like food and services like electricity to satisfy needs."
    )
    sol = (
        f"1. Household as Producer [2]: Households own the factors of production (labour). They act as producers when members offer their skills and work "
        f"(such as working as a {job}) to businesses or government to produce economic output [2].\n"
        f"2. Household as Consumer [2]: Households act as consumers when they spend their earned wages and salaries on goods (groceries, clothing) "
        f"and services (electricity, transport, schooling) to satisfy family needs and wants [2]."
    )
    return _with_metadata({
        "id": f"g7_ems_hh_roles_{rng.randint(100000, 999999)}",
        "question_type": "short_answer",
        "prompt": prompt,
        "correct_answer": sample_ans,
        "sample_answer": sample_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "hints": {
            "tier_1": "How does a household earn money (producer of labour) and how does it spend money (consumer of goods)?",
            "tier_2": "Producer = selling labour to businesses. Consumer = buying goods and services.",
            "tier_3": "Households produce labour (employment) and consume finished goods (shopping)."
        }
    }, question_family_id="household_roles_essay")


def _build_recycling_discussion(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    town = scenario["area"]
    materials = ["discarded plastic bottles", "scrap cardboard and paper", "empty metal beverage cans", "glass containers"]
    mat = rng.choice(materials)

    prompt = (
        f"A community cooperative in {town} launches a collection project for {mat}.\n\n"
        f"Discuss TWO ways in which recycling and reusing goods can help satisfy the economic needs and wants "
        f"of people in South African communities. (4 marks)"
    )
    sample_ans = (
        "1. Income and employment generation: Reclaiming and selling recyclable materials creates jobs and income for unemployed community members. "
        "2. Resource conservation and cost reduction: Reusing materials reduces the need for expensive raw materials, lowering manufacturing costs and preserving natural resources."
    )
    sol = (
        f"1. Economic Job and Income Creation [2]: Waste reclaimers and recycling depots in {town} buy collected {mat}, creating self-employment "
        f"and vital household income for unemployed community members to buy food and clothing [2].\n"
        f"2. Resource Conservation & Lower Product Costs [2]: Reusing recycled materials uses less electricity and raw materials than virgin extraction, "
        f"keeping production costs down and reducing municipal waste removal costs [2]."
    )
    return _with_metadata({
        "id": f"g7_ems_recyc_disc_{rng.randint(100000, 999999)}",
        "question_type": "short_answer",
        "prompt": prompt,
        "correct_answer": sample_ans,
        "sample_answer": sample_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "hints": {
            "tier_1": "Consider how recycling puts money in people's pockets and saves natural resources.",
            "tier_2": "Point 1: Job creation and income from collecting waste. Point 2: Conserving raw materials and cutting production costs.",
            "tier_3": "Recycling creates income for collectors and reduces production expenses."
        }
    }, question_family_id="recycling_discussion")


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Main entry point for Grade 7 Goods and Services generator."""
    rng = _rng(seed)
    questions = []

    target_sub = str(subskill or "").strip().lower()

    def _build_one(sub_name: str) -> Dict[str, Any]:
        if sub_name == "goods_services_classification" or ("goods" in sub_name and "services" in sub_name):
            return _build_goods_services_classification(rng)
        elif sub_name == "producer_consumer_roles" or "producer" in sub_name or "consumer" in sub_name:
            return _build_producer_consumer_roles(rng)
        elif sub_name == "recycling_benefits" or "benefit" in sub_name:
            return _build_recycling_benefits(rng)
        elif sub_name == "sector_classification" or "sector" in sub_name:
            return _build_sector_classification(rng)
        elif sub_name == "household_roles_essay" or "household" in sub_name:
            return _build_household_roles_essay(rng)
        elif sub_name == "recycling_discussion" or "discussion" in sub_name:
            return _build_recycling_discussion(rng)
        return _build_goods_services_classification(rng)

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        for _ in range(count):
            questions.append(_build_one(target_sub))
        return questions

    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(_build_one(sub))

    return questions
