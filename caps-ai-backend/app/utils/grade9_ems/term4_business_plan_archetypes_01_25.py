"""Grade 9 EMS - Term 4 Business Plan: Archetypes 01 to 25.

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Business Plan.md
and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African entrepreneurship contexts.
"""
from __future__ import annotations

import html
import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario


def get_ems_scenario(rng: random.Random) -> Dict[str, Any]:
    d = dict(_raw_ems_scenario(rng))
    d["business"] = f"{d['entrepreneur']} {d['business_type']}"
    return d

TOPIC_NAME = "Business Plan"
TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term4_business_plan"
CURRICULUM_REF = "Term 4 > Entrepreneurship: Business Plan"


def _fmt_r(amount: int | float) -> str:
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _esc(text: str) -> str:
    return html.escape(str(text), quote=False)


def _make_cell(coord: str, value: str, cell_type: str = "given") -> Dict[str, Any]:
    return {
        "coordinate": coord,
        "value": value,
        "type": cell_type,
        "editable": cell_type in ("required", "editable"),
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "concept_id": subskill,
        "concept_group": "business_plan",
        "learning_objective_id": f"lo_g9_bp_{subskill}",
        "curriculum_reference": CURRICULUM_REF,
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
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "hint_sections": {
            "1_nudge": hints.get("tier_1", ""),
            "2_concept": hints.get("tier_2", ""),
            "3_breakdown": hints.get("tier_3", ""),
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "business_plan", "financial_planning", "south_africa"],
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "concept_id": subskill,
        "concept_group": "business_plan",
        "learning_objective_id": f"lo_g9_bp_{subskill}",
        "curriculum_reference": CURRICULUM_REF,
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
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "hint_sections": {
            "1_nudge": hints.get("tier_1", ""),
            "2_concept": hints.get("tier_2", ""),
            "3_breakdown": hints.get("tier_3", ""),
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "business_plan", "financial_planning", "south_africa"],
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
        "topic": TOPIC_NAME,
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": subskill,
        "concept_id": subskill,
        "concept_group": "business_plan",
        "learning_objective_id": f"lo_g9_bp_{subskill}",
        "curriculum_reference": CURRICULUM_REF,
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
        "expected_answer": sample_answer,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "hint_sections": {
            "1_nudge": hints.get("tier_1", ""),
            "2_concept": hints.get("tier_2", ""),
            "3_breakdown": hints.get("tier_3", ""),
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["entrepreneurship", "business_plan", "classification_table", "south_africa"],
    }


def arch_01_business_plan_concept_and_core_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Before spending personal savings in **{sc['area']}**, **{sc['entrepreneur']}** compiles a comprehensive **business plan** for **{sc['business']}**.\n\n"
        "Which definition **best** captures what a business plan is and why entrepreneurs write one before launching?"
    )
    correct = "A formal written document outlining goals, products, market strategy, operations, and financial forecasts to test viability and guide decisions."
    distractors = [
        "A mandatory weekly municipal licence fee receipt displayed behind retail cash registers.",
        "A private employee grievance log used only by trade union shop stewards.",
        "A short price brochure handed out to walk-in shoppers on opening weekend.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_01",
        subskill="01_business_plan_concept_and_core_purpose",
        title="Concept & Purpose of a Business Plan",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Drafting a formal proposal lets **{sc['entrepreneur']}** verify on paper whether **{sc['business']}** is financially and practically viable before committing scarce cash."
        ),
        hints={
            "tier_1": "Think of a full written roadmap testing feasibility before launch.",
            "tier_2": "A business plan details goals, marketing, operations, and finances to guide growth and check viability.",
            "tier_3": correct,
        },
        misconception_tags=["thinking_a_business_plan_is_just_an_ad_or_receipt"],
    )


def arch_02_business_plan_external_audience_investors_lenders(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    loan = rng.choice([250000, 350000, 500000])
    prompt = (
        f"**{sc['entrepreneur']}** applies for **{_fmt_r(loan)}** in start-up finance from a South African commercial bank for **{sc['business']}**.\n\n"
        "Give **two** specific reasons why banks or outside investors insist on examining an applicant's written **business plan** before releasing funds."
    )
    expected = (
        f"1. To assess financial viability, break-even thresholds, and repayment ability (cash flow) for the {_fmt_r(loan)} loan; "
        "2. To evaluate management capability, real market demand, and competitor risks."
    )
    sol = (
        f"**Why Lenders & Investors Inspect Proposals ({_fmt_r(loan)}) [4 marks]:**\n\n"
        f"1. **Repayment & Viability Proof:** Banks review 3-year cash-flow and break-even numbers to confirm **{sc['business']}** can afford interest and repay **{_fmt_r(loan)}** **[2]**.\n"
        "2. **Risk & Management Check:** Investors check whether genuine target customers exist and whether owners have realistic operational strategies **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_02",
        subskill="02_business_plan_external_audience_investors_lenders",
        title="Why Banks & Investors Require a Business Plan",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Lenders want proof they will get repaid and proof the founder understands market risks.",
            "tier_2": "Mention (1) financial viability/repayment cash flow and (2) management competence & market risk check.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Verifies financial viability / cash flow to repay loan", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Evaluates market demand, risks, and owner capability", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_business_plans_only_benefit_outside_banks"],
    )


