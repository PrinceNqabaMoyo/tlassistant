"""Grade 11 Physical Sciences — Electric Circuits & Electrical Energy Generator (50-Archetype Generator).
100% aligned with South African National Curriculum Standards (Grade 11 Physics Paper 1: Term 3 Electric Circuits).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/01. Electric circuits.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Syllabus.md

Exports 50 distinct semantic subskills (01_<name> .. 50_<name>) across two modular archetype files (< 2000 lines each):
- Potential difference (V = W/Q), electric current (I = Q/dt), electron quantization, meter placement
- Ohm's Law, ohmic vs non-ohmic conductors, I-V and V-I characteristic graphs
- EMF, terminal potential difference, lost volts, internal resistance (E = I(R + r))
- Series, parallel (2, 3, and 4 resistors), and composite series-parallel networks
- Electrical power (P = VI = I^2R = V^2/R), electrical work/energy (W = VIt), bulb brightness
- Household 230 V parallel circuits, fuse ratings, kilowatt-hours (kWh), electricity tariffs & cost audits

Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints, marking schemas, and inline SVG specs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade11_physical_sciences.electric_circuits_energy_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade11_physical_sciences.electric_circuits_energy_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "grade11_physical_sciences_electric_circuits"
LO = "phys11_electric_circuits_energy"

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
    "compound": "49_comprehensive_circuit_network_and_power_synthesis",
    "elementary_resistor_network": "21_series_parallel_full_circuit_analysis",
    "elementary_power_cost": "40_single_appliance_monthly_electricity_cost",
    "network": "21_series_parallel_full_circuit_analysis",
    "cost": "40_single_appliance_monthly_electricity_cost",
    "internal_resistance": "11_internal_resistance_single_load_calculation",
    "ohms_law": "05_ohms_law_statement_and_conditions",
    "power": "29_electrical_power_definition_and_vi",
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills."""
    return list(SUBSKILLS)


def _resolve_builder(target: Optional[str]):
    if not target or target in ("mixed", "all", "default", ""):
        return None
    if target in ARCHETYPE_BUILDERS:
        return ARCHETYPE_BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in ARCHETYPE_BUILDERS:
        return ARCHETYPE_BUILDERS[LEGACY_ALIASES[target]]
    t_low = target.lower()
    for k, b in ARCHETYPE_BUILDERS.items():
        if t_low in k.lower():
            return b
    return None


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic Grade 11 Physical Sciences Electric Circuits question."""
    base_seed = 42 if seed is None else int(seed)
    r = random.Random(base_seed)

    effective_target = subskill or kwargs.get("archetype") or (mode if mode and mode in LEGACY_ALIASES else None)
    builder = _resolve_builder(effective_target)
    if not builder:
        chosen = r.choice(ORDERED_SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[chosen]

    q = builder(base_seed)
    q["difficulty"] = difficulty or q.get("difficulty", "medium")
    q["seed"] = base_seed
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate a list of deterministic Grade 11 Physical Sciences Electric Circuits questions."""
    base_seed = 42 if seed is None else int(seed)
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
