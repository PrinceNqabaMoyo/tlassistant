"""Natural Sciences Grade 9 Term 3: Series and Parallel Circuits Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/02. Series and parallel circuits.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .series_parallel_circuits_archetypes_01_25 import BUILDERS_01_25
from .series_parallel_circuits_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 3/02. Series and parallel circuits.md"
TOPIC_NAME = "Series and parallel circuits"

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
DISPATCH_TABLE["series_circuit_current_and_voltage"] = ARCHETYPE_BUILDERS["05_current_uniformity_everywhere_in_series_loop"]
DISPATCH_TABLE["parallel_circuit_current_and_voltage"] = ARCHETYPE_BUILDERS["20_parallel_branch_current_splitting_rule"]
DISPATCH_TABLE["meter_placement_ammeter_vs_voltmeter"] = ARCHETYPE_BUILDERS["35_meter_misconnection_ammeter_parallel_vs_voltmeter_series"]
DISPATCH_TABLE["bulb_failure_diagnostics_series_vs_parallel"] = ARCHETYPE_BUILDERS["48_series_parallel_troubleshooting_christmas_lights_vs_house"]
DISPATCH_TABLE["circuit_calculation_and_spec_generation"] = ARCHETYPE_BUILDERS["38_mixed_circuit_combined_resistance_and_current_calc"]


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
    """Generate questions for Grade 9 Natural Sciences: Series and parallel circuits."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        if subskill is not None and str(subskill).strip().lower() not in ("", "mixed", "auto", "all"):
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
        questions.append(q)

    return questions


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
