"""Grade 9 Mathematics deterministic question generators.
6-Pillar Generator Contract compliant, zero-LLM, 100% aligned with South African National Curriculum Standards.
Covers all 24 topics across Terms 1 to 4.
"""
from app.utils.grade9_mathematics.whole_numbers_generator import (
    generate as generate_whole_numbers,
    generate_grade9_whole_numbers_question,
)
from app.utils.grade9_mathematics.integers_generator import (
    generate as generate_integers,
    generate_grade9_integers_question,
)
from app.utils.grade9_mathematics.decimal_notation_generator import (
    generate as generate_decimal_notation,
    generate_grade9_decimal_notation_question,
)
from app.utils.grade9_mathematics.exponents_generator import (
    generate as generate_exponents,
    generate_grade9_exponents_question,
)
from app.utils.grade9_mathematics.patterns_generator import (
    generate as generate_patterns,
    generate_grade9_patterns_question,
)
from app.utils.grade9_mathematics.functions_generator import (
    generate as generate_functions,
    generate_grade9_functions_relationships_question,
)
from app.utils.grade9_mathematics.algebraic_expressions_generator import (
    generate as generate_algebraic_expressions,
    generate_grade9_algebraic_expressions_question,
)
from app.utils.grade9_mathematics.factorisation_generator import (
    generate as generate_factorisation,
)
from app.utils.grade9_mathematics.algebraic_equations_generator import (
    generate as generate_algebraic_equations,
    generate_grade9_algebraic_equations_question,
)
from app.utils.grade9_mathematics.algebraic_equations_fractions_generator import (
    generate as generate_algebraic_equations_fractions,
)
from app.utils.grade9_mathematics.fractions_generator import (
    generate as generate_fractions,
    generate_grade9_fractions_question,
)
from app.utils.grade9_mathematics.graphs_generator import (
    generate as generate_graphs,
    generate_grade9_graphs_question,
)
from app.utils.grade9_mathematics.geometry_straight_lines_generator import (
    generate as generate_geometry_straight_lines,
    generate_grade9_geometry_straight_lines_question,
)
from app.utils.grade9_mathematics.geometry_2d_shapes_generator import (
    generate as generate_geometry_2d_shapes,
    generate_grade9_geometry_2d_shapes_question,
)
from app.utils.grade9_mathematics.construction_generator import (
    generate as generate_construction,
    generate_grade9_construction_question,
)
from app.utils.grade9_mathematics.transformation_geometry_generator import (
    generate as generate_transformation_geometry,
    generate_grade9_transformation_geometry_question,
)
from app.utils.grade9_mathematics.pythagoras_generator import (
    generate as generate_pythagoras,
    generate_grade9_pythagoras_question,
)
from app.utils.grade9_mathematics.area_perimeter_2d_generator import (
    generate as generate_area_perimeter_2d,
    generate_grade9_area_perimeter_2d_question,
)
from app.utils.grade9_mathematics.geometry_3d_objects_generator import (
    generate as generate_geometry_3d_objects,
    generate_grade9_geometry_3d_objects_question,
)
from app.utils.grade9_mathematics.measurement_3d_generator import (
    generate as generate_measurement_3d,
    generate_grade9_measurement_3d_question,
)
from app.utils.grade9_mathematics.data_summarise_generator import (
    generate as generate_data_summarise,
    generate_grade9_data_summarise_question,
)
from app.utils.grade9_mathematics.data_represent_generator import (
    generate as generate_data_represent,
    generate_grade9_data_represent_question,
)
from app.utils.grade9_mathematics.data_interpret_generator import (
    generate as generate_data_interpret,
    generate_grade9_data_interpret_question,
)
from app.utils.grade9_mathematics.probability_generator import (
    generate as generate_probability,
    generate_grade9_probability_question,
)
# Backward-compatibility alias
from app.utils.grade9_mathematics.geometry_straight_lines_triangles_generator import (
    generate as generate_geometry_straight_lines_triangles,
)
from app.utils.grade9_mathematics.congruence_similarity_generator import (
    generate as generate_congruence_similarity,
)

__all__ = [
    "generate_whole_numbers",
    "generate_grade9_whole_numbers_question",
    "generate_integers",
    "generate_grade9_integers_question",
    "generate_decimal_notation",
    "generate_grade9_decimal_notation_question",
    "generate_exponents",
    "generate_grade9_exponents_question",
    "generate_patterns",
    "generate_grade9_patterns_question",
    "generate_functions",
    "generate_grade9_functions_relationships_question",
    "generate_algebraic_expressions",
    "generate_grade9_algebraic_expressions_question",
    "generate_factorisation",
    "generate_algebraic_equations",
    "generate_grade9_algebraic_equations_question",
    "generate_algebraic_equations_fractions",
    "generate_fractions",
    "generate_grade9_fractions_question",
    "generate_graphs",
    "generate_grade9_graphs_question",
    "generate_geometry_straight_lines",
    "generate_grade9_geometry_straight_lines_question",
    "generate_geometry_2d_shapes",
    "generate_grade9_geometry_2d_shapes_question",
    "generate_construction",
    "generate_grade9_construction_question",
    "generate_transformation_geometry",
    "generate_grade9_transformation_geometry_question",
    "generate_pythagoras",
    "generate_grade9_pythagoras_question",
    "generate_area_perimeter_2d",
    "generate_grade9_area_perimeter_2d_question",
    "generate_geometry_3d_objects",
    "generate_grade9_geometry_3d_objects_question",
    "generate_measurement_3d",
    "generate_grade9_measurement_3d_question",
    "generate_data_summarise",
    "generate_grade9_data_summarise_question",
    "generate_data_represent",
    "generate_grade9_data_represent_question",
    "generate_data_interpret",
    "generate_grade9_data_interpret_question",
    "generate_probability",
    "generate_grade9_probability_question",
    "generate_geometry_straight_lines_triangles",
    "generate_congruence_similarity",
]
