"""Grade 7 EMS — Inequality and Poverty: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards (Term 3: The Economy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 4/02. Inequality and poverty.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS, get_ems_scenario

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term3_inequality_and_poverty"
TOPIC_NAME = "Inequality and poverty"
CURRICULUM_REF = "Term 3 > The Economy: Inequality and Poverty"


def _fmt_zar(amount: float, decimals: int = 0) -> str:
    """Format an amount in South African Rand using spaces and comma decimals."""
    if decimals == 0 and float(amount).is_integer():
        return f"R{int(round(amount)):,}".replace(",", " ")
    formatted = f"{amount:,.{decimals}f}".replace(",", " ").replace(".", ",")
    return f"R{formatted}"


def _fmt_comma(val: float, decimals: int = 2) -> str:
    """Format a decimal number with South African comma separator."""
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
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": duration_mins,
        "curriculum_reference": CURRICULUM_REF,
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "concept_group": "inequality_and_poverty",
        "marks": marks,
        "total_marks": marks,
        "misconception_tags": misconception_tags,
        "diagnostic_tags": diagnostic_tags or ["inequality_and_poverty"],
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
        "id": f"g7_ems_ineq_{subskill[:12]}_{rng.randint(100000, 999999)}",
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
        "id": f"g7_ems_ineq_{subskill[:12]}_{rng.randint(100000, 999999)}",
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
        for c_idx, spec in enumerate(row):
            cid = f"r{r_idx}_c{c_idx}"
            ctype = spec.get("type", "given")
            if ctype == "given":
                val = str(spec.get("value", ""))
                ui_row.append({
                    "cell_id": cid,
                    "value": val,
                    "editable": False,
                    "prefilled": True,
                    "type": "given",
                })
                md_cells.append(val)
            elif ctype == "must_be_empty":
                has_must_be_empty = True
                ui_row.append({
                    "cell_id": cid,
                    "value": "",
                    "expected": "",
                    "editable": True,
                    "prefilled": False,
                    "type": "must_be_empty",
                })
                md_cells.append("*(blank)*")
            else:
                exp = str(spec.get("expected", ""))
                ui_row.append({
                    "cell_id": cid,
                    "value": "",
                    "expected": exp,
                    "editable": True,
                    "prefilled": False,
                    "type": "required",
                })
                correct_map[cid] = exp
                md_cells.append(f"**{exp}**")
                marking_points.append({
                    "id": f"mp_{mp_idx}",
                    "desc": f"Cell ({r_idx + 1}, {headers[c_idx]}): {exp}",
                    "marks": 1,
                    "editable": True,
                })
                mp_idx += 1
        rows.append(ui_row)
        md_rows.append("| " + " | ".join(md_cells) + " |")

    marks = max(2, len(marking_points))
    md_table = "\n".join(md_rows)
    deriv_text = "\n".join(f"- {d}" for d in derivations)
    memo = f"{md_table}\n\n**Derivations & Rules:**\n{deriv_text}"

    deductions = [{"rule": "must_be_empty_filled", "penalty": -1}] if has_must_be_empty else []

    return {
        **_base_meta(subskill, learning_objective_id, concept_id, marks, max(4, marks), misconception_tags),
        "id": f"g7_ems_ineq_tbl_{rng.randint(100000, 999999)}",
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
        tick_val = int(round(max_val * frac))
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="#E2E8F0" stroke-width="1"/>')
        lines.append(f'<text x="{left-8}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#475569">{tick_val}{unit_suffix}</text>')

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
        '<defs><marker id="arr" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#334155"/></marker></defs>',
        '<line x1="215" y1="65" x2="418" y2="65" stroke="#334155" stroke-width="2" marker-end="url(#arr)"/>',
        '<line x1="525" y1="95" x2="525" y2="160" stroke="#334155" stroke-width="2" marker-end="url(#arr)"/>',
        '<line x1="425" y1="195" x2="222" y2="195" stroke="#334155" stroke-width="2" marker-end="url(#arr)"/>',
        '<line x1="115" y1="165" x2="115" y2="100" stroke="#334155" stroke-width="2" marker-end="url(#arr)"/>',
    ]
    for i, (cx, cy) in enumerate(coords):
        text = nodes[i]
        part1 = text[:28]
        part2 = text[28:].strip()
        lines.append(f'<rect x="{cx-95}" y="{cy-26}" width="190" height="52" rx="8" fill="#FFFFFF" stroke="{accent_color}" stroke-width="2"/>')
        if part2:
            lines.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">{part1}</text>')
            lines.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="11" fill="#334155">{part2[:28]}</text>')
        else:
            lines.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">{part1}</text>')
    lines.append("</svg>")
    return "".join(lines)


def arch_01_socio_economic_imbalances_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"During an economic survey in {sc['area']}, community researchers document stark differences in households' "
        f"access to safe housing, healthcare clinics, and quality schooling.\n\n"
        f"Which term best describes these unequal conditions across groups in society?"
    )
    correct = "Socio-economic imbalances"
    distractors = [
        "Balanced trade surplus",
        "Monetary price deflation",
        "Private capital liquidity",
    ]
    explanation = (
        "Socio-economic imbalances refer to inequalities in people's access to essential resources such as "
        "housing, healthcare, education, and a decent standard of living."
    )
    return _mcq(
        rng,
        subskill="01_socio_economic_imbalances_definition",
        title="Defining Socio-Economic Imbalances",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Focus on the phrase describing disparities in housing, healthcare, and education.",
            "tier_2": "Imbalances combine social access (clinics, schools) and economic means (income, housing).",
            "tier_3": f"The correct term is: {correct}.",
        },
        learning_objective_id="lo_ineq_imbalances",
        concept_id="socio_economic_imbalances",
        misconception_tags=["confuses_socio_economic_with_trade"],
    )


def arch_02_standard_of_living_indicators(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    aspect = rng.choice([
        "regular access to clean piped water, adequate food, and safe housing",
        "access to reliable electricity, public transport, and primary clinics",
        "affordability of nutritious groceries, warm clothing, and schooling materials",
    ])
    prompt = (
        f"A municipal report on {sc['area']} examines residents' {aspect}.\n\n"
        f"In Economics, what does the phrase 'standard of living' measure?"
    )
    correct = "The level of access people have to goods, services, and essential resources that determine their daily comfort and wellbeing."
    distractors = [
        "The total number of commercial banks operating within a province.",
        "The exchange rate of the South African Rand against the US dollar.",
        "The fixed interest fee charged by private loan sharks.",
    ]
    explanation = (
        "Standard of living measures how well people live based on their access to goods, services, income, "
        "healthcare, clean water, and education."
    )
    return _mcq(
        rng,
        subskill="02_standard_of_living_indicators",
        title="Understanding Standard of Living",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Think about what determines whether a household lives comfortably or faces daily hardship.",
            "tier_2": "Standard of living depends on access to goods, services, housing, water, and healthcare.",
            "tier_3": "Select the option describing access to goods, services, and wellbeing.",
        },
        learning_objective_id="lo_ineq_standard_living",
        concept_id="standard_of_living",
        misconception_tags=["confuses_standard_of_living_with_fx"],
    )


def arch_03_poverty_line_definition_and_benchmark(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Social workers assisting vulnerable households in {sc['rural_area']} compare weekly earnings against the poverty line.\n\n"
        f"What is the poverty line, and what historical international benchmark is cited in development studies?"
    )
    correct = "The minimum level of income needed to meet basic survival needs, historically benchmarked at US$1 per day."
    distractors = [
        "The maximum salary an entrepreneur is allowed to earn before paying tax.",
        "A government budget surplus equal to 20% of national spending.",
        "The monthly rent charged for formal suburban housing.",
    ]
    explanation = (
        "The poverty line represents the minimum income threshold required to cover basic food, shelter, and daily needs, "
        "historically defined internationally at US$1 per person per day."
    )
    return _mcq(
        rng,
        subskill="03_poverty_line_definition_and_benchmark",
        title="Poverty Line Benchmark",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Does a poverty line mark a maximum wage or a minimum survival threshold?",
            "tier_2": "Recall the historical daily US dollar benchmark for extreme poverty.",
            "tier_3": "It is the minimum income needed for basic needs, historically US$1 per day.",
        },
        learning_objective_id="lo_ineq_poverty_line",
        concept_id="poverty_line",
        misconception_tags=["confuses_poverty_line_with_tax_threshold"],
    )


def arch_04_poverty_line_zar_conversion_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    usd_rate = rng.choice([17.50, 18.20, 18.50, 19.20, 19.80])
    usd_bench = rng.choice([1.0, 1.5, 2.0])
    days = rng.choice([30, 28, 31])
    daily_zar = round(usd_bench * usd_rate, 2)
    monthly_zar = round(daily_zar * days, 2)

    rate_comma = _fmt_comma(usd_rate, 2)
    bench_comma = _fmt_comma(usd_bench, 1) if usd_bench != 1.0 else "1"
    daily_comma = _fmt_comma(daily_zar, 2)
    monthly_comma = _fmt_zar(monthly_zar, 2)

    prompt = (
        f"Researchers in {sc['area']} convert an international poverty benchmark of US${bench_comma} per day into South African Rand (ZAR) "
        f"when the exchange rate is R{rate_comma} per US$1.\n\n"
        f"1. Calculate the poverty line per person per day in Rand.\n"
        f"2. Calculate the equivalent total for one person over a {days}-day month."
    )
    sol = (
        f"(a) **{_fmt_zar(daily_zar, 2)} per day** [2 marks]\n"
        f"$\\text{{Daily ZAR}} = {bench_comma} \\times {rate_comma} = \\text{{R}}{daily_comma}$\n\n"
        f"(b) **{monthly_comma} per month** [2 marks]\n"
        f"$\\text{{Monthly ZAR}} = {daily_comma} \\times {days} = \\text{{{monthly_comma}}}$"
    )
    return _typed(
        rng,
        subskill="04_poverty_line_zar_conversion_calculation",
        title="Converting the Poverty Line to Rand",
        prompt=prompt,
        sample_answer=f"Daily: {_fmt_zar(daily_zar, 2)}; {days}-day month: {monthly_comma}",
        correct_answer=f"{_fmt_zar(daily_zar, 2)} per day; {monthly_comma} per month",
        correct_value=monthly_zar,
        worked_solution=sol,
        marking_points=[
            f"Multiply US${bench_comma} by R{rate_comma} = {_fmt_zar(daily_zar, 2)} per day (2 marks)",
            f"Multiply daily ZAR by {days} days = {monthly_comma} per month (2 marks)",
        ],
        hints={
            "tier_1": "Convert USD to ZAR first using the exchange rate, then scale up by the number of days.",
            "tier_2": f"Daily Poverty Line (ZAR) = US${bench_comma} x R{rate_comma}.",
            "tier_3": f"Daily = {_fmt_zar(daily_zar, 2)}; Monthly ({days} days) = {monthly_comma}.",
        },
        learning_objective_id="lo_ineq_poverty_calc",
        concept_id="poverty_line_zar",
        misconception_tags=["divides_by_exchange_rate_instead_of_multiplying"],
        marks=4,
    )


def arch_05_living_below_poverty_line_hardships(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} interviews families living below the poverty line in {sc['area']}.\n\n"
        f"Describe THREE specific daily hardships faced by people living below the poverty line across basic needs, housing, and hygiene. (3 marks)"
    )
    sample = (
        "1. Basic needs: Households struggle to afford nutritious food, clean drinking water, and primary healthcare regularly.\n"
        "2. Housing: Many live in crowded informal structures or without secure shelter.\n"
        "3. Hygiene and sanitation: Limited access to running water, toilets, and personal hygiene facilities increases illness."
    )
    return _typed(
        rng,
        subskill="05_living_below_poverty_line_hardships",
        title="Standard of Living Below the Poverty Line",
        prompt=prompt,
        sample_answer=sample,
        marking_points=[
            "Struggle to access regular nutritious food, clean water, and healthcare.",
            "Live in informal settlements or insecure shelter.",
            "Lack proper sanitation and personal hygiene facilities.",
        ],
        hints={
            "tier_1": "Group your answer around food/water, shelter, and sanitation.",
            "tier_2": "Consider what basic survival items low income fails to cover.",
            "tier_3": "Mention irregular food/water/healthcare, informal housing, and poor sanitation.",
        },
        learning_objective_id="lo_ineq_hardships",
        concept_id="below_poverty_line",
        misconception_tags=["omits_non_income_dimensions_of_poverty"],
        marks=3,
    )


def arch_06_subsistence_farming_rural_vs_urban_land(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Low-income families in {sc['rural_area']} and {sc['urban_area']} both face tight household food budgets.\n\n"
        f"Why are poor rural households sometimes able to supplement food through subsistence farming whereas poor urban households usually cannot?"
    )
    correct = "Rural families may have small plots of communal or household land for crops (though often lacking funds for fertiliser), whereas crowded urban areas lack available land ownership and space."
    distractors = [
        "Urban soil cannot support vegetables because electricity cables prevent rain from soaking in.",
        "Rural households receive free supermarket delivery trucks every morning.",
        "Municipal bylaws ban all urban residents from buying vegetable seeds.",
    ]
    explanation = (
        "In rural communities, families sometimes grow vegetables or keep chickens for survival if land is available, "
        "though affordability of fertiliser remains a barrier. In dense urban townships, lack of land access makes subsistence farming impractical."
    )
    return _mcq(
        rng,
        subskill="06_subsistence_farming_rural_vs_urban_land",
        title="Subsistence Farming: Rural vs Urban Context",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Compare land space available in villages versus high-density city settlements.",
            "tier_2": "Subsistence farming depends primarily on access to arable land.",
            "tier_3": f"Choose: {correct}",
        },
        learning_objective_id="lo_ineq_subsistence",
        concept_id="subsistence_farming",
        misconception_tags=["ignores_urban_land_scarcity"],
    )


def arch_07_constitution_bill_of_rights_equality(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"In a Grade 7 civic discussion in {sc['area']}, learners examine South Africa's legal guarantee of equality.\n\n"
        f"1. Which chapter and section of the South African Constitution guarantees equality for all citizens? (2 marks)\n"
        f"2. Why does a gap still exist between this constitutional promise and everyday economic life? (2 marks)"
    )
    sample = (
        "1. Chapter 2 of the Constitution (The Bill of Rights) guarantees that all citizens are equal before the law.\n"
        "2. Economic inequality persists because deeply rooted structural disadvantages in education, wealth, and infrastructure take generations to repair."
    )
    return _typed(
        rng,
        subskill="07_constitution_bill_of_rights_equality",
        title="The Constitution & Economic Reality",
        prompt=prompt,
        sample_answer=sample,
        marking_points=[
            "Identify Chapter 2 / The Bill of Rights in the South African Constitution.",
            "Equal legal rights do not instantly erase historical poverty, skills gaps, or unequal infrastructure.",
        ],
        hints={
            "tier_1": "Think of the human rights section near the start of South Africa's 1996 Constitution.",
            "tier_2": "Chapter 2 (Bill of Rights) grants legal equality, but reversing historical wealth and education gaps takes decades.",
            "tier_3": "Chapter 2 (Bill of Rights); historical structural exclusion takes long-term investment to fix.",
        },
        learning_objective_id="lo_ineq_constitution",
        concept_id="bill_of_rights",
        misconception_tags=["confuses_legal_equality_with_income_equality"],
        marks=4,
    )


def arch_08_apartheid_structural_exclusion_causes(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Studying historical economic development near {sc['area']}, learners investigate why wealth and income remain unevenly distributed.\n\n"
        f"Which combination best explains how apartheid policies caused long-term socio-economic imbalances in South Africa?"
    )
    correct = "Laws restricted where Black, Coloured, and Indian citizens could live and own land, reserved skilled jobs for white workers, and denied quality education and affordable healthcare to the majority."
    distractors = [
        "Every province received identical school funding, equal hospital beds, and unrestricted land ownership before 1994.",
        "South Africa had zero natural mineral wealth or factories prior to the year 2000.",
        "High-interest store credit cards were banned in cities while wages were equalised everywhere.",
    ]
    explanation = (
        "Apartheid created structural exclusion through racially discriminatory education, job reservation policies, "
        "forced residential segregation, and unequal access to land, capital, and healthcare."
    )
    return _mcq(
        rng,
        subskill="08_apartheid_structural_exclusion_causes",
        title="Historical Causes of Inequality",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Look for policies affecting housing, job access, and school quality simultaneously.",
            "tier_2": "Apartheid restricted land ownership, job mobility, and educational investment by race.",
            "tier_3": f"Correct answer: {correct}",
        },
        learning_objective_id="lo_ineq_apartheid_causes",
        concept_id="structural_exclusion",
        misconception_tags=["ignores_systemic_barriers"],
    )


def arch_09_intergenerational_poverty_cycle_diagram(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    missing_stage = rng.choice([
        ("Poor Access to Quality Education", "Low Skills & Unemployed / Low Wage"),
        ("Low Household Income", "Inability to Afford Schooling & Nutrition"),
        ("Low Skills & Unemployed / Low Wage", "Low Household Income"),
    ])
    svg = _svg_cycle_flow(
        f"Cycle of Poverty Observed in {sc['rural_area'].split('(')[0].strip()}",
        [
            "Stage A: Low Household Income",
            "Stage B: Poor Nutrition & Clinics",
            "Stage C: [ ? Missing Link ? ]",
            "Stage D: Limited Job Mobility",
        ],
        accent_color="#B91C1C",
    )
    prompt = (
        f"Refer to the economic cycle flowchart below analysing poverty traps around {sc['rural_area']}.\n\n"
        f"If Stage A is low household income and Stage B causes poor nutrition and weak health support, "
        f"what critical Stage C link directly traps the next generation into Stage D (limited job mobility)?"
    )
    correct = "Lack of quality education and specialised skills training"
    distractors = [
        "Excessive personal savings in commercial banks",
        "Over-investment in automated factory robotics",
        "High municipal tax surpluses from wealthy estates",
    ]
    explanation = (
        "Without adequate income for nutritious food, study resources, and quality schools, children lack formal "
        "qualifications and specialised skills, leading directly to low-paid or scarce work in adulthood."
    )
    return _mcq(
        rng,
        subskill="09_intergenerational_poverty_cycle_diagram",
        title="Breaking the Poverty Cycle",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Follow the clockwise arrows from Stage B toward job mobility in Stage D.",
            "tier_2": "What prevents young people from qualifying for higher-paying skilled jobs?",
            "tier_3": f"Stage C is: {correct}.",
        },
        learning_objective_id="lo_ineq_poverty_cycle",
        concept_id="poverty_cycle",
        misconception_tags=["misreads_cycle_causality"],
        diagram_spec={"kind": "inline_svg", "title": "Intergenerational Poverty Cycle", "svg": svg, "diagram_role": "context"},
    )


def arch_10_twelve_year_generation_education_lag(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cohort_size = rng.choice([1200, 1500, 1800, 2400])
    grad_years = 12
    prompt = (
        f"In {sc['area']}, education planners evaluate why socio-economic imbalances persist decades after policy reform. "
        f"A Grade 1 cohort of {cohort_size} learners takes {grad_years} years of basic schooling to reach matric.\n\n"
        f"Explain why education requires a long-term commitment (~{grad_years} years per generation) before narrowing national income inequality. (3 marks)"
    )
    sample = (
        f"Educating a single generation from Grade 1 to Grade 12 takes approximately {grad_years} years, plus further post-school training "
        f"before all {cohort_size} learners enter skilled careers and break their families' poverty cycle."
    )
    return _typed(
        rng,
        subskill="10_twelve_year_generation_education_lag",
        title="Why Inequality Persists Long-Term",
        prompt=prompt,
        sample_answer=sample,
        marking_points=[
            f"Schooling a generation from Grade 1 to Grade 12 takes ~{grad_years} years.",
            "Learners must also acquire tertiary/artisan skills before earning higher salaries.",
            "Historical backlogs in schools and family wealth take multiple generations to erase.",
        ],
        hints={
            "tier_1": "Count how many years a child spends in school from Grade 1 through Matric.",
            "tier_2": "Building skilled human capital cannot happen overnight; it takes ~12 years per generation.",
            "tier_3": f"Mention the {grad_years}-year schooling timeline and gradual transition into skilled jobs.",
        },
        learning_objective_id="lo_ineq_edu_lag",
        concept_id="education_generation_lag",
        misconception_tags=["expects_instant_policy_impact"],
        marks=3,
    )


def arch_11_employment_equity_and_bbbee_reforms(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    act_choice = rng.choice([
        (
            "The Employment Equity Act of 1998",
            "Eliminating unfair workplace discrimination and ensuring equal opportunities and fair representation for previously disadvantaged groups",
            "Setting daily foreign exchange tariffs for imported fuel",
        ),
        (
            "Broad-Based Black Economic Empowerment (BBBEE)",
            "Promoting broader economic ownership, skills development, management participation, and enterprise support for historically excluded citizens",
            "Replacing commercial bank ATMs with paper cheque books",
        ),
    ])
    act_name, purpose, wrong = act_choice
    prompt = (
        f"Following South Africa's new Constitution, corrective legislation was introduced for employers operating in {sc['area']}.\n\n"
        f"What is the primary economic objective of **{act_name}**?"
    )
    return _mcq(
        rng,
        subskill="11_employment_equity_and_bbbee_reforms",
        title="Corrective Economic Legislation",
        prompt=prompt,
        correct=purpose,
        distractors=[
            wrong,
            "Restricting rural entrepreneurs from registering formal businesses in urban centres",
            "Abolishing social grants and minimum wage standards",
        ],
        explanation=f"{act_name} directly aims at redressing past economic exclusion by {purpose.lower()}.",
        hints={
            "tier_1": "Recall what South African laws were passed after 1994 to fix historical workplace and ownership exclusion.",
            "tier_2": f"Think about fairness, representation, and inclusion under {act_name}.",
            "tier_3": f"Select: {purpose}",
        },
        learning_objective_id="lo_ineq_legislation",
        concept_id="corrective_legislation",
        misconception_tags=["confuses_equity_laws_with_tax"],
    )


def arch_12_fiscal_policy_wealth_luxury_tax_redistribution(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    grant_monthly = rng.choice([530, 560, 2180])
    households = rng.choice([25, 40, 50])
    total_transfer = grant_monthly * households
    prompt = (
        f"To reduce inequality between wealthy suburbs and underserved settlements near {sc['area']}, "
        f"National Treasury collects extra revenue from wealth and luxury-item taxes and funds social grants of {_fmt_zar(grant_monthly)} per month "
        f"for {households} vulnerable households.\n\n"
        f"1. State how progressive wealth and luxury taxes help reduce inequality. (2 marks)\n"
        f"2. Calculate the total monthly social support distributed to these {households} households. (2 marks)"
    )
    sol = (
        f"(a) **Redistribution from higher-income groups to impoverished communities** [2 marks]\n"
        f"Higher tax contributions on wealth and luxury goods fund clinics, schools, water infrastructure, and grants in poorer areas.\n\n"
        f"(b) **{_fmt_zar(total_transfer)}** [2 marks]\n"
        f"${households} \\times {_fmt_zar(grant_monthly)} = \\text{{{_fmt_zar(total_transfer)}}}$"
    )
    return _typed(
        rng,
        subskill="12_fiscal_policy_wealth_luxury_tax_redistribution",
        title="Fiscal Redistribution & Social Grants",
        prompt=prompt,
        sample_answer=f"Wealth/luxury taxes redistribute resources to clinics, schools, and grants; Total monthly grants = {_fmt_zar(total_transfer)}",
        correct_answer=_fmt_zar(total_transfer),
        correct_value=float(total_transfer),
        worked_solution=sol,
        marking_points=[
            "Wealth and luxury taxes shift funds from affluent consumption into public services and poverty relief.",
            "Social grants directly raise household purchasing power for food and essentials.",
            f"Correct multiplication: {households} x {_fmt_zar(grant_monthly)} = {_fmt_zar(total_transfer)}.",
        ],
        hints={
            "tier_1": "Explain who pays luxury/wealth taxes and who benefits from grant transfers.",
            "tier_2": f"Multiply {households} households by {_fmt_zar(grant_monthly)} per household.",
            "tier_3": f"Redistribution raises funds for poorer areas; total monthly transfer = {_fmt_zar(total_transfer)}.",
        },
        learning_objective_id="lo_ineq_fiscal_redistribution",
        concept_id="fiscal_policy",
        misconception_tags=["ignores_tax_redistribution_link"],
        marks=4,
    )


def arch_13_education_budget_allocation_calculation(rng: random.Random) -> Dict[str, Any]:
    total_budget_bn = rng.choice([1800, 2000, 2100, 2250, 2400])
    edu_pct = 20
    edu_amount_bn = int(total_budget_bn * edu_pct / 100)
    non_edu_bn = total_budget_bn - edu_amount_bn

    svg = _svg_bar_chart(
        f"National Budget Split (Total: R{total_budget_bn} Billion)",
        "Rand Billions",
        [
            ("Education (20%)", edu_amount_bn, "#1D4ED8"),
            ("All Other Votes (80%)", non_edu_bn, "#94A3B8"),
        ],
        total_budget_bn,
        unit_suffix="B",
    )
    prompt = (
        f"Refer to the bar graph below. South Africa allocates roughly **{edu_pct}%** of its National Budget to education.\n\n"
        f"If the total National Budget is **R{total_budget_bn} billion**, calculate the exact Rand amount allocated to education, "
        f"and explain why prioritising education spending helps reduce future inequality."
    )
    sol = (
        f"(a) **R{edu_amount_bn} billion** [2 marks]\n"
        f"$\\text{{Education Allocation}} = \\frac{{{edu_pct}}}{{100}} \\times {total_budget_bn} = \\text{{R}}{edu_amount_bn}\\text{{ billion}}$\n\n"
        f"(b) **Human Capital Empowerment** [2 marks]\n"
        f"Funding schools and training builds skills across low-income youth, enabling higher-paid employment and breaking the poverty cycle."
    )
    return _typed(
        rng,
        subskill="13_education_budget_allocation_calculation",
        title="National Education Budget Share",
        prompt=prompt,
        sample_answer=f"R{edu_amount_bn} billion; education equips youth with skills for better-paid jobs and reduces long-term poverty.",
        correct_answer=f"R{edu_amount_bn} billion",
        correct_value=float(edu_amount_bn),
        worked_solution=sol,
        marking_points=[
            f"Calculate 20% of R{total_budget_bn} billion = R{edu_amount_bn} billion.",
            "Explain that educated citizens earn higher incomes and escape poverty.",
        ],
        hints={
            "tier_1": "Multiply the total budget by 20% (or divide by 5).",
            "tier_2": f"20% of {total_budget_bn} = 0,20 x {total_budget_bn}.",
            "tier_3": f"Education receives R{edu_amount_bn} billion to build workforce skills.",
        },
        learning_objective_id="lo_ineq_edu_budget",
        concept_id="education_budget",
        misconception_tags=["miscalculates_percentage_of_budget"],
        marks=4,
        diagram_spec={"kind": "inline_svg", "title": "National Education Budget Allocation", "svg": svg, "diagram_role": "context"},
    )


def arch_14_consequences_of_poor_quality_education(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    focus = rng.choice([
        ("crumbling classrooms, missing desks, and shared textbooks", "Inadequate infrastructure"),
        ("under-qualified teachers lacking ongoing subject methodology support", "Poor human capital"),
        ("high absenteeism and discouraged learners dropping out early", "Low motivation"),
    ])
    clue, correct = focus
    prompt = (
        f"An education audit in {sc['rural_area']} identifies a widespread problem: **{clue}**.\n\n"
        f"Which systemic consequence of poor quality education does this observation directly represent?"
    )
    all_opts = [
        "Inadequate infrastructure",
        "Poor human capital",
        "Low motivation",
        "Automated capital surplus",
    ]
    distractors = [o for o in all_opts if o != correct]
    return _mcq(
        rng,
        subskill="14_consequences_of_poor_quality_education",
        title="Consequences of Poor Quality Education",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Poor quality schooling manifests in three main ways: inadequate physical infrastructure (buildings/books), "
            f"poor human capital (teacher training), and low motivation among learners and educators. Here '{clue}' reflects {correct}."
        ),
        hints={
            "tier_1": "Match the audit observation to buildings/equipment, teacher training, or morale.",
            "tier_2": f"Re-read '{clue}' carefully to identify which category it belongs to.",
            "tier_3": f"Correct classification: {correct}.",
        },
        learning_objective_id="lo_ineq_poor_edu_effects",
        concept_id="poor_education_consequences",
        misconception_tags=["confuses_infrastructure_with_human_capital"],
    )


def arch_15_skills_shortage_definition_and_causes(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    role = rng.choice(["civil engineers", "medical doctors", "chartered accountants", "qualified ICT technicians"])
    prompt = (
        f"Hospitals and municipalities near {sc['area']} advertise vacancies for **{role}**, yet positions stay empty for months "
        f"because too few applicants hold the required qualifications.\n\n"
        f"What economic problem is occurring here?"
    )
    correct = "A skills shortage: insufficient qualified specialists exist within the country to fill available specialised roles."
    distractors = [
        "Hyperinflation caused by excessive agricultural surpluses.",
        "Complete elimination of consumer wants across rural provinces.",
        "Over-supply of trained university professors in rural clinics.",
    ]
    explanation = (
        "A skills shortage happens when the demand for specific specialised expertise (such as doctors, engineers, "
        "teachers, or accountants) exceeds the supply of qualified people available in the country."
    )
    return _mcq(
        rng,
        subskill="15_skills_shortage_definition_and_causes",
        title="Defining a Skills Shortage",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Notice that jobs are available, yet employers cannot find qualified people.",
            "tier_2": "This mismatch between specialised vacancies and qualified workers is a shortage of skills.",
            "tier_3": f"Correct option: {correct}",
        },
        learning_objective_id="lo_ineq_skills_shortage_def",
        concept_id="skills_shortage",
        misconception_tags=["confuses_skills_shortage_with_lack_of_jobs"],
    )


def arch_16_sa_key_skills_shortage_sectors_bar_chart(rng: random.Random) -> Dict[str, Any]:
    v_eng = rng.randint(14, 24) * 100
    v_med = rng.randint(11, 20) * 100
    v_ict = rng.randint(9, 17) * 100
    v_teach = rng.randint(12, 22) * 100
    v_mgmt = rng.randint(7, 13) * 100
    bars = [
        ("Engineering", v_eng, "#1D4ED8"),
        ("Medical", v_med, "#0F766E"),
        ("ICT", v_ict, "#7C3AED"),
        ("Teaching", v_teach, "#D97706"),
        ("Management", v_mgmt, "#DC2626"),
    ]
    top_sector, top_val, _ = max(bars, key=lambda x: x[1])
    total_vac = sum(x[1] for x in bars)
    svg = _svg_bar_chart(
        "Unfilled Scarce-Skills Vacancies Across 5 SA Sectors",
        "Open Vacancies",
        [(b[0], float(b[1]), b[2]) for b in bars],
        float(max(2500, ((top_val // 500) + 1) * 500)),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below showing unfilled scarce-skills vacancies across five key South African sectors.\n\n"
        f"1. Which scarce-skills sector shows the highest number of unfilled vacancies? (1 mark)\n"
        f"2. Calculate the combined total of scarce-skills vacancies across all five sectors. (2 marks)"
    )
    sol = (
        f"(a) **{top_sector}** ({top_val} vacancies) [1 mark]\n\n"
        f"(b) **{total_vac} total vacancies** [2 marks]\n"
        f"${v_eng} + {v_med} + {v_ict} + {v_teach} + {v_mgmt} = {total_vac}$"
    )
    return _typed(
        rng,
        subskill="16_sa_key_skills_shortage_sectors_bar_chart",
        title="South Africa's Scarce-Skills Sectors",
        prompt=prompt,
        sample_answer=f"Highest sector: {top_sector} ({top_val}); Total across 5 sectors: {total_vac} vacancies",
        correct_answer=f"{top_sector}; {total_vac}",
        correct_value=float(total_vac),
        worked_solution=sol,
        marking_points=[
            f"Identify {top_sector} as having the tallest bar ({top_val} vacancies).",
            f"Sum all five bars correctly: {total_vac} vacancies.",
        ],
        hints={
            "tier_1": "Find the tallest bar first, then add all five sector numbers together.",
            "tier_2": f"Sum: {v_eng} + {v_med} + {v_ict} + {v_teach} + {v_mgmt}.",
            "tier_3": f"Highest: {top_sector} ({top_val}); Total: {total_vac}.",
        },
        learning_objective_id="lo_ineq_scarce_sectors",
        concept_id="scarce_skills_sectors",
        misconception_tags=["omits_bar_in_total_sum"],
        marks=3,
        diagram_spec={"kind": "inline_svg", "title": "Scarce-Skills Sector Vacancies", "svg": svg, "diagram_role": "context"},
    )


def arch_17_skills_shortages_hinder_economic_growth(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sector = rng.choice(["water-treatment plant", "renewable solar factory", "logistics engineering depot"])
    prompt = (
        f"A fast-growing {sector} near {sc['area']} wins new export orders, yet cannot open a second production shift "
        f"because there are not enough certified technicians and managers locally.\n\n"
        f"Explain how a national skills shortage directly slows economic growth and job creation. (4 marks)"
    )
    sample = (
        "1. Businesses cannot expand operations or run additional shifts without qualified specialists.\n"
        "2. Unable to expand, firms cannot hire additional semi-skilled or unskilled support workers.\n"
        "3. Lower production capacity reduces total goods sold and slows national GDP growth.\n"
        "4. Reduced company profits also shrink tax revenue needed for public services."
    )
    return _typed(
        rng,
        subskill="17_skills_shortages_hinder_economic_growth",
        title="Impact of Skills Shortages on Growth",
        prompt=prompt,
        sample_answer=sample,
        marking_points=[
            "Firms cannot expand output without qualified specialists.",
            "Failure to expand prevents hiring extra support staff (worsening unemployment).",
            "Lower business output slows national economic growth (GDP).",
        ],
        hints={
            "tier_1": "Think about what happens to factory expansion and hiring when key specialists are missing.",
            "tier_2": "Connect stalled business expansion to fewer entry-level jobs and lower GDP.",
            "tier_3": "No specialists -> no expansion -> fewer support jobs -> slower GDP growth.",
        },
        learning_objective_id="lo_ineq_skills_growth_drag",
        concept_id="skills_growth_impact",
        misconception_tags=["ignores_multiplier_effect_of_skilled_workers"],
        marks=4,
    )


def arch_18_skills_development_act_1998_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"To overcome severe workforce skill gaps affecting firms in {sc['area']}, Parliament passed the **Skills Development Act of 1998**.\n\n"
        f"What is the primary purpose of this legislation?"
    )
    correct = "To use structured education, workplace training, and skills development to fight socio-economic inequality and boost workforce productivity."
    distractors = [
        "To prevent businesses from purchasing automated production machinery.",
        "To close technical colleges in rural municipalities.",
        "To replace household budgets with mandatory stokvel memberships.",
    ]
    explanation = (
        "The Skills Development Act of 1998 aims to upskill South Africa's workforce so citizens gain qualifications "
        "to access better jobs, raise productivity, and combat historical inequality."
    )
    return _mcq(
        rng,
        subskill="18_skills_development_act_1998_purpose",
        title="Skills Development Act of 1998",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Focus on how training empowers workers and fights past injustice.",
            "tier_2": "The Act invests in training and education to close skills shortages and reduce inequality.",
            "tier_3": f"Correct answer: {correct}",
        },
        learning_objective_id="lo_ineq_skills_act",
        concept_id="skills_development_act",
        misconception_tags=["misreads_labour_legislation"],
    )


def arch_19_learnerships_work_based_training_mechanics(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    trade = rng.choice(["diesel mechanic", "qualified electrician", "hospital pharmacy assistant", "junior bookkeeper"])
    prompt = (
        f"{sc['entrepreneur']} enrols in a 12-month **learnership** with a business in {sc['area']} to train as a {trade}.\n\n"
        f"Which statement accurately describes how a learnership works?"
    )
    correct = "A work-based learning programme where a participant works inside a business while simultaneously completing formal theoretical training for that specific occupation."
    distractors = [
        "An unpaid five-year university degree with zero practical workplace experience.",
        "A short-term cash loan granted by a commercial bank for luxury purchases.",
        "An informal neighbourhood savings club that pays out groceries in December.",
    ]
    explanation = (
        "A learnership combines structured classroom/theoretical learning with practical paid on-the-job workplace "
        "training at an employer, culminating in a recognised occupational qualification."
    )
    return _mcq(
        rng,
        subskill="19_learnerships_work_based_training_mechanics",
        title="Understanding Learnerships",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=explanation,
        hints={
            "tier_1": "Think of the two halves of a learnership: classroom theory + real workplace practice.",
            "tier_2": "A learnership lets a trainee work at a business while studying for a specific job.",
            "tier_3": f"Correct option: {correct}",
        },
        learning_objective_id="lo_ineq_learnerships",
        concept_id="learnerships",
        misconception_tags=["confuses_learnership_with_fulltime_school"],
    )


def arch_20_virtuous_cycle_of_skills_and_growth_diagram(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    wage_before = rng.choice([2800, 3200, 3500])
    wage_after = wage_before * rng.choice([2, 3])
    gain = wage_after - wage_before
    svg = _svg_cycle_flow(
        f"Virtuous Skills & Equality Cycle ({sc['area'].split('(')[0].strip()})",
        [
            "1. Education & Skills Training",
            f"2. Higher Pay ({_fmt_zar(wage_after)}/mo)",
            "3. Invest in Children & Taxes",
            "4. Stronger GDP & More Jobs",
        ],
        accent_color="#0F766E",
    )
    prompt = (
        f"Refer to the cycle flowchart below. Before completing technical training in {sc['area']}, "
        f"a worker earned {_fmt_zar(wage_before)} per month. After qualifying, monthly earnings rose to {_fmt_zar(wage_after)}.\n\n"
        f"1. Calculate the monthly income gain from acquiring marketable skills. (1 mark)\n"
        f"2. Explain how this individual income gain creates a positive cycle that lowers inequality across the wider economy. (3 marks)"
    )
    sol = (
        f"(a) **{_fmt_zar(gain)} per month** [1 mark]\n"
        f"${_fmt_zar(wage_after)} - {_fmt_zar(wage_before)} = {_fmt_zar(gain)}$\n\n"
        f"(b) **Economic Multiplier Cycle** [3 marks]\n"
        f"Higher income enables families to fund quality schooling for their children, boosts workforce productivity and GDP, "
        f"and increases tax revenue for government schools and jobs, narrowing socio-economic gaps."
    )
    return _typed(
        rng,
        subskill="20_virtuous_cycle_of_skills_and_growth_diagram",
        title="Skills Development Cycle",
        prompt=prompt,
        sample_answer=f"Gain: {_fmt_zar(gain)}; Higher pay funds children's education, raises productivity/GDP, and grows public tax revenue.",
        correct_answer=_fmt_zar(gain),
        correct_value=float(gain),
        worked_solution=sol,
        marking_points=[
            f"Subtract {_fmt_zar(wage_before)} from {_fmt_zar(wage_after)} = {_fmt_zar(gain)}.",
            "Higher earners invest in family education and health.",
            "Productive workers expand business output (GDP) and fund tax revenue for further jobs.",
        ],
        hints={
            "tier_1": "First subtract old earnings from new earnings; then trace the clockwise arrows around the loop.",
            "tier_2": f"Gain = {_fmt_zar(wage_after)} - {_fmt_zar(wage_before)}. Trace how wages fund family education and GDP.",
            "tier_3": f"Monthly gain = {_fmt_zar(gain)}; explain family education investment + GDP + job creation.",
        },
        learning_objective_id="lo_ineq_virtuous_cycle",
        concept_id="skills_virtuous_cycle",
        misconception_tags=["misses_fiscal_and_family_feedback"],
        marks=4,
        diagram_spec={"kind": "inline_svg", "title": "Virtuous Skills Cycle", "svg": svg, "diagram_role": "context"},
    )


def arch_21_urbanization_and_rural_poverty_stats_bar_graph(rng: random.Random) -> Dict[str, Any]:
    urban_pop_pct = rng.choice([62, 64, 66])
    rural_pop_pct = 100 - urban_pop_pct
    rural_poor_share = rng.choice([68, 70, 72])
    urban_poor_share = 100 - rural_poor_share

    svg = _svg_bar_chart(
        "South African Population Share vs Share of Poverty (%)",
        "Percentage (%)",
        [
            ("Urban Pop.", float(urban_pop_pct), "#2563EB"),
            ("Rural Pop.", float(rural_pop_pct), "#16A34A"),
            ("Poor in Rural", float(rural_poor_share), "#DC2626"),
            ("Poor in Urban", float(urban_poor_share), "#F59E0B"),
        ],
        100.0,
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the bar graph below comparing total population distribution against where poor South Africans reside.\n\n"
        f"1. What percentage of the total population lives in urban areas? (1 mark)\n"
        f"2. What percentage of South Africa's poor population resides in rural areas, and what does this contrast suggest? (3 marks)"
    )
    sol = (
        f"(a) **{urban_pop_pct}%** live in urban areas [1 mark]\n\n"
        f"(b) **{rural_poor_share}%** of poor residents live in rural areas [1 mark]\n"
        f"Even though only {rural_pop_pct}% of citizens live in rural regions, {rural_poor_share}% of poverty is concentrated there due to "
        f"fewer formal jobs, lower wages, and weaker infrastructure [2 marks]."
    )
    return _typed(
        rng,
        subskill="21_urbanization_and_rural_poverty_stats_bar_graph",
        title="Urban vs Rural Poverty Concentration",
        prompt=prompt,
        sample_answer=f"Urban population: {urban_pop_pct}%; Poor in rural areas: {rural_poor_share}% — showing poverty is heavily concentrated in rural communities despite smaller population size.",
        correct_answer=f"{urban_pop_pct}%; {rural_poor_share}%",
        worked_solution=sol,
        marking_points=[
            f"Read Urban Pop. bar = {urban_pop_pct}%.",
            f"Read Poor in Rural bar = {rural_poor_share}%.",
            "Explain disproportionate rural poverty concentration despite smaller rural population share.",
        ],
        hints={
            "tier_1": "Compare the green Rural Pop. bar with the tall red Poor in Rural bar.",
            "tier_2": f"Urban Pop = {urban_pop_pct}%; Rural Poor Share = {rural_poor_share}%.",
            "tier_3": f"State {urban_pop_pct}% urban and {rural_poor_share}% rural poverty share, explaining the mismatch.",
        },
        learning_objective_id="lo_ineq_urban_rural_stats",
        concept_id="rural_poverty_share",
        misconception_tags=["confuses_population_share_with_poverty_share"],
        marks=4,
        diagram_spec={"kind": "inline_svg", "title": "Urban vs Rural Population & Poverty", "svg": svg, "diagram_role": "context"},
    )


def arch_22_rural_tax_base_and_service_delivery_cost(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    households = rng.choice([200, 300, 400])
    urban_pipe_m = rng.choice([8, 10])
    rural_pipe_m = rng.choice([65, 80, 95])
    urban_total = households * urban_pipe_m
    rural_total = households * rural_pipe_m
    ratio = round(rural_total / urban_total, 1)

    prompt = (
        f"Compare laying water pipelines for {households} households in dense {sc['urban_area']} "
        f"({urban_pipe_m} m per household) versus scattered villages in {sc['rural_area']} ({rural_pipe_m} m per household).\n\n"
        f"1. Calculate total pipeline metres needed in the rural district versus the urban district. (2 marks)\n"
        f"2. Give TWO financial reasons why rural municipalities struggle to fund and deliver basic services. (2 marks)"
    )
    sol = (
        f"(a) **Rural: {rural_total:,} m | Urban: {urban_total:,} m** ({_fmt_comma(ratio, 1)}x longer in rural) [2 marks]\n"
        f"- Rural: ${households} \\times {rural_pipe_m} = {rural_total}$ m\n"
        f"- Urban: ${households} \\times {urban_pipe_m} = {urban_total}$ m\n\n"
        f"(b) **Why rural delivery lags:** [2 marks]\n"
        f"1. Low population density spreads homes over vast distances, driving up pipeline/road costs.\n"
        f"2. Smaller local tax base (fewer taxpayers and lower rural wages) leaves less municipal revenue."
    ).replace(",", " ")
    return _typed(
        rng,
        subskill="22_rural_tax_base_and_service_delivery_cost",
        title="Rural Density, Tax Base & Service Costs",
        prompt=prompt,
        sample_answer=f"Rural: {rural_total} m vs Urban: {urban_total} m. Rural areas face dispersed households (high cost per person) and fewer taxpayers / lower incomes (smaller tax base).",
        correct_answer=f"{rural_total} m vs {urban_total} m",
        correct_value=float(rural_total),
        worked_solution=sol,
        marking_points=[
            f"Rural pipeline length = {rural_total} m; Urban = {urban_total} m.",
            "Low density over long distances makes infrastructure expensive.",
            "Fewer taxpayers and lower wages create a weaker municipal tax base.",
        ],
        hints={
            "tier_1": "Multiply households by metres per household for each area, then consider municipal tax income.",
            "tier_2": f"Rural = {households} x {rural_pipe_m}; Urban = {households} x {urban_pipe_m}.",
            "tier_3": f"Rural needs {rural_total} m vs {urban_total} m; sparse density raises costs while fewer taxpayers cut revenue.",
        },
        learning_objective_id="lo_ineq_rural_tax_base",
        concept_id="rural_service_economics",
        misconception_tags=["ignores_population_density_cost"],
        marks=4,
    )


def arch_23_urban_challenges_informal_settlements_and_overcrowding(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    challenge = rng.choice([
        ("Rapid rural-to-urban migration outpaces affordable formal housing supply", "Overcrowding and informal settlements"),
        ("High youth populations compete for scarce formal factory and office roles", "High unemployment and skills mismatch"),
        ("Dense city populations strain bus networks, sewage pipes, and clinics", "Severe pressure on urban transport and municipal infrastructure"),
    ])
    cause, effect = challenge
    prompt = (
        f"City planners in {sc['urban_area']} record that **{cause.lower()}**.\n\n"
        f"Which urban socio-economic challenge results directly from this trend?"
    )
    return _mcq(
        rng,
        subskill="23_urban_challenges_informal_settlements_and_overcrowding",
        title="Urban Socio-Economic Pressures",
        prompt=prompt,
        correct=effect,
        distractors=[
            "Excess empty farm land and scarce urban population density",
            "Complete absence of industrial factories or commercial banks",
            "Guaranteed luxury housing for every incoming job-seeker",
        ],
        explanation=f"In major South African cities, {cause.lower()}, directly causing {effect.lower()}.",
        hints={
            "tier_1": "Think about what happens when thousands of people move into a city faster than houses or jobs grow.",
            "tier_2": f"Match '{cause}' to housing, jobs, or infrastructure strain.",
            "tier_3": f"Correct consequence: {effect}.",
        },
        learning_objective_id="lo_ineq_urban_challenges",
        concept_id="urban_challenges",
        misconception_tags=["confuses_urban_overcrowding_with_rural_sparsity"],
    )


def arch_24_acid_mine_drainage_environmental_economic_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Communities living downstream from abandoned gold and coal mines near {sc['area']} report contaminated river water "
        f"turning acidic and orange-brown, known as **acid mine drainage (AMD)**.\n\n"
        f"Explain TWO negative economic or living-standard impacts of acid mine drainage on local households and rural agriculture. (4 marks)"
    )
    sample = (
        "1. Polluted rivers poison livestock and crops, destroying small farmers' incomes and food security.\n"
        "2. Households face unsafe drinking water and higher healthcare costs from water-borne illnesses.\n"
        "3. Degraded land loses value and requires expensive government clean-up spending."
    )
    return _typed(
        rng,
        subskill="24_acid_mine_drainage_environmental_economic_impact",
        title="Acid Mine Drainage & Community Economy",
        prompt=prompt,
        sample_answer=sample,
        marking_points=[
            "Damages soil and irrigation water, reducing agricultural output and farm incomes.",
            "Threatens clean drinking water and human health, raising medical costs for poor households.",
        ],
        hints={
            "tier_1": "Consider how acidic, heavy-metal water affects crops, cattle, and household drinking supplies.",
            "tier_2": "Link polluted water directly to lost farming livelihoods and community health bills.",
            "tier_3": "Mention crop/livestock damage reducing income AND unsafe drinking water harming health.",
        },
        learning_objective_id="lo_ineq_amd",
        concept_id="acid_mine_drainage",
        misconception_tags=["treats_amd_as_purely_natural_without_economic_cost"],
        marks=4,
    )


def arch_25_urban_vs_rural_classification_schedule_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pairs = rng.sample([
        ("Severe shortage of affordable housing leading to informal settlements", "Urban", "High rural-to-urban migration and land pressure drive informal settlements in cities."),
        ("Fewer taxpayers and scattered distances making water piping costly", "Rural", "Low population density and lower rural incomes reduce the local municipal tax base."),
        ("Heavy industrial air pollution and overloaded commuter transport", "Urban", "Factories and commuter congestion concentrate environmental strain inside cities."),
        ("Long travel distances and costly transport to regional hospitals", "Rural", "Rural clinics are sparse, forcing costly long-distance travel for medical care."),
        ("High concentration of skilled service firms alongside intense job competition", "Urban", "Urban hubs offer more formal roles, yet face intense competition and skills mismatch."),
    ], 4)

    headers = ["Socio-Economic Challenge", "Primary Setting (Urban / Rural)", "Extra Policy Flag (Leave Blank)"]
    raw_rows = []
    cell_hints = {}
    derivations = []
    for idx, (desc, setting, reason) in enumerate(pairs):
        raw_rows.append([
            {"type": "given", "value": desc},
            {"type": "required", "expected": setting},
            {"type": "must_be_empty"},
        ])
        cell_hints[f"r{idx}_c1"] = f"Ask: does '{desc[:42]}...' typically occur in dense cities (Urban) or sparsely populated countryside (Rural)?"
        cell_hints[f"r{idx}_c2"] = "Leave this column empty; only classify each challenge in the middle column."
        derivations.append(f"Row {idx + 1} ({setting}): {reason}")

    prompt = (
        f"Researchers comparing {sc['urban_area']} and {sc['rural_area']} compiled four socio-economic challenges.\n\n"
        f"Classify each challenge in the middle column by typing **Urban** or **Rural**. "
        f"Leave the rightmost column completely blank."
    )
    return _table_q(
        rng,
        subskill="25_urban_vs_rural_classification_schedule_table",
        title="Urban vs Rural Socio-Economic Matrix",
        prompt=prompt,
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Read each challenge and decide whether it describes dense city life or sparse countryside conditions.",
            "tier_2": "Cities struggle with overcrowding and informal settlements; rural regions struggle with distance and fewer taxpayers.",
            "tier_3": "Classify each row as exactly 'Urban' or 'Rural' and leave the rightmost column blank.",
        },
        learning_objective_id="lo_ineq_urban_rural_table",
        concept_id="urban_vs_rural_table",
        misconception_tags=["inverts_urban_and_rural_challenges"],
    )


BUILDERS_01_25 = {
    "01_socio_economic_imbalances_definition": arch_01_socio_economic_imbalances_definition,
    "02_standard_of_living_indicators": arch_02_standard_of_living_indicators,
    "03_poverty_line_definition_and_benchmark": arch_03_poverty_line_definition_and_benchmark,
    "04_poverty_line_zar_conversion_calculation": arch_04_poverty_line_zar_conversion_calculation,
    "05_living_below_poverty_line_hardships": arch_05_living_below_poverty_line_hardships,
    "06_subsistence_farming_rural_vs_urban_land": arch_06_subsistence_farming_rural_vs_urban_land,
    "07_constitution_bill_of_rights_equality": arch_07_constitution_bill_of_rights_equality,
    "08_apartheid_structural_exclusion_causes": arch_08_apartheid_structural_exclusion_causes,
    "09_intergenerational_poverty_cycle_diagram": arch_09_intergenerational_poverty_cycle_diagram,
    "10_twelve_year_generation_education_lag": arch_10_twelve_year_generation_education_lag,
    "11_employment_equity_and_bbbee_reforms": arch_11_employment_equity_and_bbbee_reforms,
    "12_fiscal_policy_wealth_luxury_tax_redistribution": arch_12_fiscal_policy_wealth_luxury_tax_redistribution,
    "13_education_budget_allocation_calculation": arch_13_education_budget_allocation_calculation,
    "14_consequences_of_poor_quality_education": arch_14_consequences_of_poor_quality_education,
    "15_skills_shortage_definition_and_causes": arch_15_skills_shortage_definition_and_causes,
    "16_sa_key_skills_shortage_sectors_bar_chart": arch_16_sa_key_skills_shortage_sectors_bar_chart,
    "17_skills_shortages_hinder_economic_growth": arch_17_skills_shortages_hinder_economic_growth,
    "18_skills_development_act_1998_purpose": arch_18_skills_development_act_1998_purpose,
    "19_learnerships_work_based_training_mechanics": arch_19_learnerships_work_based_training_mechanics,
    "20_virtuous_cycle_of_skills_and_growth_diagram": arch_20_virtuous_cycle_of_skills_and_growth_diagram,
    "21_urbanization_and_rural_poverty_stats_bar_graph": arch_21_urbanization_and_rural_poverty_stats_bar_graph,
    "22_rural_tax_base_and_service_delivery_cost": arch_22_rural_tax_base_and_service_delivery_cost,
    "23_urban_challenges_informal_settlements_and_overcrowding": arch_23_urban_challenges_informal_settlements_and_overcrowding,
    "24_acid_mine_drainage_environmental_economic_impact": arch_24_acid_mine_drainage_environmental_economic_impact,
    "25_urban_vs_rural_classification_schedule_table": arch_25_urban_vs_rural_classification_schedule_table,
}
