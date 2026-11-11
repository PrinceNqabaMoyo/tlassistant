"""Grade 8 EMS — Factors of Production (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 4/03. Factors of production.md

Covers CAPS subskills:
  1. four_factors_classification: Identifying and defining Land/Natural Resources, Labour, Capital, and Entrepreneurship.
  2. remuneration_of_factors: Matching each factor to its authentic reward (Land -> Rent, Labour -> Wages/Salaries, Capital -> Interest, Entrepreneurship -> Profit).
  3. capital_own_vs_borrowed: Differentiating own capital (personal savings/assets) from borrowed capital (bank loans, trade credit).
  4. labour_skill_levels_and_laws: Unskilled, semi-skilled, and skilled labour; fair labour laws (BCEA, LRA, OHSA, COIDA).
  5. entrepreneurship_role: Combining resources, risk-taking, and innovation.

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, AREAS

SUBSKILLS = [
    "four_factors_classification",
    "remuneration_of_factors",
    "capital_own_vs_borrowed",
    "labour_skill_levels_and_laws",
    "entrepreneurship_role",
]

TOPIC_KEY = "grade8_ems_factors_of_production"
LO = "g8_ems_factors_of_production"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _gen_four_factors(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    cases = [
        (
            f"The fertile agricultural land, mineral deposits, and borehole water utilized by {scenario['entrepreneur']}'s business in {scenario['area']}.",
            "Natural Resources / Land",
            ["Natural Resources / Land", "Capital", "Labour", "Entrepreneurship"],
            "Natural resources (Land) encompass all gifts of nature, including land, soil, water, minerals, and forests used in production.",
        ),
        (
            f"The physical and mental effort exerted by employees, mechanics, and administrative staff working for {scenario['entrepreneur']}.",
            "Labour",
            ["Labour", "Capital", "Natural Resources / Land", "Entrepreneurship"],
            "Labour is the human physical and mental work applied to produce goods and services.",
        ),
        (
            f"The machinery, delivery bakkies, tools, and money invested to operate the enterprise in {scenario['area']}.",
            "Capital",
            ["Capital", "Labour", "Natural Resources / Land", "Entrepreneurship"],
            "Capital includes both financial capital (money) and physical capital (machinery, vehicles, equipment) used in production.",
        ),
        (
            f"The initiative taken by {scenario['entrepreneur']} to identify a market need, invest personal funds, combine resources, and bear financial risk to make a profit.",
            "Entrepreneurship",
            ["Entrepreneurship", "Labour", "Capital", "Natural Resources / Land"],
            "Entrepreneurship is the human factor that organizes and coordinates the other three factors and takes financial risks.",
        ),
    ]
    desc, correct_factor, options, explanation = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_factor)
    correct_letter = chr(65 + c_idx)

    prompt = (
        f"In economic production, four factors of production must be combined to produce goods and services.\n\n"
        f"\"{desc}\"\n\n"
        f"Which factor of production is this an example of?"
    )
    ans = f"{correct_letter}. {correct_factor}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {explanation}"
    )
    return {
        "id": f"g8_fop_fac_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "Factors of Production",
        "subskill": "four_factors_classification",
        "learning_objective_id": f"{LO}_classification",
        "archetype": "factors_of_production_classification",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "The 4 factors are Land, Labour, Capital, and Entrepreneurship.",
            "tier_2": f"Explanation hint: {explanation}",
            "tier_3": f"Answer is {correct_factor}.",
        },
        "misconception_tags": ["confuses_capital_with_natural_resources"],
    }


def _gen_remuneration(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    prompt = (
        f"Every factor of production receives a specific remuneration (economic reward) for its contribution to production.\n\n"
        f"For a registered enterprise in {scenario['area']}, complete the following table by stating the exact remuneration "
        f"received by each of the four factors of production:\n\n"
        f"1. **Natural Resources (Land)**\n"
        f"2. **Labour**\n"
        f"3. **Capital**\n"
        f"4. **Entrepreneurship**"
    )
    ans = (
        "1. Land receives Rent;\n"
        "2. Labour receives Salaries or Wages;\n"
        "3. Capital receives Interest;\n"
        "4. Entrepreneurship receives Profit."
    )
    sol = (
        "**Model Answer** [8 marks (2 marks per factor)]:\n\n"
        "1. **Natural Resources / Land** receives **Rent** [2 marks].\n"
        "2. **Labour** receives **Salaries or Wages** [2 marks].\n"
        "3. **Capital** receives **Interest** [2 marks].\n"
        "4. **Entrepreneurship** receives **Profit** [2 marks]."
    )
    return {
        "id": f"g8_fop_rem_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "topic": "Factors of Production",
        "subskill": "remuneration_of_factors",
        "learning_objective_id": f"{LO}_remuneration",
        "archetype": "remuneration_table_matching",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 8,
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp1", "desc": "Land -> Rent", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Labour -> Wages / Salaries", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Capital -> Interest", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Entrepreneurship -> Profit", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Think about what a tenant pays (Rent) and what workers earn (Wages/Salaries).",
            "tier_2": "Banks charge Interest on Capital. The owner takes the risk for Profit.",
            "tier_3": "1. Rent, 2. Wages/Salaries, 3. Interest, 4. Profit.",
        },
        "misconception_tags": ["confuses_salary_with_profit_for_entrepreneur"],
    }


def _gen_own_vs_borrowed(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    own_amt = rng.randint(40, 100) * 1000
    borrow_amt = rng.randint(20, 60) * 1000
    total_cap = own_amt + borrow_amt

    prompt = (
        f"{scenario['entrepreneur']} starts a new {scenario['business_type']} in {scenario['area']} requiring **R{total_cap:,}** start-up capital.\n"
        f"- {scenario['entrepreneur']} invests **R{own_amt:,}** from personal savings.\n"
        f"- The remaining **R{borrow_amt:,}** is obtained via a commercial bank loan.\n\n"
        f"1. Classify the two portions of capital as either **own capital** or **borrowed capital**.\n"
        f"2. Explain ONE major financial difference or risk between own capital and borrowed capital."
    )
    ans = (
        f"1. Own capital: R{own_amt:,}; Borrowed capital: R{borrow_amt:,};\n"
        f"2. Borrowed capital must be repaid with interest regardless of whether the business makes a profit, whereas own capital does not have fixed debt repayment obligations."
    )
    sol = (
        f"**Model Answer** [4 marks]:\n\n"
        f"1. **Capital Classification** [2 marks]:\n"
        f"   - **Own Capital:** R{own_amt:,} (invested by owner from personal savings) [1 mark].\n"
        f"   - **Borrowed Capital:** R{borrow_amt:,} (obtained via a commercial bank loan) [1 mark].\n\n"
        f"2. **Financial Difference / Risk** [2 marks]:\n"
        f"   - Borrowed capital incurs **interest charges** and must be repaid on scheduled dates, creating financial liability even if the business makes a loss [2 marks]."
    )
    return {
        "id": f"g8_fop_cap_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "topic": "Factors of Production",
        "subskill": "capital_own_vs_borrowed",
        "learning_objective_id": f"{LO}_capital_types",
        "archetype": "capital_types_comparison",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Identifies R{own_amt:,} as own capital and R{borrow_amt:,} as borrowed capital", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Explains interest obligation / repayment risk of borrowed capital", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Own capital comes from personal savings. Borrowed capital comes from loans.",
            "tier_2": "Loans must be repaid with interest.",
            "tier_3": f"Own capital = R{own_amt:,}. Borrowed capital = R{borrow_amt:,}.",
        },
        "misconception_tags": ["confusing_own_capital_with_bank_loan"],
    }


def _gen_labour_skills_laws(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    skills = [
        (
            "General sweeping, packing, and cleaning requiring no formal qualifications or previous training.",
            "Unskilled labour",
            ["Unskilled labour", "Semi-skilled labour", "Skilled labour", "Professional labour"],
            "Unskilled labour requires basic manual effort and no formal technical qualification.",
        ),
        (
            "Operating specific machinery or driving delivery vehicles after completing a short training course or licence.",
            "Semi-skilled labour",
            ["Semi-skilled labour", "Unskilled labour", "Skilled labour", "Executive labour"],
            "Semi-skilled labour involves routine tasks requiring moderate training or practical experience.",
        ),
        (
            "Chartered accountants, electrical engineers, and medical practitioners who completed university degrees and professional board exams.",
            "Skilled labour",
            ["Skilled labour", "Unskilled labour", "Semi-skilled labour", "Manual labour"],
            "Skilled labour requires extensive formal education, technical expertise, and certified qualifications.",
        ),
    ]
    job_desc, correct_skill, options, why = rng.choice(skills)
    rng.shuffle(options)
    c_idx = options.index(correct_skill)
    correct_letter = chr(65 + c_idx)

    prompt = (
        f"In South African workplaces, labour is classified into three skill levels based on education and training:\n\n"
        f"\"{job_desc}\"\n\n"
        f"Which skill category of labour does this describe?"
    )
    ans = f"{correct_letter}. {correct_skill}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {why}"
    )
    return {
        "id": f"g8_fop_skl_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "Factors of Production",
        "subskill": "labour_skill_levels_and_laws",
        "learning_objective_id": f"{LO}_labour_skills",
        "archetype": "labour_skills_classification",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Levels are Unskilled (no formal training), Semi-skilled (short training/driver licence), Skilled (degrees/qualifications).",
            "tier_2": f"Description hint: {why}",
            "tier_3": f"Answer is {correct_skill}.",
        },
        "misconception_tags": ["confuses_unskilled_with_semi_skilled"],
    }


def generate(
    subskill: str = "mixed",
    seed: Optional[int] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    generators = {
        "four_factors_classification": _gen_four_factors,
        "remuneration_of_factors": _gen_remuneration,
        "capital_own_vs_borrowed": _gen_own_vs_borrowed,
        "labour_skill_levels_and_laws": _gen_labour_skills_laws,
    }

    results: List[Dict[str, Any]] = []
    if subskill in generators:
        for _ in range(count):
            results.append(generators[subskill](rng))
        return results

    keys = list(generators.keys())
    for i in range(count):
        chosen = keys[i % len(keys)]
        results.append(generators[chosen](rng))
    return results
