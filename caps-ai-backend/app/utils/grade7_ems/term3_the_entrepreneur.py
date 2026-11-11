"""Grade 7 EMS: Term 3 - The Entrepreneur Generator.
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
        f"hires local workers, and takes the risk of financial loss to earn a profit.\n\n"
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
        f"Step 1: Understand the economic definition:\n"
        f"An entrepreneur is an individual who identifies unmet business opportunities, combines the factors of production "
        f"(land, labour, capital), and assumes the financial risk of starting and operating a business for profit.\n\n"
        f"Step 2: Connect to scenario:\n"
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
        f"Consider {person} in {area}, who {behavior}.\n\n"
        f"Which core characteristic of a successful entrepreneur is directly demonstrated?"
    )
    correct_opt = trait.capitalize()
    distractors = [t[0].capitalize() for t in traits_data if t[0] != trait]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Analyze the entrepreneurial behavior:\n"
        f"{behavior}.\n\n"
        f"Step 2: Match with national curriculum characteristics:\n"
        f"Successful entrepreneurs demonstrate key traits: perseverance, creative problem solving, risk-taking, and self-discipline.\n\n"
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
        f"In {area}, {person} notices that {problem}. {person} decides to address this by {solution_idea}.\n\n"
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
        f"Step 1: Identify the problem:\n"
        f"{problem}. This represents {need_type}.\n\n"
        f"Step 2: Connect to entrepreneurial actions:\n"
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
        "Marking Rubric (2 marks per point, max 4 marks):\n"
        "1. Job creation and income generation: Reducing dependency by employing workers and paying wages (2 marks).\n"
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
    scenarios = [
        f"In a regional economic assessment of households in {area}, researchers analyzed the national poverty threshold.",
        f"During a municipal development survey in {area}, community workers evaluated household survival budgets.",
        f"In an economic report analyzing income levels in {area}, analysts evaluated living standards against national benchmarks."
    ]
    intro = rng.choice(scenarios)
    prompt = (
        f"{intro} According to official South African economic standards, what is the definition of the **poverty line**?"
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
        "Step 1: Definition from official National Curriculum Statement:\n"
        "The poverty line is the minimum threshold of income deemed necessary to achieve an adequate standard of living, "
        "covering basic dietary requirements (nutritional intake) and essential shelter/clothing.\n\n"
        "Step 2: Application:\n"
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
