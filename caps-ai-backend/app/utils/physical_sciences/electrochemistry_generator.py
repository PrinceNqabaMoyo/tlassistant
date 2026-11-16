"""Grade 11 Physical Sciences — Energy and Chemical Change (50-Archetype Generator Wrapper).
Grounded strictly in curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/02. Energy and chemical change.md.

Complies with the 6-pillar South African curriculum contract:
- 50 distinct semantic subskills (01_<name> .. 50_<name>), zero synthetic shims
- Modular splits: electrochemistry_archetypes_01_25.py & electrochemistry_archetypes_26_50.py (< 2000 lines each)
- Preserves Grade 9 / Grade 12 legacy dispatch when explicitly passed without a Grade 11 subskill
- Zero-LLM: 100% deterministic Python with South African comma decimals and inline SVGs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.physical_sciences.electrochemistry_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.physical_sciences.electrochemistry_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "physical_sciences_electrochemistry"
LO = "phys11_energy_chemical_change"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

BUILDERS: Dict[str, Any] = ARCHETYPE_BUILDERS
ARCHETYPES: Dict[str, Any] = ARCHETYPE_BUILDERS

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

LEGACY_ALIASES: Dict[str, str] = {
    "enthalpy": "01_chemical_system_and_enthalpy_definition",
    "exothermic": "05_exothermic_energy_balance_criteria",
    "endothermic": "06_endothermic_energy_balance_criteria",
    "activation_energy": "28_exothermic_potential_energy_profile_reading",
    "catalyst": "36_catalyst_effect_on_activation_energy",
    "bond_energy": "22_bond_energy_enthalpy_combustion_hydrocarbons",
    "compound": "50_energy_and_chemical_change_comprehensive_synthesis",
    "concepts": "01_chemical_system_and_enthalpy_definition",
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills for Grade 11 Energy and chemical change."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 11 Energy and chemical change question."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    rng = random.Random(base_seed)

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
    grade: str = "11",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Energy & Chemical Change (Grade 11) with legacy Gr9/Gr12 routing."""
    gr_str = str(grade).strip()
    is_gr11_sub = subskill in ARCHETYPE_BUILDERS or (subskill in LEGACY_ALIASES)

    if not is_gr11_sub:
        if gr_str == "9":
            from app.utils.natural_sciences.ns7_acids_bases_neutrals_generator import generate as ns_gen
            return ns_gen(subskill=subskill, difficulty=difficulty, count=count, grade="9", seed=seed, mode=mode, **kwargs)
        if gr_str == "12":
            from app.utils.physical_sciences.ps12_electrochemistry_galvanic_generator import generate as ps_gen
            return ps_gen(subskill=subskill, difficulty=difficulty, count=count, grade="12", seed=seed, mode=mode, **kwargs)

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
