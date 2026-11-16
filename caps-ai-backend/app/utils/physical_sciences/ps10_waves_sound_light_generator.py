"""Physical Sciences Grade 10 — Waves, Sound & Light Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/07. Transverse pulses.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/08. Transverse waves.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/09. Longitudinal waves.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/10. Sound.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/11. Electromagnetic radiation.md

Registered Topics in caps_term_registry_data.json:
1. Transverse pulses (Grade 10 Term 1)
2. Transverse waves (Grade 10 Term 1)
3. Longitudinal waves (Grade 10 Term 1)
4. Sound (Grade 10 Term 1)
5. Electromagnetic radiation (Grade 10 Term 1)

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1, caps_weight_percent=15, suggested_duration_mins=4.
2. 50 Distinct Semantic Subskills (01..50), 0 synthetic shims.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention ("," / "{,}").
"""

from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.physical_sciences.ps10_waves_sound_light_archetypes_01_25 import BUILDERS_01_25
from app.utils.physical_sciences.ps10_waves_sound_light_archetypes_26_50 import BUILDERS_26_50

TOPIC = "grade10_waves_sound_light"
LO = "PS10.WSL"

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
    "compound": "50_waves_sound_light_diagnostic_synthesis",
    "concepts": "01_transverse_pulse_definition_and_medium",
    "scaffold": "12_crest_trough_and_amplitude_from_wave_graph",
    "transverse_wave_diagram": "12_crest_trough_and_amplitude_from_wave_graph",
    "elementary_wave_speed": "19_wave_equation_speed_frequency_wavelength",
    "elementary_sound_echo": "37_echo_distance_and_reflection_time",
    "elementary_photon_energy": "48_photon_energy_calculation_from_frequency",
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
    """Generate a single deterministic 6-pillar question for Grade 10 Waves, Sound & Light."""
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
    grade: str = "10",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Grade 10 Physical Sciences Waves, Sound & Light."""
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
