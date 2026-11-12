"""Grade 7 EMS: Term 3 - The Entrepreneur Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. The entrepreneur.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, RURAL_AREAS, URBAN_AREAS
from .term3_entrepreneurs_day_archetypes_01_25 import _mcq_q, _calc_q, _rubric_q, _svg_spec


def _given(cid: str, val: str) -> Dict[str, Any]:
    return {"cell_id": cid, "value": val, "type": "given", "editable": False}


def _req(cid: str, expected: str) -> Dict[str, Any]:
    return {"cell_id": cid, "value": "", "expected": expected, "type": "required", "editable": True}


def _ledger(
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    expected_summary: str,
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 6,
) -> Dict[str, Any]:
    return {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "expected_answer": expected_summary,
        "sample_answer": expected_summary,
        "correct_answer": expected_summary,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "total_marks": marks,
        "curriculum_reference": "Term 3 > The entrepreneur",
        "hints": hints,
        "misconception_tags": misconception_tags,
    }


def arch_01_definition_of_an_entrepreneur(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area, biz = sc["entrepreneur"], sc["area"], sc["business_type"]
    prompt = (
        f"In {area}, {person} spots a local gap, invests savings to launch a {biz}, organises daily operations, "
        f"and accepts the financial risk of failure in exchange for potential profit.\n\n"
        f"Which economic definition best describes {person}?"
    )
    correct = "An entrepreneur — a person with a business idea who invests, organises, takes risks, and runs a business to make a profit"
    distractors = [
        "A passive consumer who only purchases household groceries at supermarkets",
        "A salaried municipal clerk with fixed monthly wages and zero business ownership risk",
        "A government tax inspector collecting VAT from corner shops",
    ]
    sol = (
        f"Step 1: Recall the definition of an entrepreneur:\n"
        f"An entrepreneur originates a business idea, invests capital, organises production, accepts personal financial risk, "
        f"and operates the enterprise ({biz}) aiming to earn a profit."
    )
    return _mcq_q(
        rng, f"g7_ent_01_{rng.randint(100000, 999999)}", "01_definition_of_an_entrepreneur",
        "Definition of an Entrepreneur", prompt, correct, distractors, sol,
        {"tier_1": "Notice the combination of business idea, investment, organisation, risk, and profit motive.",
         "tier_2": "Which role combines risk-taking and business ownership?",
         "tier_3": correct},
        ["confuses_entrepreneur_with_employee"], curriculum_ref="Term 3 > The entrepreneur > Definition"
    )


def arch_02_entrepreneur_vs_salaried_employee(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    p1, p2 = rng.sample(NAMES, 2)
    area = sc["area"]
    salary = rng.choice([7500, 9000, 11000])
    prompt = (
        f"Compare two workers in {area}:\n"
        f"- {p1} works fixed shifts for a large retailer earning R{salary:,} per month regardless of store sales.\n"
        f"- {p2} starts an independent solar-charging kiosk using personal capital, keeping any net profit after expenses.\n\n"
        f"What distinguishes {p2} as an entrepreneur rather than an employee?"
    )
    correct = f"{p2} bears personal financial risk and earns residual profit (or suffers loss), whereas {p1} earns guaranteed wages without ownership risk"
    distractors = [
        f"{p1} carries all ownership losses whenever the retailer makes bad decisions",
        f"{p2} cannot change working hours, prices, or service offerings without employer permission",
        "Neither person participates in producing or selling within South Africa's economy",
    ]
    sol = (
        f"Step 1: Contrast employee vs entrepreneur:\n"
        f"{p1} trades labour time for a guaranteed R{salary:,} wage; {p2} owns the venture, assumes capital risk, "
        f"decides strategy independently, and earns profit (or absorbs losses)."
    )
    return _mcq_q(
        rng, f"g7_ent_02_{rng.randint(100000, 999999)}", "02_entrepreneur_vs_salaried_employee",
        "Entrepreneur vs Salaried Employee", prompt, correct, distractors, sol,
        {"tier_1": "Ask who carries financial loss risk and owns the business profit.",
         "tier_2": "Employees earn fixed wages; entrepreneurs risk capital for variable profit.",
         "tier_3": correct},
        ["equates_wage_labour_with_entrepreneurship"]
    )


def arch_03_smme_acronym_and_scope(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area, biz = sc["entrepreneur"], sc["area"], sc["business_type"]
    workers = rng.choice([2, 4, 6])
    prompt = (
        f"Most South African entrepreneurs operate **SMMEs**, such as {person}'s {biz} in {area} employing {workers} staff.\n\n"
        f"What does the acronym **SMME** stand for?"
    )
    correct = "Small, Medium and Micro Enterprises"
    distractors = [
        "State Monetary and Manufacturing Exchanges",
        "Standard Market Monopoly Establishments",
        "Single Monthly Merchandise Exports",
    ]
    sol = (
        f"Step 1: Expand SMME:\n"
        f"SMME stands for **Small, Medium and Micro Enterprises** — the backbone of job creation where most local entrepreneurs begin."
    )
    return _mcq_q(
        rng, f"g7_ent_03_{rng.randint(100000, 999999)}", "03_smme_acronym_and_scope",
        "SMME Acronym and Definition", prompt, correct, distractors, sol,
        {"tier_1": "Think of business sizes from tiny micro-traders up to medium firms.",
         "tier_2": "Each letter represents enterprise scale: Small, Medium, Micro, Enterprises.",
         "tier_3": correct},
        ["misinterprets_smme_acronym"]
    )


def arch_04_smme_economic_weight_south_africa_svg(rng: random.Random) -> Dict[str, Any]:
    smme_pct = 98
    large_pct = 2
    emp_pct = rng.choice([52, 55, 60])
    svg_body = (
        f'<text x="290" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">South African Business Share &amp; Workforce Impact</text>'
        f'<rect x="50" y="55" width="460" height="36" rx="4" fill="#e2e8f0"/>'
        f'<rect x="50" y="55" width="450" height="36" rx="4" fill="#2563eb"/>'
        f'<text x="275" y="78" font-size="12" font-weight="bold" text-anchor="middle" fill="#ffffff">SMMEs: {smme_pct}% of all SA businesses (Large: {large_pct}%)</text>'
        f'<rect x="50" y="120" width="460" height="36" rx="4" fill="#e2e8f0"/>'
        f'<rect x="50" y="120" width="{int(4.6 * emp_pct)}" height="36" rx="4" fill="#16a34a"/>'
        f'<text x="190" y="143" font-size="12" font-weight="bold" fill="#ffffff">&gt;50% ({emp_pct}%) of SA workers employed by SMMEs</text>'
    )
    prompt = (
        f"Study the data bars showing that SMMEs represent ~{smme_pct}% of all South African businesses and employ {emp_pct}% (over half) of workers.\n\n"
        f"Based on these bars, why is supporting aspiring small-business entrepreneurs vital for South Africa?"
    )
    correct = f"Because SMMEs form {smme_pct}% of enterprises and already employ over half ({emp_pct}%) of workers, helping them grow directly creates jobs against unemployment"
    distractors = [
        f"Because only the {large_pct}% mega-corporations contribute meaningfully to household jobs",
        "Because small businesses prevent citizens from needing food, shelter, or transport",
        "Because SMMEs are exempt from buying supplies or selling services to consumers",
    ]
    sol = (
        f"Step 1: Read the SMME figures:\n"
        f"With ~{smme_pct}% of enterprises being SMMEs and accounting for >50% ({emp_pct}%) of employment, "
        f"helping startups launch and expand multiplies job opportunities across communities."
    )
    return _mcq_q(
        rng, f"g7_ent_04_{rng.randint(100000, 999999)}", "04_smme_economic_weight_south_africa_svg",
        "SMME Role in South African Employment", prompt, correct, distractors, sol,
        {"tier_1": "Look at both the 98% enterprise share and the employment bar (>50%).",
         "tier_2": "When small businesses grow, who hires the majority of South African jobseekers?",
         "tier_3": correct},
        ["overlooks_smme_employment_share"],
        diagram_spec=_svg_spec(svg_body, 580, 185),
    )


def arch_05_push_factors_starting_a_business(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    push_reason = rng.choice([
        "high local unemployment preventing them from finding paid work",
        "earning too little despite working exhausting hours while profits go only to an employer",
        "enduring unsafe or miserable workplace conditions in a dead-end job",
    ])
    prompt = (
        f"In {area}, {person} decides to leave job hunting behind and open a mobile repair stall due to {push_reason}.\n\n"
        f"What does this scenario illustrate about why many South Africans become entrepreneurs?"
    )
    correct = "Economic necessity and workplace dissatisfaction often push individuals to create their own income instead of waiting for scarce jobs"
    distractors = [
        "Law prohibits South African adults from accepting any salaried positions",
        "Entrepreneurs never encounter financial risk or long hours once self-employed",
        "All employed workers are guaranteed instant promotion to CEO within six months",
    ]
    sol = (
        f"Step 1: Recognise curriculum push motives:\n"
        f"Curriculum notes highlight four main reasons: high unemployment, inadequate wages despite hard effort, "
        f"poor/boring working conditions, and wanting independence."
    )
    return _mcq_q(
        rng, f"g7_ent_05_{rng.randint(100000, 999999)}", "05_push_factors_starting_a_business",
        "Push Reasons for Entrepreneurship", prompt, correct, distractors, sol,
        {"tier_1": "What difficulty in the job market drove the decision to start a venture?",
         "tier_2": f"Think about unemployment, low pay, and working hard for someone else ({push_reason[:30]}...).",
         "tier_3": correct},
        ["ignores_unemployment_driver"]
    )


def arch_06_autonomy_pull_motivations(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    choice_note = rng.choice([
        "setting flexible morning and evening hours around family care",
        "choosing which creative custom designs to craft and keep all profit rewards",
        "making independent decisions on suppliers and pricing without an employer overriding them",
    ])
    prompt = (
        f"{person} opens a small business in {area} primarily to enjoy {choice_note}.\n\n"
        f"Which entrepreneurial motivation best matches this priority?"
    )
    correct = "Being your own boss — deciding what work you do, when you do it, and how you do it while keeping profits"
    distractors = [
        "Avoiding all accountability to customers, quality standards, and cash records",
        "Receiving paid public holidays and guaranteed overtime shifts from a boss",
        "Relying passively on lottery tickets instead of business planning",
    ]
    sol = (
        f"Step 1: Autonomy motivation:\n"
        f"Many people start businesses so they do not answer to a boss and can control what work is done, when, and how, "
        f"retaining rewards from {choice_note}."
    )
    return _mcq_q(
        rng, f"g7_ent_06_{rng.randint(100000, 999999)}", "06_autonomy_pull_motivations",
        "Autonomy: Being Your Own Boss", prompt, correct, distractors, sol,
        {"tier_1": "What benefit comes from answering to yourself rather than a manager?",
         "tier_2": "Independence lets owners pick schedule, methods, and retain profits.",
         "tier_3": correct},
        ["misunderstands_business_ownership_autonomy"]
    )


def arch_07_needs_wants_community_opportunities(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    gap = rng.choice([
        ("villagers walking 35 km just to buy spinach, tomatoes, and maize seedlings", "opening a fresh-produce stall and community nursery near the local clinic"),
        ("commuters waiting at a chilly dawn taxi rank with nowhere to grab hot breakfast", "running a clean mobile breakfast cart selling vetkoek and coffee"),
        ("households facing rainy-season school-bag tears", "offering stitched waterproof covers and rapid bag repairs"),
    ])
    problem, venture = gap
    prompt = (
        f"In {area}, {person} observes {problem}, and responds by {venture}.\n\n"
        f"How does this convert a community problem into an entrepreneurial opportunity?"
    )
    correct = "By satisfying an unmet local need conveniently, turning customer willingness to pay into steady business revenue"
    distractors = [
        "By forcing customers to walk even further to access basic necessities",
        "By inventing an artificial luxury item that nobody in the neighbourhood needs",
        "By shutting down rival transport routes illegally",
    ]
    sol = (
        f"Step 1: Connect unmet need to market gap:\n"
        f"Spotting {problem} identifies real demand; {venture} solves the inconvenience profitably."
    )
    return _mcq_q(
        rng, f"g7_ent_07_{rng.randint(100000, 999999)}", "07_needs_wants_community_opportunities",
        "Turning Community Needs into Ventures", prompt, correct, distractors, sol,
        {"tier_1": "Look at how solving a customer inconvenience creates demand.",
         "tier_2": "Entrepreneurs earn income by fulfilling real needs or wants reliably.",
         "tier_3": correct},
        ["ignores_customer_need_fit"]
    )


def arch_08_market_research_definition_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    sample_sz = rng.choice([40, 50, 80])
    prompt = (
        f"Before investing savings in {area}, {person} interviews {sample_sz} potential customers to learn what goods they want, "
        f"preferred flavours, and acceptable prices.\n\n"
        f"Which term defines this information-gathering process, and what does it achieve?"
    )
    correct = "Market research — asking the target market what it wants to guide product decisions and improve success odds"
    distractors = [
        "Stock liquidation — selling off damaged inventory at zero profit before closing",
        "Outsourcing — paying external factories to hide pricing data from buyers",
        "Tax auditing — submitting receipts to government before buying any supplies",
    ]
    sol = (
        f"Step 1: Define market research:\n"
        f"Market research systematically asks target customers ({sample_sz} surveyed) what they want, enabling informed decisions on goods, quality, and pricing."
    )
    return _mcq_q(
        rng, f"g7_ent_08_{rng.randint(100000, 999999)}", "08_market_research_definition_purpose",
        "Market Research Definition & Purpose", prompt, correct, distractors, sol,
        {"tier_1": "What term means surveying your target customers before producing?",
         "tier_2": f"Ask yourself how {person} avoids guessing what customers want.",
         "tier_3": correct},
        ["confuses_market_research_with_auditing"]
    )


def arch_09_competitor_mapping_and_niche_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    rivals = rng.choice([4, 5, 6])
    price_a = rng.choice([25, 30])
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Local Market Scan ({rivals} Existing Tuckshops)</text>'
        f'<rect x="35" y="45" width="245" height="125" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="157" y="70" font-size="12" font-weight="bold" text-anchor="middle" fill="#7f1d1d">{rivals} Identical Rivals</text>'
        f'<text x="157" y="95" font-size="11" text-anchor="middle" fill="#991b1b">All sell white bread &amp; fizzy soda</text>'
        f'<text x="157" y="115" font-size="11" text-anchor="middle" fill="#991b1b">All close by 16:30</text>'
        f'<text x="157" y="135" font-size="11" text-anchor="middle" fill="#991b1b">Average meal: R{price_a}</text>'
        f'<rect x="305" y="45" width="245" height="125" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="427" y="70" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">Unserved Commuter Gap</text>'
        f'<text x="427" y="95" font-size="11" text-anchor="middle" fill="#166534">0 stalls offer warm fruit/porridge</text>'
        f'<text x="427" y="115" font-size="11" text-anchor="middle" fill="#166534">Commuters arrive 05:30 - 07:30</text>'
        f'<text x="427" y="135" font-size="11" text-anchor="middle" fill="#166534">Workers return after 17:00</text>'
    )
    prompt = (
        f"Study {person}'s market scan contrasting {rivals} existing tuckshops (average meal R{price_a}) with local commuter gaps.\n\n"
        f"Why must an entrepreneur study competitors before launching, and which niche should {person} enter?"
    )
    correct = f"Studying {rivals} competitors reveals market saturation and an open early-morning/evening healthy meal gap rather than copying identical stock"
    distractors = [
        f"Open a seventh identical shop selling only white bread next door at R{price_a + 15}",
        "Ignore all rival shops because customer numbers stay infinite in every neighbourhood",
        "Close the shop at 12:00 daily before returning commuters reach the rank",
    ]
    sol = (
        f"Step 1: Competitor analysis ({rivals} rivals):\n"
        f"Checking competitors exposes crowded offerings (white bread/soda) vs unserved timing (05:30-07:30, after 17:00) and nutritious choices."
    )
    return _mcq_q(
        rng, f"g7_ent_09_{rng.randint(100000, 999999)}", "09_competitor_mapping_and_niche_svg",
        "Competitor Analysis and Finding a Niche", prompt, correct, distractors, sol,
        {"tier_1": "Look at when and what the existing rivals fail to offer.",
         "tier_2": f"Instead of copying {rivals} tuckshops, serve the early/late commuter gap.",
         "tier_3": correct},
        ["copies_crowded_competitors_blindly"],
        diagram_spec=_svg_spec(svg_body, 580, 190),
    )


def arch_10_trait_calculated_risk_taking(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    savings = rng.choice([2500, 4000, 6000])
    prompt = (
        f"{person} wants to quit a part-time job and invest R{savings:,} of personal savings into a laundry service. "
        f"First, {person} checks equipment warranties, tests 20 neighbours' willingness to pay, and saves an emergency reserve.\n\n"
        f"Which entrepreneurial characteristic does this approach demonstrate?"
    )
    correct = "Calculated risk-taking and bravery — taking action under uncertainty while researching carefully to limit loss"
    distractors = [
        "Reckless gambling — risking all funds blindly without speaking to any potential buyer",
        "Risk paralysis — refusing to ever try any venture unless success is 100% guaranteed",
        "Dishonest evasion — borrowing R{savings:,} with no intention to work",
    ].copy()
    distractors[2] = f"Dishonest evasion — borrowing R{savings:,} with no intention to work"
    sol = (
        f"Step 1: Distinguish calculated risk from recklessness:\n"
        f"Investing R{savings:,} still involves uncertainty of success or failure, yet testing demand and keeping reserves makes the risk calculated."
    )
    return _mcq_q(
        rng, f"g7_ent_10_{rng.randint(100000, 999999)}", "10_trait_calculated_risk_taking",
        "Calculated Risk-Taking vs Recklessness", prompt, correct, distractors, sol,
        {"tier_1": "Notice both willingness to take risk AND careful market testing beforehand.",
         "tier_2": "Entrepreneurs manage risk thoughtfully rather than gambling blindly.",
         "tier_3": correct},
        ["equates_entrepreneurial_risk_with_gambling"]
    )


def arch_11_trait_perseverance_in_adversity(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("Herman Mashaba", "restrictive apartheid laws, scarce capital, and the devastating fire that destroyed his hair-care factory"),
        ("Thuli", "two consecutive months of slow opening sales and a stolen delivery crate before winning local school contracts"),
    ])
    who, hurdle = case
    prompt = (
        f"Case note: {who} faced severe obstacles including {hurdle}, yet refused to quit, rebuilt operations, and achieved lasting success.\n\n"
        f"Which core characteristic is highlighted by refusing to quit despite serious setbacks?"
    )
    correct = "Perseverance (never giving up) — persisting with determination through adversity"
    distractors = [
        "Passivity — abandoning the business immediately after the first slow week",
        "Short-termism — expecting effortless millions in day one without challenges",
        "Secretiveness — refusing to talk with mentors or customers",
    ]
    sol = (
        f"Step 1: Identify perseverance:\n"
        f"When confronted by {hurdle}, {who} demonstrated perseverance — continuing to solve problems and rebuild rather than giving up."
    )
    return _mcq_q(
        rng, f"g7_ent_11_{rng.randint(100000, 999999)}", "11_trait_perseverance_in_adversity",
        "Trait: Perseverance Through Adversity", prompt, correct, distractors, sol,
        {"tier_1": "Focus on the response to setbacks: 'refused to quit' and 'rebuilt'.",
         "tier_2": "Which characteristic means never giving up when obstacles hit?",
         "tier_3": correct},
        ["confuses_perseverance_with_luck"]
    )


def arch_12_trait_creativity_and_imagination(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    invention = rng.choice([
        "upcycling discarded plastic bottles into durable solar garden lanterns",
        "formulating a brand-new hair-care line suited specifically for local customers when none existed",
        "converting bicycle trailers into mobile cold-water delivery stations",
    ])
    prompt = (
        f"In {area}, {person} solves an overlooked everyday challenge by {invention}.\n\n"
        f"Which entrepreneurial traits are directly shown when inventing original solutions?"
    )
    correct = "Creativity and imagination — generating fresh products and novel ways to serve people"
    distractors = [
        "Mechanical copying — duplicating the exact same storefront without improvements",
        "Apathy — ignoring customers' problems altogether",
        "Dependency — waiting for international firms to donate ready-made designs",
    ]
    sol = (
        f"Step 1: Identify creative innovation:\n"
        f"Imagining new value through {invention} shows creativity and willingness to try out new ideas."
    )
    return _mcq_q(
        rng, f"g7_ent_12_{rng.randint(100000, 999999)}", "12_trait_creativity_and_imagination",
        "Trait: Creativity and Imagination", prompt, correct, distractors, sol,
        {"tier_1": "Inventing a novel good/approach points directly to creative thinking.",
         "tier_2": "Entrepreneurs use imagination to spot original solutions.",
         "tier_3": correct},
        ["confuses_creativity_with_copying"]
    )


def arch_13_trait_vision_and_confidence(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    years = rng.choice([3, 5, 7])
    prompt = (
        f"Even when starting with one secondhand sewing machine, {person} pictures building a regional uniform workshop employing "
        f"15 seamstresses within {years} years and steps up to pitch the school principal confidently.\n\n"
        f"Which two personal characteristics enable {person} to pursue that {years}-year expansion?"
    )
    correct = "Having a clear vision of success and self-confidence to pitch ideas to buyers and partners"
    distractors = [
        "Having zero confidence and hiding the product from potential institutional buyers",
        "Avoiding future milestones beyond lunchtime today",
        "Waiting passively for orders to arrive without speaking to decision-makers",
    ]
    sol = (
        f"Step 1: Connect behaviour to traits:\n"
        f"Visualising a 15-staff workshop in {years} years shows a **vision of success**, while pitching the principal demonstrates **self-confidence**."
    )
    return _mcq_q(
        rng, f"g7_ent_13_{rng.randint(100000, 999999)}", "13_trait_vision_and_confidence",
        "Traits: Vision and Confidence", prompt, correct, distractors, sol,
        {"tier_1": "One trait relates to picturing the future; the other relates to pitching boldly.",
         "tier_2": "Match picturing growth -> vision; pitching principal -> self-confidence.",
         "tier_3": correct},
        ["overlooks_vision_role"]
    )


def arch_14_trait_energy_and_hard_work(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    wake = rng.choice(["04:15", "04:30", "05:00"])
    prompt = (
        f"Every morning at {wake}, {person} wakes up in {area} to bake fresh bread, deliver school tuckshop orders, "
        f"clean ovens, and balance cash receipts until evening.\n\n"
        f"Why are **high energy** and **hard work** essential characteristics for an early-stage entrepreneur?"
    )
    correct = "Because founders initially handle demanding physical operations, long hours, and admin personally before hiring big teams"
    distractors = [
        "Because running your own startup requires only working 20 minutes per week",
        "Because physical tiredness replaces the need to serve quality bread to customers",
        "Because entrepreneurs never take responsibility for daily deliveries or cleanup",
    ]
    sol = (
        f"Step 1: Link stamina to startup reality:\n"
        f"Starting at {wake} shows why abundant energy and sustained hard work keep orders reliable and cash records accurate."
    )
    return _mcq_q(
        rng, f"g7_ent_14_{rng.randint(100000, 999999)}", "14_trait_energy_and_hard_work",
        "Traits: High Energy and Hard Work", prompt, correct, distractors, sol,
        {"tier_1": "Think about how many tasks a startup founder performs alone every day.",
         "tier_2": "Long hours covering production, sales, and books demand stamina.",
         "tier_3": correct},
        ["assumes_entrepreneurship_needs_little_effort"]
    )


def arch_15_trait_curiosity_and_prototyping(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    trial_count = rng.choice([4, 6, 8])
    prompt = (
        f"{person} questions why standard solar lamps flicker in damp weather, tests {trial_count} waterproof seal designs, "
        f"and listens carefully to user feedback after each trial.\n\n"
        f"Which entrepreneurial mindset is {person} demonstrating?"
    )
    correct = "Curiosity and willingness to experiment with new ideas to improve product quality"
    distractors = [
        "Stubbornly selling faulty lamps while blaming customers for rain",
        "Refusing to ask questions or learn how materials behave",
        "Closing the business after test 1 without checking why lamps flickered",
    ]
    sol = (
        f"Step 1: Identify curiosity & experimentation:\n"
        f"Asking why things happen and testing {trial_count} prototypes reflects curiosity and trying new ideas—traits listed in the entrepreneur profile."
    )
    return _mcq_q(
        rng, f"g7_ent_15_{rng.randint(100000, 999999)}", "15_trait_curiosity_and_prototyping",
        "Trait: Curiosity and Trying New Ideas", prompt, correct, distractors, sol,
        {"tier_1": "Notice the questioning attitude and multiple prototype tests.",
         "tier_2": "Good entrepreneurs are curious and test new ideas systematically.",
         "tier_3": correct},
        ["neglects_iterative_testing"]
    )


def arch_16_trait_responsibility_and_service(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    refund_amt = rng.choice([45, 65, 85])
    prompt = (
        f"When a delivery van arrives 2 hours late in {area}, {person} apologises sincerely, refunds R{refund_amt} immediately to the customer, "
        f"and redesigns the dispatch checklist so orders are never late again.\n\n"
        f"Which combination of entrepreneurial traits is shown here?"
    )
    correct = "Being responsible and genuinely wanting to serve others with integrity"
    distractors = [
        "Shifting blame onto buyers and refusing refunds for poor service",
        "Caring solely about short-term cash while losing trust permanently",
        "Operating anonymously so unhappy clients cannot locate the business",
    ]
    sol = (
        f"Step 1: Ethics and service:\n"
        f"Accepting responsibility, refunding R{refund_amt} promptly, and fixing operations shows responsibility and dedication to serving customers."
    )
    return _mcq_q(
        rng, f"g7_ent_16_{rng.randint(100000, 999999)}", "16_trait_responsibility_and_service",
        "Traits: Responsibility and Customer Service", prompt, correct, distractors, sol,
        {"tier_1": "How does owning a mistake and protecting customer trust build long-term sales?",
         "tier_2": "A good entrepreneur is responsible, enjoys people, and wants to serve others well.",
         "tier_3": correct},
        ["justifies_unethical_customer_neglect"]
    )


def arch_17_networking_with_peers_and_mentors(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    peers = rng.choice([6, 8, 12])
    prompt = (
        f"{person} joins a monthly forum in {area} bringing together {peers} local small-business owners who share supplier discounts, "
        f"warnings about scams, and marketing tips.\n\n"
        f"Which entrepreneurial behaviour does this represent, and why is it valuable?"
    )
    correct = "Linking up with like-minded people who can help — gaining mentorship, shared insights, and practical support"
    distractors = [
        "Forming an illegal price-fixing cartel to overcharge vulnerable families",
        "Isolating the business completely so nobody learns from experienced founders",
        "Handing over 100% of business ownership to attendees for free",
    ]
    sol = (
        f"Step 1: Value of entrepreneurial networking:\n"
        f"Connecting with {peers} peers helps solve isolation, cuts supplier costs, and builds trusted business guidance."
    )
    return _mcq_q(
        rng, f"g7_ent_17_{rng.randint(100000, 999999)}", "17_networking_with_peers_and_mentors",
        "Networking with Like-Minded Entrepreneurs", prompt, correct, distractors, sol,
        {"tier_1": "Notice the collaborative sharing of supplier tips and mutual support.",
         "tier_2": "Entrepreneurs succeed faster when linking up with supportive peers and mentors.",
         "tier_3": correct},
        ["thinks_entrepreneurs_must_work_isolated"]
    )


def arch_18_skill_critical_vs_creative_thinking(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    drop_pct = rng.choice([25, 30, 35])
    prompt = (
        f"Sales at {person}'s stall fall by {drop_pct}% during mid-month. First, {person} analyses cash slips carefully and discovers "
        f"that R25 snack boxes exceed mid-month pocket money (**Skill 1**). Then {person} invents a new R8 mini combo (**Skill 2**).\n\n"
        f"Identify **Skill 1** and **Skill 2** in order."
    )
    correct = "Skill 1: Critical thinking about challenges (diagnosing root cause); Skill 2: Creative thinking (inventing a fresh solution)"
    distractors = [
        "Skill 1: Guessing blindly without cash data; Skill 2: Closing down immediately",
        "Skill 1: Outsourcing cash counting to strangers; Skill 2: Doubling snack prices to R50",
        "Skill 1: Physical lifting strength; Skill 2: Passive obedience to competitors",
    ]
    sol = (
        f"Step 1: Distinguish two core entrepreneurial skills:\n"
        f"- Critical thinking: objectively analysing the {drop_pct}% drop using cash data to spot the price barrier.\n"
        f"- Creative thinking: inventing the affordable R8 mini combo."
    )
    return _mcq_q(
        rng, f"g7_ent_18_{rng.randint(100000, 999999)}", "18_skill_critical_vs_creative_thinking",
        "Skills: Critical vs Creative Thinking", prompt, correct, distractors, sol,
        {"tier_1": "Analysing why sales dropped vs inventing a new combo.",
         "tier_2": "Diagnosing challenges logically = critical thinking; generating new ideas = creative thinking.",
         "tier_3": correct},
        ["confuses_critical_analysis_with_creativity"]
    )


def arch_19_skill_planning_and_organising(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    deliveries = rng.choice([8, 12, 15])
    prompt = (
        f"Running a catering business in {area}, {person} writes weekly prep checklists, labels cold storage shelves clearly, "
        f"and routes {deliveries} lunch boxes efficiently so zero orders arrive cold or mixed up.\n\n"
        f"Which learned entrepreneurial skills are most directly demonstrated?"
    )
    correct = "Planning ahead and organising tasks, materials, and schedules cleanly"
    distractors = [
        "Impulse spending without written lists",
        "Ignoring delivery order sequence until food turns cold",
        "Eliminating all stock labels and storage routines",
    ]
    sol = (
        f"Step 1: Identify planning & organisation:\n"
        f"Checklists, shelf labelling, and routing {deliveries} orders showcase **planning** and **organising things well**, two key curriculum skills."
    )
    return _mcq_q(
        rng, f"g7_ent_19_{rng.randint(100000, 999999)}", "19_skill_planning_and_organising",
        "Skills: Planning and Organising", prompt, correct, distractors, sol,
        {"tier_1": "Checklists and tidy routing describe operational skills.",
         "tier_2": "Think of preparing ahead and keeping resources systematically arranged.",
         "tier_3": correct},
        ["underestimates_planning_and_organisation"]
    )


def arch_20_skill_resourcefulness_and_opportunity_finding(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    capital = rng.choice([150, 200, 250])
    prompt = (
        f"With only R{capital} in capital in {area}, {person} borrows a family bicycle, cleans free off-cut wood from a local sawmill, "
        f"and builds attractive spice racks to sell outside Saturday markets.\n\n"
        f"Which skill enables {person} to launch successfully despite having minimal cash?"
    )
    correct = "Being resourceful and finding opportunities — making clever use of available assets and low-cost materials"
    distractors = [
        "Demanding a R50 000 corporate bank loan before crafting a single spice rack",
        "Waiting five years until free brand-new power tools appear",
        "Refusing to work unless paid fixed monthly government wages",
    ]
    sol = (
        f"Step 1: Resourcefulness:\n"
        f"With just R{capital}, leveraging a borrowed bike and free sawmill off-cuts demonstrates resourcefulness and spotting viable market opportunities."
    )
    return _mcq_q(
        rng, f"g7_ent_20_{rng.randint(100000, 999999)}", "20_skill_resourcefulness_and_opportunity_finding",
        "Skill: Resourcefulness with Limited Funds", prompt, correct, distractors, sol,
        {"tier_1": "Notice how clever use of free off-cuts and borrowed assets overcomes low cash.",
         "tier_2": "Making the best of scarce tools = resourcefulness.",
         "tier_3": correct},
        ["thinks_large_capital_is_always_mandatory"]
    )


def arch_21_scaling_to_large_and_multinational(rng: random.Random) -> Dict[str, Any]:
    founder = rng.choice([
        ("Mark Shuttleworth", "started a digital security business (Thawte) from a Cape Town garage and sold it globally for billions"),
        ("Herman Mashaba", "began selling Black Like Me hair products from the boot of his car and expanded across Africa"),
        ("Richard Branson", "launched a student magazine and small mail-order record business before building the multinational Virgin group"),
    ])
    who, story = founder
    prompt = (
        f"Think about famous entrepreneur {who}, who {story}.\n\n"
        f"What key lesson does {who}'s journey teach Grade 7 EMS learners about entrepreneurship?"
    )
    correct = "Entrepreneurship is not limited to tiny street stalls; strong ideas started with modest resources can grow into large national or multinational companies"
    distractors = [
        "Only people born billionaires are legally permitted to start technology or retail companies",
        "Small businesses never evolve beyond one owner selling out of a car boot",
        "Multinational businesses cannot trace their roots back to individual entrepreneurs",
    ]
    sol = (
        f"Step 1: Growth trajectory:\n"
        f"{who}'s path ({story}) proves entrepreneurial ideas can scale from small beginnings into wealth-creating national or multinational enterprises."
    )
    return _mcq_q(
        rng, f"g7_ent_21_{rng.randint(100000, 999999)}", "21_scaling_to_large_and_multinational",
        "Scaling From Startup to Multinational", prompt, correct, distractors, sol,
        {"tier_1": "Look at where the founder started versus what the enterprise grew into.",
         "tier_2": "Entrepreneurship covers micro-ventures all the way to global firms.",
         "tier_3": correct},
        ["limits_entrepreneurship_to_informal_survival"]
    )


def arch_22_sa_entrepreneur_case_study_analysis(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area, title, text = sc["entrepreneur"], sc["area"], sc["case_study_title"], sc["case_study_text"]
    prompt = (
        f"Read the case study **{title}** ({area}):\n"
        f"> {text}\n\n"
        f"Identify TWO personal characteristics and TWO practical business skills {person} demonstrates in this venture. (4 marks)"
    )
    sample = (
        f"Characteristics (2): (1) Opportunity-seeking/creative vision — spotted unmet local demand; "
        f"(2) Calculated risk-taking & initiative — invested personal capital to launch.\n"
        f"Skills (2): (1) Resourcefulness & planning — leveraged accessible resources cleanly; "
        f"(2) Organising operations & financial control — managed inputs, staffing, or records."
    )
    pts = [
        "Identifies 2 relevant entrepreneurial characteristics tied to the story (e.g. initiative, risk-taking, perseverance, creativity) [2 marks]",
        "Identifies 2 relevant entrepreneurial skills tied to the story (e.g. opportunity-spotting, planning, organising, resourcefulness) [2 marks]",
    ]
    sol = f"Marking Rubric (4 marks for {person} in {area}):\n- {pts[0]}\n- {pts[1]}"
    return _rubric_q(
        f"g7_ent_22_{rng.randint(100000, 999999)}", "22_sa_entrepreneur_case_study_analysis",
        "Case Study: Characteristics & Skills", prompt, sample, pts, sol,
        {"tier_1": "Separate personal traits (who they are) from learned skills (what they do).",
         "tier_2": "Look for actions in the text showing initiative, planning, resourcefulness, and persistence.",
         "tier_3": sample},
        ["confuses_traits_with_generic_adjectives"]
    )


def arch_23_startup_challenges_and_workload(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    prompt = (
        f"Explain THREE realistic difficulties {person} may face when starting a new small business in {area}. (4 marks)"
    )
    sample = (
        "1. Difficulty raising enough start-up capital because lenders doubt unproven businesses.\n"
        "2. Heavy time & money needed to advertise and win community trust from scratch.\n"
        "3. Workload overload: wearing all hats simultaneously—core production, finance, administration, and marketing."
    )
    pts = [
        "Scarcity of start-up capital / investor hesitation [1 mark]",
        "Effort and cost to build market awareness and community interest [1 mark]",
        "Heavy multitasking across production, finance, admin, and marketing [2 marks]",
    ]
    sol = "Marking Rubric (4 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ent_23_{rng.randint(100000, 999999)}", "23_startup_challenges_and_workload",
        "Challenges of Starting a Business", prompt, sample, pts, sol,
        {"tier_1": "Think about money needed at launch, attracting customers, and doing every job yourself.",
         "tier_2": "Cover startup capital, marketing awareness, and juggling admin/finance/core work.",
         "tier_3": sample},
        ["assumes_only_capital_is_a_challenge"]
    )


def arch_24_securing_startup_capital_investor_hesitation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    cap_need = rng.choice([5000, 8000, 12000])
    prompt = (
        f"'Entrepreneurs need money to make money.' When {person} seeks R{cap_need:,} in **start-up capital** in {area}, "
        f"local lenders hesitate.\n\n"
        f"Why is raising start-up capital often especially hard for brand-new entrepreneurs?"
    )
    correct = "New ventures have no trading track record yet, so investors cannot be sure the business will succeed or repay borrowed funds"
    distractors = [
        "South African banks are banned from ever lending money to businesses under 100 employees",
        "New entrepreneurs require zero start-up capital to purchase initial equipment or raw materials",
        "Successful startups pay back loans immediately on day one before selling anything",
    ]
    sol = (
        f"Step 1: Investor risk perspective (R{cap_need:,}):\n"
        f"Businesses need start-up capital before operating, yet investors hesitate when a brand-new founder lacks historical sales proving repayment capacity."
    )
    return _mcq_q(
        rng, f"g7_ent_24_{rng.randint(100000, 999999)}", "24_securing_startup_capital_investor_hesitation",
        "Why Start-up Capital Is Hard to Raise", prompt, correct, distractors, sol,
        {"tier_1": "Put yourself in the lender's shoes lending to a business with zero sales history.",
         "tier_2": "Uncertainty about survival and loan repayment causes lender caution.",
         "tier_3": correct},
        ["ignores_lender_repayment_risk"]
    )


def arch_25_owner_time_allocation_schedule_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    core_h = rng.choice([24, 28, 30])
    mkt_h = rng.choice([6, 8])
    fin_h = rng.choice([4, 5])
    adm_h = rng.choice([4, 6])
    tot_h = core_h + mkt_h + fin_h + adm_h
    headers = ["Business Function", "Weekly Tasks", "Hours Allocated"]
    rows = [
        [_given("r0_c0", "Core Production / Service"), _given("r0_c1", "Making goods & serving buyers"), _given("r0_c2", str(core_h))],
        [_given("r1_c0", "Marketing & Selling"), _given("r1_c1", "Posters, promos & social outreach"), _given("r1_c2", str(mkt_h))],
        [_given("r2_c0", "Finance & Bookkeeping"), _given("r2_c1", "Recording cash, banking & supplier bills"), _given("r2_c2", str(fin_h))],
        [_given("r3_c0", "Administration"), _given("r3_c1", "Stock lists, permits & emails"), _given("r3_c2", str(adm_h))],
        [_given("r4_c0", "TOTAL WEEKLY HOURS"), _given("r4_c1", "Total sole-owner workload"), _req("r4_c2", str(tot_h))],
    ]
    cmap = {"r4_c2": str(tot_h)}
    chints = {"r4_c2": "Add the four weekly hour entries across all business hats."}
    sol = f"Total weekly hours = {core_h} (Core) + {mkt_h} (Marketing) + {fin_h} (Finance) + {adm_h} (Admin) = {tot_h} hours."
    return _ledger(
        f"g7_ent_25_{rng.randint(100000, 999999)}", "25_owner_time_allocation_schedule_table",
        "Balancing Sole-Owner Business Functions",
        f"As a new owner, {person} wears all operational hats personally. Calculate {person}'s total weekly working hours in the schedule below.",
        headers, rows, cmap, chints, f"Total Weekly Hours = {tot_h}", sol,
        {"tier_1": "Add the hours across Core Production, Marketing, Finance, and Administration.",
         "tier_2": f"Sum {core_h} + {mkt_h} + {fin_h} + {adm_h}.",
         "tier_3": f"{tot_h} hours"},
        ["underestimates_non_production_admin_time"], marks=2,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_definition_of_an_entrepreneur": arch_01_definition_of_an_entrepreneur,
    "02_entrepreneur_vs_salaried_employee": arch_02_entrepreneur_vs_salaried_employee,
    "03_smme_acronym_and_scope": arch_03_smme_acronym_and_scope,
    "04_smme_economic_weight_south_africa_svg": arch_04_smme_economic_weight_south_africa_svg,
    "05_push_factors_starting_a_business": arch_05_push_factors_starting_a_business,
    "06_autonomy_pull_motivations": arch_06_autonomy_pull_motivations,
    "07_needs_wants_community_opportunities": arch_07_needs_wants_community_opportunities,
    "08_market_research_definition_purpose": arch_08_market_research_definition_purpose,
    "09_competitor_mapping_and_niche_svg": arch_09_competitor_mapping_and_niche_svg,
    "10_trait_calculated_risk_taking": arch_10_trait_calculated_risk_taking,
    "11_trait_perseverance_in_adversity": arch_11_trait_perseverance_in_adversity,
    "12_trait_creativity_and_imagination": arch_12_trait_creativity_and_imagination,
    "13_trait_vision_and_confidence": arch_13_trait_vision_and_confidence,
    "14_trait_energy_and_hard_work": arch_14_trait_energy_and_hard_work,
    "15_trait_curiosity_and_prototyping": arch_15_trait_curiosity_and_prototyping,
    "16_trait_responsibility_and_service": arch_16_trait_responsibility_and_service,
    "17_networking_with_peers_and_mentors": arch_17_networking_with_peers_and_mentors,
    "18_skill_critical_vs_creative_thinking": arch_18_skill_critical_vs_creative_thinking,
    "19_skill_planning_and_organising": arch_19_skill_planning_and_organising,
    "20_skill_resourcefulness_and_opportunity_finding": arch_20_skill_resourcefulness_and_opportunity_finding,
    "21_scaling_to_large_and_multinational": arch_21_scaling_to_large_and_multinational,
    "22_sa_entrepreneur_case_study_analysis": arch_22_sa_entrepreneur_case_study_analysis,
    "23_startup_challenges_and_workload": arch_23_startup_challenges_and_workload,
    "24_securing_startup_capital_investor_hesitation": arch_24_securing_startup_capital_investor_hesitation,
    "25_owner_time_allocation_schedule_table": arch_25_owner_time_allocation_schedule_table,
}
