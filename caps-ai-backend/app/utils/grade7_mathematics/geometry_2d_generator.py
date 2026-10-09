"""
Grade 7 Mathematics - Geometry of 2D Shapes Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/END OF YEAR EXAM 2018.md (Q1.4, Q1.5, Q1.9, Q1.10, Q7.1, Q7.3, Q7.4)
and curriculum_docs/Mathematics_Gr7/Geometry of 2D Shapes.md.

Archetypes Covered:
1. Missing angle in triangle with geometric reason (Sum of interior angles of triangle = 180°)
2. Missing angle in quadrilateral with geometric reason (Sum of interior angles of quadrilateral = 360°)
3. Properties & classification of triangles (Equilateral, Isosceles, Scalene, Right-angled)
4. Properties & classification of quadrilaterals (Parallelogram, Rectangle, Rhombus, Square, Trapezium, Kite)
5. Lines & Circles (Parallel, Perpendicular, Radius, Diameter, Chord)
"""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


# ============================================================================
# ARCHETYPE 1: Triangle Interior Angles (Exam Q7.3.2, Q1.9)
# ============================================================================

def _generate_triangle_interior_angle(rng: random.Random, is_right_angled: bool = False) -> Dict[str, Any]:
    """
    Calculate unknown interior angle in a triangle with geometric reason.
    Exam Q7.3.2: Triangle with angles 45°, 31° and y -> y = 180° - 76° = 104°.
    Exam Q1.9: Right-angled triangle with angles 90°, 40° and x -> x = 50°.
    """
    triangle_names = ["ABC", "PQR", "KLM", "DEF", "XYZ"]
    tri = rng.choice(triangle_names)
    v1, v2, v3 = tri[0], tri[1], tri[2]

    var = rng.choice(["x", "y", "a", "b", "θ"])

    if is_right_angled or rng.random() < 0.35:
        # Right angled triangle
        angle1 = 90
        angle2 = rng.randint(20, 75)
        unknown_angle = 180 - angle1 - angle2
        known_desc = f"\\(\\hat{{{v1}}} = 90^\\circ\\) and \\(\\hat{{{v2}}} = {angle2}^\\circ\\)"
        prompt = (
            f"In \\(\\Delta {tri}\\), the angle at {v1} is a right angle ({known_desc}) "
            f"and the angle at {v3} is \\({var}\\).\n\n"
            f"Calculate, with a geometric reason, the value of \\({var}\\)."
        )
        t3_calc = f"180^\\circ - (90^\\circ + {angle2}^\\circ) = 180^\\circ - {90 + angle2}^\\circ = {unknown_angle}^\\circ"
    else:
        # General triangle
        angle1 = rng.randint(30, 85)
        angle2 = rng.randint(25, 140 - angle1)
        unknown_angle = 180 - angle1 - angle2
        known_desc = f"\\(\\hat{{{v1}}} = {angle1}^\\circ\\) and \\(\\hat{{{v2}}} = {angle2}^\\circ\\)"
        prompt = (
            f"In \\(\\Delta {tri}\\), {known_desc} and \\(\\hat{{{v3}}} = {var}\\).\n\n"
            f"Calculate, with a geometric reason, the size of \\({var}\\)."
        )
        t3_calc = f"180^\\circ - ({angle1}^\\circ + {angle2}^\\circ) = 180^\\circ - {angle1 + angle2}^\\circ = {unknown_angle}^\\circ"

    reason = "Sum of interior angles of a triangle = 180° (or int. ∠s of Δ = 180°)"
    canonical_sol = (
        f"Step 1: State the sum of angles equation:\n"
        f"\\({var} + {angle1}^\\circ + {angle2}^\\circ = 180^\\circ\\) [{reason}]\n\n"
        f"Step 2: Add known angles:\n"
        f"\\({var} + {angle1 + angle2}^\\circ = 180^\\circ\\)\n\n"
        f"Step 3: Solve for {var}:\n"
        f"\\({var} = {t3_calc}\\)\n"
        f"Therefore, \\({var} = {unknown_angle}^\\circ\\)."
    )

    return {
        "id": f"g7_math_geom2d_tri_ang_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"{unknown_angle}",
        "answer_latex": f"{unknown_angle}^\\circ",
        "explanation": canonical_sol,
        "canonical_solution": canonical_sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "triangle_interior_angles",
        "learning_objective_id": "math_g7_geom_triangle_angles",
        "misconception_tags": [
            "confused_triangle_and_quad_angle_sum",
            "arithmetic_subtraction_error",
            "omitted_geometric_reason"
        ],
        "diagnostic_tags": ["geometry_2d", "triangles", "interior_angles"],
        "minimum_mastery_score": 75,
        "keywords": ["triangle", "interior angles", "180 degrees", "solve for unknown angle"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Setting up equation with known angles totaling 180°", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct geometric reason (sum of int ∠s of Δ = 180°)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct numerical value for {var} ({unknown_angle}°)", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"The three inside angles of any triangle always add up to a fixed total.",
            "tier_2": f"The interior angles of a triangle add up to 180°. Subtract the two known angles from 180°.",
            "tier_3": f"{var} = {t3_calc}."
        }
    }


