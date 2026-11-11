"""Grade 7 EMS — Term 4: Savings & Banking (Deterministic 6-Pillar Generator).
100% aligned with South African National Curriculum Standards (EMS Grade 7, Term 4).
Directly grounded in curriculum_docs_auto/EMS_Gr7/Term 4/01. Savings.md.

Covers:
1. personal_savings_calc: Calculating monthly savings (Income - Expenses) and definition.
2. purpose_of_savings: Purposes of saving (avoiding high-interest debt, emergency fund, future goals).
3. stokvel_mechanics: Indigenous community rotational savings clubs and lump-sum payout calculations.
4. role_and_services_of_banks: Safekeeping, earning interest, payment transfers (EFT), loans.
5. capital_sources: Loan capital (repayable with interest) vs Partner equity capital (shared ownership).

Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints and 6-pillar contract.
"""
from __future__ import annotations
from app.utils.ems_namelist import get_ems_scenario

import random
from typing import Any, Dict, List, Optional

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term4_savings"
CURRICULUM_REF = "EMS Grade 7 > Term 4 > Savings and Banking"

SA_NAMES = ["Sipho", "Lerato", "Kagiso", "Zanele", "Thabo", "Nomsa", "Bongani", "Nandi", "Andile", "Mpho"]
BANKS_SA = ["Standard Bank", "First National Bank (FNB)", "Nedbank", "Absa", "Capitec"]

SUBSKILLS = [
    "personal_savings_calc",
    "purpose_of_savings",
    "stokvel_mechanics",
    "role_and_services_of_banks",
    "capital_sources"
]


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)


def _with_metadata(item: Dict[str, Any], **meta) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "curriculum_reference": CURRICULUM_REF,
        "misconception_tags": meta.get("misconception_tags", []),
        "diagnostic_tags": meta.get("diagnostic_tags", ["financial_literacy", "savings"]),
        "learning_objective_id": meta.get("learning_objective_id", "lo_g7_ems_savings"),
        "question_family_id": meta.get("question_family_id", meta.get("subskill", "savings_basics")),
        "subskill": meta.get("subskill", "savings_basics"),
        "modality": item.get("modality") or ("math" if item.get("question_type") == "mcq" else "semantic"),
        "solution_type": item.get("solution_type") or item.get("question_type", "typed"),
    })
    return enriched


