from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional


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
        "id": _make_id("acct12_concepts_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "expected_answer_type": "mcq",
    }
    if str(mode or "").strip().lower() == "scaffold":
        out["explanation"] = explanation
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct12_concepts_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
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
        "id": _make_id("acct12_concepts_table_wordbank"),
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

    company_basics_pool: List[Dict[str, Any]] = []
    company_governance_pool: List[Dict[str, Any]] = []
    matching_pool: List[Dict[str, Any]] = []

    company_basics_pool.append(
        _make_mcq(
            prompt="A company is a separate legal entity. This means:",
            options=[
                "the shareholders own the company assets in their personal capacity",
                "the company can enter contracts and own assets in its own name",
                "the directors are personally responsible for all company debts",
                "the company does not pay tax",
            ],
            correct_index=1,
            explanation="A separate legal entity can own assets, enter contracts, sue/be sued, and is responsible for its own obligations.",
            mode=mode_norm,
        )
    )

    company_basics_pool.append(
        _make_mcq(
            prompt="Which business has limited liability for its owners?",
            options=[
                "Sole proprietor",
                "Partnership",
                "Public company",
                "Any business that has a bank account",
            ],
            correct_index=2,
            explanation="Shareholders in a company have limited liability; the company as a legal entity is liable for debts.",
            mode=mode_norm,
        )
    )

    company_basics_pool.append(
        _make_mcq(
            prompt="A public company name ends with:",
            options=["(Pty) Ltd", "Ltd", "Inc.", "NPC"],
            correct_index=1,
            explanation="A public company ends in Limited (Ltd).",
            mode=mode_norm,
        )
    )

    company_basics_pool.append(
        _make_mcq(
            prompt="A private company name ends with:",
            options=["(Pty) Ltd", "Ltd", "SOC Ltd", "CC"],
            correct_index=0,
            explanation="A private company ends in (Pty) Ltd.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="State TWO advantages of a company as a form of ownership.",
            sample_answer="Examples: limited liability; continuity; separate legal existence; easier to raise capital by issuing shares.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="Explain why the Companies Act requires certain public companies to be audited.",
            sample_answer="Because shareholders are not involved in day-to-day management; an independent audit provides assurance that financial statements are fairly presented and reliable.",
            mode=mode_norm,
        )
    )

    stardif_terms = [
        "Social responsibilities",
        "Transparency",
        "Accountability",
        "Responsible management",
        "Discipline",
        "Independence",
        "Fairness",
    ]
    stardif_defs = {
        "Social responsibilities": "Contributing to the community in which the business operates.",
        "Transparency": "Doing things openly with nothing to hide.",
        "Accountability": "Being able to explain and justify your actions.",
        "Responsible management": "Considering impacts such as sustainability and the environment.",
        "Discipline": "Sticking to principles, policies, and ethical standards.",
        "Independence": "Operating without undue influence from outside parties.",
        "Fairness": "Treating stakeholders appropriately and giving them what they deserve.",
    }

    matching_items = r.sample(stardif_terms, k=4)
    distractors = [t for t in stardif_terms if t not in matching_items]
    used_distractors = r.sample(distractors, k=2)

    terms = matching_items + used_distractors
    r.shuffle(terms)

    word_bank: List[Dict[str, str]] = [{"id": f"t{i}", "label": t} for i, t in enumerate(terms)]
    label_to_id = {t["label"]: t["id"] for t in word_bank}

    rows: List[List[str]] = []
    correct_map: Dict[str, Dict[str, Optional[str]]] = {}

    r.shuffle(matching_items)
    for i, term in enumerate(matching_items):
        rows.append([str(i + 1), stardif_defs[term], "", ""])
        correct_map[str(i)] = {"2": str(label_to_id[term]), "3": None}

    matching_pool.append(
        _make_table_wordbank(
            prompt="Match each definition with the correct governance principle (STARDIF).",
            headers=["#", "Definition", "Principle", ""],
            rows=rows,
            word_bank=word_bank,
            correct_map=correct_map,
            guidelines=[
                "Read each definition carefully.",
                "Choose one principle from the word bank for each row.",
            ],
        )
    )

    pools = {
        "companies": company_basics_pool,
        "basics": company_basics_pool,
        "governance": company_governance_pool,
        "stardif": matching_pool,
        "matching": matching_pool,
        "mixed": company_basics_pool + company_governance_pool + matching_pool,
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