# ============================================================================
# ARCHETYPE 2: Quadrilateral Interior Angles (Exam Q7.3.1)
# ============================================================================

def _generate_quadrilateral_interior_angle(rng: random.Random) -> Dict[str, Any]:
    """
    Calculate unknown interior angle in a quadrilateral with geometric reason.
    Exam Q7.3.1: Quadrilateral with angles 68°, 75°, 90° and x -> x = 360° - 233° = 127°.
    """
    quad_names = ["ABCD", "PQRS", "KLMN", "EFGH"]
    quad = rng.choice(quad_names)
    v1, v2, v3, v4 = quad[0], quad[1], quad[2], quad[3]
    var = rng.choice(["x", "y", "w", "z"])

    # Pick 3 realistic angles whose sum is between 180° and 320°
    a1 = rng.choice([90, rng.randint(60, 110)])
    a2 = rng.randint(65, 115)
    a3 = rng.randint(70, 110)
    sum_known = a1 + a2 + a3
    unknown_angle = 360 - sum_known

    reason = "Sum of interior angles of a quadrilateral = 360° (or int. ∠s of quad = 360°)"
    prompt = (
        f"In quadrilateral \\({quad}\\), three of the interior angles are given as:\n"
        f"\\(\\hat{{{v1}}} = {a1}^\\circ\\), \\(\\hat{{{v2}}} = {a2}^\\circ\\), and \\(\\hat{{{v3}}} = {a3}^\\circ\\).\n"
        f"The fourth interior angle is \\(\\hat{{{v4}}} = {var}\\).\n\n"
        f"Calculate, with a geometric reason, the size of \\({var}\\)."
    )

    canonical_sol = (
        f"Step 1: State the angle sum equation:\n"
        f"\\({var} + {a1}^\\circ + {a2}^\\circ + {a3}^\\circ = 360^\\circ\\) [{reason}]\n\n"
        f"Step 2: Add the three known angles:\n"
        f"\\({var} + {sum_known}^\\circ = 360^\\circ\\)\n\n"
        f"Step 3: Solve for \\({var}\\):\n"
        f"\\({var} = 360^\\circ - {sum_known}^\\circ = {unknown_angle}^\\circ\\)."
    )

    return {
        "id": f"g7_math_geom2d_quad_ang_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"{unknown_angle}",
        "answer_latex": f"{unknown_angle}^\\circ",
        "explanation": canonical_sol,
        "canonical_solution": canonical_sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "quadrilateral_interior_angles",
        "learning_objective_id": "math_g7_geom_quad_angles",
        "misconception_tags": [
            "confused_triangle_and_quad_angle_sum",
            "arithmetic_subtraction_error",
            "omitted_geometric_reason"
        ],
        "diagnostic_tags": ["geometry_2d", "quadrilaterals", "interior_angles"],
        "minimum_mastery_score": 75,
        "keywords": ["quadrilateral", "interior angles", "360 degrees", "four-sided figure"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Summing known angles to set up equation equaling 360°", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Geometric reason (sum of interior angles of quad = 360°)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct final calculated value ({unknown_angle}°)", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Any four-sided polygon (quadrilateral) can be split into two triangles.",
            "tier_2": f"The four interior angles of a quadrilateral always add up to 360°. Add the 3 known angles ({a1}° + {a2}° + {a3}° = {sum_known}°), then subtract from 360°.",
            "tier_3": f"{var} = 360° - {sum_known}° = {unknown_angle}°."
        }
    }


# ============================================================================
# ARCHETYPE 3: Triangle Classification & Properties (Exam Q1.4, Q7.1.1)
# ============================================================================

