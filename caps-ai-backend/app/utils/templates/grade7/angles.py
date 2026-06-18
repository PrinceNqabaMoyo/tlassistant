"""
Grade 7 Angle Templates
Contains 60 angle templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Angles:
    """
    Grade 7 Angle Templates
    Provides angle-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Create 20 easy angle templates"""
        templates = []
        
        # Template 1: Angle classification
        templates.append(QuestionTemplate(
            template_id="angle_classification_easy_1",
            question_template="Classify this angle: {angle}°",
            parameter_ranges={'angle': (1, 180)},
            constraints=[],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Angle measurement
        templates.append(QuestionTemplate(
            template_id="angle_measurement_easy_1",
            question_template="What is the measure of angle {angle}?",
            parameter_ranges={'angle': (30, 150)},
            constraints=['positive_dimensions'],
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
        
        # Template 3: Angle sum in triangle
        templates.append(QuestionTemplate(
            template_id="angle_sum_triangle_easy_1",
            question_template="In a triangle, two angles are {angle1}° and {angle2}°. What is the third angle?",
            parameter_ranges={'angle1': (30, 80), 'angle2': (40, 90)},
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
        
        # Template 4: Angle sum in quadrilateral
        templates.append(QuestionTemplate(
            template_id="angle_sum_quadrilateral_easy_1",
            question_template="In a quadrilateral, three angles are {angle1}°, {angle2}°, and {angle3}°. What is the fourth angle?",
            parameter_ranges={'angle1': (60, 120), 'angle2': (70, 130), 'angle3': (80, 140)},
            constraints=['angle_sum_360'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 5: Right angle identification
        templates.append(QuestionTemplate(
            template_id="right_angle_easy_1",
            question_template="Is the angle {angle}° a right angle?",
            parameter_ranges={'angle': (80, 100)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 6: Acute angle identification
        templates.append(QuestionTemplate(
            template_id="acute_angle_easy_1",
            question_template="Is the angle {angle}° acute?",
            parameter_ranges={'angle': (30, 90)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 7: Obtuse angle identification
        templates.append(QuestionTemplate(
            template_id="obtuse_angle_easy_1",
            question_template="Is the angle {angle}° obtuse?",
            parameter_ranges={'angle': (90, 180)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 8: Angle comparison
        templates.append(QuestionTemplate(
            template_id="angle_comparison_easy_1",
            question_template="Which angle is larger: {angle1}° or {angle2}°?",
            parameter_ranges={'angle1': (30, 90), 'angle2': (60, 120)},
            constraints=['positive_dimensions'],
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
        
        # Template 9: Angle addition
        templates.append(QuestionTemplate(
            template_id="angle_addition_easy_1",
            question_template="What is the sum of angles {angle1}° and {angle2}°?",
            parameter_ranges={'angle1': (20, 80), 'angle2': (30, 90)},
            constraints=['positive_dimensions'],
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
        
        # Template 10: Angle subtraction
        templates.append(QuestionTemplate(
            template_id="angle_subtraction_easy_1",
            question_template="What is the difference between angles {angle1}° and {angle2}°?",
            parameter_ranges={'angle1': (60, 120), 'angle2': (20, 80)},
            constraints=['positive_dimensions'],
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
        
        # Template 11: Real-world context (classroom)
        templates.append(QuestionTemplate(
            template_id="angle_classroom_easy_1",
            question_template="A classroom corner forms an angle of {angle}°. What type of angle is this?",
            parameter_ranges={'angle': (80, 100)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 12: Real-world context (construction)
        templates.append(QuestionTemplate(
            template_id="angle_construction_easy_1",
            question_template="A construction corner forms an angle of {angle}°. What type of angle is this?",
            parameter_ranges={'angle': (85, 95)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Real-world Applications",
            question_type=QuestionType.REAL_WORLD_APPLICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='construction',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 13: Angle properties
        templates.append(QuestionTemplate(
            template_id="angle_properties_easy_1",
            question_template="What are the properties of a {angle_type} angle?",
            parameter_ranges={'angle_type': (30, 150)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 14: Angle measurement with protractor
        templates.append(QuestionTemplate(
            template_id="angle_protractor_easy_1",
            question_template="Using a protractor, measure the angle {angle}°.",
            parameter_ranges={'angle': (30, 150)},
            constraints=['positive_dimensions'],
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
        
        # Template 15: Angle in triangle
        templates.append(QuestionTemplate(
            template_id="angle_triangle_easy_1",
            question_template="In a triangle, what is the measure of the third angle if two angles are {angle1}° and {angle2}°?",
            parameter_ranges={'angle1': (40, 80), 'angle2': (50, 90)},
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
        
        # Template 16: Angle in quadrilateral
        templates.append(QuestionTemplate(
            template_id="angle_quadrilateral_easy_1",
            question_template="In a quadrilateral, what is the measure of the fourth angle if three angles are {angle1}°, {angle2}°, and {angle3}°?",
            parameter_ranges={'angle1': (70, 110), 'angle2': (80, 120), 'angle3': (90, 130)},
            constraints=['angle_sum_360'],
            difficulty=DifficultyLevel.EASY,
            topic="Calculations involving 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 17: Angle types
        templates.append(QuestionTemplate(
            template_id="angle_types_easy_1",
            question_template="Name the type of angle: {angle}°.",
            parameter_ranges={'angle': (30, 150)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 18: Angle measurement
        templates.append(QuestionTemplate(
            template_id="angle_measurement_easy_2",
            question_template="What is the measure of angle {angle}?",
            parameter_ranges={'angle': (45, 135)},
            constraints=['positive_dimensions'],
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
        
        # Template 19: Angle classification
        templates.append(QuestionTemplate(
            template_id="angle_classification_easy_2",
            question_template="Classify the angle {angle}° as acute, right, or obtuse.",
            parameter_ranges={'angle': (45, 135)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 20: Mixed angle properties
        templates.append(QuestionTemplate(
            template_id="angle_mixed_easy_1",
            question_template="What is the measure of angle {angle}°? What type of angle is it?",
            parameter_ranges={'angle': (30, 150)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.AREA_CALCULATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium angle templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard angle templates"""
        templates = []
        # TODO: Add hard templates
        return templates
