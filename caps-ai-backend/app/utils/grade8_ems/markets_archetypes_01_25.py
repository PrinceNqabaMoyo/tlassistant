"""Grade 8 EMS — The Markets Archetypes 01–25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 4/02. The markets.md.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import AREAS, NAMES, SUPPLIERS, get_ems_scenario as _raw_ems_scenario

TOPIC_NAME = "The markets"
TOPIC_KEY = "grade8_ems_markets"
LO = "g8_ems_markets"
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
        "tier_1": "Ask who is buying, who is selling, and what is being traded (goods/services vs productive factors/money).",
        "tier_2": "Distinguish Goods & Services Markets (wholesale, retail, services) from Factor & Financial Markets.",
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
        "subtopic_id": "term4_markets",
        "grade": 8,
        "subject": "Economic and Management Sciences",
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT_PERCENT,
        "suggested_duration_mins": out.get("suggested_duration_mins", duration_mins),
        "subskill": subskill,
        "archetype": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": subskill,
        "concept_group": "the_markets",
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 4 > The Markets",
        "misconception_tags": misconception_tags or ["market_category_confusion"],
        "diagnostic_tags": ["markets", "economy", "grade8_ems"],
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
        "id": f"g8_ems_mk_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_mk_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_mk_{subskill}_{rng.randint(100000, 999999)}",
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
        "id": f"g8_ems_mk_{subskill}_{rng.randint(100000, 999999)}",
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


def svg_market_card(title: str, subtitle: str, rows: List[Tuple[str, str]]) -> str:
    """Render a crisp Paper & Ink economics market data card SVG."""
    row_h = 24
    h = 78 + len(rows) * row_h
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 {h}" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">',
        f'<rect x="4" y="4" width="532" height="{h - 8}" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>',
        '<rect x="4" y="4" width="532" height="44" rx="8" fill="#0F766E"/>',
        '<rect x="4" y="34" width="532" height="14" fill="#0F766E"/>',
        f'<text x="20" y="24" font-size="13" font-weight="bold" fill="#FFFFFF">{_xml_escape(title)}</text>',
        f'<text x="20" y="40" font-size="10" fill="#CCFBF1">{_xml_escape(subtitle)}</text>',
    ]
    for i, (lbl, val) in enumerate(rows):
        y = 70 + i * row_h
        bg = "#F8FAFC" if i % 2 == 0 else "#FFFFFF"
        lines.append(f'<rect x="14" y="{y - 15}" width="512" height="22" fill="{bg}" rx="3"/>')
        lines.append(f'<text x="22" y="{y}" font-size="12" fill="#1E293B">{_xml_escape(lbl)}</text>')
        lines.append(f'<text x="516" y="{y}" font-size="12" font-weight="bold" text-anchor="end" fill="#0F172A">{_xml_escape(val)}</text>')
    lines.append("</svg>")
    return "".join(lines)


def svg_circular_markets(area: str, biz: str, spend_amt: str, factor_amt: str) -> str:
    """Render Paper & Ink Circular Flow across Goods & Services Market and Factor Market."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 190" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">'
        '<rect x="4" y="4" width="532" height="182" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>'
        '<rect x="180" y="14" width="180" height="36" rx="6" fill="#DBEAFE" stroke="#1D4ED8" stroke-width="1.4"/>'
        f'<text x="270" y="30" font-size="11" font-weight="bold" text-anchor="middle" fill="#1E3A8A">Goods &amp; Services Market</text>'
        f'<text x="270" y="44" font-size="10" text-anchor="middle" fill="#1E40AF">Consumer Spending: {_xml_escape(spend_amt)}</text>'
        '<rect x="180" y="140" width="180" height="36" rx="6" fill="#FEF3C7" stroke="#B45309" stroke-width="1.4"/>'
        '<text x="270" y="156" font-size="11" font-weight="bold" text-anchor="middle" fill="#92400E">Factor Market</text>'
        f'<text x="270" y="170" font-size="10" text-anchor="middle" fill="#78350F">Wages/Rent/Interest: {_xml_escape(factor_amt)}</text>'
        '<rect x="16" y="72" width="142" height="48" rx="6" fill="#ECFDF5" stroke="#047857" stroke-width="1.5"/>'
        '<text x="87" y="93" font-size="11" font-weight="bold" text-anchor="middle" fill="#065F46">Households</text>'
        f'<text x="87" y="109" font-size="9.5" text-anchor="middle" fill="#334155">{_xml_escape(area)}</text>'
        '<rect x="382" y="72" width="142" height="48" rx="6" fill="#13519C"/>'
        f'<text x="453" y="93" font-size="11" font-weight="bold" text-anchor="middle" fill="#FFFFFF">{_xml_escape(biz[:18])}</text>'
        '<text x="453" y="109" font-size="9.5" text-anchor="middle" fill="#DBEAFE">Businesses</text>'
        '<path d="M 87 70 L 87 32 L 178 32" fill="none" stroke="#0F766E" stroke-width="2"/>'
        '<path d="M 362 32 L 453 32 L 453 70" fill="none" stroke="#0F766E" stroke-width="2"/>'
        '<path d="M 453 122 L 453 158 L 362 158" fill="none" stroke="#B45309" stroke-width="2"/>'
        '<path d="M 178 158 L 87 158 L 87 122" fill="none" stroke="#B45309" stroke-width="2"/>'
        '</svg>'
    )


# =============================================================================
# ARCHETYPES 01 – 25
# =============================================================================

