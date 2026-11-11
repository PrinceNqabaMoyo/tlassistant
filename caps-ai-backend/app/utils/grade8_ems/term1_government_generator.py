"""Grade 8 EMS — Government (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 1/01. Government.md

Covers CAPS subskills:
  1. three_levels_of_government: National, Provincial, Local (scope, leadership, responsibilities).
  2. roles_of_government_economy: Government as Consumer, Provider of public goods/utilities, and Regulator.
  3. circular_flow_government_role: Flow of taxes, goods/services, and public infrastructure between households, businesses, and government.
  4. municipal_service_delivery: Local government functions (water, electricity, sanitation, refuse removal).

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, AREAS

SUBSKILLS = [
    "three_levels_of_government",
    "roles_of_government_economy",
    "circular_flow_government_role",
    "municipal_service_delivery",
]

TOPIC_KEY = "grade8_ems_government"
LO = "g8_ems_government"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _gen_three_levels(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    level_data = [
        {
            "level": "Local government",
            "leader": "Mayor and Councillors (Ward Councillors)",
            "scope": "Municipality / District",
            "functions": "local service delivery such as clean water, electricity distribution, refuse removal, sanitation, and municipal roads",
            "distractor_1": "National government",
            "distractor_2": "Provincial government",
            "distractor_3": "Regional parliament",
        },
        {
            "level": "Provincial government",
            "leader": "Premier and Members of the Executive Council (MECs)",
            "scope": "Specific province (e.g. Gauteng, Western Cape, KwaZulu-Natal)",
            "functions": "regional healthcare, provincial public hospitals, provincial education administration, and provincial highways",
            "distractor_1": "Local government",
            "distractor_2": "National government",
            "distractor_3": "Municipal council",
        },
        {
            "level": "National government",
            "leader": "The President and Cabinet Ministers",
            "scope": "Entire country (South Africa)",
            "functions": "national policy, defense (SANDF), police service (SAPS), justice system, foreign affairs, and national fiscal legislation",
            "distractor_1": "Provincial government",
            "distractor_2": "Local government",
            "distractor_3": "Ward committee",
        },
    ]
    chosen = rng.choice(level_data)
    options = [chosen["level"], chosen["distractor_1"], chosen["distractor_2"], chosen["distractor_3"]]
    rng.shuffle(options)
    correct_idx = options.index(chosen["level"])
    correct_letter = chr(65 + correct_idx)

    prompt = (
        f"In South Africa, the state is structured into three distinct spheres or levels of government.\n\n"
        f"Which level of government has jurisdiction over the **{chosen['scope']}**, is led by **{chosen['leader']}**, "
        f"and is primarily responsible for **{chosen['functions']}**?"
    )
    ans = f"{correct_letter}. {chosen['level']}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** In South Africa, the **{chosen['level']}** is led by {chosen['leader']} and has constitutional "
        f"responsibility for {chosen['functions']} across {chosen['scope']}."
    )
    return {
        "id": f"g8_gov_lvl_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "Government",
        "subskill": "three_levels_of_government",
        "learning_objective_id": f"{LO}_three_levels",
        "archetype": "three_levels_classification",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(correct_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about who leads this level: {chosen['leader']}.",
            "tier_2": f"The scope is the {chosen['scope']}.",
            "tier_3": f"Correct level is {chosen['level']}.",
        },
        "misconception_tags": ["confuses_local_with_provincial_government"],
    }


def _gen_roles_of_government(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    roles = [
        {
            "role": "Consumer",
            "description": f"The government buys stationery, desks, computers, and building materials from private businesses in {scenario['area']} for local public schools.",
            "why": "The government acts as a consumer because it purchases goods and services produced by private businesses to carry out state operations.",
            "options": ["Consumer", "Producer", "Regulator", "Financier"],
            "correct": "Consumer",
        },
        {
            "role": "Producer / Provider",
            "description": f"The government provides public hospitals, clean municipal tap water, and street lighting to the residents of {scenario['area']}.",
            "why": "The government acts as a producer/provider because it directly supplies essential public utilities and services that benefit society as a whole.",
            "options": ["Producer / Provider", "Consumer", "Regulator", "Shareholder"],
            "correct": "Producer / Provider",
        },
        {
            "role": "Regulator",
            "description": f"The government passes the Basic Conditions of Employment Act (BCEA) and enforces health, safety, and competition standards on businesses in {scenario['area']}.",
            "why": "The government acts as a regulator because it creates and enforces legal rules, standards, and fair business practices to protect workers, consumers, and fair competition.",
            "options": ["Regulator", "Consumer", "Producer", "Borrower"],
            "correct": "Regulator",
        },
    ]
    chosen = rng.choice(roles)
    options = list(chosen["options"])
    rng.shuffle(options)
    correct_idx = options.index(chosen["correct"])
    correct_letter = chr(65 + correct_idx)

    prompt = (
        f"Consider the following economic activity involving the government in {scenario['area']}:\n\n"
        f"\"{chosen['description']}\"\n\n"
        f"Which primary economic role of the government does this action demonstrate?"
    )
    ans = f"{correct_letter}. {chosen['correct']}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {chosen['why']}"
    )
    return {
        "id": f"g8_gov_role_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "Government",
        "subskill": "roles_of_government_economy",
        "learning_objective_id": f"{LO}_roles",
        "archetype": "government_economic_roles",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(correct_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Government can act as a Consumer, a Producer/Provider of public goods, or a Regulator.",
            "tier_2": "Look at whether the government is buying goods, providing services, or enforcing laws.",
            "tier_3": f"This is an example of the government acting as a {chosen['correct']}.",
        },
        "misconception_tags": ["confusing_government_roles"],
    }


def _gen_circular_flow(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    prompt = (
        f"In the circular flow of economic activity, the government interacts continuously with both households and businesses:\n\n"
        f"1. What major payment do households and businesses make to the government?\n"
        f"2. State TWO essential public goods or services that the government provides in return to communities in places like {scenario['area']}."
    )
    ans = (
        "1. Taxes (such as Personal Income Tax and Corporate Income Tax);\n"
        "2. Public infrastructure/services such as roads, clean water, sanitation, public healthcare, and state education."
    )
    sol = (
        "**Model Answer** [4 marks]:\n\n"
        "1. **Taxes** [2 marks]: Households pay personal income tax (PAYE) and VAT; businesses pay company tax.\n"
        "2. **Public Goods/Services (any two)** [2 marks]:\n"
        "   - Public infrastructure (roads, bridges, streetlights)\n"
        "   - Essential services (potable water, sanitation, refuse removal)\n"
        "   - Social services (public hospitals, state schools, police protection)."
    )
    return {
        "id": f"g8_gov_flow_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "topic": "Government",
        "subskill": "circular_flow_government_role",
        "learning_objective_id": f"{LO}_circular_flow",
        "archetype": "government_circular_flow",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Taxes identified as government revenue from participants", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Two valid public services/infrastructure identified (1 mark each)", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Government gets money through taxation.",
            "tier_2": "In return for taxes, government builds roads, supplies water, and funds schools and hospitals.",
            "tier_3": f"1. Taxes. 2. Roads, water/electricity, education, healthcare.",
        },
        "misconception_tags": ["omitting_taxes_as_revenue_source"],
    }


def _gen_municipal_services(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    services = [
        ("potable tap water and sanitation (sewerage management)", "Local Municipality"),
        ("household waste and refuse collection", "Local Municipality"),
        ("national military defense (SANDF) and air defense", "National Government"),
        ("provincial public hospital networks and clinics", "Provincial Government"),
    ]
    svc, correct_gov = rng.choice(services)
    options = ["Local Municipality", "Provincial Government", "National Government", "Private Corporation"]
    correct_idx = options.index(correct_gov)
    correct_letter = chr(65 + correct_idx)

    prompt = (
        f"Which level of government is constitutionally responsible for providing and maintaining "
        f"**{svc}** in {scenario['area']}?"
    )
    ans = f"{correct_letter}. {correct_gov}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {correct_gov} is responsible for {svc} under the South African Constitution."
    )
    return {
        "id": f"g8_gov_svc_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "Government",
        "subskill": "municipal_service_delivery",
        "learning_objective_id": f"{LO}_municipal_services",
        "archetype": "service_delivery_allocation",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(correct_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Local municipalities handle daily neighbourhood services like water and refuse.",
            "tier_2": f"Consider the scope of {svc}.",
            "tier_3": f"Answer is {correct_gov}.",
        },
        "misconception_tags": ["confuses_local_with_provincial_services"],
    }


def generate(
    subskill: str = "mixed",
    seed: Optional[int] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    generators = {
        "three_levels_of_government": _gen_three_levels,
        "roles_of_government_economy": _gen_roles_of_government,
        "circular_flow_government_role": _gen_circular_flow,
        "municipal_service_delivery": _gen_municipal_services,
    }

    results: List[Dict[str, Any]] = []
    if subskill in generators:
        for _ in range(count):
            results.append(generators[subskill](rng))
        return results

    keys = list(generators.keys())
    for i in range(count):
        chosen = keys[i % len(keys)]
        results.append(generators[chosen](rng))
    return results
