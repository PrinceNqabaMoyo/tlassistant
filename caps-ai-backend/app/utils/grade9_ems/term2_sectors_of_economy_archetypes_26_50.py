"""Grade 9 EMS Term 2: Sectors of the Economy — Semantic Archetypes 26 to 50."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term2_sectors_of_economy_archetypes_01_25 import fmt_dec, fmt_zar, make_question


def _svg_sector_gdp_comparison(
    c_dev_name: str, p_dev: int, s_dev: int, t_dev: int,
    c_adv_name: str, p_adv: int, s_adv: int, t_adv: int,
) -> Dict[str, Any]:
    """Render SVG stacked horizontal GDP bars comparing Developing vs Developed sector composition."""
    w, h = 620, 225
    x0, bar_w = 185, 360

    def draw_row(y: int, label: str, p: int, s: int, t: int) -> str:
        wp = round(bar_w * p / 100.0)
        ws = round(bar_w * s / 100.0)
        wt = bar_w - wp - ws
        return (
            f'<text x="172" y="{y + 18}" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">{label}</text>'
            f'<rect x="{x0}" y="{y}" width="{wp}" height="28" fill="#d97706"/>'
            f'<rect x="{x0 + wp}" y="{y}" width="{ws}" height="28" fill="#2563eb"/>'
            f'<rect x="{x0 + wp + ws}" y="{y}" width="{wt}" height="28" fill="#059669"/>'
            f'<text x="{x0 + wp // 2}" y="{y + 18}" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{p}%</text>'
            f'<text x="{x0 + wp + ws // 2}" y="{y + 18}" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{s}%</text>'
            f'<text x="{x0 + wp + ws + wt // 2}" y="{y + 18}" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">{t}%</text>'
        )

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto">'
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff" rx="8"/>'
        f'<text x="{w // 2}" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        f'Sector Share of National GDP (%): Developing vs Developed</text>'
        '<rect x="185" y="42" width="12" height="12" fill="#d97706"/><text x="202" y="52" font-size="11" fill="#92400e">Primary %</text>'
        '<rect x="295" y="42" width="12" height="12" fill="#2563eb"/><text x="312" y="52" font-size="11" fill="#1e40af">Secondary %</text>'
        '<rect x="425" y="42" width="12" height="12" fill="#059669"/><text x="442" y="52" font-size="11" fill="#065f46">Tertiary %</text>'
        f'{draw_row(78, c_dev_name, p_dev, s_dev, t_dev)}'
        f'{draw_row(134, c_adv_name, p_adv, s_adv, t_adv)}'
        f'<text x="{w // 2}" y="196" text-anchor="middle" font-size="11" fill="#475569">'
        f'Industrialisation shifts labour and GDP share from raw Primary extraction into Secondary &amp; Tertiary.</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_wage_skill_bars(sector_title: str, u_wage: int, s_wage: int, k_wage: int) -> Dict[str, Any]:
    """Render SVG bar chart of monthly wages by skill tier."""
    max_w = k_wage
    bw = 300
    rows = [
        ("Unskilled Labour", u_wage, "#f59e0b"),
        ("Semi-skilled Labour", s_wage, "#2563eb"),
        ("Skilled Labour", k_wage, "#059669"),
    ]
    bars: List[str] = []
    for idx, (lbl, val, col) in enumerate(rows):
        y = 62 + idx * 42
        w_rect = max(24, round(bw * val / max_w))
        bars.append(
            f'<text x="155" y="{y + 17}" text-anchor="end" font-size="12" font-weight="600" fill="#1e293b">{lbl}</text>'
            f'<rect x="168" y="{y}" width="{w_rect}" height="24" fill="{col}" rx="4"/>'
            f'<text x="{176 + w_rect}" y="{y + 17}" font-size="12" font-weight="700" fill="#0f172a">{fmt_zar(val)}/mo</text>'
        )
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 210" width="100%" height="auto">'
        '<rect x="0" y="0" width="600" height="210" fill="#ffffff" rx="8"/>'
        f'<text x="300" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        f'{sector_title}: Average Monthly Wages by Skill Level</text>'
        f'{"".join(bars)}'
        '</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _build_26_developing_vs_developed_gdp_bar_chart_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    p_dev = rng.choice([34, 38, 42])
    s_dev = rng.choice([24, 22, 20])
    t_dev = 100 - p_dev - s_dev
    p_adv = rng.choice([3, 4, 5])
    s_adv = rng.choice([22, 24, 25])
    t_adv = 100 - p_adv - s_adv
    diagram = _svg_sector_gdp_comparison("Country A", p_dev, s_dev, t_dev, "Country B", p_adv, s_adv, t_adv)
    diff_prim = p_dev - p_adv
    prompt = (
        f"Study the stacked sector GDP composition for **Country A (`{p_dev}%` Primary, `{s_dev}%` Secondary, `{t_dev}%` Tertiary)** "
        f"and **Country B (`{p_adv}%` Primary, `{s_adv}%` Secondary, `{t_adv}%` Tertiary)**.\n\n"
        f"(a) Identify which country is **developing** and which is **developed**, justifying from Primary vs Tertiary shares.\n"
        f"(b) Calculate the percentage-point difference between Country A's and Country B's Primary-sector GDP share."
    )
    ans = f"Country A is developing (high {p_dev}% Primary); Country B is developed (dominant {t_adv}% Tertiary); Difference = {diff_prim} percentage points"
    sol = (
        f"**(a) Classification:**\n"
        f"- **Country A (Developing):** Relies heavily on Primary extraction ({p_dev}%), with smaller Secondary ({s_dev}%) and Tertiary ({t_dev}%) shares.\n"
        f"- **Country B (Developed):** Only {p_adv}% Primary while Tertiary services drive **{t_adv}%** of GDP alongside high-tech manufacturing.\n\n"
        f"**(b) Primary Share Gap:** ${p_dev}\\% - {p_adv}\\% = {diff_prim}$ percentage points."
    )
    return make_question(
        rng=rng,
        subskill="26_developing_vs_developed_gdp_bar_chart_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": "Identify Country A developing and Country B developed with evidence", "marks": 3, "type": "A"},
            {"step": f"Calculate difference {diff_prim} percentage points", "marks": 2, "type": "A"},
        ],
        marking_guide="3 marks for evidence-backed country classification; 2 marks for difference calculation.",
        hints={
            "tier_1": "Developed countries derive roughly 70%+ of GDP from Tertiary services.",
            "tier_2": f"Subtract Country B's {p_adv}% from Country A's {p_dev}%.",
            "tier_3": ans,
        },
        misconception_tags=["labels_high_primary_share_as_developed"],
        diagram_spec=diagram,
    )


def _build_27_primary_sector_dominance_developing_economies(rng: random.Random, mode: str) -> Dict[str, Any]:
    gdp_bn = rng.choice([400, 500, 600])
    prim_pct = rng.choice([36, 40, 44])
    prim_bn = round(gdp_bn * prim_pct / 100.0)
    prompt = (
        f"A developing economy generates total annual GDP of R{gdp_bn} billion, of which **{prim_pct}%** comes from unprocessed Primary farming and mining exports.\n\n"
        f"(a) Calculate the Rand value of Primary-sector GDP.\n"
        f"(b) Give TWO reasons why heavy reliance on raw Primary exports often keeps developing nations' living standards lower than developed industrial nations."
    )
    ans = f"Primary GDP = R{prim_bn} billion; Raw commodities earn lower prices than processed goods, suffer global price volatility, and employ mostly lower-paid unskilled labour"
    sol = (
        f"**(a) Primary GDP Value:** $\\text{{R}}{gdp_bn}\\text{{bn}} \\times {prim_pct}\\% = \\text{{R}}{prim_bn}\\text{{ billion}}$\n"
        f"**(b) Why Living Standards Lag:**\n"
        f"1. **Low Value-Add:** Unprocessed raw ores/crops sell cheaply compared with Secondary manufactured products.\n"
        f"2. **Climate & Price Risk + Lower Wages:** Commodity prices fluctuate sharply, and primary extraction relies heavily on lower-wage unskilled labour."
    )
    return make_question(
        rng=rng,
        subskill="27_primary_sector_dominance_developing_economies",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate Primary GDP R{prim_bn}bn", "marks": 2, "type": "A"},
            {"step": "Give two reasons linking raw commodity reliance to lower incomes", "marks": 3, "type": "A"},
        ],
        marking_guide="2 marks for GDP math; 3 marks for two clear developmental reasons.",
        hints={
            "tier_1": f"Multiply R{gdp_bn}bn by {prim_pct}%.",
            "tier_2": "Contrast raw commodity prices and wages against manufactured/service economies.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_having_fertile_minerals_automatically_creates_developed_wages"],
    )


def _build_28_tertiary_sector_dominance_developed_economies(rng: random.Random, mode: str) -> Dict[str, Any]:
    gdp_bn = rng.choice([8000, 9000, 10000])
    tert_pct = rng.choice([72, 74, 76])
    tert_bn = round(gdp_bn * tert_pct / 100.0)
    prompt = (
        f"In a developed high-income country with annual GDP of R{gdp_bn:,}".replace(",", " ")
        + f" billion, the **Tertiary sector** contributes **{tert_pct}%** of national output.\n\n"
        f"(a) Calculate the Tertiary sector's Rand billion contribution.\n"
        f"(b) Explain TWO reasons why developed nations hold higher living standards when Tertiary services and high-tech Secondary manufacturing dominate."
    )
    ans = f"Tertiary GDP = R{tert_bn:,} billion; Skilled services/finance/tech earn high incomes, enjoy reliable infrastructure, and export high-value expertise".replace(",", " ")
    sol = (
        f"**(a) Tertiary Output:** $\\text{{R}}{gdp_bn} \\times {tert_pct}\\% = \\text{{R}}{tert_bn}\\text{{ billion}}$\n"
        f"**(b) High Living Standards:**\n"
        f"1. **Skilled Productivity & Wages:** Banking, software, healthcare and precision engineering pay higher skilled salaries.\n"
        f"2. **Quality Services & Infrastructure:** Strong tertiary healthcare, education, transport and stable power raise everyday living standards."
    )
    return make_question(
        rng=rng,
        subskill="28_tertiary_sector_dominance_developed_economies",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate Tertiary output R{tert_bn}bn", "marks": 2, "type": "A"},
            {"step": "Explain two causes of higher living standards", "marks": 3, "type": "A"},
        ],
        marking_guide="2 marks for GDP share; 3 marks for skilled wages + service quality.",
        hints={
            "tier_1": f"Multiply R{gdp_bn}bn by {tert_pct}%.",
            "tier_2": "Focus on skilled jobs, advanced education/healthcare and high-value output.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_developed_countries_abandon_food_and_manufactured_goods"],
    )


def _build_29_sa_gdp_sector_shares_calculation_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    sa_p = rng.choice([10, 11, 12])
    sa_s = rng.choice([21, 22, 23])
    sa_t = 100 - sa_p - sa_s
    tot_gdp = rng.choice([6000, 6500, 7000])
    sa_t_bn = round(tot_gdp * sa_t / 100.0)
    diagram = _svg_sector_gdp_comparison("Rural Region", 36, 20, 44, "South Africa (Model)", sa_p, sa_s, sa_t)
    prompt = (
        f"Study South Africa's modelled GDP split (`{sa_p}%` Primary, `{sa_s}%` Secondary, `{sa_t}%` Tertiary) on an annual GDP of R{tot_gdp:,}".replace(",", " ")
        + " billion.\n\n"
        f"(a) Calculate the Tertiary sector's Rand output (`{sa_t}%` of R{tot_gdp:,}".replace(",", " ") + "bn).\n"
        f"(b) Explain why South Africa is classified as a **developing / upper-middle-income** economy with an already large Tertiary sector."
    )
    ans = f"Tertiary output = R{sa_t_bn}bn; SA combines modern Tertiary finance/retail/tourism ({sa_t}%) with persistent reliance on Primary mineral/farm exports and high unemployment"
    sol = (
        f"**(a) Tertiary Output:** $\\text{{R}}{tot_gdp}\\text{{bn}} \\times {sa_t}\\% = \\text{{R}}{sa_t_bn}\\text{{ billion}}$\n"
        f"**(b) SA Profile:** Although finance, retail and transport give SA a large Tertiary share ({sa_t}%), South Africa still faces developing-economy challenges—raw mineral export dependence, unemployment and inequality."
    )
    return make_question(
        rng=rng,
        subskill="29_sa_gdp_sector_shares_calculation_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Tertiary output R{sa_t_bn}bn", "marks": 2, "type": "A"},
            {"step": "Explain SA dual modern-tertiary + developing challenges", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for GDP share; 2 marks for nuanced South African classification.",
        hints={
            "tier_1": f"Multiply total GDP R{tot_gdp}bn by {sa_t}%.",
            "tier_2": "Note SA's dual reality: advanced banks/retail alongside commodity dependence and inequality.",
            "tier_3": ans,
        },
        misconception_tags=["calls_south_africa_purely_primary_only_economy"],
        diagram_spec=diagram,
    )


def _build_30_standard_of_living_and_sector_transition(rng: random.Random, mode: str) -> Dict[str, Any]:
    w_prim = rng.choice([5200, 5800])
    w_sec = rng.choice([12500, 14000])
    w_tert = rng.choice([18500, 21000])
    gain_pct = round(((w_tert - w_prim) / w_prim) * 100, 1)
    prompt = (
        f"As a regional economy industrialises away from subsistence Primary work (average pay {fmt_zar(w_prim)}/mo) "
        f"into Secondary manufacturing ({fmt_zar(w_sec)}/mo) and skilled Tertiary services ({fmt_zar(w_tert)}/mo):\n\n"
        f"(a) Calculate the percentage increase in monthly pay when a worker moves from {fmt_zar(w_prim)} to {fmt_zar(w_tert)}.\n"
        f"(b) Explain how structural transition lifts a nation's **standard of living**."
    )
    ans = f"+{fmt_dec(gain_pct)}% pay gain; higher earnings expand household spending on housing, education, healthcare and nutrition while funding stronger tax-backed services"
    sol = (
        f"**(a) Wage Uplift:** $\\frac{{{w_tert - w_prim}}}{{{w_prim}}} \\times 100 = {fmt_dec(gain_pct)}\\%$\n"
        f"**(b) Standard of Living:** Shifting into higher-value Secondary and Tertiary jobs raises disposable income for clean housing, healthcare and schooling while generating higher taxes for public infrastructure."
    )
    return make_question(
        rng=rng,
        subskill="30_standard_of_living_and_sector_transition",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate +{fmt_dec(gain_pct)}% wage gain", "marks": 2, "type": "A"},
            {"step": "Explain living-standard improvements via higher earnings & services", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage calculation; 2 marks for living-standard impact.",
        hints={
            "tier_1": "Divide (Tertiary wage - Primary wage) by Primary wage * 100.",
            "tier_2": "Connect higher incomes directly to housing, schooling, clinics and tax capacity.",
            "tier_3": ans,
        },
        misconception_tags=["divides_increase_by_higher_tertiary_wage"],
    )


def _build_31_unskilled_labour_definition_examples(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("hand-picking ripe oranges in an orchard, sweeping factory floors, and packing retail shelves", "labour requiring little or no formal qualifications or specialised prior training, performing mainly manual tasks"),
        ("digging trenches with picks, carrying brick hods on a building site, and washing dishes", "basic physical work learnt quickly on the job without accredited technical or university credentials"),
        ("manual weeding on farms, stacking warehouse boxes, and street sweeping", "elementary tasks not requiring formal vocational certification or advanced technical skill"),
    ]
    ex, desc = rng.choice(cases)
    distractors = [
        "roles requiring a four-year engineering degree and professional registration",
        "certified CNC machine programmers who completed multi-year trade apprenticeships",
        "licenced medical surgeons performing cardiac operations",
    ]
    prompt = f"Workers performing *{ex}* are classified as **unskilled labour**, meaning:"
    sol = f"- **Unskilled Labour:** {desc.capitalize()}.\n- Unskilled jobs exist across Primary, Secondary and Tertiary sectors and typically earn lower wages."
    return make_question(
        rng=rng,
        subskill="31_unskilled_labour_definition_examples",
        question_type="mcq",
        prompt=prompt,
        correct_answer=desc.capitalize(),
        sample_answer=desc.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify accurate unskilled labour definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for manual tasks with minimal formal qualification.",
        hints={
            "tier_1": "Look at training duration and formal qualifications required.",
            "tier_2": "Unskilled roles need minimal prior training and focus on physical/routine duties.",
            "tier_3": desc.capitalize(),
        },
        misconception_tags=["equates_unskilled_with_lazy_rather_than_training_requirements"],
        options=[desc.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_32_semi_skilled_labour_definition_examples(rng: random.Random, mode: str) -> Dict[str, Any]:
    roles = [
        ("heavy-duty delivery truck drivers and supermarket till cashiers", "moderate practical/vocational training or licences to operate specific equipment safely"),
        ("industrial sewing-machine operators and mine drillers", "focused machine-operation training without needing a university degree"),
        ("forklift operators in warehouses and bank customer-service tellers", "specific procedural/equipment competencies gained through short courses or in-service training"),
    ]
    ex, desc = rng.choice(roles)
    base_hr = rng.choice([55, 65, 75])
    hrs = rng.choice([160, 180])
    monthly = base_hr * hrs
    prompt = (
        f"Workers such as {ex} belong to the **semi-skilled labour** tier.\n\n"
        f"(a) Explain what distinguishes **semi-skilled** labour from unskilled and skilled labour.\n"
        f"(b) Calculate monthly pay for {hrs} hours at {fmt_zar(base_hr)}/hour."
    )
    ans = f"Requires {desc} (more than unskilled manual labour, less than tertiary-degree/master-artisan skilled work); Monthly pay = {fmt_zar(monthly)}"
    sol = (
        f"**(a) Semi-skilled Definition:** Requires **{desc}**—sitting between basic unskilled tasks and formally credentialed skilled professions.\n"
        f"**(b) Monthly Pay:** ${hrs} \\times {fmt_zar(base_hr)} = {fmt_zar(monthly)}$"
    )
    return make_question(
        rng=rng,
        subskill="32_semi_skilled_labour_definition_examples",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define moderate training/machinery operation tier", "marks": 2, "type": "A"},
            {"step": f"Calculate monthly pay {fmt_zar(monthly)}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for semi-skilled distinction; 2 marks for pay multiplication.",
        hints={
            "tier_1": "Think of licences, short machine courses or point-of-sale training.",
            "tier_2": f"Multiply {hrs} hours by {fmt_zar(base_hr)}.",
            "tier_3": ans,
        },
        misconception_tags=["calls_truck_drivers_or_machine_operators_unskilled"],
    )


def _build_33_skilled_labour_definition_examples(rng: random.Random, mode: str) -> Dict[str, Any]:
    prof = [
        ("mining geologist, structural civil engineer, and chartered accountant", 38000, 46000),
        ("agronomist, certified diesel-mechanic artisan, and pharmacist", 32000, 42000),
        ("industrial robotics programmer, marine biologist, and clinical doctor", 44000, 55000),
    ]
    roles, sal_lo, sal_hi = rng.choice(prof)
    mid_annual = ((sal_lo + sal_hi) / 2) * 12
    prompt = (
        f"Roles such as {roles} represent **skilled labour**.\n\n"
        f"(a) Identify two qualification/training traits defining **skilled labour**.\n"
        f"(b) If skilled salaries in a firm span {fmt_zar(sal_lo)} to {fmt_zar(sal_hi)}/month, calculate the annual pay at the midpoint salary."
    )
    ans = f"Requires advanced tertiary degree/diploma or accredited artisan apprenticeship plus high problem-solving/regulatory responsibility; Midpoint annual pay = {fmt_zar(mid_annual)}"
    sol = (
        f"**(a) Skilled Traits:**\n"
        f"1. Extensive formal education (university degree, technikon diploma, or formal Red Seal trade qualification).\n"
        f"2. Complex analytical, technical or supervisory decision-making.\n\n"
        f"**(b) Annual Midpoint Pay:** Midpoint $= {fmt_zar((sal_lo + sal_hi) / 2)}/\\text{{mo}} \\times 12 = {fmt_zar(mid_annual)}$"
    )
    return make_question(
        rng=rng,
        subskill="33_skilled_labour_definition_examples",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "State advanced qualifications + complex technical expertise", "marks": 2, "type": "A"},
            {"step": f"Calculate midpoint annual pay {fmt_zar(mid_annual)}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for skilled traits; 2 marks for midpoint * 12.",
        hints={
            "tier_1": "Average the two monthly bounds first, then multiply by 12.",
            "tier_2": "Skilled workers hold accredited degrees, diplomas or formal trade qualifications.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_to_multiply_monthly_midpoint_by_12"],
    )


def _build_34_classifying_careers_by_sector_and_skill(rng: random.Random, mode: str) -> Dict[str, Any]:
    bank = [
        ("Fruit Picker", "Primary", "Unskilled"),
        ("Mining Geologist", "Primary", "Skilled"),
        ("Sewing Machine Operator", "Secondary", "Semi-skilled"),
        ("Civil Structural Engineer", "Secondary", "Skilled"),
        ("Supermarket Shelf Cleaner", "Tertiary", "Unskilled"),
        ("Bank Branch Teller", "Tertiary", "Semi-skilled"),
        ("Hospital Cardiologist", "Tertiary", "Skilled"),
    ]
    picked = rng.sample(bank, 3)
    headers = ["Career Role", "Economic Sector", "Skill Level"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Career Role | Economic Sector | Skill Level |", "|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_cols = [1, 2] if r_idx != 2 else [2]
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx in req_cols
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Classify Sector (Primary/Secondary/Tertiary) and Skill (Unskilled/Semi-skilled/Skilled)."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="34_classifying_careers_by_sector_and_skill",
        question_type="table_completion",
        prompt="Classify each South African career by its Economic Sector and Labour Skill Level.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Career & Skill Classification:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each Sector or Skill entry.",
        hints={
            "tier_1": "First ask which sector uses the role, then judge how much training/qualification it needs.",
            "tier_2": "Picker/Cleaner = Unskilled; Operator/Teller = Semi-skilled; Geologist/Engineer/Doctor = Skilled.",
            "tier_3": md_table,
        },
        misconception_tags=["assumes_all_primary_jobs_are_unskilled"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "role", "label": headers[0]}, {"key": "sec", "label": headers[1]}, {"key": "sk", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_35_primary_sector_skill_mix_analysis(rng: random.Random, mode: str) -> Dict[str, Any]:
    tot_staff = rng.choice([200, 250, 300])
    unsk = round(tot_staff * 0.60)
    semi = round(tot_staff * 0.25)
    sk = tot_staff - unsk - semi
    pct_sk = round(sk * 100.0 / tot_staff, 1)
    prompt = (
        f"A commercial citrus estate employs {tot_staff} workers across three skill levels: "
        f"{unsk} fruit harvesters (unskilled), {semi} tractor/spray operators (semi-skilled), and {sk} agronomists & packhouse engineers (skilled).\n\n"
        f"(a) Calculate the percentage of the farm's workforce that is **skilled**.\n"
        f"(b) Explain why modern commercial agriculture still needs skilled specialists alongside manual harvesters."
    )
    ans = f"Skilled share = {fmt_dec(pct_sk)}%; agronomists and irrigation engineers boost yields, soil health and export quality compliance"
    sol = (
        f"**(a) Skilled Share:** $\\frac{{{sk}}}{{{tot_staff}}} \\times 100 = {fmt_dec(pct_sk)}\\%$\n"
        f"**(b) Specialist Value:** Skilled agronomists optimise soil/pest science and engineers maintain automated packhouses so SA fruit passes strict export standards."
    )
    return make_question(
        rng=rng,
        subskill="35_primary_sector_skill_mix_analysis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate {fmt_dec(pct_sk)}% skilled share", "marks": 2, "type": "A"},
            {"step": "Explain how skilled roles lift agricultural yields & export standards", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage; 2 marks for scientific/engineering justification.",
        hints={
            "tier_1": f"Divide {sk} skilled workers by {tot_staff} total employees times 100.",
            "tier_2": "Think of crop yields, irrigation efficiency and international export grading.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_farms_have_zero_skilled_roles"],
    )


def _build_36_secondary_sector_skill_mix_analysis(rng: random.Random, mode: str) -> Dict[str, Any]:
    n_unsk, w_unsk = rng.choice([(20, 5200), (25, 5400)])
    n_semi, w_semi = rng.choice([(30, 9500), (35, 10000)])
    n_sk, w_sk = rng.choice([(8, 28000), (10, 30000)])
    payroll = n_unsk * w_unsk + n_semi * w_semi + n_sk * w_sk
    prompt = (
        f"A Gauteng furniture factory employs:\n"
        f"- {n_unsk} unskilled loaders at {fmt_zar(w_unsk)}/mo\n"
        f"- {n_semi} semi-skilled lathe/varnish operators at {fmt_zar(w_semi)}/mo\n"
        f"- {n_sk} skilled cabinetmakers & industrial engineers at {fmt_zar(w_sk)}/mo\n\n"
        f"(a) Calculate the factory's total monthly payroll.\n"
        f"(b) Identify why Secondary manufacturing requires a larger semi-skilled share than basic primary harvesting."
    )
    ans = f"Total payroll = {fmt_zar(payroll)}; factory assembly lines rely on trained machine operators following safety and precision specs"
    sol = (
        f"**(a) Monthly Payroll:**\n"
        f"- Unskilled: ${n_unsk} \\times {fmt_zar(w_unsk)} = {fmt_zar(n_unsk * w_unsk)}$\n"
        f"- Semi-skilled: ${n_semi} \\times {fmt_zar(w_semi)} = {fmt_zar(n_semi * w_semi)}$\n"
        f"- Skilled: ${n_sk} \\times {fmt_zar(w_sk)} = {fmt_zar(n_sk * w_sk)}$\n"
        f"- **Total:** {fmt_zar(payroll)}\n\n"
        f"**(b) Factory Skill Demand:** Operating power saws, welding jigs and assembly presses safely requires formal machine training (semi-skilled)."
    )
    return make_question(
        rng=rng,
        subskill="36_secondary_sector_skill_mix_analysis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": "Compute all three tier subtotals", "marks": 2, "type": "A"},
            {"step": f"Sum total payroll {fmt_zar(payroll)}", "marks": 1, "type": "CA"},
            {"step": "Explain machine-operation training need in factories", "marks": 2, "type": "A"},
        ],
        marking_guide="3 marks for payroll math; 2 marks for machine-skill reasoning.",
        hints={
            "tier_1": "Multiply headcount by monthly wage for each tier and sum all three.",
            "tier_2": "Factory lines need trained machine operators rather than raw manual digging/picking.",
            "tier_3": ans,
        },
        misconception_tags=["sums_wage_rates_without_multiplying_by_headcounts"],
    )


def _build_37_tertiary_sector_skill_mix_analysis(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("a Sandton hospital network", "ward cleaners & porters (unskilled)", "ambulance drivers & billing clerks (semi-skilled)", "specialist surgeons & pharmacists (skilled)"),
        ("a national supermarket group", "trolley collectors & cleaners (unskilled)", "checkout cashiers & stock drivers (semi-skilled)", "supply-chain analysts & chartered accountants (skilled)"),
        ("a coastal hotel resort", "groundskeepers & dishwashers (unskilled)", "housekeeping supervisors & front-desk receptionists (semi-skilled)", "executive chefs & hospitality finance managers (skilled)"),
    ]
    org, u, s, k = rng.choice(cases)
    prompt = (
        f"Even though the Tertiary sector includes highly paid professionals, large employers like **{org}** require all three skill tiers.\n\n"
        f"Describe one specific duty for **{u}**, **{s}**, and **{k}** showing how they collaborate."
    )
    ans = f"Unskilled: {u}; Semi-skilled: {s}; Skilled: {k}—together keeping operations hygienic, responsive and professionally managed"
    sol = (
        f"- **Unskilled ({u}):** Maintains daily facility cleanliness and basic logistics.\n"
        f"- **Semi-skilled ({s}):** Executes customer-facing procedures and specialised equipment operation.\n"
        f"- **Skilled ({k}):** Provides regulated professional expertise, financial control and strategic management."
    )
    return make_question(
        rng=rng,
        subskill="37_tertiary_sector_skill_mix_analysis",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[{"step": "Describe integrated duties across Unskilled, Semi-skilled, Skilled (1 mark each)", "marks": 3, "type": "A"}],
        marking_guide="1 mark for each skill tier's duty and collaboration.",
        hints={
            "tier_1": "Cover cleaning/handling, trained operational roles, and degreed specialists.",
            "tier_2": "Show how the three roles depend on each other to serve clients.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_tertiary_sector_employs_only_university_graduates"],
    )


def _build_38_wage_disparities_across_skill_levels_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    u_w = rng.choice([4800, 5200, 5600])
    s_w = rng.choice([10400, 11200, 12000])
    k_w = rng.choice([28800, 31200, 33600])
    ratio = round(k_w / u_w, 1)
    diagram = _svg_wage_skill_bars("Mining & Engineering Workforce", u_w, s_w, k_w)
    prompt = (
        f"Study the monthly wage comparison across skill levels (`Unskilled {fmt_zar(u_w)}`, `Semi-skilled {fmt_zar(s_w)}`, `Skilled {fmt_zar(k_w)}`).\n\n"
        f"(a) Calculate how many times larger the **Skilled** monthly wage is compared with the **Unskilled** wage (to 1 decimal place).\n"
        f"(b) Give ONE economic reason explaining why skilled salaries are much higher."
    )
    ans = f"Skilled wage is {fmt_dec(ratio)} times unskilled wage; reflects higher productivity, long training investment and scarcity of qualified specialists"
    sol = (
        f"**(a) Wage Ratio:** $\\frac{{{k_w}}}{{{u_w}}} = {fmt_dec(ratio)}$ times higher.\n"
        f"**(b) Economic Cause:** Skilled workers bring years of costly education/training, produce higher output value per hour, and remain relatively scarcer than unskilled job seekers."
    )
    return make_question(
        rng=rng,
        subskill="38_wage_disparities_across_skill_levels_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate ratio {fmt_dec(ratio)}x", "marks": 2, "type": "A"},
            {"step": "Explain scarcity + training investment + higher productivity", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for ratio; 2 marks for scarcity/productivity reason.",
        hints={
            "tier_1": f"Divide Skilled wage {fmt_zar(k_w)} by Unskilled wage {fmt_zar(u_w)}.",
            "tier_2": "Recall scarcity of skills and years spent training.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_wages_instead_of_dividing_when_asked_for_multiple"],
        diagram_spec=diagram,
    )


def _build_39_training_and_skills_upskilling_benefits(rng: random.Random, mode: str) -> Dict[str, Any]:
    n_workers = rng.choice([25, 30, 40])
    old_w = rng.choice([5500, 6000])
    new_w = rng.choice([10500, 11500])
    extra_per_worker = new_w - old_w
    tot_boost = n_workers * extra_per_worker
    prompt = (
        f"Through a TVET welding and CNC apprenticeship, {n_workers} unskilled factory hands (earning {fmt_zar(old_w)}/mo) "
        f"upskill into semi-skilled machinists earning {fmt_zar(new_w)}/mo.\n\n"
        f"(a) Calculate the total additional monthly wage income gained across all {n_workers} households.\n"
        f"(b) Explain ONE benefit to the factory and ONE benefit to South Africa's broader economy."
    )
    ans = f"Monthly household income gain = {fmt_zar(tot_boost)}; Factory: higher product precision & output; Economy: lower structural unemployment, higher taxes & retail spending"
    sol = (
        f"**(a) Collective Household Gain:** ${n_workers} \\times ({fmt_zar(new_w)} - {fmt_zar(old_w)}) = {fmt_zar(tot_boost)}$ per month.\n"
        f"**(b) Benefits:**\n"
        f"- **Factory:** Higher machine productivity, fewer defective units, and stronger competitiveness.\n"
        f"- **Economy:** Stronger consumer purchasing power, expanded PAYE/VAT receipts and reduced reliance on social grants."
    )
    return make_question(
        rng=rng,
        subskill="39_training_and_skills_upskilling_benefits",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate collective gain {fmt_zar(tot_boost)}", "marks": 2, "type": "A"},
            {"step": "State one firm benefit and one macro benefit", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for wage gain; 2 marks for balanced micro/macro benefits.",
        hints={
            "tier_1": "Find wage rise per worker, then multiply by number of upskilled workers.",
            "tier_2": "Consider productivity for the factory and spending/taxes for the economy.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_benefit_to_employer_productivity"],
    )


def _build_40_beneficiation_moving_primary_to_secondary(rng: random.Random, mode: str) -> Dict[str, Any]:
    tonnes = rng.choice([50, 80, 100])
    raw_p = rng.choice([1800, 2200])
    proc_p = rng.choice([6800, 7400])
    extra = tonnes * (proc_p - raw_p)
    prompt = (
        f"**Mineral beneficiation** means processing South Africa's raw **Primary** ores domestically in **Secondary** smelters/factories "
        f"instead of exporting raw rock. Suppose {tonnes} tonnes of raw chrome ore sell at {fmt_zar(raw_p)}/t, whereas refined stainless-steel alloy sells at {fmt_zar(proc_p)}/t.\n\n"
        f"(a) Calculate the extra export earnings earned by refining all {tonnes} tonnes inside South Africa.\n"
        f"(b) Explain how beneficiation upgrades South Africa's sectoral job structure."
    )
    ans = f"Extra earnings = {fmt_zar(extra)}; expands Secondary manufacturing plants, creating semi-skilled and skilled engineering/artisan jobs"
    sol = (
        f"**(a) Extra Export Earnings:** ${tonnes} \\times ({fmt_zar(proc_p)} - {fmt_zar(raw_p)}) = {fmt_zar(extra)}$\n"
        f"**(b) Structural Upgrade:** Beneficiation builds domestic Secondary manufacturing capacity, creating higher-paid semi-skilled and skilled jobs rather than exporting raw jobs abroad."
    )
    return make_question(
        rng=rng,
        subskill="40_beneficiation_moving_primary_to_secondary",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate extra revenue {fmt_zar(extra)}", "marks": 2, "type": "A"},
            {"step": "Explain Secondary expansion & higher-skill job creation", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for arithmetic; 2 marks for structural jobs explanation.",
        hints={
            "tier_1": "Multiply (processed price - raw price) by tonnes.",
            "tier_2": "Notice moving from Primary -> Secondary adds skilled factory jobs and tax base.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_beneficiation_means_stopping_mining_completely"],
    )


def _build_41_formal_vs_informal_jobs_across_sectors(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("smallholder vegetable growers selling surpluses informally (Primary), backyard steel-gate welders (Secondary), and township spaza shops/minibus taxis (Tertiary)", "informal employment operates across all three sectors—agriculture, small-scale making/repair, and street/retail services"),
        ("subsistence fishers along coastal villages (Primary), home-based seamstresses (Secondary), and informal pavement hair braiders (Tertiary)", "every economic sector contains both registered formal companies and survivalist/informal micro-enterprises"),
    ]
    examples, core = rng.choice(cases)
    distractors = [
        "Informal sector businesses exist strictly inside the Tertiary sector and never grow crops or weld goods.",
        "Informal workers only produce goods for export airlines.",
        "South Africa forbids informal workers from selling food or haircuts.",
    ]
    prompt = f"What does the presence of *{examples}* prove about South Africa's economic sectors?"
    sol = f"- **Key Insight:** {core.capitalize()}."
    return make_question(
        rng=rng,
        subskill="41_formal_vs_informal_jobs_across_sectors",
        question_type="mcq",
        prompt=prompt,
        correct_answer=core.capitalize(),
        sample_answer=core.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Recognise informal activity spans Primary, Secondary & Tertiary", "marks": 2, "type": "A"}],
        marking_guide="2 marks for cross-sector informal insight.",
        hints={
            "tier_1": "Look at whether farming, welding and spaza shops each sit in different sectors.",
            "tier_2": "Informal work is NOT restricted only to street vending.",
            "tier_3": core.capitalize(),
        },
        misconception_tags=["restricts_informal_economy_to_tertiary_retail_only"],
        options=[core.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_42_quarternary_knowledge_and_ict_in_tertiary(rng: random.Random, mode: str) -> Dict[str, Any]:
    old_hrs = rng.choice([20, 24, 30])
    cut_pct = rng.choice([40, 50])
    new_hrs = round(old_hrs * (1 - cut_pct / 100.0), 1)
    prompt = (
        f"Modern **Tertiary** knowledge & ICT tools (cloud logistics, mobile banking, precision soil apps) streamline operations across sectors. "
        f"Automated digital customs clearance cuts a Cape fruit exporter's port-paperwork wait from {old_hrs} hours by **{cut_pct}%**.\n\n"
        f"(a) Calculate the new processing time in hours.\n"
        f"(b) Explain how fast Tertiary ICT services reduce spoilage for Primary fruit growers and Secondary canneries."
    )
    ans = f"New wait = {fmt_dec(new_hrs)} hours; faster port clearance preserves fresh produce shelf-life and speeds factory input delivery"
    sol = (
        f"**(a) Time Saving:** ${old_hrs} \\times (1 - 0.{cut_pct}) = {fmt_dec(new_hrs)}$ hours.\n"
        f"**(b) Cross-Sector ICT Impact:** Digital clearance cuts refrigerated delays, protecting Primary perishable fruit exports and ensuring Secondary plants receive inputs on schedule."
    )
    return make_question(
        rng=rng,
        subskill="42_quarternary_knowledge_and_ict_in_tertiary",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate {fmt_dec(new_hrs)} hours", "marks": 2, "type": "A"},
            {"step": "Explain shelf-life / faster supply-chain benefit", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for hours calculation; 2 marks for cross-sector efficiency.",
        hints={
            "tier_1": f"Reduce {old_hrs} hours by {cut_pct}%.",
            "tier_2": "Think of perishable agricultural exports waiting at harbours.",
            "tier_3": ans,
        },
        misconception_tags=["calculates_hours_saved_without_giving_new_time"],
    )


def _build_43_rural_vs_urban_sector_employment_patterns(rng: random.Random, mode: str) -> Dict[str, Any]:
    r_prim = rng.choice([48, 52, 56])
    u_tert = rng.choice([70, 74, 78])
    prompt = (
        f"Compare two South African municipalities:\n"
        f"- **Rural District R:** {r_prim}% of jobs lie in **Primary** agriculture and forestry.\n"
        f"- **Metro City U:** {u_tert}% of jobs lie in **Tertiary** finance, retail, healthcare and transport, alongside Secondary industrial parks.\n\n"
        f"Explain TWO economic reasons why Rural District R concentrates in Primary jobs whereas Metro City U concentrates in Tertiary & Secondary jobs."
    )
    ans = f"Rural R has vast farmland, forests and mineral deposits; Metro U has dense consumer markets, ports/transport hubs, banks and universities supporting Tertiary & Secondary firms"
    sol = (
        f"1. **Natural Endowment (Rural):** Rural districts hold fertile land, plantations and mines suited directly to Primary extraction.\n"
        f"2. **Agglomeration & Infrastructure (Urban):** Metropolitan cities offer dense consumer bases, office towers, fibre networks, industrial zones and skilled graduates suited to Tertiary services and Secondary factories."
    )
    return make_question(
        rng=rng,
        subskill="43_rural_vs_urban_sector_employment_patterns",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain rural natural-resource endowment", "marks": 2, "type": "A"},
            {"step": "Explain urban consumer market, infrastructure & skill density", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for rural Primary driver; 2 marks for urban Secondary/Tertiary drivers.",
        hints={
            "tier_1": "Contrast land/climate/minerals in rural districts against city population & infrastructure.",
            "tier_2": "Services and factories cluster near customers, roads and universities.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_urban_cities_produce_most_primary_crops"],
    )


def _build_44_foreign_exchange_earnings_by_sector(rng: random.Random, mode: str) -> Dict[str, Any]:
    prim_x = rng.choice([620, 680, 720])
    sec_x = rng.choice([410, 450, 490])
    tert_x = rng.choice([170, 210, 240])
    tot_x = prim_x + sec_x + tert_x
    prim_pct = round(prim_x * 100.0 / tot_x, 1)
    prompt = (
        f"In a sample year, South African export earnings break down across sectors as:\n"
        f"- Primary (platinum, gold, iron ore, fruit): R{prim_x} billion\n"
        f"- Secondary (assembled vehicles, machinery, processed foods): R{sec_x} billion\n"
        f"- Tertiary (international tourism, engineering & IT services): R{tert_x} billion\n\n"
        f"(a) Calculate total export earnings across all three sectors.\n"
        f"(b) Calculate the Primary sector's percentage share of total exports (to 1 decimal place)."
    )
    ans = f"Total exports = R{tot_x} billion; Primary share = {fmt_dec(prim_pct)}%"
    sol = (
        f"**(a) Total Exports:** $\\text{{R}}{prim_x} + \\text{{R}}{sec_x} + \\text{{R}}{tert_x} = \\text{{R}}{tot_x}\\text{{ billion}}$\n"
        f"**(b) Primary Share:** $\\frac{{{prim_x}}}{{{tot_x}}} \\times 100 = {fmt_dec(prim_pct)}\\%$"
    )
    return make_question(
        rng=rng,
        subskill="44_foreign_exchange_earnings_by_sector",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Sum total R{tot_x}bn", "marks": 2, "type": "A"},
            {"step": f"Calculate Primary share {fmt_dec(prim_pct)}%", "marks": 2, "type": "CA"},
        ],
        marking_guide="2 marks for sum; 2 marks for percentage share.",
        hints={
            "tier_1": "Add all three sectors for total exports.",
            "tier_2": f"Divide R{prim_x}bn by total and multiply by 100.",
            "tier_3": ans,
        },
        misconception_tags=["omits_tourism_services_from_tertiary_exports"],
    )


def _build_45_port_rail_bottleneck_primary_secondary_loss(rng: random.Random, mode: str) -> Dict[str, Any]:
    trains_missed = rng.choice([12, 15, 18])
    tonnes_per_train = rng.choice([4000, 5000])
    price_t = rng.choice([1400, 1600])
    lost_val = trains_missed * tonnes_per_train * price_t
    prompt = (
        f"Due to **Tertiary freight-rail bottlenecks**, {trains_missed} bulk ore trains (carrying {tonnes_per_train:,}".replace(",", " ")
        + f" tonnes each of export coal valued at {fmt_zar(price_t)}/tonne) fail to reach Richards Bay terminal.\n\n"
        f"(a) Calculate the delayed/lost export value in Rand.\n"
        f"(b) Explain how Tertiary transport bottlenecks constrain both Primary mining output and Secondary port-side suppliers."
    )
    ans = f"Delayed export value = {fmt_zar(lost_val)}; mines stockpile/cut shifts when trains stall, while Secondary equipment suppliers lose maintenance orders"
    sol = (
        f"**(a) Delayed Export Value:**\n"
        f"${trains_missed} \\times {tonnes_per_train} \\times {fmt_zar(price_t)} = {fmt_zar(lost_val)}$\n\n"
        f"**(b) Bottleneck Ripple:** Even when Primary mines extract ore efficiently, unreliable Tertiary rail prevents sales, forcing output caps and cutting orders from Secondary engineering firms."
    )
    return make_question(
        rng=rng,
        subskill="45_port_rail_bottleneck_primary_secondary_loss",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate delayed value {fmt_zar(lost_val)}", "marks": 2, "type": "A"},
            {"step": "Explain Tertiary bottleneck effect on Primary + Secondary", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for multiplication; 2 marks for cross-sector constraint.",
        hints={
            "tier_1": "Multiply trains missed * tonnes per train * Rand per tonne.",
            "tier_2": "Notice Tertiary freight connects extraction and manufacturing to buyers.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_one_of_the_three_factors_in_multiplication"],
    )


def _build_46_constructing_sector_gdp_summary_table(rng: random.Random, mode: str) -> Dict[str, Any]:
    tot = rng.choice([1000, 2000])
    p_pct = rng.choice([10, 12, 15])
    s_pct = rng.choice([20, 25])
    t_pct = 100 - p_pct - s_pct
    p_val = int(tot * p_pct / 100)
    s_val = int(tot * s_pct / 100)
    t_val = tot - p_val - s_val
    rows = [
        ("Primary", str(p_val), f"{p_pct}%"),
        ("Secondary", str(s_val), f"{s_pct}%"),
        ("Tertiary", str(t_val), f"{t_pct}%"),
    ]
    headers = ["Economic Sector", f"GDP Output (R bn, Total R{tot}bn)", "% Share of GDP"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [f"| Economic Sector | GDP Output (R bn, Total R{tot}bn) | % Share of GDP |", "|---|---|---|"]
    req_coords = [(0, 2), (1, 1), (2, 1), (2, 2)]
    for r_idx, vals in enumerate(rows, start=1):
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = (r_idx - 1, c_idx) in req_coords
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = f"Use Total GDP = R{tot}bn and remember all 3 sector shares sum to 100%."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="46_constructing_sector_gdp_summary_table",
        question_type="table_completion",
        prompt=f"Complete the missing Output (`R bn`) and `% Share` cells in the Sector GDP Summary Table (Total National GDP = **R{tot} billion**).",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Sector GDP Table (Total R{tot}bn):**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per calculated output or % share cell.",
        hints={
            "tier_1": "Convert % to R bn using (pct / 100) * Total GDP, and find Tertiary % by subtracting from 100%.",
            "tier_2": f"Check that Primary + Secondary + Tertiary sums to R{tot}bn and 100%.",
            "tier_3": md_table,
        },
        misconception_tags=["forgets_percentages_must_sum_to_100"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "sec", "label": headers[0]}, {"key": "gdp", "label": headers[1]}, {"key": "pct", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_47_comparing_employment_share_vs_gdp_share(rng: random.Random, mode: str) -> Dict[str, Any]:
    ag_gdp, ag_jobs = rng.choice([(120, 800000), (150, 900000)])
    fin_gdp, fin_jobs = rng.choice([(900, 600000), (960, 600000)])
    ag_per = round((ag_gdp * 1e9) / ag_jobs)
    fin_per = round((fin_gdp * 1e9) / fin_jobs)
    prompt = (
        f"In a national economy:\n"
        f"- **Agriculture (Primary)** produces R{ag_gdp} billion in output using {ag_jobs:,}".replace(",", " ") + " workers.\n"
        f"- **Finance & Business Services (Tertiary)** produces R{fin_gdp} billion using {fin_jobs:,}".replace(",", " ") + " workers.\n\n"
        f"(a) Calculate average annual GDP output per worker in each sector.\n"
        f"(b) Explain why Tertiary finance generates higher output per worker despite employing fewer people."
    )
    ans = f"Agriculture = {fmt_zar(ag_per)}/worker; Finance = {fmt_zar(fin_per)}/worker; relies heavily on high-skill professionals, software and high-value capital"
    sol = (
        f"**(a) Output per Worker:**\n"
        f"- Agriculture $= \\frac{{\\text{{R}}{ag_gdp}\\text{{bn}}}}{{{ag_jobs}}} = {fmt_zar(ag_per)}$ per worker/year\n"
        f"- Finance $= \\frac{{\\text{{R}}{fin_gdp}\\text{{bn}}}}{{{fin_jobs}}} = {fmt_zar(fin_per)}$ per worker/year\n\n"
        f"**(b) Productivity Gap:** Tertiary finance combines scarce skilled specialists and digital capital, generating far more value per worker than labour-intensive Primary farming."
    )
    return make_question(
        rng=rng,
        subskill="47_comparing_employment_share_vs_gdp_share",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Agriculture {fmt_zar(ag_per)} and Finance {fmt_zar(fin_per)}", "marks": 2, "type": "A"},
            {"step": "Explain capital + skill intensity driving higher output per worker", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for per-worker output divisions; 2 marks for productivity rationale.",
        hints={
            "tier_1": "Convert R billions into Rand (multiply by 1 000 000 000) before dividing by workers.",
            "tier_2": "Compare labour-intensive farming against skill/technology-intensive finance.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_billion_zeros_in_division"],
    )


def _build_48_green_economy_sustainable_secondary_tertiary(rng: random.Random, mode: str) -> Dict[str, Any]:
    recycled_t = rng.choice([300, 450, 600])
    co2_saved_per_t = rng.choice([1.5, 2.0])
    tot_saved = round(recycled_t * co2_saved_per_t, 1)
    prompt = (
        f"Supporting sustainable resource management, a Secondary paper mill uses {recycled_t} tonnes of recovered office cardboard "
        f"(collected by Tertiary waste-recycling co-ops) instead of virgin Primary wood pulp, cutting carbon emissions by **{fmt_dec(co2_saved_per_t)} tonnes per tonne**.\n\n"
        f"(a) Calculate total carbon emissions avoided in tonnes.\n"
        f"(b) Explain how recycling connects Tertiary collection, Secondary processing, and Primary forest conservation."
    )
    ans = f"Emissions avoided = {fmt_dec(tot_saved)} tonnes; Tertiary recyclers recover used paper for Secondary mills, sparing Primary timber plantations"
    sol = (
        f"**(a) Emissions Avoided:** ${recycled_t} \\times {fmt_dec(co2_saved_per_t)} = {fmt_dec(tot_saved)}$ tonnes.\n"
        f"**(b) Circular Sector Link:** Tertiary waste pickers and logistics firms supply Secondary mills with recovered pulp, lowering tree-felling pressure on Primary forests."
    )
    return make_question(
        rng=rng,
        subskill="48_green_economy_sustainable_secondary_tertiary",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate {fmt_dec(tot_saved)} tonnes saved", "marks": 2, "type": "A"},
            {"step": "Link Tertiary collection -> Secondary mill -> Primary conservation", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for calculation; 2 marks for 3-sector green link.",
        hints={
            "tier_1": f"Multiply {recycled_t} tonnes by {fmt_dec(co2_saved_per_t)}.",
            "tier_2": "Trace waste paper from Tertiary collector -> Secondary recycler -> saved Primary trees.",
            "tier_3": ans,
        },
        misconception_tags=["misses_how_recycling_spares_primary_timber_extraction"],
    )


def _build_49_diagnosing_sector_and_skill_misconceptions(rng: random.Random, mode: str) -> Dict[str, Any]:
    errors = [
        ("A learner claims: 'Because a truck driver delivers raw coal from Mpumalanga mines, the truck driver works in the Primary sector.'", "Driving a haulage truck provides a transport service in the Tertiary sector, even when the freight itself is a Primary mineral."),
        ("A learner claims: 'Flour millers and house builders are in the Primary sector because bread and bricks come from wheat and clay.'", "Milling flour and constructing houses transform raw materials into processed/finished outputs, placing them in the Secondary sector."),
        ("A learner claims: 'Developed nations have tiny Primary sectors because they never eat food or use metals.'", "Developed nations still consume food and minerals (via efficient mechanised farms and imports), but high-value Tertiary services and advanced Secondary industries make up a far larger share of total GDP."),
    ]
    claim, correction = rng.choice(errors)
    prompt = f"Identify and correct the economic misconception in this student statement:\n*{claim}*"
    sol = f"**Correction:**\n- {correction}"
    return make_question(
        rng=rng,
        subskill="49_diagnosing_sector_and_skill_misconceptions",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=correction,
        sample_answer=correction,
        worked_solution=sol,
        marks=3,
        marking_schema=[{"step": "Correct sector/development misconception accurately", "marks": 3, "type": "A"}],
        marking_guide="3 marks for exact diagnostic correction.",
        hints={
            "tier_1": "Separate the cargo/material handled from the actual economic activity performed.",
            "tier_2": "Focus on transport = Tertiary, processing/construction = Secondary, GDP shares vs total food intake.",
            "tier_3": correction,
        },
        misconception_tags=["repeats_cargo_activity_confusion"],
    )


def _build_50_comprehensive_sectors_gdp_and_value_chain_synthesis(rng: random.Random, mode: str) -> Dict[str, Any]:
    milk_l = rng.choice([50000, 60000, 80000])
    p_farm = rng.choice([6.0, 6.5])
    p_dairy = rng.choice([13.0, 14.0])
    p_retail = rng.choice([18.0, 19.5])
    va_sec = round((p_dairy - p_farm) * milk_l)
    va_tert = round((p_retail - p_dairy) * milk_l)
    prompt = (
        f"A Midlands dairy value chain processes **{milk_l:,}".replace(",", " ") + " litres** of milk monthly:\n"
        f"- **Stage 1 (Dairy Farm):** sells raw milk to processor at {fmt_zar(p_farm)}/L.\n"
        f"- **Stage 2 (Pasteurising & Cheese Plant):** sells packaged dairy output at {fmt_zar(p_dairy)}/L.\n"
        f"- **Stage 3 (Supermarket & Cold Freight):** retails to households at {fmt_zar(p_retail)}/L.\n\n"
        f"(a) Classify Stages 1, 2, and 3 into Primary, Secondary, and Tertiary.\n"
        f"(b) Calculate the total monthly Rand **value added** by Stage 2 and by Stage 3 across all {milk_l:,}".replace(",", " ") + " litres.\n"
        f"(c) Name ONE skilled career required across this dairy chain and explain how load-shedding threatens all three stages simultaneously."
    )
    ans = (
        f"S1=Primary, S2=Secondary, S3=Tertiary; Secondary VA={fmt_zar(va_sec)}, Tertiary VA={fmt_zar(va_tert)}; "
        f"Skilled role: veterinarian/food-technologist/accountant; Load-shedding spoils chilled milk on farms, halts pasteurisers, and spoils supermarket fridges"
    )
    sol = (
        f"**(a) Classification:** Stage 1 = **Primary** (dairy farming); Stage 2 = **Secondary** (pasteurising/packaging); Stage 3 = **Tertiary** (freight & retail).\n"
        f"**(b) Monthly Value Added:**\n"
        f"- **Secondary:** ${milk_l} \\times ({fmt_zar(p_dairy)} - {fmt_zar(p_farm)}) = {fmt_zar(va_sec)}$\n"
        f"- **Tertiary:** ${milk_l} \\times ({fmt_zar(p_retail)} - {fmt_zar(p_dairy)}) = {fmt_zar(va_tert)}$\n\n"
        f"**(c) Skilled Role & Cold-Chain Vulnerability:** Skilled roles include **veterinary surgeons, food-safety scientists or chartered accountants**. Load-shedding breaks cold storage simultaneously at farm milking parlours, factory pasteurisers, and retail chillers."
    )
    return make_question(
        rng=rng,
        subskill="50_comprehensive_sectors_gdp_and_value_chain_synthesis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=8,
        marking_schema=[
            {"step": "Classify Stages 1, 2, 3 accurately", "marks": 2, "type": "A"},
            {"step": f"Calculate Secondary VA {fmt_zar(va_sec)} and Tertiary VA {fmt_zar(va_tert)}", "marks": 3, "type": "A"},
            {"step": "Skilled career + cold-chain load-shedding disruption across all 3 stages", "marks": 3, "type": "A"},
        ],
        marking_guide="2 marks for classifications; 3 marks for value-added math; 3 marks for skilled career + cold-chain synthesis.",
        hints={
            "tier_1": "Multiply litres by per-litre price step at Stage 2 and Stage 3.",
            "tier_2": "Dairy relies on unbroken refrigeration across farm, factory and supermarket.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_cold_chain_interdependence_under_power_outages"],
        duration_mins=7,
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_developing_vs_developed_gdp_bar_chart_svg": _build_26_developing_vs_developed_gdp_bar_chart_svg,
    "27_primary_sector_dominance_developing_economies": _build_27_primary_sector_dominance_developing_economies,
    "28_tertiary_sector_dominance_developed_economies": _build_28_tertiary_sector_dominance_developed_economies,
    "29_sa_gdp_sector_shares_calculation_svg": _build_29_sa_gdp_sector_shares_calculation_svg,
    "30_standard_of_living_and_sector_transition": _build_30_standard_of_living_and_sector_transition,
    "31_unskilled_labour_definition_examples": _build_31_unskilled_labour_definition_examples,
    "32_semi_skilled_labour_definition_examples": _build_32_semi_skilled_labour_definition_examples,
    "33_skilled_labour_definition_examples": _build_33_skilled_labour_definition_examples,
    "34_classifying_careers_by_sector_and_skill": _build_34_classifying_careers_by_sector_and_skill,
    "35_primary_sector_skill_mix_analysis": _build_35_primary_sector_skill_mix_analysis,
    "36_secondary_sector_skill_mix_analysis": _build_36_secondary_sector_skill_mix_analysis,
    "37_tertiary_sector_skill_mix_analysis": _build_37_tertiary_sector_skill_mix_analysis,
    "38_wage_disparities_across_skill_levels_svg": _build_38_wage_disparities_across_skill_levels_svg,
    "39_training_and_skills_upskilling_benefits": _build_39_training_and_skills_upskilling_benefits,
    "40_beneficiation_moving_primary_to_secondary": _build_40_beneficiation_moving_primary_to_secondary,
    "41_formal_vs_informal_jobs_across_sectors": _build_41_formal_vs_informal_jobs_across_sectors,
    "42_quarternary_knowledge_and_ict_in_tertiary": _build_42_quarternary_knowledge_and_ict_in_tertiary,
    "43_rural_vs_urban_sector_employment_patterns": _build_43_rural_vs_urban_sector_employment_patterns,
    "44_foreign_exchange_earnings_by_sector": _build_44_foreign_exchange_earnings_by_sector,
    "45_port_rail_bottleneck_primary_secondary_loss": _build_45_port_rail_bottleneck_primary_secondary_loss,
    "46_constructing_sector_gdp_summary_table": _build_46_constructing_sector_gdp_summary_table,
    "47_comparing_employment_share_vs_gdp_share": _build_47_comparing_employment_share_vs_gdp_share,
    "48_green_economy_sustainable_secondary_tertiary": _build_48_green_economy_sustainable_secondary_tertiary,
    "49_diagnosing_sector_and_skill_misconceptions": _build_49_diagnosing_sector_and_skill_misconceptions,
    "50_comprehensive_sectors_gdp_and_value_chain_synthesis": _build_50_comprehensive_sectors_gdp_and_value_chain_synthesis,
}