def _b01_market_definition_non_physical(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 75) * 10
    prompt = (
        f"{s['entrepreneur']} in {s['area']} buys {s['item_sold']} over a telephone call from {s['supplier']} for {fmt_r(amt)} without ever visiting a physical shop. "
        f"Why does this telephone transaction STILL count as a market?"
    )
    ans = "Because a market is any arrangement or platform where buyers and sellers interact (physically or remotely) to exchange goods/services at agreed prices"
    opts = [
        "Because a market is any arrangement or platform where buyers and sellers interact (physically or remotely) to exchange goods/services at agreed prices",
        "Because only wholesalers require physical market stalls",
        "Because telephone purchases count as free public goods",
        "Because commercial banks create a market only when coins change hands",
    ]
    exp = f"In economics, a market is NOT limited to physical buildings: any contact (telephone, online, face-to-face) between buyer ({s['entrepreneur']}) and seller ({s['supplier']}) at an agreed price ({fmt_r(amt)}) forms a market."
    return _make_mcq(
        rng,
        subskill="01_market_definition_non_physical",
        title="Economic Definition of a Market",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Must a market have physical walls and open-air stalls?",
            "tier_2": "A market exists whenever buyers and sellers communicate to agree on price and exchange.",
            "tier_3": ans,
        },
        misconception_tags=["equates_market_solely_with_physical_venue"],
        question_family_id="market_definition",
    )


def _b02_physical_vs_virtual_online_markets(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 18) * 100
    is_virtual = rng.choice([True, False])
    if is_virtual:
        prompt = (
            f"A customer in {s['area']} orders handmade beadwork worth {fmt_r(amt)} from {s['business']} via an online shopping website and pays via instant EFT. "
            f"How is this trading arrangement classified?"
        )
        ans = "A virtual (online) market"
        exp = f"Trading over an internet storefront with digital EFT settlement ({fmt_r(amt)}) takes place in a virtual/online market."
    else:
        prompt = (
            f"Shoppers walk through {s['area']} Fresh Produce Market, inspect fruit trays face-to-face with {s['entrepreneur']}, and pay {fmt_r(amt)} cash at the stall. "
            f"How is this trading arrangement classified?"
        )
        ans = "A physical market"
        exp = f"Face-to-face exchange of produce ({fmt_r(amt)}) at a dedicated location is a physical market."
    opts = [
        "A virtual (online) market",
        "A physical market",
        "A capital stock exchange (JSE)",
        "A non-market barter gift",
    ]
    return _make_mcq(
        rng,
        subskill="02_physical_vs_virtual_online_markets",
        title="Physical vs Virtual Markets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check whether buyers and sellers meet in person at a physical stall or connect digitally.",
            "tier_2": "Internet/app/phone = Virtual market; face-to-face stall/shop = Physical market.",
            "tier_3": f"Correct answer: {ans}.",
        },
        misconception_tags=["ignores_virtual_markets"],
        question_family_id="physical_vs_virtual_market",
    )


def _b03_two_main_market_categories(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    spend = rng.randint(15, 45) * 1000
    fac = rng.randint(12, 35) * 1000
    svg = svg_circular_markets(s["area"], s["business"], fmt_r(spend), fmt_r(fac))
    prompt = (
        f"Examine the circular market model linking {s['area']} Households and {s['business']}. "
        f"Which TWO overarching market categories connect households and businesses in South Africa?"
    )
    ans = "Goods and Services Market AND Factor Market"
    opts = [
        "Goods and Services Market AND Factor Market",
        "Wholesale Stalls AND Supermarket Chains only",
        "Export Tax Offices AND Municipal Licensing Desks",
        "Petty Cash Boxes AND Cheque Counterfoils",
    ]
    exp = f"An economy runs through two main market arenas: the Goods & Services Market ({fmt_r(spend)} output sales) and the Factor Market ({fmt_r(fac)} productive inputs)."
    return _make_mcq(
        rng,
        subskill="03_two_main_market_categories",
        title="Two Main Categories of Markets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look at the top and bottom boxes in the circular model.",
            "tier_2": "Outputs trade in the Goods & Services Market; Inputs trade in the Factor Market.",
            "tier_3": ans,
        },
        misconception_tags=["omits_factor_market_category"],
        question_family_id="two_main_markets",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b04_buyers_and_sellers_roles_swap(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    wage = rng.randint(5, 14) * 1000
    prompt = (
        f"Nomsa lives in {s['area']} and earns {fmt_r(wage)} per month working at {s['business']}, then spends her income buying groceries at retail stores. "
        f"Which statement accurately contrasts Nomsa's role in the Factor Market versus the Goods & Services Market?"
    )
    ans = "Nomsa is a SELLER (of labour) in the Factor Market and a BUYER in the Goods & Services Market"
    opts = [
        "Nomsa is a SELLER (of labour) in the Factor Market and a BUYER in the Goods & Services Market",
        "Nomsa is a BUYER in both the Factor Market and the Goods & Services Market",
        "Nomsa is a SELLER in the Goods & Services Market and an employer in the Factor Market",
        "Households never participate as sellers in any economic market",
    ]
    exp = f"Households SELL productive factor services (Nomsa's labour earning {fmt_r(wage)}) in the Factor Market, and BUY final consumer products in the Goods & Services Market."
    return _make_mcq(
        rng,
        subskill="04_buyers_and_sellers_roles_swap",
        title="Households & Businesses Swap Buyer/Seller Roles",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask: What is Nomsa supplying vs what is Nomsa purchasing?",
            "tier_2": "Households sell Factors (Labour) and buy Goods & Services.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_households_are_buyers_in_factor_market"],
        question_family_id="buyer_seller_swap",
    )


def _b05_goods_vs_services_classification(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 65) * 10
    ask_svc = rng.choice([True, False])
    if ask_svc:
        prompt = f"A resident of {s['area']} pays {fmt_r(amt)} for a dental check-up and teeth cleaning at a local clinic. Is this traded in the Goods section or Services section, and why?"
        ans = "Services Market — healthcare is an intangible action/expertise performed rather than a physical item"
        exp = f"A dental check-up ({fmt_r(amt)}) is intangible — you experience the skill without taking home a physical manufactured commodity — so it belongs to the Services Market."
    else:
        prompt = f"A resident of {s['area']} pays {fmt_r(amt)} for fresh bread, cooking oil, and washing powder. How is this purchase classified?"
        ans = "Goods Market — tangible physical items that can be seen, touched, and carried home"
        exp = f"Groceries ({fmt_r(amt)}) are tangible physical products bought in the Goods Market."
    opts = [
        "Services Market — healthcare is an intangible action/expertise performed rather than a physical item",
        "Goods Market — tangible physical items that can be seen, touched, and carried home",
        "Capital Stock Market — shares issued on the JSE",
        "Labour Recruitment Agency — hiring long-term staff",
    ]
    return _make_mcq(
        rng,
        subskill="05_goods_vs_services_classification",
        title="Tangible Goods vs Intangible Services",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Test whether the buyer can touch and carry away a physical object.",
            "tier_2": "Tangible = Goods; Intangible skill/performance = Services.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_tangible_goods_with_intangible_services"],
        question_family_id="goods_vs_services",
    )


