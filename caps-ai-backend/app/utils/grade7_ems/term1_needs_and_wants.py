"""Grade 7 EMS: Term 1 - Needs and Wants Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 1/02. Needs and Wants.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, get_random_need_and_want, NAMES, AREAS

SUBSKILLS = [
    "primary_vs_secondary_needs",
    "needs_vs_wants_classification",
    "the_basic_economic_problem",
    "community_service_delivery_needs",
    "scarcity_and_choice_evaluation"
]

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 1/02. Needs and Wants.md"


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _build_primary_vs_secondary(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]

    pairs = [
        ("clean drinking water from a municipal tap", "an expensive gaming console", "water is essential for physiological survival, whereas a gaming console is non-essential entertainment"),
        ("a basic warm blanket in winter", "designer label sneakers", "warmth protects health and life, whereas designer shoes are luxury desires"),
        ("nutritious maize meal and vegetables", "imported soft drinks and candy", "food provides essential bodily nutrition, whereas candy is a non-essential luxury preference"),
        ("safe shelter with a roof", "a home theatre entertainment system", "shelter protects against the elements for survival, whereas home theatre is for comfort and luxury")
    ]
    need_item, want_item, rationale = rng.choice(pairs)

    prompt = (
        f"{person} from {area} receives a household stipend and must choose between buying "
        f"**{need_item}** and **{want_item}**.\n\n"
        f"Classify which item is a **primary need** and explain the economic difference."
    )
    correct_opt = f"Primary need: {need_item}; because {rationale}."
    distractors = [
        f"Primary need: {want_item}; because luxuries motivate people to work harder in the economy.",
        f"Both are secondary needs; because modern consumers in South Africa require both equally to live.",
        f"Both are wants; because primary needs only exist in traditional subsistence societies."
    ]
    options = [correct_opt] + distractors
    rng.shuffle(options)

    sol = (
        f"Step 1: Define Primary Needs:\n"
        f"Primary needs are things that are strictly essential for human physical survival (food, clean water, basic shelter, basic clothing).\n\n"
        f"Step 2: Define Secondary Needs & Wants:\n"
        f"Wants are desires for goods and services that are not essential for survival but improve comfort, status, or enjoyment.\n\n"
        f"Step 3: Evaluate items:\n"
        f"- {need_item} is essential to sustain life -> Primary need.\n"
        f"- {want_item} is for entertainment/comfort -> Want.\n\n"
        f"Conclusion: {correct_opt}"
    )
    return {
        "id": f"g7_ems_needs_prim_{rng.randint(100000, 999999)}",
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
        "subskill": "primary_vs_secondary_needs",
        "question_family_id": "primary_vs_secondary_needs",
        "curriculum_reference": "Term 1 > Needs and Wants > Categorizing Needs",
        "hints": {
            "tier_1": "Would a person's life or health be immediately threatened without this item?",
            "tier_2": "Primary needs = survival (food, water, shelter). Wants = luxuries and comfort.",
            "tier_3": f"Correct: {correct_opt}"
        }
    }


def _build_needs_vs_wants_classification(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]

    item_lists = [
        ([("Access to basic healthcare", "Need"), ("Cell phone with internet", "Want"), ("Maize meal and milk", "Need"), ("Jacuzzi bath", "Want")], 0),
        ([("Clean running tap water", "Need"), ("Designer sports shoes", "Want"), ("Warm school jersey", "Need"), ("Playstation console", "Want")], 0),
        ([("Hygienic sanitation and clean toilet", "Need"), ("Luxury overseas holiday", "Want"), ("Basic bread and fruit", "Need"), ("Large flat-screen television", "Want")], 0)
    ]
    items, need_idx = rng.choice(item_lists)

    prompt = (
        f"In an EMS class in {area}, {person} prepares a budget table. Study the following numbered items:\n"
        f"1. {items[0][0]}\n"
        f"2. {items[1][0]}\n"
        f"3. {items[2][0]}\n"
        f"4. {items[3][0]}\n\n"
        f"Which numbered item is strictly classified as a primary **survival need**?"
    )
    correct_opt = f"Item {need_idx + 1} only"
    distractors = [f"Item {i + 1} only" for i in range(4) if i != need_idx] + ["None of the four items"]
    options = [correct_opt] + distractors[:3]
    rng.shuffle(options)

    sol = (
        f"Classification from Curriculum Reference:\n"
        f"- 1. {items[0][0]}: {items[0][1]}\n"
        f"- 2. {items[1][0]}: {items[1][1]}\n"
        f"- 3. {items[2][0]}: {items[2][1]}\n"
        f"- 4. {items[3][0]}: {items[3][1]}\n\n"
        f"The survival need is Item {need_idx + 1} only ({items[need_idx][0]}). Survival needs are essentials required to stay alive, whereas wants can be postponed."
    )
    return {
        "id": f"g7_ems_needs_class_{rng.randint(100000, 999999)}",
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
        "subskill": "needs_vs_wants_classification",
        "question_family_id": "needs_vs_wants_classification",
        "curriculum_reference": "Term 1 > Needs and Wants > Classification Exercise: Needs vs Wants",
        "hints": {
            "tier_1": "Look for the item that directly preserves life, health, or hygiene.",
            "tier_2": "Luxuries and electronic entertainment are wants, not survival needs.",
            "tier_3": f"Correct: {correct_opt}"
        }
    }


def _build_basic_economic_problem(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]
    budget = rng.choice([500, 1000, 1500, 2500])

    prompt = (
        f"{person}'s family in {area} has a monthly household income of R{budget}, but their total list of desired goods, "
        f"services, and groceries costs R{budget * 2}.\n\n"
        f"Explain the **basic economic problem** illustrated by this situation in terms of resources and wants."
    )
    sample_ans = (
        "The basic economic problem arises because human needs and wants are unlimited, while the resources (money/income) "
        "available to satisfy them are limited and scarce. This scarcity forces the household to make choices and prioritise."
    )
    sol = (
        f"1. Core Definition [2]: The fundamental economic problem is that human wants are **unlimited**, "
        f"while productive resources (money, income of R{budget}, land, labour, capital) are **limited** or scarce [2].\n"
        f"2. Consequence of Scarcity [2]: Because resources cannot satisfy every desire, individuals and societies must make "
        f"**choices** to prioritise essential needs over discretionary wants [2]."
    )
    return {
        "id": f"g7_ems_needs_econ_prob_{rng.randint(100000, 999999)}",
        "question_type": "short_answer",
        "prompt": prompt,
        "correct_answer": sample_ans,
        "sample_answer": sample_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "the_basic_economic_problem",
        "question_family_id": "the_basic_economic_problem",
        "curriculum_reference": "Term 1 > Needs and Wants > The Economic Problem",
        "hints": {
            "tier_1": "Focus on the two key contrasting words: 'unlimited' vs 'limited'.",
            "tier_2": "Unlimited human wants versus limited (scarce) resources.",
            "tier_3": "Scarcity of resources forces people and communities to make choices."
        }
    }


def _build_community_service_delivery(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    town = scenario["area"]

    facilities = [
        ("clinics and healthcare centres", "curing illnesses and preserving life"),
        ("clean municipal water piping and sanitation", "preventing waterborne diseases like cholera"),
        ("primary schools and learning materials", "providing foundational literacy and numeracy"),
        ("refuse removal and waste disposal", "maintaining environmental hygiene in townships")
    ]
    fac, purpose = rng.choice(facilities)

    prompt = (
        f"The local municipality governing {town} has a limited annual development budget. "
        f"Community leaders argue that allocating funds towards **{fac}** must take priority over building a sports entertainment stadium.\n\n"
        f"Justify this decision based on the difference between basic community needs and recreational wants."
    )
    sample_ans = (
        f"{fac} satisfies an essential primary community need ({purpose}) necessary for survival and public health. "
        f"A stadium is a secondary want that should only be funded after basic survival infrastructure is secured."
    )
    sol = (
        f"1. Service delivery priority [2]: Municipalities are constitutionally obligated to satisfy basic primary needs first [1]. "
        f"{fac} directly addresses public survival and well-being ({purpose}) [1].\n"
        f"2. Contrast with secondary wants [2]: Recreational facilities like stadiums improve quality of life (wants) [1], "
        f"but must not take precedence over essential life-supporting infrastructure when resources are scarce [1]."
    )
    return {
        "id": f"g7_ems_needs_serv_{rng.randint(100000, 999999)}",
        "question_type": "short_answer",
        "prompt": prompt,
        "correct_answer": sample_ans,
        "sample_answer": sample_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "community_service_delivery_needs",
        "question_family_id": "community_service_delivery_needs",
        "curriculum_reference": "Term 1 > Needs and Wants > Service Delivery",
        "hints": {
            "tier_1": "Why must clean water or healthcare come before entertainment facilities?",
            "tier_2": "Survival and public health are primary needs. Entertainment and sports stadiums are secondary wants.",
            "tier_3": "Basic service delivery preserves life and health; wants only improve leisure."
        }
    }


def _build_scarcity_and_choice(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    person = scenario["entrepreneur"]
    area = scenario["area"]
    stipend = rng.choice([200, 300, 400, 500])

    prompt = (
        f"{person} has R{stipend} pocket money in {area}. {person} can either buy a required mathematics textbook "
        f"for R{stipend} or a trendy branded cap for R{stipend}. {person} chooses the textbook.\n\n"
        f"What is the economic term for the branded cap that {person} had to give up, and why was this choice made?"
    )
    correct_opt = "Opportunity cost; because the textbook satisfies an educational need while the cap is a discretionary want."
    distractors = [
        "Depreciation; because the cap would lose its monetary value immediately.",
        "Liabilities; because buying clothing creates a debt to the store.",
        "Capital; because educational books represent financial interest."
    ]
    options = [correct_opt] + distractors
    rng.shuffle(options)

    sol = (
        f"Step 1: Identify the economic concept:\n"
        f"When scarce resources force a choice between alternatives, the value of the next best alternative given up is the **opportunity cost**.\n\n"
        f"Step 2: Apply to scenario:\n"
        f"- Option chosen: Mathematics textbook (essential educational need).\n"
        f"- Alternative sacrificed: Branded cap (opportunity cost).\n\n"
        f"Conclusion: {correct_opt}"
    )
    return {
        "id": f"g7_ems_needs_choice_{rng.randint(100000, 999999)}",
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
        "subskill": "scarcity_and_choice_evaluation",
        "question_family_id": "scarcity_and_choice_evaluation",
        "curriculum_reference": "Term 1 > Needs and Wants > Critical Thinking and Analysis",
        "hints": {
            "tier_1": "What do we call the alternative benefit you sacrifice when making a decision?",
            "tier_2": "The next best forgone option is the opportunity cost.",
            "tier_3": f"Correct: {correct_opt}"
        }
    }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Main entry point for Grade 7 Needs and Wants generator."""
    rng = _rng(seed)
    questions = []

    target_sub = str(subskill or "").strip().lower()

    def _build_one(sub_name: str) -> Dict[str, Any]:
        if "prim" in sub_name or "second" in sub_name:
            return _build_primary_vs_secondary(rng)
        elif "class" in sub_name or "categor" in sub_name:
            return _build_needs_vs_wants_classification(rng)
        elif "econ" in sub_name or "problem" in sub_name:
            return _build_basic_economic_problem(rng)
        elif "serv" in sub_name or "communit" in sub_name or "deliver" in sub_name:
            return _build_community_service_delivery(rng)
        elif "scarc" in sub_name or "choice" in sub_name or "opportun" in sub_name:
            return _build_scarcity_and_choice(rng)
        return _build_primary_vs_secondary(rng)

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        for _ in range(count):
            questions.append(_build_one(target_sub))
        return questions

    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(_build_one(sub))

    return questions
