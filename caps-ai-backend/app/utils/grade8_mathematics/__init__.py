"""Grade 8 Mathematics deterministic 6-pillar question generators."""
from __future__ import annotations

from app.utils.grade8_mathematics.pythagoras_generator import (
    generate as generate_pythagoras,
)
from app.utils.grade8_mathematics.integers_generator import (
    generate as generate_integers,
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

__all__ = [
    "generate_pythagoras",
    "generate_integers",
    "generate_algebra",
    "generate_geometry_straight_lines",
    "generate_measurement_3d",
    "generate_fractions_decimals",
    "generate_geometry_2d_shapes",
    "generate_geometry_3d_objects",
]
