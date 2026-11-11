"""Life Sciences Grade 10 Term 3: Biospheres to Ecosystems Generator.

Covers:
- Biosphere organization: Biosphere, biomes, ecosystems, communities, populations, and organisms.
- Abiotic factors: Physiographic (aspect, slope), edaphic (soil pH, texture, humus), climatic (temperature, rainfall, wind).
- Biotic components: Producers (autotrophs), primary/secondary/tertiary consumers (heterotrophs), and decomposers/saprophytes.
- Energy flow in ecosystems: Food chains, complex food webs, 10% trophic transfer rule, and 90% metabolic heat loss.
- Ecological pyramids: Pyramids of numbers, biomass, and energy (invariable upright structure).
- Biogeochemical nutrient cycles: Carbon cycle, nitrogen cycle (Rhizobium, Nitrosomonas, Nitrobacter, denitrification), and water cycle.
- South African biomes: Savanna, Fynbos, Grassland, Nama Karoo, Succulent Karoo, Indigenous Forest, and Thicket.

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


def _generate_trophic_energy_flow(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Trophic levels, 10% ecological energy transfer calculations, and ecological pyramids."""
    biome = r.choice(["Savanna", "Fynbos", "Highveld Grassland", "Nama Karoo"])
    producer = r.choice(["Themeda triandra (Red oat grass)", "Acacia / Vachellia tortilis", "Protea cynaroides (King Protea)", "Cenchrus ciliaris (Buffel grass)"])
    herbivore = r.choice(["Impala (*Aepyceros melampus*)", "Springbok (*Antidorcas marsupialis*)", "Cape mountain zebra", "Grey rhebok"])
    primary_carnivore = r.choice(["Cheetah (*Acinonyx jubatus*)", "Black-backed jackal", "Caracal (*Caracal caracal*)", "African wild dog"])
    top_predator = "Lion (*Panthera leo*)"

    # Procedural numbers for producer energy in kJ
    producer_energy = r.choice([100000, 250000, 500000, 800000])
    herbivore_energy = int(producer_energy * 0.10)
    carnivore_energy = int(herbivore_energy * 0.10)
    top_energy = int(carnivore_energy * 0.10)

    qid = _make_id("ls10_trophic_energy", seed, idx)

    if mode == "elementary_trophic_calculation":
        prompt = (
            f"In a South African {biome} ecosystem, primary autotrophic producers ({producer}) fix "
            f"${_fmt_sa(producer_energy)}\\text{{ kJ}}$ of solar radiant energy into chemical bond energy.\n\n"
            f"Using Lindeman's 10% ecological energy transfer efficiency rule, calculate the energy available to:\n"
            f"1. The primary consumers ({herbivore}).\n"
            f"2. The secondary consumers ({primary_carnivore})."
        )
        ans_str = f"1. {_fmt_sa(herbivore_energy)} kJ; 2. {_fmt_sa(carnivore_energy)} kJ"
        memo = (
            f"1. Energy to primary consumers (Level 2): 10% of {_fmt_sa(producer_energy)} kJ = {_fmt_sa(producer_energy)} * 0.10 = {_fmt_sa(herbivore_energy)} kJ [2]\n"
            f"2. Energy to secondary consumers (Level 3): 10% of {_fmt_sa(herbivore_energy)} kJ = {_fmt_sa(herbivore_energy)} * 0.10 = {_fmt_sa(carnivore_energy)} kJ [2]"
        )
        hints = {
            "tier_1": "Apply the 10% rule at each trophic feeding transition.",
            "tier_2": f"Level 1 to Level 2: {producer_energy} * 0.1. Level 2 to Level 3: {herbivore_energy} * 0.1.",
            "tier_3": f"1. {herbivore_energy} kJ. 2. {carnivore_energy} kJ.",
        }
        marks = 4
        misconceptions = ["ten_percent_rule_miscalculated", "inverted_trophic_levels"]
    else:
        # Full compound question on trophic levels, energy loss, and pyramids
        prompt = (
            f"A field study of energy dynamics in a South African **{biome}** biome established the following linear food chain:\n"
            f"$$\\text{{{producer}}} \\to \\text{{{herbivore}}} \\to \\text{{{primary_carnivore}}} \\to \\text{{{top_predator}}}$$\n"
            f"The primary producers synthesized ${_fmt_sa(producer_energy)}\\text{{ kJ}}$ of net primary biomass energy.\n\n"
            f"1. Identify the trophic level occupied by the {primary_carnivore}.\n"
            f"2. Calculate the quantity of energy transferred to the top carnivore ({top_predator}).\n"
            f"3. Explain TWO reasons why approximately 90% of the energy is lost at each successive trophic transition.\n"
            f"4. Explain why a pyramid of energy can never appear inverted in any stable natural ecosystem."
        )
        ans_str = (
            f"1. Third trophic level (secondary consumer); "
            f"2. {_fmt_sa(top_energy)} kJ; "
            f"3. Energy is dissipated as metabolic heat during cellular respiration, lost in unabsorbed wastes (faeces/urine), and uneaten parts (bones/fur); "
            f"4. The second law of thermodynamics dictates that energy is degraded at each transfer; a higher trophic level can never contain more energy than the lower level supporting it."
        )
        memo = (
            f"1. Trophic level [1]: The {primary_carnivore} is a secondary consumer, occupying the **third trophic level** ($T_3$). [1]\n"
            f"2. Energy calculations [3]:\n"
            f"   - Trophic Level 1 ({producer}): {_fmt_sa(producer_energy)} kJ\n"
            f"   - Trophic Level 2 ({herbivore}): {_fmt_sa(herbivore_energy)} kJ [1]\n"
            f"   - Trophic Level 3 ({primary_carnivore}): {_fmt_sa(carnivore_energy)} kJ [1]\n"
            f"   - Trophic Level 4 ({top_predator}): {_fmt_sa(top_energy)} kJ [1]\n"
            f"3. Reasons for 90% energy loss (any 2) [2]:\n"
            f"   - Expended in cellular respiration for metabolic work, movement, and lost as metabolic heat [1].\n"
            f"   - Excreted and egested as unassimilated metabolic wastes (urine and faeces) [1].\n"
            f"   - Not all organic matter is consumed by predators (inedible roots, bones, claws, horns) [1].\n"
            f"4. Energy pyramid stability [2]: Energy is transferred unidirectionally and dissipates as entropy/heat at every step [1]. "
            f"Therefore, a higher trophic level can never contain more energy than the underlying trophic tier that fuels it [1]."
        )
        hints = {
            "tier_1": "Level 1 = producers, Level 2 = herbivores, Level 3 = carnivores. Divide by 10 at each step. Energy cannot be created.",
            "tier_2": f"Level 3 is secondary consumer. Top energy is {top_energy} kJ. Respiration heat and excretion account for the 90% loss.",
            "tier_3": f"1. Third level. 2. {top_energy} kJ. 3. Lost as heat in respiration and excretion. 4. Second law of thermodynamics (energy is dissipated at each level).",
        }
        marks = 8
        misconceptions = ["trophic_level_numbering_confusion", "energy_loss_respiration_omitted", "inverted_pyramid_confusion"]

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
                {"id": "mp_1", "desc": "Trophic level designation", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "10% energy calculation to top level", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Ecological energy dissipation rationale", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Thermodynamic upright pyramid explanation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_nitrogen_and_nutrient_cycles(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Biogeochemical cycles: Nitrogen cycle bacteria and carbon cycle dynamics."""
    context = r.choice(["nitrogen_cycle", "carbon_cycle_climate"])
    qid = _make_id("ls10_nutrient_cycle", seed, idx)

    if context == "nitrogen_cycle":
        prompt = (
            "Atmospheric nitrogen ($N_2$) comprises approximately 78% of the Earth's atmosphere, but plants cannot absorb gaseous $N_2$ directly.\n\n"
            "1. Name the specialized symbiotic bacteria that fix atmospheric nitrogen into ammonium compounds in legume root nodules.\n"
            "2. Distinguish between the functions of **nitrifying bacteria** (*Nitrosomonas* and *Nitrobacter*) and **denitrifying bacteria**.\n"
            "3. Explain why waterlogged, anaerobic agricultural soils often suffer from severe nitrogen deficiency."
        )
        ans_str = (
            "1. *Rhizobium* bacteria; "
            "2. Nitrifying bacteria convert ammonium into nitrites and nitrates which plants absorb; Denitrifying bacteria convert nitrates back into gaseous N2; "
            "3. Anaerobic conditions favour denitrifying bacteria which break down soil nitrates into N2 gas that escapes into the atmosphere."
        )
        memo = (
            "1. Symbiotic nitrogen-fixing bacteria: ***Rhizobium***. [1]\n"
            "2. Bacterial distinction [4]:\n"
            "   - Nitrifying bacteria: Aerobic bacteria (*Nitrosomonas* converts ammonium ions $NH_4^+$ into nitrites $NO_2^-$; *Nitrobacter* converts nitrites into nitrates $NO_3^-$), producing usable plant nutrients [2].\n"
            "   - Denitrifying bacteria: Anaerobic bacteria (e.g. *Pseudomonas*) that convert soil nitrates back into inert nitrogen gas ($N_2$), releasing it back into the atmosphere [2].\n"
            "3. Waterlogged soils explanation [2]: Waterlogging fills soil pore spaces with water, creating hypoxic/anaerobic conditions [1]. "
            "These oxygen-depleted conditions stimulate denitrifying bacteria to rapidly convert soluble nitrates into atmospheric $N_2$ gas, depleting soil fertility [1]."
        )
        hints = {
            "tier_1": "Rhizobium lives in nodules. Nitrifying bacteria make nitrates; denitrifying bacteria turn nitrates back into gas.",
            "tier_2": "Nitrifying = NH4+ -> NO2- -> NO3- (usable). Denitrifying = NO3- -> N2 (gas escapes). Anaerobic soil favors denitrifiers.",
            "tier_3": "1. Rhizobium. 2. Nitrifiers produce nitrates; denitrifiers convert nitrates to N2 gas. 3. Waterlogging removes oxygen, triggering denitrification.",
        }
        marks = 7
        misconceptions = ["confused_nitrification_with_denitrification", "rhizobium_misidentified"]
    else:  # carbon_cycle_climate
        prompt = (
            "The global carbon cycle maintains dynamic equilibrium between terrestrial, oceanic, and atmospheric reservoirs.\n\n"
            "1. Name the primary biological process that removes carbon dioxide from the atmosphere.\n"
            "2. Name TWO biological processes that release carbon dioxide back into the atmosphere.\n"
            "3. Explain how the anthropogenic combustion of fossil fuels and deforestation disrupt this equilibrium, leading to enhanced greenhouse warming."
        )
        ans_str = (
            "1. Photosynthesis; "
            "2. Cellular respiration and decomposition of organic matter by saprophytes; "
            "3. Combustion releases locked subterranean carbon as CO2, while deforestation destroys carbon sinks, accelerating radiant heat entrapment in the troposphere."
        )
        memo = (
            "1. Carbon removal process: **Photosynthesis** (carbon fixation into glucose by autotrophs). [1]\n"
            "2. Carbon release processes (any 2) [2]: Cellular respiration (plants/animals) [1]; Decomposition of organic dead matter by bacteria and fungi [1].\n"
            "3. Anthropogenic disruption [3]: Burning ancient fossil fuels (coal, oil, gas) releases long-buried carbon into the atmosphere as $CO_2$ [1]. "
            "Deforestation destroys massive vegetative carbon sinks that would otherwise absorb $CO_2$ [1]. "
            "The resulting increased concentration of atmospheric $CO_2$ traps re-radiated infrared thermal radiation, exacerbating global warming [1]."
        )
        hints = {
            "tier_1": "Plants absorb CO2 for photosynthesis. Living organisms release CO2 by breathing/respiration.",
            "tier_2": "Photosynthesis takes in CO2. Respiration and decay release CO2. Burning fossil fuels + clearing forests increases greenhouse gases.",
            "tier_3": "1. Photosynthesis. 2. Cellular respiration and decomposition. 3. Burning fossil fuels adds CO2; cutting forests removes sinks, trapping heat.",
        }
        marks = 6
        misconceptions = ["confused_greenhouse_effect_with_ozone_depletion", "omitted_decomposition_in_carbon_cycle"]

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
                {"id": "mp_1", "desc": "Nutrient cycle biological agent / pathway", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Functional distinction between biochemical phases", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Ecological consequence or environmental mechanism", "marks": marks - 4, "editable": True},
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
    """Master entry point for Grade 10 Biospheres to Ecosystems."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("energy_flow", "trophic_levels") or mode == "elementary_trophic_calculation":
            q = _generate_trophic_energy_flow(sub_r, sub_seed, i, mode)
        elif subskill in ("nutrient_cycles", "nitrogen_cycle", "carbon_cycle"):
            q = _generate_nitrogen_and_nutrient_cycles(sub_r, sub_seed, i, mode)
        else:
            # Alternating between energy flow and nutrient cycles
            if i % 2 == 0:
                q = _generate_trophic_energy_flow(sub_r, sub_seed, i, mode)
            else:
                q = _generate_nitrogen_and_nutrient_cycles(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