def arch_03_business_plan_eleven_components_overview_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap = rng.choice([180000, 240000, 320000])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" width="100%" height="auto">'
        '<rect x="0" y="0" width="680" height="250" fill="#f8fafc" rx="10"/>'
        f'<text x="340" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Architecture of {_esc(sc["business"])} Business Plan (Capital: {_fmt_r(cap)})</text>'
        '<rect x="20" y="42" width="148" height="44" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="94" y="62" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e3a8a">1. Cover &amp; Contents</text>'
        '<text x="94" y="76" text-anchor="middle" font-size="9.5" fill="#1e40af">Navigation &amp; details</text>'
        '<rect x="184" y="42" width="148" height="44" rx="6" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.5"/>'
        '<text x="258" y="62" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#312e81">2. Executive Summary</text>'
        '<text x="258" y="76" text-anchor="middle" font-size="9.5" fill="#3730a3">Hook: written LAST</text>'
        '<rect x="348" y="42" width="148" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        '<text x="422" y="62" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#78350f">3. Description &amp; Legal</text>'
        '<text x="422" y="76" text-anchor="middle" font-size="9.5" fill="#92400e">Ownership &amp; licences</text>'
        '<rect x="512" y="42" width="148" height="44" rx="6" fill="#fae8ff" stroke="#a21caf" stroke-width="1.5"/>'
        '<text x="586" y="62" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#701a75">4. SWOT &amp; PESTLE</text>'
        '<text x="586" y="76" text-anchor="middle" font-size="9.5" fill="#86198f">Internal &amp; external scan</text>'
        '<rect x="20" y="106" width="202" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        '<text x="121" y="128" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">5. Marketing &amp; Competitor Plan</text>'
        '<text x="121" y="144" text-anchor="middle" font-size="9.5" fill="#166534">Research, Target Market &amp; 7 Ps</text>'
        '<rect x="239" y="106" width="202" height="50" rx="6" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5"/>'
        '<text x="340" y="128" text-anchor="middle" font-size="11" font-weight="bold" fill="#134e4a">6. Operational &amp; Management</text>'
        '<text x="340" y="144" text-anchor="middle" font-size="9.5" fill="#115e59">Production workflow &amp; Organogram</text>'
        '<rect x="458" y="106" width="202" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>'
        '<text x="559" y="128" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">7. Financial Plan</text>'
        f'<text x="559" y="144" text-anchor="middle" font-size="9.5" fill="#b91c1c">{_fmt_r(cap)} Budget, Cash Flow &amp; BEP</text>'
        '<rect x="85" y="176" width="510" height="48" rx="8" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>'
        '<text x="340" y="198" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">Key Principle: All sections must tell ONE consistent financial and operational story.</text>'
        '<text x="340" y="214" text-anchor="middle" font-size="10" fill="#475569">Example: Marketing promotion spend must match figures inside the Financial budget.</text>'
        '</svg>'
    )
    prompt = (
        f"Study the structural diagram for **{sc['business']}**'s business plan (**{_fmt_r(cap)}** capital).\n\n"
        "1. Explain why **Section 2 (Executive Summary)** sits near the front yet is written **LAST**.\n"
        "2. Explain the cross-section consistency rule shown at the bottom linking **Section 5 (Marketing)** and **Section 7 (Financial)**."
    )
    expected = (
        f"1. The Executive Summary summarises highlights from every finished chapter (product, target market, {_fmt_r(cap)} funding, profit), so authors must complete all research and financial tables first. "
        "2. Every strategy promised in Marketing/Operations (e.g. radio ads or staff hires) must match the exact Rand budgets in the Financial Plan."
    )
    sol = (
        f"**Structural Logic of {sc['business']}'s Plan ({_fmt_r(cap)}) [4 marks]:**\n\n"
        f"1. **Executive Summary Written Last:** Placed upfront to hook readers, but drafted only after SWOT, Marketing, Operations, and the **{_fmt_r(cap)}** financial forecasts are finalised **[2]**.\n"
        "2. **Internal Consistency Rule:** Investors check that marketing campaigns, machinery, and staffing described in text appear accurately inside the **Financial budget and cash flow** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_03",
        subskill="03_business_plan_eleven_components_overview_svg",
        title="Business Plan Components & Structure",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Notice the labels inside Box 2 ('written LAST') and the bottom box.",
            "tier_2": "Summary condenses completed sections; budgets must reflect marketing & operational promises.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Executive Summary condenses completed SWOT/Marketing/Financial findings", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Marketing/Operational promises must match Financial Plan Rand budgets", "marks": 2, "editable": True},
        ],
        misconception_tags=["writing_executive_summary_before_financial_calculations"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_04_cover_page_and_contents_page_essentials(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['entrepreneur']}** prepares the front matter of **{sc['business']}**'s formal proposal in **{sc['area']}**.\n\n"
        "Which items belong properly on a **Cover Page** rather than inside detailed financial schedules?"
    )
    correct = "Business name and logo, document title, owner/contact details, physical address, and submission date."
    distractors = [
        "Three-year monthly cash-flow spreadsheets and break-even charts.",
        "Individual employee bank account PINs and disciplinary warnings.",
        "Full supplier invoice archives from the past five years.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_04",
        subskill="04_cover_page_and_contents_page_essentials",
        title="Cover Page & Contents Page Essentials",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A clean **Cover Page** introduces **{sc['business']}**, **{sc['entrepreneur']}**'s contact details, logo, and date, while the **Contents Page** lists headings and page numbers for fast navigation."
        ),
        hints={
            "tier_1": "Think first impression and contact details on page 1.",
            "tier_2": "Cover Page shows name, logo, title, owner contact details, and date.",
            "tier_3": correct,
        },
        misconception_tags=["crowding_break_even_tables_onto_cover_page"],
    )


def arch_05_executive_summary_purpose_and_four_aspects(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    capital = rng.choice([150000, 220000, 280000])
    prompt = (
        f"**{sc['entrepreneur']}** drafts an **Executive Summary** for **{sc['business']}** in **{sc['area']}** seeking **{_fmt_r(capital)}**.\n\n"
        "Name the **four key aspects** every compelling **Executive Summary** should state concisely on page 1."
    )
    expected = (
        f"1. Name and form of ownership of {sc['business']}; "
        "2. Core product/service and unique selling point; "
        "3. Target market and management team strength; "
        f"4. Capital required ({_fmt_r(capital)}), expected turnover, and profitability/break-even timeline."
    )
    sol = (
        f"**Four Essential Aspects of an Executive Summary ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Business Identity & Ownership:** Name (**{sc['business']}**), location (**{sc['area']}**), and legal form **[1]**.\n"
        "2. **Product & Competitive Edge:** What is sold and why customers will choose it over rivals **[1]**.\n"
        "3. **Market & Management:** Defined target customers and key owners' skills **[1]**.\n"
        f"4. **Financial Highlights:** Exact funding sought (**{_fmt_r(capital)}**) and projected sales/profit returns **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_05",
        subskill="05_executive_summary_purpose_and_four_aspects",
        title="Four Key Aspects of an Executive Summary",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "A busy investor reads only page 1 first: Who are you? What do you sell? Who buys it? How much profit/money?",
            "tier_2": "Include: Identity, Product/USP, Target Market/Team, Funding & Profit summary.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Business identity / legal ownership", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Product/service & uniqueness", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Target market & team expertise", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": f"Capital required ({_fmt_r(capital)}) & profit/viability highlights", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_funding_and_profit_highlights_from_executive_summary"],
    )


