"""Grade 7 Mathematics - Geometry of 3D Objects & Geometric Nets Generator (50 Semantic Archetypes).
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Geometry of 3D objects.md
Focus: Polyhedra vs curved solids, prisms vs pyramids, Platonic solids, properties (F, V, E), Euler's formula, general n-gon formulas, valid/invalid nets with SVGs, surface area from nets, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .geometric_nets_3d_archetypes_01_25 import (
    arch_01_classify_polyhedron_vs_curved_solid,
    arch_02_classify_prism_vs_pyramid_distinction,
    arch_03_cube_net,
    arch_04_rectangular_prism_faces_vertices_edges,
    arch_05_triangular_prism_faces_vertices_edges,
    arch_06_square_pyramid_faces_vertices_edges,
    arch_07_tetrahedron_faces_vertices_edges,
    arch_08_pentagonal_prism_faces_vertices_edges,
    arch_09_hexagonal_prism_faces_vertices_edges,
    arch_10_pentagonal_pyramid_faces_vertices_edges,
    arch_11_hexagonal_pyramid_faces_vertices_edges,
    arch_12_octahedron_platonic_solid_properties,
    arch_13_dodecahedron_platonic_solid_properties,
    arch_14_icosahedron_platonic_solid_properties,
    arch_15_cylinder_properties_curved_surfaces,
    arch_16_cone_properties_curved_surfaces,
    arch_17_sphere_properties_curved_surfaces,
    arch_18_eulers_formula_calculation,
    arch_19_eulers_formula_verify_triangular_prism,
    arch_20_eulers_formula_verify_square_pyramid,
    arch_21_eulers_formula_find_edges,
    arch_22_eulers_formula_find_vertices,
    arch_23_eulers_formula_find_faces,
    arch_24_eulers_formula_applicability_check,
    arch_25_general_prism_formula_for_n_gon,
)
from .geometric_nets_3d_archetypes_26_50 import (
    arch_26_general_pyramid_formula_for_n_gon,
    arch_27_valid_cube_net_latin_cross_svg,
    arch_28_valid_cube_net_step_pattern_svg,
    arch_29_invalid_cube_net_overlapping_faces_svg,
    arch_30_invalid_cube_net_five_in_a_row_svg,
    arch_31_opposite_faces_in_cube_net,
    arch_32_net_of_rectangular_prism_matching,
    arch_33_net_of_triangular_prism_matching,
    arch_34_net_of_square_pyramid_matching,
    arch_35_net_of_tetrahedron_matching,
    arch_36_cylinder_net_surface_area,
    arch_37_net_of_cone_matching,
    arch_38_surface_area_from_net,
    arch_39_surface_area_from_net_square_pyramid,
    arch_40_surface_area_from_net_cylinder_numeric,
    arch_41_platonic_solids_definition,
    arch_42_identifying_3d_object_from_face_description,
    arch_43_identifying_3d_object_from_two_hexagonal_bases,
    arch_44_common_misconception_confusing_vertex_and_apex,
    arch_45_common_misconception_counting_cylinder_as_polyhedron,
    arch_46_common_misconception_cube_net_six_squares_assumption,
    arch_47_right_prism_vs_oblique_prism_concept,
    arch_48_cross_sections_of_3d_solids,
    arch_49_building_3d_nets_tabs_and_assembly,
    arch_50_geometric_net_identification,
)

ARCHETYPE_BUILDERS = {
    "01_classify_polyhedron_vs_curved_solid": arch_01_classify_polyhedron_vs_curved_solid,
    "02_classify_prism_vs_pyramid_distinction": arch_02_classify_prism_vs_pyramid_distinction,
    "03_cube_net": arch_03_cube_net,
    "04_rectangular_prism_faces_vertices_edges": arch_04_rectangular_prism_faces_vertices_edges,
    "05_triangular_prism_faces_vertices_edges": arch_05_triangular_prism_faces_vertices_edges,
    "06_square_pyramid_faces_vertices_edges": arch_06_square_pyramid_faces_vertices_edges,
    "07_tetrahedron_faces_vertices_edges": arch_07_tetrahedron_faces_vertices_edges,
    "08_pentagonal_prism_faces_vertices_edges": arch_08_pentagonal_prism_faces_vertices_edges,
    "09_hexagonal_prism_faces_vertices_edges": arch_09_hexagonal_prism_faces_vertices_edges,
    "10_pentagonal_pyramid_faces_vertices_edges": arch_10_pentagonal_pyramid_faces_vertices_edges,
    "11_hexagonal_pyramid_faces_vertices_edges": arch_11_hexagonal_pyramid_faces_vertices_edges,
    "12_octahedron_platonic_solid_properties": arch_12_octahedron_platonic_solid_properties,
    "13_dodecahedron_platonic_solid_properties": arch_13_dodecahedron_platonic_solid_properties,
    "14_icosahedron_platonic_solid_properties": arch_14_icosahedron_platonic_solid_properties,
    "15_cylinder_properties_curved_surfaces": arch_15_cylinder_properties_curved_surfaces,
    "16_cone_properties_curved_surfaces": arch_16_cone_properties_curved_surfaces,
    "17_sphere_properties_curved_surfaces": arch_17_sphere_properties_curved_surfaces,
    "18_eulers_formula_calculation": arch_18_eulers_formula_calculation,
    "19_eulers_formula_verify_triangular_prism": arch_19_eulers_formula_verify_triangular_prism,
    "20_eulers_formula_verify_square_pyramid": arch_20_eulers_formula_verify_square_pyramid,
    "21_eulers_formula_find_edges": arch_21_eulers_formula_find_edges,
    "22_eulers_formula_find_vertices": arch_22_eulers_formula_find_vertices,
    "23_eulers_formula_find_faces": arch_23_eulers_formula_find_faces,
    "24_eulers_formula_applicability_check": arch_24_eulers_formula_applicability_check,
    "25_general_prism_formula_for_n_gon": arch_25_general_prism_formula_for_n_gon,
    "26_general_pyramid_formula_for_n_gon": arch_26_general_pyramid_formula_for_n_gon,
    "27_valid_cube_net_latin_cross_svg": arch_27_valid_cube_net_latin_cross_svg,
    "28_valid_cube_net_step_pattern_svg": arch_28_valid_cube_net_step_pattern_svg,
    "29_invalid_cube_net_overlapping_faces_svg": arch_29_invalid_cube_net_overlapping_faces_svg,
    "30_invalid_cube_net_five_in_a_row_svg": arch_30_invalid_cube_net_five_in_a_row_svg,
    "31_opposite_faces_in_cube_net": arch_31_opposite_faces_in_cube_net,
    "32_net_of_rectangular_prism_matching": arch_32_net_of_rectangular_prism_matching,
    "33_net_of_triangular_prism_matching": arch_33_net_of_triangular_prism_matching,
    "34_net_of_square_pyramid_matching": arch_34_net_of_square_pyramid_matching,
    "35_net_of_tetrahedron_matching": arch_35_net_of_tetrahedron_matching,
    "36_cylinder_net_surface_area": arch_36_cylinder_net_surface_area,
    "37_net_of_cone_matching": arch_37_net_of_cone_matching,
    "38_surface_area_from_net": arch_38_surface_area_from_net,
    "39_surface_area_from_net_square_pyramid": arch_39_surface_area_from_net_square_pyramid,
    "40_surface_area_from_net_cylinder_numeric": arch_40_surface_area_from_net_cylinder_numeric,
    "41_platonic_solids_definition": arch_41_platonic_solids_definition,
    "42_identifying_3d_object_from_face_description": arch_42_identifying_3d_object_from_face_description,
    "43_identifying_3d_object_from_two_hexagonal_bases": arch_43_identifying_3d_object_from_two_hexagonal_bases,
    "44_common_misconception_confusing_vertex_and_apex": arch_44_common_misconception_confusing_vertex_and_apex,
    "45_common_misconception_counting_cylinder_as_polyhedron": arch_45_common_misconception_counting_cylinder_as_polyhedron,
    "46_common_misconception_cube_net_six_squares_assumption": arch_46_common_misconception_cube_net_six_squares_assumption,
    "47_right_prism_vs_oblique_prism_concept": arch_47_right_prism_vs_oblique_prism_concept,
    "48_cross_sections_of_3d_solids": arch_48_cross_sections_of_3d_solids,
    "49_building_3d_nets_tabs_and_assembly": arch_49_building_3d_nets_tabs_and_assembly,
    "50_geometric_net_identification": arch_50_geometric_net_identification,
}

SUBSKILLS = list(ARCHETYPE_BUILDERS.keys())


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
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []
    target_sub = str(subskill or "").strip().lower()

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        matched = None
        for k in ARCHETYPE_BUILDERS:
            if target_sub == k.lower() or target_sub in k.lower():
                matched = k
                break
        for _ in range(count):
            if matched:
                questions.append(ARCHETYPE_BUILDERS[matched](rng))
            else:
                s = rng.choice(SUBSKILLS)
                questions.append(ARCHETYPE_BUILDERS[s](rng))
        return questions

    for i in range(count):
        s = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(ARCHETYPE_BUILDERS[s](rng))

    return questions
