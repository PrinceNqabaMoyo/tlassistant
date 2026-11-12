"""
Grade 7 EMS — Term 1: History of Money — Semantic Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 1/01. History of money.md.
Zero synthetic shims, deterministic rng seeding, native EMS tables & seeded inline SVG figures.
"""
from __future__ import annotations

import html
import random
from typing import Any, Callable, Dict, List, Optional

from ..ems_namelist import AREAS, NAMES, RURAL_AREAS, TUCKSHOP_ITEMS, URBAN_AREAS

TOPIC_NAME = "History of money"
SUBJECT_NAME = "Economic and Management Sciences"
GRADE_NUM = 7
TERM_NUM = 1
CAPS_WEIGHT = 25


def _pick_person(rng: random.Random) -> str:
    return rng.choice(NAMES)


def _pick_two_people(rng: random.Random) -> tuple[str, str]:
    first, second = rng.sample(NAMES, 2)
    return first, second


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
        "question_id": f"g7_ems_hom_{subskill}_{rng.randint(10000, 99999)}",
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


def _svg_two_way_flow(
    title: str, left_title: str, left_sub: str, right_title: str, right_sub: str, top_lbl: str, bot_lbl: str
) -> Dict[str, Any]:
    body = (
        f'<rect x="28" y="54" width="210" height="106" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="133" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a">{_escape(left_title)}</text>'
        f'<text x="133" y="114" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#334155">{_escape(left_sub)}</text>'
        f'<rect x="402" y="54" width="210" height="106" rx="10" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="507" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#854d0e">{_escape(right_title)}</text>'
        f'<text x="507" y="114" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#334155">{_escape(right_sub)}</text>'
        f'<line x1="244" y1="86" x2="394" y2="86" stroke="#0f766e" stroke-width="2.5"/>'
        f'<polygon points="396,86 386,80 386,92" fill="#0f766e"/>'
        f'<text x="320" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f766e">{_escape(top_lbl)}</text>'
        f'<line x1="396" y1="132" x2="246" y2="132" stroke="#b45309" stroke-width="2.5"/>'
        f'<polygon points="244,132 254,126 254,138" fill="#b45309"/>'
        f'<text x="320" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#b45309">{_escape(bot_lbl)}</text>'
    )
    return _svg_wrap(640, 185, title, body)


