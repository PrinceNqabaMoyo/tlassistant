"""Grade 10 Physical Sciences — Matter & Materials Master Generator.
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/02. Classification of matter.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/04. The atom.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/05. The periodic table.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/06. Chemical bonding.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 2/01. The particles that substances are made of.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 4/01. The hydrosphere.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 4/02. Units of measurement applied.md

Complies strictly with 6-Pillar Generator Contract:
1. Metadata: term=1, 2, 4, caps_weight_percent, suggested_duration_mins.
2. 50 distinct semantic subskills (0 synthetic shims).
3. Standardized Misconceptions tags.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade10_physical_sciences.matter_materials_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade10_physical_sciences.matter_materials_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "Classification of matter"

# 50 Semantic Archetypes
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
ALL_BUILDERS: Dict[str, Any] = {
    **BUILDERS,
}

# Legacy fallback builders for backward compatibility
def _legacy_compound(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    sub = r.choice([
        "01_classify_substance_element_compound_mixture",
        "07_atomic_number_mass_number_subatomic_particles",
        "12_sp_electron_configuration_notation_elements_1_to_20",
        "28_covalent_bonding_polyatomic_molecules_water_ammonia_methane",
        "39_percentage_composition_by_mass_calculation",
        "43_concentration_of_solutions_standard_volumetric_prep",
    ])
    return ARCHETYPES[sub](r)


def _legacy_mole(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["43_concentration_of_solutions_standard_volumetric_prep"](r)


def _legacy_isotopes(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["09_relative_atomic_mass_from_isotopic_abundance"](r)


def _legacy_bohr(r: random.Random, **kwargs: Any) -> Dict[str, Any]:
    return ARCHETYPES["11_bohr_model_energy_levels_quantum_shells"](r)


LEGACY_BUILDERS: Dict[str, Any] = {
    "compound": _legacy_compound,
    "mole": _legacy_mole,
    "concentration": _legacy_mole,
    "stoichiometry": _legacy_mole,
    "isotopes": _legacy_isotopes,
    "atomic_structure": _legacy_isotopes,
    "periodic_table": lambda r, **kw: ARCHETYPES["16_periodic_table_periods_groups_and_blocks"](r),
    "bohr_diagram": _legacy_bohr,
    "atomic_bohr_structure": _legacy_bohr,
    "bonding": lambda r, **kw: ARCHETYPES["29_ionic_bonding_electron_transfer_and_ion_formation"](r),
    "covalent": lambda r, **kw: ARCHETYPES["27_covalent_bonding_electron_sharing_diatomic_molecules_svg"](r),
    "ionic": lambda r, **kw: ARCHETYPES["30_ionic_crystal_lattice_structure_and_properties_svg"](r),
    "metallic": lambda r, **kw: ARCHETYPES["31_metallic_bonding_sea_of_delocalised_electrons_svg"](r),
    "empirical_formula": lambda r, **kw: ARCHETYPES["40_empirical_formula_from_percentage_composition"](r),
    "hydrosphere": lambda r, **kw: ARCHETYPES["44_hydrosphere_water_cycle_reservoirs_and_phase_changes_svg"](r),
    "elementary_mole_calculation": _legacy_mole,
    "elementary_solution_concentration": _legacy_mole,
    "elementary_isotope_abundance": _legacy_isotopes,
    "elementary_electron_config": lambda r, **kw: ARCHETYPES["12_sp_electron_configuration_notation_elements_1_to_20"](r),
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills."""
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
    grade: str = "10",
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

# diagram_role: context (declarative physical sciences context visualization)
