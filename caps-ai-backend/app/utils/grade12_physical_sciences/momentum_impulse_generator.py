"""Grade 12 Physical Sciences — Momentum and Impulse Generator.
Deterministic 6-pillar generator aggregating 50 distinct semantic archetypes:
- 01–08: Definition & vector nature of momentum, p = mv calculations, unit conversions, p vs Ek relations.
- 09–13: Change in momentum (Delta p = m(vf - vi)), 1D speed increase, braking, rebounds, vertical bounce, vector diagrams.
- 14–20: Newton's Second Law in terms of momentum (F_net = Delta p / Delta t), impulse definition, J = F_net * Delta t = Delta p.
- 21–24: Force-time (F-t) graphs (rectangular, triangular, trapezoidal, direction reversal) with seed-varied inline SVGs.
- 25: Momentum & impulse foundations diagnostic autopsy.
- 26–27: Isolated systems, external forces, formal principle of conservation of linear momentum.
- 28–32: 1D collisions (stick together, head-on rebound, stationary target, shunting/rear-end).
- 33–34: Elastic vs inelastic collisions (kinetic energy test: sum Ek_i vs sum Ek_f, mechanical energy lost to heat/sound/deformation).
- 35–38: Explosions and separations (stationary recoil, rocket staging in flight, ballistic bullet embeds vs passes through).
- 39–40: Ballistic pendulum and spring-loaded glider release with seed-varied inline SVGs.
- 41–44: Physics in action & safety (crumple zones, airbags, seatbelts, arrestor beds, sports follow-through & catching).
- 45–48: Cascades, post-collision friction stopping distances, ramp conversions, Newton's 3rd Law internal force cancellation.
- 49–50: Comprehensive exam synthesis rider and post-exam diagnostic autopsy / misconception triage.

Satisfies 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_physical_sciences.momentum_impulse_archetypes_01_25 import BUILDERS_01_25
from app.utils.grade12_physical_sciences.momentum_impulse_archetypes_26_50 import ARCHETYPES_26_50

TOPIC = "grade12_physical_sciences_momentum"

BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **ARCHETYPES_26_50,
}

ARCHETYPES: Dict[str, Any] = BUILDERS
SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "49_capstone_momentum_and_impulse_exam_rider",
    "compound_collision": "28_conservation_of_momentum_trolleys_colliding_stick_together",
    "compound_impulse": "20_impulse_momentum_theorem_ball_struck_by_bat",
    "conservation_of_momentum": "28_conservation_of_momentum_trolleys_colliding_stick_together",
    "conservation_of_momentum_1d": "28_conservation_of_momentum_trolleys_colliding_stick_together",
    "collisions": "28_conservation_of_momentum_trolleys_colliding_stick_together",
    "1d_collisions": "28_conservation_of_momentum_trolleys_colliding_stick_together",
    "impulse": "18_impulse_definition_and_units_equivalence",
    "impulse_newton_second_law": "14_newtons_second_law_in_terms_of_momentum_statement",
    "newtons_second_law_momentum": "14_newtons_second_law_in_terms_of_momentum_statement",
    "elementary_momentum": "02_linear_momentum_direct_calculation",
    "elementary_change_momentum": "09_change_in_momentum_same_direction_speed_increase",
    "elementary_impulse": "19_impulse_from_constant_force_and_contact_time",
}


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def get_subskills() -> List[str]:
    """Return ordered list of all 50 semantic subskill identifiers."""
    return list(SUBSKILLS)


def _resolve_builder(target: Optional[str]):
    if not target or target in ("mixed", "all", "default"):
        return None
    if target in BUILDERS:
        return BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target]]
    t_low = str(target).lower()
    for k, b in BUILDERS.items():
        if t_low in k.lower():
            return b
    return None


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic 6-pillar question for Grade 12 Momentum and Impulse."""
    r = _rng(seed)
    target = subskill or kwargs.get("subskill_id") or kwargs.get("archetype") or kwargs.get("mode")
    builder = _resolve_builder(target)
    if not builder:
        chosen = r.choice(SUBSKILLS)
        builder = BUILDERS[chosen]
    q = builder(r)
    if seed is not None:
        q["seed"] = int(seed)
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Any:
    """Main generator entrypoint adhering to the 6-pillar contract."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = (
        subskill
        or kwargs.get("subskill_id")
        or kwargs.get("archetype")
        or (mode if mode != "compound" else None)
    )

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, count)):
        item_seed = base_seed if count == 1 else (base_seed * 1000 + i)
        r = _rng(item_seed)
        builder = _resolve_builder(effective_target)
        if not builder:
            chosen = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
            builder = BUILDERS[chosen]
        q = builder(r)
        q["seed"] = item_seed
        questions.append(q)

    # Return list of question dicts directly, or return first question in dict if count=1
    return questions
