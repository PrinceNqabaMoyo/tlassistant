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
        "id": _make_id("acct12_audits_mcq"),
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
        "id": _make_id("acct12_audits_typed"),
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
        "id": _make_id("acct12_audits_table_wordbank"),
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

    audits_pool: List[Dict[str, Any]] = []
    governance_pool: List[Dict[str, Any]] = []
    shareholding_pool: List[Dict[str, Any]] = []
    matching_pool: List[Dict[str, Any]] = []

    audits_pool.append(
        _make_mcq(
            prompt="Who appoints the independent (external) auditor of a public company?",
            options=[
                "The managing director",
                "The board of directors",
                "The shareholders at the AGM",
                "SARS",
            ],
            correct_index=2,
            explanation="The independent auditor is appointed by the shareholders at the annual general meeting (AGM).",
            mode=mode_norm,
        )
    )

    audits_pool.append(
        _make_mcq(
            prompt="An unqualified audit report indicates:",
            options=[
                "a bad report with irregularities",
                "a good report (financial statements fairly presented)",
                "the auditor refused to give an opinion",
                "the company will be liquidated",
            ],
            correct_index=1,
            explanation="Unqualified = good report (in all material respects fairly presented).",
            mode=mode_norm,
        )
    )

    audits_pool.append(
        _make_typed(
            prompt="Explain why an audit is important for shareholders.",
            sample_answer="Shareholders are not involved in day-to-day management; an independent audit provides assurance that the financial statements are reliable and fairly presented.",
            mode=mode_norm,
        )
    )

    audits_pool.append(
        _make_typed(
            prompt="State TWO consequences an auditor may face if they are negligent.",
            sample_answer="Examples: disciplinary action by professional bodies; deregistration; being sued for misleading reports; loss of contracts/reputation.",
            mode=mode_norm,
        )
    )

    governance_pool.append(
        _make_mcq(
            prompt="Which governance principle relates to doing things openly with nothing to hide?",
            options=["Transparency", "Accountability", "Independence", "Discipline"],
            correct_index=0,
            explanation="Transparency refers to openness and no hidden agenda.",
            mode=mode_norm,
        )
    )

    shareholding_pool.append(
        _make_mcq(
            prompt="A public company raises capital mainly by:",
            options=[
                "increasing drawings",
                "issuing shares to the public",
                "reducing expenses",
                "changing the year-end",
            ],
            correct_index=1,
            explanation="Public companies raise capital by issuing shares to the public.",
            mode=mode_norm,
        )
    )

    shareholding_pool.append(
        _make_typed(
            prompt="Explain what is meant by 'issued shares'.",
            sample_answer="Issued shares are the shares that have been sold/allocated to shareholders (and are held by them) out of the authorised share capital.",
            mode=mode_norm,
        )
    )

    report_types = [
        "Unqualified",
        "Qualified",
        "Disclaimer / Withheld",
    ]
    report_defs = {
        "Unqualified": "Good report; financial statements are fairly presented (in all material respects).",
        "Qualified": "Bad report; irregularities/material misstatements are reported to shareholders.",
        "Disclaimer / Withheld": "Very bad report; auditor cannot form an opinion or recommends further investigation.",
    }

    chosen = r.sample(report_types, k=3)
    distractors = ["Internal", "Prospectus", "Budget"]
    used_distractors = r.sample(distractors, k=2)

    terms = chosen + used_distractors
    r.shuffle(terms)

    word_bank: List[Dict[str, str]] = [{"id": f"t{i}", "label": t} for i, t in enumerate(terms)]
    label_to_id = {t["label"]: t["id"] for t in word_bank}

    rows: List[List[str]] = []
    correct_map: Dict[str, Dict[str, Optional[str]]] = {}

    r.shuffle(chosen)
    for i, t in enumerate(chosen):
        rows.append([str(i + 1), report_defs[t], "", ""])
        correct_map[str(i)] = {"2": str(label_to_id[t]), "3": None}

    matching_pool.append(
        _make_table_wordbank(
            prompt="Match the audit report type with the correct description.",
            headers=["#", "Description", "Report type", ""],
            rows=rows,
            word_bank=word_bank,
            correct_map=correct_map,
            guidelines=[
                "Read each description carefully.",
                "Choose the correct report type from the word bank.",
            ],
        )
    )

    pools = {
        "audits": audits_pool,
        "audit": audits_pool,
        "governance": governance_pool,
        "shareholding": shareholding_pool,
        "matching": matching_pool,
        "mixed": audits_pool + governance_pool + shareholding_pool + matching_pool,
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
