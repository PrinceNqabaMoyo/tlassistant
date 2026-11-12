"""Grade 7 EMS: Term 3 - Entrepreneur's Day Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS


def _mcq_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 2,
    curriculum_ref: str = "Term 3 > Entrepreneur's Day > Hosting an Entrepreneur's Day",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + [d for d in distractors if d != correct][:3]
    rng.shuffle(options)
    c_idx = options.index(correct)
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": c_idx,
        "correct_answer": correct,
        "sample_answer": correct,
        "expected_answer": correct,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "total_marks": marks,
        "curriculum_reference": curriculum_ref,
        "hints": hints,
        "misconception_tags": misconception_tags,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _calc_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_value: str,
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 3,
    curriculum_ref: str = "Term 3 > Entrepreneur's Day > Costing and Revenue",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "math_short",
        "modality": "math",
        "solution_type": "symbolic_steps",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": expected_value,
        "sample_answer": expected_value,
        "expected_answer": expected_value,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "total_marks": marks,
        "curriculum_reference": curriculum_ref,
        "hints": hints,
        "misconception_tags": misconception_tags,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _rubric_q(
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    sample_answer: str,
    marking_points: List[str],
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 4,
    curriculum_ref: str = "Term 3 > Entrepreneur's Day > Preparation and Reflection",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    schema_pts = [
        {"id": f"mp_{i + 1}", "desc": pt, "marks": max(1, marks // len(marking_points)), "editable": True}
        for i, pt in enumerate(marking_points)
    ]
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "short_answer",
        "modality": "semantic",
        "solution_type": "marking_points",
        "prompt": prompt,
        "question": prompt,
        "marking_points": marking_points,
        "marking_schema": {"total_marks": marks, "marking_points": schema_pts, "carry_forward_rule": "consequential_accuracy"},
        "sample_answer": sample_answer,
        "correct_answer": sample_answer,
        "expected_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "total_marks": marks,
        "curriculum_reference": curriculum_ref,
        "hints": hints,
        "misconception_tags": misconception_tags,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _svg_spec(svg_body: str, width: int = 580, height: int = 240) -> Dict[str, Any]:
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" '
        f'style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;font-family:sans-serif">'
        f"{svg_body}</svg>"
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_aim_and_purpose_of_entrepreneurs_day(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    item = rng.choice(["beaded keyrings", "iced rooibos tea", "fresh popcorn cones", "fruit kebabs"])
    prompt = (
        f"Grade 7 learners at a school in {area} are preparing for their annual Entrepreneur's Day, where {person} hopes to sell {item}.\n\n"
        f"What is the primary educational aim of hosting an Entrepreneur's Day at school?"
    )
    correct = "To give learners a practical opportunity to think creatively about ways of making money and running a real mini-venture"
    distractors = [
        "To replace Mathematics and EMS written examinations permanently with playground games",
        "To ensure learners spend all their family savings on imported luxury merchandise",
        "To require every Grade 7 learner to sign multi-year commercial property leases",
    ]
    sol = (
        f"Step 1: Recall the aim of Entrepreneur's Day:\n"
        f"Entrepreneur's Day lets learners put business theory into practice, think creatively about making money, "
        f"price products such as {item}, manage stock, and prepare an Income and Expenditure Statement."
    )
    return _mcq_q(
        rng, f"g7_ed_01_{rng.randint(100000, 999999)}", "01_aim_and_purpose_of_entrepreneurs_day",
        "Aim of Entrepreneur's Day", prompt, correct, distractors, sol,
        {"tier_1": "Consider what practical skills learners practise when running a real school stall.",
         "tier_2": "Entrepreneur's Day combines creativity, costing, marketing, and recording income.",
         "tier_3": "It gives learners hands-on practice thinking creatively to earn money."},
        ["confuses_entrepreneurs_day_with_play"]
    )


def arch_02_preparation_step_order_sequence(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    prod = rng.choice(["spiced vetkoek", "decorated bookmarks", "lemonade", "herb pots"])
    prompt = (
        f"{person}'s team in {area} wants to sell {prod} at Entrepreneur's Day.\n\n"
        f"Which chronological order correctly sequences the key preparation stages from start to finish?"
    )
    correct = "1. Choose good & name -> 2. Calculate costs & selling price -> 3. Advertise & build display stand -> 4. Sell goods -> 5. Draw up Income and Expenditure Statement"
    distractors = [
        "1. Sell goods -> 2. Calculate production costs -> 3. Choose good & name -> 4. Draw up Income and Expenditure Statement",
        "1. Draw up Income and Expenditure Statement -> 2. Design poster -> 3. Choose good & name -> 4. Source ingredients",
        "1. Decorate stand -> 2. Sell goods -> 3. Decide on product -> 4. Calculate selling prices afterwards",
    ]
    sol = (
        f"Step 1: Trace the logical 10-step preparation sequence:\n"
        f"First choose the product ({prod}) and venture name, calculate costs and selling prices before buying excess stock, "
        f"advertise and prepare the display stand, conduct sales on the day, and finish with an Income and Expenditure Statement."
    )
    return _mcq_q(
        rng, f"g7_ed_02_{rng.randint(100000, 999999)}", "02_preparation_step_order_sequence",
        "Preparation Steps Sequence", prompt, correct, distractors, sol,
        {"tier_1": "Which financial document can only be finalised AFTER all sales end?",
         "tier_2": "You must select your product and costings before decorating or selling, and draw up your statement last.",
         "tier_3": f"Correct sequence: {correct}"},
        ["wrong_preparation_chronology"]
    )


def arch_03_market_research_buyer_surveys(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    survey_n = rng.choice([30, 45, 60, 75])
    item = rng.choice(["fruit smoothies", "cupcakes", "buns & polony", "handmade bracelets"])
    prompt = (
        f"Before spending money on supplies for Entrepreneur's Day in {area}, {person} surveys {survey_n} potential buyers "
        f"at break time about {item} and how much pocket money they can pay.\n\n"
        f"Why is researching potential buyers essential before buying stock?"
    )
    correct = "It confirms real learner demand and affordable pricing so money is not wasted on unwanted items"
    distractors = [
        "It legally guarantees that every surveyed learner will buy at least ten items",
        "It replaces the need to calculate ingredient costs or set a selling price",
        "It eliminates competition from every other stall at the school event",
    ]
    sol = (
        f"Step 1: Connect market research to risk reduction:\n"
        f"Surveying {survey_n} learners identifies whether classmates actually want {item} and at what price, "
        f"preventing unsold stock and financial loss."
    )
    return _mcq_q(
        rng, f"g7_ed_03_{rng.randint(100000, 999999)}", "03_market_research_buyer_surveys",
        "Researching Potential Buyers", prompt, correct, distractors, sol,
        {"tier_1": "What happens if you buy stock that learners cannot afford or do not want?",
         "tier_2": "Checking buyer preferences and pocket money limits protects against unsold waste.",
         "tier_3": "Market research confirms demand and price willingness before spending."},
        ["premature_stock_purchase"]
    )


def arch_04_low_cost_high_demand_product_choice(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    budget_cap = rng.choice([120, 150, 180, 200])
    prompt = (
        f"{person} in {area} has a modest startup budget of R{budget_cap} for Entrepreneur's Day.\n\n"
        f"Which criterion best identifies a winning Entrepreneur's Day product?"
    )
    correct = "Goods that cost very little to produce, appeal strongly to schoolmates, and yield a healthy profit margin"
    distractors = [
        "Luxury electronics requiring R2 500 per unit in imported components",
        "Perishable items that nobody at school enjoys eating or buying",
        "Complex services needing heavy industrial machinery on the sports field",
    ]
    sol = (
        f"Step 1: Evaluate startup budget constraints (R{budget_cap}):\n"
        f"Previous Entrepreneur's Day successes rely on low production costs, accessible ingredients, "
        f"high appeal among school learners, and clear positive mark-up."
    )
    return _mcq_q(
        rng, f"g7_ed_04_{rng.randint(100000, 999999)}", "04_low_cost_high_demand_product_choice",
        "Low-Cost High-Demand Selection", prompt, correct, distractors, sol,
        {"tier_1": "Think about both cost to produce and willingness of fellow learners to buy.",
         "tier_2": "Small capital requires low production cost combined with steady school demand.",
         "tier_3": "Choose affordable-to-make goods that learners strongly desire."},
        ["high_capital_product_mismatch"]
    )


def arch_05_complementary_goods_pairing(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    pair = rng.choice([
        ("hot chocolate", "home-baked rusks", "cold winter morning"),
        ("boerewors rolls", "chilled fruit juice", "warm sports afternoon"),
        ("spiced popcorn", "flavoured slushies", "sunny break-time market"),
    ])
    g1, g2, weather = pair
    prompt = (
        f"{person} sells {g1} on a {weather} and decides to add {g2} at the same stall.\n\n"
        f"Why is selling complementary goods effective at Entrepreneur's Day?"
    )
    correct = f"Buyers purchasing {g1} naturally want {g2} at the same time, increasing sales per customer"
    distractors = [
        f"Selling {g2} forces every buyer to return {g1} without paying",
        "Complementary goods can only be sold if both are priced at R0",
        "Adding a second matching item doubles the fixed stall fee automatically",
    ]
    sol = (
        f"Step 1: Apply complementary goods strategy:\n"
        f"{g1.capitalize()} and {g2} pair naturally together on a {weather}. "
        f"Customers buying one item often purchase the companion item, raising revenue per visitor."
    )
    return _mcq_q(
        rng, f"g7_ed_05_{rng.randint(100000, 999999)}", "05_complementary_goods_pairing",
        "Complementary Goods Strategy", prompt, correct, distractors, sol,
        {"tier_1": "How do two paired items like tea and biscuits affect customer spending?",
         "tier_2": "Items enjoyed together encourage cross-selling at one stand.",
         "tier_3": "Complementary goods boost basket size per buyer."},
        ["ignores_complementary_demand"]
    )


def arch_06_creative_stall_naming_branding(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    theme = rng.choice([
        ("healthy fruit smoothies & banana bars", "Smoothie Safari", "Rusty Bolts Hardware"),
        ("insect-themed Halloween biscuits & jelly snacks", "Creepy Crunch & Eat It!", "Boring Plain Biscuits Pty"),
        ("hand-painted pebble paperweights & pot plants", "Pebble & Bloom", "Bank Tax Clearance Desk"),
    ])
    goods, good_name, bad_name = theme
    prompt = (
        f"{person} is choosing a stall name to attract school buyers to a stand selling {goods}.\n\n"
        f"Which stall name is most creative, memorable, and suited to the product theme?"
    )
    correct = f"{good_name} — catchy, playful, and signals clearly what the stall offers"
    distractors = [
        f"{bad_name} — unrelated to {goods}",
        "Grade 7 Learner Group Assignment Number 14",
        "Anonymous Unnamed Table B",
    ]
    sol = (
        f"Step 1: Evaluate retail naming principles:\n"
        f"An effective Entrepreneur's Day stall name should be punchy, memorable, and link immediately to {goods}. "
        f"'{good_name}' stands out to shoppers from across the playground."
    )
    return _mcq_q(
        rng, f"g7_ed_06_{rng.randint(100000, 999999)}", "06_creative_stall_naming_branding",
        "Creative Stall Naming", prompt, correct, distractors, sol,
        {"tier_1": "A great shop name tells buyers what you sell and stays in memory.",
         "tier_2": f"Avoid generic labels; match the vibe of {goods}.",
         "tier_3": f"'{good_name}' best matches the stall offering."},
        ["generic_branding_choice"]
    )


def arch_07_school_safety_and_hygiene_rules(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    rule_case = rng.choice([
        ("using an open-flame paraffin stove inside a crowded classroom corridor", "Use pre-cooked safe food or an approved outdoor area with teacher supervision and fire safety gear", "unsafe open flames near crowded exits"),
        ("handling unpackaged pancakes directly with bare hands while taking cash", "Use clean tongs/gloves for food and separate cash handling to meet hygiene rules", "unhygienic cross-contamination between coins and food"),
        ("selling sharp glass bottles near the junior sports field", "Serve drinks in recyclable plastic cups or paper cartons as required by school safety rules", "breakage hazard on school grounds"),
    ])
    hazard, fix, reason = rule_case
    prompt = (
        f"At a school in {area}, {person}'s group considers {hazard}.\n\n"
        f"How must the team adapt to comply with school safety and hygiene requirements?"
    )
    correct = fix
    distractors = [
        "Hide the equipment under a tablecloth so teachers do not inspect the stand",
        "Raise selling prices by R2 instead of changing any unsafe handling practice",
        "Ask younger learners to guard the hazard without adult oversight",
    ]
    sol = (
        f"Step 1: Identify the safety/hygiene risk:\n"
        f"{hazard.capitalize()} creates {reason}.\n"
        f"Step 2: Apply school safety policy:\n{fix}."
    )
    return _mcq_q(
        rng, f"g7_ed_07_{rng.randint(100000, 999999)}", "07_school_safety_and_hygiene_rules",
        "School Safety and Hygiene Compliance", prompt, correct, distractors, sol,
        {"tier_1": "Identify what safety or cleanliness hazard exists for learners at school.",
         "tier_2": "Schools enforce rules preventing fires, glass injuries, and unhygienic food handling.",
         "tier_3": fix},
        ["neglects_school_safety_compliance"]
    )


def arch_08_team_role_allocation_by_strengths(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    area = sc["area"]
    n1, n2, n3 = rng.sample(NAMES, 3)
    prompt = (
        f"In {area}, three learners form an Entrepreneur's Day group:\n"
        f"- {n1} writes funny scripts well but gets nervous speaking to crowds.\n"
        f"- {n2} loves acting, projecting their voice, and engaging strangers.\n"
        f"- {n3} excels at mental arithmetic and neat cash tallying.\n\n"
        f"Which role split matches each learner's strengths?"
    )
    correct = f"{n1}: writes promotional skit/poster copy; {n2}: performs live stall promotion/sales pitch; {n3}: manages cash float and bookkeeping"
    distractors = [
        f"{n1}: handles loud intercom shouting; {n2}: stays silently behind books; {n3}: avoids counting any cash",
        "Force every shy learner to shout alone while others watch without jobs",
        "Assign all three roles at random by tossing a coin without checking skills",
    ]
    sol = (
        f"Step 1: Match group strengths:\n"
        f"Curriculum guidance recommends letting shy strong writers compose promotional scripts ({n1}), "
        f"confident performers attract customers ({n2}), and numerate members safeguard finances ({n3})."
    )
    return _mcq_q(
        rng, f"g7_ed_08_{rng.randint(100000, 999999)}", "08_team_role_allocation_by_strengths",
        "Group Strength Allocation", prompt, correct, distractors, sol,
        {"tier_1": "Pair each member with tasks matching their natural strengths.",
         "tier_2": "Writing fits introverted scriptwriters; live pitches suit confident speakers; numbers suit cashiers.",
         "tier_3": f"Assign copywriting to {n1}, live promotion to {n2}, and finances to {n3}."},
        ["ignores_team_skill_fit"]
    )


def arch_09_sourcing_startup_loan_options(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    need_amt = rng.choice([120, 160, 200, 250])
    prompt = (
        f"{person} in {area} needs R{need_amt} as a short-term start-up loan to buy baking ingredients for Entrepreneur's Day. "
        f"List THREE realistic people or local sources {person} could approach for this loan and explain one condition you should agree on before borrowing. (4 marks)"
    )
    sample = (
        f"1. Immediate family members (parents, caregivers, or older siblings).\n"
        f"2. Extended family (grandparents, aunts, uncles) or trusted community leaders.\n"
        f"3. Local community businesses or religious/community organisations.\n"
        f"Condition: Agree clearly on paying back the R{need_amt} capital from Entrepreneur's Day sales receipts before spending profit."
    )
    pts = [
        "Immediate family (parents, caregivers, older siblings) [1 mark]",
        "Extended family (grandparents, uncles, aunts) or community mentors [1 mark]",
        "Local small businesses or community organisations [1 mark]",
        "Clear repayment agreement from sales proceeds [1 mark]",
    ]
    sol = "Marking Rubric (4 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ed_09_{rng.randint(100000, 999999)}", "09_sourcing_startup_loan_options",
        "Entrepreneur's Day Start-up Loan Sources", prompt, sample, pts, sol,
        {"tier_1": "Think about realistic people near a Grade 7 learner (family and local community).",
         "tier_2": "Mention family, extended relatives, community organisations or local shops, plus repayment terms.",
         "tier_3": f"Examples: parents/caregivers, grandparents, local spaza/shop owner, with repayment of R{need_amt} agreed."},
        ["unrealistic_corporate_bank_loan"]
    )


def arch_10_repaying_startup_loans_with_interest(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    loan = rng.choice([100, 150, 200, 250])
    fee_pct = rng.choice([10, 20])
    interest = loan * fee_pct // 100
    repay = loan + interest
    sales = loan + rng.choice([220, 260, 310, 350])
    net_keep = sales - repay
    prompt = (
        f"{person} in {area} borrows R{loan} from an older sibling to buy supplies, agreeing to repay the loan plus a {fee_pct}% "
        f"thank-you return after Entrepreneur's Day. If {person}'s stall collects R{sales} in cash sales (with no extra unpaid bills), "
        f"how much net profit does {person} keep after repaying the loan and {fee_pct}% return?"
    )
    ans = f"R{net_keep}"
    sol = (
        f"Step 1: Calculate return/interest on R{loan} at {fee_pct}%:\n"
        f"Interest = {fee_pct}% of R{loan} = R{interest}\n"
        f"Step 2: Total repayment = R{loan} + R{interest} = R{repay}\n"
        f"Step 3: Remaining cash kept by {person} = R{sales} - R{repay} = R{net_keep}."
    )
    return _calc_q(
        rng, f"g7_ed_10_{rng.randint(100000, 999999)}", "10_repaying_startup_loans_with_interest",
        "Repaying Seed Loan and Profit Split", prompt, ans, sol,
        {"tier_1": f"First add the {fee_pct}% return to the borrowed R{loan}.",
         "tier_2": f"Repayment is R{loan} + R{interest}. Subtract that total from R{sales}.",
         "tier_3": f"R{sales} - R{repay} = R{net_keep}."},
        ["forgets_loan_principal_repayment"]
    )


def arch_11_detailed_materials_checklist_planning(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    craft = rng.choice(["greeting cards", "tie-dye T-shirts", "beaded bookmarks", "decorated herb jars"])
    prompt = (
        f"When sourcing materials to craft {craft} for Entrepreneur's Day, why should {person}'s team list every single item "
        f"required—even glue, string, and tape—before visiting the store?"
    )
    correct = "To capture hidden consumable costs accurately, avoid last-minute delays, and prevent overspending the budget"
    distractors = [
        "Because small items like glue and tape cost nothing at retail shops",
        "So that the group buys double quantities of random decorations just in case",
        "Because Income and Expenditure Statements exclude glue and tape by law",
    ]
    sol = (
        f"Step 1: Materials sourcing discipline:\n"
        f"Curriculum guidance stresses listing every item down to the last drop of glue. Forgotten small items "
        f"cause emergency trips, raise total costs, and erode net profit on {craft}."
    )
    return _mcq_q(
        rng, f"g7_ed_11_{rng.randint(100000, 999999)}", "11_detailed_materials_checklist_planning",
        "Comprehensive Materials Checklist", prompt, correct, distractors, sol,
        {"tier_1": "What happens to your budget if you forget small consumables like glue and ribbon?",
         "tier_2": "Omitted items cause unbudgeted expenses and production stoppages.",
         "tier_3": "Full itemised lists keep costs within budget and prevent shortages."},
        ["omits_small_consumable_costs"]
    )


def arch_12_supplier_price_comparison_shopping(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, sup1, sup2 = sc["entrepreneur"], sc["supplier"], sc["competitor"]
    packs = rng.choice([4, 5, 6])
    p1 = rng.choice([22, 24, 26, 28])
    p2 = p1 - rng.choice([3, 4])
    transport_extra = rng.choice([0, 5])
    total1 = packs * p1
    total2 = packs * p2 + transport_extra
    cheaper = sup2 if total2 < total1 else sup1
    diff = abs(total1 - total2)
    prompt = (
        f"{person} needs {packs} bulk packs of popcorn kernels for Entrepreneur's Day. "
        f"{sup1} sells each pack for R{p1} (free walk-in pickup), whereas {sup2} charges R{p2} per pack plus "
        f"R{transport_extra} taxi/delivery cost in total.\n\n"
        f"How much money does {person} save by buying from the cheaper supplier ({cheaper})?"
    )
    ans = f"R{diff}"
    sol = (
        f"Step 1: Cost at {sup1} = {packs} * R{p1} = R{total1}\n"
        f"Step 2: Cost at {sup2} = ({packs} * R{p2}) + R{transport_extra} = R{packs * p2} + R{transport_extra} = R{total2}\n"
        f"Step 3: Saving from choosing {cheaper} = |R{total1} - R{total2}| = R{diff}."
    )
    return _calc_q(
        rng, f"g7_ed_12_{rng.randint(100000, 999999)}", "12_supplier_price_comparison_shopping",
        "Comparing Supplier Costs Including Delivery", prompt, ans, sol,
        {"tier_1": "Compare the total cost (pack price * packs + any delivery fee) at both suppliers.",
         "tier_2": f"{sup1}: R{total1}. {sup2}: {packs}*R{p2} + R{transport_extra} = R{total2}.",
         "tier_3": f"Difference = R{diff}."},
        ["ignores_transport_cost_in_comparison"]
    )


def arch_13_lead_time_and_advance_ordering(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    days = rng.choice([10, 14, 21])
    prompt = (
        f"{person} wants to include custom-printed badge pins requiring a {days}-day courier delivery time from the supplier. "
        f"Entrepreneur's Day takes place in 5 days.\n\n"
        f"What planning mistake did {person} make, and how should future procurement be timed?"
    )
    correct = "Failing to source hard-to-find inputs well ahead of time; specialty orders require ordering weeks early or switching to locally stocked materials"
    distractors = [
        "Paying the courier after Entrepreneur's Day makes shipping arrive 10 days earlier",
        "Waiting until the morning of the market speeds up supplier manufacturing automatically",
        "Printing blank stickers on the stall tablecloth generates the missing badge pins instantly",
    ]
    sol = (
        f"Step 1: Procurement lead time principle:\n"
        f"Ordering inputs requiring {days} days only 5 days beforehand guarantees stock will not arrive in time. "
        f"Always source materials well ahead of time or choose readily available local substitutes."
    )
    return _mcq_q(
        rng, f"g7_ed_13_{rng.randint(100000, 999999)}", "13_lead_time_and_advance_ordering",
        "Advance Procurement and Lead Times", prompt, correct, distractors, sol,
        {"tier_1": "Compare the delivery lead time against the days remaining before the event.",
         "tier_2": f"{days} days delivery > 5 days remaining means the goods arrive too late.",
         "tier_3": "Source specialist goods weeks in advance or substitute local stock."},
        ["ignores_supplier_lead_time"]
    )


def arch_14_perishable_goods_production_scheduling(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    food = rng.choice(["cream-filled cupcakes", "fresh fruit salads", "vetkoek with mince", "iced lemon scones"])
    prompt = (
        f"{person}'s group plans to sell {food} at Entrepreneur's Day on Friday.\n\n"
        f"Which production schedule balances freshness with reliable completion?"
    )
    correct = "Pre-prepare dry non-perishable packaging early in the week, then bake/assemble fresh perishable items the evening before or morning of Friday"
    distractors = [
        f"Make all {food} two full weeks in advance and store them unrefrigerated under a school desk",
        "Begin shopping for flour and fruit 15 minutes before the first school break starts",
        "Bake half the batch a month before and mix old stock with raw dough on Friday",
    ]
    sol = (
        f"Step 1: Time management for perishable products:\n"
        f"{food.capitalize()} spoil quickly if prepared weeks ahead, yet starting everything on the morning risks delays. "
        f"Prepare signage, boxes, and dry mixes earlier, and finish fresh food preparation immediately before the market."
    )
    return _mcq_q(
        rng, f"g7_ed_14_{rng.randint(100000, 999999)}", "14_perishable_goods_production_scheduling",
        "Scheduling Perishable Goods Production", prompt, correct, distractors, sol,
        {"tier_1": "Fresh foods spoil if stored too long, so consider splitting dry prep from fresh cooking.",
         "tier_2": "Pack boxes and posters early; cook/assemble perishables right before selling.",
         "tier_3": correct},
        ["poor_perishable_scheduling"]
    )


def arch_15_division_of_labour_production_line(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    qty = rng.choice([40, 60, 80, 100])
    s1, s2, s3 = rng.sample(NAMES, 3)
    item = rng.choice(["gift jars", "sandwiches", "candy bags", "bookmarks"])
    svg_body = (
        f'<text x="290" y="26" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">Group Production System: {qty} {item}</text>'
        f'<rect x="20" y="55" width="150" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="95" y="88" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e3a8a">Step 1: Prep</text>'
        f'<text x="95" y="108" font-size="11" text-anchor="middle" fill="#1e40af">{s1}</text>'
        f'<line x1="170" y1="95" x2="210" y2="95" stroke="#475569" stroke-width="2" marker-end="url(#arr)"/>'
        f'<rect x="215" y="55" width="150" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="290" y="88" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">Step 2: Assemble</text>'
        f'<text x="290" y="108" font-size="11" text-anchor="middle" fill="#166534">{s2}</text>'
        f'<line x1="365" y1="95" x2="405" y2="95" stroke="#475569" stroke-width="2"/>'
        f'<rect x="410" y="55" width="150" height="80" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="485" y="88" font-size="12" font-weight="bold" text-anchor="middle" fill="#78350f">Step 3: Package</text>'
        f'<text x="485" y="108" font-size="11" text-anchor="middle" fill="#92400e">{s3}</text>'
        f'<text x="290" y="178" font-size="12" text-anchor="middle" fill="#334155">Batch target: {qty} units finished in parallel flow</text>'
    )
    prompt = (
        f"Study the three-stage group workflow diagram showing how {s1}, {s2}, and {s3} organise producing {qty} {item}.\n\n"
        f"Why does assigning specialised stages in a group assembly system beat having each learner make items completely alone?"
    )
    correct = "Specialisation and teamwork speed up manufacturing, maintain uniform quality, and ensure all units finish before Entrepreneur's Day"
    distractors = [
        "Having every member fetch separate tools for every step reduces communication",
        "Working sequentially one person at a time guarantees longer completion time and higher wages",
        "Assembly lines automatically halve the price of raw ingredients at retail shops",
    ]
    sol = (
        f"Step 1: Analyse the division of labour across {s1} (Prep), {s2} (Assemble), and {s3} (Package):\n"
        f"Splitting the {qty}-unit batch into specialised sequential steps eliminates wasted tool changes, keeps quality consistent, "
        f"and finishes production faster through teamwork."
    )
    return _mcq_q(
        rng, f"g7_ed_15_{rng.randint(100000, 999999)}", "15_division_of_labour_production_line",
        "Team Manufacturing System", prompt, correct, distractors, sol,
        {"tier_1": "Look at how Prep, Assemble, and Package divide work across three learners.",
         "tier_2": "Repeating one focused task improves speed and consistency.",
         "tier_3": correct},
        ["fails_to_recognise_division_of_labour"],
        diagram_spec=_svg_spec(svg_body, 580, 200),
    )


def arch_16_recycled_materials_cost_and_eco_benefits(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    qty = rng.choice([25, 30, 40, 50])
    new_jar_cost = rng.choice([6, 8, 9])
    saved = qty * new_jar_cost
    prompt = (
        f"{person} makes mini succulent pots for Entrepreneur's Day. Buying {qty} new ceramic pots costs R{new_jar_cost} per pot, "
        f"but {person} collects clean used glass jars and tin cans from family and neighbours for R0.\n\n"
        f"Calculate how much expense {person} saves, and name one environmental benefit."
    )
    ans = f"R{saved} saved; reduces landfill waste and conserves raw resources"
    sol = (
        f"Step 1: Cost saving calculation:\n"
        f"Avoided pot purchase = {qty} * R{new_jar_cost} = R{saved}.\n"
        f"Step 2: Environmental & profit impact:\n"
        f"Using recycled jars costs R0, boosts net profit by R{saved}, and keeps solid waste out of landfills."
    )
    return _calc_q(
        rng, f"g7_ed_16_{rng.randint(100000, 999999)}", "16_recycled_materials_cost_and_eco_benefits",
        "Recycled Packaging Savings", prompt, ans, sol,
        {"tier_1": "Multiply the number of jars by the avoided cost per new pot.",
         "tier_2": f"Money saved = {qty} * R{new_jar_cost}; plus think about landfill reduction.",
         "tier_3": f"R{saved} saved and less waste goes to landfill."},
        ["ignores_zero_cost_recycled_benefit"], marks=3,
    )


def arch_17_marketing_mix_product_quality_packaging(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    prod = rng.choice(["homemade fudge squares", "iced biscuits", "mini caramel popcorn", "scented bath salts"])
    prompt = (
        f"Under the Marketing Mix (**Product** element), {person} sells {prod}. "
        f"Which decision directly strengthens the **Product** aspect of the venture?"
    )
    correct = f"Ensuring consistent taste/quality, hygienic sealed packaging, and an appealing look for {prod}"
    distractors = [
        "Choosing a shaded spot near the main tuckshop walkway",
        "Putting colourful flyers on the school noticeboard on Monday",
        "Lowering the ticket price from R10 to R8 during final break",
    ]
    sol = (
        f"Step 1: Distinguish the 4 Ps of marketing:\n"
        f"- Product: quality, design, packaging, and features of {prod}.\n"
        f"- Place: stand location; Promotion: flyers/intercom; Price: R8/R10 pricing."
    )
    return _mcq_q(
        rng, f"g7_ed_17_{rng.randint(100000, 999999)}", "17_marketing_mix_product_quality_packaging",
        "Marketing Mix: Product", prompt, correct, distractors, sol,
        {"tier_1": "Separate decisions about location, adverts, and price from the item itself.",
         "tier_2": "Product decisions govern quality, hygiene, portion size, and packaging.",
         "tier_3": correct},
        ["confuses_product_with_promotion_or_place"]
    )


def arch_18_marketing_mix_place_foot_traffic_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    spot_a_buyers = rng.choice([220, 260, 300])
    spot_c_buyers = rng.choice([30, 45, 55])
    prod = rng.choice(["cold fruit slushies", "ice lollies", "warm boerewors rolls"])
    svg_body = (
        f'<text x="290" y="24" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">School Grounds Stand Placement Zones</text>'
        f'<rect x="30" y="45" width="165" height="120" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="112" y="75" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">Zone A: Main Quad Gate</text>'
        f'<text x="112" y="98" font-size="11" text-anchor="middle" fill="#166534">Shaded + power plug</text>'
        f'<text x="112" y="118" font-size="11" text-anchor="middle" fill="#166534">{spot_a_buyers} learners pass/hr</text>'
        f'<rect x="215" y="45" width="165" height="120" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="297" y="75" font-size="12" font-weight="bold" text-anchor="middle" fill="#78350f">Zone B: Library Alley</text>'
        f'<text x="297" y="98" font-size="11" text-anchor="middle" fill="#92400e">Quiet study area</text>'
        f'<text x="297" y="118" font-size="11" text-anchor="middle" fill="#92400e">No food permitted</text>'
        f'<rect x="400" y="45" width="155" height="120" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="477" y="75" font-size="12" font-weight="bold" text-anchor="middle" fill="#7f1d1d">Zone C: Far Back Fence</text>'
        f'<text x="477" y="98" font-size="11" text-anchor="middle" fill="#991b1b">Direct hot sun</text>'
        f'<text x="477" y="118" font-size="11" text-anchor="middle" fill="#991b1b">{spot_c_buyers} learners pass/hr</text>'
    )
    prompt = (
        f"Study the school placement diagram comparing Zones A, B, and C for {person}'s {prod} stall.\n\n"
        f"Which zone best satisfies the **Place** element of the 4 Ps, and why?"
    )
    correct = f"Zone A (Main Quad Gate) — highest foot traffic ({spot_a_buyers} learners/hr), shade, and utility access"
    distractors = [
        f"Zone C (Far Back Fence) — only {spot_c_buyers} learners pass, keeping the stall peaceful",
        "Zone B (Library Alley) — quiet corridor where food sales are forbidden",
        "Zone C (Far Back Fence) — direct afternoon sun preserves cold drinks longer",
    ]
    sol = (
        f"Step 1: Evaluate the Place requirement:\n"
        f"Zone A combines high buyer visibility ({spot_a_buyers} learners/hr) with shade and power, whereas Zone B prohibits food "
        f"and Zone C suffers low traffic ({spot_c_buyers} learners/hr)."
    )
    return _mcq_q(
        rng, f"g7_ed_18_{rng.randint(100000, 999999)}", "18_marketing_mix_place_foot_traffic_svg",
        "Marketing Mix: Place & Visibility", prompt, correct, distractors, sol,
        {"tier_1": "Look at foot traffic numbers and stall rules in each zone.",
         "tier_2": f"Compare {spot_a_buyers} learners/hr in shade vs {spot_c_buyers} in direct sun or library restrictions.",
         "tier_3": f"Zone A wins with {spot_a_buyers} learners/hr and proper access."},
        ["ignores_foot_traffic_placement"],
        diagram_spec=_svg_spec(svg_body, 580, 190),
    )


def arch_19_marketing_mix_price_pocket_money_fit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    avg_pocket = rng.choice([20, 25, 30])
    unit_cost = rng.choice([4, 5, 6])
    right_price = rng.choice([8, 10, 12])
    too_high = avg_pocket + 15
    prompt = (
        f"{person} finds via market research that typical learners bring R{avg_pocket} to Entrepreneur's Day. "
        f"Each cupcake costs R{unit_cost} to bake.\n\n"
        f"Which selling price demonstrates effective **Price** strategy for the 4 Ps?"
    )
    correct = f"R{right_price} — exceeds the R{unit_cost} unit cost to earn profit while fitting well within R{avg_pocket} pocket money"
    distractors = [
        f"R{too_high} — higher than almost any learner's R{avg_pocket} total spending money",
        f"R{unit_cost - 2} — priced below unit cost so every cupcake loses money",
        "R0 — giving away stock ensures customers feel satisfied",
    ]
    sol = (
        f"Step 1: Balance cost coverage and affordability:\n"
        f"Price must sit above cost (R{unit_cost}) so the venture makes money, yet stay affordable for learners carrying R{avg_pocket}."
    )
    return _mcq_q(
        rng, f"g7_ed_19_{rng.randint(100000, 999999)}", "19_marketing_mix_price_pocket_money_fit",
        "Marketing Mix: Price Calibration", prompt, correct, distractors, sol,
        {"tier_1": "Price must cover production cost AND match what buyers carry.",
         "tier_2": f"Compare options against R{unit_cost} cost and R{avg_pocket} average pocket money.",
         "tier_3": correct},
        ["prices_above_market_willingness"]
    )


def arch_20_marketing_mix_creative_school_promotion(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    tactic = rng.choice(["a 60-second comedy skit at assembly", "a catchy jingle and mascot costume", "a bright school intercom teaser and posters"])
    prompt = (
        f"{person}'s stall in {area} promotes its snacks using {tactic} instead of paid city radio ads.\n\n"
        f"Why does this exemplify smart Entrepreneur's Day **Promotion**?"
    )
    correct = "It captures learner attention creatively inside school at minimal cost, reaching the exact target buyers"
    distractors = [
        "City commuters 30 km away should hear about Grade 7 break-time cupcakes",
        "Funny skits eliminate the legal need to record sales income later",
        "Low-cost promotion reduces product quality automatically",
    ]
    sol = (
        f"Step 1: Evaluate promotion choice:\n"
        f"Using {tactic} excites peers directly where they learn, costs almost nothing, and protects net profit."
    )
    return _mcq_q(
        rng, f"g7_ed_20_{rng.randint(100000, 999999)}", "20_marketing_mix_creative_school_promotion",
        "Creative School Promotion", prompt, correct, distractors, sol,
        {"tier_1": "Ask whether city ads or direct school engagement reaches learners cheaply.",
         "tier_2": "Targeted creative promotion creates hype among classmates without draining funds.",
         "tier_3": correct},
        ["overspends_on_mass_media"]
    )


def arch_21_poster_design_five_principles_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    stall_name = rng.choice(["BERRY BLAST", "CRUNCH ZONE", "SOLAR CHILL", "SUGAR SWIRL"])
    price = rng.choice([8, 10, 12])
    svg_body = (
        f'<text x="290" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Comparison of Two Advertising Posters</text>'
        f'<rect x="30" y="42" width="245" height="170" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="152" y="65" font-size="12" font-weight="bold" text-anchor="middle" fill="#7f1d1d">Poster A (Cluttered)</text>'
        f'<text x="45" y="90" font-size="9" fill="#991b1b">Tiny text paragraph explaining every step</text>'
        f'<text x="45" y="106" font-size="9" fill="#991b1b">of baking since 1998, blue poster for red booth,</text>'
        f'<text x="45" y="122" font-size="9" fill="#991b1b">no stand location or price shown anywhere!</text>'
        f'<rect x="305" y="42" width="245" height="170" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>'
        f'<text x="427" y="68" font-size="16" font-weight="bold" text-anchor="middle" fill="#065f46">{stall_name} - R{price}</text>'
        f'<text x="427" y="100" font-size="12" text-anchor="middle" fill="#047857">Fresh Cupcakes @ Quad Table 4</text>'
        f'<text x="427" y="126" font-size="11" text-anchor="middle" fill="#065f46">Bold logo • Matching green theme</text>'
        f'<text x="427" y="152" font-size="11" text-anchor="middle" fill="#065f46">Friday Break • Poster B</text>'
    )
    prompt = (
        f"Compare Poster A and Poster B in the illustration for {stall_name} (R{price}).\n\n"
        f"Which THREE advertising poster rules from the curriculum explain why Poster B outperforms Poster A?"
    )
    correct = "Readable from a distance without clutter, gives clear product/price/location info, and matches the stand's colour identity"
    distractors = [
        "Uses tiny paragraphs so shoppers must stand 5 cm away to decipher every detail",
        f"Hides both stand location and R{price} selling price to keep buyers guessing",
        "Mixes clashing blue poster ink with a red-themed stand to confuse foot traffic",
    ]
    sol = (
        f"Step 1: Apply the five poster design principles:\n"
        f"Poster B displays '{stall_name} - R{price}' cleanly from far away, avoids heavy clutter, states location (Quad Table 4) & time, "
        f"and matches the booth's colour theme."
    )
    return _mcq_q(
        rng, f"g7_ed_21_{rng.randint(100000, 999999)}", "21_poster_design_five_principles_svg",
        "Effective Poster Design Rules", prompt, correct, distractors, sol,
        {"tier_1": "Check distance readability, clutter, stand info, and colour consistency.",
         "tier_2": "Compare Poster A's missing location/clutter against Poster B.",
         "tier_3": correct},
        ["cluttered_uninformative_poster"],
        diagram_spec=_svg_spec(svg_body, 580, 230),
    )


def arch_22_colour_identity_consistency(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    theme = rng.choice([("red-and-white", "blue"), ("yellow-and-black", "purple"), ("forest-green", "bright pink")])
    main_c, clash_c = theme
    prompt = (
        f"{person} wraps every product box and decorates the stand tablecloth in {main_c} branding. "
        f"However, a teammate wants to paint all hallway directional posters {clash_c}.\n\n"
        f"Why should {person} keep the posters in {main_c} instead of switching to {clash_c}?"
    )
    correct = "Consistent colours build a unified brand identity so buyers instantly recognise the stall from afar"
    distractors = [
        f"{clash_c.capitalize()} paint is banned from all South African schools by national law",
        "Changing colour on every sign increases unit production speed by 50%",
        "Buyers ignore colourful stalls unless every surface uses seven unrelated shades",
    ]
    sol = (
        f"Step 1: Brand colour identity rule:\n"
        f"Curriculum poster rules emphasise using consistent colour ({main_c}) across posters, packaging, and stand decorations "
        f"so buyers recognise and remember your stand immediately."
    )
    return _mcq_q(
        rng, f"g7_ed_22_{rng.randint(100000, 999999)}", "22_colour_identity_consistency",
        "Colour Identity Across Stand and Posters", prompt, correct, distractors, sol,
        {"tier_1": "How does colour help customers connect posters in hallways to your stand?",
         "tier_2": "Consistent colours link advertisements visually to your booth.",
         "tier_3": correct},
        ["breaks_brand_colour_unity"]
    )


def arch_23_display_stand_stability_and_visibility_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    heavy_item = rng.choice([
        ("heavy ceramic pot plants", "strong cardboard/wood braces with wide base"),
        ("full cups of hot chocolate", "level, steady base so hot liquid will not spill"),
        ("stacked cupcake jars", "stepped tiers so back rows stay visible above front items"),
    ])
    item, req = heavy_item
    tier_h = rng.choice([8, 10, 12])
    svg_body = (
        f'<text x="290" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Tiered Display Stand Cross-Section</text>'
        f'<rect x="90" y="150" width="380" height="35" fill="#d97706" stroke="#78350f" stroke-width="2"/>'
        f'<rect x="140" y="110" width="280" height="40" fill="#f59e0b" stroke="#78350f" stroke-width="2"/>'
        f'<rect x="190" y="70" width="180" height="40" fill="#fbbf24" stroke="#78350f" stroke-width="2"/>'
        f'<text x="280" y="95" font-size="11" font-weight="bold" text-anchor="middle" fill="#451a03">Top Tier ({tier_h} cm) - Rear Display</text>'
        f'<text x="280" y="135" font-size="11" font-weight="bold" text-anchor="middle" fill="#451a03">Mid Tier - Wide &amp; Balanced</text>'
        f'<text x="280" y="172" font-size="11" font-weight="bold" text-anchor="middle" fill="#451a03">Wide Base - Supports {item}</text>'
    )
    prompt = (
        f"Study the tiered display stand design (top step height {tier_h} cm) intended for selling {item}.\n\n"
        f"Explain THREE structural or visual requirements a good Entrepreneur's Day display stand must meet before testing it with full stock. (4 marks)"
    )
    sample = (
        f"1. Strong and steady: Must carry weight safely without wobbling or tipping when shoppers lift items ({req}).\n"
        f"2. Well-balanced: Remains stable even after front-row stock has been sold.\n"
        f"3. Stepped visibility & eco-friendly: Displays back goods clearly above front ones, ideally built attractively from recycled cardboard/wood."
    )
    pts = [
        f"Strength & steadiness suited to {item} ({req}) [1 mark]",
        "Balance even when partial stock is removed by buyers [1 mark]",
        "Clear visibility of all items (none hidden behind front rows) [1 mark]",
        "Attractive appearance and smart use of recycled materials to cut costs [1 mark]",
    ]
    sol = f"Marking Rubric (4 marks, {tier_h} cm tiered stand for {item}):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ed_23_{rng.randint(100000, 999999)}", "23_display_stand_stability_and_visibility_svg",
        "Display Stand Design Engineering", prompt, sample, pts, sol,
        {"tier_1": f"Think about safety, visibility, balance when stock sells, and materials for {item}.",
         "tier_2": "A stand needs strength, weight balance after partial removal, clear stepped visibility, and recycled materials.",
         "tier_3": sample},
        ["neglects_display_balance_or_strength"],
        diagram_spec=_svg_spec(svg_body, 580, 200),
    )


def arch_24_special_offer_bundle_revenue_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    unit_p = rng.choice([6, 8, 10])
    cost_p = rng.choice([2, 3, 4])
    bundle_count = rng.choice([8, 10, 12])
    # "Buy 2, get 1 free" -> 3 units delivered, customer pays for 2 -> bundle price = 2 * unit_p
    rev_per_bundle = 2 * unit_p
    cost_per_bundle = 3 * cost_p
    total_profit = bundle_count * (rev_per_bundle - cost_per_bundle)
    prompt = (
        f"{person} advertises a special offer on bracelets: 'Buy 2 at R{unit_p} each, get 1 free!' "
        f"Each bracelet costs R{cost_p} to bead (total 3 bracelets per bundle). "
        f"If {bundle_count} customers take this 3-bracelet offer, calculate the **net profit** earned from these bundles (ignoring stall fees)."
    )
    ans = f"R{total_profit}"
    sol = (
        f"Step 1: Revenue per bundle = 2 paid * R{unit_p} = R{rev_per_bundle}.\n"
        f"Step 2: Cost of all 3 bracelets in each bundle = 3 * R{cost_p} = R{cost_per_bundle}.\n"
        f"Step 3: Profit per bundle = R{rev_per_bundle} - R{cost_per_bundle} = R{rev_per_bundle - cost_per_bundle}.\n"
        f"Step 4: Total net profit across {bundle_count} bundles = {bundle_count} * R{rev_per_bundle - cost_per_bundle} = R{total_profit}."
    )
    return _calc_q(
        rng, f"g7_ed_24_{rng.randint(100000, 999999)}", "24_special_offer_bundle_revenue_impact",
        "Special Offer Promotional Profit", prompt, ans, sol,
        {"tier_1": "Careful: you still pay production cost for the free third bracelet!",
         "tier_2": f"Bundle income = R{rev_per_bundle}; cost of 3 items = R{cost_per_bundle}. Multiply profit by {bundle_count}.",
         "tier_3": f"R{total_profit}"},
        ["forgets_cost_of_free_bonus_item"]
    )


def arch_25_budget_discipline_overspending_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    planned_exp = rng.choice([140, 180, 220])
    impulse_extra = rng.choice([35, 45, 55])
    actual_exp = planned_exp + impulse_extra
    sales = planned_exp + rng.choice([160, 200, 240])
    planned_profit = sales - planned_exp
    actual_profit = sales - actual_exp
    prompt = (
        f"{person} budgeted R{planned_exp} in expenses and achieved R{sales} in sales on Entrepreneur's Day (planned profit: R{planned_profit}). "
        f"However, while shopping, {person} impulse-bought unbudgeted glitter and ribbon costing an extra R{impulse_extra}.\n\n"
        f"Calculate {person}'s **actual net profit** after this budget overrun."
    )
    ans = f"R{actual_profit}"
    sol = (
        f"Step 1: Compute actual total expenses:\n"
        f"Actual Expenses = R{planned_exp} + R{impulse_extra} = R{actual_exp}.\n"
        f"Step 2: Actual Net Profit = R{sales} - R{actual_exp} = R{actual_profit} "
        f"(every R1 overspent reduces profit by R1)."
    )
    return _calc_q(
        rng, f"g7_ed_25_{rng.randint(100000, 999999)}", "25_budget_discipline_overspending_impact",
        "Impact of Overspending Budget on Profit", prompt, ans, sol,
        {"tier_1": "Extra unbudgeted spending directly lowers net profit.",
         "tier_2": f"Subtract the extra R{impulse_extra} from the planned profit of R{planned_profit}.",
         "tier_3": f"R{actual_profit}"},
        ["adds_overspend_to_profit"]
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_aim_and_purpose_of_entrepreneurs_day": arch_01_aim_and_purpose_of_entrepreneurs_day,
    "02_preparation_step_order_sequence": arch_02_preparation_step_order_sequence,
    "03_market_research_buyer_surveys": arch_03_market_research_buyer_surveys,
    "04_low_cost_high_demand_product_choice": arch_04_low_cost_high_demand_product_choice,
    "05_complementary_goods_pairing": arch_05_complementary_goods_pairing,
    "06_creative_stall_naming_branding": arch_06_creative_stall_naming_branding,
    "07_school_safety_and_hygiene_rules": arch_07_school_safety_and_hygiene_rules,
    "08_team_role_allocation_by_strengths": arch_08_team_role_allocation_by_strengths,
    "09_sourcing_startup_loan_options": arch_09_sourcing_startup_loan_options,
    "10_repaying_startup_loans_with_interest": arch_10_repaying_startup_loans_with_interest,
    "11_detailed_materials_checklist_planning": arch_11_detailed_materials_checklist_planning,
    "12_supplier_price_comparison_shopping": arch_12_supplier_price_comparison_shopping,
    "13_lead_time_and_advance_ordering": arch_13_lead_time_and_advance_ordering,
    "14_perishable_goods_production_scheduling": arch_14_perishable_goods_production_scheduling,
    "15_division_of_labour_production_line": arch_15_division_of_labour_production_line,
    "16_recycled_materials_cost_and_eco_benefits": arch_16_recycled_materials_cost_and_eco_benefits,
    "17_marketing_mix_product_quality_packaging": arch_17_marketing_mix_product_quality_packaging,
    "18_marketing_mix_place_foot_traffic_svg": arch_18_marketing_mix_place_foot_traffic_svg,
    "19_marketing_mix_price_pocket_money_fit": arch_19_marketing_mix_price_pocket_money_fit,
    "20_marketing_mix_creative_school_promotion": arch_20_marketing_mix_creative_school_promotion,
    "21_poster_design_five_principles_svg": arch_21_poster_design_five_principles_svg,
    "22_colour_identity_consistency": arch_22_colour_identity_consistency,
    "23_display_stand_stability_and_visibility_svg": arch_23_display_stand_stability_and_visibility_svg,
    "24_special_offer_bundle_revenue_impact": arch_24_special_offer_bundle_revenue_impact,
    "25_budget_discipline_overspending_impact": arch_25_budget_discipline_overspending_impact,
}
