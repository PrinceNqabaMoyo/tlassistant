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
        "explanation": explanation,
        "guidelines": [explanation],
    }
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct12_concepts_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "guidelines": [f"Sample expected answer: {sample_answer}"],
    }
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

    company_governance_pool.append(
        _make_typed(
            prompt="Differentiate between the primary role of an Internal Auditor and an External Auditor in a public company.",
            sample_answer="Internal auditor: Employed by the company to evaluate and improve the effectiveness of risk management, internal controls, and governance processes.\nExternal auditor: Independent registered auditor appointed by shareholders to express an opinion on whether the financial statements are fairly presented in all material respects.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="Explain the difference between an unqualified audit report and a qualified audit report.",
            sample_answer="Unqualified report (clean report): The auditor concludes that the financial statements fairly present the financial position in accordance with IFRS/GAAP without material errors.\nQualified report: The auditor identifies specific material disagreements, misstatements, or limitations in scope, though the rest of the statements are acceptable.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="Explain TWO key functions of the Audit Committee of a listed company in South Africa.",
            sample_answer="1. Recommend the appointment and oversee the independence of external auditors.\n2. Review the integrity of financial statements, internal financial controls, and risk management systems.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="State TWO ethical responsibilities of company directors towards shareholders in terms of King IV.",
            sample_answer="1. Act in good faith and in the best interests of the company (fiduciary duty).\n2. Exercise reasonable care, skill, and diligence, ensuring transparent and accountable reporting.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="State TWO reasons why a company might decide to repurchase (buy back) its own shares on the JSE.",
            sample_answer="1. To increase the Earnings Per Share (EPS) and Net Asset Value (NAV) of the remaining shares.\n2. To return surplus cash to shareholders when the shares are undervalued in the market.",
            mode=mode_norm,
        )
    )

    company_governance_pool.append(
        _make_typed(
            prompt="Explain what is meant by 'separation of ownership and control' in a public company, and why this necessitates financial reporting regulations.",
            sample_answer="Ownership lies with the shareholders who invest capital, but control is delegated to the board of directors and executive management. Because managers may pursue personal interests rather than shareholder wealth, strict accounting standards (IFRS) and statutory audits are required to protect investors.",
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

    rows: List[List[str]] = []
    correct_map_tf: Dict[str, str] = {}
    worked_lines: List[str] = []

    r.shuffle(matching_items)
    for i, term in enumerate(matching_items):
        rows.append([str(i + 1), stardif_defs[term], f"{{r{i}_c2}}"])
        correct_map_tf[f"r{i}_c2"] = term
        worked_lines.append(f"- **{i+1}. {term}**: {stardif_defs[term]}")

    bank_str = " | ".join(f"`{t}`" for t in terms)
    matching_pool.append({
        "id": _make_id("acct12_concepts_stardif"),
        "question_type": "table_fill",
        "subskill": "king_code_stardif_principles",
        "question_text": f"Match each definition with the correct corporate governance principle (STARDIF).\n\n**Principle Bank:** {bank_str}",
        "prompt": f"Match each definition with the correct corporate governance principle (STARDIF).\n\n**Principle Bank:** {bank_str}",
        "headers": ["#", "Governance Definition", "Principle"],
        "rows": rows,
        "correct_map": correct_map_tf,
        "marks": 4,
        "worked_solution": "**King Code STARDIF Principles**\n\n" + "\n".join(worked_lines),
        "canonical_solution": "**King Code STARDIF Principles**\n\n" + "\n".join(worked_lines),
    })

    # Add Audit Opinion & Shareholding Control tables
    audit_table = {
        "id": _make_id("acct12_audit_opinions_table"),
        "question_type": "table_fill",
        "subskill": "audit_opinions_and_reports",
        "question_text": "Classify each external audit finding into the correct **Independent Audit Report Opinion** (`Unqualified`, `Qualified`, or `Disclaimer of Opinion`).",
        "headers": ["Audit Scenario", "Audit Opinion (Unqualified / Qualified / Disclaimer of Opinion)"],
        "rows": [
            ["Financial statements fairly present the company's position in accordance with IFRS and the Companies Act", "{r0_c1}"],
            ["Financial statements are fairly presented, except for an unverified R450,000 inventory item", "{r1_c1}"],
            ["Crucial accounting records were destroyed and auditors could not obtain sufficient audit evidence to form an opinion", "{r2_c1}"],
        ],
        "correct_map": {
            "r0_c1": "Unqualified",
            "r1_c1": "Qualified",
            "r2_c1": "Disclaimer of Opinion",
        },
        "marks": 6,
        "worked_solution": "- Clean report = **Unqualified**\n- Except-for material item = **Qualified**\n- Insufficient evidence to express an opinion = **Disclaimer of Opinion**",
    }

    shareholding_table = {
        "id": _make_id("acct12_shareholding_control_table"),
        "question_type": "table_fill",
        "subskill": "majority_shareholding_and_control",
        "question_text": (
            "A public company has **1,000,000 issued ordinary shares**. Shareholder M. Ndlovu currently holds **460,000 shares (46%)**. "
            "Calculate the minimum additional shares Ndlovu must buy to hold a **51% majority stake** (50% + 10,000 threshold)."
        ),
        "headers": ["Shareholding Control Calculation", "Number of Shares / %"],
        "rows": [
            ["Current shareholding % (460,000 ÷ 1,000,000 × 100)", "{r0_c1}"],
            ["Target shares required for 51% majority control (51% × 1,000,000)", "{r1_c1}"],
            ["Additional shares M. Ndlovu must purchase (Target less Current)", "{r2_c1}"],
        ],
        "correct_map": {"r0_c1": 46, "r1_c1": 510000, "r2_c1": 50000},
        "marks": 5,
        "worked_solution": "Current % = `46%`; Target shares for 51% = `510,000`; Additional shares required = `510,000 - 460,000 = 50,000 shares`.",
    }

    for idx, q in enumerate(company_basics_pool):
        q["subskill"] = "company_legal_concepts" if idx % 2 == 0 else "memorandum_of_incorporation_and_liability"
    for q in company_governance_pool:
        q["subskill"] = "directors_and_auditors_governance"

    by_subskill = {
        "company_legal_concepts": [q for q in company_basics_pool if q.get("question_type") != "typed" and q.get("subskill") == "company_legal_concepts"],
        "memorandum_of_incorporation_and_liability": [q for q in company_basics_pool if q.get("question_type") != "typed" and q.get("subskill") == "memorandum_of_incorporation_and_liability"],
        "king_code_stardif_principles": matching_pool,
        "audit_opinions_and_reports": [audit_table],
        "majority_shareholding_and_control": [shareholding_table],
    }
    if subskill in by_subskill and by_subskill[subskill]:
        return [r.choice(by_subskill[subskill]) for _ in range(n)]
    sub_keys = [k for k, v in by_subskill.items() if v]
    return [r.choice(by_subskill[r.choice(sub_keys)]) for _ in range(n)]


SUBSKILLS = [
    'company_legal_concepts',
    'memorandum_of_incorporation_and_liability',
    'king_code_stardif_principles',
    'audit_opinions_and_reports',
    'majority_shareholding_and_control',
]