def _generate_triangle_classification(rng: random.Random) -> Dict[str, Any]:
    """
    Questions testing properties of triangles:
    Equilateral, Isosceles, Scalene, Right-angled.
    Exam Q1.4: "Each angle in an equilateral triangle is: 60°"
    """
    scenarios = [
        {
            "prompt": "An equilateral triangle has three sides of equal length. What is the size of each interior angle in an equilateral triangle?",
            "correct": "60",
            "unit": "°",
            "options": ["60°", "30°", "90°", "180°"],
            "explanation": "Because an equilateral triangle has three equal sides, all three interior angles are equal. Since the angles add up to 180°, each angle is 180° ÷ 3 = 60°.",
            "subskill": "equilateral_triangle_angle",
            "h1": "All three angles in an equilateral triangle are identical.",
            "h2": "Divide 180° equally among the 3 interior angles.",
            "h3": "180° ÷ 3 = 60°."
        },
        {
            "prompt": "A triangle has side lengths of 7 cm, 7 cm, and 10 cm. Based on its side lengths, what specific type of triangle is it?",
            "correct": "Isosceles",
            "unit": "",
            "options": ["Isosceles", "Equilateral", "Scalene", "Right-angled"],
            "explanation": "A triangle with exactly two sides of equal length is called an isosceles triangle.",
            "subskill": "isosceles_identification",
            "h1": "Notice that two of the side lengths are exactly the same (7 cm and 7 cm).",
            "h2": "A triangle with two equal sides has a name that starts with 'Iso-'.",
            "h3": "The answer is Isosceles triangle."
        },
        {
            "prompt": "A triangle has side lengths of 5 cm, 8 cm, and 11 cm, with no equal sides and no 90° angle. What type of triangle is it?",
            "correct": "Scalene",
            "unit": "",
            "options": ["Scalene", "Isosceles", "Equilateral", "Right-angled"],
            "explanation": "A triangle where all three sides have different lengths is called a scalene triangle.",
            "subskill": "scalene_identification",
            "h1": "Check if any sides are equal.",
            "h2": "When all 3 sides have different lengths, the triangle is classified as scalene.",
            "h3": "The answer is Scalene."
        },
        {
            "prompt": "In a right-angled isosceles triangle, one angle is 90°. What is the size of each of the other two equal angles?",
            "correct": "45",
            "unit": "°",
            "options": ["45°", "30°", "60°", "90°"],
            "explanation": "The sum of angles is 180°. The remaining two angles must add up to 180° - 90° = 90°. Since they are equal, each is 90° ÷ 2 = 45°.",
            "subskill": "right_isosceles_angles",
            "h1": "Subtract the 90° right angle from 180° to find the total of the other two angles.",
            "h2": "180° - 90° = 90°. Since the triangle is isosceles, the base angles are equal.",
            "h3": "90° ÷ 2 = 45°."
        }
    ]

    scen = rng.choice(scenarios)
    options = list(scen["options"])
    rng.shuffle(options)

    return {
        "id": f"g7_math_geom2d_tri_class_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": scen["prompt"],
        "prompt_latex": scen["prompt"],
        "options": options,
        "options_latex": options,
        "answer_mode": "choice",
        "correct_answer": f"{scen['correct']}{scen['unit']}" if scen['unit'] else scen['correct'],
        "answer_latex": f"{scen['correct']}{scen['unit']}" if scen['unit'] else scen['correct'],
        "explanation": scen["explanation"],
        "canonical_solution": scen["explanation"],
        "marks": 2,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "subskill": scen["subskill"],
        "learning_objective_id": "math_g7_geom_tri_properties",
        "misconception_tags": [
            "confused_equilateral_and_isosceles",
            "scalene_definition_slip"
        ],
        "diagnostic_tags": ["geometry_2d", "triangles", "classification"],
        "minimum_mastery_score": 75,
        "keywords": ["equilateral", "isosceles", "scalene", "triangle properties"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of triangle geometric property", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct answer selection", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "tier_1": scen["h1"],
            "tier_2": scen["h2"],
            "tier_3": scen["h3"]
        }
    }


# ============================================================================
# ARCHETYPE 4: Quadrilateral Classification & Properties (Exam Q1.5, Q1.10, Q7.1.3, Q7.1.5)
# ============================================================================

