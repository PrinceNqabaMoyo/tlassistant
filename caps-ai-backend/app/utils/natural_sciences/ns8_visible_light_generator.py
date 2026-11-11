"""Grade 8 Natural Sciences: Term 3 - Visible Light Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/04. Visible light.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .ns8_visible_light_archetypes_01_25 import (
    arch_01_definition_of_light_as_radiant_electromagnetic_energy,
    arch_02_rectilinear_propagation_of_light_in_straight_lines,
    arch_03_speed_of_light_in_vacuum_and_travel_time_calculations,
    arch_04_distinguishing_luminous_versus_non_luminous_celestial_and_terrestrial_objects,
    arch_05_scientific_ray_diagram_conventions_and_beam_types,
    arch_06_pinhole_camera_inverted_image_formation_mechanism,
    arch_07_pinhole_camera_image_size_variation_with_object_distance,
    arch_08_pinhole_camera_aperture_size_effect_on_sharpness_and_brightness,
    arch_09_transparent_translucent_and_opaque_material_classification,
    arch_10_formation_of_shadows_by_opaque_objects_in_straight_rays,
    arch_11_shadow_umbra_and_penumbra_zones_from_extended_sources,
    arch_12_solar_and_lunar_eclipses_as_large_scale_shadow_phenomena,
    arch_13_dispersion_of_white_light_through_triangular_prism,
    arch_14_visible_spectrum_sequence_of_seven_spectral_colours_roygbiv,
    arch_15_wavelength_frequency_and_refraction_angle_relationship_in_dispersion,
    arch_16_why_violet_light_refracts_most_and_red_light_refracts_least,
    arch_17_formation_of_natural_rainbows_by_atmospheric_water_droplets,
    arch_18_specular_regular_reflection_versus_diffuse_reflection,
    arch_19_why_diffuse_reflection_allows_rough_objects_to_be_seen_from_all_angles,
    arch_20_law_of_reflection_angle_of_incidence_equals_angle_of_reflection,
    arch_21_measuring_angles_of_incidence_and_reflection_relative_to_normal,
    arch_22_plane_mirror_image_characteristics_virtual_upright_same_size,
    arch_23_plane_mirror_lateral_inversion_and_perpendicular_distance,
    arch_24_definition_and_physical_cause_of_light_refraction,
    arch_25_refraction_direction_when_entering_optically_denser_medium,
)
from .ns8_visible_light_archetypes_26_50 import (
    arch_26_refraction_direction_when_entering_optically_rarer_medium,
    arch_27_perpendicular_incidence_light_ray_entering_at_zero_degrees_to_normal,
    arch_28_apparent_depth_illusion_of_submerged_objects_due_to_refraction,
    arch_29_apparent_bending_of_pencil_or_straw_submerged_in_water,
    arch_30_mirages_and_atmospheric_refraction_of_sunlight,
    arch_31_colour_perception_via_selective_reflection_and_absorption,
    arch_32_why_white_objects_reflect_all_colours_and_stay_cooler,
    arch_33_why_black_objects_absorb_all_colours_and_convert_to_heat,
    arch_34_perceiving_coloured_objects_under_monochromatic_red_illumination,
    arch_35_perceiving_coloured_objects_under_monochromatic_blue_illumination,
    arch_36_perceiving_coloured_objects_under_monochromatic_green_illumination,
    arch_37_function_of_transparent_coloured_optical_filters,
    arch_38_primary_colours_of_light_red_green_blue_additive_mixing,
    arch_39_secondary_colours_of_light_cyan_magenta_yellow_formation,
    arch_40_structure_of_human_eye_cornea_pupil_iris_lens_retina,
    arch_41_function_of_retina_photoreceptor_cells_rods_and_cones,
    arch_42_convex_converging_lenses_and_focal_point_properties,
    arch_43_concave_diverging_lenses_and_focal_properties,
    arch_44_correcting_short_sightedness_myopia_using_concave_lenses,
    arch_45_correcting_long_sightedness_hyperopia_using_convex_lenses,
    arch_46_misconception_eyes_emit_light_rays_to_see_objects,
    arch_47_misconception_light_travels_only_a_short_distance_before_running_out,
    arch_48_misconception_colours_exist_as_matter_inside_objects_in_the_dark,
    arch_49_experimental_design_variables_in_light_and_optics_investigations,
    arch_50_visible_light_comprehensive_diagnostic_evaluation,
)

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    "01_definition_of_light_as_radiant_electromagnetic_energy": arch_01_definition_of_light_as_radiant_electromagnetic_energy,
    "02_rectilinear_propagation_of_light_in_straight_lines": arch_02_rectilinear_propagation_of_light_in_straight_lines,
    "03_speed_of_light_in_vacuum_and_travel_time_calculations": arch_03_speed_of_light_in_vacuum_and_travel_time_calculations,
    "04_distinguishing_luminous_versus_non_luminous_celestial_and_terrestrial_objects": arch_04_distinguishing_luminous_versus_non_luminous_celestial_and_terrestrial_objects,
    "05_scientific_ray_diagram_conventions_and_beam_types": arch_05_scientific_ray_diagram_conventions_and_beam_types,
    "06_pinhole_camera_inverted_image_formation_mechanism": arch_06_pinhole_camera_inverted_image_formation_mechanism,
    "07_pinhole_camera_image_size_variation_with_object_distance": arch_07_pinhole_camera_image_size_variation_with_object_distance,
    "08_pinhole_camera_aperture_size_effect_on_sharpness_and_brightness": arch_08_pinhole_camera_aperture_size_effect_on_sharpness_and_brightness,
    "09_transparent_translucent_and_opaque_material_classification": arch_09_transparent_translucent_and_opaque_material_classification,
    "10_formation_of_shadows_by_opaque_objects_in_straight_rays": arch_10_formation_of_shadows_by_opaque_objects_in_straight_rays,
    "11_shadow_umbra_and_penumbra_zones_from_extended_sources": arch_11_shadow_umbra_and_penumbra_zones_from_extended_sources,
    "12_solar_and_lunar_eclipses_as_large_scale_shadow_phenomena": arch_12_solar_and_lunar_eclipses_as_large_scale_shadow_phenomena,
    "13_dispersion_of_white_light_through_triangular_prism": arch_13_dispersion_of_white_light_through_triangular_prism,
    "14_visible_spectrum_sequence_of_seven_spectral_colours_roygbiv": arch_14_visible_spectrum_sequence_of_seven_spectral_colours_roygbiv,
    "15_wavelength_frequency_and_refraction_angle_relationship_in_dispersion": arch_15_wavelength_frequency_and_refraction_angle_relationship_in_dispersion,
    "16_why_violet_light_refracts_most_and_red_light_refracts_least": arch_16_why_violet_light_refracts_most_and_red_light_refracts_least,
    "17_formation_of_natural_rainbows_by_atmospheric_water_droplets": arch_17_formation_of_natural_rainbows_by_atmospheric_water_droplets,
    "18_specular_regular_reflection_versus_diffuse_reflection": arch_18_specular_regular_reflection_versus_diffuse_reflection,
    "19_why_diffuse_reflection_allows_rough_objects_to_be_seen_from_all_angles": arch_19_why_diffuse_reflection_allows_rough_objects_to_be_seen_from_all_angles,
    "20_law_of_reflection_angle_of_incidence_equals_angle_of_reflection": arch_20_law_of_reflection_angle_of_incidence_equals_angle_of_reflection,
    "21_measuring_angles_of_incidence_and_reflection_relative_to_normal": arch_21_measuring_angles_of_incidence_and_reflection_relative_to_normal,
    "22_plane_mirror_image_characteristics_virtual_upright_same_size": arch_22_plane_mirror_image_characteristics_virtual_upright_same_size,
    "23_plane_mirror_lateral_inversion_and_perpendicular_distance": arch_23_plane_mirror_lateral_inversion_and_perpendicular_distance,
    "24_definition_and_physical_cause_of_light_refraction": arch_24_definition_and_physical_cause_of_light_refraction,
    "25_refraction_direction_when_entering_optically_denser_medium": arch_25_refraction_direction_when_entering_optically_denser_medium,
    "26_refraction_direction_when_entering_optically_rarer_medium": arch_26_refraction_direction_when_entering_optically_rarer_medium,
    "27_perpendicular_incidence_light_ray_entering_at_zero_degrees_to_normal": arch_27_perpendicular_incidence_light_ray_entering_at_zero_degrees_to_normal,
    "28_apparent_depth_illusion_of_submerged_objects_due_to_refraction": arch_28_apparent_depth_illusion_of_submerged_objects_due_to_refraction,
    "29_apparent_bending_of_pencil_or_straw_submerged_in_water": arch_29_apparent_bending_of_pencil_or_straw_submerged_in_water,
    "30_mirages_and_atmospheric_refraction_of_sunlight": arch_30_mirages_and_atmospheric_refraction_of_sunlight,
    "31_colour_perception_via_selective_reflection_and_absorption": arch_31_colour_perception_via_selective_reflection_and_absorption,
    "32_why_white_objects_reflect_all_colours_and_stay_cooler": arch_32_why_white_objects_reflect_all_colours_and_stay_cooler,
    "33_why_black_objects_absorb_all_colours_and_convert_to_heat": arch_33_why_black_objects_absorb_all_colours_and_convert_to_heat,
    "34_perceiving_coloured_objects_under_monochromatic_red_illumination": arch_34_perceiving_coloured_objects_under_monochromatic_red_illumination,
    "35_perceiving_coloured_objects_under_monochromatic_blue_illumination": arch_35_perceiving_coloured_objects_under_monochromatic_blue_illumination,
    "36_perceiving_coloured_objects_under_monochromatic_green_illumination": arch_36_perceiving_coloured_objects_under_monochromatic_green_illumination,
    "37_function_of_transparent_coloured_optical_filters": arch_37_function_of_transparent_coloured_optical_filters,
    "38_primary_colours_of_light_red_green_blue_additive_mixing": arch_38_primary_colours_of_light_red_green_blue_additive_mixing,
    "39_secondary_colours_of_light_cyan_magenta_yellow_formation": arch_39_secondary_colours_of_light_cyan_magenta_yellow_formation,
    "40_structure_of_human_eye_cornea_pupil_iris_lens_retina": arch_40_structure_of_human_eye_cornea_pupil_iris_lens_retina,
    "41_function_of_retina_photoreceptor_cells_rods_and_cones": arch_41_function_of_retina_photoreceptor_cells_rods_and_cones,
    "42_convex_converging_lenses_and_focal_point_properties": arch_42_convex_converging_lenses_and_focal_point_properties,
    "43_concave_diverging_lenses_and_focal_properties": arch_43_concave_diverging_lenses_and_focal_properties,
    "44_correcting_short_sightedness_myopia_using_concave_lenses": arch_44_correcting_short_sightedness_myopia_using_concave_lenses,
    "45_correcting_long_sightedness_hyperopia_using_convex_lenses": arch_45_correcting_long_sightedness_hyperopia_using_convex_lenses,
    "46_misconception_eyes_emit_light_rays_to_see_objects": arch_46_misconception_eyes_emit_light_rays_to_see_objects,
    "47_misconception_light_travels_only_a_short_distance_before_running_out": arch_47_misconception_light_travels_only_a_short_distance_before_running_out,
    "48_misconception_colours_exist_as_matter_inside_objects_in_the_dark": arch_48_misconception_colours_exist_as_matter_inside_objects_in_the_dark,
    "49_experimental_design_variables_in_light_and_optics_investigations": arch_49_experimental_design_variables_in_light_and_optics_investigations,
    "50_visible_light_comprehensive_diagnostic_evaluation": arch_50_visible_light_comprehensive_diagnostic_evaluation,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed) if seed is not None else random.Random()
    if subskill is None or subskill not in ARCHETYPE_BUILDERS:
        subskill = rng.choice(SUBSKILLS)
    builder = ARCHETYPE_BUILDERS[subskill]
    return builder(rng)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    target = str(subskill or "").strip().lower()
    chosen_sub: Optional[str] = None
    if target in ARCHETYPE_BUILDERS:
        chosen_sub = target
    else:
        for k in ARCHETYPE_BUILDERS:
            if target and (target in k.lower() or k.lower() in target):
                chosen_sub = k
                break

    for i in range(count):
        active = chosen_sub if chosen_sub else SUBSKILLS[(i + (seed or 0)) % len(SUBSKILLS)]
        builder = ARCHETYPE_BUILDERS[active]
        q = builder(rng)
        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
