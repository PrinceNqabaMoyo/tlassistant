"""Grade 9 EMS Term 1: Economic Systems — Semantic Archetypes 01 to 25."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional


TOPIC_NAME = "Economic systems"
SUBTOPIC_ID = "term1_economy"


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
    """Assemble standardized 6-pillar Grade 9 EMS question payload."""
    qid = f"gr9_ems_t1_econ_{subskill}_{rng.randint(100000, 999999)}"
    payload: Dict[str, Any] = {
        "id": qid,
        "topic": TOPIC_NAME,
        "subtopic": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": f"ems_gr9_t1_economic_systems_{subskill}",
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


def _svg_spectrum(
    countries: List[tuple],
) -> Dict[str, Any]:
    """Render an SVG economic spectrum scale plotting three country markers."""
    width, height = 620, 210
    axis_y = 115
    x0, x1 = 60, 560
    span = x1 - x0
    marks_svg: List[str] = []
    for idx, (name, market_pct, color) in enumerate(countries):
        cx = x0 + round(span * market_pct / 100.0)
        label_y = 65 if idx % 2 == 0 else 168
        line_y2 = 74 if idx % 2 == 0 else 150
        marks_svg.append(
            f'<line x1="{cx}" y1="{axis_y}" x2="{cx}" y2="{line_y2}" '
            f'stroke="{color}" stroke-width="2" stroke-dasharray="3,2"/>'
            f'<circle cx="{cx}" cy="{axis_y}" r="7" fill="{color}" stroke="#0f172a" stroke-width="1.5"/>'
            f'<text x="{cx}" y="{label_y}" text-anchor="middle" font-size="12" '
            f'font-weight="700" fill="#0f172a">{name} ({market_pct}%)</text>'
        )
    ticks_svg: List[str] = []
    for pct in (0, 25, 50, 75, 100):
        tx = x0 + round(span * pct / 100.0)
        ticks_svg.append(
            f'<line x1="{tx}" y1="{axis_y - 6}" x2="{tx}" y2="{axis_y + 6}" stroke="#475569" stroke-width="1.5"/>'
            f'<text x="{tx}" y="{axis_y + 22}" text-anchor="middle" font-size="11" fill="#334155">{pct}%</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">'
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff" rx="8"/>'
        f'<text x="{width // 2}" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        f'Economic Systems Spectrum (% Market Allocation)</text>'
        f'<text x="{x0}" y="{axis_y - 16}" text-anchor="start" font-size="11" font-weight="600" fill="#b91c1c">Pure Planned (0%)</text>'
        f'<text x="{x1}" y="{axis_y - 16}" text-anchor="end" font-size="11" font-weight="600" fill="#047857">Pure Market (100%)</text>'
        f'<line x1="{x0}" y1="{axis_y}" x2="{x1}" y2="{axis_y}" stroke="#1e293b" stroke-width="3"/>'
        f'{"".join(ticks_svg)}{"".join(marks_svg)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_public_private_bars(
    entity: str, public_bn: int, private_bn: int
) -> Dict[str, Any]:
    """Render SVG comparison bars for public vs private spending."""
    total = public_bn + private_bn
    pub_pct = round(public_bn * 100.0 / total, 1)
    priv_pct = round(private_bn * 100.0 / total, 1)
    max_bar = 360
    pub_w = max(24, round(max_bar * public_bn / total))
    priv_w = max(24, max_bar - pub_w)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="100%" height="auto">'
        f'<rect x="0" y="0" width="600" height="200" fill="#ffffff" rx="8"/>'
        f'<text x="300" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">'
        f'{entity}: Annual Spending Mix (Total R{total} billion)</text>'
        f'<text x="40" y="72" font-size="12" font-weight="600" fill="#1e293b">Public Sector Goods</text>'
        f'<rect x="195" y="56" width="{pub_w}" height="24" fill="#2563eb" rx="4"/>'
        f'<text x="{203 + pub_w}" y="73" font-size="12" font-weight="700" fill="#1e3a8a">R{public_bn}bn ({fmt_dec(pub_pct)}%)</text>'
        f'<text x="40" y="122" font-size="12" font-weight="600" fill="#1e293b">Private Sector Goods</text>'
        f'<rect x="195" y="106" width="{priv_w}" height="24" fill="#059669" rx="4"/>'
        f'<text x="{203 + priv_w}" y="123" font-size="12" font-weight="700" fill="#065f46">R{private_bn}bn ({fmt_dec(priv_pct)}%)</text>'
        f'<text x="300" y="170" text-anchor="middle" font-size="11" fill="#475569">'
        f'Public allocation covers clinics, schools and roads; private covers retail and commercial output.</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _build_01_basic_economic_problem_scarcity(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("Limpopo provincial budget", 180, 115, "rural clinic upgrades and textbook delivery"),
        ("Eastern Cape municipal grant", 240, 155, "clean water pipelines and road repairs"),
        ("KwaZulu-Natal school infrastructure fund", 310, 195, "science laboratories and solar backup"),
        ("Mpumalanga local development fund", 210, 130, "agricultural irrigation and library access"),
        ("Northern Cape community reserve", 160, 95, "mobile health units and borehole maintenance"),
        ("Free State municipal allocation", 275, 170, "sanitation upgrades and storm-water drains"),
    ]
    ctx, wanted_m, available_m, goods = rng.choice(cases)
    shortfall_m = wanted_m - available_m
    pct_funded = round((available_m / wanted_m) * 100, 1)
    prompt = (
        f"A {ctx} receives community requests for {goods} totalling R{wanted_m} million, "
        f"but only R{available_m} million is available in the treasury.\n\n"
        f"(a) Explain why this situation illustrates the basic economic problem of scarcity.\n"
        f"(b) Calculate the funding shortfall in Rand millions and the percentage of requested needs that can be funded."
    )
    ans = f"Shortfall: R{shortfall_m} million; Funded: {fmt_dec(pct_funded)}%"
    sol = (
        f"**(a) The Economic Problem of Scarcity:**\n"
        f"- Human needs and wants for public services ({goods}) are unlimited, whereas productive resources and treasury funds are scarce (limited).\n"
        f"- Because R{available_m} million cannot satisfy R{wanted_m} million in requests, authorities must make choices about *what*, *how*, and *for whom* to produce.\n\n"
        f"**(b) Calculation:**\n"
        f"- Shortfall $= \\text{{R}}{wanted_m}\\text{{ million}} - \\text{{R}}{available_m}\\text{{ million}} = \\text{{R}}{shortfall_m}\\text{{ million}}$\n"
        f"- Percentage funded $= \\frac{{{available_m}}}{{{wanted_m}}} \\times 100 = {fmt_dec(pct_funded)}\\%$"
    )
    return make_question(
        rng=rng,
        subskill="01_basic_economic_problem_scarcity",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=f"Scarcity arises because unlimited wants (R{wanted_m} million) exceed limited funds (R{available_m} million), leaving a R{shortfall_m} million shortfall ({fmt_dec(pct_funded)}% funded).",
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define scarcity as unlimited wants vs limited resources", "marks": 2, "type": "A"},
            {"step": f"Calculate shortfall R{shortfall_m} million", "marks": 1, "type": "A"},
            {"step": f"Calculate {fmt_dec(pct_funded)}% funded", "marks": 1, "type": "CA"},
        ],
        marking_guide="Award 2 marks for linking unlimited wants to scarce funds; 1 mark for shortfall; 1 mark for percentage.",
        hints={
            "tier_1": "Compare unlimited community wants against finite government funds.",
            "tier_2": "Subtract available funds from total requested funds, then divide available by requested times 100.",
            "tier_3": f"Shortfall = {wanted_m} - {available_m} = R{shortfall_m} million; Funded = ({available_m}/{wanted_m}) * 100 = {fmt_dec(pct_funded)}%.",
        },
        misconception_tags=["confuses_scarcity_with_poverty", "reverses_percentage_ratio"],
    )


def _build_02_defining_economic_system(rng: random.Random, mode: str) -> Dict[str, Any]:
    contexts = [
        ("determining how maize, electricity and healthcare are distributed across households", "the way a country organises production, distribution and consumption of scarce goods and services"),
        ("deciding whether factories produce tractors or smartphones and who receives them", "the structured method a society uses to allocate scarce resources to satisfy competing needs"),
        ("coordinating decisions among households, businesses and government regarding limited resources", "an organised framework determining what is produced, how it is produced, and for whom it is produced"),
        ("resolving shortages of skilled labour, capital and raw materials across regions", "the institutional arrangement a nation adopts to manage scarcity and coordinate economic activity"),
        ("balancing private enterprise profits against essential municipal service provision", "a country's coordinated system of ownership, resource allocation and exchange"),
    ]
    focus, correct_def = rng.choice(contexts)
    distractors = [
        "a temporary marketing strategy used by commercial banks during festive seasons",
        "the physical transport network connecting harbours to inland factories",
        "a set of personal budgeting tips for individual household savings",
    ]
    prompt = f"Which statement best defines an **economic system** when {focus}?"
    sol = (
        f"An **economic system** is {correct_def}.\n\n"
        f"- Every country must answer the three core questions of **what**, **how**, and **for whom** to produce because resources are scarce."
    )
    return make_question(
        rng=rng,
        subskill="02_defining_economic_system",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct_def,
        sample_answer=correct_def,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Select accurate definition of economic system", "marks": 2, "type": "A"}],
        marking_guide="2 marks for correct definition linking resource allocation, production, distribution and consumption.",
        hints={
            "tier_1": "Think at national scale rather than individual business or transport scale.",
            "tier_2": "An economic system answers what, how and for whom scarce goods are produced.",
            "tier_3": f"Correct answer: {correct_def}.",
        },
        misconception_tags=["equates_economic_system_with_banking_only"],
        options=[correct_def] + distractors,
        duration_mins=2,
    )


def _build_03_planned_economy_origin_command(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("early 20th-century socialist revolutions seeking rapid state-led industrialisation", "Planned (command) economy", "socialist and communist political theories", "North Korea and former USSR"),
        ("post-1917 central state committees setting five-year steel and grain targets", "Planned (command) economy", "Marxist-socialist central ownership doctrine", "former Soviet Union and Cuba"),
        ("a system where a central government bureau replaces market prices with direct production orders", "Planned (command) economy", "state socialism rejecting private capital accumulation", "North Korea"),
        ("centralised national ministries assigning factory quotas and citizen rations", "Planned (command) economy", "collectivist ideology aiming to eliminate class inequality", "historical East Germany and USSR"),
        ("an economy driven strictly by central state authority rather than private profit", "Planned (command) economy", "socialist command theory", "Cuba and North Korea"),
    ]
    clue, sys_name, origin, examples = rng.choice(cases)
    prompt = (
        f"Examine this economic description: *{clue}.*\n\n"
        f"(a) Identify this economic system.\n"
        f"(b) State its ideological origin and give TWO historical or modern country examples."
    )
    ans = f"{sys_name}; rooted in {origin}; examples include {examples}"
    sol = (
        f"- **System:** {sys_name} (also called a centrally planned economy).\n"
        f"- **Origin:** Developed out of {origin}, where the state takes control of factors of production to pursue social equality.\n"
        f"- **Examples:** {examples} (e.g., Cuba, North Korea, former USSR)."
    )
    return make_question(
        rng=rng,
        subskill="03_planned_economy_origin_command",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Identify planned/command economy", "marks": 1, "type": "A"},
            {"step": "State socialist/communist origin", "marks": 1, "type": "A"},
            {"step": "Provide two country examples", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for identifying planned/command economy, 1 mark for origin, 2 marks for two valid examples.",
        hints={
            "tier_1": "Focus on central state directives and five-year targets.",
            "tier_2": "This command model comes from socialist/communist ideology.",
            "tier_3": f"{sys_name}, originating in {origin}, seen in {examples}.",
        },
        misconception_tags=["confuses_command_with_mixed_economy"],
    )


def _build_04_planned_economy_ownership_control(rng: random.Random, mode: str) -> Dict[str, Any]:
    assets = [
        ("coal mines, steel mills, farmland and transport fleets", "The central government owns and controls all factors of production on behalf of citizens."),
        ("all factories, retail stores, banks and agricultural estates", "Private ownership of business capital is prohibited; the state controls all production decisions."),
        ("national energy grids, telecommunications and housing blocks", "Central authorities own resources, set wages and determine output quotas without private competition."),
        ("manufacturing plants, raw mineral deposits and machinery", "State ministries retain full ownership of land, labour direction and capital equipment."),
        ("commercial shipping, refineries and distribution warehouses", "No private entrepreneurs are allowed to accumulate capital goods; the state acts as sole employer."),
    ]
    asset_list, correct = rng.choice(assets)
    options = [
        correct,
        "Private shareholders own factories and prices adjust solely through free market competition.",
        "Foreign multinational corporations own all public utilities without state regulation.",
        "Individual consumers vote on factory output via unregulated stock exchanges.",
    ]
    prompt = f"In a pure **planned economy**, who owns and controls {asset_list}?"
    sol = (
        f"- **Correct statement:** {correct}\n"
        f"- In a planned economy, private property rights over business capital do not exist and there is no profit motive for private entrepreneurs."
    )
    return make_question(
        rng=rng,
        subskill="04_planned_economy_ownership_control",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct,
        sample_answer=correct,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify state ownership in planned economy", "marks": 2, "type": "A"}],
        marking_guide="2 marks for selecting state ownership and central resource control.",
        hints={
            "tier_1": "Remember who controls resources when private enterprise is absent.",
            "tier_2": "In a command economy, factors of production belong to the state.",
            "tier_3": correct,
        },
        misconception_tags=["assumes_mixed_ownership_in_command_system"],
        options=options,
        duration_mins=2,
    )


def _build_05_planned_economy_advantages(rng: random.Random, mode: str) -> Dict[str, Any]:
    scenarios = [
        ("a country facing severe post-war poverty where basic clinics, schools and housing are unaffordable to most families", "guaranteed universal access to basic healthcare, education and housing", "minimising extreme unemployment because the state assigns jobs to citizens"),
        ("an economy threatened by private monopolies charging excessive water and electricity tariffs", "preventing private monopoly exploitation and wasteful duplication of infrastructure", "directing resources straight toward national priorities rather than luxury goods"),
        ("a newly formed industrial state trying to prevent extreme gaps between billionaires and destitute workers", "ensuring a more equal distribution of income and wealth", "providing essential public services such as immunisation and schooling to everyone"),
        ("a nation mobilising all factories to build railways, dams and steel plants quickly", "concentrating resources rapidly on strategic national projects", "avoiding duplicate competing factories that waste scarce raw materials"),
        ("rural communities lacking roads and clean water because private firms find them unprofitable", "prioritising basic community needs over short-term private profit", "maintaining full state employment and affordable staple rations"),
    ]
    context, adv1, adv2 = rng.choice(scenarios)
    prompt = (
        f"Consider {context}.\n\n"
        f"Identify **TWO** core advantages of a planned economy that address this situation, and explain each briefly."
    )
    ans = f"1) {adv1}; 2) {adv2}"
    sol = (
        f"**Two key advantages of a planned economy:**\n"
        f"1. **{adv1.capitalize()}:** State resources are directed toward essential social welfare rather than only profitable luxury items.\n"
        f"2. **{adv2.capitalize()}:** Central coordination aligns employment and large infrastructure without profit-driven exclusion."
    )
    return make_question(
        rng=rng,
        subskill="05_planned_economy_advantages",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "First relevant advantage + brief explanation", "marks": 2, "type": "A"},
            {"step": "Second relevant advantage + brief explanation", "marks": 2, "type": "A"},
        ],
        marking_guide="Award 2 marks for each clearly explained advantage aligned with planned economy principles.",
        hints={
            "tier_1": "Think about basic services, equality, employment and avoiding duplication.",
            "tier_2": "Focus on how central control allocates goods regardless of ability to pay.",
            "tier_3": f"Advantages: {adv1}; and {adv2}.",
        },
        misconception_tags=["lists_market_advantages_under_planned_economy"],
    )


def _build_06_planned_economy_disadvantages(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("state shoe factories producing 50 000 identical left-foot boots in winter while grocery stores run out of cooking oil", "inflexibility and severe shortages or surpluses caused by slow central bureaucracy"),
        ("government clerks ignoring customer complaints about faulty radios because salaries never change", "lack of innovation, poor product quality and absence of profit/competition incentives"),
        ("citizens waiting years for telephone connections and restricted to a single brand of soap", "very limited consumer choice and absence of consumer sovereignty"),
        ("massive coal waste in state boilers because managers are paid for tonnage rather than efficiency", "high inefficiency and wasteful resource use without cost discipline"),
        ("talented engineers leaving because extra effort brings zero personal financial reward", "suppression of individual initiative and low labour productivity"),
    ]
    case_desc, disad = rng.choice(cases)
    distractors = [
        "excessive private competition driving prices downward for consumers",
        "unregulated multinational corporations avoiding corporate income tax",
        "households having too many competing private retail brands to choose from",
    ]
    prompt = f"Which disadvantage of a planned economy is directly illustrated by *{case_desc}*?"
    sol = (
        f"- **Disadvantage:** {disad.capitalize()}.\n"
        f"- Without market price signals or competition, central planners struggle to match supply accurately with changing consumer preferences."
    )
    return make_question(
        rng=rng,
        subskill="06_planned_economy_disadvantages",
        question_type="mcq",
        prompt=prompt,
        correct_answer=disad.capitalize(),
        sample_answer=disad.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Match symptom to planned economy disadvantage", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurately identifying the structural weakness illustrated.",
        hints={
            "tier_1": "Notice whether the problem stems from bureaucracy, missing incentives or limited variety.",
            "tier_2": "Ask why state managers neither respond to consumers nor fear bankruptcy.",
            "tier_3": disad.capitalize(),
        },
        misconception_tags=["confuses_command_shortages_with_market_inflation"],
        options=[disad.capitalize()] + distractors,
        duration_mins=2,
    )


def _build_07_iron_rice_bowl_incentive_analysis(rng: random.Random, mode: str) -> Dict[str, Any]:
    factories = [
        ("state textile plant", 420, 630),
        ("command tractor workshop", 180, 270),
        ("state bicycle assembly unit", 500, 725),
        ("collectivist ceramic factory", 320, 480),
        ("state canning facility", 600, 840),
    ]
    plant, fixed_out, incentive_out = rng.choice(factories)
    diff = incentive_out - fixed_out
    pct_gain = round((diff / fixed_out) * 100, 1)
    prompt = (
        f"In historical centrally planned systems, workers held an **'iron rice bowl'** guarantee. "
        f"At a {plant}, monthly output under guaranteed fixed wages is {fixed_out} units. "
        f"When performance bonuses are later introduced, output rises to {incentive_out} units.\n\n"
        f"(a) Explain what the 'iron rice bowl' meant for job security and work motivation.\n"
        f"(b) Calculate the percentage increase in monthly production after incentives were added."
    )
    ans = f"Guaranteed lifelong job and food/pay regardless of effort, reducing motivation; +{fmt_dec(pct_gain)}%"
    sol = (
        f"**(a) Meaning of the 'Iron Rice Bowl':**\n"
        f"- The state guaranteed workers lifelong employment, fixed wages and basic welfare regardless of individual effort or efficiency.\n"
        f"- Because workers could not be dismissed for low output and earned no reward for extra effort, productivity and quality often stagnated.\n\n"
        f"**(b) Production Increase:**\n"
        f"- Increase $= {incentive_out} - {fixed_out} = {diff}$ units\n"
        f"- Percentage increase $= \\frac{{{diff}}}{{{fixed_out}}} \\times 100 = {fmt_dec(pct_gain)}\\%$"
    )
    return make_question(
        rng=rng,
        subskill="07_iron_rice_bowl_incentive_analysis",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain guaranteed job/security regardless of performance", "marks": 1, "type": "A"},
            {"step": "State negative impact on productivity/motivation", "marks": 1, "type": "A"},
            {"step": f"Calculate difference {diff} and +{fmt_dec(pct_gain)}%", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for explaining iron rice bowl + incentive effect; 2 marks for accurate % gain.",
        hints={
            "tier_1": "Think of a rice bowl that never breaks—even if work performance drops.",
            "tier_2": "Compute (New output - Old output) / Old output * 100.",
            "tier_3": f"Difference = {diff} units; Gain = ({diff}/{fixed_out}) * 100 = {fmt_dec(pct_gain)}%.",
        },
        misconception_tags=["equates_iron_rice_bowl_with_food_rationing_only"],
    )


def _build_08_market_economy_origin_capitalism(rng: random.Random, mode: str) -> Dict[str, Any]:
    theories = [
        ("Adam Smith's 1776 concept of the 'invisible hand'", "individual self-interest and free market competition naturally guide resources toward consumer wants without central state direction"),
        ("free-market capitalism (laissez-faire doctrine)", "private property, profit incentives and minimal government interference maximise economic efficiency"),
        ("market-based capital accumulation", "entrepreneurs risk private capital to earn profits by supplying goods consumers voluntarily buy"),
        ("decentralised price coordination", "millions of buyers and sellers coordinate automatically through fluctuating prices rather than state commands"),
        ("liberal economic thought from the Industrial Revolution", "competition forces producers to lower costs and innovate to survive in the market"),
    ]
    concept, meaning = rng.choice(theories)
    distractors = [
        "central government planners abolish private wealth and distribute equal food parcels",
        "commercial trade with foreign nations is outlawed to preserve self-sufficiency",
        "all commercial banks and mines are nationalised under parliament control",
    ]
    prompt = f"What does **{concept}** describe in the origin of a **market economy**?"
    sol = f"- **{concept.capitalize()}:** {meaning.capitalize()}."
    return make_question(
        rng=rng,
        subskill="08_market_economy_origin_capitalism",
        question_type="mcq",
        prompt=prompt,
        correct_answer=meaning.capitalize(),
        sample_answer=meaning.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify market economy foundational principle", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurate capitalist/market principle.",
        hints={
            "tier_1": "Think about private enterprise and voluntary exchange.",
            "tier_2": "Adam Smith argued that self-interest in competitive markets serves society's needs.",
            "tier_3": meaning.capitalize(),
        },
        misconception_tags=["thinks_invisible_hand_means_secret_government_control"],
        options=[meaning.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_09_market_economy_price_mechanism(rng: random.Random, mode: str) -> Dict[str, Any]:
    goods = [
        ("solar home inverters during load-shedding", 1800, 2650),
        ("locally manufactured leather school shoes", 320, 440),
        ("organic avocados during dry winter months", 28, 45),
        ("smartphones with dual-SIM capability", 2200, 3100),
        ("bicycles for township commuters", 1500, 2100),
    ]
    item, p_old, p_new = rng.choice(goods)
    pct_rise = round(((p_new - p_old) / p_old) * 100, 1)
    prompt = (
        f"In a pure market economy, sudden high demand pushes the price of {item} "
        f"up from {fmt_zar(p_old)} to {fmt_zar(p_new)}.\n\n"
        f"(a) Calculate the percentage rise in market price.\n"
        f"(b) Explain how the **price mechanism** signals producers to adjust 'what to produce' without government orders."
    )
    ans = f"+{fmt_dec(pct_rise)}%; higher price signals higher profit potential, attracting producers to allocate more resources to {item}"
    sol = (
        f"**(a) Price Increase:**\n"
        f"- Increase $= {fmt_zar(p_new - p_old)}$\n"
        f"- $\\frac{{{p_new - p_old}}}{{{p_old}}} \\times 100 = {fmt_dec(pct_rise)}\\%$\n\n"
        f"**(b) Price Mechanism Signal:**\n"
        f"- Rising prices increase expected profit margins, sending an automatic signal to firms to shift labour and capital toward producing more {item}."
    )
    return make_question(
        rng=rng,
        subskill="09_market_economy_price_mechanism",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate +{fmt_dec(pct_rise)}% price rise", "marks": 2, "type": "A"},
            {"step": "Explain profit signal expanding supply of the item", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage calculation; 2 marks for explaining price -> profit -> resource shift.",
        hints={
            "tier_1": "Divide price increase by original price, then link higher prices to firm profits.",
            "tier_2": "Profit-seeking businesses expand output wherever prices rise fastest.",
            "tier_3": f"+{fmt_dec(pct_rise)}%; higher prices raise profits, drawing resources into producing {item}.",
        },
        misconception_tags=["thinks_government_sets_prices_in_pure_market"],
    )


def _build_10_market_economy_characteristics(rng: random.Random, mode: str) -> Dict[str, Any]:
    features = [
        ("private ownership of land and capital", "profit motive driving business decisions", "intense competition among sellers", "freedom of consumer choice"),
        ("unrestricted entry for entrepreneurs", "market-determined wages and prices", "minimal state economic regulation", "private property protection"),
        ("self-interest guiding households and firms", "supply and demand setting prices", "competition lowering unit costs", "consumer sovereignty"),
        ("private banks financing new start-ups", "absence of central five-year quotas", "freedom to choose occupation", "profit and loss accountability"),
        ("private ownership of retail chains", "prices reflecting relative scarcity", "rival brands competing for buyers", "limited government role"),
    ]
    f1, f2, f3, f4 = rng.choice(features)
    correct_set = f"{f1.capitalize()}, {f2}, and {f3}"
    prompt = (
        f"A Grade 9 learner classifies a country's economic traits.\n\n"
        f"List **FOUR** defining characteristics of a pure **market economy** (such as {f4}) and explain how competition protects buyers."
    )
    ans = f"Private ownership, profit motive, competition, freedom of choice/enterprise, minimal state role; competition stops overcharging and improves quality"
    sol = (
        f"**Four characteristics of a pure market economy:**\n"
        f"1. **Private ownership** ({f1}).\n"
        f"2. **Profit motive** ({f2}).\n"
        f"3. **Competition** ({f3}).\n"
        f"4. **Freedom of choice & limited state intervention** ({f4}).\n\n"
        f"**Role of competition:** Rival firms must offer fair prices and better quality or lose customers to competitors."
    )
    return make_question(
        rng=rng,
        subskill="10_market_economy_characteristics",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=f"{correct_set}, plus {f4}. Competition forces lower prices and higher quality.",
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": "Four accurate market economy characteristics (1 mark each)", "marks": 4, "type": "A"},
            {"step": "Explain competition discipline on price/quality", "marks": 1, "type": "A"},
        ],
        marking_guide="4 marks for four distinct market characteristics; 1 mark for consumer-protection role of competition.",
        hints={
            "tier_1": "Think of ownership, motive, rivalry, and choice.",
            "tier_2": "Who owns firms, why do they operate, and who limits their power?",
            "tier_3": f"{correct_set}, plus {f4}. Competition prevents monopoly overpricing.",
        },
        misconception_tags=["includes_state_price_controls_as_market_trait"],
    )


def _build_11_market_economy_advantages(rng: random.Random, mode: str) -> Dict[str, Any]:
    examples = [
        ("two rival mobile networks slashing data prices and upgrading to 5G coverage", "rapid technological innovation and competitive pricing for consumers"),
        ("independent bakeries opening near new housing estates within weeks of demand growing", "quick responsiveness to shifting consumer wants without bureaucratic delay"),
        ("factories adopting energy-saving machinery to outcompete foreign rivals", "high productive efficiency and reduced resource waste per unit"),
        ("supermarkets stocking dozens of maize meal, tea and detergent brands across budgets", "wide consumer choice and variety matching diverse preferences"),
        ("software start-ups scaling globally because successful founders earn substantial returns", "strong financial incentives rewarding hard work and entrepreneurship"),
    ]
    case, adv = rng.choice(examples)
    distractors = [
        "guaranteed equal income regardless of productivity",
        "complete elimination of seasonal price changes by central decree",
        "universal free housing distributed purely through state rationing",
    ]
    prompt = f"The real-world observation *{case}* demonstrates which key **advantage** of a market economy?"
    sol = f"- **Advantage:** {adv.capitalize()}.\n- Competition and the profit motive compel private firms to stay efficient and responsive."
    return make_question(
        rng=rng,
        subskill="11_market_economy_advantages",
        question_type="mcq",
        prompt=prompt,
        correct_answer=adv.capitalize(),
        sample_answer=adv.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify advantage shown by scenario", "marks": 2, "type": "A"}],
        marking_guide="2 marks for matching the market example to the correct economic advantage.",
        hints={
            "tier_1": "Focus on what rivalry and profit encourage businesses to do.",
            "tier_2": "Market economies reward efficiency, speed, variety and innovation.",
            "tier_3": adv.capitalize(),
        },
        misconception_tags=["confuses_equity_with_efficiency_advantages"],
        options=[adv.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_12_market_economy_disadvantages(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("private ambulance companies refusing to serve distant rural farms because emergency calls there operate at a loss", "neglect of essential public and merit services when unprofitable"),
        ("the richest 5% of households owning luxury estates while unemployed workers lack basic healthcare", "severe wealth and income inequality"),
        ("chemical factories dumping untreated effluent into rivers to boost shareholder dividends", "environmental pollution and worker exploitation due to unchecked profit pursuit"),
        ("speculative housing bubbles crashing and triggering sudden mass retrenchments", "cyclical economic instability (booms and depressions)"),
        ("a dominant software firm buying out smaller rivals to raise subscription fees sharply", "emergence of unregulated private monopolies restricting competition"),
    ]
    case, disad = rng.choice(cases)
    prompt = (
        f"Analyse the scenario below in a pure market economy:\n"
        f"*{case}.*\n\n"
        f"(a) Identify the specific market-economy disadvantage illustrated.\n"
        f"(b) Suggest ONE realistic corrective action a government would take in a mixed economy."
    )
    ans = f"Disadvantage: {disad}; Corrective action: targeted state provision, taxation/redistribution, or environmental/competition regulation"
    sol = (
        f"**(a) Market Disadvantage:** {disad.capitalize()}.\n"
        f"**(b) Mixed-Economy Remedy:** Introduce targeted government intervention—such as public funding/provision, progressive taxes, anti-pollution laws, or competition regulation—without eliminating private enterprise."
    )
    return make_question(
        rng=rng,
        subskill="12_market_economy_disadvantages",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Name accurate market failure/disadvantage", "marks": 2, "type": "A"},
            {"step": "Propose feasible mixed-economy remedy", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for diagnosing the market weakness; 2 marks for an appropriate state intervention.",
        hints={
            "tier_1": "Ask what goes wrong when profit is the *only* rule.",
            "tier_2": "Identify whether the harm is inequality, missing rural services, pollution or monopoly.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_pure_market_solves_all_externalities"],
    )


def _build_13_mixed_economy_definition_origin(rng: random.Random, mode: str) -> Dict[str, Any]:
    prompts_pool = [
        ("combining private entrepreneurship with public clinics, schools and progressive taxes", "combines elements of both market and planned economies, blending private ownership with targeted government intervention"),
        ("reforming strict command or laissez-faire systems after the Great Depression and post-war reconstructions", "uses price signals and private firms alongside state regulation and welfare safety nets"),
        ("balancing capitalist efficiency against social protection", "merges private profit-driven enterprise with public sector provision of essential services"),
        ("today's dominant global national structure, including South Africa, the UK and Germany", "allows private businesses to compete freely while government regulates markets and supplies public goods"),
        ("correcting extreme inequality and market crashes without nationalising every shop", "integrates private property and free markets with public ownership of strategic utilities and social grants"),
    ]
    clue, definition = rng.choice(prompts_pool)
    distractors = [
        "eliminates money completely and relies exclusively on rural barter exchanges",
        "forbids both private entrepreneurship and public taxation simultaneously",
        "hands all farms and factories permanently to foreign diplomats",
    ]
    prompt = f"A **mixed economy**—illustrated by {clue}—is best defined as an economic system that:"
    sol = (
        f"- **Definition:** {definition.capitalize()}.\n"
        f"- Almost every modern country operates a mixed economy, differing only in the relative size of its public vs private sector."
    )
    return make_question(
        rng=rng,
        subskill="13_mixed_economy_definition_origin",
        question_type="mcq",
        prompt=prompt,
        correct_answer=definition.capitalize(),
        sample_answer=definition.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Select accurate mixed economy definition", "marks": 2, "type": "A"}],
        marking_guide="2 marks for identifying combination of private enterprise and state intervention.",
        hints={
            "tier_1": "Look for a blend rather than an extreme.",
            "tier_2": "Mixed systems keep private markets but add government rules and public services.",
            "tier_3": definition.capitalize(),
        },
        misconception_tags=["thinks_mixed_means_half_barter_half_cash"],
        options=[definition.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_14_mixed_economy_government_role(rng: random.Random, mode: str) -> Dict[str, Any]:
    roles = [
        ("enacting labour laws, consumer protection rules and anti-monopoly regulations", "Creating and enforcing the legal framework to protect consumers, workers and fair competition"),
        ("funding public primary schools, national defence and rural tarred roads", "Providing essential public and merit goods that private firms might under-supply"),
        ("levying progressive income taxes to finance old-age pensions and child grants", "Redistributing income to reduce poverty and soften extreme inequality"),
        ("using Reserve Bank interest rates and fiscal budgets during a recession", "Stabilising inflation, unemployment and economic fluctuations"),
        ("operating strategic state utilities while licensing private competitors", "Managing natural monopolies and safeguarding critical national infrastructure"),
    ]
    action, function_name = rng.choice(roles)
    prompt = (
        f"In a mixed economy, government performs four major economic functions.\n\n"
        f"State which major function is shown when the state focuses on *{action}*, "
        f"and explain why pure private markets struggle to perform this role alone."
    )
    ans = f"{function_name}; markets prioritise profit over social welfare, stability or non-excludable public benefits"
    sol = (
        f"- **Government Role:** {function_name}.\n"
        f"- **Why State Action Is Needed:** Private companies focus on profit margins and cannot easily exclude non-payers from public infrastructure or unilaterally redistribute income."
    )
    return make_question(
        rng=rng,
        subskill="14_mixed_economy_government_role",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Identify specific government economic role", "marks": 1, "type": "A"},
            {"step": "Explain why pure markets fail to deliver it adequately", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for naming the function; 2 marks for explaining private market limitation.",
        hints={
            "tier_1": "Recall the four economic roles: legal rules, public goods, redistribution, stabilisation.",
            "tier_2": "Ask why private investors would not willingly fund that activity.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_state_regulation_with_total_central_planning"],
    )


def _build_15_mixed_economy_advantages(rng: random.Random, mode: str) -> Dict[str, Any]:
    contexts = [
        ("entrepreneurs launch tech start-ups freely while pensioners receive monthly state grants", "combines private business innovation and efficiency with a social welfare safety net"),
        ("supermarkets compete vigorously on grocery prices while government enforces food-safety hygiene", "encourages competitive consumer choice while protecting public health and standards"),
        ("private factories export vehicles globally while the state builds ports and arterial highways", "pairs private export dynamism with public strategic infrastructure investment"),
        ("citizens choose their own careers while public hospitals treat emergency patients regardless of income", "preserves economic freedom alongside guaranteed essential healthcare access"),
        ("commercial banks lend capital for expansion while competition watchdogs block price-fixing cartels", "promotes entrepreneurial growth while curbing monopoly abuse"),
    ]
    obs, adv = rng.choice(contexts)
    prompt = (
        f"Read the mixed-economy example: *{obs}.*\n\n"
        f"Explain **TWO** advantages of a mixed economy highlighted by this balance."
    )
    ans = f"It {adv}, avoiding both pure command rigidity and unchecked market inequality"
    sol = (
        f"**Advantages highlighted:**\n"
        f"1. **Efficiency & Freedom:** Private enterprises remain motivated by profit, competition and consumer choice.\n"
        f"2. **Equity & Protection:** State intervention {adv}, preventing extreme deprivation or monopoly exploitation."
    )
    return make_question(
        rng=rng,
        subskill="15_mixed_economy_advantages",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Advantage related to private efficiency/choice", "marks": 2, "type": "A"},
            {"step": "Advantage related to public welfare/protection", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for market-side strength; 2 marks for state-protection strength.",
        hints={
            "tier_1": "Notice both the private-sector side and the government side of the example.",
            "tier_2": "Explain how the system captures strengths of both models.",
            "tier_3": ans,
        },
        misconception_tags=["claims_mixed_economy_eliminates_all_taxes"],
    )


def _build_16_mixed_economy_disadvantages(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("escalating personal and company taxes needed to fund growing welfare and bailout budgets", "high taxation burden that can discourage private investment and hard work"),
        ("state-owned power and rail monopolies recording billion-rand losses due to weak accountability", "inefficient or corrupt state-owned enterprises (SOEs) draining taxpayers"),
        ("small businesses waiting 14 months for municipal zoning permits and environmental clearances", "excessive bureaucratic red tape slowing private job creation"),
        ("government borrowing heavily in bond markets, pushing up interest rates for private builders", "public sector spending crowding out private sector capital"),
        ("frequent policy uncertainty between state price caps and private investment rules", "conflicting regulatory signals reducing investor confidence"),
    ]
    case, disad = rng.choice(cases)
    distractors = [
        "complete prohibition of all private small shops and retail franchises",
        "zero government spending on national defence, courts or primary schools",
        "workers holding guaranteed lifelong employment with zero private jobs",
    ]
    prompt = f"Which potential **disadvantage** of a mixed economy is shown by *{case}*?"
    sol = f"- **Disadvantage:** {disad.capitalize()}.\n- Poorly managed state intervention can undermine the efficiency gains of private markets."
    return make_question(
        rng=rng,
        subskill="16_mixed_economy_disadvantages",
        question_type="mcq",
        prompt=prompt,
        correct_answer=disad.capitalize(),
        sample_answer=disad.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify disadvantage of mixed economy", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurate weakness of mixed systems.",
        hints={
            "tier_1": "Think about what happens when the state portion grows too costly or slow.",
            "tier_2": "Match taxes, SOE inefficiency, or red tape to the description.",
            "tier_3": disad.capitalize(),
        },
        misconception_tags=["assumes_mixed_economies_have_zero_disadvantages"],
        options=[disad.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_17_compare_systems_ownership_matrix(rng: random.Random, mode: str) -> Dict[str, Any]:
    rows_bank = [
        ("Ownership of resources", "State owns all", "Private individuals/firms", "Both state and private"),
        ("Main economic motive", "Social welfare / targets", "Private profit", "Profit + social welfare"),
        ("Price determination", "Central government sets", "Demand and supply", "Markets + selective regulation"),
        ("Consumer choice", "Very limited", "Very wide", "Wide with public standards"),
        ("Role of government", "Controls everything", "Minimal / protection only", "Regulates & provides public goods"),
    ]
    chosen = rng.sample(rows_bank, 3)
    headers = ["Criterion", "Planned Economy", "Market Economy", "Mixed Economy"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [
        "| Criterion | Planned Economy | Market Economy | Mixed Economy |",
        "|---|---|---|---|",
    ]
    for r_idx, row_vals in enumerate(chosen, start=1):
        # Blank 1 required cell per row chosen deterministically by rng
        blank_col = rng.randint(1, 3)
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
                sys_lbl = headers[c_idx]
                cell_hints[coord] = f"Recall the '{row_vals[0]}' rule for a {sys_lbl}."
        rows_ui.append(row_cells)
        md_lines.append(f"| {row_vals[0]} | {row_vals[1]} | {row_vals[2]} | {row_vals[3]} |")

    prompt = (
        "Complete the missing entries in the Economic Systems Comparison Matrix across "
        "Planned, Market, and Mixed economies."
    )
    md_table = "\n".join(md_lines)
    sol = f"**Completed Economic Systems Matrix:**\n\n{md_table}"
    return make_question(
        rng=rng,
        subskill="17_compare_systems_ownership_matrix",
        question_type="table_completion",
        prompt=prompt,
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=sol,
        marks=len(correct_map),
        marking_schema=[
            {"step": f"Correct entry for {k}: {v}", "marks": 1, "type": "A"}
            for k, v in correct_map.items()
        ],
        marking_guide="1 mark for each accurately completed comparison cell.",
        hints={
            "tier_1": "Compare ownership, profit motive, pricing and state intervention.",
            "tier_2": "Planned = state control; Market = private supply & demand; Mixed = blend of both.",
            "tier_3": md_table,
        },
        misconception_tags=["swaps_market_and_planned_price_mechanisms"],
        table_payload={
            "headers": headers,
            "columns": [{"key": h.lower().replace(" ", "_"), "label": h} for h in headers],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
        duration_mins=5,
    )


def _build_18_compare_systems_allocation_questions(rng: random.Random, mode: str) -> Dict[str, Any]:
    questions_focus = [
        ("What to produce?", "Central planners decide quotas", "Consumer spending & profit signals", "Private demand + state public priorities"),
        ("How to produce?", "State assigns labour & state plants", "Least-cost competitive private methods", "Private efficiency + labour/safety laws"),
        ("For whom to produce?", "State rations & equal distribution", "Consumers able & willing to pay price", "Buyers in markets + state grants for poor"),
    ]
    picked = rng.sample(questions_focus, 2)
    headers = ["Basic Question", "Planned Economy", "Market Economy", "Mixed Economy"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = [
        "| Basic Question | Planned Economy | Market Economy | Mixed Economy |",
        "|---|---|---|---|",
    ]
    for r_idx, row_vals in enumerate(picked, start=1):
        req_cols = rng.sample([1, 2, 3], 2)
        row_cells: List[Dict[str, Any]] = []
        for c_idx, val in enumerate(row_vals):
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
                cell_hints[coord] = f"How does a {headers[c_idx]} resolve '{row_vals[0]}'?"
        rows_ui.append(row_cells)
        md_lines.append(f"| {row_vals[0]} | {row_vals[1]} | {row_vals[2]} | {row_vals[3]} |")

    md_table = "\n".join(md_lines)
    prompt = "Complete the allocation table showing how each economic system answers the fundamental resource-allocation questions."
    return make_question(
        rng=rng,
        subskill="18_compare_systems_allocation_questions",
        question_type="table_completion",
        prompt=prompt,
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Resource Allocation Matrix:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[
            {"step": f"Cell {k} correctly explains {v}", "marks": 1, "type": "A"}
            for k, v in correct_map.items()
        ],
        marking_guide="1 mark per accurately filled cell across the three allocation questions.",
        hints={
            "tier_1": "Remember: planners command, markets follow prices/ability to pay, mixed combines both.",
            "tier_2": "'For whom' depends on quotas (planned) vs purchasing power (market) vs grants + markets (mixed).",
            "tier_3": md_table,
        },
        misconception_tags=["confuses_how_to_produce_with_for_whom"],
        table_payload={
            "headers": headers,
            "columns": [{"key": h.lower().replace(" ", "_"), "label": h} for h in headers],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
        duration_mins=5,
    )


def _build_19_sa_mixed_economy_private_public(rng: random.Random, mode: str) -> Dict[str, Any]:
    pairs = [
        ("Shoprite, FNB and local hardware stores", "Eskom, Transnet and municipal clinics"),
        ("Pick n Pay, Capitec Bank and private panelbeaters", "SANRAL highways, public schools and SAPS"),
        ("Woolworths, Discovery Health and farm co-ops", "Rand Water, municipal refuse trucks and provincial hospitals"),
        ("Clicks, Sasol fuel retailers and private Uber drivers", "SABC public broadcasting, Denel and public clinics"),
        ("Checkers, MTN and independent dental practices", "PRASA commuter rail, Eskom and municipal libraries"),
    ]
    private_ex, public_ex = rng.choice(pairs)
    prompt = (
        f"South Africa operates a **mixed economy**. Contrast {private_ex} with {public_ex}.\n\n"
        f"(a) Classify each group into the private or public sector.\n"
        f"(b) Explain why South Africa maintains both sectors instead of relying purely on one."
    )
    ans = f"Private sector: {private_ex}; Public sector: {public_ex}; balances private efficiency with essential public access and social equity"
    sol = (
        f"**(a) Classification:**\n"
        f"- **Private sector** (profit-driven, private capital): {private_ex}.\n"
        f"- **Public sector** (government/state-owned, essential infrastructure & social services): {public_ex}.\n\n"
        f"**(b) Rationale:** Private firms deliver competition, choice and tax revenue, while public enterprises ensure essential services reach communities even where profit margins are low."
    )
    return make_question(
        rng=rng,
        subskill="19_sa_mixed_economy_private_public",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Correct private vs public classification", "marks": 2, "type": "A"},
            {"step": "Explain balance between efficiency and essential equity", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for classifying both examples; 2 marks for mixed-economy rationale.",
        hints={
            "tier_1": "Ask which organisations seek profit for shareholders and which belong to the state.",
            "tier_2": "Public sector handles utilities and welfare; private handles commercial retail and banking.",
            "tier_3": ans,
        },
        misconception_tags=["classifies_public_companies_listed_on_jse_as_public_sector"],
    )


def _build_20_sa_state_owned_enterprises_evaluation(rng: random.Random, mode: str) -> Dict[str, Any]:
    soes = [
        ("Transnet freight rail", 48, 12, "upgrading railway lines and port cranes"),
        ("Eskom electricity generation", 72, 18, "maintaining power stations and grid lines"),
        ("national water bulk utility", 30, 8, "repairing pump stations and reservoirs"),
        ("PRASA passenger rail", 25, 6, "replacing commuter coaches and signalling"),
        ("municipal bus service", 15, 3, "modernising commuter depots"),
    ]
    soe, revenue_bn, bailout_bn, infra = rng.choice(soes)
    bailout_pct = round((bailout_bn / revenue_bn) * 100, 1)
    prompt = (
        f"A South African state-owned enterprise ({soe}) earns R{revenue_bn} billion in annual tariff revenue, "
        f"but requires a R{bailout_bn} billion government bailout from tax funds to stay operational rather than "
        f"reinvesting solely in {infra}.\n\n"
        f"(a) Express the tax bailout as a percentage of annual tariff revenue.\n"
        f"(b) State ONE strategic argument for keeping the SOE state-owned and ONE economic risk of repeated bailouts."
    )
    ans = f"Bailout = {fmt_dec(bailout_pct)}% of revenue; Benefit: protects strategic infrastructure/affordable access; Risk: drains tax funds away from schools/clinics"
    sol = (
        f"**(a) Bailout Percentage:**\n"
        f"- $\\frac{{{bailout_bn}}}{{{revenue_bn}}} \\times 100 = {fmt_dec(bailout_pct)}\\%$\n\n"
        f"**(b) Trade-off Evaluation:**\n"
        f"- **Strategic Argument:** Prevents private monopoly overcharging and maintains vital {infra} in underserved regions.\n"
        f"- **Economic Risk:** Repeated bailouts divert scarce tax revenue away from education, clinics and roads (opportunity cost)."
    )
    return make_question(
        rng=rng,
        subskill="20_sa_state_owned_enterprises_evaluation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate {fmt_dec(bailout_pct)}%", "marks": 2, "type": "A"},
            {"step": "One valid strategic benefit of SOE", "marks": 1, "type": "A"},
            {"step": "One valid fiscal/efficiency risk", "marks": 1, "type": "A"},
        ],
        marking_guide="2 marks for percentage; 1 mark for benefit; 1 mark for fiscal opportunity cost risk.",
        hints={
            "tier_1": "Divide bailout by tariff revenue and multiply by 100.",
            "tier_2": "Consider both national strategic importance and opportunity cost of tax bailouts.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_soe_bailouts_have_zero_opportunity_cost"],
    )


def _build_21_sa_social_grants_redistribution(rng: random.Random, mode: str) -> Dict[str, Any]:
    grants = [
        ("pensioner", 2180, 3, 530),
        ("rural grandmother", 2180, 2, 530),
        ("elderly guardian", 2190, 4, 530),
        ("retired mineworker", 2180, 1, 530),
        ("senior caregiver", 2240, 3, 540),
    ]
    person, old_age, num_children, child_grant = rng.choice(grants)
    total_monthly = old_age + num_children * child_grant
    annual_total = total_monthly * 12
    prompt = (
        f"As part of South Africa's mixed-economy income redistribution, a {person} receives an old-age grant "
        f"of {fmt_zar(old_age)} per month and child support grants of {fmt_zar(child_grant)} per child for {num_children} grandchildren.\n\n"
        f"(a) Calculate the household's total monthly and annual social grant income.\n"
        f"(b) Explain how social grants help South Africa address market-driven inequality."
    )
    ans = f"Monthly: {fmt_zar(total_monthly)}; Annual: {fmt_zar(annual_total)}; grants boost basic purchasing power for food and schooling"
    sol = (
        f"**(a) Grant Income Calculation:**\n"
        f"- Child grants $= {num_children} \\times {fmt_zar(child_grant)} = {fmt_zar(num_children * child_grant)}$\n"
        f"- Monthly total $= {fmt_zar(old_age)} + {fmt_zar(num_children * child_grant)} = {fmt_zar(total_monthly)}$\n"
        f"- Annual total $= {fmt_zar(total_monthly)} \\times 12 = {fmt_zar(annual_total)}$\n\n"
        f"**(b) Redistribution Role:** Financed via progressive taxes, social grants lift vulnerable households out of extreme poverty and stimulate local retail spending."
    )
    return make_question(
        rng=rng,
        subskill="21_sa_social_grants_redistribution",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate monthly total {fmt_zar(total_monthly)}", "marks": 2, "type": "A"},
            {"step": f"Calculate annual total {fmt_zar(annual_total)}", "marks": 1, "type": "CA"},
            {"step": "Explain poverty alleviation & income redistribution", "marks": 2, "type": "A"},
        ],
        marking_guide="3 marks for arithmetic; 2 marks for linking taxes and grants to reducing inequality.",
        hints={
            "tier_1": "Multiply the child grant by the number of children before adding the old-age grant.",
            "tier_2": "Multiply the combined monthly total by 12 months for the annual figure.",
            "tier_3": ans,
        },
        misconception_tags=["forgets_to_multiply_child_grant_by_number_of_children"],
    )


def _build_22_sa_public_vs_private_goods_budget(rng: random.Random, mode: str) -> Dict[str, Any]:
    entities = ["Mixedland", "KwaZulu Coastal Province", "Western Highlands", "Vaal Metro Region", "Highveld Republic"]
    entity = rng.choice(entities)
    public_bn = rng.choice([280, 320, 350, 390, 420])
    private_bn = rng.choice([720, 680, 650, 810, 780])
    total = public_bn + private_bn
    pub_pct = round(public_bn * 100.0 / total, 1)
    diagram = _svg_public_private_bars(entity, public_bn, private_bn)
    prompt = (
        f"Study the annual spending breakdown for **{entity}** (Public Sector Goods: R{public_bn}bn; "
        f"Private Sector Goods: R{private_bn}bn).\n\n"
        f"(a) Verify the percentage share of **Public Sector Goods** out of total R{total} billion spending.\n"
        f"(b) Classify {entity}'s economic system using this evidence and give one example of a good from each sector."
    )
    ans = f"Public share = {fmt_dec(pub_pct)}%; Mixed economy (both sectors active); e.g. public clinics vs private retail shops"
    sol = (
        f"**(a) Public Share:**\n"
        f"- $\\frac{{{public_bn}}}{{{total}}} \\times 100 = {fmt_dec(pub_pct)}\\%$\n\n"
        f"**(b) Classification:** {entity} operates a **mixed economy** because private spending dominates ({fmt_dec(100 - pub_pct)}%, e.g., supermarkets/private banks) alongside substantial public sector provision ({fmt_dec(pub_pct)}%, e.g., public clinics, schools and roads)."
    )
    return make_question(
        rng=rng,
        subskill="22_sa_public_vs_private_goods_budget",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate public share {fmt_dec(pub_pct)}%", "marks": 2, "type": "A"},
            {"step": "Classify as mixed economy with one example per sector", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage calculation; 2 marks for mixed economy classification + examples.",
        hints={
            "tier_1": "Divide Public Sector Goods spending by total spending (R" + str(total) + "bn) times 100.",
            "tier_2": "Presence of both sizable public and private sectors indicates a mixed system.",
            "tier_3": ans,
        },
        misconception_tags=["divides_public_by_private_instead_of_total"],
        diagram_spec=diagram,
    )


def _build_23_classifying_economic_decisions_scenario(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("A central ministry orders every bakery to bake 2 000 brown loaves daily at a fixed state tariff, forbidding private cafés.", "Planned economy", "central state quotas, price control and prohibition of private business"),
        ("Bakery owners freely test gluten-free loaves, raise prices during wheat shortages, and open branches without permits.", "Market economy", "private ownership, price mechanism and unrestricted entrepreneurial freedom"),
        ("Private bakeries compete freely on speciality breads while government enforces hygiene laws and zero-rates VAT on brown bread.", "Mixed economy", "private enterprise operating under state regulation and targeted consumer relief"),
        ("A state commission assigns university graduates directly to state mines with identical pay scales and zero private employers.", "Planned economy", "state direction of labour and absence of private employers"),
        ("Private telecommunications firms compete for customers while an independent state regulator caps excessive roaming fees.", "Mixed economy", "competitive private ownership balanced by consumer protection regulation"),
    ]
    scenario, sys_lbl, reason = rng.choice(cases)
    options = ["Planned economy", "Market economy", "Mixed economy", "Traditional barter economy"]
    prompt = f"Classify the economic decision-making described in this case:\n*{scenario}*"
    sol = f"- **System:** {sys_lbl}.\n- **Justification:** This reflects {reason}."
    return make_question(
        rng=rng,
        subskill="23_classifying_economic_decisions_scenario",
        question_type="mcq",
        prompt=prompt,
        correct_answer=sys_lbl,
        sample_answer=f"{sys_lbl} ({reason})",
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": f"Classify scenario as {sys_lbl}", "marks": 2, "type": "A"}],
        marking_guide="2 marks for correct economic system classification.",
        hints={
            "tier_1": "Check whether private enterprise exists and how strongly the state intervenes.",
            "tier_2": "All state = Planned; all private = Market; private + state rules/relief = Mixed.",
            "tier_3": sys_lbl,
        },
        misconception_tags=["confuses_regulation_with_total_planned_economy"],
        options=options,
        duration_mins=2,
    )


def _build_24_market_failure_and_state_intervention(rng: random.Random, mode: str) -> Dict[str, Any]:
    public_goods = [
        ("township street lighting", "everyone benefits once installed, so private firms cannot charge individual passers-by (free-rider problem)"),
        ("rural flood-warning sirens and dykes", "non-paying residents cannot be excluded from protection, making private billing unviable"),
        ("national border defence and policing", "collective security must cover the entire population rather than only paying subscribers"),
        ("lighthouse beacons along the Cape coast", "every passing vessel uses the beam simultaneously without reducing light for others"),
        ("mass childhood vaccination campaigns in remote districts", "positive community health spillovers are undervalued by pure commercial pricing"),
    ]
    good, why = rng.choice(public_goods)
    prompt = (
        f"Explain why a pure market economy tends to under-provide **{good}**, "
        f"and describe how a mixed economy resolves this market failure."
    )
    ans = f"Private firms cannot earn reliable profits because {why}; government funds and provides it via taxation"
    sol = (
        f"- **Why Pure Markets Under-provide:** {why.capitalize()}, leaving private investors without a viable profit incentive.\n"
        f"- **Mixed-Economy Solution:** The state collects tax revenue and directly funds or supplies {good} for collective social benefit."
    )
    return make_question(
        rng=rng,
        subskill="24_market_failure_and_state_intervention",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": "Explain unprofitability / free-rider / non-excludable nature", "marks": 2, "type": "A"},
            {"step": "State tax-funded government provision", "marks": 1, "type": "A"},
        ],
        marking_guide="2 marks for explaining market failure; 1 mark for public tax-funded solution.",
        hints={
            "tier_1": "Think about whether a private seller can easily stop non-payers from benefiting.",
            "tier_2": "When private profits fail to reflect social value, public funding steps in.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_public_goods_means_goods_sold_in_public_malls"],
    )


def _build_25_economic_spectrum_country_positioning(rng: random.Random, mode: str) -> Dict[str, Any]:
    c1 = rng.choice([("Commandia", 10, "#dc2626"), ("Northland", 14, "#dc2626"), ("Statia", 18, "#dc2626")])
    c2 = rng.choice([("South Africa", 64, "#2563eb"), ("Mzansi", 62, "#2563eb"), ("Mixedland", 58, "#2563eb")])
    c3 = rng.choice([("Marketia", 86, "#059669"), ("Freeland", 88, "#059669"), ("Capita", 84, "#059669")])
    diagram = _svg_spectrum([c1, c2, c3])
    gap = c3[1] - c1[1]
    prompt = (
        f"Inspect the Economic Systems Spectrum plotting private-market share for "
        f"**{c1[0]} ({c1[1]}%)**, **{c2[0]} ({c2[1]}%)**, and **{c3[0]} ({c3[1]}%)**.\n\n"
        f"(a) Identify which plotted economy is closest to a pure planned economy and which is closest to a pure free market.\n"
        f"(b) Calculate the percentage-point difference in market allocation between {c3[0]} and {c1[0]}, and explain {c2[0]}'s position."
    )
    ans = f"Closest to planned: {c1[0]} ({c1[1]}%); Closest to market: {c3[0]} ({c3[1]}%); Difference: {gap} percentage points; {c2[0]} ({c2[1]}%) is a mixed economy"
    sol = (
        f"**(a) Spectrum Endpoints:**\n"
        f"- Closest to Pure Planned (0% market): **{c1[0]}** at {c1[1]}% market (86–90% state control).\n"
        f"- Closest to Pure Market (100% market): **{c3[0]}** at {c3[1]}% market.\n\n"
        f"**(b) Comparison:**\n"
        f"- Difference $= {c3[1]}\\% - {c1[1]}\\% = {gap}$ percentage points.\n"
        f"- **{c2[0]} ({c2[1]}%)** sits between the extremes as a **mixed economy**, combining substantial private enterprise with meaningful public services and regulation."
    )
    return make_question(
        rng=rng,
        subskill="25_economic_spectrum_country_positioning",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Identify {c1[0]} near planned and {c3[0]} near market", "marks": 2, "type": "A"},
            {"step": f"Compute difference {gap} percentage points", "marks": 1, "type": "A"},
            {"step": f"Classify {c2[0]} as mixed economy blending state + private", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for endpoint identifications; 1 mark for gap calculation; 2 marks for explaining middle position.",
        hints={
            "tier_1": "Left (0%) represents pure state command; right (100%) represents pure private markets.",
            "tier_2": f"Subtract {c1[1]}% from {c3[1]}% and interpret the middle marker near 60%.",
            "tier_3": ans,
        },
        misconception_tags=["reads_higher_percentage_as_stronger_central_planning"],
        diagram_spec=diagram,
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_basic_economic_problem_scarcity": _build_01_basic_economic_problem_scarcity,
    "02_defining_economic_system": _build_02_defining_economic_system,
    "03_planned_economy_origin_command": _build_03_planned_economy_origin_command,
    "04_planned_economy_ownership_control": _build_04_planned_economy_ownership_control,
    "05_planned_economy_advantages": _build_05_planned_economy_advantages,
    "06_planned_economy_disadvantages": _build_06_planned_economy_disadvantages,
    "07_iron_rice_bowl_incentive_analysis": _build_07_iron_rice_bowl_incentive_analysis,
    "08_market_economy_origin_capitalism": _build_08_market_economy_origin_capitalism,
    "09_market_economy_price_mechanism": _build_09_market_economy_price_mechanism,
    "10_market_economy_characteristics": _build_10_market_economy_characteristics,
    "11_market_economy_advantages": _build_11_market_economy_advantages,
    "12_market_economy_disadvantages": _build_12_market_economy_disadvantages,
    "13_mixed_economy_definition_origin": _build_13_mixed_economy_definition_origin,
    "14_mixed_economy_government_role": _build_14_mixed_economy_government_role,
    "15_mixed_economy_advantages": _build_15_mixed_economy_advantages,
    "16_mixed_economy_disadvantages": _build_16_mixed_economy_disadvantages,
    "17_compare_systems_ownership_matrix": _build_17_compare_systems_ownership_matrix,
    "18_compare_systems_allocation_questions": _build_18_compare_systems_allocation_questions,
    "19_sa_mixed_economy_private_public": _build_19_sa_mixed_economy_private_public,
    "20_sa_state_owned_enterprises_evaluation": _build_20_sa_state_owned_enterprises_evaluation,
    "21_sa_social_grants_redistribution": _build_21_sa_social_grants_redistribution,
    "22_sa_public_vs_private_goods_budget": _build_22_sa_public_vs_private_goods_budget,
    "23_classifying_economic_decisions_scenario": _build_23_classifying_economic_decisions_scenario,
    "24_market_failure_and_state_intervention": _build_24_market_failure_and_state_intervention,
    "25_economic_spectrum_country_positioning": _build_25_economic_spectrum_country_positioning,
}
