"""Grade 9 EMS Term 1: The Circular Flow — Semantic Archetypes 01 to 25."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional


TOPIC_NAME = "The circular flow"
SUBTOPIC_ID = "term1_circular_flow"


def fmt_zar(amount: float) -> str:
    """Format Rand currency with SA space thousands and comma decimal when needed."""
    rounded = round(amount, 2)
    if abs(rounded - round(rounded)) < 1e-9:
        n = int(round(rounded))
        return f"R{n:,}".replace(",", " ")
    whole, dec = f"{rounded:.2f}".split(".")
    whole_spaced = f"{int(whole):,}".replace(",", " ")
    return f"R{whole_spaced},{dec}"


def fmt_dec(val: float, decimals: int = 1) -> str:
    """Format decimal with South African comma separator."""
    return f"{val:.{decimals}f}".replace(".", ",")


def make_question(
    *,
    rng: random.Random,
    subskill: str,
    question_type: str,
    prompt: str,
    correct_answer: str,
    sample_answer: str,
    worked_solution: str,
    marks: int,
    marking_schema: List[Dict[str, Any]],
    marking_guide: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    options: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
    table_payload: Optional[Dict[str, Any]] = None,
    duration_mins: int = 4,
) -> Dict[str, Any]:
    """Assemble standardized 6-pillar Grade 9 EMS Circular Flow question payload."""
    qid = f"gr9_ems_t1_cf_{subskill}_{rng.randint(100000, 999999)}"
    payload: Dict[str, Any] = {
        "id": qid,
        "topic": TOPIC_NAME,
        "subtopic": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": f"ems_gr9_t1_circular_flow_{subskill}",
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": duration_mins,
        "question_type": question_type,
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct_answer,
        "sample_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "marking_schema": marking_schema,
        "marking_guide": marking_guide,
        "hints": hints,
        "misconception_tags": misconception_tags,
    }
    if options is not None:
        shuffled = list(options)
        rng.shuffle(shuffled)
        payload["options"] = shuffled
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    if table_payload is not None:
        payload.update(table_payload)
    return payload


def svg_two_sector_flow(
    hh_label: str, biz_label: str, factor_income: int, spending: int, inner_real_top: str, inner_real_bot: str
) -> Dict[str, Any]:
    """Render parameterized SVG schematic of a 2-sector circular flow model."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 280" width="100%" height="auto">'
        '<defs>'
        '<marker id="arrB" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,1 L7,4 L0,7 Z" fill="#1d4ed8"/></marker>'
        '<marker id="arrG" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,1 L7,4 L0,7 Z" fill="#059669"/></marker>'
        '</defs>'
        '<rect x="0" y="0" width="640" height="280" fill="#ffffff" rx="8"/>'
        '<text x="320" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        'Two-Sector Closed Circular Flow Schematic</text>'
        f'<rect x="30" y="95" width="150" height="72" rx="8" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="105" y="126" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">HOUSEHOLDS</text>'
        f'<text x="105" y="146" text-anchor="middle" font-size="11" fill="#334155">({hh_label})</text>'
        f'<rect x="460" y="95" width="150" height="72" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>'
        f'<text x="535" y="126" text-anchor="middle" font-size="13" font-weight="700" fill="#065f46">BUSINESSES</text>'
        f'<text x="535" y="146" text-anchor="middle" font-size="11" fill="#334155">({biz_label})</text>'
        f'<rect x="245" y="42" width="150" height="32" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        f'<text x="320" y="62" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">FACTOR MARKET</text>'
        f'<rect x="245" y="200" width="150" height="32" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        f'<text x="320" y="220" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">GOODS &amp; SERVICES MARKET</text>'
        # Inner Real Flow: HH -> Factor Market -> Biz (top), Biz -> Goods Market -> HH (bottom)
        '<path d="M120,95 L120,58 L242,58" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrG)"/>'
        '<path d="M395,58 L520,58 L520,92" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrG)"/>'
        '<path d="M520,167 L520,216 L398,216" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrG)"/>'
        '<path d="M245,216 L120,216 L120,170" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrG)"/>'
        # Outer Money Flow: Biz -> HH top dashed (Factor Income R), HH -> Biz bottom dashed (Spending R)
        '<path d="M555,95 L555,34 L85,34 L85,92" fill="none" stroke="#1d4ed8" stroke-width="2.2" stroke-dasharray="5,3" marker-end="url(#arrB)"/>'
        '<path d="M85,167 L85,254 L555,254 L555,170" fill="none" stroke="#1d4ed8" stroke-width="2.2" stroke-dasharray="5,3" marker-end="url(#arrB)"/>'
        f'<text x="320" y="88" text-anchor="middle" font-size="11" font-weight="600" fill="#065f46">Real: {inner_real_top}</text>'
        f'<text x="320" y="191" text-anchor="middle" font-size="11" font-weight="600" fill="#065f46">Real: {inner_real_bot}</text>'
        f'<text x="320" y="29" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">Money Flow (Factor Income): {fmt_zar(factor_income)}</text>'
        f'<text x="320" y="270" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">Money Flow (Consumer Spending): {fmt_zar(spending)}</text>'
        '</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def svg_three_sector_flow(
    hh_tax: int,
    biz_tax: int,
    gov_grants: int,
    gov_tenders: int,
    hh_spend: int,
    masked_slot: Optional[str] = None,
) -> Dict[str, Any]:
    """Render parameterized SVG 3-sector circular flow (Households, Businesses, Government)."""
    lbl_hh_tax = "[?]" if masked_slot == "direct_tax" else f"Direct & Indirect Tax {fmt_zar(hh_tax)}bn"
    lbl_biz_tax = "[?]" if masked_slot == "biz_tax" else f"Company Tax {fmt_zar(biz_tax)}bn"
    lbl_grants = "[?]" if masked_slot == "grants" else f"Grants & Services {fmt_zar(gov_grants)}bn"
    lbl_tenders = "[?]" if masked_slot == "tenders" else f"Tenders & Subsidies {fmt_zar(gov_tenders)}bn"
    lbl_spend = "[?]" if masked_slot == "spending" else f"Consumer Spending {fmt_zar(hh_spend)}bn"

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 320" width="100%" height="auto">'
        '<defs>'
        '<marker id="arrDark" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,1 L7,4 L0,7 Z" fill="#1e293b"/></marker>'
        '<marker id="arrRed" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,1 L7,4 L0,7 Z" fill="#b91c1c"/></marker>'
        '<marker id="arrBlue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,1 L7,4 L0,7 Z" fill="#1d4ed8"/></marker>'
        '</defs>'
        '<rect x="0" y="0" width="650" height="320" fill="#ffffff" rx="8"/>'
        '<text x="325" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        'Three-Sector Circular Flow Model (R billions)</text>'
        '<rect x="28" y="122" width="136" height="66" rx="8" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>'
        '<text x="96" y="159" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">HOUSEHOLDS</text>'
        '<rect x="486" y="122" width="136" height="66" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>'
        '<text x="554" y="159" text-anchor="middle" font-size="13" font-weight="700" fill="#065f46">BUSINESSES</text>'
        '<rect x="255" y="124" width="140" height="62" rx="8" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>'
        '<text x="325" y="159" text-anchor="middle" font-size="13" font-weight="700" fill="#991b1b">GOVERNMENT</text>'
        '<rect x="245" y="42" width="160" height="28" rx="4" fill="#fef3c7" stroke="#d97706"/>'
        '<text x="325" y="60" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">FACTOR MARKET</text>'
        '<rect x="240" y="250" width="170" height="28" rx="4" fill="#fef3c7" stroke="#d97706"/>'
        '<text x="325" y="268" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">GOODS &amp; SERVICES MARKET</text>'
        # Top factor loop & bottom goods loop
        '<path d="M554,122 L554,56 L408,56" fill="none" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrBlue)"/>'
        '<path d="M245,56 L96,56 L96,119" fill="none" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrBlue)"/>'
        '<path d="M96,188 L96,264 L237,264" fill="none" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrBlue)"/>'
        '<path d="M410,264 L554,264 L554,191" fill="none" stroke="#1d4ed8" stroke-width="2" marker-end="url(#arrBlue)"/>'
        # Taxes & Government flows
        '<path d="M164,142 L252,142" fill="none" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arrRed)"/>'
        '<path d="M255,170 L167,170" fill="none" stroke="#1e293b" stroke-width="1.8" marker-end="url(#arrDark)"/>'
        '<path d="M486,142 L398,142" fill="none" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arrRed)"/>'
        '<path d="M395,170 L483,170" fill="none" stroke="#1e293b" stroke-width="1.8" marker-end="url(#arrDark)"/>'
        # Labels
        f'<text x="208" y="135" text-anchor="middle" font-size="10" font-weight="700" fill="#b91c1c">{lbl_hh_tax}</text>'
        f'<text x="208" y="185" text-anchor="middle" font-size="10" font-weight="700" fill="#1e293b">{lbl_grants}</text>'
        f'<text x="441" y="135" text-anchor="middle" font-size="10" font-weight="700" fill="#b91c1c">{lbl_biz_tax}</text>'
        f'<text x="441" y="185" text-anchor="middle" font-size="10" font-weight="700" fill="#1e293b">{lbl_tenders}</text>'
        '<text x="325" y="34" text-anchor="middle" font-size="11" font-weight="600" fill="#1d4ed8">Wages, Rent, Interest &amp; Profit (Factor Income)</text>'
        f'<text x="325" y="299" text-anchor="middle" font-size="11" font-weight="600" fill="#1d4ed8">{lbl_spend}</text>'
        '</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _build_01_circular_flow_definition_purpose(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("households earning monthly wages and immediately buying maize, transport and electricity from local retailers", "a continuous economic model showing how money, factors of production, goods and services circulate between participants"),
        ("taxes paid by workers funding municipal clinics whose nurses spend wages at supermarkets", "an ongoing two-way interdependence linking households, businesses and government through markets"),
        ("factor payments turning into consumer spending which becomes business sales revenue", "the continuous movement of production inputs, final products and Rand payments across economic participants"),
        ("economic interactions connecting resource owners, producers and the public sector", "a simplified model illustrating how income and production flow endlessly around an economy"),
    ]
    obs, correct = rng.choice(cases)
    distractors = [
        "a once-off government register counting idle gold reserves in a central vault",
        "the physical route taken exclusively by international cargo ships at coastal harbours",
        "a personal household shopping list comparing supermarket discounts",
    ]
    prompt = f"Which definition best describes the **circular flow model**, illustrated by *{obs}*?"
    sol = f"- **Circular Flow Model:** {correct.capitalize()}.\n- One participant's spending becomes another participant's income in a continuous loop."
    return make_question(
        rng=rng,
        subskill="01_circular_flow_definition_purpose",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct.capitalize(),
        sample_answer=correct.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Select accurate circular flow definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for capturing continuous circulation of resources, goods and money.",
        hints={
            "tier_1": "Think of why the word 'circular' is used—flows never stop at one participant.",
            "tier_2": "One participant's spending returns as income to another.",
            "tier_3": correct.capitalize(),
        },
        misconception_tags=["views_spending_as_disappearing_from_economy"],
        options=[correct.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_02_closed_economy_meaning(rng: random.Random, mode: str) -> Dict[str, Any]:
    contexts = [
        ("domestic households, domestic factories and national government trading solely within national borders", "an economy that does not trade (import or export) with the rest of the world"),
        ("a simplified model excluding the foreign sector so all goods produced are consumed domestically", "a self-contained domestic system with zero international trade or foreign capital flows"),
        ("teachers studying basic internal money flows before introducing international exports and imports", "a theoretical domestic economy interacting only among local households, firms and the state"),
        ("an economy operating without cross-border merchandise trade or foreign exchange markets", "an economy completely closed to international imports and exports"),
    ]
    clue, meaning = rng.choice(contexts)
    prompt = (
        f"In Grade 9 economics, the circular flow is introduced using a **closed economy** ({clue}).\n\n"
        f"(a) Define a **closed economy**.\n"
        f"(b) State why South Africa itself is an **open** rather than a closed economy, giving ONE example."
    )
    ans = f"Closed economy: {meaning}; SA is open because it exports minerals/fruit and imports machinery/fuel with foreign countries"
    sol = (
        f"**(a) Definition:** A closed economy is {meaning}.\n"
        f"**(b) South Africa in Reality:** South Africa is an **open economy** because it trades actively worldwide—for example, exporting platinum/citrus and importing fuel, vehicles and electronics."
    )
    return make_question(
        rng=rng,
        subskill="02_closed_economy_meaning",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define closed economy (no foreign trade)", "marks": 2, "type": "A"},
            {"step": "Explain SA is open + one import/export example", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for closed definition; 2 marks for explaining South Africa's open trade links.",
        hints={
            "tier_1": "Ask which participant is left out of a closed economy.",
            "tier_2": "A closed economy omits foreign countries (no imports/exports).",
            "tier_3": ans,
        },
        misconception_tags=["thinks_closed_economy_means_shops_are_shut_down"],
    )


def _build_03_closed_economy_assumptions_vs_reality(rng: random.Random, mode: str) -> Dict[str, Any]:
    assumptions = [
        ("all households spend 100% of their income and save nothing", "in reality, households save part of income in banks and pension funds"),
        ("the country has no trade relations with foreign nations", "in reality, countries import consumer goods/machinery and export commodities"),
        ("businesses sell all output immediately without accumulating unsold stock or borrowing", "in reality, businesses borrow for investment and hold inventories"),
        ("no international financial inflows or outflows alter domestic money supply", "in reality, foreign investors and tourists move capital across borders"),
    ]
    assumed, real = rng.choice(assumptions)
    prompt = (
        f"The textbook circular flow begins with simplifying **assumptions**, such as *{assumed}*.\n\n"
        f"Contrast this simplifying assumption against real-world South African economic behaviour and list ONE additional assumption of the closed model."
    )
    ans = f"Reality contrast: {real}; Other assumption: zero foreign imports/exports (or households spend all income / businesses sell all production)"
    sol = (
        f"- **Model Assumption:** {assumed.capitalize()}.\n"
        f"- **Real-World Contrast:** {real.capitalize()}.\n"
        f"- **Additional Closed Assumption:** There are no international exports or imports, and all household factor income returns directly into domestic goods-market spending."
    )
    return make_question(
        rng=rng,
        subskill="03_closed_economy_assumptions_vs_reality",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Contrast stated assumption with real-world behaviour", "marks": 2, "type": "A"},
            {"step": "State one additional closed-model assumption", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for realistic contrast; 2 marks for valid additional assumption.",
        hints={
            "tier_1": "Think about banks/savings and international trade.",
            "tier_2": "Closed model assumes no savings leakage and no foreign sector.",
            "tier_3": ans,
        },
        misconception_tags=["believes_closed_model_assumptions_describe_actual_south_africa"],
    )


def _build_04_identifying_five_participants_and_markets(rng: random.Random, mode: str) -> Dict[str, Any]:
    items = [
        ("Consumers who own labour and purchase groceries", "Households"),
        ("Producers hiring factors of production to make bread and furniture", "Businesses"),
        ("Public authority collecting taxes and supplying schools and clinics", "Government"),
        ("Exchange arena where finished consumer products and services are bought", "Goods and services market"),
        ("Exchange arena where labour, land, capital and enterprise are hired", "Factor (resource) market"),
    ]
    picked = rng.sample(items, 3)
    headers = ["Economic Description", "Participant / Market"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Economic Description | Participant / Market |", "|---|---|"]
    for r_idx, (desc, name) in enumerate(picked, start=1):
        coord = f"R{r_idx}C1"
        rows_ui.append([
            {"coordinate": f"R{r_idx}C0", "value": desc, "type": "given", "editable": False},
            {"coordinate": coord, "value": "", "type": "required", "editable": True},
        ])
        correct_map[coord] = name
        cell_hints[coord] = "Choose among: Households, Businesses, Government, Goods and services market, Factor (resource) market."
        md_lines.append(f"| {desc} | {name} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="04_identifying_five_participants_and_markets",
        question_type="table_completion",
        prompt="Identify the correct circular-flow participant or market matching each description.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Five Elements of the Closed Circular Flow:**\n\n{md_table}",
        marks=3,
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each accurately identified participant or market.",
        hints={
            "tier_1": "Recall the three participants (Households, Businesses, Government) and two markets.",
            "tier_2": "Inputs trade in the factor market; final products trade in the goods & services market.",
            "tier_3": md_table,
        },
        misconception_tags=["confuses_factor_market_with_goods_market"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "desc", "label": headers[0]}, {"key": "element", "label": headers[1]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_05_households_owners_of_factors(rng: random.Random, mode: str) -> Dict[str, Any]:
    wages = rng.choice([14500, 16200, 18400, 15800])
    rent = rng.choice([3200, 4100, 3800, 4500])
    interest = rng.choice([650, 820, 940, 750])
    profit = rng.choice([2400, 3100, 2900, 3600])
    total = wages + rent + interest + profit
    prompt = (
        f"In a month, the Dlamini household earns:\n"
        f"- Wages from factory employment: {fmt_zar(wages)}\n"
        f"- Rental income from a backyard workshop: {fmt_zar(rent)}\n"
        f"- Interest on fixed savings: {fmt_zar(interest)}\n"
        f"- Profit share from a weekend baking business: {fmt_zar(profit)}\n\n"
        f"(a) Calculate the household's total monthly **factor income**.\n"
        f"(b) Identify the **four factors of production** households own that generated these four payments."
    )
    ans = f"Total factor income = {fmt_zar(total)}; Factors: Labour (wages), Natural resources/Land (rent), Capital (interest), Entrepreneurship (profit)"
    sol = (
        f"**(a) Total Factor Income:**\n"
        f"${fmt_zar(wages)} + {fmt_zar(rent)} + {fmt_zar(interest)} + {fmt_zar(profit)} = {fmt_zar(total)}$\n\n"
        f"**(b) Four Factors of Production:**\n"
        f"- **Labour** $\\rightarrow$ Wages\n"
        f"- **Natural resources / Land** $\\rightarrow$ Rent\n"
        f"- **Capital** $\\rightarrow$ Interest\n"
        f"- **Entrepreneurship** $\\rightarrow$ Profit"
    )
    return make_question(
        rng=rng,
        subskill="05_households_owners_of_factors",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate total factor income {fmt_zar(total)}", "marks": 1, "type": "A"},
            {"step": "Name all four factors of production accurately (1 mark each)", "marks": 4, "type": "A"},
        ],
        marking_guide="1 mark for accurate sum; 4 marks for matching all four factors of production.",
        hints={
            "tier_1": "Add all four income streams together.",
            "tier_2": "Match wages, rent, interest and profit to labour, natural resources, capital and entrepreneurship.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_businesses_own_factors_originally"],
    )


def _build_06_four_factor_remunerations_matching(rng: random.Random, mode: str) -> Dict[str, Any]:
    rows = [
        ("Natural resources (Land)", "Rent", "Farmland or mining rights leased out"),
        ("Labour", "Wages / Salaries", "Mechanics and teachers working 40 hours"),
        ("Capital", "Interest", "Money and machinery financed for expansion"),
        ("Entrepreneurship", "Profit", "Owner coordinating inputs and bearing risk"),
    ]
    picked = rng.sample(rows, 3)
    headers = ["Factor of Production", "Remuneration (Income)", "Practical Example"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Factor of Production | Remuneration (Income) | Practical Example |", "|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        blank_col = rng.choice([0, 1])
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx == blank_col
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Link each factor of production to its exact money remuneration."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="06_four_factor_remunerations_matching",
        question_type="table_completion",
        prompt="Complete the Factor of Production Remuneration table by filling in each missing factor or payment.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Factor Remuneration Matrix:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per matched factor or remuneration.",
        hints={
            "tier_1": "Recall the four pairs: Land-Rent, Labour-Wages, Capital-Interest, Entrepreneurship-Profit.",
            "tier_2": "Use the practical example column to verify your pairing.",
            "tier_3": md_table,
        },
        misconception_tags=["swaps_interest_and_profit"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "factor", "label": headers[0]}, {"key": "pay", "label": headers[1]}, {"key": "ex", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_07_businesses_producers_and_employers(rng: random.Random, mode: str) -> Dict[str, Any]:
    firms = [
        ("a Polokwane furniture factory", "timber, carpenters, saws and factory management", "wooden school desks and kitchen cupboards"),
        ("a Gqeberha dairy processor", "raw farm milk, delivery drivers, pasteurisers and supervisors", "bottled milk, yoghurt and cheddar cheese"),
        ("a Soweto bakery co-operative", "flour, ovens, bakers and store premises", "wholewheat loaves and vetkoek"),
        ("a Durban garment workshop", "cotton fabric, machinists, sewing machines and designers", "school blazers and sports shirts"),
    ]
    firm, inputs, outputs = rng.choice(firms)
    distractors = [
        "collects PAYE taxes directly for parliament and passes criminal statutes",
        "owns all household family members permanently without paying wages",
        "prints national banknotes independently whenever profits fall",
    ]
    correct = f"hires {inputs} in the factor market and sells {outputs} in the goods market"
    prompt = f"How does **{firm}** operate in **both** markets of the circular flow?"
    sol = (
        f"- **Dual Role of Businesses:** In the factor market, {firm} is a **buyer** hiring {inputs} (paying wages, rent, interest and profit).\n"
        f"- In the goods & services market, it is a **seller** supplying {outputs} to earn sales revenue."
    )
    return make_question(
        rng=rng,
        subskill="07_businesses_producers_and_employers",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct.capitalize(),
        sample_answer=correct.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify buyer role in factor market + seller role in goods market", "marks": 2, "type": "A"}],
        marking_guide="2 marks for dual role across both markets.",
        hints={
            "tier_1": "Notice that a business must obtain inputs before it can sell products.",
            "tier_2": "Businesses buy factors of production and sell finished goods/services.",
            "tier_3": correct.capitalize(),
        },
        misconception_tags=["thinks_businesses_only_act_as_sellers_in_both_markets"],
        options=[correct.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_08_factor_market_exchange_mechanics(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("skilled electricians", "Thabo & Partners Electrical", 28500, "wages"),
        ("agricultural warehouse land", "Highveld Grain Mills", 19000, "rent"),
        ("production machinery loans", "Karoo Packaging Ltd", 12400, "interest"),
        ("factory supervisors & assemblers", "Tshwane Auto Parts", 42000, "salaries and wages"),
    ]
    factor, firm, payout, pay_type = rng.choice(cases)
    hh_count = rng.choice([2, 3, 4])
    per_hh = round(payout / hh_count, 2)
    prompt = (
        f"In the **factor (resource) market**, {hh_count} local households supply {factor} to **{firm}**, "
        f"which pays a combined monthly total of {fmt_zar(payout)} in {pay_type}.\n\n"
        f"(a) Identify who is the **seller** and who is the **buyer** in this factor-market transaction.\n"
        f"(b) Calculate the average monthly factor income received per household."
    )
    ans = f"Sellers: households; Buyer: {firm}; Average income = {fmt_zar(per_hh)}"
    sol = (
        f"**(a) Market Roles:**\n"
        f"- **Sellers:** Households (supplying {factor}).\n"
        f"- **Buyer:** {firm} (hiring factors of production).\n\n"
        f"**(b) Per-Household Payment:** $\\frac{{{fmt_zar(payout)}}}{{{hh_count}}} = {fmt_zar(per_hh)}$ per household."
    )
    return make_question(
        rng=rng,
        subskill="08_factor_market_exchange_mechanics",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Correctly label households as sellers and firm as buyer", "marks": 2, "type": "A"},
            {"step": f"Calculate average {fmt_zar(per_hh)}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for seller/buyer roles; 2 marks for accurate division.",
        hints={
            "tier_1": "Remember: households own factors of production, so they supply/sell them here.",
            "tier_2": f"Divide total payout {fmt_zar(payout)} by {hh_count} households.",
            "tier_3": ans,
        },
        misconception_tags=["calls_businesses_the_sellers_in_factor_market"],
    )


def _build_09_goods_and_services_market_exchange(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("fresh bread and milk", "township households", "uMzinyathi Mini-Market", 18, 240),
        ("school exercise books and pens", "parents and learners", "Pietermaritzburg Stationers", 35, 160),
        ("haircuts and grooming services", "local residents", "Khayelitsha Style Studio", 85, 90),
        ("solar study lamps", "rural families", "Vhembe Solar Outlet", 140, 75),
    ]
    good, buyers, seller, unit_p, qty = rng.choice(cases)
    revenue = unit_p * qty
    prompt = (
        f"In the **goods and services market**, {buyers} buy {qty} units of {good} at {fmt_zar(unit_p)} each from **{seller}**.\n\n"
        f"(a) Calculate the money flow (sales revenue) received by {seller}.\n"
        f"(b) Identify the **real flow** and the **money flow** in this exchange."
    )
    ans = f"Revenue = {fmt_zar(revenue)}; Real flow: {good} moving from {seller} to {buyers}; Money flow: {fmt_zar(revenue)} paid by {buyers} to {seller}"
    sol = (
        f"**(a) Sales Revenue (Money Flow):** ${qty} \\times {fmt_zar(unit_p)} = {fmt_zar(revenue)}$\n"
        f"**(b) Opposite Flows:**\n"
        f"- **Real flow:** {good.capitalize()} flowing from **{seller}** $\\rightarrow$ **{buyers}**.\n"
        f"- **Money flow:** {fmt_zar(revenue)} flowing from **{buyers}** $\\rightarrow$ **{seller}**."
    )
    return make_question(
        rng=rng,
        subskill="09_goods_and_services_market_exchange",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate revenue {fmt_zar(revenue)}", "marks": 2, "type": "A"},
            {"step": "Correctly state both real flow and money flow directions", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for revenue multiplication; 2 marks for real vs money flow direction.",
        hints={
            "tier_1": "Multiply quantity sold by unit price.",
            "tier_2": "Physical goods go from business to consumer; Rand payment goes from consumer to business.",
            "tier_3": ans,
        },
        misconception_tags=["reverses_real_and_money_flow_directions"],
    )


def _build_10_real_flow_definition_examples(rng: random.Random, mode: str) -> Dict[str, Any]:
    pool = [
        ("farm workers harvesting oranges + supermarkets handing groceries to shoppers + municipal clinics treating patients", "physical movement of factors of production, finished goods and public services between participants"),
        ("timber deliveries entering a sawmill + finished chairs sold to families + police patrols safeguarding streets", "flow of actual labour, raw materials, finished products and public services"),
        ("nurses staffing hospitals + bakeries delivering bread loaves + builders erecting classrooms", "non-monetary circulation of productive inputs and real goods and services"),
        ("engineers operating machines + farmers supplying maize + municipalities supplying piped drinking water", "tangible resources, products and services moving around the economy"),
    ]
    examples, meaning = rng.choice(pool)
    distractors = [
        "monthly electronic salary transfers, VAT payments and pension payouts in Rand",
        "only gold coins minted by commercial banks for international shipping",
        "solely the calculation of corporate income tax returns by accountants",
    ]
    prompt = f"Which statement correctly describes the **real flow** in the circular flow, such as *{examples}*?"
    sol = f"- **Real Flow:** {meaning.capitalize()} (no Rand banknotes/bank transfers are counted inside the real flow itself)."
    return make_question(
        rng=rng,
        subskill="10_real_flow_definition_examples",
        question_type="mcq",
        prompt=prompt,
        correct_answer=meaning.capitalize(),
        sample_answer=meaning.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify real flow as physical inputs, goods and services", "marks": 2, "type": "A"}],
        marking_guide="2 marks for selecting physical resource/product/service flow.",
        hints={
            "tier_1": "Contrast physical goods/services and work against Rand payments.",
            "tier_2": "Real flow consists of inputs (FoP) and outputs (goods & services).",
            "tier_3": meaning.capitalize(),
        },
        misconception_tags=["includes_wages_and_taxes_as_real_flows"],
        options=[meaning.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_11_money_flow_definition_examples(rng: random.Random, mode: str) -> Dict[str, Any]:
    payments = [
        ("R18 500 monthly salaries + R1 400 supermarket till payments + R2 600 PAYE income tax", "wages, consumer spending and direct taxes (all Rand income/expenditure flows)"),
        ("R45 000 factory rent + R12 000 social grant payouts + R90 000 municipal road tender", "factor remuneration, government transfers and public contract expenditure"),
        ("R8 500 interest on business loans + R620 VAT receipts + R15 000 entrepreneur profit", "factor payments and indirect tax payments circulating in monetary form"),
        ("R32 000 household grocery spending + R4 800 company tax + R22 000 nurse salaries", "monetary payments circulating in the opposite direction to real goods and services"),
    ]
    tx_list, desc = rng.choice(payments)
    prompt = (
        f"Observe these circular-flow transactions: *{tx_list}.*\n\n"
        f"(a) Classify all of these under **real flow** or **money flow**.\n"
        f"(b) Explain why they fall into that category and name ONE participant receiving each type of payment."
    )
    ans = f"Money flow ({desc}); wages/grants go to households, till spending goes to businesses, taxes go to government"
    sol = (
        f"**(a) Classification:** **Money flow**.\n"
        f"**(b) Explanation:** Every listed item represents monetary income, expenditure or tax receipts ({desc}) rather than physical goods or labour."
    )
    return make_question(
        rng=rng,
        subskill="11_money_flow_definition_examples",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Classify as Money flow", "marks": 1, "type": "A"},
            {"step": "Explain Rand/monetary medium + give recipients", "marks": 3, "type": "A"},
        ],
        marking_guide="1 mark for Money flow; 3 marks for clear monetary justification and participant recipients.",
        hints={
            "tier_1": "Ask whether these flows measure physical work/goods or Rand amounts paid.",
            "tier_2": "All Rand payments—wages, rent, retail spending, taxes, grants—belong to the money flow.",
            "tier_3": ans,
        },
        misconception_tags=["calls_tax_and_wage_payments_real_flows"],
    )


def _build_12_real_vs_money_flow_direction_matrix(rng: random.Random, mode: str) -> Dict[str, Any]:
    bank = [
        ("Household workers travel to work at a factory", "Households", "Businesses", "Real flow"),
        ("Factory pays monthly salaries to workers", "Businesses", "Households", "Money flow"),
        ("Households pay Rand for groceries at checkout", "Households", "Businesses", "Money flow"),
        ("Supermarket delivers bread and milk to families", "Businesses", "Households", "Real flow"),
        ("Government pays social grants to pensioners", "Government", "Households", "Money flow"),
        ("Government operates free primary schools & clinics", "Government", "Households", "Real flow"),
    ]
    picked = rng.sample(bank, 3)
    headers = ["Transaction", "From", "To", "Flow Type"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Transaction | From | To | Flow Type |", "|---|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_cols = rng.sample([1, 2, 3], 2)
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx in req_cols
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Trace who gives what, and distinguish physical goods/work (Real) from Rand (Money)."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="12_real_vs_money_flow_direction_matrix",
        question_type="table_completion",
        prompt="Complete the missing origin ('From'), destination ('To'), or Flow Type ('Real flow' / 'Money flow') cells.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Completed Flow Matrix:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per correctly filled cell.",
        hints={
            "tier_1": "Follow physical goods/labour vs Rand payments.",
            "tier_2": "Wages/grants/purchases in Rand = Money flow; labour/goods/public clinics = Real flow.",
            "tier_3": md_table,
        },
        misconception_tags=["reverses_from_and_to_for_wages_vs_labour"],
        table_payload={
            "headers": headers,
            "columns": [{"key": h.lower().replace(" ", "_"), "label": h} for h in headers],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_13_two_sector_closed_flow_diagram(rng: random.Random, mode: str) -> Dict[str, Any]:
    hh_lbl = rng.choice(["Workers & Families", "Local Consumers", "Resource Owners"])
    biz_lbl = rng.choice(["Shops & Factories", "Domestic Firms", "Producers"])
    income = rng.choice([450, 520, 640, 780, 860])
    diagram = svg_two_sector_flow(
        hh_lbl,
        biz_lbl,
        income,
        income,
        "Factors of Production (Labour, Land, Capital, Enterprise)",
        "Finished Goods & Services",
    )
    prompt = (
        f"Study the Two-Sector Closed Circular Flow schematic ({hh_lbl} and {biz_lbl}) where Businesses pay "
        f"{fmt_zar(income)} in monthly Factor Income and Households spend {fmt_zar(income)} in Consumer Spending.\n\n"
        f"(a) Identify the TWO markets shown connecting Households and Businesses.\n"
        f"(b) Distinguish between the solid green inner loop and the dashed blue outer loop.\n"
        f"(c) Explain why total Factor Income equals Consumer Spending ({fmt_zar(income)}) in this two-sector closed model."
    )
    ans = f"Markets: Factor Market and Goods & Services Market; Green = Real flow, Blue = Money flow; assumes households spend 100% of income with no savings/taxes/imports"
    sol = (
        f"**(a) Two Markets:** **Factor Market** and **Goods & Services Market**.\n"
        f"**(b) Loops:**\n"
        f"- **Solid Green Loop (Real flow):** Factors of production flow from Households to Businesses; finished goods & services flow from Businesses to Households.\n"
        f"- **Dashed Blue Loop (Money flow):** Factor Income ({fmt_zar(income)}) flows from Businesses to Households; Consumer Spending ({fmt_zar(income)}) flows from Households to Businesses.\n"
        f"**(c) Income = Spending Identity:** The basic closed model assumes households spend all earned income and save nothing, with no leakages."
    )
    return make_question(
        rng=rng,
        subskill="13_two_sector_closed_flow_diagram",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": "Name Factor Market and Goods & Services Market", "marks": 2, "type": "A"},
            {"step": "Differentiate Real flow vs Money flow correctly", "marks": 2, "type": "A"},
            {"step": "Explain all income spent / zero savings leakage assumption", "marks": 1, "type": "A"},
        ],
        marking_guide="2 marks for markets; 2 marks for loop types; 1 mark for zero-savings equality reason.",
        hints={
            "tier_1": "Look at the top and bottom yellow boxes and the solid vs dashed arrows.",
            "tier_2": "Green carries physical resources and products; blue dashed carries Rand.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_inner_real_loop_with_money_loop"],
        diagram_spec=diagram,
    )


def _build_14_household_income_expenditure_identity(rng: random.Random, mode: str) -> Dict[str, Any]:
    wages = rng.choice([240, 280, 310, 350])
    rent = rng.choice([60, 75, 85, 90])
    interest = rng.choice([25, 35, 40, 50])
    profit = rng.choice([55, 65, 70, 80])
    total_y = wages + rent + interest + profit
    prompt = (
        f"In a simplified closed two-sector economy (no government, no savings, no foreign trade), "
        f"businesses pay households R{wages} million in wages, R{rent} million in rent, "
        f"R{interest} million in interest, and R{profit} million in profits.\n\n"
        f"(a) Calculate total household factor income.\n"
        f"(b) State the exact total business sales revenue in the goods & services market and justify your answer."
    )
    ans = f"Total factor income = R{total_y} million; Business sales revenue = R{total_y} million because all household income is spent"
    sol = (
        f"**(a) Total Factor Income:** $\\text{{R}}{wages} + \\text{{R}}{rent} + \\text{{R}}{interest} + \\text{{R}}{profit} = \\text{{R}}{total_y}\\text{{ million}}$\n"
        f"**(b) Sales Revenue:** **R{total_y} million**, because in a two-sector closed model without savings or taxes, 100% of household income returns as consumer expenditure."
    )
    return make_question(
        rng=rng,
        subskill="14_household_income_expenditure_identity",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Sum total factor income R{total_y} million", "marks": 2, "type": "A"},
            {"step": f"Deduce revenue R{total_y} million + closed-assumption reason", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for sum; 2 marks for equality deduction and explanation.",
        hints={
            "tier_1": "Add wages, rent, interest and profit first.",
            "tier_2": "Remember that closed two-sector models assume zero savings.",
            "tier_3": ans,
        },
        misconception_tags=["omits_profit_or_interest_from_factor_income"],
    )


def _build_15_government_role_as_participant(rng: random.Random, mode: str) -> Dict[str, Any]:
    angles = [
        ("Parliament collects tax revenue, hires nurses/teachers, buys uniforms/textbooks, and runs public clinics", "both a tax collector/redistributor and a major buyer in the factor & goods markets and supplier of public services"),
        ("The public sector employs civil servants, awards building tenders, pays grants, and charges VAT", "central participant interacting simultaneously with households, businesses and both markets"),
        ("Municipalities and national ministries gather rates/taxes to fund roads, policing and indigent pensions", "tax-collecting authority providing non-market public services and social transfers"),
        ("SARS collects direct & indirect tax so government can pay salaries, subsidies and public-infrastructure contracts", "collector of taxes and provider of public goods, salaries and transfers"),
    ]
    clue, role_desc = rng.choice(angles)
    prompt = (
        f"In the three-sector circular flow, government occupies the centre because *{clue}.*\n\n"
        f"State **THREE** distinct ways government participates in flows with Households and Businesses."
    )
    ans = f"1) Collects direct & indirect taxes; 2) Buys labour (factor market) and supplies/contracts goods (goods market); 3) Supplies public services, subsidies and social grants ({role_desc})"
    sol = (
        f"**Three distinct circular-flow functions of Government:**\n"
        f"1. **Taxation (Money inflow):** Collects direct income/corporate taxes and indirect taxes (VAT, excise) from households and firms.\n"
        f"2. **Market Purchases (Money outflow / Real inflow):** Hires civil servants in the factor market and buys supplies/tenders from firms in the goods market.\n"
        f"3. **Public Provision & Transfers:** Supplies public goods/services (clinics, roads, schools) plus social grants and subsidies."
    )
    return make_question(
        rng=rng,
        subskill="15_government_role_as_participant",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=6,
        marking_schema=[
            {"step": "Tax collection from households and businesses", "marks": 2, "type": "A"},
            {"step": "Hiring factors & buying goods/tenders", "marks": 2, "type": "A"},
            {"step": "Providing public services, grants & subsidies", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for each of three distinct circular-flow functions.",
        hints={
            "tier_1": "Think of money coming INTO government, money going OUT of government, and public services supplied.",
            "tier_2": "Cover taxation, factor/goods hiring, and public goods/grants.",
            "tier_3": ans,
        },
        misconception_tags=["treats_government_strictly_as_tax_taker_giving_nothing_back"],
    )


def _build_16_government_factor_market_hiring(rng: random.Random, mode: str) -> Dict[str, Any]:
    depts = [
        ("public hospital", 45, 32000, "nurses and doctors"),
        ("provincial high school", 32, 28500, "teachers"),
        ("municipal engineering unit", 25, 24000, "water technicians"),
        ("district police station", 40, 26000, "police officers"),
    ]
    inst, staff_n, avg_sal, roles = rng.choice(depts)
    payroll = staff_n * avg_sal
    prompt = (
        f"To run a {inst}, government hires {staff_n} {roles} at an average monthly salary of {fmt_zar(avg_sal)}.\n\n"
        f"(a) Calculate the total monthly salary bill.\n"
        f"(b) Identify which **market** this hiring takes place in and trace the directions of both the real flow and the money flow."
    )
    ans = f"Monthly payroll = {fmt_zar(payroll)}; Factor market; Real flow: labour from households to government; Money flow: {fmt_zar(payroll)} from government to households"
    sol = (
        f"**(a) Monthly Salary Bill:** ${staff_n} \\times {fmt_zar(avg_sal)} = {fmt_zar(payroll)}$\n"
        f"**(b) Market & Flows:**\n"
        f"- **Market:** **Factor (resource) market**.\n"
        f"- **Real flow:** {roles.capitalize()} (labour) move from **Households $\\rightarrow$ Government**.\n"
        f"- **Money flow:** Salaries ({fmt_zar(payroll)}) move from **Government $\\rightarrow$ Households**."
    )
    return make_question(
        rng=rng,
        subskill="16_government_factor_market_hiring",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate payroll {fmt_zar(payroll)}", "marks": 2, "type": "A"},
            {"step": "Identify Factor market", "marks": 1, "type": "A"},
            {"step": "Trace Real flow (labour) vs Money flow (salaries)", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for payroll calc; 1 mark for Factor market; 2 marks for flow directions.",
        hints={
            "tier_1": "Multiply staff count by average salary.",
            "tier_2": "Public servants supply labour through the factor market just like private workers.",
            "tier_3": ans,
        },
        misconception_tags=["places_civil_service_hiring_in_goods_market"],
    )


def _build_17_government_goods_market_procurement(rng: random.Random, mode: str) -> Dict[str, Any]:
    orders = [
        ("grade 9 mathematics textbooks from a local printer", 600, 145),
        ("solar backup lamps for rural clinics", 180, 450),
        ("protective boots for municipal road crews", 320, 380),
        ("student desks from a local furniture manufacturer", 250, 620),
    ]
    item, qty, unit_p = rng.choice(orders)
    total_cost = qty * unit_p
    prompt = (
        f"Government buys {qty} {item} at {fmt_zar(unit_p)} per unit.\n\n"
        f"(a) Calculate the total government expenditure.\n"
        f"(b) Identify the market where this procurement happens and state which participant receives the payment."
    )
    ans = f"Expenditure = {fmt_zar(total_cost)}; Goods and services market; Businesses receive the payment"
    sol = (
        f"**(a) Procurement Cost:** ${qty} \\times {fmt_zar(unit_p)} = {fmt_zar(total_cost)}$\n"
        f"**(b) Market & Recipient:** Occurs in the **goods and services market**, where **businesses** supply physical goods (real flow) and receive {fmt_zar(total_cost)} in revenue (money flow)."
    )
    return make_question(
        rng=rng,
        subskill="17_government_goods_market_procurement",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate cost {fmt_zar(total_cost)}", "marks": 2, "type": "A"},
            {"step": "Identify Goods & services market + Businesses as recipient", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for cost arithmetic; 2 marks for market and recipient.",
        hints={
            "tier_1": "Multiply units ordered by price per unit.",
            "tier_2": "Finished items like textbooks and desks trade in the goods & services market.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_finished_equipment_purchase_with_factor_market"],
    )


def _build_18_public_goods_and_services_flow(rng: random.Random, mode: str) -> Dict[str, Any]:
    services = [
        ("public schools, primary healthcare clinics and community policing", "households (and businesses via a healthy, educated workforce and safe trading environment)"),
        ("paved national highways, harbours and commercial courts", "businesses (lowering transport and contract-enforcement costs) and households"),
        ("clean municipal water supply, street lighting and fire brigades", "both households and local shops through essential daily infrastructure"),
        ("agricultural extension advice, veterinary clinics and rural bridges", "farming businesses and rural families"),
    ]
    public_svcs, beneficiaries = rng.choice(services)
    distractors = [
        "They are money flows because taxpayers withdraw banknotes directly from clinics.",
        "They exist only in open foreign markets outside national borders.",
        "They move from households back to businesses as raw natural resources.",
    ]
    correct = f"Real flows supplied by government to {beneficiaries}, financed by tax revenues"
    prompt = f"How should **{public_svcs}** be classified inside the circular flow model?"
    sol = f"- **Classification:** {correct}.\n- Even though funded by money taxes, the clinics, schools, highways and policing themselves are **real flows** of services."
    return make_question(
        rng=rng,
        subskill="18_public_goods_and_services_flow",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct,
        sample_answer=correct,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Classify public services as government real flows", "marks": 2, "type": "A"}],
        marking_guide="2 marks for classifying public services as real flows from government.",
        hints={
            "tier_1": "Schools, roads and policing are services rather than Rand payouts.",
            "tier_2": "Public services form a real flow from Government to Households and Businesses.",
            "tier_3": correct,
        },
        misconception_tags=["labels_public_hospitals_as_money_flow_because_taxes_pay_for_them"],
        options=[correct] + distractors,
        duration_mins=2,
    )


def _build_19_direct_taxes_salaries_profits(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        (360000, 18, 500000, 27),
        (420000, 20, 600000, 27),
        (280000, 15, 400000, 27),
        (500000, 22, 800000, 27),
    ]
    sal, sal_r, biz_prof, corp_r = rng.choice(cases)
    sal_tax = sal * sal_r / 100.0
    corp_tax = biz_prof * corp_r / 100.0
    tot_direct = sal_tax + corp_tax
    prompt = (
        f"Consider two **direct taxes** paid straight to government revenue services:\n"
        f"- An engineer earns an annual salary of {fmt_zar(sal)} taxed at an effective PAYE rate of {sal_r}%.\n"
        f"- A small manufacturing company earns net profit of {fmt_zar(biz_prof)} taxed at the {corp_r}% corporate rate.\n\n"
        f"(a) Calculate the total direct tax collected from both taxpayers.\n"
        f"(b) Explain why both taxes are classified as **direct** taxes."
    )
    ans = f"PAYE: {fmt_zar(sal_tax)} + Corporate tax: {fmt_zar(corp_tax)} = {fmt_zar(tot_direct)}; levied directly on the income/profit of the person or firm bearing the tax"
    sol = (
        f"**(a) Direct Tax Calculation:**\n"
        f"- Individual PAYE $= {fmt_zar(sal)} \\times {sal_r}\\% = {fmt_zar(sal_tax)}$\n"
        f"- Corporate tax $= {fmt_zar(biz_prof)} \\times {corp_r}\\% = {fmt_zar(corp_tax)}$\n"
        f"- Combined direct tax $= {fmt_zar(tot_direct)}$\n\n"
        f"**(b) Direct Tax Definition:** Charged directly on the income or profits of individuals and businesses, who pay the tax burden directly rather than shifting it onto retail prices."
    )
    return make_question(
        rng=rng,
        subskill="19_direct_taxes_salaries_profits",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate PAYE {fmt_zar(sal_tax)} and corporate tax {fmt_zar(corp_tax)}", "marks": 2, "type": "A"},
            {"step": f"Sum total direct tax {fmt_zar(tot_direct)}", "marks": 1, "type": "CA"},
            {"step": "Explain direct incidence on income/profit", "marks": 2, "type": "A"},
        ],
        marking_guide="3 marks for tax calculations; 2 marks for direct-tax explanation.",
        hints={
            "tier_1": "Multiply salary by PAYE % and profit by corporate %, then add.",
            "tier_2": "Direct taxes target income/profit directly rather than retail sales.",
            "tier_3": ans,
        },
        misconception_tags=["treats_company_tax_as_indirect_tax"],
    )


def _build_20_indirect_taxes_vat_excise(rng: random.Random, mode: str) -> Dict[str, Any]:
    items = [
        ("a microwave oven", 1600, 15),
        ("a pair of leather school shoes", 600, 15),
        ("a smartphone handset", 2800, 15),
        ("an electric kettle and toaster set", 900, 15),
        ("household furniture", 4400, 15),
    ]
    item, base_p, vat_r = rng.choice(items)
    vat_amt = base_p * vat_r / 100.0
    total_p = base_p + vat_amt
    prompt = (
        f"A shop prices {item} at {fmt_zar(base_p)} before **Value-Added Tax (VAT)** of {vat_r}%.\n\n"
        f"(a) Calculate the VAT amount and the final VAT-inclusive shelf price paid by the household.\n"
        f"(b) Explain why VAT is classified as an **indirect tax** in the circular flow."
    )
    ans = f"VAT = {fmt_zar(vat_amt)}; Final price = {fmt_zar(total_p)}; indirect because charged on goods/spending and collected via the retailer"
    sol = (
        f"**(a) VAT Calculation:**\n"
        f"- VAT $= {fmt_zar(base_p)} \\times \\frac{{{vat_r}}}{{100}} = {fmt_zar(vat_amt)}$\n"
        f"- Inclusive price $= {fmt_zar(base_p)} + {fmt_zar(vat_amt)} = {fmt_zar(total_p)}$\n\n"
        f"**(b) Why Indirect:** VAT is added onto consumer spending in the goods market—the business collects {fmt_zar(vat_amt)} from the shopper and remits it to government (SARS)."
    )
    return make_question(
        rng=rng,
        subskill="20_indirect_taxes_vat_excise",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate VAT {fmt_zar(vat_amt)} and total {fmt_zar(total_p)}", "marks": 2, "type": "A"},
            {"step": "Explain spending basis + retailer intermediary collection", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for VAT + total calculation; 2 marks for indirect-tax mechanism.",
        hints={
            "tier_1": "Find 15% of the pre-VAT price and add it.",
            "tier_2": "Indirect taxes fall on goods/services spending and pass through retailers to government.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_15_percent_instead_of_adding_vat"],
    )


def _build_21_direct_vs_indirect_tax_classification(rng: random.Random, mode: str) -> Dict[str, Any]:
    bank = [
        ("Personal Income Tax (PAYE)", "Direct tax", "Individuals (Households)", "Salary / wage income"),
        ("Corporate / Company Tax", "Direct tax", "Businesses", "Annual business profit"),
        ("Value-Added Tax (15% VAT)", "Indirect tax", "Consumers via Retailers", "Spending on goods & services"),
        ("Fuel Levy", "Indirect tax", "Motorists via Petrol Stations", "Litres of petrol/diesel bought"),
        ("Excise (Sin) Tax on tobacco", "Indirect tax", "Consumers via Producers", "Units sold"),
    ]
    picked = rng.sample(bank, 3)
    headers = ["Tax Name", "Tax Type", "Who Pays / Remits", "Tax Base"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Tax Name | Tax Type | Who Pays / Remits | Tax Base |", "|---|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        blank_col = rng.choice([1, 3])
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx == blank_col
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Direct taxes apply to income/profit; Indirect taxes apply to consumption/units."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="21_direct_vs_indirect_tax_classification",
        question_type="table_completion",
        prompt="Classify each South African tax in the table as a Direct tax or Indirect tax and specify its tax base.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Tax Classification Summary:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each correct classification or tax base.",
        hints={
            "tier_1": "Direct = income/profit; Indirect = spending on goods/fuel/excisable items.",
            "tier_2": "VAT and Fuel Levy pass through sellers onto consumer spending.",
            "tier_3": md_table,
        },
        misconception_tags=["classifies_vat_as_direct_tax"],
        table_payload={
            "headers": headers,
            "columns": [{"key": h.lower().replace(" ", "_"), "label": h} for h in headers],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_22_government_transfers_social_grants(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        (40, 2180, "old-age pensions"),
        (120, 530, "child support grants"),
        (55, 2180, "disability grants"),
        (80, 1060, "double child-grant households"),
    ]
    households_n, payout_each, label = rng.choice(cases)
    tot_transfer = households_n * payout_each
    spent_pct = rng.choice([85, 90, 95])
    local_retail = round(tot_transfer * spent_pct / 100.0)
    prompt = (
        f"In a rural ward, government pays monthly {label} of {fmt_zar(payout_each)} to {households_n} households.\n\n"
        f"(a) Calculate the total monthly government **transfer payment**.\n"
        f"(b) If recipients spend {spent_pct}% of those grants on food and clothing locally, calculate how much money flows directly to local businesses in the goods market."
    )
    ans = f"Total transfer = {fmt_zar(tot_transfer)}; Flow to local businesses = {fmt_zar(local_retail)}"
    sol = (
        f"**(a) Total Grant Transfer (Government $\\rightarrow$ Households):**\n"
        f"${households_n} \\times {fmt_zar(payout_each)} = {fmt_zar(tot_transfer)}$\n\n"
        f"**(b) Goods-Market Circulation (Households $\\rightarrow$ Businesses):**\n"
        f"${fmt_zar(tot_transfer)} \\times {spent_pct}\\% = {fmt_zar(local_retail)}$"
    )
    return make_question(
        rng=rng,
        subskill="22_government_transfers_social_grants",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate transfer total {fmt_zar(tot_transfer)}", "marks": 2, "type": "A"},
            {"step": f"Calculate retail spending flow {fmt_zar(local_retail)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for total grant payout; 2 marks for percentage spent in local goods market.",
        hints={
            "tier_1": "Multiply grant value by number of households first.",
            "tier_2": f"Multiply total grant payout by {spent_pct}%.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_social_grants_reenter_goods_market_via_spending"],
    )


def _build_23_government_subsidies_and_tenders(rng: random.Random, mode: str) -> Dict[str, Any]:
    contracts = [
        ("school sanitation & classroom maintenance tender", 480000, 15, "Mbombela Builders Ltd"),
        ("provincial scholar-transport bus tender", 620000, 20, "Mthatha Fleet Services"),
        ("smallholder maize-seed subsidy & delivery contract", 350000, 25, "Free State Agri Supply"),
        ("municipal streetlight LED upgrade tender", 540000, 15, "Polokwane Grid Works"),
    ]
    tender_desc, value, sub_pct, contractor = rng.choice(contracts)
    retained_wage_share = round(value * sub_pct / 100.0)
    prompt = (
        f"Government awards a **{tender_desc}** worth {fmt_zar(value)} to **{contractor}**. "
        f"{contractor} spends {sub_pct}% of that contract amount directly on wages for local labourers.\n\n"
        f"(a) Calculate how much flows onward from {contractor} to local households via the **factor market**.\n"
        f"(b) Distinguish between a **government tender** and a **government subsidy** in flows between state and business."
    )
    ans = f"Wages to households = {fmt_zar(retained_wage_share)}; Tender buys contracted goods/services for the state, whereas subsidy lowers a firm's production costs without the state buying the output"
    sol = (
        f"**(a) Onward Factor Payment:** ${fmt_zar(value)} \\times {sub_pct}\\% = {fmt_zar(retained_wage_share)}$\n"
        f"**(b) Tender vs Subsidy:**\n"
        f"- **Government tender:** Competitive procurement contract where the state pays a business to supply goods/construction/services.\n"
        f"- **Subsidy:** Financial support paid to producers/industries to keep essential goods affordable or sustain production."
    )
    return make_question(
        rng=rng,
        subskill="23_government_subsidies_and_tenders",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate wage flow {fmt_zar(retained_wage_share)}", "marks": 2, "type": "A"},
            {"step": "Contrast tender vs subsidy accurately", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for wage calculation; 2 marks for accurate tender vs subsidy distinction.",
        hints={
            "tier_1": "Multiply tender value by the wage percentage.",
            "tier_2": "A tender purchases work for the state; a subsidy supports a firm's costs/prices.",
            "tier_3": ans,
        },
        misconception_tags=["treats_subsidy_and_tender_as_identical"],
    )


def _build_24_three_sector_circular_flow_diagram(rng: random.Random, mode: str) -> Dict[str, Any]:
    hh_tax = rng.choice([320, 350, 380, 410])
    biz_tax = rng.choice([210, 240, 260, 290])
    gov_grants = rng.choice([280, 310, 340, 360])
    gov_tenders = rng.choice([190, 220, 240, 270])
    hh_spend = rng.choice([1100, 1250, 1400, 1550])
    tot_tax = hh_tax + biz_tax
    tot_gov_out = gov_grants + gov_tenders
    net_fiscal = tot_tax - tot_gov_out
    diagram = svg_three_sector_flow(hh_tax, biz_tax, gov_grants, gov_tenders, hh_spend)
    prompt = (
        f"Analyse the Three-Sector Circular Flow values (in R billions): Household Taxes = R{hh_tax}bn, "
        f"Company Tax = R{biz_tax}bn, Government Grants & Services = R{gov_grants}bn, "
        f"Government Tenders & Subsidies = R{gov_tenders}bn, Consumer Spending = R{hh_spend}bn.\n\n"
        f"(a) Calculate **total government tax receipts** from Households and Businesses.\n"
        f"(b) Calculate **total government outlays** (grants/services + tenders/subsidies) and state whether tax receipts exceed outlays (fiscal surplus) or fall short (deficit)."
    )
    status = "surplus" if net_fiscal >= 0 else "deficit"
    ans = f"Tax receipts = R{tot_tax}bn; Outlays = R{tot_gov_out}bn; Budget {status} of R{abs(net_fiscal)}bn"
    sol = (
        f"**(a) Total Tax Receipts:** $\\text{{R}}{hh_tax}\\text{{bn}} + \\text{{R}}{biz_tax}\\text{{bn}} = \\text{{R}}{tot_tax}\\text{{bn}}$\n"
        f"**(b) Total Outlays & Fiscal Balance:**\n"
        f"- Outlays $= \\text{{R}}{gov_grants}\\text{{bn}} + \\text{{R}}{gov_tenders}\\text{{bn}} = \\text{{R}}{tot_gov_out}\\text{{bn}}$\n"
        f"- Balance $= \\text{{R}}{tot_tax}\\text{{bn}} - \\text{{R}}{tot_gov_out}\\text{{bn}} = {'+' if net_fiscal >= 0 else '-'}R{abs(net_fiscal)}\\text{{bn}}$ (fiscal **{status}**)."
    )
    return make_question(
        rng=rng,
        subskill="24_three_sector_circular_flow_diagram",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate tax receipts R{tot_tax}bn", "marks": 2, "type": "A"},
            {"step": f"Calculate outlays R{tot_gov_out}bn", "marks": 1, "type": "A"},
            {"step": f"Determine {status} of R{abs(net_fiscal)}bn", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for tax sum; 1 mark for outlays sum; 2 marks for surplus/deficit determination.",
        hints={
            "tier_1": "Add both red tax arrows entering Government, then add both black outlay arrows leaving Government.",
            "tier_2": "Subtract outlays from tax receipts to check for surplus or deficit.",
            "tier_3": ans,
        },
        misconception_tags=["includes_consumer_spending_in_government_tax_total"],
        diagram_spec=diagram,
    )


def _build_25_real_vs_money_opposite_directions(rng: random.Random, mode: str) -> Dict[str, Any]:
    pairs = [
        ("Households", "Businesses", "Capital & Labour", "Interest & Wages", rng.choice([620, 740, 880])),
        ("Households", "Businesses", "Maize Meal & Bread", "Consumer Spending", rng.choice([480, 560, 690])),
        ("Government", "Businesses", "Roads & Policing Services", "Company & VAT Taxes", rng.choice([310, 390, 440])),
    ]
    p1, p2, real_txt, money_txt, amt = rng.choice(pairs)
    diagram = svg_two_sector_flow("Workers & Consumers", "Local Enterprises", amt, amt, real_txt, "Finished Products")
    prompt = (
        f"Inspect the directional loops in the circular flow schematic (showing R{amt} in monetary flows alongside real flows such as {real_txt}).\n\n"
        f"Explain why **real flows** and **money flows** between participants like {p1} and {p2} always travel in **opposite directions**."
    )
    ans = "Every exchange swaps a real input or product in one direction in return for a Rand payment flowing back in the opposite direction"
    sol = (
        f"- **Opposite Directions Principle:** In every voluntary market exchange, one side hands over something **real** (e.g., {real_txt}) "
        f"while the other side sends **money** (e.g., {money_txt} = {fmt_zar(amt)}) back in payment.\n"
        f"- Thus real flows circulate in one direction around the economy while money flows circulate in the reverse direction."
    )
    return make_question(
        rng=rng,
        subskill="25_real_vs_money_opposite_directions",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[{"step": "Explain bilateral swap (real item vs Rand payment moving opposite ways)", "marks": 3, "type": "A"}],
        marking_guide="3 marks for clear bilateral exchange explanation.",
        hints={
            "tier_1": "Trace one hand giving groceries/labour and the other hand receiving Rand.",
            "tier_2": "Compare the clockwise/counter-clockwise direction of green vs blue dashed arrows.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_real_and_money_flows_move_same_direction"],
        diagram_spec=diagram,
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_circular_flow_definition_purpose": _build_01_circular_flow_definition_purpose,
    "02_closed_economy_meaning": _build_02_closed_economy_meaning,
    "03_closed_economy_assumptions_vs_reality": _build_03_closed_economy_assumptions_vs_reality,
    "04_identifying_five_participants_and_markets": _build_04_identifying_five_participants_and_markets,
    "05_households_owners_of_factors": _build_05_households_owners_of_factors,
    "06_four_factor_remunerations_matching": _build_06_four_factor_remunerations_matching,
    "07_businesses_producers_and_employers": _build_07_businesses_producers_and_employers,
    "08_factor_market_exchange_mechanics": _build_08_factor_market_exchange_mechanics,
    "09_goods_and_services_market_exchange": _build_09_goods_and_services_market_exchange,
    "10_real_flow_definition_examples": _build_10_real_flow_definition_examples,
    "11_money_flow_definition_examples": _build_11_money_flow_definition_examples,
    "12_real_vs_money_flow_direction_matrix": _build_12_real_vs_money_flow_direction_matrix,
    "13_two_sector_closed_flow_diagram": _build_13_two_sector_closed_flow_diagram,
    "14_household_income_expenditure_identity": _build_14_household_income_expenditure_identity,
    "15_government_role_as_participant": _build_15_government_role_as_participant,
    "16_government_factor_market_hiring": _build_16_government_factor_market_hiring,
    "17_government_goods_market_procurement": _build_17_government_goods_market_procurement,
    "18_public_goods_and_services_flow": _build_18_public_goods_and_services_flow,
    "19_direct_taxes_salaries_profits": _build_19_direct_taxes_salaries_profits,
    "20_indirect_taxes_vat_excise": _build_20_indirect_taxes_vat_excise,
    "21_direct_vs_indirect_tax_classification": _build_21_direct_vs_indirect_tax_classification,
    "22_government_transfers_social_grants": _build_22_government_transfers_social_grants,
    "23_government_subsidies_and_tenders": _build_23_government_subsidies_and_tenders,
    "24_three_sector_circular_flow_diagram": _build_24_three_sector_circular_flow_diagram,
    "25_real_vs_money_opposite_directions": _build_25_real_vs_money_opposite_directions,
}