def _b06_wholesale_market_definition_role(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cases = rng.randint(25, 80)
    sup = rng.choice(SUPPLIERS)
    prompt = (
        f"{s['business']} buys {cases} sealed bulk cartons of canned goods from {sup} to stock its township retail shelves. "
        f"Which type of market does {sup} operate in, and who are its main customers?"
    )
    ans = f"Wholesale market — buys large bulk quantities from manufacturers and sells in bulk to retailers like {s['business']}"
    opts = [
        f"Wholesale market — buys large bulk quantities from manufacturers and sells in bulk to retailers like {s['business']}",
        "Flea market — sells single homemade crafts to weekend pedestrians only",
        "Factor market — hires casual weekend till packers",
        "Money market — issues 30-day short-term commercial loans",
    ]
    exp = f"Wholesalers such as {sup} operate in the Wholesale Market, supplying bulk cartons ({cases} cases) to retail shops rather than single units to households."
    return _make_mcq(
        rng,
        subskill="06_wholesale_market_definition_role",
        title="Role of the Wholesale Market",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice the purchase is 25–80 bulk cartons bought FOR RESALE.",
            "tier_2": "Wholesale markets bridge manufacturers and retail businesses via bulk trade.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_wholesale_and_retail_buyers"],
        question_family_id="wholesale_market_role",
    )


def _b07_retail_market_role_to_consumers(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 18) * 10
    prompt = (
        f"After work in {s['area']}, Thabo stops at a neighbourhood convenience store and buys one loaf of bread and 1 L of milk for {fmt_r(amt)}. "
        f"In which type of market is Thabo shopping?"
    )
    ans = "Retail market (selling small individual quantities directly to final consumers)"
    opts = [
        "Retail market (selling small individual quantities directly to final consumers)",
        "Wholesale market (selling pallet loads to factory distributors)",
        "Financial Capital Market (trading company shares on the JSE)",
        "Factor Market (purchasing productive machinery inputs)",
    ]
    exp = f"Buying small daily household quantities ({fmt_r(amt)}) from a shop for personal consumption happens in the Retail Market."
    return _make_mcq(
        rng,
        subskill="07_retail_market_role_to_consumers",
        title="Role of the Retail Market",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice Thabo buys single consumer units for family consumption, not bulk cartons for resale.",
            "tier_2": "Retail markets break bulk down into convenient small units for households.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_retail_and_wholesale_markets"],
        question_family_id="retail_market_role",
    )