def _svg_timeline(title: str, nodes: List[tuple[str, str]]) -> Dict[str, Any]:
    n = max(1, len(nodes))
    step = 560 // n
    parts = ['<line x1="50" y1="100" x2="590" y2="100" stroke="#64748b" stroke-width="3"/>']
    for i, (yr, desc) in enumerate(nodes):
        cx = 50 + step // 2 + i * step
        parts.append(f'<circle cx="{cx}" cy="100" r="9" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>')
        parts.append(f'<text x="{cx}" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#1e3a8a">{_escape(yr)}</text>')
        parts.append(f'<rect x="{cx - 64}" y="118" width="128" height="44" rx="6" fill="#eff6ff" stroke="#93c5fd"/>')
        parts.append(f'<text x="{cx}" y="144" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#0f172a">{_escape(desc)}</text>')
    return _svg_wrap(640, 185, title, "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 01 – 25
# ---------------------------------------------------------------------------

def _b01(rng: random.Random) -> Dict[str, Any]:
    area = _pick_place(rng, rural=True)
    name = _pick_person(rng)
    prompt = (
        f"While researching past communities near {area}, {name} notices that families produced only what they "
        f"needed for survival using natural resources, with no factories or modern currency. "
        f"Which term best describes this type of community?"
    )
    return _mcq(
        rng,
        "01_traditional_society_definition",
        prompt,
        "Traditional society",
        ["Modern industrialised society", "Digital consumer economy", "Multinational commercial hub"],
        "A traditional society is characterised by subsistence living close to nature, low specialisation, "
        "self-sufficiency, and exchange without modern notes, coins, or digital banking.",
        {
            "tier_1": "Think about communities that depend directly on the natural environment for survival rather than factories.",
            "tier_2": "Distinguish early self-sufficient lifestyles from modern economies built on industry and banking.",
            "tier_3": "Eliminate choices mentioning industry, digital commerce, or multinationals to identify the early community type.",
        },
        ["confuses_traditional_with_modern_society"],
    )


def _b02(rng: random.Random) -> Dict[str, Any]:
    city = _pick_place(rng, rural=False)
    name = _pick_person(rng)
    job = rng.choice(["software programmer", "chartered accountant", "electrical engineer", "pharmacist"])
    prompt = (
        f"In {city}, {name} works as a {job}, receives a monthly bank transfer salary, and buys groceries "
        f"made by specialised factories. Which statement accurately describes a modern society like this?"
    )
    return _mcq(
        rng,
        "02_modern_society_characteristics",
        prompt,
        "People specialise in specific jobs and rely on money to exchange goods and services",
        [
            "Every household grows all of its own food and weaves its own clothes",
            "Families rely solely on silent barter and hunting without currency",
            "Wealth is measured exclusively by the number of cattle kept near the hut",
        ],
        "Modern societies feature high job specialisation, urban industrial production, and standardised "
        "money or electronic payments so workers do not have to produce every item themselves.",
        {
            "tier_1": "Focus on how specialisation prevents each household from producing every daily item on its own.",
            "tier_2": "Compare modern wage earners who buy factory goods against self-sufficient subsistence households.",
            "tier_3": "Select the option linking job specialisation with the everyday use of money.",
        },
        ["misunderstands_modern_specialisation"],
    )


def _b03(rng: random.Random) -> Dict[str, Any]:
    name = _pick_person(rng)
    area = _pick_place(rng, rural=True)
    crops = rng.sample(["maize", "sorghum", "pumpkins", "beans", "melons"], 2)
    craft = rng.choice(["clay pots", "woven grass mats", "wooden bowls", "leather sandals"])
    prompt = (
        f"In an early settlement outside {area}, {name}'s household grew {crops[0]} and {crops[1]}, tended cattle "
        f"for milk, and crafted {craft} for daily household use without visiting shops or using coins. "
        f"Define self-sufficiency and explain two ways this household achieved it."
    )
    sample = (
        f"Self-sufficiency means a household produces all the goods and services it needs to survive without "
        f"depending on outside trade or money. {name}'s household achieved this by (1) growing its own food "
        f"({crops[0]}, {crops[1]}, and milk) and (2) making essential household tools ({craft}) from natural materials."
    )
    worked = (
        f"1. **Definition [1]:** Self-sufficiency means meeting all survival needs (food, shelter, tools) using the household's own labour and natural resources without money.\n"
        f"2. **Food production [1]:** Cultivating {crops[0]} and {crops[1]} and keeping livestock for milk supplied daily nutrition.\n"
        f"3. **Craft & shelter [1]:** Making {craft} from local natural materials eliminated the need to purchase goods."
    )
    return _q(
        rng,
        "03_self_sufficiency_subsistence",
        prompt,
        sample,
        worked,
        "Traditional subsistence households survived by producing food and domestic items directly from local resources.",
        {
            "tier_1": "First define what 'self-sufficient' means when no shops or currency exist.",
            "tier_2": "Look at the two distinct categories of needs mentioned: nutrition and household equipment.",
            "tier_3": f"Link growing {crops[0]}/{crops[1]} and crafting {craft} directly to independent survival.",
        },
        ["incomplete_self_sufficiency_definition"],
        [
            {"criterion": "Accurate definition of self-sufficiency without external trade", "marks": 1},
            {"criterion": f"Food production example ({crops[0]}, {crops[1]}, milk)", "marks": 1},
            {"criterion": f"Crafting household items ({craft}) from natural resources", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b04(rng: random.Random) -> Dict[str, Any]:
    crop = rng.choice(["maize", "sorghum", "millet"])
    city = _pick_place(rng, rural=False)
    skill = rng.choice(["dentistry", "civil engineering", "accounting", "radiography"])
    prompt = (
        "Classify each community practice into **Traditional Society** or **Modern Society** in the table below."
    )
    row_specs = [
        {
            "cells": [f"Families grow {crop} and herd goats only for their own survival", None],
            "expected": ["Traditional Society"],
            "cell_hints": ["Ask whether this activity describes subsistence self-sufficiency or specialised industry."],
        },
        {
            "cells": [f"Workers in {city} specialise in {skill} and pay rent via EFT", None],
            "expected": ["Modern Society"],
            "cell_hints": ["Look for career specialisation and electronic banking."],
        },
        {
            "cells": ["Surplus grain is swapped directly for pottery with no cash used", None],
            "expected": ["Traditional Society"],
            "cell_hints": ["Direct swapping without money belongs to pre-currency trade."],
        },
        {
            "cells": ["Factories mass-produce clothing sold in shopping malls", None],
            "expected": ["Modern Society"],
            "cell_hints": ["Large-scale industrial manufacturing and retail stores characterise modern economies."],
        },
    ]
    return _table_q(
        rng,
        "04_traditional_vs_modern_table",
        prompt,
        ["Community Practice", "Society Type"],
        row_specs,
        "Traditional societies focus on subsistence living and direct exchange, whereas modern societies rely on specialisation, industrial production, and money.",
        {
            "tier_1": "Compare subsistence self-reliance against industrial specialisation and digital money.",
            "tier_2": "Check each description for clues such as 'for their own survival', 'swapped directly', 'EFT', or 'factories'.",
            "tier_3": "Group direct subsistence/barter practices as Traditional Society and specialised cash/EFT activities as Modern Society.",
        },
        ["confuses_traditional_modern_features"],
    )


def _b05(rng: random.Random) -> Dict[str, Any]:
    band = rng.choice(["San hunter-gatherer band", "early nomadic foraging group", "nomadic Khoi-San clan"])
    resource = rng.choice(["wild berries, tubers, and antelope", "ostrich eggs, roots, and game"])
    prompt = (
        f"Members of an early {band} moved seasonally in search of {resource}. "
        f"Why did nomadic hunter-gatherers rarely accumulate large hoards of physical wealth?"
    )
    return _mcq(
        rng,
        "05_hunter_gatherer_nomadic_living",
        prompt,
        "Constant movement meant families could only carry lightweight essential survival tools",
        [
            "Commercial banks charged high interest on stored arrowheads",
            "Government laws prohibited individuals from owning more than two spears",
            "Paper banknotes lost ink value whenever carried outdoors",
        ],
        "Nomadic hunter-gatherers moved frequently to follow water and food, making heavy possessions "
        "impractical and focusing communities on sharing daily survival resources.",
        {
            "tier_1": "Consider how moving camp regularly affects what a family can transport on foot.",
            "tier_2": "Eliminate options that invent banks, written laws, or paper currency in prehistoric nomadic groups.",
            "tier_3": "Connect constant seasonal migration with the need to travel light.",
        },
        ["anachronistic_wealth_assumption"],
    )


def _b06(rng: random.Random) -> Dict[str, Any]:
    name = _pick_person(rng)
    area = _pick_place(rng, rural=True)
    herd = rng.randint(14, 28)
    lobola_head = rng.randint(6, 12)
    prompt = (
        f"In a traditional rural community near {area}, {name}'s family keeps {herd} head of cattle and sets aside "
        f"{lobola_head} cattle for lobola negotiations. Explain why cattle served as an effective store of wealth "
        f"before coins existed, and state one limitation of using cattle for everyday small purchases."
    )
    sample = (
        f"Cattle served as a store of wealth because they were universally valued for milk, meat, hides, and status, "
        f"multiplied naturally over time, and represented large value in major ceremonies like lobola ({lobola_head} cattle). "
        f"A major limitation for everyday trade is lack of divisibility: you cannot pay for a single basket of grain with a fraction of a live cow."
    )
    worked = (
        f"1. **Why cattle stored wealth [2]:** Cattle provided ongoing food/materials (milk, meat, hides), reproduced to grow the herd from {herd} cattle, and carried social respect for lobola.\n"
        f"2. **Limitation for small purchases [1]:** Lack of divisibility and transport difficulty — a live cow cannot be split into small change for minor daily goods."
    )
    return _q(
        rng,
        "06_cattle_herding_wealth_lobola",
        prompt,
        sample,
        worked,
        "Cattle held strong intrinsic and cultural value for lobola and wealth, yet were too large and indivisible for petty daily trade.",
        {
            "tier_1": "Think of two practical reasons families valued cattle long-term, and one problem with using a live animal at a small market.",
            "tier_2": "Consider milk/reproduction/cultural status as strengths, and 'divisibility' as the key weakness.",
            "tier_3": "Contrast cattle's natural growth and lobola role with the impossibility of breaking one cow into small change.",
        },
        ["overlooks_indivisibility_of_livestock"],
        [
            {"criterion": "Explains intrinsic value/reproduction/status of cattle as wealth", "marks": 1},
            {"criterion": "Links cattle to major social exchange such as lobola", "marks": 1},
            {"criterion": "Identifies lack of divisibility (or transport difficulty) for small purchases", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b07(rng: random.Random) -> Dict[str, Any]:
    karoo_good = rng.choice(["wool fleeces", "sheep mutton", "dried lamb skins"])
    knysna_good = rng.choice(["yellowwood timber", "stinkwood planks", "carved wagon wood"])
    qty_k = rng.randint(4, 9)
    qty_n = rng.randint(2, 5)
    diag = _svg_two_way_flow(
        "Regional Environment & Barter Exchange",
        "Semi-Arid Karoo",
        f"Produces: {qty_k} {karoo_good}",
        "Knysna Forest",
        f"Produces: {qty_n} {knysna_good}",
        f"{qty_k} {karoo_good}",
        f"{qty_n} {knysna_good}",
    )
    prompt = (
        f"Refer to the diagram illustrating regional trade between two South African areas. "
        f"Explain how differing natural environments encouraged communities in the Semi-Arid Karoo "
        f"({qty_k} {karoo_good}) and Knysna Forest ({qty_n} {knysna_good}) to begin bartering."
    )
    sample = (
        f"Different natural climates meant each region produced surpluses the other lacked: dry Karoo grazing suited "
        f"sheep farming ({karoo_good}), whereas wet Knysna forests supplied dense hardwood ({knysna_good}). "
        f"Communities bartered {qty_k} {karoo_good} for {qty_n} {knysna_good} to obtain essential resources not found locally."
    )
    worked = (
        f"1. **Karoo advantage [1]:** Dry grazing conditions favoured livestock, yielding {qty_k} {karoo_good} without large forests.\n"
        f"2. **Knysna advantage [1]:** High rainfall supported indigenous timber, producing {qty_n} {knysna_good} for shelter and wagons.\n"
        f"3. **Reason for barter [1]:** Geographic scarcity meant swapping surpluses allowed both regions to improve living standards."
    )
    return _q(
        rng,
        "07_environment_shapes_barter_karoo_knysna",
        prompt,
        sample,
        worked,
        "Regional resource differences pushed early communities from pure self-sufficiency toward inter-regional bartering.",
        {
            "tier_1": "Look at why the dry Karoo and forested Knysna could not naturally produce the exact same materials.",
            "tier_2": "Relate rainfall and soil/climate to the specific product each community holds in the diagram.",
            "tier_3": f"Explain that exchanging {qty_k} {karoo_good} for {qty_n} {knysna_good} solved local resource scarcity.",
        },
        ["ignores_environmental_specialisation"],
        [
            {"criterion": f"Links dry Karoo environment to {karoo_good}", "marks": 1},
            {"criterion": f"Links forested Knysna environment to {knysna_good}", "marks": 1},
            {"criterion": "Explains mutual benefit of exchanging regional surpluses", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b08(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    g1 = rng.choice(["three crates of oranges", "two sacks of potatoes", "four bags of dried beans"])
    g2 = rng.choice(["mending a leaky roof", "repairing a bicycle", "sewing two school uniforms"])
    prompt = (
        f"At a community harvest day, {p1} agrees to give {p2} {g1} in exchange for {g2}, and no coins, "
        f"banknotes, or electronic payments change hands. What economic activity is taking place?"
    )
    return _mcq(
        rng,
        "08_bartering_definition_mechanism",
        prompt,
        "Bartering",
        ["Electronic funds transfer", "Issuing a promissory note", "Paying fiat currency"],
        "Bartering is the direct exchange of goods or services for other goods or services without using money.",
        {
            "tier_1": "Notice that neither physical money nor a written promise to pay later is used here.",
            "tier_2": "Remember that goods can be swapped directly for services as well as other goods.",
            "tier_3": "Select the term describing direct moneyless exchange.",
        },
        ["confuses_barter_with_credit_note"],
    )


def _b09(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    p3 = _pick_person(rng)
    while p3 in (p1, p2):
        p3 = _pick_person(rng)
    item_a = rng.choice(["fresh pumpkins", "honey jars", "woven baskets"])
    item_b = rng.choice(["iron hoes", "copper pots", "leather boots"])
    item_c = rng.choice(["dried fish", "sea salt", "wool blankets"])
    prompt = (
        f"{p1} brings {item_a} to market and wants {item_b}. {p2} has {item_b} to spare, but refuses {item_a} "
        f"because {p2} only wants {item_c} (which {p3} owns). Identify this specific obstacle to bartering "
        f"and explain why it slows down trade."
    )
    sample = (
        f"This obstacle is the lack of a double coincidence of wants. Both {p1} and {p2} must simultaneously want "
        f"exactly what the other offers. Because {p2} wants {item_c} instead of {item_a}, {p1} must waste time searching "
        f"for {p3} and arranging an indirect three-way swap."
    )
    worked = (
        f"1. **Obstacle [1]:** Lack of a **double coincidence of wants**.\n"
        f"2. **Why trade slows [2]:** {p1} wants {p2}'s {item_b}, but {p2} does not want {item_a}; {p1} must first trade with {p3} for {item_c}, causing high search costs and delays."
    )
    return _q(
        rng,
        "09_double_coincidence_of_wants",
        prompt,
        sample,
        worked,
        "A double coincidence of wants requires two parties to desire each other's exact goods at the same time.",
        {
            "tier_1": "Recall the formal EMS term used when two traders do not both want what the other is offering.",
            "tier_2": f"Trace why {p1} cannot trade directly with {p2} even though {p2} owns {item_b}.",
            "tier_3": f"Name 'double coincidence of wants' and explain the extra step needed through {p3}.",
        },
        ["cannot_identify_double_coincidence_of_wants"],
        [
            {"criterion": "Correctly names 'double coincidence of wants'", "marks": 1},
            {"criterion": "Explains mismatch between what traders hold and want", "marks": 1},
            {"criterion": "Notes wasted search time / indirect multi-step swapping", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b10(rng: random.Random) -> Dict[str, Any]:
    gold_kg = rng.randint(2, 6)
    salt_slabs = rng.randint(8, 20)
    signal = rng.choice(["beating drums", "sounding horns", "lighting signal fires"])
    diag = _svg_two_way_flow(
        "Trans-Saharan Silent Barter Exchange",
        "North African Merchants",
        f"Leave {salt_slabs} salt slabs",
        "West African Miners",
        f"Leave {gold_kg} kg gold",
        f"{salt_slabs} salt slabs placed & retreat",
        f"{gold_kg} kg gold placed; {signal}",
    )
    prompt = (
        f"Refer to the diagram illustrating silent barter across the Sahara. North African merchants place "
        f"{salt_slabs} salt slabs on the riverbank and withdraw; West African miners leave {gold_kg} kg of gold "
        f"and signal by {signal}. Explain TWO reasons why traders used silent barter instead of face-to-face bargaining."
    )
    sample = (
        f"Traders used silent barter because (1) the North African and West African groups did not share a common "
        f"spoken language, so non-verbal inspection of {salt_slabs} salt slabs against {gold_kg} kg of gold enabled fair "
        f"pricing, and (2) keeping distance protected the secret location of the gold mines and reduced conflict."
    )
    worked = (
        f"1. **Language barrier [2]:** Merchants and miners spoke different languages; stepping back while {signal} signalled readiness allowed non-verbal negotiation over {salt_slabs} salt slabs and {gold_kg} kg of gold.\n"
        f"2. **Security & secrecy [2]:** Avoiding direct contact reduced theft/ambush risk and prevented outsiders from discovering secret West African gold mining sites."
    )
    return _q(
        rng,
        "10_silent_barter_trans_saharan",
        prompt,
        sample,
        worked,
        "Silent barter allowed honest trade across linguistic barriers while protecting miners' mine locations and personal safety.",
        {
            "tier_1": "Think about communication obstacles and safety concerns when strangers from distant regions met.",
            "tier_2": "Consider why neither side wanted to speak face-to-face or reveal where the gold came from.",
            "tier_3": "State two distinct reasons: overcoming language differences and protecting mine secrecy/safety.",
        },
        ["guesses_silent_barter_was_about_shyness"],
        [
            {"criterion": "Reason 1: Overcomes language barrier between distant trading groups", "marks": 2},
            {"criterion": "Reason 2: Protects gold mine secrecy and physical security", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=4,
        diagram_spec=diag,
    )


def _b11(rng: random.Random) -> Dict[str, Any]:
    name = _pick_person(rng)
    animal = rng.choice(["dairy cow", "trek ox", "breeding bull"])
    pots_worth = rng.choice([12, 16, 20, 24])
    pots_wanted = rng.choice([2, 3, 4])
    prompt = (
        f"In a barter market, {name}'s {animal} is valued at {pots_worth} clay cooking pots. However, {name} only "
        f"wants {pots_wanted} clay pots to cook for one week. What percentage of the {animal}'s value are the "
        f"{pots_wanted} pots, and which bartering problem prevents {name} from handing over only that fraction of the {animal}?"
    )
    pct_val = 100 * pots_wanted / pots_worth
    if 100 * pots_wanted % pots_worth != 0:
        pct_str = f"{pct_val:.1f}".replace(".", ",") + "%"
    else:
        pct_str = f"{int(round(pct_val))}%"
    worked = (
        f"1. **Value fraction [1]:** {pots_wanted} / {pots_worth} x 100 = **{pct_str}**.\n"
        f"2. **Bartering problem [1]:** **Lack of divisibility** — a live {animal} loses its value or dies if cut into smaller pieces, unlike divisible coins."
    )
    correct = f"{pct_str}; lack of divisibility"
    return _q(
        rng,
        "11_barter_indivisibility_problem",
        prompt,
        correct,
        worked,
        "Unlike currency with small denominations, large indivisible barter items such as livestock cannot be split without destroying their value.",
        {
            "tier_1": "Compute the percentage as (wanted pots / total pot value) x 100, then identify the barter flaw.",
            "tier_2": "Ask whether a live animal can be divided into small pieces while staying alive and useful.",
            "tier_3": f"Calculate {pots_wanted}/{pots_worth} x 100 and name 'lack of divisibility'.",
        },
        ["ignores_indivisibility_of_barter_assets"],
        [
            {"criterion": f"Calculates {pct_str}", "marks": 1},
            {"criterion": "Identifies lack of divisibility", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b12(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    goods = rng.choice(["fresh cow's milk and ripe mangoes", "freshly caught river trout", "soft spinach and fresh berries"])
    prompt = (
        f"{trader} catches and harvests {goods} to barter later in the year during winter. "
        f"Why is {goods} unsuitable as a long-term store of value in bartering?"
    )
    return _mcq(
        rng,
        "12_barter_perishability_storage",
        prompt,
        "Perishable food spoils quickly and loses all exchange value during storage",
        [
            "Fresh produce automatically appreciates in price by ten times each week",
            "Perishable goods are strictly illegal to transport across provincial borders",
            "Spinach and fruit dissolve metal scales when traders try to weigh them",
        ],
        "Unlike durable money, perishable food rots within days or weeks, making it impossible to save "
        "purchasing power for future seasons.",
        {
            "tier_1": "Think about what happens to fresh milk, fruit, or fish if stored without modern refrigeration.",
            "tier_2": "Connect rotting or spoilage to the inability to store value for future purchases.",
            "tier_3": "Pick the option explaining spoilage and loss of exchange value.",
        },
        ["confuses_perishable_with_durable_goods"],
    )


def _b13(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    pots_per_goat = rng.randint(4, 7)
    loaves_per_pot = rng.randint(3, 6)
    goats = rng.randint(2, 5)
    total_loaves = goats * pots_per_goat * loaves_per_pot
    prompt = (
        f"At a barter exchange, 1 goat trades for {pots_per_goat} clay pots, and 1 clay pot trades for "
        f"{loaves_per_pot} loaves of bread. How many loaves of bread must {p1} offer {p2} in a fair barter "
        f"for {goats} goats?"
    )
    worked = (
        f"1. **Convert goats to clay pots [1]:** {goats} goats x {pots_per_goat} clay pots/goat = {goats * pots_per_goat} clay pots.\n"
        f"2. **Convert clay pots to loaves [1]:** {goats * pots_per_goat} x {loaves_per_pot} loaves/pot = **{total_loaves} loaves of bread**."
    )
    return _q(
        rng,
        "13_barter_valuation_rate_calculation",
        prompt,
        f"{total_loaves} loaves",
        worked,
        "Without a shared monetary unit of account, traders must multiply conversion ratios step by step.",
        {
            "tier_1": "First find how many clay pots equal all the goats.",
            "tier_2": f"Multiply {goats} by {pots_per_goat}, then multiply that intermediate amount by {loaves_per_pot}.",
            "tier_3": f"Compute {goats} x {pots_per_goat} x {loaves_per_pot} loaves.",
        },
        ["adds_exchange_rates_instead_of_multiplying"],
        [
            {"criterion": f"Converts goats to {goats * pots_per_goat} clay pots", "marks": 1},
            {"criterion": f"Multiplies to find {total_loaves} loaves of bread", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b14(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    school = _pick_place(rng, rural=True)
    item1 = rng.choice(["spare vegetable seedlings", "outgrown soccer boots", "extra wooden planks"])
    item2 = rng.choice(["a repaired study desk", "maths textbooks", "home-knitted jerseys"])
    prompt = (
        f"During a cash shortage in {school}, {p1} swaps {item1} with {p2} for {item2}. "
        f"Explain TWO practical advantages that bartering offers communities in situations like this."
    )
    sample = (
        f"(1) Bartering allows trade to continue without needing physical cash or bank accounts, and "
        f"(2) it clears surplus/unused items ({item1}) while obtaining needed goods ({item2}) and building mutual trust."
    )
    worked = (
        f"1. **No cash needed [1]:** Trade takes place immediately even when households lack coins or notes.\n"
        f"2. **Uses surpluses & builds cooperation [1]:** Both {p1} and {p2} convert unused surplus ({item1}) into useful items ({item2}) with flexible, mutually agreed terms."
    )
    return _q(
        rng,
        "14_barter_advantages_context",
        prompt,
        sample,
        worked,
        "Despite its limitations in complex economies, bartering remains useful for cash-strapped communities with complementary surpluses.",
        {
            "tier_1": "Think about what happens to people who have useful spare goods but zero cash on hand.",
            "tier_2": "Identify how surpluses become useful goods and how direct swapping encourages cooperation.",
            "tier_3": "State two benefits: cash-free exchange and turning unused surplus stock into needed items.",
        },
        ["thinks_barter_has_zero_benefits"],
        [
            {"criterion": "Explains ability to trade without cash or credit", "marks": 1},
            {"criterion": "Explains clearing surplus goods or flexible community cooperation", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b15(rng: random.Random) -> Dict[str, Any]:
    p1 = _pick_person(rng)
    prompt = "Match each trading difficulty experienced during bartering to its exact economic disadvantage."
    row_specs = [
        {
            "cells": [f"{p1} wants shoes, but the shoemaker refuses {p1}'s beans", None],
            "expected": ["Double coincidence of wants"],
            "cell_hints": ["Both parties must want what the other holds at the same time."],
        },
        {
            "cells": ["A farmer cannot cut half of a live cow to buy three clay bowls", None],
            "expected": ["Lack of divisibility"],
            "cell_hints": ["Certain items lose value if split into small change."],
        },
        {
            "cells": ["Baskets of fresh tomatoes rot before winter arrives", None],
            "expected": ["Perishability / storage problem"],
            "cell_hints": ["Fresh agricultural items spoil over time."],
        },
        {
            "cells": ["Hauling twenty heavy timber logs 40 km to market is exhausting", None],
            "expected": ["Transport difficulty"],
            "cell_hints": ["Bulky goods require heavy effort to move between markets."],
        },
    ]
    return _table_q(
        rng,
        "15_barter_disadvantages_table",
        prompt,
        ["Trading Scenario", "Bartering Disadvantage"],
        row_specs,
        "These four practical problems — double coincidence of wants, indivisibility, perishability, and bulky transport — drove societies to adopt commodity money and coins.",
        {
            "tier_1": "Identify the four core flaws of barter: matching wants, splitting items, rotting goods, and heavy carrying.",
            "tier_2": "Read each clue carefully: shoes/beans -> matching wants; live cow -> splitting; tomatoes -> rotting; logs -> moving.",
            "tier_3": "Assign Double coincidence of wants, Lack of divisibility, Perishability / storage problem, and Transport difficulty.",
        },
        ["mixes_up_barter_disadvantages"],
    )


def _b16(rng: random.Random) -> Dict[str, Any]:
    route_choice = rng.choice(["gold and ivory for silk and glass beads", "gold dust and kola nuts for Saharan salt slabs"])
    qty = rng.randint(5, 14)
    diag = _svg_two_way_flow(
        "Early Long-Distance Commodity Trade",
        "African Trade Centres",
        f"Supplied {qty} loads of gold & ivory",
        "Arab & Asian Merchants",
        "Supplied silk, ceramics & glass beads",
        f"{qty} loads gold & ivory",
        "Silk, ceramics & glass beads",
    )
    prompt = (
        f"Refer to the diagram of early international barter routes exchanging {route_choice}. "
        f"How did early long-distance trade between African, Arab, and Asian merchants change local communities?"
    )
    return _mcq(
        rng,
        "16_early_trade_routes_commodities",
        prompt,
        "Communities specialised in valuable export goods and gained access to scarce imported products",
        [
            "Every village stopped farming and became completely dependent on paper IOUs",
            "Traders banned all non-food goods so only fresh fruit could travel by sea",
            "Rulers prohibited all local crafts so artisans could work in banks",
        ],
        "Long-distance trade encouraged regional specialisation (mining gold, harvesting salt, crafting beads/silk) "
        "and connected distant economies long before modern electronic banking.",
        {
            "tier_1": "Think about what happens when regions trade goods they have in abundance for rare foreign goods.",
            "tier_2": "Look at the diagram arrows: each region supplies what it produces best in exchange for what it lacks.",
            "tier_3": "Choose the answer connecting regional specialisation with access to new goods.",
        },
        ["misses_specialisation_effect_of_trade"],
        diagram_spec=diag,
    )


def _b17(rng: random.Random) -> Dict[str, Any]:
    example = rng.choice(["cowrie shells", "compressed tea bricks", "rock salt bars", "cacao beans"])
    trader = _pick_person(rng)
    prompt = (
        f"Before stamped metal coins became universal, {trader} read about communities using {example} "
        f"to price goods and pay debts. What general category of money do {example} belong to?"
    )
    return _mcq(
        rng,
        "17_commodity_money_examples",
        prompt,
        "Commodity money",
        ["Fiat electronic money", "Bank overdraft credit", "Paper fiat banknotes"],
        f"Commodity money consists of physical items like {example}, cattle, or salt bars that hold "
        f"practical or cultural value in themselves while also serving as a medium of exchange.",
        {
            "tier_1": "Ask whether these objects have value on their own (intrinsic value) or are purely paper/digital promises.",
            "tier_2": "Distinguish physical trade goods adopted as money from government-issued paper fiat notes.",
            "tier_3": "Select the option naming physical goods used directly as currency.",
        },
        ["confuses_commodity_with_fiat_money"],
    )


def _b18(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["West African coastal markets", "East African Indian Ocean ports", "ancient Chinese trade towns"])
    shells = rng.randint(40, 120)
    prompt = (
        f"In {region}, merchants accepted {shells} cowrie shells as payment instead of grain or livestock. "
        f"Explain THREE properties that made cowrie shells effective as early commodity money."
    )
    sample = (
        f"Cowrie shells were effective because they were (1) durable and did not rot like grain, "
        f"(2) uniform in size and countable in exact amounts such as {shells} shells (divisible), and "
        f"(3) lightweight to carry and impossible to counterfeit locally."
    )
    worked = (
        f"1. **Durability [1]:** Hard calcium shells resisted moisture and decay far longer than grain or meat.\n"
        f"2. **Countability / divisibility [1]:** Small, uniform shells allowed exact prices like {shells} shells without splitting.\n"
        f"3. **Portability & scarcity [1]:** Lightweight to transport over distance and impossible to forge artificially."
    )
    return _q(
        rng,
        "18_cowrie_shells_properties",
        prompt,
        sample,
        worked,
        "Cowrie shells combined durability, small uniform units, light weight, and natural scarcity.",
        {
            "tier_1": "Think of the ideal physical characteristics of money: lasting long, splitting prices easily, and carrying easily.",
            "tier_2": f"Compare {shells} hard small shells against a sack of grain or a heavy cow.",
            "tier_3": "Give three clear properties: durability, easy counting/divisibility, and portability or anti-counterfeit scarcity.",
        },
        ["lists_irrelevant_shell_features"],
        [
            {"criterion": "Durability (does not spoil or rot)", "marks": 1},
            {"criterion": "Divisibility / uniformity (easy to count exact prices)", "marks": 1},
            {"criterion": "Portability or natural scarcity (cannot easily be forged)", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b19(rng: random.Random) -> Dict[str, Any]:
    metal = rng.choice(["silver ingots", "copper bars", "gold nuggets"])
    merchant = _pick_person(rng)
    prompt = (
        f"Before standardised stamped coins appeared, {merchant} examined early traders using {metal} in exchange "
        f"for silk and spices. What practical hassle slowed down transactions using unstamped {metal}?"
    )
    return _mcq(
        rng,
        "19_metal_ingots_weighed_silver",
        prompt,
        "Merchants had to weigh the metal on scales and test its purity during every transaction",
        [
            "Metal ingots dissolved when exposed to sunlight in open marketplaces",
            "Traders needed an internet connection to verify ingot serial numbers",
            "Unstamped metal bars could only buy agricultural crops and never spices",
        ],
        f"Unstamped {metal} varied in weight and purity, forcing buyers and sellers to carry balance scales and "
        f"assay tests to verify how much pure metal was actually changing hands.",
        {
            "tier_1": "Imagine buying cloth with an irregular lump of silver when no denomination is stamped on it.",
            "tier_2": "How would a cautious seller verify both how heavy and how pure an unstamped metal bar is?",
            "tier_3": "Choose the answer describing weighing on scales and checking purity at each trade.",
        },
        ["assumes_ingots_had_fixed_face_value"],
    )


def _b20(rng: random.Random) -> Dict[str, Any]:
    kingdom = rng.choice(["ancient Lydia", "early Chinese mints", "classical Mediterranean ports"])
    trader = _pick_person(rng)
    weight_g = rng.randint(5, 15)
    prompt = (
        f"In {kingdom}, rulers began stamping a royal seal onto {weight_g} g pieces of precious metal to make coins. "
        f"Explain to {trader} how official mint stamping sped up marketplace transactions."
    )
    sample = (
        f"An official royal stamp guaranteed both the exact weight ({weight_g} g) and metal purity of each coin, "
        f"so traders like {trader} could simply count coins instead of weighing and testing metal every time they traded."
    )
    worked = (
        f"1. **Guaranteed weight & purity [1]:** The ruler's emblem certified each coin's {weight_g} g mass and fineness.\n"
        f"2. **Faster exchange [1]:** Sellers no longer needed balance scales at every sale, allowing quick counting by unit."
    )
    return _q(
        rng,
        "20_early_stamped_coins_lydia_china",
        prompt,
        sample,
        worked,
        "Official mint stamps created public trust in standardised coin weight and purity, turning weighing into fast counting.",
        {
            "tier_1": "Recall what problem unstamped metal ingots caused before rulers stamped coins.",
            "tier_2": f"Think about what the royal seal guaranteed regarding the {weight_g} g piece of metal.",
            "tier_3": "State that stamping certified exact weight and purity, allowing traders to count coins instead of weighing them.",
        },
        ["misses_trust_guarantee_of_mint_stamp"],
        [
            {"criterion": "Stamp guarantees standardised weight and purity", "marks": 1},
            {"criterion": "Eliminates repeated weighing/testing, allowing fast counting", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b21(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Complete the table classifying historical metal coinage materials according to their typical value tier or minting purpose."
    )
    row_specs = [
        {
            "cells": ["Gold", None],
            "expected": ["High-value large transactions"],
            "cell_hints": ["Scarcest precious metal used for high-denomination trade."],
        },
        {
            "cells": ["Silver", None],
            "expected": ["Medium-value everyday trade"],
            "cell_hints": ["Intermediate precious metal between gold and copper."],
        },
        {
            "cells": ["Copper / Bronze", None],
            "expected": ["Low-value small change"],
            "cell_hints": ["Common base metal minted for small everyday purchases."],
        },
        {
            "cells": ["Mixed alloy (e.g. nickel-brass)", None],
            "expected": ["Hardness and durability"],
            "cell_hints": ["Pure precious metals are soft and wear down quickly when circulated."],
        },
    ]
    return _table_q(
        rng,
        "21_coin_metals_gold_silver_copper",
        prompt,
        ["Coin Metal / Feature", "Primary Minting Role"],
        row_specs,
        "Mints matched scarce metals (gold, silver) to higher values, base metals (copper) to small change, and mixed alloys to protect coins from wear.",
        {
            "tier_1": "Compare the rarity of gold, silver, and copper, plus why pure soft metals are mixed with harder metals.",
            "tier_2": "Match the most expensive metal to large payments and the most common base metal to small change.",
            "tier_3": "Assign Gold->High-value, Silver->Medium-value, Copper->Low-value small change, Alloy->Hardness and durability.",
        },
        ["confuses_coin_metal_value_tiers"],
    )


def _b22(rng: random.Random) -> Dict[str, Any]:
    note_year = rng.choice(["1892 (ZAR Mint)", "1923 (Pretoria Royal Mint)", "1961 (Decimal Rand)"])
    diag = _svg_timeline(
        "South African Coinage History Milestones",
        [
            ("1652", "Dutch guilders & riksdaalders"),
            ("1806+", "British pounds & shillings"),
            ("1961", "Decimal Rand (R) & cents"),
            ("Modern", note_year),
        ],
    )
    prompt = (
        f"Refer to the timeline of South African currency history highlighting {note_year}. "
        f"Identify the European currencies that circulated in early South Africa before 1961, and state what happened in 1961."
    )
    sample = (
        "Before 1961, early South Africa used Dutch currency (guilders and riksdaalders from 1652) followed by "
        "British imperial currency (pounds, shillings, and pence from 1806 onward). In 1961, South Africa decimalised "
        "its currency and introduced the Rand (R) divided into 100 cents."
    )
    worked = (
        "1. **Pre-1961 currencies [2]:** Dutch guilders/riksdaalders (1652 Cape settlement) and British pounds/shillings/pence (19th-mid 20th century).\n"
        "2. **1961 change [1]:** Introduction of the decimalised **South African Rand (R)** = 100 cents on 14 February 1961."
    )
    return _q(
        rng,
        "22_sa_coinage_history_timeline",
        prompt,
        sample,
        worked,
        "South African currency evolved from Dutch and British colonial coinage to the sovereign decimal Rand in 1961.",
        {
            "tier_1": "Read the first three milestones on the South African timeline carefully.",
            "tier_2": "Identify both colonial powers whose coins circulated prior to 1961, then describe the 1961 change.",
            "tier_3": "Name Dutch guilders/riksdaalders, British pounds/shillings, and the 1961 switch to Rand and cents.",
        },
        ["forgets_colonial_coinage_before_1961"],
        [
            {"criterion": "Mentions Dutch guilders/riksdaalders", "marks": 1},
            {"criterion": "Mentions British pounds/shillings/pence", "marks": 1},
            {"criterion": "Explains 1961 decimalisation into Rand and cents", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b23(rng: random.Random) -> Dict[str, Any]:
    pounds = rng.randint(15, 85)
    shillings = rng.choice([0, 10])
    rand_total = pounds * 2 + (1 if shillings == 10 else 0)
    buyer = _pick_person(rng)
    shil_text = f" and {shillings} shillings" if shillings else ""
    prompt = (
        f"When South Africa adopted the decimal Rand on 14 February 1961, the conversion rate was £1 = R2 "
        f"(with 20 shillings in £1, so 10 shillings = R1). If {buyer} held £{pounds}{shil_text} in savings, "
        f"what was its equivalent value in Rands (R)?"
    )
    worked = (
        f"1. **Convert pounds [1]:** £{pounds} x 2 = R{pounds * 2}.\n"
        + (f"2. **Add shillings [1]:** {shillings} shillings = R1 -> R{pounds * 2} + R1 = **{_fmt_rand(rand_total)}**." if shillings else f"2. **Total value [1]:** **{_fmt_rand(rand_total)}**.")
    )
    return _q(
        rng,
        "23_decimalisation_pound_to_rand_1961",
        prompt,
        _fmt_rand(rand_total),
        worked,
        "At decimalisation in 1961, one British pound converted into exactly two Rand, and ten shillings into one Rand.",
        {
            "tier_1": "Multiply the number of pounds by 2 to convert pounds into Rand.",
            "tier_2": "Remember that 10 shillings equals half a pound, which converts to R1.",
            "tier_3": f"Compute ({pounds} x 2)" + (" + 1" if shillings else "") + " in Rand.",
        },
        ["halves_pounds_instead_of_doubling"],
        [
            {"criterion": f"Converts £{pounds} to R{pounds * 2}", "marks": 1},
            {"criterion": f"States final amount {_fmt_rand(rand_total)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b24(rng: random.Random) -> Dict[str, Any]:
    merchant = _pick_person(rng)
    town1 = _pick_place(rng, rural=False)
    town2 = _pick_place(rng, rural=True)
    bags = rng.randint(4, 10)
    prompt = (
        f"{merchant} needed to travel from {town1} to {town2} carrying {bags} heavy leather sacks of silver coins "
        f"to buy wholesale stock. Which historical disadvantage of relying solely on metal coins is highlighted here?"
    )
    return _mcq(
        rng,
        "24_metal_coinage_disadvantages",
        prompt,
        "Large coin payments are heavy to carry and expose travellers to high robbery risk",
        [
            "Metal coins decompose into soil within two weeks of transport",
            "Silver coins cannot be divided into smaller change under any system",
            "Metal coins require electricity and mobile towers to confirm payment",
        ],
        "Although metal coins improved on barter, transporting large sums in heavy sacks was exhausting and "
        "attracted bandits, motivating merchants to invent promissory notes and paper money.",
        {
            "tier_1": "Think of the physical difficulty and danger of moving sacks full of heavy metal along roads.",
            "tier_2": "Ignore false claims about coins decomposing quickly or needing electricity.",
            "tier_3": "Pick the option describing weight and theft danger on long journeys.",
        },
        ["overlooks_coin_weight_and_robbery_risk"],
    )


def _b25(rng: random.Random) -> Dict[str, Any]:
    trader = _pick_person(rng)
    amount = rng.choice([2500, 4000, 6500, 8000])
    prompt = (
        f"To avoid carrying {_fmt_rand(amount)} worth of heavy gold coins along bandit-prone caravan trails, "
        f"{trader} writes a signed legal promise to pay the supplier later at a safe destination bank. "
        f"Which financial instrument is {trader} using?"
    )
    return _mcq(
        rng,
        "25_promissory_note_definition_purpose",
        prompt,
        "A promissory note",
        ["A till cash receipt", "A perishable commodity", "A barter livestock tally"],
        "A promissory note is a signed, unconditional written promise to pay a specific sum of money to a "
        "named payee at a stated future date or on demand, allowing safe long-distance trade without hauling heavy coins.",
        {
            "tier_1": "Notice this document is a signed written promise to pay in the future, not proof of past payment.",
            "tier_2": "Distinguish a forward promise to pay from a till receipt confirming money already handed over.",
            "tier_3": "Select the instrument whose name literally means a written promise to pay.",
        },
        ["confuses_promissory_note_with_receipt"],
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_traditional_society_definition": _b01,
    "02_modern_society_characteristics": _b02,
    "03_self_sufficiency_subsistence": _b03,
    "04_traditional_vs_modern_table": _b04,
    "05_hunter_gatherer_nomadic_living": _b05,
    "06_cattle_herding_wealth_lobola": _b06,
    "07_environment_shapes_barter_karoo_knysna": _b07,
    "08_bartering_definition_mechanism": _b08,
    "09_double_coincidence_of_wants": _b09,
    "10_silent_barter_trans_saharan": _b10,
    "11_barter_indivisibility_problem": _b11,
    "12_barter_perishability_storage": _b12,
    "13_barter_valuation_rate_calculation": _b13,
    "14_barter_advantages_context": _b14,
    "15_barter_disadvantages_table": _b15,
    "16_early_trade_routes_commodities": _b16,
    "17_commodity_money_examples": _b17,
    "18_cowrie_shells_properties": _b18,
    "19_metal_ingots_weighed_silver": _b19,
    "20_early_stamped_coins_lydia_china": _b20,
    "21_coin_metals_gold_silver_copper": _b21,
    "22_sa_coinage_history_timeline": _b22,
    "23_decimalisation_pound_to_rand_1961": _b23,
    "24_metal_coinage_disadvantages": _b24,
    "25_promissory_note_definition_purpose": _b25,
}
