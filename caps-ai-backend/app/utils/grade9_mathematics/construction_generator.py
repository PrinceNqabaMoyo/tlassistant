"""Grade 9 Mathematics - Construction of Geometric Figures Generator (50 Semantic Archetypes).
=============================================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 3 Topic: Construction of geometric figures
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/01. Construction of geometric figures.md
  - Chapter 4: Compass and straightedge constructions, angle bisection, perpendicular
    bisectors, special angle constructions (30°, 45°, 60°, 75°, 90°, 105°, 120°, 135°),
    triangle constructions (SSS, SAS, ASA, RHS), quadrilateral constructions,
    triangle centers (circumcentre, incentre, centroid, orthocentre), circle tangents,
    scale drawings, bearings, and diagnostic error analysis.

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .construction_archetypes_01_25 import (
    arch_01_angle_classification_and_measurement,
    arch_02_angle_bisector_concept_and_definition,
    arch_03_angle_bisector_algebraic_equation,
    arch_04_identify_angle_bisector_compass_arcs,
    arch_05_bisect_obtuse_or_reflex_angle,
    arch_06_adjacent_supplementary_angle_bisectors_perpendicular,
    arch_07_angle_trisection_vs_bisection_concepts,
    arch_08_perpendicular_bisector_definition_and_midpoint,
    arch_09_perpendicular_bisector_equidistance_property,
    arch_10_perpendicular_bisector_compass_radius_condition,
    arch_11_perpendicular_line_through_point_on_line,
    arch_12_perpendicular_line_from_external_point_to_line,
    arch_13_shortest_distance_from_point_to_line,
    arch_14_equidistant_locus_of_two_parallel_lines,
    arch_15_construct_60_degree_angle_equilateral_triangle,
    arch_16_construct_30_degree_angle_by_bisecting_60,
    arch_17_construct_90_degree_angle_perpendicular,
    arch_18_construct_45_degree_angle_by_bisecting_90,
    arch_19_construct_15_degree_angle_by_bisecting_30,
    arch_20_construct_75_degree_angle_combination,
    arch_21_construct_105_degree_angle_combination,
    arch_22_construct_120_and_135_degree_angles,
    arch_23_triangle_inequality_theorem_validity,
    arch_24_triangle_inequality_range_of_third_side,
    arch_25_construct_triangle_sss_three_sides,
)
from .construction_archetypes_26_50 import (
    arch_26_construct_triangle_sas_two_sides_included_angle,
    arch_27_construct_triangle_asa_two_angles_one_side,
    arch_28_construct_right_angled_triangle_rhs,
    arch_29_construct_equilateral_triangle_given_side,
    arch_30_construct_square_given_side_length,
    arch_31_construct_rectangle_given_length_and_breadth,
    arch_32_construct_parallelogram_given_two_sides_and_angle,
    arch_33_construct_rhombus_given_side_and_diagonal,
    arch_34_construct_regular_hexagon_inscribed_in_circle,
    arch_35_circumcentre_and_circumscribed_circle,
    arch_36_incentre_and_inscribed_circle,
    arch_37_centroid_intersection_of_medians,
    arch_38_orthocentre_intersection_of_altitudes,
    arch_39_circumcentre_location_acute_right_obtuse,
    arch_40_tangent_to_a_circle_perpendicular_to_radius,
    arch_41_tangents_from_external_point_equal_length,
    arch_42_common_chord_of_two_intersecting_circles,
    arch_43_scale_drawing_triangle_actual_distance,
    arch_44_three_figure_bearing_construction,
    arch_45_compass_radius_error_non_intersecting_arcs,
    arch_46_error_analysis_protractor_inner_vs_outer_scale,
    arch_47_error_analysis_ambiguous_triangle_ssa_not_congruent,
    arch_48_dividing_line_segment_into_n_equal_parts,
    arch_49_geometric_locus_equidistant_from_two_intersecting_lines,
    arch_50_compound_multi_step_geometric_construction_synthesis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_angle_classification_and_measurement": arch_01_angle_classification_and_measurement,
    "02_angle_bisector_concept_and_definition": arch_02_angle_bisector_concept_and_definition,
    "03_angle_bisector_algebraic_equation": arch_03_angle_bisector_algebraic_equation,
    "04_identify_angle_bisector_compass_arcs": arch_04_identify_angle_bisector_compass_arcs,
    "05_bisect_obtuse_or_reflex_angle": arch_05_bisect_obtuse_or_reflex_angle,
    "06_adjacent_supplementary_angle_bisectors_perpendicular": arch_06_adjacent_supplementary_angle_bisectors_perpendicular,
    "07_angle_trisection_vs_bisection_concepts": arch_07_angle_trisection_vs_bisection_concepts,
    "08_perpendicular_bisector_definition_and_midpoint": arch_08_perpendicular_bisector_definition_and_midpoint,
    "09_perpendicular_bisector_equidistance_property": arch_09_perpendicular_bisector_equidistance_property,
    "10_perpendicular_bisector_compass_radius_condition": arch_10_perpendicular_bisector_compass_radius_condition,
    "11_perpendicular_line_through_point_on_line": arch_11_perpendicular_line_through_point_on_line,
    "12_perpendicular_line_from_external_point_to_line": arch_12_perpendicular_line_from_external_point_to_line,
    "13_shortest_distance_from_point_to_line": arch_13_shortest_distance_from_point_to_line,
    "14_equidistant_locus_of_two_parallel_lines": arch_14_equidistant_locus_of_two_parallel_lines,
    "15_construct_60_degree_angle_equilateral_triangle": arch_15_construct_60_degree_angle_equilateral_triangle,
    "16_construct_30_degree_angle_by_bisecting_60": arch_16_construct_30_degree_angle_by_bisecting_60,
    "17_construct_90_degree_angle_perpendicular": arch_17_construct_90_degree_angle_perpendicular,
    "18_construct_45_degree_angle_by_bisecting_90": arch_18_construct_45_degree_angle_by_bisecting_90,
    "19_construct_15_degree_angle_by_bisecting_30": arch_19_construct_15_degree_angle_by_bisecting_30,
    "20_construct_75_degree_angle_combination": arch_20_construct_75_degree_angle_combination,
    "21_construct_105_degree_angle_combination": arch_21_construct_105_degree_angle_combination,
    "22_construct_120_and_135_degree_angles": arch_22_construct_120_and_135_degree_angles,
    "23_triangle_inequality_theorem_validity": arch_23_triangle_inequality_theorem_validity,
    "24_triangle_inequality_range_of_third_side": arch_24_triangle_inequality_range_of_third_side,
    "25_construct_triangle_sss_three_sides": arch_25_construct_triangle_sss_three_sides,
    "26_construct_triangle_sas_two_sides_included_angle": arch_26_construct_triangle_sas_two_sides_included_angle,
    "27_construct_triangle_asa_two_angles_one_side": arch_27_construct_triangle_asa_two_angles_one_side,
    "28_construct_right_angled_triangle_rhs": arch_28_construct_right_angled_triangle_rhs,
    "29_construct_equilateral_triangle_given_side": arch_29_construct_equilateral_triangle_given_side,
    "30_construct_square_given_side_length": arch_30_construct_square_given_side_length,
    "31_construct_rectangle_given_length_and_breadth": arch_31_construct_rectangle_given_length_and_breadth,
    "32_construct_parallelogram_given_two_sides_and_angle": arch_32_construct_parallelogram_given_two_sides_and_angle,
    "33_construct_rhombus_given_side_and_diagonal": arch_33_construct_rhombus_given_side_and_diagonal,
    "34_construct_regular_hexagon_inscribed_in_circle": arch_34_construct_regular_hexagon_inscribed_in_circle,
    "35_circumcentre_and_circumscribed_circle": arch_35_circumcentre_and_circumscribed_circle,
    "36_incentre_and_inscribed_circle": arch_36_incentre_and_inscribed_circle,
    "37_centroid_intersection_of_medians": arch_37_centroid_intersection_of_medians,
    "38_orthocentre_intersection_of_altitudes": arch_38_orthocentre_intersection_of_altitudes,
    "39_circumcentre_location_acute_right_obtuse": arch_39_circumcentre_location_acute_right_obtuse,
    "40_tangent_to_a_circle_perpendicular_to_radius": arch_40_tangent_to_a_circle_perpendicular_to_radius,
    "41_tangents_from_external_point_equal_length": arch_41_tangents_from_external_point_equal_length,
    "42_common_chord_of_two_intersecting_circles": arch_42_common_chord_of_two_intersecting_circles,
    "43_scale_drawing_triangle_actual_distance": arch_43_scale_drawing_triangle_actual_distance,
    "44_three_figure_bearing_construction": arch_44_three_figure_bearing_construction,
    "45_compass_radius_error_non_intersecting_arcs": arch_45_compass_radius_error_non_intersecting_arcs,
    "46_error_analysis_protractor_inner_vs_outer_scale": arch_46_error_analysis_protractor_inner_vs_outer_scale,
    "47_error_analysis_ambiguous_triangle_ssa_not_congruent": arch_47_error_analysis_ambiguous_triangle_ssa_not_congruent,
    "48_dividing_line_segment_into_n_equal_parts": arch_48_dividing_line_segment_into_n_equal_parts,
    "49_geometric_locus_equidistant_from_two_intersecting_lines": arch_49_geometric_locus_equidistant_from_two_intersecting_lines,
    "50_compound_multi_step_geometric_construction_synthesis": arch_50_compound_multi_step_geometric_construction_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

SUBSKILLS_TUPLES: List[Tuple[str, str]] = [
    (key, key[3:].replace("_", " ").title()) for key in SUBSKILLS
]


def generate_grade9_construction_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Construction of Geometric Figures question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        builder = ARCHETYPE_MAP[subskill]
        chosen_subskill = subskill
    elif subskill:
        # Match by prefix or substring if requested
        s_clean = str(subskill).strip()
        matched = None
        for k, b in ARCHETYPE_MAP.items():
            if k.startswith(s_clean) or s_clean in k:
                matched = (k, b)
                break
        if matched:
            chosen_subskill, builder = matched
        else:
            chosen_subskill = r.choice(SUBSKILLS)
            builder = ARCHETYPE_MAP[chosen_subskill]
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Construction of geometric figures"
    q["term"] = 3
    q.setdefault("caps_weight_percent", 10)
    q.setdefault("suggested_duration_mins", 4)
    q.setdefault("difficulty", "medium")
    q.setdefault("mode", "compound")
    if not q.get("prompt"):
        q["prompt"] = q.get("question_text")
    if not q.get("sample_answer"):
        q["sample_answer"] = str(q.get("correct_answer"))
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
        q = generate_grade9_construction_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