def arch_06_business_description_and_location_factors(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"When describing **{sc['business']}** in **{sc['area']}** inside a start-up proposal, which factor is **crucial** to justify when choosing the physical premises?"
    )
    correct = "Proximity to target customers, reliable electricity/water/transport access, municipal zoning compliance, and affordable rent."
    distractors = [
        "Choosing the highest possible monthly commercial rent regardless of foot traffic.",
        "Hiding the premises far from roads and public transport routes.",
        "Avoiding municipal trading licences to reduce paperwork.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_06",
        subskill="06_business_description_and_location_factors",
        title="Business Description & Site Location Factors",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Justifying location for **{sc['business']}** in **{sc['area']}** requires balancing customer convenience, supplier transport, utilities, zoning laws, and sustainable rental costs."
        ),
        hints={
            "tier_1": "Think of customers, transport, utilities, zoning, and affordable rent.",
            "tier_2": "Customer access, infrastructure, zoning compliance, and cost-effective rent.",
            "tier_3": correct,
        },
        misconception_tags=["ignoring_zoning_and_infrastructure_in_location_decisions"],
    )


def arch_07_vision_mission_goals_and_objectives_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("To become South Africa's most trusted eco-packaging leader by 2035", "Vision", "Long-range inspirational future"),
        ("To supply affordable biodegradable containers to local food traders daily", "Mission", "Core present purpose & customers"),
        ("Expand warehouse distribution across three provinces within 5 years", "Long-term goal", "Broad multi-year strategic aim"),
        ("Increase monthly unit sales by 15% before 30 November this year", "Short-term objective", "Specific, measurable, timed target"),
    ]
    rng.shuffle(pool)
    headers = ["Strategic Statement", "Focus", "Classification (Vision / Mission / Long-term goal / Short-term objective)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Strategic Statement | Focus | Classification |", "| :--- | :--- | :--- |"]
    for idx, (stmt, cls, foc) in enumerate(pool):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", stmt, "given"),
            _make_cell(f"t0_r{idx}_c1", foc, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = cls
        cell_hints[coord] = "Enter exact term: Vision, Mission, Long-term goal, or Short-term objective."
        memo_lines.append(f"| {stmt} | {foc} | {cls} |")

    sample = "; ".join(f"{i+1}: {pool[i][1]}" for i in range(4))
    worked = f"**Strategic Direction Statements ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_07",
        subskill="07_vision_mission_goals_and_objectives_table",
        title="Vision, Mission, Goals & Objectives",
        prompt=(
            f"Classify four strategic statements drafted for **{sc['business']}** in **{sc['area']}** as **Vision**, **Mission**, **Long-term goal**, or **Short-term objective**."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Vision = distant dream; Mission = daily purpose; Goal = multi-year aim; Objective = short-term measurable target.",
            "tier_2": "Use exact strings: Vision, Mission, Long-term goal, Short-term objective.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Classifies as {pool[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_vision_dream_with_present_mission_or_smart_objective"],
    )


def arch_08_smart_objectives_formulation_exercise(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pct = rng.choice([12, 15, 20])
    months = rng.choice([6, 9, 12])
    prompt = (
        f"**{sc['entrepreneur']}** writes a vague wish for **{sc['business']}** in **{sc['area']}**: *'We want to make more sales soon.'*\n\n"
        f"Rewrite this wish into a proper **SMART objective** (increasing turnover by **{pct}%** within **{months} months**), and name what each letter in **SMART** represents."
    )
    expected = (
        f"SMART stands for Specific, Measurable, Achievable, Realistic, Time-bound. "
        f"Objective: 'Increase {sc['business']} monthly sales turnover by {pct}% within {months} months through local distributor partnerships.'"
    )
    sol = (
        f"**SMART Objective Formulation ({sc['business']}) [4 marks]:**\n\n"
        "- **SMART Meaning:** **S**pecific, **M**easurable, **A**chievable, **R**ealistic, **T**ime-bound **[2]**.\n"
        f"- **Rewritten Objective:** *'Increase **{sc['business']}**'s sales turnover by **{pct}%** (measurable/specific) through expanded retail accounts within the next **{months} months** (time-bound).'* **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_08",
        subskill="08_smart_objectives_formulation_exercise",
        title="Writing Measurable SMART Business Objectives",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "A SMART objective has exact numbers (%) and a clear deadline (months).",
            "tier_2": "Specific, Measurable, Achievable, Realistic, Time-bound + rewrite using the exact % and months.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Expands S-M-A-R-T accurately", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Valid SMART objective incorporating {pct}% and {months} months", "marks": 2, "editable": True},
        ],
        misconception_tags=["writing_vague_unmeasurable_business_goals"],
    )


def arch_09_forms_of_ownership_and_organisational_structure_link(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"**{sc['entrepreneur']}** compares operating **{sc['business']}** as a **Sole Trader** versus a **Private Company ((Pty) Ltd)**.\n\n"
        "How does the chosen **form of ownership** shape management structure and owner risk?"
    )
    correct = "A Sole Trader has full personal control yet unlimited personal liability; a Private Company creates a separate legal entity with limited liability, continuity, and stricter formal governance."
    distractors = [
        "Sole Traders must elect an external ten-member board before opening a bank account.",
        "Private Companies pay zero company tax and cannot employ salaried managers.",
        "Forms of ownership have zero effect on personal asset risk or succession.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_09",
        subskill="09_forms_of_ownership_and_organisational_structure_link",
        title="Forms of Ownership, Liability & Structure",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Choosing **Sole Trader** gives **{sc['entrepreneur']}** simple management but exposes personal savings to business debt (**unlimited liability**), whereas **(Pty) Ltd** protects personal assets and eases multi-shareholder expansion."
        ),
        hints={
            "tier_1": "Compare personal debt liability and governance between Sole Traders and Private Companies.",
            "tier_2": "Sole Trader = simple + unlimited liability; (Pty) Ltd = limited liability + continuity + formal structure.",
            "tier_3": correct,
        },
        misconception_tags=["believing_sole_traders_enjoy_limited_liability"],
    )


