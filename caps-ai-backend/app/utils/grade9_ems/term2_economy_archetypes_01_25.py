"""Grade 9 EMS Term 2: Price Theory — Semantic Archetypes 01 to 25."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple


TOPIC_NAME = "Price theory"
SUBTOPIC_ID = "term2_economy"


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
    """Assemble standardized 6-pillar Grade 9 EMS Price Theory question payload."""
    qid = f"gr9_ems_t2_pt_{subskill}_{rng.randint(100000, 999999)}"
    payload: Dict[str, Any] = {
        "id": qid,
        "topic": TOPIC_NAME,
        "subtopic": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": f"ems_gr9_t2_price_theory_{subskill}",
        "term": 2,
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


def svg_market_graph(
    *,
    title: str,
    max_q: int,
    max_p: int,
    d_pts: Optional[List[Tuple[int, int]]] = None,
    s_pts: Optional[List[Tuple[int, int]]] = None,
    d2_pts: Optional[List[Tuple[int, int]]] = None,
    s2_pts: Optional[List[Tuple[int, int]]] = None,
    eq_pt: Optional[Tuple[int, int, str]] = None,
    eq2_pt: Optional[Tuple[int, int, str]] = None,
    h_line_p: Optional[Tuple[int, str, str]] = None,
    d_label: str = "D",
    s_label: str = "S",
    d2_label: str = "D1",
    s2_label: str = "S1",
) -> Dict[str, Any]:
    """Render clean Cartesian Price (Y-axis) vs Quantity (X-axis) SVG model."""
    w, h = 580, 340
    ox, oy = 76, 282
    plot_w, plot_h = 440, 224

    def px(q: float) -> float:
        return ox + (q / max_q) * plot_w

    def py(p: float) -> float:
        return oy - (p / max_p) * plot_h

    grid: List[str] = []
    for i in range(1, 6):
        qv = round(max_q * i / 5)
        xp = px(qv)
        grid.append(
            f'<line x1="{xp:.1f}" y1="{oy}" x2="{xp:.1f}" y2="{oy - plot_h}" stroke="#e2e8f0" stroke-width="1"/>'
            f'<text x="{xp:.1f}" y="{oy + 17}" text-anchor="middle" font-size="11" fill="#334155">{qv}</text>'
        )
        pv = round(max_p * i / 5)
        yp = py(pv)
        grid.append(
            f'<line x1="{ox}" y1="{yp:.1f}" x2="{ox + plot_w}" y2="{yp:.1f}" stroke="#e2e8f0" stroke-width="1"/>'
            f'<text x="{ox - 8}" y="{yp + 4:.1f}" text-anchor="end" font-size="11" fill="#334155">R{pv}</text>'
        )

    def polyline(pts: List[Tuple[int, int]], color: str, dashed: bool = False, lbl: str = "") -> str:
        coords = " ".join(f"{px(q):.1f},{py(p):.1f}" for q, p in pts)
        dash = ' stroke-dasharray="6,4"' if dashed else ""
        lx, ly = px(pts[-1][0]), py(pts[-1][1])
        dots = "".join(
            f'<circle cx="{px(q):.1f}" cy="{py(p):.1f}" r="3.5" fill="{color}"/>'
            for q, p in pts
        )
        return (
            f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="2.6"{dash}/>'
            f'{dots}'
            f'<text x="{lx + 7:.1f}" y="{ly + 4:.1f}" font-size="13" font-weight="700" fill="{color}">{lbl}</text>'
        )

    extras: List[str] = []
    if d_pts:
        extras.append(polyline(d_pts, "#dc2626", False, d_label))
    if s_pts:
        extras.append(polyline(s_pts, "#2563eb", False, s_label))
    if d2_pts:
        extras.append(polyline(d2_pts, "#991b1b", True, d2_label))
    if s2_pts:
        extras.append(polyline(s2_pts, "#1e40af", True, s2_label))
    if h_line_p is not None:
        pval, lbl, col = h_line_p
        yp = py(pval)
        extras.append(
            f'<line x1="{ox}" y1="{yp:.1f}" x2="{ox + plot_w}" y2="{yp:.1f}" '
            f'stroke="{col}" stroke-width="2" stroke-dasharray="4,3"/>'
            f'<text x="{ox + plot_w - 4}" y="{yp - 6:.1f}" text-anchor="end" font-size="11" font-weight="700" fill="{col}">{lbl}</text>'
        )
    if eq_pt is not None:
        eq, ep, elbl = eq_pt
        ex, ey = px(eq), py(ep)
        extras.append(
            f'<line x1="{ox}" y1="{ey:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#0f172a" stroke-width="1.3" stroke-dasharray="3,3"/>'
            f'<line x1="{ex:.1f}" y1="{oy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#0f172a" stroke-width="1.3" stroke-dasharray="3,3"/>'
            f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="5" fill="#059669" stroke="#ffffff" stroke-width="1.5"/>'
            f'<text x="{ex + 8:.1f}" y="{ey - 7:.1f}" font-size="12" font-weight="700" fill="#065f46">{elbl} ({eq}; R{ep})</text>'
        )
    if eq2_pt is not None:
        eq, ep, elbl = eq2_pt
        ex, ey = px(eq), py(ep)
        extras.append(
            f'<line x1="{ox}" y1="{ey:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#6b21a8" stroke-width="1.3" stroke-dasharray="3,3"/>'
            f'<line x1="{ex:.1f}" y1="{oy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#6b21a8" stroke-width="1.3" stroke-dasharray="3,3"/>'
            f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="5" fill="#7c3aed" stroke="#ffffff" stroke-width="1.5"/>'
            f'<text x="{ex + 8:.1f}" y="{ey + 14:.1f}" font-size="12" font-weight="700" fill="#5b21b6">{elbl} ({eq}; R{ep})</text>'
        )

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff" rx="8"/>'
        f'<text x="{w // 2}" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{title}</text>'
        f'{"".join(grid)}'
        f'<line x1="{ox}" y1="{oy}" x2="{ox + plot_w + 10}" y2="{oy}" stroke="#0f172a" stroke-width="2.2"/>'
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - plot_h - 12}" stroke="#0f172a" stroke-width="2.2"/>'
        f'<text x="{ox - 10}" y="{oy + 14}" text-anchor="end" font-size="11" fill="#334155">0</text>'
        f'<text x="{ox + plot_w // 2}" y="{oy + 38}" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Quantity (Q)</text>'
        f'<text x="20" y="{oy - plot_h // 2}" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" '
        f'transform="rotate(-90 20 {oy - plot_h // 2})">Price (R)</text>'
        f'{"".join(extras)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _build_01_price_theory_meaning_market_forces(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("how avocado prices adjust in winter and summer at Johannesburg fresh-produce markets", "the economic study of how demand and supply interact in markets to determine prices and quantities"),
        ("why concert tickets sell for more than pocket calculators in a competitive market", "the analysis of how buyers' willingness to pay and producers' cost-driven supply set equilibrium prices"),
        ("how price signals guide scarce resources across goods without central price controls", "explaining how market price formation allocates scarce goods through demand and supply forces"),
        ("how sellers and consumers arrive at a mutually acceptable selling price", "the explanation of how supply and demand determine market values and exchange quantities"),
    ]
    obs, ans = rng.choice(cases)
    distractors = [
        "a government law forbidding all price changes throughout the calendar year",
        "the study of historical coins minted prior to industrial banking",
        "calculating only a municipality's annual refuse-collection tariff",
    ]
    prompt = f"Which statement best explains **Price Theory** when examining *{obs}*?"
    sol = f"- **Price Theory:** {ans.capitalize()}.\n- Prices act as vital signals linking consumer demand and producer supply."
    return make_question(
        rng=rng,
        subskill="01_price_theory_meaning_market_forces",
        question_type="mcq",
        prompt=prompt,
        correct_answer=ans.capitalize(),
        sample_answer=ans.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Select accurate price theory definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for linking demand & supply interaction to price/quantity determination.",
        hints={
            "tier_1": "Focus on the two market forces that meet to set prices.",
            "tier_2": "Price theory studies demand, supply and equilibrium price formation.",
            "tier_3": ans.capitalize(),
        },
        misconception_tags=["thinks_price_theory_means_cost_accounting_markup_only"],
        options=[ans.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_02_effective_demand_willing_and_able(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("Learner A wants a R4 500 bicycle and has saved R4 800 to buy it today; Learner B admires the bicycle but has only R350.", "Learner A (willing AND able to pay)"),
        ("Shopper X wants solar backup lights priced at R250 and carries R300 cash; Shopper Y likes the lights but lacks the funds.", "Shopper X (willing AND able to pay)"),
        ("Commuter M plans to buy a R1 200 monthly train pass and holds R1 500 in her account; Commuter N wishes for one with R0.", "Commuter M (willing AND able to pay)"),
        ("Chef P wants 10 kg fresh tomatoes at R22/kg and brings R250; Chef Q dislikes tomatoes despite having R500.", "Chef P (willing AND able to pay)"),
    ]
    scenario, correct = rng.choice(cases)
    prompt = (
        f"In Price Theory, **effective demand** requires two simultaneous conditions. Consider this case:\n"
        f"*{scenario}*\n\n"
        f"State which person creates **effective demand** and explain the two requirements."
    )
    ans = f"{correct}; effective demand requires both willingness (desire) and financial ability (purchasing power) at a specific price"
    sol = (
        f"- **Who Creates Demand:** **{correct}**.\n"
        f"- **Two Conditions:** Demand only exists in economics when a consumer is both **willing** to buy AND **financially able** to pay the market price."
    )
    return make_question(
        rng=rng,
        subskill="02_effective_demand_willing_and_able",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": f"Identify {correct}", "marks": 1, "type": "A"},
            {"step": "State willingness + ability to pay", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for identifying the effective buyer; 2 marks for willingness + ability to pay.",
        hints={
            "tier_1": "Wishing for an item without money does not count in market demand.",
            "tier_2": "Both willingness AND ability to pay must hold.",
            "tier_3": ans,
        },
        misconception_tags=["treats_mere_wants_without_purchasing_power_as_demand"],
    )


def _build_03_law_of_demand_inverse_relationship(rng: random.Random, mode: str) -> Dict[str, Any]:
    goods = [
        ("skateboards", 750, 300, 450, 1200),
        ("USB power banks", 400, 600, 220, 1150),
        ("2L sunflower cooking oil", 95, 500, 65, 850),
        ("cotton school jerseys", 320, 400, 210, 750),
    ]
    item, p1, q1, p2, q2 = rng.choice(goods)
    prompt = (
        f"When the price of **{item}** drops from {fmt_zar(p1)} to {fmt_zar(p2)} (*ceteris paribus*), "
        f"quantity demanded increases from {q1} units to {q2} units.\n\n"
        f"(a) State the **Law of Demand** accurately.\n"
        f"(b) Identify whether the mathematical relationship between price and quantity demanded is **direct** or **inverse**, and state the slope direction of the demand curve."
    )
    ans = "As price rises, quantity demanded falls (and as price falls, quantity demanded rises), ceteris paribus; inverse (negative) relationship; slopes downward from top-left to bottom-right"
    sol = (
        f"**(a) Law of Demand:** *Ceteris paribus* (all other factors equal), the higher the price of a good, the smaller the quantity demanded; the lower the price, the greater the quantity demanded.\n"
        f"**(b) Relationship & Curve Shape:** Price and quantity demanded have an **inverse (negative)** relationship, giving a curve sloping **downward from top-left to bottom-right**."
    )
    return make_question(
        rng=rng,
        subskill="03_law_of_demand_inverse_relationship",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "State Law of Demand accurately with ceteris paribus", "marks": 2, "type": "A"},
            {"step": "Identify inverse relationship + downward slope (top-left to bottom-right)", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Law of Demand; 2 marks for inverse relationship + slope direction.",
        hints={
            "tier_1": "Look at whether P and Q move in opposite directions.",
            "tier_2": "Opposite movement = inverse relationship = downward slope.",
            "tier_3": ans,
        },
        misconception_tags=["calls_demand_relationship_direct_or_upward_sloping"],
    )


def _build_04_ceteris_paribus_assumption_meaning(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("testing how bread prices affect bread demand while assuming household income, tastes and butter prices stay unchanged", "all other influencing factors remain constant while analysing one price change"),
        ("measuring solar-panel supply response to price without changing panel import tariffs or factory technology", "holding non-price determinants fixed to isolate the effect of price alone"),
        ("drawing a single demand curve for apples assuming mango prices and consumer wages do not vary", "keeping income, substitute prices and preferences constant"),
    ]
    clue, correct = rng.choice(cases)
    distractors = [
        "prices must remain frozen by parliament for ten consecutive years",
        "only agricultural products can ever follow demand and supply curves",
        "buyers and sellers trade exclusively without using any currency",
    ]
    prompt = f"In Price Theory, what does the Latin phrase ***ceteris paribus*** mean when *{clue}*?"
    sol = f"- ***Ceteris paribus*:** {correct.capitalize()}."
    return make_question(
        rng=rng,
        subskill="04_ceteris_paribus_assumption_meaning",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct.capitalize(),
        sample_answer=correct.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify exact meaning of ceteris paribus", "marks": 2, "type": "A"}],
        marking_guide="2 marks for 'all other factors held constant'.",
        hints={
            "tier_1": "Think of controlled science experiments where only one variable changes at a time.",
            "tier_2": "Ceteris paribus translates as 'other things being equal/constant'.",
            "tier_3": correct.capitalize(),
        },
        misconception_tags=["interprets_ceteris_paribus_as_constant_price"],
        options=[correct.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_05_reading_demand_schedule_values(rng: random.Random, mode: str) -> Dict[str, Any]:
    goods = ["Skateboards", "Solar Lanterns", "School Backpacks", "Mountain Helmets"]
    item = rng.choice(goods)
    p0 = rng.choice([100, 150, 200])
    dp = rng.choice([50, 100])
    q0 = rng.choice([1200, 1400, 1500])
    dq = rng.choice([200, 250, 300])
    rows_data = [(p0 + i * dp, q0 - i * dq) for i in range(4)]
    headers = [f"Price per {item[:-1]} (R)", "Quantity Demanded (Qd)"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [f"| Price per {item[:-1]} (R) | Quantity Demanded (Qd) |", "|---|---|"]
    req_rows = rng.sample([1, 2], 1) + [3]
    for r_idx, (p, q) in enumerate(rows_data, start=1):
        p_str, q_str = f"R{p}", str(q)
        req_q = (r_idx - 1) in req_rows
        c0 = {"coordinate": f"R{r_idx}C0", "value": p_str, "type": "given", "editable": False}
        c1 = {"coordinate": f"R{r_idx}C1", "value": "" if req_q else q_str, "type": "required" if req_q else "given", "editable": req_q}
        if req_q:
            correct_map[f"R{r_idx}C1"] = q_str
            cell_hints[f"R{r_idx}C1"] = f"Every R{dp} price increase reduces Quantity Demanded uniformly by {dq} units."
        rows_ui.append([c0, c1])
        md_lines.append(f"| {p_str} | {q_str} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="05_reading_demand_schedule_values",
        question_type="table_completion",
        prompt=f"Complete the linear **Demand Schedule** for **{item}** by applying the constant demand step pattern.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Completed Linear Demand Schedule ({item}):**\n\n- Step pattern: as price rises by R{dp}, quantity demanded drops by {dq} units.\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k} = {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per completed linear demand cell.",
        hints={
            "tier_1": "Find the constant change in Qd between consecutive given rows.",
            "tier_2": f"Each +R{dp} price step reduces Qd by {dq}.",
            "tier_3": md_table,
        },
        misconception_tags=["adds_quantity_step_instead_of_subtracting_on_demand_schedule"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "price", "label": headers[0]}, {"key": "qd", "label": headers[1]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_06_graphing_axes_price_y_quantity_x(rng: random.Random, mode: str) -> Dict[str, Any]:
    item = rng.choice(["Bicycles", "Oranges (bags)", "Textbooks", "Loaves of Bread"])
    max_p = rng.choice([50, 100, 200])
    max_q = rng.choice([500, 1000])
    d_pts = [(round(max_q * 0.2), round(max_p * 0.8)), (round(max_q * 0.5), round(max_p * 0.5)), (round(max_q * 0.8), round(max_p * 0.2))]
    diagram = svg_market_graph(title=f"{item} Market Model", max_q=max_q, max_p=max_p, d_pts=d_pts)
    prompt = (
        f"Inspect the plotted Demand Model for **{item}**.\n\n"
        f"(a) Which economic variable is always plotted on the **vertical Y-axis** and which on the **horizontal X-axis**?\n"
        f"(b) Explain why the `D` curve runs from top-left to bottom-right."
    )
    ans = "Vertical Y-axis: Price (R); Horizontal X-axis: Quantity (Q); slopes downward due to inverse Law of Demand"
    sol = (
        f"**(a) Standard Economics Axes:**\n"
        f"- **Vertical Y-axis:** Price (in Rand, `R`).\n"
        f"- **Horizontal X-axis:** Quantity (`Q`).\n\n"
        f"**(b) Slope Direction:** Because of the **Law of Demand**, higher prices correspond to smaller quantities (top-left) and lower prices to larger quantities (bottom-right)."
    )
    return make_question(
        rng=rng,
        subskill="06_graphing_axes_price_y_quantity_x",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Price on Y-axis and Quantity on X-axis", "marks": 2, "type": "A"},
            {"step": "Downward slope explained via inverse price-quantity link", "marks": 1, "type": "A"},
        ],
        marking_guide="2 marks for axes labels; 1 mark for inverse Law of Demand link.",
        hints={
            "tier_1": "Read the vertical and horizontal labels on the axes.",
            "tier_2": "Price goes up the vertical axis; Quantity goes across the horizontal axis.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_price_and_quantity_axes"],
        diagram_spec=diagram,
    )


def _build_07_interpreting_demand_curve_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    item = rng.choice(["Backpacks", "Skateboards", "Coffee Mug Sets", "Solar Chargers"])
    p_step = rng.choice([50, 100])
    max_p = p_step * 5
    q_step = rng.choice([100, 200])
    max_q = q_step * 5
    d_pts = [(q_step, 4 * p_step), (2 * q_step, 3 * p_step), (3 * q_step, 2 * p_step), (4 * q_step, p_step)]
    pick_idx = rng.choice([0, 1, 2, 3])
    q_ans, p_ask = d_pts[pick_idx]
    spending = p_ask * q_ans
    diagram = svg_market_graph(title=f"Demand Curve for {item}", max_q=max_q, max_p=max_p, d_pts=d_pts)
    prompt = (
        f"Study the Demand Curve `D` for **{item}** (passing through `({q_step}; R{4 * p_step})`, `({2 * q_step}; R{3 * p_step})`, `({3 * q_step}; R{2 * p_step})`, `({4 * q_step}; R{p_step})`).\n\n"
        f"(a) Read the quantity consumers are willing and able to buy at a price of **R{p_ask}**.\n"
        f"(b) Calculate total consumer expenditure (`Price * Quantity`) at R{p_ask}."
    )
    ans = f"Qd = {q_ans} units; Total expenditure = {fmt_zar(spending)}"
    sol = (
        f"**(a) Quantity Demanded:** Moving horizontally from **R{p_ask}** to curve `D` and down to the X-axis gives **Qd = {q_ans} units**.\n"
        f"**(b) Consumer Expenditure:** ${fmt_zar(p_ask)} \\times {q_ans} = {fmt_zar(spending)}$"
    )
    return make_question(
        rng=rng,
        subskill="07_interpreting_demand_curve_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Read Qd = {q_ans} units at R{p_ask}", "marks": 2, "type": "A"},
            {"step": f"Calculate expenditure {fmt_zar(spending)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for reading Qd; 2 marks for multiplying Price * Qd.",
        hints={
            "tier_1": f"Locate R{p_ask} on the vertical Price axis and trace across to curve D.",
            "tier_2": "Multiply price by quantity demanded.",
            "tier_3": ans,
        },
        misconception_tags=["reads_horizontal_axis_for_price"],
        diagram_spec=diagram,
    )


def _build_08_demand_change_movement_along_curve(rng: random.Random, mode: str) -> Dict[str, Any]:
    p1 = rng.choice([200, 300, 400])
    p2 = p1 - rng.choice([50, 100])
    q1 = rng.choice([400, 500, 600])
    q2 = q1 + rng.choice([150, 200, 250])
    dq = q2 - q1
    item = rng.choice(["denim jeans", "cricket bats", "electric fans", "study desks"])
    prompt = (
        f"The selling price of {item} drops from {fmt_zar(p1)} to {fmt_zar(p2)}, causing buyers to purchase {q2} units instead of {q1} units.\n\n"
        f"(a) Calculate the change in quantity demanded.\n"
        f"(b) Explain why economics calls this a **movement along the demand curve** rather than a shift of the demand curve."
    )
    ans = f"Change in Qd = +{dq} units; caused solely by a change in the product's own price (ceteris paribus), not a non-price determinant"
    sol = (
        f"**(a) Change in Quantity Demanded:** ${q2} - {q1} = +{dq}$ units.\n"
        f"**(b) Movement vs Shift:** Only the product's **own price** changed while non-price factors stayed constant, moving consumers down **along** the existing `D` curve."
    )
    return make_question(
        rng=rng,
        subskill="08_demand_change_movement_along_curve",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate +{dq} units", "marks": 2, "type": "A"},
            {"step": "Explain own-price change causes movement along D", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for arithmetic difference; 2 marks for distinguishing movement from shift.",
        hints={
            "tier_1": "Subtract original quantity from new quantity.",
            "tier_2": "Own-price changes move along a curve; non-price changes shift the whole curve.",
            "tier_3": ans,
        },
        misconception_tags=["claims_own_price_drop_shifts_entire_demand_curve_right"],
    )


def _build_09_non_price_determinants_shifting_demand(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("average factory worker salaries increase by 12% across Gauteng", "higher household income increasing consumer purchasing power"),
        ("a popular viral social-media campaign endorses reusable steel bottles", "shift in consumer tastes and preferences"),
        ("50 000 new residents move into a rapidly expanding coastal town", "increase in population / number of buyers in the market"),
        ("households expect maize-meal prices to double next month", "expectations of future price increases encouraging immediate stockpiling"),
    ]
    event, factor = rng.choice(cases)
    distractors = [
        "a change in the item's own current selling price (causing movement along the same curve)",
        "higher corporate wages paid by competing copper mines abroad",
        "the fixed vertical height of the Y-axis drawn in a textbook",
    ]
    prompt = f"Which **non-price determinant** shifts the entire demand curve rightward when *{event}*?"
    sol = f"- **Determinant:** {factor.capitalize()}.\n- Non-price factors change quantity demanded at **every** possible price, shifting the entire curve `D` rightward."
    return make_question(
        rng=rng,
        subskill="09_non_price_determinants_shifting_demand",
        question_type="mcq",
        prompt=prompt,
        correct_answer=factor.capitalize(),
        sample_answer=factor.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify correct non-price demand determinant", "marks": 2, "type": "A"}],
        marking_guide="2 marks for matching event to demand shifter.",
        hints={
            "tier_1": "Identify which factor besides the product's own price changed.",
            "tier_2": "Determinants include income, tastes, population, related goods and expectations.",
            "tier_3": factor.capitalize(),
        },
        misconception_tags=["labels_own_price_as_a_curve_shifter"],
        options=[factor.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_10_substitutes_price_cross_effect_demand(rng: random.Random, mode: str) -> Dict[str, Any]:
    pairs = [
        ("butter", 58, 76, "margarine", "spreads"),
        ("beef", 120, 155, "chicken", "protein"),
        ("brand-name cola", 18, 25, "store-brand lemonade", "cold drinks"),
        ("petrol-powered commuter taxis", 22, 30, "Metrorail commuter train passes", "daily commuting"),
    ]
    good_a, old_p, new_p, sub_b, cat = rng.choice(pairs)
    prompt = (
        f"In the {cat} market, **{good_a}** and **{sub_b}** are **substitutes**. "
        f"Suppose the price of {good_a} jumps from {fmt_zar(old_p)} to {fmt_zar(new_p)}.\n\n"
        f"(a) What happens to quantity demanded of {good_a}?\n"
        f"(b) Explain how and in which direction the demand curve for **{sub_b}** shifts."
    )
    ans = f"Qd for {good_a} falls; demand curve for {sub_b} shifts rightward (increases) as buyers switch to the cheaper substitute"
    sol = (
        f"**(a) Own Good ({good_a}):** Quantity demanded **decreases** (upward movement along {good_a}'s demand curve).\n"
        f"**(b) Substitute ({sub_b}):** Demand for {sub_b} **increases (shifts rightward)** because shoppers switch away from costlier {good_a} toward relatively cheaper {sub_b}."
    )
    return make_question(
        rng=rng,
        subskill="10_substitutes_price_cross_effect_demand",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"State Qd of {good_a} decreases", "marks": 1, "type": "A"},
            {"step": f"State D curve of {sub_b} shifts right + explain substitution", "marks": 3, "type": "A"},
        ],
        marking_guide="1 mark for Qd drop on A; 3 marks for rightward shift + rationale on B.",
        hints={
            "tier_1": "Substitutes satisfy the same want—when one becomes dearer, buyers switch.",
            "tier_2": "A price rise for A increases demand (rightward shift) for substitute B.",
            "tier_3": ans,
        },
        misconception_tags=["shifts_demand_for_substitute_left_when_rival_gets_pricier"],
    )


def _build_11_complements_price_cross_effect_demand(rng: random.Random, mode: str) -> Dict[str, Any]:
    pairs = [
        ("inkjet printers", "replacement ink cartridges"),
        ("petrol", "large fuel-heavy SUVs"),
        ("hotdog rolls", "viennas"),
        ("coffee beans", "coffee plungers"),
    ]
    good_a, comp_b = rng.choice(pairs)
    pct = rng.choice([25, 30, 40])
    prompt = (
        f"**{good_a.capitalize()}** and **{comp_b}** are **complementary goods** (used together).\n\n"
        f"If the price of {good_a} rises sharply by {pct}%, predict and explain the resulting shift in the demand curve for **{comp_b}**."
    )
    ans = f"Demand curve for {comp_b} shifts leftward (decreases) because fewer people buy costly {good_a}, lowering joint usage of {comp_b}"
    sol = (
        f"- **Direction:** The demand curve for **{comp_b}** shifts **leftward (decreases)**.\n"
        f"- **Reason:** Because {good_a} and {comp_b} are consumed together, higher prices for {good_a} reduce purchases of {good_a}, automatically reducing demand for {comp_b} at every price."
    )
    return make_question(
        rng=rng,
        subskill="11_complements_price_cross_effect_demand",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "State leftward shift (decrease) in demand for complement", "marks": 1, "type": "A"},
            {"step": "Explain joint consumption link", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for leftward shift; 2 marks for joint-use explanation.",
        hints={
            "tier_1": "Complements are bought and used together rather than instead of each other.",
            "tier_2": "If fewer people buy A, fewer people need complement B.",
            "tier_3": ans,
        },
        misconception_tags=["treats_complements_like_substitutes"],
    )


def _build_12_supply_definition_willing_and_able(rng: random.Random, mode: str) -> Dict[str, Any]:
    firms = [
        ("Western Cape apple orchards bringing graded crates to fresh markets across winter prices", "the various quantities of a good or service producers are willing and able to offer for sale at each price over a given period"),
        ("Gauteng furniture workshops planning monthly desk production at different tender prices", "how much output sellers are willing and able to place on the market across price levels, ceteris paribus"),
        ("bakery chains adjusting daily loaf output depending on wholesale selling prices", "the schedule of quantities suppliers are ready and capable of producing and selling at each price"),
    ]
    clue, correct = rng.choice(firms)
    distractors = [
        "the quantity households wish they could afford even with zero income",
        "government welfare grants paid directly to retired citizens",
        "the physical depreciation of unused machinery inside a closed factory",
    ]
    prompt = f"In Price Theory, **supply**—such as *{clue}*—is defined as:"
    sol = f"- **Supply:** {correct.capitalize()}."
    return make_question(
        rng=rng,
        subskill="12_supply_definition_willing_and_able",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct.capitalize(),
        sample_answer=correct.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Select accurate supply definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for producers' willingness + ability across prices.",
        hints={
            "tier_1": "Supply comes from the producer/seller side of the market.",
            "tier_2": "Look for 'willing and able to offer for sale at different prices'.",
            "tier_3": correct.capitalize(),
        },
        misconception_tags=["defines_supply_as_consumer_desire"],
        options=[correct.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_13_law_of_supply_direct_relationship(rng: random.Random, mode: str) -> Dict[str, Any]:
    items = [
        ("artisan leather sandals", 180, 300, 320, 650),
        ("locally assembled bicycles", 1400, 200, 2200, 500),
        ("bagged mielie meal (10kg)", 95, 400, 145, 780),
        ("solar study lanterns", 120, 350, 210, 720),
    ]
    item, p1, q1, p2, q2 = rng.choice(items)
    prompt = (
        f"As the market price of {item} climbs from {fmt_zar(p1)} to {fmt_zar(p2)} (*ceteris paribus*), "
        f"producers increase quantity supplied from {q1} to {q2} units.\n\n"
        f"(a) State the **Law of Supply**.\n"
        f"(b) State whether price and quantity supplied move in a **direct** or **inverse** relationship, and state the slope direction of the `S` curve."
    )
    ans = "As price rises, quantity supplied rises (and as price falls, quantity supplied falls), ceteris paribus; direct (positive) relationship; slopes upward from bottom-left to top-right"
    sol = (
        f"**(a) Law of Supply:** *Ceteris paribus*, the higher the price of a good, the greater the quantity supplied; the lower the price, the smaller the quantity supplied.\n"
        f"**(b) Direct Link & Slope:** Price and quantity supplied move together (**direct/positive** relationship), producing an `S` curve sloping **upward from bottom-left to top-right**."
    )
    return make_question(
        rng=rng,
        subskill="13_law_of_supply_direct_relationship",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "State Law of Supply accurately", "marks": 2, "type": "A"},
            {"step": "Identify direct/positive link + upward slope", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Law of Supply; 2 marks for direct link + upward slope.",
        hints={
            "tier_1": "Check whether P and Qs rise together.",
            "tier_2": "Same direction = direct/positive relationship = upward slope.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_supply_curve_slopes_downward"],
    )


def _build_14_reading_supply_schedule_values(rng: random.Random, mode: str) -> Dict[str, Any]:
    goods = ["Skateboards", "Keyrings", "Bread Loaves", "Solar Lamps"]
    item = rng.choice(goods)
    p0 = rng.choice([50, 100, 150])
    dp = rng.choice([50, 100])
    q0 = rng.choice([200, 300, 400])
    dq = rng.choice([150, 200, 250])
    rows_data = [(p0 + i * dp, q0 + i * dq) for i in range(4)]
    headers = [f"Price per {item[:-1]} (R)", "Quantity Supplied (Qs)"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [f"| Price per {item[:-1]} (R) | Quantity Supplied (Qs) |", "|---|---|"]
    req_rows = [1, 3] if rng.random() < 0.5 else [2, 3]
    for r_idx, (p, q) in enumerate(rows_data, start=1):
        p_str, q_str = f"R{p}", str(q)
        req_q = (r_idx - 1) in req_rows
        rows_ui.append([
            {"coordinate": f"R{r_idx}C0", "value": p_str, "type": "given", "editable": False},
            {"coordinate": f"R{r_idx}C1", "value": "" if req_q else q_str, "type": "required" if req_q else "given", "editable": req_q},
        ])
        if req_q:
            correct_map[f"R{r_idx}C1"] = q_str
            cell_hints[f"R{r_idx}C1"] = f"Every R{dp} price increase raises Quantity Supplied linearly by {dq} units."
        md_lines.append(f"| {p_str} | {q_str} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="14_reading_supply_schedule_values",
        question_type="table_completion",
        prompt=f"Complete the linear **Supply Schedule** for **{item}** using the constant supply step.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Completed Linear Supply Schedule ({item}):**\n\n- Each +R{dp} increase adds +{dq} units supplied.\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k} = {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per completed supply cell.",
        hints={
            "tier_1": "Observe how much Qs increases per price step.",
            "tier_2": f"Add +{dq} units for each +R{dp} price rise.",
            "tier_3": md_table,
        },
        misconception_tags=["subtracts_step_on_supply_schedule"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "price", "label": headers[0]}, {"key": "qs", "label": headers[1]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_15_interpreting_supply_curve_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    item = rng.choice(["Jerseys", "Kettles", "Tinned Tomatoes", "Bicycles"])
    p_step = rng.choice([50, 100])
    max_p = p_step * 5
    q_step = rng.choice([150, 200])
    max_q = q_step * 5
    s_pts = [(q_step, p_step), (2 * q_step, 2 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 4 * p_step)]
    q_ans, p_ask = rng.choice(s_pts)
    rev = p_ask * q_ans
    diagram = svg_market_graph(title=f"Supply Curve for {item}", max_q=max_q, max_p=max_p, s_pts=s_pts)
    prompt = (
        f"Study the Supply Curve `S` for **{item}** (passing through `({q_step}; R{p_step})`, `({2 * q_step}; R{2 * p_step})`, `({3 * q_step}; R{3 * p_step})`, `({4 * q_step}; R{4 * p_step})`).\n\n"
        f"(a) Read the quantity producers offer for sale at **R{p_ask}**.\n"
        f"(b) Calculate gross revenue if all {q_ans} supplied units sell at R{p_ask}."
    )
    ans = f"Qs = {q_ans} units; Gross revenue = {fmt_zar(rev)}"
    sol = (
        f"**(a) Quantity Supplied:** At **R{p_ask}**, reading across to curve `S` gives **Qs = {q_ans} units**.\n"
        f"**(b) Gross Revenue:** ${fmt_zar(p_ask)} \\times {q_ans} = {fmt_zar(rev)}$"
    )
    return make_question(
        rng=rng,
        subskill="15_interpreting_supply_curve_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Read Qs = {q_ans} at R{p_ask}", "marks": 2, "type": "A"},
            {"step": f"Calculate revenue {fmt_zar(rev)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for reading Qs; 2 marks for Price * Qs multiplication.",
        hints={
            "tier_1": f"Locate R{p_ask} on the Y-axis and move right to curve S.",
            "tier_2": "Multiply unit price by quantity supplied.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_supply_slope_with_demand_slope"],
        diagram_spec=diagram,
    )


def _build_16_supply_change_movement_along_curve(rng: random.Random, mode: str) -> Dict[str, Any]:
    p1 = rng.choice([120, 150, 200])
    p2 = p1 + rng.choice([40, 60, 80])
    q1 = rng.choice([300, 400, 500])
    q2 = q1 + rng.choice([120, 180, 240])
    dqs = q2 - q1
    prompt = (
        f"When the market price of locally roasted coffee rises from {fmt_zar(p1)} to {fmt_zar(p2)} per bag (*ceteris paribus*), "
        f"roasteries expand output supplied from {q1} to {q2} bags.\n\n"
        f"(a) Calculate the increase in quantity supplied.\n"
        f"(b) State whether this represents a **movement along** the supply curve or a **shift of** the supply curve, and explain why."
    )
    ans = f"+{dqs} bags; movement upward along the existing supply curve because only the product's own price changed"
    sol = (
        f"**(a) Quantity Supplied Increase:** ${q2} - {q1} = +{dqs}$ bags.\n"
        f"**(b) Movement Along S:** Because non-price costs/technology remained constant and only the **own selling price** increased, firms move upward along the same `S` curve."
    )
    return make_question(
        rng=rng,
        subskill="16_supply_change_movement_along_curve",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate +{dqs} bags", "marks": 2, "type": "A"},
            {"step": "Identify movement along S + own-price justification", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for change in Qs; 2 marks for movement-along explanation.",
        hints={
            "tier_1": "Subtract initial Qs from new Qs.",
            "tier_2": "Own-price changes move along a curve; cost/technology changes shift the curve.",
            "tier_3": ans,
        },
        misconception_tags=["calls_own_price_supply_expansion_a_rightward_shift"],
    )


def _build_17_non_price_determinants_shifting_supply(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("a 25% spike in commercial electricity and diesel generator costs", "higher input/production costs shifting Supply leftward"),
        ("high-speed automated bottling robotics cutting per-unit packaging time in half", "technological improvement lowering unit cost and shifting Supply rightward"),
        ("severe prolonged drought across maize-growing districts", "adverse natural/weather conditions reducing supply and shifting Supply leftward"),
        ("three new competing bakeries opening in the same town", "more sellers entering the market, shifting Supply rightward"),
    ]
    event, outcome = rng.choice(cases)
    distractors = [
        "buyers suddenly preferring tea over coffee while costs stay unchanged",
        "the product's own market price moving from R40 to R45",
        "households receiving higher overtime salaries at banks",
    ]
    prompt = f"In Price Theory, *{event}* is a non-price determinant causing:"
    sol = f"- **Supply Effect:** {outcome.capitalize()}."
    return make_question(
        rng=rng,
        subskill="17_non_price_determinants_shifting_supply",
        question_type="mcq",
        prompt=prompt,
        correct_answer=outcome.capitalize(),
        sample_answer=outcome.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify accurate non-price supply shift", "marks": 2, "type": "A"}],
        marking_guide="2 marks for correct supply-shifter direction.",
        hints={
            "tier_1": "Check whether the event alters producers' costs/capacity rather than buyer wants.",
            "tier_2": "Lower costs/better tech/more firms shift S right; higher costs/droughts shift S left.",
            "tier_3": outcome.capitalize(),
        },
        misconception_tags=["confuses_supply_determinants_with_demand_tastes"],
        options=[outcome.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_18_technology_and_cost_cut_supply_shift(rng: random.Random, mode: str) -> Dict[str, Any]:
    old_cost = rng.choice([80, 100, 120])
    cut_pct = rng.choice([20, 25])
    new_cost = old_cost * (1 - cut_pct / 100.0)
    q_before = rng.choice([400, 500, 600])
    q_after = q_before + rng.choice([150, 200, 250])
    prompt = (
        f"New precision sewing machines cut a uniform manufacturer's cost per blazer by {cut_pct}% from {fmt_zar(old_cost)}. "
        f"At the unchanged selling price of R300, monthly supply jumps from {q_before} to {q_after} blazers.\n\n"
        f"(a) Calculate the new unit production cost.\n"
        f"(b) State the exact direction the supply curve shifts and calculate the extra supply at R300."
    )
    extra_q = q_after - q_before
    ans = f"New unit cost = {fmt_zar(new_cost)}; Supply curve shifts rightward (+{extra_q} blazers at R300)"
    sol = (
        f"**(a) New Unit Cost:** ${fmt_zar(old_cost)} \\times (1 - 0.{cut_pct}) = {fmt_zar(new_cost)}$\n"
        f"**(b) Supply Shift:** Lower cost increases profit per unit at every price, shifting the `S` curve **rightward** by **+{extra_q} blazers** at R300."
    )
    return make_question(
        rng=rng,
        subskill="18_technology_and_cost_cut_supply_shift",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate new unit cost {fmt_zar(new_cost)}", "marks": 2, "type": "A"},
            {"step": f"Identify rightward shift and +{extra_q} blazers", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for new unit cost; 2 marks for rightward shift + extra units.",
        hints={
            "tier_1": f"Reduce {fmt_zar(old_cost)} by {cut_pct}%.",
            "tier_2": "Higher Qs at the exact same price signals a rightward shift of Supply.",
            "tier_3": ans,
        },
        misconception_tags=["shifts_supply_leftward_when_costs_fall"],
    )


def _build_19_input_cost_or_loadshedding_supply_shift(rng: random.Random, mode: str) -> Dict[str, Any]:
    shocks = [
        ("frequent electricity outages forcing bakeries to buy diesel fuel", 45, 58),
        ("imported timber shortages raising plank prices for furniture shops", 140, 185),
        ("higher flour and yeast bills for township bread producers", 8, 12),
    ]
    cause, old_c, new_c = rng.choice(shocks)
    pct_up = round(((new_c - old_c) / old_c) * 100, 1)
    prompt = (
        f"Due to **{cause}**, a small firm's unit input cost climbs from {fmt_zar(old_c)} to {fmt_zar(new_c)}.\n\n"
        f"(a) Calculate the percentage increase in unit cost (to 1 decimal place).\n"
        f"(b) Explain which direction the firm's **supply curve** shifts and what happens to market equilibrium price (*ceteris paribus*)."
    )
    ans = f"+{fmt_dec(pct_up)}% cost rise; Supply shifts leftward (decreases), pushing equilibrium price upward"
    sol = (
        f"**(a) Cost Increase:** $\\frac{{{new_c - old_c}}}{{{old_c}}} \\times 100 = {fmt_dec(pct_up)}\\%$\n"
        f"**(b) Market Impact:** Higher production costs shrink profit margins, shifting the `S` curve **leftward** (less supplied at every price), causing equilibrium price to **rise** and equilibrium quantity to **fall**."
    )
    return make_question(
        rng=rng,
        subskill="19_input_cost_or_loadshedding_supply_shift",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate +{fmt_dec(pct_up)}% cost rise", "marks": 2, "type": "A"},
            {"step": "State leftward S shift + higher Pe", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage; 2 marks for leftward supply shift + higher price.",
        hints={
            "tier_1": "Divide the Rand cost increase by the original unit cost * 100.",
            "tier_2": "Costlier production makes firms supply less -> S shifts left -> Pe rises.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_higher_input_costs_shift_demand_instead_of_supply"],
    )


def _build_20_tax_vs_subsidy_impact_on_supply(rng: random.Random, mode: str) -> Dict[str, Any]:
    base_cost = rng.choice([100, 120, 160])
    subsidy = rng.choice([20, 30])
    tax = rng.choice([15, 25])
    net_sub = base_cost - subsidy
    net_tax = base_cost + tax
    prompt = (
        f"Solar-heater assemblers incur a baseline unit cost of {fmt_zar(base_cost)}.\n"
        f"- **Policy Option 1:** Government grants a production **subsidy** of {fmt_zar(subsidy)} per unit.\n"
        f"- **Policy Option 2:** Government levies an indirect manufacturing **tax** of {fmt_zar(tax)} per unit.\n\n"
        f"(a) Calculate the effective producer unit cost under Option 1 and Option 2.\n"
        f"(b) State the shift direction of the supply curve (`S`) under each policy."
    )
    ans = f"Subsidy cost = {fmt_zar(net_sub)} (S shifts right); Tax cost = {fmt_zar(net_tax)} (S shifts left)"
    sol = (
        f"**(a) Net Costs:**\n"
        f"- **Subsidy (Option 1):** ${fmt_zar(base_cost)} - {fmt_zar(subsidy)} = {fmt_zar(net_sub)}$\n"
        f"- **Indirect Tax (Option 2):** ${fmt_zar(base_cost)} + {fmt_zar(tax)} = {fmt_zar(net_tax)}$\n\n"
        f"**(b) Supply Shifts:** Subsidy lowers cost so `S` shifts **rightward** (supply rises); indirect tax raises cost so `S` shifts **leftward** (supply falls)."
    )
    return make_question(
        rng=rng,
        subskill="20_tax_vs_subsidy_impact_on_supply",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Option 1 {fmt_zar(net_sub)} and Option 2 {fmt_zar(net_tax)}", "marks": 2, "type": "A"},
            {"step": "Correct shift directions (right for subsidy, left for tax)", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for net costs; 2 marks for right/left shift directions.",
        hints={
            "tier_1": "Subsidies subtract from producer cost; indirect taxes add to producer cost.",
            "tier_2": "Lower cost -> S shifts right; higher cost -> S shifts left.",
            "tier_3": ans,
        },
        misconception_tags=["reverses_subsidy_and_tax_shift_directions"],
    )


def _build_21_market_equilibrium_definition_condition(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("every loaf of brown bread baked for R16 is bought by shoppers with zero unsold loaves and zero unserved buyers", "the price at which quantity demanded equals quantity supplied (Qd = Qs), clearing the market with zero surplus or shortage"),
        ("800 pairs of trainers are offered at R500 and buyers purchase all 800 pairs willingly", "market balance where buyers' planned purchases match sellers' planned sales at one stable price"),
        ("neither upward bidding by frustrated buyers nor price-cutting discounts by stuck sellers occur", "a state of market rest where demand equals supply and price faces no pressure to change"),
    ]
    obs, correct = rng.choice(cases)
    distractors = [
        "the highest price sellers ever charge even if zero consumers buy",
        "a situation where unsold surplus piles up endlessly every week",
        "the price level where government freezes wages regardless of shortages",
    ]
    prompt = f"Which definition accurately describes **market equilibrium**, as seen when *{obs}*?"
    sol = f"- **Market Equilibrium:** {correct.capitalize()}."
    return make_question(
        rng=rng,
        subskill="21_market_equilibrium_definition_condition",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct.capitalize(),
        sample_answer=correct.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify Qd = Qs market clearing definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for Qd = Qs market balance condition.",
        hints={
            "tier_1": "Look for exact balance between buyers and sellers.",
            "tier_2": "Equilibrium requires Qd = Qs with zero excess demand or excess supply.",
            "tier_3": correct.capitalize(),
        },
        misconception_tags=["equates_equilibrium_with_lowest_possible_price"],
        options=[correct.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_22_identifying_equilibrium_from_combined_schedule(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_base = rng.choice([150, 200])
    step_p = rng.choice([50, 100])
    q_eq = rng.choice([600, 800, 900])
    step_q = rng.choice([100, 200])
    # 5 price rows centered at index 2 -> P_eq = p_base + 2*step_p
    rows_raw = []
    for idx in range(5):
        p = p_base + idx * step_p
        qd = q_eq + (2 - idx) * step_q
        qs = q_eq + (idx - 2) * step_q
        diff = qs - qd
        st = "Equilibrium" if diff == 0 else (f"Shortage ({abs(diff)})" if diff < 0 else f"Surplus ({diff})")
        rows_raw.append((f"R{p}", str(qd), str(qs), st))

    headers = ["Price", "Quantity Demanded (Qd)", "Quantity Supplied (Qs)", "Market Status"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Price | Quantity Demanded (Qd) | Quantity Supplied (Qs) | Market Status |", "|---|---|---|---|"]
    req_targets = [(1, 3), (3, 3), (4, 3)] if rng.random() < 0.5 else [(0, 3), (2, 3), (4, 3)]
    for r_idx, vals in enumerate(rows_raw, start=1):
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = (r_idx - 1, c_idx) in req_targets
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Compare Qs vs Qd: Qd > Qs = Shortage (Qd-Qs); Qs > Qd = Surplus (Qs-Qd); equal = Equilibrium."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
    md_table = "\n".join(md_lines)
    p_eq = p_base + 2 * step_p
    return make_question(
        rng=rng,
        subskill="22_identifying_equilibrium_from_combined_schedule",
        question_type="table_completion",
        prompt=f"Complete the **Market Equilibrium Schedule** status cells (Equilibrium, `Shortage (units)`, or `Surplus (units)`).",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Equilibrium occurs at R{p_eq} (`Qd = Qs = {q_eq}`):**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each correct Market Status entry.",
        hints={
            "tier_1": "Check whether Qd > Qs or Qs > Qd on each row.",
            "tier_2": "Write exact difference inside parentheses, or Equilibrium when Qd = Qs.",
            "tier_3": md_table,
        },
        misconception_tags=["writes_surplus_when_demand_exceeds_supply"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "p", "label": headers[0]}, {"key": "qd", "label": headers[1]}, {"key": "qs", "label": headers[2]}, {"key": "st", "label": headers[3]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_23_identifying_equilibrium_from_svg_graph(rng: random.Random, mode: str) -> Dict[str, Any]:
    item = rng.choice(["Skateboards", "Keyrings", "School Blazers", "Basketballs"])
    p_step = rng.choice([50, 100, 150])
    q_step = rng.choice([200, 300])
    max_p, max_q = p_step * 5, q_step * 5
    eq_q, eq_p = 3 * q_step, 3 * p_step
    d_pts = [(q_step, 5 * p_step), (2 * q_step, 4 * p_step), (eq_q, eq_p), (4 * q_step, 2 * p_step), (5 * q_step, p_step)]
    s_pts = [(q_step, p_step), (2 * q_step, 2 * p_step), (eq_q, eq_p), (4 * q_step, 4 * p_step), (5 * q_step, 5 * p_step)]
    tr = eq_p * eq_q
    diagram = svg_market_graph(
        title=f"Market Equilibrium for {item}",
        max_q=max_q,
        max_p=max_p,
        d_pts=d_pts,
        s_pts=s_pts,
        eq_pt=(eq_q, eq_p, "E"),
    )
    prompt = (
        f"Study the Demand (`D`) and Supply (`S`) curves for **{item}** intersecting at point **E**.\n\n"
        f"(a) Read the **equilibrium price (`Pe`)** and **equilibrium quantity (`Qe`)**.\n"
        f"(b) Calculate total market turnover (`Pe * Qe`) at equilibrium."
    )
    ans = f"Pe = {fmt_zar(eq_p)}; Qe = {eq_q} units; Turnover = {fmt_zar(tr)}"
    sol = (
        f"**(a) Equilibrium Intersection E:**\n"
        f"- **Equilibrium Price (`Pe`):** **{fmt_zar(eq_p)}**\n"
        f"- **Equilibrium Quantity (`Qe`):** **{eq_q} units**\n\n"
        f"**(b) Market Turnover:** ${fmt_zar(eq_p)} \\times {eq_q} = {fmt_zar(tr)}$"
    )
    return make_question(
        rng=rng,
        subskill="23_identifying_equilibrium_from_svg_graph",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Read Pe = {fmt_zar(eq_p)} and Qe = {eq_q}", "marks": 2, "type": "A"},
            {"step": f"Calculate turnover {fmt_zar(tr)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="1+1 marks for reading Pe and Qe; 2 marks for multiplying them.",
        hints={
            "tier_1": "Locate intersection point E where D crosses S.",
            "tier_2": "Read price from vertical axis and quantity from horizontal axis, then multiply.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_pe_and_qe_coordinates"],
        diagram_spec=diagram,
    )


def _build_24_calculating_equilibrium_revenue_and_units(rng: random.Random, mode: str) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4])
    d = rng.choice([1, 2, 3])
    p_eq = rng.choice([20, 30, 40, 50])
    q_eq = rng.choice([120, 150, 180, 240])
    a = q_eq + b * p_eq
    c = q_eq - d * p_eq
    rev = p_eq * q_eq
    prompt = (
        f"A local farmers' market satisfies two linear equations in Price (`P` in Rand):\n"
        f"- Demand: `Qd = {a} - {b}P`\n"
        f"- Supply: `Qs = {c} + {d}P`\n\n"
        f"(a) Set `Qd = Qs` to solve algebraically for the **equilibrium price (`Pe`)** and **equilibrium quantity (`Qe`)**.\n"
        f"(b) Calculate total farmers' revenue at equilibrium."
    )
    ans = f"Pe = {fmt_zar(p_eq)}; Qe = {q_eq} units; Total revenue = {fmt_zar(rev)}"
    sol = (
        f"**(a) Solve `Qd = Qs`:**\n"
        f"- ${a} - {b}P = {c} + {d}P$\n"
        f"- ${a - c} = {b + d}P \\implies P_e = \\frac{{{a - c}}}{{{b + d}}} = {fmt_zar(p_eq)}$\n"
        f"- $Q_e = {a} - {b}({p_eq}) = {q_eq}\\text{{ units}}$\n\n"
        f"**(b) Revenue:** ${fmt_zar(p_eq)} \\times {q_eq} = {fmt_zar(rev)}$"
    )
    return make_question(
        rng=rng,
        subskill="24_calculating_equilibrium_revenue_and_units",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Set Qd = Qs and solve Pe = {fmt_zar(p_eq)}", "marks": 2, "type": "M"},
            {"step": f"Substitute to get Qe = {q_eq}", "marks": 1, "type": "CA"},
            {"step": f"Compute revenue {fmt_zar(rev)}", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for solving Pe; 1 mark for Qe; 2 marks for TR = Pe * Qe.",
        hints={
            "tier_1": "Equate Qd and Qs and collect P terms on one side.",
            "tier_2": "Substitute Pe back into either equation to get Qe, then multiply Pe * Qe.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_slopes_instead_of_adding_when_transposing"],
    )


def _build_25_market_disequilibrium_surplus_calculation(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_step = rng.choice([50, 100])
    q_step = rng.choice([200, 250])
    max_p, max_q = 5 * p_step, 5 * q_step
    eq_q, eq_p = 3 * q_step, 3 * p_step
    p_high = 4 * p_step
    qd_high = 2 * q_step
    qs_high = 4 * q_step
    surplus = qs_high - qd_high
    d_pts = [(q_step, 5 * p_step), (2 * q_step, 4 * p_step), (eq_q, eq_p), (4 * q_step, 2 * p_step), (5 * q_step, p_step)]
    s_pts = [(q_step, p_step), (2 * q_step, 2 * p_step), (eq_q, eq_p), (4 * q_step, 4 * p_step), (5 * q_step, 5 * p_step)]
    diagram = svg_market_graph(
        title="Market Disequilibrium: Price Above Equilibrium",
        max_q=max_q,
        max_p=max_p,
        d_pts=d_pts,
        s_pts=s_pts,
        eq_pt=(eq_q, eq_p, "E"),
        h_line_p=(p_high, f"High Price R{p_high} (Qd={qd_high}, Qs={qs_high})", "#d97706"),
    )
    prompt = (
        f"Inspect the Price Theory model where equilibrium `E` lies at `({eq_q}; R{eq_p})`, "
        f"but sellers set a higher price of **R{p_high}** (`Qd = {qd_high}`, `Qs = {qs_high}`).\n\n"
        f"(a) Calculate the exact **excess supply (market surplus)** at R{p_high}.\n"
        f"(b) Explain how market forces push the price back toward R{eq_p}."
    )
    ans = f"Surplus = {surplus} units; unsold stock forces sellers to cut prices toward R{eq_p}, raising Qd and reducing Qs until Qd = Qs"
    sol = (
        f"**(a) Surplus Calculation:** $\\text{{Surplus}} = Q_s - Q_d = {qs_high} - {qd_high} = {surplus}$ unsold units.\n"
        f"**(b) Downward Price Adjustment:** Holding unsold stock forces sellers to offer discounts, lowering the price from **R{p_high}** back down to **R{eq_p}**, clearing the market."
    )
    return make_question(
        rng=rng,
        subskill="25_market_disequilibrium_surplus_calculation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate surplus {surplus} units (Qs - Qd)", "marks": 2, "type": "A"},
            {"step": "Explain downward price pressure back to equilibrium", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Qs - Qd; 2 marks for explaining price drop mechanism.",
        hints={
            "tier_1": "At a high price, sellers supply more than buyers purchase.",
            "tier_2": f"Compute Qs - Qd = {qs_high} - {qd_high}.",
            "tier_3": ans,
        },
        misconception_tags=["calls_excess_supply_a_shortage"],
        diagram_spec=diagram,
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_price_theory_meaning_market_forces": _build_01_price_theory_meaning_market_forces,
    "02_effective_demand_willing_and_able": _build_02_effective_demand_willing_and_able,
    "03_law_of_demand_inverse_relationship": _build_03_law_of_demand_inverse_relationship,
    "04_ceteris_paribus_assumption_meaning": _build_04_ceteris_paribus_assumption_meaning,
    "05_reading_demand_schedule_values": _build_05_reading_demand_schedule_values,
    "06_graphing_axes_price_y_quantity_x": _build_06_graphing_axes_price_y_quantity_x,
    "07_interpreting_demand_curve_svg": _build_07_interpreting_demand_curve_svg,
    "08_demand_change_movement_along_curve": _build_08_demand_change_movement_along_curve,
    "09_non_price_determinants_shifting_demand": _build_09_non_price_determinants_shifting_demand,
    "10_substitutes_price_cross_effect_demand": _build_10_substitutes_price_cross_effect_demand,
    "11_complements_price_cross_effect_demand": _build_11_complements_price_cross_effect_demand,
    "12_supply_definition_willing_and_able": _build_12_supply_definition_willing_and_able,
    "13_law_of_supply_direct_relationship": _build_13_law_of_supply_direct_relationship,
    "14_reading_supply_schedule_values": _build_14_reading_supply_schedule_values,
    "15_interpreting_supply_curve_svg": _build_15_interpreting_supply_curve_svg,
    "16_supply_change_movement_along_curve": _build_16_supply_change_movement_along_curve,
    "17_non_price_determinants_shifting_supply": _build_17_non_price_determinants_shifting_supply,
    "18_technology_and_cost_cut_supply_shift": _build_18_technology_and_cost_cut_supply_shift,
    "19_input_cost_or_loadshedding_supply_shift": _build_19_input_cost_or_loadshedding_supply_shift,
    "20_tax_vs_subsidy_impact_on_supply": _build_20_tax_vs_subsidy_impact_on_supply,
    "21_market_equilibrium_definition_condition": _build_21_market_equilibrium_definition_condition,
    "22_identifying_equilibrium_from_combined_schedule": _build_22_identifying_equilibrium_from_combined_schedule,
    "23_identifying_equilibrium_from_svg_graph": _build_23_identifying_equilibrium_from_svg_graph,
    "24_calculating_equilibrium_revenue_and_units": _build_24_calculating_equilibrium_revenue_and_units,
    "25_market_disequilibrium_surplus_calculation": _build_25_market_disequilibrium_surplus_calculation,
}
