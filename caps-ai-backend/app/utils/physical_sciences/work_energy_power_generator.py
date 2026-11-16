"""Physical Sciences (Grade 12 Term 1) — Work, Energy and Power Generator.

Aggregates 50 distinct semantic archetypes across:
- Subskills 01–25: Work Done & Work-Energy Theorem (Constant horizontal forces, forces at angles,
  zero-work perpendicular forces, negative friction work, gravity work in vertical drop and inclines,
  net work via sum of works and resultant force methods, F-x graph area integration,
  kinetic energy, and Work-Energy Theorem applications on horizontal surfaces, rough inclines,
  stopping distance scaling, bullet penetration, vertical hoists, and pendulums).
- Subskills 26–50: Non-Conservative Forces, Energy Conservation & Power (Conservative vs non-conservative
  forces, path dependence, W_nc = Delta E_k + Delta E_p theorem on rough inclines, falling with drag,
  roller coasters, ski jump, conservation of mechanical energy and vertical loop-the-loop,
  power definitions P = W/Delta t and P = F*v, accelerating vehicles, aerodynamic drag scaling P ~ v^3,
  climbing vehicles, borehole submersible pumps, hydroelectric pumped-storage, escalators,
  mechanical efficiency, kilowatt-hour tariffs, multi-stage riders, and diagnostic autopsy).

Strictly complies with the 6-Pillar Generator Contract (100% deterministic, zero-LLM).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .work_energy_power_archetypes_01_25 import (
    BUILDERS_01_25,
    G_ACCEL,
    _fmt_sa,
)
from .work_energy_power_archetypes_26_50 import BUILDERS_26_50

TOPIC = "Work energy and power"
LO = "ps_work_energy_and_power"

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())
ARCHETYPES: List[str] = list(BUILDERS.keys())

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "49_work_energy_power_capstone_synthesis",
    "concepts": "16_work_energy_theorem_horizontal_acceleration_from_rest",
    "work_energy": "16_work_energy_theorem_horizontal_acceleration_from_rest",
    "work_done": "01_work_done_constant_horizontal_force",
    "elementary_work_done": "01_work_done_constant_horizontal_force",
    "work_angle": "02_work_done_force_at_angle_above_horizontal",
    "elementary_work_angle": "02_work_done_force_at_angle_above_horizontal",
    "perpendicular_force": "04_zero_work_done_by_perpendicular_forces",
    "friction_work": "05_negative_work_done_by_kinetic_friction",
    "gravity_work": "06_work_done_by_gravity_vertical_free_fall",
    "fx_graph": "13_work_from_force_displacement_graph_rectangle_triangle",
    "kinetic_energy": "15_kinetic_energy_and_change_in_kinetic_energy",
    "elementary_kinetic_energy": "15_kinetic_energy_and_change_in_kinetic_energy",
    "work_energy_theorem": "16_work_energy_theorem_horizontal_acceleration_from_rest",
    "elementary_work_energy": "16_work_energy_theorem_horizontal_acceleration_from_rest",
    "stopping_distance": "18_work_energy_theorem_braking_stopping_distance",
    "incline_rough": "22_work_energy_theorem_sliding_down_rough_incline",
    "conservative_forces": "26_conservative_forces_and_path_independence",
    "non_conservative_forces": "27_non_conservative_forces_and_path_dependence",
    "wnc_theorem": "28_work_done_by_non_conservative_forces_theorem",
    "elementary_wnc": "28_work_done_by_non_conservative_forces_theorem",
    "wnc_horizontal": "29_wnc_on_horizontal_surface_with_friction",
    "wnc_incline": "30_wnc_sliding_down_rough_incline",
    "falling_air_drag": "32_wnc_falling_with_air_resistance",
    "curved_track": "33_wnc_curved_roller_coaster_track_with_friction",
    "conservation_of_mechanical_energy": "35_conservation_of_mechanical_energy_isolated_system",
    "loop_the_loop": "36_conservation_of_mechanical_energy_loop_the_loop",
    "power": "37_average_power_definition_and_formula",
    "elementary_power": "37_average_power_definition_and_formula",
    "power_hoist": "38_power_lifting_mass_at_constant_speed",
    "power_vehicle": "40_power_formula_p_equals_f_v_constant_speed",
    "aerodynamic_drag": "41_power_car_cruising_against_air_resistance",
    "incline_power": "42_power_vehicle_climbing_rough_incline",
    "borehole_pump": "43_borehole_submersible_pump_power",
    "hydroelectric_power": "44_hydroelectric_pump_storage_generation_power",
    "escalator_power": "45_escalator_human_passenger_transport_power",
    "mechanical_efficiency": "46_mechanical_efficiency_of_machines",
    "kwh_tariff": "47_kilowatt_hour_and_electrical_energy_cost",
    "composite_rider": "48_work_energy_power_composite_multistage_rider",
    "capstone_synthesis": "49_work_energy_power_capstone_synthesis",
    "diagnostic_autopsy": "50_work_energy_power_diagnostic_autopsy",
}


def _resolve_builder(target: Optional[str]) -> Optional[Callable[[random.Random], Dict[str, Any]]]:
    if not target or target in ("mixed", "all", "default"):
        return None
    if target in BUILDERS:
        return BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target]]
    t_low = target.lower()
    for k, b in BUILDERS.items():
        if t_low in k.lower():
            return b
    return None


def _normalize_question_payload(q: Dict[str, Any], seed_val: Optional[int], difficulty: str, mode: str) -> Dict[str, Any]:
    prompt_str = q.get("prompt") or q.get("question") or ""
    ans_str = q.get("answer_latex") or q.get("correct_answer") or q.get("sample_answer") or ""
    q.setdefault("question", prompt_str)
    q.setdefault("question_text", prompt_str)
    q.setdefault("prompt", prompt_str)
    q.setdefault("prompt_latex", prompt_str)
    q.setdefault("correct_answer", ans_str)
    q.setdefault("sample_answer", ans_str)
    q.setdefault("answer_latex", ans_str)
    q.setdefault("worked_solution", ans_str)
    q.setdefault("explanation", ans_str)
    q.setdefault("question_type", "short_answer")
    q.setdefault("difficulty", difficulty)
    q.setdefault("mode", mode or "compound")
    if seed_val is not None:
        q["seed"] = seed_val
    return q


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single deterministic 6-pillar question for Work, Energy and Power."""
    r = random.Random(seed) if seed is not None else random.Random(42)
    effective_target = subskill or kwargs.get("archetype") or kwargs.get("mode")
    builder = _resolve_builder(effective_target)
    if not builder:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = BUILDERS[chosen_subskill]

    q = builder(r)
    return _normalize_question_payload(q, seed, difficulty, kwargs.get("mode", "compound"))


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Physical Sciences Grade 12 Work, Energy and Power."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = subskill or kwargs.get("archetype") or (mode if mode != "compound" else None)
    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        item_seed = base_seed if count == 1 else (base_seed * 1000 + i)
        sub_r = random.Random(item_seed)

        builder = _resolve_builder(effective_target)
        if not builder:
            chosen_subskill = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
            builder = BUILDERS[chosen_subskill]

        q = builder(sub_r)
        q = _normalize_question_payload(q, item_seed, difficulty, mode)
        questions.append(q)

    return questions