def arch_10_legal_requirements_bcea_lra_nca_and_licences_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    laws = [
        ("Sets maximum weekly hours, overtime pay, and worker leave entitlements", "BCEA", "Employment conditions"),
        ("Protects consumers on credit agreements and stops reckless lending", "NCA", "Consumer credit rules"),
        ("Regulates broadcasting, telecoms, and digital electronic communications", "ECA", "Communications compliance"),
        ("Municipal approval needed before selling prepared food or trading on site", "Trading licence", "Municipal permit"),
    ]
    rng.shuffle(laws)
    headers = ["Legal Requirement in Proposal", "Scope", "Exact Requirement (BCEA / NCA / ECA / Trading licence)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Legal Requirement | Scope | Exact Label |", "| :--- | :--- | :--- |"]
    for idx, (desc, label, scope) in enumerate(laws):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", desc, "given"),
            _make_cell(f"t0_r{idx}_c1", scope, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = label
        cell_hints[coord] = "Enter exact label: BCEA, NCA, ECA, or Trading licence."
        memo_lines.append(f"| {desc} | {scope} | {label} |")

    sample = "; ".join(f"{i+1}: {laws[i][1]}" for i in range(4))
    worked = f"**Legal Compliance Requirements ({area}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_10",
        subskill="10_legal_requirements_bcea_lra_nca_and_licences_table",
        title="Legal Compliance & Licences Schedule",
        prompt=(
            f"Entrepreneurs launching a venture in **{area}** list statutory compliance rules.\n\n"
            "Enter **BCEA**, **NCA**, **ECA**, or **Trading licence** in Column 3 for each item."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Work hours->BCEA; Credit->NCA; Telecoms->ECA; Local premises permit->Trading licence.",
            "tier_2": "Use exact labels: BCEA, NCA, ECA, Trading licence.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Matches {laws[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["omitting_local_trading_licences_and_credit_laws_from_plans"],
    )


def arch_11_intellectual_property_patents_copyrights_trademarks(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    invention = rng.choice(["solar-powered water purifier", "custom biodegradable food lid", "mobile inventory app interface"])
    prompt = (
        f"**{sc['business']}** develops an original **{invention}** in **{sc['area']}** and wants legal protection against copycats.\n\n"
        "Which pair accurately matches South African **intellectual property protections**?"
    )
    correct = "A patent protects a novel technical invention; copyright protects original written, software, or artistic works; a trademark protects distinctive brand names and logos."
    distractors = [
        "A trading licence grants global copyright over every rival product's selling price.",
        "Patents only protect retail shop lease contracts from property inflation.",
        "Copyright automatically registers commercial driver's licences for delivery vans.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_11",
        subskill="11_intellectual_property_patents_copyrights_trademarks",
        title="Intellectual Property: Patents, Copyright & Trademarks",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Before marketing an innovative **{invention}**, **{sc['business']}** registers **patents** (inventions), **trademarks** (brand identity), and relies on **copyright** (original code/manuals/art)."
        ),
        hints={
            "tier_1": "Separate technical inventions, creative text/software, and brand logos.",
            "tier_2": "Patent = invention; Copyright = original creative/code work; Trademark = logo/brand name.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_patents_with_trademarks_and_municipal_licences"],
    )


def arch_12_pestle_macro_environment_analysis_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    pool = [
        ("Rising interest rates and inflation squeezing household budgets", "Economic", "Borrowing costs & purchasing power"),
        ("New plastic bag environmental levy and waste recycling rules", "Environmental", "Ecological & sustainability compliance"),
        ("Municipal solar micro-grid approvals and digital mobile payment adoption", "Technological", "Automation & energy tech"),
        ("Strict minimum wage and Employment Equity workplace mandates", "Legal", "Statutory labour regulations"),
        ("Changing youth preference toward healthy plant-based snacks", "Social", "Demographic & lifestyle trends"),
        ("National export trade agreement incentives and municipal stability", "Political", "Government policy & governance"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["External Macro Factor", "Example Impact", "PESTLE Dimension (Political / Economic / Social / Technological / Legal / Environmental)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| External Macro Factor | Example Impact | PESTLE Dimension |", "| :--- | :--- | :--- |"]
    for idx, (fac, dim, imp) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", fac, "given"),
            _make_cell(f"t0_r{idx}_c1", imp, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = dim
        cell_hints[coord] = "Enter exact PESTLE dimension: Political, Economic, Social, Technological, Legal, or Environmental."
        memo_lines.append(f"| {fac} | {imp} | {dim} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**PESTLE Macro-Environment Scan ({area}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_12",
        subskill="12_pestle_macro_environment_analysis_table",
        title="PESTLE Macro-Environment Classification",
        prompt=(
            f"Classify four external macro forces affecting new businesses in **{area}** under the exact **PESTLE** dimension in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "P=Political, E=Economic, S=Social, T=Technological, L=Legal, E=Environmental.",
            "tier_2": "Write exact words: Political, Economic, Social, Technological, Legal, or Environmental.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Identifies {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_internal_weaknesses_with_macro_pestle_forces"],
    )


def arch_13_economic_and_social_macro_factors_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    rate_hike = rng.choice(["interest rates rise sharply", "fuel and electricity tariffs surge"])
    prompt = (
        f"While preparing cash forecasts for **{sc['business']}** in **{sc['area']}**, **{sc['entrepreneur']}** sees that **{rate_hike}** across South Africa.\n\n"
        "Explain **two** concrete impacts this macro-economic shift should trigger inside **{sc['business']}**'s operational and financial budgets."
    )
    expected = (
        f"1. Higher operating/financing costs squeeze profit margins (if {rate_hike}, loan interest or transport costs increase), requiring larger cash reserves. "
        "2. Households cut discretionary spending, so unit sales forecasts must stay conservative or offer affordable entry-level pack sizes."
    )
    sol = (
        f"**Macro-Economic Sensitivity ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Cost & Cash Buffer Adjustment:** When **{rate_hike}**, monthly expenses and debt repayments rise -> build conservative expense allowances and cash reserves **[2]**.\n"
        "2. **Demand & Pricing Strategy:** Financially pressured shoppers buy fewer luxury items -> forecast realistic sales volume and offer cost-effective value packs **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_13",
        subskill="13_economic_and_social_macro_factors_impact",
        title="Adapting Forecasts to Macro-Economic Shifts",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Think of both business expense lines AND customer spending power.",
            "tier_2": "Higher operating/debt costs -> bigger cash buffer; lower household income -> conservative sales & value packs.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Raises operating/interest costs requiring larger cash reserves", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Lowers household spending -> realistic sales forecasts or value pricing", "marks": 2, "editable": True},
        ],
        misconception_tags=["treating_sales_forecasts_as_immune_to_inflation_or_interest_rates"],
    )


def arch_14_swot_analysis_internal_vs_external_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    items = [
        ("Experienced, certified technicians with loyal client service", "Strength", "Internal positive"),
        ("Limited start-up cash reserve and single small delivery van", "Weakness", "Internal limitation"),
        ("New housing estate nearby creating 400 potential households", "Opportunity", "External positive"),
        ("Established supermarket chain launching cut-price delivery nearby", "Threat", "External risk"),
    ]
    rng.shuffle(items)
    headers = ["Observation on Venture", "Environment Origin", "SWOT Element (Strength / Weakness / Opportunity / Threat)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Observation on Venture | Environment Origin | SWOT Element |", "| :--- | :--- | :--- |"]
    for idx, (obs, sw, orig) in enumerate(items):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", obs, "given"),
            _make_cell(f"t0_r{idx}_c1", orig, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = sw
        cell_hints[coord] = "Enter exact word: Strength, Weakness, Opportunity, or Threat."
        memo_lines.append(f"| {obs} | {orig} | {sw} |")

    sample = "; ".join(f"{i+1}: {items[i][1]}" for i in range(4))
    worked = f"**SWOT Matrix Classification ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_14",
        subskill="14_swot_analysis_internal_vs_external_classification_table",
        title="SWOT Classification Table (Internal vs External)",
        prompt=(
            f"Classify four findings for **{sc['business']}** in **{sc['area']}** as **Strength**, **Weakness**, **Opportunity**, or **Threat** in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Strengths & Weaknesses are inside the business; Opportunities & Threats come from outside.",
            "tier_2": "Write exact labels: Strength, Weakness, Opportunity, Threat.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Classifies as {items[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["confusing_external_opportunities_with_internal_strengths"],
    )


def arch_15_swot_matrix_four_quadrants_diagram_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    houses = rng.choice([350, 500, 650])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 245" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="245" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">SWOT Matrix: {_esc(sc["business"])} ({_esc(sc["area"])})</text>'
        '<text x="195" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">HELPFUL (Positive)</text>'
        '<text x="465" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">HARMFUL (Negative)</text>'
        '<rect x="65" y="52" width="255" height="80" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        '<text x="192" y="75" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#14532d">STRENGTHS (Internal)</text>'
        '<text x="192" y="96" text-anchor="middle" font-size="10" fill="#166534">Fast repair turnaround &amp; skilled founder</text>'
        '<text x="192" y="114" text-anchor="middle" font-size="10" fill="#166534">Direct personal customer rapport</text>'
        '<rect x="335" y="52" width="255" height="80" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        '<text x="462" y="75" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#78350f">WEAKNESSES (Internal)</text>'
        '<text x="462" y="96" text-anchor="middle" font-size="10" fill="#92400e">No backup generator during outages</text>'
        '<text x="462" y="114" text-anchor="middle" font-size="10" fill="#92400e">Limited spare-parts cash reserve</text>'
        '<rect x="65" y="142" width="255" height="80" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="192" y="165" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1e3a8a">OPPORTUNITIES (External)</text>'
        f'<text x="192" y="186" text-anchor="middle" font-size="10" fill="#1e40af">{houses} remote-work households nearby</text>'
        '<text x="192" y="204" text-anchor="middle" font-size="10" fill="#1e40af">Local municipal SMME contract tender</text>'
        '<rect x="335" y="142" width="255" height="80" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>'
        '<text x="462" y="165" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#991b1b">THREATS (External)</text>'
        '<text x="462" y="186" text-anchor="middle" font-size="10" fill="#b91c1c">National retail chain opening nearby</text>'
        '<text x="462" y="204" text-anchor="middle" font-size="10" fill="#b91c1c">Frequent municipal power outages</text>'
        '</svg>'
    )
    prompt = (
        f"Study the 4-quadrant **SWOT matrix diagram** for **{sc['business']}** serving **{houses} nearby households** in **{sc['area']}**.\n\n"
        f"1. State **which two quadrants** management can **directly control** inside **{sc['business']}**.\n"
        f"2. Suggest **one** strategy pairing the firm's **Strength** with its **Opportunity ({houses} remote households)**, and **one** fix countering its **Weakness + Power Threat**."
    )
    expected = (
        "1. Internal quadrants: Strengths and Weaknesses. "
        f"2. Strength+Opportunity: Advertise same-day personal repairs to the {houses} remote-work households. "
        "Weakness+Threat fix: Budget for an inverter/solar backup system so outages do not halt service."
    )
    sol = (
        f"**Strategic SWOT Matrix Actions ({sc['business']}) [4 marks]:**\n\n"
        "1. **Directly Controllable Factors:** **Strengths and Weaknesses** (internal environment) **[1]**.\n"
        f"2. **Leverage Strength -> Opportunity:** Pitch fast turnaround and personal founder care directly to the **{houses} remote households** and municipal SMME buyers **[1.5]**.\n"
        "3. **Mitigate Weakness + Threat:** Invest in an inverter/UPS backup power kit and ring-fence an emergency parts reserve to stay operational during outages **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_15",
        subskill="15_swot_matrix_four_quadrants_diagram_svg",
        title="Applying a 2x2 SWOT Matrix to Strategy",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Internal factors (S & W) can be changed directly; External factors (O & T) exist outside.",
            "tier_2": "Identify S & W as controllable, then combine fast service -> remote households & backup power -> outages.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Strengths and Weaknesses (internal)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Links fast repair strength to {houses} remote households", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Addresses generator/cash weakness against outage threat", "marks": 1, "editable": True},
        ],
        misconception_tags=["listing_swot_bullets_without_turning_them_into_action_strategies"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_16_converting_swot_weaknesses_and_threats_into_strategy(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"During an internal audit in **{sc['area']}**, **{sc['business']}** discovers **two** gaps:\n"
        "- Weakness: Employees lack digital spreadsheet skills for quoting.\n"
        "- Threat: A low-cost online competitor enters **{sc['area']}**.\n\n"
        "Propose **one** actionable step to overcome the **Weakness** and **one** competitive response to counter the **Threat**."
    )
    expected = (
        "Weakness fix: Enrol staff in short spreadsheet/quoting training or deploy user-friendly quoting software. "
        "Threat response: Differentiate through fast local personal support, same-day delivery, or bundled loyalty warranties."
    )
    sol = (
        f"**Actionable SWOT Turnaround ({sc['business']}) [4 marks]:**\n\n"
        "1. **Addressing Weakness:** Run targeted staff spreadsheet/quoting workshops or install automated template software to speed up accurate quotes **[2]**.\n"
        "2. **Countering Threat:** Compete on superior **local convenience** (same-day delivery, free installation, after-sales guarantees) where distant online rivals cannot match personal care **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_16",
        subskill="16_converting_swot_weaknesses_and_threats_into_strategy",
        title="Turning SWOT Gaps into Action Strategies",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Solve internal skill gaps via training/tools; beat cheap online rivals via speed, quality, and personal service.",
            "tier_2": "Training/software for quoting + local convenience/service differentiation against online rival.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Staff training / digital quoting template fixes Weakness", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Local speed, service, or warranty loyalty counters Threat", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_businesses_must_always_cut_prices_to_beat_rivals"],
    )


def arch_17_market_research_target_market_segmentation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Before ordering opening inventory for **{sc['business']}** in **{sc['area']}**, **{sc['entrepreneur']}** surveys 80 local shoppers.\n\n"
        "Why must market research define a **target market** clearly inside a venture's marketing section?"
    )
    correct = "To pinpoint exactly who the most likely buyers are (age, income, location, needs) so pricing, product design, and adverts match real demand."
    distractors = [
        "To guarantee every citizen across all nine provinces buys identical luxury items.",
        "To eliminate all municipal electricity charges for the first three years.",
        "To replace financial cash-flow budgets with customer opinion polls.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_17",
        subskill="17_market_research_target_market_segmentation",
        title="Market Research & Target Market Selection",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Targeting everyone wastes scarce promotion money; defining a clear **target market** aligns **{sc['business']}**'s product features, pricing, and channels to buyers most willing to purchase."
        ),
        hints={
            "tier_1": "Should a new SME advertise randomly to everyone, or aim at buyers with matching needs and budget?",
            "tier_2": "Define demographics, income, and habits of likely buyers so 4 Ps fit demand.",
            "tier_3": correct,
        },
        misconception_tags=["defining_target_market_as_everyone_in_south_africa"],
    )


def arch_18_marketing_mix_7ps_product_price_place_promotion(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prod = rng.choice(["organic rusks", "custom school jerseys", "solar phone chargers"])
    prompt = (
        f"**{sc['business']}** plans to sell **{prod}** to commuters and families in **{sc['area']}**.\n\n"
        f"Outline **one** concrete marketing decision for each of the **4 traditional Ps** (**Product**, **Price**, **Place**, **Promotion**) fitting **{prod}**."
    )
    expected = (
        f"Product: Durable/fresh quality {prod} with clear labelling; "
        "Price: Competitive cost-plus pricing matching commuter budgets; "
        "Place: Sold directly at taxi-rank kiosks and local supermarkets; "
        "Promotion: Introductory flyers, WhatsApp status specials, and free tasting/demo stands."
    )
    sol = (
        f"**4 Ps Marketing Application ({prod} at {sc['business']}) [4 marks]:**\n\n"
        f"- **Product:** High quality, durable packaging, and appealing variety of **{prod}** **[1]**.\n"
        "- **Price:** Affordable penetration or cost-plus price aligned to local commuter wallets **[1]**.\n"
        f"- **Place:** Convenient outlets in **{sc['area']}** (high-foot-traffic stalls, local shops, or WhatsApp delivery) **[1]**.\n"
        "- **Promotion:** Flyers, referral discounts, community radio, and social-media demos **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_18",
        subskill="18_marketing_mix_7ps_product_price_place_promotion",
        title="Applying the 4 Ps to a New Launch",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Give one realistic example each for Product design, Price level, Place (selling points), and Promotion.",
            "tier_2": "Cover quality/packaging (Product), competitive pricing (Price), distribution spots (Place), adverts/specials (Promotion).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Concrete Product decision (quality, packaging, features)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Concrete Price decision (cost-plus / competitor-aligned)", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Concrete Place decision (outlets / distribution)", "marks": 1, "editable": True},
            {"id": "mp_4", "desc": "Concrete Promotion decision (flyers, social media, specials)", "marks": 1, "editable": True},
        ],
        misconception_tags=["mixing_up_place_distribution_and_promotion_advertising"],
    )


def arch_19_extended_service_marketing_people_process_physical_env(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    service = rng.choice(["hair and beauty salon", "mobile car-wash service", "tutoring and computer clinic"])
    prompt = (
        f"Because **{sc['business']}** operates a **{service}** in **{sc['area']}**, its marketing section expands from **4 Ps to 7 Ps**.\n\n"
        "Which **three additional elements** make up the extended service **7 Ps**?"
    )
    correct = "People (friendly skilled staff), Process (smooth booking/delivery steps), and Physical Environment (clean, safe, welcoming premises)."
    distractors = [
        "Payroll, Profit Tax, and Public Debt.",
        "Purchasing, Patents, and Productivity Ratios.",
        "Plastics, Paperwork, and Provincial Bylaws.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_19",
        subskill="19_extended_service_marketing_people_process_physical_env",
        title="Extended 7 Ps for Service Businesses",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Service firms like a **{service}** cannot rely only on goods — **People** delivering care, smooth **Processes** (booking/queueing), and a spotless **Physical Environment** define customer experience."
        ),
        hints={
            "tier_1": "Think of who serves clients, how queues/bookings flow, and how the shop looks and feels.",
            "tier_2": "People, Process, and Physical Environment.",
            "tier_3": correct,
        },
        misconception_tags=["omitting_people_process_and_physical_environment_from_7ps"],
    )


def arch_20_five_distribution_channels_place_strategy(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"In selecting **Place (distribution)** for **{sc['business']}** in **{sc['area']}**, **{sc['entrepreneur']}** compares selling directly from the workshop versus using intermediaries.\n\n"
        "Which route represents South Africa's **shortest direct distribution channel**?"
    )
    correct = "Producer -> Consumer (direct sales via own shopfront, market stall, or online order)."
    distractors = [
        "Producer -> Agent -> Wholesaler -> Retailer -> Consumer.",
        "Producer -> Wholesaler -> Retailer -> Consumer.",
        "Producer -> Importer -> Broker -> Wholesaler -> Retailer -> Consumer.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_20",
        subskill="20_five_distribution_channels_place_strategy",
        title="Distribution Channels (Place Strategy)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"**Producer -> Consumer** skips middleman mark-ups so **{sc['business']}** earns higher profit per unit and collects immediate cash and feedback."
        ),
        hints={
            "tier_1": "Shortest channel has zero wholesalers, agents, or outside retailers in between.",
            "tier_2": "Producer -> Consumer (direct channel).",
            "tier_3": correct,
        },
        misconception_tags=["confusing_direct_channel_with_multi_tier_wholesale_chain"],
    )


