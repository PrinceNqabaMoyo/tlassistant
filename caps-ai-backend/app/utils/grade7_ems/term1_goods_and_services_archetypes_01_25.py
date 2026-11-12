"""
Grade 7 EMS — Term 1: Goods and Services — Semantic Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 1/03. Goods and Service.md.
"""
from __future__ import annotations

import html
import random
from typing import Any, Callable, Dict, List, Optional

from ..ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

TOPIC_NAME = "Goods and services"
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
        "question_id": f"g7_ems_gs_{subskill}_{rng.randint(10000, 99999)}",
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


def _svg_exchange(title: str, left_h: str, left_s: str, right_h: str, right_s: str, top_a: str, bot_a: str) -> Dict[str, Any]:
    body = (
        f'<rect x="28" y="54" width="210" height="104" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="133" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#1e3a8a">{_escape(left_h)}</text>'
        f'<text x="133" y="114" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#334155">{_escape(left_s)}</text>'
        f'<rect x="402" y="54" width="210" height="104" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="507" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#166534">{_escape(right_h)}</text>'
        f'<text x="507" y="114" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#334155">{_escape(right_s)}</text>'
        f'<line x1="244" y1="86" x2="394" y2="86" stroke="#0f766e" stroke-width="2.5"/>'
        f'<polygon points="396,86 386,80 386,92" fill="#0f766e"/>'
        f'<text x="320" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f766e">{_escape(top_a)}</text>'
        f'<line x1="396" y1="132" x2="246" y2="132" stroke="#b45309" stroke-width="2.5"/>'
        f'<polygon points="244,132 254,126 254,138" fill="#b45309"/>'
        f'<text x="320" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#b45309">{_escape(bot_a)}</text>'
    )
    return _svg_wrap(640, 184, title, body)


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


