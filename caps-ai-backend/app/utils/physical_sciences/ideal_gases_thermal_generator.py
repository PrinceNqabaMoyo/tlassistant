"""Grade 11 Physical Sciences — Term 1 Chapter 7: Ideal Gases & Thermal Physics Generator
50-Archetype Modular Aggregator (`physical_sciences_ideal_gases_thermal`).

Strictly complies with the 6-Pillar Generator Contract:
- 50 distinct semantic subskills (`01_kinetic_molecular_theory_assumptions` .. `50_ideal_gas_thermal_capstone_synthesis`)
- Procedural determinism via `random.Random(seed)`
- South African comma decimal convention (`{,}`)
- Valid inline vector SVGs in `diagram_spec`
- Zero LLM calls (100% AST Purity)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.physical_sciences.ideal_gases_thermal_archetypes_01_25 import BUILDERS_01_25
from app.utils.physical_sciences.ideal_gases_thermal_archetypes_26_50 import BUILDERS_26_50

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

BUILDERS = ARCHETYPE_BUILDERS
SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())

LEGACY_ALIASES: Dict[str, str] = {
    "kinetic_theory": "01_kinetic_molecular_theory_assumptions",
    "states_of_matter": "02_gas_pressure_microscopic_interpretation",
    "elementary_celsius_to_kelvin": "03_temperature_kelvin_conversion",
    "elementary_boyle_law": "07_boyles_law_calculate_volume",
    "boyle_law": "07_boyles_law_calculate_volume",
    "charles_law": "14_charles_law_calculate_volume",
    "gay_lussac_law": "20_gay_lussacs_law_calculate_pressure",
    "general_gas_equation": "27_general_gas_equation_solve_v2",
    "ideal_gas_equation": "33_ideal_gas_law_solve_pressure",
    "real_gas_deviations": "46_ideal_vs_real_gas_definitions_comparison",
}


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()

    if subskill in ("particle_diagram", "particle_model"):
        from app.utils.natural_sciences.natural_sciences_builders import build_particle_model_question
        grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "10"
        gr_int = int(grade_num) if grade_num in ("8", "10") else 10
        s_val = seed if seed is not None else rng.randint(1, 1_000_000)
        return build_particle_model_question(s_val, grade=gr_int, mode=mode)

    if mode in LEGACY_ALIASES and (not subskill or subskill in ("mixed", "all")):
        resolved_sub = LEGACY_ALIASES[mode]
    elif subskill and subskill in ARCHETYPE_BUILDERS:
        resolved_sub = subskill
    elif subskill and subskill in LEGACY_ALIASES:
        resolved_sub = LEGACY_ALIASES[subskill]
    else:
        resolved_sub = rng.choice(SUBSKILLS)

    builder = ARCHETYPE_BUILDERS[resolved_sub]
    q = builder(rng)
    q["subskill"] = resolved_sub
    if mode and mode != "compound":
        q["mode"] = mode
    return q


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator entry point for Physical Sciences Grade 11 Ideal Gases."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        item_seed = (seed + i * 1009) if seed is not None else rng.randint(1, 1_000_000_000)
        if subskill and subskill not in ("mixed", "all"):
            chosen_sub = subskill
        else:
            chosen_sub = SUBSKILLS[(i + (seed or 0)) % len(SUBSKILLS)]

        q = generate_question(subskill=chosen_sub, seed=item_seed, mode=mode, grade=grade, **kwargs)
        questions.append(q)

    return questions