def arch_21_promotional_mix_advertising_sales_promo_pr_direct(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    budget = rng.choice([3500, 4800, 6000])
    prompt = (
        f"**{sc['business']}** has a modest launch marketing budget of **{_fmt_r(budget)}** in **{sc['area']}**.\n\n"
        f"Explain why **two** low-cost promotional methods (from **social media/WhatsApp**, **sales promotions/samples**, **word-of-mouth**, or **local flyers**) fit **{_fmt_r(budget)}** better than national television adverts."
    )
    expected = (
        f"National TV far exceeds {_fmt_r(budget)} and wastes money on distant viewers; "
        f"targeted local flyers, free samples, and WhatsApp/social-media posts reach nearby buyers directly within {_fmt_r(budget)} and generate immediate measurable foot traffic."
    )
    sol = (
        f"**Budget-Fit Promotional Mix ({_fmt_r(budget)}) [4 marks]:**\n\n"
        f"1. **Cost & Local Targeting:** National TV is prohibitively expensive and hits non-local audiences, whereas **local flyers / community WhatsApp & social posts** concentrate **{_fmt_r(budget)}** strictly in **{sc['area']}** **[2]**.\n"
        "2. **Trial & Conversion:** **In-store demonstrations / introductory discounts** create instant product trial and rapid word-of-mouth referrals **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_21",
        subskill="21_promotional_mix_advertising_sales_promo_pr_direct",
        title="Selecting Cost-Effective Promotional Tools",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Match a small R3 500–R6 000 budget to high-impact neighbourhood outreach.",
            "tier_2": "Compare massive waste/cost of TV vs targeted local flyers, social posts, and free samples/discounts.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Explains budget constraint & local target precision vs TV waste", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Justifies two concrete low-cost tools driving trial/word-of-mouth", "marks": 2, "editable": True},
        ],
        misconception_tags=["proposing_unaffordable_mass_media_in_small_startups"],
    )