def _svg_chain_three(title: str, stages: List[tuple[str, str, int]]) -> Dict[str, Any]:
    parts: List[str] = []
    colors = ["#dcfce7", "#dbeafe", "#fef9c3"]
    strokes = ["#16a34a", "#2563eb", "#ca8a04"]
    for idx, (sec, desc, price) in enumerate(stages):
        x = 26 + idx * 204
        parts.append(f'<rect x="{x}" y="54" width="178" height="92" rx="8" fill="{colors[idx]}" stroke="{strokes[idx]}" stroke-width="2"/>')
        parts.append(f'<text x="{x + 89}" y="80" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{_escape(sec)}</text>')
        parts.append(f'<text x="{x + 89}" y="104" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" fill="#334155">{_escape(desc)}</text>')
        parts.append(f'<text x="{x + 89}" y="130" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Price: {_escape(_fmt_rand(price))}</text>')
        if idx < 2:
            parts.append(f'<line x1="{x + 178}" y1="100" x2="{x + 202}" y2="100" stroke="#475569" stroke-width="2.5"/>')
            parts.append(f'<polygon points="{x + 204},100 {x + 195},95 {x + 195},105" fill="#475569"/>')
    return _svg_wrap(640, 170, title, "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 01 – 25
# ---------------------------------------------------------------------------

def _b01(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    good = rng.choice(["a wooden classroom desk and a loaf of bread", "a pair of canvas takkies and bottled juice", "a stainless-steel kettle and wool blanket"])
    prompt = (
        f"{buyer} walks out of a store carrying {good}. Because these items are physical objects that can be seen, "
        f"touched, weighed, and owned, how are they classified in economics?"
    )
    return _mcq(
        rng,
        "01_goods_tangible_definition",
        prompt,
        "Goods",
        ["Intangible services", "Tertiary labour actions", "Electronic skill deliveries"],
        "Goods are tangible physical products that satisfy human needs and wants and can be touched, stored, and transferred in ownership.",
        {
            "tier_1": "Ask whether the items have physical form that you can hold in your hands.",
            "tier_2": "Distinguish tangible physical objects from actions or advice performed for a customer.",
            "tier_3": "Select 'Goods'.",
        },
        ["confuses_physical_goods_with_services"],
    )


def _b02(rng: random.Random) -> Dict[str, Any]:
    client = _pick_person(rng)
    service = rng.choice(["getting a haircut at a salon", "receiving a dental check-up at a clinic", "riding a minibus taxi to school"])
    prompt = (
        f"After {service}, {client} pays the provider for skill, time, and effort without taking home a new physical object. "
        f"What economic term describes {service}?"
    )
    return _mcq(
        rng,
        "02_services_intangible_definition",
        prompt,
        "Services",
        ["Tangible durable goods", "Raw natural commodities", "Manufactured capital machinery"],
        "Services are intangible economic activities or tasks performed by people or firms for consumers, consumed at the moment of delivery.",
        {
            "tier_1": "Notice {client} paid for an action/expertise rather than owning a physical object.".format(client=client),
            "tier_2": "Intangible actions consumed while performed belong outside physical goods.",
            "tier_3": "Choose 'Services'.",
        },
        ["classifies_all_paid_transactions_as_goods"],
    )


def _b03(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each item or activity available in {town} as either **Goods** or **Services** in the table below."
    )
    pool = [
        {"cells": ["2 kg packet of maize meal bought from a grocer", None], "expected": ["Goods"], "cell_hints": ["Tangible physical food item."]},
        {"cells": ["Plumber repairing a burst kitchen pipe at home", None], "expected": ["Services"], "cell_hints": ["Skilled repair work performed by a technician."]},
        {"cells": ["Maths textbook and geometry ruler set", None], "expected": ["Goods"], "cell_hints": ["Physical objects kept by the learner."]},
        {"cells": ["Bus driver transporting commuters from suburb to city centre", None], "expected": ["Services"], "cell_hints": ["Intangible transport action."]},
        {"cells": ["Nurse administering an annual flu vaccination", None], "expected": ["Services"], "cell_hints": ["Healthcare activity delivered by a professional."]},
        {"cells": ["Aluminium cooking pot bought at a hardware store", None], "expected": ["Goods"], "cell_hints": ["Physical kitchenware you can touch and store."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "03_goods_vs_services_classification_table",
        prompt,
        ["Market Offering", "Category (Goods / Services)"],
        chosen,
        "Goods are tangible physical items that can be touched and stored, whereas services are intangible actions performed for customers.",
        {
            "tier_1": "Apply the touch-and-carry-home test to every row.",
            "tier_2": "Maize meal, books, and pots are physical; plumbing repair, bus rides, and vaccinations are actions.",
            "tier_3": "Label each row strictly 'Goods' or 'Services'.",
        },
        ["confuses_goods_and_services_in_everyday_examples"],
    )


def _b04(rng: random.Random) -> Dict[str, Any]:
    harvester = _pick_person(rng)
    raw = rng.choice(["fresh mountain spring water and wild honey", "uncut wild pine timber and river fish", "ripe orchard apples picked straight from trees"])
    prompt = (
        f"During an excursion, {harvester} collects {raw}, which exist directly in nature without factory processing. "
        f"Which category of goods do these belong to?"
    )
    return _mcq(
        rng,
        "04_natural_goods_raw_examples",
        prompt,
        "Natural goods",
        ["Luxury manufactured goods", "Capital electronics", "Synthetic plastic goods"],
        "Natural goods are unprocessed gifts of nature such as fresh water, fruit, wild timber, coal, and fish before industrial transformation.",
        {
            "tier_1": "Check whether any factory machinery altered these items before collection.",
            "tier_2": "Unaltered resources gathered directly from the environment carry a specific goods name.",
            "tier_3": "Select 'Natural goods'.",
        },
        ["thinks_only_minerals_are_natural_goods"],
    )


def _b05(rng: random.Random) -> Dict[str, Any]:
    raw_mat, finished = rng.choice([
        ("raw wheat grain", "packaged sliced bread"),
        ("pine tree logs", "varnished school desks"),
        ("raw sheep wool", "knitted school jerseys"),
        ("iron ore and coal", "steel roof sheets"),
    ])
    town = _pick_place(rng, rural=False)
    prompt = (
        f"In an industrial workshop in {town}, workers and machinery convert {raw_mat} into {finished}. "
        f"Define **manufactured goods** and explain two ways processing increases value for consumers."
    )
    sample = (
        f"Manufactured goods are products created by transforming raw materials ({raw_mat}) into usable finished items "
        f"({finished}) using labour and machines. Processing increases value by (1) making raw inputs immediately usable "
        f"by households and (2) improving durability, safety, and storage life."
    )
    worked = (
        f"1. **Definition [1]:** Manufactured goods result from processing raw or semi-finished materials into finished products ({finished}).\n"
        f"2. **Value increase [2]:** Processing turns unusable raw {raw_mat} into ready-to-use, longer-lasting, higher-utility products for {town} consumers."
    )
    return _q(
        rng,
        "05_manufactured_goods_processing",
        prompt,
        sample,
        worked,
        "Secondary manufacturing adds form utility, quality, and higher exchange value to raw primary inputs.",
        {
            "tier_1": f"Describe what changed between {raw_mat} and {finished}.",
            "tier_2": "Think of why shoppers pay more for finished desks, jerseys, or bread than raw logs or raw grain.",
            "tier_3": "Define manufactured goods and list two consumer gains: usability and durability/convenience.",
        },
        ["confuses_raw_inputs_with_manufactured_goods"],
        [
            {"criterion": "Defines manufactured goods (processed from raw materials)", "marks": 1},
            {"criterion": "Benefit 1: Immediate consumer usability / convenience", "marks": 1},
            {"criterion": "Benefit 2: Improved durability, safety, or higher utility", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b06(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    util = rng.choice(["bar soap, toothpaste, and dishwashing liquid", "exercise books, pencils, and a sweeping broom", "toilet paper, washing powder, and cooking salt"])
    prompt = (
        f"{buyer} buys {util} every month strictly for everyday hygiene, cleaning, and schoolwork. "
        f"What specific category of practical everyday goods are these called?"
    )
    return _mcq(
        rng,
        "06_utility_goods_everyday_function",
        prompt,
        "Utility goods",
        ["Luxury status goods", "Capital industrial machinery", "Raw primary ores"],
        "Utility goods are ordinary practical products needed for everyday household functioning, hygiene, and work rather than prestige or luxury.",
        {
            "tier_1": "Think of the word meaning 'practical everyday usefulness'.",
            "tier_2": "Contrast soap, brooms, and stationery against luxury jewellery or factory lathes.",
            "tier_3": "Select 'Utility goods'.",
        },
        ["classifies_household_soap_as_luxury_or_capital_good"],
    )


def _b07(rng: random.Random) -> Dict[str, Any]:
    city = _pick_place(rng, rural=False)
    lux = rng.choice(["Swiss diamond wristwatches", "imported Italian sports cars", "custom designer evening gowns"])
    price = rng.choice([25000, 48000, 85000])
    prompt = (
        f"Boutiques in {city} sell {lux} priced around {_fmt_rand(price)}. Define **luxury goods** and explain why "
        f"demand for them rises or falls sharply when household incomes change."
    )
    sample = (
        f"Luxury goods are expensive non-essential products (like {lux} at {_fmt_rand(price)}) desired for prestige, "
        f"comfort, or status rather than survival. Because families prioritise needs first, demand rises when incomes grow "
        f"and drops quickly during recessions or unemployment."
    )
    worked = (
        f"1. **Definition [1]:** Luxury goods are high-priced non-essentials bought for prestige or indulgence once basic needs are covered.\n"
        f"2. **Income sensitivity [2]:** During tough times households cut {_fmt_rand(price)} luxury spending first; when incomes rise strongly, discretionary luxury purchases expand."
    )
    return _q(
        rng,
        "07_luxury_goods_status_examples",
        prompt,
        sample,
        worked,
        "Unlike essential utility goods, luxury goods are highly sensitive to changes in disposable household income.",
        {
            "tier_1": "First define what distinguishes luxury goods from everyday necessities.",
            "tier_2": f"Ask what happens first to a {_fmt_rand(price)} luxury purchase if a family's income drops.",
            "tier_3": "State the luxury definition and explain that households delay luxury spending whenever incomes tighten.",
        },
        ["thinks_luxury_demand_stays_constant_during_income_drops"],
        [
            {"criterion": "Defines luxury goods (non-essential high-price status/comfort goods)", "marks": 1},
            {"criterion": "Explains sharp drop/rise in demand as disposable income shifts", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b08(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    cons = rng.choice(["fresh milk, petrol, and printing paper", "apples, matches, and bar soap"])
    dur = rng.choice(["a stainless-steel refrigerator and steel study desk", "a bicycle and gas stove"])
    prompt = (
        f"{buyer} purchases {cons} weekly, while buying {dur} only once every five to ten years. "
        f"Contrast **consumable goods** with **durable goods** using these examples."
    )
    sample = (
        f"Consumable (non-durable) goods like {cons} are used up immediately or within a short time and must be replaced frequently, "
        f"whereas durable goods like {dur} withstand repeated use over several years."
    )
    worked = (
        f"1. **Consumable goods [1.5]:** Short-lived items ({cons}) consumed in one or a few uses, requiring regular repurchasing.\n"
        f"2. **Durable goods [1.5]:** Long-lasting items ({dur}) providing repeated service across many years."
    )
    return _q(
        rng,
        "08_consumable_vs_durable_goods",
        prompt,
        sample,
        worked,
        "Lifespan distinguishes consumable goods (used up quickly) from durable goods (lasting multiple years).",
        {
            "tier_1": "Compare how long each group lasts after purchase.",
            "tier_2": f"Milk/petrol finish quickly; {dur} remain usable year after year.",
            "tier_3": "Define consumable (used up fast) vs durable (repeated multi-year use) with the given items.",
        },
        ["swaps_consumable_and_durable_terms"],
        [
            {"criterion": f"Defines consumable goods using {cons} (used up quickly)", "marks": 1},
            {"criterion": f"Defines durable goods using {dur} (long multi-year lifespan)", "marks": 2},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b09(rng: random.Random) -> Dict[str, Any]:
    firm = _pick_person(rng)
    gear = rng.choice(["an industrial bread dough mixer and bakery oven", "a farm combine harvester and irrigation pump", "a commercial printing press and laser cutter"])
    prompt = (
        f"{firm}'s workshop purchases {gear} not for household use, but to produce goods that will be sold to customers. "
        f"How are {gear} classified?"
    )
    return _mcq(
        rng,
        "09_capital_goods_production_role",
        prompt,
        "Capital goods",
        ["Consumable household goods", "Unprocessed natural goods", "Intangible tertiary services"],
        "Capital goods are man-made durable assets (machinery, tools, equipment, factories) purchased by businesses specifically to produce other goods and services.",
        {
            "tier_1": "Ask who uses this machinery and why: a private kitchen dinner or commercial production?",
            "tier_2": "Man-made machines that manufacture other items belong to a distinct goods category.",
            "tier_3": "Select 'Capital goods'.",
        },
        ["labels_factory_machines_as_consumer_goods"],
    )


def _b10(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Classify each item in the table into its exact EMS goods category: **Natural Good**, **Luxury Good**, "
        "**Consumable Good**, or **Capital Good**."
    )
    row_specs = [
        {"cells": ["Fresh river water and wild sandstone rock", None], "expected": ["Natural Good"], "cell_hints": ["Exists directly in nature prior to processing."]},
        {"cells": ["Handcrafted platinum and diamond bracelet", None], "expected": ["Luxury Good"], "cell_hints": ["High-price non-essential status item."]},
        {"cells": ["Loaf of brown bread eaten at breakfast", None], "expected": ["Consumable Good"], "cell_hints": ["Used up immediately after purchase."]},
        {"cells": ["Commercial sewing machine in a uniform factory", None], "expected": ["Capital Good"], "cell_hints": ["Machine owned by a business to make other products."]},
    ]
    return _table_q(
        rng,
        "10_seven_categories_of_goods_table",
        prompt,
        ["Product Example", "Goods Category"],
        row_specs,
        "Goods span multiple economic categories depending on origin (natural vs manufactured), purpose (utility/luxury vs capital), and lifespan (consumable vs durable).",
        {
            "tier_1": "Focus on origin (nature vs workshop), purpose (consumption vs production), and necessity level.",
            "tier_2": "River water->Natural, diamond bracelet->Luxury, bread->Consumable, commercial sewing machine->Capital.",
            "tier_3": "Use labels: Natural Good, Luxury Good, Consumable Good, and Capital Good.",
        },
        ["confuses_natural_consumable_and_capital_goods"],
    )


def _b11(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each service provided in {town} into either **Essential Service** or **Non-essential Service**."
    )
    pool = [
        {"cells": ["Emergency ambulance and public hospital treatment", None], "expected": ["Essential Service"], "cell_hints": ["Directly protects human life and public health."]},
        {"cells": ["Municipal clean water supply and sanitation removal", None], "expected": ["Essential Service"], "cell_hints": ["Vital survival and disease-prevention service."]},
        {"cells": ["Luxury pet grooming spa and weekend limousine hire", None], "expected": ["Non-essential Service"], "cell_hints": ["Optional lifestyle comfort service."]},
        {"cells": ["Theme park roller-coaster ride and cinema ticket", None], "expected": ["Non-essential Service"], "cell_hints": ["Entertainment activity not needed for survival or basic learning."]},
        {"cells": ["Primary school classroom teaching", None], "expected": ["Essential Service"], "cell_hints": ["Foundational public service needed for literacy and development."]},
        {"cells": ["Premium interior garden landscaping for decorative fountains", None], "expected": ["Non-essential Service"], "cell_hints": ["Aesthetic luxury service."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "11_essential_vs_nonessential_services",
        prompt,
        ["Service Example", "Service Classification"],
        chosen,
        "Essential services safeguard life, health, safety, and foundational education; non-essential services provide leisure or luxury convenience.",
        {
            "tier_1": "Test whether public health, safety, or basic education suffers if the service stops.",
            "tier_2": "Ambulances, water sanitation, and schooling are Essential; cinemas, theme parks, and luxury grooming are Non-essential.",
            "tier_3": "Fill in 'Essential Service' or 'Non-essential Service'.",
        },
        ["treats_entertainment_venues_as_essential_services"],
    )


def _b12(rng: random.Random) -> Dict[str, Any]:
    brand = _pick_person(rng)
    prod = rng.choice(["affordable toothpaste tubes", "school exercise books", "bar soap multipacks"])
    unit_p = rng.randint(12, 25)
    prompt = (
        f"{brand}'s factory mass-produces {prod} sold at {_fmt_rand(unit_p)} directly to households in supermarkets. "
        f"Define **consumer goods** and explain why mass production helps keep prices affordable for families."
    )
    sample = (
        f"Consumer goods are finished goods bought by households for direct personal/family use rather than factory resale. "
        f"Mass production lowers the cost per unit ({_fmt_rand(unit_p)}) through specialised assembly lines and bulk material buying."
    )
    worked = (
        f"1. **Definition [1]:** Consumer goods (like {prod}) satisfy final household needs/wants directly.\n"
        f"2. **Affordability via mass production [2]:** Producing thousands of uniform units spreads machinery costs across huge output, keeping retail price low ({_fmt_rand(unit_p)})."
    )
    return _q(
        rng,
        "12_consumer_goods_mass_market",
        prompt,
        sample,
        worked,
        "Mass-market consumer goods rely on large-scale specialisation to deliver affordable everyday products.",
        {
            "tier_1": "Explain who uses consumer goods, then consider why making 100 000 units costs less per unit than making 5.",
            "tier_2": f"Mention direct household consumption and economies of large-scale production keeping price at {_fmt_rand(unit_p)}.",
            "tier_3": "Define consumer goods and explain lower per-unit manufacturing costs under mass production.",
        },
        ["confuses_consumer_goods_with_capital_machinery"],
        [
            {"criterion": "Defines consumer goods (final use by households)", "marks": 1},
            {"criterion": "Explains lower cost per unit through mass production / specialisation", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b13(rng: random.Random) -> Dict[str, Any]:
    maker = _pick_person(rng)
    act = rng.choice(["bakes 300 loaves of bread daily for a neighbourhood shop", "repairs laptops and installs school software for fees", "grows organic spinach and carrots to supply local stalls"])
    prompt = (
        f"{maker} {act}. In economics, what general role is {maker} performing in the market?"
    )
    return _mcq(
        rng,
        "13_producer_definition_value_addition",
        prompt,
        "Producer",
        ["Passive final consumer", "Fiscal tax regulator", "Non-working dependant"],
        "A producer combines natural resources, labour, and capital to create goods or render services for exchange.",
        {
            "tier_1": "Ask whether this person is buying final goods to eat/use, or creating/supplying them.",
            "tier_2": "Anyone making goods or performing paid services acts in this production role.",
            "tier_3": "Choose 'Producer'.",
        },
        ["thinks_only_large_factories_are_producers"],
    )


def _b14(rng: random.Random) -> Dict[str, Any]:
    shopper = _pick_person(rng)
    purchase = rng.choice(["a school tracksuit and warm soup", "bus fare and fresh fruit", "a haircut and stationery pack"])
    prompt = (
        f"On Saturday morning, {shopper} buys {purchase} to use personally and within the household. "
        f"Which economic role is {shopper} fulfilling?"
    )
    return _mcq(
        rng,
        "14_consumer_definition_buying_power",
        prompt,
        "Consumer",
        ["Industrial raw extractor", "Wholesale factory producer", "Primary sector miner"],
        "A consumer is any person or household purchasing and using final goods and services to satisfy personal needs and wants.",
        {
            "tier_1": "Notice who is buying final goods and services to use personally rather than to manufacture or resell.",
            "tier_2": "Individuals satisfying personal needs/wants act in the demand role.",
            "tier_3": "Select 'Consumer'.",
        },
        ["confuses_buying_final_goods_with_producing"],
    )


def _b15(rng: random.Random) -> Dict[str, Any]:
    p_name, c_name = _pick_two_people(rng)
    amt = rng.choice([450, 680, 920])
    diag = _svg_exchange(
        "Producer & Consumer Interdependence",
        f"Producer ({p_name})",
        "Makes shoes & repair services",
        f"Consumer ({c_name})",
        f"Pays {_fmt_rand(amt)} for needs",
        f"Goods & services worth {_fmt_rand(amt)}",
        f"Rand revenue: {_fmt_rand(amt)}",
    )
    prompt = (
        f"Refer to the exchange diagram between Producer ({p_name}) and Consumer ({c_name}) involving {_fmt_rand(amt)}. "
        f"Explain why producers and consumers cannot operate successfully without one another."
    )
    sample = (
        f"Producers like {p_name} depend on consumers like {c_name} to buy their output and generate {_fmt_rand(amt)} "
        f"revenue to pay wages and stay open; consumers depend on producers to supply essential goods and services they cannot make alone."
    )
    worked = (
        f"1. **Producer's need for consumers [1]:** Without {c_name} spending {_fmt_rand(amt)}, {p_name} cannot earn income or recover production costs.\n"
        f"2. **Consumer's need for producers [1]:** Without {p_name} specialising and supplying shoes/services, {c_name} cannot easily satisfy daily needs."
    )
    return _q(
        rng,
        "15_producers_and_consumers_interdependence",
        prompt,
        sample,
        worked,
        "Producers and consumers form a two-way interdependence via goods/services flows and Rand spending flows.",
        {
            "tier_1": "Follow both arrows in the diagram — what travels left-to-right and what travels right-to-left?",
            "tier_2": f"Ask what happens to {p_name} if nobody pays {_fmt_rand(amt)}, and to {c_name} if no goods are made.",
            "tier_3": "Explain both directions: producers need consumer revenue, consumers need producer goods/services.",
        },
        ["sees_relationship_as_one_sided"],
        [
            {"criterion": f"Explains producer reliance on consumer spending ({_fmt_rand(amt)})", "marks": 1},
            {"criterion": "Explains consumer reliance on producer goods and services", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b16(rng: random.Random) -> Dict[str, Any]:
    area = _pick_place(rng, rural=True)
    act = rng.choice(["coal mining and commercial wheat farming", "deep-sea snoek fishing and pine forestry", "citrus orchards and iron ore quarrying"])
    prompt = (
        f"Around {area}, major employers focus on {act}, extracting raw natural resources straight from the earth and sea. "
        f"Which economic sector do these activities belong to?"
    )
    return _mcq(
        rng,
        "16_primary_sector_extraction",
        prompt,
        "Primary sector",
        ["Secondary manufacturing sector", "Tertiary retail service sector", "Quaternary banking sector"],
        "The primary sector encompasses farming, mining, forestry, and fishing — all industries that harvest raw materials directly from nature.",
        {
            "tier_1": "Ask whether these workers are extracting raw materials directly from soil, mines, forests, or oceans.",
            "tier_2": "Recall the three economic sectors: extracting raw goods is Stage 1.",
            "tier_3": "Select 'Primary sector'.",
        },
        ["confuses_primary_extraction_with_secondary_factories"],
    )


def _b17(rng: random.Random) -> Dict[str, Any]:
    city = _pick_place(rng, rural=False)
    ind = rng.choice(["fruit canning and bottling plant", "cotton textile and school-shirt factory", "steel vehicle assembly workshop"])
    prompt = (
        f"In {city}, a {ind} buys raw primary inputs and turns them into finished consumer goods. "
        f"Name this economic sector and give TWO other South African examples belonging to the same sector."
    )
    sample = (
        f"This belongs to the **secondary sector**. Two other South African secondary-sector examples are "
        f"(1) sugar refineries/bakeries processing cane and flour into food, and (2) construction/furniture companies "
        f"turning timber, bricks, and cement into houses and desks."
    )
    worked = (
        f"1. **Sector [1]:** **Secondary sector** (processing raw materials into manufactured products).\n"
        f"2. **Two SA examples [2]:** Bakeries/dairy factories, brickworks/construction firms, paper mills, or oil refineries (any two valid manufacturing/construction activities)."
    )
    return _q(
        rng,
        "17_secondary_sector_manufacturing",
        prompt,
        sample,
        worked,
        "The secondary sector transforms primary raw commodities into manufactured, built, or processed goods.",
        {
            "tier_1": "Name the middle sector between raw extraction and retail services.",
            "tier_2": "Think of factories, bakeries, construction builders, and clothing makers in South Africa.",
            "tier_3": "Identify 'Secondary sector' and list two clear manufacturing or construction examples.",
        },
        ["lists_shops_or_banks_as_secondary_sector"],
        [
            {"criterion": "Correctly identifies Secondary sector", "marks": 1},
            {"criterion": "Valid secondary manufacturing/construction example 1", "marks": 1},
            {"criterion": "Valid secondary manufacturing/construction example 2", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b18(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    biz = rng.choice(["supermarkets, freight trucking, and commercial banks", "private dental surgeries, hair salons, and pharmacies"])
    prompt = (
        f"Along the main street of {town}, {biz} distribute finished products and provide personal or commercial services "
        f"rather than farming or manufacturing. Which economic sector do they belong to?"
    )
    return _mcq(
        rng,
        "18_tertiary_sector_services_retail",
        prompt,
        "Tertiary sector",
        ["Primary extractive sector", "Secondary industrial sector", "Subsistence barter sector"],
        "The tertiary sector consists of retail/wholesale trade, banking, transport, healthcare, tourism, education, and all service businesses.",
        {
            "tier_1": "Notice these firms neither dig raw materials out of the ground nor run assembly factories.",
            "tier_2": "Shops, transport, banks, and personal care services belong to Stage 3.",
            "tier_3": "Select 'Tertiary sector'.",
        },
        ["classifies_supermarkets_as_secondary_producers"],
    )


def _b19(rng: random.Random) -> Dict[str, Any]:
    city = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each South African enterprise operating near {city} into the **Primary Sector**, "
        f"**Secondary Sector**, or **Tertiary Sector**."
    )
    pool = [
        {"cells": ["Sugar cane farm harvesting raw cane in KwaZulu-Natal", None], "expected": ["Primary Sector"], "cell_hints": ["Grows raw agricultural crop directly on the land."]},
        {"cells": ["Sugar mill refining raw cane into packaged white sugar", None], "expected": ["Secondary Sector"], "cell_hints": ["Industrial processing of raw crop into packaged product."]},
        {"cells": ["Clothing factory sewing school blazers from woven fabric", None], "expected": ["Secondary Sector"], "cell_hints": ["Manufactures finished garments."]},
        {"cells": ["Shipping logistics company and local grocery supermarket", None], "expected": ["Tertiary Sector"], "cell_hints": ["Provides transport and retail distribution services."]},
        {"cells": ["Deep-level platinum mine extracting raw ore", None], "expected": ["Primary Sector"], "cell_hints": ["Extracts raw minerals from the earth."]},
        {"cells": ["Commercial bank offering business accounts and EFT services", None], "expected": ["Tertiary Sector"], "cell_hints": ["Delivers intangible financial services."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "19_three_economic_sectors_table",
        prompt,
        ["Business Activity", "Economic Sector"],
        chosen,
        "Primary extracts raw resources, Secondary processes/manufactures goods, and Tertiary distributes goods and renders services.",
        {
            "tier_1": "Ask: extract raw from nature (Primary), manufacture/build (Secondary), or sell/deliver service (Tertiary)?",
            "tier_2": "Match farms/mines->Primary, mills/clothing factories->Secondary, supermarkets/banks->Tertiary.",
            "tier_3": "Use labels: Primary Sector, Secondary Sector, Tertiary Sector.",
        },
        ["places_retail_shops_into_secondary_sector"],
    )


def _b20(rng: random.Random) -> Dict[str, Any]:
    chain = rng.choice([
        ("Wheat farm", "Flour mill & bakery", "Corner supermarket", "1 ton wheat", "Loaves of bread", "Retail bread"),
        ("Timber plantation", "Furniture workshop", "School supplier", "Pine logs", "Classroom desks", "Delivered desks"),
    ])
    p1 = rng.randint(15, 25)
    p2 = p1 + rng.randint(18, 30)
    p3 = p2 + rng.randint(12, 20)
    diag = _svg_chain_three(
        f"Production Chain: {chain[2]}",
        [
            ("Primary", chain[0], p1),
            ("Secondary", chain[1], p2),
            ("Tertiary", chain[2], p3),
        ],
    )
    prompt = (
        f"Refer to the three-stage production diagram showing {chain[0]} ({_fmt_rand(p1)}) -> {chain[1]} ({_fmt_rand(p2)}) -> "
        f"{chain[2]} ({_fmt_rand(p3)}). Briefly describe what economic activity happens in each of the three sectors "
        f"along this chain."
    )
    sample = (
        f"In the **Primary sector**, {chain[0]} harvests the raw input ({chain[3]}, valued at {_fmt_rand(p1)}). "
        f"In the **Secondary sector**, {chain[1]} processes it into {chain[4]} ({_fmt_rand(p2)}). "
        f"In the **Tertiary sector**, {chain[2]} transports, markets, and sells {chain[5]} to households for {_fmt_rand(p3)}."
    )
    worked = (
        f"1. **Primary ({chain[0]}) [1]:** Extracts/grows raw {chain[3]} sold for {_fmt_rand(p1)}.\n"
        f"2. **Secondary ({chain[1]}) [1]:** Transforms raw input into finished {chain[4]} priced at {_fmt_rand(p2)}.\n"
        f"3. **Tertiary ({chain[2]}) [1]:** Distributes and retails {chain[5]} directly to final consumers at {_fmt_rand(p3)}."
    )
    return _q(
        rng,
        "20_production_chain_bread_or_sugar",
        prompt,
        sample,
        worked,
        "Every everyday product passes through interconnected primary extraction, secondary manufacturing, and tertiary retail services.",
        {
            "tier_1": "Read the three coloured boxes left to right: Primary, Secondary, Tertiary.",
            "tier_2": f"Describe what each stage contributes from {_fmt_rand(p1)} raw input up to {_fmt_rand(p3)} retail sale.",
            "tier_3": "Explain harvesting/growing (Primary), factory processing (Secondary), and retail distribution (Tertiary).",
        },
        ["omits_tertiary_retail_and_distribution_role"],
        [
            {"criterion": f"Explains Primary raw extraction ({chain[0]}, {_fmt_rand(p1)})", "marks": 1},
            {"criterion": f"Explains Secondary processing ({chain[1]}, {_fmt_rand(p2)})", "marks": 1},
            {"criterion": f"Explains Tertiary distribution/retail ({chain[2]}, {_fmt_rand(p3)})", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b21(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    p_farm = rng.randint(40, 80)
    add_sec = rng.randint(70, 120)
    add_ter = rng.randint(35, 65)
    p_sec = p_farm + add_sec
    p_ter = p_sec + add_ter
    prompt = (
        f"In {town}, a dairy farmer sells raw milk to a cheese factory for {_fmt_rand(p_farm)}. "
        f"The factory processes it into packaged cheese sold to a grocer for {_fmt_rand(p_sec)}, and the grocer "
        f"sells it to consumers for {_fmt_rand(p_ter)}. Calculate the combined Rand **value added** by the "
        f"secondary and tertiary sectors after the farm gate."
    )
    added_after_farm = p_ter - p_farm
    worked = (
        f"1. **Secondary value added [1]:** {_fmt_rand(p_sec)} - {_fmt_rand(p_farm)} = {_fmt_rand(add_sec)}.\n"
        f"2. **Tertiary value added [1]:** {_fmt_rand(p_ter)} - {_fmt_rand(p_sec)} = {_fmt_rand(add_ter)}.\n"
        f"3. **Combined post-farm value added [1]:** {_fmt_rand(add_sec)} + {_fmt_rand(add_ter)} = **{_fmt_rand(added_after_farm)}**."
    )
    return _q(
        rng,
        "21_sector_value_added_calculation",
        prompt,
        _fmt_rand(added_after_farm),
        worked,
        "Value added measures the extra Rand worth created at each manufacturing and service stage above the cost of purchased inputs.",
        {
            "tier_1": "Subtract the raw farm selling price from the final supermarket selling price (or sum the two post-farm jumps).",
            "tier_2": f"Compute ({_fmt_rand(p_sec)} - {_fmt_rand(p_farm)}) + ({_fmt_rand(p_ter)} - {_fmt_rand(p_sec)}).",
            "tier_3": f"Subtract {_fmt_rand(p_farm)} from {_fmt_rand(p_ter)} to get {_fmt_rand(added_after_farm)}.",
        },
        ["adds_all_three_prices_together_causing_double_counting"],
        [
            {"criterion": f"Secondary value added = {_fmt_rand(add_sec)}", "marks": 1},
            {"criterion": f"Tertiary value added = {_fmt_rand(add_ter)}", "marks": 1},
            {"criterion": f"Total post-farm value added = {_fmt_rand(added_after_farm)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="hard",
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b22(rng: random.Random) -> Dict[str, Any]:
    dev_t = rng.choice([72, 75, 78])
    dev_p = rng.choice([2, 3, 4])
    low_p = rng.choice([42, 48, 52])
    low_t = rng.choice([30, 34, 38])
    diag = _svg_bars(
        "Employment Share (%): Developing vs Developed Economy",
        [
            ("Developing Country — Primary Sector", low_p, "#16a34a"),
            ("Developing Country — Tertiary Sector", low_t, "#0284c7"),
            ("Developed Country — Primary Sector", dev_p, "#86efac"),
            ("Developed Country — Tertiary Sector", dev_t, "#2563eb"),
        ],
        unit_prefix="",
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the employment bar diagram comparing a developing country ({low_p}% primary, {low_t}% tertiary) "
        f"with a developed country ({dev_p}% primary, {dev_t}% tertiary). Explain why developing countries rely much more "
        f"on primary-sector jobs while developed countries concentrate employment in the tertiary sector."
    )
    sample = (
        f"Developing countries have less industrial machinery and fewer service/finance firms, so a large workforce "
        f"({low_p}%) works directly in farming, fishing, and mining. Developed economies use mechanised farming "
        f"(needing only {dev_p}% workers in primary) and have higher incomes demanding specialised tertiary services "
        f"like banking, IT, healthcare, and education ({dev_t}%)."
    )
    worked = (
        f"1. **Developing pattern ({low_p}% primary) [1.5]:** Lower mechanisation and greater reliance on subsistence/smallholder agriculture and raw exports.\n"
        f"2. **Developed pattern ({dev_t}% tertiary) [1.5]:** High farm automation frees workers for finance, retail, healthcare, technology, and professional services."
    )
    return _q(
        rng,
        "22_developing_vs_developed_sector_share",
        prompt,
        sample,
        worked,
        "As economies industrialise and incomes rise, employment shifts away from primary extraction toward secondary manufacturing and tertiary services.",
        {
            "tier_1": "Compare the green primary bars against the blue tertiary bars across the two countries.",
            "tier_2": f"Think about why modern mechanised farms only need {dev_p}% of workers, and what rich service economies buy instead.",
            "tier_3": "Link lower mechanisation to high primary jobs in developing countries, and automation + high service demand to tertiary dominance.",
        },
        ["thinks_primary_shrinking_means_less_food_is_grown"],
        [
            {"criterion": f"Explains {low_p}% primary reliance in developing economies", "marks": 1},
            {"criterion": f"Explains automation & high service demand driving {dev_t}% tertiary share", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b23(rng: random.Random) -> Dict[str, Any]:
    shock = rng.choice([
        ("severe drought reduces citrus and tomato harvests", "fruit juice canning factories", "grocery stores and restaurants"),
        ("geological fault temporarily closes iron-ore mines", "steel fabrication plants", "hardware wholesalers and freight hauliers"),
    ])
    province = _pick_place(rng, rural=True)
    prompt = (
        f"When a {shock[0]} in {province}, trace ONE direct disruption to the secondary sector ({shock[1]}) and "
        f"ONE knock-on effect on the tertiary sector ({shock[2]})."
    )
    sample = (
        f"Secondary effect: {shock[1].capitalize()} suffer raw-material shortages and rising input costs, forcing lower factory output. "
        f"Tertiary effect: {shock[2].capitalize()} receive smaller deliveries, face higher retail prices or empty shelves, and earn less revenue."
    )
    worked = (
        f"1. **Secondary impact [1.5]:** Raw input scarcity slows {shock[1]} production and threatens factory shift hours.\n"
        f"2. **Tertiary impact [1.5]:** {shock[2].capitalize()} lose stock turnover and transport/retail income — showing all three sectors are interdependent."
    )
    return _q(
        rng,
        "23_sector_interdependence_disruption",
        prompt,
        sample,
        worked,
        "Because primary outputs feed secondary factories and tertiary retailers, a primary shock ripples right through the economy.",
        {
            "tier_1": "Trace the chain forward: without raw material, what happens at the factory and then at the shop?",
            "tier_2": f"Link {shock[0]} -> {shock[1]} -> {shock[2]}.",
            "tier_3": "Give one factory disruption (shortage/higher cost/cut output) and one retail/transport consequence.",
        },
        ["treats_three_sectors_as_completely_isolated"],
        [
            {"criterion": f"Explains secondary manufacturing disruption at {shock[1]}", "marks": 1},
            {"criterion": f"Explains tertiary retail/freight impact at {shock[2]}", "marks": 2},
        ],
        cognitive_level="Problem Solving",
        marks=3,
    )


def _b24(rng: random.Random) -> Dict[str, Any]:
    hh = _pick_person(rng)
    goods_amt = rng.choice([2400, 3000, 3600])
    serv_amt = rng.choice([1600, 2000, 2400])
    total = goods_amt + serv_amt
    serv_pct = round(100 * serv_amt / total)
    prompt = (
        f"As consumers, {hh}'s household spends {_fmt_rand(goods_amt)} on physical **goods** (groceries, electricity prepaid units, "
        f"clothing) and {_fmt_rand(serv_amt)} on **services** (taxi transport, clinic fees, mobile airtime/data) in one month. "
        f"Calculate what percentage of {hh}'s total spending went toward **services**."
    )
    worked = (
        f"1. **Total consumer spending [1]:** {_fmt_rand(goods_amt)} + {_fmt_rand(serv_amt)} = {_fmt_rand(total)}.\n"
        f"2. **Service share [1]:** ({_fmt_rand(serv_amt)} / {_fmt_rand(total)}) x 100 = **{serv_pct}%**."
    )
    return _q(
        rng,
        "24_households_as_consumers_budget",
        prompt,
        f"{serv_pct}%",
        worked,
        "Modern households spend substantial shares of income on services alongside tangible retail goods.",
        {
            "tier_1": "First add goods spending and services spending to find the total monthly spend.",
            "tier_2": f"Divide {_fmt_rand(serv_amt)} by the combined total and multiply by 100.",
            "tier_3": f"Compute ({serv_amt} / {total}) x 100 = {serv_pct}%.",
        },
        ["divides_services_by_goods_instead_of_total_spending"],
        [
            {"criterion": f"Calculates total monthly spending = {_fmt_rand(total)}", "marks": 1},
            {"criterion": f"Calculates services percentage = {serv_pct}%", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b25(rng: random.Random) -> Dict[str, Any]:
    hh = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    act = rng.choice(["baking muffins for Saturday markets while working weekdays as a carpenter", "growing backyard spinach for sale while working at a local clinic"])
    prompt = (
        f"In {town}, {hh}'s household acts not only as consumers, but also participates in the economy by {act}. "
        f"Explain TWO ways households act as **producers** in the South African economy."
    )
    sample = (
        f"(1) Households supply essential factors of production — especially labour, entrepreneurship, and savings/capital — "
        f"to businesses in exchange for wages and income; and (2) households directly produce goods and services at home "
        f"or through micro-enterprises ({act})."
    )
    worked = (
        f"1. **Factor suppliers [2]:** Households sell their labour, skills, land, and capital to firms to enable production.\n"
        f"2. **Home / micro-production [1]:** Families also produce meals, crops, crafts, or childcare services directly ({act})."
    )
    return _q(
        rng,
        "25_households_as_producers_labour_factors",
        prompt,
        sample,
        worked,
        "Households play a vital producer role by supplying labour and entrepreneurial skill to businesses and producing home/micro-enterprise goods.",
        {
            "tier_1": "Remember households are not merely shoppers: who supplies workers and skills to factories and shops?",
            "tier_2": "Include both supplying factors of production (labour/entrepreneurship) and direct home/small-scale production.",
            "tier_3": "State two producer roles: providing labour/skills/capital to businesses, and making goods/services directly.",
        },
        ["thinks_households_are_only_passive_consumers"],
        [
            {"criterion": "Explains households supply labour/factors of production to businesses", "marks": 2},
            {"criterion": "Explains direct household/home/micro-enterprise production", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_goods_tangible_definition": _b01,
    "02_services_intangible_definition": _b02,
    "03_goods_vs_services_classification_table": _b03,
    "04_natural_goods_raw_examples": _b04,
    "05_manufactured_goods_processing": _b05,
    "06_utility_goods_everyday_function": _b06,
    "07_luxury_goods_status_examples": _b07,
    "08_consumable_vs_durable_goods": _b08,
    "09_capital_goods_production_role": _b09,
    "10_seven_categories_of_goods_table": _b10,
    "11_essential_vs_nonessential_services": _b11,
    "12_consumer_goods_mass_market": _b12,
    "13_producer_definition_value_addition": _b13,
    "14_consumer_definition_buying_power": _b14,
    "15_producers_and_consumers_interdependence": _b15,
    "16_primary_sector_extraction": _b16,
    "17_secondary_sector_manufacturing": _b17,
    "18_tertiary_sector_services_retail": _b18,
    "19_three_economic_sectors_table": _b19,
    "20_production_chain_bread_or_sugar": _b20,
    "21_sector_value_added_calculation": _b21,
    "22_developing_vs_developed_sector_share": _b22,
    "23_sector_interdependence_disruption": _b23,
    "24_households_as_consumers_budget": _b24,
    "25_households_as_producers_labour_factors": _b25,
}
