"""Natural Sciences Grade 9 Term 3: Energy and the National Electricity Grid Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Energy and the national electricity grid.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .national_grid_archetypes_01_25 import BUILDERS_01_25
from .national_grid_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Energy and the national electricity grid.md"
TOPIC_NAME = "Energy and the national electricity grid"

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

# Legacy backward-compatibility aliases
DISPATCH_TABLE["power_station_energy_conversions"] = ARCHETYPE_BUILDERS["02_coal_station_complete_energy_transformation_chain"]
DISPATCH_TABLE["step_up_and_step_down_transformers"] = ARCHETYPE_BUILDERS["42_step_up_vs_step_down_transformer_voltage_current_effect"]
DISPATCH_TABLE["transmission_heating_losses_and_high_voltage"] = ARCHETYPE_BUILDERS["45_joule_heating_power_loss_formula_i_squared_r"]
DISPATCH_TABLE["south_african_power_mix_and_koeberg"] = ARCHETYPE_BUILDERS["30_koeberg_nuclear_power_station_location_and_cooling"]
DISPATCH_TABLE["environmental_impacts_and_renewable_alternatives"] = ARCHETYPE_BUILDERS["08_coal_combustion_greenhouse_gases_and_acid_rain_impacts"]


def _normalize_res(res: Dict[str, Any], term: int = 3) -> Dict[str, Any]:
    """Normalize legacy result fields while keeping 6-pillar contract metadata."""
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    elif "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res.setdefault("grade", 9)
    res.setdefault("subject", "Natural Sciences")
    res.setdefault("topic", TOPIC_NAME)
    res["term"] = term
    return res


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Grade 9 Natural Sciences: Energy and the national electricity grid."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        if subskill is not None:
            sub_key = str(subskill).strip()
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
        q.setdefault("mode", mode)
        questions.append(_normalize_res(q, term=3))

    return questions


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
