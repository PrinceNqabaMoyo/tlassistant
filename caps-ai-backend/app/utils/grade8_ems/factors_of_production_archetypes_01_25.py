"""Grade 8 EMS — Factors of Production Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 4/03. Factors of production.md.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import AREAS, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario

TOPIC_NAME = "Factors of production"
TOPIC_KEY = "grade8_ems_factors_of_production"
LO = "g8_ems_factors_of_production"
TERM = 4
CAPS_WEIGHT_PERCENT = 20

_BANKS = ["FNB", "Absa", "Standard Bank", "Nedbank", "Capitec Business"]


def get_ems_scenario(rng: Optional[random.Random] = None) -> Dict[str, Any]:
    s = _raw_ems_scenario(rng)
    first = str(s["entrepreneur"]).split()[0]
    s["business"] = f"{first}'s {s['business_type'].title()}"
    return s


def fmt_r(amount: int | float) -> str:
    """Format an integer or float Rand amount using SA space thousands separator."""
    if isinstance(amount, float) and not amount.is_integer():
        whole = int(amount)
        cents = round((amount - whole) * 100)
        whole_str = f"{whole:,}".replace(",", " ")
        return f"R{whole_str},{cents:02d}"
    return f"R{int(round(amount)):,}".replace(",", " ")


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    misconception_tags: Optional[List[str]] = None,
    duration_mins: int = 4,
) -> Dict[str, Any]:
    out = dict(item)
    hints = out.get("hints") or {
        "tier_1": "Identify which of the 4 Factors (Natural Resources, Labour, Capital, Entrepreneurship) applies.",
        "tier_2": "Match factors to Rent, Salaries/Wages, Interest, and Profit; check SA labour law protections.",
        "tier_3": str(out.get("correct_answer") or out.get("sample_answer") or ""),
    }
    out["hints"] = hints
    out["hint_sections"] = out.get("hint_sections") or [
        hints.get("tier_1", ""),
        hints.get("tier_2", ""),
        hints.get("tier_3", ""),
    ]
    out.update({
        "topic": TOPIC_NAME,
        "topic_id": "grade8_ems",
        "subtopic_id": "term4_factors_of_production",
        "grade": 8,
        "subject": "Economic and Management Sciences",
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT_PERCENT,
        "suggested_duration_mins": out.get("suggested_duration_mins", duration_mins),
        "subskill": subskill,
        "archetype": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": subskill,
        "concept_group": "factors_of_production",
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 4 > Factors of Production",
        "misconception_tags": misconception_tags or ["factor_classification_error"],
        "diagnostic_tags": ["factors_of_production", "labour_law", "grade8_ems"],
    })
    return out


def _make_mcq(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    options: List[str],
    correct_ans: str,
    explanation: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    shuffled = list(options)
    rng.shuffle(shuffled)
    c_idx = shuffled.index(correct_ans)
    letter = chr(65 + c_idx)
    full_ans = f"{letter}. {correct_ans}"
    worked = f"**{full_ans}** [{marks} marks]\n\n**Explanation:**\n- {explanation}"
    payload: Dict[str, Any] = {
        "id": f"g8_ems_fp_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "options": shuffled,
        "correct_index": str(c_idx),
        "correct_answer": full_ans,
        "expected_answer": full_ans,
        "sample_answer": full_ans,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct_ans}", "marks": marks, "editable": True}
            ],
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=3,
    )


def _make_typed(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    correct_ans: str,
    steps: List[str],
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    marks: int = 3,
    acceptable_answers: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    steps_md = "\n".join(f"- {s}" for s in steps)
    worked = f"**Answer:** {correct_ans} [{marks} marks]\n\n**Step-by-Step Working:**\n{steps_md}"
    payload: Dict[str, Any] = {
        "id": f"g8_ems_fp_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "typed",
        "modality": "math",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "expected_answer": correct_ans,
        "acceptable_answers": acceptable_answers or [correct_ans],
        "sample_answer": correct_ans,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{idx + 1}", "desc": st, "marks": 1, "editable": True}
                for idx, st in enumerate(steps[:marks])
            ],
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=4,
    )


def _make_rubric(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    sample_answer: str,
    marking_points: List[str],
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    marks: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    pts_md = "\n".join(f"- {p} [1 mark]" for p in marking_points)
    worked = f"**Model Answer** [{marks} marks]\n\n{sample_answer}\n\n**Marking Breakdown:**\n{pts_md}"
    payload: Dict[str, Any] = {
        "id": f"g8_ems_fp_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "short_answer",
        "modality": "semantic",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": sample_answer,
        "expected_answer": sample_answer,
        "sample_answer": sample_answer,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "marking_points": marking_points,
        "guidelines": marking_points,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{idx + 1}", "desc": p, "marks": 1, "editable": True}
                for idx, p in enumerate(marking_points)
            ],
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=5,
    )


def _make_table(
    rng: random.Random,
    *,
    subskill: str,
    title: str,
    prompt: str,
    journal_type: str,
    headers: List[str],
    table_rows: List[List[Tuple[str, str, bool]]],
    cell_hints: Dict[str, str],
    hints: Dict[str, str],
    misconception_tags: List[str],
    question_family_id: str,
    worked_notes: str = "",
) -> Dict[str, Any]:
    ui_rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    md_rows: List[List[str]] = []

    for r_idx, row in enumerate(table_rows):
        ui_row: List[Dict[str, Any]] = []
        md_row: List[str] = []
        for c_idx, (val, ctype, editable) in enumerate(row):
            coord = f"t0_r{r_idx}_c{c_idx}"
            ui_row.append({
                "coordinate": coord,
                "value": val if not editable else "",
                "type": ctype,
                "editable": editable,
                "prefilled": not editable,
            })
            if editable:
                correct_map[coord] = val
            md_row.append(f"**{val}**" if editable and val else (val or "-"))
        ui_rows.append(ui_row)
        md_rows.append(md_row)

    header_line = "| " + " | ".join(headers) + " |"
    sep_line = "| " + " | ".join("---" for _ in headers) + " |"
    body_lines = ["| " + " | ".join(r) + " |" for r in md_rows]
    md_table = "\n".join([header_line, sep_line] + body_lines)

    marks = max(2, len(correct_map))
    worked = f"**Completed Table** [{marks} marks]\n\n{md_table}"
    if worked_notes:
        worked += f"\n\n**Notes:**\n{worked_notes}"

    payload: Dict[str, Any] = {
        "id": f"g8_ems_fp_{subskill}_{rng.randint(100000, 999999)}",
        "title": title,
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "headers": headers,
        "rows": ui_rows,
        "journal": {
            "journal_type": journal_type,
            "headers": headers,
            "rows": ui_rows,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{k}", "desc": f"Cell {k}: {v}", "marks": 1, "editable": True}
                for k, v in list(correct_map.items())[:marks]
            ],
        },
        "sample_answer": worked,
        "ideal_answer": worked,
        "expected_answer": worked,
        "worked_solution": worked,
        "canonical_solution": worked,
        "explanation": worked,
        "hints": hints,
    }
    return _with_metadata(
        payload,
        subskill=subskill,
        learning_objective_id=f"{LO}_{subskill}",
        question_family_id=question_family_id,
        misconception_tags=misconception_tags,
        duration_mins=6,
    )


def svg_factor_card(title: str, subtitle: str, rows: List[Tuple[str, str]]) -> str:
    """Render Paper & Ink Factor of Production summary card SVG."""
    row_h = 24
    h = 78 + len(rows) * row_h
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 {h}" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">',
        f'<rect x="4" y="4" width="532" height="{h - 8}" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>',
        '<rect x="4" y="4" width="532" height="44" rx="8" fill="#92400E"/>',
        '<rect x="4" y="34" width="532" height="14" fill="#92400E"/>',
        f'<text x="20" y="24" font-size="13" font-weight="bold" fill="#FFFFFF">{_xml_escape(title)}</text>',
        f'<text x="20" y="40" font-size="10" fill="#FEF3C7">{_xml_escape(subtitle)}</text>',
    ]
    for i, (lbl, val) in enumerate(rows):
        y = 70 + i * row_h
        bg = "#FFFBEB" if i % 2 == 0 else "#FFFFFF"
        lines.append(f'<rect x="14" y="{y - 15}" width="512" height="22" fill="{bg}" rx="3"/>')
        lines.append(f'<text x="22" y="{y}" font-size="12" fill="#1E293B">{_xml_escape(lbl)}</text>')
        lines.append(f'<text x="516" y="{y}" font-size="12" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(val)}</text>')
    lines.append("</svg>")
    return "".join(lines)


# =============================================================================
# ARCHETYPES 01 – 25
# =============================================================================

def _b01_inputs_vs_outputs_production(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    units = rng.randint(150, 400)
    prompt = (
        f"At {s['business']} in {s['area']}, wheat flour, clean water, electric ovens, and skilled bakers are combined to bake {units} fresh loaves of bread daily. "
        f"In the production process, how are the flour, ovens, and bakers classified compared to the {units} baked loaves?"
    )
    ans = f"Flour, ovens, and bakers are INPUTS (factors/resources used); the {units} loaves are OUTPUTS (finished consumer products)"
    opts = [
        f"Flour, ovens, and bakers are INPUTS (factors/resources used); the {units} loaves are OUTPUTS (finished consumer products)",
        f"The {units} loaves are INPUTS; the ovens and bakers are OUTPUTS",
        "Only electric ovens count as outputs because machinery lasts several years",
        "Neither flour nor bakers enter production because bread is a service",
    ]
    exp = f"Production transforms Inputs (resources/factors like flour, ovens, and labour) into valuable Outputs ({units} loaves of bread)."
    return _make_mcq(
        rng,
        subskill="01_inputs_vs_outputs_production",
        title="Inputs vs Outputs in Production",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask: What goes INTO the baking process vs what comes OUT ready for sale?",
            "tier_2": "Inputs = resources/factors put in; Outputs = finished goods/services produced.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_production_inputs_and_outputs"],
        question_family_id="inputs_vs_outputs",
    )


def _b02_four_factors_identification(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(40, 120) * 1000
    prompt = (
        f"{s['entrepreneur']} invests {fmt_r(amt)} to launch a furniture workshop in {s['area']}, using indigenous timber, hiring two carpenters, buying wood saws, and taking business risk. "
        f"Which group lists the FOUR Factors of Production represented here?"
    )
    ans = "Natural resources (timber), Labour (carpenters), Capital (R-investment & saws), Entrepreneurship (owner taking risk)"
    opts = [
        "Natural resources (timber), Labour (carpenters), Capital (R-investment & saws), Entrepreneurship (owner taking risk)",
        "Wholesale, Retail, Flea markets, and Bank statements",
        "Stationery, Telephone, Drawings, and Bank charges",
        "CRJ, CPJ, General Ledger, and Trial Balance",
    ]
    exp = f"The 4 Factors of Production are Natural resources (timber), Labour (carpenters), Capital ({fmt_r(amt)} & saws), and Entrepreneurship ({s['entrepreneur']})."
    return _make_mcq(
        rng,
        subskill="02_four_factors_identification",
        title="Identifying All Four Factors of Production",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Match each concrete example (timber, carpenters, saws/money, owner risk) to a factor name.",
            "tier_2": "The 4 factors are Natural Resources/Land, Labour, Capital, and Entrepreneurship.",
            "tier_3": ans,
        },
        misconception_tags=["lists_accounting_books_as_factors_of_production"],
        question_family_id="four_factors_id",
    )


def _b03_factor_remuneration_matching(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 18) * 1000
    cases = [
        ("Natural Resources (Land)", "Rent", f"mining land or shop site yielding {fmt_r(amt)}/month"),
        ("Labour", "Salaries and Wages", f"workers contributing effort earning {fmt_r(amt)}/month"),
        ("Capital", "Interest", f"lent machinery/bank funds earning {fmt_r(amt)}/year"),
        ("Entrepreneurship", "Profit", f"business owner taking calculated risk and earning {fmt_r(amt)} net gain"),
    ]
    factor, remun, desc = rng.choice(cases)
    prompt = (
        f"At {s['business']} in {s['area']}, {factor} is supplied ({desc}). "
        f"What is the exact economic term for the remuneration (reward) earned by {factor}?"
    )
    opts = ["Rent", "Salaries and Wages", "Interest", "Profit"]
    exp = f"In economics, {factor} always receives {remun} as its factor remuneration."
    return _make_mcq(
        rng,
        subskill="03_factor_remuneration_matching",
        title="Factor Remuneration Pairing",
        prompt=prompt,
        options=opts,
        correct_ans=remun,
        explanation=exp,
        hints={
            "tier_1": "Remember the 4 classic factor rewards: Rent, Salaries/Wages, Interest, Profit.",
            "tier_2": "Natural Resources->Rent | Labour->Salaries/Wages | Capital->Interest | Entrepreneurship->Profit.",
            "tier_3": f"Remuneration for {factor}: {remun}.",
        },
        misconception_tags=["confuses_factor_remuneration_names"],
        question_family_id="factor_remun_mcq",
    )


def _b04_factors_and_remuneration_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rent_v = rng.randint(4, 12) * 1000
    wage_v = rng.randint(6, 15) * 1000
    int_v = rng.randint(15, 35) * 100
    prof_v = rng.randint(10, 28) * 1000
    pool = [
        (f"Monthly farm / shop premises lease ({fmt_r(rent_v)})", "Natural Resources / Land", "Rent"),
        (f"Bi-weekly factory operator payroll ({fmt_r(wage_v)})", "Labour", "Salaries / Wages"),
        (f"Bank finance charge on machinery loan ({fmt_r(int_v)})", "Capital", "Interest"),
        (f"Owner's net gain after all expenses ({fmt_r(prof_v)})", "Entrepreneurship", "Profit"),
    ]
    rng.shuffle(pool)
    headers = ["Business Payment / Return", "Factor of Production", "Economic Remuneration"]
    table_rows = [[(item, "given", False), (f, "required", True), (r, "required", True)] for item, f, r in pool]
    cell_hints = {}
    for idx, (item, f, r) in enumerate(pool):
        cell_hints[f"t0_r{idx}_c1"] = f"Identify which of the 4 factors this refers to."
        cell_hints[f"t0_r{idx}_c2"] = f"State Rent, Salaries / Wages, Interest, or Profit."
    prompt = f"Classify each factor return at {s['business']} in {s['area']} into its Factor of Production and Economic Remuneration."
    return _make_table(
        rng,
        subskill="04_factors_and_remuneration_table",
        title="Factors & Remuneration Matrix Table",
        prompt=prompt,
        journal_type="factors_remuneration_matrix",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Match premises -> Land, payroll -> Labour, loan cost -> Capital, owner net gain -> Entrepreneurship.",
            "tier_2": "Land->Rent | Labour->Salaries / Wages | Capital->Interest | Entrepreneurship->Profit.",
            "tier_3": " | ".join(f"{f}: {r}" for _, f, r in pool),
        },
        misconception_tags=["mixes_up_factor_and_remuneration_columns"],
        question_family_id="factors_remun_table",
    )


def _b05_natural_resources_land_definition(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    res_example = rng.choice(["clean river water and sunlight for solar panels", "coastal fish stocks and fertile soil", "coal deposits and timber forests"])
    prompt = (
        f"In {s['area']}, {s['business']} depends on {res_example}. "
        f"In economics, why are all gifts of nature (minerals, oceans, air, sunlight, water, soil) grouped under the factor called **Natural Resources (Land)**?"
    )
    ans = "Because they come directly from the natural environment without being created by human manufacturing"
    opts = [
        "Because they come directly from the natural environment without being created by human manufacturing",
        "Because commercial banks manufacture mineral seams and sunlight",
        "Because every natural resource is unlimited and never runs out",
        "Because only flat farmland counts as Land in South Africa",
    ]
    exp = f"Natural Resources (Land) encompasses all unprocessed natural gifts ({res_example}) extracted from soil, water, air, and earth."
    return _make_mcq(
        rng,
        subskill="05_natural_resources_land_definition",
        title="Scope of Natural Resources (Land)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice 'Land' in economics includes air, oceans, minerals, forests, and solar energy — not just soil!",
            "tier_2": "Any raw gift provided by nature (not man-made) is Natural Resources (Land).",
            "tier_3": ans,
        },
        misconception_tags=["limits_land_only_to_agricultural_soil"],
        question_family_id="land_definition",
    )


def _b06_renewable_vs_non_renewable_resources(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    ask_non = rng.choice([True, False])
    if ask_non:
        prompt = (
            f"A mining supplier serving {s['area']} extracts coal, iron ore, and crude oil. "
            f"Why are these natural resources classified as **non-renewable**?"
        )
        ans = "They exist in fixed finite quantities on Earth and cannot be replaced within a human lifetime once depleted"
        exp = "Fossil fuels and minerals (coal, iron ore, crude oil, gold) take millions of years to form and are non-renewable once mined."
    else:
        prompt = (
            f"A sustainable farm near {s['area']} uses solar energy, wind turbines, and replanted pine plantations. "
            f"Why are these classified as **renewable** natural resources?"
        )
        ans = "They replenish naturally or can be regrown sustainably over time if responsibly managed"
        exp = "Solar energy, wind, water cycles, and properly replanted timber can regenerate and remain renewable when protected from overuse."
    opts = [
        "They exist in fixed finite quantities on Earth and cannot be replaced within a human lifetime once depleted",
        "They replenish naturally or can be regrown sustainably over time if responsibly managed",
        "They are human-made capital goods manufactured in factories",
        "They require zero care because pollution can never harm forests or fish",
    ]
    return _make_mcq(
        rng,
        subskill="06_renewable_vs_non_renewable_resources",
        title="Renewable vs Non-Renewable Natural Resources",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Compare finite minerals mined out of rock vs solar/wind/replanted trees.",
            "tier_2": "Finite/irreplaceable = Non-renewable; naturally replenishable = Renewable.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_coal_and_gold_are_renewable"],
        question_family_id="renewable_vs_non_renewable",
    )


def _b07_sustainability_and_pollution_risk(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    waste_litres = rng.randint(5, 20) * 100
    prompt = (
        f"A textile dye factory near {s['area']} dumps {waste_litres} litres of untreated chemical waste into a local river weekly to cut costs, while over-harvesting local wood. "
        f"Explain THREE economic and social consequences of failing to manage Natural Resources sustainably."
    )
    sample = (
        f"1. Long-term resource depletion: Over-harvesting without replanting destroys future raw materials needed for jobs and production.\n"
        f"2. Water & ecosystem damage: Dumping {waste_litres} L/week pollutes clean water, harming downstream farms, fishing livelihoods, and community health.\n"
        "3. Regulatory fines & shutdowns: Environmental non-compliance exposes the business to heavy government penalties, clean-up costs, and lost customers."
    )
    pts = [
        "Depletes future raw materials needed for ongoing production and employment.",
        f"Pollutes clean water/soil ({waste_litres} L waste), damaging health and nearby communities/farms.",
        "Triggers legal fines, clean-up liabilities, or loss of market reputation.",
    ]
    return _make_rubric(
        rng,
        subskill="07_sustainability_and_pollution_risk",
        title="Sustainable Use of Natural Resources",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about future raw materials, community health/water, and environmental fines.",
            "tier_2": "Discuss resource exhaustion, pollution harm to downstream users, and legal/reputational costs.",
            "tier_3": sample,
        },
        misconception_tags=["ignores_long_term_economic_cost_of_pollution"],
        question_family_id="sustainability_rubric",
        marks=3,
    )


def _b08_natural_resource_depletion_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    annual = rng.choice([2000, 2500, 4000, 5000])
    years = rng.randint(8, 20)
    reserve = annual * years
    ans = f"{years} years"
    svg = svg_factor_card(
        f"Non-Renewable Mineral Reserve — {s['area']}",
        f"Supplied to {s['business']}",
        [
            ("Total Confirmed Coal/Aggregate Reserve", f"{reserve:,} tonnes".replace(",", " ")),
            ("Annual Extraction Rate", f"{annual:,} tonnes/year".replace(",", " ")),
            ("Estimated Years Until Depletion", "??? years"),
        ],
    )
    prompt = (
        f"Inspect the Non-Renewable Reserve summary near {s['area']}. "
        f"At an extraction rate of {annual:,} tonnes per year, calculate how many years the {reserve:,} tonnes of finite reserves will last (`??? years`).".replace(",", " ")
    )
    steps = [
        f"Total Reserve = {reserve:,} tonnes; Annual extraction = {annual:,} tonnes/year.".replace(",", " "),
        f"Years remaining = {reserve:,} / {annual:,} = {years} years.".replace(",", " "),
    ]
    return _make_typed(
        rng,
        subskill="08_natural_resource_depletion_calc",
        title="Non-Renewable Resource Depletion Horizon",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, str(years)],
        steps=steps,
        hints={
            "tier_1": "Divide total finite reserves by the yearly rate of extraction.",
            "tier_2": f"{reserve} / {annual}.",
            "tier_3": f"{years} years.",
        },
        misconception_tags=["multiplies_reserves_by_extraction_rate"],
        question_family_id="resource_depletion_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b09_labour_definition_human_effort(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    hrs = rng.randint(35, 45)
    prompt = (
        f"Every week at {s['business']}, delivery drivers haul stock while the software clerk maintains digital sales spreadsheets for {hrs} hours. "
        f"Which economic statement best defines **Labour**?"
    )
    ans = "All physical AND mental human effort applied in producing goods and services in exchange for salaries or wages"
    opts = [
        "All physical AND mental human effort applied in producing goods and services in exchange for salaries or wages",
        "Strictly heavy outdoor lifting, excluding computer or office thinking work",
        "Bank loans and machinery bought to replace employees",
        "Unpaid weekend hobbies done purely for personal entertainment",
    ]
    exp = f"Labour includes BOTH physical work (drivers) and mental effort (accounting/computing over {hrs} hrs) rewarded with Salaries or Wages."
    return _make_mcq(
        rng,
        subskill="09_labour_definition_human_effort",
        title="Definition of Labour (Physical & Mental)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Does office computing/problem-solving count as Labour alongside physical factory work?",
            "tier_2": "Labour covers ALL physical and mental human productive work paid via salaries/wages.",
            "tier_3": ans,
        },
        misconception_tags=["limits_labour_only_to_manual_physical_work"],
        question_family_id="labour_definition",
    )


def _b10_unskilled_labour_characteristics(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    workers = rng.randint(4, 12)
    prompt = (
        f"{s['business']} hires {workers} seasonal workers to sweep yards and pack fruit crates — tasks learned in under one hour without formal qualifications. "
        f"What skill category is this, and why are wages usually lower?"
    )
    ans = "Unskilled labour — no specialised training required, high supply of applicants, generally paid weekly/hourly wages"
    opts = [
        "Unskilled labour — no specialised training required, high supply of applicants, generally paid weekly/hourly wages",
        "Skilled professional labour — requires a 4-year university degree",
        "Semi-skilled labour — requires national trade board certification",
        "Entrepreneurship — employees assume full company bankruptcy risk",
    ]
    exp = f"Routine jobs needing minimal training ({workers} packers) represent Unskilled Labour, where high worker availability keeps wage rates lower."
    return _make_mcq(
        rng,
        subskill="10_unskilled_labour_characteristics",
        title="Unskilled Labour Characteristics",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice the tasks take under an hour to learn with zero prior certification.",
            "tier_2": "Minimal training + abundant supply + hourly/weekly wages = Unskilled labour.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_unskilled_and_semi_skilled_labour"],
        question_family_id="unskilled_labour",
    )


def _b11_semi_skilled_labour_characteristics(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    role = rng.choice([
        "certified forklift driver operating warehouse lifts after a 3-week course",
        "industrial sewing-machine operator trained in factory safety & stitching",
        "point-of-sale cashier trained in till reconciliation and card speedpoints",
    ])
    prompt = (
        f"A worker at {s['business']} in {s['area']} works as a {role}. How is this employee classified on the skills spectrum?"
    )
    ans = "Semi-skilled labour (requires short practical training or basic certificate, not a multi-year tertiary qualification)"
    opts = [
        "Semi-skilled labour (requires short practical training or basic certificate, not a multi-year tertiary qualification)",
        "Unskilled labour (zero instruction needed)",
        "Skilled professional labour (requires a 4-year university engineering degree)",
        "Physical Capital Good (classified as factory equipment)",
    ]
    exp = f"Operating specialist machines or point-of-sale tills after short focused training sits between unskilled manual jobs and university-qualified professions -> Semi-skilled labour."
    return _make_mcq(
        rng,
        subskill="11_semi_skilled_labour_characteristics",
        title="Semi-Skilled Labour Characteristics",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "It needs some specific course/on-the-job machine training, though not a university degree.",
            "tier_2": "Machine operators, drivers, and trained cashiers = Semi-skilled labour.",
            "tier_3": ans,
        },
        misconception_tags=["classifies_machine_operators_as_capital_goods_or_unskilled"],
        question_family_id="semi_skilled_labour",
    )


def _b12_skilled_labour_characteristics(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    role = rng.choice([
        ("qualified Red Seal artisan electrician", "apprenticeship and trade test"),
        ("registered nurse", "university/college nursing degree and clinical board licensing"),
        ("chartered accountant", "university degree, articles, and board exams"),
    ])
    prompt = (
        f"A {role[0]} serving {s['area']} completed an extensive {role[1]} before practising independently. "
        f"Identify the labour classification and typical payment mode."
    )
    ans = "Skilled labour — requires accredited tertiary/artisan training and typically earns higher monthly Salaries"
    opts = [
        "Skilled labour — requires accredited tertiary/artisan training and typically earns higher monthly Salaries",
        "Unskilled labour — performs routine errands for daily cash tips",
        "Semi-skilled labour — needs only 2 hours of induction",
        "Natural Resources — extracted directly from mineral rock",
    ]
    exp = f"A {role[0]} holds scarce, formally accredited expertise ({role[1]}), representing Skilled Labour rewarded with higher monthly Salaries."
    return _make_mcq(
        rng,
        subskill="12_skilled_labour_characteristics",
        title="Skilled Labour Characteristics",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for accredited multi-year artisan or professional degrees.",
            "tier_2": "High qualification + scarce supply + monthly salary = Skilled labour.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_artisan_skilled_trades_with_unskilled"],
        question_family_id="skilled_labour",
    )


def _b13_classify_labour_skill_levels_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("Fruit picker / Yard cleaner", "Unskilled", "No formal qualification needed"),
        ("Forklift operator / Till cashier", "Semi-skilled", "Short practical / machine training"),
        ("Civil engineer / Qualified plumber", "Skilled", "Degree / Accredited trade apprenticeship"),
    ]
    rng.shuffle(pool)
    headers = ["Job Role", "Skill Level", "Typical Training Requirement"]
    table_rows = [[(j, "given", False), (lvl, "required", True), (tr, "required", True)] for j, lvl, tr in pool]
    cell_hints = {}
    for idx, (j, _, _) in enumerate(pool):
        cell_hints[f"t0_r{idx}_c1"] = "Write Unskilled, Semi-skilled, or Skilled."
        cell_hints[f"t0_r{idx}_c2"] = "Summarise formal/practical training duration needed."
    prompt = f"Classify these workers in {s['area']} by Skill Level (`Unskilled`, `Semi-skilled`, `Skilled`) and Training Requirement."
    return _make_table(
        rng,
        subskill="13_classify_labour_skill_levels_table",
        title="Labour Skill Levels Classification Table",
        prompt=prompt,
        journal_type="labour_skills_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Sort from no formal training -> short machine/course training -> full degree/artisan qualification.",
            "tier_2": "Cleaner = Unskilled; Forklift = Semi-skilled; Engineer/Plumber = Skilled.",
            "tier_3": " | ".join(f"{j}: {l}" for j, l, _ in pool),
        },
        misconception_tags=["mislabels_skill_levels_in_table"],
        question_family_id="labour_skills_table",
    )


def _b14_human_capital_experience_growth(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    yr1 = rng.randint(12, 22)
    yr5 = yr1 + rng.randint(14, 24)
    svg = svg_factor_card(
        f"Human Capital Growth — {s['business']}",
        f"Area: {s['area']}",
        [
            ("New Trainee Output (Year 1)", f"{yr1} orders/week"),
            ("Mentored & Trained Staff Output (Year 5)", f"{yr5} orders/week"),
            ("Productivity Improvement", f"+{yr5 - yr1} orders/week"),
        ],
    )
    prompt = (
        f"Examine the Human Capital Growth summary for {s['business']}. "
        f"Why does output rise from {yr1} to {yr5} orders/week as workers gain experience and workplace training?"
    )
    ans = "Education, skills training, and workplace experience build Human Capital, making workers faster, more accurate, and more productive"
    opts = [
        "Education, skills training, and workplace experience build Human Capital, making workers faster, more accurate, and more productive",
        "Workers automatically turn into non-renewable Natural Resources after 5 years",
        "Long-serving staff require zero Wages under South African law",
        "Borrowed Capital always pays for itself without human effort",
    ]
    exp = f"Investing in training and retaining experienced staff builds **Human Capital**, boosting weekly output from {yr1} to {yr5} orders/week."
    return _make_mcq(
        rng,
        subskill="14_human_capital_experience_growth",
        title="Human Capital & Experience Productivity",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think of the skills, knowledge, and experience embodied inside workers (Human Capital).",
            "tier_2": "Training + experience raise efficiency and quality -> stronger Human Capital.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_human_capital_with_physical_machinery"],
        question_family_id="human_capital_growth",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b15_training_pathways_tvet_learnership(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    youth = rng.choice(NAMES)
    pathway = rng.choice([
        ("Apprenticeship / Trade Test", "combines paid workshop practice under a master artisan with theory classes to qualify in plumbing, welding, or electrical trades"),
        ("SETA Learnership", "provides a structured work-based learning programme combining classroom theory with practical workplace experience leading to an NQF qualification"),
        ("TVET College", "offers vocational technical certificates bridging school directly into industry trades"),
    ])
    prompt = (
        f"{youth}, a school-leaver in {s['area']}, wants practical workplace skills while earning a stipend rather than pure academic theory. "
        f"Which South African training pathway best matches: '{pathway[1]}'?"
    )
    ans = pathway[0]
    opts = [
        "Apprenticeship / Trade Test",
        "SETA Learnership",
        "TVET College",
        "Money Market Overdraft",
    ]
    exp = f"In South Africa, a {pathway[0]} develops practical employability because it {pathway[1]}."
    return _make_mcq(
        rng,
        subskill="15_training_pathways_tvet_learnership",
        title="SA Skills Training Pathways",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Distinguish artisan Trade Tests, SETA Learnerships, and vocational TVET colleges.",
            "tier_2": f"Match the exact description to {pathway[0]}.",
            "tier_3": ans,
        },
        misconception_tags=["unaware_of_vocational_learnership_pathways"],
        question_family_id="sa_training_pathways",
    )


def _b16_worker_value_creativity_innovation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    save_pct = rng.randint(12, 28)
    prompt = (
        f"A workshop assistant at {s['business']} in {s['area']} designs a simpler packaging layout that cuts cardboard waste by {save_pct}% and speeds up dispatch. "
        f"Explain TWO reasons why valuing workers' ideas and creativity increases business competitiveness beyond just counting hours worked."
    )
    sample = (
        f"1. Cost efficiency & innovation: Frontline employees spot daily workflow bottlenecks and invent improvements (like {save_pct}% waste reduction) managers might miss.\n"
        "2. Higher morale & customer goodwill: Respected, motivated workers serve clients warmly and stay loyal to the enterprise, cutting costly staff turnover."
    )
    pts = [
        f"Frontline employee ideas uncover cost savings ({save_pct}% waste cut) and process innovation.",
        "Valuing employees improves motivation, customer service quality, and staff retention.",
    ]
    return _make_rubric(
        rng,
        subskill="16_worker_value_creativity_innovation",
        title="Employee Creativity & Workplace Value",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Consider cost-saving ideas from frontline workers AND employee morale/loyalty.",
            "tier_2": "Address operational innovation (waste cut) and staff motivation/retention.",
            "tier_3": sample,
        },
        misconception_tags=["views_labour_purely_as_mechanical_clocking_hours"],
        question_family_id="worker_creativity_rubric",
        marks=2,
    )


def _b17_sa_critical_skills_shortages(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    vacancies = rng.randint(3, 12)
    prompt = (
        f"South African employers near {s['area']} struggle to fill {vacancies} senior technical roles for months. "
        f"Which group represents **critical scarce skills** highlighted in South Africa's economy?"
    )
    ans = "Mathematics, Physical Sciences, Engineering, ICT/Software, Certified Artisan Trades, and Project Management"
    opts = [
        "Mathematics, Physical Sciences, Engineering, ICT/Software, Certified Artisan Trades, and Project Management",
        "Basic manual leaflet distribution with zero technical training",
        "Daily till cash counting without computer skills",
        "Unregistered informal kerbside parking attendants",
    ]
    exp = f"SA's scarce-skill bottlenecks (leaving {vacancies} roles unfilled) centre on STEM (Maths, Science, Engineering), ICT, certified artisans, and project management."
    return _make_mcq(
        rng,
        subskill="17_sa_critical_skills_shortages",
        title="South African Critical Skills Shortages",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for technical, STEM, ICT, artisan, and management fields in short supply.",
            "tier_2": "SA experiences critical shortages in Engineering, Maths, Science, ICT, Artisans, and Project Management.",
            "tier_3": ans,
        },
        misconception_tags=["misses_sa_scarce_skills_priorities"],
        question_family_id="sa_scarce_skills",
    )


def _b18_labour_productivity_output_per_worker(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    workers = rng.choice([5, 6, 8, 10])
    old_per = rng.randint(15, 25)
    new_per = old_per + rng.randint(4, 10)
    total_after = workers * new_per
    ans = f"{new_per} units per worker"
    prompt = (
        f"Before skills training, {workers} workers at {s['business']} produced {workers * old_per} units per day ({old_per} units/worker). "
        f"After completing a practical workshop course, the same {workers} workers produce {total_after} units per day. "
        f"Calculate the NEW labour productivity (output per worker per day)."
    )
    steps = [
        f"Productivity = Total Output / Number of Workers.",
        f"New productivity = {total_after} units / {workers} workers = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="18_labour_productivity_output_per_worker",
        title="Calculate Labour Productivity After Training",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, str(new_per), f"{new_per} units"],
        steps=steps,
        hints={
            "tier_1": "Divide the NEW total daily output by the number of workers.",
            "tier_2": f"{total_after} / {workers}.",
            "tier_3": f"New labour productivity = {ans}.",
        },
        misconception_tags=["computes_productivity_gain_instead_of_new_rate"],
        question_family_id="labour_productivity_calc",
    )


def _b19_labour_shortage_business_impact_rubric(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    delay_wks = rng.randint(3, 8)
    prompt = (
        f"Due to a shortage of qualified diesel mechanics in {s['area']}, {s['business']} waits {delay_wks} weeks whenever delivery vehicles break down. "
        f"Explain THREE negative impacts that skilled labour shortages have on local businesses and the broader SA economy."
    )
    sample = (
        f"1. Lost sales & delays: Vehicles standing idle for {delay_wks} weeks stop {s['business']} from delivering orders on time.\n"
        "2. Inflated salary/repair costs: Scarce technicians charge premium rates, pushing up operating expenses and consumer prices.\n"
        "3. Slower expansion & unemployment: Firms cannot open new shifts or hire junior support workers when key technical supervisors are missing."
    )
    pts = [
        f"Production/delivery delays ({delay_wks}-week bottlenecks) causing lost revenue.",
        "Higher scarcity wages/fees driving up operating costs.",
        "Limits expansion and job creation for semi-skilled/unskilled support staff.",
    ]
    return _make_rubric(
        rng,
        subskill="19_labour_shortage_business_impact_rubric",
        title="Impact of Skills Shortages on Business",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about stalled operations, higher wages/repair bills, and lost expansion jobs.",
            "tier_2": "Cover production delays, higher labour costs, and fewer support jobs created.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_skills_shortages_only_affect_big_corporations"],
        question_family_id="skills_shortage_impact",
        marks=3,
    )


def _b20_capital_financial_vs_physical_goods(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(30, 95) * 1000
    ask_phys = rng.choice([True, False])
    if ask_phys:
        prompt = (
            f"{s['business']} buys industrial baking ovens, sewing machines, and computer workstations worth {fmt_r(amt)}. "
            f"Why are these man-made tools called **Physical (Real) Capital Goods** rather than consumer goods?"
        )
        ans = "Because they are man-made assets used repeatedly to produce OTHER goods and services rather than being consumed directly by households"
        exp = f"Ovens, sewing machines, and workstations ({fmt_r(amt)}) are man-made goods used to produce further outputs -> Physical/Real Capital Goods."
    else:
        prompt = (
            f"{s['entrepreneur']} raises {fmt_r(amt)} cash in the business bank account to fund raw materials, rent, and machinery purchases. "
            f"What form of capital does this {fmt_r(amt)} cash fund represent?"
        )
        ans = "Financial Capital (money available to invest and pay for physical capital goods and operations)"
        exp = f"Cash funds ({fmt_r(amt)}) ready to be invested in machinery and working inventory represent Financial Capital."
    opts = [
        "Because they are man-made assets used repeatedly to produce OTHER goods and services rather than being consumed directly by households",
        "Financial Capital (money available to invest and pay for physical capital goods and operations)",
        "Non-renewable Natural Resources dug out of deep mines",
        "Weekly hourly wages paid to cleaners",
    ]
    return _make_mcq(
        rng,
        subskill="20_capital_financial_vs_physical_goods",
        title="Financial Capital vs Physical Capital Goods",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Money used to invest = Financial Capital; Man-made machines/tools used to produce = Physical Capital Goods.",
            "tier_2": "Distinguish cash funding from productive equipment.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_financial_capital_with_physical_machinery"],
        question_family_id="financial_vs_physical_capital",
    )


def _b21_consumer_good_vs_capital_good(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(8, 22) * 1000
    prompt = (
        f"Both Sipho's household and {s['business']} buy the exact same {fmt_r(amt)} commercial laptop in {s['area']}. "
        f"Sipho's family uses theirs to stream weekend movies, while {s['business']} uses theirs to run invoicing and graphic design for clients. "
        f"Classify each laptop correctly:"
    )
    ans = "Family laptop = Consumer Good; Business laptop = Capital Good"
    opts = [
        "Family laptop = Consumer Good; Business laptop = Capital Good",
        "Both laptops are Capital Goods because both cost over R5 000",
        "Both laptops are Consumer Goods because laptops are electronics",
        "Family laptop = Natural Resource; Business laptop = Financial Capital",
    ]
    exp = f"Whether an item ({fmt_r(amt)} laptop) is a Capital Good or Consumer Good depends on its USE: household leisure = Consumer Good; business production of services = Capital Good."
    return _make_mcq(
        rng,
        subskill="21_consumer_good_vs_capital_good",
        title="Consumer Good vs Capital Good by Use",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice classification depends on PURPOSE of use, not what the object looks like.",
            "tier_2": "Personal household enjoyment = Consumer Good; producing business goods/services = Capital Good.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_goods_classification_is_fixed_regardless_of_use"],
        question_family_id="consumer_vs_capital_use",
    )


def _b22_own_vs_borrowed_capital_comparison(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    amt = rng.randint(25, 75) * 1000
    prompt = (
        f"{s['entrepreneur']} considers expanding {s['business']} by borrowing {fmt_r(amt)} from {bank} instead of waiting two years to save Own Capital. "
        f"What is the key disadvantage of Borrowed Capital compared to Own Capital?"
    )
    ans = f"Borrowed capital must be repaid on fixed dates WITH interest to {bank}, creating fixed cash-flow pressure"
    opts = [
        f"Borrowed capital must be repaid on fixed dates WITH interest to {bank}, creating fixed cash-flow pressure",
        f"Borrowed capital gives customers ownership shares in {s['business']}",
        f"Own capital carries higher monthly interest charges paid to {bank}",
        "Borrowed capital cannot be used to buy Physical Capital Goods",
    ]
    exp = f"Own capital carries no interest or repayment deadline, whereas Borrowed capital ({fmt_r(amt)} from {bank}) adds mandatory interest expense and repayment risk."
    return _make_mcq(
        rng,
        subskill="22_own_vs_borrowed_capital_comparison",
        title="Own Capital vs Borrowed Capital Trade-offs",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask: Which option creates mandatory debt and interest obligations?",
            "tier_2": "Borrowed capital = fixed repayment + interest cost; Own capital = debt-free.",
            "tier_3": ans,
        },
        misconception_tags=["ignores_repayment_and_interest_burden_of_borrowed_capital"],
        question_family_id="own_vs_borrowed_capital",
    )


def _b23_borrowed_capital_interest_cost_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    loan = rng.choice([20000, 30000, 40000, 50000])
    rate = rng.choice([10, 12, 15])
    years = rng.choice([2, 3])
    interest = int(loan * (rate / 100.0) * years)
    total_repay = loan + interest
    ans = fmt_r(total_repay)
    svg = svg_factor_card(
        f"{bank} — Borrowed Capital Machinery Loan",
        f"Borrower: {s['business']} ({s['area']})",
        [
            ("Principal Borrowed Capital", fmt_r(loan)),
            ("Simple Interest Rate", f"{rate}% per year"),
            ("Loan Term", f"{years} years"),
            ("Total Amount Repayable (Principal + Interest)", "R ???"),
        ],
    )
    prompt = (
        f"Examine the {bank} Borrowed Capital quote for {s['business']}. "
        f"Calculate the Total Amount Repayable (`R ???`, including {years} years of simple interest at {rate}% p.a.)."
    )
    steps = [
        f"Annual interest = {fmt_r(loan)} x {rate}% = {fmt_r(int(loan * rate / 100))}/year.",
        f"Total {years}-year interest = {years} x {fmt_r(int(loan * rate / 100))} = {fmt_r(interest)}.",
        f"Total Repayable = Principal ({fmt_r(loan)}) + Interest ({fmt_r(interest)}) = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="23_borrowed_capital_interest_cost_calc",
        title="Calculate Borrowed Capital Total Repayment",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total_repay}", str(total_repay)],
        steps=steps,
        hints={
            "tier_1": "First find simple interest across all years, then add the original loan principal.",
            "tier_2": f"Interest = {fmt_r(loan)} x {rate}% x {years}. Add to {fmt_r(loan)}.",
            "tier_3": f"Total Repayable = {ans}.",
        },
        misconception_tags=["answers_interest_only_instead_of_total_repayment"],
        question_family_id="borrowed_capital_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b24_capital_investment_table_drill(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt1 = rng.randint(20, 50) * 1000
    amt2 = rng.randint(15, 45) * 1000
    amt3 = rng.randint(25, 65) * 1000
    amt4 = rng.randint(6, 15) * 1000
    headers = ["Item / Resource", "Capital Classification"]
    table_rows = [
        [(f"{s['entrepreneur']} invests {fmt_r(amt1)} personal savings", "given", False), ("Own Financial Capital", "required", True)],
        [(f"Commercial welding machine ({fmt_r(amt2)}) used in workshop", "given", False), ("Physical (Real) Capital Good", "required", True)],
        [(f"5-year machinery loan ({fmt_r(amt3)}) from bank", "given", False), ("Borrowed Financial Capital", "required", True)],
        [(f"Owner's private lounge sofa ({fmt_r(amt4)}) at home", "given", False), ("Consumer Good (Not Capital)", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Own Financial Capital",
        "t0_r1_c1": "Physical (Real) Capital Good",
        "t0_r2_c1": "Borrowed Financial Capital",
        "t0_r3_c1": "Consumer Good (Not Capital)",
    }
    prompt = f"Classify each resource linked to {s['business']} into `Own Financial Capital`, `Borrowed Financial Capital`, `Physical (Real) Capital Good`, or `Consumer Good (Not Capital)`."
    return _make_table(
        rng,
        subskill="24_capital_investment_table_drill",
        title="Capital Classification Drill Table",
        prompt=prompt,
        journal_type="capital_classification_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Distinguish personal money (Own Capital), bank loans (Borrowed), factory machines (Physical Capital), and home use (Consumer Good).",
            "tier_2": "Only productive business funds/tools are Capital.",
            "tier_3": "1: Own Financial Capital | 2: Physical Capital Good | 3: Borrowed Financial Capital | 4: Consumer Good (Not Capital).",
        },
        misconception_tags=["treats_home_furniture_as_business_capital"],
        question_family_id="capital_class_table",
    )


def _b25_entrepreneurship_combining_factors_role(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap = rng.randint(30, 80) * 1000
    prompt = (
        f"{s['entrepreneur']} notices commuters in {s['area']} lack healthy hot lunches, invests {fmt_r(cap)}, leases a kitchen kiosk, hires two cooks, and manages operations. "
        f"What distinct economic role does **Entrepreneurship** perform compared to Labour?"
    )
    ans = "Spotting opportunities, taking financial risk of profit/loss, and organising Land, Labour, and Capital together into an enterprise"
    opts = [
        "Spotting opportunities, taking financial risk of profit/loss, and organising Land, Labour, and Capital together into an enterprise",
        "Only working fixed hourly till shifts for guaranteed overtime wages without financial risk",
        "Eliminating all need for Capital and Natural Resources",
        "Passing laws through the South African Reserve Bank",
    ]
    exp = f"Entrepreneurship ({s['entrepreneur']} risking {fmt_r(cap)}) is the driving force that spots gaps, assumes risk, and coordinates Land, Labour, and Capital to earn Profit."
    return _make_mcq(
        rng,
        subskill="25_entrepreneurship_combining_factors_role",
        title="Unique Economic Role of Entrepreneurship",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Who takes the financial risk of loss vs profit and coordinates the other three factors?",
            "tier_2": "Entrepreneurship initiates, organises the 3 factors, and bears risk for Profit.",
            "tier_3": ans,
        },
        misconception_tags=["treats_entrepreneurship_as_ordinary_salaried_labour"],
        question_family_id="entrepreneurship_role",
    )


ARCHETYPES_01_25 = {
    "01_inputs_vs_outputs_production": _b01_inputs_vs_outputs_production,
    "02_four_factors_identification": _b02_four_factors_identification,
    "03_factor_remuneration_matching": _b03_factor_remuneration_matching,
    "04_factors_and_remuneration_table": _b04_factors_and_remuneration_table,
    "05_natural_resources_land_definition": _b05_natural_resources_land_definition,
    "06_renewable_vs_non_renewable_resources": _b06_renewable_vs_non_renewable_resources,
    "07_sustainability_and_pollution_risk": _b07_sustainability_and_pollution_risk,
    "08_natural_resource_depletion_calc": _b08_natural_resource_depletion_calc,
    "09_labour_definition_human_effort": _b09_labour_definition_human_effort,
    "10_unskilled_labour_characteristics": _b10_unskilled_labour_characteristics,
    "11_semi_skilled_labour_characteristics": _b11_semi_skilled_labour_characteristics,
    "12_skilled_labour_characteristics": _b12_skilled_labour_characteristics,
    "13_classify_labour_skill_levels_table": _b13_classify_labour_skill_levels_table,
    "14_human_capital_experience_growth": _b14_human_capital_experience_growth,
    "15_training_pathways_tvet_learnership": _b15_training_pathways_tvet_learnership,
    "16_worker_value_creativity_innovation": _b16_worker_value_creativity_innovation,
    "17_sa_critical_skills_shortages": _b17_sa_critical_skills_shortages,
    "18_labour_productivity_output_per_worker": _b18_labour_productivity_output_per_worker,
    "19_labour_shortage_business_impact_rubric": _b19_labour_shortage_business_impact_rubric,
    "20_capital_financial_vs_physical_goods": _b20_capital_financial_vs_physical_goods,
    "21_consumer_good_vs_capital_good": _b21_consumer_good_vs_capital_good,
    "22_own_vs_borrowed_capital_comparison": _b22_own_vs_borrowed_capital_comparison,
    "23_borrowed_capital_interest_cost_calc": _b23_borrowed_capital_interest_cost_calc,
    "24_capital_investment_table_drill": _b24_capital_investment_table_drill,
    "25_entrepreneurship_combining_factors_role": _b25_entrepreneurship_combining_factors_role,
}
