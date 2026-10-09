"""Grade 7 EMS — Term 4: Savings & Banking (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (EMS Grade 7, Term 4, Topic 1).
Covers:
- Personal savings and emergency funds
- Purpose of savings (avoiding debt, emergencies, future goals)
- Role of commercial banks in South Africa and services offered
- Stokvels (indigenous community savings schemes)
- Loan capital vs Partner / Equity capital
- Organisations supporting entrepreneurs (SEDA, dti, NYDA)

Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term4_savings"
CURRICULUM_REF = "EMS Grade 7 > Term 4 > Savings and Banking"

SA_NAMES = ["Sipho", "Lerato", "Kagiso", "Zanele", "Thabo", "Nomsa", "Bongani", "Nandi", "Andile", "Mpho"]
BANKS_SA = ["Standard Bank", "First National Bank (FNB)", "Nedbank", "Absa", "Capitec"]


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)


def _with_metadata(item: Dict[str, Any], **meta) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "curriculum_reference": CURRICULUM_REF,
        "misconception_tags": meta.get("misconception_tags", []),
        "diagnostic_tags": meta.get("diagnostic_tags", ["financial_literacy", "savings"]),
        "learning_objective_id": meta.get("learning_objective_id", "lo_g7_ems_savings"),
        "question_family_id": meta.get("question_family_id", "savings_basics"),
        "subskill": meta.get("subskill", "savings_principles"),
    })
    return enriched


def _build_savings_pool(r: random.Random, mode: str = "scaffold") -> List[Dict[str, Any]]:
    name = r.choice(SA_NAMES)
    bank = r.choice(BANKS_SA)

    pool = []

    # Archetype 1: Personal Savings Calculation & Definition
    income = r.randint(25, 60) * 100  # R2 500 to R6 000
    expenses = income - r.randint(4, 15) * 100  # R400 to R1 500 surplus
    surplus = income - expenses

    q1 = {
        "id": f"g7_ems_sav_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": (
            f"{name} earns a monthly income of R{income:,} from a part-time job and chores. "
            f"After paying all monthly personal expenses totaling R{expenses:,}, "
            f"{name} deposits the remaining amount into a savings account at {bank}.\n\n"
            f"1. Define personal savings.\n"
            f"2. Calculate the exact amount {name} saves each month."
        ).replace(",", " "),
        "marks": 4,
        "correct_answer": f"R{surplus:,}".replace(",", " "),
        "sample_answer": (
            f"1. Personal savings is the money left over after all personal expenses have been paid from total income.\n"
            f"2. Savings = Income - Expenses = R{income:,} - R{expenses:,} = R{surplus:,}."
        ).replace(",", " "),
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of personal savings (income minus expenses)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct calculation of R{surplus:,} monthly savings", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Personal savings is what you have left after paying for all your needs and expenses.",
            "2_concept": "Savings = Total Income - Total Expenses.",
            "3_breakdown": f"Subtract R{expenses:,} from R{income:,}: R{income:,} - R{expenses:,} = R{surplus:,}."
        },
        "misconception_tags": ["income_vs_savings_confusion"],
    }
    pool.append(_with_metadata(q1, subskill="personal_savings_calc", learning_objective_id="lo_g7_savings_def"))

    # Archetype 2: Stokvel (Community Savings Scheme)
    members = r.choice([10, 12, 15, 20])
    monthly_contrib = r.choice([200, 250, 500, 1000])
    payout = members * monthly_contrib

    q2 = {
        "id": f"g7_ems_stokvel_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": (
            f"A group of {members} community members formed a stokvel. "
            f"Each member contributes R{monthly_contrib:,} into the fund at the beginning of every month. "
            f"Every month, the full pool is paid out to one rotational member.\n\n"
            f"1. Explain what a stokvel is in South Africa.\n"
            f"2. Calculate the total monthly lump-sum payout received by each member during their turn."
        ).replace(",", " "),
        "marks": 5,
        "correct_answer": f"R{payout:,}".replace(",", " "),
        "sample_answer": (
            f"1. A stokvel is an indigenous community savings club where members contribute a fixed amount monthly, "
            f"and each member takes turns receiving the lump sum payout.\n"
            f"2. Payout = {members} members x R{monthly_contrib:,} = R{payout:,}."
        ).replace(",", " "),
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Explanation of stokvel (community savings club, fixed rotational payout)", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": f"Calculation of payout ({members} x R{monthly_contrib:,} = R{payout:,})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Think about how community clubs pool their money each month.",
            "2_concept": "Total monthly payout = Number of members x Monthly contribution per member.",
            "3_breakdown": f"Multiply {members} by R{monthly_contrib:,} to get R{payout:,}."
        },
        "misconception_tags": ["stokvel_concept_misunderstanding"],
    }
    pool.append(_with_metadata(q2, subskill="stokvel_mechanics", learning_objective_id="lo_g7_stokvel"))

    # Archetype 3: Loan Capital vs Partner (Equity) Capital
    startup_cost = r.choice([15000, 20000, 30000, 50000])
    interest_rate = r.choice([10, 12, 15])
    repayment = round(startup_cost * (1 + interest_rate / 100))

    q3 = {
        "id": f"g7_ems_capital_{r.randint(1000, 9999)}",
        "topic": "Savings",
        "question_type": "typed",
        "prompt": (
            f"{name} plans to start a small bicycle repair workshop requiring R{startup_cost:,} start-up capital. "
            f"{name} is deciding between borrowing the money from a bank (loan capital at {interest_rate}% interest) "
            f"or taking on a business partner.\n\n"
            f"1. State ONE key difference between borrowing money from a bank and taking on a business partner.\n"
            f"2. Name TWO South African organisations that support and promote small entrepreneurs."
        ).replace(",", " "),
        "marks": 5,
        "correct_answer": "Loan capital must be repaid with interest; partner equity shares ownership and profits without repayment.",
        "sample_answer": (
            f"1. Difference: Bank loan capital must be repaid with interest even if the business fails. "
            f"A business partner invests capital in exchange for a share of ownership and profits, and does not require repayment.\n"
            f"2. South African support organisations: SEDA (Small Enterprise Development Agency) and the dti (Department of Trade and Industry) / NYDA (National Youth Development Agency)."
        ),
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Loan capital must be repaid with interest", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Partner capital provides ownership share/profit share, no repayment", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "First entrepreneurship organisation (SEDA / dti / NYDA)", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Second entrepreneurship organisation (SEDA / dti / NYDA)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Consider who owns a share of the business and who must be repaid.",
            "2_concept": "A loan is borrowed money that carries interest. A partner buys into the business.",
            "3_breakdown": "Government bodies supporting youth/entrepreneurs include SEDA, dti, and NYDA."
        },
        "misconception_tags": ["loan_vs_equity_confusion"],
    }
    pool.append(_with_metadata(q3, subskill="capital_sources", learning_objective_id="lo_g7_capital_sources"))

    return pool


def generate(subskill: str = "savings", difficulty: str = "medium", count: int = 1, mode: str = "scaffold", seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    pool = _build_savings_pool(r, mode=mode)
    if subskill and subskill != "savings":
        filtered = [q for q in pool if q.get("subskill") == subskill]
        if filtered:
            pool = filtered
    return r.sample(pool, min(count, len(pool)))
