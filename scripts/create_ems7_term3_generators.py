"""
Script to generate the 4 dedicated Grade 7 EMS Term 3 generators:
1. term3_the_entrepreneur.py
2. term3_entrepreneurs_day.py
3. term3_businesses.py
4. term3_starting_a_business.py
All 100% grounded in curriculum_docs_auto/EMS_Gr7/Term 3/
"""

import os

base_dir = os.path.join("caps-ai-backend", "app", "utils", "grade7_ems")

# ============================================================================
# 1. term3_the_entrepreneur.py
# ============================================================================
code_entrepreneur = '''"""Grade 7 EMS: Term 3 - The Entrepreneur Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. The entrepreneur.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "def_entrepreneur",
    "entrepreneurial_traits",
    "needs_wants_opportunity",
    "explain_imbalances",
    "def_poverty_line"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/01. The entrepreneur.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_def_entrepreneur(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    biz = sc["business_type"]
    prompt = (
        f"{person} from {area} identifies a local market need, invests personal savings to start a new {biz}, "
        f"hires local workers, and takes the risk of financial loss to earn a profit.\\n\\n"
        f"Which term best defines {person}'s role in the South African economy?"
    )
    correct_opt = "An entrepreneur"
    options = [
        "An entrepreneur",
        "A civil service regulator",
        "A passive financial investor",
        "A non-profit volunteer"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand the economic definition:\\n"
        f"An entrepreneur is an individual who identifies unmet business opportunities, combines the factors of production "
        f"(land, labour, capital), and assumes the financial risk of starting and operating a business for profit.\\n\\n"
        f"Step 2: Connect to scenario:\\n"
        f"{person} took the risk to start {biz} in {area}. Therefore, {person} is an entrepreneur."
    )
    return {
        "id": f"g7_ems_ent_def_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "def_entrepreneur",
        "question_family_id": "def_entrepreneur",
        "curriculum_reference": "Term 3 > The entrepreneur > Definition of an entrepreneur",
        "hints": {
            "tier_1": "Think about the person who takes financial risks to turn ideas into profitable businesses.",
            "tier_2": "Look for the key economic agent that combines land, labour, and capital.",
            "tier_3": "An entrepreneur is someone who starts and runs a business venture taking on risk."
        },
        "misconception_tags": ["entrepreneur_vs_employee_confusion"]
    }


def _build_entrepreneurial_traits(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    traits_data = [
        ("perseverance and resilience", "keeps marketing and improving recipes despite failing to make sales during the first two months"),
        ("innovative and creative thinking", "designs a foldable solar-powered charger using recycled plastics to solve local load shedding issues"),
        ("calculated risk-taking", "resigns from a salaried position to open a bakery after conducting thorough market research"),
        ("self-discipline and organisation", "wakes up at 04:30 daily to bake fresh bread, update financial ledgers, and manage supplier deliveries")
    ]
    trait, behavior = rng.choice(traits_data)
    prompt = (
        f"Consider {person} in {area}, who {behavior}.\\n\\n"
        f"Which core characteristic of a successful entrepreneur is directly demonstrated?"
    )
    correct_opt = trait.capitalize()
    distractors = [t[0].capitalize() for t in traits_data if t[0] != trait]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Analyze the entrepreneurial behavior:\\n"
        f"{behavior}.\\n\\n"
        f"Step 2: Match with CAPS curriculum characteristics:\\n"
        f"Successful entrepreneurs demonstrate key traits: perseverance, creative problem solving, risk-taking, and self-discipline.\\n\\n"
        f"Conclusion: The demonstrated characteristic is {trait}."
    )
    return {
        "id": f"g7_ems_ent_trait_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "entrepreneurial_traits",
        "question_family_id": "entrepreneurial_traits",
        "curriculum_reference": "Term 3 > The entrepreneur > Characteristics of an entrepreneur",
        "hints": {
            "tier_1": "Observe what the person is doing in the face of challenges or new ideas.",
            "tier_2": "Match the specific action described in the prompt to the matching characteristic.",
            "tier_3": f"The action specifically illustrates {trait}."
        },
        "misconception_tags": ["generic_trait_misclassification"]
    }


def _build_needs_wants_opportunity(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    cases = [
        ("commuters waiting in long queues at the train station who have no access to breakfast", "a mobile cart selling affordable fresh muffins, coffee, and fruit", "Needs for breakfast and food on the go"),
        ("school learners who have torn school bags during rainy seasons", "repairing and producing waterproof school backpack covers from recycled materials", "Needs for protecting study materials and dry transport"),
        ("residents in an informal settlement walking 5 km to buy prepaid electricity tokens", "setting up a local community vendor kiosk for instant utility top-ups", "Needs for local access to essential household utilities")
    ]
    problem, solution_idea, need_type = rng.choice(cases)
    prompt = (
        f"In {area}, {person} notices that {problem}. {person} decides to address this by {solution_idea}.\\n\\n"
        f"How does this initiative illustrate the entrepreneurial process?"
    )
    correct_opt = "Identifying an unmet community need and converting it into a viable business opportunity"
    options = [
        correct_opt,
        "Operating an illegal monopoly to prevent competition",
        "Creating artificial luxury wants through aggressive marketing",
        "Relying entirely on government grants without selling goods"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify the problem:\\n"
        f"{problem}. This represents {need_type}.\\n\\n"
        f"Step 2: Connect to entrepreneurial actions:\\n"
        f"Entrepreneurs succeed by observing gaps in the market where consumer needs are unmet and providing accessible, value-adding solutions."
    )
    return {
        "id": f"g7_ems_ent_opp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "needs_wants_opportunity",
        "question_family_id": "needs_wants_opportunity",
        "curriculum_reference": "Term 3 > The entrepreneur > Entrepreneurial actions: Buying, selling, producing",
        "hints": {
            "tier_1": "Think about how observing community difficulties leads to business creation.",
            "tier_2": "Entrepreneurs find solutions to real-world consumer problems.",
            "tier_3": "The entrepreneur spots an unmet need and creates a business solution."
        },
        "misconception_tags": ["needs_vs_wants_confusion"]
    }


def _build_explain_imbalances(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"South Africa faces high rates of youth unemployment and poverty. Explain TWO ways in which encouraging "
        f"entrepreneurs like {person} in {area} helps reduce socio-economic imbalances. (4 marks)"
    )
    marking_points = [
        "Entrepreneurs create direct employment for themselves and others in the community.",
        "They generate household income, enabling families to afford basic survival needs.",
        "They stimulate local economic circulation and small business development (SMMEs).",
        "They foster innovation and local service delivery in historically disadvantaged areas."
    ]
    sample_answer = (
        "Firstly, entrepreneurs create new jobs for local jobseekers, reducing unemployment and providing households "
        "with stable wage income to meet their basic needs. Secondly, local businesses circulate money within the community, "
        "developing small business infrastructure and empowering disadvantaged communities to achieve economic independence."
    )
    sol = (
        "Marking Rubric (2 marks per point, max 4 marks):\\n"
        "1. Job creation and income generation: Reducing dependency by employing workers and paying wages (2 marks).\\n"
        "2. Economic development: Circulating wealth locally and developing community SMME capacity (2 marks)."
    )
    return {
        "id": f"g7_ems_ent_imbal_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "explain_imbalances",
        "question_family_id": "explain_imbalances",
        "curriculum_reference": "Term 3 > The entrepreneur > Unemployment and wealth creation in South Africa",
        "hints": {
            "tier_1": "Focus on jobs and income circulation.",
            "tier_2": "Point 1: Employment creation. Point 2: Wealth generation and poverty alleviation.",
            "tier_3": "Explain how hiring workers and earning business profits reduces inequality."
        },
        "misconception_tags": ["vague_unemployment_explanation"]
    }


def _build_def_poverty_line(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    area = sc["area"]
    prompt = (
        f"Statistics South Africa publishes the Food Poverty Line and Upper-Bound Poverty Line. "
        f"What is the economic definition of the **poverty line** in South Africa?"
    )
    correct_opt = "The minimum monthly income required to purchase sufficient food and essential non-food items to survive"
    options = [
        correct_opt,
        "The highest tax bracket payable by luxury commercial enterprises",
        "The average salary earned by corporate executives in Johannesburg",
        "The total amount of money deposited into a commercial bank account"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition from official National Curriculum Statement:\\n"
        "The poverty line is the minimum threshold of income deemed necessary to achieve an adequate standard of living, "
        "covering basic dietary requirements (nutritional intake) and essential shelter/clothing.\\n\\n"
        "Step 2: Application:\\n"
        "Individuals living below this threshold cannot meet their basic physiological survival needs."
    )
    return {
        "id": f"g7_ems_ent_pov_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "def_poverty_line",
        "question_family_id": "def_poverty_line",
        "curriculum_reference": "Term 3 > The entrepreneur > The poverty line and basic needs",
        "hints": {
            "tier_1": "Think about the minimum amount of money needed to buy basic food to survive.",
            "tier_2": "The poverty line is a benchmark for essential living requirements.",
            "tier_3": "It is the minimum income needed to afford adequate food and essential necessities."
        },
        "misconception_tags": ["poverty_line_tax_confusion"]
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()

    builders = {
        "def_entrepreneur": _build_def_entrepreneur,
        "entrepreneurial_traits": _build_entrepreneurial_traits,
        "needs_wants_opportunity": _build_needs_wants_opportunity,
        "explain_imbalances": _build_explain_imbalances,
        "def_poverty_line": _build_def_poverty_line
    }

    if target in builders:
        return [builders[target](rng) for _ in range(count)]

    # Substring match
    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]

    # Mixed rotation
    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
'''

