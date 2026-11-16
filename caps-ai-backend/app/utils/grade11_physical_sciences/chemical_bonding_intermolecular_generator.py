"""Grade 11 Physical Sciences — Chemical Bonding, Intermolecular Forces & The Lithosphere (50-Archetype Generator).
100% aligned with South African National Curriculum Standards (Grade 11 Chemistry Paper 2: Matter & Materials, Chemical Systems).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/02. Atomic combinations.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/03. Intermolecular forces.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 4/01. The lithosphere.md

Exports 50 distinct semantic subskills (01_<name> .. 50_<name>) across two modular archetype files (< 2000 lines each).
Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints, marking schemas, and inline SVG specs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_physical_sciences.chemical_bonding_intermolecular_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade11_physical_sciences.chemical_bonding_intermolecular_archetypes_26_50 import (
    BUILDERS_26_50,
)

try:
    from app.utils.physical_sciences.physical_sciences_builders import build_chemical_bonding_molecules_question
except ImportError:
    from ..physical_sciences.physical_sciences_builders import build_chemical_bonding_molecules_question

TOPIC = "grade11_physical_sciences_chemistry"
LO = "phys11_chemical_bonding_imf"

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
    "vsepr": "09_vsepr_shapes_with_lone_pairs_distortion",
    "imf": "26_boiling_point_comparison_hydrides_anomaly",
    "compound": "50_grade11_chemistry_comprehensive_synthesis",
    "atomic_combinations": "25_atomic_combinations_vsepr_polarity_synthesis",
    "intermolecular_forces": "26_boiling_point_comparison_hydrides_anomaly",
    "lithosphere": "42_gold_mining_cyanidation_process_flowchart",
    "lewis": "04_lewis_dot_diagrams_single_covalent_bonds",
    "electronegativity": "12_bond_polarity_spectrum_classification",
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
    """Generate a single deterministic Grade 11 Physical Sciences Chemistry question."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    rng = random.Random(base_seed)

    if subskill in ("diagram", "chemical_bonding_molecules", "molecular_geometry"):
        return build_chemical_bonding_molecules_question(base_seed, grade=11)

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
    """Generate a list of deterministic Grade 11 Physical Sciences Chemistry questions."""
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
