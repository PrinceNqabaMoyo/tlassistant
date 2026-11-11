"""Grade 7 Natural Sciences: Term 2 - Properties of Materials Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/01. Properties of materials.md.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_properties_of_materials_archetypes_01_25 import (
    arch_01_malleability_definition_and_examples,
    arch_02_ductility_definition_and_wires,
    arch_03_tensile_strength_applications,
    arch_04_compressive_strength_construction,
    arch_05_experimental_strength_test_load,
    arch_06_flexibility_vs_stiffness,
    arch_07_brittleness_in_solids,
    arch_08_hardness_scratch_test,
    arch_09_density_comparison_floating_sinking,
    arch_10_melting_point_definition_and_state,
    arch_11_boiling_point_definition_and_state,
    arch_12_three_states_state_identification_temp,
    arch_13_pure_substance_sharp_melting_point,
    arch_14_mixtures_melting_range_impure,
    arch_15_heating_curve_phase_change_plateau,
    arch_16_cooling_curve_freezing_condensation,
    arch_17_electrical_conductors_identification,
    arch_18_electrical_insulators_identification,
    arch_19_testing_electrical_conductivity_circuit,
    arch_20_thermal_conductors_identification,
    arch_21_thermal_insulators_everyday_uses,
    arch_22_thermal_conductivity_experiment_wax_pins,
    arch_23_dual_property_selection_cookware,
    arch_24_dual_property_selection_cables,
    arch_25_magnetic_vs_non_magnetic_materials,
)

from .ns7_properties_of_materials_archetypes_26_50 import (
    arch_26_ferrous_vs_non_ferrous_metals,
    arch_27_corrosion_and_rusting_protection,
    arch_28_transparency_translucency_opacity,
    arch_29_suitability_of_materials_safety_gear,
    arch_30_textiles_natural_vs_synthetic_fibres,
    arch_31_environmental_impact_open_cast_mining,
    arch_32_acid_mine_drainage_and_water,
    arch_33_energy_consumption_raw_vs_recycled,
    arch_34_air_pollution_smelting_greenhouse_gases,
    arch_35_biodegradable_definition_and_examples,
    arch_36_non_biodegradable_plastics_persistence,
    arch_37_impact_of_plastics_on_marine_life,
    arch_38_waste_hierarchy_refuse_reduce_reuse_recycle,
    arch_39_recyclable_materials_identification_symbols,
    arch_40_non_recyclable_items_contamination,
    arch_41_landfill_management_leachate_problems,
    arch_42_informal_waste_reclaimers_role,
    arch_43_lifecycle_analysis_shopping_bags,
    arch_44_glass_recycling_closed_loop,
    arch_45_paper_recycling_and_deforestation,
    arch_46_designing_sustainable_packaging,
    arch_47_evaluating_material_tradeoffs_cost_strength,
    arch_48_evaluating_material_tradeoffs_weight_insulation,
    arch_49_scientific_inquiry_fair_test_variables,
    arch_50_interpreting_data_tables_material_selection,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 09: Mechanical & Physical Properties
    arch_01_malleability_definition_and_examples,
    arch_02_ductility_definition_and_wires,
    arch_03_tensile_strength_applications,
    arch_04_compressive_strength_construction,
    arch_05_experimental_strength_test_load,
    arch_06_flexibility_vs_stiffness,
    arch_07_brittleness_in_solids,
    arch_08_hardness_scratch_test,
    arch_09_density_comparison_floating_sinking,
    # 10 - 16: Boiling, Melting & Thermal Curves
    arch_10_melting_point_definition_and_state,
    arch_11_boiling_point_definition_and_state,
    arch_12_three_states_state_identification_temp,
    arch_13_pure_substance_sharp_melting_point,
    arch_14_mixtures_melting_range_impure,
    arch_15_heating_curve_phase_change_plateau,
    arch_16_cooling_curve_freezing_condensation,
    # 17 - 25: Electrical & Thermal Conductivity
    arch_17_electrical_conductors_identification,
    arch_18_electrical_insulators_identification,
    arch_19_testing_electrical_conductivity_circuit,
    arch_20_thermal_conductors_identification,
    arch_21_thermal_insulators_everyday_uses,
    arch_22_thermal_conductivity_experiment_wax_pins,
    arch_23_dual_property_selection_cookware,
    arch_24_dual_property_selection_cables,
    arch_25_magnetic_vs_non_magnetic_materials,
    # 26 - 30: Metal Types, Corrosion & Optical Properties
    arch_26_ferrous_vs_non_ferrous_metals,
    arch_27_corrosion_and_rusting_protection,
    arch_28_transparency_translucency_opacity,
    arch_29_suitability_of_materials_safety_gear,
    arch_30_textiles_natural_vs_synthetic_fibres,
    # 31 - 37: Environmental Impact of Mining & Manufacturing
    arch_31_environmental_impact_open_cast_mining,
    arch_32_acid_mine_drainage_and_water,
    arch_33_energy_consumption_raw_vs_recycled,
    arch_34_air_pollution_smelting_greenhouse_gases,
    arch_35_biodegradable_definition_and_examples,
    arch_36_non_biodegradable_plastics_persistence,
    arch_37_impact_of_plastics_on_marine_life,
    # 38 - 50: Recycling & Material Selection
    arch_38_waste_hierarchy_refuse_reduce_reuse_recycle,
    arch_39_recyclable_materials_identification_symbols,
    arch_40_non_recyclable_items_contamination,
    arch_41_landfill_management_leachate_problems,
    arch_42_informal_waste_reclaimers_role,
    arch_43_lifecycle_analysis_shopping_bags,
    arch_44_glass_recycling_closed_loop,
    arch_45_paper_recycling_and_deforestation,
    arch_46_designing_sustainable_packaging,
    arch_47_evaluating_material_tradeoffs_cost_strength,
    arch_48_evaluating_material_tradeoffs_weight_insulation,
    arch_49_scientific_inquiry_fair_test_variables,
    arch_50_interpreting_data_tables_material_selection,
]

SUBSKILLS: List[str] = [
    # 01 - 09
    "01_malleability_definition_and_examples",
    "02_ductility_definition_and_wires",
    "03_tensile_strength_applications",
    "04_compressive_strength_construction",
    "05_experimental_strength_test_load",
    "06_flexibility_vs_stiffness",
    "07_brittleness_in_solids",
    "08_hardness_scratch_test",
    "09_density_comparison_floating_sinking",
    # 10 - 16
    "10_melting_point_definition_and_state",
    "11_boiling_point_definition_and_state",
    "12_three_states_state_identification_temp",
    "13_pure_substance_sharp_melting_point",
    "14_mixtures_melting_range_impure",
    "15_heating_curve_phase_change_plateau",
    "16_cooling_curve_freezing_condensation",
    # 17 - 25
    "17_electrical_conductors_identification",
    "18_electrical_insulators_identification",
    "19_testing_electrical_conductivity_circuit",
    "20_thermal_conductors_identification",
    "21_thermal_insulators_everyday_uses",
    "22_thermal_conductivity_experiment_wax_pins",
    "23_dual_property_selection_cookware",
    "24_dual_property_selection_cables",
    "25_magnetic_vs_non_magnetic_materials",
    # 26 - 30
    "26_ferrous_vs_non_ferrous_metals",
    "27_corrosion_and_rusting_protection",
    "28_transparency_translucency_opacity",
    "29_suitability_of_materials_safety_gear",
    "30_textiles_natural_vs_synthetic_fibres",
    # 31 - 37
    "31_environmental_impact_open_cast_mining",
    "32_acid_mine_drainage_and_water",
    "33_energy_consumption_raw_vs_recycled",
    "34_air_pollution_smelting_greenhouse_gases",
    "35_biodegradable_definition_and_examples",
    "36_non_biodegradable_plastics_persistence",
    "37_impact_of_plastics_on_marine_life",
    # 38 - 50
    "38_waste_hierarchy_refuse_reduce_reuse_recycle",
    "39_recyclable_materials_identification_symbols",
    "40_non_recyclable_items_contamination",
    "41_landfill_management_leachate_problems",
    "42_informal_waste_reclaimers_role",
    "43_lifecycle_analysis_shopping_bags",
    "44_glass_recycling_closed_loop",
    "45_paper_recycling_and_deforestation",
    "46_designing_sustainable_packaging",
    "47_evaluating_material_tradeoffs_cost_strength",
    "48_evaluating_material_tradeoffs_weight_insulation",
    "49_scientific_inquiry_fair_test_variables",
    "50_interpreting_data_tables_material_selection",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based integer and padded string aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["physical_properties_malleability_ductility"] = arch_01_malleability_definition_and_examples
DISPATCH_TABLE["thermal_and_electrical_conductivity"] = arch_20_thermal_conductors_identification
DISPATCH_TABLE["strength_tensile_and_compressive"] = arch_03_tensile_strength_applications
DISPATCH_TABLE["boiling_and_melting_points_pure_substances"] = arch_10_melting_point_definition_and_state
DISPATCH_TABLE["environmental_impact_and_recycling"] = arch_38_waste_hierarchy_refuse_reduce_reuse_recycle


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Natural Sciences: Properties of Materials Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
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
                elif 1 <= idx <= len(BUILDERS):
                    builder = BUILDERS[idx - 1]
            except (ValueError, TypeError):
                pass

        if builder is None:
            builder = rng.choice(BUILDERS)

        q = builder(rng)
        q.setdefault("grade", 7)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("topic", "Properties of materials")
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
