"""Grade 7 Natural Sciences: Term 4 - Historical Development of Astronomy Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_astronomy_history_archetypes_01_25 import (
    arch_01_indigenous_african_astronomy_heritage,
    arch_02_xhosa_traditional_calendar_isilimela_pleiades,
    arch_03_sotho_tswana_starlore_selemela_agriculture,
    arch_04_san_bushman_starlore_milky_way_ashes,
    arch_05_san_bushman_celestial_hunters_magellanic_clouds,
    arch_06_venus_morning_evening_star_ikhwezi,
    arch_07_southern_cross_crux_and_pointers_navigation,
    arch_08_sirius_inkwenkwezi_agricultural_calendar,
    arch_09_ancient_african_observatories_adams_calendar,
    arch_10_ancient_african_observatories_nabta_playa,
    arch_11_cultural_interpretations_shooting_stars_meteors,
    arch_12_cultural_interpretations_comets_celestial_messengers,
    arch_13_geocentric_model_aristotle_ptolemy_earth_centred,
    arch_14_ptolemaic_epicycles_explaining_planetary_motion,
    arch_15_heliocentric_model_copernicus_sun_centred,
    arch_16_apparent_retrograde_motion_mars_perspective,
    arch_17_tycho_brahe_naked_eye_astronomical_measurements,
    arch_18_keplers_first_law_elliptical_orbits,
    arch_19_keplers_second_law_orbital_speeds_perihelion_aphelion,
    arch_20_keplers_third_law_orbital_period_distance_ratio,
    arch_21_invention_of_optical_telescope_hans_lippershey,
    arch_22_galileo_galilei_systematic_telescopic_observations,
    arch_23_galilean_moons_of_jupiter_revolution,
    arch_24_phases_of_venus_proving_heliocentrism,
    arch_25_lunar_craters_and_imperfection_of_celestial_bodies,
)
from .ns7_astronomy_history_archetypes_26_50 import (
    arch_26_sunspots_observation_solar_rotation,
    arch_27_saturns_rings_early_telescopic_puzzles,
    arch_28_galileos_conflict_with_inquisition_house_arrest,
    arch_29_isaac_newton_law_of_universal_gravitation,
    arch_30_newton_explaining_keplers_elliptical_orbits,
    arch_31_invention_of_reflecting_telescope_newton_mirrors,
    arch_32_refracting_telescopes_lenses_chromatic_aberration,
    arch_33_reflecting_telescopes_concave_mirrors_advantages,
    arch_34_optical_vs_radio_telescopes_comparison,
    arch_35_radio_astronomy_history_karl_jansky,
    arch_36_radio_waves_penetrating_interstellar_dust,
    arch_37_south_african_astronomy_heritage_royal_observatory,
    arch_38_sutherland_karoo_ideal_astronomical_site,
    arch_39_south_african_large_telescope_salt_specifications,
    arch_40_salt_hexagonal_primary_mirror_technology,
    arch_41_hartraao_hartbeeshoek_radio_astronomy,
    arch_42_meerkat_radio_telescope_karoo_precursor,
    arch_43_square_kilometre_array_ska_global_scientific_collaboration,
    arch_44_ska_scientific_goals_cosmic_origins_dark_ages,
    arch_45_space_telescopes_hubble_avoiding_atmospheric_distortion,
    arch_46_james_webb_space_telescope_infrared_astronomy,
    arch_47_ground_vs_space_based_observatories_tradeoffs,
    arch_48_multispectral_astronomy_visible_radio_xray,
    arch_49_astronomy_careers_and_stem_skills_south_africa,
    arch_50_astronomy_history_comprehensive_diagnostic_autopsy,
)

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_indigenous_african_astronomy_heritage": arch_01_indigenous_african_astronomy_heritage,
    "02_xhosa_traditional_calendar_isilimela_pleiades": arch_02_xhosa_traditional_calendar_isilimela_pleiades,
    "03_sotho_tswana_starlore_selemela_agriculture": arch_03_sotho_tswana_starlore_selemela_agriculture,
    "04_san_bushman_starlore_milky_way_ashes": arch_04_san_bushman_starlore_milky_way_ashes,
    "05_san_bushman_celestial_hunters_magellanic_clouds": arch_05_san_bushman_celestial_hunters_magellanic_clouds,
    "06_venus_morning_evening_star_ikhwezi": arch_06_venus_morning_evening_star_ikhwezi,
    "07_southern_cross_crux_and_pointers_navigation": arch_07_southern_cross_crux_and_pointers_navigation,
    "08_sirius_inkwenkwezi_agricultural_calendar": arch_08_sirius_inkwenkwezi_agricultural_calendar,
    "09_ancient_african_observatories_adams_calendar": arch_09_ancient_african_observatories_adams_calendar,
    "10_ancient_african_observatories_nabta_playa": arch_10_ancient_african_observatories_nabta_playa,
    "11_cultural_interpretations_shooting_stars_meteors": arch_11_cultural_interpretations_shooting_stars_meteors,
    "12_cultural_interpretations_comets_celestial_messengers": arch_12_cultural_interpretations_comets_celestial_messengers,
    "13_geocentric_model_aristotle_ptolemy_earth_centred": arch_13_geocentric_model_aristotle_ptolemy_earth_centred,
    "14_ptolemaic_epicycles_explaining_planetary_motion": arch_14_ptolemaic_epicycles_explaining_planetary_motion,
    "15_heliocentric_model_copernicus_sun_centred": arch_15_heliocentric_model_copernicus_sun_centred,
    "16_apparent_retrograde_motion_mars_perspective": arch_16_apparent_retrograde_motion_mars_perspective,
    "17_tycho_brahe_naked_eye_astronomical_measurements": arch_17_tycho_brahe_naked_eye_astronomical_measurements,
    "18_keplers_first_law_elliptical_orbits": arch_18_keplers_first_law_elliptical_orbits,
    "19_keplers_second_law_orbital_speeds_perihelion_aphelion": arch_19_keplers_second_law_orbital_speeds_perihelion_aphelion,
    "20_keplers_third_law_orbital_period_distance_ratio": arch_20_keplers_third_law_orbital_period_distance_ratio,
    "21_invention_of_optical_telescope_hans_lippershey": arch_21_invention_of_optical_telescope_hans_lippershey,
    "22_galileo_galilei_systematic_telescopic_observations": arch_22_galileo_galilei_systematic_telescopic_observations,
    "23_galilean_moons_of_jupiter_revolution": arch_23_galilean_moons_of_jupiter_revolution,
    "24_phases_of_venus_proving_heliocentrism": arch_24_phases_of_venus_proving_heliocentrism,
    "25_lunar_craters_and_imperfection_of_celestial_bodies": arch_25_lunar_craters_and_imperfection_of_celestial_bodies,
    "26_sunspots_observation_solar_rotation": arch_26_sunspots_observation_solar_rotation,
    "27_saturns_rings_early_telescopic_puzzles": arch_27_saturns_rings_early_telescopic_puzzles,
    "28_galileos_conflict_with_inquisition_house_arrest": arch_28_galileos_conflict_with_inquisition_house_arrest,
    "29_isaac_newton_law_of_universal_gravitation": arch_29_isaac_newton_law_of_universal_gravitation,
    "30_newton_explaining_keplers_elliptical_orbits": arch_30_newton_explaining_keplers_elliptical_orbits,
    "31_invention_of_reflecting_telescope_newton_mirrors": arch_31_invention_of_reflecting_telescope_newton_mirrors,
    "32_refracting_telescopes_lenses_chromatic_aberration": arch_32_refracting_telescopes_lenses_chromatic_aberration,
    "33_reflecting_telescopes_concave_mirrors_advantages": arch_33_reflecting_telescopes_concave_mirrors_advantages,
    "34_optical_vs_radio_telescopes_comparison": arch_34_optical_vs_radio_telescopes_comparison,
    "35_radio_astronomy_history_karl_jansky": arch_35_radio_astronomy_history_karl_jansky,
    "36_radio_waves_penetrating_interstellar_dust": arch_36_radio_waves_penetrating_interstellar_dust,
    "37_south_african_astronomy_heritage_royal_observatory": arch_37_south_african_astronomy_heritage_royal_observatory,
    "38_sutherland_karoo_ideal_astronomical_site": arch_38_sutherland_karoo_ideal_astronomical_site,
    "39_south_african_large_telescope_salt_specifications": arch_39_south_african_large_telescope_salt_specifications,
    "40_salt_hexagonal_primary_mirror_technology": arch_40_salt_hexagonal_primary_mirror_technology,
    "41_hartraao_hartbeeshoek_radio_astronomy": arch_41_hartraao_hartbeeshoek_radio_astronomy,
    "42_meerkat_radio_telescope_karoo_precursor": arch_42_meerkat_radio_telescope_karoo_precursor,
    "43_square_kilometre_array_ska_global_scientific_collaboration": arch_43_square_kilometre_array_ska_global_scientific_collaboration,
    "44_ska_scientific_goals_cosmic_origins_dark_ages": arch_44_ska_scientific_goals_cosmic_origins_dark_ages,
    "45_space_telescopes_hubble_avoiding_atmospheric_distortion": arch_45_space_telescopes_hubble_avoiding_atmospheric_distortion,
    "46_james_webb_space_telescope_infrared_astronomy": arch_46_james_webb_space_telescope_infrared_astronomy,
    "47_ground_vs_space_based_observatories_tradeoffs": arch_47_ground_vs_space_based_observatories_tradeoffs,
    "48_multispectral_astronomy_visible_radio_xray": arch_48_multispectral_astronomy_visible_radio_xray,
    "49_astronomy_careers_and_stem_skills_south_africa": arch_49_astronomy_careers_and_stem_skills_south_africa,
    "50_astronomy_history_comprehensive_diagnostic_autopsy": arch_50_astronomy_history_comprehensive_diagnostic_autopsy,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Historical Development of Astronomy.

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
        q.setdefault("topic", "Historical development of astronomy")
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
