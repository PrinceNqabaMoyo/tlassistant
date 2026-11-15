"""Grade 10 & 11 Mathematics — Measurements: 50 Distinct Semantic Subskill Archetypes.
Deterministic 6-Pillar Generator conforming to South African National Curriculum Standards.
Reference curriculum:
- curriculum_docs_auto/Mathematics_Gr10/Term 4/01. Measurements.md
- curriculum_docs_auto/Mathematics_Gr11/Term 3/01. Measurement.md

Covers 50 distinct semantic subskills (01..50):
- 2D Polygons, Circles, Sectors, Annuli & Composite Areas (01..12)
- Right Prisms & Right Circular Cylinders (13..25)
- Right Pyramids & Right Circular Cones (26..34)
- Spheres, Hemispheres & Composite Solids (35..43)
- Dimensional Scaling (k-factor), Unit Conversions, Costing & Diagnostic Autopsy (44..50)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .._math_common import rng
from .measurements_archetypes_01_25 import ARCHETYPES_01_25
from .measurements_archetypes_26_50 import ARCHETYPES_26_50

ARCHETYPES: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **ARCHETYPES_01_25,
    **ARCHETYPES_26_50,
}

BUILDERS = ARCHETYPES
SUBSKILLS: List[str] = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS
AVAILABLE_SUBSKILLS: List[str] = SUBSKILLS

LEGACY_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "elementary_surface_area": ARCHETYPES["21_total_surface_area_closed_cylinder_svg"],
    "elementary_volume": ARCHETYPES["19_volume_of_right_circular_cylinder_svg"],
    "elementary_scaling_k": ARCHETYPES["45_scaling_all_dimensions_by_k_effect_on_volume"],
}


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill identifiers."""
    return list(SUBSKILLS)


def generate_question(subskill: Optional[str] = None, seed: Optional[int] = None) -> Dict[str, Any]:
    """Generate a single deterministic Measurements question for the requested subskill."""
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
