"""Grade 9 EMS — Economic Systems (Planned, Market, and Mixed Economies).
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr9/Term 1/01. Economic systems.md`.
Covers:
- The three major economic systems: Planned economy, Market economy, Mixed economy
- Resource control & allocation matrix (Natural resources, Labour, Capital, What to produce, Distribution)
- Advantages and disadvantages of Planned and Market systems
- The South African mixed economy context, welfare nets, and the global economy
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term1_economy"
CURRICULUM_REFERENCE = "Term 1 > The Economy: Economic Systems"


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: Optional[str] = None,
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group or "economic_systems",
        "question_family_id": question_family_id,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["economics", "ems"],
    })
    return enriched


# --------------------------------------------------------------------------- #
# Sub-Drill 1: Economic Systems Comparison Matrix
# --------------------------------------------------------------------------- #
def _generate_systems_matrix_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    criteria = [
        ("Who owns and controls natural resources (land)?", "The Government / State", "Private individuals & businesses", "Government AND private businesses"),
        ("Who controls capital and factories?", "The Government / State", "Private investors & businesses", "Government AND private businesses"),
        ("Who decides WHAT to produce and HOW MUCH?", "The Government (Central Planners)", "Consumers & businesses (Market forces)", "Businesses (with government regulations)"),
        ("What is the primary driving motive of production?", "Citizen welfare & equality", "Profit motive & wealth accumulation", "Balance of profit AND social welfare"),
        ("How are worker jobs and wages determined?", "Government / State allocates jobs", "Market forces of supply and demand", "Negotiation & collective bargaining (LRA)"),
    ]

    selected_criteria = r.sample(criteria, 3)

    headers = ["Economic Characteristic", "Planned Economy", "Market Economy", "Mixed Economy (e.g. South Africa)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for idx, (crit, planned_ans, market_ans, mixed_ans) in enumerate(selected_criteria):
        c_plan = f"t0_r{idx}_c1"
        c_mkt = f"t0_r{idx}_c2"
        c_mix = f"t0_r{idx}_c3"

        correct_map[c_plan] = planned_ans
        correct_map[c_mkt] = market_ans
        correct_map[c_mix] = mixed_ans

        cell_hints[c_plan] = f"In a planned (command) economy, the government controls economic decisions."
        cell_hints[c_mkt] = f"In a market (capitalist) economy, private individuals and market forces decide."
        cell_hints[c_mix] = f"In a mixed economy, both the state and private sector participate."

        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "value": crit, "type": "given", "editable": False},
            {"coordinate": c_plan, "value": planned_ans if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": c_mkt, "value": market_ans if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": c_mix, "value": mixed_ans if mode == "scaffold" else "", "type": "required", "editable": True},
        ])

    item = {
        "id": f"ems9_econ_matrix_{r.randint(1000, 9999)}",
        "title": "Economic Systems Comparison Matrix",
        "question_type": "table_completion",
        "prompt": "Complete the comparative matrix below to distinguish how **Planned**, **Market**, and **Mixed** economic systems answer the fundamental economic questions.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 9,
        "sample_answer": f"Row 1: {selected_criteria[0][1]} | {selected_criteria[0][2]} | {selected_criteria[0][3]}",
        "ideal_answer": "Complete matrix comparing role of government vs private sector across the three economic systems.",
        "hint_sections": {
            "1_nudge": "Planned = State control; Market = Private control & profit; Mixed = Shared between state and private sector.",
            "2_concept": "South Africa has a mixed economy where private businesses operate freely, but government provides public services and welfare.",
            "3_breakdown": f"Planned economies focus on welfare; market economies focus on profit."
        },
        "marking_schema": {
            "total_marks": 9,
            "marking_points": [
                {"id": f"mp_{i}_plan", "desc": f"Planned system: {crit[0][:30]}...", "marks": 1, "editable": True}
                for i, crit in enumerate(selected_criteria)
            ] + [
                {"id": f"mp_{i}_mkt", "desc": f"Market system: {crit[0][:30]}...", "marks": 1, "editable": True}
                for i, crit in enumerate(selected_criteria)
            ] + [
                {"id": f"mp_{i}_mix", "desc": f"Mixed system: {crit[0][:30]}...", "marks": 1, "editable": True}
                for i, crit in enumerate(selected_criteria)
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confuses_planned_and_market_ownership", "assumes_mixed_economy_has_no_private_property"],
    }
    return _with_metadata(
        item,
        subskill="economic_systems_matrix",
        learning_objective_id="lo_g9_econ_systems_matrix",
        question_family_id="econ_matrix_table",
        misconception_tags=["confuses_planned_and_market_ownership", "assumes_mixed_economy_has_no_private_property"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 2: Advantages and Disadvantages Analysis
# --------------------------------------------------------------------------- #
def _generate_pros_cons_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    system_type = r.choice(["Planned Economy", "Market Economy"])

    if system_type == "Planned Economy":
        prompt = (
            "Evaluate the **Planned (Command) Economic System** (such as Cuba or the former Soviet Union).\n\n"
            "1. State **TWO advantages** of a planned economy.\n"
            "2. State **TWO disadvantages** of a planned economy.\n"
            "3. Explain why planned economies provided workers with job security known historically as the 'iron rice bowl'."
        )
        sample_ans = (
            "Advantages: 1. Focuses on citizens' welfare rather than profit. 2. Resources can be directed quickly to heavy industry and public infrastructure.\n"
            "Disadvantages: 1. Inflexible and slow to adapt to changing consumer demand. 2. No incentive for innovation or entrepreneurship.\n"
            "Explanation: The government guaranteed lifelong employment, housing, and food, meaning workers had absolute job security regardless of individual performance."
        )
        points = [
            "Advantage: Greater equality and focus on welfare/basic needs.",
            "Advantage: Government directs resources to essential services without waiting for capital accumulation.",
            "Disadvantage: Lack of consumer choice and shortages of consumer goods.",
            "Disadvantage: Inflexibility and lack of worker motivation/incentives.",
            "Iron rice bowl: Guarantees of lifelong employment and necessities by the state.",
        ]
    else:
        prompt = (
            "Evaluate the **Market Economic System (Capitalism)** (such as the United States).\n\n"
            "1. State **TWO advantages** of a market economy.\n"
            "2. State **TWO disadvantages** of a market economy.\n"
            "3. Explain why market economies can result in a wide gap between rich and poor."
        )
        sample_ans = (
            "Advantages: 1. High consumer choice and competition. 2. Strong incentive for innovation, efficiency, and profit.\n"
            "Disadvantages: 1. Severe inequality and poverty for unskilled workers. 2. Essential public goods (health, education) may be neglected if unprofitable.\n"
            "Explanation: Because the economy is profit-driven and resources are privately owned, owners of capital accumulate wealth while unskilled labour can be exploited."
        )
        points = [
            "Advantage: Wide variety of consumer goods and high innovation.",
            "Advantage: Efficient allocation of resources driven by consumer demand.",
            "Disadvantage: Large gap between rich and poor / unequal wealth distribution.",
            "Disadvantage: Potential exploitation of workers and neglect of unprofitable social needs.",
            "Inequality explanation: Profit-driven nature concentrates capital among business owners.",
        ]

    item = {
        "id": f"ems9_econ_proscons_{r.randint(1000, 9999)}",
        "title": f"Evaluation of {system_type}",
        "question_type": "typed",
        "prompt": prompt,
        "marks": 6,
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "marking_points": points,
        "hint_sections": {
            "1_nudge": f"Think about who wins and who loses in a {system_type}.",
            "2_concept": "Planned economies excel at equality and welfare but fail at innovation. Market economies excel at innovation and choices but struggle with inequality.",
            "3_breakdown": "Answer both parts: two distinct advantages and two distinct disadvantages."
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_adv1", "desc": "First valid advantage", "marks": 1, "editable": True},
                {"id": "mp_adv2", "desc": "Second valid advantage", "marks": 1, "editable": True},
                {"id": "mp_dis1", "desc": "First valid disadvantage", "marks": 1, "editable": True},
                {"id": "mp_dis2", "desc": "Second valid disadvantage", "marks": 1, "editable": True},
                {"id": "mp_exp", "desc": "Thorough explanation of social impact", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confused_advantages_between_systems", "oversimplified_system_critique"],
    }
    return _with_metadata(
        item,
        subskill="advantages_disadvantages",
        learning_objective_id="lo_g9_econ_pros_cons",
        question_family_id="econ_pros_cons_essay",
        misconception_tags=["confused_advantages_between_systems", "oversimplified_system_critique"],
    )


# --------------------------------------------------------------------------- #
# Sub-Drill 3: The South African Mixed Economy Case Study
# --------------------------------------------------------------------------- #
def _generate_sa_mixed_drill(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    issues = [
        {
            "scenario": "South Africa's government provides social security grants to over 18 million vulnerable citizens while maintaining a free market with private banks and retail giants like Shoprite and Woolworths.",
            "question": "Explain which characteristics in this scenario prove that South Africa operates a **mixed economy** rather than a pure market economy.",
            "answer": "The existence of free-market retail businesses and private banks reflects private enterprise, while government intervention through social grants to reduce poverty reflects state welfare, which defines a mixed economy.",
            "marks": 4,
        },
        {
            "scenario": "State-Owned Enterprises (SOEs) such as Eskom and Transnet provide electricity and freight rail, while private independent power producers (IPPs) and private courier companies compete in the open market.",
            "question": "Why does a developing country like South Africa rely on both State-Owned Enterprises and private businesses?",
            "answer": "SOEs provide essential public infrastructure that private companies might not afford or find profitable to deliver to poor communities, while private businesses drive innovation, investment, and operational efficiency.",
            "marks": 4,
        },
    ]
    chosen = r.choice(issues)

    item = {
        "id": f"ems9_econ_sa_{r.randint(1000, 9999)}",
        "title": "South Africa's Mixed Economy",
        "question_type": "typed",
        "prompt": f"**Case Study:**\n{chosen['scenario']}\n\n**Question:**\n{chosen['question']} ({chosen['marks']} marks)",
        "marks": chosen["marks"],
        "sample_answer": chosen["answer"],
        "ideal_answer": chosen["answer"],
        "marking_points": [
            "Identifies the role of private enterprise in generating economic wealth.",
            "Identifies the role of government in social welfare and public infrastructure.",
            "Connects both elements to the definition and purpose of a mixed economy.",
        ],
        "hint_sections": {
            "1_nudge": "A mixed economy combines private business with government regulation and welfare.",
            "2_concept": "South Africa uses private business for economic growth, and government intervention to fight historical inequality and poverty.",
            "3_breakdown": "Highlight both the private sector side and the government welfare/regulation side."
        },
        "marking_schema": {
            "total_marks": chosen["marks"],
            "marking_points": [
                {"id": "mp_pvt", "desc": "Identification of private sector role", "marks": 2, "editable": True},
                {"id": "mp_state", "desc": "Identification of state/welfare role", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["fails_to_identify_mixed_characteristics"],
    }
    return _with_metadata(
        item,
        subskill="south_african_mixed_economy",
        learning_objective_id="lo_g9_sa_mixed_economy",
        question_family_id="sa_mixed_case",
        misconception_tags=["fails_to_identify_mixed_characteristics"],
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "economic_systems_matrix": lambda rng, mode: [_generate_systems_matrix_drill(rng, mode)],
    "elementary_matrix": lambda rng, mode: [_generate_systems_matrix_drill(rng, mode)],
    "advantages_disadvantages": lambda rng, mode: [_generate_pros_cons_drill(rng, mode)],
    "south_african_mixed_economy": lambda rng, mode: [_generate_sa_mixed_drill(rng, mode)],
    "concepts": lambda rng, mode: [_generate_systems_matrix_drill(rng, mode)],
}


def generate(
    subskill: str = "economic_systems_matrix",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    builder = BUILDERS.get(subskill)
    if builder is not None:
        pool = builder(rng, mode)
    else:
        pool = (
            [_generate_systems_matrix_drill(rng, mode)]
            + [_generate_pros_cons_drill(rng, mode)]
            + [_generate_sa_mixed_drill(rng, mode)]
        )

    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
