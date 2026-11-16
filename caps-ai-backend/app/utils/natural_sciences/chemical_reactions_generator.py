"""Physical Sciences Grade 10 Term 3 — Reactions in Aqueous Solution.
Deterministic 6-Pillar Generator aggregating 50 semantic archetypes:
- Polarity of water and hydration
- Dissociation of 1:1, multivalent, and polyatomic salts
- Dissociation vs ionisation & covalent dissolution
- Electrolytes & electrical conductivity circuit interpretation
- Factors affecting conductivity (concentration, ion count/charge, weak vs strong electrolytes)
- Ion concentration calculations
- Precipitation reactions & solubility rules (halides, sulphates, carbonates, hydroxides)
- Spectator ions, full ionic and net ionic equations
- Qualitative tests for anions (Cl-, Br-, I-, SO4^2-, CO3^2-)
- Distinguishing tests and unknown salt identification protocol
- Ion exchange general form and driving forces
- Gas-forming reactions (carbonate, hydrogen carbonate, sulphite, sulphide)
- Acid-base neutralisation (Arrhenius & Brønsted-Lowry, proton transfer, net ionic equations, metal oxides, antacids)
- Redox reactions in aqueous solutions (electron transfer, oxidation numbers, oxidising/reducing agents)
- Displacement reactions (metal displacement, halogen displacement, metal-acid)
- Distinguishing ion exchange vs redox
- Stoichiometric calculations in aqueous solutions (precipitation mass, limiting reactant, antacid purity at STP)
- Aqueous reactions capstone synthesis
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import rng
from app.utils.natural_sciences.chemical_reactions_archetypes_01_25 import BUILDERS_01_25
from app.utils.natural_sciences.chemical_reactions_archetypes_26_50 import BUILDERS_26_50

TOPIC = "natural_sciences_chemical_reactions"
LO = "ps10_reactions_in_aqueous_solution"

# Aggregate all 50 distinct semantic archetype builders
BUILDERS = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS = list(BUILDERS.keys())
ARCHETYPES = list(BUILDERS.keys())

# Legacy alias mappings for backwards compatibility with earlier drills
LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_aqueous_reactions_capstone_synthesis",
    "chemical_reactions_compound": "50_aqueous_reactions_capstone_synthesis",
    "elementary_balancing_atoms": "03_dissociation_single_charge_salts",
    "balancing_equations_elementary": "03_dissociation_single_charge_salts",
    "elementary_ph_scale_identification": "34_acid_base_definitions_arrhenius_and_bronsted",
    "ph_scale_elementary": "34_acid_base_definitions_arrhenius_and_bronsted",
    "elementary_reactants_products_identification": "30_ion_exchange_reaction_general_form",
    "reactants_products_elementary": "30_ion_exchange_reaction_general_form",
}


def _resolve_builder(target: Optional[str]):
    if not target or target in ("mixed", "all", "default"):
        return None
    if target in BUILDERS:
        return BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target]]
    # Match by partial name or number prefix
    t_low = target.lower()
    for k, b in BUILDERS.items():
        if t_low in k.lower():
            return b
    return None


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single deterministic 6-pillar question for Reactions in Aqueous Solution."""
    r = rng(seed)
    builder = _resolve_builder(subskill) or _resolve_builder(kwargs.get("mode"))
    if not builder:
        # Pick subskill deterministically from seed
        chosen_subskill = r.choice(SUBSKILLS)
        builder = BUILDERS[chosen_subskill]

    q = builder(r, difficulty=difficulty)
    if seed is not None:
        q["seed"] = seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Public generator entrypoint returning a dictionary with a list of questions."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = subskill or kwargs.get("archetype") or mode

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, count)):
        item_seed = base_seed * 1000 + i
        r = rng(item_seed)
        builder = _resolve_builder(effective_target)
        if not builder:
            chosen_subskill = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
            builder = BUILDERS[chosen_subskill]

        q = builder(r, difficulty=difficulty)
        q["seed"] = item_seed
        questions.append(q)

    return {"questions": questions}
