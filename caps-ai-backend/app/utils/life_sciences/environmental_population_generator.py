"""Life Sciences & Senior Phase Natural Sciences — Environmental Ecology & Population Dynamics.
Covers food webs, trophic energy transfer, Lincoln-Petersen mark-recapture estimation, and population growth curves.
Strictly complies with the 6-Pillar Generator Contract:
- Multi-grade vertical strand (Gr7/8 NS, Gr10/11 LS)
- Procedural seeded PRNG determinism (random.Random(seed))
- Atomic elementary sub-drills (mode="compound" | "elementary_*")
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention (",")
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr78_ecosystems(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 7/8 Natural Sciences: Food chains, food webs, and 10% trophic energy transfer."""
    biome = r.choice(["Savanna", "Fynbos", "Grassland", "Nama Karoo"])
    producer = r.choice(["Acacia trees and red grass", "Proteas and restios", "Themeda triandra grass"])
    herbivore = r.choice(["Impala", "Cape mountain zebra", "Springbok"])
    carnivore = r.choice(["Leopard", "Cheetah", "Black-backed jackal"])
    top_predator = "Lion"

    producer_energy = r.choice([50000, 100000, 200000, 500000])  # in kJ
    herbivore_energy = producer_energy // 10
    carnivore_energy = herbivore_energy // 10
    top_energy = carnivore_energy // 10

    qid = _make_id("ns78_ecology", seed, idx)

    if mode == "elementary_trophic_energy_calc":
        prompt = (
            f"In a South African {biome} ecosystem, the total chemical potential energy stored in the primary producers "
            f"({producer}) is ${_fmt_sa(producer_energy)}\\text{{ kJ}}.\n\n"
            f"Using the 10% ecological energy transfer rule, calculate the energy available to the primary consumers ({herbivore}) "
            f"and secondary consumers ({carnivore})."
        )
        ans_str = f"Primary consumers: {_fmt_sa(herbivore_energy)} kJ; Secondary consumers: {_fmt_sa(carnivore_energy)} kJ"
        memo = (
            f"1. Energy to primary consumers: 10% of {_fmt_sa(producer_energy)} kJ = {_fmt_sa(producer_energy)} * 0.10 = {_fmt_sa(herbivore_energy)} kJ [2]\n"
            f"2. Energy to secondary consumers: 10% of {_fmt_sa(herbivore_energy)} kJ = {_fmt_sa(herbivore_energy)} * 0.10 = {_fmt_sa(carnivore_energy)} kJ [2]"
        )
        hints = {
            "tier_1": "Only approximately 10% of energy is transferred from one trophic level to the next.",
            "tier_2": "Divide by 10 for each trophic step (Producers -> Primary consumers -> Secondary consumers).",
            "tier_3": f"Primary = {producer_energy} * 0.1 = {herbivore_energy} kJ. Secondary = {herbivore_energy} * 0.1 = {carnivore_energy} kJ.",
        }
        marks = 4
    else:
        prompt = (
            f"A study of a {biome} ecosystem recorded the following food chain:\n"
            f"$$\\text{{{producer}}} \\to \\text{{{herbivore}}} \\to \\text{{{carnivore}}} \\to \\text{{{top_predator}}}$$\n"
            f"The primary producers fix ${_fmt_sa(producer_energy)}\\text{{ kJ}}$ of energy.\n\n"
            f"1. Identify the trophic level occupied by the {herbivore}.\n"
            f"2. Calculate the energy available at the top carnivore level ({top_predator}).\n"
            f"3. Explain why 90% of the energy is lost at each trophic level transfer."
        )
        ans_str = (
            f"1. Second trophic level (primary consumer); "
            f"2. {_fmt_sa(top_energy)} kJ; "
            f"3. Lost as heat from cellular respiration, excretion/waste, and unconsumed parts."
        )
        memo = (
            f"1. {herbivore} is a primary consumer, occupying the second trophic level. [1]\n"
            f"2. Energy calculations [3]:\n"
            f"   - Trophic level 1 (Producers): {_fmt_sa(producer_energy)} kJ\n"
            f"   - Trophic level 2 ({herbivore}): {_fmt_sa(herbivore_energy)} kJ\n"
            f"   - Trophic level 3 ({carnivore}): {_fmt_sa(carnivore_energy)} kJ\n"
            f"   - Trophic level 4 ({top_predator}): {_fmt_sa(top_energy)} kJ [A]\n"
            f"3. Energy loss reasons [2]: Energy is expended in metabolic processes and released as metabolic heat during respiration; "
            f"lost through excretion and egestion; not all organic tissue is eaten by the consumer."
        )
        hints = {
            "tier_1": "Producers are level 1. Divide by 10 at each consumer step.",
            "tier_2": "Energy decreases tenfold at each step: Producers -> Herbivores -> Carnivores -> Top predators. 90% lost to respiration heat and waste.",
            "tier_3": f"1. 2nd level. 2. {top_energy} kJ. 3. Lost as heat in respiration, waste, and uneaten biomass.",
        }
        marks = 6

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["trophic_level_numbering_confusion", "energy_loss_respiration_omitted", "ten_percent_rule_miscalculated"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Trophic level identification", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Sequential 10% energy calculation", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Ecological rationale for energy dissipation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_population_ecology(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Life Sciences: Lincoln-Petersen mark-recapture index, growth curves, and predator-prey dynamics."""
    species = r.choice(["geometric tortoises", "riverine rabbits", "African penguin chicks", "bontebok"])
    m_marked = r.choice([40, 50, 60, 80, 100, 120])
    s_second = r.choice([30, 45, 50, 75, 90])
    # Ensure clean integer or near-integer population estimate: P = (M * S) / R
    r_recaptured = r.choice([5, 6, 8, 10, 12, 15])
    p_estimate = int(round((m_marked * s_second) / r_recaptured))

    qid = _make_id("ls11_population_ecology", seed, idx)

    if mode == "elementary_mark_recapture_calc":
        prompt = (
            f"Ecologists conducted a survey to estimate the total population size of {species} in a nature reserve.\n"
            f"- Initial sample captured, marked, and released ($M$): ${m_marked}$\n"
            f"- Second sample captured after two weeks ($S$): ${s_second}$\n"
            f"- Number of marked individuals in second sample ($R$): ${r_recaptured}$\n\n"
            f"Use the Lincoln-Petersen formula to calculate the estimated population size ($P$)."
        )
        ans_str = f"P = {_fmt_sa(p_estimate)}"
        memo = (
            f"1. Formula: $P = \\frac{{M \\times S}}{{R}}$ [M]\n"
            f"2. Substitution: $P = \\frac{{{m_marked} \\times {s_second}}}{{{r_recaptured}}}$ [M]\n"
            f"3. Estimated population: $P = {_fmt_sa(p_estimate)}$ individuals [A]"
        )
        hints = {
            "tier_1": "Apply the Lincoln-Petersen formula: Population = (First Sample * Second Sample) / Recaptured.",
            "tier_2": "Substitute: M = " + f"{m_marked}, S = {s_second}, R = {r_recaptured}.",
            "tier_3": f"Calculate: ({m_marked} * {s_second}) / {r_recaptured} = {p_estimate}.",
        }
        marks = 3
    else:
        # Full compound Gr11 question: Calculation + Validity conditions + Carrying capacity
        carrying_k = p_estimate + r.choice([50, 100, 150])
        prompt = (
            f"A scientific investigation was conducted to estimate the population of {species} in an isolated nature reserve.\n"
            f"- ${m_marked}$ individuals were captured, marked with waterproof paint/tags, and released ($M$).\n"
            f"- Two weeks later, a second sample of ${s_second}$ individuals was captured ($S$), of which ${r_recaptured}$ were found to be marked ($R$).\n\n"
            f"1. Calculate the estimated population size of the {species} using the Lincoln-Petersen index.\n"
            f"2. State two validity conditions/assumptions that must be met for this capture-mark-recapture estimate to be reliable.\n"
            f"3. The carrying capacity ($K$) of this reserve for this species is estimated at ${carrying_k}$. "
            f"Explain what will happen to the population growth rate as the population size approaches $K$."
        )
        ans_str = (
            f"1. P = {_fmt_sa(p_estimate)}; "
            f"2. Assumptions: closed population (no births/deaths/migration), marking does not affect survival/predation, marks do not fade, random mixing; "
            f"3. Growth rate decelerates due to environmental resistance (limited food/space) reaching equilibrium phase."
        )
        memo = (
            f"1. Lincoln Index [3]:\n"
            f"   $$P = \\frac{{M \\times S}}{{R}} = \\frac{{{m_marked} \\times {s_second}}}{{{r_recaptured}}} = {_fmt_sa(p_estimate)}\\text{{ individuals}}$$ [A]\n"
            f"2. Validity assumptions (any 2) [2]:\n"
            f"   - The population must be closed (no births, deaths, immigration, or emigration during the sampling interval).\n"
            f"   - The mark must not harm the animal, restrict its movement, or make it more vulnerable to predators.\n"
            f"   - Marked individuals must mix randomly back into the general population before the second sample.\n"
            f"   - The mark must not wash off or fade between captures.\n"
            f"3. Carrying capacity explanation [3]: As population approaches $K = {carrying_k}$, environmental resistance increases "
            f"(competition for food, shelter, disease increases). The growth rate decelerates (enters decelerating phase) until birth rate equals death rate, "
            f"fluctuating in dynamic equilibrium around $K$ (logistic/S-shaped growth)."
        )
        hints = {
            "tier_1": "Formula: P = (M * S) / R. Think about what assumptions ensure the ratio remains accurate.",
            "tier_2": "Calculate P = (M * S) / R. Validity: no migration/births, marks must last, animals mix randomly. Near K, growth slows down.",
            "tier_3": f"1. P = {p_estimate}. 2. Closed population; marks don't hinder survival. 3. Growth rate slows down due to environmental resistance.",
        }
        marks = 8

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["lincoln_index_parameter_inversion", "mark_recapture_assumption_violation", "carrying_capacity_misread"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Lincoln-Petersen formula and substitution", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculated population value", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Mark-recapture validity assumptions", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Carrying capacity and environmental resistance", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Environmental Ecology & Population Dynamics."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "11"

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if grade_num in ("7", "8") or subskill in ("ecosystems", "food_webs", "energy_pyramid") or mode == "elementary_trophic_energy_calc":
            q = _generate_gr78_ecosystems(sub_r, sub_seed, i, mode)
        else:
            # Grade 10 / 11 Life Sciences population ecology
            q = _generate_gr11_population_ecology(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
