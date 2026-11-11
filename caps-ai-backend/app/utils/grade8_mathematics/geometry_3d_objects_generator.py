"""Grade 8 Mathematics — Geometry of 3D Objects Generator.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/02. Geometry of 3D objects.md

Expanded to 50 distinct semantic archetypes covering:
  - Polyhedra classification vs curved solids (cylinders, spheres, cones).
  - Prisms: triangular, rectangular/cuboid, cube, pentagonal, hexagonal, octagonal, general n-gon formulas.
  - Pyramids: tetrahedron, square, rectangular, pentagonal, hexagonal, general n-gon formulas, apex, prism vs pyramid.
  - Euler's formula: F + V - E = 2, verification, solving for F, V, or E, applicability, algebraic proofs.
  - Platonic solids: definition, regular tetrahedron, cube, octahedron, dodecahedron, icosahedron, why only 5, duals, real-world.
  - Nets of 3D objects: Latin cross, T-cross, invalid nets, opposite faces, triangular prism, square pyramid, cylinder/cone, truncated polyhedra.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_3d_objects_archetypes_01_25 import (
    arch_01_classify_polyhedron_vs_curved_solids,
    arch_02_identify_faces_vertices_edges_definitions,
    arch_03_triangular_prism_properties_faces_vertices_edges,
    arch_04_rectangular_prism_cuboid_faces_vertices_edges,
    arch_05_cube_properties_all_faces_congruent_squares,
    arch_06_pentagonal_prism_faces_vertices_edges,
    arch_07_hexagonal_prism_faces_vertices_edges,
    arch_08_octagonal_prism_faces_vertices_edges,
    arch_09_general_prism_algebraic_formulas_n_gon,
    arch_10_prism_cross_section_parallel_to_base,
    arch_11_triangular_pyramid_tetrahedron_faces_vertices_edges,
    arch_12_square_based_pyramid_faces_vertices_edges,
    arch_13_rectangular_pyramid_faces_vertices_edges,
    arch_14_pentagonal_pyramid_faces_vertices_edges,
    arch_15_hexagonal_pyramid_faces_vertices_edges,
    arch_16_general_pyramid_algebraic_formulas_n_gon,
    arch_17_apex_of_pyramid_definition_and_properties,
    arch_18_compare_prism_vs_pyramid_properties,
    arch_19_right_pyramid_vs_oblique_pyramid_concept,
    arch_20_pyramid_cross_section_parallel_to_base,
    arch_21_eulers_formula_statement_and_variables,
    arch_22_eulers_formula_verify_cube_and_cuboid,
    arch_23_eulers_formula_verify_triangular_prism,
    arch_24_eulers_formula_verify_square_pyramid,
    arch_25_eulers_formula_find_faces_given_vertices_and_edges,
)
from .geometry_3d_objects_archetypes_26_50 import (
    arch_26_eulers_formula_find_vertices_given_faces_and_edges,
    arch_27_eulers_formula_find_edges_given_faces_and_vertices,
    arch_28_eulers_formula_non_polyhedra_inapplicability,
    arch_29_eulers_formula_algebraic_proof_n_gon_prism,
    arch_30_eulers_formula_algebraic_proof_n_gon_pyramid,
    arch_31_platonic_solids_definition_and_criteria,
    arch_32_platonic_solid_regular_tetrahedron,
    arch_33_platonic_solid_cube_hexahedron,
    arch_34_platonic_solid_regular_octahedron,
    arch_35_platonic_solid_regular_dodecahedron,
    arch_36_platonic_solid_regular_icosahedron,
    arch_37_platonic_solids_why_only_five_exist,
    arch_38_platonic_solids_dual_polyhedra_pairs,
    arch_39_platonic_solids_euler_verification_table,
    arch_40_platonic_solids_real_world_examples,
    arch_41_valid_cube_net_latin_cross_svg,
    arch_42_valid_cube_net_t_cross_pattern_svg,
    arch_43_invalid_cube_net_overlapping_faces_svg,
    arch_44_cube_net_opposite_faces_identification,
    arch_45_net_of_triangular_prism_identification_svg,
    arch_46_net_of_square_pyramid_identification_svg,
    arch_47_net_of_cylinder_components,
    arch_48_net_of_cone_components,
    arch_49_truncated_polyhedra_cutting_corners_of_cube,
    arch_50_3d_spatial_reasoning_packaging_box_construction,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_classify_polyhedron_vs_curved_solids": arch_01_classify_polyhedron_vs_curved_solids,
    "02_identify_faces_vertices_edges_definitions": arch_02_identify_faces_vertices_edges_definitions,
    "03_triangular_prism_properties_faces_vertices_edges": arch_03_triangular_prism_properties_faces_vertices_edges,
    "04_rectangular_prism_cuboid_faces_vertices_edges": arch_04_rectangular_prism_cuboid_faces_vertices_edges,
    "05_cube_properties_all_faces_congruent_squares": arch_05_cube_properties_all_faces_congruent_squares,
    "06_pentagonal_prism_faces_vertices_edges": arch_06_pentagonal_prism_faces_vertices_edges,
    "07_hexagonal_prism_faces_vertices_edges": arch_07_hexagonal_prism_faces_vertices_edges,
    "08_octagonal_prism_faces_vertices_edges": arch_08_octagonal_prism_faces_vertices_edges,
    "09_general_prism_algebraic_formulas_n_gon": arch_09_general_prism_algebraic_formulas_n_gon,
    "10_prism_cross_section_parallel_to_base": arch_10_prism_cross_section_parallel_to_base,
    "11_triangular_pyramid_tetrahedron_faces_vertices_edges": arch_11_triangular_pyramid_tetrahedron_faces_vertices_edges,
    "12_square_based_pyramid_faces_vertices_edges": arch_12_square_based_pyramid_faces_vertices_edges,
    "13_rectangular_pyramid_faces_vertices_edges": arch_13_rectangular_pyramid_faces_vertices_edges,
    "14_pentagonal_pyramid_faces_vertices_edges": arch_14_pentagonal_pyramid_faces_vertices_edges,
    "15_hexagonal_pyramid_faces_vertices_edges": arch_15_hexagonal_pyramid_faces_vertices_edges,
    "16_general_pyramid_algebraic_formulas_n_gon": arch_16_general_pyramid_algebraic_formulas_n_gon,
    "17_apex_of_pyramid_definition_and_properties": arch_17_apex_of_pyramid_definition_and_properties,
    "18_compare_prism_vs_pyramid_properties": arch_18_compare_prism_vs_pyramid_properties,
    "19_right_pyramid_vs_oblique_pyramid_concept": arch_19_right_pyramid_vs_oblique_pyramid_concept,
    "20_pyramid_cross_section_parallel_to_base": arch_20_pyramid_cross_section_parallel_to_base,
    "21_eulers_formula_statement_and_variables": arch_21_eulers_formula_statement_and_variables,
    "22_eulers_formula_verify_cube_and_cuboid": arch_22_eulers_formula_verify_cube_and_cuboid,
    "23_eulers_formula_verify_triangular_prism": arch_23_eulers_formula_verify_triangular_prism,
    "24_eulers_formula_verify_square_pyramid": arch_24_eulers_formula_verify_square_pyramid,
    "25_eulers_formula_find_faces_given_vertices_and_edges": arch_25_eulers_formula_find_faces_given_vertices_and_edges,
    "26_eulers_formula_find_vertices_given_faces_and_edges": arch_26_eulers_formula_find_vertices_given_faces_and_edges,
    "27_eulers_formula_find_edges_given_faces_and_vertices": arch_27_eulers_formula_find_edges_given_faces_and_vertices,
    "28_eulers_formula_non_polyhedra_inapplicability": arch_28_eulers_formula_non_polyhedra_inapplicability,
    "29_eulers_formula_algebraic_proof_n_gon_prism": arch_29_eulers_formula_algebraic_proof_n_gon_prism,
    "30_eulers_formula_algebraic_proof_n_gon_pyramid": arch_30_eulers_formula_algebraic_proof_n_gon_pyramid,
    "31_platonic_solids_definition_and_criteria": arch_31_platonic_solids_definition_and_criteria,
    "32_platonic_solid_regular_tetrahedron": arch_32_platonic_solid_regular_tetrahedron,
    "33_platonic_solid_cube_hexahedron": arch_33_platonic_solid_cube_hexahedron,
    "34_platonic_solid_regular_octahedron": arch_34_platonic_solid_regular_octahedron,
    "35_platonic_solid_regular_dodecahedron": arch_35_platonic_solid_regular_dodecahedron,
    "36_platonic_solid_regular_icosahedron": arch_36_platonic_solid_regular_icosahedron,
    "37_platonic_solids_why_only_five_exist": arch_37_platonic_solids_why_only_five_exist,
    "38_platonic_solids_dual_polyhedra_pairs": arch_38_platonic_solids_dual_polyhedra_pairs,
    "39_platonic_solids_euler_verification_table": arch_39_platonic_solids_euler_verification_table,
    "40_platonic_solids_real_world_examples": arch_40_platonic_solids_real_world_examples,
    "41_valid_cube_net_latin_cross_svg": arch_41_valid_cube_net_latin_cross_svg,
    "42_valid_cube_net_t_cross_pattern_svg": arch_42_valid_cube_net_t_cross_pattern_svg,
    "43_invalid_cube_net_overlapping_faces_svg": arch_43_invalid_cube_net_overlapping_faces_svg,
    "44_cube_net_opposite_faces_identification": arch_44_cube_net_opposite_faces_identification,
    "45_net_of_triangular_prism_identification_svg": arch_45_net_of_triangular_prism_identification_svg,
    "46_net_of_square_pyramid_identification_svg": arch_46_net_of_square_pyramid_identification_svg,
    "47_net_of_cylinder_components": arch_47_net_of_cylinder_components,
    "48_net_of_cone_components": arch_48_net_of_cone_components,
    "49_truncated_polyhedra_cutting_corners_of_cube": arch_49_truncated_polyhedra_cutting_corners_of_cube,
    "50_3d_spatial_reasoning_packaging_box_construction": arch_50_3d_spatial_reasoning_packaging_box_construction,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())


def generate_grade8_geometry_of_3d_objects_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    target_subskill = subskill
    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        if mode and mode.startswith("elementary_"):
            candidate = mode[len("elementary_"):]
            if candidate in ARCHETYPE_MAP:
                target_subskill = candidate
            else:
                for k in ARCHETYPE_MAP:
                    if candidate in k:
                        target_subskill = k
                        break

    if not target_subskill or target_subskill not in ARCHETYPE_MAP:
        target_subskill = rng.choice(SUBSKILLS)

    generator_fn = ARCHETYPE_MAP[target_subskill]
    q_data = generator_fn(rng)

    q_data["subject"] = "mathematics"
    q_data["grade"] = "grade-8"
    q_data["topic"] = "Geometry of 3D objects"
    q_data["term"] = 3
    q_data["caps_weight_percent"] = 9
    q_data["suggested_duration_mins"] = 3
    q_data["difficulty"] = difficulty
    q_data["mode"] = mode
    q_data["subskill"] = target_subskill

    if "marking_schema" not in q_data:
        m = q_data.get("marks", 2)
        q_data["marking_schema"] = {
            "total_marks": m,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of 3D solid properties or formula setup", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate calculation or property deduction", "marks": m - 1, "editable": True},
            ],
            "deductions": [{"rule": "incorrect_reason_or_count", "penalty": 1}],
            "carry_forward_rule": "consequential_accuracy",
        }

    return q_data


generate = generate_grade8_geometry_of_3d_objects_question
generate_grade8_3d_objects_question = generate_grade8_geometry_of_3d_objects_question
