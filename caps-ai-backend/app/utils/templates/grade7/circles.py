"""
Grade 7 Circle Templates
Contains 60 circle templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Circles:
    """
    Grade 7 Circle Templates
    Provides circle-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Create 20 easy circle templates"""
        templates = []
        
        # Template 1: Circle area
        templates.append(QuestionTemplate(
            template_id="circle_area_easy_1",
            question_template="A circle has radius {radius} cm. What is its area?",
            parameter_ranges={'radius': (1, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Circle circumference
        templates.append(QuestionTemplate(
            template_id="circle_circumference_easy_1",
            question_template="A circle has radius {radius} cm. What is its circumference?",
            parameter_ranges={'radius': (3, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Circle diameter
        templates.append(QuestionTemplate(
            template_id="circle_diameter_easy_1",
            question_template="A circle has diameter {diameter} cm. What is its radius?",
            parameter_ranges={'diameter': (4, 16)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 4: Circle radius from area
        templates.append(QuestionTemplate(
            template_id="circle_radius_easy_1",
            question_template="A circle has area {area} cm². What is its radius?",
            parameter_ranges={'area': (10, 50)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 5: Circle area with diameter
        templates.append(QuestionTemplate(
            template_id="circle_area_diameter_easy_1",
            question_template="A circle has diameter {diameter} cm. What is its area?",
            parameter_ranges={'diameter': (4, 12)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 6: Circle circumference with diameter
        templates.append(QuestionTemplate(
            template_id="circle_circumference_diameter_easy_1",
            question_template="A circle has diameter {diameter} cm. What is its circumference?",
            parameter_ranges={'diameter': (6, 18)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 7: Unit conversion (cm to mm)
        templates.append(QuestionTemplate(
            template_id="circle_conversion_easy_1",
            question_template="Convert {value} cm to mm.",
            parameter_ranges={'value': (5, 20)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 8: Area with unit conversion
        templates.append(QuestionTemplate(
            template_id="circle_area_conversion_easy_1",
            question_template="A circle has radius {radius} cm. What is its area in mm²?",
            parameter_ranges={'radius': (2, 5)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 9: Real-world context (classroom)
        templates.append(QuestionTemplate(
            template_id="circle_classroom_easy_1",
            question_template="A circular table has radius {radius} cm. What is its area?",
            parameter_ranges={'radius': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 10: Real-world context (garden)
        templates.append(QuestionTemplate(
            template_id="circle_garden_easy_1",
            question_template="A circular flower bed has radius {radius} m. What is its area?",
            parameter_ranges={'radius': (2, 6)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='garden',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 11: Real-world context (construction)
        templates.append(QuestionTemplate(
            template_id="circle_construction_easy_1",
            question_template="A circular foundation has radius {radius} m. What is its area?",
            parameter_ranges={'radius': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='construction',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 12: Real-world context (sports)
        templates.append(QuestionTemplate(
            template_id="circle_sports_easy_1",
            question_template="A circular track has radius {radius} m. What is its circumference?",
            parameter_ranges={'radius': (5, 15)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='sports',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 13: Circle properties
        templates.append(QuestionTemplate(
            template_id="circle_properties_easy_1",
            question_template="A circle has radius {radius} cm. What are its area and circumference?",
            parameter_ranges={'radius': (3, 9)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 14: Circle diameter from circumference
        templates.append(QuestionTemplate(
            template_id="circle_diameter_circumference_easy_1",
            question_template="A circle has circumference {circumference} cm. What is its diameter?",
            parameter_ranges={'circumference': (15, 40)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 15: Circle radius from circumference
        templates.append(QuestionTemplate(
            template_id="circle_radius_circumference_easy_1",
            question_template="A circle has circumference {circumference} cm. What is its radius?",
            parameter_ranges={'circumference': (20, 50)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 16: Perimeter with unit conversion
        templates.append(QuestionTemplate(
            template_id="circle_perimeter_conversion_easy_1",
            question_template="A circle has radius {radius} cm. What is its circumference in mm?",
            parameter_ranges={'radius': (3, 8)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.PERIMETER_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm', 'mm'],
            conversion_types=['cm_mm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 17: Real-world context (community)
        templates.append(QuestionTemplate(
            template_id="circle_community_easy_1",
            question_template="A circular park has radius {radius} m. What is its area?",
            parameter_ranges={'radius': (4, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='community',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 18: Real-world context (farm)
        templates.append(QuestionTemplate(
            template_id="circle_farm_easy_1",
            question_template="A circular field has radius {radius} m. What is its area?",
            parameter_ranges={'radius': (5, 12)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['m'],
            conversion_types=[],
            real_world_context='farm',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 19: Unit conversion (mm to cm)
        templates.append(QuestionTemplate(
            template_id="circle_conversion_easy_2",
            question_template="Convert {value} mm to cm.",
            parameter_ranges={'value': (20, 80)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Unit Conversions",
            question_type=QuestionType.UNIT_CONVERSION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['mm', 'cm'],
            conversion_types=['mm_cm'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 20: Mixed circle properties
        templates.append(QuestionTemplate(
            template_id="circle_mixed_easy_1",
            question_template="A circle has radius {radius} cm. What is its area? What is its circumference?",
            parameter_ranges={'radius': (4, 10)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium circle templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard circle templates"""
        templates = []
        # TODO: Add hard templates
        return templates
