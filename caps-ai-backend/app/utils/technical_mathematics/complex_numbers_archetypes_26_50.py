"""Grade 12 Technical Mathematics — Complex Numbers: Archetypes 26–50
===================================================================
100% Aligned with South African National Curriculum Standards.
Grounded strictly in curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/01. Complex numbers.md.

Combines subskills 26–38 (polar operations, de Moivre powers, complex roots, Argand polygon geometry)
and 39–50 (higher roots, roots of unity, quadratic & cubic equations in C, and AC electrical impedance Z = R + jX).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict

from app.utils.technical_mathematics.complex_numbers_archetypes_26_38 import (
    BUILDERS_26_38,
)
from app.utils.technical_mathematics.complex_numbers_archetypes_39_50 import (
    BUILDERS_39_50,
    SUBSKILLS_39_50,
)

BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_26_38,
    **BUILDERS_39_50,
}

SUBSKILLS_26_50: Dict[str, str] = {
    "26_polar_multiplication_moduli_and_arguments": "Multiplication of Complex Numbers in Polar Form",
    "27_polar_multiplication_angle_reduction": "Polar Multiplication with Argument Reduction",
    "28_polar_division_moduli_and_arguments": "Division of Complex Numbers in Polar Form",
    "29_polar_division_negative_angle_adjustment": "Polar Division with Negative Angle Adjustment",
    "30_polar_combined_multiplication_and_division": "Combined Polar Multiplication and Division Operations",
    "31_de_moivre_theorem_small_positive_power": "de Moivre's Theorem for Small Positive Integer Powers",
    "32_de_moivre_theorem_higher_power_with_angle_reduction": "de Moivre's Theorem for Higher Powers with Angle Reduction",
    "33_de_moivre_theorem_convert_to_rectangular": "de Moivre's Theorem with Conversion Back to Rectangular Form",
    "34_de_moivre_theorem_negative_integer_power": "de Moivre's Theorem for Negative Integer Powers",
    "35_complex_square_roots_polar_form": "Determination of Complex Square Roots in Polar Form",
    "36_complex_cube_roots_polar_form": "Determination of Complex Cube Roots in Polar Form",
    "37_argand_roots_regular_polygon_geometry": "Geometric Representation of Complex Roots on Argand Plane",
    "38_rectangular_to_polar_then_de_moivre": "Rectangular to Polar Conversion with de Moivre Evaluation",
    **SUBSKILLS_39_50,
}