def arch_22_competitor_analysis_and_competitive_advantage(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"A bank manager reviews **{sc['business']}**'s competitor section in **{sc['area']}**, which skips naming rival businesses entirely.\n\n"
        "Why is claiming *'We have no competitors'* a serious red flag in an entrepreneur's proposal?"
    )
    correct = "Every product faces direct rivals or indirect substitutes competing for the customer's Rand; overlooking rivals signals weak market research and unrealistic sales forecasts."
    distractors = [
        "South African law requires all entrepreneurs to transfer half their profits to rivals.",
        "Banks only fund businesses that operate illegal monopolies.",
        "Competitor analysis reduces the cost of raw flour and electricity automatically.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_22",
        subskill="22_competitor_analysis_and_competitive_advantage",
        title="Why Competitor Analysis Matters",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Customers always have alternative ways to spend money. Studying rivals lets **{sc['business']}** pinpoint gaps and build a credible **competitive advantage (USP)**."
        ),
        hints={
            "tier_1": "Think of both direct rivals and indirect substitutes fighting for household spending.",
            "tier_2": "Ignoring competition shows weak research and unrealistically optimistic demand projections.",
            "tier_3": correct,
        },
        misconception_tags=["believing_a_new_product_faces_zero_direct_or_indirect_rivals"],
    )


