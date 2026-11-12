"""Grade 9 EMS Term 2: Sectors of the Economy — Semantic Archetypes 01 to 25."""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional


TOPIC_NAME = "Sectors of the economy"
SUBTOPIC_ID = "term2_sectors_of_economy"


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
    """Assemble standardized 6-pillar Grade 9 EMS Sectors question payload."""
    qid = f"gr9_ems_t2_sec_{subskill}_{rng.randint(100000, 999999)}"
    payload: Dict[str, Any] = {
        "id": qid,
        "topic": TOPIC_NAME,
        "subtopic": SUBTOPIC_ID,
        "subskill": subskill,
        "question_family_id": f"ems_gr9_t2_sectors_of_economy_{subskill}",
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


def svg_value_chain(
    title: str,
    s1_name: str,
    s1_desc: str,
    p1: float,
    s2_name: str,
    s2_desc: str,
    p2: float,
    s3_name: str,
    s3_desc: str,
    p3: float,
) -> Dict[str, Any]:
    """Render parameterized SVG 3-stage Primary -> Secondary -> Tertiary value chain."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 220" width="100%" height="auto">'
        '<defs>'
        '<marker id="arrChain" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,1 L7,4 L0,7 Z" fill="#0f172a"/></marker>'
        '</defs>'
        '<rect x="0" y="0" width="650" height="220" fill="#ffffff" rx="8"/>'
        f'<text x="325" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{title}</text>'
        # Stage 1 Primary
        '<rect x="24" y="58" width="174" height="106" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="111" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">1. PRIMARY SECTOR</text>'
        f'<text x="111" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">{s1_name}</text>'
        f'<text x="111" y="122" text-anchor="middle" font-size="10" fill="#475569">{s1_desc}</text>'
        f'<text x="111" y="148" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">Sale: {fmt_zar(p1)}</text>'
        # Stage 2 Secondary
        '<rect x="238" y="58" width="174" height="106" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="325" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">2. SECONDARY SECTOR</text>'
        f'<text x="325" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">{s2_name}</text>'
        f'<text x="325" y="122" text-anchor="middle" font-size="10" fill="#475569">{s2_desc}</text>'
        f'<text x="325" y="148" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8">Sale: {fmt_zar(p2)}</text>'
        # Stage 3 Tertiary
        '<rect x="452" y="58" width="174" height="106" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="2"/>'
        '<text x="539" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#065f46">3. TERTIARY SECTOR</text>'
        f'<text x="539" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">{s3_name}</text>'
        f'<text x="539" y="122" text-anchor="middle" font-size="10" fill="#475569">{s3_desc}</text>'
        f'<text x="539" y="148" text-anchor="middle" font-size="12" font-weight="700" fill="#047857">Retail: {fmt_zar(p3)}</text>'
        # Arrows
        '<line x1="198" y1="111" x2="235" y2="111" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arrChain)"/>'
        '<line x1="412" y1="111" x2="449" y2="111" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arrChain)"/>'
        '<text x="325" y="194" text-anchor="middle" font-size="11" fill="#475569">'
        'Each downstream sector adds processing or distribution value onto upstream inputs.</text>'
        '</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _build_01_three_economic_sectors_overview(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("extracting raw copper ore, smelting electrical copper wire in a factory, and retailing hardware switches at a shop", "Primary (extraction), Secondary (manufacturing), and Tertiary (retail distribution/services)"),
        ("growing sugar cane on a KwaZulu-Natal farm, refining brown sugar at a mill, and delivering packets to supermarkets", "Primary (farming), Secondary (refining/processing), and Tertiary (transport and retail)"),
        ("catching hake off Saldanha Bay, canning fish fillets at a plant, and serving fish meals in a restaurant", "Primary (fishing), Secondary (food processing), and Tertiary (hospitality service)"),
    ]
    chain, correct = rng.choice(cases)
    distractors = [
        "Households, Businesses and Foreign Embassies only",
        "Monetary policy, Fiscal policy and International Tariffs",
        "Command economy, Barter system and Informal banking",
    ]
    prompt = f"Which sequence correctly matches the **three economic sectors** shown in *{chain}*?"
    sol = f"- **Three Sectors:** {correct}."
    return make_question(
        rng=rng,
        subskill="01_three_economic_sectors_overview",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct,
        sample_answer=correct,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Match stages to Primary, Secondary and Tertiary sectors", "marks": 2, "type": "A"}],
        marking_guide="2 marks for correct 3-sector sequence.",
        hints={
            "tier_1": "Start with nature, move to factory processing, end with distribution/services.",
            "tier_2": "Primary = raw extraction; Secondary = manufacturing; Tertiary = services/retail.",
            "tier_3": correct,
        },
        misconception_tags=["confuses_three_sectors_with_circular_flow_participants"],
        options=[correct] + distractors,
        duration_mins=2,
    )


def _build_02_primary_sector_definition_industries(rng: random.Random, mode: str) -> Dict[str, Any]:
    examples = [
        ("Rustenburg platinum mining, Free State maize farming, Knysna commercial forestry, and West Coast pelagic fishing", "extracting or harvesting raw natural resources directly from nature"),
        ("Northern Cape iron-ore quarrying, Limpopo avocado orchards, and Mpumalanga pine plantations", "producing raw agricultural, mineral, timber and marine commodities directly from the earth"),
        ("coal extraction in Emalahleni, sugarcane cultivation, and deep-sea hake trawling", "obtaining unprocessed raw materials straight from natural resources"),
    ]
    list_ex, core = rng.choice(examples)
    prompt = (
        f"South African industries such as {list_ex} all operate in the **Primary sector**.\n\n"
        f"(a) Define the **Primary sector**.\n"
        f"(b) Identify the FOUR main primary industry groups operating in South Africa."
    )
    ans = f"Sector focused on {core}; Four groups: agriculture (farming), mining, forestry, and fishing"
    sol = (
        f"**(a) Definition:** The Primary sector focuses on **{core}**.\n"
        f"**(b) Four Main Industries:** **Agriculture (farming), Mining, Forestry, and Fishing**."
    )
    return make_question(
        rng=rng,
        subskill="02_primary_sector_definition_industries",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define primary sector as extracting raw natural resources", "marks": 2, "type": "A"},
            {"step": "List farming, mining, forestry and fishing", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for definition; 2 marks for all four South African primary sub-sectors.",
        hints={
            "tier_1": "Think of raw materials harvested straight from land, forest, sea or underground.",
            "tier_2": "Include agriculture, mining, forestry and fishing.",
            "tier_3": ans,
        },
        misconception_tags=["includes_factory_smelting_inside_primary_sector"],
    )


def _build_03_secondary_sector_definition_industries(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("converting raw iron ore and coal into sheet steel and assembling motor vehicles", "manufacturing, processing and construction that transform raw materials into finished or semi-finished goods"),
        ("milling wheat into flour, canning peaches, spinning wool into yarn, and building brick houses", "adding physical value by turning raw inputs into consumer or capital products"),
        ("refining crude oil into diesel/plastics, bottling fruit juices, and constructing bridges", "industrial production, food processing, assembly and civil construction"),
    ]
    examples, desc = rng.choice(cases)
    distractors = [
        "harvesting wild fish straight from the Atlantic Ocean without processing",
        "operating commercial bank branches, tourism guesthouses and primary schools",
        "extracting raw underground gold reef before any crushing or refining",
    ]
    prompt = f"Which description defines the **Secondary sector**, as illustrated by *{examples}*?"
    sol = f"- **Secondary Sector:** {desc.capitalize()}."
    return make_question(
        rng=rng,
        subskill="03_secondary_sector_definition_industries",
        question_type="mcq",
        prompt=prompt,
        correct_answer=desc.capitalize(),
        sample_answer=desc.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify secondary sector manufacturing/processing/construction", "marks": 2, "type": "A"}],
        marking_guide="2 marks for processing/manufacturing/construction definition.",
        hints={
            "tier_1": "Notice raw resources are transformed or assembled into new products.",
            "tier_2": "Manufacturing, processing and construction all belong to the Secondary sector.",
            "tier_3": desc.capitalize(),
        },
        misconception_tags=["classifies_house_construction_as_tertiary"],
        options=[desc.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


def _build_04_tertiary_sector_definition_services(rng: random.Random, mode: str) -> Dict[str, Any]:
    bundles = [
        ("Checkers supermarkets, Transnet freight logistics, FNB banking, and Cape Town hotels", "wholesale/retail distribution and commercial, financial, transport and hospitality services"),
        ("medical clinics, public high schools, insurance brokers, and cellphone networks", "delivering intangible professional, public, communications and personal services plus product distribution"),
        ("courier vans, accounting practices, tourism tour guides, and hardware retailers", "providing commercial and personal services and moving finished goods to final consumers"),
    ]
    ex, desc = rng.choice(bundles)
    prompt = (
        f"Explain why enterprises such as {ex} belong to the **Tertiary sector**, "
        f"and explain how the tertiary sector supports both primary and secondary firms."
    )
    ans = f"They provide {desc} rather than extracting or manufacturing physical goods; they transport inputs, provide finance/insurance and retail finished goods"
    sol = (
        f"- **Tertiary Definition:** Focuses on **{desc}** instead of extracting raw materials or manufacturing physical products.\n"
        f"- **Support Role:** Provides transport, banking credit, insurance, marketing and retail outlets needed by farms, mines and factories."
    )
    return make_question(
        rng=rng,
        subskill="04_tertiary_sector_definition_services",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Define tertiary sector as services & distribution", "marks": 2, "type": "A"},
            {"step": "Explain transport/finance/retail support to Primary & Secondary", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for definition; 2 marks for support services link.",
        hints={
            "tier_1": "Ask whether these firms sell physical raw ore, manufactured goods, or services/distribution.",
            "tier_2": "Retail, transport, banking, healthcare and education are tertiary.",
            "tier_3": ans,
        },
        misconception_tags=["places_supermarket_retailing_in_secondary_sector"],
    )


def _build_05_classifying_sa_businesses_into_sectors(rng: random.Random, mode: str) -> Dict[str, Any]:
    bank = [
        ("Limpopo Citrus Orchard (harvests fresh oranges)", "Primary", "Raw agricultural produce"),
        ("Uitenhage Vehicle Assembly Plant (builds bakkies)", "Secondary", "Manufactured cars"),
        ("Durban Harbour Container Logistics (ships freight)", "Tertiary", "Transport service"),
        ("Mpumalanga Sawmill & Furniture Factory (crafts desks)", "Secondary", "Processed wooden goods"),
        ("Pretoria Commercial Bank Branch (grants business loans)", "Tertiary", "Financial service"),
        ("Northern Cape Manganese Mine (extracts ore)", "Primary", "Raw mineral ore"),
    ]
    picked = rng.sample(bank, 3)
    headers = ["South African Enterprise", "Economic Sector", "Main Output Category"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| South African Enterprise | Economic Sector | Main Output Category |", "|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_cols = rng.sample([1, 2], 1 if r_idx == 2 else 2)
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx in req_cols
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Classify as Primary (raw extraction), Secondary (manufacturing), or Tertiary (services)."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="05_classifying_sa_businesses_into_sectors",
        question_type="table_completion",
        prompt="Classify each South African enterprise by Economic Sector (Primary, Secondary, or Tertiary) and Output Category.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Sector Classification Matrix:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark for each correct sector or output classification.",
        hints={
            "tier_1": "Check whether the firm extracts raw nature, processes goods, or delivers services.",
            "tier_2": "Assembly/furniture = Secondary; transport/banking = Tertiary; orchards/mines = Primary.",
            "tier_3": md_table,
        },
        misconception_tags=["places_mining_company_offices_confusion_over_core_activity"],
        table_payload={
            "headers": headers,
            "columns": [{"key": "biz", "label": headers[0]}, {"key": "sec", "label": headers[1]}, {"key": "out", "label": headers[2]}],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_06_agriculture_mining_forestry_fishing_examples(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("Mpumalanga pine plantations harvesting 4 200 tonnes of raw logs at R950/tonne", "Forestry (Primary)", 4200 * 950),
        ("Gansbaai trawlers landing 180 tonnes of fresh hake at R18 000/tonne", "Fishing (Primary)", 180 * 18000),
        ("Free State farms harvesting 650 tonnes of yellow maize at R4 200/tonne", "Agriculture (Primary)", 650 * 4200),
        ("Northern Cape mines extracting 500 tonnes of iron ore at R1 600/tonne", "Mining (Primary)", 500 * 1600),
    ]
    desc, sub_sec, rev = rng.choice(cases)
    prompt = (
        f"Examine this primary-sector activity: *{desc}.*\n\n"
        f"(a) Identify the specific **Primary sub-sector**.\n"
        f"(b) Calculate the total gross output value in Rand."
    )
    ans = f"{sub_sec}; Gross output value = {fmt_zar(rev)}"
    sol = (
        f"**(a) Sub-sector:** **{sub_sec}**.\n"
        f"**(b) Gross Value:** Output = **{fmt_zar(rev)}**."
    )
    return make_question(
        rng=rng,
        subskill="06_agriculture_mining_forestry_fishing_examples",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": f"Identify {sub_sec}", "marks": 1, "type": "A"},
            {"step": f"Calculate gross value {fmt_zar(rev)}", "marks": 2, "type": "A"},
        ],
        marking_guide="1 mark for sub-sector; 2 marks for Rand multiplication.",
        hints={
            "tier_1": "Name which of the four primary industries (agriculture, mining, forestry, fishing) applies.",
            "tier_2": "Multiply tonnes by Rand price per tonne.",
            "tier_3": ans,
        },
        misconception_tags=["omits_zeros_when_multiplying_tonnes_by_price"],
    )


def _build_07_construction_and_manufacturing_subsectors(rng: random.Random, mode: str) -> Dict[str, Any]:
    units = rng.choice([40, 50, 60, 80])
    brick_cost = rng.choice([12000, 15000, 18000])
    cement_roof = rng.choice([25000, 30000, 35000])
    unit_sale = brick_cost + cement_roof + rng.choice([20000, 25000])
    tot_val = units * unit_sale
    prompt = (
        f"A construction contractor builds {units} RDP starter houses. Per house, it transforms raw bricks ({fmt_zar(brick_cost)}) "
        f"and cement/roofing materials ({fmt_zar(cement_roof)}) into a completed home valued at {fmt_zar(unit_sale)}.\n\n"
        f"(a) Explain why house **construction** belongs to the **Secondary sector** rather than Primary or Tertiary.\n"
        f"(b) Calculate the total value of completed houses built."
    )
    ans = f"Construction transforms raw/processed inputs (bricks, cement, timber) into physical capital structures; Total = {fmt_zar(tot_val)}"
    sol = (
        f"**(a) Why Secondary Sector:** Construction combines and transforms raw/semi-processed materials (clay bricks, cement, steel, timber) into finished physical structures—a core **Secondary** activity.\n"
        f"**(b) Total Value:** ${units} \\times {fmt_zar(unit_sale)} = {fmt_zar(tot_val)}$"
    )
    return make_question(
        rng=rng,
        subskill="07_construction_and_manufacturing_subsectors",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain transformation of inputs into physical structures", "marks": 2, "type": "A"},
            {"step": f"Calculate total value {fmt_zar(tot_val)}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for explaining why construction is Secondary; 2 marks for value calculation.",
        hints={
            "tier_1": "Ask whether building a house creates a tangible structure from raw/processed materials.",
            "tier_2": f"Multiply {units} houses by selling value per house.",
            "tier_3": ans,
        },
        misconception_tags=["classifies_civil_construction_as_tertiary_service"],
    )


def _build_08_commerce_transport_finance_and_public_services(rng: random.Random, mode: str) -> Dict[str, Any]:
    loads = rng.choice([25, 30, 40])
    fee_per_load = rng.choice([4200, 4800, 5500])
    total_fee = loads * fee_per_load
    prompt = (
        f"A freight logistics carrier hauls {loads} refrigerated truckloads of apples from Grabouw packhouses to Cape Town harbour at {fmt_zar(fee_per_load)} per trip.\n\n"
        f"(a) Classify the freight company into its economic sector.\n"
        f"(b) Calculate total transport revenue earned and name ONE other Tertiary service supporting the apple export."
    )
    ans = f"Tertiary sector; Revenue = {fmt_zar(total_fee)}; Other tertiary service: marine insurance, commercial banking/forex, or export brokerage"
    sol = (
        f"**(a) Sector:** **Tertiary sector** (transport & distribution service—it does not grow the apples nor process them).\n"
        f"**(b) Revenue & Companion Services:**\n"
        f"- Transport revenue $= {loads} \\times {fmt_zar(fee_per_load)} = {fmt_zar(total_fee)}$\n"
        f"- Companion tertiary services: cargo insurance, commercial banking/foreign exchange, harbour cold-storage or retail marketing."
    )
    return make_question(
        rng=rng,
        subskill="08_commerce_transport_finance_and_public_services",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Classify haulage as Tertiary sector", "marks": 1, "type": "A"},
            {"step": f"Calculate revenue {fmt_zar(total_fee)}", "marks": 2, "type": "A"},
            {"step": "Name one companion tertiary service", "marks": 1, "type": "A"},
        ],
        marking_guide="1 mark for Tertiary; 2 marks for calculation; 1 mark for companion service.",
        hints={
            "tier_1": "Transporting agricultural produce without growing or canning it is a service.",
            "tier_2": f"Multiply {loads} loads by {fmt_zar(fee_per_load)}.",
            "tier_3": ans,
        },
        misconception_tags=["puts_farm_trucking_into_primary_sector_just_because_cargo_is_apples"],
    )


def _build_09_bokomo_wheat_to_retail_value_chain_svg(rng: random.Random, mode: str) -> Dict[str, Any]:
    p1 = rng.choice([5.0, 5.5, 6.0])
    p2 = rng.choice([12.0, 12.5, 13.0])
    p3 = rng.choice([17.5, 18.0, 19.0])
    va2 = round(p2 - p1, 2)
    va3 = round(p3 - p2, 2)
    diagram = svg_value_chain(
        "South African Bread Value Chain (Per Loaf)",
        "Wheat Farmer",
        "Harvests raw wheat grain",
        p1,
        "Mill & Bakery",
        "Mills flour & bakes loaf",
        p2,
        "Supermarket",
        "Transports & retails bread",
        p3,
    )
    prompt = (
        f"Study the Three-Sector Bread Value Chain (Farmer sells wheat at {fmt_zar(p1)}; Mill/Bakery sells baked loaf at {fmt_zar(p2)}; "
        f"Supermarket retails loaf to household at {fmt_zar(p3)}).\n\n"
        f"(a) Calculate the **value added** by the Secondary Sector (Mill & Bakery) and by the Tertiary Sector (Supermarket).\n"
        f"(b) Explain why **value added** equals total final price (`{fmt_zar(p1)} + {fmt_zar(va2)} + {fmt_zar(va3)} = {fmt_zar(p3)}`)."
    )
    ans = f"Secondary value added = {fmt_zar(va2)}; Tertiary value added = {fmt_zar(va3)}; summing value added avoids double-counting raw wheat and flour"
    sol = (
        f"**(a) Value Added per Stage:**\n"
        f"- Primary (Farmer): {fmt_zar(p1)}\n"
        f"- **Secondary (Mill & Bakery):** ${fmt_zar(p2)} - {fmt_zar(p1)} = {fmt_zar(va2)}$\n"
        f"- **Tertiary (Supermarket):** ${fmt_zar(p3)} - {fmt_zar(p2)} = {fmt_zar(va3)}$\n\n"
        f"**(b) No Double-Counting:** Summing stage value added (${fmt_zar(p1)} + {fmt_zar(va2)} + {fmt_zar(va3)} = {fmt_zar(p3)}$) equals the final retail price because intermediate inputs are counted once."
    )
    return make_question(
        rng=rng,
        subskill="09_bokomo_wheat_to_retail_value_chain_svg",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Secondary value added {fmt_zar(va2)} and Tertiary {fmt_zar(va3)}", "marks": 2, "type": "A"},
            {"step": "Explain sum of value added equals retail price without double-counting", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for both subtractions; 2 marks for value-added explanation.",
        hints={
            "tier_1": "Value added at each stage = Selling price minus Input purchase price.",
            "tier_2": "Verify that Stage 1 + Stage 2 VA + Stage 3 VA equals final shelf price.",
            "tier_3": ans,
        },
        misconception_tags=["sums_gross_sales_of_all_three_stages_instead_of_value_added"],
        diagram_spec=diagram,
    )


def _build_10_timber_to_school_desk_production_chain(rng: random.Random, mode: str) -> Dict[str, Any]:
    p1 = rng.choice([180, 210, 240])
    p2 = p1 + rng.choice([320, 360, 400])
    p3 = p2 + rng.choice([150, 180, 210])
    va2 = p2 - p1
    va3 = p3 - p2
    diagram = svg_value_chain(
        "Timber-to-School-Desk Production Chain",
        "Pine Plantation",
        "Fells raw timber logs",
        p1,
        "Furniture Factory",
        "Planes & bolts wooden desks",
        p2,
        "Education Supplier",
        "Delivers & wholesales to schools",
        p3,
    )
    prompt = (
        f"Trace a classroom desk across the three sectors: Plantation sells timber logs at {fmt_zar(p1)}, "
        f"Factory sells finished desks at {fmt_zar(p2)}, and Supplier delivers to schools at {fmt_zar(p3)}.\n\n"
        f"(a) Identify which stage transforms timber into furniture.\n"
        f"(b) Calculate the value added in the Secondary and Tertiary stages."
    )
    ans = f"Secondary sector (Furniture Factory); Secondary value added = {fmt_zar(va2)}; Tertiary value added = {fmt_zar(va3)}"
    sol = (
        f"**(a) Transformation Stage:** **Secondary sector** (Furniture Factory turning raw logs into finished desks).\n"
        f"**(b) Value Added:**\n"
        f"- Secondary: ${fmt_zar(p2)} - {fmt_zar(p1)} = {fmt_zar(va2)}$\n"
        f"- Tertiary: ${fmt_zar(p3)} - {fmt_zar(p2)} = {fmt_zar(va3)}$"
    )
    return make_question(
        rng=rng,
        subskill="10_timber_to_school_desk_production_chain",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Identify Secondary sector", "marks": 1, "type": "A"},
            {"step": f"Calculate {fmt_zar(va2)} and {fmt_zar(va3)}", "marks": 3, "type": "A"},
        ],
        marking_guide="1 mark for Secondary; 3 marks for value-added subtractions.",
        hints={
            "tier_1": "Processing raw timber into furniture is Secondary.",
            "tier_2": "Subtract upstream input price from stage selling price.",
            "tier_3": ans,
        },
        misconception_tags=["treats_sawmill_furniture_making_as_forestry"],
        diagram_spec=diagram,
    )


def _build_11_iron_ore_to_motor_vehicle_chain(rng: random.Random, mode: str) -> Dict[str, Any]:
    p1 = rng.choice([24000, 28000, 32000])
    p2 = rng.choice([290000, 320000, 350000])
    p3 = p2 + rng.choice([45000, 55000, 65000])
    va2 = p2 - p1
    diagram = svg_value_chain(
        "Automotive Production & Dealership Chain",
        "Iron Ore Mine",
        "Extracts iron ore & platinum",
        p1,
        "Steel & Auto Plant",
        "Smelts steel & assembles car",
        p2,
        "Auto Dealership",
        "Retails, insures & finances car",
        p3,
    )
    prompt = (
        f"Study the Automotive Value Chain (Raw mined ore share {fmt_zar(p1)}, Assembled factory car {fmt_zar(p2)}, Dealership retail price {fmt_zar(p3)}).\n\n"
        f"(a) Calculate the Secondary manufacturing value added per vehicle (`{fmt_zar(p2)} - {fmt_zar(p1)}`).\n"
        f"(b) List TWO Tertiary services provided by the dealership and financial partners."
    )
    ans = f"Secondary value added = {fmt_zar(va2)}; Tertiary services: retail showroom sales, vehicle financing/credit, car insurance, or after-sales servicing"
    sol = (
        f"**(a) Manufacturing Value Added:** ${fmt_zar(p2)} - {fmt_zar(p1)} = {fmt_zar(va2)}$\n"
        f"**(b) Tertiary Services:** Retail sales assistance, bank vehicle finance, comprehensive motor insurance, and routine maintenance servicing."
    )
    return make_question(
        rng=rng,
        subskill="11_iron_ore_to_motor_vehicle_chain",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate manufacturing value added {fmt_zar(va2)}", "marks": 2, "type": "A"},
            {"step": "List two tertiary automotive services", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for subtraction; 2 marks for two distinct tertiary services.",
        hints={
            "tier_1": "Subtract raw ore input value from assembled factory value.",
            "tier_2": "Think of what a car dealership, bank and insurer add after manufacturing.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_car_dealership_with_secondary_sector"],
        diagram_spec=diagram,
    )


def _build_12_cotton_to_clothing_retail_chain(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("harvesting raw cotton bolls in KwaZulu-Natal", "spinning cotton yarn & sewing school shirts in Cape Town", "delivering & merchandising shirts at retail outlets nationwide"),
        ("shearing merino wool clips in the Karoo", "weaving woollen blankets at a textile mill", "export logistics & department-store retailing"),
        ("growing hemp & flax fibre crops", "dyeing & stitching canvas backpacks at a factory", "e-commerce order fulfilment & courier delivery"),
    ]
    p_act, s_act, t_act = rng.choice(cases)
    prompt = (
        f"Classify each textile activity into Primary, Secondary, or Tertiary and explain the flow connecting them:\n"
        f"- Activity X: *{p_act}*\n"
        f"- Activity Y: *{s_act}*\n"
        f"- Activity Z: *{t_act}*"
    )
    ans = "X = Primary (raw fibre extraction); Y = Secondary (manufacturing textiles/garments); Z = Tertiary (logistics & retail service)"
    sol = (
        f"- **Activity X (Primary):** {p_act.capitalize()} produces raw natural fibre.\n"
        f"- **Activity Y (Secondary):** {s_act.capitalize()} manufactures finished wearable goods.\n"
        f"- **Activity Z (Tertiary):** {t_act.capitalize()} distributes and sells finished garments to households."
    )
    return make_question(
        rng=rng,
        subskill="12_cotton_to_clothing_retail_chain",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[{"step": "Classify X=Primary, Y=Secondary, Z=Tertiary (1 mark each)", "marks": 3, "type": "A"}],
        marking_guide="1 mark for each correct sector classification.",
        hints={
            "tier_1": "Follow the chain from raw crop/wool -> factory stitching -> retail delivery.",
            "tier_2": "X=Primary, Y=Secondary, Z=Tertiary.",
            "tier_3": ans,
        },
        misconception_tags=["places_textile_mill_into_primary_sector"],
    )


def _build_13_sectoral_value_added_percentage_calc(rng: random.Random, mode: str) -> Dict[str, Any]:
    p1 = rng.choice([20, 25, 30])
    p2 = rng.choice([70, 75, 80])
    p3 = 100
    va1 = p1
    va2 = p2 - p1
    va3 = p3 - p2
    max_stage = "Secondary" if va2 >= max(va1, va3) else ("Primary" if va1 >= va3 else "Tertiary")
    pct_s2 = round(va2 * 100.0 / p3, 1)
    prompt = (
        f"Along a canned-fruit value chain sold at retail for **R{p3}** per crate:\n"
        f"- Primary orchard supplies raw peaches at **R{p1}**.\n"
        f"- Secondary cannery processes and cans the fruit, selling crates at **R{p2}**.\n"
        f"- Tertiary distributor & supermarket retail the crate at **R{p3}**.\n\n"
        f"(a) Calculate the percentage of the final R{p3} price added by the **Secondary** sector.\n"
        f"(b) Identify which sector adds the **largest Rand value** to the final product."
    )
    ans = f"Secondary share = {fmt_dec(pct_s2)}% (R{va2}); Largest contributor: {max_stage} sector"
    sol = (
        f"**(a) Secondary Value Added:**\n"
        f"- Value added $= \\text{{R}}{p2} - \\text{{R}}{p1} = \\text{{R}}{va2}$\n"
        f"- Percentage $= \\frac{{{va2}}}{{{p3}}} \\times 100 = {fmt_dec(pct_s2)}\\%$\n\n"
        f"**(b) Largest Contributor:** Primary adds R{va1}, Secondary adds R{va2}, Tertiary adds R{va3} $\\implies$ **{max_stage} sector**."
    )
    return make_question(
        rng=rng,
        subskill="13_sectoral_value_added_percentage_calc",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate Secondary VA R{va2} and {fmt_dec(pct_s2)}%", "marks": 2, "type": "A"},
            {"step": f"Compare stages and identify {max_stage}", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Secondary VA %; 2 marks for stage comparison.",
        hints={
            "tier_1": f"First subtract R{p1} from R{p2}, then express over final R{p3}.",
            "tier_2": "Compute value added for all three stages before comparing sizes.",
            "tier_3": ans,
        },
        misconception_tags=["uses_gross_p2_70_percent_instead_of_value_added"],
    )


def _build_14_interdependence_primary_relies_on_secondary_tertiary(rng: random.Random, mode: str) -> Dict[str, Any]:
    machinery = rng.choice([120000, 150000, 180000])
    fert = rng.choice([45000, 60000, 75000])
    haulage = rng.choice([30000, 40000])
    insur = rng.choice([18000, 24000])
    sec_tot = machinery + fert
    ter_tot = haulage + insur
    prompt = (
        f"A commercial Limpopo vegetable farm incurs monthly operational inputs from other sectors:\n"
        f"- Tractor spare parts & manufactured fertiliser: {fmt_zar(machinery)} + {fmt_zar(fert)}\n"
        f"- Refrigerated courier haulage & crop insurance: {fmt_zar(haulage)} + {fmt_zar(insur)}\n\n"
        f"(a) Calculate how much the farm spends on **Secondary** inputs versus **Tertiary** services.\n"
        f"(b) Explain why a primary farm cannot function independently of the other two sectors."
    )
    ans = f"Secondary inputs = {fmt_zar(sec_tot)}; Tertiary services = {fmt_zar(ter_tot)}; farms rely on factories for machinery/fertiliser and services for transport/finance/retail"
    sol = (
        f"**(a) Sectoral Input Totals:**\n"
        f"- **Secondary inputs** (parts + fertiliser) $= {fmt_zar(machinery)} + {fmt_zar(fert)} = {fmt_zar(sec_tot)}$\n"
        f"- **Tertiary services** (haulage + insurance) $= {fmt_zar(haulage)} + {fmt_zar(insur)} = {fmt_zar(ter_tot)}$\n\n"
        f"**(b) Interdependence:** Primary producers rely on Secondary industries for tractors, tools and chemicals, and on Tertiary services for cold-chain logistics, credit and retail distribution."
    )
    return make_question(
        rng=rng,
        subskill="14_interdependence_primary_relies_on_secondary_tertiary",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Sum Secondary {fmt_zar(sec_tot)} and Tertiary {fmt_zar(ter_tot)}", "marks": 2, "type": "A"},
            {"step": "Explain primary farm reliance on Secondary + Tertiary", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for both sums; 2 marks for interdependence explanation.",
        hints={
            "tier_1": "Group manufactured physical inputs (Secondary) separately from transport/insurance (Tertiary).",
            "tier_2": "Explain what happens to crops without tractors, fertiliser, trucks or insurance.",
            "tier_3": ans,
        },
        misconception_tags=["mixes_fertiliser_with_tertiary_services"],
    )


def _build_15_interdependence_secondary_relies_on_primary_tertiary(rng: random.Random, mode: str) -> Dict[str, Any]:
    plants = [
        ("a Johannesburg cannery", "fresh tomatoes from Limpopo farms (Primary)", "steel cans & cardboard boxes", "wholesale distribution, warehousing and banking (Tertiary)"),
        ("a Durban paper mill", "raw eucalyptus timber from Zululand plantations (Primary)", "newsprint rolls & packaging cartons", "port logistics, commercial finance and insurance (Tertiary)"),
        ("a Vereeniging steel foundry", "iron ore and coking coal from mines (Primary)", "construction beams & fencing wire", "freight rail transport and engineering consultancy (Tertiary)"),
    ]
    plant, prim_in, out_good, tert_svc = rng.choice(plants)
    prompt = (
        f"Explain how **{plant}** producing {out_good} sits in the middle of sectoral interdependence, relying on:\n"
        f"1. The **Primary sector** (e.g. {prim_in}), and\n"
        f"2. The **Tertiary sector** (e.g. {tert_svc})."
    )
    ans = f"Secondary factories need Primary raw inputs ({prim_in}) to process into {out_good}, and Tertiary services ({tert_svc}) to finance, insure and distribute finished output"
    sol = (
        f"- **Primary Dependency:** Without {prim_in}, {plant} lacks raw feedstock to process into {out_good}.\n"
        f"- **Tertiary Dependency:** Without {tert_svc}, the factory cannot finance capital, insure operations, or transport and sell finished goods to customers."
    )
    return make_question(
        rng=rng,
        subskill="15_interdependence_secondary_relies_on_primary_tertiary",
        question_type="structured",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Explain reliance on Primary raw materials", "marks": 2, "type": "A"},
            {"step": "Explain reliance on Tertiary logistics/finance/retail", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for Primary dependency; 2 marks for Tertiary dependency.",
        hints={
            "tier_1": "Identify what enters the factory (raw) vs what moves/finances its output.",
            "tier_2": "Cover both upstream raw inputs and downstream services.",
            "tier_3": ans,
        },
        misconception_tags=["assumes_factories_can_manufacture_without_raw_commodities"],
    )


def _build_16_interdependence_tertiary_relies_on_primary_secondary(rng: random.Random, mode: str) -> Dict[str, Any]:
    cases = [
        ("A supermarket chain", "fresh apples, eggs and milk (Primary)", "tinned food, soap, refrigerators and cash registers (Secondary)"),
        ("A national passenger airline", "aviation fuel refined from crude oil/coal (Primary/Secondary)", "manufactured aircraft, passenger seats and tarmac runways (Secondary)"),
        ("A dental clinic", "raw minerals/precious metals used in instruments (Primary)", "sterile chairs, X-ray machines, gloves and computers (Secondary)"),
    ]
    tert_biz, prim_need, sec_need = rng.choice(cases)
    distractors = [
        "Tertiary businesses create apples, aircraft and X-ray machines internally from thin air.",
        "Only Tertiary firms ever pay salaries to South African households.",
        "Primary and Secondary sectors have zero customers once Tertiary services exist.",
    ]
    correct = f"{tert_biz} relies on {prim_need} and {sec_need} to deliver its service"
    prompt = f"How does **{tert_biz}** (Tertiary sector) depend directly on the Primary and Secondary sectors?"
    sol = f"- **Correct Interdependence:** {correct}."
    return make_question(
        rng=rng,
        subskill="16_interdependence_tertiary_relies_on_primary_secondary",
        question_type="mcq",
        prompt=prompt,
        correct_answer=correct,
        sample_answer=correct,
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Identify upstream Primary + Secondary dependency of Tertiary firm", "marks": 2, "type": "A"}],
        marking_guide="2 marks for concrete upward dependency on Primary & Secondary sectors.",
        hints={
            "tier_1": "Services and shops still need physical goods, equipment and food produced upstream.",
            "tier_2": "Match raw food/minerals (Primary) and manufactured equipment/goods (Secondary).",
            "tier_3": correct,
        },
        misconception_tags=["thinks_service_businesses_operate_without_physical_goods"],
        options=[correct] + distractors,
        duration_mins=2,
    )


def _build_17_interrelationship_three_sector_matrix(rng: random.Random, mode: str) -> Dict[str, Any]:
    rows = [
        ("Primary", "Raw wheat & cotton", "Secondary mills & factories", "Buys tractors & bank loans"),
        ("Secondary", "Canned fruit & bicycles", "Tertiary wholesalers/retailers", "Buys ore/crops & haulage"),
        ("Tertiary", "Transport, finance & retail", "Primary & Secondary firms", "Sells manufactured equipment & fresh food"),
    ]
    picked = rng.sample(rows, 2)
    headers = ["Sector", "Supplies To Other Sectors", "Primary Customer Sector", "Depends On Other Sectors For"]
    rows_ui: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Sector | Supplies To Other Sectors | Primary Customer Sector | Depends On Other Sectors For |", "|---|---|---|---|"]
    for r_idx, vals in enumerate(picked, start=1):
        req_cols = rng.sample([1, 2, 3], 2)
        cells: List[Dict[str, Any]] = []
        for c_idx, v in enumerate(vals):
            coord = f"R{r_idx}C{c_idx}"
            req = c_idx in req_cols
            cells.append({"coordinate": coord, "value": "" if req else v, "type": "required" if req else "given", "editable": req})
            if req:
                correct_map[coord] = v
                cell_hints[coord] = "Trace what each sector supplies forward and buys backward."
        rows_ui.append(cells)
        md_lines.append(f"| {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
    md_table = "\n".join(md_lines)
    return make_question(
        rng=rng,
        subskill="17_interrelationship_three_sector_matrix",
        question_type="table_completion",
        prompt="Complete the Sectoral Interdependence Matrix showing how Primary, Secondary, and Tertiary sectors supply and rely upon each other.",
        correct_answer="; ".join(f"{k}: {v}" for k, v in correct_map.items()),
        sample_answer=md_table,
        worked_solution=f"**Sectoral Interdependence Matrix:**\n\n{md_table}",
        marks=len(correct_map),
        marking_schema=[{"step": f"{k}: {v}", "marks": 1, "type": "A"} for k, v in correct_map.items()],
        marking_guide="1 mark per interdependence cell.",
        hints={
            "tier_1": "Match Primary -> raw inputs, Secondary -> finished items, Tertiary -> services/retail.",
            "tier_2": "Notice every sector both supplies outputs and purchases inputs/services.",
            "tier_3": md_table,
        },
        misconception_tags=["treats_primary_sector_as_independent_from_banks_and_factories"],
        table_payload={
            "headers": headers,
            "columns": [{"key": f"c{i}", "label": h} for i, h in enumerate(headers)],
            "rows": rows_ui,
            "correct_map": correct_map,
            "cell_hints": cell_hints,
        },
    )


def _build_18_drought_cascading_shock_across_sectors(rng: random.Random, mode: str) -> Dict[str, Any]:
    normal_tonnes = rng.choice([1000, 1200, 1500])
    drop_pct = rng.choice([30, 35, 40])
    remaining = round(normal_tonnes * (1 - drop_pct / 100.0))
    prompt = (
        f"A severe regional drought cuts a grain district's normal wheat harvest of {normal_tonnes} tonnes by **{drop_pct}%**.\n\n"
        f"(a) Calculate the drought-reduced wheat harvest in tonnes (**Primary sector**).\n"
        f"(b) Trace ONE knock-on impact onto the **Secondary sector** (bakeries/mills) and ONE onto the **Tertiary sector** (supermarkets/consumers)."
    )
    ans = f"Harvest falls to {remaining} tonnes; Secondary: flour mills/bakeries run short and pay higher grain costs; Tertiary: supermarkets raise bread prices and haulage/sales volumes fall"
    sol = (
        f"**(a) Primary Output Drop:**\n"
        f"${normal_tonnes} \\times (1 - 0.{drop_pct}) = {remaining}$ tonnes harvested.\n\n"
        f"**(b) Cascading Shock:**\n"
        f"- **Secondary sector:** Flour mills and bakeries face raw wheat shortages, higher input costs and lower factory utilisation.\n"
        f"- **Tertiary sector:** Freight trucks haul smaller volumes and supermarkets face higher wholesale bread prices and reduced consumer spending."
    )
    return make_question(
        rng=rng,
        subskill="18_drought_cascading_shock_across_sectors",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate reduced harvest {remaining} tonnes", "marks": 2, "type": "A"},
            {"step": "Explain Secondary mill impact + Tertiary retail/haulage impact", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for harvest calculation; 2 marks for Secondary and Tertiary ripple effects.",
        hints={
            "tier_1": f"Reduce {normal_tonnes} tonnes by {drop_pct}%.",
            "tier_2": "Follow the wheat from farm -> flour mill/bakery -> grocery shelf.",
            "tier_3": ans,
        },
        misconception_tags=["isolates_drought_to_farms_without_mill_or_shop_impact"],
    )


def _build_19_loadshedding_impact_mining_forestry_agriculture(rng: random.Random, mode: str) -> Dict[str, Any]:
    gdp_bn = rng.choice([4000, 4500, 5000])
    hit_pct = rng.choice([1.8, 2.1, 2.4])
    lost_bn = round(gdp_bn * hit_pct / 100.0, 1)
    prompt = (
        f"Reserve Bank analysis estimates electricity outages (load-shedding) reduced quarterly GDP by **{fmt_dec(hit_pct)}%** "
        f"on a national quarterly output base of R{gdp_bn} billion, hitting **mining, forestry, and agriculture** hardest.\n\n"
        f"(a) Calculate the estimated Rand billion output lost during that quarter.\n"
        f"(b) Explain specifically why load-shedding disrupts **Mining**, **Forestry**, and **Agriculture**."
    )
    ans = f"Lost GDP = R{fmt_dec(lost_bn)}bn; Mining: deep lifts/ventilation/pumps stop; Forestry: electric sawmills/pulping stall; Agriculture: irrigation pumps and cold-chain storage fail"
    sol = (
        f"**(a) Quarterly GDP Loss:** $\\text{{R}}{gdp_bn}\\text{{bn}} \\times {fmt_dec(hit_pct)}\\% = \\text{{R}}{fmt_dec(lost_bn)}\\text{{ billion}}$\n"
        f"**(b) Sector Impacts:**\n"
        f"- **Mining:** Deep-shaft ventilation, water pumps and rock hoists halt without reliable power, risking worker safety.\n"
        f"- **Forestry:** Electric sawmills and timber-drying kilns stall, cutting milled wood output.\n"
        f"- **Agriculture:** Electric irrigation pivots and cold-storage packhouses fail, causing crop stress and spoilage."
    )
    return make_question(
        rng=rng,
        subskill="19_loadshedding_impact_mining_forestry_agriculture",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=5,
        marking_schema=[
            {"step": f"Calculate lost output R{fmt_dec(lost_bn)}bn", "marks": 2, "type": "A"},
            {"step": "Explain Mining, Forestry and Agriculture disruption (1 mark each)", "marks": 3, "type": "A"},
        ],
        marking_guide="2 marks for percentage loss; 1 mark per explained primary sub-sector mechanism.",
        hints={
            "tier_1": f"Multiply R{gdp_bn}bn by {fmt_dec(hit_pct)}%.",
            "tier_2": "Focus on lifts/ventilation in mines, sawmills in forestry, and irrigation/cold storage on farms.",
            "tier_3": ans,
        },
        misconception_tags=["gives_generic_no_lights_answer_without_mining_forestry_farm_mechanisms"],
    )


def _build_20_factory_fire_or_strike_ripple_across_sectors(rng: random.Random, mode: str) -> Dict[str, Any]:
    shocks = [
        ("a major dairy-processing factory closing for 4 weeks after a boiler fire", "Primary dairy farmers lose their buyer and face spoiling raw milk", "Tertiary supermarkets run short of yoghurt/cheese and hauliers lose contracts"),
        ("a month-long shutdown at an automotive assembly plant", "Primary steel/platinum component mines see orders drop", "Tertiary car dealerships have empty showrooms and bank car-loan approvals dip"),
        ("a prolonged strike halting a textile mill", "Primary wool/cotton growers cannot sell clipped bales locally", "Tertiary clothing stores face stock shortages and courier deliveries drop"),
    ]
    event, prim_eff, tert_eff = rng.choice(shocks)
    prompt = (
        f"Consider a **Secondary-sector disruption**: *{event}.*\n\n"
        f"Trace one backward effect on the **Primary sector** and one forward effect on the **Tertiary sector**."
    )
    ans = f"Backward to Primary: {prim_eff}; Forward to Tertiary: {tert_eff}"
    sol = (
        f"- **Backward Linkage (Primary Sector):** {prim_eff.capitalize()}.\n"
        f"- **Forward Linkage (Tertiary Sector):** {tert_eff.capitalize()}."
    )
    return make_question(
        rng=rng,
        subskill="20_factory_fire_or_strike_ripple_across_sectors",
        question_type="short_answer",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": "Accurate backward impact on Primary suppliers", "marks": 2, "type": "A"},
            {"step": "Accurate forward impact on Tertiary retailers/logistics", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for backward Primary effect; 2 marks for forward Tertiary effect.",
        hints={
            "tier_1": "Ask who sells raw inputs TO the factory (Primary) and who distributes outputs FROM it (Tertiary).",
            "tier_2": "Secondary shocks travel both backward and forward.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_secondary_disruptions_only_move_forward"],
    )


def _build_21_sustainable_primary_resource_forestry(rng: random.Random, mode: str) -> Dict[str, Any]:
    felled = rng.choice([600, 850, 1100, 1400])
    ratio = rng.choice([2, 3])
    replanted = felled * ratio
    prompt = (
        f"To ensure **sustainable use of primary forest resources**, a Sabie forestry company enforces a "
        f"`{ratio}-for-1` replanting policy alongside controlled firebreaks. This season it harvests {felled} mature pine trees.\n\n"
        f"(a) Calculate how many saplings it must plant to honour its sustainability commitment.\n"
        f"(b) Explain why clear-felling without replanting harms both future **Secondary** sawmills and local **Tertiary** eco-tourism."
    )
    ans = f"Saplings planted = {replanted}; deforestation exhausts future timber inputs for sawmills/furniture factories and ruins scenic trails/eco-tourism"
    sol = (
        f"**(a) Replanting Target:** ${felled} \\times {ratio} = {replanted}$ saplings.\n"
        f"**(b) Cross-Sector Sustainability:** Unchecked deforestation destroys long-term timber supplies needed by Secondary sawmills/paper mills and degrades forest biodiversity supporting Tertiary eco-tourism."
    )
    return make_question(
        rng=rng,
        subskill="21_sustainable_primary_resource_forestry",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate {replanted} saplings", "marks": 2, "type": "A"},
            {"step": "Explain long-term Secondary + Tertiary consequences", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for multiplication; 2 marks for downstream sustainability reasons.",
        hints={
            "tier_1": f"Multiply harvested trees by {ratio}.",
            "tier_2": "Think of both timber supply for factories and tourist trails/biodiversity.",
            "tier_3": ans,
        },
        misconception_tags=["divides_felled_trees_by_ratio"],
    )


def _build_22_sustainable_fishing_quotas_marine_care(rng: random.Random, mode: str) -> Dict[str, Any]:
    tac = rng.choice([12000, 15000, 18000])
    num_fleets = rng.choice([10, 12, 15])
    per_fleet = round(tac / num_fleets, 1)
    prompt = (
        f"To prevent overfishing of West Coast rock lobster and hake, marine regulators set a sustainable **Total Allowable Catch (TAC)** "
        f"quota of {tac:,}".replace(",", " ") + f" tonnes shared equally among {num_fleets} licensed fishing fleets.\n\n"
        f"(a) Calculate each fleet's maximum legal annual catch.\n"
        f"(b) Give ONE additional sustainable marine practice besides catch quotas."
    )
    ans = f"Max catch = {fmt_dec(per_fleet)} tonnes/fleet; Other practices: minimum net mesh size to let juveniles escape, closed breeding seasons, or marine protected areas"
    sol = (
        f"**(a) Fleet Quota:** $\\frac{{{tac}}}{{{num_fleets}}} = {fmt_dec(per_fleet)}$ tonnes per fleet.\n"
        f"**(b) Additional Safeguard:** Enforcing minimum net mesh sizes so juvenile fish breed before capture, closed spawning seasons, or no-take marine reserves."
    )
    return make_question(
        rng=rng,
        subskill="22_sustainable_fishing_quotas_marine_care",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=3,
        marking_schema=[
            {"step": f"Calculate {fmt_dec(per_fleet)} tonnes/fleet", "marks": 2, "type": "A"},
            {"step": "Give one valid additional sustainable marine safeguard", "marks": 1, "type": "A"},
        ],
        marking_guide="2 marks for quota division; 1 mark for net size/closed season/reserve safeguard.",
        hints={
            "tier_1": f"Divide {tac} tonnes equally by {num_fleets} fleets.",
            "tier_2": "Recall mesh-size rules or breeding-season bans.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_larger_mesh_size_catches_smaller_fish"],
    )


def _build_23_sustainable_agriculture_soil_and_water(rng: random.Random, mode: str) -> Dict[str, Any]:
    flood_l = rng.choice([80000, 100000, 120000])
    save_pct = rng.choice([35, 40, 45])
    drip_l = round(flood_l * (1 - save_pct / 100.0))
    saved_l = flood_l - drip_l
    prompt = (
        f"A Western Cape grape farm replaces wasteful flood irrigation (using {flood_l:,}".replace(",", " ")
        + f" L/day) with precision **drip irrigation**, cutting daily water use by **{save_pct}%**.\n\n"
        f"(a) Calculate how many litres of water are saved daily and the new daily usage.\n"
        f"(b) Name ONE additional sustainable farming practice protecting long-term soil fertility."
    )
    ans = f"Water saved = {saved_l:,} L/day (new usage {drip_l:,} L/day); Other practice: crop rotation, contour ploughing, organic composting, or controlled grazing".replace(",", " ")
    sol = (
        f"**(a) Water Conservation:**\n"
        f"- Saved $= {flood_l} \\times {save_pct}\\% = {saved_l}$ L/day\n"
        f"- New usage $= {flood_l} - {saved_l} = {drip_l}$ L/day\n\n"
        f"**(b) Soil Protection:** Practicing **crop rotation**, organic mulching/composting, contour ploughing or rotational grazing prevents soil erosion and nutrient exhaustion."
    )
    return make_question(
        rng=rng,
        subskill="23_sustainable_agriculture_soil_and_water",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate {saved_l} L saved and {drip_l} L new usage", "marks": 2, "type": "A"},
            {"step": "Name valid soil-conservation practice", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for litres saved & new usage; 2 marks for soil practice.",
        hints={
            "tier_1": f"Find {save_pct}% of {flood_l} litres, then subtract from {flood_l}.",
            "tier_2": "Recall crop rotation, contour ploughing or anti-overgrazing measures.",
            "tier_3": ans,
        },
        misconception_tags=["subtracts_incorrectly_after_percentage_water_saving"],
    )


def _build_24_sustainable_mining_and_rehabilitation(rng: random.Random, mode: str) -> Dict[str, Any]:
    rev_m = rng.choice([200, 250, 300, 400])
    rehab_pct = rng.choice([4, 5, 6])
    rehab_m = rev_m * rehab_pct / 100.0
    prompt = (
        f"A Mpumalanga coal mine generates R{rev_m} million in annual revenue and sets aside **{rehab_pct}%** "
        f"into a statutory **environmental rehabilitation fund** to restore topsoil and treat acid mine drainage after closure.\n\n"
        f"(a) Calculate the annual Rand million contribution to the rehabilitation fund.\n"
        f"(b) Explain why mining requires long-term rehabilitation even though coal is a non-renewable resource."
    )
    ans = f"Annual reserve = R{fmt_dec(rehab_m)} million; restores land for farming/conservation and prevents toxic water pollution affecting nearby communities"
    sol = (
        f"**(a) Annual Rehabilitation Contribution:** $\\text{{R}}{rev_m}\\text{{m}} \\times {rehab_pct}\\% = \\text{{R}}{fmt_dec(rehab_m)}\\text{{ million}}$\n"
        f"**(b) Importance:** Rehabilitating old mine pits restores arable land, seals dangerous shafts, and prevents acid mine drainage from contaminating rivers needed by downstream households and farms."
    )
    return make_question(
        rng=rng,
        subskill="24_sustainable_mining_and_rehabilitation",
        question_type="calculation",
        prompt=prompt,
        correct_answer=ans,
        sample_answer=ans,
        worked_solution=sol,
        marks=4,
        marking_schema=[
            {"step": f"Calculate R{fmt_dec(rehab_m)}m reserve", "marks": 2, "type": "A"},
            {"step": "Explain post-mining topsoil/water safety protection", "marks": 2, "type": "A"},
        ],
        marking_guide="2 marks for percentage calculation; 2 marks for environmental rationale.",
        hints={
            "tier_1": f"Multiply R{rev_m} million by {rehab_pct}%.",
            "tier_2": "Think about rivers, soil fertility and post-closure land safety.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_rehabilitation_means_regrowing_coal_underground"],
    )


def _build_25_renewable_vs_non_renewable_primary_resources(rng: random.Random, mode: str) -> Dict[str, Any]:
    pairs = [
        ("commercial pine plantations and Atlantic mackerel stocks vs Bushveld platinum and Highveld coal seams", "pine timber and fish are renewable if harvested sustainably, whereas platinum and coal are finite/non-renewable"),
        ("irrigated citrus orchards and solar sunshine vs Northern Cape iron ore and alluvial diamonds", "citrus/solar replenish naturally, whereas iron ore and diamonds cannot be replaced once mined"),
        ("free-range beef cattle and harvested kelp vs natural crude oil and gold reefs", "livestock and kelp regenerate if managed well, whereas oil and gold are exhaustible non-renewables"),
    ]
    pair_txt, ans = rng.choice(pairs)
    distractors = [
        "mined metals and coal regenerate every spring automatically after rainfall",
        "no biological resource can ever be exhausted by extreme over-harvesting",
        "only Secondary factory machines count as renewable primary resources",
    ]
    prompt = f"Which statement accurately classifies *{pair_txt}*?"
    sol = f"- **Correct Classification:** {ans.capitalize()}."
    return make_question(
        rng=rng,
        subskill="25_renewable_vs_non_renewable_primary_resources",
        question_type="mcq",
        prompt=prompt,
        correct_answer=ans.capitalize(),
        sample_answer=ans.capitalize(),
        worked_solution=sol,
        marks=2,
        marking_schema=[{"step": "Distinguish renewable biological vs exhaustible mineral resources", "marks": 2, "type": "A"}],
        marking_guide="2 marks for accurate renewable vs non-renewable distinction.",
        hints={
            "tier_1": "Biological living stocks/crops can regenerate; underground minerals take millions of years.",
            "tier_2": "Remember even renewable stocks can collapse if overexploited beyond recovery.",
            "tier_3": ans.capitalize(),
        },
        misconception_tags=["classifies_coal_or_minerals_as_renewable"],
        options=[ans.capitalize()] + [d.capitalize() for d in distractors],
        duration_mins=2,
    )


ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_three_economic_sectors_overview": _build_01_three_economic_sectors_overview,
    "02_primary_sector_definition_industries": _build_02_primary_sector_definition_industries,
    "03_secondary_sector_definition_industries": _build_03_secondary_sector_definition_industries,
    "04_tertiary_sector_definition_services": _build_04_tertiary_sector_definition_services,
    "05_classifying_sa_businesses_into_sectors": _build_05_classifying_sa_businesses_into_sectors,
    "06_agriculture_mining_forestry_fishing_examples": _build_06_agriculture_mining_forestry_fishing_examples,
    "07_construction_and_manufacturing_subsectors": _build_07_construction_and_manufacturing_subsectors,
    "08_commerce_transport_finance_and_public_services": _build_08_commerce_transport_finance_and_public_services,
    "09_bokomo_wheat_to_retail_value_chain_svg": _build_09_bokomo_wheat_to_retail_value_chain_svg,
    "10_timber_to_school_desk_production_chain": _build_10_timber_to_school_desk_production_chain,
    "11_iron_ore_to_motor_vehicle_chain": _build_11_iron_ore_to_motor_vehicle_chain,
    "12_cotton_to_clothing_retail_chain": _build_12_cotton_to_clothing_retail_chain,
    "13_sectoral_value_added_percentage_calc": _build_13_sectoral_value_added_percentage_calc,
    "14_interdependence_primary_relies_on_secondary_tertiary": _build_14_interdependence_primary_relies_on_secondary_tertiary,
    "15_interdependence_secondary_relies_on_primary_tertiary": _build_15_interdependence_secondary_relies_on_primary_tertiary,
    "16_interdependence_tertiary_relies_on_primary_secondary": _build_16_interdependence_tertiary_relies_on_primary_secondary,
    "17_interrelationship_three_sector_matrix": _build_17_interrelationship_three_sector_matrix,
    "18_drought_cascading_shock_across_sectors": _build_18_drought_cascading_shock_across_sectors,
    "19_loadshedding_impact_mining_forestry_agriculture": _build_19_loadshedding_impact_mining_forestry_agriculture,
    "20_factory_fire_or_strike_ripple_across_sectors": _build_20_factory_fire_or_strike_ripple_across_sectors,
    "21_sustainable_primary_resource_forestry": _build_21_sustainable_primary_resource_forestry,
    "22_sustainable_fishing_quotas_marine_care": _build_22_sustainable_fishing_quotas_marine_care,
    "23_sustainable_agriculture_soil_and_water": _build_23_sustainable_agriculture_soil_and_water,
    "24_sustainable_mining_and_rehabilitation": _build_24_sustainable_mining_and_rehabilitation,
    "25_renewable_vs_non_renewable_primary_resources": _build_25_renewable_vs_non_renewable_primary_resources,
}
