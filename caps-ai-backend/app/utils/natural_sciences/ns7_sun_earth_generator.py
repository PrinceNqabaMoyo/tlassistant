"""Grade 7 Natural Sciences: Term 4 - Relationship of the Sun to the Earth Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_sun_earth_archetypes_01_25 import (
    arch_01_sun_characteristics_star_fusion,
    arch_02_sun_distance_and_light_travel_time,
    arch_03_earth_rotation_axis_poles,
    arch_04_earth_rotation_period_24_hours,
    arch_05_earth_rotation_direction_west_to_east,
    arch_06_day_and_night_cycle_cause,
    arch_07_apparent_motion_sun_east_to_west,
    arch_08_solar_noon_shadow_length_and_direction,
    arch_09_shadow_diurnal_progression_morning_to_evening,
    arch_10_time_zones_and_longitudinal_rotation,
    arch_11_earth_revolution_period_365_days,
    arch_12_leap_year_astronomical_basis,
    arch_13_earth_orbit_elliptical_perihelion_aphelion,
    arch_14_distance_to_sun_not_cause_of_seasons_debunk,
    arch_15_earth_axial_tilt_angle_23_5_degrees,
    arch_16_axial_parallelism_polar_star_orientation,
    arch_17_angle_of_incidence_direct_vs_indirect_sunlight,
    arch_18_solar_energy_concentration_per_unit_surface_area,
    arch_19_seasonal_temperature_variations_mechanism,
    arch_20_day_length_variations_summer_vs_winter,
    arch_21_southern_hemisphere_summer_solstice_december,
    arch_22_southern_hemisphere_winter_solstice_june,
    arch_23_vernal_autumnal_equinoxes_equal_day_night,
    arch_24_tropic_of_capricorn_zenith_sun,
    arch_25_tropic_of_cancer_zenith_sun,
)
from .ns7_sun_earth_archetypes_26_50 import (
    arch_26_polar_day_and_night_midnight_sun,
    arch_27_opposite_seasons_northern_vs_southern_hemisphere,
    arch_28_seasonal_lag_thermal_inertia_oceans,
    arch_29_solar_energy_sustaining_photosynthesis,
    arch_30_solar_energy_driving_the_water_cycle,
    arch_31_solar_heating_driving_global_winds,
    arch_32_solar_energy_ocean_currents_convection,
    arch_33_solar_radiation_spectrum_visible_uv_infrared,
    arch_34_earths_atmosphere_insulation_greenhouse_effect,
    arch_35_ozone_layer_uv_protection,
    arch_36_earths_magnetic_field_solar_wind_deflection,
    arch_37_aurora_australis_southern_lights_phenomenon,
    arch_38_solar_flares_and_space_weather_impact,
    arch_39_sundials_and_gnomon_timekeeping,
    arch_40_seasonal_agricultural_cycles_south_africa,
    arch_41_solar_power_photovoltaic_renewable_energy,
    arch_42_solar_thermal_water_heating_principles,
    arch_43_passive_solar_building_design_insulation,
    arch_44_albedo_effect_surface_reflectivity_ice_land,
    arch_45_diffuse_vs_direct_solar_radiation_cloud_cover,
    arch_46_equatorial_vs_polar_climate_solar_distribution,
    arch_47_zenith_angle_and_atmospheric_path_length,
    arch_48_seasonal_animal_behaviour_hibernation_migration,
    arch_49_seasonal_plant_adaptations_deciduous_dormancy,
    arch_50_sun_earth_comprehensive_diagnostic_autopsy,
)

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_sun_characteristics_star_fusion": arch_01_sun_characteristics_star_fusion,
    "02_sun_distance_and_light_travel_time": arch_02_sun_distance_and_light_travel_time,
    "03_earth_rotation_axis_poles": arch_03_earth_rotation_axis_poles,
    "04_earth_rotation_period_24_hours": arch_04_earth_rotation_period_24_hours,
    "05_earth_rotation_direction_west_to_east": arch_05_earth_rotation_direction_west_to_east,
    "06_day_and_night_cycle_cause": arch_06_day_and_night_cycle_cause,
    "07_apparent_motion_sun_east_to_west": arch_07_apparent_motion_sun_east_to_west,
    "08_solar_noon_shadow_length_and_direction": arch_08_solar_noon_shadow_length_and_direction,
    "09_shadow_diurnal_progression_morning_to_evening": arch_09_shadow_diurnal_progression_morning_to_evening,
    "10_time_zones_and_longitudinal_rotation": arch_10_time_zones_and_longitudinal_rotation,
    "11_earth_revolution_period_365_days": arch_11_earth_revolution_period_365_days,
    "12_leap_year_astronomical_basis": arch_12_leap_year_astronomical_basis,
    "13_earth_orbit_elliptical_perihelion_aphelion": arch_13_earth_orbit_elliptical_perihelion_aphelion,
    "14_distance_to_sun_not_cause_of_seasons_debunk": arch_14_distance_to_sun_not_cause_of_seasons_debunk,
    "15_earth_axial_tilt_angle_23_5_degrees": arch_15_earth_axial_tilt_angle_23_5_degrees,
    "16_axial_parallelism_polar_star_orientation": arch_16_axial_parallelism_polar_star_orientation,
    "17_angle_of_incidence_direct_vs_indirect_sunlight": arch_17_angle_of_incidence_direct_vs_indirect_sunlight,
    "18_solar_energy_concentration_per_unit_surface_area": arch_18_solar_energy_concentration_per_unit_surface_area,
    "19_seasonal_temperature_variations_mechanism": arch_19_seasonal_temperature_variations_mechanism,
    "20_day_length_variations_summer_vs_winter": arch_20_day_length_variations_summer_vs_winter,
    "21_southern_hemisphere_summer_solstice_december": arch_21_southern_hemisphere_summer_solstice_december,
    "22_southern_hemisphere_winter_solstice_june": arch_22_southern_hemisphere_winter_solstice_june,
    "23_vernal_autumnal_equinoxes_equal_day_night": arch_23_vernal_autumnal_equinoxes_equal_day_night,
    "24_tropic_of_capricorn_zenith_sun": arch_24_tropic_of_capricorn_zenith_sun,
    "25_tropic_of_cancer_zenith_sun": arch_25_tropic_of_cancer_zenith_sun,
    "26_polar_day_and_night_midnight_sun": arch_26_polar_day_and_night_midnight_sun,
    "27_opposite_seasons_northern_vs_southern_hemisphere": arch_27_opposite_seasons_northern_vs_southern_hemisphere,
    "28_seasonal_lag_thermal_inertia_oceans": arch_28_seasonal_lag_thermal_inertia_oceans,
    "29_solar_energy_sustaining_photosynthesis": arch_29_solar_energy_sustaining_photosynthesis,
    "30_solar_energy_driving_the_water_cycle": arch_30_solar_energy_driving_the_water_cycle,
    "31_solar_heating_driving_global_winds": arch_31_solar_heating_driving_global_winds,
    "32_solar_energy_ocean_currents_convection": arch_32_solar_energy_ocean_currents_convection,
    "33_solar_radiation_spectrum_visible_uv_infrared": arch_33_solar_radiation_spectrum_visible_uv_infrared,
    "34_earths_atmosphere_insulation_greenhouse_effect": arch_34_earths_atmosphere_insulation_greenhouse_effect,
    "35_ozone_layer_uv_protection": arch_35_ozone_layer_uv_protection,
    "36_earths_magnetic_field_solar_wind_deflection": arch_36_earths_magnetic_field_solar_wind_deflection,
    "37_aurora_australis_southern_lights_phenomenon": arch_37_aurora_australis_southern_lights_phenomenon,
    "38_solar_flares_and_space_weather_impact": arch_38_solar_flares_and_space_weather_impact,
    "39_sundials_and_gnomon_timekeeping": arch_39_sundials_and_gnomon_timekeeping,
    "40_seasonal_agricultural_cycles_south_africa": arch_40_seasonal_agricultural_cycles_south_africa,
    "41_solar_power_photovoltaic_renewable_energy": arch_41_solar_power_photovoltaic_renewable_energy,
    "42_solar_thermal_water_heating_principles": arch_42_solar_thermal_water_heating_principles,
    "43_passive_solar_building_design_insulation": arch_43_passive_solar_building_design_insulation,
    "44_albedo_effect_surface_reflectivity_ice_land": arch_44_albedo_effect_surface_reflectivity_ice_land,
    "45_diffuse_vs_direct_solar_radiation_cloud_cover": arch_45_diffuse_vs_direct_solar_radiation_cloud_cover,
    "46_equatorial_vs_polar_climate_solar_distribution": arch_46_equatorial_vs_polar_climate_solar_distribution,
    "47_zenith_angle_and_atmospheric_path_length": arch_47_zenith_angle_and_atmospheric_path_length,
    "48_seasonal_animal_behaviour_hibernation_migration": arch_48_seasonal_animal_behaviour_hibernation_migration,
    "49_seasonal_plant_adaptations_deciduous_dormancy": arch_49_seasonal_plant_adaptations_deciduous_dormancy,
    "50_sun_earth_comprehensive_diagnostic_autopsy": arch_50_sun_earth_comprehensive_diagnostic_autopsy,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Relationship of the Sun to the Earth.

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
        q.setdefault("topic", "Relationship of the sun to the Earth")
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