def _build_savings_pool(r: random.Random) -> Dict[str, Dict[str, Any]]:
    name = r.choice(SA_NAMES)
    bank = r.choice(BANKS_SA)

    # 1. Personal Savings Calculation & Definition
    income = r.randint(25, 60) * 100
    expenses = income - r.randint(4, 15) * 100
    surplus = income - expenses

    prompt1 = (
        f"{name} earns a monthly income of R{income:,} from work and chores. "
        f"After paying monthly personal expenses totaling R{expenses:,}, "
        f"{name} deposits the remaining amount into a savings account at {bank}.\n\n"
        f"1. Define personal savings.\n"
        f"2. Calculate the exact amount {name} saves each month."
    ).replace(",", " ")

    memo1 = (
        f"1. Personal savings is the money left over after all personal expenses have been paid from total income. [2]\n"
        f"2. Savings = Income - Expenses = R{income:,} - R{expenses:,} = R{surplus:,}. [2]"
    ).replace(",", " ")

    q1 = {
        "id": f"g7_ems_sav_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": prompt1,
        "marks": 4,
        "correct_answer": f"R{surplus:,}".replace(",", " "),
        "sample_answer": memo1,
        "explanation": memo1,
        "worked_solution": memo1,
        "canonical_solution": memo1,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of personal savings (income minus expenses)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct calculation of R{surplus:,} monthly savings", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Personal savings is what you have left after paying for all your needs and expenses.",
            "tier_2": "Use the formula: Savings = Total Income - Total Expenses.",
            "tier_3": f"Subtract R{expenses:,} from R{income:,}: Savings = R{surplus:,}."
        },
        "misconception_tags": ["income_vs_savings_confusion"],
    }

    # 2. Purpose of Savings
    purposes = [
        ("avoiding high-interest debt", "Buying items with savings prevents paying expensive interest on credit or store cards."),
        ("emergency fund", "Having savings ensures money is immediately available for unexpected crises (e.g. medical or repairs)."),
        ("future planning and education", "Saving allows individuals to afford major future goals such as university studies or tools.")
    ]
    p1, p2 = r.sample(purposes, 2)
    scenario = get_ems_scenario(r)
    prompt2 = (
        f"A financial advisor in {scenario['area']} consults with {scenario['entrepreneur']} on long-term family wealth.\n\n"
        f"Explain TWO important purposes of personal savings. (4 marks)"
    )
    memo2 = (
        f"1. {p1[0].capitalize()}: {p1[1]} [2]\n"
        f"2. {p2[0].capitalize()}: {p2[1]} [2]"
    )
    q2 = {
        "id": f"g7_ems_purp_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": prompt2,
        "marks": 4,
        "correct_answer": f"1. {p1[0]}; 2. {p2[0]}",
        "sample_answer": memo2,
        "explanation": memo2,
        "worked_solution": memo2,
        "canonical_solution": memo2,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"First valid purpose of savings ({p1[0]}) with explanation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Second valid purpose of savings ({p2[0]}) with explanation", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "strict",
        },
        "hints": {
            "tier_1": "Think about what happens when an unexpected expense occurs or when buying on credit.",
            "tier_2": "Savings protect against debt and provide security during emergencies.",
            "tier_3": "Valid points include avoiding debt, emergency funds, and saving for future education."
        },
        "misconception_tags": ["thinks_credit_is_cheaper_than_saving"],
    }

    # 3. Stokvel Mechanics
    members = r.choice([10, 12, 15, 20])
    monthly_contrib = r.choice([200, 250, 500, 1000])
    payout = members * monthly_contrib

    prompt3 = (
        f"A group of {members} community members in a South African township formed a stokvel. "
        f"Each member contributes R{monthly_contrib:,} into the fund at the start of each month. "
        f"Every month, the full pool is paid out to one rotational member.\n\n"
        f"1. Explain what a stokvel is.\n"
        f"2. Calculate the total monthly lump-sum payout received by each member during their turn."
    ).replace(",", " ")

    memo3 = (
        f"1. A stokvel is an indigenous community savings club where members contribute a fixed amount monthly, "
        f"and each member takes turns receiving the full rotational lump-sum payout. [3]\n"
        f"2. Payout = {members} members x R{monthly_contrib:,} = R{payout:,}. [2]"
    ).replace(",", " ")

    q3 = {
        "id": f"g7_ems_stokvel_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "headers": ["Stokvel Item", "Calculation / Members", "Amount (R)"],
        "rows": [
            [{"cell_id": "r0_c0", "value": "Monthly Contribution per Member", "editable": False}, {"cell_id": "r0_c1", "value": "1 Member", "editable": False}, {"cell_id": "r0_c2", "value": "", "expected": str(monthly_contrib), "editable": True}],
            [{"cell_id": "r1_c0", "value": "Total Monthly Pool Payout", "editable": False}, {"cell_id": "r1_c1", "value": f"{members} Members", "editable": False}, {"cell_id": "r1_c2", "value": "", "expected": str(payout), "editable": True}],
        ],
        "correct_map": {"r0_c2": str(monthly_contrib), "r1_c2": str(payout)},
        "prompt": prompt3,
        "marks": 5,
        "correct_answer": f"R{payout:,}".replace(",", " "),
        "sample_answer": memo3,
        "explanation": memo3,
        "worked_solution": memo3,
        "canonical_solution": memo3,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Explanation of stokvel (community savings club, rotational payout)", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": f"Correct calculation of payout ({members} x R{monthly_contrib:,} = R{payout:,})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "A stokvel is an informal community club pooling money together.",
            "tier_2": "Calculate total payout by multiplying number of members by monthly contribution.",
            "tier_3": f"Payout = {members} x R{monthly_contrib:,} = R{payout:,}."
        },
        "misconception_tags": ["stokvel_concept_misunderstanding"],
    }

    # 4. Role and Services of Commercial Banks
    prompt4 = (
        f"Commercial banks in South Africa (such as {bank}) play a vital role in the national economy.\n\n"
        f"1. State TWO key services that commercial banks provide to individuals.\n"
        f"2. Explain how banks encourage people to save money with them."
    )
    memo4 = (
        f"1. Bank services (any two): Safe storage of money, payment facilities (debit cards, EFTs, ATMs), and loan facilities. [2]\n"
        f"2. Banks encourage saving by paying interest on positive savings account balances, which grows the depositor's money over time. [2]"
    )
    q4 = {
        "id": f"g7_ems_banks_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": prompt4,
        "marks": 4,
        "correct_answer": "Safe storage and electronic payments; paying interest on savings balances.",
        "sample_answer": memo4,
        "explanation": memo4,
        "worked_solution": memo4,
        "canonical_solution": memo4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Two valid banking services for individuals", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Explanation of earning interest on savings deposits", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "strict",
        },
        "hints": {
            "tier_1": "Think about why people keep money in a bank rather than at home under a mattress.",
            "tier_2": "Banks provide security, debit cards, and reward savers with interest.",
            "tier_3": "Services: safe storage, ATM/EFT payments. Incentive: earning interest on deposits."
        },
        "misconception_tags": ["confuses_bank_charges_with_interest_earned"],
    }

    # 5. Loan Capital vs Partner Equity Capital
    startup_cost = r.choice([15000, 20000, 30000, 50000])
    interest_rate = r.choice([10, 12, 15])
    prompt5 = (
        f"{name} wants to start a small repair workshop requiring R{startup_cost:,} start-up capital. "
        f"{name} is deciding between borrowing the money from a bank (loan capital at {interest_rate}% interest) "
        f"or taking on a business partner.\n\n"
        f"1. State ONE key difference between borrowing loan capital from a bank and taking on a business partner.\n"
        f"2. Name TWO South African organisations that support and promote small entrepreneurs."
    ).replace(",", " ")

    memo5 = (
        f"1. Difference: Loan capital from a bank must be repaid with interest regardless of profit or loss. "
        f"A business partner invests equity capital in exchange for partial ownership and profit sharing, with no fixed repayment obligation. [3]\n"
        f"2. Support organisations (any two): SEDA (Small Enterprise Development Agency), the dti, NYDA (National Youth Development Agency). [2]"
    )
    q5 = {
        "id": f"g7_ems_capital_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": prompt5,
        "marks": 5,
        "correct_answer": "Loan capital must be repaid with interest; partner equity shares ownership and profits without repayment obligation.",
        "sample_answer": memo5,
        "explanation": memo5,
        "worked_solution": memo5,
        "canonical_solution": memo5,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Loan capital must be repaid with interest even if business fails", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Partner equity provides ownership share, no debt repayment", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Two valid South African support bodies (SEDA, dti, NYDA)", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Consider who owns a share of the business and who must be repaid.",
            "tier_2": "A loan creates a debt with interest; a partner buys into the business.",
            "tier_3": "Support bodies include SEDA and the dti / NYDA."
        },
        "misconception_tags": ["loan_vs_equity_confusion"],
    }

    return {
        "personal_savings_calc": _with_metadata(q1, subskill="personal_savings_calc", learning_objective_id="lo_g7_savings_def"),
        "purpose_of_savings": _with_metadata(q2, subskill="purpose_of_savings", learning_objective_id="lo_g7_savings_purpose"),
        "stokvel_mechanics": _with_metadata(q3, subskill="stokvel_mechanics", learning_objective_id="lo_g7_stokvel"),
        "role_and_services_of_banks": _with_metadata(q4, subskill="role_and_services_of_banks", learning_objective_id="lo_g7_bank_services"),
        "capital_sources": _with_metadata(q5, subskill="capital_sources", learning_objective_id="lo_g7_capital_sources"),
    }


def generate(subskill: str = "savings", difficulty: str = "medium", count: int = 1, mode: str = "scaffold", seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    pool_dict = _build_savings_pool(r)
    target_sub = str(subskill or "").strip().lower()

    if target_sub in pool_dict:
        return [pool_dict[target_sub]]

    # If count requested, return distinct questions across the 5 subskills
    questions = []
    for i in range(count):
        sub_key = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(pool_dict[sub_key])
    return questions
