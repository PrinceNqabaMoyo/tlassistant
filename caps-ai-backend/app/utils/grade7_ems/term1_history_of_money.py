"""Grade 7 EMS: Term 1 - History of Money Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 1/01. History of money.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "traditional_vs_modern_societies",
    "bartering_limitations",
    "promissory_notes_and_receipts",
    "evolution_of_money",
    "functions_of_money"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 1/01. History of money.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_traditional_vs_modern(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]
    occupations = [
        ("auto mechanic", "specialised trade services for money to buy food"),
        ("school teacher", "educational services in exchange for a salary"),
        ("registered nurse", "healthcare services and relies on shops for groceries"),
        ("software technician", "IT support and pays for municipal services electronically")
    ]
    occ, role_desc = rng.choice(occupations)

    prompt = (
        f"{person} lives in {area} and works as a {occ}, providing {role_desc}.\n\n"
        f"Does {person}'s community represent a **traditional society** or a **modern society**, and what is the key economic characteristic?"
    )
    correct_opt = "Modern society, because individuals have specialised skills and rely on trade/money for goods they cannot produce themselves."
    options = [
        correct_opt,
        "Traditional society, because all community members hunt and produce only for their own subsistence.",
        "Traditional society, because people rely exclusively on bartering livestock without currency.",
        "Neither, because modern societies do not use specialised skills or money."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify characteristics of society types:\n"
        f"A modern society is an industrialised society where people have specialised skills ({occ}) and trade their labour for money to buy goods they cannot make themselves.\n\n"
        f"Step 2: Compare with traditional societies:\n"
        f"Traditional societies are self-sufficient communities using basic hunting, gathering, and subsistence farming without formal technology or currency.\n\n"
        f"Conclusion: {person} lives in a modern society."
    )
    return {
        "id": f"g7_ems_money_trad_{rng.randint(100000, 999999)}",
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
        "subskill": "traditional_vs_modern_societies",
        "question_family_id": "traditional_vs_modern_societies",
        "curriculum_reference": "Term 1 > History of Money > Traditional vs Modern societies",
        "hints": {
            "tier_1": "Think about whether this community is self-sufficient or relies on specialised jobs and money.",
            "tier_2": "In a modern society, people specialize (like teachers or mechanics) and use money to buy goods.",
            "tier_3": f"Correct: Modern society with specialised skills and currency."
        }
    }


def _build_bartering_limitations(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person1 = scenario["entrepreneur"]
    person2 = rng.choice([n for n in NAMES if n != person1])
    area = scenario["area"]

    trades = [
        ("3 sacks of fresh cabbages", "a dairy cow", "Cabbages rot quickly (perishability) and a cow cannot easily be divided into small change without killing it"),
        ("5 woven reed baskets", "a bag of cement", "Both parties must want what the other has (double coincidence of wants)"),
        ("10 kg of ripe tomatoes", "a pair of leather boots", "Tomatoes spoil rapidly and do not have equal agreed value to the boots"),
        ("2 bags of maize meal", "a bicycle tyre", "Difficulty in agreeing on the exact exchange rate between different items")
    ]
    item1, item2, drawback = rng.choice(trades)

    prompt = (
        f"In an informal market near {area}, {person1} has {item1} and wants to trade with {person2} for {item2} using bartering (trading goods without money).\n\n"
        f"Identify the major economic problem or limitation with this barter transaction."
    )
    correct_opt = f"Problem: {drawback}."
    distractors = [
        "Bartering requires electronic banking terminals which may lose power.",
        "The South African Reserve Bank bans the exchange of physical goods between learners.",
        "Bartering only works when people use gold and silver coins."
    ]
    options = [correct_opt] + distractors
    rng.shuffle(options)

    sol = (
        f"Step 1: Define bartering:\n"
        f"Bartering is the direct exchange of goods and services without using money.\n\n"
        f"Step 2: Identify limitations from national curriculum:\n"
        f"Key limitations include:\n"
        f"- Double coincidence of wants (both people must want what the other is offering).\n"
        f"- Perishability (fresh food items spoil before a trade happens).\n"
        f"- Lack of divisibility (large items like cows cannot be split for small trades).\n"
        f"- Difficulty in determining a standard unit of value.\n\n"
        f"Conclusion: {drawback}."
    )
    return {
        "id": f"g7_ems_money_barter_{rng.randint(100000, 999999)}",
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
        "subskill": "bartering_limitations",
        "question_family_id": "bartering_limitations",
        "curriculum_reference": "Term 1 > History of Money > Bartering",
        "hints": {
            "tier_1": "Think about why trading fresh food for durable items or finding someone who wants your exact goods is difficult.",
            "tier_2": "Barter suffers from the 'double coincidence of wants', perishability, and indivisibility.",
            "tier_3": f"Correct: {correct_opt}"
        }
    }


def _build_promissory_notes(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    merchant = scenario["entrepreneur"]
    area = scenario["area"]
    deposit_amount = rng.choice([50, 100, 200, 500])

    prompt = (
        f"Historically, merchants in early trading towns deposited {deposit_amount} gold coins with trustworthy goldsmiths for safe keeping. "
        f"The goldsmith issued a written paper receipt promising to return the gold to the bearer on demand.\n\n"
        f"Explain how these **promissory notes** evolved into early paper money."
    )
    sol = (
        f"1. Safe Storage [1]: Traders deposited heavy, valuable gold coins with goldsmiths for safe keeping [1].\n"
        f"2. Written Receipts [1]: The goldsmith issued a written promissory note confirming the deposit of {deposit_amount} coins [1].\n"
        f"3. Circulating Medium [2]: Instead of carrying heavy gold, merchants began passing the signed paper receipts to other traders to pay for goods, "
        f"because people trusted the goldsmith would honour the promise to pay [1]. This receipt became early paper money [1]."
    )
    sample_ans = (
        "Traders deposited gold coins with goldsmiths for safety and received written promissory notes. "
        "Because carrying gold was dangerous, merchants began trading the paper receipts directly as payment, creating early paper currency."
    )
    return {
        "id": f"g7_ems_money_promissory_{rng.randint(100000, 999999)}",
        "question_type": "short_answer",
        "prompt": prompt,
        "correct_answer": sample_ans,
        "sample_answer": sample_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "diagram_spec": {
        "diagram_role": "context",
            "kind": "promissory_note",
            "amount": str(deposit_amount),
            "merchant": merchant,
            "city": area,
            "date": "14 March 1785"
        },
        "subskill": "promissory_notes_and_receipts",
        "question_family_id": "promissory_notes_and_receipts",
        "curriculum_reference": "Term 1 > History of Money > Promissory notes",
        "hints": {
            "tier_1": "Think about why carrying paper receipts was safer than carrying heavy bags of gold.",
            "tier_2": "Goldsmiths stored gold and wrote receipts. Merchants began trading the paper receipts directly.",
            "tier_3": "Promissory notes were trusted written promises to pay gold, which began circulating as paper money."
        }
    }


def _build_evolution_of_money(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]

    stages = [
        ("Commodity money", "using valuable goods like cattle, shells, or salt as currency"),
        ("Metallic coins", "stamping gold, silver, and copper into coins of standard weight"),
        ("Paper money", "banknotes issued and guaranteed by the South African Reserve Bank"),
        ("Electronic banking / EFTs", "digital transfers of funds between bank accounts using smartphones or ATMs")
    ]
    target_stage, desc = rng.choice(stages)

    prompt = (
        f"The development of currency has evolved through historical stages to facilitate trade in South Africa.\n\n"
        f"Which stage of the evolution of money is described by: '{desc}'?"
    )
    correct_opt = target_stage
    options = [s[0] for s in stages]
    rng.shuffle(options)

    sol = (
        f"Historical timeline of money:\n"
        f"1. Barter: Direct exchange of goods without currency.\n"
        f"2. Commodity money: Using practical goods (cattle, salt, cowrie shells).\n"
        f"3. Metallic coins: Standardised metal coins (gold, silver, bronze).\n"
        f"4. Paper money: Printed notes backed by central reserves.\n"
        f"5. Electronic banking: EFTs, debit cards, and digital transactions.\n\n"
        f"The description corresponds to: {target_stage}."
    )
    return {
        "id": f"g7_ems_money_evol_{rng.randint(100000, 999999)}",
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
        "subskill": "evolution_of_money",
        "question_family_id": "evolution_of_money",
        "curriculum_reference": "Term 1 > History of Money > The evolution of currency",
        "hints": {
            "tier_1": "Trace the timeline from cattle/shells to coins, paper banknotes, and electronic transfers.",
            "tier_2": f"Description refers to: {desc}.",
            "tier_3": f"Correct stage: {target_stage}."
        }
    }


def _build_functions_of_money(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]
    item = scenario["item_sold"]
    price = rng.choice([15, 25, 40, 80, 150])

    functions = [
        ("Medium of exchange", f"{person} hands over R{price} cash to buy {item} at a local shop in {area}, avoiding barter"),
        ("Unit of account (measure of value)", f"A price tag on a shelf in {area} indicates that {item} costs R{price}, allowing shoppers to compare values"),
        ("Store of value", f"{person} deposits R{price * 10} in a savings account to spend on school supplies next term")
    ]
    target_func, example = rng.choice(functions)

    prompt = (
        f"Consider the following everyday economic situation in {area}:\n"
        f"'{example}.'\n\n"
        f"Which of the primary **functions of money** is best demonstrated by this example?"
    )
    correct_opt = target_func
    options = [f[0] for f in functions] + ["Standard of production"]
    rng.shuffle(options)

    sol = (
        f"Primary functions of money in Grade 7 EMS:\n"
        f"1. Medium of exchange: Used to facilitate trade and purchase goods and services without bartering.\n"
        f"2. Unit of account: Provides a common denominator (Rand) to quote and compare prices.\n"
        f"3. Store of value: Allows people to save purchasing power for future use.\n\n"
        f"In this scenario, '{example}' directly illustrates the function of: {target_func}."
    )
    return {
        "id": f"g7_ems_money_func_{rng.randint(100000, 999999)}",
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
        "subskill": "functions_of_money",
        "question_family_id": "functions_of_money",
        "curriculum_reference": "Term 1 > History of Money > The role of money",
        "hints": {
            "tier_1": "Is money being used to buy something, measure a price, or save for the future?",
            "tier_2": "Medium of exchange = buying; Unit of account = pricing; Store of value = saving.",
            "tier_3": f"Correct function: {target_func}."
        }
    }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Main entry point for Grade 7 History of Money generator."""
    rng = _rng(seed)
    questions = []

    target_sub = str(subskill or "").strip().lower()

    def _build_one(sub_name: str) -> Dict[str, Any]:
        if "trad" in sub_name or "modern" in sub_name:
            return _build_traditional_vs_modern(rng)
        elif "barter" in sub_name:
            return _build_bartering_limitations(rng)
        elif "promiss" in sub_name or "note" in sub_name or "receipt" in sub_name:
            return _build_promissory_notes(rng)
        elif "evol" in sub_name or "coin" in sub_name or "eft" in sub_name:
            return _build_evolution_of_money(rng)
        elif "func" in sub_name or "role" in sub_name:
            return _build_functions_of_money(rng)
        return _build_traditional_vs_modern(rng)

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        for _ in range(count):
            questions.append(_build_one(target_sub))
        return questions

    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(_build_one(sub))

    return questions