def arch_23_seven_strategies_to_overcome_competition_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Offering free same-day delivery and 7-day customer care", "Superior service", "Service excellence"),
        ("Sourcing longer-lasting materials that outlast cheap imports", "Improved quality", "Product reliability"),
        ("Creating a loyalty punch-card giving every 10th item free", "Loyalty incentives", "Repeat-buyer rewards"),
        ("Opening next to a busy taxi rank with extended 06:30–19:00 hours", "Convenience", "Location & timing"),
        ("Introducing vegan and sugar-free flavours unavailable elsewhere", "Niche innovation", "Unique product variety"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Action Against Rivals", "Advantage", "Competitive Strategy (Superior service / Improved quality / Loyalty incentives / Convenience / Niche innovation)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Action Against Rivals | Advantage | Strategy |", "| :--- | :--- | :--- |"]
    for idx, (act, strat, adv) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", act, "given"),
            _make_cell(f"t0_r{idx}_c1", adv, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = strat
        cell_hints[coord] = "Enter exact strategy: Superior service, Improved quality, Loyalty incentives, Convenience, or Niche innovation."
        memo_lines.append(f"| {act} | {adv} | {strat} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Strategies to Overcome Competition ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_23",
        subskill="23_seven_strategies_to_overcome_competition_table",
        title="Strategies to Overcome Competition",
        prompt=(
            f"Classify four competitive tactics planned by **{sc['business']}** in **{sc['area']}** into exact strategy names in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Match care->Superior service, durability->Improved quality, punch-card->Loyalty incentives, hours/site->Convenience, unique flavours->Niche innovation.",
            "tier_2": "Use exact names in Column 3.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Matches {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["assuming_price_slashing_is_the_only_competitive_strategy"],
    )


def arch_24_operational_production_plan_capacity_and_suppliers(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    daily_cap = rng.choice([180, 240, 300])
    prompt = (
        f"In drafting an **Operational Plan** for **{sc['business']}** in **{sc['area']}** (capacity **{daily_cap} units/day** using inputs from **{sup}**), "
        "state **three** key operational details that must be specified."
    )
    expected = (
        f"1. Machinery, tools, and daily maximum production capacity ({daily_cap} units/day); "
        f"2. Approved raw-material suppliers (including {sup} and backups) plus delivery lead times; "
        "3. Step-by-step production workflow, quality control checks, and workplace safety protocols."
    )
    sol = (
        f"**Operational Plan Components ({sc['business']}) [3 marks]:**\n\n"
        f"1. **Equipment & Capacity:** Exact machines, floor layout, and daily capacity (**{daily_cap} units/day**) **[1]**.\n"
        f"2. **Suppliers & Inventory Control:** Key supplier contracts (such as **{sup}** + backup vendor) and stock reorder levels **[1]**.\n"
        "3. **Process & Quality Standards:** Step-by-step manufacturing/service workflow, quality checks, and worker safety compliance **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_24",
        subskill="24_operational_production_plan_capacity_and_suppliers",
        title="Operational & Production Section Contents",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "How is the product actually made each day — with what machines, suppliers, and quality steps?",
            "tier_2": "Cover equipment/capacity, suppliers/inventory, and workflow/quality control.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Equipment, premises layout & capacity ({daily_cap} units/day)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Suppliers & inventory management", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Production workflow, quality & safety checks", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_supplier_logistics_and_capacity_limits_from_operations"],
    )


def arch_25_management_plan_organogram_and_key_roles_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prod_staff = rng.choice([4, 6, 8])
    sales_staff = rng.choice([2, 3, 4])
    total_staff = 4 + prod_staff + sales_staff
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 235" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="235" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Management Organogram: {_esc(sc["business"])} ({total_staff} Staff)</text>'
        '<rect x="220" y="38" width="200" height="44" rx="8" fill="#1e3a8a" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="320" y="57" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#ffffff">{_esc(sc["entrepreneur"])} (MD)</text>'
        '<text x="320" y="73" text-anchor="middle" font-size="9.5" fill="#dbeafe">Overall Strategy &amp; Control</text>'
        '<line x1="320" y1="82" x2="320" y2="104" stroke="#334155" stroke-width="2"/>'
        '<line x1="115" y1="104" x2="525" y2="104" stroke="#334155" stroke-width="2"/>'
        '<line x1="115" y1="104" x2="115" y2="122" stroke="#334155" stroke-width="2"/>'
        '<line x1="320" y1="104" x2="320" y2="122" stroke="#334155" stroke-width="2"/>'
        '<line x1="525" y1="104" x2="525" y2="122" stroke="#334155" stroke-width="2"/>'
        '<rect x="30" y="122" width="170" height="48" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>'
        '<text x="115" y="143" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">Operations Lead (1)</text>'
        f'<text x="115" y="159" text-anchor="middle" font-size="9.5" fill="#1e40af">Manages {prod_staff} factory staff</text>'
        '<rect x="235" y="122" width="170" height="48" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>'
        '<text x="320" y="143" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">Finance &amp; Admin (1)</text>'
        '<text x="320" y="159" text-anchor="middle" font-size="9.5" fill="#b91c1c">Books, payroll &amp; SARS</text>'
        '<rect x="440" y="122" width="170" height="48" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>'
        '<text x="525" y="143" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">Sales &amp; Marketing (1)</text>'
        f'<text x="525" y="159" text-anchor="middle" font-size="9.5" fill="#166534">Leads {sales_staff} field reps</text>'
        '<rect x="42" y="184" width="146" height="32" rx="5" fill="#f1f5f9" stroke="#64748b"/>'
        f'<text x="115" y="204" text-anchor="middle" font-size="10" fill="#334155">{prod_staff} Production Operators</text>'
        '<rect x="452" y="184" width="146" height="32" rx="5" fill="#f1f5f9" stroke="#64748b"/>'
        f'<text x="525" y="204" text-anchor="middle" font-size="10" fill="#334155">{sales_staff} Sales Representatives</text>'
        '</svg>'
    )
    prompt = (
        f"Examine the organisational chart (organogram) for **{sc['business']}** showing **{total_staff} total staff** "
        f"(including **{prod_staff} Production Operators** and **{sales_staff} Sales Representatives**).\n\n"
        f"1. Who does the **Sales & Marketing Lead** report to, and how many **field reps** report downward to them?\n"
        "2. State **two** reasons investors examine an organogram and key managers' CVs inside a start-up proposal."
    )
    expected = (
        f"1. Reports upward to {sc['entrepreneur']} (MD); supervises {sales_staff} Sales Representatives downward. "
        "2. Clarifies lines of authority/accountability (no overlapping duties) and proves the team possesses relevant technical, financial, and sales skills."
    )
    sol = (
        f"**Organogram Analysis ({sc['business']}, {total_staff} staff) [4 marks]:**\n\n"
        f"1. **Reporting Line:** Reports upward to **{sc['entrepreneur']} (MD)** **[1]** and directly supervises **{sales_staff} Sales Representatives** **[1]**.\n"
        "2. **Investor Value:** Proves clear accountability (every worker knows their supervisor) and demonstrates balanced expertise across Operations, Finance, and Marketing **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_25",
        subskill="25_management_plan_organogram_and_key_roles_svg",
        title="Organogram & Management Reporting Lines",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Follow the vertical line above Sales & Marketing and the box directly underneath it.",
            "tier_2": f"Reports to {sc['entrepreneur']} (MD); manages {sales_staff} reps; proves clear authority & skills.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Reports to {sc['entrepreneur']} (MD)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Supervises {sales_staff} Sales Representatives", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Clarifies accountability & proves team capability", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_organograms_as_decorative_without_reporting_lines"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25 = {
    "01_business_plan_concept_and_core_purpose": arch_01_business_plan_concept_and_core_purpose,
    "02_business_plan_external_audience_investors_lenders": arch_02_business_plan_external_audience_investors_lenders,
    "03_business_plan_eleven_components_overview_svg": arch_03_business_plan_eleven_components_overview_svg,
    "04_cover_page_and_contents_page_essentials": arch_04_cover_page_and_contents_page_essentials,
    "05_executive_summary_purpose_and_four_aspects": arch_05_executive_summary_purpose_and_four_aspects,
    "06_business_description_and_location_factors": arch_06_business_description_and_location_factors,
    "07_vision_mission_goals_and_objectives_table": arch_07_vision_mission_goals_and_objectives_table,
    "08_smart_objectives_formulation_exercise": arch_08_smart_objectives_formulation_exercise,
    "09_forms_of_ownership_and_organisational_structure_link": arch_09_forms_of_ownership_and_organisational_structure_link,
    "10_legal_requirements_bcea_lra_nca_and_licences_table": arch_10_legal_requirements_bcea_lra_nca_and_licences_table,
    "11_intellectual_property_patents_copyrights_trademarks": arch_11_intellectual_property_patents_copyrights_trademarks,
    "12_pestle_macro_environment_analysis_table": arch_12_pestle_macro_environment_analysis_table,
    "13_economic_and_social_macro_factors_impact": arch_13_economic_and_social_macro_factors_impact,
    "14_swot_analysis_internal_vs_external_classification_table": arch_14_swot_analysis_internal_vs_external_classification_table,
    "15_swot_matrix_four_quadrants_diagram_svg": arch_15_swot_matrix_four_quadrants_diagram_svg,
    "16_converting_swot_weaknesses_and_threats_into_strategy": arch_16_converting_swot_weaknesses_and_threats_into_strategy,
    "17_market_research_target_market_segmentation": arch_17_market_research_target_market_segmentation,
    "18_marketing_mix_7ps_product_price_place_promotion": arch_18_marketing_mix_7ps_product_price_place_promotion,
    "19_extended_service_marketing_people_process_physical_env": arch_19_extended_service_marketing_people_process_physical_env,
    "20_five_distribution_channels_place_strategy": arch_20_five_distribution_channels_place_strategy,
    "21_promotional_mix_advertising_sales_promo_pr_direct": arch_21_promotional_mix_advertising_sales_promo_pr_direct,
    "22_competitor_analysis_and_competitive_advantage": arch_22_competitor_analysis_and_competitive_advantage,
    "23_seven_strategies_to_overcome_competition_table": arch_23_seven_strategies_to_overcome_competition_table,
    "24_operational_production_plan_capacity_and_suppliers": arch_24_operational_production_plan_capacity_and_suppliers,
    "25_management_plan_organogram_and_key_roles_svg": arch_25_management_plan_organogram_and_key_roles_svg,
}
