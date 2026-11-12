"""
Grade 7 EMS — Term 1: Businesses — Semantic Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md
and curriculum_docs/EMS_Gr7/Term 1/4-Businesses.md.
"""
from __future__ import annotations

import html
import random
from typing import Any, Callable, Dict, List, Optional

from ..ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

TOPIC_NAME = "Businesses"
SUBJECT_NAME = "Economic and Management Sciences"
GRADE_NUM = 7
TERM_NUM = 1
CAPS_WEIGHT = 25


def _pick_person(rng: random.Random) -> str:
    return rng.choice(NAMES)


def _pick_two_people(rng: random.Random) -> tuple[str, str]:
    a, b = rng.sample(NAMES, 2)
    return a, b


def _pick_place(rng: random.Random, rural: bool = False) -> str:
    pool = RURAL_AREAS if rural else URBAN_AREAS
    return rng.choice(pool or AREAS)


def _escape(val: Any) -> str:
    return html.escape(str(val), quote=True)


def _fmt_rand(amount: int) -> str:
    s = f"{amount:,}".replace(",", " ")
    return f"R{s}"


def _q(
    rng: random.Random,
    subskill: str,
    prompt: str,
    correct_answer: str,
    worked_solution: str,
    explanation: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marking_points: List[Dict[str, Any]],
    question_type: str = "short_answer",
    difficulty: str = "medium",
    cognitive_level: str = "Knowledge",
    marks: Optional[int] = None,
    duration: int = 3,
    sample_answer: Optional[str] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    total_marks = marks if marks is not None else sum(int(p.get("marks", 1)) for p in marking_points)
    total_marks = max(1, total_marks)
    sample = sample_answer or correct_answer
    item: Dict[str, Any] = {
        "question_id": f"g7_ems_biz_{subskill}_{rng.randint(10000, 99999)}",
        "archetype_id": subskill,
        "subskill": subskill,
        "topic": TOPIC_NAME,
        "subject": SUBJECT_NAME,
        "grade": GRADE_NUM,
        "term": TERM_NUM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": duration,
        "difficulty": difficulty,
        "cognitive_level": cognitive_level,
        "question_type": question_type,
        "modality": extra.get("modality", "text") if extra else "text",
        "solution_type": extra.get("solution_type", question_type) if extra else question_type,
        "prompt": prompt,
        "question_text": prompt,
        "marks": total_marks,
        "correct_answer": correct_answer,
        "sample_answer": sample,
        "worked_solution": worked_solution,
        "canonical_solution": worked_solution,
        "explanation": explanation,
        "hints": hints,
        "misconception_tags": misconception_tags,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": marking_points,
            "carry_forward_rule": "Award method and reasoning marks where steps are logically justified.",
        },
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    if extra:
        item.update(extra)
    return item


def _mcq(
    rng: random.Random,
    subskill: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    why_correct: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    difficulty: str = "easy",
    cognitive_level: str = "Knowledge",
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + list(distractors[:3])
    rng.shuffle(options)
    idx = options.index(correct)
    letter = "ABCD"[idx]
    worked = f"({letter}) **{correct}** [{marks}]\n\n{why_correct}"
    points = [{"criterion": f"Select option ({letter}): {correct}", "marks": marks}]
    return _q(
        rng=rng,
        subskill=subskill,
        prompt=prompt,
        correct_answer=correct,
        sample_answer=f"({letter}) {correct}",
        worked_solution=worked,
        explanation=why_correct,
        hints=hints,
        misconception_tags=misconception_tags,
        marking_points=points,
        question_type="mcq",
        difficulty=difficulty,
        cognitive_level=cognitive_level,
        marks=marks,
        duration=2,
        diagram_spec=diagram_spec,
        extra={
            "modality": "mcq",
            "solution_type": "mcq",
            "options": options,
            "correct_option": letter,
            "correct_option_index": idx,
        },
    )


def _table_q(
    rng: random.Random,
    subskill: str,
    prompt: str,
    headers: List[str],
    row_specs: List[Dict[str, Any]],
    summary_note: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    difficulty: str = "medium",
    cognitive_level: str = "Routine Procedures",
    diagram_spec: Optional[Dict[str, Any]] = None,
    shuffle_rows: bool = True,
) -> Dict[str, Any]:
    specs = list(row_specs)
    if shuffle_rows:
        rng.shuffle(specs)
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_rows: List[str] = []
    marking_points: List[Dict[str, Any]] = []
    summary_pairs: List[str] = []

    for r_idx, spec in enumerate(specs):
        row_cells: List[Dict[str, Any]] = []
        md_cells: List[str] = []
        exp_iter = iter(spec["expected"])
        hint_iter = iter(spec["cell_hints"])
        for c_idx, val in enumerate(spec["cells"]):
            cid = f"r{r_idx}_c{c_idx}"
            if val is None:
                exp_val = str(next(exp_iter))
                row_cells.append({"cell_id": cid, "value": "", "expected": exp_val, "editable": True})
                correct_map[cid] = exp_val
                cell_hints[cid] = str(next(hint_iter))
                md_cells.append(f"**{exp_val}**")
                marking_points.append({"criterion": f"Row {r_idx + 1} ({spec['cells'][0]}): {exp_val}", "marks": 1})
                summary_pairs.append(f"{spec['cells'][0]} -> {exp_val}")
            else:
                row_cells.append({"cell_id": cid, "value": str(val), "editable": False})
                md_cells.append(str(val))
        rows.append(row_cells)
        md_rows.append("| " + " | ".join(md_cells) + " |")

    md_header = "| " + " | ".join(headers) + " |\n| " + " | ".join(["---"] * len(headers)) + " |"
    md_table = md_header + "\n" + "\n".join(md_rows)
    worked = f"**Completed Memorandum Table**\n\n{md_table}\n\n{summary_note}"
    correct_summary = "; ".join(summary_pairs)
    return _q(
        rng=rng,
        subskill=subskill,
        prompt=prompt,
        correct_answer=correct_summary,
        sample_answer=correct_summary,
        worked_solution=worked,
        explanation=summary_note,
        hints=hints,
        misconception_tags=misconception_tags,
        marking_points=marking_points,
        question_type="journal",
        difficulty=difficulty,
        cognitive_level=cognitive_level,
        marks=len(correct_map),
        duration=4,
        diagram_spec=diagram_spec,
        extra={
            "modality": "ledger",
            "solution_type": "tabular_cells",
            "headers": headers,
            "rows": rows,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _svg_wrap(width: int, height: int, title: str, body: str) -> Dict[str, Any]:
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="{_escape(title)}">'
        f'<rect width="{width}" height="{height}" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
        f'<text x="{width // 2}" y="28" text-anchor="middle" font-family="Arial, sans-serif" '
        f'font-size="15" font-weight="bold" fill="#0f172a">{_escape(title)}</text>'
        f'{body}</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_bars(title: str, bars: List[tuple[str, int, str]], unit_prefix: str = "R", unit_suffix: str = "") -> Dict[str, Any]:
    max_val = max(1, max(v for _, v, _ in bars))
    parts: List[str] = []
    for idx, (label, val, color) in enumerate(bars):
        y = 54 + idx * 36
        bar_w = max(24, int(290 * val / max_val))
        val_txt = f"{_fmt_rand(val)}" if unit_prefix == "R" else f"{unit_prefix}{val}{unit_suffix}"
        parts.append(f'<text x="24" y="{y + 18}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">{_escape(label)}</text>')
        parts.append(f'<rect x="230" y="{y + 2}" width="{bar_w}" height="22" rx="4" fill="{color}"/>')
        parts.append(f'<text x="{238 + bar_w}" y="{y + 18}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">{_escape(val_txt)}</text>')
    return _svg_wrap(640, 68 + len(bars) * 36, title, "".join(parts))


def _svg_matrix_sectors(town: str, formal_ex: tuple[str, str, str], informal_ex: tuple[str, str, str]) -> Dict[str, Any]:
    body = (
        f'<rect x="24" y="48" width="286" height="148" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="167" y="74" text-anchor="middle" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#1e3a8a">Formal Sector (Registered)</text>'
        f'<text x="42" y="102" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">Trading: {_escape(formal_ex[0])}</text>'
        f'<text x="42" y="130" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">Manufacturing: {_escape(formal_ex[1])}</text>'
        f'<text x="42" y="158" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">Service: {_escape(formal_ex[2])}</text>'
        f'<rect x="330" y="48" width="286" height="148" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="473" y="74" text-anchor="middle" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#854d0e">Informal Sector (Unregistered)</text>'
        f'<text x="348" y="102" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">Trading: {_escape(informal_ex[0])}</text>'
        f'<text x="348" y="130" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">Manufacturing: {_escape(informal_ex[1])}</text>'
        f'<text x="348" y="158" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">Service: {_escape(informal_ex[2])}</text>'
    )
    return _svg_wrap(640, 214, f"{town} Business Sector Matrix", body)


def _svg_three_boxes(title: str, boxes: List[tuple[str, str, str]]) -> Dict[str, Any]:
    fills = ["#fee2e2", "#fef3c7", "#dbeafe"]
    strokes = ["#dc2626", "#d97706", "#2563eb"]
    parts: List[str] = []
    for idx, (head, line1, line2) in enumerate(boxes):
        x = 24 + idx * 204
        parts.append(f'<rect x="{x}" y="52" width="180" height="96" rx="8" fill="{fills[idx]}" stroke="{strokes[idx]}" stroke-width="2"/>')
        parts.append(f'<text x="{x + 90}" y="78" text-anchor="middle" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#0f172a">{_escape(head)}</text>')
        parts.append(f'<text x="{x + 90}" y="102" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" fill="#334155">{_escape(line1)}</text>')
        parts.append(f'<text x="{x + 90}" y="124" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#1e293b">{_escape(line2)}</text>')
        if idx < 2:
            parts.append(f'<line x1="{x + 180}" y1="100" x2="{x + 202}" y2="100" stroke="#475569" stroke-width="2"/>')
    return _svg_wrap(640, 168, title, "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 01 – 25
# ---------------------------------------------------------------------------

def _b01(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    city = _pick_place(rng, rural=False)
    firm = rng.choice(["a licensed hardware store chain", "a registered pharmaceutical wholesaler", "a taxed civil engineering company"])
    prompt = (
        f"In {city}, {owner} registers {firm} with CIPC, keeps formal financial books, pays SARS taxes, and follows "
        f"labour regulations. Which sector of business does this belong to?"
    )
    return _mcq(
        rng,
        "01_formal_business_definition",
        prompt,
        "Formal business",
        ["Informal business", "Traditional barter exchange", "Unregistered subsistence stall"],
        "A formal business is officially registered, regulated by labour and health laws, keeps accounting records, and pays income/VAT taxes to SARS.",
        {
            "tier_1": "Check whether this business is registered with government and pays formal taxes.",
            "tier_2": "Registered, taxed, and regulated firms sit inside the formal sector.",
            "tier_3": "Select 'Formal business'.",
        },
        ["confuses_formal_registration_with_informal_trading"],
    )


def _b02(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    stall = rng.choice(["a roadside fruit table outside a taxi rank", "a backyard hair-braiding veranda", "an unregistered weekend car-guard vest service"])
    prompt = (
        f"Outside {town}, {trader} operates {stall} for cash earnings without municipal trading permits, formal tax returns, "
        f"or registered staff contracts. How is {trader}'s business classified?"
    )
    return _mcq(
        rng,
        "02_informal_business_definition",
        prompt,
        "Informal business",
        ["Listed public corporation", "Formal regulated supermarket", "State-owned national utility"],
        "Informal businesses operate legally or semi-legally outside formal tax registration, commercial licensing, and government monitoring.",
        {
            "tier_1": "Notice there are no municipal trading licences, tax filings, or formal registrations.",
            "tier_2": "Micro-enterprises outside tax and business registration belong to the unregistered sector.",
            "tier_3": "Choose 'Informal business'.",
        },
        ["assumes_small_formal_shops_are_informal"],
    )


def _b03(rng: random.Random) -> Dict[str, Any]:
    city = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each South African business operating in {city} as either **Formal Business** or **Informal Business**."
    )
    pool = [
        {"cells": ["National clothing retail chain registered for VAT and PAYE", None], "expected": ["Formal Business"], "cell_hints": ["Pays SARS taxes and operates registered branches."]},
        {"cells": ["Pavement vendor selling loose oranges without a licence or tax number", None], "expected": ["Informal Business"], "cell_hints": ["Unregistered micro-trader operating in cash."]},
        {"cells": ["Unregistered weekend car wash using buckets at a taxi rank", None], "expected": ["Informal Business"], "cell_hints": ["Not registered with CIPC or SARS."]},
        {"cells": ["Licensed dental surgery employing salaried hygienists", None], "expected": ["Formal Business"], "cell_hints": ["Regulated professional clinic with formal employment contracts."]},
        {"cells": ["Commercial bread factory inspected for HACCP food safety", None], "expected": ["Formal Business"], "cell_hints": ["Subject to official municipal/national health monitoring."]},
        {"cells": ["Home-based dressmaker mending skirts for cash without formal books", None], "expected": ["Informal Business"], "cell_hints": ["Micro-business outside formal accounting and tax registration."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "03_formal_vs_informal_classification_table",
        prompt,
        ["Business Example", "Sector (Formal Business / Informal Business)"],
        chosen,
        "Formal businesses are registered, taxed, and monitored; informal businesses are unregistered cash micro-enterprises.",
        {
            "tier_1": "Test each row for registration, SARS taxes, and formal regulation.",
            "tier_2": "Retail chains, dental clinics, and HACCP factories are Formal; pavement vendors, rank car washes, and unregistered home tailors are Informal.",
            "tier_3": "Enter 'Formal Business' or 'Informal Business'.",
        },
        ["classifies_any_small_shop_as_informal"],
    )


def _b04(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    goods = rng.choice(["tinned food, soap, and prepaid airtime", "fresh apples, bottled water, and loaves of bread"])
    prompt = (
        f"{owner} buys {goods} in bulk from a wholesaler and resells them unchanged at a slightly higher markup price "
        f"to neighbourhood shoppers. Which business type is {owner} operating?"
    )
    return _mcq(
        rng,
        "04_trading_business_model",
        prompt,
        "Trading business",
        ["Manufacturing business", "Primary mining enterprise", "Intangible advisory firm"],
        "Trading (retail/wholesale) businesses buy finished products and sell them directly onward at a profit markup without manufacturing alterations.",
        {
            "tier_1": "Notice {owner} buys finished goods and resells the exact same items unchanged.".format(owner=owner),
            "tier_2": "Distinguish buying-and-reselling from assembling goods or selling pure labour services.",
            "tier_3": "Select 'Trading business'.",
        },
        ["confuses_trading_retail_with_manufacturing"],
    )


def _b05(rng: random.Random) -> Dict[str, Any]:
    maker = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    inputs, output = rng.choice([
        ("steel bars, welding rods, and hinges", "burglar bars and security gates"),
        ("flour, yeast, butter, and sugar", "freshly baked loaves and vetkoek"),
        ("pine timber boards, nails, and varnish", "classroom bookshelves and stools"),
    ])
    prompt = (
        f"In {town}, {maker} buys {inputs} and transforms them with tools and labour into {output} for customers. "
        f"Define a **manufacturing business** and explain how it differs from a pure trading business."
    )
    sample = (
        f"A manufacturing business buys raw materials or components ({inputs}) and processes them using labour and machinery "
        f"into new finished products ({output}). Unlike a trading business that simply resells finished stock unchanged, "
        f"a manufacturer physically transforms inputs into a different higher-value product."
    )
    worked = (
        f"1. **Definition [1.5]:** Manufacturing combines raw inputs ({inputs}), tools, and labour to produce new finished goods ({output}).\n"
        f"2. **Difference from trading [1.5]:** Traders resell finished products as bought, whereas {maker} alters raw materials physically."
    )
    return _q(
        rng,
        "05_manufacturing_business_model",
        prompt,
        sample,
        worked,
        "Manufacturing creates new tangible products from raw inputs, distinguishing it from retail trading.",
        {
            "tier_1": f"Focus on what happens to {inputs} inside {maker}'s workshop before customers buy {output}.",
            "tier_2": "Compare physically building new products against simply unpacking boxes to resell.",
            "tier_3": "Define manufacturing and contrast physical transformation of inputs against unchanged resale.",
        },
        ["labels_bakeries_and_welders_purely_as_traders"],
        [
            {"criterion": f"Defines manufacturing using transformation of {inputs} into {output}", "marks": 2},
            {"criterion": "Contrasts physical transformation against unchanged resale in trading", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b06(rng: random.Random) -> Dict[str, Any]:
    provider = _pick_person(rng)
    skill = rng.choice(["repairs burst bathroom geysers and leaks", "cuts and styles customers' hair", "delivers parcels across suburbs by scooter"])
    prompt = (
        f"{provider} earns daily income by selling time, effort, and skill — specifically, {provider} {skill} "
        f"for paying clients rather than selling factory goods on shelves. What type of business is this?"
    )
    return _mcq(
        rng,
        "06_service_business_model",
        prompt,
        "Service business",
        ["Trading business", "Manufacturing factory", "Primary agriculture farm"],
        "A service business earns revenue by performing useful tasks, skills, or professional actions for customers.",
        {
            "tier_1": "Ask whether clients leave with physical stock from a shelf or benefit from skilled work done for them.",
            "tier_2": "Selling skills, repairs, transport, or personal care defines the third main business category.",
            "tier_3": "Choose 'Service business'.",
        },
        ["confuses_plumber_or_salon_with_trading_store"],
    )


def _b07(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Both formal and informal enterprises in {town} operate as trading, manufacturing, or service firms. "
        f"Classify each enterprise into **Trading**, **Manufacturing**, or **Service**."
    )
    pool = [
        {"cells": ["Pavement hawker buying bulk sweets and selling them individually", None], "expected": ["Trading"], "cell_hints": ["Buys finished sweets and resells at markup."]},
        {"cells": ["Informal backyard welder turning scrap steel into security gates", None], "expected": ["Manufacturing"], "cell_hints": ["Transforms metal inputs into finished gates."]},
        {"cells": ["Formal commercial bank processing savings and home loans", None], "expected": ["Service"], "cell_hints": ["Delivers intangible financial services."]},
        {"cells": ["Informal minibus taxi operator driving daily commuters", None], "expected": ["Service"], "cell_hints": ["Provides passenger transport service."]},
        {"cells": ["Registered supermarket chain selling boxed cereal and milk", None], "expected": ["Trading"], "cell_hints": ["Retail buying and reselling of packaged consumer goods."]},
        {"cells": ["Commercial shoe factory turning leather hides into school shoes", None], "expected": ["Manufacturing"], "cell_hints": ["Converts raw materials into finished footwear."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "07_three_business_types_table",
        prompt,
        ["Business Example", "Business Type (Trading / Manufacturing / Service)"],
        chosen,
        "Trading resells finished stock, Manufacturing converts raw materials into goods, and Service businesses sell skills/effort across both formal and informal sectors.",
        {
            "tier_1": "Ignore whether the firm is large or small for a moment and look only at WHAT it sells: resold goods, made goods, or actions.",
            "tier_2": "Sweets hawker & supermarket->Trading; welder & shoe factory->Manufacturing; bank & taxi->Service.",
            "tier_3": "Fill in Trading, Manufacturing, or Service.",
        },
        ["assumes_informal_firms_are_all_trading_stalls"],
    )


def _b08(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    formal_ex = rng.choice([("Supermarket", "Furniture factory", "Private clinic"), ("Pharmacy", "Clothing mill", "Accounting firm")])
    informal_ex = rng.choice([("Street hawker", "Home baker", "Car wash stall"), ("Spaza stall", "Beadwork crafter", "Shoe repairer")])
    diag = _svg_matrix_sectors(town, formal_ex, informal_ex)
    prompt = (
        f"Refer to the matrix diagram for {town} comparing Formal Sector ({formal_ex[0]}, {formal_ex[1]}, {formal_ex[2]}) "
        f"and Informal Sector ({informal_ex[0]}, {informal_ex[1]}, {informal_ex[2]}). Explain TWO key operational "
        f"differences between a formal business and its matching informal counterpart shown in the diagram."
    )
    sample = (
        f"(1) Formal firms like the {formal_ex[0]} register with CIPC/SARS, pay tax, keep formal financial records, and hold "
        f"trading licences, whereas informal operators like the {informal_ex[0]} operate cash-based without formal registration; "
        f"(2) Formal firms face strict labour/safety compliance and pay rent, while informal enterprises operate flexibly with tiny start-up costs."
    )
    worked = (
        f"1. **Registration & tax [1.5]:** Formal examples ({formal_ex[0]}/{formal_ex[1]}) pay SARS tax and keep audited books; informal ({informal_ex[0]}/{informal_ex[1]}) do not.\n"
        f"2. **Capital, premises & rules [1.5]:** Formal firms comply with labour/safety inspections and afford leased premises; informal firms rely on low start-up capital and flexible locations."
    )
    return _q(
        rng,
        "08_formal_informal_sectors_3x2_examples",
        prompt,
        sample,
        worked,
        "Both formal and informal economies cover trading, manufacturing, and services, differing sharply in legal registration, taxation, and scale.",
        {
            "tier_1": "Look left vs right across the two boxes in the diagram.",
            "tier_2": f"Compare how {formal_ex[0]} operates legally and financially versus {informal_ex[0]}.",
            "tier_3": "Contrast tax/CIPC registration + compliance against unregistered low-capital flexible operation.",
        },
        ["claims_informal_sector_has_no_manufacturers_or_service_firms"],
        [
            {"criterion": "Contrasts legal registration, tax compliance, and recordkeeping", "marks": 1},
            {"criterion": f"Contrasts scale, capital access, or premises using diagram examples ({formal_ex[0]} vs {informal_ex[0]})", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b09(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    packs = rng.randint(40, 75)
    buy_p = rng.choice([8, 10])
    sell_p = rng.choice([14, 15, 16])
    profit = packs * (sell_p - buy_p)
    prompt = (
        f"At a commuter rank, {trader}'s trading stall buys {packs} snack packs wholesale at {_fmt_rand(buy_p)} each and "
        f"sells all {packs} packs to commuters at {_fmt_rand(sell_p)} each. Calculate {trader}'s total gross profit in Rands."
    )
    rev = packs * sell_p
    cost = packs * buy_p
    worked = (
        f"1. **Total sales revenue [1]:** {packs} x {_fmt_rand(sell_p)} = {_fmt_rand(rev)}.\n"
        f"2. **Wholesale cost of stock [1]:** {packs} x {_fmt_rand(buy_p)} = {_fmt_rand(cost)}.\n"
        f"3. **Gross profit [1]:** {_fmt_rand(rev)} - {_fmt_rand(cost)} = **{_fmt_rand(profit)}**."
    )
    return _q(
        rng,
        "09_trading_markup_profit_calculation",
        prompt,
        _fmt_rand(profit),
        worked,
        "Trading enterprises earn gross profit from the markup margin between wholesale purchase cost and retail selling price.",
        {
            "tier_1": "Find profit per pack first (selling price - wholesale price) or compute total sales minus total cost.",
            "tier_2": f"Multiply ({sell_p} - {buy_p}) by {packs}.",
            "tier_3": f"Compute {_fmt_rand(rev)} - {_fmt_rand(cost)} = {_fmt_rand(profit)}.",
        },
        ["reports_total_sales_revenue_as_profit"],
        [
            {"criterion": f"Sales revenue = {_fmt_rand(rev)}", "marks": 1},
            {"criterion": f"Wholesale cost = {_fmt_rand(cost)}", "marks": 1},
            {"criterion": f"Gross profit = {_fmt_rand(profit)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b10(rng: random.Random) -> Dict[str, Any]:
    maker = _pick_person(rng)
    prod = rng.choice(["woven baskets", "wooden stools", "hand-sewn school aprons"])
    qty = rng.randint(15, 25)
    mat_cost = rng.choice([650, 800, 950])
    misc_cost = rng.choice([150, 200])
    unit_sell = rng.choice([90, 110, 120])
    sales = qty * unit_sell
    total_cost = mat_cost + misc_cost
    profit = sales - total_cost
    prompt = (
        f"A small manufacturer, {maker}, produces {qty} {prod} using {_fmt_rand(mat_cost)} of raw materials plus "
        f"{_fmt_rand(misc_cost)} for electricity and packaging, then sells all {qty} {prod} at {_fmt_rand(unit_sell)} each. "
        f"Calculate {maker}'s net profit in Rands."
    )
    worked = (
        f"1. **Total sales revenue [1]:** {qty} x {_fmt_rand(unit_sell)} = {_fmt_rand(sales)}.\n"
        f"2. **Total production cost [1]:** {_fmt_rand(mat_cost)} + {_fmt_rand(misc_cost)} = {_fmt_rand(total_cost)}.\n"
        f"3. **Net profit [1]:** {_fmt_rand(sales)} - {_fmt_rand(total_cost)} = **{_fmt_rand(profit)}**."
    )
    return _q(
        rng,
        "10_manufacturing_unit_cost_and_profit",
        prompt,
        _fmt_rand(profit),
        worked,
        "Manufacturers must cover all raw-material, energy, and packaging costs from output sales to stay profitable.",
        {
            "tier_1": "Compute total revenue from selling all units, and add both expense amounts together.",
            "tier_2": f"Subtract total expenses ({_fmt_rand(total_cost)}) from total sales ({_fmt_rand(sales)}).",
            "tier_3": f"Compute {_fmt_rand(sales)} - {_fmt_rand(total_cost)} = {_fmt_rand(profit)}.",
        },
        ["subtracts_only_materials_and_forgets_electricity_cost"],
        [
            {"criterion": f"Sales revenue = {_fmt_rand(sales)}", "marks": 1},
            {"criterion": f"Total cost = {_fmt_rand(total_cost)}", "marks": 1},
            {"criterion": f"Net profit = {_fmt_rand(profit)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b11(rng: random.Random) -> Dict[str, Any]:
    worker = _pick_person(rng)
    service = rng.choice(["washes cars", "repairs smartphone screens", "braids hair"])
    clients = rng.randint(6, 12)
    fee = rng.choice([70, 80, 90])
    supplies = rng.choice([110, 140, 160])
    income = clients * fee
    net = income - supplies
    prompt = (
        f"In an informal service enterprise, {worker} {service} for {clients} clients on Saturday, charging {_fmt_rand(fee)} "
        f"per client. After paying {_fmt_rand(supplies)} for cleaning supplies and taxi transport, how many Rands of net "
        f"take-home income did {worker} earn?"
    )
    worked = (
        f"1. **Gross service fees [1]:** {clients} x {_fmt_rand(fee)} = {_fmt_rand(income)}.\n"
        f"2. **Less daily operating costs [1]:** {_fmt_rand(income)} - {_fmt_rand(supplies)} = **{_fmt_rand(net)}**."
    )
    return _q(
        rng,
        "11_service_business_daily_income",
        prompt,
        _fmt_rand(net),
        worked,
        "Service entrepreneurs calculate net take-home earnings by subtracting transport and consumable supplies from gross client fees.",
        {
            "tier_1": "Multiply the number of clients by the fee charged per client.",
            "tier_2": f"Subtract {_fmt_rand(supplies)} for supplies/transport from gross fees.",
            "tier_3": f"Compute {_fmt_rand(income)} - {_fmt_rand(supplies)} = {_fmt_rand(net)}.",
        },
        ["forgets_to_subtract_transport_and_supply_costs"],
        [
            {"criterion": f"Gross service fees = {_fmt_rand(income)}", "marks": 1},
            {"criterion": f"Net daily income = {_fmt_rand(net)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b12(rng: random.Random) -> Dict[str, Any]:
    founder = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        f"{founder} considers registering a growing catering business in {town} as a formal enterprise. "
        f"Explain THREE major business advantages that operating in the **formal sector** unlocks."
    )
    sample = (
        "(1) Easier access to commercial bank loans and investor finance using audited books and tax records; "
        "(2) ability to bid for corporate and government supply tenders requiring tax-clearance certificates; and "
        "(3) legal protection, brand credibility, and permanent premises supporting long-term expansion."
    )
    worked = (
        "1. **Bank & credit access [1]:** Formal statements and CIPC registration qualify for expansion loans.\n"
        "2. **Corporate & public tenders [1]:** Eligible to supply large companies, schools, and municipalities.\n"
        "3. **Legal protection & credibility [1]:** Enforceable contracts, customer trust, and insurable assets."
    )
    return _q(
        rng,
        "12_formal_sector_advantages_scale",
        prompt,
        sample,
        worked,
        "Formal status creates credibility, contract enforcement, tender eligibility, and access to bank capital.",
        {
            "tier_1": "Think about finance, big corporate/government contracts, and legal safety.",
            "tier_2": "Ask what a registered firm with audited accounts can obtain that an unregistered street stall cannot.",
            "tier_3": "State bank loans, tender eligibility, and legal protection/brand trust.",
        },
        ["thinks_formalisation_only_adds_tax_costs_with_zero_benefits"],
        [
            {"criterion": "Advantage 1: Access to bank loans and investor finance", "marks": 1},
            {"criterion": "Advantage 2: Eligibility for corporate/government contracts and tenders", "marks": 1},
            {"criterion": "Advantage 3: Legal protection, insurance, and customer brand credibility", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b13(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    city = _pick_place(rng, rural=False)
    prompt = (
        f"Despite its strengths, formal registration in {city} creates real challenges for small entrepreneurs like {owner}. "
        f"Which statement accurately describes a **disadvantage** of operating a formal business?"
    )
    return _mcq(
        rng,
        "13_formal_sector_disadvantages_compliance",
        prompt,
        "Higher start-up costs, regular accounting fees, SARS tax payments, and strict regulatory paperwork",
        [
            "Total exclusion from opening commercial business bank accounts",
            "Inability to advertise products on legal street signboards",
            "Prohibition against hiring trained permanent staff on written contracts",
        ],
        "Formal businesses bear heavier compliance expenses — CIPC fees, bookkeeping, SARS income/VAT taxes, municipal licences, and labour administration.",
        {
            "tier_1": "Look for costs, taxes, and administrative paperwork burdens that informal traders avoid.",
            "tier_2": "Eliminate claims saying formal firms cannot open bank accounts or hire staff.",
            "tier_3": "Select the option noting compliance costs, taxes, and regulatory paperwork.",
        },
        ["confuses_informal_barriers_with_formal_disadvantages"],
    )


def _b14(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    capital = rng.choice([250, 350, 450])
    prompt = (
        f"With only {_fmt_rand(capital)} and no bank loan, {trader} starts an informal spice and vegetable stall near {town}. "
        f"Explain THREE practical advantages of the **informal sector** for people and communities."
    )
    sample = (
        f"(1) Very low start-up capital ({_fmt_rand(capital)}) allows rapid entry with zero CIPC/permit delays; "
        f"(2) creates immediate self-employment income for unemployed households; and "
        f"(3) breaks bulk into affordable small quantities at flexible hours close to commuters."
    )
    worked = (
        f"1. **Low entry barriers [1]:** Needs tiny start-up cash ({_fmt_rand(capital)}) and no lengthy registration paperwork.\n"
        f"2. **Job & survival income [1]:** Generates quick cash earnings during unemployment.\n"
        f"3. **Convenience & affordability [1]:** Serves low-income commuters in flexible hours and small unit packs in {town}."
    )
    return _q(
        rng,
        "14_informal_sector_advantages_flexibility",
        prompt,
        sample,
        worked,
        "Informal micro-enterprises cushion unemployment and serve local commuters conveniently with tiny capital.",
        {
            "tier_1": "Consider both the entrepreneur (cost/speed/income) and local shoppers (convenience/small packs).",
            "tier_2": f"Mention starting quickly with {_fmt_rand(capital)}, survival jobs, and flexible local hours.",
            "tier_3": "State low start-up cost/no red tape, self-employment income, and convenient broken-bulk local access.",
        },
        ["assumes_informal_sector_contributes_no_community_value"],
        [
            {"criterion": f"Low start-up capital ({_fmt_rand(capital)}) / fast entry without red tape", "marks": 1},
            {"criterion": "Creates immediate self-employment / household income", "marks": 1},
            {"criterion": "Convenient flexible hours / affordable small quantities for commuters", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b15(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        f"{trader} runs an unregistered pavement shoe-repair and snack stall in {town}. "
        f"Explain THREE serious **disadvantages or risks** faced by informal business owners like {trader}."
    )
    sample = (
        "(1) Inability to obtain commercial bank loans for growth due to lacking registration and financial records; "
        "(2) no legal protection, business insurance, or secure permanent shelter against rain, theft, or municipal eviction; and "
        "(3) unstable daily income with zero paid sick leave, UIF, or pension benefits."
    )
    worked = (
        "1. **No formal bank credit [1]:** Lacks collateral, tax clearance, and bookkeeping to borrow expansion funds.\n"
        "2. **High vulnerability & zero insurance [1]:** Exposed to bad weather, stock theft, and bylaw confiscations without insurance.\n"
        "3. **No social safety net [1]:** No paid sick leave, medical aid, or retirement security if unable to trade."
    )
    return _q(
        rng,
        "15_informal_sector_disadvantages_risks",
        prompt,
        sample,
        worked,
        "Informal traders face acute credit exclusion, physical/weather vulnerability, and zero formal income protection.",
        {
            "tier_1": "Think of money growth barriers, street exposure/theft risks, and personal illness/benefit gaps.",
            "tier_2": "Recall why banks refuse loans, what rain/theft does to uninsured stalls, and what happens during illness.",
            "tier_3": "Explain lack of bank credit, uninsured weather/theft risk, and absence of sick leave/UIF/pension.",
        },
        ["only_lists_small_income_without_credit_or_safety_net"],
        [
            {"criterion": "Credit exclusion (cannot easily get commercial bank loans)", "marks": 1},
            {"criterion": "Exposure to weather, theft, or bylaw risk without insurance", "marks": 1},
            {"criterion": "No UIF, paid sick leave, or pension benefits", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b16(rng: random.Random) -> Dict[str, Any]:
    inf_pct = rng.choice([68, 70, 72])
    dev_pct = rng.choice([12, 14, 16])
    workforce = rng.choice([10000, 15000, 20000])
    inf_workers = (workforce * inf_pct) // 100
    diag = _svg_bars(
        f"Informal Workforce Share (% of {workforce} Sample Workers)",
        [
            ("Developing Economy (Informal %)", inf_pct, "#d97706"),
            ("Developed Economy (Informal %)", dev_pct, "#2563eb"),
        ],
        unit_prefix="",
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the diagram comparing informal employment shares: {inf_pct}% in a typical developing economy "
        f"(out of {workforce} surveyed town workers) versus {dev_pct}% in a developed economy. "
        f"Calculate how many workers in the developing town work in the informal sector, and explain ONE reason why "
        f"developing economies have a much larger informal sector."
    )
    worked = (
        f"1. **Informal workers count [1]:** {inf_pct}% of {workforce} = **{_escape(f'{inf_workers}')}** workers.\n"
        f"2. **Economic reason [2]:** Slower formal industrial job creation, limited start-up capital, or lower formal education/compliance access pushes unemployed households into informal survival trading."
    )
    return _q(
        rng,
        "16_developing_country_informal_share",
        prompt,
        f"{inf_workers} workers",
        worked,
        "In many developing cities roughly 70% of livelihoods sit in the informal economy because formal factory and corporate jobs cannot absorb all job seekers.",
        {
            "tier_1": f"Multiply {workforce} by {inf_pct}% first, then explain why fewer formal jobs exist.",
            "tier_2": "Compute the worker count, then point to scarce formal jobs or limited capital/compliance access.",
            "tier_3": f"State {inf_workers} workers and explain structural shortage of formal wage jobs / low barriers to informal survival trade.",
        },
        ["calculates_developed_city_percentage_instead"],
        [
            {"criterion": f"Calculates informal workers = {inf_workers}", "marks": 1},
            {"criterion": "Explains formal job scarcity / low barriers / limited capital in developing economies", "marks": 2},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b17(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    loan_amt = rng.choice([25000, 40000, 60000])
    prompt = (
        f"{trader} runs a busy unregistered backyard baking stall and asks a commercial bank for a {_fmt_rand(loan_amt)} "
        f"oven-expansion loan, but the application is declined. State TWO reasons why banks view unregistered informal "
        f"businesses as high credit risk, and suggest ONE step {trader} could take to improve bank eligibility."
    )
    sample = (
        f"Why declined: (1) No formal financial statements or audited bank turnover proving steady income to repay {_fmt_rand(loan_amt)}; "
        f"(2) no CIPC registration, tax clearance, or fixed property collateral to secure the loan. "
        f"Step forward: Register the business formally, open a dedicated business bank account, and keep monthly income/expense records."
    )
    worked = (
        f"1. **Bank risk reasons [2]:** (a) No audited financial books/bank statements proving repayment capacity for {_fmt_rand(loan_amt)}; (b) No legal registration, tax number, or collateral security.\n"
        f"2. **Improvement step [1]:** Open a dedicated business account, record daily sales/costs systematically, and register with CIPC/SARS (or join a micro-finance group)."
    )
    return _q(
        rng,
        "17_banks_loans_informal_barrier",
        prompt,
        sample,
        worked,
        "Banks lend based on verified cash-flow records, legal standing, and collateral — areas where unregistered cash enterprises lack proof.",
        {
            "tier_1": "Put yourself in a bank manager's shoes evaluating an unrecorded cash business.",
            "tier_2": f"Ask what proof is missing for a {_fmt_rand(loan_amt)} loan, and how {trader} can create a verified paper trail.",
            "tier_3": "Cite missing financial statements and missing registration/collateral, plus opening a business account and registering.",
        },
        ["claims_banks_refuse_loans_simply_because_stalls_are_small"],
        [
            {"criterion": "Risk reason 1: No formal financial statements / verified bank cash-flow", "marks": 1},
            {"criterion": "Risk reason 2: No legal registration, tax certificate, or collateral", "marks": 1},
            {"criterion": "Constructive step: Register formally / separate business account / keep books", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b18(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    policy = rng.choice(["enterprise-development grants and BBBEE supplier programmes", "formal township industrial hubs and preferential procurement"])
    prompt = (
        f"In South African EMS, learners study how past apartheid exclusions pushed many Black entrepreneurs around {town} "
        f"into informal survival trade. Explain how initiatives such as {policy} help bridge informal businesses into the formal economy."
    )
    sample = (
        f"Apartheid laws once barred Black South Africans from owning licensed commercial firms in urban centres, confining "
        f"many to informal trade. Today, {policy} provide training, start-up capital, mentorship, and corporate supply-chain "
        f"access so informal micro-businesses can formalise, hire staff, and grow sustainably."
    )
    worked = (
        f"1. **Historical context [1]:** Past apartheid spatial and licensing barriers excluded majority citizens from formal business ownership.\n"
        f"2. **Bridging role [2]:** {policy.capitalize()} supply skills training, finance, and corporate market links so informal operators in {town} can register and scale into formal suppliers."
    )
    return _q(
        rng,
        "18_apartheid_legacy_and_bbbee_link",
        prompt,
        sample,
        worked,
        "Connecting South Africa's informal micro-businesses to formal corporate supply chains addresses historic exclusion and creates broader growth.",
        {
            "tier_1": "Link historical legal barriers to modern supplier-development support.",
            "tier_2": f"Explain both why exclusion occurred earlier and how {policy} lowers barriers today.",
            "tier_3": "Connect apartheid licensing exclusion with finance, skills, and market procurement support.",
        },
        ["ignores_historical_roots_of_sa_informal_economy"],
        [
            {"criterion": "Explains historical exclusion under apartheid laws", "marks": 1},
            {"criterion": f"Explains how {policy} builds formal capacity and market access", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b19(rng: random.Random) -> Dict[str, Any]:
    director = _pick_person(rng)
    tax_type = rng.choice(["Value-Added Tax (VAT) and company income tax", "Pay-As-You-Earn (PAYE) employee tax and corporate tax"])
    prompt = (
        f"Every year, {director}'s formal manufacturing company submits audited tax returns and pays {tax_type}. "
        f"Which official South African institution collects these taxes to fund public roads, clinics, and schools?"
    )
    return _mcq(
        rng,
        "19_sars_tax_registration_vat_compliance",
        prompt,
        "South African Revenue Service (SARS)",
        ["Informal Street Traders Association", "Private Retail Warehouse Guild", "Commercial Bank Loan Desk"],
        "SARS (South African Revenue Service) is the national tax authority collecting company tax, VAT, and PAYE from formal businesses to fund public services.",
        {
            "tier_1": "Recall the four-letter national revenue agency responsible for collecting taxes across South Africa.",
            "tier_2": "Distinguish the official tax collector from trade unions or commercial banks.",
            "tier_3": "Select 'South African Revenue Service (SARS)'.",
        },
        ["confuses_sars_with_cipc_or_commercial_banks"],
    )


def _b20(rng: random.Random) -> Dict[str, Any]:
    plant = _pick_person(rng)
    food = rng.choice(["canned dairy and yoghurt", "frozen chicken portions", "fresh bakery pies"])
    prompt = (
        f"{plant}'s formal food factory supplies {food} to supermarkets nationwide and must obey strict **HACCP hygiene "
        f"and safety standards**. Explain TWO reasons why government and retailers enforce standards like HACCP on food "
        f"and manufacturing businesses."
    )
    sample = (
        f"(1) Protects consumers from contaminated food ({food}), illness, and injury by controlling hazards across production; "
        f"(2) builds public and export trust, preventing costly recalls, legal fines, or factory closures for {plant}."
    )
    worked = (
        f"1. **Consumer health & safety [1.5]:** Prevents contamination, food poisoning, or unsafe defects in {food}.\n"
        f"2. **Business reputation & compliance [1.5]:** Maintains supermarket/export contracts and avoids shutdowns or legal liability."
    )
    return _q(
        rng,
        "20_haccp_food_and_safety_standards",
        prompt,
        sample,
        worked,
        "Safety and hygiene certifications like HACCP protect public health and preserve formal market access.",
        {
            "tier_1": "Think of both the customer eating the food and the factory's own business contracts.",
            "tier_2": "Consider preventing foodborne illness alongside avoiding recalls and losing supermarket buyers.",
            "tier_3": "State consumer safety protection and maintaining legal compliance/market trust.",
        },
        ["views_hygiene_rules_purely_as_unnecessary_red_tape"],
        [
            {"criterion": f"Protects consumers from contamination/illness from {food}", "marks": 1},
            {"criterion": "Protects brand trust, export/retail eligibility, and legal compliance", "marks": 2},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b21(rng: random.Random) -> Dict[str, Any]:
    firm = _pick_person(rng)
    inputs_r = rng.choice([12000, 18000, 24000])
    sales_r = rng.choice([30000, 38000, 46000])
    diag = _svg_three_boxes(
        f"{firm}'s Bakery: Consumer & Producer Roles",
        [
            ("1. Acts as Consumer", "Buys flour, power & labour", f"Pays {_fmt_rand(inputs_r)}"),
            ("2. Transformation", "Mixes & bakes bread", "Adds value"),
            ("3. Acts as Producer", "Sells fresh loaves", f"Earns {_fmt_rand(sales_r)}"),
        ],
    )
    prompt = (
        f"Refer to the three-stage diagram for {firm}'s Bakery spending {_fmt_rand(inputs_r)} on flour, electricity, "
        f"and labour while selling bread for {_fmt_rand(sales_r)}. Explain how a business is BOTH a **consumer** and a **producer**."
    )
    sample = (
        f"A business acts as a **consumer** when it buys raw materials, utilities, equipment, and worker hours from suppliers "
        f"and households (spending {_fmt_rand(inputs_r)}). It acts as a **producer** when it transforms those inputs into "
        f"finished bread sold to households for {_fmt_rand(sales_r)}."
    )
    worked = (
        f"1. **Business as consumer ({_fmt_rand(inputs_r)}) [1.5]:** Purchases flour, electricity, machinery, and labour from other firms/households.\n"
        f"2. **Business as producer ({_fmt_rand(sales_r)}) [1.5]:** Bakes and supplies finished goods/services to final customers."
    )
    return _q(
        rng,
        "21_business_as_producer_and_consumer",
        prompt,
        sample,
        worked,
        "Just like households, businesses play dual roles: consuming productive inputs on the left and producing market output on the right.",
        {
            "tier_1": "Read Box 1 (inputs bought) and Box 3 (outputs sold) in the diagram.",
            "tier_2": f"Link {_fmt_rand(inputs_r)} to consuming raw/factor inputs, and {_fmt_rand(sales_r)} to producing finished bread.",
            "tier_3": "Explain both buying inputs as a consumer and creating bread for sale as a producer.",
        },
        ["assumes_only_households_can_be_consumers"],
        [
            {"criterion": f"Explains business as consumer buying inputs ({_fmt_rand(inputs_r)})", "marks": 1},
            {"criterion": f"Explains business as producer creating finished output ({_fmt_rand(sales_r)})", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b22(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Match each business attribute in the table to whether it represents a **Formal Advantage**, "
        "**Formal Disadvantage**, **Informal Advantage**, or **Informal Disadvantage**."
    )
    row_specs = [
        {"cells": ["Qualifies for commercial bank loans and large government tenders", None], "expected": ["Formal Advantage"], "cell_hints": ["Benefit unlocked by registration and audited books."]},
        {"cells": ["Bears high tax rates, accounting fees, and complex compliance paperwork", None], "expected": ["Formal Disadvantage"], "cell_hints": ["Extra cost and administrative burden of registration."]},
        {"cells": ["Requires very little start-up money and zero bureaucratic delays", None], "expected": ["Informal Advantage"], "cell_hints": ["Easy fast entry for cash-strapped micro-traders."]},
        {"cells": ["Lacks insurance cover, credit access, and weather-proof premises", None], "expected": ["Informal Disadvantage"], "cell_hints": ["Risk and financing barrier of operating unregistered."]},
    ]
    return _table_q(
        rng,
        "22_formal_vs_informal_advantages_table",
        prompt,
        ["Business Characteristic", "Sector Evaluation"],
        row_specs,
        "Evaluating formal versus informal businesses requires balancing formal scale/finance strengths against red-tape costs, and informal agility against credit/safety risks.",
        {
            "tier_1": "Decide first whether the statement describes a registered or unregistered enterprise, then whether it helps or hurts the owner.",
            "tier_2": "Bank loans->Formal Advantage, high tax/paperwork->Formal Disadvantage, easy cheap start->Informal Advantage, no insurance/credit->Informal Disadvantage.",
            "tier_3": "Use exact labels: Formal Advantage, Formal Disadvantage, Informal Advantage, Informal Disadvantage.",
        },
        ["confuses_informal_advantages_with_formal_advantages"],
    )


def _b23(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    event = rng.choice(["severe river floods, coastal cyclones, and prolonged droughts", "earthquakes, mudslides, and runaway veldfires"])
    prompt = (
        f"Around {town}, businesses face sudden economic shocks caused by {event}. "
        f"How are uncontrollable extreme weather or geological shocks classified in EMS?"
    )
    return _mcq(
        rng,
        "23_natural_disasters_definition_examples",
        prompt,
        "Natural disasters",
        ["Voluntary marketing promotions", "Consumer seasonal fashions", "Internal staff appraisals"],
        "Natural disasters are extreme natural events (floods, droughts, hurricanes, earthquakes, tsunamis) that disrupt production, supply chains, and human safety outside a firm's control.",
        {
            "tier_1": "Notice floods, droughts, and earthquakes are external environmental emergencies.",
            "tier_2": "Distinguish uncontrollable environmental shocks from internal business management choices.",
            "tier_3": "Select 'Natural disasters'.",
        },
        ["blames_floods_on_poor_shop_bookkeeping"],
    )


def _b24(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    owner = _pick_person(rng)
    disaster = rng.choice(["severe seasonal flooding", "a destructive wildfire"])
    prompt = (
        f"After {disaster} hits {town}, {owner}'s retail warehouse and surrounding streets are badly affected. "
        f"Explain THREE specific ways natural disasters harm local businesses."
    )
    sample = (
        f"(1) Physical destruction of stock, buildings, and equipment inside {owner}'s warehouse; "
        f"(2) disrupted electricity, water, and washed-out roads halting deliveries and production; and "
        f"(3) loss of customer income/foot traffic and injured or displaced workers unable to report for duty."
    )
    worked = (
        f"1. **Damaged assets & inventory [1]:** Ruins stock, machinery, and shop premises of {owner}.\n"
        f"2. **Infrastructure & supply disruption [1]:** Power/water outages and damaged roads block suppliers and deliveries.\n"
        f"3. **Worker & customer loss [1]:** Displaced employees miss shifts while affected households cut back normal spending."
    )
    return _q(
        rng,
        "24_five_impacts_of_disasters_on_business",
        prompt,
        sample,
        worked,
        "Natural disasters strike businesses simultaneously across physical assets, utility/transport links, staff availability, and local demand.",
        {
            "tier_1": "Think of three distinct angles: inside the shop, roads/power outside, and workers/customers.",
            "tier_2": f"Relate each angle directly to {town} and {owner}'s warehouse.",
            "tier_3": "Explain stock/building damage, utility/transport breakdowns, and worker absence / lower customer sales.",
        },
        ["only_mentions_broken_windows_missing_supply_and_customer_impacts"],
        [
            {"criterion": "Damage/loss of stock, buildings, or equipment", "marks": 1},
            {"criterion": "Disruption of power, water, or transport supply chains", "marks": 1},
            {"criterion": "Loss of workers / drop in customer demand and revenue", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b25(rng: random.Random) -> Dict[str, Any]:
    port = rng.choice(["Durban container port", "Eastern Cape coastal rail", "overseas electronics hub"])
    drop_pct = rng.choice([40, 50, 60])
    diag = _svg_three_boxes(
        "Supply Chain Ripple After Port Flood",
        [
            ("1. Port / Factory Hit", f"{port}", f"Supply drops {drop_pct}%"),
            ("2. Local Assemblers", "Wait on key parts", "Factory output slows"),
            ("3. SA Retail Stores", "Empty appliance shelves", "Sales & jobs fall"),
        ],
    )
    prompt = (
        f"Refer to the supply-chain diagram showing a flood at {port} cutting component deliveries by {drop_pct}%. "
        f"Trace how one disaster in Stage 1 causes economic losses at BOTH Stage 2 (local assemblers) and Stage 3 (SA retail stores)."
    )
    sample = (
        f"Even without being flooded directly, Stage 2 local assemblers run short of imported parts (down {drop_pct}%), "
        f"forcing production halts and lost shifts. Consequently, Stage 3 South African retail shops face empty shelves, "
        f"fewer sales, higher scarcity prices, and pressure on retail jobs."
    )
    worked = (
        f"1. **Stage 2 assemblers ({drop_pct}% supply drop) [1.5]:** Input shortages halt assembly lines and raise unit costs.\n"
        f"2. **Stage 3 retail stores [1.5]:** Undelivered stock reduces store turnover and threatens retail commissions and wages."
    )
    return _q(
        rng,
        "25_tsunami_flood_supply_chain_ripple",
        prompt,
        sample,
        worked,
        "Modern interconnected supply chains transmit natural-disaster disruptions globally from raw ports to local retail shelves.",
        {
            "tier_1": "Read Boxes 1, 2, and 3 from left to right.",
            "tier_2": f"Explain why a {drop_pct}% component shortage at {port} affects factories and shops kilometres away.",
            "tier_3": "Link input shortage in Stage 2 factories to stockouts and lost sales in Stage 3 retailers.",
        },
        ["thinks_only_flooded_buildings_suffer_financial_losses"],
        [
            {"criterion": f"Explains Stage 2 factory stoppage from {drop_pct}% input drop", "marks": 1},
            {"criterion": "Explains Stage 3 retail stock shortages and lost sales", "marks": 2},
        ],
        cognitive_level="Problem Solving",
        marks=3,
        diagram_spec=diag,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_formal_business_definition": _b01,
    "02_informal_business_definition": _b02,
    "03_formal_vs_informal_classification_table": _b03,
    "04_trading_business_model": _b04,
    "05_manufacturing_business_model": _b05,
    "06_service_business_model": _b06,
    "07_three_business_types_table": _b07,
    "08_formal_informal_sectors_3x2_examples": _b08,
    "09_trading_markup_profit_calculation": _b09,
    "10_manufacturing_unit_cost_and_profit": _b10,
    "11_service_business_daily_income": _b11,
    "12_formal_sector_advantages_scale": _b12,
    "13_formal_sector_disadvantages_compliance": _b13,
    "14_informal_sector_advantages_flexibility": _b14,
    "15_informal_sector_disadvantages_risks": _b15,
    "16_developing_country_informal_share": _b16,
    "17_banks_loans_informal_barrier": _b17,
    "18_apartheid_legacy_and_bbbee_link": _b18,
    "19_sars_tax_registration_vat_compliance": _b19,
    "20_haccp_food_and_safety_standards": _b20,
    "21_business_as_producer_and_consumer": _b21,
    "22_formal_vs_informal_advantages_table": _b22,
    "23_natural_disasters_definition_examples": _b23,
    "24_five_impacts_of_disasters_on_business": _b24,
    "25_tsunami_flood_supply_chain_ripple": _b25,
}
