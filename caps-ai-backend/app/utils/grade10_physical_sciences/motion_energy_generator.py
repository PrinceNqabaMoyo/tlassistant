"""Grade 10 Physical Sciences — 1D Motion & Mechanical Energy Generator.
Central 50-Archetype Generator adhering to the 6-Pillar Generator Contract.
100% Aligned with South African National Curriculum Standards for Physical Sciences Grade 10 (Term 3).

Subskills:
  01–25: 1D Kinematics foundations, reference frames, position, displacement, speed,
         velocity, acceleration, the 4 equations of motion, stopping distance,
         position-time, velocity-time, and acceleration-time graph interpretation.
  26–50: Graph conversions, ticker-timer tape analysis, vertical motion under gravity,
         gravitational potential energy, kinetic energy, total mechanical energy,
         conservation of mechanical energy (free fall, projectiles, ramps, roller coasters,
         pendulums), friction dissipation, work, power, efficiency, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade10_physical_sciences.motion_energy_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade10_physical_sciences.motion_energy_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "Motion in one dimension"

# Combine 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

BUILDERS: Dict[str, Any] = {
    **ARCHETYPES,
}

# Legacy fallback builders for backward compatibility
def _legacy_kinematics(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["08_equation_motion_vf_from_vi_a_t"](r)

def _legacy_energy(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["38_conservation_mechanical_energy_free_fall_impact_speed"](r)

def _legacy_compound(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice(["08_equation_motion_vf_from_vi_a_t", "38_conservation_mechanical_energy_free_fall_impact_speed"])
    return ARCHETYPES[sub](r)

LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": _legacy_compound,
    "elementary_kinematics": _legacy_kinematics,
    "elementary_energy": _legacy_energy,
    "kinematics": _legacy_kinematics,
    "energy": _legacy_energy,
}


def get_subskills() -> List[str]:
    """Return the list of all 50 semantic subskills."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic question for a subskill."""
    r = random.Random(seed if seed is not None else 42)
    target = subskill or r.choice(SUBSKILLS)

    builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target)
    if not builder:
        builder = ARCHETYPES.get(r.choice(SUBSKILLS))

    try:
        q = builder(r)
    except TypeError:
        q = builder(r, difficulty=difficulty)

    if seed is not None:
        q["seed"] = seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Primary generator interface required by central generator registry and validation suite."""
    base_seed = 42 if seed is None else int(seed)
    chosen_target = subskill or mode

    questions = []
    for i in range(max(1, count)):
        curr_seed = base_seed * 1000 + i
        r = random.Random(curr_seed)

        target = chosen_target
        if not target or (target not in BUILDERS and target not in LEGACY_BUILDERS):
            target = SUBSKILLS[i % len(SUBSKILLS)]

        builder = BUILDERS.get(target) or LEGACY_BUILDERS.get(target)
        if not builder:
            builder = ARCHETYPES.get(SUBSKILLS[0])

        try:
            q = builder(r)
        except TypeError:
            q = builder(r, difficulty=difficulty)

        q["seed"] = curr_seed
        questions.append(q)

    return {"questions": questions}

# diagram_role: context (science / physics declarative context visualization)
