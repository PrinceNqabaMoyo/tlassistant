"""Grade 11 Mathematics — Linear Programming & Investigations: 50 Distinct Semantic Subskill Archetypes.
Deterministic 6-Pillar Generator conforming to South African National Curriculum Standards.
Reference curriculum:
- curriculum_docs_auto/Mathematics_Gr11/Term 1/01. Linear programming.md
- curriculum_docs_auto/Mathematics_Gr11/Term 1/02. investigation and projects.md

Covers 50 distinct semantic subskills (01..50):
- Formulating linear inequality constraints and objective functions from word contexts (01..10)
- Graphing linear inequalities, boundary lines, feasible regions, and corner vertices (11..25)
- Objective function evaluation, search-line gradient method, and corner-point theorem (26..38)
- Applied optimisation models, mathematical investigations, sensitivity analysis, and diagnostic autopsy (39..50)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from ._math_common import rng
from .linear_programming_archetypes_01_25 import ARCHETYPES_01_25
from .linear_programming_archetypes_26_50 import ARCHETYPES_26_50

ARCHETYPES: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

BUILDERS = ARCHETYPES
SUBSKILLS: List[str] = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS
AVAILABLE_SUBSKILLS: List[str] = SUBSKILLS

LEGACY_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "elementary_inequalities_formulation": ARCHETYPES["06_formulate_two_resource_manufacturing_system_from_table"],
    "elementary_corner_points": ARCHETYPES["22_list_all_corner_point_vertices_of_bounded_feasible_region_svg"],
    "elementary_profit_maximisation": ARCHETYPES["27_maximise_profit_using_corner_point_theorem_svg"],
}


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill identifiers."""
    return list(SUBSKILLS)


def generate_question(subskill: Optional[str] = None, seed: Optional[int] = None) -> Dict[str, Any]:
    """Generate a single deterministic Linear Programming question for the requested subskill."""
    r = rng(seed)
    if subskill and subskill in ARCHETYPES:
        return ARCHETYPES[subskill](r)
    if subskill and subskill in LEGACY_BUILDERS:
        return LEGACY_BUILDERS[subskill](r)
    chosen = r.choice(SUBSKILLS)
    return ARCHETYPES[chosen](r)


def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Public 6-pillar generator entry point returning {'questions': [...]}."""
    r = rng(seed)
    questions: List[Dict[str, Any]] = []

    target_key: Optional[str] = None
    if subskill and subskill in ARCHETYPES:
        target_key = subskill
    elif mode in ARCHETYPES:
        target_key = mode
    elif subskill and subskill in LEGACY_BUILDERS:
        target_key = subskill
    elif mode in LEGACY_BUILDERS:
        target_key = mode

    for i in range(max(1, count)):
        sub_r = rng(r.randint(1, 1_000_000_000) + i * 97)
        if target_key and target_key in ARCHETYPES:
            questions.append(ARCHETYPES[target_key](sub_r))
        elif target_key and target_key in LEGACY_BUILDERS:
            questions.append(LEGACY_BUILDERS[target_key](sub_r))
        else:
            key = SUBSKILLS[(r.randint(0, len(SUBSKILLS) - 1) + i) % len(SUBSKILLS)]
            questions.append(ARCHETYPES[key](sub_r))

    return {"questions": questions}
