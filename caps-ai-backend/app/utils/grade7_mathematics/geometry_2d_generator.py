"""
Grade 7 Mathematics - Geometry of 2D Shapes Generator (50 Semantic Archetypes).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of 2D shapes.md.
"""
from __future__ import annotations
import random
from typing import Any, Callable, Dict, List, Optional

from .geometry_2d_archetypes_01_25 import (
    arch_01_classify_triangle_by_sides,
    arch_02_classify_triangle_by_angles,
    arch_03_equilateral_triangle_angle_property,
    arch_04_isosceles_base_angle_property,
    arch_05_right_angled_isosceles_angles,
    arch_06_scalene_triangle_properties,
    arch_07_geometric_impossibility_two_obtuse_angles,
    arch_08_adjacent_vs_opposite_sides,
    arch_09_missing_angle_scalene_triangle,
    arch_10_missing_acute_angle_right_triangle,
    arch_11_base_angles_isosceles_triangle,
    arch_12_vertex_angle_isosceles_from_base,
    arch_13_exterior_angle_of_triangle,
    arch_14_equilateral_triangle_solve_variable,
    arch_15_algebraic_angles_in_triangle,
    arch_16_overlapping_composite_triangles,
    arch_17_properties_of_rectangle,
    arch_18_properties_of_square,
    arch_19_properties_of_parallelogram,
    arch_20_properties_of_rhombus,
    arch_21_properties_of_trapezium,
    arch_22_properties_of_kite,
    arch_23_distinguish_square_from_rhombus,
    arch_24_distinguish_rectangle_from_parallelogram,
    arch_25_quadrilateral_hierarchy_true_false,
)

from .geometry_2d_archetypes_26_50 import (
    arch_26_quadrilateral_interior_angle_sum,
    arch_27_missing_fourth_angle_quadrilateral,
    arch_28_opposite_angles_in_parallelogram,
    arch_29_consecutive_angles_in_parallelogram,
    arch_30_angles_in_a_rhombus,
    arch_31_angles_in_a_kite,
    arch_32_isosceles_trapezium_angles,
    arch_33_trapezium_cointerior_angles,
    arch_34_algebraic_angles_quadrilateral,
    arch_35_congruent_shapes_definition,
    arch_36_similar_shapes_definition,
    arch_37_congruence_condition_sss,
    arch_38_congruence_condition_sas,
    arch_39_congruence_condition_asa,
    arch_40_congruence_condition_rhs,
    arch_41_scale_factor_similar_triangles,
    arch_42_missing_side_in_similar_triangles,
    arch_43_identify_circle_lines_on_diagram,
    arch_44_radius_diameter_conversion,
    arch_45_angle_in_a_semicircle,
    arch_46_regular_vs_irregular_polygons,
    arch_47_pentagon_properties_and_angle_sum,
    arch_48_hexagon_properties_and_angle_sum,
    arch_49_number_of_diagonals_in_polygon,
    arch_50_line_symmetry_of_quadrilaterals,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    # 01 - 08: Triangle Classification & Properties
    arch_01_classify_triangle_by_sides,
    arch_02_classify_triangle_by_angles,
    arch_03_equilateral_triangle_angle_property,
    arch_04_isosceles_base_angle_property,
    arch_05_right_angled_isosceles_angles,
    arch_06_scalene_triangle_properties,
    arch_07_geometric_impossibility_two_obtuse_angles,
    arch_08_adjacent_vs_opposite_sides,
    # 09 - 16: Triangle Interior Angles Calculation
    arch_09_missing_angle_scalene_triangle,
    arch_10_missing_acute_angle_right_triangle,
    arch_11_base_angles_isosceles_triangle,
    arch_12_vertex_angle_isosceles_from_base,
    arch_13_exterior_angle_of_triangle,
    arch_14_equilateral_triangle_solve_variable,
    arch_15_algebraic_angles_in_triangle,
    arch_16_overlapping_composite_triangles,
    # 17 - 25: Quadrilateral Classification & Properties
    arch_17_properties_of_rectangle,
    arch_18_properties_of_square,
    arch_19_properties_of_parallelogram,
    arch_20_properties_of_rhombus,
    arch_21_properties_of_trapezium,
    arch_22_properties_of_kite,
    arch_23_distinguish_square_from_rhombus,
    arch_24_distinguish_rectangle_from_parallelogram,
    arch_25_quadrilateral_hierarchy_true_false,
    # 26 - 34: Quadrilateral Interior Angles Calculation
    arch_26_quadrilateral_interior_angle_sum,
    arch_27_missing_fourth_angle_quadrilateral,
    arch_28_opposite_angles_in_parallelogram,
    arch_29_consecutive_angles_in_parallelogram,
    arch_30_angles_in_a_rhombus,
    arch_31_angles_in_a_kite,
    arch_32_isosceles_trapezium_angles,
    arch_33_trapezium_cointerior_angles,
    arch_34_algebraic_angles_quadrilateral,
    # 35 - 42: Congruence & Similarity
    arch_35_congruent_shapes_definition,
    arch_36_similar_shapes_definition,
    arch_37_congruence_condition_sss,
    arch_38_congruence_condition_sas,
    arch_39_congruence_condition_asa,
    arch_40_congruence_condition_rhs,
    arch_41_scale_factor_similar_triangles,
    arch_42_missing_side_in_similar_triangles,
    # 43 - 50: Circles, Polygons & Line Symmetry
    arch_43_identify_circle_lines_on_diagram,
    arch_44_radius_diameter_conversion,
    arch_45_angle_in_a_semicircle,
    arch_46_regular_vs_irregular_polygons,
    arch_47_pentagon_properties_and_angle_sum,
    arch_48_hexagon_properties_and_angle_sum,
    arch_49_number_of_diagonals_in_polygon,
    arch_50_line_symmetry_of_quadrilaterals,
]

