"""Grade 12 Physical Sciences — Optical Phenomena & Properties of Matter Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 3/03. Optical phenomena and properties of matter.md

Registered Topics in caps_term_registry_data.json:
1. Optical phenomena and properties of matter (Grade 12 Term 3)

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=3, caps_weight_percent=15, suggested_duration_mins=5.
2. 50 Distinct Semantic Subskills (01..50), 0 synthetic shims.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Pre-Baked Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade12_physical_sciences.optical_phenomena_photoelectric_archetypes_01_25 import (
    BUILDERS_01_25,
    SUBSKILLS_01_25,
)
from app.utils.grade12_physical_sciences.optical_phenomena_photoelectric_archetypes_26_50 import (
    BUILDERS_26_50,
    SUBSKILLS_26_50,
)

TOPIC = "grade12_optical_phenomena"
LO = "PS12.OPP"

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
    "compound": "50_photoelectric_and_spectra_diagnostic_synthesis",
    "concepts": "01_photoelectric_effect_definition_and_significance",
    "scaffold": "03_photon_energy_from_frequency",
    "work_function": "06_work_function_definition",
    "threshold_frequency": "07_threshold_frequency_calculation",
    "photoelectric_equation": "11_photoelectric_equation_maximum_kinetic_energy",
    "photoelectron_speed": "13_maximum_speed_of_photoelectrons",
    "stopping_potential": "22_stopping_potential_calculation_from_kinetic_energy",
    "photocell": "24_photocell_retarding_circuit_diagram",
    "kmax_graph": "33_kinetic_energy_vs_frequency_graph_planck_gradient",
    "spectra": "38_line_emission_spectrum_definition_and_origin",
    "bohr_transitions": "43_bohr_energy_level_transition_photon_emission",
    "skills_for_science": "49_skills_for_science_plancks_constant_uncertainty",
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
    """Generate a single deterministic 6-pillar question for Grade 12 Optical Phenomena."""
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
    """Master generation endpoint for Grade 12 Physical Sciences Optical Phenomena."""
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
