"""Grade 8 EMS — Forms of Ownership (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 3/01. Forms of ownership.md

Covers CAPS subskills:
  1. sole_trader_characteristics: 1 owner, personal capital, unlimited liability, full profit retention, easy formation.
  2. partnerships_characteristics: 2-20 partners, partnership agreement, pooled resources, shared profits, joint and several liability.
  3. close_corporation_characteristics: 1-10 members, Founding Statement (CK1), CC suffix, separate legal entity, limited liability.
  4. companies_private_vs_public: (Pty) Ltd vs Ltd, shareholders, limited liability, board of directors, prospectus, JSE trading.
  5. smme_and_sustainable_job_creation: Role of SMMEs in job creation, poverty reduction, and sustainable use of natural resources.
  6. liability_and_legal_persona_comparison: Limited vs unlimited liability, separate legal entity, and continuity of existence.

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "sole_trader_characteristics",
    "partnerships_characteristics",
    "close_corporation_characteristics",
    "companies_private_vs_public",
    "smme_and_sustainable_job_creation",
    "liability_and_legal_persona_comparison",
]

TOPIC_KEY = "grade8_ems_ownership"
LO = "g8_ems_ownership"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: str = "ownership",
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_ownership",
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group,
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 3 > Forms of Ownership",
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["entrepreneurship", "ownership"],
    })
    return enriched


def _gen_sole_trader(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cases = [
        (
            f"{owner} runs a small {scenario['business_type']} in {scenario['area']} as a sole trader. If the business incurs large debts that cannot be paid from its bank account, what does the law dictate regarding {owner}'s personal possessions?",
            "The owner has unlimited liability; personal assets can be seized and sold to settle business debts.",
            "A sole trader has unlimited liability because there is no legal separation between the owner and the business.",
            [
                "The owner has unlimited liability; personal assets can be seized and sold to settle business debts.",
                "The owner has limited liability; only the money initially invested in the business can be lost.",
                "The government will automatically absorb the business debt under SMME development schemes.",
                "Suppliers are legally prohibited from claiming any money outside the business premises.",
            ],
        ),
        (
            f"Which of the following is a primary ADVANTAGE of operating a business as a sole trader?",
            "Quick decision-making and the owner retains 100% of all profits",
            "Because there is only one owner, decisions can be made immediately without consulting partners, and all profits belong directly to the owner.",
            [
                "Quick decision-making and the owner retains 100% of all profits",
                "The business continues to exist indefinitely even if the owner passes away",
                "Large amounts of capital can easily be raised by issuing shares to the public",
                "The owner enjoys limited liability protecting all personal belongings",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)
    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Explanation:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_sole_{rng.randint(100000, 999999)}",
        "title": "Sole Trader Characteristics",
        "question_type": "mcq",
        "topic": "Forms of ownership",
        "subskill": "sole_trader_characteristics",
        "learning_objective_id": f"{LO}_sole_trader",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Consider how many people own a sole trader and who is responsible for the debts.",
            "tier_2": "A sole trader has 1 owner and unlimited liability.",
            "tier_3": f"Correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_sole_trader_liability"],
    }, subskill="sole_trader_characteristics", learning_objective_id=f"{LO}_sole_trader", question_family_id="sole_trader_drill")


def _gen_partnerships(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]
    partner = scenario["competitor"]

    cases = [
        (
            f"{owner} and {partner} decide to pool their savings and technical skills to start a joint enterprise in {scenario['area']}. Under South African law, what are the minimum and maximum number of partners permitted in a standard partnership?",
            "Minimum 2, Maximum 20",
            "A partnership requires at least 2 people to form an agreement and is generally capped at 20 partners.",
            [
                "Minimum 2, Maximum 20",
                "Minimum 1, Maximum 10",
                "Minimum 2, Maximum 50",
                "Minimum 7, Maximum unlimited",
            ],
        ),
        (
            f"Before trading, {owner} and {partner} draw up a written legal document outlining how profits will be divided, responsibilities allocated, and disputes resolved. This document is known as the:",
            "Partnership Agreement (Articles of Partnership)",
            "A partnership agreement is a formal contract drawn up by the partners governing capital contributions, profit sharing, and operational duties.",
            [
                "Partnership Agreement (Articles of Partnership)",
                "Prospectus",
                "Founding Statement (CK1)",
                "Memorandum of Incorporation",
            ],
        ),
        (
            f"In a standard partnership, if one partner signs a large business loan and disappears, what is the legal liability of the remaining partner?",
            "Joint and several unlimited liability; the remaining partner is personally liable for the full debt",
            "Partners share joint and several liability, meaning each partner can be held personally responsible for all financial debts incurred by any partner in the name of the business.",
            [
                "Joint and several unlimited liability; the remaining partner is personally liable for the full debt",
                "The remaining partner is only liable for their own initial percentage contribution",
                "The partnership automatically converts into a Close Corporation with limited liability",
                "The bank cannot claim payment because both partners must be present",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)
    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Explanation:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_part_{rng.randint(100000, 999999)}",
        "title": "Partnerships Characteristics",
        "question_type": "mcq",
        "topic": "Forms of ownership",
        "subskill": "partnerships_characteristics",
        "learning_objective_id": f"{LO}_partnerships",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Recall the legal framework for partnerships: number of partners and liability.",
            "tier_2": "A partnership has 2-20 owners who share joint and several unlimited liability.",
            "tier_3": f"Correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_partnership_rules"],
    }, subskill="partnerships_characteristics", learning_objective_id=f"{LO}_partnerships", question_family_id="partnerships_drill")


def _gen_close_corporation(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cases = [
        (
            f"A group of entrepreneurs in {scenario['area']} operate a business registered as 'Ubuntu Logistics CC'. What does 'CC' stand for, and what is the maximum number of members permitted?",
            "Close Corporation; maximum of 10 members",
            "A Close Corporation (CC) is owned by 1 to 10 members, registered using a Founding Statement (CK1).",
            [
                "Close Corporation; maximum of 10 members",
                "Commercial Company; maximum of 50 members",
                "Co-operative Community; maximum of 20 members",
                "Credit Corporation; unlimited number of members",
            ],
        ),
        (
            f"Which of the following is a key legal feature of a Close Corporation (CC) that protects the personal assets of its members?",
            "It is a separate legal entity with limited liability for its members",
            "A CC possesses its own legal personality. Debts belong to the corporation, not to the members personally (limited liability), provided there is no reckless or fraudulent trading.",
            [
                "It is a separate legal entity with limited liability for its members",
                "Members have unlimited liability and must surrender personal property",
                "The CC is exempt from paying any South African corporate income taxes",
                "Members can freely sell public shares on the Johannesburg Stock Exchange",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)
    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Explanation:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_cc_{rng.randint(100000, 999999)}",
        "title": "Close Corporation Characteristics",
        "question_type": "mcq",
        "topic": "Forms of ownership",
        "subskill": "close_corporation_characteristics",
        "learning_objective_id": f"{LO}_cc",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Recall the meaning of CC and how many members can own it.",
            "tier_2": "A Close Corporation has 1-10 members and limited liability.",
            "tier_3": f"Correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_cc_and_companies"],
    }, subskill="close_corporation_characteristics", learning_objective_id=f"{LO}_cc", question_family_id="cc_drill")


def _gen_companies(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)

    cases = [
        (
            "What is the key difference in capital raising between a Private Company ((Pty) Ltd) and a Public Company (Ltd)?",
            "A Public Company can invite the general public to buy shares on the stock exchange (JSE), whereas a Private Company cannot offer shares to the public.",
            "Public companies issue a prospectus and invite the public to purchase shares on the JSE. Private companies raise capital privately from invited shareholders and their shares are not traded publicly.",
            [
                "A Public Company can invite the general public to buy shares on the stock exchange (JSE), whereas a Private Company cannot offer shares to the public.",
                "A Private Company has unlimited liability, while a Public Company has limited liability.",
                "A Private Company requires a minimum of 50 shareholders, while a Public Company requires only 1.",
                "A Public Company is managed by the government, while a Private Company is managed by sole traders.",
            ],
        ),
        (
            "Before a Public Company (Ltd) can issue shares to the public to raise millions of Rand in capital, what legal document must it publish providing full details of its financial health and operational plans?",
            "A Prospectus",
            "A prospectus is a legally mandated document inviting the public to subscribe for shares, disclosing audited financial records, risks, and director details.",
            [
                "A Prospectus",
                "A Partnership Agreement",
                "A Duplicate Receipt",
                "A Till Register Roll",
            ],
        ),
        (
            "What does the principle of 'continuity of existence' mean for a registered company ((Pty) Ltd or Ltd)?",
            "The business continues to exist as an ongoing legal entity even if a shareholder dies, retires, or sells their shares",
            "Because a registered company has its own legal personality, its life is not tied to the lifespan of its owners; it enjoys perpetual continuity.",
            [
                "The business continues to exist as an ongoing legal entity even if a shareholder dies, retires, or sells their shares",
                "The company must operate 24 hours a day without closing its doors",
                "The company cannot change its original business name under any circumstance",
                "All company profits must be paid out to shareholders on a continuous weekly basis",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)
    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Explanation:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_comp_{rng.randint(100000, 999999)}",
        "title": "Companies: Private vs Public",
        "question_type": "mcq",
        "topic": "Forms of ownership",
        "subskill": "companies_private_vs_public",
        "learning_objective_id": f"{LO}_companies",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Recall the difference between (Pty) Ltd and Ltd regarding public share trading.",
            "tier_2": "Public companies sell shares to anyone via the JSE using a prospectus.",
            "tier_3": f"Correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_pty_ltd_with_ltd"],
    }, subskill="companies_private_vs_public", learning_objective_id=f"{LO}_companies", question_family_id="companies_drill")


def _gen_smme_job_creation(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    cases = [
        (
            f"In South Africa, small, medium, and micro enterprises (SMMEs) like {owner}'s service shop play a crucial role in the national economy by:",
            "Creating sustainable employment opportunities and equipping workers with practical skills",
            "SMMEs account for the majority of employment creation in local communities, alleviating poverty and building entrepreneurial skills.",
            [
                "Creating sustainable employment opportunities and equipping workers with practical skills",
                "Replacing all large commercial banks with informal cash lenders",
                "Eliminating the need for South Africa to trade with international partners",
                "Ensuring that no businesses ever pay VAT or company income taxes",
            ],
        ),
        (
            "How do responsible businesses ensure the SUSTAINABLE use of natural resources in their operations?",
            "By conserving water and electricity, minimizing waste, and utilizing renewable resources wherever possible",
            "Sustainable use of resources means meeting present economic needs without depleting or damaging the environment for future generations.",
            [
                "By conserving water and electricity, minimizing waste, and utilizing renewable resources wherever possible",
                "By consuming raw materials as rapidly as possible to maximize immediate short-term profit",
                "By dumping manufacturing by-products into local municipal drainage systems",
                "By operating only during the night to avoid daylight environmental regulations",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)
    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Explanation:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_smme_{rng.randint(100000, 999999)}",
        "title": "SMMEs & Sustainable Job Creation",
        "question_type": "mcq",
        "topic": "Forms of ownership",
        "subskill": "smme_and_sustainable_job_creation",
        "learning_objective_id": f"{LO}_smme",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Think about why small businesses are vital for addressing unemployment in South Africa.",
            "tier_2": "SMMEs create local jobs and sustainable practices protect the environment for future generations.",
            "tier_3": f"Correct answer is {correct_ans}.",
        },
        "misconception_tags": ["underestimates_smme_role"],
    }, subskill="smme_and_sustainable_job_creation", learning_objective_id=f"{LO}_smme", question_family_id="smme_drill")


def _gen_liability_comparison(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)

    cases = [
        (
            "Which pair of business forms BOTH have UNLIMITED liability, meaning the owners' personal assets can be seized to pay business debts?",
            "Sole Trader and Partnership",
            "Both sole traders and partnerships lack separate legal personality; their owners bear unlimited liability.",
            [
                "Sole Trader and Partnership",
                "Close Corporation and Private Company",
                "Public Company and Partnership",
                "Close Corporation and Sole Trader",
            ],
        ),
        (
            "Which of the following forms of ownership is recognized by South African law as a SEPARATE LEGAL ENTITY from its owners?",
            "Private Company ((Pty) Ltd)",
            "Companies and Close Corporations have separate legal personality (legal entity), unlike Sole Traders and Partnerships.",
            [
                "Private Company ((Pty) Ltd)",
                "Sole Trader",
                "Standard Partnership",
                "Informal Tuckshop Syndicate",
            ],
        ),
    ]
    prompt, correct_ans, explanation, options = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    correct_letter = chr(65 + c_idx)
    full_ans = f"{correct_letter}. {correct_ans}"
    sol = f"**{full_ans}** [2 marks]\n\n**Explanation:** {explanation}"

    return _with_metadata({
        "id": f"g8_ems_liab_comp_{rng.randint(100000, 999999)}",
        "title": "Liability & Legal Persona Comparison",
        "question_type": "mcq",
        "topic": "Forms of ownership",
        "subskill": "liability_and_legal_persona_comparison",
        "learning_objective_id": f"{LO}_comparison",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Distinguish between businesses where owners are personally liable vs those with separate legal personality.",
            "tier_2": "Sole traders and partnerships have unlimited liability. CCs and companies have limited liability and separate legal personality.",
            "tier_3": f"Correct answer is {correct_ans}.",
        },
        "misconception_tags": ["confuses_legal_persona"],
    }, subskill="liability_and_legal_persona_comparison", learning_objective_id=f"{LO}_comparison", question_family_id="comparison_drill")


def generate(subskill: str = "mixed", difficulty: str = "medium", count: int = 1, mode: str = "scaffold", seed: Optional[int] = None, **kwargs) -> Any:
    rng = _rng(seed)
    sub = str(subskill or "mixed").strip().lower()

    generators = {
        "sole_trader_characteristics": _gen_sole_trader,
        "partnerships_characteristics": _gen_partnerships,
        "close_corporation_characteristics": _gen_close_corporation,
        "companies_private_vs_public": _gen_companies,
        "smme_and_sustainable_job_creation": _gen_smme_job_creation,
        "liability_and_legal_persona_comparison": _gen_liability_comparison,
    }

    if sub in generators:
        fn = generators[sub]
        results = [fn(rng) for _ in range(count)]
    elif sub == "concepts":
        concept_fns = [_gen_sole_trader, _gen_partnerships, _gen_close_corporation, _gen_companies]
        results = [rng.choice(concept_fns)(rng) for _ in range(count)]
    else:
        # Mixed: sample across all 6 subskills
        all_fns = list(generators.values())
        results = [rng.choice(all_fns)(rng) for _ in range(count)]

    if count == 1 and len(results) == 1:
        return results[0]
    return results
