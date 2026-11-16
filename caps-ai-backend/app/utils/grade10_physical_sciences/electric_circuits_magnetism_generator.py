"""Grade 10 Physical Sciences — Electric Circuits & Magnetism (50 Semantic Archetypes).
Grounded strictly in curriculum_docs_auto/PhysicalSciences_Gr10/Term 2/:
- 04. Magnetism.md: Magnetic fields, poles, field lines, Earth's magnetic field, compass directions, ferromagnetic domains.
- 05. Electrostatics.md: Triboelectric charging, conservation of charge (Q_new = (Q1+Q2)/2), charge quantisation (Q = n*e, e = 1,6 x 10^-19 C), electron transfer direction & mass.
- 06. Electric circuits.md: Circuit symbols, conventional current vs electron drift, current I = Q/Delta t, potential difference V = W/Q, EMF vs terminal potential difference, voltmeter & ammeter placement, cells in series and parallel, resistance R = V/I, factors affecting resistance, ohmic vs non-ohmic conductors, series & parallel resistor networks, combination circuits, switch dynamics, short circuits, electrical energy & power, electricity cost calculations, and comprehensive diagnostic autopsy.

100% Aligned with South African National Curriculum Standards.
Complies strictly with 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.grade10_physical_sciences.electric_circuits_magnetism_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade10_physical_sciences.electric_circuits_magnetism_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "Electric circuits"
SUBJECT = "Physical Sciences"
GRADE = "10"

ALL_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ALL_BUILDERS.keys())
ARCHETYPES: List[str] = SUBSKILLS
VALID_SUBSKILLS: List[str] = SUBSKILLS
BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = ALL_BUILDERS

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "44_series_parallel_multimeter_readings_calculation",
    "elementary_charge": "08_charge_conservation_two_identical_spheres",
    "elementary_circuit": "30_calculating_unknown_resistor_from_V_and_I",
    "electrostatics": "08_charge_conservation_two_identical_spheres",
    "charge_conservation": "08_charge_conservation_two_identical_spheres",
    "charge_quantisation": "10_charge_quantization_number_of_electrons",
    "magnetism": "01_magnetic_poles_attraction_repulsion",
    "magnetic_field": "02_magnetic_field_lines_and_direction",
    "current": "15_electric_current_definition_I_Q_t",
    "potential_difference": "19_potential_difference_definition_V_W_Q",
    "emf": "20_electromotive_force_emf_open_circuit",
    "resistance": "26_resistance_definition_ratio_V_I",
    "series": "31_series_equivalent_resistance_two_resistors",
    "parallel": "38_parallel_equivalent_resistance_two_different",
    "series_parallel": "43_series_parallel_network_resistor_in_series_with_parallel_pair",
    "energy_power": "48_electrical_energy_transfer_E_V_I_t",
    "cost": "49_electrical_power_and_cost_of_electricity",
    "diagnostic": "50_comprehensive_grade10_electric_circuits_synthesis",
}


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


# --------------------------------------------------------------------------- #
# Legacy Drill Builders (Preserved for 100% Backward Compatibility)
# --------------------------------------------------------------------------- #
E_CHARGE = 1.6e-19


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{{,}}")


def _build_charge_drill(r: random.Random) -> Dict[str, Any]:
    return ALL_BUILDERS["08_charge_conservation_two_identical_spheres"](r)


def _build_circuit_drill(r: random.Random) -> Dict[str, Any]:
    return ALL_BUILDERS["34_series_circuit_potential_division"](r)


# --------------------------------------------------------------------------- #
# Master Generator Function
# --------------------------------------------------------------------------- #
def generate(
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    grade: str = "10",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master 6-pillar question generator for Grade 10 Physical Sciences: Electric Circuits & Magnetism."""
    base_seed = int(seed) if seed is not None else random.randint(1, 1_000_000_000)
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, int(count))):
        cur_seed = base_seed * 1000 + i if seed is not None else None
        rng = _rng(cur_seed)

        resolved = subskill or mode
        if resolved and str(resolved).startswith("elementary_") and str(resolved)[11:] in ALL_BUILDERS:
            resolved = str(resolved)[11:]

        if resolved in LEGACY_ALIASES:
            resolved = LEGACY_ALIASES[resolved]

        if not resolved or resolved in ("mixed", "all", "default", "compound"):
            resolved = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
        elif resolved not in ALL_BUILDERS:
            matches = [s for s in SUBSKILLS if resolved in s]
            resolved = matches[0] if matches else SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]

        builder = ALL_BUILDERS[resolved]
        q = builder(rng, difficulty=difficulty or "medium")
        if cur_seed is not None:
            q["seed"] = cur_seed
            q["id"] = f"phys10_circ_{resolved}_{cur_seed}"
            q["question_id"] = q["id"]
        questions.append(q)

    return questions


generate_question = generate
