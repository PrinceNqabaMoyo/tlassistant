"""Natural Sciences Grade 9 Term 3: Cost of Electrical Energy Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Cost of electrical energy.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .cost_electrical_energy_archetypes_01_25 import BUILDERS_01_25
from .cost_electrical_energy_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Cost of electrical energy.md"
TOPIC_NAME = "Cost of electrical energy"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for idx, key in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[idx] = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[key]

# Legacy backward-compatibility aliases from original 5-subskill module
DISPATCH_TABLE["power_rating_and_watt_unit_conversion"] = ARCHETYPE_BUILDERS["08_converting_watts_to_kilowatts_divide_by_1000"]
DISPATCH_TABLE["electrical_energy_kwh_formula"] = ARCHETYPE_BUILDERS["21_calculating_energy_kwh_watts_to_kw_conversion"]
DISPATCH_TABLE["cost_calculation_with_tariffs"] = ARCHETYPE_BUILDERS["28_single_appliance_operating_cost_watts_hours_tariff"]
DISPATCH_TABLE["appliance_consumption_ranking"] = ARCHETYPE_BUILDERS["14_sequencing_appliances_highest_to_lowest_power"]
DISPATCH_TABLE["energy_efficiency_and_conservation_strategies"] = ARCHETYPE_BUILDERS["43_percentage_energy_saved_led_bulb_upgrade"]


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    archetype: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Grade 9 Natural Sciences: Cost of electrical energy."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []
    target = subskill if subskill not in (None, "", "mixed", "auto", "default") else archetype

    for _ in range(max(1, count)):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        if target is not None:
            sub_key = str(target).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            try:
                idx = int(archetype_index)
                if idx in DISPATCH_TABLE:
                    builder = DISPATCH_TABLE[idx]
                elif 1 <= idx <= len(SUBSKILLS):
                    builder = ARCHETYPE_BUILDERS[SUBSKILLS[idx - 1]]
            except (ValueError, TypeError):
                pass

        if builder is None:
            builder = ARCHETYPE_BUILDERS[rng.choice(SUBSKILLS)]

        q = builder(rng)
        q.setdefault("grade", 9)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("term", 3)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
