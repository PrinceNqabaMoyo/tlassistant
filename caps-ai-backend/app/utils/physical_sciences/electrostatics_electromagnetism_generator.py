"""Physical Sciences (Grades 10 & 11) — Electrostatics & Electromagnetism Generator.

Aggregates 50 distinct semantic archetypes across:
- Subskills 01–25: Electrostatics (Triboelectric charging, charge conservation for 2 and 3 spheres,
  charge quantization Q = n*e, electron mass transfer, gold-leaf electroscope induction,
  insulator polarisation, Coulomb's Law direct & inverse problems, 1D collinear multi-charge forces,
  zero-force equilibrium, 2D right-angled multi-charge forces, suspended pith ball equilibrium,
  electric fields E = F/q and E = kQ/r^2, field line patterns, neutral point, parallel plates, Millikan oil drop).
- Subskills 26–50: Electromagnetism & Synthesis (Magnetic field around straight wire, circular loop,
  and solenoid, Right-Hand Rules, magnetic flux Phi = B*A*cos(theta) for perpendicular, angled,
  circular, and rectangular coils, Faraday's Law of Electromagnetic Induction for varying B, varying A,
  180-deg and 90-deg rotations, induced current and total charge flow, Lenz's Law for approaching/receding
  magnets and planar loops, motional emf = BLv, magnetic braking drag, Lorentz force on moving charges
  and current-carrying wires, AC vs DC generators, ideal transformers, synthesis rider, diagnostic autopsy).

Strictly complies with the 6-Pillar Generator Contract (100% deterministic, zero-LLM).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .electrostatics_electromagnetism_archetypes_01_25 import (
    BUILDERS_01_25,
    E_CHARGE,
    K_COULOMB,
    _fmt_sa,
)
from .electrostatics_electromagnetism_archetypes_26_50 import BUILDERS_26_50

TOPIC = "physical_sciences_electrostatics"
LO = "ps_electrostatics_and_electromagnetism"

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())
ARCHETYPES: List[str] = list(BUILDERS.keys())

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "49_electrostatics_and_electromagnetism_synthesis_rider",
    "electrostatics_gr10": "02_principle_of_charge_conservation_two_spheres",
    "elementary_charge_conservation": "02_principle_of_charge_conservation_two_spheres",
    "coulomb_law": "08_coulombs_law_two_point_charges_direct",
    "elementary_coulomb_force": "08_coulombs_law_two_point_charges_direct",
    "elementary_coulombs_law": "08_coulombs_law_two_point_charges_direct",
    "electromagnetism": "34_faradays_law_change_in_magnetic_field",
    "elementary_faradays_law": "34_faradays_law_change_in_magnetic_field",
}


def _resolve_builder(target: Optional[str]) -> Optional[Callable[[random.Random], Dict[str, Any]]]:
    if not target or target in ("mixed", "all", "default"):
        return None
    if target in BUILDERS:
        return BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target]]
    t_low = target.lower()
    for k, b in BUILDERS.items():
        if t_low in k.lower():
            return b
    return None


def _normalize_question_payload(q: Dict[str, Any], seed_val: Optional[int], difficulty: str, mode: str) -> Dict[str, Any]:
    prompt_str = q.get("prompt") or q.get("question") or ""
    ans_str = q.get("answer_latex") or q.get("correct_answer") or q.get("sample_answer") or ""
    q.setdefault("question", prompt_str)
    q.setdefault("question_text", prompt_str)
    q.setdefault("prompt", prompt_str)
    q.setdefault("prompt_latex", prompt_str)
    q.setdefault("correct_answer", ans_str)
    q.setdefault("sample_answer", ans_str)
    q.setdefault("answer_latex", ans_str)
    q.setdefault("worked_solution", ans_str)
    q.setdefault("explanation", ans_str)
    q.setdefault("question_type", "short_answer")
    q.setdefault("difficulty", difficulty)
    q.setdefault("mode", mode or "compound")
    if seed_val is not None:
        q["seed"] = seed_val
    return q


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single deterministic 6-pillar question for Electrostatics or Electromagnetism."""
    r = random.Random(seed) if seed is not None else random.Random(42)
    effective_target = subskill or kwargs.get("archetype") or kwargs.get("mode")
    builder = _resolve_builder(effective_target)
    if not builder:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = BUILDERS[chosen_subskill]

    q = builder(r)
    return _normalize_question_payload(q, seed, difficulty, kwargs.get("mode", "compound"))


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Physical Sciences Electrostatics & Electromagnetism."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = subskill or kwargs.get("archetype") or (mode if mode != "compound" else None)
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        item_seed = base_seed if count == 1 else (base_seed * 1000 + i)
        sub_r = random.Random(item_seed)

        if effective_target in ("ac_dc_generator_motor_apparatus", "ac_generator", "dc_motor", "electrodynamics"):
            from app.utils.physical_sciences.physical_sciences_builders import (
                build_ac_dc_generator_motor_apparatus_question,
            )
            q = build_ac_dc_generator_motor_apparatus_question(seed=item_seed, grade=12, mode=mode)
        else:
            builder = _resolve_builder(effective_target)
            if not builder:
                chosen_subskill = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
                builder = BUILDERS[chosen_subskill]
            q = builder(sub_r)
            q = _normalize_question_payload(q, item_seed, difficulty, mode)

        questions.append(q)

    return questions