SUBSKILLS: List[str] = [
    # 01 - 08
    "01_classify_triangle_by_sides",
    "02_classify_triangle_by_angles",
    "03_equilateral_triangle_angle_property",
    "04_isosceles_base_angle_property",
    "05_right_angled_isosceles_angles",
    "06_scalene_triangle_properties",
    "07_geometric_impossibility_two_obtuse_angles",
    "08_adjacent_vs_opposite_sides",
    # 09 - 16
    "09_missing_angle_scalene_triangle",
    "10_missing_acute_angle_right_triangle",
    "11_base_angles_isosceles_triangle",
    "12_vertex_angle_isosceles_from_base",
    "13_exterior_angle_of_triangle",
    "14_equilateral_triangle_solve_variable",
    "15_algebraic_angles_in_triangle",
    "16_overlapping_composite_triangles",
    # 17 - 25
    "17_properties_of_rectangle",
    "18_properties_of_square",
    "19_properties_of_parallelogram",
    "20_properties_of_rhombus",
    "21_properties_of_trapezium",
    "22_properties_of_kite",
    "23_distinguish_square_from_rhombus",
    "24_distinguish_rectangle_from_parallelogram",
    "25_quadrilateral_hierarchy_true_false",
    # 26 - 34
    "26_quadrilateral_interior_angle_sum",
    "27_missing_fourth_angle_quadrilateral",
    "28_opposite_angles_in_parallelogram",
    "29_consecutive_angles_in_parallelogram",
    "30_angles_in_a_rhombus",
    "31_angles_in_a_kite",
    "32_isosceles_trapezium_angles",
    "33_trapezium_cointerior_angles",
    "34_algebraic_angles_quadrilateral",
    # 35 - 42
    "35_congruent_shapes_definition",
    "36_similar_shapes_definition",
    "37_congruence_condition_sss",
    "38_congruence_condition_sas",
    "39_congruence_condition_asa",
    "40_congruence_condition_rhs",
    "41_scale_factor_similar_triangles",
    "42_missing_side_in_similar_triangles",
    # 43 - 50
    "43_identify_circle_lines_on_diagram",
    "44_radius_diameter_conversion",
    "45_angle_in_a_semicircle",
    "46_regular_vs_irregular_polygons",
    "47_pentagon_properties_and_angle_sum",
    "48_hexagon_properties_and_angle_sum",
    "49_number_of_diagonals_in_polygon",
    "50_line_symmetry_of_quadrilaterals",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    s: b for s, b in zip(SUBSKILLS, BUILDERS)
}

# 1-based index aliases
for idx, b in enumerate(BUILDERS, 1):
    DISPATCH_TABLE[idx] = b
    DISPATCH_TABLE[f"{idx:02d}"] = b

# Backward compatibility aliases for legacy subskill names
DISPATCH_TABLE["circle_radius_diameter"] = arch_44_radius_diameter_conversion
DISPATCH_TABLE["triangle_interior_angles"] = arch_09_missing_angle_scalene_triangle
DISPATCH_TABLE["quadrilateral_interior_angles"] = arch_27_missing_fourth_angle_quadrilateral
DISPATCH_TABLE["rectangle_definition"] = arch_17_properties_of_rectangle
DISPATCH_TABLE["isosceles_identification"] = arch_04_isosceles_base_angle_property
DISPATCH_TABLE["kite_definition"] = arch_22_properties_of_kite
DISPATCH_TABLE["trapezium_definition"] = arch_21_properties_of_trapezium
DISPATCH_TABLE["circle_definitions"] = arch_43_identify_circle_lines_on_diagram
DISPATCH_TABLE["right_isosceles_angles"] = arch_05_right_angled_isosceles_angles
DISPATCH_TABLE["equilateral_triangle_angle"] = arch_03_equilateral_triangle_angle_property


def get_subskills() -> List[str]:
    """Returns the list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Geometry of 2D Shapes Generator.
    Supports exact archetype dispatch via subskill or archetype_index, and compound mode.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None

        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            idx = int(archetype_index)
            if idx in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[idx]
            elif 1 <= idx <= len(BUILDERS):
                builder = BUILDERS[idx - 1]

        if builder is None:
            builder = rng.choice(BUILDERS)

        q = builder(rng)
        q.setdefault("grade", 7)
        q.setdefault("subject", "Mathematics")
        q.setdefault("topic", "Geometry of 2D shapes")
        q.setdefault("term", 1)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions
