"""Grade 9 EMS Term 2: Price Theory — Semantic Archetypes 26 to 50."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term2_economy_archetypes_01_25 import fmt_dec, fmt_zar, make_question, svg_market_graph


def _build_26_market_disequilibrium_shortage_calculation(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_step = rng.choice([40, 50, 80])
    q_step = rng.choice([200, 300])
    max_p, max_q = 5 * p_step, 5 * q_step
    eq_q, eq_p = 3 * q_step, 3 * p_step
    p_low = 2 * p_step
    qs_low, qd_low = 2 * q_step, 4 * q_step
    shortage = qd_low - qs_low
    d_pts = [(q_step, 5 * p_step), (2 * q_step, 4 * p_step), (eq_q, eq_p), (4 * q_step, 2 * p_step), (5 * q_step, p_step)]
    s_pts = [(q_step, p_step), (2 * q_step, 2 * p_step), (eq_q, eq_p), (4 * q_step, 4 * p_step), (5 * q_step, 5 * p_step)]
    diagram = svg_market_graph(
        title="Market Disequilibrium: Price Below Equilibrium",
        max_q=max_q,
        max_p=max_p,
        d_pts=d_pts,
        s_pts=s_pts,
        eq_pt=(eq_q, eq_p, "E"),
        h_line_p=(p_low, f"Low Price R{p_low} (Qs={qs_low}, Qd={qd_low})", "#dc2626"),
    )
    prompt = (
        f"Study the market curves intersecting at `E({eq_q}; R{eq_p})` when price temporarily rests at **R{p_low}** "
        f"(`Qs = {qs_low}`, `Qd = {qd_low}`).\n\n"
        f"(a) Calculate the exact **excess demand (market shortage)** at R{p_low}.\n"
        f"(b) Explain how frustrated buyers restore equilibrium at R{eq_p}."
    )
    ans = f"Shortage = {shortage} units; buyers bid price upward toward R{eq_p}, encouraging higher supply and fewer purchases until Qd = Qs"
    sol = (
        f"**(a) Shortage Calculation:** $\\text{{Shortage}} = Q_d - Q_s = {qd_low} - {qs_low} = {shortage}$ units unfulfilled.\n"
        f"**(b) Upward Price Pressure:** Competing buyers willing to pay more bid prices upward from **R{p_low}** to **R{eq_p}**, expanding Qs and trimming Qd to equilibrium."
    )
    return make_question(
        rng=rng,
        subskill="26_market_disequilibrium_shortage_calculation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate shortage {shortage} units (Qd - Qs)", "marks": 2, "type": "A"},
            {"step": "Explain upward bidding back to equilibrium", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Qd - Qs; 2 marks for upward price mechanism.",
        hints={
            "tier_1": "At a low price, buyers want more than firms offer.",
            "tier_2": f"Compute Qd - Qs = {qd_low} - {qs_low}.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_qd_from_qs_and_calls_negative_value_a_surplus"],
        diagram_spec=diagram,
    )


def _build_27_price_adjustment_mechanism_to_equilibrium(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("piles of unsold winter jackets remain on racks because the store price is R400 above equilibrium", "surplus -> sellers cut prices -> Qd rises and Qs falls -> equilibrium restored"),
        ("queues form outside bakeries every morning because fixed prices sit R8 below equilibrium", "shortage -> buyers bid price up -> Qs rises and Qd falls -> equilibrium restored"),
        ("warehouse stockpiles of oranges grow due to an overly high initial price", "excess supply -> downward discounting pressure until Qd equals Qs"),
    ]
    clue, chain = rng.choice(cases)
    distractors = [
        "buyers demand even fewer jackets as discounts widen",
        "producers throw surplus output into rivers so price doubles further",
        "the market stays permanently locked with zero price response",
    ]
    prompt = f"If *{clue}*, which self-correcting adjustment sequence restores market equilibrium?"
    sol = f"- **Self-Correcting Mechanism:** {chain}."
    return make_question(
        rng=rng,
        subskill="27_price_adjustment_mechanism_to_equilibrium",
        question_type="mcq",
        prompt=prompt,
        correct_answer=chain,
        sample_answer=chain,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify correct disequilibrium adjustment sequence", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurate price-clearing adjustment path.",
        hints={
            "tier_1": "First identify whether there is unsold surplus or unfilled queues (shortage).",
            "tier_2": "Surpluses push prices down; shortages push prices up.",
            "tier_3": chain,
        },
        misconception_tags=["thinks_surplus_pushes_prices_upward"],
        options=[chain] + distractors,
        duration_mins=2,
    )


def _build_28_movement_along_vs_curve_shift_classification(rng: random.Random, mode: str) -> Dict[str, Any]:
    events = [
        ("The price of the product itself rises from R50 to R70.", "Movement along curve", "Upward along D / S"),
        ("Consumer household incomes surge across the city.", "Shift of Demand curve", "Rightward (D -> D1)"),
        ("New automated machinery cuts factory unit cost by 30%.", "Shift of Supply curve", "Rightward (S -> S1)"),
        ("Severe drought damages vegetable harvests nationwide.", "Shift of Supply curve", "Leftward (S -> S2)"),
        ("Price of a key substitute drops sharply.", "Shift of Demand curve", "Leftward (D -> D2)"),
    ]
    picked = rng.sample(events, 3)
    headers = ["Market Event", "Movement vs Shift", "Direction"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Market Event | Movement vs Shift | Direction |", "|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_col = rng.choice([1, 2])
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx == req_col
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Own price -> Movement along curve; Non-price factor -> Shift of D or S."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="28_movement_along_vs_curve_shift_classification",
        question_type="table_completion",
        prompt="Classify each market event into Movement along a curve vs Shift of Demand/Supply, and specify its direction.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Movement vs Shift Classification:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per classification or direction cell.",
        hints={
            "tier_1": "Ask: Did the good's own price change, or did an external factor change?",
            "tier_2": "External buyer factors shift D; external producer cost/weather factors shift S.",
            "tier_3": md_table,
        },
        misconception_tags=["treats_own_price_change_as_curve_shift"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "ev", "label": headers[0]}, {"key": "type", "label": headers[1]}, {"key": "dir", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_29_demand_increase_shift_right_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_step = rng.choice([20, 50])
    q_step = rng.choice([100, 150])
    max_p, max_q = 6 * p_step, 6 * q_step
    d1 = [(q_step, 5 * p_step), (2 * q_step, 4 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 2 * p_step), (5 * q_step, p_step)]
    s1 = [(q_step, p_step), (2 * q_step, 2 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 4 * p_step), (5 * q_step, 5 * p_step)]
    d_right = [(q + 2 * q_step, p) for q, p in d1 if q + 2 * q_step <= max_q]
    e0 = (3 * q_step, 3 * p_step, "E0")
    e1 = (4 * q_step, 4 * p_step, "E1")
    diagram = svg_market_graph(
        title="Rightward Demand Shift (D -> D1)",
        max_q=max_q,
        max_p=max_p,
        d_pts=d1,
        s_pts=s1,
        d2_pts=d_right,
        eq_pt=e0,
        eq2_pt=e1,
        d2_label="D1",
    )
    dp = e1[1] - e0[1]
    dq = e1[0] - e0[0]
    prompt = (
        f"Study the rightward demand shift from `D` (`E0: {e0[0]}; R{e0[1]}`) to `D1` (`E1: {e1[0]}; R{e1[1]}`).\n\n"
        f"(a) Calculate the increase in equilibrium price and equilibrium quantity.\n"
        f"(b) Give ONE realistic non-price event in South Africa that causes `D` to shift right to `D1`."
    )
    ans = f"Pe rises by {fmt_zar(dp)} (to {fmt_zar(e1[1])}); Qe rises by {dq} units (to {e1[0]}); caused by higher household income, population growth, or successful advertising"
    sol = (
        f"**(a) Equilibrium Changes:**\n"
        f"- $\\Delta P_e = {fmt_zar(e1[1])} - {fmt_zar(e0[1])} = +{fmt_zar(dp)}$\n"
        f"- $\\Delta Q_e = {e1[0]} - {e0[0]} = +{dq}\\text{{ units}}$\n\n"
        f"**(b) Possible Causes:** Rising consumer incomes, successful marketing, population influx, or higher prices of a substitute product."
    )
    return make_question(
        rng=rng,
        subskill="29_demand_increase_shift_right_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Compute +{fmt_zar(dp)} and +{dq} units", "marks": 2, "type": "A"},
            {"step": "Provide valid rightward demand shifter", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for deltas; 2 marks for valid demand shifter.",
        hints={
            "tier_1": "Compare coordinates of E1 against E0.",
            "tier_2": "A rightward demand shift increases BOTH Pe and Qe.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_demand_increase_lowers_equilibrium_price"],
        diagram_spec=diagram,
    )


def _build_30_demand_decrease_shift_left_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_step = rng.choice([25, 50])
    q_step = rng.choice([100, 200])
    max_p, max_q = 6 * p_step, 6 * q_step
    d1 = [(2 * q_step, 5 * p_step), (3 * q_step, 4 * p_step), (4 * q_step, 3 * p_step), (5 * q_step, 2 * p_step)]
    s1 = [(q_step, 2 * p_step), (2 * q_step, 3 * p_step), (3 * q_step, 4 * p_step), (4 * q_step, 5 * p_step)]
    # Check intersection: d1 passes (3q,4p),(4q,3p); s1 passes (2q,3p),(3q,4p) -> intersection E0=(3q,4p).
    # Leftward shift by 2q: d2 passes (q,4p),(2q,3p),(3q,2p) intersecting s1 at E1=(2q,3p)!
    d_left = [(q - 2 * q_step, p) for q, p in d1 if q - 2 * q_step >= 0] + [(3 * q_step, 2 * p_step)]
    e0 = (3 * q_step, 4 * p_step, "E0")
    e1 = (2 * q_step, 3 * p_step, "E1")
    rev0 = e0[0] * e0[1]
    rev1 = e1[0] * e1[1]
    diagram = svg_market_graph(
        title="Leftward Demand Shift (D -> D2)",
        max_q=max_q,
        max_p=max_p,
        d_pts=d1,
        s_pts=s1,
        d2_pts=[(q_step, 4 * p_step), (2 * q_step, 3 * p_step), (3 * q_step, 2 * p_step)],
        eq_pt=e0,
        eq2_pt=e1,
        d2_label="D2",
    )
    prompt = (
        f"Observe the leftward demand shift from `D` (`E0: {e0[0]}; R{e0[1]}`) to `D2` (`E1: {e1[0]}; R{e1[1]}`).\n\n"
        f"(a) Describe what happens to both equilibrium price and equilibrium quantity.\n"
        f"(b) Calculate the total Rand fall in market revenue between `E0` and `E1`."
    )
    rev_drop = rev0 - rev1
    ans = f"Pe falls (R{e0[1]} -> R{e1[1]}) and Qe falls ({e0[0]} -> {e1[0]}); Revenue drops by {fmt_zar(rev_drop)}"
    sol = (
        f"**(a) Direction:** Both **Pe falls** (`R{e0[1]} -> R{e1[1]}`) and **Qe falls** (`{e0[0]} -> {e1[0]}`).\n"
        f"**(b) Revenue Drop:**\n"
        f"- Before (`E0`): ${e0[0]} \\times {fmt_zar(e0[1])} = {fmt_zar(rev0)}$\n"
        f"- After (`E1`): ${e1[0]} \\times {fmt_zar(e1[1])} = {fmt_zar(rev1)}$\n"
        f"- Fall $= {fmt_zar(rev_drop)}$"
    )
    return make_question(
        rng=rng,
        subskill="30_demand_decrease_shift_left_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "State both Pe and Qe decrease", "marks": 2, "type": "A"},
            {"step": f"Calculate revenue drop {fmt_zar(rev_drop)}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Pe/Qe direction; 2 marks for revenue loss.",
        hints={
            "tier_1": "Multiply P * Q at E0 and E1 separately.",
            "tier_2": "A leftward demand shift decreases both price and quantity.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_prices_before_multiplying_quantities"],
        diagram_spec=diagram,
    )


def _build_31_supply_increase_shift_right_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_step = rng.choice([20, 40, 60])
    q_step = rng.choice([100, 150])
    max_p, max_q = 6 * p_step, 6 * q_step
    d1 = [(q_step, 5 * p_step), (2 * q_step, 4 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 2 * p_step)]
    s0 = [(q_step, 3 * p_step), (2 * q_step, 4 * p_step), (3 * q_step, 5 * p_step)]
    s1 = [(2 * q_step, 2 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 4 * p_step)]
    e0 = (2 * q_step, 4 * p_step, "E0")
    e1 = (3 * q_step, 3 * p_step, "E1")
    diagram = svg_market_graph(
        title="Rightward Supply Shift (S -> S1)",
        max_q=max_q,
        max_p=max_p,
        d_pts=d1,
        s_pts=s0,
        s2_pts=s1,
        eq_pt=e0,
        eq2_pt=e1,
        s2_label="S1",
    )
    prompt = (
        f"Study the rightward supply shift from `S` (`E0: {e0[0]}; R{e0[1]}`) to `S1` (`E1: {e1[0]}; R{e1[1]}`).\n\n"
        f"(a) State the exact changes in equilibrium price (`Pe`) and equilibrium quantity (`Qe`).\n"
        f"(b) Explain why consumers benefit from a rightward supply shift."
    )
    ans = f"Pe falls by {fmt_zar(e0[1] - e1[1])} to {fmt_zar(e1[1])}, while Qe rises by {e1[0] - e0[0]} to {e1[0]}; buyers obtain more goods at lower prices"
    sol = (
        f"**(a) Equilibrium Effect:** **Pe drops** from {fmt_zar(e0[1])} to {fmt_zar(e1[1])}, and **Qe increases** from {e0[0]} to {e1[0]} units.\n"
        f"**(b) Consumer Gain:** Improved productivity or lower costs let buyers purchase larger quantities at cheaper prices."
    )
    return make_question(
        rng=rng,
        subskill="31_supply_increase_shift_right_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "State exact fall in Pe and rise in Qe", "marks": 2, "type": "A"},
            {"step": "Explain consumer gain (cheaper + more available)", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Pe/Qe values; 2 marks for consumer benefit.",
        hints={
            "tier_1": "Track coordinates moving from E0 to E1 along unchanged D.",
            "tier_2": "Rightward S lowers Pe and increases Qe.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_supply_increase_raises_market_price"],
        diagram_spec=diagram,
    )


def _build_32_supply_decrease_shift_left_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_step = rng.choice([25, 50, 75])
    q_step = rng.choice([100, 200])
    max_p, max_q = 6 * p_step, 6 * q_step
    d1 = [(2 * q_step, 4 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 2 * p_step), (5 * q_step, p_step)]
    s0 = [(2 * q_step, 2 * p_step), (3 * q_step, 3 * p_step), (4 * q_step, 4 * p_step)]
    s2 = [(q_step, 3 * p_step), (2 * q_step, 4 * p_step), (3 * q_step, 5 * p_step)]
    e0 = (3 * q_step, 3 * p_step, "E0")
    e1 = (2 * q_step, 4 * p_step, "E1")
    diagram = svg_market_graph(
        title="Leftward Supply Shift (S -> S2)",
        max_q=max_q,
        max_p=max_p,
        d_pts=d1,
        s_pts=s0,
        s2_pts=s2,
        eq_pt=e0,
        eq2_pt=e1,
        s2_label="S2",
    )
    pct_p = round(((e1[1] - e0[1]) / e0[1]) * 100, 1)
    prompt = (
        f"Study the leftward supply shift from `S` (`E0: {e0[0]}; R{e0[1]}`) to `S2` (`E1: {e1[0]}; R{e1[1]}`).\n\n"
        f"(a) Calculate the percentage rise in equilibrium price from `E0` to `E1`.\n"
        f"(b) Identify the new equilibrium quantity `Qe` and give ONE cost or climate cause of `S -> S2`."
    )
    ans = f"+{fmt_dec(pct_p)}% price rise (Pe -> {fmt_zar(e1[1])}); Qe drops to {e1[0]}; caused by drought, loadshedding or wage/input cost spike"
    sol = (
        f"**(a) Price Percentage Rise:** $\\frac{{{e1[1]} - {e0[1]}}}{{{e0[1]}}} \\times 100 = {fmt_dec(pct_p)}\\%$\n"
        f"**(b) New Quantity & Cause:** `Qe` drops to **{e1[0]} units**, triggered by higher raw-material/electricity costs, indirect taxes, or drought."
    )
    return make_question(
        rng=rng,
        subskill="32_supply_decrease_shift_left_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate +{fmt_dec(pct_p)}% price jump", "marks": 2, "type": "A"},
            {"step": f"Identify Qe = {e1[0]} + valid leftward S cause", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage; 2 marks for Qe + valid supply shock.",
        hints={
            "tier_1": "Divide price increase by original equilibrium price E0 * 100.",
            "tier_2": "Leftward S shrinks available output and raises price.",
            "tier_3": ans,
        },
        misconception_tags=["reverses_new_and_old_price_in_percentage_change"],
        diagram_spec=diagram,
    )


def _build_33_agricultural_drought_maize_price_shock(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_old = rng.choice([70, 80, 90])
    p_new = p_old + rng.choice([25, 35, 45])
    bags_yr = rng.choice([12, 18, 24])
    extra_yr = (p_new - p_old) * bags_yr
    prompt = (
        f"An El Niño drought in the Free State reduces national maize harvests, shifting maize supply leftward "
        f"and raising the price of a 10 kg bag of mielie meal from {fmt_zar(p_old)} to {fmt_zar(p_new)}.\n\n"
        f"(a) Explain why the **Supply** curve rather than the Demand curve shifts initially.\n"
        f"(b) Calculate the extra annual staple-food expense for a household purchasing {bags_yr} bags per year."
    )
    ans = f"Drought destroys farm output capacity (Supply shifts left); Extra household cost = {fmt_zar(extra_yr)}/year"
    sol = (
        f"**(a) Supply Curve Shift:** Drought restricts farmers' physical ability to grow and harvest maize, shifting the **Supply** curve leftward while household need remains intact.\n"
        f"**(b) Household Impact:** $({fmt_zar(p_new)} - {fmt_zar(p_old)}) \\times {bags_yr} = {fmt_zar(extra_yr)}$ extra per year."
    )
    return make_question(
        rng=rng,
        subskill="33_agricultural_drought_maize_price_shock",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain drought shifts Supply curve left", "marks": 2, "type": "A"},
            {"step": f"Calculate extra annual expense {fmt_zar(extra_yr)}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for supply-shock reasoning; 2 marks for annual budget impact.",
        hints={
            "tier_1": "Weather directly hits crop production (supply side).",
            "tier_2": f"Multiply price increase per bag by {bags_yr} bags.",
            "tier_3": ans,
        },
        misconception_tags=["shifts_demand_curve_on_harvest_failure"],
    )


def _build_34_seasonal_demand_spike_retail_effect(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("January school reopening for school shoes", 280, 350),
        ("cold June snap for electric room heaters", 420, 540),
        ("December coastal holiday boom for guesthouse rooms", 950, 1300),
    ]
    event, p0, p1 = rng.choice(cases)
    pct = round(((p1 - p0) / p0) * 100, 1)
    prompt = (
        f"During the **{event}**, buyer demand jumps, driving equilibrium price up from {fmt_zar(p0)} to {fmt_zar(p1)}.\n\n"
        f"(a) Identify which curve shifted and in which direction.\n"
        f"(b) Calculate the percentage price surge (to 1 decimal place) and state what happens to equilibrium quantity."
    )
    ans = f"Demand curve shifted rightward; Price surged +{fmt_dec(pct)}%; Equilibrium quantity increases"
    sol = (
        f"**(a) Shift:** **Demand curve** shifts **rightward**.\n"
        f"**(b) Calculation & Quantity:** $\\frac{{{p1 - p0}}}{{{p0}}} \\times 100 = {fmt_dec(pct)}\\%$; equilibrium quantity **increases** as sellers expand supply along `S` to meet higher seasonal demand."
    )
    return make_question(
        rng=rng,
        subskill="34_seasonal_demand_spike_retail_effect",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Identify rightward shift of Demand curve", "marks": 1, "type": "A"},
            {"step": f"Calculate +{fmt_dec(pct)}% surge", "marks": 2, "type": "A"},
            {"step": "State equilibrium quantity increases", "marks": 1, "type": "A"},
        ],
        marking_guide="1 mark for D shift right; 2 marks for %; 1 mark for Qe rise.",
        hints={
            "tier_1": "Seasonal urgency comes from the buyer/consumer side.",
            "tier_2": "A rightward Demand shift raises both Pe and Qe.",
            "tier_3": ans,
        },
        misconception_tags=["shifts_supply_rightward_for_seasonal_shopping_rush"],
    )


def _build_35_total_market_revenue_comparison_across_prices(rng: random.Random, mode: str) -> Dict[str, Any]:
    pe = rng.choice([40, 50, 60])
    qe = rng.choice([500, 600, 700])
    p_hi = pe + 20
    qd_hi = qe - 200
    tr_eq = pe * qe
    tr_hi = p_hi * qd_hi
    prompt = (
        f"At equilibrium price {fmt_zar(pe)}, sellers clear all {qe} units (`Qd = Qs = {qe}`). "
        f"At a higher price of {fmt_zar(p_hi)}, sellers want to supply {qe + 200} units, yet consumers are only willing to buy **{qd_hi} units**.\n\n"
        f"(a) Calculate actual realised market revenue (`Price * Quantity actually sold`) at {fmt_zar(pe)} and at {fmt_zar(p_hi)}.\n"
        f"(b) Explain why sellers cannot count unsold surplus units toward revenue."
    )
    ans = f"TR at {fmt_zar(pe)} = {fmt_zar(tr_eq)}; Realised TR at {fmt_zar(p_hi)} = {fmt_zar(tr_hi)} (based on Qd = {qd_hi}); revenue only occurs when a buyer purchases a unit"
    sol = (
        f"**(a) Realised Revenue (`TR = P * Q_sold`):**\n"
        f"- At equilibrium {fmt_zar(pe)}: ${fmt_zar(pe)} \\times {qe} = {fmt_zar(tr_eq)}$\n"
        f"- At high price {fmt_zar(p_hi)}: only {qd_hi} units are bought, so ${fmt_zar(p_hi)} \\times {qd_hi} = {fmt_zar(tr_hi)}$\n\n"
        f"**(b) Short-Side Rule:** Market transactions require both a willing buyer and seller—actual sales equal `min(Qd, Qs)`, leaving unsold stock generating R0 until discounted."
    )
    return make_question(
        rng=rng,
        subskill="35_total_market_revenue_comparison_across_prices",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate TR_eq {fmt_zar(tr_eq)} and TR_hi {fmt_zar(tr_hi)}", "marks": 2, "type": "A"},
            {"step": "Explain only actually purchased units (Qd) earn revenue", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for both revenues; 2 marks for explaining short-side exchange rule.",
        hints={
            "tier_1": "At a high price with excess supply, the lower number (Qd) limits how many units actually sell.",
            "tier_2": f"Multiply R{p_hi} by Qd={qd_hi}, NOT by Qs.",
            "tier_3": ans,
        },
        misconception_tags=["multiplies_high_price_by_quantity_supplied_even_though_unsold"],
    )


def _build_36_linear_demand_equation_evaluation(rng: random.Random, mode: str) -> Dict[str, Any]:
    a = rng.choice([1000, 1200, 1500])
    b = rng.choice([10, 15, 20])
    p1 = rng.choice([20, 25])
    p2 = p1 + 20
    q1 = a - b * p1
    q2 = a - b * p2
    prompt = (
        f"Market demand for reusable water bottles obeys the formula `Qd = {a} - {b}P`, where `P` is price in Rand.\n\n"
        f"(a) Calculate `Qd` when `P = {fmt_zar(p1)}` and when `P = {fmt_zar(p2)}`.\n"
        f"(b) Explain what the negative coefficient `-{b}` tells us economically."
    )
    ans = f"At {fmt_zar(p1)}: Qd = {q1}; At {fmt_zar(p2)}: Qd = {q2}; every R1 price increase lowers quantity demanded by {b} bottles (Law of Demand)"
    sol = (
        f"**(a) Substitutions:**\n"
        f"- At {fmt_zar(p1)}: $Q_d = {a} - {b}({p1}) = {q1}$\n"
        f"- At {fmt_zar(p2)}: $Q_d = {a} - {b}({p2}) = {q2}$\n\n"
        f"**(b) Meaning of `-{b}`:** Each R1 increase in price reduces quantity demanded by {b} bottles, demonstrating the inverse **Law of Demand**."
    )
    return make_question(
        rng=rng,
        subskill="36_linear_demand_equation_evaluation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Qd({p1}) = {q1} and Qd({p2}) = {q2}", "marks": 2, "type": "A"},
            {"step": f"Interpret -{b} per R1 inverse Law of Demand slope", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for evaluations; 2 marks for slope interpretation.",
        hints={
            "tier_1": f"Substitute P={p1} and P={p2} into {a} - {b}P.",
            "tier_2": "Notice the minus sign confirms that higher prices yield smaller Qd.",
            "tier_3": ans,
        },
        misconception_tags=["adds_bP_instead_of_subtracting"],
    )


def _build_37_linear_supply_equation_evaluation(rng: random.Random, mode: str) -> Dict[str, Any]:
    c = rng.choice([100, 150, 200])
    d = rng.choice([5, 8, 10])
    p1 = rng.choice([20, 30])
    p2 = p1 + 30
    q1 = c + d * p1
    q2 = c + d * p2
    prompt = (
        f"Producer supply of handmade woven baskets follows `Qs = {c} + {d}P`, where `P` is price in Rand.\n\n"
        f"(a) Calculate `Qs` at `P = {fmt_zar(p1)}` and at `P = {fmt_zar(p2)}`.\n"
        f"(b) Explain how the positive `+{d}P` term reflects the **Law of Supply**."
    )
    ans = f"At {fmt_zar(p1)}: Qs = {q1}; At {fmt_zar(p2)}: Qs = {q2}; each R1 price rise motivates firms to supply {d} extra baskets"
    sol = (
        f"**(a) Substitutions:**\n"
        f"- At {fmt_zar(p1)}: $Q_s = {c} + {d}({p1}) = {q1}$\n"
        f"- At {fmt_zar(p2)}: $Q_s = {c} + {d}({p2}) = {q2}$\n\n"
        f"**(b) Economic Meaning:** The positive coefficient `+{d}` confirms a **direct** relationship—higher selling prices motivate producers to supply more baskets."
    )
    return make_question(
        rng=rng,
        subskill="37_linear_supply_equation_evaluation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Qs({p1}) = {q1} and Qs({p2}) = {q2}", "marks": 2, "type": "A"},
            {"step": "Explain direct positive Law of Supply relationship", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Qs evaluations; 2 marks for Law of Supply meaning.",
        hints={
            "tier_1": f"Substitute P={p1} and P={p2} into {c} + {d}P.",
            "tier_2": "Positive +dP reflects direct price-quantity response.",
            "tier_3": ans,
        },
        misconception_tags=["interprets_plus_slope_as_excess_demand"],
    )


def _build_38_interpreting_slope_price_sensitivity(rng: random.Random, mode: str) -> Dict[str, Any]:
    pct_p = rng.choice([20, 25])
    drop_essential = rng.choice([4, 6])
    drop_luxury = rng.choice([35, 45])
    prompt = (
        f"After a {pct_p}% price increase:\n"
        f"- Quantity demanded of **essential basic insulin** drops by only **{drop_essential}%**.\n"
        f"- Quantity demanded of **luxury cinema snacks** drops by **{drop_luxury}%**.\n\n"
        f"Which good shows **higher buyer price sensitivity** (`% change in Qd` vs `% change in P`), and give ONE economic reason why."
    )
    ans = f"Luxury cinema snacks (-{drop_luxury}% vs -{drop_essential}%); non-essential discretionary goods have close substitutes or can easily be skipped when prices rise"
    sol = (
        f"- **More Price-Sensitive:** **Luxury cinema snacks** (dropped **{drop_luxury}%** compared with **{drop_essential}%** for insulin for the identical {pct_p}% price jump).\n"
        f"- **Why:** Essential medical/staple items have no viable substitute and must still be bought, whereas optional luxuries can easily be skipped or replaced."
    )
    return make_question(
        rng=rng,
        subskill="38_interpreting_slope_price_sensitivity",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Identify luxury cinema snacks as more sensitive", "marks": 1, "type": "A"},
            {"step": "Give necessity vs luxury / substitute availability rationale", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for identifying cinema snacks; 2 marks for necessity vs luxury reasoning.",
        hints={
            "tier_1": f"Compare {drop_luxury}% against {drop_essential}% for the same {pct_p}% price rise.",
            "tier_2": "Think about whether households can survive without insulin vs movie popcorn.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_essentials_drop_more_than_luxuries_when_prices_rise"],
    )


def _build_39_price_ceiling_maximum_price_shortage(rng: random.Random, mode: str) -> Dict[str, Any]:
    pe = rng.choice([18, 20, 22])
    p_cap = pe - rng.choice([4, 5, 6])
    qd_cap = rng.choice([1400, 1600, 1800])
    qs_cap = rng.choice([850, 950, 1050])
    shortage = qd_cap - qs_cap
    prompt = (
        f"Suppose municipal equilibrium price for paraffin is {fmt_zar(pe)}/litre. To help poor families, authorities pass a binding "
        f"**maximum price (price ceiling)** of {fmt_zar(p_cap)}/litre, where `Qd = {qd_cap} litres` and `Qs = {qs_cap} litres`.\n\n"
        f"(a) Calculate the resulting persistent market **shortage**.\n"
        f"(b) Identify ONE unintended consequence (e.g., informal black markets or rationing queues) of freezing prices below equilibrium."
    )
    ans = f"Shortage = {shortage} litres; unintended consequence: long queues, supplier hoarding or illegal black-market sales above {fmt_zar(p_cap)}"
    sol = (
        f"**(a) Persistent Shortage:** ${qd_cap} - {qs_cap} = {shortage}$ litres.\n"
        f"**(b) Unintended Consequence:** Because sellers legally cannot raise prices to clear the market, queues form, producers cut supply, and informal black-market reselling can emerge above {fmt_zar(p_cap)}."
    )
    return make_question(
        rng=rng,
        subskill="39_price_ceiling_maximum_price_shortage",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate shortage {shortage} litres", "marks": 2, "type": "A"},
            {"step": "Identify queues/hoarding/black market risk", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for shortage math; 2 marks for unintended consequence.",
        hints={
            "tier_1": "Subtract Qs from Qd at the regulated ceiling price.",
            "tier_2": "Ask how buyers react when supply is legally blocked from catching up to demand.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_price_ceilings_create_surpluses"],
    )


def _build_40_price_floor_minimum_price_surplus(rng: random.Random, mode: str) -> Dict[str, Any]:
    pe = rng.choice([4500, 4800, 5000])
    p_floor = pe + rng.choice([800, 1000, 1200])
    qs_fl = rng.choice([2400, 2600, 2800])
    qd_fl = rng.choice([1700, 1850, 1950])
    surplus = qs_fl - qd_fl
    prompt = (
        f"Equilibrium wheat price is {fmt_zar(pe)}/tonne. To protect rural farmers' income, government sets a binding "
        f"**minimum price (price floor)** of {fmt_zar(p_floor)}/tonne, resulting in `Qs = {qs_fl} tonnes` and `Qd = {qd_fl} tonnes`.\n\n"
        f"(a) Calculate the resulting unsold **market surplus**.\n"
        f"(b) Explain why private sellers cannot dispose of this surplus through normal discounting."
    )
    ans = f"Surplus = {surplus} tonnes; discounting below {fmt_zar(p_floor)} is prohibited by law, leaving unsold stockpiles unless government buys the surplus"
    sol = (
        f"**(a) Surplus Calculation:** ${qs_fl} - {qd_fl} = {surplus}$ tonnes unsold.\n"
        f"**(b) Why Surplus Persists:** Normally excess supply forces prices down to {fmt_zar(pe)}, but a legal price floor forbids selling below {fmt_zar(p_floor)}, leaving surplus grain unless bought into state reserves."
    )
    return make_question(
        rng=rng,
        subskill="40_price_floor_minimum_price_surplus",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate surplus {surplus} tonnes", "marks": 2, "type": "A"},
            {"step": "Explain legal floor blocks price cuts", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for surplus math; 2 marks for floor blocking clearing discounts.",
        hints={
            "tier_1": "Subtract Qd from Qs at the floor price.",
            "tier_2": "Legal minimum prices stop prices from falling to equilibrium.",
            "tier_3": ans,
        },
        misconception_tags=["labels_price_floor_excess_as_shortage"],
    )


def _build_41_constructing_market_schedule_from_word_problem(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_start = rng.choice([10, 20])
    step_p = rng.choice([10, 20])
    qd0 = rng.choice([500, 600])
    d_step = rng.choice([100, 120])
    qs0 = rng.choice([100, 120])
    s_step = rng.choice([100, 120])
    # Ensure exact match on row 2 (index 2 -> p = p_start + 2*step_p):
    # Actually enforce equal step if d_step == s_step and qd0 - 2*step == qs0 + 2*step!
    step_q = rng.choice([100, 150])
    qd0 = 5 * step_q
    qs0 = 1 * step_q
    # Row 0: qd=5s, qs=1s; Row 1: 4s, 2s; Row 2: 3s, 3s (Equilibrium!); Row 3: 2s, 4s
    rows = [(p_start + i * step_p, qd0 - i * step_q, qs0 + i * step_q) for i in range(4)]
    headers = ["Price (R)", "Quantity Demanded (Qd)", "Quantity Supplied (Qs)"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Price (R) | Quantity Demanded (Qd) | Quantity Supplied (Qs) |", "|---|---|---|"]
    req_coords = [(1, 1), (2, 1), (2, 2), (3, 2)]
    for r_idx, (p, qd, qs) in enumerate(rows, start=1):
        vals = [f"R{p}", str(qd), str(qs)]
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = (r_idx - 1, c_idx) in req_coords
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = f"Apply Qd dropping by {step_q} and Qs rising by {step_q} per +R{step_p} price step."
        rows_ui.append(cells)
        md_lines.append(f"| R{p} | {qd} | {qs} |")
    md_table = "\n".join(md_lines)
    pe = p_start + 2 * step_p
    qe = 3 * step_q
    prompt = (
        f"In a local fresh-juice market starting at **R{p_start}** (`Qd = {qd0}`, `Qs = {qs0}`), every **R{step_p}** price rise "
        f"reduces `Qd` by **{step_q}** units and increases `Qs` by **{step_q}** units.\n"
        f"Build the missing cells in the market schedule (equilibrium occurs at R{pe}, {qe} units)."
    )
    return make_question(
        rng=rng,
        subskill="41_constructing_market_schedule_from_word_problem",
        question_type="table_completion",
        prompt=prompt,
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Constructed Market Schedule (`Pe = R{pe}`, `Qe = {qe}`):**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per generated schedule entry.",
        hints={
            "tier_1": f"Step price by +R{step_p} on each row.",
            "tier_2": f"Subtract {step_q} down the Qd column; add {step_q} down the Qs column.",
            "tier_3": md_table,
        },
        misconception_tags=["adds_instead_of_subtracts_along_demand_column"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "p", "label": headers[0]}, {"key": "qd", "label": headers[1]}, {"key": "qs", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_42_simultaneous_demand_supply_shift_direction(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("Both Demand AND Supply shift rightward simultaneously (e.g., rising consumer incomes plus new cost-saving factory technology)", "Equilibrium quantity definitely increases; price change is ambiguous (depends on relative shift size)"),
        ("Demand shifts rightward while Supply shifts leftward simultaneously (e.g., holiday demand surge alongside electricity-cost shock)", "Equilibrium price definitely rises; quantity change is ambiguous (depends on relative shift size)"),
        ("Demand shifts leftward while Supply shifts rightward simultaneously (e.g., buyers switch away while harvests hit record bumper yields)", "Equilibrium price definitely falls; quantity change is ambiguous"),
    ]
    clue, ans = rng.choice(cases)
    distractors = [
        "Both equilibrium price and quantity always remain locked at their exact old values",
        "Supply and demand curves become completely horizontal forever",
        "Neither price nor quantity ever reacts to dual market shifts",
    ]
    prompt = f"What happens in a market when *{clue}*?"
    sol = f"- **Combined Shift Result:** {ans}."
    return make_question(
        rng=rng,
        subskill="42_simultaneous_demand_supply_shift_direction",
        question_type="mcq",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify definite effect vs ambiguous variable", "marks": 2, "type": "A"}],
        marking_guide="2 marks for distinguishing the definite variable from the ambiguous variable.",
        hints={
            "tier_1": "Check whether the two shifts push P in the same direction or opposite directions, then do the same for Q.",
            "tier_2": "When both shifts push one variable the same way, its direction is certain.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_both_price_and_quantity_are_always_unambiguous_under_dual_shifts"],
        options=[ans] + distractors,
        duration_mins=3,
    )


def _build_43_keyring_market_reading_exam_case(rng: random.Random, mode: str) -> Dict[str, Any]:
    item = rng.choice(["Keyrings", "Canvas Tote Bags", "Cricket Caps", "Coffee Mugs"])
    p_step = rng.choice([10, 20])
    q_step = rng.choice([100, 150, 200])
    max_p, max_q = 5 * p_step, 5 * q_step
    eq_q, eq_p = 3 * q_step, 3 * p_step
    d_pts = [(q_step, 5 * p_step), (2 * q_step, 4 * p_step), (eq_q, eq_p), (4 * q_step, 2 * p_step), (5 * q_step, p_step)]
    s_pts = [(q_step, p_step), (2 * q_step, 2 * p_step), (eq_q, eq_p), (4 * q_step, 4 * p_step), (5 * q_step, 5 * p_step)]
    ask_p = 2 * p_step
    qd_at_ask = 4 * q_step
    diagram = svg_market_graph(
        title=f"Market Model for {item}",
        max_q=max_q,
        max_p=max_p,
        d_pts=d_pts,
        s_pts=s_pts,
        eq_pt=(eq_q, eq_p, "E"),
    )
    prompt = (
        f"Examine the demand and supply curve model for **{item}**.\n\n"
        f"(a) Name the variable plotted on the **vertical Y-axis** and on the **horizontal X-axis**.\n"
        f"(b) How many {item.lower()} are consumers willing to buy (`Qd`) at a price of **R{ask_p}** (`({qd_at_ask}; R{ask_p})` on `D`)?\n"
        f"(c) Identify the **equilibrium price** and **equilibrium quantity**."
    )
    ans = f"Vertical Y-axis: Price (R); Horizontal X-axis: Quantity; Qd at R{ask_p} = {qd_at_ask}; Pe = R{eq_p}; Qe = {eq_q}"
    sol = (
        f"**(a) Axes:** Vertical Y-axis = **Price (R)**; Horizontal X-axis = **Quantity**.\n"
        f"**(b) Quantity Demanded at R{ask_p}:** **{qd_at_ask} {item.lower()}**.\n"
        f"**(c) Equilibrium:** **Pe = R{eq_p}** and **Qe = {eq_q} {item.lower()}**."
    )
    return make_question(
        rng=rng,
        subskill="43_keyring_market_reading_exam_case",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=6,
        marking_schema=[
            {"step": "Correctly name Y-axis (Price) and X-axis (Quantity)", "marks": 2, "type": "A"},
            {"step": f"Read Qd = {qd_at_ask} at R{ask_p}", "marks": 2, "type": "A"},
            {"step": f"Identify Pe = R{eq_p} and Qe = {eq_q}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for axes; 2 marks for reading Qd; 2 marks for Pe & Qe.",
        hints={
            "tier_1": "Read the vertical label for Y-axis and horizontal label for X-axis.",
            "tier_2": f"Locate R{ask_p} on Price axis and follow across to D; find crossing point E for Pe & Qe.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_x_and_y_axes"],
        diagram_spec=diagram,
        duration_mins=6,
    )


def _build_44_number_of_buyers_market_demand_sum(rng: random.Random, mode: str) -> Dict[str, Any]:
    buyers_n = rng.choice([25, 40, 50, 60])
    ind_p1_q = rng.choice([4, 6, 8])
    ind_p2_q = ind_p1_q - 2
    p1 = rng.choice([30, 40])
    p2 = p1 + 20
    mkt_q1 = buyers_n * ind_p1_q
    mkt_q2 = buyers_n * ind_p2_q
    prompt = (
        f"In a small town with **{buyers_n} identical households**, each household buys {ind_p1_q} cartons of milk per week at {fmt_zar(p1)} "
        f"or {ind_p2_q} cartons per week at {fmt_zar(p2)}.\n\n"
        f"(a) Calculate **total market demand** at {fmt_zar(p1)} and at {fmt_zar(p2)}.\n"
        f"(b) Explain how market demand changes if 10 new families move into the town."
    )
    ans = f"At {fmt_zar(p1)}: {mkt_q1} cartons; At {fmt_zar(p2)}: {mkt_q2} cartons; 10 new families shift the entire market demand curve rightward"
    sol = (
        f"**(a) Horizontal Sum of Individual Demands:**\n"
        f"- At {fmt_zar(p1)}: ${buyers_n} \\times {ind_p1_q} = {mkt_q1}$ cartons\n"
        f"- At {fmt_zar(p2)}: ${buyers_n} \\times {ind_p2_q} = {mkt_q2}$ cartons\n\n"
        f"**(b) Population Effect:** More buyers at every price shifts the **market demand curve rightward**."
    )
    return make_question(
        rng=rng,
        subskill="44_number_of_buyers_market_demand_sum",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate market demand {mkt_q1} and {mkt_q2}", "marks": 2, "type": "A"},
            {"step": "Explain rightward shift from larger number of buyers", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for market sums; 2 marks for population shift.",
        hints={
            "tier_1": "Multiply individual household quantity by the total number of households.",
            "tier_2": "More buyers increase market demand at every price (rightward shift).",
            "tier_3": ans,
        },
        misconception_tags=["averages_individual_demand_instead_of_summing"],
    )


def _build_45_number_of_sellers_market_supply_sum(rng: random.Random, mode: str) -> Dict[str, Any]:
    firms_n = rng.choice([8, 10, 12, 15])
    per_firm_low = rng.choice([50, 60, 80])
    per_firm_hi = per_firm_low + 40
    p_low = rng.choice([80, 100])
    p_hi = p_low + 40
    mkt_low = firms_n * per_firm_low
    mkt_hi = firms_n * per_firm_hi
    prompt = (
        f"At a regional craft market, **{firms_n} identical potteries** each supply {per_firm_low} bowls per month at {fmt_zar(p_low)} "
        f"or {per_firm_hi} bowls per month at {fmt_zar(p_hi)}.\n\n"
        f"(a) Calculate **total market supply** at {fmt_zar(p_low)} and at {fmt_zar(p_hi)}.\n"
        f"(b) State the shift direction of market supply if 3 potteries close permanently."
    )
    ans = f"At {fmt_zar(p_low)}: {mkt_low} bowls; At {fmt_zar(p_hi)}: {mkt_hi} bowls; 3 closures shift market supply leftward"
    sol = (
        f"**(a) Market Supply Totals:**\n"
        f"- At {fmt_zar(p_low)}: ${firms_n} \\times {per_firm_low} = {mkt_low}$ bowls\n"
        f"- At {fmt_zar(p_hi)}: ${firms_n} \\times {per_firm_hi} = {mkt_hi}$ bowls\n\n"
        f"**(b) Fewer Sellers:** Losing 3 producers reduces total quantity supplied at every price, shifting the **market supply curve leftward**."
    )
    return make_question(
        rng=rng,
        subskill="45_number_of_sellers_market_supply_sum",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate market supply {mkt_low} and {mkt_hi}", "marks": 2, "type": "A"},
            {"step": "Identify leftward supply shift from seller exits", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for market supply totals; 2 marks for seller-exit shift.",
        hints={
            "tier_1": f"Multiply per-pottery supply by {firms_n}.",
            "tier_2": "Fewer sellers reduce supply -> leftward shift.",
            "tier_3": ans,
        },
        misconception_tags=["claims_closing_firms_shift_supply_right"],
    )


def _build_46_consumers_substituting_to_cheaper_alternatives(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("mutton chops jumping by 35%", "households switching to chicken portions and lentils (substitution effect) while real budgets stretch less far (income effect)"),
        ("cinema tickets doubling from R75 to R150", "families choosing home streaming or park outings instead (substitution effect) and cutting ticket purchases"),
        ("arabica ground coffee spiking by 40%", "shoppers buying rooibos tea or chicory blends instead, lowering quantity demanded of ground coffee"),
    ]
    shock, reason = rng.choice(cases)
    prompt = (
        f"When consumers experience *{shock}*, explain **TWO** economic mechanisms (substitution effect and purchasing-power/income effect) "
        f"explaining why quantity demanded falls."
    )
    ans = reason.capitalize()
    sol = (
        f"**Two Reasons Quantity Demanded Falls:**\n"
        f"1. **Substitution Effect:** As the product becomes relatively costlier, buyers switch to cheaper substitutes.\n"
        f"2. **Purchasing-Power (Income) Effect:** A fixed Rand budget now buys fewer units overall, lowering quantity demanded ({reason})."
    )
    return make_question(
        rng=rng,
        subskill="46_consumers_substituting_to_cheaper_alternatives",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain substitution effect toward cheaper alternatives", "marks": 2, "type": "A"},
            {"step": "Explain income / purchasing-power shrinkage effect", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for substitution effect; 2 marks for purchasing-power effect.",
        hints={
            "tier_1": "Think of both rival products AND how far a shopper's R500 note stretches.",
            "tier_2": "Cover substitution + purchasing-power erosion.",
            "tier_3": ans,
        },
        misconception_tags=["ignores_substitution_when_explaining_law_of_demand"],
    )


def _build_47_profit_incentive_behind_law_of_supply(rng: random.Random, mode: str) -> Dict[str, Any]:
    unit_cost = rng.choice([60, 75, 90])
    p1 = unit_cost + 25
    p2 = unit_cost + 60
    margin1 = p1 - unit_cost
    margin2 = p2 - unit_cost
    prompt = (
        f"A small shoe workshop produces sandals at a cost of {fmt_zar(unit_cost)}/pair.\n\n"
        f"(a) Calculate the profit margin per pair if market price rises from {fmt_zar(p1)} to {fmt_zar(p2)}.\n"
        f"(b) Explain why this wider profit margin causes the **Law of Supply** to hold."
    )
    ans = f"Margin grows from {fmt_zar(margin1)} to {fmt_zar(margin2)} per pair; higher unit profitability rewards overtime shifts and extra output"
    sol = (
        f"**(a) Profit per Pair:**\n"
        f"- At {fmt_zar(p1)}: ${fmt_zar(p1)} - {fmt_zar(unit_cost)} = {fmt_zar(margin1)}$\n"
        f"- At {fmt_zar(p2)}: ${fmt_zar(p2)} - {fmt_zar(unit_cost)} = {fmt_zar(margin2)}$\n\n"
        f"**(b) Law of Supply Rationale:** Higher unit profits justify hiring extra labour or running overtime machines, increasing quantity supplied."
    )
    return make_question(
        rng=rng,
        subskill="47_profit_incentive_behind_law_of_supply",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate margins {fmt_zar(margin1)} and {fmt_zar(margin2)}", "marks": 2, "type": "A"},
            {"step": "Link higher profitability to expanded production", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for margins; 2 marks for profit-incentive link to higher supply.",
        hints={
            "tier_1": "Subtract production cost from both selling prices.",
            "tier_2": "Profit motive encourages producers to allocate more resources when price rises.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_higher_price_raises_firm_costs_equally"],
    )


def _build_48_diagnosing_graph_reading_and_axis_errors(rng: random.Random, mode: str) -> Dict[str, Any]:
    errors = [
        ("A student writes: 'On a demand and supply model, Quantity sits on the vertical Y-axis and Price sits on the horizontal X-axis.'", "In standard economics, Price (R) is always placed on the vertical Y-axis and Quantity on the horizontal X-axis."),
        ("A student writes: 'When the price of apples rises, the entire Demand curve shifts leftward.'", "A change in the product's own price causes an upward movement ALONG the existing Demand curve (a fall in quantity demanded), not a shift of the curve."),
        ("A student writes: 'At a price below equilibrium where Qd = 900 and Qs = 400, there is a surplus of 500 units.'", "When Qd exceeds Qs (900 > 400), there is a SHORTAGE (excess demand) of 500 units, putting upward pressure on price."),
    ]
    claim, correction = rng.choice(errors)
    prompt = f"Spot and correct the Price Theory error in this statement:\n*{claim}*"
    sol = f"**Correction:**\n- {correction}"
    return make_question(
        rng=rng,
        subskill="48_diagnosing_graph_reading_and_axis_errors",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=correction,
        sample_answer=correction,
        worked_solution=sol,
        marks=3,
        marking_schema=[{"step": "Correct error accurately with Price Theory reasoning", "marks": 3, "type": "A"}],
        marking_guide="3 marks for exact correction of axis, movement-vs-shift, or shortage/surplus error.",
        hints={
            "tier_1": "Check axis conventions, own-price vs non-price rules, or Qd vs Qs inequality.",
            "tier_2": "State the opposite accurate rule cleanly.",
            "tier_3": correction,
        },
        misconception_tags=["repeats_erroneous_student_statement"],
    )


def _build_49_complete_disequilibrium_and_shift_table(rng: random.Random, mode: str) -> Dict[str, Any]:
    shocks = [
        ("Rise in household income", "Demand (D)", "Rightward", "Pe rises, Qe rises"),
        ("Drop in price of substitute", "Demand (D)", "Leftward", "Pe falls, Qe falls"),
        ("Cost-saving production tech", "Supply (S)", "Rightward", "Pe falls, Qe rises"),
        ("Higher raw-material tariffs", "Supply (S)", "Leftward", "Pe rises, Qe falls"),
    ]
    picked = rng.sample(shocks, 3)
    headers = ["Shock Event", "Curve Shifted", "Shift Direction", "Equilibrium Effect (Pe & Qe)"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Shock Event | Curve Shifted | Shift Direction | Equilibrium Effect (Pe & Qe) |", "|---|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_cols = rng.sample([1, 2, 3], 2)
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx in req_cols
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Trace Curve -> Right/Left -> Effect on both Pe and Qe."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="49_complete_disequilibrium_and_shift_table",
        question_type="table_completion",
        prompt="Complete the Market Equilibrium Shift Matrix by identifying the affected curve, shift direction, and effect on `Pe` and `Qe`.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Market Shift Summary:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per correct shift matrix cell.",
        hints={
            "tier_1": "Demand shifts move Pe and Qe in the same direction; Supply shifts move Pe and Qe in opposite directions.",
            "tier_2": "Verify whether the shock affects consumers (D) or producer costs/tech (S).",
            "tier_3": md_table,
        },
        misconception_tags=["moves_price_and_quantity_same_way_under_supply_shift"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "ev", "label": headers[0]}, {"key": "c", "label": headers[1]}, {"key": "d", "label": headers[2]}, {"key": "eq", "label": headers[3]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_50_comprehensive_price_theory_market_synthesis(rng: random.Random, mode: str) -> Dict[str, Any]:
    pe = rng.choice([25, 30, 40])
    qe = rng.choice([300, 400, 500])
    a = qe + 10 * pe
    c = qe - 10 * pe
    p_hi = pe + 10
    qd_hi = a - 10 * p_hi
    qs_hi = c + 10 * p_hi
    surplus = qs_hi - qd_hi
    tr_eq = pe * qe
    prompt = (
        f"In a competitive school-bag market, demand obeys `Qd = {a} - 10P` and supply obeys `Qs = {c} + 10P`:\n\n"
        f"(a) Calculate the **equilibrium price (`Pe`)** and **equilibrium quantity (`Qe`)**.\n"
        f"(b) Calculate total market revenue (`TR = Pe * Qe`) at equilibrium.\n"
        f"(c) At a higher price of **R{p_hi}**, determine whether a **surplus** or **shortage** exists and calculate its size.\n"
        f"(d) Predict the direction of `Pe` and `Qe` if consumer incomes rise suddenly (*ceteris paribus*)."
    )
    ans = f"Pe = {fmt_zar(pe)}, Qe = {qe}; TR = {fmt_zar(tr_eq)}; At R{p_hi}: surplus of {surplus} bags; Income rise -> D shifts right -> both Pe and Qe increase"
    sol = (
        f"**(a) Equilibrium (`Qd = Qs`):**\n"
        f"${a} - 10P = {c} + 10P \\implies 20P = {a - c} \\implies P_e = {fmt_zar(pe)}$, $Q_e = {qe}$ bags.\n\n"
        f"**(b) Total Revenue:** ${fmt_zar(pe)} \\times {qe} = {fmt_zar(tr_eq)}$\n\n"
        f"**(c) At R{p_hi}:** $Q_d = {qd_hi}$, $Q_s = {qs_hi}$ $\\implies$ **Surplus** of ${qs_hi} - {qd_hi} = {surplus}$ bags.\n\n"
        f"**(d) Income Increase Shock:** Demand shifts **rightward** $\\implies$ both **Pe rises** and **Qe rises**."
    )
    return make_question(
        rng=rng,
        subskill="50_comprehensive_price_theory_market_synthesis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=8,
        marking_schema=[
            {"step": f"Solve Pe = {fmt_zar(pe)} and Qe = {qe}", "marks": 2, "type": "M"},
            {"step": f"Calculate equilibrium revenue {fmt_zar(tr_eq)}", "marks": 2, "type": "CA"},
            {"step": f"Compute surplus {surplus} bags at R{p_hi}", "marks": 2, "type": "A"},
            {"step": "Predict rightward D shift raising Pe and Qe", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks each across parts (a), (b), (c), and (d).",
        hints={
            "tier_1": "Equate Qd and Qs first, then substitute Pe to find Qe.",
            "tier_2": f"Check Qd and Qs at R{p_hi} separately to find Surplus = Qs - Qd.",
            "tier_3": ans,
        },
        misconception_tags=["fails_to_distinguish_disequilibrium_from_shift"],
        duration_mins=7,
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_market_disequilibrium_shortage_calculation": _build_26_market_disequilibrium_shortage_calculation,
    "27_price_adjustment_mechanism_to_equilibrium": _build_27_price_adjustment_mechanism_to_equilibrium,
    "28_movement_along_vs_curve_shift_classification": _build_28_movement_along_vs_curve_shift_classification,
    "29_demand_increase_shift_right_svg": _build_29_demand_increase_shift_right_svg,
    "30_demand_decrease_shift_left_svg": _build_30_demand_decrease_shift_left_svg,
    "31_supply_increase_shift_right_svg": _build_31_supply_increase_shift_right_svg,
    "32_supply_decrease_shift_left_svg": _build_32_supply_decrease_shift_left_svg,
    "33_agricultural_drought_maize_price_shock": _build_33_agricultural_drought_maize_price_shock,
    "34_seasonal_demand_spike_retail_effect": _build_34_seasonal_demand_spike_retail_effect,
    "35_total_market_revenue_comparison_across_prices": _build_35_total_market_revenue_comparison_across_prices,
    "36_linear_demand_equation_evaluation": _build_36_linear_demand_equation_evaluation,
    "37_linear_supply_equation_evaluation": _build_37_linear_supply_equation_evaluation,
    "38_interpreting_slope_price_sensitivity": _build_38_interpreting_slope_price_sensitivity,
    "39_price_ceiling_maximum_price_shortage": _build_39_price_ceiling_maximum_price_shortage,
    "40_price_floor_minimum_price_surplus": _build_40_price_floor_minimum_price_surplus,
    "41_constructing_market_schedule_from_word_problem": _build_41_constructing_market_schedule_from_word_problem,
    "42_simultaneous_demand_supply_shift_direction": _build_42_simultaneous_demand_supply_shift_direction,
    "43_keyring_market_reading_exam_case": _build_43_keyring_market_reading_exam_case,
    "44_number_of_buyers_market_demand_sum": _build_44_number_of_buyers_market_demand_sum,
    "45_number_of_sellers_market_supply_sum": _build_45_number_of_sellers_market_supply_sum,
    "46_consumers_substituting_to_cheaper_alternatives": _build_46_consumers_substituting_to_cheaper_alternatives,
    "47_profit_incentive_behind_law_of_supply": _build_47_profit_incentive_behind_law_of_supply,
    "48_diagnosing_graph_reading_and_axis_errors": _build_48_diagnosing_graph_reading_and_axis_errors,
    "49_complete_disequilibrium_and_shift_table": _build_49_complete_disequilibrium_and_shift_table,
    "50_comprehensive_price_theory_market_synthesis": _build_50_comprehensive_price_theory_market_synthesis,
}
