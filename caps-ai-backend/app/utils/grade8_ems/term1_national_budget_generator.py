"""Grade 8 EMS — The National Budget (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 1/02. The National Budget.md

Covers CAPS subskills:
  1. direct_vs_indirect_taxes: Income Tax (PAYE) vs VAT, fuel levy, excise/sin taxes.
  2. government_expenditure_categories: Education, health, housing/infrastructure, social development grants, safety & security.
  3. budget_balance_and_national_debt: Revenue vs expenditure, budget deficit, state borrowing, and servicing national debt.
  4. role_of_national_treasury: Minister of Finance, National Treasury, and the annual budget speech.

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, AREAS

SUBSKILLS = [
    "direct_vs_indirect_taxes",
    "government_expenditure_categories",
    "budget_balance_and_national_debt",
    "role_of_national_treasury",
]

TOPIC_KEY = "grade8_ems_national_budget"
LO = "g8_ems_national_budget"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _gen_direct_vs_indirect(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    tax_cases = [
        (
            f"When {scenario['entrepreneur']} earns income from running a registered business and pays Personal Income Tax directly to SARS,",
            "Direct tax",
            "Direct tax is paid straight by the individual or entity earning the income directly to the South African Revenue Service (SARS).",
            ["Direct tax", "Indirect tax", "Customs duty", "Municipal tariff"],
        ),
        (
            f"When customers buy products from a retail shop in {scenario['area']} and pay 15% Value-Added Tax (VAT) included in the retail price,",
            "Indirect tax",
            "VAT is an indirect tax because the shop acts as an intermediary collecting the tax on behalf of SARS; the consumer bears the economic burden indirectly.",
            ["Indirect tax", "Direct tax", "Corporate income tax", "Capital gains tax"],
        ),
        (
            f"When motorists in {scenario['area']} buy petrol or diesel and pay the fuel levy and Road Accident Fund (RAF) levy built into the fuel price,",
            "Indirect tax",
            "The fuel levy is an indirect tax added to the purchase price of goods rather than levied directly on a person's income.",
            ["Indirect tax", "Direct tax", "PAYE tax", "Donations tax"],
        ),
        (
            f"When a company deducts Pay-As-You-Earn (PAYE) each month from an employee's salary and pays it over to SARS,",
            "Direct tax",
            "PAYE is a direct tax on personal earnings, paid directly from the worker's taxable salary to the government.",
            ["Direct tax", "Indirect tax", "Excise duty", "Value-Added Tax"],
        ),
    ]
    stmt, tax_type, explanation, options = rng.choice(tax_cases)
    rng.shuffle(options)
    c_idx = options.index(tax_type)
    correct_letter = chr(65 + c_idx)

    prompt = (
        f"{stmt} what type of taxation is this classified as under South African public finance?"
    )
    ans = f"{correct_letter}. {tax_type}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {explanation}"
    )
    return {
        "id": f"g8_bud_tax_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "The National Budget",
        "subskill": "direct_vs_indirect_taxes",
        "learning_objective_id": f"{LO}_tax_types",
        "archetype": "tax_type_classification",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Direct tax is paid directly on income or profits (e.g. Income tax/PAYE).",
            "tier_2": "Indirect tax is added onto the price of goods and services (e.g. VAT, excise duties).",
            "tier_3": f"Correct answer is {tax_type}.",
        },
        "misconception_tags": ["confuses_direct_with_indirect_tax"],
    }


def _gen_expenditure_categories(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    expenditures = [
        (
            "Building new primary and secondary schools, providing textbooks, and paying teachers' salaries in South Africa.",
            "Education and basic learning",
            ["Education and basic learning", "Defense and military", "Transport and freight", "Foreign affairs"],
            "Education",
        ),
        (
            "Distributing Old Age pensions, Child Support Grants, and Disability Grants to vulnerable citizens through SASSA.",
            "Social Development and Grants",
            ["Social Development and Grants", "Trade and industry", "Agriculture and forestry", "Environmental protection"],
            "Social development",
        ),
        (
            "Constructing public clinics and regional hospitals, procuring vaccines, and employing doctors and nurses.",
            "Healthcare and medical services",
            ["Healthcare and medical services", "Tourism and marketing", "Postal communication", "Mining exploration"],
            "Healthcare",
        ),
        (
            "Upgrading the South African Police Service (SAPS), courts, and correctional services to fight crime.",
            "Peace and Safety & Security",
            ["Peace and Safety & Security", "Recreation and arts", "Housing developments", "Water irrigation"],
            "Safety and Security",
        ),
    ]
    action, category, options, short_name = rng.choice(expenditures)
    rng.shuffle(options)
    c_idx = options.index(category)
    correct_letter = chr(65 + c_idx)

    prompt = (
        f"In the South African National Budget, government revenue is allocated across major expenditure functional categories.\n\n"
        f"Under which primary category of government expenditure does the following spending fall:\n"
        f"\"{action}\"?"
    )
    ans = f"{correct_letter}. {category}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** Allocations for {action.lower()} fall under **{category}** in the National Budget."
    )
    return {
        "id": f"g8_bud_exp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "The National Budget",
        "subskill": "government_expenditure_categories",
        "learning_objective_id": f"{LO}_expenditure",
        "archetype": "budget_expenditure_allocation",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Look at the purpose of the funds: {short_name}.",
            "tier_2": f"Select the matching functional area from the budget options.",
            "tier_3": f"Answer is {category}.",
        },
        "misconception_tags": ["misclassifying_government_expenditure"],
    }


def _gen_budget_balance_and_debt(rng: random.Random) -> Dict[str, Any]:
    revenue_bn = rng.randint(1700, 2100)
    expenditure_bn = revenue_bn + rng.randint(200, 380)
    deficit_bn = expenditure_bn - revenue_bn

    prompt = (
        f"The Minister of Finance presents the annual National Budget to Parliament with the following projected figures:\n"
        f"- Projected Government Tax Revenue: **R{revenue_bn} billion**\n"
        f"- Projected Government Total Expenditure: **R{expenditure_bn} billion**\n\n"
        f"1. Is the government running a budget surplus or a budget deficit? Calculate the exact amount in Rands.\n"
        f"2. How must the government fund this shortfall, and what economic consequence does this have for South Africa's national debt?"
    )
    ans = (
        f"1. Budget deficit of R{deficit_bn} billion;\n"
        f"2. The government must borrow money (issue government bonds / take international loans), which increases national debt and debt-servicing costs."
    )
    sol = (
        f"**Model Answer** [4 marks]:\n\n"
        f"1. **Budget Deficit** [2 marks]:\n"
        f"   Expenditure (R{expenditure_bn} bn) exceeds Revenue (R{revenue_bn} bn).\n"
        f"   Deficit = R{expenditure_bn} billion - R{revenue_bn} billion = **R{deficit_bn} billion**.\n\n"
        f"2. **Funding and National Debt** [2 marks]:\n"
        f"   The state funds the deficit through borrowing (selling government bonds) [1 mark]. "
        f"   This increases the country's **national debt** and raises future interest payments (debt-service costs) [1 mark]."
    )
    return {
        "id": f"g8_bud_bal_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "topic": "The National Budget",
        "subskill": "budget_balance_and_national_debt",
        "learning_objective_id": f"{LO}_balance_debt",
        "archetype": "budget_deficit_and_debt",
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
                {"id": "mp1", "desc": f"Correct deficit identification and calculation of R{deficit_bn} billion", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Identification of government borrowing / bond issues", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Consequence: increase in national debt and debt servicing costs", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"When spending exceeds revenue, it is a deficit: {expenditure_bn} - {revenue_bn}.",
            "tier_2": "The shortfall must be borrowed from financial markets.",
            "tier_3": f"Deficit = R{deficit_bn} billion. Borrowing adds to national debt.",
        },
        "misconception_tags": ["confusing_surplus_and_deficit", "omitting_debt_interest_costs"],
    }


def _gen_national_treasury(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In South Africa, which government department is tasked with preparing the annual National Budget, "
        "managing public finances, and allocating revenue to provincial and national departments?"
    )
    options = ["The National Treasury", "The Reserve Bank (SARB)", "The Auditor-General", "The Department of Trade and Industry"]
    c_idx = 0
    ans = "A. The National Treasury"
    sol = (
        "**A. The National Treasury** [2 marks]\n\n"
        "**Explanation:** The **National Treasury**, led by the Minister of Finance, is responsible for preparing the National Budget, "
        "managing government spending, and coordinating fiscal policy under the Public Finance Management Act (PFMA)."
    )
    return {
        "id": f"g8_bud_trs_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "The National Budget",
        "subskill": "role_of_national_treasury",
        "learning_objective_id": f"{LO}_treasury_role",
        "archetype": "treasury_role_check",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": "0",
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "The department led by the Minister of Finance.",
            "tier_2": "Responsible for government finances (Treasury).",
            "tier_3": "Correct answer is The National Treasury.",
        },
        "misconception_tags": ["confusing_treasury_with_reserve_bank"],
    }


def generate(
    subskill: str = "mixed",
    seed: Optional[int] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    generators = {
        "direct_vs_indirect_taxes": _gen_direct_vs_indirect,
        "government_expenditure_categories": _gen_expenditure_categories,
        "budget_balance_and_national_debt": _gen_budget_balance_and_debt,
        "role_of_national_treasury": _gen_national_treasury,
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
