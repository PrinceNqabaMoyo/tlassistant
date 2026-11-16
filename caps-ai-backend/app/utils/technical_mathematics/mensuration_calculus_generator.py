"""Grade 11-12 Technical Mathematics — Mensuration & Integration (50 Semantic Archetypes).

Grounded strictly in:
- curriculum_docs_auto/TechnicalMathematics_Gr11/Term 4/01. Mensuration.md
- curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/04. Integration.md

Covers:
- 01–25: Right prisms, cylinders, hollow cylinders, pyramids, cones, spheres, composite solids,
         dimensional scaling, interval width h, mid-ordinate rule, trapezoidal rule, engineering excavation,
         indefinite integrals, power rule, and definite integrals as area.
- 26–50: Advanced mid-ordinate rule, trapezoidal rule, cubic curve area, fractional power integrals,
         area between curves, solids of revolution V = pi*int(y^2 dx), washer method,
         piecewise engineering profiles, work done by gas, hydrostatic force, and technical synthesis.

100% deterministic, zero-LLM, South African National Curriculum Standards compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.technical_mathematics.mensuration_calculus_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.technical_mathematics.mensuration_calculus_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "technical_mathematics_mensuration"
LO = "techmath_mensuration_calculus"

ALL_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ALL_BUILDERS.keys())
ARCHETYPES: List[str] = SUBSKILLS
BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = ALL_BUILDERS

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "03_trapezoidal_rule_four_intervals",
    "elementary_ordinate_interval": "01_interval_width_and_ordinate_count",
    "elementary_trapezoidal_formula": "03_trapezoidal_rule_four_intervals",
    "trapezoidal_rule": "04_trapezoidal_rule_five_intervals",
    "mid_ordinate_rule": "02_mid_ordinate_rule_calculation",
    "cylinder_surface_area": "11_cylinder_volume_and_total_surface_area",
    "cone_surface_area": "14_right_cone_slant_height_curved_surface_area",
    "pyramid_volume": "13_right_pyramid_square_base_volume_and_slant_height",
    "sphere_volume": "16_sphere_surface_area_and_volume",
    "definite_integral": "24_definite_integral_polynomial_evaluation",
    "solid_of_revolution": "42_volume_solid_of_revolution_cylindrical_disc",
}


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate(
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic questions for Technical Mathematics Mensuration & Integration."""
    base_seed = int(seed) if seed is not None else 42
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, int(count))):
        cur_seed = base_seed * 1000 + i if seed is not None else None
        rng = _rng(cur_seed)

        resolved = subskill or mode
        if resolved in LEGACY_ALIASES:
            resolved = LEGACY_ALIASES[resolved]

        if not resolved or resolved in ("mixed", "all", "default", "compound"):
            resolved = rng.choice(SUBSKILLS)
        elif resolved not in ALL_BUILDERS:
            matches = [s for s in SUBSKILLS if resolved in s]
            resolved = matches[0] if matches else rng.choice(SUBSKILLS)

        builder = ALL_BUILDERS[resolved]
        q = builder(rng)
        if cur_seed is not None:
            q["seed"] = cur_seed
            q["id"] = f"{TOPIC}_{resolved}_{cur_seed}"
        questions.append(q)

    return {"questions": questions}


generate_question = generate