def _b08_wholesale_vs_retail_price_markup_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    qty = rng.choice([20, 25, 30, 40])
    cost_box = rng.randint(12, 24) * 100
    retail_unit = int(cost_box / qty) + rng.randint(15, 35)
    retail_rev = qty * retail_unit
    gross_profit = retail_rev - cost_box
    ans = fmt_r(gross_profit)
    svg = svg_market_card(
        f"{s['business']} — Wholesale to Retail Pricing",
        f"Supplier: {s['supplier']} -> Area: {s['area']}",
        [
            ("Wholesale Bulk Purchase", f"{qty} packs for {fmt_r(cost_box)}"),
            ("Retail Selling Price per Pack", fmt_r(retail_unit)),
            ("Total Retail Sales Revenue", fmt_r(retail_rev)),
            ("Gross Retail Profit Earned", "R ???"),
        ],
    )
    prompt = (
        f"Examine the Wholesale-to-Retail pricing card for {s['business']}. "
        f"Calculate the Gross Retail Profit (`R ???`) earned after buying {qty} packs wholesale for {fmt_r(cost_box)} and selling all {qty} packs retail at {fmt_r(retail_unit)} each."
    )
    steps = [
        f"Retail Revenue = {qty} x {fmt_r(retail_unit)} = {fmt_r(retail_rev)}.",
        f"Subtract Wholesale Cost ({fmt_r(cost_box)}): {fmt_r(retail_rev)} - {fmt_r(cost_box)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="08_wholesale_vs_retail_price_markup_calc",
        title="Calculate Wholesale-to-Retail Gross Profit",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{gross_profit}", str(gross_profit)],
        steps=steps,
        hints={
            "tier_1": "Compare Total Retail Sales Revenue against the Wholesale Cost.",
            "tier_2": f"Gross Profit = ({qty} x {fmt_r(retail_unit)}) - {fmt_r(cost_box)}.",
            "tier_3": f"Gross Profit = {ans}.",
        },
        misconception_tags=["subtracts_unit_price_instead_of_total_cost"],
        question_family_id="wholesale_retail_profit",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b09_farmer_craft_and_flea_markets(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    stalls = rng.randint(35, 95)
    prompt = (
        f"Every Saturday in {s['area']}, {stalls} local vegetable growers, wood-carvers, and second-hand clothes sellers set up temporary tables to sell straight to passing shoppers. "
        f"Which sub-category of Goods Markets does this describe?"
    )
    ans = "Farmer, craft, and flea markets (informal/periodic direct producer-to-consumer markets)"
    opts = [
        "Farmer, craft, and flea markets (informal/periodic direct producer-to-consumer markets)",
        "The Johannesburg Stock Exchange (JSE)",
        "An inter-bank Money Market trading desk",
        "A multinational wholesale import warehouse",
    ]
    exp = f"Weekend markets of {stalls} local growers and artisans selling directly to shoppers are classic Farmer, Craft, and Flea Markets."
    return _make_mcq(
        rng,
        subskill="09_farmer_craft_and_flea_markets",
        title="Farmer, Craft & Flea Markets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for local growers, craft makers, and periodic weekend stalls.",
            "tier_2": "Informal weekend venues with growers and crafters are farmer/craft/flea markets.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_flea_markets_with_financial_markets"],
        question_family_id="farmer_craft_flea_markets",
    )


def _b10_distribution_chain_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("Producer / Manufacturer", "Makes raw goods into bulk finished crates", "Wholesalers"),
        ("Wholesale Market", "Breaks huge factory batches into smaller bulk cartons", "Retailers & Spazas"),
        ("Retail Market", "Sells single convenient units in local shops", "Final Consumers / Households"),
        ("Consumer / Household", "Purchases final items to satisfy needs & wants", "End Use (No Resale)"),
    ]
    headers = ["Market Chain Link", "Core Function", "Typical Buyer"]
    table_rows = [[(lnk, "given", False), (fn, "required", True), (byr, "required", True)] for lnk, fn, byr in pool]
    cell_hints = {}
    for idx, (lnk, _, _) in enumerate(pool):
        cell_hints[f"t0_r{idx}_c1"] = f"Describe the function of {lnk}."
        cell_hints[f"t0_r{idx}_c2"] = f"Name who buys from {lnk}."
    prompt = f"Complete the Goods Distribution Chain table below for products sold in {s['area']}."
    return _make_table(
        rng,
        subskill="10_distribution_chain_table",
        title="Goods Market Distribution Chain Table",
        prompt=prompt,
        journal_type="distribution_chain",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Trace goods moving from Factory -> Wholesaler -> Retailer -> Consumer.",
            "tier_2": "Each link breaks bulk down further until households buy single units.",
            "tier_3": " | ".join(f"{l}: {b}" for l, _, b in pool),
        },
        misconception_tags=["swaps_wholesaler_and_retailer_order"],
        question_family_id="distribution_chain_table",
    )


def _b11_services_market_intangible_examples(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 15) * 100
    prompt = (
        f"Which group of providers in {s['area']} operates purely in the **Services Market** (charging e.g. {fmt_r(amt)} for intangible labour/expertise rather than physical stock)?"
    )
    ans = "Plumbers, electricians, hairstylists, doctors, attorneys, and mechanics"
    opts = [
        "Plumbers, electricians, hairstylists, doctors, attorneys, and mechanics",
        "Maize mills, brick factories, and wholesale cold-storage depots",
        "Supermarket bakery shelves selling bread and bottled juice",
        "Shoe shops selling imported leather boots and socks",
    ]
    exp = f"Service providers (plumbers, electricians, doctors, salons, mechanics) sell expertise and action ({fmt_r(amt)}) rather than physical goods, placing them in the Services Market."
    return _make_mcq(
        rng,
        subskill="11_services_market_intangible_examples",
        title="Identifying Providers in the Services Market",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for professions paid for their skilled work/time rather than selling boxes of stock.",
            "tier_2": "Doctors, plumbers, electricians, mechanics, and hairstylists operate in the Services Market.",
            "tier_3": ans,
        },
        misconception_tags=["classifies_mechanics_or_salons_as_physical_goods_only"],
        question_family_id="services_market_examples",
    )


def _b12_utilities_airtime_as_service_market(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 65) * 10
    util = rng.choice(["prepaid municipal electricity tokens", "mobile airtime and data bundles"])
    prompt = (
        f"{s['entrepreneur']} buys {fmt_r(amt)} of {util} via a smartphone app for {s['business']}. "
        f"Why is purchasing {util} classified inside the Services Market?"
    )
    ans = "Because energy supply and telecommunications connectivity are intangible services consumed without acquiring a physical good"
    opts = [
        "Because energy supply and telecommunications connectivity are intangible services consumed without acquiring a physical good",
        "Because municipal electricity tokens are agricultural goods from farmer markets",
        "Because buying airtime grants ownership shares on the Johannesburg Stock Exchange",
        "Because mobile apps automatically qualify as Factor Markets",
    ]
    exp = f"Buying {util} ({fmt_r(amt)}) purchases access to intangible utility/network service rather than a physical item, so it sits within the Services Market."
    return _make_mcq(
        rng,
        subskill="12_utilities_airtime_as_service_market",
        title="Electricity & Airtime in the Services Market",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Can you hold 1 GB of mobile data or 50 kWh of electricity in your hand?",
            "tier_2": "Electricity and mobile airtime/data are intangible services.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_prepaid_tokens_are_physical_goods"],
        question_family_id="utilities_services_market",
    )


