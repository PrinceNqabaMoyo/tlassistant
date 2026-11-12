"""Grade 7 EMS: Term 3 - Starting a Business Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/03. Starting a business.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List
from app.utils.ems_namelist import get_ems_scenario
from .term3_entrepreneurs_day_archetypes_01_25 import _mcq_q, _calc_q, _rubric_q, _svg_spec
from .term3_the_entrepreneur_archetypes_01_25 import _given, _req, _ledger


def arch_01_sequential_steps_to_start_business(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    biz = sc["business_type"]
    prompt = (
        f"{person} plans to open a {biz} in {area}.\n\n"
        f"Which logical pathway orders the curriculum steps for starting a new business from beginning to launch?"
    )
    correct = "1. Identify business idea & self-fit -> 2. Research consumer needs/wants -> 3. Perform SWOT & set SMART goals -> 4. Budget & source capital -> 5. Advertise & launch"
    distractors = [
        "1. Launch operations & buy bulk machines -> 2. Borrow funds -> 3. Think of product idea -> 4. Research buyers next year",
        "1. Spend startup money on posters -> 2. Run SWOT analysis after closing -> 3. Decide what business to start",
        "1. Lease luxury city offices -> 2. Recruit 20 workers -> 3. Set goals once profits arrive",
    ]
    sol = (
        f"Step 1: Logical startup preparation pathway:\n"
        f"Start by choosing an idea suited to {person}'s strengths, verify customer needs via market research, complete a SWOT & SMART goals, "
        f"cost inputs in a startup budget, then advertise and launch."
    )
    return _mcq_q(
        rng, f"g7_sb_01_{rng.randint(100000, 999999)}", "01_sequential_steps_to_start_business",
        "Steps to Start a Business", prompt, correct, distractors, sol,
        {"tier_1": "Which steps happen BEFORE spending startup cash vs AT launch?",
         "tier_2": "Idea & research come first, followed by SWOT/goals/budget, then advertising & launch.",
         "tier_3": correct},
        ["reverses_research_and_launch_order"], curriculum_ref="Term 3 > Starting a business > Startup Steps"
    )


def arch_02_matching_idea_to_personal_aptitude(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    profile = rng.choice([
        ("enjoys early mornings, skilled at baking pastries, dislikes working with electronics", "Community home bakery & fresh bread delivery"),
        ("passionate about fixing bicycles, mechanical aptitude, strong outdoor stamina", "Neighbourhood bicycle & scooter repair workshop"),
        ("loves gardening, patient with seedlings, dislikes loud crowded food stalls", "Indigenous herb & vegetable seedling nursery"),
    ])
    likes, best_biz = profile
    prompt = (
        f"In {area}, {person} reviews personal likes, dislikes, and abilities before choosing a venture: {likes}.\n\n"
        f"Why should {person} start '{best_biz}', and how does self-assessment prevent failure?"
    )
    correct = f"Because '{best_biz}' aligns with {person}'s genuine skills and motivation, boosting endurance during tough startup months"
    distractors = [
        "Because personal dislikes make no difference once money is invested",
        "Because every entrepreneur is legally forced to pick whichever sector they dislike most",
        "Because starting a business only takes 15 minutes with zero personal skill required",
    ]
    sol = (
        f"Step 1: Step 1 of startup preparation:\n"
        f"Assessing personal likes, dislikes, and entrepreneurial qualities steers {person} toward '{best_biz}', sustaining high daily effort."
    )
    return _mcq_q(
        rng, f"g7_sb_02_{rng.randint(100000, 999999)}", "02_matching_idea_to_personal_aptitude",
        "Matching Venture Idea to Entrepreneurial Fit", prompt, correct, distractors, sol,
        {"tier_1": "Check which enterprise aligns naturally with the entrepreneur's hobbies and strengths.",
         "tier_2": "Alignment between skills and daily business work builds perseverance.",
         "tier_3": correct},
        ["ignores_owner_skill_and_passion_fit"]
    )


def arch_03_distinguishing_consumer_needs_vs_wants(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    area = sc["area"]
    case = rng.choice([
        ("clean bottled drinking water and nutritious staple food hampers", "Need — essential for human survival", "Want"),
        ("custom glitter cellphone covers and decorative party balloons", "Want — desirable extra lifestyle item, not essential for physical survival", "Need"),
        ("warm winter school jerseys and basic shelter tarps", "Need — essential protection for human survival and health", "Want"),
    ])
    good, classification, opp = case
    prompt = (
        f"While investigating consumer demand in {area}, an entrepreneur considers selling {good}.\n\n"
        f"How should {good} be classified according to consumer needs and wants?"
    )
    correct = classification
    distractors = [
        f"{opp} — every single purchase satisfies identical biological survival",
        "Neither — households buy goods without having either needs or wants",
        "Liability — customer purchases always reduce personal wealth by definition",
    ]
    sol = (
        f"Step 1: Distinguish needs vs wants (Doc Q15):\n"
        f"- Needs: things people cannot survive without.\n"
        f"- Wants: things people would like to have but do not require to survive.\n"
        f"Conclusion: {good.capitalize()} -> {classification}."
    )
    return _mcq_q(
        rng, f"g7_sb_03_{rng.randint(100000, 999999)}", "03_distinguishing_consumer_needs_vs_wants",
        "Consumer Needs vs Wants Analysis", prompt, correct, distractors, sol,
        {"tier_1": "Ask: can a person physically survive without these items?",
         "tier_2": "Survival items = needs; desirable optional goods = wants.",
         "tier_3": correct},
        ["confuses_needs_and_wants"]
    )


def arch_04_market_research_target_market_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    group = rng.choice(["high school teenagers aged 13-17", "working office commuters", "new parents with toddlers"])
    prompt = (
        f"{person} launches an enterprise in {area} focused specifically on serving **{group}** and surveys 50 of them before buying stock.\n\n"
        f"In marketing, what is the specific group ({group}) toward whom a business aims its products and advertising called?"
    )
    correct = "Target market"
    distractors = [
        "Mass media",
        "Fixed cost",
        "SWOT threat",
    ]
    sol = (
        f"Step 1: Define target market:\n"
        f"A **target market** is the distinct group of consumers ({group}) at which a business directs its goods, pricing, and advertising."
    )
    return _mcq_q(
        rng, f"g7_sb_04_{rng.randint(100000, 999999)}", "04_market_research_target_market_definition",
        "Target Market Identification", prompt, correct, distractors, sol,
        {"tier_1": "Which term describes the exact customer audience a business 'targets'?",
         "tier_2": f"Asking 50 {group} surveys your target...",
         "tier_3": correct},
        ["confuses_target_market_with_mass_media"]
    )


def arch_05_importance_of_analysing_business_idea(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, biz = sc["entrepreneur"], sc["business_type"]
    cap = rng.choice([1500, 2500, 3500])
    prompt = (
        f"Before risking R{cap:,} on {biz}, {person} performs a structured pre-launch analysis instead of rushing straight to open doors.\n\n"
        f"Why is analysing a business idea essential BEFORE launching (Doc Q16)?"
    )
    correct = "It gathers vital intelligence on likely performance, uncovers internal gaps, and flags external risks before startup capital is committed"
    distractors = [
        "It guarantees zero competition forever without improving products",
        "It turns fixed costs like rent into R0 automatically",
        "It removes any need to satisfy consumer needs or keep budgets",
    ]
    sol = (
        f"Step 1: Purpose of pre-launch idea evaluation:\n"
        f"Testing feasibility before spending R{cap:,} reveals hidden flaws and obstacles early—typically mapped through a SWOT analysis."
    )
    return _mcq_q(
        rng, f"g7_sb_05_{rng.randint(100000, 999999)}", "05_importance_of_analysing_business_idea",
        "Why Analyse a Business Idea First", prompt, correct, distractors, sol,
        {"tier_1": "Think about catching weaknesses and risks BEFORE losing R" + f"{cap:,}.",
         "tier_2": "A SWOT check previews performance and potential hazards ahead of time.",
         "tier_3": correct},
        ["rushes_launch_without_feasibility_check"]
    )


def arch_06_swot_acronym_and_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, biz = sc["entrepreneur"], sc["business_type"]
    prompt = (
        f"To anticipate problems before launching {biz}, {person} draws up a **SWOT analysis**.\n\n"
        f"What does **SWOT** stand for, and what does this strategic tool help an entrepreneur do?"
    )
    correct = "Strengths, Weaknesses, Opportunities, and Threats — mapping internal advantages/flaws and external chances/risks to guide decisions"
    distractors = [
        "Sales, Wages, Overheads, and Taxes — listing only historical bank receipts",
        "Savings, Wealth, Outputs, and Trade — replacing cash budgets completely",
        "Specific, Workable, Organised, and Timed — writing personal exercise targets",
    ]
    sol = (
        f"Step 1: Expand SWOT (Doc Q10, Q17, Q18):\n"
        f"S = Strengths, W = Weaknesses, O = Opportunities, T = Threats.\n"
        f"It identifies areas to emphasise (S/O) and areas to strengthen or guard against (W/T)."
    )
    return _mcq_q(
        rng, f"g7_sb_06_{rng.randint(100000, 999999)}", "06_swot_acronym_and_purpose",
        "SWOT Acronym & Strategic Value", prompt, correct, distractors, sol,
        {"tier_1": "Recall the four quadrants: S, W, O, and T (not SMART!).",
         "tier_2": "Internal Strengths/Weaknesses + External Opportunities/Threats.",
         "tier_3": correct},
        ["confuses_swot_with_smart"]
    )


def arch_07_swot_internal_vs_external_classification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    factor_pair = rng.choice([
        ("lack of bookkeeping training inside the founding team", "Weakness (Internal — inside business control)", "Threat"),
        ("new municipal bus terminal opening right beside the stall bringing 500 daily riders", "Opportunity (External — outside business control)", "Strength"),
        ("stage 6 load shedding interrupting electric ovens unexpectedly", "Threat (External — negative outside force)", "Weakness"),
        ("owning a high-efficiency commercial blender and pastry diploma", "Strength (Internal — inside positive capability)", "Opportunity"),
    ])
    desc, ans_type, confuse_type = factor_pair
    prompt = (
        f"While auditing a startup in {area}, {person} notes: '{desc}'.\n\n"
        f"Which SWOT quadrant is this, and is it **internal** or **external**?"
    )
    correct = ans_type
    distractors = [
        f"{confuse_type} (wrong internal/external boundary)",
        "SMART Time-bound indicator",
        "Variable production cost",
    ]
    sol = (
        f"Step 1: Classify SWOT origin & impact:\n"
        f"- Internal (controllable inside business): Strengths (+), Weaknesses (-).\n"
        f"- External (environment outside control): Opportunities (+), Threats (-).\n"
        f"Hence '{desc}' is a {ans_type}."
    )
    return _mcq_q(
        rng, f"g7_sb_07_{rng.randint(100000, 999999)}", "07_swot_internal_vs_external_classification",
        "SWOT Internal vs External Boundaries", prompt, correct, distractors, sol,
        {"tier_1": "Ask: does this come from INSIDE the business or from OUTSIDE in the wider world?",
         "tier_2": "Internal = S/W; External = O/T.",
         "tier_3": correct},
        ["confuses_internal_weakness_with_external_threat"]
    )


def arch_08_swot_quadrant_matrix_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    s_txt = rng.choice(["Experienced baker", "Secret family spice mix", "Zero debt startup"])
    w_txt = rng.choice(["Small cramped kitchen", "No delivery vehicle", "Weak social marketing"])
    o_txt = rng.choice(["School sports festival", "New clinic opening nearby", "Growing vegan demand"])
    t_txt = rng.choice(["Rival discount bakery", "Rising flour prices", "Frequent power cuts"])
    target_q = rng.choice([
        ("Weakness", w_txt, "Internal Negative"),
        ("Opportunity", o_txt, "External Positive"),
        ("Threat", t_txt, "External Negative"),
    ])
    q_name, q_fact, q_nature = target_q
    svg_body = (
        f'<text x="290" y="20" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">SWOT Quadrant Matrix: {person}&apos;s Venture</text>'
        f'<rect x="30" y="36" width="250" height="82" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="155" y="60" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">STRENGTHS (Internal +)</text>'
        f'<text x="155" y="84" font-size="11" text-anchor="middle" fill="#166534">{s_txt}</text>'
        f'<rect x="300" y="36" width="250" height="82" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="425" y="60" font-size="12" font-weight="bold" text-anchor="middle" fill="#78350f">WEAKNESSES (Internal -)</text>'
        f'<text x="425" y="84" font-size="11" text-anchor="middle" fill="#92400e">{w_txt}</text>'
        f'<rect x="30" y="130" width="250" height="82" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="155" y="154" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e3a8a">OPPORTUNITIES (External +)</text>'
        f'<text x="155" y="178" font-size="11" text-anchor="middle" fill="#1e40af">{o_txt}</text>'
        f'<rect x="300" y="130" width="250" height="82" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="425" y="154" font-size="12" font-weight="bold" text-anchor="middle" fill="#7f1d1d">THREATS (External -)</text>'
        f'<text x="425" y="178" font-size="11" text-anchor="middle" fill="#991b1b">{t_txt}</text>'
    )
    prompt = (
        f"Study the 2x2 SWOT diagram constructed for {person}'s startup.\n\n"
        f"Identify which entry falls in the **{q_name}** ({q_nature}) quadrant."
    )
    correct = q_fact
    distractors = [x for x in (s_txt, w_txt, o_txt, t_txt) if x != q_fact]
    sol = f"Reading the {q_name} ({q_nature}) cell in the SWOT matrix yields: **{q_fact}**."
    return _mcq_q(
        rng, f"g7_sb_08_{rng.randint(100000, 999999)}", "08_swot_quadrant_matrix_svg",
        "Reading a 2x2 SWOT Matrix Diagram", prompt, correct, distractors, sol,
        {"tier_1": f"Locate the {q_name} ({q_nature}) box in the matrix.",
         "tier_2": "Read the item printed inside that specific box.",
         "tier_3": q_fact},
        ["reads_wrong_swot_quadrant"],
        diagram_spec=_svg_spec(svg_body, 580, 226),
    )


def arch_09_swot_case_study_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area, biz = sc["entrepreneur"], sc["area"], sc["business_type"]
    f_s = rng.choice(["Staff have 5 years of certified welding experience", "Owns paid-off industrial sewing machines"])
    f_w = rng.choice(["Has zero bookkeeping skills and tracks sales poorly", "Only one delivery bicycle limits large orders"])
    f_o = rng.choice(["A new housing estate adds 300 nearby households", "Local high school seeks a regular catering vendor"])
    f_t = rng.choice(["Frequent municipal water cuts halt washing operations", "Large discount chain opens across the street"])
    headers = ["Business Fact from Case Study", "SWOT Quadrant (Strength / Weakness / Opportunity / Threat)"]
    rows = [
        [_given("r0_c0", f_s), _req("r0_c1", "Strength")],
        [_given("r1_c0", f_w), _req("r1_c1", "Weakness")],
        [_given("r2_c0", f_o), _req("r2_c1", "Opportunity")],
        [_given("r3_c0", f_t), _req("r3_c1", "Threat")],
    ]
    cmap = {"r0_c1": "Strength", "r1_c1": "Weakness", "r2_c1": "Opportunity", "r3_c1": "Threat"}
    chints = {
        "r0_c1": "Internal positive capability.",
        "r1_c1": "Internal shortage or shortcoming.",
        "r2_c1": "Favourable external demand trend.",
        "r3_c1": "Outside hazard beyond owner's direct control.",
    }
    sol = f"1. '{f_s}' -> Strength\n2. '{f_w}' -> Weakness\n3. '{f_o}' -> Opportunity\n4. '{f_t}' -> Threat."
    return _ledger(
        f"g7_sb_09_{rng.randint(100000, 999999)}", "09_swot_case_study_classification_table",
        "SWOT Matrix Classification Table",
        f"{person} operates a {biz} in {area}. Classify all four business facts in the table by entering Strength, Weakness, Opportunity, or Threat.",
        headers, rows, cmap, chints, "Strength; Weakness; Opportunity; Threat", sol,
        {"tier_1": "Check Internal (S/W) vs External (O/T) and Positive (S/O) vs Negative (W/T).",
         "tier_2": "Fact 1 is an internal advantage; Fact 4 is an external risk.",
         "tier_3": "1. Strength, 2. Weakness, 3. Opportunity, 4. Threat."},
        ["mixes_weakness_and_threat_rows"], marks=8,
    )


def arch_10_swot_strategic_response_mitigation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    weak_str = rng.choice(["weak financial record-keeping", "no backup power during load shedding"])
    opp_str = rng.choice(["high local demand for evening takeaways", "nearby weekend sports tournaments"])
    prompt = (
        f"In {area}, {person}'s SWOT reveals an internal limitation ({weak_str}) alongside an external market gap ({opp_str}).\n\n"
        f"Explain TWO practical actions {person} can take so the business neutralises the limitation and captures the opportunity. (4 marks)"
    )
    sample = (
        f"1. Overcome {weak_str}: Attend a free community bookkeeping workshop / invest in backup rechargeable gas burners.\n"
        f"2. Seize {opp_str}: Prepare quick grab-and-go combo packs priced affordably and promote directly at the venue."
    )
    pts = [
        f"Proposes concrete mitigation addressing {weak_str} [2 marks]",
        f"Proposes concrete commercial action capturing {opp_str} [2 marks]",
    ]
    sol = "Marking Rubric (4 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_sb_10_{rng.randint(100000, 999999)}", "10_swot_strategic_response_mitigation",
        "Turning SWOT Insights into Action", prompt, sample, pts, sol,
        {"tier_1": "Respond directly to BOTH the weakness/threat AND the opportunity.",
         "tier_2": "Action 1 fixes the limitation; Action 2 monetises the demand gap.",
         "tier_3": sample},
        ["lists_swot_words_without_action"]
    )


def arch_11_importance_of_setting_business_goals(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, biz = sc["entrepreneur"], sc["business_type"]
    prompt = (
        f"{person} starts a {biz} without setting any written targets, sales milestones, or completion dates.\n\n"
        f"Why is setting structured business goals vital for business survival and growth (Doc Q1, Q20)?"
    )
    correct = "Goals give clear direction, help measure real progress against milestones, and motivate disciplined execution before time or cash runs out"
    distractors = [
        "Goals pay off bank loans automatically without selling goods",
        "Goals guarantee that rivals close permanently within one week",
        "Without goals, expenses magically drop to zero every month",
    ]
    sol = (
        f"Step 1: Role of goals in entrepreneurship:\n"
        f"Without clear SMART goals, {person} cannot tell if sales are on track, risks drifting aimlessly, and rarely achieves sustained growth."
    )
    return _mcq_q(
        rng, f"g7_sb_11_{rng.randint(100000, 999999)}", "11_importance_of_setting_business_goals",
        "Importance of Setting Business Goals", prompt, correct, distractors, sol,
        {"tier_1": "Consider direction, motivation, and measuring progress.",
         "tier_2": "A goal with deadlines lets owners track success rather than guessing.",
         "tier_3": correct},
        ["undervalues_structured_goal_setting"]
    )


def arch_12_smart_goals_acronym_diagram_svg(rng: random.Random) -> Dict[str, Any]:
    target_profit = rng.choice([450, 600, 750])
    weeks = rng.choice([4, 6, 8])
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">SMART Business Goal Framework (Target R{target_profit} in {weeks} wks)</text>'
        f'<rect x="20" y="45" width="98" height="90" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="69" y="72" font-size="14" font-weight="bold" text-anchor="middle" fill="#1e3a8a">S</text>'
        f'<text x="69" y="96" font-size="10" text-anchor="middle" fill="#1e40af">Specific</text>'
        f'<text x="69" y="114" font-size="9" text-anchor="middle" fill="#1e40af">Clear focus</text>'
        f'<rect x="130" y="45" width="98" height="90" rx="6" fill="#dcfce7" stroke="#16a34a"/>'
        f'<text x="179" y="72" font-size="14" font-weight="bold" text-anchor="middle" fill="#14532d">M</text>'
        f'<text x="179" y="96" font-size="10" text-anchor="middle" fill="#166534">Measurable</text>'
        f'<text x="179" y="114" font-size="9" text-anchor="middle" fill="#166534">R{target_profit} metric</text>'
        f'<rect x="240" y="45" width="98" height="90" rx="6" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="289" y="72" font-size="14" font-weight="bold" text-anchor="middle" fill="#78350f">A</text>'
        f'<text x="289" y="96" font-size="10" text-anchor="middle" fill="#92400e">Achievable</text>'
        f'<text x="289" y="114" font-size="9" text-anchor="middle" fill="#92400e">Within reach</text>'
        f'<rect x="350" y="45" width="98" height="90" rx="6" fill="#f3e8ff" stroke="#7c3aed"/>'
        f'<text x="399" y="72" font-size="14" font-weight="bold" text-anchor="middle" fill="#4c1d95">R</text>'
        f'<text x="399" y="96" font-size="10" text-anchor="middle" fill="#5b21b6">Realistic</text>'
        f'<text x="399" y="114" font-size="9" text-anchor="middle" fill="#5b21b6">Real resources</text>'
        f'<rect x="460" y="45" width="100" height="90" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="510" y="72" font-size="14" font-weight="bold" text-anchor="middle" fill="#7f1d1d">T</text>'
        f'<text x="510" y="96" font-size="10" text-anchor="middle" fill="#991b1b">Time-bound</text>'
        f'<text x="510" y="114" font-size="9" text-anchor="middle" fill="#991b1b">In {weeks} weeks</text>'
    )
    prompt = (
        f"Examine the SMART visual guide for setting a R{target_profit} profit target over {weeks} weeks.\n\n"
        f"Which option correctly expands all five letters of **SMART**?"
    )
    correct = "Specific, Measurable, Achievable, Realistic, and Time-bound"
    distractors = [
        "Simple, Monetary, Aggressive, Rapid, and Traditional",
        "Strengths, Markets, Assets, Receipts, and Tax",
        "Seasonal, Managed, Audited, Retail, and Temporary",
    ]
    sol = f"SMART stands for **Specific, Measurable (R{target_profit}), Achievable, Realistic, and Time-bound ({weeks} weeks)**."
    return _mcq_q(
        rng, f"g7_sb_12_{rng.randint(100000, 999999)}", "12_smart_goals_acronym_diagram_svg",
        "SMART Goals Framework", prompt, correct, distractors, sol,
        {"tier_1": "Read the five labels inside boxes S, M, A, R, T.",
         "tier_2": "Check exact wording for each initial letter.",
         "tier_3": correct},
        ["misstates_smart_acronym"],
        diagram_spec=_svg_spec(svg_body, 580, 158),
    )


def arch_13_smart_specific_and_measurable_rewrites(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    cups = rng.choice([50, 75, 90])
    profit = cups * 4
    prompt = (
        f"{person} originally writes a vague business wish: 'Sell plenty of lemonade soon and make good money.'\n\n"
        f"Which revision satisfies both **Specific** and **Measurable** criteria?"
    )
    correct = f"Sell {cups} cups of fresh mint lemonade at the Saturday craft market to earn R{profit} net profit by 16:00"
    distractors = [
        "Become super famous in the beverage world somehow one day",
        "Try harder every week whenever feeling energetic enough",
        "Maybe sell drinks if friends feel thirsty",
    ]
    sol = (
        f"Step 1: Specific & Measurable upgrade:\n"
        f"Stating the exact item (mint lemonade), exact quantity ({cups} cups), and exact Rand target (R{profit}) makes progress objectively countable."
    )
    return _mcq_q(
        rng, f"g7_sb_13_{rng.randint(100000, 999999)}", "13_smart_specific_and_measurable_rewrites",
        "Making Goals Specific and Measurable", prompt, correct, distractors, sol,
        {"tier_1": "Look for exact product details and countable numbers (cups and Rand).",
         "tier_2": f"Which option specifies exact units ({cups}) and Rand profit (R{profit})?",
         "tier_3": correct},
        ["accepts_unmeasurable_wish_as_smart_goal"]
    )


def arch_14_smart_achievable_and_realistic_audit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    unrealistic_n = rng.choice([5000, 10000])
    prompt = (
        f"With only one small home oven baking 12 muffins per hour and R200 capital, {person} sets a goal: "
        f"'Bake and sell {unrealistic_n:,} gourmet wedding cakes before tomorrow afternoon.'\n\n"
        f"Which SMART rules does this goal blatantly violate?"
    )
    correct = "Achievable and Realistic — production capacity, budget, and 1-day timeframe make baking thousands of cakes impossible"
    distractors = [
        "Specific and Time-bound — because numbers and tomorrow are completely missing",
        "Measurable — because cakes cannot be counted in whole numbers",
        "Strengths and Threats — because baking belongs outside SWOT",
    ]
    sol = (
        f"Step 1: Realistic & Achievable check (Doc Q3, Q23-24):\n"
        f"A home oven and R200 cannot produce {unrealistic_n:,} wedding cakes overnight. Realistic goals match real-world equipment, cash, and capacity."
    )
    return _mcq_q(
        rng, f"g7_sb_14_{rng.randint(100000, 999999)}", "14_smart_achievable_and_realistic_audit",
        "Auditing Achievable and Realistic Criteria", prompt, correct, distractors, sol,
        {"tier_1": f"Compare {unrealistic_n:,} cakes against 1 oven and R200 cash.",
         "tier_2": "A goal with numbers and dates can still fail Realistic & Achievable checks!",
         "tier_3": correct},
        ["confuses_measurable_with_realistic"]
    )


def arch_15_smart_time_bound_deadline_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    target = rng.choice([300, 450, 600])
    deadline = rng.choice(["end of Term 3", "30 October", "next Friday at 15:00"])
    prompt = (
        f"{person} sets Goal X ('Save R{target} from stall sales') vs Goal Y ('Save R{target} from stall sales by {deadline}').\n\n"
        f"Why is Goal Y far easier to achieve in business practice than Goal X?"
    )
    correct = f"Because specifying a concrete deadline ({deadline}) makes the goal Time-bound, creating urgency, scheduling checkpoints, and accountability"
    distractors = [
        f"Because open-ended wishes without dates automatically attract R{target} faster",
        "Because deadlines double ingredient costs unnecessarily",
        "Because Time-bound goals exclude the need to sell products",
    ]
    sol = (
        f"Step 1: Importance of Time-bound deadlines:\n"
        f"Curriculum notes stress that a goal without a timeframe is far harder to achieve than one anchored to {deadline}."
    )
    return _mcq_q(
        rng, f"g7_sb_15_{rng.randint(100000, 999999)}", "15_smart_time_bound_deadline_impact",
        "Why Deadlines Matter (Time-bound)", prompt, correct, distractors, sol,
        {"tier_1": "What difference does adding '" + deadline + "' create?",
         "tier_2": "Deadlines turn vague wishes into scheduled action.",
         "tier_3": correct},
        ["neglects_timeframe_in_goal_setting"]
    )


def arch_16_drafting_complete_smart_goal(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, item = sc["entrepreneur"], sc["item_sold"]
    qty = rng.choice([40, 60, 80])
    prof = rng.choice([250, 350, 450])
    wks = rng.choice([3, 4, 6])
    prompt = (
        f"Write ONE complete **SMART business goal** for {person}, who plans to sell {item} using R250 seed savings over the next {wks} weeks, "
        f"and briefly prove how your sentence meets all FIVE SMART elements. (5 marks)"
    )
    sample = (
        f"Goal: 'Sell {qty} portions of fresh {item} at Saturday school sports fixtures within {wks} weeks to earn R{prof} net profit.'\n"
        f"- Specific: Focuses clearly on selling {item} at Saturday fixtures.\n"
        f"- Measurable: Exact {qty} portions and R{prof} profit.\n"
        f"- Achievable & Realistic: Fits {wks} weeks and R250 startup capital.\n"
        f"- Time-bound: Clear {wks}-week completion deadline."
    )
    pts = [
        "States Specific product/activity clearly [1 mark]",
        "Includes Measurable numerical quantity/Rand figure [1 mark]",
        "Demonstrates Achievable & Realistic scale given R250 capital [2 marks]",
        f"Specifies Time-bound deadline ({wks} weeks) [1 mark]",
    ]
    sol = "Marking Rubric (5 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_sb_16_{rng.randint(100000, 999999)}", "16_drafting_complete_smart_goal",
        "Writing a Complete 5-Part SMART Goal", prompt, sample, pts, sol,
        {"tier_1": "Include what you sell, exact numbers/Rand, realistic budget fit, and a deadline.",
         "tier_2": f"Cover S, M ({qty} units / R{prof}), A, R (R250 capital), T ({wks} weeks).",
         "tier_3": sample},
        ["omits_time_or_measurement_from_goal"], marks=5,
    )


def arch_17_advertising_definition_and_role(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area, biz = sc["entrepreneur"], sc["area"], sc["business_type"]
    prompt = (
        f"{person} opens a new {biz} in {area}.\n\n"
        f"What is **advertising**, and what two essential facts must every good advertisement communicate to consumers (Doc Q27)?"
    )
    correct = "A key marketing tool that informs people about what goods or services are offered and clearly tells them where/how to access them"
    distractors = [
        "The accounting rule for subtracting fixed rent from total cash sales",
        "Keeping a product secret from everyone except close family",
        "Throwing away damaged raw materials at the end of a market",
    ]
    sol = (
        f"Step 1: Definition of advertising:\n"
        f"Advertising informs buyers (1) **what** goods/services the business sells and (2) **where/how** to obtain them."
    )
    return _mcq_q(
        rng, f"g7_sb_17_{rng.randint(100000, 999999)}", "17_advertising_definition_and_role",
        "Definition and Role of Advertising", prompt, correct, distractors, sol,
        {"tier_1": "Think about letting customers know both WHAT you offer and WHERE to buy it.",
         "tier_2": "Advertising communicates offering details + access/location.",
         "tier_3": correct},
        ["confuses_advertising_with_accounting"]
    )


def arch_18_how_advertising_persuades_consumers(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    rival_count = rng.choice([3, 4, 5])
    prompt = (
        f"On a busy shopping street with {rival_count} competing hair salons, {person} runs persuasive advertisements highlighting "
        f"free scalp massage and weekend hours.\n\n"
        f"How do persuasive advertisements influence consumer purchasing choices (Doc Q28)?"
    )
    correct = f"They deliver a memorable message persuading customers to choose {person}'s business over the {rival_count} competing businesses"
    distractors = [
        "They force shoppers legally to buy services they cannot afford",
        "They erase every rival salon physically from the street",
        "They prevent consumers from comparing quality or prices",
    ]
    sol = (
        f"Step 1: Persuasive effect:\n"
        f"Adverts persuade buyers that your unique benefits outweigh the {rival_count} rival options."
    )
    return _mcq_q(
        rng, f"g7_sb_18_{rng.randint(100000, 999999)}", "18_how_advertising_persuades_consumers",
        "Persuasive Effect of Advertising", prompt, correct, distractors, sol,
        {"tier_1": "Notice the presence of competing salons offering alternatives.",
         "tier_2": "Persuasive ads differentiate your offer over competitors.",
         "tier_3": correct},
        ["assumes_adverts_compel_buyers_by_force"]
    )


def arch_19_advertising_media_types_comparison(rng: random.Random) -> Dict[str, Any]:
    media_pair = rng.choice([
        ("leaflets, local newspapers, magazines, and billboards", "Print and outdoor visual media"),
        ("television, community radio, websites, and SMS text messages", "Broadcast and digital/electronic media"),
    ])
    ex_list, category = media_pair
    prompt = (
        f"Advertising media are the channels businesses use to carry promotional messages to buyers.\n\n"
        f"Which category best classifies {ex_list}?"
    )
    correct = category
    distractors = [
        "Raw manufacturing ingredients",
        "Cash float coin denominations",
        "Financial liability obligations",
    ]
    sol = f"Step 1: Classify advertising channels: {ex_list} belong to **{category}** (Doc Q29)."
    return _mcq_q(
        rng, f"g7_sb_19_{rng.randint(100000, 999999)}", "19_advertising_media_types_comparison",
        "Classification of Advertising Media", prompt, correct, distractors, sol,
        {"tier_1": "Are these physical printed channels or electronic/broadcast media?",
         "tier_2": "Distinguish print/outdoor from radio/TV/digital channels.",
         "tier_3": correct},
        ["confuses_media_channels_with_inputs"]
    )


def arch_20_mass_media_vs_smme_affordability(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    tv_cost = rng.choice([45000, 60000])
    budget = rng.choice([200, 300])
    prompt = (
        f"{person} is opening a corner craft stall in {area} with R{budget} for promotion. A national TV slot costs R{tv_cost:,}.\n\n"
        f"What is **mass media**, and why do small startups usually avoid national mass media?"
    )
    correct = f"Media reaching huge national audiences (TV, national radio/press); startups avoid them because R{tv_cost:,} campaigns exceed small budgets and waste reach outside local buyers"
    distractors = [
        "Free hand-drawn school posters; startups avoid them because learners dislike drawings",
        "Private one-on-one phone calls between two close friends",
        "Government newsletters distributed only inside Parliament",
    ]
    sol = (
        f"Step 1: Mass media economics (Doc Q30):\n"
        f"Television, major newspapers, and national radio reach huge crowds at steep cost (R{tv_cost:,}), unaffordable for a R{budget} micro-budget."
    )
    return _mcq_q(
        rng, f"g7_sb_20_{rng.randint(100000, 999999)}", "20_mass_media_vs_smme_affordability",
        "Mass Media vs Small-Business Budgets", prompt, correct, distractors, sol,
        {"tier_1": "Look at both definition (large-audience media) and cost fit (R" + f"{tv_cost:,} vs R{budget}).",
         "tier_2": "Mass media reaches millions at huge expense.",
         "tier_3": correct},
        ["recommends_tv_ads_for_micro_startups"]
    )


def arch_21_four_principles_of_advertising(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    prompt = (
        f"Explain the FOUR core **principles of advertising** {person} must follow when promoting a small business in {area}. (4 marks)"
    )
    sample = (
        "1. Reach the target market: Choose channels your specific buyers actually read/watch.\n"
        "2. Match business & budget: Pick affordable local media (flyers, community radio) over expensive TV.\n"
        "3. Give clear info: State what is sold, where to buy it, and contact details.\n"
        "4. Stand out & repeat name: Use bold colours/designs and repeat the business name so buyers remember it."
    )
    pts = [
        "Reach the intended target market [1 mark]",
        "Choose media aligned with the business budget [1 mark]",
        "Give clear product, location, and contact details [1 mark]",
        "Make the design stand out and repeat the business name [1 mark]",
    ]
    sol = "Marking Rubric (4 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_sb_21_{rng.randint(100000, 999999)}", "21_four_principles_of_advertising",
        "Four Principles of Advertising", prompt, sample, pts, sol,
        {"tier_1": "Think of audience, cost, clear location/contact info, and memorability (Doc Q31).",
         "tier_2": "Target market + budget fit + clear info + stand out/repeat name.",
         "tier_3": sample},
        ["omits_contact_or_budget_principle"]
    )


def arch_22_selecting_media_by_target_demographic(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("high-school teenagers buying custom phone covers", "SMS/social posts and vibrant school noticeboard flyers instead of broadsheet business newspapers", "broadsheet newspapers read rarely by teens"),
        ("retired pensioners living near a community hall", "local community radio spots and clear printed leaflets at clinics rather than fast-scrolling gaming streams", "youth gaming livestreams"),
    ])
    market, best_media, poor_media = case
    prompt = (
        f"Applying Principle 1 ('Reach your target market'), an entrepreneur targets **{market}**.\n\n"
        f"Which advertising choice best fits this demographic?"
    )
    correct = f"Use {best_media}"
    distractors = [
        f"Rely exclusively on {poor_media}",
        "Advertise only in an unrelated foreign language",
        "Skip advertising completely and wait silently",
    ]
    sol = f"Step 1: Audience alignment (Doc Q31): Serving {market} calls for {best_media}, avoiding wasted spend on {poor_media}."
    return _mcq_q(
        rng, f"g7_sb_22_{rng.randint(100000, 999999)}", "22_selecting_media_by_target_demographic",
        "Matching Media to Target Market", prompt, correct, distractors, sol,
        {"tier_1": "Where does this specific age/customer group actually look for information?",
         "tier_2": f"Pick the media channel most used by {market}.",
         "tier_3": correct},
        ["mismatches_media_channel_with_age_group"]
    )


def arch_23_case_study_kruger_carwash_advertising(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Q4: Kruger National Park tourist car-wash
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    gate = rng.choice(["Phabeni Gate", "Numbi Gate", "Orpen Gate", "Malelane Gate"])
    prompt = (
        f"{person} starts a new car-wash near {gate} of the Kruger National Park to wash muddy 4x4 tourist vehicles exiting dirt roads.\n\n"
        f"Applying the four principles of advertising, describe FOUR concrete ways {person} should design and place the campaign. (8 marks)"
    )
    sample = (
        f"1. Reach target market: Aim specifically at tourists/holidaymakers leaving {gate} with dusty/muddy cars.\n"
        f"2. Fit budget: Choose low-cost, memorable pamphlets and signs at rest camps/exit gates rather than national TV.\n"
        f"3. Clear info: Include simple directions/landmarks from {gate}, prices, and a cellphone number.\n"
        f"4. Stand out visually: Feature memorable Big Five icons and muddy 4x4 visuals while repeating the business name."
    )
    pts = [
        f"Target market fit: aimed specifically at dusty tourists exiting {gate} [2 marks]",
        "Budget fit: inexpensive signage/pamphlets inside camps/near gate [2 marks]",
        "Clear info: prices, directions/route details, and phone contact [2 marks]",
        "Memorable visuals & name: Big Five / muddy 4x4 artwork + repeated brand name [2 marks]",
    ]
    sol = "Marking Rubric (8 marks — 2 per advertising principle):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_sb_23_{rng.randint(100000, 999999)}", "23_case_study_kruger_carwash_advertising",
        "Case Study: Kruger Gate Tourist Car Wash Ads", prompt, sample, pts, sol,
        {"tier_1": "Apply all 4 advertising principles directly to tourists leaving the wildlife park.",
         "tier_2": "Cover target audience, cheap local camp signs, directions/phone, and Big Five imagery.",
         "tier_3": sample},
        ["gives_generic_carwash_answer_without_kruger_context"], marks=8,
    )


def arch_24_print_vs_radio_advert_essentials(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    phone = f"08{rng.randint(2,4)} {rng.randint(100,999)} {rng.randint(1000,9999)}"
    prompt = (
        f"{person} writes a 30-second community radio advertisement for a mobile laundry service in {area} (contact: {phone}).\n\n"
        f"Unlike a printed poster, why should a spoken radio script repeat the business name and {phone} slowly at least twice?"
    )
    correct = "Listeners hear radio audio only briefly while driving or busy and cannot re-read details later unless the name and phone number are repeated clearly"
    distractors = [
        "Because radio listeners see printed photographs magically through speakers",
        "Because repeating the name twice cuts airtime fees in half automatically",
        "Because radio regulations prohibit stating where a business operates",
    ]
    sol = (
        f"Step 1: Medium constraints:\n"
        f"Audio adverts pass quickly. Repeating the business name and contact ({phone}) twice improves recall so listeners act later."
    )
    return _mcq_q(
        rng, f"g7_sb_24_{rng.randint(100000, 999999)}", "24_print_vs_radio_advert_essentials",
        "Radio vs Print Advert Design", prompt, correct, distractors, sol,
        {"tier_1": "Compare fleeting audio listening with reading a printed page anytime.",
         "tier_2": "People driving cannot pause live radio to copy a number like " + phone + ".",
         "tier_3": correct},
        ["treats_radio_script_like_visual_flyer"]
    )


def arch_25_marketing_four_ps_integration_svg(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice(["Handmade Soy Candles", "Solar Phone Banks", "Organic Honey Jars"])
    price = rng.choice([35, 45, 55])
    place = rng.choice(["Saturday Market Stall 3", "School Fete Gazebo", "Community Hall Entrance"])
    promo = rng.choice(["Local Radio + Flyers", "Colour Posters + WhatsApp", "Free Sample Tasting"])
    svg_body = (
        f'<text x="290" y="20" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Four Ps of Marketing Alignment</text>'
        f'<rect x="35" y="38" width="245" height="72" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="157" y="64" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e3a8a">PRODUCT</text>'
        f'<text x="157" y="86" font-size="11" text-anchor="middle" fill="#1e40af">{item}</text>'
        f'<rect x="300" y="38" width="245" height="72" rx="6" fill="#dcfce7" stroke="#16a34a"/>'
        f'<text x="422" y="64" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">PRICE</text>'
        f'<text x="422" y="86" font-size="11" text-anchor="middle" fill="#166534">R{price} per unit</text>'
        f'<rect x="35" y="124" width="245" height="72" rx="6" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="157" y="150" font-size="12" font-weight="bold" text-anchor="middle" fill="#78350f">PLACE</text>'
        f'<text x="157" y="172" font-size="11" text-anchor="middle" fill="#92400e">{place}</text>'
        f'<rect x="300" y="124" width="245" height="72" rx="6" fill="#f3e8ff" stroke="#7c3aed"/>'
        f'<text x="422" y="150" font-size="12" font-weight="bold" text-anchor="middle" fill="#4c1d95">PROMOTION</text>'
        f'<text x="422" y="172" font-size="11" text-anchor="middle" fill="#5b21b6">{promo}</text>'
    )
    prompt = (
        f"Study the Four Ps Marketing diagram showing {item} sold for R{price} at {place} using {promo}.\n\n"
        f"Which element represents **Place** in this strategy, and why must all four Ps align?"
    )
    correct = f"Place = {place}; all four Ps must reinforce one another so targeted buyers know where to find an attractively priced quality product"
    distractors = [
        f"Place = R{price}; promotion must never mention where customers can buy {item}",
        "Place = raw material factory cost only",
        "The four Ps operate completely independently with no connection to buyers",
    ]
    sol = f"Step 1: Identify Place ({place}) and holistic alignment among Product ({item}), Price (R{price}), Place, and Promotion ({promo})."
    return _mcq_q(
        rng, f"g7_sb_25_{rng.randint(100000, 999999)}", "25_marketing_four_ps_integration_svg",
        "Integrating the Four Ps of Marketing", prompt, correct, distractors, sol,
        {"tier_1": "Look at the bottom-left quadrant labelled PLACE.",
         "tier_2": "Product, Price, Place, and Promotion work together as one coherent offering.",
         "tier_3": correct},
        ["isolates_four_ps_elements"],
        diagram_spec=_svg_spec(svg_body, 580, 212),
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_sequential_steps_to_start_business": arch_01_sequential_steps_to_start_business,
    "02_matching_idea_to_personal_aptitude": arch_02_matching_idea_to_personal_aptitude,
    "03_distinguishing_consumer_needs_vs_wants": arch_03_distinguishing_consumer_needs_vs_wants,
    "04_market_research_target_market_definition": arch_04_market_research_target_market_definition,
    "05_importance_of_analysing_business_idea": arch_05_importance_of_analysing_business_idea,
    "06_swot_acronym_and_purpose": arch_06_swot_acronym_and_purpose,
    "07_swot_internal_vs_external_classification": arch_07_swot_internal_vs_external_classification,
    "08_swot_quadrant_matrix_svg": arch_08_swot_quadrant_matrix_svg,
    "09_swot_case_study_classification_table": arch_09_swot_case_study_classification_table,
    "10_swot_strategic_response_mitigation": arch_10_swot_strategic_response_mitigation,
    "11_importance_of_setting_business_goals": arch_11_importance_of_setting_business_goals,
    "12_smart_goals_acronym_diagram_svg": arch_12_smart_goals_acronym_diagram_svg,
    "13_smart_specific_and_measurable_rewrites": arch_13_smart_specific_and_measurable_rewrites,
    "14_smart_achievable_and_realistic_audit": arch_14_smart_achievable_and_realistic_audit,
    "15_smart_time_bound_deadline_impact": arch_15_smart_time_bound_deadline_impact,
    "16_drafting_complete_smart_goal": arch_16_drafting_complete_smart_goal,
    "17_advertising_definition_and_role": arch_17_advertising_definition_and_role,
    "18_how_advertising_persuades_consumers": arch_18_how_advertising_persuades_consumers,
    "19_advertising_media_types_comparison": arch_19_advertising_media_types_comparison,
    "20_mass_media_vs_smme_affordability": arch_20_mass_media_vs_smme_affordability,
    "21_four_principles_of_advertising": arch_21_four_principles_of_advertising,
    "22_selecting_media_by_target_demographic": arch_22_selecting_media_by_target_demographic,
    "23_case_study_kruger_carwash_advertising": arch_23_case_study_kruger_carwash_advertising,
    "24_print_vs_radio_advert_essentials": arch_24_print_vs_radio_advert_essentials,
    "25_marketing_four_ps_integration_svg": arch_25_marketing_four_ps_integration_svg,
}
