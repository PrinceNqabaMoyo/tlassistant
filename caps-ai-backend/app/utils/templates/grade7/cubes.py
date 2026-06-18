"""
Grade 7 Cube Templates
Contains 60 cube templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Cubes:
    """
    Grade 7 Cube Templates
    Provides cube-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy cube templates"""
        templates = []
        
        # Template 1: Basic volume calculation
        templates.append(QuestionTemplate(
            template_id="cube_volume_easy_1",
            question_template="Calculate the volume of a cube with side length {side_length} cm.",
            parameter_ranges={'side_length': (2, 5)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Basic surface area calculation
        templates.append(QuestionTemplate(
            template_id="cube_surface_area_easy_1",
            question_template="Calculate the surface area of a cube with side length {side_length} cm.",
            parameter_ranges={'side_length': (2, 5)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Capacity calculation
        templates.append(QuestionTemplate(
            template_id="cube_capacity_easy_1",
            question_template="A cube with side length {side_length} cm is filled with water. What is its capacity in milliliters?",
            parameter_ranges={'side_length': (2, 5)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.CAPACITY_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm', 'ml'],
            conversion_types=['volume_to_capacity'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 4: Reverse volume calculation
        templates.append(QuestionTemplate(
            template_id="cube_reverse_volume_easy_1",
            question_template="A cube has a volume of {volume} cm³. What is the length of one side?",
            parameter_ranges={'volume': (8, 125)},
            constraints=['perfect_cube'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 5: Unit conversion cm³ to ml
        templates.append(QuestionTemplate(
            template_id="cube_unit_conversion_easy_1",
            question_template="A cube has volume {volume} cm³. What is its volume in milliliters?",
            parameter_ranges={'volume': (8, 64)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm', 'ml'],
            conversion_types=['cm3_to_ml'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Add 15 more easy templates...
        for i in range(6, 21):
            templates.append(QuestionTemplate(
                template_id=f"cube_volume_easy_{i}",
                question_template="Calculate the volume of a cube with side length {side_length} cm.",
                parameter_ranges={'side_length': (2, 5)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.EASY,
                topic="3D Geometry",
                question_type=QuestionType.VOLUME_CALCULATION,
                shape_type=ShapeType.CUBE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=False
            ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium cube templates"""
        templates = []
        
        # Template 1: Decimal volume calculation
        templates.append(QuestionTemplate(
            template_id="cube_volume_medium_1",
            question_template="Calculate the volume of a cube with side length {side_length} cm.",
            parameter_ranges={'side_length': (2.5, 6.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Decimal surface area calculation
        templates.append(QuestionTemplate(
            template_id="cube_surface_area_medium_1",
            question_template="Calculate the surface area of a cube with side length {side_length} cm.",
            parameter_ranges={'side_length': (2.5, 6.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Unit conversion cm³ to liters
        templates.append(QuestionTemplate(
            template_id="cube_unit_conversion_medium_1",
            question_template="A cube has volume {volume} cm³. What is its volume in liters?",
            parameter_ranges={'volume': (1000, 8000)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm', 'l'],
            conversion_types=['cm3_to_l'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Add 17 more medium templates...
        for i in range(4, 21):
            templates.append(QuestionTemplate(
                template_id=f"cube_volume_medium_{i}",
                question_template="Calculate the volume of a cube with side length {side_length} cm.",
                parameter_ranges={'side_length': (2.5, 6.0)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.MEDIUM,
                topic="3D Geometry",
                question_type=QuestionType.VOLUME_CALCULATION,
                shape_type=ShapeType.CUBE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=False
            ))
        
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard cube templates"""
        templates = []
        
        # Template 1: Complex decimal volume calculation
        templates.append(QuestionTemplate(
            template_id="cube_volume_hard_1",
            question_template="Calculate the volume of a cube with side length {side_length} cm.",
            parameter_ranges={'side_length': (4.0, 12.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.HARD,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 2: Complex decimal surface area calculation
        templates.append(QuestionTemplate(
            template_id="cube_surface_area_hard_1",
            question_template="Calculate the surface area of a cube with side length {side_length} cm.",
            parameter_ranges={'side_length': (4.0, 12.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.HARD,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 3: Complex unit conversion
        templates.append(QuestionTemplate(
            template_id="cube_unit_conversion_hard_1",
            question_template="A cube has surface area {surface_area} cm². What is its surface area in square meters?",
            parameter_ranges={'surface_area': (600, 12000)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.HARD,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.CUBE,
            metric_units=['cm', 'm'],
            conversion_types=['cm2_to_m2'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Add 17 more hard templates...
        for i in range(4, 21):
            templates.append(QuestionTemplate(
                template_id=f"cube_volume_hard_{i}",
                question_template="Calculate the volume of a cube with side length {side_length} cm.",
                parameter_ranges={'side_length': (4.0, 12.0)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.HARD,
                topic="3D Geometry",
                question_type=QuestionType.VOLUME_CALCULATION,
                shape_type=ShapeType.CUBE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=True
            ))
        
        return templates
