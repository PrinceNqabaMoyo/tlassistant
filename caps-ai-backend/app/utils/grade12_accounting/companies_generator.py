"""Fundile Learning — Grade 12 Accounting: Companies & Corporate Governance Generator.
NSC Accounting Paper 1 (6-12 marks).
100% deterministic zero-LLM generator conforming to the 6-Pillar Contract.

Archetypes from curriculum_docs_auto/Accounting_Gr12/Companies.md:
- Company concepts (directors, auditors, shareholders, MOI, AGM)
- Share capital (authorised vs issued, no par value, issue/repurchase)
- Ledger accounts (Ordinary Share Capital, SARS Income Tax, Shareholders for Dividends, Retained Income)
- Dividends (interim vs final), provisional tax, income tax
- GAAP principles in company context

Supports compound (10 marks) and elementary sub-drills:
- elementary_concepts (3 marks): terminology MCQ and definitions
- elementary_share_capital (4 marks): share issue/repurchase calculations
- elementary_dividends_tax (3 marks): dividend and tax calculations
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ..sa_naming_engine import generate_sa_enterprise


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed(int(seed) if seed is not None else None)
    return r


def _fmt(val: float | int) -> str:
    rounded = int(round(val))
    return f"{rounded:,}".replace(",", " ")


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _pick_company(r: random.Random) -> str:
    ent = generate_sa_enterprise(r, form="Public Company")
    return ent.get("business_name") or "Nkosi Holdings Ltd"


# Company concepts pool (procedurally selected subsets for unlimited variation)
CONCEPTS_POOL = [
    ("Directors", "People appointed by shareholders to manage the day-to-day operations of a company."),
    ("Independent auditor", "An external auditor who expresses an opinion on the financial statements."),
    ("Internal auditor", "An auditor employed by the company to supervise financial statements and internal control."),
    ("Shareholders", "The owners of a company who have invested by buying shares."),
    ("Authorised share capital", "The maximum number of shares a company is legally permitted to sell."),
    ("Issued share capital", "The actual number of shares sold to shareholders."),
    ("Limited liability", "Shareholder liability is restricted to the amount invested; personal assets are protected."),
    ("No par value shares", "Shares that have no fixed monetary value until they are issued."),
    ("Retained income", "Profits after tax not distributed as dividends but reinvested in the company."),
    ("Interim dividends", "Dividends paid to shareholders during the financial year."),
    ("Final dividends", "Dividends recommended to shareholders at the end of the financial year."),
    ("Provisional tax", "Payments made to SARS twice a year based on estimated profits."),
    ("MOI (Memorandum of Incorporation)", "A legal document that sets out the rules for how a company must be run."),
    ("AGM (Annual General Meeting)", "An annual meeting where shareholders discuss the company's performance."),
    ("Unqualified audit report", "When auditors find the financial statements acceptable in all respects."),
    ("Qualified audit report", "When auditors find the statements acceptable except for some aspects."),
    ("Disclaimer", "When auditors are not prepared to express an opinion on the financial statements."),
    ("JSE", "Johannesburg Securities Exchange where public company shares are traded."),
]

GAAP_POOL = [
    ("Business entity rule", "Company finances must be kept separate from shareholders' personal finances."),
    ("Going concern", "Financial statements assume the company will continue to operate."),
    ("Historical cost", "Assets are recorded at their original purchase price."),
    ("Matching", "Income and expenses must be recorded in the same period to which they relate."),
    ("Materiality", "Significant items must be disclosed separately in financial statements."),
    ("Prudence", "Financial figures should be realistic and conservative; avoid overstating assets."),
]


# --------------------------------------------------------------------------- #
# Sub-drill 1: Company Concepts (3 marks)
# --------------------------------------------------------------------------- #
def _build_concepts(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    selected = r.sample(CONCEPTS_POOL, 4)
    term_bank = [t for t, _ in selected]
    r.shuffle(term_bank)
    headers = ["#", "Company Accounting Definition", "Matching Company Term"]
    rows = []
    correct_map = {}
    worked_lines = []
    for i, (term, defn) in enumerate(selected):
        rows.append([str(i + 1), defn, f"{{r{i}_c2}}"])
        correct_map[f"r{i}_c2"] = term
        worked_lines.append(f"- **{i+1}. {term}**: {defn}")

    bank_str = " | ".join(f"`{t}`" for t in term_bank)
    q_text = (
        f"Match each corporate definition for **{company}** to the correct term from the Term Bank.\n\n"
        f"**Term Bank:** {bank_str}"
    )
    worked = "**Company Concepts Matching**\n\n" + "\n".join(worked_lines)
    return {
        "id": _make_id("company_concepts"),
        "question_type": "table_fill",
        "subskill": "elementary_concepts",
        "question_text": q_text,
        "prompt": q_text,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: Share Capital Calculations (4 marks)
# --------------------------------------------------------------------------- #
def _build_share_capital(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    auth_shares = r.choice([500_000, 1_000_000, 2_000_000, 5_000_000])
    issued_begin = int(auth_shares * r.uniform(0.4, 0.7))

    # Issue new shares
    new_shares = r.randint(50, 200) * 1000
    issue_price = r.choice([200, 250, 300, 350, 400, 500])
    issue_proceeds = new_shares * issue_price

    # Repurchase shares
    repurchase_shares = r.randint(10, 50) * 1000
    repurchase_price = r.choice([220, 280, 320, 380, 420])
    repurchase_cost = repurchase_shares * repurchase_price

    issued_end = issued_begin + new_shares - repurchase_shares
    capital_begin = issued_begin * r.choice([180, 200, 250])  # avg issue price historically
    capital_end = capital_begin + issue_proceeds - (repurchase_shares * (capital_begin // issued_begin))

    prompt = (
        f"**{company}** — Share Capital for the year ended 28 February {year}.\n\n"
        f"**Information:**\n"
        f"• Authorised share capital: {_fmt(auth_shares)} ordinary no par value shares.\n"
        f"• Issued shares at beginning of year: {_fmt(issued_begin)} shares.\n"
        f"• During the year: {_fmt(new_shares)} new shares were issued at R{issue_price} each.\n"
        f"• The company repurchased {_fmt(repurchase_shares)} shares at R{repurchase_price} each.\n\n"
        f"**Required:**\n"
        f"1. Calculate the proceeds from the issue of new shares.\n"
        f"2. Calculate the cost of the shares repurchased.\n"
        f"3. Calculate the number of issued shares at the end of the year.\n"
        f"4. State whether the company can still issue more shares and explain why."
    )

    can_issue = issued_end < auth_shares
    remaining = auth_shares - issued_end

    correct = {
        "proceeds": str(issue_proceeds),
        "repurchase_cost": str(repurchase_cost),
        "issued_end": str(issued_end),
        "can_issue": f"{'Yes' if can_issue else 'No'} — {_fmt(remaining)} shares remain of the {_fmt(auth_shares)} authorised.",
    }

    return {
        "id": _make_id("company_shares"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"Proceeds: R{_fmt(issue_proceeds)}",
        "marks": 4,
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "learning_objective_id": "acct12_companies_share_capital",
        "mode": "elementary_share_capital",
        "misconception_tags": ["auth_vs_issued_share_capital", "forgot_repurchase_reduces_issued"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Issue proceeds", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Repurchase cost", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Issued shares end", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Can issue more + reason", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Proceeds = new shares × issue price. Cost = repurchased shares × repurchase price.",
            "tier_2": "Issued shares at end = Beginning + New issues − Repurchased. Compare with authorised.",
            "tier_3": f"Proceeds = {_fmt(new_shares)} × R{issue_price} = R{_fmt(issue_proceeds)}. "
                      f"End shares = {_fmt(issued_begin)} + {_fmt(new_shares)} − {_fmt(repurchase_shares)} = {_fmt(issued_end)}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: Dividends & Tax (3 marks)
# --------------------------------------------------------------------------- #
def _build_dividends_tax(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    issued_shares = r.randint(200, 800) * 1000
    net_profit_after_tax = r.randint(500, 2000) * 10000

    interim_cps = r.choice([20, 25, 30, 40, 50])  # cents per share
    final_cps = r.choice([30, 40, 50, 60, 75])

    interim_total = int(issued_shares * interim_cps / 100)
    final_total = int(issued_shares * final_cps / 100)
    total_dividends = interim_total + final_total

    retained_income_begin = r.randint(200, 600) * 10000
    retained_income_end = retained_income_begin + net_profit_after_tax - total_dividends

    eps = round(net_profit_after_tax / issued_shares * 100, 2)  # in cents
    dps = round(total_dividends / issued_shares * 100, 2)  # in cents

    prompt = (
        f"**{company}** — Dividends and Retained Income for year ended 28 February {year}.\n\n"
        f"**Information:**\n"
        f"• Issued shares: {_fmt(issued_shares)}\n"
        f"• Net Profit after Tax: R{_fmt(net_profit_after_tax)}\n"
        f"• Interim dividend: {interim_cps} cents per share (already paid).\n"
        f"• Final dividend: {final_cps} cents per share (declared, not yet paid).\n"
        f"• Retained Income at beginning of year: R{_fmt(retained_income_begin)}.\n\n"
        f"**Required:**\n"
        f"1. Calculate total interim dividends.\n"
        f"2. Calculate total final dividends.\n"
        f"3. Calculate Retained Income at end of year."
    )

    correct = {
        "interim_total": str(interim_total),
        "final_total": str(final_total),
        "retained_income_end": str(retained_income_end),
    }

    return {
        "id": _make_id("company_div"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"Retained Income at end: R{_fmt(retained_income_end)}",
        "marks": 3,
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "learning_objective_id": "acct12_companies_dividends",
        "mode": "elementary_dividends_tax",
        "misconception_tags": ["confused_eps_and_dps", "forgot_interim_in_retained_income",
                               "cents_to_rands_conversion_error"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Total interim dividends", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Total final dividends", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Retained Income at end", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Total dividends = shares × cents per share ÷ 100 (convert cents to rands).",
            "tier_2": "Retained Income end = Opening RI + Net Profit after Tax − Total Dividends (interim + final).",
            "tier_3": f"Interim = {_fmt(issued_shares)} × {interim_cps}c ÷ 100 = R{_fmt(interim_total)}. "
                      f"RI end = R{_fmt(retained_income_begin)} + R{_fmt(net_profit_after_tax)} − R{_fmt(total_dividends)} = R{_fmt(retained_income_end)}.",
        },
    }


# --------------------------------------------------------------------------- #
# COMPOUND: Full Companies Question (10 marks)
# --------------------------------------------------------------------------- #
def _build_compound(r: random.Random) -> List[Dict[str, Any]]:
    return [
        _build_concepts(r),
        _build_share_capital(r),
        _build_dividends_tax(r),
    ]


# --------------------------------------------------------------------------- #
# PUBLIC API
# --------------------------------------------------------------------------- #
def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: str = "mixed",
    difficulty: str = "medium",
    **kwargs,
) -> List[Dict[str, Any]]:
    from app.utils.grade12_accounting.company_general_ledger_generator import generate_questions as gen_ledger
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []

    all_subskills = [
        "elementary_concepts",
        "elementary_share_capital",
        "elementary_dividends_tax",
        "ordinary_share_capital_ledger",
        "retained_income_ledger",
        "sars_income_tax_ledger",
        "shareholders_for_dividends_ledger",
        "appropriation_account_ledger",
    ]

    ledger_map = {
        "ordinary_share_capital_ledger": "ordinary-share-capital",
        "retained_income_ledger": "retained-option1",
        "sars_income_tax_ledger": "sars",
        "shareholders_for_dividends_ledger": "dividends",
        "appropriation_account_ledger": "appropriation-option1",
    }

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = _rng(sub_seed)
        chosen = subskill if (subskill in all_subskills) else r.choice(all_subskills)
        if chosen == "elementary_concepts":
            q = _build_concepts(sub_r)
        elif chosen == "elementary_share_capital":
            q = _build_share_capital(sub_r)
        elif chosen == "elementary_dividends_tax":
            q = _build_dividends_tax(sub_r)
        else:
            lq = gen_ledger(subskill=ledger_map[chosen], difficulty=difficulty, count=1, seed=sub_seed)
            q = lq[0]
        q["subskill"] = chosen
        questions.append(q)

    return questions
