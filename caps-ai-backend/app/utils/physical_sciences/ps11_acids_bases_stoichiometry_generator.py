"""Physical Sciences Grade 11 & 12 — Acids, Bases, Titrations & Stoichiometry Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/03. Types of reaction.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/04. Quantitative aspects of chemical change.md
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/03. Acids and bases.md

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=3 (Gr 11), caps_weight_percent=20, suggested_duration_mins=8.
2. Deconstructible compound questions & atomic sub-drills across 50 semantic archetypes.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.physical_sciences.ps11_acids_bases_stoichiometry_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.physical_sciences.ps11_acids_bases_stoichiometry_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "grade11_physical_sciences_acids_bases_stoichiometry"

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_ALIASES: Dict[str, str] = {
    "concepts": "01_arrhenius_acid_base_definitions",
    "titration_apparatus_diagram": "11_titration_apparatus_identification",
    "titration_apparatus": "11_titration_apparatus_identification",
    "elementary_titration_stoichiometry": "16_titration_volumetric_calculation_monoprotic",
    "titration_calc": "17_titration_volumetric_calculation_diprotic",
    "moles_mass": "26_mole_and_avogadro_constant",
    "molar_mass": "27_molar_mass_compound_calculations",
    "gas_volume": "28_molar_gas_volume_stp_calculations",
    "concentration": "29_molar_concentration_calculations",
    "dilution": "30_solution_dilution_calculations",
    "empirical_formula": "32_empirical_formula_from_percentage",
    "molecular_formula": "34_molecular_formula_from_empirical",
    "limiting_reagent": "41_limiting_reagent_mole_identification",
    "percentage_yield": "45_percentage_yield_calculations",
    "purity": "46_percentage_purity_of_reactants",
    "back_titration": "48_back_titration_stoichiometry",
}


def get_subskills() -> List[str]:
    """Returns the ordered list of 50 semantic subskill identifiers."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single question dictionary from a specific subskill or random choice."""
    rng = random.Random(seed)
    chosen_sub = subskill or rng.choice(SUBSKILLS)
    actual_sub = LEGACY_ALIASES.get(chosen_sub, chosen_sub)
    builder = BUILDERS.get(actual_sub)

    if not builder:
        builder = BUILDERS[SUBSKILLS[0]]
        actual_sub = SUBSKILLS[0]

    q = builder(rng)
    # Ensure standard schema keys
    if "question" not in q:
        q["question"] = q.get("prompt", "")
    if "worked_solution" not in q:
        q["worked_solution"] = q.get("explanation") or q.get("sample_answer") or ""
    if "explanation" not in q:
        q["explanation"] = q["worked_solution"]
    if "correct_answer" not in q:
        q["correct_answer"] = q.get("sample_answer", "")

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
    """Master generation endpoint complying with CAPS Universal Generator Contract."""
    base_seed = seed if seed is not None else random.randint(1000, 999999)
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = base_seed + i * 37
        q = generate_question(subskill=subskill, seed=sub_seed, mode=mode, **kwargs)
        questions.append(q)

    return questions


# Topic-specific convenience aliases
generate_types_of_reaction = generate
generate_quantitative_chemical_change = generate
