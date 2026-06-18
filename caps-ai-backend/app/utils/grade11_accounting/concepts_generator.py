from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ..grade10_accounting.scenario_builder import build_scenario


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str, mode: str) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_concepts_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "expected_answer_type": "mcq",
        "guidelines": [explanation],
    }
    if str(mode or "").strip().lower() == "scaffold":
        out["explanation"] = explanation
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_concepts_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
        "guidelines": [f"Sample expected answer: {sample_answer}"],
    }
    if str(mode or "").strip().lower() == "scaffold":
        out["sample_answer"] = sample_answer
    return out


def _make_table_wordbank(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[str]],
    word_bank: List[Dict[str, str]],
    correct_map: Dict[str, Dict[str, Optional[str]]],
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_concepts_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {
            "headers": headers,
            "rows": rows,
        },
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "table_wordbank",
    }


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    partnerships_pool: List[Dict[str, Any]] = []
    ethics_pool: List[Dict[str, Any]] = []
    gaap_adjustments_pool: List[Dict[str, Any]] = []
    matching_pool: List[Dict[str, Any]] = []

    scenario1 = build_scenario(seed=seed)
    scenario2 = build_scenario(seed=(seed + 1) if seed else random.randint(1, 1000))

    partnerships_pool.append(
        _make_mcq(
            prompt=f"{scenario1['intro']}\n\n#### REQUIRED:\nWhat is the main aim of {scenario1['business']}?",
            options=[
                "increase assets only",
                "make a profit",
                "avoid paying expenses",
                "reduce liabilities to zero",
            ],
            correct_index=1,
            explanation="The main aim of a business is to make a profit.",
            mode=mode_norm,
        )
    )

    partnerships_pool.append(
        _make_mcq(
            prompt=f"In the books of {scenario2['business']}, Owner's equity is best described as:",
            options=[
                "money owed by the owner to the business",
                "the owner's interest in the business (what the business owes the owner)",
                "all the business expenses",
                "only the value of fixed assets",
            ],
            correct_index=1,
            explanation="Owner's equity is the owner's interest in the business (the amount the business owes to the owner).",
            mode=mode_norm,
        )
    )

    partnerships_pool.append(
        _make_typed(
            prompt=f"{scenario1['intro']}\n\n#### REQUIRED:\nExplain the difference between gross profit and net profit to {scenario1['owner']}.",
            sample_answer="Gross profit = (Sales - Debtors allowances) - Cost of Sales. Net profit = Gross profit + Income - Expenses.",
            mode=mode_norm,
        )
    )

    gaap_adjustments_pool.append(
        _make_mcq(
            prompt=f"{scenario2['intro']}\n\n#### REQUIRED:\nWhy should {scenario2['business']} make year-end adjustments?",
            options=[
                "To hide losses",
                "To ensure income and expenses are recorded in the correct accounting period",
                "To increase drawings",
                "To reduce stock",
            ],
            correct_index=1,
            explanation="Adjustments ensure accurate financial statements by matching income/expenses to the correct period and correcting balances according to GAAP.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_mcq(
            prompt=f"Which principle requires {scenario1['owner']} to act without bias and not be influenced by personal feelings?",
            options=["Objectivity", "Integrity", "Confidentiality", "Discipline"],
            correct_index=0,
            explanation="Objectivity is the ability to act in an unbiased way and base decisions on true facts.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario2['intro']}\n\n#### REQUIRED:\nGive one example of how {scenario2['owner']} can show integrity at work.",
            sample_answer=f"Example: {scenario2['owner']} is honest, follows the same rules as everyone, and does not use their position for personal gain.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_mcq(
            prompt=f"{scenario1['intro']}\n\n#### REQUIRED:\nWhat does 'triple bottom line' accounting refer to?",
            options=[
                "Reporting only on financial performance",
                "Reporting on and disclosing information about financial, social and environmental performance (people, planet, profit)",
                "Reporting only on social performance",
                "Reporting only on environmental performance"
            ],
            correct_index=1,
            explanation="The triple bottom line refers to reporting on financial, social and environmental performance (people, planet, profit).",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario2['intro']}\n\n#### REQUIRED:\nWhat is a 'code of ethics' in a business?",
            sample_answer="A code of ethics is a written set of rules and guidelines outlining the moral standards and ethical principles by which a business and all of its employees should conduct themselves.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario1['intro']}\n\n#### REQUIRED:\nExplain what 'Integrated reporting' means for a company.",
            sample_answer="Integrated reporting means companies reporting not only on their financial performance, but also on their social performance and their impact on the environment.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_table_wordbank(
            prompt="Match the ethics and internal control definitions with the correct term.",
            headers=["#", "Definition", "Term", ""],
            rows=[
                ["1", "Taking responsibility for what you say and do; being able to justify your actions.", "", ""],
                ["2", "Behaviour must be such that it is clear that you have nothing to hide.", "", ""],
                ["3", "Can be defined as honesty and upholding values and norms.", "", ""],
                ["4", "The ability to maintain economic, social and environmental resources.", "", ""]
            ],
            word_bank=[
                {"id": "t0", "label": "Accountability"},
                {"id": "t1", "label": "Transparency"},
                {"id": "t2", "label": "Integrity"},
                {"id": "t3", "label": "Sustainability"},
                {"id": "t4", "label": "Fairness"},
                {"id": "t5", "label": "Objectivity"}
            ],
            correct_map={
                "0": {"2": "t0", "3": None},
                "1": {"2": "t1", "3": None},
                "2": {"2": "t2", "3": None},
                "3": {"2": "t3", "3": None}
            },
            guidelines=[
                "Read each definition carefully.",
                "Choose one term from the word bank for each row."
            ]
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario1['intro']}\n\n{scenario1['owner']} has selected their nephew for the position of manager despite the nephew lacking the required qualifications and experience.\n\n#### REQUIRED:\nExplain which ethical principle is being violated here, and why it is important for {scenario1['owner']} to be objective.",
            sample_answer=f"The ethical principle being violated is objectivity / transparency. {scenario1['owner']} is showing bias (nepotism / favouritism). It is important to be objective so that employees are selected on merit, ensuring the business performs at its best and fairness is maintained.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario2['intro']}\n\nAn employee of {scenario2['business']} has been using the company delivery vehicle to transport personal goods on weekends without permission.\n\n#### REQUIRED:\nIdentify the internal control risk in this scenario, and suggest TWO internal control measures {scenario2['owner']} can implement to prevent this.",
            sample_answer="Risk: Unauthorised use of business assets (vehicle misuse) leading to wear and tear, and fuel theft.\nInternal controls: \n1. Keep vehicle keys locked in a safe and require sign-out logs.\n2. Compare vehicle mileage logs to authorised delivery routes.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario1['intro']}\n\n{scenario1['owner']} noticed that the cashier does not always deposit the cash received on the same day. She sometimes 'borrows' the cash for personal expenses and 'pays it back' at the end of the month.\n\n#### REQUIRED:\nExplain why this behaviour is unethical and state ONE internal control measure that should be put in place regarding cash deposits.",
            sample_answer="This is unethical because it is essentially theft/fraud (rolling of cash); she is using business funds for personal use without authorisation. Internal control: Cash must be deposited daily, and duties should be divided so the person collecting cash is not the same person depositing and recording it (segregation of duties).",
            mode=mode_norm,
        )
    )

    matching_items = [
        {"definition": "Taking responsibility for what you say and do; being able to justify your actions.", "term": "Accountability"},
        {"definition": "Behaviour must be such that it is clear that you have nothing to hide.", "term": "Transparency"},
        {"definition": "The ability to act in an unbiased way.", "term": "Objectivity"},
        {"definition": "Can be defined as honesty and upholding values and norms.", "term": "Integrity"},
    ]
    distractors = ["Fairness", "Sustainability", "Professional conduct", "Discipline"]

    r.shuffle(matching_items)
    used_distractors = r.sample(distractors, k=2)
    terms = [m["term"] for m in matching_items] + used_distractors
    r.shuffle(terms)

    word_bank: List[Dict[str, str]] = [{"id": f"t{i}", "label": t} for i, t in enumerate(terms)]
    label_to_id = {t["label"]: t["id"] for t in word_bank}

    rows: List[List[str]] = []
    correct_map: Dict[str, Dict[str, Optional[str]]] = {}
    for i, item in enumerate(matching_items):
        rows.append([str(i + 1), item["definition"], "", ""])
        correct_map[str(i)] = {"2": str(label_to_id[item["term"]]), "3": None}

    matching_pool.append(
        _make_table_wordbank(
            prompt="Match each definition with the correct term.",
            headers=["#", "Definition", "Term", ""],
            rows=rows,
            word_bank=word_bank,
            correct_map=correct_map,
            guidelines=[
                "Read each definition carefully.",
                "Choose one term from the word bank for each row.",
            ],
        )
    )

    pools = {
        "partnerships": partnerships_pool,
        "ethics": ethics_pool,
        "gaap": gaap_adjustments_pool,
        "adjustments": gaap_adjustments_pool,
        "matching": matching_pool,
        "mixed": partnerships_pool + ethics_pool + gaap_adjustments_pool + matching_pool,
    }

    pool = pools.get(subskill_norm, pools["mixed"])

    if qtype_norm != "mixed":
        if qtype_norm == "mcq":
            pool = [q for q in pool if q.get("question_type") == "mcq"]
        elif qtype_norm in {"typed", "text"}:
            pool = [q for q in pool if q.get("question_type") == "typed"]
        elif qtype_norm in {"table_wordbank", "matching"}:
            pool = [q for q in pool if q.get("question_type") == "table_wordbank"]

    if not pool:
        pool = pools["mixed"]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))

    return out
