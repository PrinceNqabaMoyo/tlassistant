"""Grade 12 Physical Sciences — Rate and Extent of Reaction, Chemical Equilibrium & The Chemical Industry.
100% aligned with South African National Curriculum Standards (CAPS Grade 12 Physical Sciences Paper 2 Chemistry).
Satisfies the 6-Pillar Generator Contract. Zero-LLM deterministic implementation.

Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/01. Rate and Extent of Reaction.md
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/02. Chemical equilibrium.md
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 3/05. The chemical industry.md

Maps to 3 CAPS Curriculum Topics:
1. Rate and Extent of Reaction (Grade 12 Term 2)
2. Chemical equilibrium (Grade 12 Term 2)
3. The chemical industry (Grade 12 Term 3)

Exports 50 distinct semantic subskills (01_<name> .. 50_<name>) across two modular archetype files (< 2000 lines each).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_physical_sciences.stoichiometry_equilibrium_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade12_physical_sciences.stoichiometry_equilibrium_archetypes_26_50 import (
    BUILDERS_26_50,
)

try:
    from app.utils.physical_sciences.physical_sciences_builders import (
        build_gas_evolution_rate_apparatus_question,
    )
except ImportError:
    from ..physical_sciences.physical_sciences_builders import (
        build_gas_evolution_rate_apparatus_question,
    )

TOPIC = "physical_sciences_chemistry_equilibrium"
LO = "phys12_rates_equilibrium_chemical_industry"

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
    "compound": "50_equilibrium_capstone_misconception_autopsy",
    "elementary_molar_mass_calc": "48_npk_fertilizer_ratio_and_percentage_calculations",
    "elementary_kc_expression": "26_equilibrium_constant_kc_expression_homogeneous",
    "reaction_energy_profile": "15_catalyzed_energy_profile_diagram",
    "gas_evolution_rate_apparatus": "08_measuring_rate_gas_syringe_apparatus",
    "rates": "01_reaction_rate_definition_and_units",
    "collision_theory": "02_collision_theory_criteria",
    "maxwell_boltzmann": "03_maxwell_boltzmann_temperature_shift",
    "equilibrium": "22_dynamic_chemical_equilibrium_definition",
    "le_chatelier": "34_le_chatelier_principle_statement",
    "ice_table": "41_ice_table_kc_calculation_moles_and_volume",
    "haber_process": "45_industrial_haber_process_compromise_conditions",
    "contact_process": "46_industrial_contact_process_conditions_and_oleum",
    "ostwald_process": "47_industrial_ostwald_process_nitric_acid",
    "fertilizer": "48_npk_fertilizer_ratio_and_percentage_calculations",
    "eutrophication": "49_eutrophication_environmental_impact",
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
    """Generate a single deterministic Grade 12 Chemistry Equilibrium question."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    rng = random.Random(base_seed)

    if subskill in ("rate_apparatus", "gas_evolution_rate_apparatus"):
        return build_gas_evolution_rate_apparatus_question(base_seed, grade=12)

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
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate a list of deterministic Grade 12 Chemistry Equilibrium questions."""
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
