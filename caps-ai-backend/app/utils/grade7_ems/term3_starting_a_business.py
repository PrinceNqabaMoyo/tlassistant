"""Grade 7 EMS: Term 3 - Starting a Business Generator.
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
        f"The business {scenario_desc}.\n\n"
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
        f"Step 1: Understand SWOT analysis categories:\n"
        f"- Strengths: Internal advantages/skills inside the business.\n"
        f"- Weaknesses: Internal shortcomings or lack of resources inside the business.\n"
        f"- Opportunities: External favourable market factors in the outside environment.\n"
        f"- Threats: External risks and challenges from competitors or economic conditions.\n\n"
        f"Step 2: Conclusion:\n"
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
        f"Case Study: {person} operates {biz} in {area}. Study the following business facts:\n"
        f"1. Highly skilled staff who deliver excellent craftsmanship.\n"
        f"2. Insufficient startup capital to purchase modern electric machinery.\n"
        f"3. High demand from local builders for timber products.\n"
        f"4. Frequent load shedding disrupts daily production.\n\n"
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
        "Analysis of SWOT facts:\n"
        "- Fact 1 (Skilled staff): Internal positive capability = STRENGTH.\n"
        "- Fact 2 (Insufficient capital): Internal negative limitation = WEAKNESS.\n"
        "- Fact 3 (High builder demand): External positive market trend = OPPORTUNITY.\n"
        "- Fact 4 (Load shedding): External negative infrastructure threat = THREAT.\n\n"
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
        "SMART stands for: Specific, Measurable, Achievable, Realistic, and Time-bound.\n\n"
        "Setting SMART goals is essential because it gives the business clear direction, prevents aimless spending, "
        "enables the owner to track progress against targets, and motivates staff to achieve specific milestones within a set deadline."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. SMART acronym defined correctly: Specific, Measurable, Achievable, Realistic, Time-bound (2 marks).\n"
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
        "Correct Stepwise Pathway for Starting a Business:\n"
        "1. Identify a viable business idea based on consumer needs.\n"
        "2. Conduct market research to confirm customer interest and pricing.\n"
        "3. Draw up a detailed business plan including costings and budget.\n"
        "4. Secure required startup capital (savings, loans, grants).\n"
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
