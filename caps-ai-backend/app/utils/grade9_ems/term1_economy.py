"""
Grade 9 EMS Term 1: The Economy - Economic Systems.
Deterministic 50-archetype question generator grounded in SA curriculum standards.
"""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term1_economy_archetypes_01_25 import ARCHETYPE_BUILDERS_01_25, SUBTOPIC_ID, TOPIC_NAME
from .term1_economy_archetypes_26_50 import ARCHETYPE_BUILDERS_26_50


TOPIC_ID = "grade9_ems"
CURRICULUM_REFERENCE = "Term 1 > The Economy: Economic Systems"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {}
ARCHETYPE_BUILDERS.update(ARCHETYPE_BUILDERS_01_25)
ARCHETYPE_BUILDERS.update(ARCHETYPE_BUILDERS_26_50)

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

DISPATCH_TABLE: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for idx, skill_name in enumerate(ORDERED_SUBSKILLS, start=1):
    DISPATCH_TABLE[str(idx)] = ARCHETYPE_BUILDERS[skill_name]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[skill_name]

# Legacy caller aliases preserved for full backward compatibility
DISPATCH_TABLE["economic_systems_matrix"] = ARCHETYPE_BUILDERS["17_compare_systems_ownership_matrix"]
DISPATCH_TABLE["elementary_matrix"] = ARCHETYPE_BUILDERS["18_compare_systems_allocation_questions"]
DISPATCH_TABLE["advantages_disadvantages"] = ARCHETYPE_BUILDERS["26_pros_cons_system_matching_matrix"]
DISPATCH_TABLE["south_african_mixed_economy"] = ARCHETYPE_BUILDERS["19_sa_mixed_economy_private_public"]
DISPATCH_TABLE["global_economy_trade"] = ARCHETYPE_BUILDERS["35_imports_vs_exports_balance_of_trade"]
DISPATCH_TABLE["concepts"] = ARCHETYPE_BUILDERS["01_basic_economic_problem_scarcity"]

BUILDERS = DISPATCH_TABLE


def get_subskills() -> List[str]:
    """Return ordered list of all 50 semantic subskill identifiers."""
    return list(ORDERED_SUBSKILLS)


def _resolve_builder(subskill: Optional[str], rng: random.Random) -> Callable[[random.Random, str], Dict[str, Any]]:
    if subskill and subskill not in ("all", "compound", "default", "mixed"):
        key = str(subskill).strip()
        if key in DISPATCH_TABLE:
            return DISPATCH_TABLE[key]
        low = key.lower()
        for k, fn in ARCHETYPE_BUILDERS.items():
            if low in k:
                return fn
    return ARCHETYPE_BUILDERS[rng.choice(ORDERED_SUBSKILLS)]


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate Grade 9 EMS Term 1 Economic Systems questions."""
    base_seed = seed if seed is not None else random.randint(1, 10**6)
    results: List[Dict[str, Any]] = []
    for idx in range(max(1, int(count))):
        item_rng = random.Random(int(base_seed) + idx * 7919)
        builder = _resolve_builder(subskill, item_rng)
        q = builder(item_rng, mode)
        q["difficulty"] = difficulty
        q["mode"] = mode
        q["topic"] = TOPIC_NAME
        q["subtopic"] = SUBTOPIC_ID
        results.append(q)
    return results


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single Grade 9 EMS Term 1 Economic Systems question."""
    return generate(
        subskill=subskill,
        difficulty=difficulty,
        count=1,
        mode=mode,
        seed=seed,
        **kwargs,
    )[0]
