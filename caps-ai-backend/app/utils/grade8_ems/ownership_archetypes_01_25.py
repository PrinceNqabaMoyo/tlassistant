"""Grade 8 EMS - Forms of ownership: Archetypes 01 to 25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 3/01. Forms of ownership.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, NAMES as PERSON_NAMES


def _fmt_r(amount: int | float) -> str:
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _make_cell(coord: str, value: str, cell_type: str) -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "cell_id": coord,
        "value": value,
        "type": cell_type,
    }


def _build_mcq(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    correct_text: str,
    distractors: List[str],
    explanation: str,
    marks: int = 2,
    hints: Dict[str, str],
    misconception_tags: List[str],
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct_text] + list(distractors)
    rng.shuffle(options)
    c_idx = options.index(correct_text)
    letter = chr(65 + c_idx)
    ans_full = f"{letter}. {correct_text}"
    worked = f"**{ans_full}** [{marks} marks]\n\n{explanation}"
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "Forms of ownership",
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_ownership",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_own_{subskill}",
        "question_type": "mcq",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans_full,
        "expected_answer": ans_full,
        "sample_answer": ans_full,
        "worked_solution": worked,
        "explanation": worked,
        "canonical_solution": worked,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "forms_of_ownership", "south_africa"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _build_short(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_answer: str,
    worked_solution: str,
    marks: int = 3,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
    qtype: str = "short_answer",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "Forms of ownership",
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_ownership",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_own_{subskill}",
        "question_type": qtype,
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "correct_answer": expected_answer,
        "expected_answer": expected_answer,
        "sample_answer": expected_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "forms_of_ownership", "south_africa"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _build_table(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    worked_solution: str,
    sample_answer: str,
    marks: int,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
) -> Dict[str, Any]:
    return {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "Forms of ownership",
        "topic_id": "grade8_ems",
        "subtopic_id": "term3_ownership",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_own_{subskill}",
        "question_type": "table_completion",
        "modality": "ledger",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "correct_answer": sample_answer,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "forms_of_ownership", "south_africa"],
    }


def arch_01_sole_trader_definition_and_single_owner(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    area = rng.choice(AREAS)
    trade = rng.choice(["a neighbourhood plumbing repair service", "a corner bakery and tuckshop", "a mobile hair salon"])
    prompt = (
        f"**{owner}** opens **{trade}** in **{area}** using personal savings, makes all business decisions alone, and keeps 100% of the profit.\n\n"
        "Which form of ownership describes this business?"
    )
    correct = "Sole trader (sole proprietorship), owned and managed by a single individual with no separate legal entity."
    distractors = [
        "Public company (Ltd) trading shares on the Johannesburg Stock Exchange.",
        "Partnership requiring 2 to 20 partners under a written agreement.",
        "Close Corporation (CC) with up to 10 members and limited liability.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_01",
        subskill="01_sole_trader_definition_and_single_owner",
        title="Sole Trader: Single Owner Definition",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Because **{owner}** owns the business alone, controls all decisions, and takes all profit without separate juristic status, it is a **sole trader**."
        ),
        hints={
            "tier_1": "Count how many owners run the business and keep all profits.",
            "tier_2": "'Sole' means one single owner.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_sole_trader_with_private_company"],
    )


def arch_02_sole_trader_advantages_and_disadvantages(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    trade = rng.choice(["custom tailoring studio", "fresh produce stall", "bicycle repair workshop"])
    cap = rng.choice([15000, 25000, 35000])
    prompt = (
        f"**{owner}** starts a **{trade}** as a **sole trader** with **{_fmt_r(cap)}**.\n\n"
        f"State **two advantages** and **two disadvantages** of running **{owner}**'s business as a sole trader."
    )
    expected = (
        "Advantages: 1) Simple and inexpensive to start with minimal legal formalities; 2) Owner keeps all profits and makes fast, independent decisions. "
        "Disadvantages: 1) Unlimited liability puts personal assets at risk; 2) Limited capital/skills and no continuity if the owner falls ill or dies."
    )
    sol = (
        f"**Sole Trader Pros & Cons ({owner}) [4 marks]:**\n\n"
        "**Advantages (any two) [2 marks]:**\n"
        "1. Easy and cheap to establish with few legal formalities **[1]**.\n"
        "2. Owner keeps all net profits and makes quick decisions independently **[1]**.\n\n"
        "**Disadvantages (any two) [2 marks]:**\n"
        "1. **Unlimited liability** — personal house, vehicle, or savings can be claimed to settle business debts **[1]**.\n"
        f"2. **Limited capital ({_fmt_r(cap)}) and no continuity** — business closes if **{owner}** retires or passes away **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_02",
        subskill="02_sole_trader_advantages_and_disadvantages",
        title="Sole Trader: Advantages & Disadvantages",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Think of profit/control on the upside, and personal liability/money limits/continuity on the downside.",
            "tier_2": "Give two distinct advantages and two distinct disadvantages.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Advantage 1: easy/cheap setup or fast decisions", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Advantage 2: owner keeps 100% of profit", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Disadvantage 1: unlimited liability putting personal assets at risk", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Disadvantage 2: limited capital/skills or lack of continuity", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_sole_trader_enjoys_limited_liability"],
    )


def arch_03_sole_trader_unlimited_liability_risk_calculation(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    biz_assets = rng.choice([90000, 110000, 130000])
    biz_debt = biz_assets + rng.choice([65000, 85000, 95000])
    shortfall = biz_debt - biz_assets

    prompt = (
        f"**{owner}** operates a hardware kiosk as a **sole trader**. After tough trading, the business closes owing suppliers **{_fmt_r(biz_debt)}**, "
        f"while selling all business stock and shelves raises only **{_fmt_r(biz_assets)}**.\n\n"
        "(a) Calculate the **remaining debt shortfall** unpaid after selling business assets;\n"
        f"(b) Explain legally how creditors recover this **{_fmt_r(shortfall)}** shortfall from **{owner}**."
    )
    expected = (
        f"(a) Remaining shortfall = {_fmt_r(shortfall)}. "
        f"(b) Because a sole trader has unlimited liability and no separate legal entity, creditors can claim {owner}'s personal assets (car, savings, property) to recover {_fmt_r(shortfall)}."
    )
    sol = (
        f"**Sole Trader Unlimited Liability Case ({owner}) [3 marks]:**\n\n"
        f"**(a) Unpaid Debt Shortfall:** ${_fmt_r(biz_debt)} - {_fmt_r(biz_assets)} = {_fmt_r(shortfall)}$ **[1]**\n\n"
        "**(b) Legal Consequence:** Because a sole trader is **not a separate legal entity** and carries **unlimited liability**, "
        f"creditors may legally attach **{owner}**'s **personal assets** (such as personal bank savings or vehicle) until the **{_fmt_r(shortfall)}** debt is settled **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_03",
        subskill="03_sole_trader_unlimited_liability_risk_calculation",
        title="Unlimited Liability Debt Shortfall Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Subtract business asset proceeds from total business debt.",
            "tier_2": "Link the shortfall to unlimited liability and lack of separate legal entity.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Debt shortfall = {_fmt_r(shortfall)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Explains unlimited liability puts personal assets at legal risk", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_creditors_stop_at_business_assets_for_sole_traders"],
        qtype="calculation",
    )


def arch_04_partnership_owner_range_and_agreement(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(PERSON_NAMES)
    p2 = rng.choice([n for n in PERSON_NAMES if n != p1])
    field = rng.choice(["an accounting and tax practice", "a dental clinic", "an electrical engineering practice"])
    prompt = (
        f"**{p1}** and **{p2}** team up with three colleagues to run **{field}** together, pooling skills and capital.\n\n"
        "Under traditional South African curriculum rules for a **Partnership**, what is the permitted number of partners and what foundational agreement governs them?"
    )
    correct = "Between 2 and 20 partners, governed by a written (or verbal) Partnership Agreement detailing capital, duties, and profit sharing."
    distractors = [
        "Between 1 and 10 members, registered via a CK1 Founding Statement as a legal entity.",
        "Minimum 7 shareholders and 3 directors, issuing a Prospectus on the JSE.",
        "Strictly 1 single owner who has limited liability for all business debts.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_04",
        subskill="04_partnership_owner_range_and_agreement",
        title="Partnership Ownership Range & Partnership Agreement",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **partnership** consists of **2 to 20 partners** sharing skills, capital, risks, and profits under a **Partnership Agreement**."
        ),
        hints={
            "tier_1": "Recall the owner limits (2–20) and governing document for partnerships.",
            "tier_2": "Partnerships have 2–20 partners and rely on a Partnership Agreement (unlike CK1 or MOI).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_partnership_2_to_20_with_cc_1_to_10"],
    )


def arch_05_partnership_profit_sharing_ratio_calculation(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(PERSON_NAMES)
    p2 = rng.choice([n for n in PERSON_NAMES if n != p1])
    cap1 = rng.choice([60000, 80000, 100000])
    cap2 = cap1 * 2 // 2  # let's pick distinct 2:3 or 3:2 ratio
    r1, r2 = rng.choice([(2, 3), (3, 1), (3, 2)])
    unit = rng.choice([40000, 50000])
    c1_amt = r1 * unit
    c2_amt = r2 * unit
    profit = (r1 + r2) * rng.choice([25000, 35000, 45000])
    share1 = profit * r1 // (r1 + r2)
    share2 = profit * r2 // (r1 + r2)

    prompt = (
        f"**{p1}** contributed **{_fmt_r(c1_amt)}** and **{p2}** contributed **{_fmt_r(c2_amt)}** to form a partnership. "
        f"Their Partnership Agreement specifies sharing annual profits in the **exact ratio of their capital contributions ({r1} : {r2})**.\n\n"
        f"If the partnership earns a net profit of **{_fmt_r(profit)}**, calculate the **Rand share of profit** received by **{p1}** and **{p2}**."
    )
    expected = f"{p1}: {_fmt_r(share1)}; {p2}: {_fmt_r(share2)}"
    sol = (
        f"**Partnership Profit Split ({r1}:{r2}) [4 marks]:**\n\n"
        f"- **Total ratio parts:** ${r1} + {r2} = {r1 + r2}$ **[1]**\n"
        f"- **{p1}'s share ($\\frac{{{r1}}}{{{r1 + r2}}}$):** ${_fmt_r(profit)} \\times \\frac{{{r1}}}{{{r1 + r2}}} = {_fmt_r(share1)}$ **[1.5]**\n"
        f"- **{p2}'s share ($\\frac{{{r2}}}{{{r1 + r2}}}$):** ${_fmt_r(profit)} \\times \\frac{{{r2}}}{{{r1 + r2}}} = {_fmt_r(share2)}$ **[1.5]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_05",
        subskill="05_partnership_profit_sharing_ratio_calculation",
        title="Partnership Profit Sharing in Capital Ratio",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Add the ratio parts ({r1} + {r2}) first to find the denominator.",
            "tier_2": f"Multiply {_fmt_r(profit)} by {r1}/{r1 + r2} for {p1} and {r2}/{r1 + r2} for {p2}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total ratio parts = {r1 + r2}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"{p1} = {_fmt_r(share1)}", "marks": 1.5, "editable": True},
            {"id": "mp_3", "desc": f"{p2} = {_fmt_r(share2)}", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["splitting_partnership_profit_50_50_ignoring_agreement_ratio"],
        qtype="calculation",
    )


def arch_06_partnership_joint_liability_and_continuity_exit(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(PERSON_NAMES)
    p2 = rng.choice([n for n in PERSON_NAMES if n != p1])
    area = rng.choice(AREAS)
    prompt = (
        f"**{p1}** and **{p2}** run a physiotherapy partnership in **{area}**. After five years, **{p2}** decides to retire permanently.\n\n"
        "Explain **(a)** what happens legally to the existing **partnership's continuity**, and **(b)** why **disputes or joint liability** can create major risk in partnerships."
    )
    expected = (
        f"(a) No continuity: When {p2} retires (or passes away), the existing partnership dissolves legally; a new partnership agreement would be needed to continue. "
        "(b) Partners share unlimited, joint-and-several liability for debts/decisions made by co-partners, putting personal assets at risk if disagreements or losses occur."
    )
    sol = (
        f"**Partnership Continuity & Joint Risk ({p1} & {p2}) [4 marks]:**\n\n"
        f"**(a) Lack of Continuity:** A partnership is **not a separate legal entity**, so when **{p2}** retires or leaves, the original partnership legally **dissolves** (no automatic continuity) **[2]**.\n\n"
        "**(b) Joint Unlimited Liability & Conflict Risk:** Partners can be held **personally liable** for debts incurred by a co-partner, and disagreements over strategy or work effort can stall decisions **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_06",
        subskill="06_partnership_joint_liability_and_continuity_exit",
        title="Partnership Continuity & Joint Liability Risks",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Does a partnership survive unchanged when a partner leaves or dies?",
            "tier_2": "Cover (a) automatic dissolution / no continuity, and (b) unlimited liability for partner debts + conflict risk.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Existing partnership dissolves upon exit/retirement (no continuity)", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Joint unlimited liability putting personal assets at risk / conflict risk", "marks": 2, "editable": True},
        ],
        misconception_tags=["believing_partnerships_have_automatic_continuity"],
    )


def arch_07_close_corporation_cc_members_and_ck1_statement(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    members = rng.choice([3, 5, 7, 9])
    name = rng.choice(["Imbali Catering", "Kasi Printers", "Vula Logistics", "Naledi Packaging"])
    prompt = (
        f"A small enterprise in **{area}** has **{members} natural-person members** operating under the registered name **{name} CC**.\n\n"
        "Which feature accurately describes this **Close Corporation (CC)**?"
    )
    correct = "Has 1 to 10 members, uses a Founding Statement (CK1), holds separate legal personality with limited liability, and carries 'CC' after its name."
    distractors = [
        "Must have at least 7 shareholders and 3 directors and list shares on the JSE.",
        "Has unlimited personal liability and must dissolve whenever one member withdraws.",
        "Requires a public Prospectus before admitting its 2nd member.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_07",
        subskill="07_close_corporation_cc_members_and_ck1_statement",
        title="Close Corporation (CC): Members, CK1 & Legal Status",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**{name} CC** has **1–10 members**, was founded with a **CK1 Founding Statement**, enjoys **limited liability**, and owns separate **legal personality**."
        ),
        hints={
            "tier_1": "Recall member count (1–10), CK1 form, and limited liability for CCs.",
            "tier_2": "CCs are separate legal entities with 1–10 members (no JSE shares).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_close_corporation_with_public_company"],
    )


def arch_08_close_corporation_legal_entity_and_continuity(rng: random.Random) -> Dict[str, Any]:
    m1 = rng.choice(PERSON_NAMES)
    m2 = rng.choice([n for n in PERSON_NAMES if n != m1])
    cc_name = rng.choice(["Mfula Electrical CC", "Siyanda Bakers CC", "Bafana Spares CC"])
    prompt = (
        f"**{m1}** and **{m2}** are members of **{cc_name}**. Later, **{m1}** sells their member's interest to a new qualifying member.\n\n"
        f"Explain **(a)** what happens to the **continuity of existence** of **{cc_name}**, and **(b)** how **limited liability** protects **{m2}**'s personal savings."
    )
    expected = (
        f"(a) {cc_name} has continuous existence as a separate legal entity, so it keeps operating without dissolving when {m1} leaves. "
        f"(b) Limited liability means {m2} risks only the capital contributed to {cc_name}, shielding personal savings from business debts."
    )
    sol = (
        f"**Continuity & Limited Liability in a CC ({cc_name}) [3 marks]:**\n\n"
        f"**(a) Continuity:** Because **{cc_name}** is a **separate legal entity**, its existence continues seamlessly when a member changes **[1.5]**.\n\n"
        f"**(b) Limited Liability:** **{m2}** is liable only up to their investment in the CC; creditors cannot seize **{m2}**'s personal home or savings for CC debts **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_08",
        subskill="08_close_corporation_legal_entity_and_continuity",
        title="Close Corporation Continuity & Limited Liability",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Compare how a CC differs from a partnership when one owner leaves or when debts exceed assets.",
            "tier_2": "Address continuity (continues) + limited liability (personal assets protected).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "CC continues operating when membership changes (continuity of existence)", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": "Member's personal savings/home protected by limited liability", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["thinking_cc_members_face_unlimited_liability"],
    )


def arch_09_private_company_pty_ltd_name_and_share_restrictions(rng: random.Random) -> Dict[str, Any]:
    firm = rng.choice(["Karabo Tech Solutions (Pty) Ltd", "Thabo Logistics (Pty) Ltd", "Zanele Foods (Pty) Ltd"])
    prompt = (
        f"A fast-growing South African enterprise is registered as **{firm}**.\n\n"
        "What does the **`(Pty) Ltd`** suffix legally signify about its ownership and share trading?"
    )
    correct = "It is a Private Company (Proprietary Limited) with separate legal personality and limited liability whose shares CANNOT be traded freely to the general public."
    distractors = [
        "It is a Public Company required to advertise shares to all citizens on the JSE.",
        "It is an informal partnership with unlimited personal liability for up to 20 partners.",
        "It is a municipal government department exempt from registering with CIPC.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_09",
        subskill="09_private_company_pty_ltd_name_and_share_restrictions",
        title="Private Company (Pty) Ltd: Meaning & Share Rules",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**`(Pty) Ltd`** identifies a **Private Company (Proprietary Limited)**: owners (1–50 per Grade 8 syllabus) hold **limited liability**, "
            "and share transfers are restricted rather than offered to the public."
        ),
        hints={
            "tier_1": "'Proprietary' means privately held; 'Limited' refers to liability.",
            "tier_2": "(Pty) Ltd = Private Company whose shares cannot trade publicly on a stock exchange.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_pty_ltd_with_public_jse_company"],
    )


def arch_10_private_company_moi_and_cipc_registration(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    co_name = rng.choice(["Naledi Solar (Pty) Ltd", "Lunga Agri (Pty) Ltd", "Lerato Print (Pty) Ltd"])
    prompt = (
        f"**{founder}** registers **{co_name}** with the Companies and Intellectual Property Commission (**CIPC**).\n\n"
        "Name the **founding governing document** submitted to register a company, and state **two compliance/governance obligations** a company faces compared to a sole trader."
    )
    expected = (
        "Founding document: Memorandum of Incorporation (MOI). "
        "Obligations: 1) More complex & costly registration with CIPC; 2) Must maintain formal financial records/audits and hold shareholder/board meetings."
    )
    sol = (
        f"**Company Registration & Governance ({co_name}) [3 marks]:**\n\n"
        "1. **Governing Document:** **Memorandum of Incorporation (MOI)** registered with CIPC **[1]**.\n"
        "2. **Two Additional Obligations:**\n"
        "   - Higher setup cost and legal compliance steps **[1]**.\n"
        "   - Required to prepare **regular financial/audited statements** and hold **annual shareholder meetings** **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_10",
        subskill="10_private_company_moi_and_cipc_registration",
        title="Company Registration: MOI & Governance Duties",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Which document replaces CK1 for companies? What extra paperwork/meetings must companies maintain?",
            "tier_2": "State Memorandum of Incorporation (MOI) plus formal financial reporting/audits and shareholder meetings.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Memorandum of Incorporation (MOI)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Higher registration cost/compliance with CIPC", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Regular audited/financial statements and annual shareholder meetings", "marks": 1, "editable": True},
        ],
        misconception_tags=["confusing_moi_with_ck1_or_partnership_agreement"],
    )


def arch_11_public_company_ltd_minimums_jse_and_prospectus(rng: random.Random) -> Dict[str, Any]:
    co = rng.choice(["Mzansi Energy Ltd", "Southern Rail Ltd", "Cape Harvest Ltd", "Vula Telecoms Ltd"])
    prompt = (
        f"**{co}** plans to list on the **Johannesburg Stock Exchange (JSE)** so millions of ordinary investors and pension funds can buy shares.\n\n"
        "Which set of features applies strictly to a **Public Company (`Ltd`)** under Grade 8 EMS rules?"
    )
    correct = "Ends in 'Ltd', has at least 7 shareholders (up to issued share limit) and 3 directors, issues a Prospectus, and trades shares publicly."
    distractors = [
        "Ends in '(Pty) Ltd', bans public share sales, and allows at most 1 owner.",
        "Ends in 'CC', has 1–10 members, and uses a CK1 Founding Statement.",
        "Operates with unlimited liability so every JSE shareholder loses their house if profit drops.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_11",
        subskill="11_public_company_ltd_minimums_jse_and_prospectus",
        title="Public Company (Ltd): Shareholders, Directors & JSE",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **Public Company** (`Ltd` — **{co}**) raises huge capital by issuing a **prospectus** and selling shares publicly (e.g. on the **JSE**), "
            "requiring **at least 7 shareholders** and **at least 3 directors** per the Grade 8 curriculum specification."
        ),
        hints={
            "tier_1": "Check the suffix ('Ltd' vs '(Pty) Ltd'), minimum shareholders/directors, and public stock exchange listing.",
            "tier_2": "Public companies end in 'Ltd', issue a Prospectus, and sell shares to the public.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_public_company_is_a_government_department"],
    )


def arch_12_prospectus_purpose_for_public_share_offer(rng: random.Random) -> Dict[str, Any]:
    co = rng.choice(["Ubuntu Gold Ltd", "Horizon Solar Ltd", "Karoo Agri Ltd"])
    target_m = rng.choice([250, 400, 600])
    prompt = (
        f"Before **{co}** invites members of the South African public to subscribe for **R{target_m} million** in new shares, it publishes a **Prospectus**.\n\n"
        f"Define a **Prospectus** and give **two types of information** prospective investors expect inside it."
    )
    expected = (
        f"A prospectus is an official formal document issued by a public company ({co}) inviting the public to buy its shares. "
        "It sets out the share offer price/quantity, company financial history/risks, directors' details, and how the capital will be used."
    )
    sol = (
        f"**Purpose of a Public Company Prospectus ({co}) [3 marks]:**\n\n"
        f"1. **Definition:** A legally regulated invitation document inviting members of the public to buy shares in a **public company** to raise capital (**R{target_m} million**) **[1]**.\n"
        "2. **Investor Information (any two):** Details on **share price and terms**, **financial performance/risks**, **names of directors**, and **how the raised funds will be invested** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_12",
        subskill="12_prospectus_purpose_for_public_share_offer",
        title="The Prospectus in Public Share Offers",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think about what ordinary investors need to read BEFORE handing over savings to buy JSE shares.",
            "tier_2": "Define it as an official public share invitation disclosing finances, share price, directors, and plans.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Official public invitation to buy shares in a public company", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Two valid contents (financial records/risks, share price, directors, use of capital)", "marks": 2, "editable": True},
        ],
        misconception_tags=["thinking_sole_traders_or_ccs_issue_a_prospectus"],
    )


def arch_13_dividends_and_shareholder_return_calculation(rng: random.Random) -> Dict[str, Any]:
    investor = rng.choice(PERSON_NAMES)
    co = rng.choice(["Mfula Mining Ltd", "Naledi Retail Ltd", "Vula Power Ltd"])
    total_shares = rng.choice([100000, 200000, 250000])
    total_dividend = total_shares * rng.choice([3, 4, 5])
    div_per_share = total_dividend // total_shares
    held_shares = rng.choice([400, 600, 800, 1200])
    investor_payout = held_shares * div_per_share

    prompt = (
        f"**{co}** has **{total_shares:,}** issued shares and its board declares a total annual **dividend payout** of **{_fmt_r(total_dividend)}** out of after-tax profits. "
        f"**{investor}** owns **{held_shares:,} shares** in **{co}**.\n\n"
        "(a) Define a **dividend**;\n"
        "(b) Calculate the **dividend per share**;\n"
        f"(c) Calculate the **total dividend income** paid to **{investor}**."
    )
    expected = (
        f"(a) A dividend is the portion of a company's after-tax profit distributed to shareholders. "
        f"(b) Dividend per share = {_fmt_r(div_per_share)}; (c) {investor}'s payout = {_fmt_r(investor_payout)}"
    )
    sol = (
        f"**Shareholder Dividend Calculation ({co}) [4 marks]:**\n\n"
        "**(a) Definition:** A **dividend** is the share of a company's distributed profit paid out to shareholders **[1]**.\n\n"
        "**(b) Dividend per Share:**\n"
        f"$${_fmt_r(total_dividend)} \\div {total_shares:,} = {_fmt_r(div_per_share)}\\text{{ per share}}$$ **[1.5]**\n\n"
        f"**(c) {investor}'s Payout ({held_shares:,} shares):**\n"
        f"$${held_shares:,} \\times {_fmt_r(div_per_share)} = {_fmt_r(investor_payout)}$$ **[1.5]**"
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_13",
        subskill="13_dividends_and_shareholder_return_calculation",
        title="Dividends & Shareholder Payout Calculation",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Divide total dividend payout by total issued shares first.",
            "tier_2": f"Multiply the dividend per share by {investor}'s {held_shares} shares.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Defines dividend as share of company profits paid to shareholders", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Dividend per share = {_fmt_r(div_per_share)}", "marks": 1.5, "editable": True},
            {"id": "mp_3", "desc": f"{investor}'s dividend = {_fmt_r(investor_payout)}", "marks": 1.5, "editable": True},
        ],
        misconception_tags=["confusing_dividends_with_employee_salaries"],
        qtype="calculation",
    )


def arch_14_legal_entity_concept_suing_and_property_ownership(rng: random.Random) -> Dict[str, Any]:
    firm = rng.choice(["Bafana Transport (Pty) Ltd", "Imbali Foods CC", "Thabo Steel Ltd"])
    prompt = (
        f"**{firm}** buys a delivery warehouse registered in the company's own name and signs a bank loan contract independently of its owners.\n\n"
        "Which legal concept explains why **{0}** itself owns property, signs contracts, and can sue or be sued in its own name?".format(firm)
    )
    correct = "Separate legal entity (juristic persona) — the business exists in law apart from its individual members or shareholders."
    distractors = [
        "Unlimited liability — meaning owners and the company are legally one single person.",
        "Sole proprietorship privilege — exclusive to businesses with only one owner.",
        "Tax evasion status — allowing the firm never to submit financial records.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_14",
        subskill="14_legal_entity_concept_suing_and_property_ownership",
        title="Separate Legal Entity (Juristic Personality)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A **legal entity** (**{firm}**) possesses legal rights and obligations separate from its owners, enabling limited liability and continuity."
        ),
        hints={
            "tier_1": "What term means the business is treated by courts as its own legal 'person'?",
            "tier_2": "Separate legal entity (applies to CCs, Private Companies, and Public Companies).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_legal_entity_with_physical_office_building"],
    )


def arch_15_limited_vs_unlimited_liability_case_comparison(rng: random.Random) -> Dict[str, Any]:
    owner_a = rng.choice(PERSON_NAMES)
    owner_b = rng.choice([n for n in PERSON_NAMES if n != owner_a])
    shortfall = rng.choice([180000, 240000, 350000])
    prompt = (
        f"**{owner_a}** owns a sole trader grocery store that fails with **{_fmt_r(shortfall)}** in unpaid debts. "
        f"**{owner_b}** owns shares in a failed private company `(Pty) Ltd` that also has **{_fmt_r(shortfall)}** in unpaid debts.\n\n"
        f"Compare the **personal asset risk** faced by **{owner_a}** versus **{owner_b}** by explaining **unlimited liability** and **limited liability**."
    )
    expected = (
        f"{owner_a} (sole trader) has unlimited liability: creditors can seize personal home, car, or savings to cover {_fmt_r(shortfall)}. "
        f"{owner_b} ((Pty) Ltd shareholder) has limited liability: risk is capped at money invested in shares; personal assets stay protected."
    )
    sol = (
        f"**Limited vs Unlimited Liability Comparison ({_fmt_r(shortfall)} Debt) [4 marks]:**\n\n"
        f"1. **{owner_a} (Unlimited Liability — Sole Trader):** No separation between owner and business; personal home, car, and savings can be attached for the **{_fmt_r(shortfall)}** debt **[2]**.\n"
        f"2. **{owner_b} (Limited Liability — Private Co):** Company is a separate legal entity; **{owner_b}** loses only the capital invested in shares, while personal property stays safe **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_15",
        subskill="15_limited_vs_unlimited_liability_case_comparison",
        title="Comparing Limited vs Unlimited Liability",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare Sole Trader (no legal shield) against (Pty) Ltd (separate legal shield).",
            "tier_2": "Show personal asset exposure for unlimited liability vs investment-only risk for limited liability.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Explains unlimited liability puts {owner_a}'s personal assets at risk", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Explains limited liability caps {owner_b}'s loss to invested capital", "marks": 2, "editable": True},
        ],
        misconception_tags=["reversing_limited_and_unlimited_liability"],
    )


def arch_16_continuity_of_existence_across_ownership_forms(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    co = rng.choice(["Vula Motors Ltd", "Naledi Builders (Pty) Ltd", "Siyanda Foods CC"])
    prompt = (
        f"Suppose **{founder}**, a founder and major investor in **{co}**, unexpectedly passes away.\n\n"
        "Why does **{0}** continue trading uninterrupted the next morning, whereas a **sole trader or partnership** does not?".format(co)
    )
    correct = "Because CCs and Companies have continuity of existence as separate legal entities; ownership transfers by shares/member interest without dissolving the firm."
    distractors = [
        "Because courts automatically transfer all private sole-trader shops directly to the municipality.",
        "Because employees in a company receive no wages after a founder retires.",
        "Because companies have unlimited liability while sole traders have limited liability.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_16",
        subskill="16_continuity_of_existence_across_ownership_forms",
        title="Continuity of Existence Across Ownership Forms",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Continuity of existence** means **{co}** survives the death or exit of individual founders, unlike sole traders and partnerships."
        ),
        hints={
            "tier_1": "Which ownership forms survive unchanged when an owner passes away or sells their stake?",
            "tier_2": "Separate legal entity confers continuity (CC, Private Co, Public Co).",
            "tier_3": correct,
        },
        misconception_tags=["thinking_a_company_closes_when_a_shareholder_dies"],
    )


def arch_17_naming_suffixes_identification_table(rng: random.Random) -> Dict[str, Any]:
    owner = rng.choice(PERSON_NAMES)
    pool = [
        (f"{owner}'s Fresh Bakery (owned by 1 person)", "Sole trader"),
        ("Mfula & Nkomo Attorneys (3 co-owners)", "Partnership"),
        ("Ubuntu Printers CC", "Close Corporation"),
        ("Thabo Solar (Pty) Ltd", "Private Company"),
        ("Sasol Ltd", "Public Company"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["South African Enterprise Name", "Exact Form of Ownership"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| South African Enterprise Name | Exact Form of Ownership |", "| :--- | :--- |"]
    for idx, (ent, form) in enumerate(chosen):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", ent, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = form
        cell_hints[c1] = "Write: Sole trader, Partnership, Close Corporation, Private Company, or Public Company."
        memo_lines.append(f"| {ent} | {form} |")

    worked = "**Completed Business Suffix Classification [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{e} -> {f}" for e, f in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_17",
        subskill="17_naming_suffixes_identification_table",
        title="Identifying Ownership Forms from Naming Conventions",
        prompt=(
            "Classify each South African enterprise using its legal naming suffix or structure: "
            "**Sole trader**, **Partnership**, **Close Corporation**, **Private Company**, or **Public Company**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Look closely at CC, (Pty) Ltd, Ltd, single owner, and co-owners.",
            "tier_2": "(Pty) Ltd = Private Company; Ltd = Public Company; CC = Close Corporation.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]} -> {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_ltd_and_pty_ltd_suffixes"],
    )


def arch_18_owner_count_and_leadership_structure_table(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Sole trader", "1", "No"),
        ("Partnership", "2 - 20", "No"),
        ("Close Corporation (CC)", "1 - 10", "Yes"),
        ("Private Company (Pty) Ltd", "1 - 50", "Yes"),
        ("Public Company (Ltd)", "Minimum 7", "Yes"),
    ]
    chosen = rng.sample(pool, 3)
    headers = ["Form of Ownership", "Permitted Owner / Shareholder Range", "Continuity of Existence (Yes / No)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Form of Ownership | Permitted Owner / Shareholder Range | Continuity |", "| :--- | :--- | :--- |"]
    for idx, (form, cnt, cont) in enumerate(chosen):
        c1 = f"r{idx}c1"
        c2 = f"r{idx}c2"
        rows.append([
            _make_cell(f"r{idx}c0", form, "given"),
            _make_cell(c1, "", "required"),
            _make_cell(c2, "", "required"),
        ])
        correct_map[c1] = cnt
        correct_map[c2] = cont
        cell_hints[c1] = "E.g., 1, 2 - 20, 1 - 10, 1 - 50, or Minimum 7."
        cell_hints[c2] = "Write Yes or No."
        memo_lines.append(f"| {form} | {cnt} | {cont} |")

    worked = "**Completed Ownership Limits & Continuity Schedule [6 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{f}: Owners={c}, Continuity={k}" for f, c, k in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_18",
        subskill="18_owner_count_and_leadership_structure_table",
        title="Owner Counts & Continuity Matrix",
        prompt="Complete the Grade 8 comparison matrix by entering the **permitted owner/shareholder count** and whether the business has **continuity of existence** (**Yes** or **No**).",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Counts: Sole=1, Partnership=2-20, CC=1-10, Private Co=1-50, Public Co=Minimum 7.",
            "tier_2": "Continuity is Yes only for separate legal entities (CC, Private Co, Public Co).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]}: {chosen[i][1]} & Continuity {chosen[i][2]}", "marks": 2, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["confusing_owner_counts_across_cc_and_companies"],
    )


def arch_19_liability_and_legal_persona_comparison_table(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Sole trader", "No", "Unlimited"),
        ("Partnership", "No", "Unlimited"),
        ("Close Corporation (CC)", "Yes", "Limited"),
        ("Private Company (Pty) Ltd", "Yes", "Limited"),
        ("Public Company (Ltd)", "Yes", "Limited"),
    ]
    chosen = rng.sample(pool, 3)
    headers = ["Form of Ownership", "Separate Legal Entity? (Yes / No)", "Liability of Owners (Limited / Unlimited)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Form of Ownership | Separate Legal Entity? | Liability |", "| :--- | :--- | :--- |"]
    for idx, (form, ent, liab) in enumerate(chosen):
        c1 = f"r{idx}c1"
        c2 = f"r{idx}c2"
        rows.append([
            _make_cell(f"r{idx}c0", form, "given"),
            _make_cell(c1, "", "required"),
            _make_cell(c2, "", "required"),
        ])
        correct_map[c1] = ent
        correct_map[c2] = liab
        cell_hints[c1] = "Enter Yes or No."
        cell_hints[c2] = "Enter Limited or Unlimited."
        memo_lines.append(f"| {form} | {ent} | {liab} |")

    worked = "**Completed Legal Entity & Liability Schedule [6 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{f}: LegalEntity={e}, Liability={l}" for f, e, l in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_own_19",
        subskill="19_liability_and_legal_persona_comparison_table",
        title="Legal Entity & Liability Comparison Audit",
        prompt="Complete each row by stating whether the ownership form is a **Separate Legal Entity** (**Yes** or **No**) and whether owners carry **Limited** or **Unlimited** liability.",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Separate legal entity (Yes) always pairs with Limited liability!",
            "tier_2": "Sole trader and Partnership = No / Unlimited; CC and Companies = Yes / Limited.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{chosen[i][0]}: Entity {chosen[i][1]}, Liability {chosen[i][2]}", "marks": 2, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["mismatching_separate_legal_entity_with_unlimited_liability"],
    )


def arch_20_sole_trader_vs_partnership_capital_and_skills_tradeoff(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice(PERSON_NAMES)
    partner = rng.choice([n for n in PERSON_NAMES if n != founder])
    cap_alone = rng.choice([40000, 60000])
    cap_combined = cap_alone * 2 + rng.choice([30000, 50000])
    prompt = (
        f"**{founder}** runs a busy bakery as a **sole trader** with **{_fmt_r(cap_alone)}** capital, handling baking, deliveries, and bookkeeping alone. "
        f"**{partner}** offers to join as a partner, bringing extra baking skills and boosting combined capital to **{_fmt_r(cap_combined)}**.\n\n"
        f"Give **two benefits** for **{founder}** of converting into a **partnership** with **{partner}**, and **one trade-off** **{founder}** must accept."
    )
    expected = (
        f"Benefits: 1) Greater capital ({_fmt_r(cap_combined)}) to expand ovens/stock; 2) Shared workload and complementary management skills. "
        f"Trade-off: {founder} must share profits and decision-making control with {partner} (and remains exposed to joint unlimited liability)."
    )
    sol = (
        f"**Converting Sole Trader to Partnership ({founder} & {partner}) [3 marks]:**\n\n"
        "1. **Two Benefits [2 marks]:**\n"
        f"   - Larger pooled capital (**{_fmt_r(cap_combined)}** vs **{_fmt_r(cap_alone)}**) for business expansion **[1]**.\n"
        f"   - Combined skills and shared workload reduce burnout **[1]**.\n"
        "2. **One Trade-Off [1 mark]:**\n"
        f"   - Profits and decision authority must now be **shared** with **{partner}** (and unlimited joint liability continues) **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_20",
        subskill="20_sole_trader_vs_partnership_capital_and_skills_tradeoff",
        title="Sole Trader vs Partnership: Growth Trade-Offs",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "What does a second owner add (capital & skills), and what does the original owner give up (100% profit/control)?",
            "tier_2": "State two partnership gains and one loss of sole control/profit share.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Larger pooled capital", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Shared workload and complementary skills", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Must share profits / control / joint debt liability", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_partnership_eliminates_unlimited_liability"],
    )


def arch_21_private_co_vs_public_co_capital_raising_and_control(rng: random.Random) -> Dict[str, Any]:
    firm = rng.choice(["Vula Engineering", "Mfula Foods", "Karoo Renewables"])
    prompt = (
        f"The founders of **{firm} (Pty) Ltd** want to raise **R500 million** from ordinary investors across South Africa by listing on the JSE.\n\n"
        f"Why must **{firm} (Pty) Ltd** convert into a **Public Company (`Ltd`)** before listing, and what control risk do the original founders face?"
    )
    correct = "A (Pty) Ltd cannot invite the public to buy shares; converting to Ltd lets it issue a Prospectus on the JSE to raise vast capital, though outside shareholders could outvote founders."
    distractors = [
        "A (Pty) Ltd already sells shares publicly, so converting to Ltd merely lowers corporate tax to 0%.",
        "Converting to Ltd removes separate legal personality and restores unlimited liability.",
        "Only partnerships with fewer than 20 owners are allowed to list on the JSE.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_21",
        subskill="21_private_co_vs_public_co_capital_raising_and_control",
        title="Private Co (Pty) Ltd vs Public Co (Ltd) Listing",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Converting **{firm} (Pty) Ltd** into a **Public Company (`Ltd`)** unlocks vast public equity via a **Prospectus** and JSE listing, "
            "at the cost of public financial disclosure and diluted founder voting control."
        ),
        hints={
            "tier_1": "Remember: (Pty) Ltd shares are privately restricted, whereas Ltd shares sell publicly.",
            "tier_2": "Converting to Ltd grants huge capital access while diluting private founder control.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_pty_ltd_companies_can_list_shares_on_jse"],
    )


def arch_22_partnership_capital_contribution_and_debt_shortfall(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice(PERSON_NAMES)
    p2 = rng.choice([n for n in PERSON_NAMES if n != p1])
    total_debt = rng.choice([300000, 420000, 500000])
    assets_sold = rng.choice([180000, 220000, 260000])
    shortfall = total_debt - assets_sold
    each_equal = shortfall // 2

    prompt = (
        f"**{p1}** and **{p2}** dissolve their equal 50:50 partnership owing creditors **{_fmt_r(total_debt)}**. "
        f"Selling all partnership machinery raises **{_fmt_r(assets_sold)}**.\n\n"
        "(a) Calculate the **unpaid debt shortfall**;\n"
        f"(b) If they contribute equally from personal savings to settle creditors, how much must **{p1}** and **{p2}** each pay personally, and why?"
    )
    expected = (
        f"(a) Shortfall = {_fmt_r(shortfall)}. "
        f"(b) Each pays {_fmt_r(each_equal)} personally because partners carry unlimited liability for partnership debts."
    )
    sol = (
        f"**Partnership Debt Settlement ({p1} & {p2}) [4 marks]:**\n\n"
        f"**(a) Unpaid Shortfall:** ${_fmt_r(total_debt)} - {_fmt_r(assets_sold)} = {_fmt_r(shortfall)}$ **[1.5]**\n\n"
        f"**(b) Equal Personal Contribution & Legal Reason:**\n"
        f"- Each partner pays ${_fmt_r(shortfall)} \\div 2 = {_fmt_r(each_equal)}$ **[1.5]**.\n"
        "- Reason: Partnerships lack limited liability, leaving partners personally responsible for remaining debts **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_22",
        subskill="22_partnership_capital_contribution_and_debt_shortfall",
        title="Partnership Liquidation Debt Shortfall",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Find debt minus asset proceeds first, then divide by 2.",
            "tier_2": "State why personal money must be used (unlimited liability).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Shortfall = {_fmt_r(shortfall)}", "marks": 1.5, "editable": True},
            {"id": "mp_2", "desc": f"Each pays {_fmt_r(each_equal)}", "marks": 1.5, "editable": True},
            {"id": "mp_3", "desc": "Explains unlimited liability", "marks": 1, "editable": True},
        ],
        misconception_tags=["thinking_partners_walk_away_from_shortfall_without_paying"],
        qtype="calculation",
    )


def arch_23_formation_documents_matching_table(rng: random.Random) -> Dict[str, Any]:
    docs = [
        ("Partnership Agreement", "Partnership"),
        ("Founding Statement (CK1)", "Close Corporation"),
        ("Memorandum of Incorporation (MOI)", "Private and Public Companies"),
        ("Prospectus", "Public Company"),
    ]
    rng.shuffle(docs)
    headers = ["Key Formation / Governing Document", "Form of Ownership Using This Document"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Key Formation / Governing Document | Form of Ownership |", "| :--- | :--- |"]
    for idx, (doc, own) in enumerate(docs):
        c1 = f"r{idx}c1"
        rows.append([_make_cell(f"r{idx}c0", doc, "given"), _make_cell(c1, "", "required")])
        correct_map[c1] = own
        cell_hints[c1] = "Choose: Partnership, Close Corporation, Private and Public Companies, or Public Company."
        memo_lines.append(f"| {doc} | {own} |")

    worked = "**Completed Formation Documents Schedule [4 marks]:**\n\n" + "\n".join(memo_lines)
    sample = "; ".join(f"{d} -> {o}" for d, o in docs)
    return _build_table(
        rng,
        qid_prefix="g8_own_23",
        subskill="23_formation_documents_matching_table",
        title="Legal Formation & Governance Documents Schedule",
        prompt=(
            "Match each South African business document to its corresponding form of ownership: "
            "**Partnership**, **Close Corporation**, **Private and Public Companies**, or **Public Company**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "CK1 belongs to CCs; MOI governs companies; only a Public Company invites public investors via a Prospectus.",
            "tier_2": "Match each exact label provided in the prompt.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{docs[i][0]} -> {docs[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["mixing_up_ck1_and_moi_documents"],
    )


def arch_24_ownership_spectrum_svg_diagram_comparison(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    founder = rng.choice(PERSON_NAMES)
    pub_co = rng.choice(["Vula Mining Ltd", "Mzansi Foods Ltd", "Cape Energy Ltd"])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 205" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="205" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Ownership Capital &amp; Liability Ladder ({area})</text>'
        '<rect x="20" y="45" width="280" height="110" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        '<text x="160" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">UNLIMITED LIABILITY (No Legal Entity)</text>'
        f'<text x="160" y="96" text-anchor="middle" font-size="11" fill="#7f1d1d">1. Sole Trader ({founder}\'s Kiosk: 1)</text>'
        '<text x="160" y="122" text-anchor="middle" font-size="11" fill="#7f1d1d">2. Partnership (2 - 20 Partners)</text>'
        '<rect x="330" y="45" width="330" height="110" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<text x="495" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#14532d">LIMITED LIABILITY (Separate Legal Entity)</text>'
        '<text x="495" y="94" text-anchor="middle" font-size="11" fill="#166534">3. Close Corporation (CC: 1 - 10 Members)</text>'
        '<text x="495" y="116" text-anchor="middle" font-size="11" fill="#166534">4. Private Co (Pty) Ltd (Restricted Shares)</text>'
        f'<text x="495" y="138" text-anchor="middle" font-size="11" fill="#166534">5. Public Co ({pub_co}: Min 7, JSE)</text>'
        '<text x="340" y="182" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">Capital-Raising Power Increases Left to Right --&gt;</text>'
        '</svg>'
    )
    prompt = (
        f"Study the ownership ladder diagram contrasting **{founder}'s Kiosk** (left box) and **{pub_co}** (right box) in **{area}**.\n\n"
        f"(a) Explain **two key legal differences** between the forms in the left box and the forms in the right box;\n"
        f"(b) Why can **{pub_co}** raise much larger capital than **{founder}'s Kiosk**?"
    )
    expected = (
        "(a) Left box (Sole trader/Partnership) has unlimited liability, no separate legal entity, and no continuity; right box (CC/Companies) has limited liability, separate legal entity, and continuity. "
        f"(b) {pub_co} sells shares publicly (via a Prospectus on the JSE) to countless investors instead of relying solely on {founder}'s personal savings."
    )
    sol = (
        f"**Ownership Spectrum Comparison ({founder}'s Kiosk vs {pub_co}) [4 marks]:**\n\n"
        "**(a) Two Legal Differences [2 marks]:**\n"
        "1. **Liability:** Left box carries **unlimited liability**; right box gives owners **limited liability** **[1]**.\n"
        "2. **Legal Personality & Continuity:** Right-box entities are **separate legal entities** with **continuity of existence**, whereas left-box businesses are not **[1]**.\n\n"
        f"**(b) Capital-Raising Power ({pub_co}) [2 marks]:**\n"
        f"**{pub_co}** (`Ltd`) can issue a **Prospectus** and list shares publicly on the **JSE** to pool massive funds from thousands of investors, unlike **{founder}'s** personal savings **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g8_own_24",
        subskill="24_ownership_spectrum_svg_diagram_comparison",
        title="Ownership Spectrum Diagram: Liability & Capital Growth",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare the headings of the left red box vs right green box in the diagram.",
            "tier_2": "Highlight limited vs unlimited liability, separate legal entity/continuity, and public share sales.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Distinguishes limited vs unlimited liability", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Distinguishes separate legal entity / continuity", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Public share issuance / JSE access raises vast capital", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_public_companies_have_unlimited_liability"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_25_coca_cola_sa_pty_ltd_case_study_classification(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"**Coca-Cola South Africa (Pty) Ltd** distributes beverages to supermarkets and spaza shops across **{area}** and nationwide.\n\n"
        "Based strictly on its registered legal form **`(Pty) Ltd`**, which statement about Coca-Cola South Africa is **correct**?"
    )
    correct = "It is a Private Company that has separate legal personality and limited liability, and cannot offer its shares for sale to the general public on a stock exchange."
    distractors = [
        "It is a Close Corporation owned by between 1 and 10 local municipal councillors.",
        "Any shopper can freely buy shares in Coca-Cola South Africa (Pty) Ltd directly on the JSE.",
        "Its shareholders carry unlimited personal liability for all beverage factory loans.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_own_25",
        subskill="25_coca_cola_sa_pty_ltd_case_study_classification",
        title="Real-World Case: Coca-Cola South Africa (Pty) Ltd",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Even large national brands registered as **`(Pty) Ltd`** (like **Coca-Cola South Africa (Pty) Ltd**) remain **Private Companies**: "
            "they are separate legal entities with limited liability, but do not trade shares publicly on the JSE."
        ),
        hints={
            "tier_1": "Do not let the huge size of a brand fool you — check the `(Pty) Ltd` suffix!",
            "tier_2": "`(Pty) Ltd` means Private Company -> separate legal entity + no public share trading.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_every_large_brand_in_sa_is_a_public_company"],
    )


BUILDERS_01_25 = {
    "01_sole_trader_definition_and_single_owner": arch_01_sole_trader_definition_and_single_owner,
    "02_sole_trader_advantages_and_disadvantages": arch_02_sole_trader_advantages_and_disadvantages,
    "03_sole_trader_unlimited_liability_risk_calculation": arch_03_sole_trader_unlimited_liability_risk_calculation,
    "04_partnership_owner_range_and_agreement": arch_04_partnership_owner_range_and_agreement,
    "05_partnership_profit_sharing_ratio_calculation": arch_05_partnership_profit_sharing_ratio_calculation,
    "06_partnership_joint_liability_and_continuity_exit": arch_06_partnership_joint_liability_and_continuity_exit,
    "07_close_corporation_cc_members_and_ck1_statement": arch_07_close_corporation_cc_members_and_ck1_statement,
    "08_close_corporation_legal_entity_and_continuity": arch_08_close_corporation_legal_entity_and_continuity,
    "09_private_company_pty_ltd_name_and_share_restrictions": arch_09_private_company_pty_ltd_name_and_share_restrictions,
    "10_private_company_moi_and_cipc_registration": arch_10_private_company_moi_and_cipc_registration,
    "11_public_company_ltd_minimums_jse_and_prospectus": arch_11_public_company_ltd_minimums_jse_and_prospectus,
    "12_prospectus_purpose_for_public_share_offer": arch_12_prospectus_purpose_for_public_share_offer,
    "13_dividends_and_shareholder_return_calculation": arch_13_dividends_and_shareholder_return_calculation,
    "14_legal_entity_concept_suing_and_property_ownership": arch_14_legal_entity_concept_suing_and_property_ownership,
    "15_limited_vs_unlimited_liability_case_comparison": arch_15_limited_vs_unlimited_liability_case_comparison,
    "16_continuity_of_existence_across_ownership_forms": arch_16_continuity_of_existence_across_ownership_forms,
    "17_naming_suffixes_identification_table": arch_17_naming_suffixes_identification_table,
    "18_owner_count_and_leadership_structure_table": arch_18_owner_count_and_leadership_structure_table,
    "19_liability_and_legal_persona_comparison_table": arch_19_liability_and_legal_persona_comparison_table,
    "20_sole_trader_vs_partnership_capital_and_skills_tradeoff": arch_20_sole_trader_vs_partnership_capital_and_skills_tradeoff,
    "21_private_co_vs_public_co_capital_raising_and_control": arch_21_private_co_vs_public_co_capital_raising_and_control,
    "22_partnership_capital_contribution_and_debt_shortfall": arch_22_partnership_capital_contribution_and_debt_shortfall,
    "23_formation_documents_matching_table": arch_23_formation_documents_matching_table,
    "24_ownership_spectrum_svg_diagram_comparison": arch_24_ownership_spectrum_svg_diagram_comparison,
    "25_coca_cola_sa_pty_ltd_case_study_classification": arch_25_coca_cola_sa_pty_ltd_case_study_classification,
}
