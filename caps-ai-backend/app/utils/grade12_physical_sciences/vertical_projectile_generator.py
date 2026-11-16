"""Grade 12 Physical Sciences — Vertical Projectile Motion in 1D & Skills for Science Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/02. Vertical projectile motion in one dimension.md

Registered Topics in caps_term_registry_data.json:
1. Vertical projectile motion in one dimension (Grade 12 Term 1)
2. Skills for science (Grade 12 Term 4)

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1, caps_weight_percent=20, suggested_duration_mins=5.
2. 50 Distinct Semantic Subskills (01..50), 0 synthetic shims.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Pre-Baked Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade12_physical_sciences.vertical_projectile_archetypes_01_25 import (
    BUILDERS_01_25,
    SUBSKILLS_01_25,
)
from app.utils.grade12_physical_sciences.vertical_projectile_archetypes_26_50 import (
    BUILDERS_26_50,
    SUBSKILLS_26_50,
)

TOPIC = "grade12_vertical_projectile"
LO = "PS12.VPM"

# Aggregate all 50 distinct semantic archetype builders
BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(BUILDERS.keys())
ARCHETYPES: List[str] = list(BUILDERS.keys())
AVAILABLE_SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_vertical_projectile_diagnostic_synthesis",
    "concepts": "01_free_fall_and_projectile_definition",
    "scaffold": "04_dropped_object_velocity_after_time",
    "ground": "12_projected_upwards_maximum_height_reached",
    "max_height": "12_projected_upwards_maximum_height_reached",
    "apex": "02_acceleration_at_maximum_height_apex",
    "cliff": "18_cliff_launch_upwards_maximum_height_above_ground",
    "building": "22_cliff_height_from_upward_launch_and_time",
    "flight_time": "20_cliff_launch_upwards_total_flight_time",
    "elementary_projectile_apex_time": "11_projected_upwards_time_to_maximum_height",
    "elementary_projectile_max_height": "12_projected_upwards_maximum_height_reached",
    "elementary_projectile_impact_velocity": "19_cliff_launch_upwards_final_impact_velocity",
    "elementary_cliff_trajectory": "18_cliff_launch_upwards_maximum_height_above_ground",
    "skills_for_science": "48_skills_for_science_percentage_error_and_uncertainty",
    "variables": "49_skills_for_science_independent_dependent_controlled_variables",
    "ticker_timer": "46_experimental_data_ticker_timer_free_fall",
    "photogate": "47_experimental_data_photogate_dual_flag_timing",
    "bouncing_ball": "26_bouncing_ball_rebound_velocity_and_speed_loss",
    "balloon": "29_hot_air_balloon_ascending_dropped_object",
    "graphs": "35_velocity_time_graph_upward_projection_from_ground",
}


def get_subskills() -> List[str]:
    """Return ordered list of all 50 semantic subskill identifiers."""
    return list(SUBSKILLS)


def _resolve_builder(target: Optional[str]) -> Optional[Callable[[random.Random], Dict[str, Any]]]:
    if not target or target in ("mixed", "all", "default"):
        return None
    if target in BUILDERS:
        return BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target]]
    t_low = str(target).strip().lower()
    for k, b in BUILDERS.items():
        if t_low == k.lower() or t_low in k.lower():
            return b
    return None


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic 6-pillar question for Grade 12 Vertical Projectile Motion."""
    base_seed = 42 if seed is None else int(seed)
    r = random.Random(base_seed)
    effective_target = subskill or kwargs.get("archetype") or kwargs.get("mode")
    builder = _resolve_builder(effective_target)
    if not builder:
        chosen_subskill = SUBSKILLS[base_seed % len(SUBSKILLS)]
        builder = BUILDERS[chosen_subskill]

    q = builder(r)
    q["seed"] = base_seed
    q["difficulty"] = difficulty
    return q


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "12",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Grade 12 Physical Sciences Vertical Projectile Motion."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = (
        subskill
        if (subskill and subskill not in ("concepts", "default", "mixed", "all"))
        else (kwargs.get("archetype") or mode)
    )

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, count)):
        sub_seed = base_seed + i * 37
        r = random.Random(sub_seed)
        builder = _resolve_builder(effective_target)
        if not builder:
            chosen_subskill = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
            builder = BUILDERS[chosen_subskill]

        q = builder(r)
        q["seed"] = sub_seed
        q["difficulty"] = difficulty
        q["grade"] = str(grade)
        q["mode"] = mode
        questions.append(q)

    return questions