def _b13_consumer_goods_durable_vs_non_durable(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 16) * 1000
    is_dur = rng.choice([True, False])
    if is_dur:
        prompt = (
            f"A family in {s['area']} buys a commercial chest freezer for {fmt_r(amt)} expected to work for 8 to 10 years. "
            f"Within the Goods Market, what kind of consumer good is this freezer?"
        )
        ans = "A durable good (used repeatedly over many years)"
        exp = f"A chest freezer ({fmt_r(amt)}) delivers service repeatedly over many years -> Durable consumer good."
    else:
        prompt = (
            f"A family in {s['area']} spends {fmt_r(int(amt / 40))} on fresh milk, vegetables, and bread consumed that same week. "
            f"How are these items classified in the Goods Market?"
        )
        ans = "Non-durable goods (used up quickly in one or a few uses)"
        exp = "Foodstuffs consumed immediately or within days are Non-durable consumer goods."
    opts = [
        "A durable good (used repeatedly over many years)",
        "Non-durable goods (used up quickly in one or a few uses)",
        "A service bought in the Factor Market",
        "A share certificate on the Capital Market",
    ]
    return _make_mcq(
        rng,
        subskill="13_consumer_goods_durable_vs_non_durable",
        title="Durable vs Non-Durable Goods",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Compare how long the product lasts during normal household use.",
            "tier_2": "Appliances lasting years = Durable; food/fuel consumed rapidly = Non-durable.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_durable_and_non_durable_goods"],
        question_family_id="durable_non_durable",
    )


