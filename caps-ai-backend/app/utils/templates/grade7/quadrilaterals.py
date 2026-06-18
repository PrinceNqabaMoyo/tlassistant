"""
Grade 7 Quadrilateral Templates
Contains 60 quadrilateral templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Quadrilaterals:
    """
    Grade 7 Quadrilateral Templates
    Provides quadrilateral-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Create 20 easy quadrilateral templates"""
        templates = []
        
        # Template 1: Rectangle area
        templates.append(QuestionTemplate(
            template_id="rectangle_area_easy_1",
            question_template="A rectangle has length {length} cm and width {width} cm. What is its area?",
            parameter_ranges={'length': (1, 10), 'width': (1, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Rectangle perimeter
        templates.append(QuestionTemplate(
            template_id="rectangle_perimeter_easy_1",
            question_template="A rectangle has length {length} cm and width {width} cm. What is its perimeter?",
            parameter_ranges={'length': (3, 10), 'width': (2, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Square area
        templates.append(QuestionTemplate(
            template_id="square_area_easy_1",
            question_template="A square has side length {side} cm. What is its area?",
            parameter_ranges={'side': (2, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.SQUARE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 4: Square perimeter
        templates.append(QuestionTemplate(
            template_id="square_perimeter_easy_1",
            question_template="A square has side length {side} cm. What is its perimeter?",
            parameter_ranges={'side': (3, 9)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.SQUARE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 5: Rhombus area
        templates.append(QuestionTemplate(
            template_id="rhombus_area_easy_1",
            question_template="A rhombus has base {base} cm and height {height} cm. What is its area?",
            parameter_ranges={'base': (3, 8), 'height': (2, 7)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RHOMBUS,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 6: Parallelogram area
        templates.append(QuestionTemplate(
            template_id="parallelogram_area_easy_1",
            question_template="A parallelogram has base {base} cm and height {height} cm. What is its area?",
            parameter_ranges={'base': (4, 9), 'height': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.PARALLELOGRAM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 7: Kite area
        templates.append(QuestionTemplate(
            template_id="kite_area_easy_1",
            question_template="A kite has diagonals {d1} cm and {d2} cm. What is its area?",
            parameter_ranges={'d1': (4, 10), 'd2': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.KITE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 8: Trapezium area
        templates.append(QuestionTemplate(
            template_id="trapezium_area_easy_1",
            question_template="A trapezium has parallel sides {a} cm and {b} cm, and height {height} cm. What is its area?",
            parameter_ranges={'a': (3, 8), 'b': (2, 7), 'height': (2, 6)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRAPEZIUM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 9: Unit conversion (cm to mm)
        templates.append(QuestionTemplate(
            template_id="quadrilateral_conversion_easy_1",
            question_template="Convert {value} cm to mm.",
            parameter_ranges={'value': (5, 20)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 10: Area with unit conversion
        templates.append(QuestionTemplate(
            template_id="quadrilateral_area_conversion_easy_1",
            question_template="A rectangle has length {length} cm and width {width} cm. What is its area in mm²?",
            parameter_ranges={'length': (2, 5), 'width': (2, 5)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 11: Real-world context (classroom)
        templates.append(QuestionTemplate(
            template_id="quadrilateral_classroom_easy_1",
            question_template="A classroom has a rectangular floor {length} m × {width} m. What is its area?",
            parameter_ranges={'length': (4, 8), 'width': (3, 6)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 12: Real-world context (garden)
        templates.append(QuestionTemplate(
            template_id="quadrilateral_garden_easy_1",
            question_template="A rectangular garden plot is {length} m × {width} m. What is its area?",
            parameter_ranges={'length': (3, 7), 'width': (2, 5)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='garden',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 13: Shape classification
        templates.append(QuestionTemplate(
            template_id="quadrilateral_classification_easy_1",
            question_template="A quadrilateral has all sides equal ({side} cm) and all angles equal (90°). What type is it?",
            parameter_ranges={'side': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.SQUARE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 14: Rectangle properties
        templates.append(QuestionTemplate(
            template_id="rectangle_properties_easy_1",
            question_template="A rectangle has length {length} cm and width {width} cm. What are its area and perimeter?",
            parameter_ranges={'length': (4, 10), 'width': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 15: Square properties
        templates.append(QuestionTemplate(
            template_id="square_properties_easy_1",
            question_template="A square has side length {side} cm. What are its area and perimeter?",
            parameter_ranges={'side': (3, 9)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.SQUARE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 16: Perimeter with unit conversion
        templates.append(QuestionTemplate(
            template_id="quadrilateral_perimeter_conversion_easy_1",
            question_template="A rectangle has length {length} cm and width {width} cm. What is its perimeter in mm?",
            parameter_ranges={'length': (3, 7), 'width': (2, 6)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 17: Real-world context (construction)
        templates.append(QuestionTemplate(
            template_id="quadrilateral_construction_easy_1",
            question_template="A rectangular foundation is {length} m × {width} m. What is its area?",
            parameter_ranges={'length': (5, 10), 'width': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='construction',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 18: Real-world context (sports)
        templates.append(QuestionTemplate(
            template_id="quadrilateral_sports_easy_1",
            question_template="A rectangular sports field is {length} m × {width} m. What is its area?",
            parameter_ranges={'length': (8, 15), 'width': (5, 12)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='sports',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 19: Unit conversion (mm to cm)
        templates.append(QuestionTemplate(
            template_id="quadrilateral_conversion_easy_2",
            question_template="Convert {value} mm to cm.",
            parameter_ranges={'value': (20, 80)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['mm', 'cm'],
            conversion_types=['mm_cm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 20: Mixed quadrilateral properties
        templates.append(QuestionTemplate(
            template_id="quadrilateral_mixed_easy_1",
            question_template="A quadrilateral has length {length} cm and width {width} cm. If it's a rectangle, what is its area? If it's a square, what is its perimeter?",
            parameter_ranges={'length': (4, 8), 'width': (4, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium quadrilateral templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard quadrilateral templates"""
        templates = []
        # TODO: Add hard templates
        return templates
