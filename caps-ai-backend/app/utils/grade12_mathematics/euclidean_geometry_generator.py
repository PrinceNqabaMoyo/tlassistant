"""Grade 12 Mathematics — Euclidean Geometry 50-Archetype Generator Wrapper.
Complies with official South African curriculum standards:
- 50 semantic archetypes across proportionality, similarity, and circle riders
- Zero synthetic shims (01_<name> .. 50_<name>)
- 100% deterministic with seed variance across seeds [101, 102, 103]
- 6-pillar contract: term, caps_weight_percent, duration, hints, marking schema, misconception tags
- Inline SVG diagram specs with diagram_role='context'
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_mathematics.euclidean_geometry_archetypes_01_25 import BUILDERS_01_25
from app.utils.grade12_mathematics.euclidean_geometry_archetypes_26_50 import BUILDERS_26_50

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = ORDERED_SUBSKILLS

# Legacy / shorthand aliases for backwards compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "proportionality_theorem": "07_proportionality_theorem_single_parallel_side",
    "proportionality": "07_proportionality_theorem_single_parallel_side",
    "similarity": "28_similarity_finding_corresponding_side_lengths",
    "similar_triangles": "26_similarity_equiangular_definition_and_identification",
    "pythagoras_similarity": "36_pythagorean_proof_similarity_altitude_to_hypotenuse",
    "geometric_mean": "37_pythagorean_proof_geometric_mean_relations",
    "circle_similarity": "40_circle_similarity_subtended_angles_bowtie",
    "tangent_secant": "42_circle_similarity_tangent_secant_theorem",
    "compound": "50_euclidean_geometry_comprehensive_synthesis_rider",
    "rider": "50_euclidean_geometry_comprehensive_synthesis_rider",
}


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 12 Euclidean Geometry question dict."""
    rng = random.Random(seed)

    if subskill:
        # Check direct or alias
        target_subskill = LEGACY_ALIASES.get(subskill, subskill)
        builder = ARCHETYPE_BUILDERS.get(target_subskill)
        if not builder:
            # Substring fallback
            matches = [s for s in ORDERED_SUBSKILLS if subskill.lower() in s.lower()]
            if matches:
                builder = ARCHETYPE_BUILDERS[matches[0]]
            else:
                builder = ARCHETYPE_BUILDERS[ORDERED_SUBSKILLS[0]]
    else:
        # Pick uniformly or via seed
        target_subskill = rng.choice(ORDERED_SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[target_subskill]

    return builder(rng)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates a list of count Grade 12 Euclidean Geometry question dicts."""
    base_seed = seed if seed is not None else random.randint(1, 1000000)
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        item_seed = base_seed + (i * 37)
        if subskill:
            q = generate_question(subskill=subskill, seed=item_seed, **kwargs)
        else:
            sub = ORDERED_SUBSKILLS[i % len(ORDERED_SUBSKILLS)]
            q = generate_question(subskill=sub, seed=item_seed, **kwargs)
        questions.append(q)

    return questions
