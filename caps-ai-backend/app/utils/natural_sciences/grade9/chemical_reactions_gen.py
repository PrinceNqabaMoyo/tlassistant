"""Grade 9 Natural Sciences: Term 2 - Chemical Reactions Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Chemical reactions.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .chemical_reactions_archetypes_01_25 import BUILDERS_01_25
from .chemical_reactions_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Chemical reactions.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)

# Add integer 1..50 and 2-digit string "01".."50" keys
for idx, key in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[idx] = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[key]

# Legacy backward compatibility aliases
if "19_law_of_conservation_of_atoms_principle" in ARCHETYPE_BUILDERS:
    DISPATCH_TABLE["law_of_conservation_of_atoms"] = ARCHETYPE_BUILDERS["19_law_of_conservation_of_atoms_principle"]
    DISPATCH_TABLE["balancing_synthesis_reactions"] = ARCHETYPE_BUILDERS["27_balancing_synthesis_hydrogen_and_oxygen_to_water"]
    DISPATCH_TABLE["subscripts_vs_coefficients"] = ARCHETYPE_BUILDERS["17_subscripts_indicate_atoms_per_molecule_immutable"]
    DISPATCH_TABLE["macroscopic_reaction_evidence"] = ARCHETYPE_BUILDERS["03_macroscopic_evidence_of_reaction_gas_precipitate_color_temp"]
    DISPATCH_TABLE["particle_reaction_modeling"] = ARCHETYPE_BUILDERS["09_particle_model_diagram_rearrangement_of_atoms"]


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 9 Natural Sciences: Chemical Reactions Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    Returns a list of question dicts adhering to the 6-pillar contract.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None

        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            try:
                idx = int(archetype_index)
                if idx in DISPATCH_TABLE:
                    builder = DISPATCH_TABLE[idx]
                elif 1 <= idx <= len(SUBSKILLS):
                    builder = ARCHETYPE_BUILDERS[SUBSKILLS[idx - 1]]
            except (ValueError, TypeError):
                pass

        if builder is None:
            chosen = rng.choice(SUBSKILLS)
            builder = ARCHETYPE_BUILDERS[chosen]

        q = builder(rng)
        q.setdefault("grade", 9)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("topic", "Chemical reactions")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
