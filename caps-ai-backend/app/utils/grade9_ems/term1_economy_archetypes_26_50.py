"""Grade 9 EMS Term 1: Economic Systems — Semantic Archetypes 26 to 50."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term1_economy_archetypes_01_25 import fmt_dec, fmt_zar, make_question


def _svg_horizontal_bar_chart(title: str, bars: List[tuple], unit: str) -> Dict[str, Any]:
    """Render parameterized horizontal bar chart SVG."""
    width = 620
    row_h = 34
    height = 75 + len(bars) * row_h
    max_val = max(v for _, v, _ in bars) or 1
    bar_max_w = 320
    lines: List[str] = []
    for i, (label, val, color) in enumerate(bars):
        y = 52 + i * row_h
        bw = max(16, round(bar_max_w * val / max_val))
        val_txt = fmt_dec(val, 1) if isinstance(val, float) else str(val)
        lines.append(
            f'<text x="150" y="{y + 15}" text-anchor="end" font-size="12" font-weight="600" fill="#1e293b">{label}</text>'
            f'<rect x="162" y="{y}" width="{bw}" height="22" fill="{color}" rx="4"/>'
            f'<text x="{170 + bw}" y="{y + 15}" font-size="12" font-weight="700" fill="#0f172a">{val_txt}{unit}</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">'
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff" rx="8"/>'
        f'<text x="{width // 2}" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{title}</text>'
        f'{"".join(lines)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_stacked_country_shares(countries: List[tuple]) -> Dict[str, Any]:
    """Render stacked Public vs Private % GDP bars across three countries."""
    width, height = 620, 235
    x_bar, bar_w = 185, 340
    blocks: List[str] = []
    for i, (name, pub_pct, priv_pct) in enumerate(countries):
        y = 66 + i * 48
        w_pub = max(12, round(bar_w * pub_pct / 100.0))
        w_priv = bar_w - w_pub
        blocks.append(
            f'<text x="172" y="{y + 17}" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">{name}</text>'
            f'<rect x="{x_bar}" y="{y}" width="{w_pub}" height="26" fill="#1d4ed8"/>'
            f'<rect x="{x_bar + w_pub}" y="{y}" width="{w_priv}" height="26" fill="#10b981"/>'
            f'<text x="{x_bar + w_pub // 2}" y="{y + 17}" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{pub_pct}%</text>'
            f'<text x="{x_bar + w_pub + w_priv // 2}" y="{y + 17}" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{priv_pct}%</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">'
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff" rx="8"/>'
        f'<text x="{width // 2}" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        f'Public vs Private Share of National Output (%)</text>'
        f'<rect x="190" y="38" width="12" height="12" fill="#1d4ed8"/>'
        f'<text x="208" y="48" font-size="11" fill="#1e3a8a">Public Sector %</text>'
        f'<rect x="330" y="38" width="12" height="12" fill="#10b981"/>'
        f'<text x="348" y="48" font-size="11" fill="#065f46">Private Sector %</text>'
        f'{"".join(blocks)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _build_26_pros_cons_system_matching_matrix(rng: random.Random, mode: str) -> Dict[str, Any]:
    bank = [
        ("Prevents extreme private monopoly exploitation", "Planned Economy", "Advantage"),
        ("Poor motivation under guaranteed pay ('iron rice bowl')", "Planned Economy", "Disadvantage"),
        ("High innovation and swift response to consumer trends", "Market Economy", "Advantage"),
        ("Widening gap between ultra-wealthy and destitute households", "Market Economy", "Disadvantage"),
        ("Blends private efficiency with state-funded public welfare", "Mixed Economy", "Advantage"),
        ("Heavy taxes and potential bureaucratic red tape or SOE bailouts", "Mixed Economy", "Disadvantage"),
    ]
    chosen = rng.sample(bank, 3)
    headers = ["Economic Statement", "Economic System", "Advantage / Disadvantage"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Economic Statement | Economic System | Advantage / Disadvantage |", "|---|---|---|"]
    for r_idx, row_vals in enumerate(chosen, start=1):
        blank_col = rng.choice([1, 2])
        row_cells: List[Dict[str, Any]] = []
        for c_idx, val in enumerate(row_vals):
            coord = f"R{r_idx}C{c_idx}"
            is_req = c_idx == blank_col
            row_cells.append({
                "coordinate": coord,
                "value": "" if is_req else val,
                "type": "required" if is_req else "given",
                "editable": is_req,
            })
            if is_req:
                correct_map[coord] = val
                cell_hints[coord] = "Decide whether the statement praises or criticises Planned, Market, or Mixed."
        rows_ui.append(row_cells)
        md_lines.append(f"| {row_vals[0]} | {row_vals[1]} | {row_vals[2]} |")

    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="26_pros_cons_system_matching_matrix",
        question_type="table_completion",
        prompt="Classify each economic characteristic in the evaluation matrix below as belonging to Planned, Market, or Mixed economies and as an Advantage or Disadvantage.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Evaluative Classification Matrix:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k} = {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each correct system/evaluation entry.",
        hints={
            "tier_1": "Link each clue first to state command, free competition, or balanced welfare.",
            "tier_2": "Determine whether the outcome benefits society (Advantage) or harms it (Disadvantage).",
            "tier_3": md_table,
        },
        misconception_tags=["labels_market_inequality_as_advantage"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "statement", "label": headers[0]}, {"key": "system", "label": headers[1]}, {"key": "eval", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_27_2007_2008_global_financial_crisis_lesson(rng: random.Random, mode: str) -> Dict[str, Any]:
    angles = [
        ("unchecked US subprime mortgage lending collapsing into worldwide bank failures", "unregulated free markets can destabilise global finance, proving why mixed-economy banking regulation and central bank oversight are necessary"),
        ("major international banks needing emergency taxpayer bailouts in 2008", "governments must act as stabilisers during systemic market crashes because pure laissez-faire cannot self-correct instantly"),
        ("South Africa losing export orders and jobs despite having stricter domestic banking rules", "in an interconnected global economy, financial shocks abroad rapidly spill over into domestic jobs and trade"),
        ("governments worldwide shifting away from extreme deregulation back toward supervised finance", "balanced mixed-economy rules protect depositors without eliminating private banking innovation"),
    ]
    trigger, lesson = rng.choice(angles)
    prompt = (
        f"During the **2007–2008 global financial crisis**, {trigger}.\n\n"
        f"Explain the core economic lesson this crisis taught policymakers about pure market capitalism versus a **mixed economy**."
    )
    ans = f"It showed that {lesson}"
    sol = (
        f"- **Lesson from 2007–2008:** {lesson.capitalize()}.\n"
        f"- Consequently, South Africa's stricter National Credit Act and Reserve Bank supervision helped shield local banks from outright collapse."
    )
    return make_question(
        rng=rng,
        subskill="27_2007_2008_global_financial_crisis_lesson",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Explain risk of deregulation/market failure", "marks": 2, "type": "A"},
            {"step": "Link to necessity of state financial oversight/mixed economy", "marks": 1, "type": "A"},
        ],
        marking_guide="2 marks for explaining crisis link to deregulation/interdependence; 1 mark for mixed-economy regulation.",
        hints={
            "tier_1": "Ask who had to rescue failing private banks in 2008.",
            "tier_2": "Focus on why prudential banking regulation matters in a mixed economy.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_2008_crisis_was_caused_by_state_command_economies"],
    )


def _build_28_global_economy_definition_interdependence(rng: random.Random, mode: str) -> Dict[str, Any]:
    examples = [
        ("mining platinum in Rustenburg, refining catalytic components in Germany, and selling vehicles across North America", "the interconnected worldwide system in which nations trade goods, services, capital, technology and labour across borders"),
        ("Cape Town call centres supporting European airlines while SA supermarkets stock Brazilian coffee and Chinese electronics", "global economic interdependence linking production, trade and consumption across countries"),
        ("South African pension funds investing on international stock exchanges while foreign automakers build plants in Gqeberha", "cross-border integration of national economies through trade and foreign investment"),
        ("agricultural exporters, shipping lines and overseas retail chains operating as one worldwide network", "one interdependent international marketplace connecting producers and consumers across nations"),
    ]
    case, correct = rng.choice(examples)
    distractors = [
        "a closed village system that forbids foreign goods and international currency exchange",
        "the internal municipal budget of a single South African metropolitan city",
        "a government rule requiring all food to be grown within 10 km of every consumer",
    ]
    prompt = f"Which option best defines the **global economy**, as illustrated by *{case}*?"
    sol = f"- **Global Economy:** {correct.capitalize()}."
    return make_question(
        rng=rng,
        subskill="28_global_economy_definition_interdependence",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct.capitalize(),
        sample_answer=correct.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Select accurate global economy definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurate definition of global economic interdependence.",
        hints={
            "tier_1": "Notice that production spans multiple continents.",
            "tier_2": "Look for cross-border trade, investment and interdependence.",
            "tier_3": correct.capitalize(),
        },
        misconception_tags=["confuses_global_economy_with_closed_domestic_economy"],
        options=[correct.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_29_globalisation_concept_drivers(rng: random.Random, mode: str) -> Dict[str, Any]:
    drivers = [
        ("high-speed fibre internet and cloud software allowing instant cross-border payments and teamwork", "fast digital communication and ICT"),
        ("standardised steel shipping containers slashing ocean freight times and costs", "cheaper, faster global transport"),
        ("lower import tariffs negotiated under international trade agreements", "trade liberalisation and reduced tariff barriers"),
        ("multinational corporations establishing factories and supply hubs across dozens of countries", "expansion of multinational corporations and global capital flows"),
    ]
    clue, driver = rng.choice(drivers)
    prompt = (
        f"**Globalisation** deepens economic integration worldwide.\n\n"
        f"(a) Define the term **globalisation**.\n"
        f"(b) Identify the driver described by *{clue}* and give ONE additional driver."
    )
    ans = f"Globalisation: worldwide integration and trade/exchange of goods, services, capital and ideas across countries; Driver: {driver}"
    sol = (
        f"**(a) Globalisation:** The increasing integration and trade/exchange of goods, services, capital, technology and people across national borders.\n"
        f"**(b) Drivers:** The scenario illustrates **{driver}**; another key driver is improved ocean/air logistics, lower trade tariffs, or multinational enterprises."
    )
    return make_question(
        rng=rng,
        subskill="29_globalisation_concept_drivers",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define globalisation accurately", "marks": 2, "type": "A"},
            {"step": "Identify scenario driver + one extra driver", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for definition; 1 mark for scenario driver; 1 mark for second valid driver.",
        hints={
            "tier_1": "Focus on faster cross-border integration of trade, technology and capital.",
            "tier_2": "Consider ICT, shipping containers, tariffs and multinational firms.",
            "tier_3": ans,
        },
        misconception_tags=["defines_globalisation_as_tourism_only"],
    )


def _build_30_globalisation_benefits_consumers_firms(rng: random.Random, mode: str) -> Dict[str, Any]:
    firms = [
        ("Western Cape citrus farmers exporting oranges to Europe and Asia", "larger global export markets and foreign currency earnings"),
        ("South African consumers choosing affordable smartphones and appliances from competing brands", "wider consumer choice and lower prices through international competition"),
        ("Gauteng engineering plants licensing precision robotics from Germany", "access to advanced foreign technology and skills transfer"),
        ("automotive manufacturers attracting foreign direct investment (FDI) to build assembly lines in Tshwane and Gqeberha", "foreign capital inflow creating local skilled jobs"),
    ]
    case, benefit = rng.choice(firms)
    prompt = (
        f"Explain how South African households or producers gain from globalisation through *{case}*, "
        f"and identify ONE additional benefit of globalisation for South Africa."
    )
    ans = f"Benefit shown: {benefit}; additional benefit: access to cheaper inputs, FDI, technology transfer or broader export markets"
    sol = (
        f"- **Primary Benefit Illustrated:** {benefit.capitalize()}.\n"
        f"- **Additional Benefit:** Increased competition drives efficiency, draws foreign direct investment, and brings global technological innovation to local firms."
    )
    return make_question(
        rng=rng,
        subskill="30_globalisation_benefits_consumers_firms",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain benefit directly illustrated", "marks": 2, "type": "A"},
            {"step": "State one additional valid benefit", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for contextual benefit; 2 marks for distinct second benefit.",
        hints={
            "tier_1": "Think of export scale, consumer variety, lower prices, FDI and technology.",
            "tier_2": "Distinguish consumer gains from producer export/technology gains.",
            "tier_3": ans,
        },
        misconception_tags=["ignores_export_market_access_for_local_farmers"],
    )


def _build_31_globalisation_risks_local_industry(rng: random.Random, mode: str) -> Dict[str, Any]:
    risks = [
        ("Cape Town clothing factories closing because ultra-cheap imported garments flood retail stores", "closure of uncompetitive local industries and domestic job losses"),
        ("qualified doctors, nurses and software engineers emigrating for higher salaries abroad", "brain drain (loss of scarce domestic skilled professionals)"),
        ("a sudden slowdown in foreign commodity demand immediately reducing South African export revenues", "heightened vulnerability to global economic downturns"),
        ("large multinational retailers squeezing out small independent township shops", "local SMEs struggling against giant multinational scale"),
    ]
    case, risk = rng.choice(risks)
    distractors = [
        "complete isolation from international shipping and export markets",
        "citizens receiving identical guaranteed pay regardless of effort",
        "zero imported fuel, machinery or consumer electronics entering ports",
    ]
    prompt = f"Which economic **challenge** of globalisation for developing countries is illustrated by *{case}*?"
    sol = f"- **Challenge:** {risk.capitalize()}.\n- Developing economies must balance openness with skills training and targeted industry support."
    return make_question(
        rng=rng,
        subskill="31_globalisation_risks_local_industry",
        question_type="mcq",
        prompt=prompt,
        correct_answer=risk.capitalize(),
        sample_answer=risk.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify challenge of globalisation", "marks": 2, "type": "A"}],
        marking_guide="2 marks for matching scenario to globalisation risk.",
        hints={
            "tier_1": "Look for local jobs, skills or vulnerability under global competition.",
            "tier_2": "Focus on the specific harm mentioned in the scenario.",
            "tier_3": risk.capitalize(),
        },
        misconception_tags=["assumes_globalisation_has_only_positive_effects"],
        options=[risk.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_32_brics_membership_objectives(rng: random.Random, mode: str) -> Dict[str, Any]:
    angles = [
        ("South Africa joining in December 2010 / attending its first summit in 2011", "strengthening trade, infrastructure financing (New Development Bank) and diplomatic voice among major emerging markets"),
        ("Brazil, Russia, India, China and South Africa forming a cooperative economic bloc", "expanding intra-bloc investment, trade diversification and technology sharing outside traditional Western blocs"),
        ("using the New Development Bank (NDB) to co-finance renewable energy, water and port upgrades", "mobilising long-term development capital for emerging-economy infrastructure"),
        ("expanding South African mineral and agricultural sales directly into large Asian and Latin American markets", "diversifying export destinations and boosting emerging-market cooperation"),
    ]
    focus, goal = rng.choice(angles)
    prompt = (
        f"**BRICS** is an influential emerging-market economic grouping ({focus}).\n\n"
        f"(a) Name the **FIVE** founding/core member countries represented by the acronym **BRICS**.\n"
        f"(b) Explain South Africa's main economic objective for participating in BRICS."
    )
    ans = f"Brazil, Russia, India, China, South Africa; Objective: {goal}"
    sol = (
        f"**(a) Five BRICS Members:** **B**razil, **R**ussia, **I**ndia, **C**hina, and **S**outh Africa.\n"
        f"**(b) Economic Objective:** {goal.capitalize()}, creating jobs and infrastructure investment opportunities for South Africa."
    )
    return make_question(
        rng=rng,
        subskill="32_brics_membership_objectives",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Correctly name all 5 BRICS countries (2 marks: half mark each rounded / key accuracy)", "marks": 2, "type": "A"},
            {"step": "Explain SA trade/investment/NDB objective", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for naming all five countries accurately; 2 marks for strategic trade/investment objective.",
        hints={
            "tier_1": "Each letter B-R-I-C-S stands for a major emerging nation.",
            "tier_2": "Think trade diversification, foreign investment and New Development Bank infrastructure loans.",
            "tier_3": ans,
        },
        misconception_tags=["replaces_russia_with_rwanda_or_china_with_canada"],
    )


def _build_33_brics_trade_share_analysis(rng: random.Random, mode: str) -> Dict[str, Any]:
    china_v = rng.randint(185, 245)
    india_v = rng.randint(85, 130)
    brazil_v = rng.randint(24, 48)
    russia_v = rng.randint(12, 28)
    bars = [
        ("China", float(china_v), "#dc2626"),
        ("India", float(india_v), "#f59e0b"),
        ("Brazil", float(brazil_v), "#16a34a"),
        ("Russia", float(russia_v), "#2563eb"),
    ]
    total = china_v + india_v + brazil_v + russia_v
    china_share = round(china_v * 100.0 / total, 1)
    diagram = _svg_horizontal_bar_chart("SA Annual Export Value to BRICS Partners (R billions)", bars, "bn")
    prompt = (
        f"Study the horizontal bar comparison of South Africa's annual exports to key BRICS partners "
        f"(China R{china_v}bn, India R{india_v}bn, Brazil R{brazil_v}bn, Russia R{russia_v}bn).\n\n"
        f"(a) Calculate South Africa's total export value across these four partners.\n"
        f"(b) Calculate China's percentage share of this BRICS export total (to 1 decimal place)."
    )
    ans = f"Total = R{total} billion; China's share = {fmt_dec(china_share)}%"
    sol = (
        f"**(a) Total Exports:** $R{china_v} + R{india_v} + R{brazil_v} + R{russia_v} = \\text{{R}}{total}\\text{{ billion}}$\n"
        f"**(b) China's Percentage Share:** $\\frac{{{china_v}}}{{{total}}} \\times 100 = {fmt_dec(china_share)}\\%$"
    )
    return make_question(
        rng=rng,
        subskill="33_brics_trade_share_analysis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Sum total R{total} billion", "marks": 2, "type": "A"},
            {"step": f"Compute China's share {fmt_dec(china_share)}%", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for correct total sum; 2 marks for accurate % share.",
        hints={
            "tier_1": "Add all four bar values first.",
            "tier_2": f"Divide China's value (R{china_v}bn) by the combined total and multiply by 100.",
            "tier_3": ans,
        },
        misconception_tags=["divides_china_by_all_other_three_instead_of_total"],
        diagram_spec=diagram,
    )


def _build_34_sa_top_export_partners_bar_chart(rng: random.Random, mode: str) -> Dict[str, Any]:
    china_p = rng.choice([9.7, 10.4, 11.2, 10.8])
    usa_p = rng.choice([8.8, 8.2, 7.9, 8.5])
    ger_p = rng.choice([8.1, 7.6, 7.4, 8.0])
    jap_p = rng.choice([7.0, 6.5, 6.8, 7.2])
    uk_p = rng.choice([5.1, 4.8, 5.4, 5.0])
    bots_p = rng.choice([3.8, 4.1, 3.6, 4.0])
    bars = [
        ("China", china_p, "#ef4444"),
        ("USA", usa_p, "#2563eb"),
        ("Germany", ger_p, "#f59e0b"),
        ("Japan", jap_p, "#8b5cf6"),
        ("United Kingdom", uk_p, "#06b6d4"),
        ("Botswana", bots_p, "#10b981"),
    ]
    top_two = round(china_p + usa_p, 1)
    diagram = _svg_horizontal_bar_chart("South Africa's Leading Export Partners (% Share)", bars, "%")
    prompt = (
        f"Examine South Africa's export partner shares plotted in the bar display "
        f"(China {fmt_dec(china_p)}%, USA {fmt_dec(usa_p)}%, Germany {fmt_dec(ger_p)}%, "
        f"Japan {fmt_dec(jap_p)}%, UK {fmt_dec(uk_p)}%, Botswana {fmt_dec(bots_p)}%).\n\n"
        f"(a) Identify South Africa's single largest individual trading partner shown.\n"
        f"(b) Calculate the combined export share of the top TWO partners."
    )
    ans = f"Largest partner: China ({fmt_dec(china_p)}%); Combined top-two share: {fmt_dec(top_two)}%"
    sol = (
        f"**(a) Largest Individual Partner:** **China** ({fmt_dec(china_p)}%).\n"
        f"**(b) Combined Top-Two Share:** ${fmt_dec(china_p)}\\% + {fmt_dec(usa_p)}\\% = {fmt_dec(top_two)}\\%$."
    )
    return make_question(
        rng=rng,
        subskill="34_sa_top_export_partners_bar_chart",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Identify China as largest partner", "marks": 1, "type": "A"},
            {"step": f"Calculate top-two share {fmt_dec(top_two)}%", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for identifying China; 2 marks for adding top two shares accurately.",
        hints={
            "tier_1": "Look for the longest individual country bar.",
            "tier_2": f"Add the percentages for China and USA ({fmt_dec(china_p)}% + {fmt_dec(usa_p)}%).",
            "tier_3": ans,
        },
        misconception_tags=["includes_eu_total_without_distinguishing_individual_partner"],
        diagram_spec=diagram,
    )


def _build_35_imports_vs_exports_balance_of_trade(rng: random.Random, mode: str) -> Dict[str, Any]:
    exports_bn = rng.choice([1840, 1920, 1650, 2040, 1780])
    delta = rng.choice([-110, -75, 95, 140, -60, 125])
    imports_bn = exports_bn - delta
    status = "trade surplus" if delta > 0 else "trade deficit"
    prompt = (
        f"In a given year, South Africa records merchandise **exports** of R{exports_bn} billion "
        f"and merchandise **imports** of R{imports_bn} billion.\n\n"
        f"(a) Distinguish between **exports** and **imports**.\n"
        f"(b) Calculate the **balance of trade** (`Exports - Imports`) and state whether the country achieved a trade surplus or trade deficit."
    )
    sign_str = f"+R{delta} billion" if delta >= 0 else f"-R{abs(delta)} billion"
    ans = f"Exports leave SA (earn foreign currency); Imports enter SA (spend currency); Balance = {sign_str} ({status})"
    sol = (
        f"**(a) Definitions:**\n"
        f"- **Exports:** Goods and services produced domestically and sold to buyers in other countries (inflow of foreign currency).\n"
        f"- **Imports:** Foreign-produced goods and services purchased by domestic households and firms (outflow of currency).\n\n"
        f"**(b) Trade Balance:**\n"
        f"- $\\text{{Balance}} = \\text{{R}}{exports_bn}\\text{{bn}} - \\text{{R}}{imports_bn}\\text{{bn}} = {sign_str}$\n"
        f"- Because exports are {'greater' if delta > 0 else 'smaller'} than imports, this is a **{status}**."
    )
    return make_question(
        rng=rng,
        subskill="35_imports_vs_exports_balance_of_trade",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define exports and imports clearly", "marks": 2, "type": "A"},
            {"step": f"Calculate balance {sign_str}", "marks": 1, "type": "A"},
            {"step": f"Identify {status}", "marks": 1, "type": "CA"},
        ],
        marking_guide="2 marks for definitions; 1 mark for arithmetic difference; 1 mark for surplus/deficit label.",
        hints={
            "tier_1": "Exports exit South Africa and bring money in; imports enter South Africa.",
            "tier_2": "Trade balance = Exports minus Imports.",
            "tier_3": ans,
        },
        misconception_tags=["reverses_exports_minus_imports_formula"],
    )


def _build_36_sa_primary_vs_manufactured_exports(rng: random.Random, mode: str) -> Dict[str, Any]:
    commodities = [
        ("raw iron ore", 1400, "fabricated structural steel", 4900, 120),
        ("raw platinum concentrate", 18500, "finished catalytic converter units", 52000, 15),
        ("unprocessed wool bales", 950, "woven export blankets", 3100, 80),
        ("fresh citrus fruit", 620, "bottled export juice concentrate", 1860, 150),
        ("crude hardwood timber", 1100, "crafted export furniture", 3850, 40),
    ]
    raw_name, raw_p, proc_name, proc_p, qty = rng.choice(commodities)
    gain_per_t = proc_p - raw_p
    total_gain = gain_per_t * qty
    prompt = (
        f"South Africa traditionally exports raw commodities such as {raw_name} at {fmt_zar(raw_p)} per unit, "
        f"yet local **beneficiation** can convert it into {proc_name} valued at {fmt_zar(proc_p)} per unit.\n\n"
        f"(a) Calculate the additional export value earned across {qty} units when processed locally instead of exported raw.\n"
        f"(b) Explain why beneficiation strengthens South Africa's economic system."
    )
    ans = f"Additional value = {fmt_zar(total_gain)}; retains manufacturing jobs, tax revenue and higher export earnings inside SA"
    sol = (
        f"**(a) Value Added:**\n"
        f"- Gain per unit $= {fmt_zar(proc_p)} - {fmt_zar(raw_p)} = {fmt_zar(gain_per_t)}$\n"
        f"- Total gain $= {qty} \\times {fmt_zar(gain_per_t)} = {fmt_zar(total_gain)}$\n\n"
        f"**(b) Economic Advantage:** Beneficiation creates skilled local manufacturing jobs, keeps higher profits and tax revenues in South Africa, and reduces costly re-importing of finished goods."
    )
    return make_question(
        rng=rng,
        subskill="36_sa_primary_vs_manufactured_exports",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate value add {fmt_zar(total_gain)}", "marks": 2, "type": "A"},
            {"step": "Explain local jobs + higher export revenue", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for value-add calculation; 2 marks for explaining manufacturing jobs & foreign exchange gain.",
        hints={
            "tier_1": "Subtract the raw price per unit from the processed price per unit first.",
            "tier_2": f"Multiply ({proc_p} - {raw_p}) by {qty} units.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_to_multiply_per_unit_gain_by_quantity"],
    )


def _build_37_technological_innovation_export_competitiveness(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("precision automated sorting in Limpopo citrus packhouses", 220, 176, "lower spoilage and competitive international pricing"),
        ("digital ore-sensing equipment in Northern Cape mining", 950, 760, "lower extraction cost per tonne and higher export reliability"),
        ("e-commerce tracking and cold-chain logistics at Durban harbour", 480, 384, "faster delivery to overseas supermarket chains"),
        ("solar-powered irrigation pumps on Karoo wool farms", 350, 266, "lower unit production cost and clean export branding"),
    ]
    tech, old_cost, new_cost, impact = rng.choice(cases)
    pct_cut = round(((old_cost - new_cost) / old_cost) * 100, 1)
    prompt = (
        f"Adopting **{tech}** cuts a South African exporter's unit cost from {fmt_zar(old_cost)} to {fmt_zar(new_cost)}.\n\n"
        f"(a) Calculate the percentage reduction in cost per unit.\n"
        f"(b) Explain how technological innovation and globalisation together expand South African export markets."
    )
    ans = f"-{fmt_dec(pct_cut)}% cost reduction; {impact}, reaching wider international buyers via modern transport & digital communication"
    sol = (
        f"**(a) Unit Cost Reduction:**\n"
        f"- Saving $= {fmt_zar(old_cost - new_cost)}$\n"
        f"- Percentage reduction $= \\frac{{{old_cost - new_cost}}}{{{old_cost}}} \\times 100 = {fmt_dec(pct_cut)}\\%$\n\n"
        f"**(b) Competitiveness Impact:** Technology improves efficiency ({impact}), while global transport and digital marketing help local exporters reach customers worldwide."
    )
    return make_question(
        rng=rng,
        subskill="37_technological_innovation_export_competitiveness",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Compute {fmt_dec(pct_cut)}% cost reduction", "marks": 2, "type": "A"},
            {"step": "Link technology + global marketing/logistics to export competitiveness", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage calculation; 2 marks for explaining competitiveness and market reach.",
        hints={
            "tier_1": "Divide cost saving by the original unit cost.",
            "tier_2": "Explain both efficiency/price competitiveness and global customer reach.",
            "tier_3": ans,
        },
        misconception_tags=["divides_saving_by_new_cost_instead_of_original_cost"],
    )


def _build_38_exchange_rate_zar_import_export_effect(rng: random.Random, mode: str) -> Dict[str, Any]:
    rates = [(17.50, 19.50), (18.00, 20.00), (17.20, 19.00), (18.40, 20.40), (16.80, 18.80)]
    r_old, r_new = rng.choice(rates)
    usd_invoice = rng.choice([400, 500, 650, 800])
    zar_old = usd_invoice * r_old
    zar_new = usd_invoice * r_new
    extra_zar = zar_new - zar_old
    prompt = (
        f"The South African Rand weakens (depreciates) from **{fmt_zar(r_old)} = US$1** to **{fmt_zar(r_new)} = US$1**.\n\n"
        f"(a) Calculate how much extra Rand a local importer must pay for a US${usd_invoice} equipment invoice after depreciation.\n"
        f"(b) State whether a weaker Rand generally helps South African **exporters** or **importers**, and why."
    )
    ans = f"Extra cost: {fmt_zar(extra_zar)} (from {fmt_zar(zar_old)} to {fmt_zar(zar_new)}); helps exporters because SA goods become cheaper abroad and earn more Rand per Dollar"
    sol = (
        f"**(a) Import Cost Change:**\n"
        f"- Before: $\\text{{US\\$}}{usd_invoice} \\times {fmt_dec(r_old, 2)} = {fmt_zar(zar_old)}$\n"
        f"- After: $\\text{{US\\$}}{usd_invoice} \\times {fmt_dec(r_new, 2)} = {fmt_zar(zar_new)}$\n"
        f"- Extra Rand needed $= {fmt_zar(zar_new)} - {fmt_zar(zar_old)} = {fmt_zar(extra_zar)}$\n\n"
        f"**(b) Exporters vs Importers:** A weaker Rand **helps South African exporters** (foreign buyers pay less in Dollars, and exporters convert Dollars into more Rand), while hurting importers via higher Rand import bills."
    )
    return make_question(
        rng=rng,
        subskill="38_exchange_rate_zar_import_export_effect",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate old & new Rand totals and extra {fmt_zar(extra_zar)}", "marks": 2, "type": "A"},
            {"step": "Identify exporters benefit and give clear reason", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Rand conversion difference; 2 marks for explaining exporter advantage.",
        hints={
            "tier_1": "Multiply the USD invoice by both exchange rates first.",
            "tier_2": "A weaker Rand makes foreign invoices cost more Rand, but boosts Rand receipts for export sales.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_weaker_rand_makes_imports_cheaper"],
    )


def _build_39_multinational_corporations_in_sa(rng: random.Random, mode: str) -> Dict[str, Any]:
    mncs = [
        ("an international vehicle manufacturer assembling engines in Rosslyn", "direct skilled job creation, local supplier contracts and tax contributions", "repatriating net dividends overseas rather than reinvesting everything locally"),
        ("a global cloud-tech company building data centres in Johannesburg", "skills training for local engineers and world-class infrastructure", "concentrating high-level research patents outside South Africa"),
        ("a multinational beverage group operating bottling lines across provinces", "steady tax revenue and reliable logistics networks", "displacing smaller independent regional producers"),
        ("an international mining house financing a deep-level shaft", "large-scale foreign direct investment and export tax flows", "exposure to parent-company board decisions made abroad"),
    ]
    firm, pro, con = rng.choice(mncs)
    prompt = (
        f"Evaluate the economic impact of {firm} in South Africa's mixed globalised economy.\n\n"
        f"Give **ONE** positive contribution and **ONE** potential economic concern regarding multinational corporations."
    )
    ans = f"Positive: {pro}; Concern: {con}"
    sol = (
        f"- **Positive Contribution:** {pro.capitalize()}.\n"
        f"- **Potential Concern:** {con.capitalize()}."
    )
    return make_question(
        rng=rng,
        subskill="39_multinational_corporations_in_sa",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "One valid positive contribution of MNC", "marks": 2, "type": "A"},
            {"step": "One valid economic concern", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for balanced positive contribution; 2 marks for valid concern.",
        hints={
            "tier_1": "Think about jobs/FDI/tax versus profit outflow or crowding out small local firms.",
            "tier_2": "Balance employment and skills gains against external control and dividend repatriation.",
            "tier_3": ans,
        },
        misconception_tags=["treats_mncs_as_state_owned_enterprises"],
    )


def _build_40_tariffs_and_trade_protectionism(rng: random.Random, mode: str) -> Dict[str, Any]:
    goods = [
        ("imported cotton T-shirts", 120, 45),
        ("foreign ceramic floor tiles", 240, 25),
        ("imported frozen poultry packs", 80, 35),
        ("imported bicycle tyres", 160, 20),
        ("foreign leather work boots", 400, 30),
    ]
    item, cif_price, tariff_pct = rng.choice(goods)
    duty = cif_price * tariff_pct / 100.0
    landed = cif_price + duty
    prompt = (
        f"To shield local producers from ultra-cheap competition, government imposes a **{tariff_pct}% import tariff** "
        f"on {item} whose pre-duty landed value is {fmt_zar(cif_price)} per unit.\n\n"
        f"(a) Calculate the new tax-inclusive price of the imported item.\n"
        f"(b) Explain ONE reason government uses protective tariffs and ONE cost borne by consumers."
    )
    ans = f"Landed price = {fmt_zar(landed)}; Reason: protects local factory jobs; Consumer cost: higher retail prices"
    sol = (
        f"**(a) Tariff Calculation:**\n"
        f"- Tariff duty $= {fmt_zar(cif_price)} \\times \\frac{{{tariff_pct}}}{{100}} = {fmt_zar(duty)}$\n"
        f"- New price $= {fmt_zar(cif_price)} + {fmt_zar(duty)} = {fmt_zar(landed)}$\n\n"
        f"**(b) Trade-off:**\n"
        f"- **Protection Reason:** Safeguards domestic manufacturing jobs and infant industries.\n"
        f"- **Consumer Cost:** Households pay higher retail prices and face less variety."
    )
    return make_question(
        rng=rng,
        subskill="40_tariffs_and_trade_protectionism",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate tariff {fmt_zar(duty)} and final price {fmt_zar(landed)}", "marks": 2, "type": "A"},
            {"step": "State domestic job protection + higher consumer price cost", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for arithmetic; 2 marks for balanced policy trade-off.",
        hints={
            "tier_1": "Add the percentage tariff onto the original pre-duty price.",
            "tier_2": "Consider both local worker protection and household checkout prices.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_tariff_from_price_instead_of_adding"],
    )


def _build_41_mixed_economy_income_inequality_gini(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        (360000, 18, 840000, 35),
        (240000, 15, 720000, 32),
        (300000, 16, 900000, 36),
        (420000, 20, 960000, 38),
    ]
    low_inc, low_rate, high_inc, high_rate = rng.choice(cases)
    low_tax = low_inc * low_rate / 100.0
    high_tax = high_inc * high_rate / 100.0
    prompt = (
        f"In a mixed economy using **progressive taxation** to curb market inequality, "
        f"Citizen A earns {fmt_zar(low_inc)}/year (average tax {low_rate}%) while Citizen B earns {fmt_zar(high_inc)}/year (average tax {high_rate}%).\n\n"
        f"(a) Calculate the annual income tax paid by Citizen A and Citizen B.\n"
        f"(b) Explain how progressive taxation narrows post-tax inequality compared with a pure market economy."
    )
    ans = f"Citizen A tax: {fmt_zar(low_tax)}; Citizen B tax: {fmt_zar(high_tax)}; higher earners pay a larger percentage to fund public clinics, schools and grants"
    sol = (
        f"**(a) Tax Paid:**\n"
        f"- Citizen A $= {fmt_zar(low_inc)} \\times {low_rate}\\% = {fmt_zar(low_tax)}$\n"
        f"- Citizen B $= {fmt_zar(high_inc)} \\times {high_rate}\\% = {fmt_zar(high_tax)}$\n\n"
        f"**(b) Inequality Impact:** Higher-income households contribute a larger proportion of their income, funding public education, clinics and social grants that uplift lower-income households."
    )
    return make_question(
        rng=rng,
        subskill="41_mixed_economy_income_inequality_gini",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Citizen A {fmt_zar(low_tax)} and Citizen B {fmt_zar(high_tax)}", "marks": 2, "type": "A"},
            {"step": "Explain progressive tax funding public services/grants", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for both tax amounts; 2 marks for redistribution explanation.",
        hints={
            "tier_1": "Multiply each annual income by its own tax percentage.",
            "tier_2": "Progressive tax means both total Rand tax and percentage rate rise with income.",
            "tier_3": ans,
        },
        misconception_tags=["applies_flat_percentage_to_both_taxpayers"],
    )


def _build_42_planned_to_mixed_transition_reforms(rng: random.Random, mode: str) -> Dict[str, Any]:
    reforms = [
        ("allowing farmers to sell surplus harvests privately after delivering modest state quotas", "private profit incentives boost farm productivity and food variety"),
        ("creating coastal Special Economic Zones open to foreign factories while keeping key state banks", "moving toward a mixed system attracts foreign capital and exports"),
        ("letting small restaurants and repair shops operate privately instead of banning private trade", "consumer choice expands and local employment diversifies"),
        ("replacing uniform fixed state wages with performance bonuses and market-determined retail prices", "efficiency rises and chronic consumer shortages diminish"),
    ]
    reform, result = rng.choice(reforms)
    prompt = (
        f"During late-20th-century economic transition reforms, formerly strict command economies adopted measures like *{reform}*.\n\n"
        f"(a) Identify which direction along the economic spectrum this transition represents.\n"
        f"(b) Explain how consumer welfare and factory productivity change under these reforms."
    )
    ans = f"Shift from pure planned toward a mixed economy; {result}"
    sol = (
        f"**(a) Direction of Shift:** Moving from a strict **planned economy** toward a **mixed economy**.\n"
        f"**(b) Expected Impact:** {result.capitalize()}, reducing bureaucratic waste while retaining strategic public oversight."
    )
    return make_question(
        rng=rng,
        subskill="42_planned_to_mixed_transition_reforms",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Identify planned -> mixed shift", "marks": 1, "type": "A"},
            {"step": "Explain productivity & consumer choice gains", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for direction; 2 marks for productivity and consumer variety effects.",
        hints={
            "tier_1": "Notice that private enterprise is being introduced alongside retained state roles.",
            "tier_2": "When incentives replace strict quotas, supply responds faster to buyers.",
            "tier_3": ans,
        },
        misconception_tags=["claims_introducing_private_shops_eliminates_all_state_roles"],
    )


def _build_43_mixed_economy_public_private_partnership(rng: random.Random, mode: str) -> Dict[str, Any]:
    ppps = [
        ("Gautrain rapid rail link", "private consortium builds and operates trains efficiently while government retains long-term asset ownership and subsidises commuter fares"),
        ("Renewable Energy Independent Power Producers (REIPPs)", "private wind and solar firms finance and build clean power plants selling electricity via long-term grid contracts"),
        ("National toll highway upgrades", "private engineering partners fund road resurfacing quickly in return for regulated toll concessions"),
        ("Provincial hospital equipment & radiology modernisation", "private specialists maintain diagnostic scanners under strict public access standards"),
    ]
    project, mechanism = rng.choice(ppps)
    distractors = [
        "banning private engineering companies from every public construction site",
        "selling public schools outright to foreign stock exchanges with zero regulation",
        "forcing citizens to barter raw food directly at municipal clinics",
    ]
    prompt = f"How does a **Public-Private Partnership (PPP)**—such as South Africa's **{project}**—illustrate mixed-economy cooperation?"
    sol = f"- **PPP Mechanism:** {mechanism.capitalize()}.\n- PPPs combine private capital and operational efficiency with public oversight."
    return make_question(
        rng=rng,
        subskill="43_mixed_economy_public_private_partnership",
        question_type="mcq",
        prompt=prompt,
        correct_answer=mechanism.capitalize(),
        sample_answer=mechanism.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify PPP shared risk/delivery mechanism", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurate explanation of public-private partnership.",
        hints={
            "tier_1": "Look for collaboration rather than pure nationalisation or pure deregulation.",
            "tier_2": "Private partners bring capital and efficiency; the state safeguards public standards.",
            "tier_3": mechanism.capitalize(),
        },
        misconception_tags=["thinks_ppp_means_permanent_loss_of_public_oversight"],
        options=[mechanism.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_44_resource_allocation_bar_chart_comparison(rng: random.Random, mode: str) -> Dict[str, Any]:
    pub_cmd = rng.choice([88, 84, 90, 82])
    pub_mix = rng.choice([36, 40, 34, 42])
    pub_mkt = rng.choice([14, 16, 12, 18])
    countries = [
        ("Country X", pub_cmd, 100 - pub_cmd),
        ("Country Y", pub_mix, 100 - pub_mix),
        ("Country Z", pub_mkt, 100 - pub_mkt),
    ]
    gdp_y = rng.choice([500, 600, 750, 800])
    pub_val_y = round(gdp_y * pub_mix / 100.0)
    diagram = _svg_stacked_country_shares(countries)
    prompt = (
        f"Analyse the stacked output comparison for **Country X ({pub_cmd}% public)**, **Country Y ({pub_mix}% public)**, "
        f"and **Country Z ({pub_mkt}% public)**.\n\n"
        f"(a) Match Country X, Country Y, and Country Z to the closest economic system type "
        f"(predominantly Planned, Balanced Mixed, predominantly Market).\n"
        f"(b) If Country Y's total GDP is R{gdp_y} billion, calculate the Rand value of its public-sector output."
    )
    ans = f"X: predominantly Planned ({pub_cmd}% public); Y: Balanced Mixed ({pub_mix}% public); Z: predominantly Market ({pub_mkt}% public); Y public output = R{pub_val_y} billion"
    sol = (
        f"**(a) System Classification:**\n"
        f"- **Country X** ({pub_cmd}% public / {100 - pub_cmd}% private) $\\rightarrow$ predominantly **Planned**.\n"
        f"- **Country Y** ({pub_mix}% public / {100 - pub_mix}% private) $\\rightarrow$ **Balanced Mixed**.\n"
        f"- **Country Z** ({pub_mkt}% public / {100 - pub_mkt}% private) $\\rightarrow$ predominantly **Market**.\n\n"
        f"**(b) Country Y Public Output:** $\\text{{R}}{gdp_y}\\text{{bn}} \\times \\frac{{{pub_mix}}}{{100}} = \\text{{R}}{pub_val_y}\\text{{ billion}}$."
    )
    return make_question(
        rng=rng,
        subskill="44_resource_allocation_bar_chart_comparison",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": "Classify Country X, Y, Z accurately (1 mark each)", "marks": 3, "type": "A"},
            {"step": f"Calculate Country Y public GDP R{pub_val_y} billion", "marks": 2, "type": "A"},
        ],
        marking_guide="3 marks for matching the 3 percentages; 2 marks for GDP share calculation.",
        hints={
            "tier_1": "High public % points toward state command; high private % points toward free markets.",
            "tier_2": f"Multiply Country Y's R{gdp_y}bn GDP by {pub_mix}%.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_private_and_public_bars"],
        diagram_spec=diagram,
    )


def _build_45_consumer_sovereignty_vs_state_quotas(rng: random.Random, mode: str) -> Dict[str, Any]:
    goods = [
        ("winter coats", 12000, 17500),
        ("smart-meter units", 8000, 11200),
        ("textbook packs", 20000, 26000),
        ("bicycle tyres", 15000, 21000),
    ]
    item, quota, demand = rng.choice(goods)
    shortfall = demand - quota
    prompt = (
        f"A central planning agency fixes a strict annual quota of {quota:,}".replace(",", " ")
        + f" {item}, whereas actual household demand reaches {demand:,}".replace(",", " ")
        + f" units.\n\n"
        f"(a) Calculate the unmet consumer shortage.\n"
        f"(b) Contrast how **consumer sovereignty** in a market economy resolves this mismatch differently from state quotas."
    )
    ans = f"Shortage = {shortfall} units; under consumer sovereignty, rising demand and higher prices induce firms to expand supply automatically"
    sol = (
        f"**(a) Shortage Calculation:** ${demand} - {quota} = {shortfall}$ units unsatisfied.\n"
        f"**(b) Consumer Sovereignty Contrast:** Under consumer sovereignty, household spending acts like 'Rand votes'—excess demand raises prices and profits, prompting competing firms to rapidly increase output of {item}."
    )
    return make_question(
        rng=rng,
        subskill="45_consumer_sovereignty_vs_state_quotas",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate shortage of {shortfall} units", "marks": 1, "type": "A"},
            {"step": "Explain consumer sovereignty ('spending votes') adjusting supply", "marks": 3, "type": "A"},
        ],
        marking_guide="1 mark for shortage calculation; 3 marks for contrasting consumer sovereignty against rigid quotas.",
        hints={
            "tier_1": "Subtract the fixed quota from actual demand.",
            "tier_2": "Consumer sovereignty means buyers steer what firms produce through spending choices.",
            "tier_3": ans,
        },
        misconception_tags=["equates_consumer_sovereignty_with_monarch_rule"],
    )


def _build_46_comparative_trade_balance_table(rng: random.Random, mode: str) -> Dict[str, Any]:
    partners = ["Partner Alpha", "Partner Beta", "Partner Gamma"]
    e1, i1 = rng.randint(140, 190), rng.randint(95, 130)
    e2, i2 = rng.randint(70, 105), rng.randint(120, 165)
    e3, i3 = rng.randint(110, 150), rng.randint(80, 105)
    data = [
        (partners[0], e1, i1, e1 - i1, "Surplus"),
        (partners[1], e2, i2, e2 - i2, "Deficit"),
        (partners[2], e3, i3, e3 - i3, "Surplus"),
    ]
    headers = ["Partner", "Exports (R bn)", "Imports (R bn)", "Trade Balance (R bn)", "Status"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [
        "| Partner | Exports (R bn) | Imports (R bn) | Trade Balance (R bn) | Status |",
        "|---|---|---|---|---|",
    ]
    for r_idx, (p, ex, im, bal, st) in enumerate(data, start=1):
        vals = [p, str(ex), str(im), str(bal), st]
        req_cols = [3, 4] if r_idx != 2 else [3]
        row_cells: List[Dict[str, Any]] = []
        for c_idx, val in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            is_req = c_idx in req_cols
            row_cells.append({
                "coordinate": coord,
                "value": "" if is_req else val,
                "type": "required" if is_req else "given",
                "editable": is_req,
            })
            if is_req:
                correct_map[coord] = val
                cell_hints[coord] = "Use Trade Balance = Exports - Imports; positive = Surplus, negative = Deficit."
        rows_ui.append(row_cells)
        md_lines.append(f"| {p} | {ex} | {im} | {bal} | {st} |")

    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="46_comparative_trade_balance_table",
        question_type="table_completion",
        prompt="Complete the South African Bilateral Trade Summary table by calculating each Trade Balance (`Exports - Imports`) and classifying Surplus or Deficit.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Completed Trade Balance Table:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per calculated balance or Surplus/Deficit classification.",
        hints={
            "tier_1": "Subtract Imports from Exports for each row.",
            "tier_2": "A positive difference is a Surplus; a negative difference is a Deficit.",
            "tier_3": md_table,
        },
        misconception_tags=["forgets_negative_sign_on_trade_deficit"],
        table_payload={
            "headers": headers,
            "columns": [{"key": h.lower().replace(" ", "_"), "label": h} for h in headers],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_47_minimum_wage_and_labour_market_intervention(rng: random.Random, mode: str) -> Dict[str, Any]:
    wage_rates = [27.58, 28.79, 29.00, 30.20, 26.50]
    min_hr = rng.choice(wage_rates)
    hours_wk = rng.choice([40, 45])
    weeks = 4
    min_4wk = round(min_hr * hours_wk * weeks, 2)
    prompt = (
        f"In South Africa's mixed economy, government enforces a **National Minimum Wage** of **{fmt_zar(min_hr)} per hour**.\n\n"
        f"(a) Calculate the minimum legal gross pay for a worker completing {hours_wk} hours per week over {weeks} weeks.\n"
        f"(b) Explain why a mixed economy uses a minimum wage rather than leaving wages completely unregulated."
    )
    ans = f"Minimum 4-week pay = {fmt_zar(min_4wk)}; protects vulnerable workers against exploitation and supports basic living standards"
    sol = (
        f"**(a) Minimum Legal Pay:**\n"
        f"- Weekly pay $= {fmt_zar(min_hr)} \\times {hours_wk} = {fmt_zar(min_hr * hours_wk)}$\n"
        f"- 4-week pay $= {fmt_zar(min_hr * hours_wk)} \\times {weeks} = {fmt_zar(min_4wk)}$\n\n"
        f"**(b) Mixed-Economy Purpose:** Prevents extreme wage exploitation in low-bargaining-power jobs and narrows working poverty, unlike an unregulated pure market."
    )
    return make_question(
        rng=rng,
        subskill="47_minimum_wage_and_labour_market_intervention",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate 4-week gross minimum pay {fmt_zar(min_4wk)}", "marks": 2, "type": "A"},
            {"step": "Explain worker protection in mixed economy", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for wage multiplication; 2 marks for explaining labour-market protection.",
        hints={
            "tier_1": "Multiply hourly wage by hours per week, then by 4 weeks.",
            "tier_2": "Consider how minimum wages counter worker exploitation in low-wage jobs.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_to_multiply_weekly_total_by_4_weeks"],
    )


def _build_48_subsidies_and_essential_food_affordability(rng: random.Random, mode: str) -> Dict[str, Any]:
    baskets = [
        ("maize meal, brown bread, milk and cooking oil", 420, 15),
        ("staple food essentials (bread, rice, lentils, milk)", 560, 15),
        ("household basic nutrition basket", 480, 15),
        ("monthly staple groceries (maize, brown bread, eggs, beans)", 640, 15),
    ]
    items, base_cost, vat_pct = rng.choice(baskets)
    vat_saved = base_cost * vat_pct / 100.0
    taxed_cost = base_cost + vat_saved
    prompt = (
        f"South Africa's mixed-economy tax policy zero-rates VAT ({vat_pct}%) on basic staples such as {items}. "
        f"A low-income family's monthly staple basket costs {fmt_zar(base_cost)} VAT-free.\n\n"
        f"(a) Calculate how much more the basket would cost per month if {vat_pct}% VAT were charged.\n"
        f"(b) Explain how zero-rating basic foodstuffs reduces inequality compared with taxing all goods equally."
    )
    ans = f"Monthly VAT saving = {fmt_zar(vat_saved)} (taxed cost would be {fmt_zar(taxed_cost)}); relieves poorer households who spend most of their income on food"
    sol = (
        f"**(a) Monthly Household Saving:**\n"
        f"- VAT saved $= {fmt_zar(base_cost)} \\times \\frac{{{vat_pct}}}{{100}} = {fmt_zar(vat_saved)}$\n"
        f"- Cost if VAT applied $= {fmt_zar(base_cost)} + {fmt_zar(vat_saved)} = {fmt_zar(taxed_cost)}$\n\n"
        f"**(b) Equity Benefit:** Low-income households spend a large fraction of monthly income on basic food, so zero-rating protects food security."
    )
    return make_question(
        rng=rng,
        subskill="48_subsidies_and_essential_food_affordability",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate VAT saving {fmt_zar(vat_saved)}", "marks": 2, "type": "A"},
            {"step": "Explain food security / progressive relief for poor families", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for VAT saving calculation; 2 marks for explaining pro-poor impact.",
        hints={
            "tier_1": "Multiply the VAT-free basket price by 15%.",
            "tier_2": "Consider why food costs weigh far heavier on low-income budgets.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_vat_zero_rating_with_free_state_food_rationing"],
    )


def _build_49_global_supply_chain_shock_impact(rng: random.Random, mode: str) -> Dict[str, Any]:
    shocks = [
        ("international maritime shipping delays", 18000, 12),
        ("global semiconductor shortages affecting imported vehicle electronics", 24000, 15),
        ("sudden global crude-oil spikes raising imported diesel and freight costs", 15000, 20),
        ("overseas port congestion slowing imported machinery deliveries", 32000, 10),
    ]
    shock_name, base_price, pct_jump = rng.choice(shocks)
    increase = base_price * pct_jump / 100.0
    new_price = base_price + increase
    prompt = (
        f"Due to **{shock_name}** in the global economy, the cost of an imported component rises by {pct_jump}% "
        f"from {fmt_zar(base_price)}.\n\n"
        f"(a) Calculate the new Rand price of the component.\n"
        f"(b) Explain how global interdependence transmits overseas supply shocks into South African prices and jobs."
    )
    ans = f"New price = {fmt_zar(new_price)}; higher imported input costs raise domestic retail prices and can slow local factory output"
    sol = (
        f"**(a) New Component Cost:**\n"
        f"- Increase $= {fmt_zar(base_price)} \\times \\frac{{{pct_jump}}}{{100}} = {fmt_zar(increase)}$\n"
        f"- New price $= {fmt_zar(base_price)} + {fmt_zar(increase)} = {fmt_zar(new_price)}$\n\n"
        f"**(b) Transmission Mechanism:** Because local assembly plants depend on imported components and global energy prices, foreign disruptions raise domestic production costs and squeeze local consumer purchasing power."
    )
    return make_question(
        rng=rng,
        subskill="49_global_supply_chain_shock_impact",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate increase {fmt_zar(increase)} and new price {fmt_zar(new_price)}", "marks": 2, "type": "A"},
            {"step": "Explain cost push into local retail prices/output", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for price calculation; 2 marks for explaining global-to-local transmission.",
        hints={
            "tier_1": "Add the percentage rise to the base component price.",
            "tier_2": "Local businesses rely on imported inputs, so overseas delays raise local prices.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_domestic_prices_are_immune_to_global_trade"],
    )


def _build_50_evaluating_sa_economic_policy_tradeoff(rng: random.Random, mode: str) -> Dict[str, Any]:
    policies = [
        ("allowing private freight operators onto Transnet rail corridors under state track ownership", "faster logistics efficiency, private investment and higher export volumes", "tariff/access fairness and safeguarding rural branch lines"),
        ("raising corporate income tax rates sharply to double infrastructure spending", "expanded tax funding for clinics, schools and public works", "risk of lower private business investment and slower private hiring"),
        ("licensing private municipal solar micro-grids alongside municipal distribution", "improved electricity reliability and lower outage losses for SMEs", "protecting municipal cross-subsidy revenue for indigent households"),
        ("tightening import tariffs on imported steel while subsidising local automotive plants", "preserving domestic steel foundry jobs", "higher steel costs for downstream local builders and consumers"),
    ]
    policy, pro, trade_off = rng.choice(policies)
    prompt = (
        f"South Africa considers a mixed-economy reform: *{policy}.*\n\n"
        f"Write a balanced economic evaluation containing:\n"
        f"(a) ONE expected **market/efficiency or fiscal benefit**;\n"
        f"(b) ONE **trade-off or risk** requiring government safeguards;\n"
        f"(c) ONE way the policy reflects the **mixed economy** model."
    )
    ans = f"Benefit: {pro}; Risk/Trade-off: {trade_off}; Mixed trait: blends private participation/market efficiency with public oversight/social safeguards"
    sol = (
        f"**(a) Expected Benefit:** {pro.capitalize()}.\n"
        f"**(b) Trade-off / Safeguard Needed:** {trade_off.capitalize()}.\n"
        f"**(c) Mixed-Economy Synthesis:** Rather than total state monopoly or laissez-faire deregulation, the policy pairs private efficiency with targeted state oversight."
    )
    return make_question(
        rng=rng,
        subskill="50_evaluating_sa_economic_policy_tradeoff",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=6,
        marking_schema=[
            {"step": "Relevant efficiency or fiscal benefit", "marks": 2, "type": "A"},
            {"step": "Clear trade-off or regulatory safeguard", "marks": 2, "type": "A"},
            {"step": "Synthesis connecting private + state roles in mixed economy", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks each for benefit, risk/safeguard, and mixed-economy synthesis.",
        hints={
            "tier_1": "Evaluate both what improves efficiency/revenue and who might face higher costs or risks.",
            "tier_2": "Show how the state and private sector share responsibility.",
            "tier_3": ans,
        },
        misconception_tags=["gives_one_sided_evaluation_without_policy_tradeoff"],
        duration_mins=6,
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_pros_cons_system_matching_matrix": _build_26_pros_cons_system_matching_matrix,
    "27_2007_2008_global_financial_crisis_lesson": _build_27_2007_2008_global_financial_crisis_lesson,
    "28_global_economy_definition_interdependence": _build_28_global_economy_definition_interdependence,
    "29_globalisation_concept_drivers": _build_29_globalisation_concept_drivers,
    "30_globalisation_benefits_consumers_firms": _build_30_globalisation_benefits_consumers_firms,
    "31_globalisation_risks_local_industry": _build_31_globalisation_risks_local_industry,
    "32_brics_membership_objectives": _build_32_brics_membership_objectives,
    "33_brics_trade_share_analysis": _build_33_brics_trade_share_analysis,
    "34_sa_top_export_partners_bar_chart": _build_34_sa_top_export_partners_bar_chart,
    "35_imports_vs_exports_balance_of_trade": _build_35_imports_vs_exports_balance_of_trade,
    "36_sa_primary_vs_manufactured_exports": _build_36_sa_primary_vs_manufactured_exports,
    "37_technological_innovation_export_competitiveness": _build_37_technological_innovation_export_competitiveness,
    "38_exchange_rate_zar_import_export_effect": _build_38_exchange_rate_zar_import_export_effect,
    "39_multinational_corporations_in_sa": _build_39_multinational_corporations_in_sa,
    "40_tariffs_and_trade_protectionism": _build_40_tariffs_and_trade_protectionism,
    "41_mixed_economy_income_inequality_gini": _build_41_mixed_economy_income_inequality_gini,
    "42_planned_to_mixed_transition_reforms": _build_42_planned_to_mixed_transition_reforms,
    "43_mixed_economy_public_private_partnership": _build_43_mixed_economy_public_private_partnership,
    "44_resource_allocation_bar_chart_comparison": _build_44_resource_allocation_bar_chart_comparison,
    "45_consumer_sovereignty_vs_state_quotas": _build_45_consumer_sovereignty_vs_state_quotas,
    "46_comparative_trade_balance_table": _build_46_comparative_trade_balance_table,
    "47_minimum_wage_and_labour_market_intervention": _build_47_minimum_wage_and_labour_market_intervention,
    "48_subsidies_and_essential_food_affordability": _build_48_subsidies_and_essential_food_affordability,
    "49_global_supply_chain_shock_impact": _build_49_global_supply_chain_shock_impact,
    "50_evaluating_sa_economic_policy_tradeoff": _build_50_evaluating_sa_economic_policy_tradeoff,
}
