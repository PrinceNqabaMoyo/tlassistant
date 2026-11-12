"""
Grade 7 EMS — Term 1: Needs and Wants — Semantic Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 1/02. Needs and Wants.md.
"""
from __future__ import annotations

import html
import random
from typing import Any, Callable, Dict, List, Optional

from ..ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

TOPIC_NAME = "Needs and Wants"
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
        "question_id": f"g7_ems_nw_{subskill}_{rng.randint(10000, 99999)}",
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
    height = 68 + len(bars) * 36
    return _svg_wrap(640, height, title, "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 01 – 25
# ---------------------------------------------------------------------------

def _b01(rng: random.Random) -> Dict[str, Any]:
    name = _pick_person(rng)
    place = _pick_place(rng, rural=True)
    need = rng.choice(["clean drinking water and basic shelter", "nutritious food and essential medicine", "warm winter clothing and sanitation"])
    prompt = (
        f"During an EMS survey in {place}, {name} lists items required immediately for human survival and health, "
        f"including {need}. What are these essential survival items called in economics?"
    )
    return _mcq(
        rng,
        "01_needs_definition_survival",
        prompt,
        "Needs",
        ["Luxury wants", "Discretionary hobbies", "Unnecessary extras"],
        "Needs are basic goods and services — such as water, food, shelter, clothing, sanitation, and healthcare — "
        "without which human survival, safety, and basic health are threatened.",
        {
            "tier_1": "Ask whether life and physical health depend directly on having these items.",
            "tier_2": "Distinguish survival essentials from non-essential desires.",
            "tier_3": "Select the economic term for essentials people cannot live without.",
        },
        ["confuses_needs_with_wants"],
    )


def _b02(rng: random.Random) -> Dict[str, Any]:
    name = _pick_person(rng)
    city = _pick_place(rng, rural=False)
    desire = rng.choice(["a designer watch and latest gaming console", "branded headphones and VIP concert tickets", "a luxury electric scooter and gourmet pastries"])
    prompt = (
        f"While window-shopping in {city}, {name} dreams about owning {desire}. Although pleasant to have, "
        f"survival is unaffected without them. How are items like {desire} classified?"
    )
    return _mcq(
        rng,
        "02_wants_definition_desires",
        prompt,
        "Wants",
        ["Primary survival needs", "Public community infrastructure", "Non-renewable capital assets"],
        "Wants are goods and services people desire to improve comfort or status, even though they can survive safely without them.",
        {
            "tier_1": "Check whether going without these items puts physical survival at risk.",
            "tier_2": "Items driven by lifestyle, fashion, or entertainment fall outside basic needs.",
            "tier_3": "Choose 'Wants'.",
        },
        ["treats_branded_luxuries_as_survival_needs"],
    )


def _b03(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    item = rng.choice([
        ("plain school shoes for walking safely to class", "limited-edition designer sneakers"),
        ("a basic nutritious lunch", "an expensive fast-food combo with gourmet milkshake"),
        ("a durable warm winter jacket", "an imported luxury branded leather jacket"),
    ])
    price_low = rng.randint(180, 320)
    price_high = rng.randint(1200, 2400)
    prompt = (
        f"{learner} compares {item[0]} costing {_fmt_rand(price_low)} with {item[1]} costing {_fmt_rand(price_high)}. "
        f"Explain why the underlying category can be a **need**, yet the specific branded upgrade becomes a **want**."
    )
    sample = (
        f"The basic item ({item[0]} at {_fmt_rand(price_low)}) satisfies a survival/health **need** for protection and daily wellbeing, "
        f"whereas paying {_fmt_rand(price_high)} for {item[1]} adds fashion prestige beyond survival, turning the upgrade into a **want**."
    )
    worked = (
        f"1. **Basic need [1]:** {item[0]} ({_fmt_rand(price_low)}) protects health/safety and is necessary for daily life.\n"
        f"2. **Upgraded want [2]:** {item[1]} ({_fmt_rand(price_high)}) costs extra purely for style, branding, or status rather than survival."
    )
    return _q(
        rng,
        "03_needs_vs_wants_distinction",
        prompt,
        sample,
        worked,
        "A basic functional product often satisfies a need, while expensive prestige upgrades reflect unlimited human wants.",
        {
            "tier_1": "Compare the functional purpose of the cheaper item against the extra cost of the luxury version.",
            "tier_2": "Ask: is the extra money buying survival protection, or fashion and prestige?",
            "tier_3": f"Classify {item[0]} as a need and explain why the {_fmt_rand(price_high)} brand version is a want.",
        },
        ["classifies_all_shoes_or_food_strictly_as_needs"],
        [
            {"criterion": f"Identifies {item[0]} as meeting a genuine basic need", "marks": 1},
            {"criterion": f"Explains {item[1]} adds status/brand desire making it a want", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b04(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    prompt = (
        f"Help {learner} classify each household item into **Need** or **Want** in the table below."
    )
    pool = [
        {"cells": ["Clean municipal tap water for drinking and cooking", None], "expected": ["Need"], "cell_hints": ["Essential for survival every day."]},
        {"cells": ["Latest video game console and wireless controllers", None], "expected": ["Want"], "cell_hints": ["Entertainment item not required for physical survival."]},
        {"cells": ["Clinic antibiotics to treat a bacterial chest infection", None], "expected": ["Need"], "cell_hints": ["Essential healthcare protects human life."]},
        {"cells": ["Designer sunglasses and imported chocolate box", None], "expected": ["Want"], "cell_hints": ["Luxury lifestyle items desired beyond basic shelter/nutrition."]},
        {"cells": ["Weatherproof house roof and warm blanket in winter", None], "expected": ["Need"], "cell_hints": ["Shelter and warmth are primary survival requirements."]},
        {"cells": ["Streaming subscription for weekend cinema releases", None], "expected": ["Want"], "cell_hints": ["Optional leisure service."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "04_needs_vs_wants_table",
        prompt,
        ["Household Item", "Classification (Need / Want)"],
        chosen,
        "Needs protect human survival and basic health; wants are optional comfort or status goods.",
        {
            "tier_1": "Test each row: can a family stay healthy and survive without it?",
            "tier_2": "Water, medicine, and shelter protect life; games, luxury snacks, and cinema subscriptions do not.",
            "tier_3": "Write 'Need' for survival essentials and 'Want' for leisure or luxury upgrades.",
        },
        ["marks_entertainment_as_survival_need"],
    )


def _b05(rng: random.Random) -> Dict[str, Any]:
    family = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    prompt = (
        f"After a winter storm in {town}, {family}'s family immediately secures the essentials listed in South African "
        f"EMS as **primary needs**. Which group consists strictly of primary survival needs?"
    )
    return _mcq(
        rng,
        "05_primary_needs_survival_list",
        prompt,
        "Water, nutritious food, shelter, basic clothing, and emergency healthcare",
        [
            "High-speed gaming fibre, overseas holidays, and sports cars",
            "Tertiary university textbooks, club sports gear, and concert passes",
            "Gold jewellery, branded cosmetics, and restaurant takeaways",
        ],
        "Primary needs are the immediate biological and safety essentials — clean water, basic food, shelter, clothing, and life-saving healthcare.",
        {
            "tier_1": "Focus strictly on immediate physical survival needs.",
            "tier_2": "Secondary needs (like education or recreation) and luxury wants come only after survival essentials.",
            "tier_3": "Pick the list containing water, food, shelter, basic clothes, and healthcare.",
        },
        ["confuses_secondary_needs_with_primary_survival"],
    )


def _b06(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    sec_ex = rng.choice(["public transport and schooling", "safe electricity and internet access for homework", "community sports facilities and vocational training"])
    prompt = (
        f"Once a household has safe shelter, clean water, and enough food, {learner} notes that families also seek "
        f"{sec_ex}. Define **secondary needs** and explain why satisfying them matters for human development."
    )
    sample = (
        f"Secondary needs are non-immediate physical survival needs that support comfort, education, social belonging, "
        f"and productivity (such as {sec_ex}). Satisfying them improves quality of life, skills, and future income opportunities."
    )
    worked = (
        f"1. **Definition [1]:** Secondary needs go beyond bare physical survival to cover psychological, social, educational, and convenience wellbeing.\n"
        f"2. **Importance [2]:** Access to {sec_ex} builds knowledge, community connection, and better long-term employment prospects."
    )
    return _q(
        rng,
        "06_secondary_needs_wellbeing",
        prompt,
        sample,
        worked,
        "Secondary needs elevate life above basic survival by enabling learning, mobility, social inclusion, and economic growth.",
        {
            "tier_1": "Distinguish staying alive today (primary) from developing skills, comfort, and belonging (secondary).",
            "tier_2": f"Think about how {sec_ex} impacts a young South African's future opportunities.",
            "tier_3": "Define secondary needs and link them to quality of life, education, and earning potential.",
        },
        ["confuses_secondary_needs_with_frivolous_wants"],
        [
            {"criterion": "Defines secondary needs (comfort, social, educational wellbeing beyond survival)", "marks": 1},
            {"criterion": f"Explains impact of {sec_ex} on productivity/quality of life", "marks": 2},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b07(rng: random.Random) -> Dict[str, Any]:
    city = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each requirement observed in {city} as either a **Primary Need** or a **Secondary Need**."
    )
    pool = [
        {"cells": ["25 litres per person of clean drinking water daily", None], "expected": ["Primary Need"], "cell_hints": ["Direct biological survival requirement."]},
        {"cells": ["Weatherproof brick home protecting a family from cold rain", None], "expected": ["Primary Need"], "cell_hints": ["Basic physical shelter for survival."]},
        {"cells": ["Public library books and computer access for high school projects", None], "expected": ["Secondary Need"], "cell_hints": ["Educational growth after survival is met."]},
        {"cells": ["Safe community park and youth soccer club membership", None], "expected": ["Secondary Need"], "cell_hints": ["Social and recreational wellbeing."]},
        {"cells": ["Basic staple food (maize meal, beans, vegetables)", None], "expected": ["Primary Need"], "cell_hints": ["Core daily nutrition for survival."]},
        {"cells": ["Reliable commuter bus route to reach technical college", None], "expected": ["Secondary Need"], "cell_hints": ["Mobility supporting learning and employment."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "07_primary_vs_secondary_table",
        prompt,
        ["Requirement", "Need Tier (Primary Need / Secondary Need)"],
        chosen,
        "Primary needs ensure immediate physical survival (food, water, shelter), while secondary needs support education, transport, social growth, and comfort.",
        {
            "tier_1": "Separate biological survival (today) from education, recreation, and transport (wellbeing).",
            "tier_2": "Water, shelter, and staple food are Primary Needs; libraries, sports clubs, and buses are Secondary Needs.",
            "tier_3": "Use exact labels: 'Primary Need' or 'Secondary Need'.",
        },
        ["blurs_primary_survival_with_secondary_growth"],
    )


def _b08(rng: random.Random) -> Dict[str, Any]:
    parent = _pick_person(rng)
    budget = rng.choice([2500, 3000, 3600])
    food_cost = rng.choice([1100, 1300, 1500])
    water_elec = rng.choice([450, 550, 650])
    med_cost = rng.choice([250, 350])
    total_primary = food_cost + water_elec + med_cost
    remaining = budget - total_primary
    diag = _svg_bars(
        f"{parent}'s Monthly Priority Budget ({_fmt_rand(budget)})",
        [
            ("Staple Food (Primary)", food_cost, "#16a34a"),
            ("Water & Power (Primary)", water_elec, "#0284c7"),
            ("Clinic Medicine (Primary)", med_cost, "#0d9488"),
            ("Total Budget Limit", budget, "#475569"),
        ],
    )
    prompt = (
        f"Refer to the budget diagram showing {parent}'s total monthly budget of {_fmt_rand(budget)} and three primary "
        f"survival expenses: Staple Food ({_fmt_rand(food_cost)}), Water & Power ({_fmt_rand(water_elec)}), and "
        f"Clinic Medicine ({_fmt_rand(med_cost)}). After prioritising all three primary needs first, how many Rands remain "
        f"for secondary needs or savings?"
    )
    worked = (
        f"1. **Total primary needs [1]:** {_fmt_rand(food_cost)} + {_fmt_rand(water_elec)} + {_fmt_rand(med_cost)} = {_fmt_rand(total_primary)}.\n"
        f"2. **Remaining Rand balance [1]:** {_fmt_rand(budget)} - {_fmt_rand(total_primary)} = **{_fmt_rand(remaining)}**."
    )
    return _q(
        rng,
        "08_prioritising_primary_over_secondary",
        prompt,
        _fmt_rand(remaining),
        worked,
        "Sound financial planning funds primary survival needs before allocating remaining funds to secondary needs or wants.",
        {
            "tier_1": "Add up the three primary expense bars first.",
            "tier_2": f"Subtract ({_fmt_rand(food_cost)} + {_fmt_rand(water_elec)} + {_fmt_rand(med_cost)}) from {_fmt_rand(budget)}.",
            "tier_3": f"Compute {_fmt_rand(budget)} - {_fmt_rand(total_primary)} = {_fmt_rand(remaining)}.",
        },
        ["spends_on_wants_before_totalling_primary_needs"],
        [
            {"criterion": f"Sums primary needs = {_fmt_rand(total_primary)}", "marks": 1},
            {"criterion": f"Subtracts from budget to obtain {_fmt_rand(remaining)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b09(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    need_example = rng.choice(["nutritious breakfast and a calm place to study", "clean water, warm sleepwear, and personal safety"])
    prompt = (
        f"In EMS, needs are studied across individuals, families, communities, and countries. If {learner} needs "
        f"{need_example}, which level of needs is directly illustrated?"
    )
    return _mcq(
        rng,
        "09_needs_of_individuals",
        prompt,
        "Individual needs",
        ["National defence needs", "International export tariffs", "Municipal sewerage contracts"],
        "Individual needs refer to the personal physical, safety, and developmental requirements of one person, such as nutrition, clothing, rest, and study space.",
        {
            "tier_1": "Look at who directly experiences this need: one learner or the whole municipal town?",
            "tier_2": "Distinguish personal survival/study requirements from shared public infrastructure.",
            "tier_3": "Select 'Individual needs'.",
        },
        ["confuses_individual_and_national_needs"],
    )


def _b10(rng: random.Random) -> Dict[str, Any]:
    parent, child = _pick_two_people(rng)
    home = _pick_place(rng, rural=False)
    prompt = (
        f"In {home}, {parent} provides {child}'s household with brick walls, electricity, and groceries. "
        f"Beyond physical shelter and food, state and briefly explain THREE non-material needs (emotional, social, "
        f"or intellectual) that healthy families require."
    )
    sample = (
        f"Healthy families also need (1) emotional support, love, and security so members feel safe; "
        f"(2) social belonging and communication to resolve conflicts constructively; and "
        f"(3) intellectual stimulation, education, and spiritual/creative expression to develop each member's potential."
    )
    worked = (
        f"1. **Emotional security & love [1]:** Care, encouragement, and psychological safety at home.\n"
        f"2. **Social belonging & respect [1]:** Healthy family communication, companionship, and shared traditions.\n"
        f"3. **Intellectual / spiritual / creative needs [1]:** Supporting schooling, curiosity, values, and personal hobbies."
    )
    return _q(
        rng,
        "10_family_emotional_social_needs",
        prompt,
        sample,
        worked,
        "South African EMS syllabus highlights that family needs encompass emotional, social, intellectual, spiritual, and creative dimensions alongside food and shelter.",
        {
            "tier_1": "Think about what keeps a family thriving emotionally and mentally after food and roof are provided.",
            "tier_2": "Recall the non-material family categories: emotional, social, intellectual, spiritual, or creative.",
            "tier_3": "State and explain any three: love/emotional safety, social belonging, and intellectual/educational support.",
        },
        ["limits_family_needs_only_to_food_and_shelter"],
        [
            {"criterion": "Emotional need (love, security, care)", "marks": 1},
            {"criterion": "Social need (belonging, family communication)", "marks": 1},
            {"criterion": "Intellectual, spiritual, or creative development need", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b11(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    infra = rng.choice(["a working primary clinic, piped clean water, and safe tarred roads", "street lighting, refuse removal, and reliable storm-water drainage"])
    prompt = (
        f"Residents across {town} petition their local ward councillor for {infra}. "
        f"Which category of needs is this neighbourhood requesting?"
    )
    return _mcq(
        rng,
        "11_community_needs_infrastructure",
        prompt,
        "Community needs",
        ["Private luxury wants", "Individual personal hobbies", "Corporate shareholder dividends"],
        "Community needs are shared public facilities and services — clinics, piped water, roads, street lights, refuse removal, and schools — required by an entire neighbourhood.",
        {
            "tier_1": "Ask whether one household builds its own municipal clinic and tarred road, or whether the whole neighbourhood shares them.",
            "tier_2": "Shared neighbourhood facilities fall between family needs and national defence.",
            "tier_3": "Pick 'Community needs'.",
        },
        ["mistakes_public_community_services_for_private_wants"],
    )


def _b12(rng: random.Random) -> Dict[str, Any]:
    country_sector = rng.choice(["public hospitals and pandemic readiness", "national power grid reliability", "rail freight corridors and clean water dams"])
    name = _pick_person(rng)
    prompt = (
        f"In a Grade 7 EMS debate, {name} highlights the importance of {country_sector} for South Africa. "
        f"Give TWO other examples of **national (country) needs** and explain why central government must coordinate them."
    )
    sample = (
        f"Two other national needs are (1) national defence/policing to protect borders and citizens, and "
        f"(2) nationwide public education and food-security systems. Central government coordinates them because "
        f"they require nationwide laws, huge tax funding, and equal access across all nine provinces."
    )
    worked = (
        f"1. **Two national examples [2]:** National defence/border security, nationwide education system, national highways, or law courts (any two valid).\n"
        f"2. **Why central coordination [1]:** Individual households and single towns lack the budget and legal authority to fund nationwide systems equitably."
    )
    return _q(
        rng,
        "12_country_national_needs",
        prompt,
        sample,
        worked,
        "Country needs protect sovereignty, macroeconomic stability, nationwide infrastructure, and equal development across provinces.",
        {
            "tier_1": "Think of systems needed by all 60+ million citizens across every province, not just one suburb.",
            "tier_2": "Consider defence, courts, national highways, dams, and nationwide schooling/health systems.",
            "tier_3": "List two clear country needs and explain the scale of nationwide tax funding and coordination.",
        },
        ["gives_household_examples_as_country_needs"],
        [
            {"criterion": "Valid national need example 1 (e.g. defence, courts, national grid)", "marks": 1},
            {"criterion": "Valid national need example 2 (e.g. education policy, national roads)", "marks": 1},
            {"criterion": "Explains why nationwide scale/funding requires government", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b13(rng: random.Random) -> Dict[str, Any]:
    person = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        "Match each example to the correct level of society: **Individual**, **Family**, **Community**, or **Country**."
    )
    row_specs = [
        {
            "cells": [f"{person} needs warm school shoes and sleep before exams", None],
            "expected": ["Individual"],
            "cell_hints": ["Focuses on one learner's personal survival and study wellbeing."],
        },
        {
            "cells": ["Parents and children sharing emotional support, care, and a safe home", None],
            "expected": ["Family"],
            "cell_hints": ["Household unit providing love, shelter, and guidance."],
        },
        {
            "cells": [f"Refuse collection trucks and streetlights serving all streets in {town}", None],
            "expected": ["Community"],
            "cell_hints": ["Shared municipal neighbourhood services."],
        },
        {
            "cells": ["National border defence and South Africa's judicial court system", None],
            "expected": ["Country"],
            "cell_hints": ["Sovereign systems serving the entire nation."],
        },
    ]
    return _table_q(
        rng,
        "13_four_levels_of_needs_table",
        prompt,
        ["Need Example", "Society Level"],
        row_specs,
        "Economic needs expand in scale from Individuals and Families up to local Communities and the Country as a whole.",
        {
            "tier_1": "Match scale: single person -> household -> local town -> entire nation.",
            "tier_2": "Look for scope clues: one learner, parents & children, neighbourhood streets, national borders.",
            "tier_3": "Assign Individual, Family, Community, and Country.",
        },
        ["mixes_community_and_country_levels"],
    )


def _b14(rng: random.Random) -> Dict[str, Any]:
    teen = _pick_person(rng)
    trend = rng.choice(["social media influencer ads", "shiny sneaker billboards", "friends upgrading smartphones"])
    prompt = (
        f"Every time {teen} buys one item on a wish-list, {trend} quickly spark desire for three more products. "
        f"Explain TWO economic reasons why human wants are described as **unlimited**."
    )
    sample = (
        f"Human wants are unlimited because (1) satisfying one want immediately creates new desires as incomes and expectations rise, "
        f"and (2) persuasive advertising and peer trends ({trend}) continually invent new fashionable products people aspire to own."
    )
    worked = (
        f"1. **Insatiable nature [1]:** Once a desire is satisfied, tastes expand and people desire upgrades or variety.\n"
        f"2. **Marketing & innovation [1]:** {trend.capitalize()} and new technology continually create fresh wants that never run out."
    )
    return _q(
        rng,
        "14_unlimited_wants_advertising_effect",
        prompt,
        sample,
        worked,
        "Unlike limited physical survival needs, human desires grow continuously through innovation, advertising, and social comparison.",
        {
            "tier_1": "Ask why reaching a wish-list goal rarely stops people from wanting the next item.",
            "tier_2": "Think of both inner human nature (rising expectations) and outside triggers (ads, technology, peers).",
            "tier_3": "State two reasons: wants regenerate after satisfaction, and marketing/innovation keep creating new desires.",
        },
        ["thinks_wants_stop_once_a_budget_increases"],
        [
            {"criterion": "Explains psychological growth/upgrades once current wants are met", "marks": 1},
            {"criterion": "Explains impact of advertising, peers, or new technology", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b15(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    scarce = rng.choice(["fresh water during a summer drought", "municipal funds for road repairs", "fertile farming soil"])
    prompt = (
        f"In {town}, demand for {scarce} exceeds the limited amount available. Which single economic concept "
        f"describes a shortage of resources relative to unlimited human wants?"
    )
    return _mcq(
        rng,
        "15_limited_resources_scarcity_definition",
        prompt,
        "Scarcity",
        ["Self-sufficiency", "Hyper-abundance", "Consumer surplus"],
        "Scarcity arises because natural resources, money, labour, and time are finite while human wants are virtually endless.",
        {
            "tier_1": "Name the fundamental condition where there is never enough of a resource to satisfy every single want.",
            "tier_2": "Eliminate words suggesting excess abundance or household isolation.",
            "tier_3": "Choose 'Scarcity'.",
        },
        ["confuses_scarcity_with_zero_quantity"],
    )


def _b16(rng: random.Random) -> Dict[str, Any]:
    earner = _pick_person(rng)
    income = rng.choice([3200, 4000, 4800])
    wishes = rng.choice([7500, 9200, 10500])
    gap = wishes - income
    diag = _svg_bars(
        f"The Basic Economic Problem — {earner}",
        [
            ("Limited Income", income, "#2563eb"),
            ("Unlimited Wish-List", wishes, "#dc2626"),
        ],
    )
    prompt = (
        f"Refer to the diagram comparing {earner}'s limited monthly income ({_fmt_rand(income)}) against household "
        f"wish-list desires ({_fmt_rand(wishes)}), leaving a {_fmt_rand(gap)} gap. Define **the basic economic problem** "
        f"and explain what {earner} is forced to do as a result."
    )
    sample = (
        f"The basic economic problem is that human wants ({_fmt_rand(wishes)}) are unlimited while economic resources "
        f"such as money ({_fmt_rand(income)}) are scarce/limited. Therefore, {earner} cannot afford everything and is "
        f"forced to make choices by prioritising needs first and giving up lower-priority wants."
    )
    worked = (
        f"1. **Basic economic problem [2]:** Unlimited wants ({_fmt_rand(wishes)}) collide with limited scarce resources ({_fmt_rand(income)}).\n"
        f"2. **Forced action [1]:** {earner} must make **choices** (ranking needs ahead of wants) and accept opportunity costs worth {_fmt_rand(gap)}."
    )
    return _q(
        rng,
        "16_basic_economic_problem_statement",
        prompt,
        sample,
        worked,
        "Scarcity forces every individual, firm, and government to choose how best to allocate limited resources.",
        {
            "tier_1": "Combine two facts visible in the two bars: resources are finite, desires are larger.",
            "tier_2": "What consequence follows when income cannot cover the whole wish-list?",
            "tier_3": "State unlimited wants vs scarce resources, and explain forced prioritisation/choices.",
        },
        ["only_defines_budget_deficit_without_scarcity"],
        [
            {"criterion": "States unlimited human wants vs scarce/limited resources", "marks": 2},
            {"criterion": "Explains forced economic choices and prioritisation", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b17(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    budget = rng.choice([300, 400, 500])
    bag = rng.choice([210, 240, 260])
    shoes = rng.choice([180, 220, 250])
    headset = rng.choice([140, 170, 190])
    total_want = bag + shoes + headset
    shortfall = total_want - budget
    prompt = (
        f"{learner} has a limited allowance of {_fmt_rand(budget)}, yet wants to buy a school bag ({_fmt_rand(bag)}), "
        f"running shoes ({_fmt_rand(shoes)}), and a headset ({_fmt_rand(headset)}). "
        f"Calculate how many Rands {learner} is short to buy all three items."
    )
    worked = (
        f"1. **Total cost of all wants [1]:** {_fmt_rand(bag)} + {_fmt_rand(shoes)} + {_fmt_rand(headset)} = {_fmt_rand(total_want)}.\n"
        f"2. **Shortfall due to scarcity [1]:** {_fmt_rand(total_want)} - {_fmt_rand(budget)} = **{_fmt_rand(shortfall)}**."
    )
    return _q(
        rng,
        "17_scarcity_choice_budget_calculation",
        prompt,
        _fmt_rand(shortfall),
        worked,
        "Calculating the Rand gap illustrates scarcity concretely and shows why items must be prioritised.",
        {
            "tier_1": "Add the prices of all three desired items together first.",
            "tier_2": f"Subtract {learner}'s available {_fmt_rand(budget)} from the combined price.",
            "tier_3": f"Compute ({_fmt_rand(bag)} + {_fmt_rand(shoes)} + {_fmt_rand(headset)}) - {_fmt_rand(budget)}.",
        },
        ["subtracts_only_two_items"],
        [
            {"criterion": f"Sums all three items = {_fmt_rand(total_want)}", "marks": 1},
            {"criterion": f"Calculates shortfall = {_fmt_rand(shortfall)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b18(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    cash = rng.choice([250, 300, 350])
    opt_a = rng.choice(["a warm school jersey", "an EMS textbook and calculator", "school track pants"])
    opt_b = rng.choice(["cinema tickets and snacks", "a trendy phone case", "two video game skins"])
    prompt = (
        f"{buyer} has {_fmt_rand(cash)} saved and must choose between spending it on {opt_a} OR on {opt_b} "
        f"(both cost {_fmt_rand(cash)}). If {buyer} chooses {opt_a}, identify the **opportunity cost** and define the term."
    )
    sample = (
        f"The opportunity cost is **{opt_b}** (worth {_fmt_rand(cash)}). Opportunity cost is the value of the "
        f"next-best alternative that is given up whenever a choice is made with scarce resources."
    )
    worked = (
        f"1. **Opportunity cost here [1]:** **{opt_b}** (valued at {_fmt_rand(cash)}).\n"
        f"2. **Definition [1]:** Opportunity cost is the next-best alternative sacrificed when choosing one option over another due to scarcity."
    )
    return _q(
        rng,
        "18_opportunity_cost_tradeoff",
        prompt,
        sample,
        worked,
        "Every economic choice carries an opportunity cost equal to the best alternative option forfeited.",
        {
            "tier_1": "Look at what item was NOT bought because the scarce Rands went to the chosen item.",
            "tier_2": "Opportunity cost is not the Rand amount spent alone; it is the sacrificed alternative option.",
            "tier_3": f"State {opt_b} as the opportunity cost and define it as the next-best alternative given up.",
        },
        ["thinks_opportunity_cost_means_price_paid"],
        [
            {"criterion": f"Identifies {opt_b} as the sacrificed alternative", "marks": 1},
            {"criterion": "Accurately defines opportunity cost as next-best alternative foregone", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b19(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    free_mins = rng.choice([180, 210, 240])
    ems_mins = rng.choice([60, 75, 90])
    math_mins = rng.choice([60, 75])
    left_mins = free_mins - ems_mins - math_mins
    prompt = (
        f"Scarcity affects time as well as money. {learner} has {free_mins} free minutes after school, spends "
        f"{ems_mins} minutes revising EMS and {math_mins} minutes on Mathematics. How many minutes remain for "
        f"sport or rest?"
    )
    worked = (
        f"1. **Study time used [1]:** {ems_mins} + {math_mins} = {ems_mins + math_mins} minutes.\n"
        f"2. **Remaining minutes [1]:** {free_mins} - {ems_mins + math_mins} = **{left_mins} minutes**."
    )
    return _q(
        rng,
        "19_scarce_time_allocation_choice",
        prompt,
        f"{left_mins} minutes",
        worked,
        "Time is an inelastic scarce resource (24 hours per day), forcing learners to allocate minutes thoughtfully.",
        {
            "tier_1": "Add the two study blocks together first.",
            "tier_2": f"Subtract total study minutes from {free_mins} minutes.",
            "tier_3": f"Compute {free_mins} - ({ems_mins} + {math_mins}) = {left_mins} minutes.",
        },
        ["forgets_to_subtract_second_study_block"],
        [
            {"criterion": f"Sums study time = {ems_mins + math_mins} minutes", "marks": 1},
            {"criterion": f"Finds remaining {left_mins} minutes", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b20(rng: random.Random) -> Dict[str, Any]:
    home = _pick_place(rng, rural=False)
    old_l = rng.choice([300, 360, 420])
    new_l = rng.choice([180, 210, 240])
    saved_daily = old_l - new_l
    saved_month = saved_daily * 30
    diag = _svg_bars(
        f"{home} Household Daily Water Usage (Litres)",
        [
            ("Before Water-Saving", old_l, "#ef4444"),
            ("After Fixing Leaks", new_l, "#10b981"),
        ],
        unit_prefix="",
        unit_suffix=" L",
    )
    prompt = (
        f"Refer to the diagram comparing daily household water use in {home} before ({old_l} L/day) and after fixing leaks "
        f"({new_l} L/day). Calculate how many litres of scarce municipal water this household saves over a 30-day month."
    )
    worked = (
        f"1. **Daily saving [1]:** {old_l} L - {new_l} L = {saved_daily} L per day.\n"
        f"2. **30-day monthly saving [1]:** {saved_daily} L x 30 = **{saved_month} L**."
    )
    return _q(
        rng,
        "20_scarce_water_household_conservation",
        prompt,
        f"{saved_month} L",
        worked,
        "Reducing daily water waste stretches scarce municipal reserves substantially across an entire month.",
        {
            "tier_1": "Find how many litres are saved in a single day from the two bars first.",
            "tier_2": "Multiply the daily water saving by 30 days.",
            "tier_3": f"Compute ({old_l} - {new_l}) x 30 = {saved_month} L.",
        },
        ["forgets_to_multiply_daily_saving_by_30"],
        [
            {"criterion": f"Calculates daily saving = {saved_daily} L", "marks": 1},
            {"criterion": f"Multiplies by 30 to obtain {saved_month} L", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b21(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    gift = rng.choice(["underground platinum ore, river water, and fertile topsoil", "wild timber forests, sunlight, and coastal fisheries"])
    prompt = (
        f"In {town}, producers rely on {gift} to create goods. Under the four economic factors of production, "
        f"what category do these gifts of nature belong to?"
    )
    return _mcq(
        rng,
        "21_natural_resources_land_examples",
        prompt,
        "Natural resources (Land)",
        ["Human entrepreneurship", "Manufactured financial capital", "Skilled factory labour"],
        "Natural resources (land) include all untouched gifts of nature — fertile soil, water, minerals, sunlight, and forests — used in production.",
        {
            "tier_1": "Ask whether humans built these items in a factory or found them occurring in nature.",
            "tier_2": "Recall the four factors of production: natural resources (land), labour, capital, entrepreneurship.",
            "tier_3": "Select 'Natural resources (Land)'.",
        },
        ["confuses_raw_natural_inputs_with_capital"],
    )


def _b22(rng: random.Random) -> Dict[str, Any]:
    worker = _pick_person(rng)
    skilled = rng.choice(["electrician", "civil engineer", "nurse", "software developer"])
    unskilled = rng.choice(["fruit picker", "warehouse packer", "general cleaner"])
    prompt = (
        f"{worker} studies how people contribute to production as a {skilled} versus as a {unskilled}. "
        f"Define **labour** as a factor of production and explain the difference between **skilled** and **unskilled** labour."
    )
    sample = (
        f"Labour is the physical and mental human effort used to produce goods and services. "
        f"Skilled labour (such as a {skilled}) requires formal training, qualifications, or technical expertise, "
        f"whereas unskilled labour (such as a {unskilled}) requires minimal specialised training."
    )
    worked = (
        f"1. **Definition of labour [1]:** Human physical and mental work applied in production.\n"
        f"2. **Skilled vs unskilled [2]:** A {skilled} undergoes formal education/apprenticeship (higher specialised skill), while a {unskilled} performs tasks needing little formal qualification."
    )
    return _q(
        rng,
        "22_labour_human_effort_skills",
        prompt,
        sample,
        worked,
        "Labour encompasses all physical and intellectual work, varying in training intensity across roles.",
        {
            "tier_1": "Remember labour covers both physical strength and mental effort.",
            "tier_2": f"Compare the training years needed for a {skilled} versus a {unskilled}.",
            "tier_3": "Define labour and contrast specialised training against minimal formal training.",
        },
        ["thinks_labour_only_means_manual_physical_work"],
        [
            {"criterion": "Defines labour as human physical and mental effort", "marks": 1},
            {"criterion": f"Explains skilled labour using {skilled} (training/qualifications)", "marks": 1},
            {"criterion": f"Explains unskilled labour using {unskilled}", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b23(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    biz = rng.choice(["commercial sewing workshop", "wooden furniture factory", "bread bakery"])
    gear = rng.choice(["industrial ovens, mixing machines, and delivery vans", "heavy lathes, power saws, and workshop buildings", "overlocking machines, cutting tables, and computers"])
    prompt = (
        f"{owner} opens a {biz} equipped with {gear}. In economics, what factor of production do these man-made "
        f"machines, tools, and equipment represent?"
    )
    return _mcq(
        rng,
        "23_capital_physical_vs_money",
        prompt,
        "Capital",
        ["Natural resources (Land)", "Raw mineral ore", "Household consumption wants"],
        "Capital consists of man-made resources (machinery, tools, factories, delivery vehicles) and funds invested to produce further goods and services.",
        {
            "tier_1": "Notice these machines and buildings were manufactured by humans specifically to help make more goods.",
            "tier_2": "Do not confuse factory equipment with untouched gifts of nature (land) or worker effort (labour).",
            "tier_3": "Pick 'Capital'.",
        },
        ["thinks_capital_means_only_cash_never_machinery"],
    )


def _b24(rng: random.Random) -> Dict[str, Any]:
    founder = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    idea = rng.choice(["eco-friendly solar phone charging kiosks", "fresh school lunchbox deliveries", "recycled school-bag repairs"])
    capital_amt = rng.choice([5000, 8000, 12000])
    prompt = (
        f"In {town}, {founder} spots an unmet neighbourhood need and invests {_fmt_rand(capital_amt)} of savings to "
        f"start {idea}, hiring two assistants and organising supplies. Identify which factor of production {founder} "
        f"provides, and state TWO key qualities of this role."
    )
    sample = (
        f"{founder} provides **entrepreneurship**. Two key qualities are (1) spotting unmet needs and innovating, "
        f"and (2) organising the other three factors (land, labour, capital) while taking the financial risk of losing {_fmt_rand(capital_amt)} for potential profit."
    )
    worked = (
        f"1. **Factor of production [1]:** **Entrepreneurship**.\n"
        f"2. **Two qualities [2]:** (a) Initiative/innovation to solve an unmet need ({idea}), and (b) Risk-taking & combining land, labour, and {_fmt_rand(capital_amt)} capital."
    )
    return _q(
        rng,
        "24_entrepreneurship_role_innovation",
        prompt,
        sample,
        worked,
        "Entrepreneurs drive economic growth by combining natural resources, labour, and capital while bearing risk.",
        {
            "tier_1": "Name the fourth factor of production responsible for starting the business and taking risk.",
            "tier_2": "Consider how the founder spotted the gap and risked personal savings to coordinate everything.",
            "tier_3": "Name 'Entrepreneurship' and give two traits: innovation/coordination and financial risk-bearing.",
        },
        ["confuses_entrepreneur_with_ordinary_employee"],
        [
            {"criterion": "Identifies Entrepreneurship", "marks": 1},
            {"criterion": "Quality 1: Spotting opportunities / innovating / coordinating factors", "marks": 1},
            {"criterion": "Quality 2: Bearing financial risk to earn profit", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b25(rng: random.Random) -> Dict[str, Any]:
    founder = _pick_person(rng)
    biz = rng.choice(["maize bakery", "timber carpentry shop", "bottled fruit juice plant"])
    prompt = (
        f"Classify each input used by {founder}'s {biz} into one of the four factors of production: "
        f"**Natural Resources (Land)**, **Labour**, **Capital**, or **Entrepreneurship**."
    )
    row_specs = [
        {
            "cells": ["Clean spring water, sunlight, and raw land", None],
            "expected": ["Natural Resources (Land)"],
            "cell_hints": ["Untouched gift of nature not built by humans."],
        },
        {
            "cells": ["Trained bakers/operators working eight-hour daily shifts", None],
            "expected": ["Labour"],
            "cell_hints": ["Human physical and mental work."],
        },
        {
            "cells": ["Electric ovens, delivery bakkie, and stainless-steel tables", None],
            "expected": ["Capital"],
            "cell_hints": ["Man-made tools, equipment, and vehicles used in production."],
        },
        {
            "cells": [f"{founder}'s initiative in combining inputs and risking start-up money", None],
            "expected": ["Entrepreneurship"],
            "cell_hints": ["Founder organising the other three factors and bearing risk."],
        },
    ]
    return _table_q(
        rng,
        "25_four_factors_of_production_table",
        prompt,
        ["Business Input", "Factor of Production"],
        row_specs,
        "Every business requires all four factors — natural resources, labour, capital, and entrepreneurship — to transform scarce inputs into goods and services.",
        {
            "tier_1": "Review the four factors of production: nature, human work, man-made equipment, and business founder.",
            "tier_2": "Match raw water/land->Natural Resources, workers->Labour, ovens/bakkie->Capital, founder->Entrepreneurship.",
            "tier_3": "Fill in Natural Resources (Land), Labour, Capital, and Entrepreneurship.",
        },
        ["swaps_capital_and_natural_resources"],
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_needs_definition_survival": _b01,
    "02_wants_definition_desires": _b02,
    "03_needs_vs_wants_distinction": _b03,
    "04_needs_vs_wants_table": _b04,
    "05_primary_needs_survival_list": _b05,
    "06_secondary_needs_wellbeing": _b06,
    "07_primary_vs_secondary_table": _b07,
    "08_prioritising_primary_over_secondary": _b08,
    "09_needs_of_individuals": _b09,
    "10_family_emotional_social_needs": _b10,
    "11_community_needs_infrastructure": _b11,
    "12_country_national_needs": _b12,
    "13_four_levels_of_needs_table": _b13,
    "14_unlimited_wants_advertising_effect": _b14,
    "15_limited_resources_scarcity_definition": _b15,
    "16_basic_economic_problem_statement": _b16,
    "17_scarcity_choice_budget_calculation": _b17,
    "18_opportunity_cost_tradeoff": _b18,
    "19_scarce_time_allocation_choice": _b19,
    "20_scarce_water_household_conservation": _b20,
    "21_natural_resources_land_examples": _b21,
    "22_labour_human_effort_skills": _b22,
    "23_capital_physical_vs_money": _b23,
    "24_entrepreneurship_role_innovation": _b24,
    "25_four_factors_of_production_table": _b25,
}