# ============================================================================
# 2. term3_entrepreneurs_day.py
# ============================================================================
code_entrepreneurs_day = '''"""Grade 7 EMS: Term 3 - Entrepreneur's Day Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "planning_entrepreneurs_day",
    "promotional_channels",
    "variable_costs_production",
    "calculate_profit_simple"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_planning_entrepreneurs_day(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    item = rng.choice(["fruit smoothies", "beaded keyholders", "homemade popcorn", "decorated bookmarks", "baked cupcakes"])
    prompt = (
        f"A Grade 7 class in {area} prepares to host an Entrepreneur's Day. {person} plans a stall selling {item}.\\n\\n"
        f"Which step should {person} take FIRST before purchasing any materials?"
    )
    correct_opt = "Conduct market research among fellow learners to confirm demand and willingness to pay"
    options = [
        correct_opt,
        "Spend all available personal money immediately on packaging boxes",
        "Sign a long-term lease contract for commercial off-campus premises",
        "Hire adult staff members on fixed monthly contracts"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand planning for Entrepreneur's Day:\\n"
        f"Before committing financial capital to produce {item}, the learner must conduct market research "
        f"to determine whether there is sufficient customer demand and what price learners can afford.\\n\\n"
        f"Step 2: Conclusion:\\n"
        f"Market research prevents wasting money on unwanted products."
    )
    return {
        "id": f"g7_ems_day_plan_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "planning_entrepreneurs_day",
        "question_family_id": "planning_entrepreneurs_day",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Hosting an Entrepreneur's Day",
        "hints": {
            "tier_1": "What must you know about your customers before you spend money making a product?",
            "tier_2": "You need to find out if learners actually want to buy what you plan to sell.",
            "tier_3": "Conduct market research first to confirm customer demand and price expectations."
        },
        "misconception_tags": ["premature_spending_planning_error"]
    }


def _build_promotional_channels(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    stall_prod = rng.choice(["freshly squeezed lemonade", "ice lollies", "handmade cards", "pancake treats"])
    prompt = (
        f"{person} wants to advertise a {stall_prod} stall for Entrepreneur's Day at school in {area}.\\n\\n"
        f"Which promotional strategy is the most cost-effective and appropriate for a school market?"
    )
    correct_opt = "Colourful noticeboard posters, intercom announcements, and word-of-mouth promotion"
    options = [
        correct_opt,
        "Purchasing expensive prime-time television commercial slots on national TV",
        "Taking out a full-page colour advert in a national weekly Sunday newspaper",
        "Placing large commercial highway billboards outside the town"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Principles of school advertising (The 4 Ps - Promotion):\\n"
        f"Advertising must be targeted directly at the intended market (learners and teachers) at low cost.\\n\\n"
        f"Step 2: Evaluate options:\\n"
        f"Television and billboards are extremely expensive and reach outside audiences. School posters, intercom notices, "
        f"and word-of-mouth are targeted, highly effective, and virtually free."
    )
    return {
        "id": f"g7_ems_day_promo_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "promotional_channels",
        "question_family_id": "promotional_channels",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Principles of advertising and marketing",
        "hints": {
            "tier_1": "Consider who the customers are (school learners) and how to reach them cheaply.",
            "tier_2": "Look for promotional methods that cost little or nothing and reach learners at school.",
            "tier_3": "Posters on school noticeboards and intercom announcements are ideal for school stalls."
        },
        "misconception_tags": ["inappropriate_mass_media_choice"]
    }


def _build_variable_costs_production(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"At an Entrepreneur's Day stall in {area}, {person} rents a stall table for a fixed fee of R20, "
        f"and buys ingredients (milk, sugar, flavouring) costing R3 per ice lolly produced.\\n\\n"
        f"Which cost item is classified as a **variable cost**, and why?"
    )
    correct_opt = "The ingredients (R3 per lolly), because total ingredient costs change with the number of units produced"
    options = [
        correct_opt,
        "The table rental (R20), because it changes every time an ice lolly is sold",
        "Neither, because all business costs are permanently fixed",
        "Both, because all production expenses are identical"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define cost concepts:\\n"
        "- Fixed cost: Costs that remain constant regardless of output volume (e.g. table rental of R20).\\n"
        "- Variable cost: Costs that increase or decrease in direct proportion to the number of units produced (e.g. ingredients at R3 per unit).\\n\\n"
        "Step 2: Conclusion:\\n"
        "The ingredients are a variable cost because total expense directly depends on how many lollies are made."
    )
    return {
        "id": f"g7_ems_day_varcost_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "variable_costs_production",
        "question_family_id": "variable_costs_production",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Fixed vs variable costs",
        "hints": {
            "tier_1": "Ask yourself: which expense changes if you produce 100 units instead of 10 units?",
            "tier_2": "Variable costs vary with production volume; fixed costs stay the same.",
            "tier_3": "Ingredients change with quantity produced, making them variable costs."
        },
        "misconception_tags": ["fixed_variable_cost_inversion"]
    }


def _build_calculate_profit_simple(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    item_sold = rng.choice(["cupcakes", "muffins", "hotdogs", "smoothies"])
    
    qty = rng.choice([30, 40, 50, 60])
    selling_price = rng.choice([8, 10, 12, 15])
    cost_per_unit = rng.choice([4, 5, 6])
    stall_fee = rng.choice([20, 25, 30])
    
    total_income = qty * selling_price
    total_expenses = (qty * cost_per_unit) + stall_fee
    profit = total_income - total_expenses
    
    prompt = (
        f"For Entrepreneur's Day, {person} in {area} sells {qty} {item_sold} at R{selling_price} each. "
        f"The production ingredients cost R{cost_per_unit} per {item_sold[:-1] if item_sold.endswith('s') else item_sold}, "
        f"and the school stall fee is R{stall_fee}.\\n\\n"
        f"Calculate the **net profit** earned by {person}'s stall."
    )
    correct_opt = f"R{profit}"
    distractors = [
        f"R{total_income}",
        f"R{total_expenses}",
        f"R{total_income - (qty * cost_per_unit)}",
        f"R{profit + 20}"
    ]
    options = [correct_opt] + [d for d in distractors if d != correct_opt][:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Calculate Total Income (Revenue):\\n"
        f"Total Income = {qty} units × R{selling_price} = R{total_income}\\n\\n"
        f"Step 2: Calculate Total Expenses:\\n"
        f"Ingredient Cost = {qty} × R{cost_per_unit} = R{qty * cost_per_unit}\\n"
        f"Stall Fee (Fixed Cost) = R{stall_fee}\\n"
        f"Total Expenses = R{qty * cost_per_unit} + R{stall_fee} = R{total_expenses}\\n\\n"
        f"Step 3: Calculate Net Profit:\\n"
        f"Profit = Total Income - Total Expenses = R{total_income} - R{total_expenses} = R{profit}"
    )
    return {
        "id": f"g7_ems_day_prof_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "calculate_profit_simple",
        "question_family_id": "calculate_profit_simple",
        "curriculum_reference": "Term 3 > Entrepreneur's Day > Income and Expenditure Statement and profit",
        "hints": {
            "tier_1": "Profit = Total Income minus Total Expenses.",
            "tier_2": f"Total income is {qty} × R{selling_price} = R{total_income}. Now subtract all ingredient and stall costs.",
            "tier_3": f"R{total_income} - R{total_expenses} = R{profit}."
        },
        "misconception_tags": ["revenue_profit_confusion", "omitted_fixed_cost"]
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()

    builders = {
        "planning_entrepreneurs_day": _build_planning_entrepreneurs_day,
        "promotional_channels": _build_promotional_channels,
        "variable_costs_production": _build_variable_costs_production,
        "calculate_profit_simple": _build_calculate_profit_simple
    }

    if target in builders:
        return [builders[target](rng) for _ in range(count)]

    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]

    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
'''