def _b14_market_goods_services_audit_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt1 = rng.randint(3, 12) * 1000
    amt2 = rng.randint(15, 55) * 10
    amt3 = rng.randint(2, 8) * 100
    headers = ["Market Transaction", "Physical / Virtual", "Goods / Services", "Sub-Market Type"]
    table_rows = [
        [(f"Spaza owner buys 40 cases cold drinks at cash-and-carry warehouse ({fmt_r(amt1)}).", "given", False), ("Physical", "required", True), ("Goods", "required", True), ("Wholesale Market", "required", True)],
        [(f"Household downloads {fmt_r(amt2)} prepaid airtime on banking app.", "given", False), ("Virtual", "required", True), ("Services", "required", True), ("Services Market", "required", True)],
        [(f"Tourist buys hand-carved bowl ({fmt_r(amt3)}) at weekend craft stall.", "given", False), ("Physical", "required", True), ("Goods", "required", True), ("Craft / Flea Market", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Physical", "t0_r0_c2": "Goods", "t0_r0_c3": "Wholesale Market",
        "t0_r1_c1": "Virtual", "t0_r1_c2": "Services", "t0_r1_c3": "Services Market",
        "t0_r2_c1": "Physical", "t0_r2_c2": "Goods", "t0_r2_c3": "Craft / Flea Market",
    }
    prompt = f"Classify these three market transactions observed in {s['area']} across channel, product nature, and sub-market type."
    return _make_table(
        rng,
        subskill="14_market_goods_services_audit_table",
        title="Goods & Services Market Classification Table",
        prompt=prompt,
        journal_type="market_audit_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Check app/online vs walk-in store, physical vs intangible, and bulk vs single-unit stall.",
            "tier_2": "Row 1: Physical / Goods / Wholesale; Row 2: Virtual / Services / Services Market; Row 3: Physical / Goods / Craft Market.",
            "tier_3": "Complete all 3 columns per row matching channel, product, and venue.",
        },
        misconception_tags=["misclassifies_virtual_services_or_wholesale"],
        question_family_id="market_audit_table",
    )


def _b15_local_spaza_wholesale_vs_direct_sourcing(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bulk_disc = rng.randint(15, 28)
    prompt = (
        f"{s['entrepreneur']} runs a convenience shop in {s['area']} and saves {bulk_disc}% per unit by purchasing stock from a regional Wholesaler instead of a local Retail supermarket. "
        f"Explain TWO advantages and ONE challenge of sourcing from Wholesale Markets for a small retailer."
    )
    sample = (
        f"Advantages: (1) Lower bulk unit cost (saving {bulk_disc}%) enables competitive retail pricing and higher profit margins; (2) Reliable bulk variety saves daily shopping trips.\n"
        "Challenge: Requires higher upfront working capital and storage space to buy full cartons/pallets at once."
    )
    pts = [
        f"Advantage 1: Lower unit price ({bulk_disc}% savings) raises profit margin or allows lower retail prices.",
        "Advantage 2: Convenient one-stop bulk supply reduces frequent stock-runs.",
        "Challenge: Requires larger upfront cash outflow and storage space for bulk stock.",
    ]
    return _make_rubric(
        rng,
        subskill="15_local_spaza_wholesale_vs_direct_sourcing",
        title="Wholesale Sourcing Pros & Cons for Small Retailers",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Compare bulk discount savings against cash-flow and storage constraints.",
            "tier_2": "Give two benefits (lower unit cost, bulk supply) and one challenge (upfront cash/storage).",
            "tier_3": sample,
        },
        misconception_tags=["assumes_wholesalers_sell_single_items_on_zero_capital"],
        question_family_id="wholesale_sourcing_rubric",
        marks=3,
    )


def _b16_ecommerce_delivery_growth_sa(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    reach = rng.randint(5, 25) * 1000
    prompt = (
        f"By joining a virtual online marketplace, {s['business']} in {s['area']} expands beyond local foot traffic to reach over {reach:,} potential shoppers across provinces. "
        f"State TWO advantages and ONE risk of operating in a virtual/online Goods & Services market."
    )
    sample = (
        f"Advantages: (1) Expands geographic market reach to {reach:,}+ customers 24/7 without paying for extra physical shop rent; (2) Lowers overhead and automates digital receipts/EFTs.\n"
        "Risk: Courier/delivery logistics costs, data connectivity gaps, or online payment/phishing fraud."
    )
    pts = [
        "Advantage 1: Geographic reach beyond local neighbourhood / 24-hour trading.",
        "Advantage 2: Lower physical shop rent and automated digital transaction trail.",
        "Risk: Courier costs, internet access gaps, or cybersecurity/fraud risks.",
    ]
    return _make_rubric(
        rng,
        subskill="16_ecommerce_delivery_growth_sa",
        title="Virtual Marketplace Opportunities & Risks",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about customer reach, shop rent vs courier delivery, and online trust.",
            "tier_2": "Include wider 24/7 reach & lower physical rent vs courier/cyber risk.",
            "tier_3": sample,
        },
        misconception_tags=["ignores_logistics_and_fraud_risks_in_virtual_markets"],
        question_family_id="virtual_market_rubric",
        marks=3,
    )


def _b17_price_negotiation_in_flea_market(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    list_price = rng.randint(4, 15) * 100
    disc_pct = rng.choice([10, 15, 20])
    disc_amt = int(list_price * disc_pct / 100)
    final_price = list_price - disc_amt
    ans = fmt_r(final_price)
    prompt = (
        f"At a weekend craft market in {s['area']}, an artisan asks {fmt_r(list_price)} for a hand-woven basket. "
        f"After friendly bargaining, the buyer and seller agree on a {disc_pct}% cash discount. "
        f"Calculate the final agreed market price paid."
    )
    steps = [
        f"Discount amount = {disc_pct}% of {fmt_r(list_price)} = {fmt_r(disc_amt)}.",
        f"Final agreed market price = {fmt_r(list_price)} - {fmt_r(disc_amt)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="17_price_negotiation_in_flea_market",
        title="Agreed Price in Flea/Craft Market Bargaining",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{final_price}", str(final_price)],
        steps=steps,
        hints={
            "tier_1": f"First calculate {disc_pct}% of {fmt_r(list_price)}.",
            "tier_2": "Subtract that Rand discount from the asking price.",
            "tier_3": f"Agreed market price = {ans}.",
        },
        misconception_tags=["reports_discount_amount_instead_of_final_price"],
        question_family_id="flea_market_bargaining",
    )


def _b18_consumer_rights_in_goods_market(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(4, 18) * 100
    prompt = (
        f"Under South African consumer protection rules in retail markets, a customer buys an electric kettle for {fmt_r(amt)} at {s['business']}, "
        f"only to discover a factory electrical fault at home the next day. What right applies in a fair retail market?"
    )
    ans = "The right to safe, quality goods — and a repair, replacement, or refund with proof of purchase"
    opts = [
        "The right to safe, quality goods — and a repair, replacement, or refund with proof of purchase",
        "The buyer must permanently absorb any factory defect once money leaves the till",
        "Retailers may hide prices until after goods leave the store",
        "Only wholesale corporate buyers receive quality protection",
    ]
    exp = f"Fair Goods Markets protect consumers' right to safe, functional items ({fmt_r(amt)}) and fair remedies (repair, replacement, or refund) for defective goods."
    return _make_mcq(
        rng,
        subskill="18_consumer_rights_in_goods_market",
        title="Consumer Rights in Retail Goods Markets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Consider South African consumer rights regarding defective electrical goods.",
            "tier_2": "Consumers are entitled to safe quality goods and repair/replacement/refund.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_no_returns_apply_to_defective_goods"],
        question_family_id="consumer_rights_market",
    )


def _b19_circular_flow_goods_market_trace(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    spend = rng.randint(25, 80) * 1000
    fac = rng.randint(18, 60) * 1000
    svg = svg_circular_markets(s["area"], s["business"], fmt_r(spend), fmt_r(fac))
    prompt = (
        f"Inspect the circular flow paths connecting {s['area']} Households and {s['business']}. "
        f"What do the {fmt_r(spend)} flows passing through the **Goods & Services Market** represent?"
    )
    ans = f"Household consumption expenditure ({fmt_r(spend)}) flowing TO {s['business']} in exchange for consumer goods and services"
    opts = [
        f"Household consumption expenditure ({fmt_r(spend)}) flowing TO {s['business']} in exchange for consumer goods and services",
        f"Monthly salaries paid BY {s['business']} to factory workers",
        "Interest paid by the Reserve Bank to foreign investors",
        "Fixed Assets donated free of charge to households",
    ]
    exp = f"Through the Goods & Services Market, households spend {fmt_r(spend)} (money flow) to receive final goods and services (real flow) from businesses like {s['business']}."
    return _make_mcq(
        rng,
        subskill="19_circular_flow_goods_market_trace",
        title="Goods & Services Market Flow Trace",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Follow the top loop labelled Goods & Services Market.",
            "tier_2": "Households spend consumption income in the Goods Market to buy products from Businesses.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_goods_market_spending_with_factor_wages"],
        question_family_id="circular_goods_flow",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b20_local_informal_market_economic_value(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    traders = rng.randint(40, 120)
    prompt = (
        f"A municipal township market in {s['area']} hosts {traders} informal food, clothing, and craft vendors every weekend. "
        f"Explain THREE ways informal markets strengthen local community economies."
    )
    sample = (
        f"1. Job creation & self-employment: Allows {traders} local entrepreneurs to earn livelihoods with minimal startup capital.\n"
        "2. Affordable local access: Households buy fresh produce and daily essentials close to home without expensive taxi/bus fares.\n"
        "3. Local income circulation: Earnings spent at neighbouring spazas, transport operators, and suppliers boost wider township prosperity."
    )
    pts = [
        f"Creates self-employment and income for {traders} small entrepreneurs with low start-up barriers.",
        "Offers convenient, affordable goods locally without high travel costs for residents.",
        "Keeps money circulating inside the local economy among surrounding suppliers and services.",
    ]
    return _make_rubric(
        rng,
        subskill="20_local_informal_market_economic_value",
        title="Economic Value of Local Informal Markets",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about employment, transport savings for shoppers, and where vendors spend their profits.",
            "tier_2": "Cover low-barrier jobs, local affordability, and community income circulation.",
            "tier_3": sample,
        },
        misconception_tags=["dismisses_informal_markets_as_economically_unimportant"],
        question_family_id="informal_market_value",
        marks=3,
    )


def _b21_wholesale_break_bulk_unit_cost_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    units = rng.choice([20, 24, 25, 40])
    crate_cost = units * rng.randint(12, 28)
    transport = units * rng.choice([2, 3])
    total_cost = crate_cost + transport
    unit_cost = int(total_cost / units)
    ans = fmt_r(unit_cost)
    prompt = (
        f"{s['business']} purchases a wholesale crate of {units} cooking-oil bottles from {s['supplier']} for {fmt_r(crate_cost)} "
        f"and pays {fmt_r(transport)} delivery transport to {s['area']}. "
        f"Calculate the true landed wholesale cost PER BOTTLE before adding retail profit."
    )
    steps = [
        f"Total landed cost = Wholesale crate ({fmt_r(crate_cost)}) + Transport ({fmt_r(transport)}) = {fmt_r(total_cost)}.",
        f"Cost per bottle = {fmt_r(total_cost)} / {units} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="21_wholesale_break_bulk_unit_cost_calc",
        title="Calculate Landed Wholesale Unit Cost",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{unit_cost}", str(unit_cost)],
        steps=steps,
        hints={
            "tier_1": "Don't forget to add delivery transport before dividing by the number of bottles!",
            "tier_2": f"({fmt_r(crate_cost)} + {fmt_r(transport)}) / {units}.",
            "tier_3": f"Landed unit cost = {ans}.",
        },
        misconception_tags=["ignores_transport_cost_in_unit_pricing"],
        question_family_id="wholesale_unit_cost",
    )


def _b22_service_provider_quote_vs_rate_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    callout = rng.randint(250, 450)
    rate = rng.randint(200, 350)
    hours = rng.choice([2, 3, 4])
    total = callout + rate * hours
    ans = fmt_r(total)
    prompt = (
        f"A licensed electrician operating in {s['area']}'s Services Market charges a fixed call-out fee of {fmt_r(callout)} "
        f"plus {fmt_r(rate)} per hour of labour. If a repair at {s['business']} takes {hours} hours, calculate the total service charge."
    )
    steps = [
        f"Hourly labour charge = {hours} hours x {fmt_r(rate)} = {fmt_r(hours * rate)}.",
        f"Add call-out fee ({fmt_r(callout)}): {fmt_r(callout)} + {fmt_r(hours * rate)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="22_service_provider_quote_vs_rate_calc",
        title="Calculate Total Fee in Services Market",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total}", str(total)],
        steps=steps,
        hints={
            "tier_1": "Separate the one-time call-out fee from the hourly rate.",
            "tier_2": f"{fmt_r(callout)} + ({hours} x {fmt_r(rate)}).",
            "tier_3": f"Total service charge = {ans}.",
        },
        misconception_tags=["multiplies_call_out_fee_by_hours"],
        question_family_id="services_fee_calc",
    )


def _b23_match_market_venue_to_type_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pool = [
        ("Makro / Cash & Carry Warehouse", "Wholesale Market", "Bulk cartons for retail resale"),
        ("Neighbourhood Spaza / Supermarket", "Retail Market", "Single grocery units for households"),
        (f"{s['area']} Weekend Artisan Stalls", "Craft / Flea Market", "Handmade items direct to shoppers"),
        ("Local Plumbing & Electrical Repair Co.", "Services Market", "Intangible maintenance expertise"),
    ]
    rng.shuffle(pool)
    headers = ["South African Market Example", "Specific Market Type", "What Is Traded"]
    table_rows = [[(ex, "given", False), (mt, "required", True), (tr, "required", True)] for ex, mt, tr in pool]
    cell_hints = {}
    for idx, (ex, _, _) in enumerate(pool):
        cell_hints[f"t0_r{idx}_c1"] = f"Classify {ex} as Wholesale, Retail, Craft/Flea, or Services Market."
        cell_hints[f"t0_r{idx}_c2"] = f"Describe whether it trades bulk goods, single units, craft items, or intangible service."
    prompt = (
        f"{s['entrepreneur']} of {s['business']} ({s['area']}) reviews four South African trading examples. "
        f"Match each example below to its Specific Market Type and What Is Traded."
    )
    return _make_table(
        rng,
        subskill="23_match_market_venue_to_type_table",
        title="SA Market Venues Matching Table",
        prompt=prompt,
        journal_type="market_venues_match",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Distinguish bulk B2B supply, single consumer sales, informal stalls, and intangible labour skills.",
            "tier_2": "Makro = Wholesale; Spaza = Retail; Stalls = Craft/Flea; Plumbing = Services.",
            "tier_3": " | ".join(f"{mt}: {tr}" for _, mt, tr in pool),
        },
        misconception_tags=["mislabels_wholesale_retail_and_services_venues"],
        question_family_id="market_venues_table",
    )


def _b24_spot_market_classification_misconception(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    fee = rng.randint(2, 9) * 100
    prompt = (
        f"A learner in {s['area']} insists: 'Only physical fruit stalls and supermarkets count as markets; hiring a tutor for {fmt_r(fee)} or buying shares online is not a market.' "
        f"Which correction is economically accurate?"
    )
    ans = "Markets include intangible services (tutoring) and virtual financial platforms (share trading) wherever buyers and sellers trade at agreed prices"
    opts = [
        "Markets include intangible services (tutoring) and virtual financial platforms (share trading) wherever buyers and sellers trade at agreed prices",
        "The learner is right — markets only trade agricultural produce",
        "Markets only exist when municipal business licences are posted outside a building",
        "Hiring a tutor belongs in the Wholesale Bulk Market",
    ]
    exp = f"Markets exist in physical and virtual forms across Goods, Services (like {fmt_r(fee)} tutoring), Factor, and Financial exchanges."
    return _make_mcq(
        rng,
        subskill="24_spot_market_classification_misconception",
        title="Correcting Narrow Definitions of Markets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Does economic theory limit markets strictly to physical produce stalls?",
            "tier_2": "Include intangible services and virtual financial exchanges in the definition of markets.",
            "tier_3": ans,
        },
        misconception_tags=["restricts_markets_to_tangible_physical_places"],
        question_family_id="market_misconception",
    )


def _b25_goods_market_case_comparison(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    loaves = rng.randint(80, 200)
    prompt = (
        f"A community bakery in {s['area']} bakes fresh loaves daily: every morning it sells {loaves} loaves in bulk crates to nearby tuckshops, "
        f"and through the front counter it sells single loaves directly to neighbourhood families. "
        f"Explain how ONE bakery participates in BOTH the Wholesale Market and the Retail Market."
    )
    sample = (
        f"1. Wholesale role: Selling {loaves} loaves in bulk crates to tuckshops (other businesses for resale) places the bakery in the Wholesale Market.\n"
        "2. Retail role: Selling single loaves across the counter directly to final household consumers places the exact same bakery in the Retail Market."
    )
    pts = [
        f"Identifies Wholesale role: selling {loaves} bulk loaves to tuckshops for resale.",
        "Identifies Retail role: selling single loaves directly to final household consumers.",
    ]
    return _make_rubric(
        rng,
        subskill="25_goods_market_case_comparison",
        title="Dual Wholesale & Retail Roles Case Study",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Distinguish WHO is buying in each channel: tuckshops (for resale) vs families (for eating).",
            "tier_2": "Bulk to tuckshops = Wholesale; Single units to households = Retail.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_business_can_only_use_one_market_channel"],
        question_family_id="dual_wholesale_retail_case",
        marks=2,
    )


ARCHETYPES_01_25 = {
    "01_market_definition_non_physical": _b01_market_definition_non_physical,
    "02_physical_vs_virtual_online_markets": _b02_physical_vs_virtual_online_markets,
    "03_two_main_market_categories": _b03_two_main_market_categories,
    "04_buyers_and_sellers_roles_swap": _b04_buyers_and_sellers_roles_swap,
    "05_goods_vs_services_classification": _b05_goods_vs_services_classification,
    "06_wholesale_market_definition_role": _b06_wholesale_market_definition_role,
    "07_retail_market_role_to_consumers": _b07_retail_market_role_to_consumers,
    "08_wholesale_vs_retail_price_markup_calc": _b08_wholesale_vs_retail_price_markup_calc,
    "09_farmer_craft_and_flea_markets": _b09_farmer_craft_and_flea_markets,
    "10_distribution_chain_table": _b10_distribution_chain_table,
    "11_services_market_intangible_examples": _b11_services_market_intangible_examples,
    "12_utilities_airtime_as_service_market": _b12_utilities_airtime_as_service_market,
    "13_consumer_goods_durable_vs_non_durable": _b13_consumer_goods_durable_vs_non_durable,
    "14_market_goods_services_audit_table": _b14_market_goods_services_audit_table,
    "15_local_spaza_wholesale_vs_direct_sourcing": _b15_local_spaza_wholesale_vs_direct_sourcing,
    "16_ecommerce_delivery_growth_sa": _b16_ecommerce_delivery_growth_sa,
    "17_price_negotiation_in_flea_market": _b17_price_negotiation_in_flea_market,
    "18_consumer_rights_in_goods_market": _b18_consumer_rights_in_goods_market,
    "19_circular_flow_goods_market_trace": _b19_circular_flow_goods_market_trace,
    "20_local_informal_market_economic_value": _b20_local_informal_market_economic_value,
    "21_wholesale_break_bulk_unit_cost_calc": _b21_wholesale_break_bulk_unit_cost_calc,
    "22_service_provider_quote_vs_rate_calc": _b22_service_provider_quote_vs_rate_calc,
    "23_match_market_venue_to_type_table": _b23_match_market_venue_to_type_table,
    "24_spot_market_classification_misconception": _b24_spot_market_classification_misconception,
    "25_goods_market_case_comparison": _b25_goods_market_case_comparison,
}
