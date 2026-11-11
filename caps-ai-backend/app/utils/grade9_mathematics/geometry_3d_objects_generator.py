"""Grade 9 Mathematics - Geometry of 3D Objects Generator (50 Semantic Archetypes).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/01. Geometry of 3D objects.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_3d_objects_archetypes_01_25 import (
    arch_01_classify_polyhedron_vs_non_polyhedron,
    arch_02_identify_faces_vertices_edges_cube,
    arch_03_identify_faces_vertices_edges_triangular_prism,
    arch_04_identify_faces_vertices_edges_square_pyramid,
    arch_05_identify_faces_vertices_edges_tetrahedron,
    arch_06_identify_faces_vertices_edges_pentagonal_prism,
    arch_07_identify_faces_vertices_edges_hexagonal_prism,
    arch_08_identify_faces_vertices_edges_pentagonal_pyramid,
    arch_09_identify_faces_vertices_edges_hexagonal_pyramid,
    arch_10_general_formula_n_gonal_prism,
    arch_11_general_formula_n_gonal_pyramid,
    arch_12_distinguish_prism_vs_pyramid,
    arch_13_platonic_solids_identification,
    arch_14_platonic_solid_face_shapes,
    arch_15_platonic_solids_faces_count,
    arch_16_platonic_solid_vertices_edges,
    arch_17_platonic_solids_vertex_angle_sum_proof,
    arch_18_euler_formula_verification_prisms,
    arch_19_euler_formula_verification_pyramids,
    arch_20_euler_formula_verification_platonic_solids,
    arch_21_euler_formula_solve_edges,
    arch_22_euler_formula_solve_vertices,
    arch_23_euler_formula_solve_faces,
    arch_24_curved_solids_cylinder_properties,
    arch_25_curved_solids_cone_sphere_properties,
)
from .geometry_3d_objects_archetypes_26_50 import (
    arch_26_cube_net_validity_hexomino,
    arch_27_cube_net_opposite_faces,
    arch_28_cube_net_standard_die_dots,
    arch_29_rectangular_prism_net,
    arch_30_triangular_prism_net,
    arch_31_square_pyramid_net,
    arch_32_tetrahedron_net,
    arch_33_cylinder_net_components,
    arch_34_cylinder_net_rectangle_dimensions,
    arch_35_cone_net_components,
    arch_36_cross_section_cube_horizontal_vertical,
    arch_37_cross_section_cube_diagonal,
    arch_38_cross_section_cylinder,
    arch_39_cross_section_cone,
    arch_40_cross_section_square_pyramid,
    arch_41_cross_section_sphere,
    arch_42_right_vs_oblique_prisms,
    arch_43_right_vs_oblique_pyramids,
    arch_44_truncated_pyramid_frustum,
    arch_45_truncated_cube_faces_vertices_edges,
    arch_46_composite_solid_silo_components,
    arch_47_composite_solid_tent_house_components,
    arch_48_count_faces_composite_joined_solids,
    arch_49_spatial_reasoning_identify_solid_from_views,
    arch_50_3d_geometry_capstone_synthesis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random, int], Dict[str, Any]]] = {
    "01_classify_polyhedron_vs_non_polyhedron": arch_01_classify_polyhedron_vs_non_polyhedron,
    "02_identify_faces_vertices_edges_cube": arch_02_identify_faces_vertices_edges_cube,
    "03_identify_faces_vertices_edges_triangular_prism": arch_03_identify_faces_vertices_edges_triangular_prism,
    "04_identify_faces_vertices_edges_square_pyramid": arch_04_identify_faces_vertices_edges_square_pyramid,
    "05_identify_faces_vertices_edges_tetrahedron": arch_05_identify_faces_vertices_edges_tetrahedron,
    "06_identify_faces_vertices_edges_pentagonal_prism": arch_06_identify_faces_vertices_edges_pentagonal_prism,
    "07_identify_faces_vertices_edges_hexagonal_prism": arch_07_identify_faces_vertices_edges_hexagonal_prism,
    "08_identify_faces_vertices_edges_pentagonal_pyramid": arch_08_identify_faces_vertices_edges_pentagonal_pyramid,
    "09_identify_faces_vertices_edges_hexagonal_pyramid": arch_09_identify_faces_vertices_edges_hexagonal_pyramid,
    "10_general_formula_n_gonal_prism": arch_10_general_formula_n_gonal_prism,
    "11_general_formula_n_gonal_pyramid": arch_11_general_formula_n_gonal_pyramid,
    "12_distinguish_prism_vs_pyramid": arch_12_distinguish_prism_vs_pyramid,
    "13_platonic_solids_identification": arch_13_platonic_solids_identification,
    "14_platonic_solid_face_shapes": arch_14_platonic_solid_face_shapes,
    "15_platonic_solids_faces_count": arch_15_platonic_solids_faces_count,
    "16_platonic_solid_vertices_edges": arch_16_platonic_solid_vertices_edges,
    "17_platonic_solids_vertex_angle_sum_proof": arch_17_platonic_solids_vertex_angle_sum_proof,
    "18_euler_formula_verification_prisms": arch_18_euler_formula_verification_prisms,
    "19_euler_formula_verification_pyramids": arch_19_euler_formula_verification_pyramids,
    "20_euler_formula_verification_platonic_solids": arch_20_euler_formula_verification_platonic_solids,
    "21_euler_formula_solve_edges": arch_21_euler_formula_solve_edges,
    "22_euler_formula_solve_vertices": arch_22_euler_formula_solve_vertices,
    "23_euler_formula_solve_faces": arch_23_euler_formula_solve_faces,
    "24_curved_solids_cylinder_properties": arch_24_curved_solids_cylinder_properties,
    "25_curved_solids_cone_sphere_properties": arch_25_curved_solids_cone_sphere_properties,
    "26_cube_net_validity_hexomino": arch_26_cube_net_validity_hexomino,
    "27_cube_net_opposite_faces": arch_27_cube_net_opposite_faces,
    "28_cube_net_standard_die_dots": arch_28_cube_net_standard_die_dots,
    "29_rectangular_prism_net": arch_29_rectangular_prism_net,
    "30_triangular_prism_net": arch_30_triangular_prism_net,
    "31_square_pyramid_net": arch_31_square_pyramid_net,
    "32_tetrahedron_net": arch_32_tetrahedron_net,
    "33_cylinder_net_components": arch_33_cylinder_net_components,
    "34_cylinder_net_rectangle_dimensions": arch_34_cylinder_net_rectangle_dimensions,
    "35_cone_net_components": arch_35_cone_net_components,
    "36_cross_section_cube_horizontal_vertical": arch_36_cross_section_cube_horizontal_vertical,
    "37_cross_section_cube_diagonal": arch_37_cross_section_cube_diagonal,
    "38_cross_section_cylinder": arch_38_cross_section_cylinder,
    "39_cross_section_cone": arch_39_cross_section_cone,
    "40_cross_section_square_pyramid": arch_40_cross_section_square_pyramid,
    "41_cross_section_sphere": arch_41_cross_section_sphere,
    "42_right_vs_oblique_prisms": arch_42_right_vs_oblique_prisms,
    "43_right_vs_oblique_pyramids": arch_43_right_vs_oblique_pyramids,
    "44_truncated_pyramid_frustum": arch_44_truncated_pyramid_frustum,
    "45_truncated_cube_faces_vertices_edges": arch_45_truncated_cube_faces_vertices_edges,
    "46_composite_solid_silo_components": arch_46_composite_solid_silo_components,
    "47_composite_solid_tent_house_components": arch_47_composite_solid_tent_house_components,
    "48_count_faces_composite_joined_solids": arch_48_count_faces_composite_joined_solids,
    "49_spatial_reasoning_identify_solid_from_views": arch_49_spatial_reasoning_identify_solid_from_views,
    "50_3d_geometry_capstone_synthesis": arch_50_3d_geometry_capstone_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
SUBSKILLS_TUPLES = [(k, k.replace("_", " ").title()) for k in SUBSKILLS]


def generate_grade9_geometry_3d_objects_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single Grade 9 Geometry of 3D Objects question."""
    if seed is None:
        seed = random.randint(1, 1_000_000_000)
    rng = random.Random(seed)

    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    else:
        chosen_subskill = rng.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(rng, seed)

    # Attach CAPS metadata
    q["seed"] = seed
    q["grade"] = 9
    q["term"] = 4
    q["subject"] = "Mathematics"
    q["topic"] = "Geometry of 3D objects"
    q["topic_slug"] = "grade9_math_geometry_of_3d_objects"
    q["subskill"] = chosen_subskill

    # Synchronize prompt fields
    if "question_text" in q and "prompt" not in q:
        q["prompt"] = q["question_text"]
    elif "prompt" in q and "question_text" not in q:
        q["question_text"] = q["prompt"]

    # Sync answer aliases
    if "correct_answer" in q:
        q["correct_value"] = q["correct_answer"]
        q["expected_answer"] = q["correct_answer"]
    elif "correct_value" in q:
        q["correct_answer"] = q["correct_value"]
        q["expected_answer"] = q["correct_value"]

    # Worked solution from hints or schema
    hints = q.get("hints", [])
    if hints and "sample_answer" not in q:
        q["sample_answer"] = hints[-1]
    if hints and "worked_solution" not in q:
        q["worked_solution"] = "\n".join(hints)

    schema = q.get("marking_schema")
    if isinstance(schema, list) and "marks" not in q:
        q["marks"] = sum(p.get("marks", 1) for p in schema if isinstance(p, dict)) or 2
    elif "marks" not in q:
        q["marks"] = 2

    q.setdefault("caps_weight_percent", 10)
    q.setdefault("suggested_duration_mins", 3)
    q.setdefault("mode", "compound")
    q.setdefault("difficulty", "medium")

    return q


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """6-Pillar Generator Contract entry point."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    if subskill and subskill in ARCHETYPE_MAP:
        candidates = [subskill]
    else:
        candidates = SUBSKILLS

    for i in range(count):
        sub = candidates[i % len(candidates)] if len(candidates) > 1 else candidates[0]
        sub_seed = r.randint(1, 1_000_000_000)
        q = generate_grade9_geometry_3d_objects_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
