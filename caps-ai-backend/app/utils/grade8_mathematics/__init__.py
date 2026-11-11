"""Grade 8 Mathematics deterministic 6-pillar question generators."""
from __future__ import annotations

from app.utils.grade8_mathematics.pythagoras_generator import (
    generate as generate_pythagoras,
)
from app.utils.grade8_mathematics.integers_generator import (
    generate as generate_integers,
)
from app.utils.grade8_mathematics.whole_numbers_generator import (
    generate as generate_whole_numbers,
)
from app.utils.grade8_mathematics.exponents_generator import (
    generate as generate_exponents,
)
from app.utils.grade8_mathematics.patterns_generator import (
    generate as generate_patterns,
)
from app.utils.grade8_mathematics.algebraic_expressions_equations_generator import (
    generate as generate_algebra,
)
from app.utils.grade8_mathematics.geometry_straight_lines_generator import (
    generate as generate_geometry_straight_lines,
)
from app.utils.grade8_mathematics.measurement_3d_generator import (
    generate as generate_measurement_3d,
)
from app.utils.grade8_mathematics.fractions_decimals_generator import (
    generate as generate_fractions_decimals,
)
from app.utils.grade8_mathematics.geometry_2d_shapes_generator import (
    generate as generate_geometry_2d_shapes,
)
from app.utils.grade8_mathematics.geometry_3d_objects_generator import (
    generate as generate_geometry_3d_objects,
)
from app.utils.grade8_mathematics.probability_generator import (
    generate as generate_probability,
)

from . import (
    algebraic_expressions_1_generator,
    algebraic_expressions_2_generator,
    algebraic_equations_1_generator,
    algebraic_equations_2_generator,
    algebraic_equations_3_generator,
    functions_relationships_1_generator,
    functions_relationships_2_generator,
    graphs_generator,
    data_collect_organise_generator,
    data_representation_generator,
    data_measures_generator,
    perimeter_area_2d_generator,
    construction_generator,
    transformation_geometry_generator,
    decimal_fractions_generator,
    whole_numbers_generator,
    exponents_generator,
    patterns_generator,
    probability_generator,
)

__all__ = [
    "generate_pythagoras",
    "generate_integers",
    "generate_whole_numbers",
    "generate_exponents",
    "generate_patterns",
    "generate_algebra",
    "generate_geometry_straight_lines",
    "generate_measurement_3d",
    "generate_fractions_decimals",
    "generate_geometry_2d_shapes",
    "generate_geometry_3d_objects",
    "generate_probability",
    "algebraic_expressions_1_generator",
    "algebraic_expressions_2_generator",
    "algebraic_equations_1_generator",
    "algebraic_equations_2_generator",
    "algebraic_equations_3_generator",
    "functions_relationships_1_generator",
    "functions_relationships_2_generator",
    "graphs_generator",
    "data_collect_organise_generator",
    "data_representation_generator",
    "data_measures_generator",
    "perimeter_area_2d_generator",
    "construction_generator",
    "transformation_geometry_generator",
    "decimal_fractions_generator",
    "probability_generator",
]
