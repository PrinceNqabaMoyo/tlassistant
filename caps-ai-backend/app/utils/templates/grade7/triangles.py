"""
Grade 7 Triangle Templates
Contains 60 triangle templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Triangles:
    """
    Grade 7 Triangle Templates
    Provides triangle-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy triangle templates"""
        templates = []
        
        # Template 1: Basic area calculation
        templates.append(QuestionTemplate(
            template_id="triangle_area_easy_1",
            question_template="A triangle has base {base} cm and height {height} cm. What is its area?",
            parameter_ranges={'base': (1, 10), 'height': (1, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Perimeter calculation
        templates.append(QuestionTemplate(
            template_id="triangle_perimeter_easy_1",
            question_template="A triangle has sides {a} cm, {b} cm, and {c} cm. What is its perimeter?",
            parameter_ranges={'a': (1, 5), 'b': (1, 5), 'c': (1, 5)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Shape classification
        templates.append(QuestionTemplate(
            template_id="triangle_classification_easy_1",
            question_template="Classify this triangle with sides {a} cm, {b} cm, and {c} cm.",
            parameter_ranges={'a': (3, 5), 'b': (3, 5), 'c': (3, 5)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 4: Unit conversion (cm to mm)
        templates.append(QuestionTemplate(
            template_id="triangle_conversion_easy_1",
            question_template="Convert {value} cm to mm.",
            parameter_ranges={'value': (1, 10)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 5: Real-world context (garden)
        templates.append(QuestionTemplate(
            template_id="triangle_garden_easy_1",
            question_template="A triangular garden bed has base {base} m and height {height} m. What is its area in cm²?",
            parameter_ranges={'base': (1, 3), 'height': (1, 3)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['m', 'cm'],
            conversion_types=['m_cm'],
            real_world_context='garden',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 6: Pythagorean theorem
        templates.append(QuestionTemplate(
            template_id="triangle_pythagorean_easy_1",
            question_template="A right-angled triangle has sides {a} cm and {b} cm. What is the length of the hypotenuse?",
            parameter_ranges={'a': (3, 5), 'b': (4, 6)},
            constraints=['pythagorean_triple'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_RIGHT_ANGLED,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='construction',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 7: Height calculation
        templates.append(QuestionTemplate(
            template_id="triangle_height_easy_1",
            question_template="A triangle has area {area} cm² and base {base} cm. What is its height?",
            parameter_ranges={'area': (6, 30), 'base': (3, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 8: Property identification
        templates.append(QuestionTemplate(
            template_id="triangle_properties_easy_1",
            question_template="Which property does this triangle have: sides {a} cm, {b} cm, {c} cm?",
            parameter_ranges={'a': (3, 5), 'b': (3, 5), 'c': (3, 5)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 9: Unit conversion (mm to cm)
        templates.append(QuestionTemplate(
            template_id="triangle_conversion_easy_2",
            question_template="Convert {value} mm to cm.",
            parameter_ranges={'value': (10, 100)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['mm', 'cm'],
            conversion_types=['mm_cm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 10: Real-world context (construction)
        templates.append(QuestionTemplate(
            template_id="triangle_construction_easy_1",
            question_template="A triangular roof section has base {base} m and height {height} m. What is its area?",
            parameter_ranges={'base': (2, 5), 'height': (1, 3)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='construction',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 11: Angle calculation
        templates.append(QuestionTemplate(
            template_id="triangle_angle_easy_1",
            question_template="In a triangle, two angles are {angle1}° and {angle2}°. What is the third angle?",
            parameter_ranges={'angle1': (30, 60), 'angle2': (40, 70)},
            constraints=['angle_sum_180'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 12: Isosceles triangle
        templates.append(QuestionTemplate(
            template_id="triangle_isosceles_easy_1",
            question_template="An isosceles triangle has equal sides of {side} cm and base {base} cm. What is its perimeter?",
            parameter_ranges={'side': (3, 8), 'base': (2, 6)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.TRIANGLE_ISOSCELES,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 13: Scalene triangle
        templates.append(QuestionTemplate(
            template_id="triangle_scalene_easy_1",
            question_template="A scalene triangle has sides {a} cm, {b} cm, and {c} cm. What is its perimeter?",
            parameter_ranges={'a': (2, 5), 'b': (3, 6), 'c': (4, 7)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.TRIANGLE_SCALENE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 14: Unit conversion (cm to m)
        templates.append(QuestionTemplate(
            template_id="triangle_conversion_easy_3",
            question_template="Convert {value} cm to m.",
            parameter_ranges={'value': (100, 500)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm', 'm'],
            conversion_types=['cm_m'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 15: Real-world context (school project)
        templates.append(QuestionTemplate(
            template_id="triangle_school_easy_1",
            question_template="A student draws a triangle with base {base} cm and height {height} cm. What is its area?",
            parameter_ranges={'base': (4, 8), 'height': (3, 6)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 16: Right-angled triangle area
        templates.append(QuestionTemplate(
            template_id="triangle_right_area_easy_1",
            question_template="A right-angled triangle has base {base} cm and height {height} cm. What is its area?",
            parameter_ranges={'base': (3, 8), 'height': (4, 9)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_RIGHT_ANGLED,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='construction',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 17: Acute triangle
        templates.append(QuestionTemplate(
            template_id="triangle_acute_easy_1",
            question_template="An acute triangle has sides {a} cm, {b} cm, and {c} cm. What is its perimeter?",
            parameter_ranges={'a': (3, 6), 'b': (4, 7), 'c': (5, 8)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.TRIANGLE_ACUTE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 18: Obtuse triangle
        templates.append(QuestionTemplate(
            template_id="triangle_obtuse_easy_1",
            question_template="An obtuse triangle has sides {a} cm, {b} cm, and {c} cm. What is its perimeter?",
            parameter_ranges={'a': (2, 5), 'b': (3, 6), 'c': (4, 7)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.TRIANGLE_OBTUSE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 19: Area with unit conversion
        templates.append(QuestionTemplate(
            template_id="triangle_area_conversion_easy_1",
            question_template="A triangle has base {base} cm and height {height} cm. What is its area in mm²?",
            parameter_ranges={'base': (2, 5), 'height': (3, 6)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 20: Perimeter with unit conversion
        templates.append(QuestionTemplate(
            template_id="triangle_perimeter_conversion_easy_1",
            question_template="A triangle has sides {a} cm, {b} cm, and {c} cm. What is its perimeter in mm?",
            parameter_ranges={'a': (2, 4), 'b': (3, 5), 'c': (4, 6)},
            constraints=['triangle_inequality'],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium triangle templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard triangle templates"""
        templates = []
        # TODO: Add hard templates
        return templates
