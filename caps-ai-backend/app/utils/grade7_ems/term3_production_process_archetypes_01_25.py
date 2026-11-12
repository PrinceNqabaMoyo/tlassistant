"""Grade 7 EMS — The Production Process: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards (Term 4: The Economy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 3/03. The production process.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, RURAL_AREAS, URBAN_AREAS

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term3_production_process"
TOPIC_NAME = "The production process"
CURRICULUM_REF = "Term 4 > The Economy: The Production Process"


def _fmt_zar(amount: float, decimals: int = 0) -> str:
    if decimals == 0 and float(amount).is_integer():
        return f"R{int(round(amount)):,}".replace(",", " ")
    formatted = f"{amount:,.{decimals}f}".replace(",", " ").replace(".", ",")
    return f"R{formatted}"


def _fmt_comma(val: float, decimals: int = 2) -> str:
    return f"{val:.{decimals}f}".replace(".", ",")


def _base_meta(
    subskill: str,
    learning_objective_id: str,
    concept_id: str,
    marks: int,
    duration_mins: int,
    misconception_tags: List[str],
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "topic": TOPIC_NAME,
        "grade": 7,
        "subject": "Economic and Management Sciences",
        "term": 4,
        "caps_weight_percent": 20,
        "suggested_duration_mins": duration_mins,
        "curriculum_reference": CURRICULUM_REF,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "concept_group": "production_process",
        "marks": marks,
        "total_marks": marks,
        "misconception_tags": misconception_tags,
        "diagnostic_tags": diagnostic_tags or ["production_process"],
    }


def _mcq(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    explanation: str,
    hints: Dict[str, str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    correct_idx = options.index(correct)
    letter = chr(65 + correct_idx)
    ws = f"({letter}) **{correct}** [{marks} marks]\n\n**Explanation / Working:**\n{explanation}"
    q: Dict[str, Any] = {
        **_base_meta(subskill, learning_objective_id, concept_id, marks, 2, misconception_tags),
        "id": f"g7_ems_prod_{subskill[:12]}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(correct_idx),
        "correct_answer": correct,
        "expected_answer": correct,
        "sample_answer": correct,
        "ideal_answer": correct,
        "explanation": ws,
        "worked_solution": ws,
        "canonical_solution": ws,
        "marking_points": [correct],
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}
            ],
            "carry_forward_rule": "strict",
        },
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _typed(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    sample_answer: str,
    marking_points: List[str],
    hints: Dict[str, str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    marks: Optional[int] = None,
    correct_answer: Optional[str] = None,
    correct_value: Optional[float] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
    worked_solution: Optional[str] = None,
) -> Dict[str, Any]:
    total_marks = marks if marks is not None else max(2, len(marking_points))
    ws = worked_solution or sample_answer
    ans_str = correct_answer or sample_answer
    q: Dict[str, Any] = {
        **_base_meta(subskill, learning_objective_id, concept_id, total_marks, max(3, total_marks), misconception_tags),
        "id": f"g7_ems_prod_{subskill[:12]}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "typed",
        "modality": "math" if correct_value is not None else "semantic",
        "solution_type": "numeric" if correct_value is not None else "marking_points",
        "prompt": prompt,
        "question": prompt,
        "marks": total_marks,
        "total_marks": total_marks,
        "marking_points": marking_points,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "correct_answer": ans_str,
        "expected_answer": str(correct_value) if correct_value is not None else ans_str,
        "explanation": ws,
        "worked_solution": ws,
        "canonical_solution": ws,
        "hints": hints,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": [
                {"id": f"mp_{idx + 1}", "desc": mp, "marks": 1, "editable": True}
                for idx, mp in enumerate(marking_points)
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
    }
    if correct_value is not None:
        q["correct_value"] = correct_value
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _table_q(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    raw_rows: List[List[Dict[str, Any]]],
    cell_hints: Dict[str, str],
    derivations: List[str],
    hints: Dict[str, str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
) -> Dict[str, Any]:
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    marking_points: List[Dict[str, Any]] = []
    has_must_be_empty = False

    md_header = "| " + " | ".join(headers) + " |"
    md_sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    md_rows = [md_header, md_sep]

    mp_idx = 1
    for r_idx, row in enumerate(raw_rows):
        ui_row: List[Dict[str, Any]] = []
        md_cells: List[str] = []
        for c_idx, cell in enumerate(row):
            cell_id = f"r{r_idx}_c{c_idx}"
            ctype = cell["type"]
            if ctype == "given":
                val = str(cell["value"])
                ui_row.append({"id": cell_id, "type": "given", "value": val, "label": headers[c_idx]})
                md_cells.append(val)
            elif ctype == "required":
                exp = str(cell["expected"])
                ui_row.append({"id": cell_id, "type": "required", "value": "", "expected": exp, "label": headers[c_idx]})
                correct_map[cell_id] = exp
                marking_points.append({"id": f"mp_{mp_idx}", "desc": f"{headers[c_idx]} (Row {r_idx + 1}): {exp}", "marks": 1, "editable": True})
                mp_idx += 1
                md_cells.append(f"**{exp}**")
            else:
                has_must_be_empty = True
                ui_row.append({"id": cell_id, "type": "must_be_empty", "value": "", "expected": "", "label": headers[c_idx]})
                correct_map[cell_id] = ""
                md_cells.append("*(blank)*")
        rows.append(ui_row)
        md_rows.append("| " + " | ".join(md_cells) + " |")

    marks = max(1, len(marking_points))
    md_table = "\n".join(md_rows)
    deriv_text = "\n".join(f"- {d}" for d in derivations)
    memo = f"{md_table}\n\n**Derivations & Rules:**\n{deriv_text}"
    deductions = [{"rule": "must_be_empty_filled", "penalty": -1}] if has_must_be_empty else []

    return {
        **_base_meta(subskill, learning_objective_id, concept_id, marks, max(4, marks), misconception_tags),
        "id": f"g7_ems_prod_tbl_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": marks,
        "total_marks": marks,
        "sample_answer": memo,
        "ideal_answer": memo,
        "expected_answer": "; ".join(f"{k}={v}" for k, v in correct_map.items()),
        "correct_answer": "; ".join(f"{k}={v}" for k, v in correct_map.items()),
        "worked_solution": memo,
        "canonical_solution": memo,
        "explanation": memo,
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": deductions,
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _svg_bar_chart(
    title: str,
    y_label: str,
    bars: List[Tuple[str, float, str]],
    max_val: float,
    unit_suffix: str = "%",
) -> str:
    w, h = 620, 300
    left, top, right, bottom = 75, 52, 585, 240
    chart_h = bottom - top
    n = len(bars)
    slot_w = (right - left) / max(1, n)
    bar_w = min(68, slot_w * 0.56)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:620px;background:#FFFFFF;font-family:Arial,sans-serif;">',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#FAF8F3" stroke="#CBD5E1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">{title}</text>',
    ]
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = bottom - frac * chart_h
        tick_val = round(max_val * frac, 1)
        tick_lbl = str(int(tick_val)) if float(tick_val).is_integer() else _fmt_comma(tick_val, 1)
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="#E2E8F0" stroke-width="1"/>')
        lines.append(f'<text x="{left-8}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#475569">{tick_lbl}{unit_suffix}</text>')

    lines.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#1E293B" stroke-width="2"/>')
    lines.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#1E293B" stroke-width="2"/>')
    lines.append(
        f'<text x="20" y="{(top+bottom)//2}" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155" transform="rotate(-90 20 {(top+bottom)//2})">{y_label}</text>'
    )

    for idx, (label, val, color) in enumerate(bars):
        cx = left + slot_w * (idx + 0.5)
        bx = cx - bar_w / 2
        bh = (val / max(1e-6, max_val)) * chart_h
        by = bottom - bh
        val_lbl = f"{int(val)}{unit_suffix}" if float(val).is_integer() else f"{_fmt_comma(val, 1)}{unit_suffix}"
        lines.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" rx="4" fill="{color}" stroke="#0F172A" stroke-width="1"/>')
        lines.append(f'<text x="{cx:.1f}" y="{by-6:.1f}" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">{val_lbl}</text>')
        lines.append(f'<text x="{cx:.1f}" y="{bottom+18}" text-anchor="middle" font-size="11" font-weight="bold" fill="#1E293B">{label}</text>')

    lines.append("</svg>")
    return "".join(lines)


def _svg_linear_flow(
    title: str,
    stages: List[Tuple[str, str, str]],
) -> str:
    w, h = 660, 175
    n = len(stages)
    box_w = 175
    gap = (w - 40 - n * box_w) // max(1, n - 1) if n > 1 else 0
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:660px;background:#FFFFFF;font-family:Arial,sans-serif;">',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#FAF8F3" stroke="#CBD5E1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">{title}</text>',
        '<defs><marker id="arr_lin" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#334155"/></marker></defs>',
    ]
    for i, (head, body, fill_hex) in enumerate(stages):
        x = 20 + i * (box_w + gap)
        y = 50
        lines.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="96" rx="8" fill="#FFFFFF" stroke="{fill_hex}" stroke-width="2.2"/>')
        lines.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="28" rx="6" fill="{fill_hex}"/>')
        lines.append(f'<text x="{x + box_w/2:.1f}" y="{y + 19}" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFFFFF">{head}</text>')
        lines.append(f'<text x="{x + box_w/2:.1f}" y="{y + 52}" text-anchor="middle" font-size="11" fill="#1E293B">{body[:28]}</text>')
        if len(body) > 28:
            lines.append(f'<text x="{x + box_w/2:.1f}" y="{y + 70}" text-anchor="middle" font-size="11" fill="#1E293B">{body[28:56]}</text>')
        if i < n - 1:
            x1 = x + box_w + 4
            x2 = x + box_w + gap - 4
            ym = y + 48
            lines.append(f'<line x1="{x1}" y1="{ym}" x2="{x2}" y2="{ym}" stroke="#334155" stroke-width="2" marker-end="url(#arr_lin)"/>')
    lines.append("</svg>")
    return "".join(lines)


def _svg_cycle_flow(
    title: str,
    nodes: List[str],
    accent_color: str = "#1D4ED8",
) -> str:
    w, h = 640, 260
    coords = [(115, 65), (525, 65), (525, 195), (115, 195)]
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:640px;background:#FFFFFF;font-family:Arial,sans-serif;">',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="8" fill="#FAF8F3" stroke="#CBD5E1" stroke-width="1.5"/>',
        f'<text x="{w//2}" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">{title}</text>',
        '<defs><marker id="arr_cyc" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#334155"/></marker></defs>',
        '<line x1="215" y1="65" x2="418" y2="65" stroke="#334155" stroke-width="2" marker-end="url(#arr_cyc)"/>',
        '<line x1="525" y1="95" x2="525" y2="160" stroke="#334155" stroke-width="2" marker-end="url(#arr_cyc)"/>',
        '<line x1="425" y1="195" x2="222" y2="195" stroke="#334155" stroke-width="2" marker-end="url(#arr_cyc)"/>',
        '<line x1="115" y1="165" x2="115" y2="100" stroke="#334155" stroke-width="2" marker-end="url(#arr_cyc)"/>',
    ]
    for i, (cx, cy) in enumerate(coords):
        text = nodes[i]
        part1 = text[:28]
        part2 = text[28:56].strip()
        lines.append(f'<rect x="{cx-95}" y="{cy-26}" width="190" height="52" rx="8" fill="#EFF6FF" stroke="{accent_color}" stroke-width="2"/>')
        if part2:
            lines.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">{part1}</text>')
            lines.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">{part2}</text>')
        else:
            lines.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0F172A">{part1}</text>')
    lines.append("</svg>")
    return "".join(lines)


def arch_01_production_definition_transformation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(["bakery", "furniture workshop", "clothing factory", "brickyard"])
    prompt = (
        f"A {biz} in {area} buys raw materials, runs machinery with electricity, and relies on skilled staff to "
        f"turn inputs into finished items for sale.\n\n"
        f"Which economic term BEST defines this activity?"
    )
    correct = "Production: transforming inputs into goods and services that satisfy human needs and wants"
    distractors = [
        "Consumption: using up finished items purely for leisure without creating anything new",
        "Hoarding: locking raw materials away permanently so no customers can ever buy them",
        "Deflation: lowering bank interest rates without altering business operations",
    ]
    return _mcq(
        rng,
        subskill="01_production_definition_transformation",
        title="Definition of Production",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Production is the process by which a {biz} combines inputs (raw materials, labour, capital, entrepreneurship) "
            f"to create useful goods and services satisfying needs and wants."
        ),
        hints={
            "tier_1": "Think of what turns raw ingredients or timber into finished products.",
            "tier_2": "Production always transforms inputs into useful outputs.",
            "tier_3": "Select 'Production: transforming inputs into goods and services that satisfy human needs and wants'.",
        },
        learning_objective_id="lo_prod_definition",
        concept_id="production_definition",
        misconception_tags=["confuses_production_with_consumption"],
    )


def arch_02_consumer_vs_producer_perspective(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    item = rng.choice(["fresh bread", "a school jersey", "a solar lamp", "maize meal"])
    prompt = (
        f"In {area}, {name} works during the week at a cooperative making {item} for customers, and on Saturday buys "
        f"groceries for the family table.\n\n"
        f"What separates the role of a PRODUCER from the role of a CONSUMER?"
    )
    correct = (
        "A producer combines inputs to supply goods or services to earn income/profit, while a consumer buys and uses goods or services to satisfy needs and wants"
    )
    distractors = [
        "A producer never pays for raw materials, whereas a consumer manufactures every household item at home",
        "Only large listed corporations can be consumers, while individuals are always producers",
        "Producers exist solely in rural towns, while consumers live only in capital cities",
    ]
    return _mcq(
        rng,
        subskill="02_consumer_vs_producer_perspective",
        title="Producer vs Consumer Roles",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Individuals play both economic roles: as workers/entrepreneurs they help produce goods and services for sale, "
            "and as households they act as consumers purchasing items to satisfy needs and wants."
        ),
        hints={
            "tier_1": "Compare creating/supplying products against buying/using them.",
            "tier_2": "Producers transform resources for sale; consumers buy outputs to satisfy wants and needs.",
            "tier_3": "Choose the statement distinguishing input-transformation for profit/income from buying and using outputs.",
        },
        learning_objective_id="lo_prod_consumer_vs_producer",
        concept_id="producer_vs_consumer",
        misconception_tags=["thinks_person_cannot_be_both_roles"],
    )


def arch_03_goods_vs_services_classification(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    scenarios = [
        ("hairdressing, dental check-ups, and minibus taxi transport", "Services — intangible activities performed directly for customers"),
        ("school desks, loaves of bread, and bottled juice", "Goods — tangible physical items you can touch, store, and carry home"),
    ]
    example, correct = rng.choice(scenarios)
    if "Services" in correct:
        distractors = [
            "Goods — tangible physical items that stay in a warehouse for years",
            "Natural minerals — raw coal and iron ore dug directly from underground mines",
            "Intermediate steel bars — physical metal rods stockpiled before construction",
        ]
    else:
        distractors = [
            "Services — intangible tasks performed immediately with zero physical object left behind",
            "Non-material advice — spoken legal guidance that cannot be held in your hand",
            "Human skills — invisible entrepreneurial creativity before any factory opens",
        ]
    prompt = (
        f"Businesses in {area} provide {example} to local residents.\n\n"
        f"How are {example} classified in economics?"
    )
    return _mcq(
        rng,
        subskill="03_goods_vs_services_classification",
        title="Goods vs Services Classification",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Goods are physical, tangible objects (bread, furniture), while services are intangible actions/expertise "
            "(haircuts, transport, medical care) consumed as they are delivered."
        ),
        hints={
            "tier_1": "Ask yourself: can you hold, weigh, and store this output on a shelf?",
            "tier_2": "Tangible physical products are goods; intangible performed activities are services.",
            "tier_3": f"Select '{correct}'.",
        },
        learning_objective_id="lo_prod_goods_vs_services",
        concept_id="goods_vs_services",
        misconception_tags=["confuses_tangible_goods_with_intangible_services"],
    )


def arch_04_tangible_vs_intangible_inputs(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(["custom carpentry shop", "community catering kitchen", "shoe-repair stall"])
    prompt = (
        f"A {biz} in {area} needs wood/ingredients, tools, electricity, workers' technical know-how, and the owner's "
        f"business creativity to operate.\n\n"
        f"Give TWO examples of tangible inputs and TWO examples of intangible inputs needed for production."
    )
    return _typed(
        rng,
        subskill="04_tangible_vs_intangible_inputs",
        title="Tangible vs Intangible Production Inputs",
        prompt=prompt,
        sample_answer=(
            "Tangible inputs (physical items): raw materials (wood/flour/leather) and tools/equipment (saws/ovens/sewing machines).\n"
            "Intangible inputs (non-physical): labour skills/knowledge and entrepreneurship/business ideas (plus electricity/water supply)."
        ),
        marking_points=[
            "Two valid tangible inputs (e.g. raw materials and machinery/tools) [2]",
            "Two valid intangible inputs (e.g. labour skills, management know-how, entrepreneurial ideas, water/power services) [2]",
        ],
        hints={
            "tier_1": "Tangible means you can physically touch it; intangible means knowledge, skills, ideas, or utility energy.",
            "tier_2": "List 2 physical items (materials + tools) and 2 non-physical inputs (skills + ideas/electricity).",
            "tier_3": "Tangible: raw materials & machines; Intangible: workers' skills/knowledge & entrepreneurial ideas.",
        },
        learning_objective_id="lo_prod_tangible_intangible_inputs",
        concept_id="tangible_vs_intangible_inputs",
        misconception_tags=["forgets_knowledge_and_skills_are_inputs"],
        marks=4,
    )


def arch_05_inputs_process_outputs_ipo_flowchart(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Artisan Bakery", "Flour, water, yeast & oven", "Mixing, kneading & baking", "Fresh loaves of brown bread"),
        ("Furniture Maker", "Pine timber, glue & saws", "Cutting, assembling & varnishing", "Sturdy classroom desks"),
        ("Fruit Cannery", "Fresh peaches, sugar & tins", "Washing, cooking & sealing", "Canned peach halves"),
    ]
    biz, inp, proc, outp = rng.choice(cases)
    area = rng.choice(AREAS)
    svg = _svg_linear_flow(
        title=f"Production System: {biz} ({area})",
        stages=[
            ("1. INPUTS", inp, "#1D4ED8"),
            ("2. PROCESS", proc, "#D97706"),
            ("3. OUTPUTS", outp, "#15803D"),
        ],
    )
    prompt = (
        f"Refer to the flowchart below illustrating the production stages of a {biz} in {area}.\n\n"
        f"Explain what happens in Stage 2 ('{proc}') and why an enterprise cannot generate '{outp}' without Stage 1 ('{inp}')."
    )
    return _typed(
        rng,
        subskill="05_inputs_process_outputs_ipo_flowchart",
        title="Inputs-Process-Outputs System (Flowchart)",
        prompt=prompt,
        sample_answer=(
            f"In Stage 2 ({proc}), workers and machinery transform raw materials ({inp}) into higher-value finished goods. "
            f"Without Stage 1 inputs (raw materials, equipment, labour), there is nothing physical or skilled to transform into {outp}."
        ),
        marking_points=[
            f"Explains that Stage 2 ({proc}) physically transforms raw inputs into finished value-added products [2]",
            f"Explains that without Stage 1 ({inp}), transformation cannot begin or yield {outp} [1]",
        ],
        hints={
            "tier_1": "Examine the middle box labelled '2. PROCESS' and follow the arrows from left to right.",
            "tier_2": "Production turns low-value raw inputs into higher-value outputs through a transformation stage.",
            "tier_3": f"Describe '{proc}' as transforming '{inp}' into useful finished '{outp}'.",
        },
        learning_objective_id="lo_prod_ipo_flowchart",
        concept_id="ipo_production_system",
        misconception_tags=["omits_transformation_process"],
        marks=3,
        diagram_spec={"kind": "inline_svg", "title": f"IPO Flowchart: {biz}", "svg": svg, "diagram_role": "context"},
    )


def arch_06_factors_of_production_natural_resources(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    resource = rng.choice(["fertile farmland and river water", "platinum deposits and groundwater", "indigenous timber and sunlight"])
    prompt = (
        f"An enterprise near {rural_area} depends heavily on {resource} provided directly by nature.\n\n"
        f"Which Factor of Production do these natural endowments represent, and what is the income paid to its owners called?"
    )
    correct = "Natural resources (Land) — paid Rent"
    distractors = [
        "Labour — paid Wages",
        "Capital — paid Interest",
        "Entrepreneurship — paid Profit",
    ]
    return _mcq(
        rng,
        subskill="06_factors_of_production_natural_resources",
        title="Factor of Production: Natural Resources (Land)",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Natural resources (Land) encompass all gifts of nature—soil, water, forests, minerals, and sunlight—and "
            "their economic remuneration is Rent."
        ),
        hints={
            "tier_1": "Identify which of the four factors covers raw gifts of nature rather than human effort or man-made tools.",
            "tier_2": "Land/natural resources earn Rent, whereas Labour earns Wages and Capital earns Interest.",
            "tier_3": "Select 'Natural resources (Land) — paid Rent'.",
        },
        learning_objective_id="lo_prod_factor_land",
        concept_id="factor_natural_resources",
        misconception_tags=["confuses_land_with_capital"],
    )


def arch_07_factors_of_production_labour(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    workers = rng.randint(14, 48)
    prompt = (
        f"A manufacturing plant in {area} hires {workers} machinists, quality inspectors, and delivery drivers to contribute "
        f"physical and mental work.\n\n"
        f"Which Factor of Production do these employees provide, and what is their remuneration?"
    )
    correct = "Labour — paid Wages or Salaries"
    distractors = [
        "Capital — paid Rent",
        "Natural resources — paid Profit",
        "Entrepreneurship — paid Interest",
    ]
    return _mcq(
        rng,
        subskill="07_factors_of_production_labour",
        title="Factor of Production: Labour",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Labour refers to the physical and mental human effort applied in production; those {workers} staff earn "
            f"Wages or Salaries."
        ),
        hints={
            "tier_1": "Focus on human physical and mental effort.",
            "tier_2": "Employees earn Wages or Salaries for supplying Labour.",
            "tier_3": "Select 'Labour — paid Wages or Salaries'.",
        },
        learning_objective_id="lo_prod_factor_labour",
        concept_id="factor_labour",
        misconception_tags=["confuses_labour_with_entrepreneurship"],
    )


def arch_08_factors_of_production_capital(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    loan_val = rng.choice([120000, 180000, 250000])
    prompt = (
        f"To expand production in {area}, a workshop buys welding machines, delivery vans, and factory shelving using "
        f"{_fmt_zar(loan_val)} in invested funds.\n\n"
        f"Which Factor of Production covers these man-made tools, buildings, and invested money, and what is its reward?"
    )
    correct = "Capital — paid Interest"
    distractors = [
        "Land — paid Wages",
        "Labour — paid Rent",
        "Entrepreneurship — paid Taxes",
    ]
    return _mcq(
        rng,
        subskill="08_factors_of_production_capital",
        title="Factor of Production: Capital",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Capital consists of man-made assets (tools, machinery, factory buildings, vehicles) and funds invested to "
            "produce further goods; the financial reward for Capital is Interest."
        ),
        hints={
            "tier_1": "Man-made machines and start-up money are NOT natural gifts of nature.",
            "tier_2": "Machines, buildings, and finance together make up Capital, which earns Interest.",
            "tier_3": "Select 'Capital — paid Interest'.",
        },
        learning_objective_id="lo_prod_factor_capital",
        concept_id="factor_capital",
        misconception_tags=["confuses_capital_machines_with_natural_land"],
    )


def arch_09_factors_of_production_entrepreneurship(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    startup = rng.choice([45000, 65000, 80000])
    prompt = (
        f"{name} invests {_fmt_zar(startup)} in {area} to rent workshop space, hire two artisans, purchase sewing "
        f"machines, and market school uniforms despite the risk of losing money.\n\n"
        f"Identify the fourth Factor of Production that {name} supplies, name its financial reward, and explain why this "
        f"factor is essential to bring the other three factors together."
    )
    return _typed(
        rng,
        subskill="09_factors_of_production_entrepreneurship",
        title="Factor of Production: Entrepreneurship",
        prompt=prompt,
        sample_answer=(
            f"Factor: Entrepreneurship. Reward: Profit.\n"
            f"Why essential: Without {name} taking the initiative and financial risk to organise Land (workshop), Labour "
            f"(artisans), and Capital (machines and {_fmt_zar(startup)}), the idle resources would never combine to produce uniforms."
        ),
        marking_points=[
            "Identifies Entrepreneurship as the Factor of Production [1]",
            "Identifies Profit as the remuneration/reward [1]",
            "Explains that the entrepreneur takes risks and coordinates Land, Labour, and Capital into production [1]",
        ],
        hints={
            "tier_1": "Name the human factor that takes business risk and organises the other three factors.",
            "tier_2": "Entrepreneurs earn Profit (not wages or interest) for risking capital and coordinating production.",
            "tier_3": "State Entrepreneurship -> Profit -> organises Land, Labour, and Capital while taking financial risk.",
        },
        learning_objective_id="lo_prod_factor_entrepreneurship",
        concept_id="factor_entrepreneurship",
        misconception_tags=["confuses_entrepreneur_profit_with_salary"],
        marks=3,
    )


def arch_10_factors_of_production_matching_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["Production Resource Example", "Factor of Production", "Remuneration / Reward", "Check"]
    raw_rows = [
        [
            {"type": "given", "value": "Irrigated soil & coal seam"},
            {"type": "required", "expected": "Natural resources"},
            {"type": "required", "expected": "Rent"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Skilled millers & truck drivers"},
            {"type": "given", "value": "Labour"},
            {"type": "required", "expected": "Wages or salaries"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Industrial oven & delivery truck"},
            {"type": "required", "expected": "Capital"},
            {"type": "given", "value": "Interest"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Founder organising business risk"},
            {"type": "given", "value": "Entrepreneurship"},
            {"type": "required", "expected": "Profit"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Use exact term: 'Natural resources'.",
        "r0_c2": "Reward for Land / Natural resources is 'Rent'.",
        "r1_c2": "Use exact phrase: 'Wages or salaries'.",
        "r2_c1": "Man-made ovens and trucks belong to 'Capital'.",
        "r3_c2": "Reward for Entrepreneurship is 'Profit'.",
    }
    derivations = [
        "Soil & coal -> Natural resources -> Rent.",
        "Millers & drivers -> Labour -> Wages or salaries.",
        "Industrial oven & truck -> Capital -> Interest.",
        "Founder taking risk -> Entrepreneurship -> Profit.",
    ]
    return _table_q(
        rng,
        subskill="10_factors_of_production_matching_table",
        title="Factors of Production & Remuneration Table",
        prompt=(
            f"Complete the Factors of Production table for an enterprise operating in {area}. Use exact terms: "
            f"'Natural resources', 'Capital', 'Rent', 'Wages or salaries', and 'Profit'. Leave 'Check' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Pair each real-world example with one of the 4 Factors and its specific income type.",
            "tier_2": "Land->Rent, Labour->Wages or salaries, Capital->Interest, Entrepreneurship->Profit.",
            "tier_3": "Fill r0_c1='Natural resources', r0_c2='Rent', r1_c2='Wages or salaries', r2_c1='Capital', r3_c2='Profit'.",
        },
        learning_objective_id="lo_prod_factors_table",
        concept_id="factors_of_production_matrix",
        misconception_tags=["swaps_interest_and_profit", "fills_must_be_empty_cell"],
    )


def arch_11_intermediate_vs_final_goods(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pair = rng.choice([
        ("sacks of milled wheat flour bought by a bakery", "loaves of sliced bread sold to families"),
        ("rolls of woven cotton fabric bought by a clothing factory", "school shirts sold at a retail shop"),
        ("sheets of steel bought by a trailer manufacturer", "completed farm trailers sold to farmers"),
    ])
    inter, final = pair
    prompt = (
        f"In {area}, economists distinguish {inter} from {final}.\n\n"
        f"Why are {inter} classified as INTERMEDIATE goods rather than final consumer goods?"
    )
    correct = (
        "They are inputs purchased by another business to be processed further into a finished good for end consumers"
    )
    distractors = [
        "They are completely free gifts of nature that required zero human processing",
        "They can never be bought or sold using South African Rand",
        "They are intangible services consumed immediately with no physical form",
    ]
    return _mcq(
        rng,
        subskill="11_intermediate_vs_final_goods",
        title="Intermediate Goods vs Final Goods",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Intermediate goods ({inter}) are already processed once, yet serve as raw inputs for the next business stage "
            f"to manufacture final consumer goods ({final})."
        ),
        hints={
            "tier_1": "Ask who buys the flour, fabric, or steel — an end household consumer or another factory/bakery?",
            "tier_2": "Goods processed further by another enterprise before reaching the final user are intermediate goods.",
            "tier_3": "Select 'They are inputs purchased by another business to be processed further into a finished good for end consumers'.",
        },
        learning_objective_id="lo_prod_intermediate_goods",
        concept_id="intermediate_vs_final_goods",
        misconception_tags=["confuses_intermediate_goods_with_final_goods"],
    )


def arch_12_primary_sector_extraction_role(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    activity = rng.choice([
        "sugar-cane farming, pine forestry, and coal mining",
        "cattle ranching, deep-sea snoek fishing, and gold mining",
    ])
    prompt = (
        f"Around {rural_area}, major employers are engaged in {activity}.\n\n"
        f"To which economic sector do these activities belong, and what defines that sector?"
    )
    correct = (
        "Primary sector — harvesting and extracting raw materials directly from nature"
    )
    distractors = [
        "Secondary sector — assembling electronic parts inside urban factories",
        "Tertiary sector — insuring, banking, and transporting finished retail products",
        "Quaternary sector — purely providing banking loans without raw materials",
    ]
    return _mcq(
        rng,
        subskill="12_primary_sector_extraction_role",
        title="The Primary Sector",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Farming, forestry, fishing, and mining ({activity}) take raw materials directly from Earth's surface, seas, "
            f"or underground — defining the Primary sector."
        ),
        hints={
            "tier_1": "Identify which stage comes FIRST before factories process anything.",
            "tier_2": "Extracting minerals, crops, timber, and fish directly from nature is Primary production.",
            "tier_3": "Select 'Primary sector — harvesting and extracting raw materials directly from nature'.",
        },
        learning_objective_id="lo_prod_primary_sector",
        concept_id="primary_sector",
        misconception_tags=["places_mining_in_secondary_sector"],
    )


def arch_13_secondary_sector_manufacturing_processing(rng: random.Random) -> Dict[str, Any]:
    urban_area = rng.choice(URBAN_AREAS)
    activity = rng.choice([
        "refining crude oil into petrol and plastics, and canning fresh fruit",
        "smelting iron ore into steel beams and assembling motor vehicles",
        "milling maize into maize meal and constructing brick houses",
    ])
    prompt = (
        f"Industrial parks near {urban_area} focus on {activity}.\n\n"
        f"To which economic sector do these manufacturing and construction businesses belong?"
    )
    correct = (
        "Secondary sector — processing raw materials from the primary sector into finished or semi-finished goods"
    )
    distractors = [
        "Primary sector — extracting unprocessed rocks directly from open-pit mines",
        "Tertiary sector — selling ready-made goods over supermarket tills without altering them",
        "Consumer household sector — using purchased goods solely at home",
    ]
    return _mcq(
        rng,
        subskill="13_secondary_sector_manufacturing_processing",
        title="The Secondary Sector",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Manufacturing, processing, and construction ({activity}) transform raw primary outputs into usable goods — "
            f"the core function of the Secondary sector."
        ),
        hints={
            "tier_1": "Think of the SECOND stage after farming/mining: factories and builders.",
            "tier_2": "Turning raw inputs into finished tangible products happens in the Secondary sector.",
            "tier_3": "Select 'Secondary sector — processing raw materials from the primary sector into finished or semi-finished goods'.",
        },
        learning_objective_id="lo_prod_secondary_sector",
        concept_id="secondary_sector",
        misconception_tags=["confuses_construction_with_tertiary"],
    )


def arch_14_tertiary_sector_services_distribution(rng: random.Random) -> Dict[str, Any]:
    urban_area = rng.choice(URBAN_AREAS)
    services = rng.choice([
        "supermarkets, commercial banks, courier trucks, schools, and clinics",
        "insurance brokers, hardware retailers, pharmacies, and legal practices",
    ])
    prompt = (
        f"Along the main avenue of {urban_area}, businesses include {services}.\n\n"
        f"Which economic sector encompasses all of these businesses, and what is its core role?"
    )
    correct = (
        "Tertiary sector — delivering services and distributing goods from producers to final consumers"
    )
    distractors = [
        "Primary sector — drilling and cultivating raw crops directly from farmland",
        "Secondary sector — operating blast furnaces and textile looms in heavy factories",
        "Intermediate mining sector — digging raw limestone from underground shafts",
    ]
    return _mcq(
        rng,
        subskill="14_tertiary_sector_services_distribution",
        title="The Tertiary Sector",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "The Tertiary (service) sector includes wholesale/retail trade, transport, banking, insurance, healthcare, "
            "and education — moving finished goods to buyers and supplying essential services."
        ),
        hints={
            "tier_1": "Retail shops, banks, transport, and healthcare do not farm or manufacture physical products.",
            "tier_2": "Distribution and service delivery belong to the third (Tertiary) sector.",
            "tier_3": "Select 'Tertiary sector — delivering services and distributing goods from producers to final consumers'.",
        },
        learning_objective_id="lo_prod_tertiary_sector",
        concept_id="tertiary_sector",
        misconception_tags=["places_retail_shops_in_secondary_sector"],
    )


def arch_15_three_sector_production_chain_diagram(rng: random.Random) -> Dict[str, Any]:
    chains = [
        ("Forestry Farm", "Planting & felling pine trees", "Paper & Desk Mill", "Making timber & paper books", "Stationery Store", "Transport & retail sales"),
        ("Dairy Farm", "Milking cows in Eastern Cape", "Creamery Factory", "Pasteurising & bottling cheese", "Supermarket", "Refrigerated retail display"),
        ("Maize Farm", "Harvesting yellow maize grain", "Grain Mill", "Grinding maize into meal", "Spaza & Wholesale", "Distributing bags to families"),
    ]
    p_name, p_desc, s_name, s_desc, t_name, t_desc = rng.choice(chains)
    svg = _svg_linear_flow(
        title="Three-Sector Production Chain",
        stages=[
            (f"PRIMARY: {p_name[:12]}", p_desc, "#15803D"),
            (f"SECONDARY: {s_name[:10]}", s_desc, "#1D4ED8"),
            (f"TERTIARY: {t_name[:11]}", t_desc, "#7C3AED"),
        ],
    )
    prompt = (
        f"Refer to the flowchart below tracing a product from '{p_name}' through '{s_name}' to '{t_name}'.\n\n"
        f"Identify the role played by EACH of the three sectors in this specific value chain."
    )
    return _typed(
        rng,
        subskill="15_three_sector_production_chain_diagram",
        title="Three-Sector Supply Chain (Flowchart)",
        prompt=prompt,
        sample_answer=(
            f"1. Primary sector ({p_name}): {p_desc} to supply raw natural inputs.\n"
            f"2. Secondary sector ({s_name}): {s_desc} to transform raw material into finished consumer goods.\n"
            f"3. Tertiary sector ({t_name}): {t_desc} to reach final consumers."
        ),
        marking_points=[
            f"Explains Primary stage ({p_name}: {p_desc}) [1]",
            f"Explains Secondary stage ({s_name}: {s_desc}) [1]",
            f"Explains Tertiary stage ({t_name}: {t_desc}) [1]",
        ],
        hints={
            "tier_1": "Read each of the three boxes from left to right along the arrows.",
            "tier_2": "Primary extracts raw material -> Secondary processes/manufactures -> Tertiary transports and sells.",
            "tier_3": f"Describe Primary ({p_name}), Secondary ({s_name}), and Tertiary ({t_name}) in sequence.",
        },
        learning_objective_id="lo_prod_three_sector_chain",
        concept_id="three_sector_chain",
        misconception_tags=["mixes_up_secondary_and_tertiary_stages"],
        marks=3,
        diagram_spec={"kind": "inline_svg", "title": "Three-Sector Production Chain", "svg": svg, "diagram_role": "context"},
    )


def arch_16_sector_classification_schedule_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["South African Enterprise", "Main Activity", "Economic Sector", "Code"]
    raw_rows = [
        [
            {"type": "given", "value": "Limpopo Citrus Orchard"},
            {"type": "given", "value": "Growing & picking oranges"},
            {"type": "required", "expected": "Primary"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "KZN Fruit Bottling Plant"},
            {"type": "given", "value": "Juicing & canning oranges"},
            {"type": "required", "expected": "Secondary"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Durban Logistics Freight"},
            {"type": "given", "value": "Delivering crates to shops"},
            {"type": "required", "expected": "Tertiary"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Rustenburg Chrome Mine"},
            {"type": "given", "value": "Mining chrome ore underground"},
            {"type": "required", "expected": "Primary"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Growing fruit directly from land: 'Primary'.",
        "r1_c2": "Factory juicing & canning: 'Secondary'.",
        "r2_c2": "Freight delivery service: 'Tertiary'.",
        "r3_c2": "Extracting ore from nature: 'Primary'.",
    }
    derivations = [
        "Orchard & Chrome Mine extract raw natural resources -> Primary.",
        "Fruit Bottling Plant processes oranges into juice cans -> Secondary.",
        "Logistics Freight provides transport distribution -> Tertiary.",
    ]
    return _table_q(
        rng,
        subskill="16_sector_classification_schedule_table",
        title="Economic Sector Classification Matrix",
        prompt=(
            f"A regional trade survey in {area} lists four enterprises. Classify each enterprise as 'Primary', 'Secondary', "
            f"or 'Tertiary'. Leave the 'Code' column blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Decide whether each business extracts raw materials, manufactures goods, or delivers services.",
            "tier_2": "Mining/farming = Primary; factory processing = Secondary; freight/transport = Tertiary.",
            "tier_3": "Fill Primary, Secondary, Tertiary, Primary down the Economic Sector column.",
        },
        learning_objective_id="lo_prod_sector_table",
        concept_id="sector_classification_table",
        misconception_tags=["classifies_freight_as_secondary", "fills_must_be_empty_cell"],
    )


def arch_17_rural_primary_vs_urban_secondary_tertiary_location(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    urban_area = rng.choice(URBAN_AREAS)
    prompt = (
        f"Notice how primary farming and forestry cluster in {rural_area}, whereas secondary factories and tertiary banks "
        f"concentrate around {urban_area}.\n\n"
        f"Give TWO clear economic reasons for this difference in geographic location."
    )
    return _typed(
        rng,
        subskill="17_rural_primary_vs_urban_secondary_tertiary_location",
        title="Location of Primary vs Secondary/Tertiary Sectors",
        prompt=prompt,
        sample_answer=(
            f"1. Primary activities in {rural_area} depend on abundant cheap land, fertile soil, water, forests, or mineral deposits that cannot be moved.\n"
            f"2. Secondary and tertiary firms locate in {urban_area} to access reliable power, transport hubs, skilled labour pools, and large concentrations of paying customers."
        ),
        marking_points=[
            "Primary activities locate near immobile natural resources (land, soil, mines, water) in rural regions [1]",
            "Secondary/tertiary activities cluster in towns/cities for infrastructure, utilities, skilled staff, and large customer markets [1]",
        ],
        hints={
            "tier_1": "Think about what farms/mines need versus what factories, shops, and banks need.",
            "tier_2": "Natural resources stay fixed in rural areas; consumers and transport networks gather in cities.",
            "tier_3": "Give one reason tied to immobile land/minerals (rural) and one tied to infrastructure/customers/skills (urban).",
        },
        learning_objective_id="lo_prod_sector_location",
        concept_id="rural_urban_sector_location",
        misconception_tags=["omits_market_and_infrastructure_pull"],
        marks=2,
    )


def arch_18_developing_countries_primary_sector_dependency(rng: random.Random) -> Dict[str, Any]:
    pct_primary = rng.randint(52, 68)
    prompt = (
        f"Many developing nations generate around {pct_primary}% of export income from unprocessed primary commodities "
        f"(raw minerals, timber, and crops) rather than finished manufactured products.\n\n"
        f"Why does over-reliance on exporting unprocessed primary goods limit a developing country's earnings?"
    )
    correct = (
        "Raw commodities sell at much lower, volatile prices than value-added manufactured goods and create fewer high-skill jobs locally"
    )
    distractors = [
        "Raw coal and crops always sell at triple the price of finished cars and electronics",
        "Primary exports require zero natural resources or rural workers",
        "Importing finished machinery earns export profits for the raw-material country",
    ]
    return _mcq(
        rng,
        subskill="18_developing_countries_primary_sector_dependency",
        title="Primary-Sector Dependency in Developing Economies",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Processing raw commodities domestically (beneficiation) adds substantial value and creates skilled factory "
            "and service jobs; exporting raw materials lets foreign factories capture most of the final price."
        ),
        hints={
            "tier_1": "Compare the price of raw iron ore or raw cacao beans against a finished car or chocolate bar.",
            "tier_2": "Most profit and skilled jobs are created during Secondary manufacturing, not raw extraction.",
            "tier_3": "Select the option noting lower/volatile prices for raw commodities and fewer value-added local jobs.",
        },
        learning_objective_id="lo_prod_developing_primary_share",
        concept_id="developing_country_sectors",
        misconception_tags=["believes_raw_exports_yield_highest_margin"],
    )


def arch_19_sector_share_gdp_comparison_bar_graph(rng: random.Random) -> Dict[str, Any]:
    dev_prim = rng.randint(24, 34)
    dev_sec = rng.randint(24, 30)
    dev_tert = 100 - dev_prim - dev_sec

    adv_prim = rng.randint(2, 5)
    adv_sec = rng.randint(22, 27)
    adv_tert = 100 - adv_prim - adv_sec
    diff = adv_tert - dev_tert

    svg = _svg_bar_chart(
        title="GDP Share by Sector: Developing vs Developed (%)",
        y_label="Share of GDP (%)",
        bars=[
            ("Dev-ing Prim", float(dev_prim), "#15803D"),
            ("Dev-ing Tert", float(dev_tert), "#0284C7"),
            ("Adv-ed Prim", float(adv_prim), "#D97706"),
            ("Adv-ed Tert", float(adv_tert), "#1D4ED8"),
        ],
        max_val=100.0,
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the bar graph below comparing Primary and Tertiary GDP shares between a Developing economy "
        f"(Primary {dev_prim}%, Tertiary {dev_tert}%) and a Developed economy (Primary {adv_prim}%, Tertiary {adv_tert}%).\n\n"
        f"Calculate how many percentage points larger the Developed economy's Tertiary sector share is compared with "
        f"the Developing economy's Tertiary sector share."
    )
    return _typed(
        rng,
        subskill="19_sector_share_gdp_comparison_bar_graph",
        title="Developing vs Developed Sector Shares (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Tertiary GDP share difference = {adv_tert}% - {dev_tert}% = {diff} percentage points.",
        marking_points=[
            f"Read Developed Tertiary ({adv_tert}%) and Developing Tertiary ({dev_tert}%) [1]",
            f"Compute difference = {adv_tert} - {dev_tert} = {diff} percentage points [2]",
        ],
        hints={
            "tier_1": "Locate the two Tertiary bars ('Dev-ing Tert' and 'Adv-ed Tert').",
            "tier_2": f"Subtract {dev_tert}% from {adv_tert}%.",
            "tier_3": f"{adv_tert}% - {dev_tert}% = {diff} percentage points.",
        },
        learning_objective_id="lo_prod_sector_gdp_bar_graph",
        concept_id="sector_gdp_comparison",
        misconception_tags=["compares_primary_instead_of_tertiary"],
        marks=3,
        correct_answer=f"{diff} percentage points",
        correct_value=float(diff),
        diagram_spec={"kind": "inline_svg", "title": "GDP Share by Sector", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Tertiary gap = {adv_tert}% - {dev_tert}% = {diff} percentage points",
    )


def arch_20_sector_interdependence_domino_effect(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    shock = rng.choice([
        ("A severe drought destroys 45% of wheat and maize harvests", "flour mills and bakeries", "supermarkets and households"),
        ("A diesel fuel tanker strike halts freight deliveries for two weeks", "factories waiting for spare parts", "mines unable to ship coal to ports"),
    ])
    event, sec_hit, third_hit = shock
    prompt = (
        f"{event} around {area}.\n\n"
        f"Using the concept of sector interdependence (domino effect), explain how this shock affects BOTH {sec_hit} "
        f"and {third_hit}."
    )
    return _typed(
        rng,
        subskill="20_sector_interdependence_domino_effect",
        title="Sector Interdependence and Domino Effects",
        prompt=prompt,
        sample_answer=(
            f"The three sectors depend directly on one another like dominoes. This shock leaves {sec_hit} short of "
            f"essential inputs/parts, cutting output and risking job losses, while {third_hit} face shortages, higher "
            f"prices, or stalled revenues across the supply chain."
        ),
        marking_points=[
            "Defines sector interdependence (each sector relies on inputs/services from the others) [1]",
            f"Explains concrete knock-on effect on {sec_hit} [1]",
            f"Explains concrete knock-on effect on {third_hit} [1]",
        ],
        hints={
            "tier_1": "Remember: Primary feeds Secondary, Secondary supplies tools/goods, Tertiary moves/finances everything.",
            "tier_2": "Trace how missing inputs or stalled transport cascades down to mills/factories and shops/consumers.",
            "tier_3": f"State sector interdependence and trace specific impacts onto {sec_hit} and {third_hit}.",
        },
        learning_objective_id="lo_prod_interdependence",
        concept_id="sector_interdependence",
        misconception_tags=["treats_sectors_as_isolated_silos"],
        marks=3,
    )


def arch_21_renewable_resources_definition_and_examples(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    prompt = (
        f"Community cooperatives near {rural_area} generate power from sunlight and replant harvested pine forests "
        f"every winter.\n\n"
        f"Why are sunlight, wind, and sustainably managed forests classified as RENEWABLE resources?"
    )
    correct = (
        "They are naturally replenished over a human lifetime or regrow continuously if harvested responsibly"
    )
    distractors = [
        "They took 300 million years to form underground and disappear permanently once used once",
        "They consist solely of synthetic plastic factory machinery",
        "They can never be exhausted even if every tree is clear-cut without replanting",
    ]
    return _mcq(
        rng,
        subskill="21_renewable_resources_definition_and_examples",
        title="Renewable Resources",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Renewable resources (sunlight, wind, rain, crops, sustainably replanted forests) regenerate naturally within "
            "short timescales, provided harvest rates do not exceed regrowth."
        ),
        hints={
            "tier_1": "Think about what 're-new-able' means regarding supply over a human lifetime.",
            "tier_2": "Solar energy arrives continuously and replanted trees regrow within years, unlike coal.",
            "tier_3": "Select 'They are naturally replenished over a human lifetime or regrow continuously if harvested responsibly'.",
        },
        learning_objective_id="lo_prod_renewable_resources",
        concept_id="renewable_resources",
        misconception_tags=["thinks_renewable_resources_cannot_be_overexploited"],
    )


def arch_22_non_renewable_resources_finite_depletion(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    mineral = rng.choice(["coal and crude oil", "gold and platinum ore", "iron ore and natural gas"])
    prompt = (
        f"Industries near {area} consume {mineral} formed deep underground over millions of years.\n\n"
        f"What makes {mineral} NON-RENEWABLE resources?"
    )
    correct = (
        "Their Earth reserves are finite and cannot be replaced on a human timescale once extracted and burned/used"
    )
    distractors = [
        "They grow back automatically inside mine shafts within two rainy seasons",
        "They are manufactured quickly out of rainwater and sunlight in laboratories",
        "They remain 100% intact and reusable after coal is burned in power stations",
    ]
    return _mcq(
        rng,
        subskill="22_non_renewable_resources_finite_depletion",
        title="Non-Renewable Resources",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Fossil fuels and mineral ores ({mineral}) took geological eras to form; once extracted and consumed, "
            f"total reserves shrink permanently."
        ),
        hints={
            "tier_1": "Can coal or crude oil regrow after a power station burns it?",
            "tier_2": "Non-renewable stocks are fixed/finite over human lifetimes.",
            "tier_3": "Select 'Their Earth reserves are finite and cannot be replaced on a human timescale once extracted and burned/used'.",
        },
        learning_objective_id="lo_prod_non_renewable_resources",
        concept_id="non_renewable_resources",
        misconception_tags=["confuses_minerals_with_renewable_timber"],
    )


def arch_23_sustainable_use_of_resources_definition(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"A municipality near {area} adopts a resource policy requiring factories to reduce waste, recycle scrap, and "
        f"replant harvested trees.\n\n"
        f"What is the core principle of SUSTAINABLE use of resources?"
    )
    correct = (
        "Using natural resources responsibly today without depleting them or damaging ecosystems for future generations"
    )
    distractors = [
        "Using up every mineral deposit and forest immediately to maximise this month's sales",
        "Banning all schools, farms, and clinics permanently so no resources are ever touched",
        "Dumping untreated factory chemicals into local rivers to lower production fees",
    ]
    return _mcq(
        rng,
        subskill="23_sustainable_use_of_resources_definition",
        title="Meaning of Sustainable Resource Use",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Sustainable production balances present economic needs with long-term environmental stewardship so future "
            "generations still enjoy fertile soils, clean water, and raw materials."
        ),
        hints={
            "tier_1": "Look for the balance between TODAY'S production needs and FUTURE generations.",
            "tier_2": "Sustainability neither wastes everything now nor stops all human production.",
            "tier_3": "Choose 'Using natural resources responsibly today without depleting them or damaging ecosystems for future generations'.",
        },
        learning_objective_id="lo_prod_sustainable_definition",
        concept_id="sustainable_resource_use",
        misconception_tags=["equates_sustainability_with_zero_production"],
    )


def arch_24_five_sustainable_practices_sa_context(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Mpumalanga forestry plantations", "Northern Cape solar farms", "Western Cape fruit packaging plants"])
    prompt = (
        f"In South Africa (including {region}), responsible producers aim to use resources sustainably.\n\n"
        f"State THREE practical sustainable production methods used in South Africa and explain how each protects future supply."
    )
    return _typed(
        rng,
        subskill="24_five_sustainable_practices_sa_context",
        title="Sustainable Production Practices in South Africa",
        prompt=prompt,
        sample_answer=(
            "1. Replanting harvested forests (e.g. Mpumalanga plantations): ensures continuous timber supply without destroying habitats.\n"
            "2. Switching to solar and wind renewable energy: reduces reliance on finite coal and lowers carbon pollution.\n"
            "3. Recycling glass, paper, cans, and scrap metal: cuts landfill waste and saves energy/virgin raw materials (plus crop rotation/water saving)."
        ),
        marking_points=[
            "Practice 1 with protection explanation (e.g. forestry replanting / sustainable fishing quotas) [1]",
            "Practice 2 with protection explanation (e.g. solar/wind renewable energy replacing finite coal) [1]",
            "Practice 3 with protection explanation (e.g. industrial recycling, water conservation, or soil rotation) [1]",
        ],
        hints={
            "tier_1": "Think of forestry in Mpumalanga, sunny/windy clean energy, and recycling materials.",
            "tier_2": "Name three concrete actions AND state why each extends resource availability.",
            "tier_3": "Include replanting trees, clean solar/wind power, and recycling scrap/conserving water or soil.",
        },
        learning_objective_id="lo_prod_sa_sustainable_practices",
        concept_id="sa_sustainable_practices",
        misconception_tags=["lists_slogans_without_explanation"],
        marks=3,
    )


def arch_25_developed_vs_developing_resource_consumption(rng: random.Random) -> Dict[str, Any]:
    urban_area = rng.choice(URBAN_AREAS)
    prompt = (
        f"While preparing a trade briefing in {urban_area}, learners compare resource consumption between wealthy "
        f"developed countries and lower-income developing countries.\n\n"
        f"Explain TWO key contrasts between how developed and developing countries use and manage natural resources."
    )
    return _typed(
        rng,
        subskill="25_developed_vs_developing_resource_consumption",
        title="Resource Use: Developed vs Developing Countries",
        prompt=prompt,
        sample_answer=(
            "1. Per-capita consumption: Developed nations consume far more energy, manufactured goods, and raw materials per person, often importing commodities from developing nations.\n"
            "2. Recycling and conservation capacity: Developed countries can usually afford stricter pollution controls and advanced recycling plants, whereas developing economies face budget pressure to extract raw exports for urgent jobs and income."
        ),
        marking_points=[
            "Notes higher per-person consumption of energy/raw resources in developed nations [1]",
            "Contrasts stronger financing for clean technology/recycling in developed economies against immediate resource-export dependency in developing nations [1]",
        ],
        hints={
            "tier_1": "Compare how much energy/goods each person uses AND who can afford clean recycling systems.",
            "tier_2": "Wealthy nations consume much more per person, yet have capital to enforce green laws and recycling.",
            "tier_3": "Contrast high per-capita consumption vs export pressure and green-tech affordability.",
        },
        learning_objective_id="lo_prod_dev_vs_deving_resources",
        concept_id="resource_consumption_comparison",
        misconception_tags=["assumes_poorer_countries_consume_more_per_capita"],
        marks=2,
    )


BUILDERS_01_25 = {
    "01_production_definition_transformation": arch_01_production_definition_transformation,
    "02_consumer_vs_producer_perspective": arch_02_consumer_vs_producer_perspective,
    "03_goods_vs_services_classification": arch_03_goods_vs_services_classification,
    "04_tangible_vs_intangible_inputs": arch_04_tangible_vs_intangible_inputs,
    "05_inputs_process_outputs_ipo_flowchart": arch_05_inputs_process_outputs_ipo_flowchart,
    "06_factors_of_production_natural_resources": arch_06_factors_of_production_natural_resources,
    "07_factors_of_production_labour": arch_07_factors_of_production_labour,
    "08_factors_of_production_capital": arch_08_factors_of_production_capital,
    "09_factors_of_production_entrepreneurship": arch_09_factors_of_production_entrepreneurship,
    "10_factors_of_production_matching_table": arch_10_factors_of_production_matching_table,
    "11_intermediate_vs_final_goods": arch_11_intermediate_vs_final_goods,
    "12_primary_sector_extraction_role": arch_12_primary_sector_extraction_role,
    "13_secondary_sector_manufacturing_processing": arch_13_secondary_sector_manufacturing_processing,
    "14_tertiary_sector_services_distribution": arch_14_tertiary_sector_services_distribution,
    "15_three_sector_production_chain_diagram": arch_15_three_sector_production_chain_diagram,
    "16_sector_classification_schedule_table": arch_16_sector_classification_schedule_table,
    "17_rural_primary_vs_urban_secondary_tertiary_location": arch_17_rural_primary_vs_urban_secondary_tertiary_location,
    "18_developing_countries_primary_sector_dependency": arch_18_developing_countries_primary_sector_dependency,
    "19_sector_share_gdp_comparison_bar_graph": arch_19_sector_share_gdp_comparison_bar_graph,
    "20_sector_interdependence_domino_effect": arch_20_sector_interdependence_domino_effect,
    "21_renewable_resources_definition_and_examples": arch_21_renewable_resources_definition_and_examples,
    "22_non_renewable_resources_finite_depletion": arch_22_non_renewable_resources_finite_depletion,
    "23_sustainable_use_of_resources_definition": arch_23_sustainable_use_of_resources_definition,
    "24_five_sustainable_practices_sa_context": arch_24_five_sustainable_practices_sa_context,
    "25_developed_vs_developing_resource_consumption": arch_25_developed_vs_developing_resource_consumption,
}