# ============================================================================
# 3. term3_starting_a_business.py
# ============================================================================
code_starting_a_business = '''"""Grade 7 EMS: Term 3 - Starting a Business Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/03. Starting a business.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "swot_factors",
    "swot_case_study_exam",
    "explain_goals",
    "start_business_steps"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/03. Starting a business.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_swot_factors(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    factors = [
        ("Strength (Internal)", "has certified pastry baking training and owns commercial baking equipment", "Internal positive attribute of the business owner"),
        ("Weakness (Internal)", "has zero bookkeeping experience and struggles to manage cash flow", "Internal limitation or deficiency within the business"),
        ("Opportunity (External)", "a new office park opens nearby with 400 employees seeking lunch", "External positive market trend outside the business control"),
        ("Threat (External)", "a large supermarket chain opens a discount bakery across the street", "External risk or competitive danger from the outside environment")
    ]
    swot_type, scenario_desc, expl = rng.choice(factors)
    prompt = (
        f"{person} plans to start a bakery in {area} and conducts a SWOT analysis. "
        f"The business {scenario_desc}.\\n\\n"
        f"Which quadrant of the SWOT analysis does this represent?"
    )
    correct_opt = swot_type
    options = [
        "Strength (Internal)",
        "Weakness (Internal)",
        "Opportunity (External)",
        "Threat (External)"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand SWOT analysis categories:\\n"
        f"- Strengths: Internal advantages/skills inside the business.\\n"
        f"- Weaknesses: Internal shortcomings or lack of resources inside the business.\\n"
        f"- Opportunities: External favourable market factors in the outside environment.\\n"
        f"- Threats: External risks and challenges from competitors or economic conditions.\\n\\n"
        f"Step 2: Conclusion:\\n"
        f"This scenario represents {swot_type} because it is an {expl.lower()}."
    )
    return {
        "id": f"g7_ems_start_swot_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "swot_factors",
        "question_family_id": "swot_factors",
        "curriculum_reference": "Term 3 > Starting a business > SWOT analysis elements",
        "hints": {
            "tier_1": "Is this factor internal (inside the business) or external (outside in the environment)?",
            "tier_2": "Positive internal factors are Strengths; negative internal factors are Weaknesses; positive external factors are Opportunities; negative external factors are Threats.",
            "tier_3": f"This factor is classified as {swot_type}."
        },
        "misconception_tags": ["swot_internal_external_confusion"]
    }


def _build_swot_case_study_exam(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    biz = sc["business_type"]
    prompt = (
        f"Case Study: {person} operates {biz} in {area}. Study the following business facts:\\n"
        f"1. Highly skilled staff who deliver excellent craftsmanship.\\n"
        f"2. Insufficient startup capital to purchase modern electric machinery.\\n"
        f"3. High demand from local builders for timber products.\\n"
        f"4. Frequent load shedding disrupts daily production.\\n\\n"
        f"Identify ONE **Strength** and ONE **Threat** from the facts listed above."
    )
    correct_opt = "Strength: Fact 1 (Highly skilled staff) | Threat: Fact 4 (Load shedding disruptions)"
    options = [
        "Strength: Fact 1 (Highly skilled staff) | Threat: Fact 4 (Load shedding disruptions)",
        "Strength: Fact 2 (Insufficient capital) | Threat: Fact 3 (High demand)",
        "Strength: Fact 4 (Load shedding) | Threat: Fact 1 (Skilled staff)",
        "Strength: Fact 3 (High demand) | Threat: Fact 2 (Insufficient capital)"
    ]
    rng.shuffle(options)
    sol = (
        "Analysis of SWOT facts:\\n"
        "- Fact 1 (Skilled staff): Internal positive capability = STRENGTH.\\n"
        "- Fact 2 (Insufficient capital): Internal negative limitation = WEAKNESS.\\n"
        "- Fact 3 (High builder demand): External positive market trend = OPPORTUNITY.\\n"
        "- Fact 4 (Load shedding): External negative infrastructure threat = THREAT.\\n\\n"
        "Conclusion: Fact 1 is a Strength and Fact 4 is a Threat."
    )
    return {
        "id": f"g7_ems_start_case_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "swot_case_study_exam",
        "question_family_id": "swot_case_study_exam",
        "curriculum_reference": "Term 3 > Starting a business > SWOT analysis case study",
        "hints": {
            "tier_1": "Remember: Strengths are internal positives; Threats are external negative forces.",
            "tier_2": "Skilled staff comes from within the team; power blackouts come from the external power grid.",
            "tier_3": "Fact 1 is the Strength and Fact 4 is the Threat."
        },
        "misconception_tags": ["swot_matrix_mapping_error"]
    }


def _build_explain_goals(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"{person} is starting a new venture in {area}. Explain why setting **SMART goals** is essential "
        f"for business success, and state what the acronym 'SMART' stands for. (4 marks)"
    )
    sample_answer = (
        "SMART stands for: Specific, Measurable, Achievable, Realistic, and Time-bound.\\n\\n"
        "Setting SMART goals is essential because it gives the business clear direction, prevents aimless spending, "
        "enables the owner to track progress against targets, and motivates staff to achieve specific milestones within a set deadline."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. SMART acronym defined correctly: Specific, Measurable, Achievable, Realistic, Time-bound (2 marks).\\n"
        "2. Explanation of importance: Provides direction, enables measurement of progress, and sets deadlines (2 marks)."
    )
    return {
        "id": f"g7_ems_start_goals_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "explain_goals",
        "question_family_id": "explain_goals",
        "curriculum_reference": "Term 3 > Starting a business > Setting and achieving business goals",
        "hints": {
            "tier_1": "List the five letters of SMART and explain how goals help guide a business.",
            "tier_2": "S = Specific, M = Measurable, A = Achievable, R = Realistic, T = Time-bound.",
            "tier_3": "Explain that goals give direction and allow tracking of financial success."
        },
        "misconception_tags": ["vague_goal_definition"]
    }


def _build_start_business_steps(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"Which sequence correctly outlines the logical steps {person} in {area} must follow when starting a new business?"
    )
    correct_opt = "1. Identify business idea → 2. Conduct market research → 3. Formulate business plan & budget → 4. Secure startup capital → 5. Launch & produce"
    options = [
        correct_opt,
        "1. Launch & produce → 2. Secure startup capital → 3. Conduct market research → 4. Formulate business plan",
        "1. Secure loan → 2. Launch production → 3. Formulate business idea → 4. Conduct market research",
        "1. Pay rent for premises → 2. Hire 10 staff → 3. Decide on product idea → 4. Draft budget"
    ]
    rng.shuffle(options)
    sol = (
        "Correct Stepwise Pathway for Starting a Business:\\n"
        "1. Identify a viable business idea based on consumer needs.\\n"
        "2. Conduct market research to confirm customer interest and pricing.\\n"
        "3. Draw up a detailed business plan including costings and budget.\\n"
        "4. Secure required startup capital (savings, loans, grants).\\n"
        "5. Purchase materials, set up operations, and officially launch the business."
    )
    return {
        "id": f"g7_ems_start_steps_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "start_business_steps",
        "question_family_id": "start_business_steps",
        "curriculum_reference": "Term 3 > Starting a business > Startup pathway and planning",
        "hints": {
            "tier_1": "You must have an idea and do research before you write a business plan or borrow money.",
            "tier_2": "Idea comes first, followed by market research, planning, funding, then launch.",
            "tier_3": "The logical sequence begins with identifying the idea and ends with launch."
        },
        "misconception_tags": ["premature_startup_launch_error"]
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()

    builders = {
        "swot_factors": _build_swot_factors,
        "swot_case_study_exam": _build_swot_case_study_exam,
        "explain_goals": _build_explain_goals,
        "start_business_steps": _build_start_business_steps
    }

    if target in builders:
        return [builders[target](rng) for _ in range(count)]

    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]

    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
'''