def _generate_quadrilateral_classification(rng: random.Random) -> Dict[str, Any]:
    """
    Questions testing properties of quadrilaterals:
    Parallelogram, Rectangle, Rhombus, Square, Trapezium, Kite.
    Exam Q1.5: Parallelogram with opposite parallel sides.
    Exam Q1.10: Identify which is NOT a quadrilateral (Pentagon).
    Exam Q7.1.5: Quadrilateral with 1 pair of parallel sides (Trapezium).
    """
    scenarios = [
        {
            "prompt": "A quadrilateral has exactly ONE pair of opposite sides that are parallel. What is the name of this quadrilateral?",
            "correct": "Trapezium",
            "options": ["Trapezium", "Parallelogram", "Rhombus", "Rectangle"],
            "explanation": "A trapezium is defined as a quadrilateral with exactly one pair of opposite sides parallel.",
            "subskill": "trapezium_definition",
            "h1": "Parallelograms have two pairs of parallel sides. This shape only has one pair.",
            "h2": "A quadrilateral with only one pair of parallel sides is called a trapezium.",
            "h3": "The answer is Trapezium."
        },
        {
            "prompt": "A quadrilateral has both pairs of opposite sides parallel, and ALL FOUR sides are equal in length, but none of its angles are 90°. What is the shape called?",
            "correct": "Rhombus",
            "options": ["Rhombus", "Square", "Rectangle", "Trapezium"],
            "explanation": "A quadrilateral with all four sides equal and opposite sides parallel, but without right angles, is a rhombus.",
            "subskill": "rhombus_definition",
            "h1": "If it had 90° angles, it would be a square.",
            "h2": "A slanted shape with all four sides equal is a rhombus.",
            "h3": "The answer is Rhombus."
        },
        {
            "prompt": "Which of the following polygons is NOT an example of a quadrilateral?",
            "correct": "Pentagon",
            "options": ["Pentagon", "Trapezium", "Parallelogram", "Rhombus"],
            "explanation": "A quadrilateral is a 4-sided polygon. A pentagon has 5 sides, so it is not a quadrilateral.",
            "subskill": "quadrilateral_non_example",
            "h1": "A quadrilateral must have exactly 4 straight sides.",
            "h2": "Count the number of sides: Pentagon has 5 sides.",
            "h3": "The answer is Pentagon."
        },
        {
            "prompt": "A quadrilateral has two pairs of adjacent sides that are equal in length, but opposite sides are NOT equal. What is the name of this quadrilateral?",
            "correct": "Kite",
            "options": ["Kite", "Parallelogram", "Rectangle", "Trapezium"],
            "explanation": "A kite has two distinct pairs of adjacent equal sides, with one pair of opposite angles equal.",
            "subskill": "kite_definition",
            "h1": "Think of the traditional flying shape with two shorter equal sides at the top and two longer equal sides below.",
            "h2": "The shape is called a kite.",
            "h3": "The answer is Kite."
        },
        {
            "prompt": "A parallelogram has opposite sides equal and parallel. If all four interior angles are 90°, what special parallelogram is it?",
            "correct": "Rectangle",
            "options": ["Rectangle", "Rhombus", "Trapezium", "Kite"],
            "explanation": "A rectangle is a parallelogram with four right angles (90°).",
            "subskill": "rectangle_definition",
            "h1": "Opposite sides are equal and all corner angles are right angles (90°).",
            "h2": "This is the definition of a rectangle.",
            "h3": "The answer is Rectangle."
        }
    ]

    scen = rng.choice(scenarios)
    options = list(scen["options"])
    rng.shuffle(options)

    return {
        "id": f"g7_math_geom2d_quad_class_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": scen["prompt"],
        "prompt_latex": scen["prompt"],
        "options": options,
        "options_latex": options,
        "answer_mode": "choice",
        "correct_answer": scen["correct"],
        "answer_latex": scen["correct"],
        "explanation": scen["explanation"],
        "canonical_solution": scen["explanation"],
        "marks": 2,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "subskill": scen["subskill"],
        "learning_objective_id": "math_g7_geom_quad_properties",
        "misconception_tags": [
            "rhombus_vs_parallelogram_confusion",
            "trapezium_vs_parallelogram_confusion"
        ],
        "diagnostic_tags": ["geometry_2d", "quadrilaterals", "classification"],
        "minimum_mastery_score": 75,
        "keywords": ["quadrilateral", "trapezium", "rhombus", "rectangle", "kite", "parallelogram"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Knowledge of quadrilateral properties", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct shape classification", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "tier_1": scen["h1"],
            "tier_2": scen["h2"],
            "tier_3": scen["h3"]
        }
    }


# ============================================================================
# ARCHETYPE 5: Lines & Circle Terminology (Exam Q7.1.2, Q7.1.4, Q7.4.1)
# ============================================================================

