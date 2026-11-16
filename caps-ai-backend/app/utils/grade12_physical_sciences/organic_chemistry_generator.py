"""Grade 12 Physical Sciences — Organic Molecules (Deterministic 6-Pillar Generator).
100% aligned with South African National Curriculum Standards (Grade 12 Chemistry Paper 2: Term 1).
Grounded strictly in:
  curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/04. Organic molecules.md

Complies with the 6-Pillar Generator Contract:
  1. Metadata: term=1, caps_weight_percent=25, suggested_duration_mins=9.
  2. 50 Distinct Semantic Subskill Archetypes (0 generic shims).
  3. Standardized Misconceptions.
  4. Teacher-Editable Marking Schema.
  5. Deterministic 3-Tier Pre-Baked Hints.
  6. South African comma decimal convention (",").

Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints, marking schemas, and inline SVG specs.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

try:
    from app.utils.grade12_physical_sciences.organic_chemistry_archetypes_01_25 import (
        BUILDERS_01_25,
    )
    from app.utils.grade12_physical_sciences.organic_chemistry_archetypes_26_50 import (
        BUILDERS_26_50,
    )
except ImportError:
    from .organic_chemistry_archetypes_01_25 import BUILDERS_01_25
    from .organic_chemistry_archetypes_26_50 import BUILDERS_26_50

TOPIC = "Organic molecules"
TOPIC_KEY = "grade12_physical_sciences_organic_chemistry"

# Combined roster of all 50 semantic builders
BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = BUILDERS
ARCHETYPES: Dict[str, Callable[[random.Random], Dict[str, Any]]] = BUILDERS

# List of all 50 semantic subskill IDs
SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

# Legacy alias mappings to ensure backward compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_organic_chemistry_diagnostic_autopsy_and_structural_analysis",
    "elementary_iupac": "05_alkanes_branched_chain_iupac_naming",
    "elementary_isomers": "20_chain_isomers_alkanes_and_alkenes",
    "elementary_physical_properties": "27_boiling_point_comparison_homologous_series_chain_length",
    "elementary_reactions": "35_addition_reactions_hydrogenation_of_alkenes",
    "iupac": "05_alkanes_branched_chain_iupac_naming",
    "isomers": "20_chain_isomers_alkanes_and_alkenes",
    "phys_prop": "27_boiling_point_comparison_homologous_series_chain_length",
    "physical_properties": "27_boiling_point_comparison_homologous_series_chain_length",
    "reactions": "35_addition_reactions_hydrogenation_of_alkenes",
    "addition": "35_addition_reactions_hydrogenation_of_alkenes",
    "substitution": "42_substitution_reactions_halogenation_of_alkanes_uv_light",
    "elimination": "39_elimination_reactions_dehydrohalogenation_zaitsev_rule",
    "esterification": "45_esterification_condensation_reaction_mechanism_and_conditions",
    "polymers": "47_plastics_and_polymers_addition_polymerisation_polyethene",
    "cracking": "41_elimination_reactions_thermal_and_catalytic_cracking",
    "combustion": "34_combustion_reactions_complete_oxidation_alkanes",
    "intermolecular_forces": "26_intermolecular_forces_london_dipole_hydrogen_in_organics",
    "boiling_point": "27_boiling_point_comparison_homologous_series_chain_length",
    "vapour_pressure": "30_vapour_pressure_inversely_proportional_to_imf_strength",
    "functional_isomers": "23_functional_isomers_carboxylic_acids_and_esters",
    "positional_isomers": "21_positional_isomers_alkenes_and_haloalkanes",
    "chain_isomers": "20_chain_isomers_alkanes_and_alkenes",
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills supported by this generator."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 12 Organic Molecules question."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    rng = random.Random(base_seed)

    target = subskill or (mode if mode and mode in LEGACY_ALIASES else None)
    if target and target not in ("mixed", "all", ""):
        resolved = LEGACY_ALIASES.get(target, target)
        builder = BUILDERS.get(resolved)
        if not builder:
            matches = [s for s in ORDERED_SUBSKILLS if target.lower() in s.lower()]
            builder = BUILDERS[matches[0]] if matches else BUILDERS[ORDERED_SUBSKILLS[0]]
    else:
        chosen = rng.choice(ORDERED_SUBSKILLS)
        builder = BUILDERS[chosen]

    q = builder(rng)
    if seed is not None:
        q["seed"] = seed
    if "question" not in q and "prompt" in q:
        q["question"] = q["prompt"]
    if "question_text" not in q and "prompt" in q:
        q["question_text"] = q["prompt"]
    if "prompt" not in q and "question" in q:
        q["prompt"] = q["question"]
    if "correct_answer" not in q and "sample_answer" in q:
        q["correct_answer"] = q["sample_answer"]
    if "sample_answer" not in q and "correct_answer" in q:
        q["sample_answer"] = q["correct_answer"]
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    grade: str = "12",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Physical Sciences Organic Molecules questions."""
    base_seed = seed if seed is not None else random.randint(1, 1_000_000)
    questions: List[Dict[str, Any]] = []

    target_sub = subskill
    if target_sub in LEGACY_ALIASES:
        target_sub = LEGACY_ALIASES[target_sub]
    elif mode in LEGACY_ALIASES:
        target_sub = LEGACY_ALIASES[mode]

    for i in range(max(1, count)):
        curr_seed = base_seed + (i * 47)
        if target_sub and target_sub not in ("mixed", "all", ""):
            q = generate_question(subskill=target_sub, seed=curr_seed, difficulty=difficulty, mode=mode, **kwargs)
        else:
            sub = ORDERED_SUBSKILLS[(base_seed + i) % len(ORDERED_SUBSKILLS)]
            q = generate_question(subskill=sub, seed=curr_seed, difficulty=difficulty, mode=mode, **kwargs)
        questions.append(q)

    return questions