# ============================================================================
# 4. term3_businesses.py
# ============================================================================
code_businesses = '''"""Grade 7 EMS: Term 3 - Businesses Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "formal_informal_classification",
    "service_business_classification",
    "households_producers_explanation",
    "informal_business_advantages",
    "epidemics_impact"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/02. Businesses.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_formal_informal_classification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    examples = [
        ("operates a registered accounting consultancy with a formal business registration number, pays VAT and company tax, and leases permanent office suites", "Formal business", "Registered with SARS/CIPC, pays taxes, operates from fixed commercial premises"),
        ("sells fresh fruit, snacks, and phone cards from a temporary street-corner wooden stall, keeps no formal written accounts, and is not registered with SARS", "Informal business", "Unregistered with authorities, cash-based, operates without fixed legal structures"),
        ("runs a licensed pharmacy chain with 15 branches, employs 60 registered pharmacists, and complies with national labour regulations", "Formal business", "Legally registered company adhering to official regulations and payroll taxes"),
        ("cuts grass and prunes garden hedges for neighborhood homes using personal hand tools, receiving cash payments daily without formal invoices", "Informal business", "Unregistered micro-enterprise, cash transactions, zero formal regulatory paperwork")
    ]
    biz_desc, biz_type, rationale = rng.choice(examples)
    prompt = (
        f"In {area}, {person} {biz_desc}.\\n\\n"
        f"Is this business classified as a **formal business** or an **informal business**, and what is the defining characteristic?"
    )
    correct_opt = f"{biz_type}, because it is {rationale.lower()}."
    alt_type = "Informal business" if biz_type == "Formal business" else "Formal business"
    options = [
        correct_opt,
        f"{alt_type}, because all small businesses in South Africa are legally exempt from registration",
        f"{alt_type}, because any business that makes a cash profit is automatically formal",
        "Neither, because individual businesses cannot be classified by formal economic status"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Classification standards from Curriculum Reference:\\n"
        f"- Formal business: Legally registered with government bodies (CIPC, SARS), pays corporate and employment taxes, operates from fixed commercial premises, and complies with labour laws.\\n"
        f"- Informal business: Not legally registered, operates mainly in cash, keeps minimal formal records, and has no legal protection.\\n\\n"
        f"Step 2: Conclusion:\\n"
        f"{person}'s venture is a {biz_type} because it is {rationale.lower()}."
    )
    return {
        "id": f"g7_ems_bus_class_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "formal_informal_classification",
        "question_family_id": "formal_informal_classification",
        "curriculum_reference": "Term 3 > Businesses > Formal and informal businesses",
        "hints": {
            "tier_1": "Check whether the business is officially registered with SARS and has fixed formal premises.",
            "tier_2": "Formal businesses are registered and pay tax; informal businesses operate without official registration.",
            "tier_3": f"This business is classified as a {biz_type}."
        },
        "misconception_tags": ["formal_informal_tax_confusion"]
    }


def _build_service_business_classification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    types = [
        ("Trading business", "buys packaged clothing from wholesalers and sells them directly to retail shoppers at a markup"),
        ("Manufacturing business", "purchases raw pine timber, cuts and assembles dining tables and chairs for sale"),
        ("Service business", "provides professional electrical installation, maintenance, and wiring repairs for homeowners")
    ]
    chosen_type, chosen_desc = rng.choice(types)
    prompt = (
        f"In {area}, {person} operates an enterprise that {chosen_desc}.\\n\\n"
        f"Into which business type does this enterprise fall?"
    )
    correct_opt = chosen_type
    options = ["Trading business", "Manufacturing business", "Service business", "Extraction syndicate"]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand the three primary types of businesses:\\n"
        "- Trading business: Buys finished goods and resells them at a higher price without altering them.\\n"
        "- Manufacturing business: Converts raw materials into new finished physical products.\\n"
        "- Service business: Provides specialised labour, skills, or intellectual expertise rather than tangible goods.\\n\\n"
        f"Step 2: Conclusion:\\n"
        f"Because this enterprise {chosen_desc}, it is a {chosen_type}."
    )
    return {
        "id": f"g7_ems_bus_type_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "service_business_classification",
        "question_family_id": "service_business_classification",
        "curriculum_reference": "Term 3 > Businesses > Types of businesses: Trading, manufacturing, service",
        "hints": {
            "tier_1": "Is the business making goods from raw materials, buying and reselling goods, or providing a skill?",
            "tier_2": "Trading = buying and selling; Manufacturing = making new goods; Service = offering skills/work.",
            "tier_3": f"This business is classified as a {chosen_type}."
        },
        "misconception_tags": ["trading_vs_service_confusion"]
    }


def _build_households_producers_explanation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"In {area}, households interact daily with formal and informal businesses. "
        f"Explain the dual role of **households** as both consumers and producers in the economic cycle. (4 marks)"
    )
    sample_answer = (
        "Households act as consumers because they spend their earned income to purchase finished goods and services "
        "produced by businesses to satisfy their personal needs and wants. Simultaneously, households act as producers "
        "because household members supply the essential factors of production—namely their labour, skills, entrepreneurial ideas, "
        "and capital—to businesses, without which businesses cannot produce output."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Households as consumers: Spend wages/income to buy goods and services to satisfy needs and wants (2 marks).\\n"
        "2. Households as producers: Provide the factors of production (labour, skills, land, capital) to businesses (2 marks)."
    )
    return {
        "id": f"g7_ems_bus_house_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "households_producers_explanation",
        "question_family_id": "households_producers_explanation",
        "curriculum_reference": "Term 3 > Businesses > Role of households as producers and consumers",
        "hints": {
            "tier_1": "Households buy goods (consumers) and supply their work/labour to businesses (producers).",
            "tier_2": "Explain what households buy from businesses and what households provide to businesses.",
            "tier_3": "Consumers buy products; producers supply factors of production like labour."
        },
        "misconception_tags": ["household_role_omission"]
    }


def _build_informal_business_advantages(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"{person} decides to open an informal spaza shop in {area} rather than registering a formal company immediately.\\n\\n"
        f"Which statement correctly identifies ONE key advantage and ONE key disadvantage of running an **informal business**?"
    )
    correct_opt = "Advantage: Low startup costs and minimal legal bureaucracy | Disadvantage: No legal protection and difficult access to commercial bank loans"
    options = [
        correct_opt,
        "Advantage: Guaranteed multi-million Rand government contracts | Disadvantage: Compulsory corporate tax audits every week",
        "Advantage: Unlimited legal liability protection | Disadvantage: Forbidden from trading with cash",
        "Advantage: Automatic listing on the Johannesburg Stock Exchange | Disadvantage: Cannot hire family members"
    ]
    rng.shuffle(options)
    sol = (
        "Analysis of Informal Business Pros and Cons:\\n"
        "- Advantages: Very low startup capital needed, flexible operating hours, zero costly legal registration fees, direct cash flow.\\n"
        "- Disadvantages: No formal bank loan access (lack of credit history), vulnerable to municipal confiscation or crime, no worker benefits, no legal entity status.\\n\\n"
        "Conclusion: Low startup costs is an advantage, while lack of legal protection and loan access is a disadvantage."
    )
    return {
        "id": f"g7_ems_bus_adv_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "informal_business_advantages",
        "question_family_id": "informal_business_advantages",
        "curriculum_reference": "Term 3 > Businesses > Advantages and disadvantages of informal businesses",
        "hints": {
            "tier_1": "Think about why informal businesses are easy to start, but hard to grow through commercial bank loans.",
            "tier_2": "Informal businesses have low barriers to entry but lack formal legal protections.",
            "tier_3": "Low startup cost is the advantage; difficulty obtaining loans is the disadvantage."
        },
        "misconception_tags": ["informal_business_privilege_misconception"]
    }


def _build_epidemics_impact(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    area = sc["area"]
    prompt = (
        f"Explain how widespread health epidemics (such as HIV/AIDS or tuberculosis) and natural disasters (like floods) "
        f"impact workforce productivity and business continuity in South Africa. (4 marks)"
    )
    sample_answer = (
        "Health epidemics lead to increased worker absenteeism, fatigue, and lost production hours as employees fall ill "
        "or take time off to care for sick relatives. This forces businesses to incur higher training costs to replace skilled workers. "
        "Natural disasters damage infrastructure, destroy stock and transport links, and interrupt water and electricity supply, "
        "causing temporary or permanent business closures and lost sales."
    )
    sol = (
        "Marking Rubric (4 marks total):\\n"
        "1. Impact of epidemics: Increased absenteeism, loss of experienced labour, reduced productivity, and retraining costs (2 marks).\\n"
        "2. Impact of disasters: Physical destruction of premises/stock, supply chain disruption, and loss of trading revenue (2 marks)."
    )
    return {
        "id": f"g7_ems_bus_epid_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "epidemics_impact",
        "question_family_id": "epidemics_impact",
        "curriculum_reference": "Term 3 > Businesses > Effect of natural disasters and health epidemics on businesses",
        "hints": {
            "tier_1": "Discuss worker sickness/absenteeism and physical destruction of stock/premises.",
            "tier_2": "Epidemics cause absenteeism and lost skills; disasters destroy infrastructure and halt production.",
            "tier_3": "Address both lost labour hours and damage to physical business operations."
        },
        "misconception_tags": ["vague_epidemic_answer"]
    }


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()

    builders = {
        "formal_informal_classification": _build_formal_informal_classification,
        "service_business_classification": _build_service_business_classification,
        "households_producers_explanation": _build_households_producers_explanation,
        "informal_business_advantages": _build_informal_business_advantages,
        "epidemics_impact": _build_epidemics_impact
    }

    if target in builders:
        return [builders[target](rng) for _ in range(count)]

    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]

    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
'''

with open(os.path.join(base_dir, "term3_the_entrepreneur.py"), "w", encoding="utf-8") as f:
    f.write(code_entrepreneur)
print("Wrote term3_the_entrepreneur.py")

with open(os.path.join(base_dir, "term3_entrepreneurs_day.py"), "w", encoding="utf-8") as f:
    f.write(code_entrepreneurs_day)
print("Wrote term3_entrepreneurs_day.py")

with open(os.path.join(base_dir, "term3_starting_a_business.py"), "w", encoding="utf-8") as f:
    f.write(code_starting_a_business)
print("Wrote term3_starting_a_business.py")

with open(os.path.join(base_dir, "term3_businesses.py"), "w", encoding="utf-8") as f:
    f.write(code_businesses)
print("Wrote term3_businesses.py")
