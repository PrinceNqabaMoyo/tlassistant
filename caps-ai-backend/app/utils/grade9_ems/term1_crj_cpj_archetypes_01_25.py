"""Grade 9 EMS - Cash Receipts Journal & Cash Payments Journal (Sole Trader): Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 2/02. Cash receipts journal and Cash payments journal (sole trader).md

Zero-LLM, 100% deterministic, authentic South African Rand (R) sole-trader contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import get_ems_scenario

TOPIC_NAME = "Cash receipts journal and Cash payments journal (sole trader)"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term1_crj_cpj"

TRADER_SUFFIXES = [
    "Traders",
    "Stores",
    "Suppliers",
    "Hardware",
    "Clothing Boutique",
    "General Dealer",
    "Bookshop",
    "Outfitter",
    "Stationers",
    "Wholesalers",
]

MONTH_YEARS = [
    ("March", "2025", "31", "Mar"),
    ("May", "2025", "31", "May"),
    ("June", "2025", "30", "Jun"),
    ("July", "2025", "31", "Jul"),
    ("August", "2025", "31", "Aug"),
    ("October", "2025", "31", "Oct"),
]

CUSTOMERS_AND_PAYEES = [
    "Khanyisa Primary",
    "Thaba Hardware",
    "Bhekinkosi Wholesalers",
    "Mamelodi Distributors",
    "Gqeberha Stationery Co.",
    "Palesa Furnishers",
    "Zanele Logistics",
    "Eskom",
    "Telkom SA",
    "City Treasurer",
    "Vodacom Business",
    "Metro Municipality",
]


def _fmt_r(amount: int | float) -> str:
    """Format South African Rand amounts with space thousands separator and comma decimals."""
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _cents_to_r(cents: int) -> str:
    """Format exact integer cents as clean Rand display (drops ,00 when exact Rand)."""
    if cents % 100 == 0:
        return _fmt_r(cents // 100)
    rands = cents // 100
    rem = cents % 100
    return f"R{rands:,}".replace(",", " ") + f",{rem:02d}"


def _cents_to_input(cents: int) -> str:
    """Format exact integer cents as numeric answer string without currency symbol or spaces."""
    if cents % 100 == 0:
        return str(cents // 100)
    return f"{cents // 100},{cents % 100:02d}"


def _trader_name(rng: random.Random, sc: Dict[str, Any]) -> str:
    return f"{sc['entrepreneur']} {rng.choice(TRADER_SUFFIXES)}"


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
    term: int = 1,
    caps_weight: int = 30,
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_crj_cpj_{subskill}",
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
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Selects {letter}: {correct_text}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "cash_journals", "sole_trader"],
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
    qtype: str = "math_short",
    term: int = 1,
    caps_weight: int = 30,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_crj_cpj_{subskill}",
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
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "cash_journals", "sole_trader"],
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
    term: int = 1,
    caps_weight: int = 30,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g9_crj_cpj_{subskill}",
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
        "term": term,
        "caps_weight_percent": caps_weight,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["accounting", "cash_journals", "ledger_table"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _source_doc_svg(
    header_title: str,
    doc_no: str,
    date_str: str,
    lines: List[tuple[str, str]],
    accent: str = "#0f766e",
) -> str:
    """Render an authentic source-document SVG card for Duplicate Receipt / Till Slip / Cheque Counterfoil."""
    y = 86
    body_parts: List[str] = []
    for lbl, val in lines:
        body_parts.append(
            f'<text x="24" y="{y}" font-size="11" font-weight="bold" fill="#475569">{lbl}:</text>'
            f'<text x="155" y="{y}" font-size="11.5" font-weight="bold" fill="#0f172a">{val}</text>'
            f'<line x1="24" y1="{y + 7}" x2="496" y2="{y + 7}" stroke="#e2e8f0" stroke-width="1"/>'
        )
        y += 28
    h = max(195, y + 18)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 {h}" width="520" height="{h}">'
        f'<rect x="6" y="6" width="508" height="{h - 12}" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<rect x="6" y="6" width="508" height="44" rx="8" fill="{accent}"/>'
        f'<text x="24" y="33" font-size="13" font-weight="bold" fill="#ffffff">{header_title}</text>'
        f'<text x="496" y="25" font-size="11" font-weight="bold" text-anchor="end" fill="#f8fafc">No: {doc_no}</text>'
        f'<text x="496" y="42" font-size="10" text-anchor="end" fill="#e2e8f0">Date: {date_str}</text>'
        + "".join(body_parts)
        + "</svg>"
    )


def arch_01_service_vs_trading_business_comparison(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    variants = [
        (
            f"buys {sc['item_sold']} and household stock from {sc['supplier']} to resell at a profit mark-up",
            "Trading business: uses Sales, Cost of Sales, and Trading Stock columns in its CRJ and CPJ because physical merchandise is bought and resold.",
            [
                "Service business: uses Current Income only and never tracks Cost of Sales or Trading Stock.",
                "Manufacturing only: records raw material depreciation rather than Cash Receipts or Payments Journals.",
                "Non-profit entity: does not maintain a Bank column or profit mark-up on goods sold.",
            ],
            "Buying stock for resale classifies the enterprise as a trading business.",
        ),
        (
            f"switches from a pure repair service to selling spare parts and {sc['item_sold']} for cash",
            "The business must introduce Trading Stock, Sales, and Cost of Sales columns because merchandise bought for resale must be tracked at both selling price and cost price.",
            [
                "The business removes the Bank column and merges Capital directly into Current Income.",
                "Sales revenue is replaced entirely by Drawings whenever stock is handed to customers.",
                "Cost of Sales replaces Wages so workers are paid directly out of the till slip.",
            ],
            "Selling tangible goods adds Trading Stock, Sales, and Cost of Sales to the journals.",
        ),
        (
            f"runs {biz} in {sc['area']} stocking goods purchased wholesale from {sc['supplier']}",
            "Sales records total cash received at selling price (revenue), whereas Cost of Sales records the original cost price of the stock that left the shelves.",
            [
                "Sales records the owner's capital contribution, while Cost of Sales records monthly water and electricity.",
                "Sales and Cost of Sales are identical amounts on every Cash Register Roll regardless of profit mark-up.",
                "Sales is recorded only in the CPJ, while Cost of Sales is added to the Bank deposit slip.",
            ],
            "A trading business records both revenue (Sales) and stock cost (Cost of Sales) on every sale.",
        ),
    ]
    desc, correct, distractors, why = rng.choice(variants)
    prompt = (
        f"**{biz}** (owned by **{sc['entrepreneur']}** in {sc['area']}) {desc}.\n\n"
        f"Which accounting classification and Cash Journal distinction accurately describes a **sole-trader trading business** compared to a Grade 8 service business?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_01",
        subskill="01_service_vs_trading_business_comparison",
        title="Service vs Trading Sole Trader Journals",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"{why} Specifically: **{correct}**",
        hints={
            "tier_1": "Think about what changes when a business sells physical merchandise instead of only labour/services.",
            "tier_2": "A trading business buys Trading Stock and sells it for Sales while simultaneously recording Cost of Sales.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_service_and_trading_journals"],
    )


def arch_02_what_i_want_what_i_have_markup_framework(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    markup = rng.choice([25, 30, 40, 50, 60, 75])
    cp_sample = rng.randint(12, 40) * 100
    sp_sample = cp_sample * (100 + markup) // 100

    prompt = (
        f"At **{biz}**, merchandise is marked up at **{markup}% on cost price**. "
        f"A cash sale rings up at a Selling Price of **{_fmt_r(sp_sample)}**.\n\n"
        f"Using the standard **'What I WANT / What I HAVE'** percentage table (`Cost Price % = 100%`), "
        f"which fraction correctly calculates the **Cost of Sales**?"
    )
    sp_pct = 100 + markup
    correct = f"{_fmt_r(sp_sample)} × 100 / {sp_pct} (Want Cost Price = 100%, Have Selling Price = {sp_pct}%)"
    distractors = [
        f"{_fmt_r(sp_sample)} × {sp_pct} / 100 (multiplies Selling Price above 100%)",
        f"{_fmt_r(sp_sample)} × {100 - markup} / 100 (subtracts {markup}% straight from Selling Price)",
        f"{_fmt_r(sp_sample)} × {markup} / 100 (computes profit percentage on Selling Price instead of Cost)",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_02",
        subskill="02_what_i_want_what_i_have_markup_framework",
        title="What I WANT / What I HAVE Mark-up Setup",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"With profit mark-up on cost = **{markup}%**: Cost Price = **100%**, Profit = **{markup}%**, and Selling Price = **{sp_pct}%**.\n\n"
            f"Because we **WANT** Cost Price (100%) and **HAVE** Selling Price ({sp_pct}% = {_fmt_r(sp_sample)}):\n"
            f"- Formula: `{_fmt_r(sp_sample)} × 100 / {sp_pct} = {_fmt_r(cp_sample)}`.\n"
            f"- Subtracting `{markup}%` directly from Selling Price is wrong because `{markup}%` is a percentage of Cost Price, not Selling Price."
        ),
        hints={
            "tier_1": "Set Cost Price = 100%, Profit = Mark-up %, and Selling Price = 100% + Mark-up %.",
            "tier_2": f"Selling Price corresponds to {sp_pct}%, while Cost Price corresponds to 100%.",
            "tier_3": f"Multiply Selling Price ({_fmt_r(sp_sample)}) by (Want / Have) = 100 / {sp_pct}.",
        },
        misconception_tags=["subtracting_markup_from_selling_price"],
    )


def arch_03_selling_price_from_cost_and_markup(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cp = rng.randint(15, 95) * 25 + rng.choice([0, 12, 18, 25])
    markup = rng.choice([13, 20, 25, 29, 35, 40, 45, 50, 60, 75])
    sp_cents = cp * (100 + markup)
    expected = _cents_to_input(sp_cents)
    sp_disp = _cents_to_r(sp_cents)
    sp_pct = 100 + markup

    prompt = (
        f"**{biz}** in {sc['area']} sells merchandise with a **cost price of {_fmt_r(cp)}** at a profit mark-up of **{markup}% on cost**.\n\n"
        f"Calculate the **Selling Price** for the Cash Receipts Journal.\n"
        f"*(Enter digits without spaces or the R symbol; use a comma for cents if applicable, e.g. `2514,25`.)*"
    )
    worked = (
        f"**Selling Price Calculation** [3 marks]\n\n"
        f"| Component | Percentage | Rand Amount |\n"
        f"| --- | --- | --- |\n"
        f"| Cost Price (HAVE) | 100% | {_fmt_r(cp)} |\n"
        f"| Profit Mark-up | +{markup}% | {_cents_to_r(cp * markup)} |\n"
        f"| **Selling Price (WANT)** | **{sp_pct}%** | **{sp_disp}** |\n\n"
        f"Working: `{_fmt_r(cp)} × {sp_pct}/100 = {sp_disp}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_03",
        subskill="03_selling_price_from_cost_and_markup",
        title="Calculate Selling Price from Cost & Mark-up",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Selling Price = Cost Price + Mark-up on Cost Price.",
            "tier_2": f"Using What I WANT / What I HAVE: {_fmt_r(cp)} × ({sp_pct} / 100).",
            "tier_3": f"{_fmt_r(cp)} × {sp_pct} ÷ 100 = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct percentage multiplier ({sp_pct}/100)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Accurate calculation resulting in {sp_disp}", "marks": 2, "editable": True},
        ],
        misconception_tags=["markup_percent_multiplication_error"],
    )


def arch_04_cost_of_sales_from_selling_price_and_markup(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cp = rng.randint(18, 96) * 50 + rng.choice([0, 15, 35, 45])
    markup = rng.choice([15, 25, 35, 43, 50, 57, 60, 75, 80])
    sp_cents = cp * (100 + markup)
    sp_disp = _cents_to_r(sp_cents)
    sp_pct = 100 + markup
    expected = str(cp)

    prompt = (
        f"At **{biz}**, cash sales per the Cash Register Roll amount to **{sp_disp}**. "
        f"The business marks up goods by **{markup}% on cost price**.\n\n"
        f"Calculate the **Cost of Sales** amount to be entered in the CRJ.\n"
        f"*(Enter the whole Rand number without spaces or the R symbol.)*"
    )
    worked = (
        f"**Cost of Sales Calculation** [3 marks]\n\n"
        f"| Component | Percentage | Rand Amount |\n"
        f"| --- | --- | --- |\n"
        f"| **Cost Price / Cost of Sales (WANT)** | **100%** | **{_fmt_r(cp)}** |\n"
        f"| Profit Mark-up | +{markup}% | {_cents_to_r(cp * markup)} |\n"
        f"| Selling Price (HAVE) | {sp_pct}% | {sp_disp} |\n\n"
        f"Working: `{sp_disp} × 100/{sp_pct} = {_fmt_r(cp)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_04",
        subskill="04_cost_of_sales_from_selling_price_and_markup",
        title="Calculate Cost of Sales from Selling Price",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Never subtract the mark-up percentage directly from Selling Price; divide by (100 + mark-up%).",
            "tier_2": f"Cost of Sales = {sp_disp} × 100 / {sp_pct}.",
            "tier_3": f"Cost of Sales = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct ratio 100/{sp_pct}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Exact Cost of Sales = {_fmt_r(cp)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_markup_from_selling_price"],
    )


def arch_05_profit_amount_from_selling_price_and_markup(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cp = rng.randint(16, 85) * 100
    markup = rng.choice([20, 25, 30, 40, 45, 50, 60, 75])
    profit = cp * markup // 100
    sp = cp + profit
    sp_pct = 100 + markup
    expected = str(profit)

    prompt = (
        f"**{biz}** records total Cash Sales of **{_fmt_r(sp)}** on {sc['item_sold']} using a standard **{markup}% profit mark-up on cost**.\n\n"
        f"Calculate the **Rand profit earned** directly from this sale.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Gross Profit Calculation** [3 marks]\n\n"
        f"- Selling Price = {sp_pct}% = {_fmt_r(sp)}\n"
        f"- Profit (WANT) = {markup}%\n"
        f"- Formula: `{_fmt_r(sp)} × {markup}/{sp_pct} = {_fmt_r(profit)}` (check: Cost Price = {_fmt_r(cp)}, Profit = {_fmt_r(sp)} - {_fmt_r(cp)} = {_fmt_r(profit)})\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_05",
        subskill="05_profit_amount_from_selling_price_and_markup",
        title="Calculate Gross Profit from Selling Price",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Notice you WANT Profit (mark-up %) and HAVE Selling Price (100% + mark-up %).",
            "tier_2": f"Profit = {_fmt_r(sp)} × {markup} / {sp_pct}.",
            "tier_3": f"Profit earned = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct fraction {markup}/{sp_pct}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Profit = {_fmt_r(profit)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["computing_profit_on_selling_price"],
    )


def arch_06_markup_percentage_from_sales_and_cost(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    markup = rng.choice([20, 25, 28, 30, 35, 40, 45, 50, 60, 75, 80, 120])
    cp = rng.randint(25, 95) * 100
    profit = cp * markup // 100
    sp = cp + profit
    expected = str(markup)

    prompt = (
        f"During the month, **{biz}** sold merchandise with a **Cost Price of {_fmt_r(cp)}** for a **Selling Price of {_fmt_r(sp)}**.\n\n"
        f"Calculate the **profit mark-up percentage on cost price**.\n"
        f"*(Enter the integer percentage number without the `%` symbol.)*"
    )
    worked = (
        f"**Profit Mark-up Percentage Calculation** [3 marks]\n\n"
        f"1. Gross Profit = Selling Price - Cost Price = `{_fmt_r(sp)} - {_fmt_r(cp)} = {_fmt_r(profit)}`\n"
        f"2. Mark-up % on Cost = `(Gross Profit ÷ Cost Price) × 100` = `({profit} ÷ {cp}) × 100 = {markup}%`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_06",
        subskill="06_markup_percentage_from_sales_and_cost",
        title="Calculate Mark-up Percentage on Cost",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "First find Gross Profit (Sales minus Cost of Sales), then divide by Cost of Sales.",
            "tier_2": f"Mark-up % = (({_fmt_r(sp)} - {_fmt_r(cp)}) ÷ {_fmt_r(cp)}) × 100.",
            "tier_3": f"{profit} ÷ {cp} × 100 = {markup}% (enter {expected}).",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Gross profit = {_fmt_r(profit)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Divides by Cost Price {_fmt_r(cp)} × 100 = {markup}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_profit_by_selling_price"],
    )


def arch_07_implied_markup_ratio_applied_to_new_sale(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    markup = rng.choice([25, 40, 50, 60, 75, 80, 100])
    tb_cos = rng.randint(25, 85) * 100
    tb_sales = tb_cos * (100 + markup) // 100
    new_cp = rng.randint(15, 75) * 100
    new_sp = new_cp * (100 + markup) // 100
    expected = str(new_cp)

    prompt = (
        f"The Trial Balance of **{biz}** shows:\n"
        f"- **Sales:** {_fmt_r(tb_sales)}\n"
        f"- **Cost of sales:** {_fmt_r(tb_cos)}\n\n"
        f"Using the business's consistent profit mark-up percentage, merchandise with a **Selling Price of {_fmt_r(new_sp)}** is sold for cash. "
        f"Calculate the **Cost of Sales** for this new transaction.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Two-Step Mark-up Derivation & Cost of Sales** [4 marks]\n\n"
        f"1. **Step 1 (Find consistent mark-up %):**\n"
        f"   - Gross Profit = `{_fmt_r(tb_sales)} - {_fmt_r(tb_cos)} = {_fmt_r(tb_sales - tb_cos)}`\n"
        f"   - Mark-up % = `({tb_sales - tb_cos} ÷ {tb_cos}) × 100 = {markup}%`\n"
        f"2. **Step 2 (Find new Cost of Sales):**\n"
        f"   - Cost of Sales = `{_fmt_r(new_sp)} × 100/{100 + markup} = {_fmt_r(new_cp)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_07",
        subskill="07_implied_markup_ratio_applied_to_new_sale",
        title="Derive Trial Balance Mark-up & Find Cost of Sales",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=4,
        hints={
            "tier_1": "Use Sales and Cost of Sales from the Trial Balance first to calculate the mark-up percentage.",
            "tier_2": f"Mark-up = {markup}%. Now apply 100 / {100 + markup} to {_fmt_r(new_sp)}.",
            "tier_3": f"Cost of Sales = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Finds mark-up % = {markup}%", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Applies 100/{100 + markup} to get {_fmt_r(new_cp)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["inconsistent_markup_base_error"],
    )


def arch_08_implied_markup_applied_to_new_cost_price(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    markup = rng.choice([20, 25, 50, 60, 80, 114])
    tb_cos = rng.randint(20, 75) * 100
    tb_sales = tb_cos * (100 + markup) // 100
    new_cp = rng.randint(12, 65) * 100
    new_sp = new_cp * (100 + markup) // 100
    expected = str(new_sp)

    prompt = (
        f"The Trial Balance of **{biz}** shows:\n"
        f"- **Sales:** {_fmt_r(tb_sales)}\n"
        f"- **Cost of sales:** {_fmt_r(tb_cos)}\n\n"
        f"Assuming the same mark-up policy applies, merchandise with a **Cost Price of {_fmt_r(new_cp)}** is sold. "
        f"Calculate the **Selling Price** to record in the CRJ.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Two-Step Mark-up Derivation & Selling Price** [4 marks]\n\n"
        f"1. **Step 1 (Mark-up % from Trial Balance):**\n"
        f"   - Profit = `{_fmt_r(tb_sales)} - {_fmt_r(tb_cos)} = {_fmt_r(tb_sales - tb_cos)}`\n"
        f"   - Mark-up % = `({tb_sales - tb_cos} ÷ {tb_cos}) × 100 = {markup}%`\n"
        f"2. **Step 2 (New Selling Price):**\n"
        f"   - Selling Price = `{_fmt_r(new_cp)} × {100 + markup}/100 = {_fmt_r(new_sp)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_08",
        subskill="08_implied_markup_applied_to_new_cost_price",
        title="Derive Mark-up & Find New Selling Price",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=4,
        hints={
            "tier_1": "Determine the mark-up % from the Trial Balance balances before pricing the new stock.",
            "tier_2": f"Mark-up = {markup}%, so Selling Price = {_fmt_r(new_cp)} × {100 + markup}/100.",
            "tier_3": f"Selling Price = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Derives mark-up = {markup}%", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Calculates Selling Price = {_fmt_r(new_sp)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["markup_percent_multiplication_error"],
    )


def arch_09_gross_profit_vs_cash_discount_received(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    # Mix both clean integer % discount and 12,5% trade/cash discount with packing material
    use_half = rng.choice([True, False])
    if use_half:
        goods = rng.randint(6, 20) * 800
        disc_pct_disp = "12,5%"
        disc_amt = goods * 125 // 1000
        net_goods = goods - disc_amt
        packing = rng.choice([0, rng.randint(2, 9) * 50])
    else:
        goods = rng.randint(10, 45) * 200
        disc_pct = rng.choice([5, 10, 15, 20])
        disc_pct_disp = f"{disc_pct}%"
        disc_amt = goods * disc_pct // 100
        net_goods = goods - disc_amt
        packing = rng.randint(2, 12) * 45

    total_chq = net_goods + packing
    expected = str(total_chq)
    pack_txt = f" plus **packing material of {_fmt_r(packing)}** (no discount on packing)" if packing > 0 else ""

    prompt = (
        f"**{biz}** buys trading stock from **{sc['supplier']}** priced at **{_fmt_r(goods)}** "
        f"less a **{disc_pct_disp} cash discount**{pack_txt} and settles by EFT/cheque immediately.\n\n"
        f"Calculate the **final amount payable** recorded in the **Bank** column of the CPJ.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Cash Discount & Net Payment Calculation** [3 marks]\n\n"
        f"- Discount on stock: `{disc_pct_disp} × {_fmt_r(goods)} = {_fmt_r(disc_amt)}`\n"
        f"- Net Trading Stock cost: `{_fmt_r(goods)} - {_fmt_r(disc_amt)} = {_fmt_r(net_goods)}`\n"
        + (f"- Add non-discounted packing material: `{_fmt_r(net_goods)} + {_fmt_r(packing)} = {_fmt_r(total_chq)}`\n" if packing > 0 else "")
        + f"- CPJ Bank payment: `{_fmt_r(total_chq)}` -> Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_09",
        subskill="09_gross_profit_vs_cash_discount_received",
        title="Cash Discount on Stock Purchases (CPJ)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Trade/cash discounts given at purchase reduce the Bank payment entered in the CPJ.",
            "tier_2": f"Discount = {_fmt_r(disc_amt)}; Net stock = {_fmt_r(net_goods)}" + (f" + {_fmt_r(packing)}." if packing > 0 else "."),
            "tier_3": f"Total Bank amount = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts discount ({_fmt_r(disc_amt)}) from goods", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Final CPJ Bank payment = {_fmt_r(total_chq)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["forgetting_cash_discount_deduction"],
    )


def arch_10_capital_increase_percentage_backward_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    pct = rng.choice([10, 12, 15, 17, 20, 25])
    orig_cap = rng.randint(80, 240) * 1000
    inc = orig_cap * pct // 100
    new_cap = orig_cap + inc
    expected = str(inc)

    prompt = (
        f"The owner of **{biz}**, **{sc['entrepreneur']}**, increased capital in the business by **{pct}%** "
        f"to a new balance of **{_fmt_r(new_cap)}**.\n\n"
        f"Calculate the **capital increase** to be entered in the **Cash Receipts Journal (CRJ)**.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Capital Increase (Percentage-Inclusive) Calculation** [3 marks]\n\n"
        f"- Original Capital = `100%`\n"
        f"- Increase = `+{pct}%`\n"
        f"- New Capital (HAVE) = `{100 + pct}%` = `{_fmt_r(new_cap)}`\n"
        f"- Capital Increase (WANT) = `{_fmt_r(new_cap)} × {pct}/{100 + pct} = {_fmt_r(inc)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_10",
        subskill="10_capital_increase_percentage_backward_calc",
        title="Calculate Capital Increase from Percentage New Total",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": f"The new balance ({_fmt_r(new_cap)}) already includes the {pct}% increase, so it represents {100 + pct}%.",
            "tier_2": f"Use What I WANT / What I HAVE: {_fmt_r(new_cap)} × {pct} / {100 + pct}.",
            "tier_3": f"Capital increase = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Recognises {_fmt_r(new_cap)} represents {100 + pct}%", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Calculates CRJ Capital entry = {_fmt_r(inc)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["applying_increase_pct_to_final_balance"],
    )


def arch_11_capital_topup_crj_entry_from_trial_balance(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    old_cap = rng.randint(150, 380) * 1000
    add_cap = rng.randint(35, 145) * 1000
    new_cap = old_cap + add_cap
    expected = str(add_cap)

    prompt = (
        f"The Trial Balance of **{biz}** shows a **Capital** balance of **{_fmt_r(old_cap)}**. "
        f"**{sc['entrepreneur']}** deposits additional funds directly into the business bank account to increase total Capital to **{_fmt_r(new_cap)}**.\n\n"
        f"Calculate the amount that must be entered in the **CRJ** (Bank and Sundry Accounts).\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**CRJ Capital Contribution Entry** [2 marks]\n\n"
        f"- New Capital target: `{_fmt_r(new_cap)}`\n"
        f"- Existing Capital balance: `{_fmt_r(old_cap)}`\n"
        f"- Additional cash contributed (CRJ entry): `{_fmt_r(new_cap)} - {_fmt_r(old_cap)} = {_fmt_r(add_cap)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_11",
        subskill="11_capital_topup_crj_entry_from_trial_balance",
        title="Capital Top-Up CRJ Amount from Trial Balance",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Journals record only the new transaction movement, not the old cumulative balance.",
            "tier_2": f"Subtract existing Capital ({_fmt_r(old_cap)}) from the new total ({_fmt_r(new_cap)}).",
            "tier_3": f"CRJ Capital entry = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts {_fmt_r(old_cap)} from {_fmt_r(new_cap)} = {_fmt_r(add_cap)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["entering_full_balance_instead_of_movement"],
    )


def arch_12_annual_rent_to_monthly_crj_or_cpj(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    monthly = rng.randint(18, 75) * 150
    annual = monthly * 12
    expected = str(monthly)
    is_receipt = rng.choice([True, False])
    journal_str = "CRJ (Rent Income)" if is_receipt else "CPJ (Rent Expense)"
    verb = "sub-lets a spare storeroom for an annual rental of" if is_receipt else "rents shop premises for an annual rental of"

    prompt = (
        f"**{biz}** {verb} **{_fmt_r(annual)} per year**, settled monthly.\n\n"
        f"Calculate the monthly amount to be recorded in the **{journal_str}**.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Monthly Rental Calculation ({journal_str})** [2 marks]\n\n"
        f"- Annual rent: `{_fmt_r(annual)}` (12 months)\n"
        f"- Monthly rent: `{_fmt_r(annual)} ÷ 12 = {_fmt_r(monthly)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_12",
        subskill="12_annual_rent_to_monthly_crj_or_cpj",
        title="Convert Annual Rent to Monthly Journal Entry",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Cash journals cover one calendar month at a time.",
            "tier_2": f"Divide the annual rent ({_fmt_r(annual)}) by 12 months.",
            "tier_3": f"Monthly rent = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Divides {_fmt_r(annual)} by 12 = {_fmt_r(monthly)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["recording_annual_amount_in_monthly_journal"],
    )


def arch_13_mixed_payment_cheque_split_drawings(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    bus_amt = rng.randint(12, 48) * 35
    draw_amt = rng.randint(6, 28) * 35
    total_amt = bus_amt + draw_amt
    util = rng.choice(["water and electricity", "telephone account", "municipal rates and refuse"])
    ask_drawings = rng.choice([True, False])

    if ask_drawings:
        expected = str(draw_amt)
        prompt = (
            f"**{biz}** issued a single EFT/cheque for **{_fmt_r(total_amt)}** to pay the business's **{util}** of **{_fmt_r(bus_amt)}**, "
            f"with the remainder paying **{sc['entrepreneur']}'s personal {util}**.\n\n"
            f"Calculate the **Drawings** amount to be entered in the CPJ.\n"
            f"*(Enter digits without spaces or the R symbol.)*"
        )
        worked = (
            f"**Split Payment Drawings Calculation** [2 marks]\n\n"
            f"- Total CPJ Bank outflow: `{_fmt_r(total_amt)}`\n"
            f"- Business {util}: `{_fmt_r(bus_amt)}`\n"
            f"- Owner's personal portion (**Drawings**): `{_fmt_r(total_amt)} - {_fmt_r(bus_amt)} = {_fmt_r(draw_amt)}`\n"
            f"- Answer: `{expected}`"
        )
        t2 = f"Subtract business portion ({_fmt_r(bus_amt)}) from total payment ({_fmt_r(total_amt)})."
    else:
        expected = str(total_amt)
        prompt = (
            f"**{biz}** pays **{_fmt_r(bus_amt)}** for the business's **{util}** together with **{_fmt_r(draw_amt)}** "
            f"for **{sc['entrepreneur']}'s personal {util}** on one cheque/EFT.\n\n"
            f"Calculate the total amount entered in the **Bank** column of the CPJ.\n"
            f"*(Enter digits without spaces or the R symbol.)*"
        )
        worked = (
            f"**Combined Business & Drawings Payment** [2 marks]\n\n"
            f"- Business {util}: `{_fmt_r(bus_amt)}`\n"
            f"- Personal Drawings: `{_fmt_r(draw_amt)}`\n"
            f"- Total Bank outflow (CPJ): `{_fmt_r(bus_amt)} + {_fmt_r(draw_amt)} = {_fmt_r(total_amt)}`\n"
            f"- Answer: `{expected}`"
        )
        t2 = f"Add business portion ({_fmt_r(bus_amt)}) and personal Drawings ({_fmt_r(draw_amt)})."

    return _build_short(
        rng,
        qid_prefix="g9_cc_13",
        subskill="13_mixed_payment_cheque_split_drawings",
        title="Split Business Expense & Personal Drawings",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Personal expenses paid from the business bank account belong to Drawings, never business expenses.",
            "tier_2": t2,
            "tier_3": f"Answer: {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct split calculation = {expected}", "marks": 2, "editable": True},
        ],
        misconception_tags=["mixing_drawings_into_business_expenses"],
    )


def arch_14_split_consumables_stationery_and_packing_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    packing = rng.randint(6, 26) * 25
    stationery = rng.randint(4, 18) * 25
    total = packing + stationery
    expected = str(stationery)

    prompt = (
        f"**{biz}** paid **{_fmt_r(total)}** in total to **{sc['supplier']}** for **packing material** and **stationery**. "
        f"The packing material portion cost **{_fmt_r(packing)}**.\n\n"
        f"Calculate the amount to allocate to **Stationery** in the CPJ.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**Split Consumables Allocation** [2 marks]\n\n"
        f"- Total CPJ Bank payment: `{_fmt_r(total)}`\n"
        f"- Packing Material portion: `{_fmt_r(packing)}`\n"
        f"- Stationery balance: `{_fmt_r(total)} - {_fmt_r(packing)} = {_fmt_r(stationery)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_14",
        subskill="14_split_consumables_stationery_and_packing_calc",
        title="Split Invoice: Packing Material vs Stationery",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "A single cheque/EFT can settle two different expense accounts; the two parts must sum to the Bank outflow.",
            "tier_2": f"Subtract packing material ({_fmt_r(packing)}) from total payment ({_fmt_r(total)}).",
            "tier_3": f"Stationery = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Subtracts {_fmt_r(packing)} from {_fmt_r(total)} = {_fmt_r(stationery)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["putting_full_split_invoice_into_one_column"],
    )


def arch_15_source_document_classification_crj_vs_cpj_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    pool = [
        ("Duplicate Receipt", "CRJ", "Cash received from owner (Capital) or tenant (Rent Income)"),
        ("Cash Register Roll (CRR) / Till Slip", "CRJ", "Daily cash sales of trading stock"),
        ("Duplicate Deposit Slip / EFT Receipt Proof", "CRJ", "Direct cash/EFT banked directly into business account"),
        ("Cheque Counterfoil / EFT Payment Confirmation", "CPJ", "Cash paid for Trading Stock, Wages, or Expenses"),
        ("Bank Debit Note / Bank Statement Charges", "CPJ", "Monthly bank service fees and interest paid"),
    ]
    rng.shuffle(pool)
    headers = ["Source Document", "Subsidiary Journal (CRJ / CPJ)", "Typical Sole-Trader Transaction"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [
        "| Source Document | Subsidiary Journal | Typical Transaction |",
        "| --- | --- | --- |",
    ]
    for i, (doc, jnl, desc) in enumerate(pool):
        correct_map[f"t0_r{i}_c1"] = jnl
        cell_hints[f"t0_r{i}_c1"] = f"Ask whether '{doc}' shows cash coming INTO the bank (CRJ) or going OUT (CPJ)."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": doc, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": desc, "type": "given", "editable": False},
        ])
        md_lines.append(f"| {doc} | **{jnl}** | {desc} |")

    prompt = (
        f"The bookkeeper at **{biz}** is sorting source documents before posting to the cash journals.\n\n"
        f"Complete the classification table below by entering **`CRJ`** or **`CPJ`** for each source document."
    )
    sample = "; ".join(f"{doc} -> {jnl}" for doc, jnl, _ in pool)
    worked = "**Source Document to Cash Journal Mapping** [5 marks]:\n\n" + "\n".join(md_lines)
    return _build_table(
        rng,
        qid_prefix="g9_cc_15",
        subskill="15_source_document_classification_crj_vs_cpj_table",
        title="Source Documents to CRJ / CPJ Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Cash flowing INTO the business bank uses CRJ; cash flowing OUT uses CPJ.",
            "tier_2": "Duplicates (receipts, deposit slips) and till rolls go to CRJ; counterfoils and EFT payment confirmations go to CPJ.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"{doc}: {jnl}", "marks": 1, "editable": True} for i, (doc, jnl, _) in enumerate(pool)],
        misconception_tags=["source_document_journal_swap"],
    )


def arch_16_visual_duplicate_receipt_interpretation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    day = f"{rng.randint(2, 24):02d}"
    rec_no = f"REC {rng.randint(104, 498)}"
    is_cap = rng.choice([True, False])
    amt = rng.randint(12, 65) * 500 if is_cap else rng.randint(4, 18) * 450
    payer = sc["entrepreneur"] if is_cap else rng.choice(CUSTOMERS_AND_PAYEES[:6])
    reason = "Additional capital contribution" if is_cap else "Monthly shop sub-lease rental"
    target_acc = "Capital" if is_cap else "Rent Income"

    svg = _source_doc_svg(
        f"DUPLICATE RECEIPT — {biz.upper()}",
        rec_no,
        f"{day} {m_name} {yr}",
        [
            ("Received from", payer),
            ("Amount", _fmt_r(amt)),
            ("For", reason),
        ],
        accent="#1d4ed8",
    )
    prompt = (
        f"Inspect the **Duplicate Receipt** above from **{biz}**.\n\n"
        f"How must document **{rec_no}** be recorded in the **Cash Receipts Journal**?"
    )
    correct = f"CRJ: Analysis of Receipts {_fmt_r(amt)}, Bank {_fmt_r(amt)} (if only receipt that day), and Sundry Accounts -> {target_acc} {_fmt_r(amt)}."
    distractors = [
        f"CPJ: Bank {_fmt_r(amt)} and Sales {_fmt_r(amt)} because a receipt is issued for stock sold.",
        f"CRJ: Sales {_fmt_r(amt)} and Cost of Sales {_fmt_r(amt)} regardless of why cash was received.",
        f"General Journal only, because non-sales cash receipts are excluded from the Cash Receipts Journal.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_16",
        subskill="16_visual_duplicate_receipt_interpretation",
        title="Interpret Duplicate Receipt Source Document",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"A **Duplicate Receipt** proves cash was received at the business premises, so it enters the **CRJ** (`Analysis of Receipts`, `Bank`, and **Sundry Accounts: {target_acc}** with **{_fmt_r(amt)}** — never `Sales` or `Cost of Sales`).",
        hints={
            "tier_1": "Duplicate Receipts enter the CRJ; check the 'For' line to select the Sundry account.",
            "tier_2": f"This receipt is for '{reason}', which is NOT cash sales of stock, so it goes to Sundry Accounts -> {target_acc}.",
            "tier_3": correct,
        },
        misconception_tags=["putting_sundry_receipts_into_sales"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_17_visual_cash_register_roll_crj_extraction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, yr, _, _ = rng.choice(MONTH_YEARS)
    day = f"{rng.randint(3, 26):02d}"
    crr_no = f"CRR {rng.randint(12, 94)}"
    markup = rng.choice([25, 40, 50, 60])
    cos = rng.randint(14, 55) * 100
    sales = cos * (100 + markup) // 100

    svg = _source_doc_svg(
        f"CASH REGISTER ROLL (TILL Z-TOTAL) — {biz.upper()}",
        crr_no,
        f"{day} {m_name} {yr}",
        [
            ("Item Summary", f"Cash sales of {sc['item_sold']} & merchandise"),
            ("Mark-up Policy", f"{markup}% on cost price"),
            ("Total Cash Sales", _fmt_r(sales)),
        ],
        accent="#047857",
    )
    expected = str(cos)
    prompt = (
        f"Inspect the **Cash Register Roll (CRR)** above for **{biz}**.\n\n"
        f"After recording **{_fmt_r(sales)}** in `Analysis of Receipts`, `Bank`, and `Sales` in the CRJ, "
        f"calculate the **Cost of Sales** amount to enter in the Cost of Sales column.\n"
        f"*(Enter digits without spaces or the R symbol.)*"
    )
    worked = (
        f"**CRR to CRJ Cost of Sales Extraction** [3 marks]\n\n"
        f"- Document `{crr_no}` Cash Sales = `{_fmt_r(sales)}` (`100% + {markup}% = {100 + markup}%`)\n"
        f"- Cost of Sales = `{_fmt_r(sales)} × 100/{100 + markup} = {_fmt_r(cos)}`\n"
        f"- Answer: `{expected}`"
    )
    return _build_short(
        rng,
        qid_prefix="g9_cc_17",
        subskill="17_visual_cash_register_roll_crj_extraction",
        title="Extract CRJ Cost of Sales from Cash Register Roll",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Cash Register Rolls record Selling Price; Cost of Sales equals Selling Price × 100 / (100 + mark-up%).",
            "tier_2": f"Cost of Sales = {_fmt_r(sales)} × 100 / {100 + markup}.",
            "tier_3": f"Cost of Sales = {expected}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Applies 100/{100 + markup} to {_fmt_r(sales)} = {_fmt_r(cos)}", "marks": 3, "editable": True},
        ],
        misconception_tags=["subtracting_markup_from_selling_price"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_18_crj_analysis_of_receipts_same_day_banking(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    m_name, _, _, _ = rng.choice(MONTH_YEARS)
    day = rng.randint(4, 21)
    r1 = rng.randint(12, 42) * 100
    r2 = rng.randint(5, 22) * 100
    bank_day = r1 + r2

    prompt = (
        f"On **{day} {m_name}**, **{biz}** receives two separate cash amounts in the till:\n"
        f"1. Cash sales per Cash Register Roll: **{_fmt_r(r1)}**\n"
        f"2. Rent received in cash from a tenant (Duplicate Receipt): **{_fmt_r(r2)}**\n\n"
        f"Both amounts are deposited together at the end of the day. How are **`Analysis of Receipts`** and **`Bank`** completed for **{day} {m_name}**?"
    )
    correct = f"Enter {_fmt_r(r1)} and {_fmt_r(r2)} separately in Analysis of Receipts, underline {_fmt_r(r2)}, and record one combined deposit of {_fmt_r(bank_day)} in the Bank column."
    distractors = [
        f"Enter {_fmt_r(r1)} and {_fmt_r(r2)} directly into the Bank column on two separate lines and leave Analysis of Receipts blank.",
        f"Record only {_fmt_r(bank_day)} in Analysis of Receipts and write {_fmt_r(r1)} in Bank because Rent Income goes straight to CPJ.",
        f"Bank {_fmt_r(r1)} twice and exclude {_fmt_r(r2)} from Bank so Sales matches Bank.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_18",
        subskill="18_crj_analysis_of_receipts_same_day_banking",
        title="Same-Day Till Receipts & Daily Banking Rule",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The **Analysis of Receipts** column acts as the till tally during the day (`{_fmt_r(r1)}` + `{_fmt_r(r2)}`). "
            f"At day-end, the last entry on that date is underlined and ONE combined deposit total (**{_fmt_r(bank_day)}**) is carried to **Bank** on the last line of that day."
        ),
        hints={
            "tier_1": "Cash collected in the till on the same day is banked in one total deposit at day-end.",
            "tier_2": f"Analysis shows {_fmt_r(r1)} and {_fmt_r(r2)} individually; Bank shows their combined sum ({_fmt_r(bank_day)}) once.",
            "tier_3": correct,
        },
        misconception_tags=["banking_each_till_receipt_separately"],
    )


def arch_19_crj_direct_eft_deposit_bypass_rule(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(15, 75) * 1000
    scenario_item = rng.choice(["additional Capital", "a business bank loan", "tenant Rent Income"])

    prompt = (
        f"A customer or owner transfers **{_fmt_r(amt)}** for **{scenario_item}** directly into **{biz}**'s business bank account via **direct EFT / bank deposit** (the cash never passed through the shop till).\n\n"
        f"Why must **{_fmt_r(amt)}** NOT be entered into the **`Analysis of Receipts`** column of the CRJ?"
    )
    correct = "Because cash deposited directly into the bank skips the till completely; enter it straight into Bank and Sundry Accounts."
    distractors = [
        "Because direct EFT transfers are never recorded in the Cash Receipts Journal and go into the CPJ.",
        "Because Analysis of Receipts is used exclusively for Cost of Sales calculations on trading stock.",
        "Because direct EFT receipts reduce the Bank total instead of increasing it.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_19",
        subskill="19_crj_direct_eft_deposit_bypass_rule",
        title="Direct Deposit / EFT Bypass of Analysis Column",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"`Analysis of Receipts` tracks cash received **in the till** awaiting banking. "
            f"A direct EFT or bank-counter deposit of **{_fmt_r(amt)}** is already inside the bank account, so `Analysis of Receipts` stays blank and `{_fmt_r(amt)}` goes straight to **Bank** and **Sundry Accounts**."
        ),
        hints={
            "tier_1": "Ask: Did this money ever sit inside the shop cash register / till?",
            "tier_2": "Direct EFT payments go directly into the bank account, bypassing Analysis of Receipts.",
            "tier_3": correct,
        },
        misconception_tags=["entering_direct_eft_in_analysis_of_receipts"],
    )


def arch_20_crj_cost_of_sales_memorandum_column_rule(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    sales_tot = rng.randint(18, 60) * 500
    cos_tot = int(sales_tot * 100 // 125)
    sundry_tot = rng.randint(10, 40) * 500
    bank_tot = sales_tot + sundry_tot

    prompt = (
        f"At month-end, **{biz}**'s Cash Receipts Journal totals are:\n"
        f"- `Sales`: {_fmt_r(sales_tot)}\n"
        f"- `Cost of Sales`: {_fmt_r(cos_tot)}\n"
        f"- `Sundry Accounts`: {_fmt_r(sundry_tot)}\n\n"
        f"When cross-checking the **Bank** total (**{_fmt_r(bank_tot)}**), why is **Cost of Sales** excluded from `Sales + Sundry Accounts`?"
    )
    correct = "Because Cost of Sales is a non-cash memorandum cost of stock already included in Selling Price (Bank only sums Sales + Sundry Accounts)."
    distractors = [
        "Because Cost of Sales is paid out in cheques and therefore added to the Cash Payments Journal Bank total instead.",
        "Because Cost of Sales is an asset that doubles the cash deposited at the bank every evening.",
        "Because Cost of Sales should actually be subtracted from Bank to find cash banked.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_20",
        subskill="20_crj_cost_of_sales_memorandum_column_rule",
        title="CRJ Cross-Check: Excluding Cost of Sales",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"The CRJ cross-check identity is **`Bank Total = Sales Total + Sundry Accounts Total`** (`{_fmt_r(sales_tot)} + {_fmt_r(sundry_tot)} = {_fmt_r(bank_tot)}`). "
            f"**Cost of Sales** ({_fmt_r(cos_tot)}) is NOT cash received—it merely tracks the cost of stock leaving the storeroom."
        ),
        hints={
            "tier_1": "Compare cash received (Sales + Sundry) against the non-cash cost of stock sold.",
            "tier_2": f"Notice {_fmt_r(sales_tot)} + {_fmt_r(sundry_tot)} = {_fmt_r(bank_tot)}, proving Cost of Sales is excluded.",
            "tier_3": correct,
        },
        misconception_tags=["adding_cost_of_sales_to_bank_total"],
    )


def arch_21_crj_missing_column_cross_check_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    markup = rng.choice([25, 40, 50, 60])
    cos_tot = rng.randint(15, 60) * 200
    sales_tot = cos_tot * (100 + markup) // 100
    sundry_tot = rng.randint(8, 35) * 500
    bank_tot = sales_tot + sundry_tot

    headers = ["CRJ Column Total", "Given / Calculated", "Amount (R)"]
    specs = [
        ("Sales", "given", str(sales_tot), False),
        (f"Cost of Sales (mark-up {markup}% on cost)", "required", str(cos_tot), True),
        ("Sundry Accounts", "given", str(sundry_tot), False),
        ("Bank (Total Cash Receipts)", "required", str(bank_tot), True),
    ]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| CRJ Column Total | Status | Amount (R) |", "| --- | --- | --- |"]

    for i, (col, ctype, val, ed) in enumerate(specs):
        status_txt = "Enter numeric total" if ed else "Given"
        if ed:
            correct_map[f"t0_r{i}_c2"] = val
            if "Cost of Sales" in col:
                cell_hints[f"t0_r{i}_c2"] = f"Calculate Sales × 100 / {100 + markup} without spaces or R."
            else:
                cell_hints[f"t0_r{i}_c2"] = "Sum cash receipt columns ONLY (Sales + Sundry Accounts; EXCLUDE Cost of Sales)."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": col, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": status_txt, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "" if ed else val, "type": ctype, "editable": ed},
        ])
        md_lines.append(f"| {col} | {status_txt} | **{_fmt_r(int(val))}** |" if ed else f"| {col} | {status_txt} | {_fmt_r(int(val))} |")

    prompt = (
        f"Reconcile the month-end Cash Receipts Journal totals for **{biz}** (profit mark-up is **{markup}% on cost**).\n\n"
        f"Complete the missing CRJ column totals in the table below (`Cost of Sales` and `Bank`; enter whole digits without spaces or R)."
    )
    sample = f"Cost of Sales = {cos_tot}; Bank = {bank_tot}"
    worked = (
        f"**CRJ Totals Reconciliation Memorandum** [4 marks]\n\n"
        + "\n".join(md_lines)
        + f"\n\n- `Cost of Sales = {_fmt_r(sales_tot)} × 100/{100 + markup} = {_fmt_r(cos_tot)}`\n"
        + f"- `Bank = Sales + Sundry = {_fmt_r(sales_tot)} + {_fmt_r(sundry_tot)} = {_fmt_r(bank_tot)}` (Cost of Sales excluded)"
    )
    return _build_table(
        rng,
        qid_prefix="g9_cc_21",
        subskill="21_crj_missing_column_cross_check_table",
        title="CRJ Column Totals Cross-Check Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "First compute Cost of Sales from Sales and mark-up %, then remember Bank = Sales + Sundry.",
            "tier_2": f"Cost of Sales = {sales_tot} × 100/{100 + markup}; Bank = {sales_tot} + {sundry_tot}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Cost of Sales = {cos_tot}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Bank = {bank_tot} (excludes Cost of Sales)", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_cost_of_sales_to_bank_total"],
    )


def arch_22_accounting_equation_cash_purchase_of_stock(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    amt = rng.randint(15, 75) * 200

    headers = ["Account Debited", "Account Credited", "Assets (Net Effect)", "Owner's Equity (Effect)", "Liabilities (Effect)"]
    rows = [[
        {"coordinate": "t0_r0_c0", "cell_id": "t0_r0_c0", "value": "", "type": "required", "editable": True},
        {"coordinate": "t0_r0_c1", "cell_id": "t0_r0_c1", "value": "", "type": "required", "editable": True},
        {"coordinate": "t0_r0_c2", "cell_id": "t0_r0_c2", "value": "", "type": "required", "editable": True},
        {"coordinate": "t0_r0_c3", "cell_id": "t0_r0_c3", "value": "", "type": "required", "editable": True},
        {"coordinate": "t0_r0_c4", "cell_id": "t0_r0_c4", "value": "0", "type": "given", "editable": False},
    ]]
    correct_map = {
        "t0_r0_c0": "Trading Stock",
        "t0_r0_c1": "Bank",
        "t0_r0_c2": "0",
        "t0_r0_c3": "0",
    }
    cell_hints = {
        "t0_r0_c0": "Which Asset account increases when stock for resale is purchased? (Trading Stock)",
        "t0_r0_c1": "Which Asset account decreases when a cheque/EFT is paid? (Bank)",
        "t0_r0_c2": f"Trading Stock +{amt} and Bank -{amt} -> net effect on total Assets is 0.",
        "t0_r0_c3": "Buying stock for cash exchanges one Asset for another; Owner's Equity effect is 0.",
    }
    prompt = (
        f"**{biz}** buys trading stock ({sc['item_sold']}) by EFT from **{sc['supplier']}** for **{_fmt_r(amt)}**.\n\n"
        f"Complete the Accounting Equation (`A = OE + L`) table below (`0` for no net change)."
    )
    sample = f"Dr Trading Stock; Cr Bank; Assets net 0 (+{amt}/-{amt}); OE 0; L 0"
    worked = (
        f"**Accounting Equation: Cash Purchase of Trading Stock** [4 marks]\n\n"
        f"| Account Debited | Account Credited | Assets (Net Effect) | Owner's Equity | Liabilities |\n"
        f"| --- | --- | --- | --- | --- |\n"
        f"| **Trading Stock** | **Bank** | **0** (+{_fmt_r(amt)} Stock, -{_fmt_r(amt)} Bank) | **0** | 0 |\n"
    )
    return _build_table(
        rng,
        qid_prefix="g9_cc_22",
        subskill="22_accounting_equation_cash_purchase_of_stock",
        title="Accounting Equation: Cash Purchase of Trading Stock",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Buying inventory for cash swaps one Asset (Bank) for another Asset (Trading Stock).",
            "tier_2": f"Debit Trading Stock, Credit Bank; +{amt} and -{amt} cancel to net 0 on Assets.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Account Debited = Trading Stock", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Account Credited = Bank", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Net Assets = 0", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Owner's Equity = 0", "marks": 1, "editable": True},
        ],
        misconception_tags=["treating_stock_purchase_as_expense"],
    )


def arch_23_accounting_equation_cash_sale_dual_entry(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    markup = rng.choice([25, 40, 50, 60])
    cp = rng.randint(15, 65) * 100
    sp = cp * (100 + markup) // 100
    gp = sp - cp

    headers = ["Leg", "Account Debited", "Account Credited", "Assets (Amount, e.g. +5000 / -4000)", "Owner's Equity (Effect)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "cell_id": "t0_r0_c0", "value": "1. Cash Receipt (SP)", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "cell_id": "t0_r0_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c2", "cell_id": "t0_r0_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c3", "cell_id": "t0_r0_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c4", "cell_id": "t0_r0_c4", "value": f"+{sp}", "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "cell_id": "t0_r1_c0", "value": "2. Stock Cost (CP)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "cell_id": "t0_r1_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c2", "cell_id": "t0_r1_c2", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c3", "cell_id": "t0_r1_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c4", "cell_id": "t0_r1_c4", "value": f"-{cp}", "type": "given", "editable": False},
        ],
    ]
    correct_map = {
        "t0_r0_c1": "Bank",
        "t0_r0_c2": "Sales",
        "t0_r0_c3": f"+{sp}",
        "t0_r1_c1": "Cost of Sales",
        "t0_r1_c2": "Trading Stock",
        "t0_r1_c3": f"-{cp}",
    }
    cell_hints = {
        "t0_r0_c1": "Cash increases Bank (Debit).",
        "t0_r0_c2": "Revenue from selling stock is Sales (Credit).",
        "t0_r0_c3": f"Bank (Asset) increases by +{sp} (no spaces or R).",
        "t0_r1_c1": "Cost of stock sold is an expense: Cost of Sales (Debit).",
        "t0_r1_c2": "Stock leaving the shelves reduces Trading Stock (Credit).",
        "t0_r1_c3": f"Calculate Cost Price = {sp} × 100 / {100 + markup} and enter with minus sign (-{cp}).",
    }
    prompt = (
        f"**{biz}** sells merchandise for **{_fmt_r(sp)} cash** (Cash Register Roll). "
        f"The mark-up is **{markup}% on cost**.\n\n"
        f"Complete both legs of the Cash Sale in the Accounting Equation table below (`+/-` integers without spaces or R)."
    )
    sample = f"Leg 1: Dr Bank, Cr Sales, A +{sp}, OE +{sp}; Leg 2: Dr Cost of Sales, Cr Trading Stock, A -{cp}, OE -{cp} (Net profit +{gp})"
    worked = (
        f"**Accounting Equation: Dual-Entry Cash Sale** [6 marks]\n\n"
        f"| Leg | Account Debited | Account Credited | Assets | Owner's Equity |\n"
        f"| --- | --- | --- | --- | --- |\n"
        f"| 1. Cash Receipt (SP) | **Bank** | **Sales** | **+{sp}** | +{sp} (Income) |\n"
        f"| 2. Stock Cost (CP) | **Cost of Sales** | **Trading Stock** | **-{cp}** | -{cp} (Expense) |\n\n"
        f"- Cost of Sales = `{_fmt_r(sp)} × 100/{100 + markup} = {_fmt_r(cp)}`\n"
        f"- Net Profit (Owner's Equity net change) = `+{_fmt_r(sp)} - {_fmt_r(cp)} = +{_fmt_r(gp)}`"
    )
    return _build_table(
        rng,
        qid_prefix="g9_cc_23",
        subskill="23_accounting_equation_cash_sale_dual_entry",
        title="Accounting Equation: Dual-Entry Cash Sale",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Every cash sale has two double entries: (1) Selling Price received in Bank, and (2) Cost Price leaving Trading Stock.",
            "tier_2": f"Leg 1: Dr Bank / Cr Sales (+{sp}); Leg 2: Dr Cost of Sales / Cr Trading Stock (-{cp}).",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Leg 1 accounts: Bank / Sales", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Leg 1 Assets +{sp}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Leg 2 accounts: Cost of Sales / Trading Stock", "marks": 2, "editable": True},
            {"id": "mp_4", "desc": f"Leg 2 Assets -{cp}", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_cost_of_sales_second_entry"],
    )


def arch_24_accounting_equation_mixed_cpj_expense_and_stock(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    stock_amt = rng.randint(14, 52) * 200
    stat_amt = rng.randint(3, 14) * 50
    tot_amt = stock_amt + stat_amt

    headers = ["Portion", "Account Debited", "Account Credited", "Net Assets Effect", "Owner's Equity Effect"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "cell_id": "t0_r0_c0", "value": f"Stock ({_fmt_r(stock_amt)})", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "cell_id": "t0_r0_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c2", "cell_id": "t0_r0_c2", "value": "Bank", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c3", "cell_id": "t0_r0_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r0_c4", "cell_id": "t0_r0_c4", "value": "0", "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "cell_id": "t0_r1_c0", "value": f"Stationery ({_fmt_r(stat_amt)})", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "cell_id": "t0_r1_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c2", "cell_id": "t0_r1_c2", "value": "Bank", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c3", "cell_id": "t0_r1_c3", "value": "", "type": "required", "editable": True},
            {"coordinate": "t0_r1_c4", "cell_id": "t0_r1_c4", "value": "", "type": "required", "editable": True},
        ],
    ]
    correct_map = {
        "t0_r0_c1": "Trading Stock",
        "t0_r0_c3": "0",
        "t0_r1_c1": "Stationery",
        "t0_r1_c3": f"-{stat_amt}",
        "t0_r1_c4": f"-{stat_amt}",
    }
    cell_hints = {
        "t0_r0_c1": "Stock bought for resale goes to Trading Stock.",
        "t0_r0_c3": f"+{stock_amt} Stock and -{stock_amt} Bank cancel out to 0.",
        "t0_r1_c1": "Office consumables are debited to Stationery.",
        "t0_r1_c3": f"Bank decreases by -{stat_amt} on the stationery portion.",
        "t0_r1_c4": f"Stationery expense decreases Owner's Equity by -{stat_amt}.",
    }
    prompt = (
        f"**{biz}** issues one EFT for **{_fmt_r(tot_amt)}** to **{sc['supplier']}** for **Trading Stock ({_fmt_r(stock_amt)})** "
        f"and **Stationery ({_fmt_r(stat_amt)})**.\n\n"
        f"Complete the Accounting Equation table below (`0` for no net change; include `-` sign for decreases without spaces or R)."
    )
    sample = f"Stock: Dr Trading Stock / Cr Bank (Net A 0, OE 0); Stationery: Dr Stationery / Cr Bank (A -{stat_amt}, OE -{stat_amt})"
    worked = (
        f"**Accounting Equation: Mixed CPJ Payment** [5 marks]\n\n"
        f"| Portion | Account Debited | Account Credited | Net Assets Effect | Owner's Equity Effect |\n"
        f"| --- | --- | --- | --- | --- |\n"
        f"| Stock ({_fmt_r(stock_amt)}) | **Trading Stock** | Bank | **0** | 0 |\n"
        f"| Stationery ({_fmt_r(stat_amt)}) | **Stationery** | Bank | **-{stat_amt}** | **-{stat_amt}** |\n"
    )
    return _build_table(
        rng,
        qid_prefix="g9_cc_24",
        subskill="24_accounting_equation_mixed_cpj_expense_and_stock",
        title="Accounting Equation: Split Stock & Stationery Cheque",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=5,
        hints={
            "tier_1": "Split the single cheque into two effects: Asset-for-Asset on stock (net 0) and Expense reducing Bank and OE on stationery.",
            "tier_2": f"Trading Stock swaps +{stock_amt}/-{stock_amt} = 0; Stationery causes A -{stat_amt} and OE -{stat_amt}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Row 1: Trading Stock, Net Assets 0", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Row 2: Stationery, A -{stat_amt}, OE -{stat_amt}", "marks": 3, "editable": True},
        ],
        misconception_tags=["lumping_stationery_into_trading_stock"],
    )


def arch_25_stock_control_and_continuous_inventory_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = _trader_name(rng, sc)
    cases = [
        (
            "why recording Cost of Sales at every sale enables continuous stock control",
            "It lets the owner compare theoretical stock remaining against physical stock counts to detect theft, shrinkage, and optimal reorder levels early.",
            [
                "It eliminates the need to issue duplicate receipts or bank daily cash takings.",
                "It automatically doubles the business's mark-up percentage without changing selling prices.",
                "It allows employees to draw personal goods without recording Drawings or Cost of Sales.",
            ],
        ),
        (
            "which risk occurs if a sole trader fails to maintain proper stock control alongside its CRJ and CPJ",
            "Undetected shoplifting/damage, sudden stock-outs of fast-moving lines, or over-capitalising cash in slow-moving items.",
            [
                "The Bank column total in the CRJ becomes equal to total Drawings.",
                "Fixed assets like Vehicles are automatically reclassified as Stationery.",
                "The business is legally prevented from preparing a monthly Trial Balance.",
            ],
        ),
        (
            "how the CRJ and CPJ work together to compute theoretical Trading Stock on hand before a physical stocktake",
            "Opening Stock + CPJ Trading Stock purchases minus CRJ Cost of Sales gives the expected closing stock balance.",
            [
                "CRJ Sales total + CPJ Wages total minus CRJ Sundry Accounts gives expected closing stock.",
                "CPJ Bank total minus CRJ Bank total directly measures physical stock units on the shelves.",
                "Cost of Sales is added to Opening Stock and Sales is subtracted from Bank.",
            ],
        ),
    ]
    focus, correct, distractors = rng.choice(cases)
    prompt = (
        f"**{biz}** in {sc['area']} sells high-turnover {sc['item_sold']}.\n\n"
        f"Explain {focus}:"
    )
    return _build_mcq(
        rng,
        qid_prefix="g9_cc_25",
        subskill="25_stock_control_and_continuous_inventory_purpose",
        title="Stock Control & Continuous Inventory System",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Continuous stock control (`Opening Stock + Purchases [CPJ] - Cost of Sales [CRJ] = Closing Stock`) tracks inventory continuously. "
            f"**{correct}**"
        ),
        hints={
            "tier_1": "Think of how a trading shop knows what inventory SHOULD be on the shelves without closing for a week.",
            "tier_2": "CPJ records stock coming in at cost price; CRJ Cost of Sales records stock going out at cost price.",
            "tier_3": correct,
        },
        misconception_tags=["stock_control_purpose_confusion"],
    )


BUILDERS_01_25 = {
    "01_service_vs_trading_business_comparison": arch_01_service_vs_trading_business_comparison,
    "02_what_i_want_what_i_have_markup_framework": arch_02_what_i_want_what_i_have_markup_framework,
    "03_selling_price_from_cost_and_markup": arch_03_selling_price_from_cost_and_markup,
    "04_cost_of_sales_from_selling_price_and_markup": arch_04_cost_of_sales_from_selling_price_and_markup,
    "05_profit_amount_from_selling_price_and_markup": arch_05_profit_amount_from_selling_price_and_markup,
    "06_markup_percentage_from_sales_and_cost": arch_06_markup_percentage_from_sales_and_cost,
    "07_implied_markup_ratio_applied_to_new_sale": arch_07_implied_markup_ratio_applied_to_new_sale,
    "08_implied_markup_applied_to_new_cost_price": arch_08_implied_markup_applied_to_new_cost_price,
    "09_gross_profit_vs_cash_discount_received": arch_09_gross_profit_vs_cash_discount_received,
    "10_capital_increase_percentage_backward_calc": arch_10_capital_increase_percentage_backward_calc,
    "11_capital_topup_crj_entry_from_trial_balance": arch_11_capital_topup_crj_entry_from_trial_balance,
    "12_annual_rent_to_monthly_crj_or_cpj": arch_12_annual_rent_to_monthly_crj_or_cpj,
    "13_mixed_payment_cheque_split_drawings": arch_13_mixed_payment_cheque_split_drawings,
    "14_split_consumables_stationery_and_packing_calc": arch_14_split_consumables_stationery_and_packing_calc,
    "15_source_document_classification_crj_vs_cpj_table": arch_15_source_document_classification_crj_vs_cpj_table,
    "16_visual_duplicate_receipt_interpretation": arch_16_visual_duplicate_receipt_interpretation,
    "17_visual_cash_register_roll_crj_extraction": arch_17_visual_cash_register_roll_crj_extraction,
    "18_crj_analysis_of_receipts_same_day_banking": arch_18_crj_analysis_of_receipts_same_day_banking,
    "19_crj_direct_eft_deposit_bypass_rule": arch_19_crj_direct_eft_deposit_bypass_rule,
    "20_crj_cost_of_sales_memorandum_column_rule": arch_20_crj_cost_of_sales_memorandum_column_rule,
    "21_crj_missing_column_cross_check_table": arch_21_crj_missing_column_cross_check_table,
    "22_accounting_equation_cash_purchase_of_stock": arch_22_accounting_equation_cash_purchase_of_stock,
    "23_accounting_equation_cash_sale_dual_entry": arch_23_accounting_equation_cash_sale_dual_entry,
    "24_accounting_equation_mixed_cpj_expense_and_stock": arch_24_accounting_equation_mixed_cpj_expense_and_stock,
    "25_stock_control_and_continuous_inventory_purpose": arch_25_stock_control_and_continuous_inventory_purpose,
}