def _generate_lines_and_circles(rng: random.Random) -> Dict[str, Any]:
    """
    Lines (parallel vs perpendicular) and Circle parts (radius, diameter, chord).
    Exam Q7.1.2: Parallel lines.
    Exam Q7.1.4: Perpendicular lines.
    Exam Q7.4.1: Circle with radius 4 cm -> diameter = 8 cm.
    """
    sub_type = rng.choice(["circle_radius_diameter", "circle_definitions", "lines_properties"])

    if sub_type == "circle_radius_diameter":
        radius = rng.randint(3, 15)
        diameter = radius * 2
        ask_diameter = rng.choice([True, False])

        if ask_diameter:
            prompt = (
                f"A circle with centre \\(O\\) has a radius of \\({radius}\\text{{ cm}}\\).\n\n"
                f"Calculate the length of the diameter of this circle."
            )
            ans = str(diameter)
            ans_display = f"{diameter} cm"
            sol = f"The diameter is twice the radius: \\(D = 2 \\times r = 2 \\times {radius}\\text{{ cm}} = {diameter}\\text{{ cm}}\\)."
            t1 = "Recall the relationship between the radius and diameter of a circle."
            t2 = f"Diameter = 2 × radius. Multiply {radius} by 2."
            t3 = f"Diameter = 2 × {radius} = {diameter} cm."
        else:
            prompt = (
                f"A circle has a diameter of \\({diameter}\\text{{ cm}}\\).\n\n"
                f"Calculate the length of the radius of this circle."
            )
            ans = str(radius)
            ans_display = f"{radius} cm"
            sol = f"The radius is half the diameter: \\(r = \\frac{{D}}{{2}} = \\frac{{{diameter}}}{{2}} = {radius}\\text{{ cm}}\\)."
            t1 = "The radius runs from the center to the edge, which is half of the diameter."
            t2 = f"Radius = Diameter ÷ 2. Divide {diameter} by 2."
            t3 = f"Radius = {diameter} ÷ 2 = {radius} cm."

        return {
            "id": f"g7_math_geom2d_circle_calc_{rng.randint(100000, 999999)}",
            "question_type": "typed",
            "prompt": prompt,
            "prompt_latex": prompt,
            "answer_mode": "text",
            "correct_answer": ans,
            "answer_latex": ans_display,
            "explanation": sol,
            "canonical_solution": sol,
            "marks": 2,
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "subskill": "circle_radius_diameter",
            "learning_objective_id": "math_g7_geom_circle_metric",
            "misconception_tags": ["radius_diameter_inversion"],
            "diagnostic_tags": ["geometry_2d", "circles", "radius_diameter"],
            "minimum_mastery_score": 75,
            "keywords": ["circle", "radius", "diameter", "centre"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Application of formula relating radius and diameter", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Correct calculated length ({ans_display})", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy"
            },
            "hints": {
                "tier_1": t1,
                "tier_2": t2,
                "tier_3": t3
            }
        }

    elif sub_type == "circle_definitions":
        scens = [
            {
                "prompt": "What is the straight line segment that connects two points on the circumference of a circle without necessarily passing through the centre called?",
                "correct": "Chord",
                "options": ["Chord", "Diameter", "Radius", "Arc"],
                "explanation": "A chord connects any two points on the circumference of a circle. (A diameter is a special chord that passes through the centre).",
                "h1": "It joins two points on the circle boundary.",
                "h2": "The line is called a chord.",
                "h3": "The answer is Chord."
            },
            {
                "prompt": "What do we call the line segment drawn from the centre of a circle to any point on its boundary?",
                "correct": "Radius",
                "options": ["Radius", "Diameter", "Chord", "Tangent"],
                "explanation": "A line segment from the centre of a circle to any point on the circumference is called a radius.",
                "h1": "It reaches halfway across the circle, from the center to the outside.",
                "h2": "This segment is called the radius.",
                "h3": "The answer is Radius."
            }
        ]
        scen = rng.choice(scens)
        options = list(scen["options"])
        rng.shuffle(options)

        return {
            "id": f"g7_math_geom2d_circle_def_{rng.randint(100000, 999999)}",
            "question_type": "mcq",
            "prompt": scen["prompt"],
            "prompt_latex": scen["prompt"],
            "options": options,
            "options_latex": options,
            "answer_mode": "choice",
            "correct_answer": scen["correct"],
            "answer_latex": scen["correct"],
            "explanation": scen["explanation"],
            "canonical_solution": scen["explanation"],
            "marks": 2,
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "subskill": "circle_definitions",
            "learning_objective_id": "math_g7_geom_circle_parts",
            "misconception_tags": ["chord_vs_diameter_confusion"],
            "diagnostic_tags": ["geometry_2d", "circles", "terminology"],
            "minimum_mastery_score": 75,
            "keywords": ["circle", "chord", "radius", "diameter", "circumference"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Knowledge of circle terminology", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Correct option selection", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "strict"
            },
            "hints": {
                "tier_1": scen["h1"],
                "tier_2": scen["h2"],
                "tier_3": scen["h3"]
            }
        }

    else: # lines_properties
        scens = [
            {
                "prompt": "Two straight lines intersect and form an angle of 90°. What term describes the relationship between these two lines?",
                "correct": "Perpendicular lines",
                "options": ["Perpendicular lines", "Parallel lines", "Collinear lines", "Skew lines"],
                "explanation": "Lines that intersect at a 90° right angle are perpendicular lines.",
                "h1": "Look at the angle formed: 90° (a right angle).",
                "h2": "Lines meeting at right angles are called perpendicular.",
                "h3": "The answer is Perpendicular lines."
            },
            {
                "prompt": "Two straight lines lie in the same plane and remain the same distance apart, never meeting no matter how far they are extended. What term describes these lines?",
                "correct": "Parallel lines",
                "options": ["Parallel lines", "Perpendicular lines", "Intersecting lines", "Concurrent lines"],
                "explanation": "Lines in the same plane that never intersect and are always equidistant are parallel lines.",
                "h1": "They are like train tracks that never cross.",
                "h2": "Lines that never meet are parallel.",
                "h3": "The answer is Parallel lines."
            }
        ]
        scen = rng.choice(scens)
        options = list(scen["options"])
        rng.shuffle(options)

        return {
            "id": f"g7_math_geom2d_lines_{rng.randint(100000, 999999)}",
            "question_type": "mcq",
            "prompt": scen["prompt"],
            "prompt_latex": scen["prompt"],
            "options": options,
            "options_latex": options,
            "answer_mode": "choice",
            "correct_answer": scen["correct"],
            "answer_latex": scen["correct"],
            "explanation": scen["explanation"],
            "canonical_solution": scen["explanation"],
            "marks": 2,
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "subskill": "lines_properties",
            "learning_objective_id": "math_g7_geom_lines",
            "misconception_tags": ["parallel_vs_perpendicular_confusion"],
            "diagnostic_tags": ["geometry_2d", "lines", "parallel_perpendicular"],
            "minimum_mastery_score": 75,
            "keywords": ["parallel lines", "perpendicular lines", "right angle", "intersection"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Geometric line property recognition", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Correct line type identification", "marks": 1, "editable": True}
                ],
                "deductions": [],
                "carry_forward_rule": "strict"
            },
            "hints": {
                "tier_1": scen["h1"],
                "tier_2": scen["h2"],
                "tier_3": scen["h3"]
            }
        }


