"""Life Sciences Grade 11 Term 3: Population Ecology Generator.

Covers:
- Lincoln-Petersen capture-mark-recapture estimation:
  P = (M * S) / R
- Validity assumptions and sampling reliability criteria.
- Population growth models:
  - Exponential (J-shaped curve) vs Logistic (S-shaped curve).
  - Carrying capacity (K) and environmental resistance (density-dependent vs density-independent).
- Predator-prey cyclic interactions and dynamic equilibrium oscillations.
- Age-gender population structure pyramids (expanding, stable, and contracting profiles).

Strictly complies with the 6-Pillar Generator Contract.
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


def _generate_mark_recapture_investigation(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Capture-mark-recapture calculations and ecological validity conditions."""
    species = r.choice([
        "Geometric tortoises (*Psammobates geometricus*)",
        "Riverine rabbits (*Bunolagus monticularis*)",
        "African penguin chicks (*Spheniscus demersus*)",
        "Bontebok (*Damaliscus pygargus*)",
        "Knysna seahorses (*Hippocampus capensis*)",
    ])
    reserve = r.choice(["De Hoop Nature Reserve", "Karoo National Park", "Boulders Beach Marine Sanctuary", "Elandsberg Nature Reserve"])

    # Clean procedural numbers for Lincoln index: P = (M * S) / R
    m_marked = r.choice([40, 50, 60, 80, 100, 120])
    s_second = r.choice([30, 45, 50, 60, 75, 90])
    r_recaptured = r.choice([5, 6, 8, 10, 12, 15])
    p_estimate = int(round((m_marked * s_second) / r_recaptured))
    carrying_k = p_estimate + r.choice([60, 120, 180])

    qid = _make_id("ls11_mark_recapture", seed, idx)

    if mode == "elementary_mark_recapture_formula":
        prompt = (
            f"Ecologists conducted a survey in {reserve} to estimate the population size of {species}.\n"
            f"- First sample captured, marked, and released ($M$): ${m_marked}$\n"
            f"- Second sample captured after two weeks ($S$): ${s_second}$\n"
            f"- Number of marked individuals found in the second sample ($R$): ${r_recaptured}$\n\n"
            f"Use the Lincoln-Petersen index formula to calculate the estimated population size ($P$)."
        )
        ans_str = f"P = {_fmt_sa(p_estimate)}"
        memo = (
            f"1. Formula: $P = \\frac{{M \\times S}}{{R}}$ [M]\n"
            f"2. Substitution: $P = \\frac{{{m_marked} \\times {s_second}}}{{{r_recaptured}}}$ [M]\n"
            f"3. Estimated population: $P = {_fmt_sa(p_estimate)}$ individuals [A]"
        )
        hints = {
            "tier_1": "Apply the Lincoln-Petersen formula: P = (M * S) / R.",
            "tier_2": f"Substitute: ({m_marked} * {s_second}) / {r_recaptured}.",
            "tier_3": f"P = {p_estimate} individuals.",
        }
        marks = 3
        misconceptions = ["lincoln_index_parameter_inversion", "arithmetic_division_error"]
    else:
        # Full compound question: Lincoln Index + Assumptions + Carrying capacity
        prompt = (
            f"Conservation biologists conducted a research survey in {reserve} to evaluate the population status of **{species}**.\n"
            f"- ${m_marked}$ individuals were safely captured, marked with durable, non-toxic tags, and released back into the habitat ($M$).\n"
            f"- Two weeks later, a second sample of ${s_second}$ individuals was captured ($S$), of which ${r_recaptured}$ bore marks ($R$).\n\n"
            f"1. Use the Lincoln-Petersen index to calculate the estimated total population size ($P$) of {species}.\n"
            f"2. State TWO validity assumptions that must be satisfied for this mark-recapture estimate to be mathematically sound.\n"
            f"3. The carrying capacity ($K$) of {reserve} for this species is ${_fmt_sa(carrying_k)}$ individuals. "
            f"Explain how environmental resistance stabilizes the population growth rate as the population approaches $K$."
        )
        ans_str = (
            f"1. P = {_fmt_sa(p_estimate)}; "
            f"2. Assumptions: closed population (no births, deaths, immigration, emigration), marks do not wash off, marks do not affect survival/predation, random mixing; "
            f"3. Increased density amplifies competition for food/space and disease transmission, decelerating growth rate until birth rate equals death rate (dynamic equilibrium)."
        )
        memo = (
            f"1. Lincoln-Petersen calculation [3]:\n"
            f"   $$P = \\frac{{M \\times S}}{{R}} = \\frac{{{m_marked} \\times {s_second}}}{{{r_recaptured}}} = {_fmt_sa(p_estimate)}\\text{{ individuals}}$$ [3]\n"
            f"2. Validity assumptions (any 2) [2]:\n"
            f"   - The population is closed (no births, deaths, immigration, or emigration during the sampling interval).\n"
            f"   - The mark does not harm the animal, hinder locomotion, or increase conspicuousness to predators.\n"
            f"   - Marked animals mix thoroughly and randomly throughout the entire population prior to second sampling.\n"
            f"   - Marks remain permanent and legible throughout the survey duration.\n"
            f"3. Environmental resistance and carrying capacity [3]: As the population approaches $K = {_fmt_sa(carrying_k)}$, "
            f"density-dependent environmental resistance factors intensify (severe competition for food, nesting territories, increased disease) [1]. "
            f"This causes the population growth rate to decelerate [1], reaching a stable plateau where birth rate balances mortality in dynamic equilibrium [1]."
        )
        hints = {
            "tier_1": "Formula: P = (M * S) / R. Validity requires no movement in/out of the area and marks must last.",
            "tier_2": f"Calculate: ({m_marked} * {s_second}) / {r_recaptured} = {p_estimate}. Environmental resistance slows growth near K.",
            "tier_3": f"1. P = {p_estimate}. 2. Closed population; marks don't affect survival. 3. Competition and limited resources slow growth rate to equilibrium at K.",
        }
        marks = 8
        misconceptions = ["lincoln_index_parameter_inversion", "mark_recapture_assumption_violation", "carrying_capacity_misread"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Lincoln-Petersen formula, substitution and correct answer", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Capture-mark-recapture validity conditions", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Carrying capacity and environmental resistance mechanics", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_growth_curves_and_predator_prey(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Logistic vs exponential growth curves and predator-prey dynamics."""
    context = r.choice(["growth_curves", "predator_prey_cycle"])
    qid = _make_id("ls11_pop_dynamics", seed, idx)

    if context == "growth_curves":
        organism = r.choice(["yeast cells in a closed sugar broth", "aphids in a rose garden", "paramecia in pond water"])
        prompt = (
            f"A laboratory population of {organism} exhibited a classic sigmoid (S-shaped) logistic growth curve over a 30-day period.\n\n"
            "1. Name the FOUR distinct sequential phases of a logistic growth curve.\n"
            "2. Explain why the population grows very slowly during the initial lag phase.\n"
            "3. Distinguish between **density-dependent** and **density-independent** limiting factors, giving ONE example of each."
        )
        ans_str = (
            "1. Lag phase, Geometric/Exponential accelerating phase, Decelerating phase, Stationary/Equilibrium phase; "
            "2. Low initial number of individuals adapting to the environment and finding mates; "
            "3. Density-dependent factors depend on population density (e.g. food competition, disease); Density-independent factors affect population regardless of density (e.g. floods, wildfires)."
        )
        memo = (
            "1. Logistic growth phases [4]:\n"
            "   - Lag phase [1]\n"
            "   - Accelerating / Exponential / Geometric phase [1]\n"
            "   - Decelerating phase [1]\n"
            "   - Stationary / Dynamic equilibrium phase [1]\n"
            "2. Lag phase explanation [2]: The starting breeding population is very small [1], and organisms require time to acclimatize to the environment, synthesize required enzymes, and locate reproductive partners [1].\n"
            "3. Limiting factors distinction [3]:\n"
            "   - Density-dependent factors: Exert greater pressure as population density rises (e.g. competition for food/shelter, predation pressure, infectious parasite spread) [1.5].\n"
            "   - Density-independent factors: Exert identical mortality regardless of population density (e.g. catastrophic droughts, volcanic eruptions, veld fires, flash floods) [1.5]."
        )
        hints = {
            "tier_1": "Think about the S-curve: starting slow, speeding up, slowing down, flattening out.",
            "tier_2": "Lag -> Exponential -> Deceleration -> Stationary. Density-dependent = competition/disease. Density-independent = weather disasters.",
            "tier_3": "1. Lag, Exponential, Decelerating, Stationary. 2. Small population adapting. 3. Density-dependent: food/disease; Independent: fire/floods.",
        }
        marks = 9
        misconceptions = ["confused_exponential_with_logistic", "density_dependent_independent_confusion"]
    else:  # predator_prey_cycle
        predator = r.choice(["Lion (*Panthera leo*)", "Cheetah (*Acinonyx jubatus*)", "Black-backed jackal"])
        prey = r.choice(["Zebra (*Equus quagga*)", "Springbok (*Antidorcas marsupialis*)", "Cape scrub hare"])
        prompt = (
            f"A multi-year ecological census in an unfenced game park tracked the fluctuating population numbers of **{prey}** (prey) "
            f"and **{predator}** (predator).\n\n"
            f"1. Explain why prey population peaks always precede the predator population peaks in a cyclic predator-prey graph.\n"
            f"2. Describe what happens to the predator population when the prey population crashes due to extreme drought.\n"
            f"3. Explain why predators are ecologically essential for maintaining genetic fitness within the prey population."
        )
        ans_str = (
            "1. Predators require an abundance of food before their birth rates can increase; therefore predator response lags behind prey peaks; "
            "2. Predator population declines through starvation and reduced reproduction; "
            "3. Predators selectively hunt the sick, weak, aged, or genetically inferior individuals, leaving healthier prey to reproduce."
        )
        memo = (
            "1. Predator lag rationale [2]: Increased prey provides abundant food, which subsequently elevates predator nutritional status, "
            "conception rates, and offspring survival [1]. Because gestation and maturation take time, the predator peak lags chronologically behind the prey peak [1].\n"
            "2. Drought prey crash effect [2]: A crash in prey numbers drastically diminishes the predator food supply [1], "
            "leading to widespread predator starvation, lower fecundity, elevated cub mortality, and a subsequent predator population crash [1].\n"
            "3. Evolutionary genetic fitness role [2]: Predators naturally cull the slowest, oldest, sickest, or genetically disadvantaged individuals [1], "
            "preventing harmful alleles from spreading and ensuring only the most fit individuals survive to pass on adaptive traits [1]."
        )
        hints = {
            "tier_1": "More food allows predators to reproduce, but it takes time. What happens when prey runs out?",
            "tier_2": "Predator numbers lag behind because of gestation time. When prey drops, predators starve. Predators cull the weakest prey.",
            "tier_3": "1. Predator reproduction lags behind food abundance. 2. Predators starve and numbers decline. 3. Predators remove weak/diseased individuals.",
        }
        marks = 6
        misconceptions = ["predator_peaks_first_misconception", "omitted_evolutionary_culling_role"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Phase identification or population peak lag mechanism", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Ecological rationale (limiting factors or starvation crash)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Evolutionary role or density dependent distinction", "marks": marks - 4, "editable": True},
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
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 11 Population Ecology."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("mark_recapture", "lincoln_index") or mode == "elementary_mark_recapture_formula":
            q = _generate_mark_recapture_investigation(sub_r, sub_seed, i, mode)
        elif subskill in ("growth_curves", "predator_prey", "carrying_capacity"):
            q = _generate_growth_curves_and_predator_prey(sub_r, sub_seed, i, mode)
        else:
            # Alternating between mark-recapture and population growth/predator-prey
            if i % 2 == 0:
                q = _generate_mark_recapture_investigation(sub_r, sub_seed, i, mode)
            else:
                q = _generate_growth_curves_and_predator_prey(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
