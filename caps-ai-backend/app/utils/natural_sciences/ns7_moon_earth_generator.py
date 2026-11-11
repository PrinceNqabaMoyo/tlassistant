"""Grade 7 Natural Sciences: Term 4 - Relationship of the Moon to the Earth Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_moon_earth_archetypes_01_25 import (
    arch_01_moon_revolution_period,
    arch_02_moon_synchronous_rotation,
    arch_03_near_side_vs_far_side_observation,
    arch_04_moon_distance_and_elliptical_orbit,
    arch_05_moon_surface_regolith_and_craters,
    arch_06_moon_absence_of_atmosphere,
    arch_07_moon_temperature_extremes,
    arch_08_lunar_phases_cause_geometry,
    arch_09_lunar_phase_new_moon,
    arch_10_lunar_phase_waxing_crescent,
    arch_11_lunar_phase_first_quarter,
    arch_12_lunar_phase_waxing_gibbous,
    arch_13_lunar_phase_full_moon,
    arch_14_lunar_phase_waning_gibbous,
    arch_15_lunar_phase_third_quarter,
    arch_16_lunar_phase_waning_crescent,
    arch_17_lunar_phase_full_cycle_sequence,
    arch_18_lunar_illumination_reflected_sunlight,
    arch_19_relative_positions_sun_earth_moon,
    arch_20_solar_eclipse_alignment_order,
    arch_21_solar_eclipse_umbra_penumbra_shadows,
    arch_22_solar_eclipse_angular_size_ratio,
    arch_23_total_vs_partial_solar_eclipse_zones,
    arch_24_solar_eclipse_path_of_totality,
    arch_25_solar_eclipse_safety_and_pinhole_projection,
)
from .ns7_moon_earth_archetypes_26_50 import (
    arch_26_lunar_eclipse_alignment_order,
    arch_27_lunar_eclipse_earth_shadow_types,
    arch_28_lunar_eclipse_red_blood_moon_refraction,
    arch_29_lunar_eclipse_night_hemisphere_visibility,
    arch_30_eclipse_scarcity_orbital_plane_tilt,
    arch_31_gravity_definition_non_contact_attraction,
    arch_32_gravity_factors_mass_and_distance,
    arch_33_gravity_keeps_moon_in_orbit,
    arch_34_mass_concept_invariance_kg,
    arch_35_weight_concept_gravitational_force_newtons,
    arch_36_weight_calculation_earth_gravity,
    arch_37_weight_calculation_moon_gravity,
    arch_38_weight_comparison_earth_vs_moon_ratio,
    arch_39_bathroom_scale_vs_beam_balance_physics,
    arch_40_astronaut_motion_reduced_gravity,
    arch_41_ocean_tides_gravitational_pull_cause,
    arch_42_two_high_and_two_low_tides_daily,
    arch_43_tidal_cycle_period_24_hours_50_minutes,
    arch_44_spring_tides_syzygy_alignment,
    arch_45_spring_tides_maximum_tidal_range,
    arch_46_neap_tides_quadrature_right_angle,
    arch_47_neap_tides_minimum_tidal_range,
    arch_48_tide_table_interpretation_and_predictions,
    arch_49_coastal_tides_maritime_and_ecological_impact,
    arch_50_moon_earth_comprehensive_diagnostic_autopsy,
)

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_moon_revolution_period": arch_01_moon_revolution_period,
    "02_moon_synchronous_rotation": arch_02_moon_synchronous_rotation,
    "03_near_side_vs_far_side_observation": arch_03_near_side_vs_far_side_observation,
    "04_moon_distance_and_elliptical_orbit": arch_04_moon_distance_and_elliptical_orbit,
    "05_moon_surface_regolith_and_craters": arch_05_moon_surface_regolith_and_craters,
    "06_moon_absence_of_atmosphere": arch_06_moon_absence_of_atmosphere,
    "07_moon_temperature_extremes": arch_07_moon_temperature_extremes,
    "08_lunar_phases_cause_geometry": arch_08_lunar_phases_cause_geometry,
    "09_lunar_phase_new_moon": arch_09_lunar_phase_new_moon,
    "10_lunar_phase_waxing_crescent": arch_10_lunar_phase_waxing_crescent,
    "11_lunar_phase_first_quarter": arch_11_lunar_phase_first_quarter,
    "12_lunar_phase_waxing_gibbous": arch_12_lunar_phase_waxing_gibbous,
    "13_lunar_phase_full_moon": arch_13_lunar_phase_full_moon,
    "14_lunar_phase_waning_gibbous": arch_14_lunar_phase_waning_gibbous,
    "15_lunar_phase_third_quarter": arch_15_lunar_phase_third_quarter,
    "16_lunar_phase_waning_crescent": arch_16_lunar_phase_waning_crescent,
    "17_lunar_phase_full_cycle_sequence": arch_17_lunar_phase_full_cycle_sequence,
    "18_lunar_illumination_reflected_sunlight": arch_18_lunar_illumination_reflected_sunlight,
    "19_relative_positions_sun_earth_moon": arch_19_relative_positions_sun_earth_moon,
    "20_solar_eclipse_alignment_order": arch_20_solar_eclipse_alignment_order,
    "21_solar_eclipse_umbra_penumbra_shadows": arch_21_solar_eclipse_umbra_penumbra_shadows,
    "22_solar_eclipse_angular_size_ratio": arch_22_solar_eclipse_angular_size_ratio,
    "23_total_vs_partial_solar_eclipse_zones": arch_23_total_vs_partial_solar_eclipse_zones,
    "24_solar_eclipse_path_of_totality": arch_24_solar_eclipse_path_of_totality,
    "25_solar_eclipse_safety_and_pinhole_projection": arch_25_solar_eclipse_safety_and_pinhole_projection,
    "26_lunar_eclipse_alignment_order": arch_26_lunar_eclipse_alignment_order,
    "27_lunar_eclipse_earth_shadow_types": arch_27_lunar_eclipse_earth_shadow_types,
    "28_lunar_eclipse_red_blood_moon_refraction": arch_28_lunar_eclipse_red_blood_moon_refraction,
    "29_lunar_eclipse_night_hemisphere_visibility": arch_29_lunar_eclipse_night_hemisphere_visibility,
    "30_eclipse_scarcity_orbital_plane_tilt": arch_30_eclipse_scarcity_orbital_plane_tilt,
    "31_gravity_definition_non_contact_attraction": arch_31_gravity_definition_non_contact_attraction,
    "32_gravity_factors_mass_and_distance": arch_32_gravity_factors_mass_and_distance,
    "33_gravity_keeps_moon_in_orbit": arch_33_gravity_keeps_moon_in_orbit,
    "34_mass_concept_invariance_kg": arch_34_mass_concept_invariance_kg,
    "35_weight_concept_gravitational_force_newtons": arch_35_weight_concept_gravitational_force_newtons,
    "36_weight_calculation_earth_gravity": arch_36_weight_calculation_earth_gravity,
    "37_weight_calculation_moon_gravity": arch_37_weight_calculation_moon_gravity,
    "38_weight_comparison_earth_vs_moon_ratio": arch_38_weight_comparison_earth_vs_moon_ratio,
    "39_bathroom_scale_vs_beam_balance_physics": arch_39_bathroom_scale_vs_beam_balance_physics,
    "40_astronaut_motion_reduced_gravity": arch_40_astronaut_motion_reduced_gravity,
    "41_ocean_tides_gravitational_pull_cause": arch_41_ocean_tides_gravitational_pull_cause,
    "42_two_high_and_two_low_tides_daily": arch_42_two_high_and_two_low_tides_daily,
    "43_tidal_cycle_period_24_hours_50_minutes": arch_43_tidal_cycle_period_24_hours_50_minutes,
    "44_spring_tides_syzygy_alignment": arch_44_spring_tides_syzygy_alignment,
    "45_spring_tides_maximum_tidal_range": arch_45_spring_tides_maximum_tidal_range,
    "46_neap_tides_quadrature_right_angle": arch_46_neap_tides_quadrature_right_angle,
    "47_neap_tides_minimum_tidal_range": arch_47_neap_tides_minimum_tidal_range,
    "48_tide_table_interpretation_and_predictions": arch_48_tide_table_interpretation_and_predictions,
    "49_coastal_tides_maritime_and_ecological_impact": arch_49_coastal_tides_maritime_and_ecological_impact,
    "50_moon_earth_comprehensive_diagnostic_autopsy": arch_50_moon_earth_comprehensive_diagnostic_autopsy,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Relationship of the Moon to the Earth.

    Returns a list of question dicts adhering to the 6-pillar contract.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill
        if not chosen_subskill or chosen_subskill not in ARCHETYPE_BUILDERS:
            chosen_subskill = rng.choice(SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[chosen_subskill]
        q = builder(rng)
        # Ensure common metadata
        q.setdefault("grade", 7)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("term", 4)
        q.setdefault("topic", "Relationship of the moon to the earth")
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
