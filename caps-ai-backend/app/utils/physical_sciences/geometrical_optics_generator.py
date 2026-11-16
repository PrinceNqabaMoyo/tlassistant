"""Physical Sciences Grade 11: Geometrical Optics & 2D and 3D Wavefronts Generator.
Focus: Reflection, Refraction, Snell's Law, Critical Angles, Total Internal Reflection (TIR),
Lenses, Optical Instruments, Wavefronts, Huygens' Principle & Single-Slit Diffraction.

Complies strictly with the 6-Pillar Generator Contract:
- Multi-grade vertical strand (Gr8 NS, Gr11 PS)
- 50 semantic subskills with 0 shims
- Seed-deterministic via random.Random(seed)
- South African comma decimal convention ({{,}})
- Zero curriculum trademarks (CAPS/IEB/DBE/NSC)
- Valid DiagramRenderer inline_svg specifications with dynamic seed variation
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.physical_sciences.geometrical_optics_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.physical_sciences.geometrical_optics_archetypes_26_50 import (
    BUILDERS_26_50,
)

ALL_BUILDERS: List[Callable[[random.Random, Optional[int]], Dict[str, Any]]] = (
    BUILDERS_01_25 + BUILDERS_26_50
)

SUBSKILLS: List[str] = [
    # Subskills 01–25: Ray Optics, Refraction & Snell's Law, Prisms & TIR
    "01_rectilinear_propagation_and_shadow_formation",
    "02_law_of_reflection_plane_mirror",
    "03_refractive_index_and_wave_speed",
    "04_wavelength_change_in_refraction_frequency_constant",
    "05_optical_density_and_ray_bending_towards_away_normal",
    "06_snells_law_solve_angle_of_refraction",
    "07_snells_law_solve_angle_of_incidence",
    "08_snells_law_solve_refractive_index_of_unknown_medium",
    "09_rectangular_glass_block_lateral_displacement_parallel_emergence",
    "10_apparent_depth_real_depth_refraction",
    "11_critical_angle_definition_and_formula",
    "12_critical_angle_calculation_dense_to_air",
    "13_critical_angle_calculation_between_two_dense_media",
    "14_total_internal_reflection_two_conditions_evaluation",
    "15_tir_in_45_degree_right_angle_prisms_periscope",
    "16_tir_in_porro_prisms_binoculars",
    "17_optical_fibre_core_cladding_acceptance_angle",
    "18_triangular_prism_minimum_deviation_angle",
    "19_dispersion_of_white_light_prism_refractive_index_vs_wavelength",
    "20_atmospheric_refraction_mirages_and_delayed_sunset",
    "21_diamond_brilliance_critical_angle_cut_geometry",
    "22_snells_law_graphical_analysis_sin_theta_i_vs_sin_theta_r",
    "23_multi_layer_parallel_refraction_air_water_glass",
    "24_semi_circular_glass_block_refraction_at_curved_vs_flat_surface",
    "25_geometrical_optics_diagnostic_misconception_autopsy_part1",
    # Subskills 26–50: Lenses, Optical Instruments, Wavefronts & Single-Slit Diffraction
    "26_thin_converging_lens_focal_point_and_principal_rays",
    "27_thin_diverging_lens_virtual_focus_and_ray_diagram",
    "28_lens_equation_converging_real_image",
    "29_lens_equation_converging_virtual_image_magnifying_glass",
    "30_lens_equation_diverging_virtual_diminished_image",
    "31_linear_magnification_and_image_height_calculation",
    "32_compound_microscope_or_refracting_telescope_principles",
    "33_wavefront_definition_and_ray_perpendicularity",
    "34_circular_vs_plane_wavefronts_propagation",
    "35_huygens_principle_statement_and_secondary_wavelets",
    "36_huygens_construction_proving_law_of_reflection",
    "37_huygens_construction_proving_snells_law_of_refraction",
    "38_diffraction_definition_and_wave_nature_evidence",
    "39_diffraction_qualitative_aperture_size_vs_wavelength_ratio",
    "40_single_slit_diffraction_pattern_central_broad_maximum",
    "41_single_slit_diffraction_first_minimum_condition_formula",
    "42_single_slit_diffraction_angular_width_of_central_maximum",
    "43_single_slit_effect_of_decreasing_increasing_slit_width",
    "44_single_slit_effect_of_changing_wavelength_red_vs_blue_light",
    "45_single_slit_white_light_diffraction_colored_fringes",
    "46_single_slit_intensity_distribution_profile_analysis",
    "47_diffraction_of_water_waves_in_ripple_tank",
    "48_sound_diffraction_around_corners_vs_light_diffraction",
    "49_capstone_optics_wavefront_synthesis_multi_tier",
    "50_wavefronts_diffraction_diagnostic_misconception_autopsy_part2",
]

ARCHETYPES = SUBSKILLS
ORDERED_SUBSKILLS = SUBSKILLS
AVAILABLE_SUBSKILLS = SUBSKILLS

BUILDERS: Dict[str, Callable[[random.Random, Optional[int]], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, ALL_BUILDERS)
}

LEGACY_ALIASES: Dict[str, str] = {
    "snell_optics": "06_snells_law_solve_angle_of_refraction",
    "thin_lens": "28_lens_equation_converging_real_image",
    "visible_light": "03_refractive_index_and_wave_speed",
    "spectrum": "19_dispersion_of_white_light_prism_refractive_index_vs_wavelength",
    "reflection_gr8": "02_law_of_reflection_plane_mirror",
    "lenses": "26_thin_converging_lens_focal_point_and_principal_rays",
    "ray_tracing": "26_thin_converging_lens_focal_point_and_principal_rays",
    "refraction": "05_optical_density_and_ray_bending_towards_away_normal",
    "critical_angle": "12_critical_angle_calculation_dense_to_air",
    "tir": "14_total_internal_reflection_two_conditions_evaluation",
    "dispersion": "19_dispersion_of_white_light_prism_refractive_index_vs_wavelength",
    "diffraction": "38_diffraction_definition_and_wave_nature_evidence",
    "wavefronts": "33_wavefront_definition_and_ray_perpendicularity",
    "huygens": "35_huygens_principle_statement_and_secondary_wavelets",
    "single_slit": "40_single_slit_diffraction_pattern_central_broad_maximum",
}


def get_subskills() -> List[str]:
    """Return all 50 available semantic subskills."""
    return list(SUBSKILLS)


def generate_question(
    subskill: str = "mixed",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic question for a requested subskill."""
    rng = random.Random(seed) if seed is not None else random.Random()

    resolved_subskill = subskill
    if resolved_subskill in LEGACY_ALIASES:
        resolved_subskill = LEGACY_ALIASES[resolved_subskill]

    if resolved_subskill in BUILDERS:
        builder = BUILDERS[resolved_subskill]
    elif resolved_subskill == "mixed" or not resolved_subskill:
        builder = rng.choice(ALL_BUILDERS)
    else:
        # Match by partial string or integer prefix
        matched = [s for s in SUBSKILLS if resolved_subskill.lower() in s.lower()]
        builder = BUILDERS[matched[0]] if matched else rng.choice(ALL_BUILDERS)

    return builder(rng, seed)


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator conforming to platform contract."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = rng.randint(1, 1_000_000_000)
        q = generate_question(subskill=subskill, seed=sub_seed, **kwargs)
        questions.append(q)

    return questions
