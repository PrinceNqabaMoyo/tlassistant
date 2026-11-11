"""Grade 9 Mathematics - Geometry of Straight Lines Generator (50 Semantic Archetypes).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/03. Geometry of straight lines.md

100% CAPS-aligned deterministic question generator.
Zero LLM calls, zero token cost, 100% AST pure.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_straight_lines_archetypes_01_25 import (
    arch_01_vertically_opposite_angles_numeric,
    arch_02_vertically_opposite_angles_algebraic_linear,
    arch_03_vertically_opposite_angles_calculate_angle_size,
    arch_04_adjacent_angles_straight_line_numeric_two_angles,
    arch_05_adjacent_angles_straight_line_numeric_three_angles,
    arch_06_adjacent_angles_straight_line_algebraic_linear,
    arch_07_adjacent_angles_straight_line_algebraic_three_angles,
    arch_08_perpendicular_adjacent_angles_numeric,
    arch_09_perpendicular_adjacent_angles_algebraic,
    arch_10_angles_around_a_point_revolution_numeric,
    arch_11_angles_around_a_point_revolution_algebraic,
    arch_12_intersecting_lines_four_angles_complete_set,
    arch_13_parallel_lines_corresponding_angles_numeric,
    arch_14_parallel_lines_corresponding_angles_algebraic,
    arch_15_parallel_lines_corresponding_angles_calculate_angle,
    arch_16_parallel_lines_alternate_angles_numeric,
    arch_17_parallel_lines_alternate_angles_algebraic,
    arch_18_parallel_lines_alternate_angles_calculate_angle,
    arch_19_parallel_lines_cointerior_angles_numeric,
    arch_20_parallel_lines_cointerior_angles_algebraic,
    arch_21_parallel_lines_cointerior_angles_calculate_angle,
    arch_22_parallel_transversal_full_eight_angles_deduction,
    arch_23_statement_reason_fill_transversal_angle,
    arch_24_statement_reason_fill_transversal_statement,
    arch_25_error_analysis_confusing_alternate_and_cointerior,
)
from .geometry_straight_lines_archetypes_26_50 import (
    arch_26_error_analysis_omitting_parallel_line_reference_in_reason,
    arch_27_prove_lines_parallel_alternate_angles_converse,
    arch_28_prove_lines_parallel_corresponding_angles_converse,
    arch_29_prove_lines_parallel_cointerior_angles_converse,
    arch_30_parallel_lines_dual_transversal_triangle_formed,
    arch_31_parallel_lines_zigzag_auxiliary_line_numeric,
    arch_32_parallel_lines_zigzag_auxiliary_line_algebraic,
    arch_33_parallel_lines_perpendicular_transversal,
    arch_34_bisector_of_adjacent_supplementary_angles,
    arch_35_bisector_of_vertically_opposite_angles,
    arch_36_multi_step_parallel_transversal_with_straight_line_combo,
    arch_37_multi_step_parallel_transversal_with_vert_opp_combo,
    arch_38_three_parallel_lines_two_transversals_numeric,
    arch_39_three_parallel_lines_two_transversals_algebraic,
    arch_40_parallel_lines_ratio_cointerior_angles,
    arch_41_adjacent_angles_straight_line_ratio,
    arch_42_algebraic_system_two_variables_transversal,
    arch_43_converse_test_determine_if_lines_are_parallel,
    arch_44_formal_euclidean_proof_step_vert_opp_transversal,
    arch_45_parallel_lines_exterior_alternate_angles,
    arch_46_straight_line_adjacent_angles_with_algebraic_fractions,
    arch_47_parallel_lines_cointerior_fractions,
    arch_48_real_world_context_railway_track_transversal,
    arch_49_real_world_context_bridge_truss_parallel_struts,
    arch_50_compound_multi_line_geometric_synthesis,
)

ARCHETYPE_MAP: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_vertically_opposite_angles_numeric": arch_01_vertically_opposite_angles_numeric,
    "02_vertically_opposite_angles_algebraic_linear": arch_02_vertically_opposite_angles_algebraic_linear,
    "03_vertically_opposite_angles_calculate_angle_size": arch_03_vertically_opposite_angles_calculate_angle_size,
    "04_adjacent_angles_straight_line_numeric_two_angles": arch_04_adjacent_angles_straight_line_numeric_two_angles,
    "05_adjacent_angles_straight_line_numeric_three_angles": arch_05_adjacent_angles_straight_line_numeric_three_angles,
    "06_adjacent_angles_straight_line_algebraic_linear": arch_06_adjacent_angles_straight_line_algebraic_linear,
    "07_adjacent_angles_straight_line_algebraic_three_angles": arch_07_adjacent_angles_straight_line_algebraic_three_angles,
    "08_perpendicular_adjacent_angles_numeric": arch_08_perpendicular_adjacent_angles_numeric,
    "09_perpendicular_adjacent_angles_algebraic": arch_09_perpendicular_adjacent_angles_algebraic,
    "10_angles_around_a_point_revolution_numeric": arch_10_angles_around_a_point_revolution_numeric,
    "11_angles_around_a_point_revolution_algebraic": arch_11_angles_around_a_point_revolution_algebraic,
    "12_intersecting_lines_four_angles_complete_set": arch_12_intersecting_lines_four_angles_complete_set,
    "13_parallel_lines_corresponding_angles_numeric": arch_13_parallel_lines_corresponding_angles_numeric,
    "14_parallel_lines_corresponding_angles_algebraic": arch_14_parallel_lines_corresponding_angles_algebraic,
    "15_parallel_lines_corresponding_angles_calculate_angle": arch_15_parallel_lines_corresponding_angles_calculate_angle,
    "16_parallel_lines_alternate_angles_numeric": arch_16_parallel_lines_alternate_angles_numeric,
    "17_parallel_lines_alternate_angles_algebraic": arch_17_parallel_lines_alternate_angles_algebraic,
    "18_parallel_lines_alternate_angles_calculate_angle": arch_18_parallel_lines_alternate_angles_calculate_angle,
    "19_parallel_lines_cointerior_angles_numeric": arch_19_parallel_lines_cointerior_angles_numeric,
    "20_parallel_lines_cointerior_angles_algebraic": arch_20_parallel_lines_cointerior_angles_algebraic,
    "21_parallel_lines_cointerior_angles_calculate_angle": arch_21_parallel_lines_cointerior_angles_calculate_angle,
    "22_parallel_transversal_full_eight_angles_deduction": arch_22_parallel_transversal_full_eight_angles_deduction,
    "23_statement_reason_fill_transversal_angle": arch_23_statement_reason_fill_transversal_angle,
    "24_statement_reason_fill_transversal_statement": arch_24_statement_reason_fill_transversal_statement,
    "25_error_analysis_confusing_alternate_and_cointerior": arch_25_error_analysis_confusing_alternate_and_cointerior,
    "26_error_analysis_omitting_parallel_line_reference_in_reason": arch_26_error_analysis_omitting_parallel_line_reference_in_reason,
    "27_prove_lines_parallel_alternate_angles_converse": arch_27_prove_lines_parallel_alternate_angles_converse,
    "28_prove_lines_parallel_corresponding_angles_converse": arch_28_prove_lines_parallel_corresponding_angles_converse,
    "29_prove_lines_parallel_cointerior_angles_converse": arch_29_prove_lines_parallel_cointerior_angles_converse,
    "30_parallel_lines_dual_transversal_triangle_formed": arch_30_parallel_lines_dual_transversal_triangle_formed,
    "31_parallel_lines_zigzag_auxiliary_line_numeric": arch_31_parallel_lines_zigzag_auxiliary_line_numeric,
    "32_parallel_lines_zigzag_auxiliary_line_algebraic": arch_32_parallel_lines_zigzag_auxiliary_line_algebraic,
    "33_parallel_lines_perpendicular_transversal": arch_33_parallel_lines_perpendicular_transversal,
    "34_bisector_of_adjacent_supplementary_angles": arch_34_bisector_of_adjacent_supplementary_angles,
    "35_bisector_of_vertically_opposite_angles": arch_35_bisector_of_vertically_opposite_angles,
    "36_multi_step_parallel_transversal_with_straight_line_combo": arch_36_multi_step_parallel_transversal_with_straight_line_combo,
    "37_multi_step_parallel_transversal_with_vert_opp_combo": arch_37_multi_step_parallel_transversal_with_vert_opp_combo,
    "38_three_parallel_lines_two_transversals_numeric": arch_38_three_parallel_lines_two_transversals_numeric,
    "39_three_parallel_lines_two_transversals_algebraic": arch_39_three_parallel_lines_two_transversals_algebraic,
    "40_parallel_lines_ratio_cointerior_angles": arch_40_parallel_lines_ratio_cointerior_angles,
    "41_adjacent_angles_straight_line_ratio": arch_41_adjacent_angles_straight_line_ratio,
    "42_algebraic_system_two_variables_transversal": arch_42_algebraic_system_two_variables_transversal,
    "43_converse_test_determine_if_lines_are_parallel": arch_43_converse_test_determine_if_lines_are_parallel,
    "44_formal_euclidean_proof_step_vert_opp_transversal": arch_44_formal_euclidean_proof_step_vert_opp_transversal,
    "45_parallel_lines_exterior_alternate_angles": arch_45_parallel_lines_exterior_alternate_angles,
    "46_straight_line_adjacent_angles_with_algebraic_fractions": arch_46_straight_line_adjacent_angles_with_algebraic_fractions,
    "47_parallel_lines_cointerior_fractions": arch_47_parallel_lines_cointerior_fractions,
    "48_real_world_context_railway_track_transversal": arch_48_real_world_context_railway_track_transversal,
    "49_real_world_context_bridge_truss_parallel_struts": arch_49_real_world_context_bridge_truss_parallel_struts,
    "50_compound_multi_line_geometric_synthesis": arch_50_compound_multi_line_geometric_synthesis,
}

SUBSKILLS: List[str] = list(ARCHETYPE_MAP.keys())
ARCHETYPES: List[str] = SUBSKILLS
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate_grade9_geometry_straight_lines_question(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates a single Grade 9 Geometry of Straight Lines question."""
    r = random.Random(seed)
    if subskill and subskill in ARCHETYPE_MAP:
        chosen_subskill = subskill
        builder = ARCHETYPE_MAP[subskill]
    else:
        chosen_subskill = r.choice(SUBSKILLS)
        builder = ARCHETYPE_MAP[chosen_subskill]

    q = builder(r)
    q["subskill"] = chosen_subskill
    q["grade"] = "9"
    q["subject"] = "Mathematics"
    q["topic"] = "Geometry of straight lines"
    q["term"] = 2
    q["learning_objective_id"] = f"g9_geom_lines_{chosen_subskill}"
    q["archetype"] = chosen_subskill

    # Sync prompt and question text
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

    # Worked solution from hints or marking schema
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

    q.setdefault("caps_weight_percent", 15)
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
        q = generate_grade9_geometry_straight_lines_question(seed=sub_seed, subskill=sub, **kwargs)
        questions.append(q)

    return questions
