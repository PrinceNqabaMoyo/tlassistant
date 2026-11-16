"""Grade 11 Physical Sciences — Vectors in 2D, Newton's Laws & Units Applied (50-Archetype Generator).
100% aligned with South African National Curriculum Standards (Grade 11 Physics Paper 1: Term 1, Term 2, Term 4).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/01. Vectors in two dimensions.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 2/01. Newton's laws.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 4/02. Units applied.md

Exports 50 distinct semantic subskills (01_<name> .. 50_<name>) across two modular archetype files (< 2000 lines each).
Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints, marking schemas, and inline SVG specs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_physical_sciences.vectors_newton_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade11_physical_sciences.vectors_newton_archetypes_26_50 import (
    BUILDERS_26_50,
)

try:
    from app.utils.physical_sciences.physical_sciences_builders import (
        build_pulley_incline_masses_system_question,
    )
except ImportError:
    from ..physical_sciences.physical_sciences_builders import (
        build_pulley_incline_masses_system_question,
    )

TOPIC = "grade11_vectors_newton"
LO = "phys11_vectors_newton"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

BUILDERS: Dict[str, Any] = ARCHETYPE_BUILDERS
ARCHETYPES: Dict[str, Any] = ARCHETYPE_BUILDERS

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

# Legacy shorthand aliases for backwards compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "compound": "48_half_atwood_pulley_system_horizontal_and_hanging_mass",
    "vectors": "06_vector_components_horizontal_cosine",
    "components": "06_vector_components_horizontal_cosine",
    "resolution": "06_vector_components_horizontal_cosine",
    "elementary_vector_resolution": "06_vector_components_horizontal_cosine",
    "elementary_resultant_pythagoras": "11_resultant_two_perpendicular_forces_pythagoras",
    "newton": "31_newtons_second_law_horizontal_accelerating_crate",
    "friction": "37_kinetic_friction_constant_velocity_or_acceleration",
    "second_law": "31_newtons_second_law_horizontal_accelerating_crate",
    "elementary_newton_second_law": "31_newtons_second_law_horizontal_accelerating_crate",
    "incline": "40_inclined_plane_weight_components_parallel_perpendicular",
    "slope": "40_inclined_plane_weight_components_parallel_perpendicular",
    "ramp": "40_inclined_plane_weight_components_parallel_perpendicular",
    "elementary_inclined_friction": "42_inclined_plane_sliding_down_with_kinetic_friction",
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 11 Physical Sciences Vectors & Newton's Laws question."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    rng = random.Random(base_seed)

    if subskill in ("pulley", "incline_pulley", "connected_masses", "pulley_incline_masses_system") or mode == "elementary_pulley_incline":
        return build_pulley_incline_masses_system_question(base_seed, grade=11, mode=mode or "compound")

    target = subskill or (mode if mode and mode in LEGACY_ALIASES else None)
    if target and target not in ("mixed", "all", ""):
        resolved = LEGACY_ALIASES.get(target, target)
        builder = ARCHETYPE_BUILDERS.get(resolved)
        if not builder:
            matches = [s for s in ORDERED_SUBSKILLS if target.lower() in s.lower()]
            builder = ARCHETYPE_BUILDERS[matches[0]] if matches else ARCHETYPE_BUILDERS[ORDERED_SUBSKILLS[0]]
    else:
        chosen = rng.choice(ORDERED_SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[chosen]

    q = builder(rng)
    if seed is not None:
        q["seed"] = seed
    if "question" not in q and "prompt" in q:
        q["question"] = q["prompt"]
    if "question_text" not in q and "prompt" in q:
        q["question_text"] = q["prompt"]
    if "correct_answer" not in q and "answer_latex" in q:
        q["correct_answer"] = q["answer_latex"]
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate a list of deterministic Grade 11 Physical Sciences Vectors & Newton's Laws questions."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        curr_seed = base_seed + (i * 37)
        if subskill and subskill not in ("mixed", "all", ""):
            q = generate_question(subskill=subskill, seed=curr_seed, difficulty=difficulty, mode=mode, **kwargs)
        else:
            sub = ORDERED_SUBSKILLS[(base_seed + i) % len(ORDERED_SUBSKILLS)]
            q = generate_question(subskill=sub, seed=curr_seed, difficulty=difficulty, mode=mode, **kwargs)
        questions.append(q)

    return questions
