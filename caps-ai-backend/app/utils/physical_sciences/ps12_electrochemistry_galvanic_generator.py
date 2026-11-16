"""Physical Sciences (Grade 12 Term 3) — Electrochemical Reactions & Galvanic Cells Generator.

Aggregates 50 distinct semantic archetypes across:
- Subskills 01–25: Galvanic / Voltaic Cells, Electrode Potentials, Cell Notation & Dynamics
  (Conversion of chemical to electrical energy, standard conditions 298 K, 1 mol/dm3, 101,3 kPa,
  Standard Hydrogen Electrode SHE reference, Anode vs Cathode definitions, external circuit electron flow,
  Standard Reduction Potentials Table 4A/4B, predicting spontaneity, Daniell cell (Zn-Cu), Mg-Cu,
  Al-Cu, Ni-Ag, Pb-Ag, Fe-Cu galvanic corrosion protection, standard cell notation with solid
  and inert platinum electrodes, E0_cell = E0_cathode - E0_anode, determining unknown electrode potentials,
  Le Chatelier concentration effects, electrode surface area, equilibrium E_cell = 0 V,
  electrode mass stoichiometry, Faraday charge and current, and halogen half-cells).
- Subskills 26–50: Salt Bridge Mechanics, Electrolytic Cells, Industrial Applications & Autopsy
  (Salt bridge functions, electrical neutrality, ion migration, salt bridge removal,
  electrolyte precipitation incompatibility, internal resistance, electrolytic cell definitions,
  electrical to chemical energy conversion, non-spontaneous reactions, electrode polarities,
  electrolysis of molten NaCl in Downs cell, electrolysis of aqueous CuCl2, competing aqueous reactions,
  industrial electroplating of silver and nickel, quantitative Faraday mass calculations,
  electrorefining of blister copper, anode sludge precious metal recovery, Hall-Héroult aluminium extraction,
  cryolite flux, carbon anode consumption into CO2, chlor-alkali membrane cell, composite galvanic-electrolytic
  circuits, capstone synthesis rider, and diagnostic autopsy).

Strictly complies with the 6-Pillar Generator Contract (100% deterministic, zero-LLM).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ps12_electrochemistry_galvanic_archetypes_01_25 import (
    BUILDERS_01_25,
    FARADAY_CONST,
    STANDARD_REDUCTION_DATA,
    _fmt_sa,
)
from .ps12_electrochemistry_galvanic_archetypes_26_50 import BUILDERS_26_50

TOPIC = "Electrochemical reactions"
LO = "ps12_electrochemical_reactions"

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(BUILDERS.keys())
ARCHETYPES: List[str] = list(BUILDERS.keys())

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "49_electrochemistry_capstone_synthesis_rider",
    "galvanic_derivation": "08_daniell_cell_zn_cu_reactions_and_observations",
    "daniell_cell": "08_daniell_cell_zn_cu_reactions_and_observations",
    "galvanic_cell": "08_daniell_cell_zn_cu_reactions_and_observations",
    "elementary_galvanic": "01_galvanic_cell_definition_energy_conversion",
    "standard_conditions": "02_standard_conditions_galvanic_cells",
    "she_reference": "03_standard_hydrogen_electrode_she_reference",
    "anode_cathode": "04_anode_and_cathode_definitions_redox",
    "electron_flow": "05_electron_flow_direction_external_circuit",
    "table_potentials": "06_table_of_standard_reduction_potentials_table_4a_4b",
    "spontaneity": "07_predicting_spontaneity_from_reduction_potentials",
    "cell_notation": "14_standard_cell_notation_solid_electrodes",
    "inert_electrode": "15_standard_cell_notation_inert_platinum_electrodes",
    "cell_potential": "16_cell_potential_formula_ecell_ecathode_minus_eanode",
    "unknown_potential": "17_determining_unknown_electrode_potential_from_ecell",
    "concentration_effect": "18_effect_of_concentration_changes_on_cell_potential",
    "surface_area": "19_effect_of_electrode_surface_area_on_potential_and_current",
    "equilibrium_emf": "20_cell_potential_drop_to_zero_at_chemical_equilibrium",
    "electrode_mass": "21_mass_changes_of_electrodes_quantitative_stoichiometry",
    "faraday_law": "22_faraday_charge_and_electron_moles_in_galvanic_cell",
    "halides": "23_halide_half_cells_chlorine_bromine_iodine_potentials",
    "galvanic_diagram": "24_galvanic_cell_with_seed_varied_inline_diagram",
    "salt_bridge": "26_salt_bridge_functions_and_mechanics",
    "ion_migration": "27_salt_bridge_ion_migration_anion_cation",
    "salt_bridge_removal": "28_salt_bridge_removal_effect_on_current",
    "precipitation": "29_salt_bridge_electrolyte_precipitation_incompatibility",
    "internal_resistance": "30_internal_resistance_of_galvanic_cell",
    "electrolytic_cell": "31_electrolytic_cell_definition_and_energy_conversion",
    "cell_comparison": "32_galvanic_vs_electrolytic_cell_structural_comparison",
    "electrolytic_polarities": "33_electrolytic_cell_anode_and_cathode_polarities",
    "molten_nacl": "34_electrolysis_of_molten_sodium_chloride_downs_cell",
    "aqueous_cucl2": "35_electrolysis_of_aqueous_copper_chloride",
    "competing_reactions": "36_electrolysis_competing_reactions_water_vs_halide",
    "electroplating": "37_electroplating_principles_and_setup",
    "silver_plating": "38_electroplating_silver_onto_cutlery",
    "nickel_plating": "39_electroplating_nickel_onto_iron",
    "faraday_mass": "40_quantitative_electroplating_faraday_law_mass_deposited",
    "copper_refining": "41_electrorefining_of_copper_impure_blister_copper",
    "anode_sludge": "42_anode_sludge_recovery_in_copper_electrorefining",
    "aluminium_extraction": "43_hall_heroult_aluminium_extraction_principles",
    "carbon_anode": "44_carbon_anode_consumption_in_aluminium_smelting",
    "chloralkali": "45_membrane_cell_chloralkali_industry_overview",
    "membrane_cell": "46_chloralkali_membrane_cell_half_reactions",
    "electrolytic_diagram": "47_electrochemical_cells_with_inline_svg_diagram",
    "composite_circuit": "48_galvanic_cell_powering_electrolytic_cell_composite_rider",
    "capstone_synthesis": "49_electrochemistry_capstone_synthesis_rider",
    "diagnostic_autopsy": "50_electrochemistry_diagnostic_autopsy",
}


def _resolve_builder(target: Optional[str]) -> Optional[Callable[[random.Random], Dict[str, Any]]]:
    if not target or target in ("mixed", "all", "default"):
        return None
    target_clean = target.removeprefix("elementary_")
    if target_clean in BUILDERS:
        return BUILDERS[target_clean]
    if target_clean in LEGACY_ALIASES and LEGACY_ALIASES[target_clean] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target_clean]]
    t_low = target_clean.lower()
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
    """Generates a single deterministic 6-pillar question for Electrochemical Reactions."""
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
    """Master generator for Physical Sciences Grade 12 Electrochemical Reactions."""
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