# ============================================================================
# MASTER GENERATE FUNCTION (6-Pillar Contract)
# ============================================================================

def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 2D Geometry Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_triangle_angles": Angle calculation in triangle (180°)
    - mode="elementary_quadrilateral_angles": Angle calculation in quadrilateral (360°)
    - mode="elementary_triangles": Classification & properties of triangles
    - mode="elementary_quadrilaterals": Classification & properties of quadrilaterals
    - mode="elementary_lines_circles": Circle terminology & parallel/perpendicular lines
    - mode="compound": Full authentic exam paper mix
    """
    rng = _rng(seed)
    questions = []

    for _ in range(count):
        if mode == "elementary_triangle_angles" or subskill == "triangle_angles":
            q = _generate_triangle_interior_angle(rng)
        elif mode == "elementary_quadrilateral_angles" or subskill == "quadrilateral_angles":
            q = _generate_quadrilateral_interior_angle(rng)
        elif mode == "elementary_triangles" or subskill == "triangles":
            q = _generate_triangle_classification(rng)
        elif mode == "elementary_quadrilaterals" or subskill == "quadrilaterals":
            q = _generate_quadrilateral_classification(rng)
        elif mode == "elementary_lines_circles" or subskill in ["lines", "circles"]:
            q = _generate_lines_and_circles(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                lambda: _generate_triangle_interior_angle(rng),
                lambda: _generate_quadrilateral_interior_angle(rng),
                lambda: _generate_triangle_classification(rng),
                lambda: _generate_quadrilateral_classification(rng),
                lambda: _generate_lines_and_circles(rng)
            ])
            q = archetype()
        questions.append(q)

    return questions
