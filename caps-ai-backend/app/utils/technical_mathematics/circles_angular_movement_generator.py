"""Grade 10–12 Technical Mathematics — Circles, Angles & Angular Movement Generator.
Deterministic 6-pillar question generator covering Paper 2 (Term 3).
100% Aligned with South African National Curriculum Standards for Technical Mathematics.

Subskills:
  01–25: Radian and degree conversions, arc lengths, circular sector perimeters and areas,
         segment areas (minor and major), sagitta and chord lengths, annular rings (washers),
         liquid levels in cylindrical tanks and pipes.
  26–50: Angular velocity and rotational frequency (rpm, rps, rad/s), circumferential linear
         speed (v = omega * r), belt-and-pulley transmission systems, meshed gear trains,
         winch drums, vehicle wheel speed conversions, conveyors, diagnostic autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.technical_mathematics.circles_angular_movement_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.technical_mathematics.circles_angular_movement_archetypes_26_50 import (
    ARCHETYPES_26_50,
)

TOPIC = "Circles, angles and angular movement"

# Combine 50 semantic subskills
ARCHETYPES: Dict[str, Any] = {
    **BUILDERS_01_25,
    **ARCHETYPES_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPES.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

BUILDERS: Dict[str, Any] = {
    **ARCHETYPES,
}

# Legacy fallback builders for backward compatibility
def _legacy_arc_sector(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["12_area_of_circular_sector_given_radians"](r)

def _legacy_angular_velocity(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["27_angular_velocity_from_rotational_frequency_rad_per_sec"](r)

def _legacy_hydraulic_gears_pulleys(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["36_belt_and_pulley_drive_equal_linear_speed_svg"](r)

def _legacy_compound(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "12_area_of_circular_sector_given_radians",
        "31_circumferential_linear_velocity_from_radius_and_omega_svg",
    ])
    return ARCHETYPES[sub](r)

LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": _legacy_compound,
    "elementary_arc_sector": _legacy_arc_sector,
    "elementary_angular_velocity": _legacy_angular_velocity,
    "radian_sector": lambda r, **kw: ARCHETYPES["07_calculate_arc_length_given_radius_and_radians"](r),
    "arc_sector": _legacy_arc_sector,
    "sector": lambda r, **kw: ARCHETYPES["13_area_of_circular_sector_given_degrees"](r),
    "angular_velocity": _legacy_angular_velocity,
    "velocity": lambda r, **kw: ARCHETYPES["31_circumferential_linear_velocity_from_radius_and_omega_svg"](r),
    "hydraulic_gears_belt_pulley": _legacy_hydraulic_gears_pulleys,
    "gears_pulleys": lambda r, **kw: ARCHETYPES["41_meshed_spur_gears_velocity_ratio_and_teeth_count_svg"](r),
    "gears": lambda r, **kw: ARCHETYPES["41_meshed_spur_gears_velocity_ratio_and_teeth_count_svg"](r),
    "hydraulics": _legacy_hydraulic_gears_pulleys,
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

# diagram_role: context (math / ems declarative context visualization)
