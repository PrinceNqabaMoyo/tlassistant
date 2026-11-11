"""
Grade 7 Mathematics - Geometry of Straight Lines Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of straight lines.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .straight_lines_archetypes_01_25 import (
    arch_01_line_segment_definition_and_endpoints,
    arch_02_ray_definition_and_direction,
    arch_03_line_infinite_extent_properties,
    arch_04_identify_line_ray_segment_from_diagram,
    arch_05_symbolic_notation_matching,
    arch_06_parallel_lines_concept_and_distance,
    arch_07_parallel_lines_arrow_symbol_notation,
    arch_08_perpendicular_lines_right_angle_concept,
    arch_09_perpendicular_symbol_and_identifying_90_deg,
    arch_10_intersecting_lines_point_of_intersection,
    arch_11_adjacent_angles_on_straight_line_numeric,
    arch_12_adjacent_angles_on_straight_line_algebraic,
    arch_13_adjacent_three_angles_on_straight_line,
    arch_14_perpendicular_line_adjacent_complement,
    arch_15_complementary_angles_concept_and_calc,
    arch_16_vertically_opposite_angles_identification,
    arch_17_vertically_opposite_angles_numeric_solve,
    arch_18_vertically_opposite_angles_algebraic_solve,
    arch_19_intersecting_lines_four_angles_puzzle,
    arch_20_angles_around_a_point_revolution_numeric,
    arch_21_angles_around_a_point_revolution_algebraic,
    arch_22_perpendicular_bisector_visual_properties,
    arch_23_parallel_lines_transversal_identification,
    arch_24_corresponding_angles_f_shape_identification,
    arch_25_corresponding_angles_solve_for_x,
)

from .straight_lines_archetypes_26_50 import (
    arch_26_alternate_interior_angles_z_shape_identification,
    arch_27_alternate_interior_angles_solve_for_x,
    arch_28_co_interior_angles_c_shape_identification,
    arch_29_co_interior_angles_solve_supplementary,
    arch_30_parallel_lines_mixed_angle_pair_identification,
    arch_31_parallel_lines_multi_step_two_unknowns,
    arch_32_parallel_lines_algebraic_corresponding_equation,
    arch_33_parallel_lines_algebraic_alternate_equation,
    arch_34_parallel_lines_algebraic_co_interior_equation,
    arch_35_testing_parallel_lines_equal_alternate_angles,
    arch_36_testing_parallel_lines_equal_corresponding_angles,
    arch_37_testing_parallel_lines_supplementary_co_interior,
    arch_38_parallel_lines_with_transversal_and_bisector,
    arch_39_two_transversals_intersecting_between_parallels,
    arch_40_transversal_perpendicular_to_parallel_line,
    arch_41_straight_line_with_perpendicular_ray_and_angle,
    arch_42_geometric_reasons_matching_straight_line_theorems,
    arch_43_spot_the_error_angle_on_straight_line,
    arch_44_spot_the_error_vertically_opposite_reason,
    arch_45_spot_the_error_parallel_line_angle_assumption,
    arch_46_practical_context_clock_hands_straight_angle,
    arch_47_practical_context_road_intersection_angles,
    arch_48_practical_context_railway_tracks_and_switch_transversal,
    arch_49_practical_context_roof_truss_parallel_chords,
    arch_50_comprehensive_multi_angle_proof_and_calculation,
)

ARCHETYPE_BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_line_segment_definition_and_endpoints,
    arch_02_ray_definition_and_direction,
    arch_03_line_infinite_extent_properties,
    arch_04_identify_line_ray_segment_from_diagram,
    arch_05_symbolic_notation_matching,
    arch_06_parallel_lines_concept_and_distance,
    arch_07_parallel_lines_arrow_symbol_notation,
    arch_08_perpendicular_lines_right_angle_concept,
    arch_09_perpendicular_symbol_and_identifying_90_deg,
    arch_10_intersecting_lines_point_of_intersection,
    arch_11_adjacent_angles_on_straight_line_numeric,
    arch_12_adjacent_angles_on_straight_line_algebraic,
    arch_13_adjacent_three_angles_on_straight_line,
    arch_14_perpendicular_line_adjacent_complement,
    arch_15_complementary_angles_concept_and_calc,
    arch_16_vertically_opposite_angles_identification,
    arch_17_vertically_opposite_angles_numeric_solve,
    arch_18_vertically_opposite_angles_algebraic_solve,
    arch_19_intersecting_lines_four_angles_puzzle,
    arch_20_angles_around_a_point_revolution_numeric,
    arch_21_angles_around_a_point_revolution_algebraic,
    arch_22_perpendicular_bisector_visual_properties,
    arch_23_parallel_lines_transversal_identification,
    arch_24_corresponding_angles_f_shape_identification,
    arch_25_corresponding_angles_solve_for_x,
    arch_26_alternate_interior_angles_z_shape_identification,
    arch_27_alternate_interior_angles_solve_for_x,
    arch_28_co_interior_angles_c_shape_identification,
    arch_29_co_interior_angles_solve_supplementary,
    arch_30_parallel_lines_mixed_angle_pair_identification,
    arch_31_parallel_lines_multi_step_two_unknowns,
    arch_32_parallel_lines_algebraic_corresponding_equation,
    arch_33_parallel_lines_algebraic_alternate_equation,
    arch_34_parallel_lines_algebraic_co_interior_equation,
    arch_35_testing_parallel_lines_equal_alternate_angles,
    arch_36_testing_parallel_lines_equal_corresponding_angles,
    arch_37_testing_parallel_lines_supplementary_co_interior,
    arch_38_parallel_lines_with_transversal_and_bisector,
    arch_39_two_transversals_intersecting_between_parallels,
    arch_40_transversal_perpendicular_to_parallel_line,
    arch_41_straight_line_with_perpendicular_ray_and_angle,
    arch_42_geometric_reasons_matching_straight_line_theorems,
    arch_43_spot_the_error_angle_on_straight_line,
    arch_44_spot_the_error_vertically_opposite_reason,
    arch_45_spot_the_error_parallel_line_angle_assumption,
    arch_46_practical_context_clock_hands_straight_angle,
    arch_47_practical_context_road_intersection_angles,
    arch_48_practical_context_railway_tracks_and_switch_transversal,
    arch_49_practical_context_roof_truss_parallel_chords,
    arch_50_comprehensive_multi_angle_proof_and_calculation,
]

SUBSKILLS: List[str] = [
    "01_line_segment_definition_and_endpoints",
    "02_ray_definition_and_direction",
    "03_line_infinite_extent_properties",
    "04_identify_line_ray_segment_from_diagram",
    "05_symbolic_notation_matching",
    "06_parallel_lines_concept_and_distance",
    "07_parallel_lines_arrow_symbol_notation",
    "08_perpendicular_lines_right_angle_concept",
    "09_perpendicular_symbol_and_identifying_90_deg",
    "10_intersecting_lines_point_of_intersection",
    "11_adjacent_angles_on_straight_line_numeric",
    "12_adjacent_angles_on_straight_line_algebraic",
    "13_adjacent_three_angles_on_straight_line",
    "14_perpendicular_line_adjacent_complement",
    "15_complementary_angles_concept_and_calc",
    "16_vertically_opposite_angles_identification",
    "17_vertically_opposite_angles_numeric_solve",
    "18_vertically_opposite_angles_algebraic_solve",
    "19_intersecting_lines_four_angles_puzzle",
    "20_angles_around_a_point_revolution_numeric",
    "21_angles_around_a_point_revolution_algebraic",
    "22_perpendicular_bisector_visual_properties",
    "23_parallel_lines_transversal_identification",
    "24_corresponding_angles_f_shape_identification",
    "25_corresponding_angles_solve_for_x",
    "26_alternate_interior_angles_z_shape_identification",
    "27_alternate_interior_angles_solve_for_x",
    "28_co_interior_angles_c_shape_identification",
    "29_co_interior_angles_solve_supplementary",
    "30_parallel_lines_mixed_angle_pair_identification",
    "31_parallel_lines_multi_step_two_unknowns",
    "32_parallel_lines_algebraic_corresponding_equation",
    "33_parallel_lines_algebraic_alternate_equation",
    "34_parallel_lines_algebraic_co_interior_equation",
    "35_testing_parallel_lines_equal_alternate_angles",
    "36_testing_parallel_lines_equal_corresponding_angles",
    "37_testing_parallel_lines_supplementary_co_interior",
    "38_parallel_lines_with_transversal_and_bisector",
    "39_two_transversals_intersecting_between_parallels",
    "40_transversal_perpendicular_to_parallel_line",
    "41_straight_line_with_perpendicular_ray_and_angle",
    "42_geometric_reasons_matching_straight_line_theorems",
    "43_spot_the_error_angle_on_straight_line",
    "44_spot_the_error_vertically_opposite_reason",
    "45_spot_the_error_parallel_line_angle_assumption",
    "46_practical_context_clock_hands_straight_angle",
    "47_practical_context_road_intersection_angles",
    "48_practical_context_railway_tracks_and_switch_transversal",
    "49_practical_context_roof_truss_parallel_chords",
    "50_comprehensive_multi_angle_proof_and_calculation",
]

_SUBSKILL_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    name: builder for name, builder in zip(SUBSKILLS, ARCHETYPE_BUILDERS)
}


def generate_question(
    rng: Optional[random.Random] = None,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """Generates a fully calibrated Grade 7 Geometry of Straight Lines question."""
    if rng is None:
        rng = random.Random(seed) if seed is not None else random.Random()

    if subskill and subskill in _SUBSKILL_MAP:
        builder = _SUBSKILL_MAP[subskill]
    else:
        builder = rng.choice(ARCHETYPE_BUILDERS)

    payload = builder(rng)

    # Inject 6-pillar standard metadata
    payload.setdefault("term", 1)
    payload.setdefault("grade", 7)
    payload.setdefault("subject", "Mathematics")
    payload.setdefault("topic", "Geometry of straight lines")
    payload.setdefault("caps_weight_percent", 10.0)
    payload.setdefault("suggested_duration_mins", 3)
    payload.setdefault("mode", "elementary_" + payload.get("subskill", "straight_lines"))
    payload.setdefault(
        "marking_schema",
        [
            {"step": "Correct geometric statement", "marks": 1, "type": "M"},
            {"step": "Correct calculation and valid reason", "marks": max(1, payload.get("marks", 2) - 1), "type": "A"},
        ],
    )
    return payload


generate = generate_question
