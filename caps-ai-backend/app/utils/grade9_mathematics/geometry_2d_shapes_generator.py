"""Grade 9 Mathematics - Geometry of 2D Shapes Generator (50 Semantic Archetypes).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 2/04. Geometry of 2D shapes.md

Deterministic question generator compliant with South African curriculum standards.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_2d_shapes_archetypes_01_25 import (
    arch_01_classify_triangle_by_sides_and_angles,
    arch_02_triangle_interior_angle_sum_basic,
    arch_03_triangle_interior_angles_algebraic_linear,
    arch_04_triangle_exterior_angle_theorem_numeric,
    arch_05_triangle_exterior_angle_theorem_algebraic,
    arch_06_isosceles_triangle_base_angles_calculation,
    arch_07_isosceles_triangle_vertex_angle_from_base,
    arch_08_isosceles_triangle_with_exterior_angle,
    arch_09_equilateral_triangle_properties_and_algebra,
    arch_10_right_angled_triangle_acute_angles_complementary,
    arch_11_triangle_inequality_theorem,
    arch_12_congruence_identify_condition_sss,
    arch_13_congruence_identify_condition_sas,
    arch_14_congruence_identify_condition_aas,
    arch_15_congruence_identify_condition_rhs,
    arch_16_congruence_non_condition_ssa_counterexample,
    arch_17_congruence_statement_correct_vertex_correspondence,
    arch_18_congruence_formal_proof_sss,
    arch_19_congruence_formal_proof_sas,
    arch_20_congruence_formal_proof_aas,
    arch_21_congruence_formal_proof_rhs,
    arch_22_congruence_deduce_unknown_side_after_proof,
    arch_23_congruence_deduce_unknown_angle_after_proof,
    arch_24_overlapping_triangles_common_side_congruence,
    arch_25_triangles_with_vertically_opposite_angles_congruence,
)
from .geometry_2d_shapes_archetypes_26_50 import (
    arch_26_similarity_condition_aaa_equiangular,
    arch_27_similarity_statement_correct_vertex_order,
    arch_28_similarity_calculate_scale_factor,
    arch_29_similarity_calculate_unknown_side_proportion,
    arch_30_similarity_formal_proof_equiangular,
    arch_31_similarity_nested_triangles_parallel_transversal,
    arch_32_quadrilateral_interior_angle_sum_numeric,
    arch_33_quadrilateral_interior_angles_algebraic,
    arch_34_parallelogram_opposite_angles_equal,
    arch_35_parallelogram_cointerior_consecutive_angles_supplementary,
    arch_36_parallelogram_opposite_sides_equal_algebra,
    arch_37_parallelogram_diagonals_bisect_each_other,
    arch_38_rectangle_properties_right_angles_and_diagonals,
    arch_39_rhombus_perpendicular_diagonals_calculation,
    arch_40_rhombus_diagonals_bisect_corner_angles,
    arch_41_square_combined_properties_calculation,
    arch_42_trapezium_cointerior_angles_parallel_sides,
    arch_43_isosceles_trapezium_base_angles_equal,
    arch_44_kite_properties_axis_of_symmetry_and_angles,
    arch_45_prove_quadrilateral_is_parallelogram_conditions,
    arch_46_regular_polygon_interior_angle_sum,
    arch_47_regular_polygon_size_of_each_interior_angle,
    arch_48_regular_polygon_size_of_each_exterior_angle,
    arch_49_error_analysis_diagnose_geometric_congruency_error,
    arch_50_compound_multi_step_geometry_2d_synthesis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_classify_triangle_by_sides_and_angles": arch_01_classify_triangle_by_sides_and_angles,
    "02_triangle_interior_angle_sum_basic": arch_02_triangle_interior_angle_sum_basic,
    "03_triangle_interior_angles_algebraic_linear": arch_03_triangle_interior_angles_algebraic_linear,
    "04_triangle_exterior_angle_theorem_numeric": arch_04_triangle_exterior_angle_theorem_numeric,
    "05_triangle_exterior_angle_theorem_algebraic": arch_05_triangle_exterior_angle_theorem_algebraic,
    "06_isosceles_triangle_base_angles_calculation": arch_06_isosceles_triangle_base_angles_calculation,
    "07_isosceles_triangle_vertex_angle_from_base": arch_07_isosceles_triangle_vertex_angle_from_base,
    "08_isosceles_triangle_with_exterior_angle": arch_08_isosceles_triangle_with_exterior_angle,
    "09_equilateral_triangle_properties_and_algebra": arch_09_equilateral_triangle_properties_and_algebra,
    "10_right_angled_triangle_acute_angles_complementary": arch_10_right_angled_triangle_acute_angles_complementary,
    "11_triangle_inequality_theorem": arch_11_triangle_inequality_theorem,
    "12_congruence_identify_condition_sss": arch_12_congruence_identify_condition_sss,
    "13_congruence_identify_condition_sas": arch_13_congruence_identify_condition_sas,
    "14_congruence_identify_condition_aas": arch_14_congruence_identify_condition_aas,
    "15_congruence_identify_condition_rhs": arch_15_congruence_identify_condition_rhs,
    "16_congruence_non_condition_ssa_counterexample": arch_16_congruence_non_condition_ssa_counterexample,
    "17_congruence_statement_correct_vertex_correspondence": arch_17_congruence_statement_correct_vertex_correspondence,
    "18_congruence_formal_proof_sss": arch_18_congruence_formal_proof_sss,
    "19_congruence_formal_proof_sas": arch_19_congruence_formal_proof_sas,
    "20_congruence_formal_proof_aas": arch_20_congruence_formal_proof_aas,
    "21_congruence_formal_proof_rhs": arch_21_congruence_formal_proof_rhs,
    "22_congruence_deduce_unknown_side_after_proof": arch_22_congruence_deduce_unknown_side_after_proof,
    "23_congruence_deduce_unknown_angle_after_proof": arch_23_congruence_deduce_unknown_angle_after_proof,
    "24_overlapping_triangles_common_side_congruence": arch_24_overlapping_triangles_common_side_congruence,
    "25_triangles_with_vertically_opposite_angles_congruence": arch_25_triangles_with_vertically_opposite_angles_congruence,
    "26_similarity_condition_aaa_equiangular": arch_26_similarity_condition_aaa_equiangular,
    "27_similarity_statement_correct_vertex_order": arch_27_similarity_statement_correct_vertex_order,
    "28_similarity_calculate_scale_factor": arch_28_similarity_calculate_scale_factor,
    "29_similarity_calculate_unknown_side_proportion": arch_29_similarity_calculate_unknown_side_proportion,
    "30_similarity_formal_proof_equiangular": arch_30_similarity_formal_proof_equiangular,
    "31_similarity_nested_triangles_parallel_transversal": arch_31_similarity_nested_triangles_parallel_transversal,
    "32_quadrilateral_interior_angle_sum_numeric": arch_32_quadrilateral_interior_angle_sum_numeric,
    "33_quadrilateral_interior_angles_algebraic": arch_33_quadrilateral_interior_angles_algebraic,
    "34_parallelogram_opposite_angles_equal": arch_34_parallelogram_opposite_angles_equal,
    "35_parallelogram_cointerior_consecutive_angles_supplementary": arch_35_parallelogram_cointerior_consecutive_angles_supplementary,
    "36_parallelogram_opposite_sides_equal_algebra": arch_36_parallelogram_opposite_sides_equal_algebra,
    "37_parallelogram_diagonals_bisect_each_other": arch_37_parallelogram_diagonals_bisect_each_other,
    "38_rectangle_properties_right_angles_and_diagonals": arch_38_rectangle_properties_right_angles_and_diagonals,
    "39_rhombus_perpendicular_diagonals_calculation": arch_39_rhombus_perpendicular_diagonals_calculation,
    "40_rhombus_diagonals_bisect_corner_angles": arch_40_rhombus_diagonals_bisect_corner_angles,
    "41_square_combined_properties_calculation": arch_41_square_combined_properties_calculation,
    "42_trapezium_cointerior_angles_parallel_sides": arch_42_trapezium_cointerior_angles_parallel_sides,
    "43_isosceles_trapezium_base_angles_equal": arch_43_isosceles_trapezium_base_angles_equal,
    "44_kite_properties_axis_of_symmetry_and_angles": arch_44_kite_properties_axis_of_symmetry_and_angles,
    "45_prove_quadrilateral_is_parallelogram_conditions": arch_45_prove_quadrilateral_is_parallelogram_conditions,
    "46_regular_polygon_interior_angle_sum": arch_46_regular_polygon_interior_angle_sum,
    "47_regular_polygon_size_of_each_interior_angle": arch_47_regular_polygon_size_of_each_interior_angle,
    "48_regular_polygon_size_of_each_exterior_angle": arch_48_regular_polygon_size_of_each_exterior_angle,
    "49_error_analysis_diagnose_geometric_congruency_error": arch_49_error_analysis_diagnose_geometric_congruency_error,
    "50_compound_multi_step_geometry_2d_synthesis": arch_50_compound_multi_step_geometry_2d_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_geometry_2d_shapes_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Geometry of 2D Shapes question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Geometry of 2D shapes"
    q["term"] = 2
    q["caps_weight_percent"] = 12
    q["suggested_duration_mins"] = 3
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
        q = generate_grade9_geometry_2d_shapes_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
