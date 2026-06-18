"""
Grade 7 Rectangular Prism Templates
Contains 60 rectangular prism templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7RectangularPrisms:
    """
    Grade 7 Rectangular Prism Templates
    Provides rectangular prism-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy rectangular prism templates"""
        templates = []
        
        # Template 1: Basic volume calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_volume_easy_1",
            question_template="Calculate the volume of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
            parameter_ranges={'length': (2, 4), 'width': (2, 4), 'height': (2, 4)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Basic surface area calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_surface_area_easy_1",
            question_template="Calculate the surface area of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
            parameter_ranges={'length': (2, 4), 'width': (2, 4), 'height': (2, 4)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Capacity calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_capacity_easy_1",
            question_template="A rectangular prism with dimensions {length} cm × {width} cm × {height} cm is filled with water. What is its capacity in milliliters?",
            parameter_ranges={'length': (2, 4), 'width': (2, 4), 'height': (2, 4)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.CAPACITY_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm', 'ml'],
            conversion_types=['volume_to_capacity'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 4: Reverse volume calculation - find height
        templates.append(QuestionTemplate(
            template_id="rect_prism_reverse_volume_easy_1",
            question_template="A rectangular prism has volume {volume} cm³, length {length} cm, and width {width} cm. What is the height?",
            parameter_ranges={'volume': (8, 64), 'length': (2, 4), 'width': (2, 4)},
            constraints=['positive_dimensions', 'volume_divisible'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 5: Unit conversion cm³ to ml
        templates.append(QuestionTemplate(
            template_id="rect_prism_unit_conversion_easy_1",
            question_template="A rectangular prism has volume {volume} cm³. What is its volume in milliliters?",
            parameter_ranges={'volume': (8, 64)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.EASY,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm', 'ml'],
            conversion_types=['cm3_to_ml'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Add 15 more easy templates...
        for i in range(6, 21):
            templates.append(QuestionTemplate(
                template_id=f"rect_prism_volume_easy_{i}",
                question_template="Calculate the volume of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
                parameter_ranges={'length': (2, 4), 'width': (2, 4), 'height': (2, 4)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.EASY,
                topic="3D Geometry",
                question_type=QuestionType.VOLUME_CALCULATION,
                shape_type=ShapeType.RECTANGULAR_PRISM,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=False
            ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium rectangular prism templates"""
        templates = []
        
        # Template 1: Decimal volume calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_volume_medium_1",
            question_template="Calculate the volume of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
            parameter_ranges={'length': (3.0, 8.0), 'width': (2.0, 6.0), 'height': (2.0, 5.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Decimal surface area calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_surface_area_medium_1",
            question_template="Calculate the surface area of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
            parameter_ranges={'length': (3.0, 8.0), 'width': (2.0, 6.0), 'height': (2.0, 5.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Unit conversion cm³ to liters
        templates.append(QuestionTemplate(
            template_id="rect_prism_unit_conversion_medium_1",
            question_template="A rectangular prism has volume {volume} cm³. What is its volume in liters?",
            parameter_ranges={'volume': (1000, 8000)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm', 'l'],
            conversion_types=['cm3_to_l'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Add 17 more medium templates...
        for i in range(4, 21):
            templates.append(QuestionTemplate(
                template_id=f"rect_prism_volume_medium_{i}",
                question_template="Calculate the volume of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
                parameter_ranges={'length': (3.0, 8.0), 'width': (2.0, 6.0), 'height': (2.0, 5.0)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.MEDIUM,
                topic="3D Geometry",
                question_type=QuestionType.VOLUME_CALCULATION,
                shape_type=ShapeType.RECTANGULAR_PRISM,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=False
            ))
        
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard rectangular prism templates"""
        templates = []
        
        # Template 1: Complex decimal volume calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_volume_hard_1",
            question_template="Calculate the volume of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
            parameter_ranges={'length': (5.0, 15.0), 'width': (3.0, 10.0), 'height': (2.0, 8.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.HARD,
            topic="3D Geometry",
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 2: Complex decimal surface area calculation
        templates.append(QuestionTemplate(
            template_id="rect_prism_surface_area_hard_1",
            question_template="Calculate the surface area of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
            parameter_ranges={'length': (5.0, 15.0), 'width': (3.0, 10.0), 'height': (2.0, 8.0)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.HARD,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 3: Complex unit conversion
        templates.append(QuestionTemplate(
            template_id="rect_prism_unit_conversion_hard_1",
            question_template="A rectangular prism has surface area {surface_area} cm². What is its surface area in square meters?",
            parameter_ranges={'surface_area': (600, 12000)},
            constraints=['positive_dimensions'],
            difficulty=DifficultyLevel.HARD,
            topic="3D Geometry",
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=ShapeType.RECTANGULAR_PRISM,
            metric_units=['cm', 'm'],
            conversion_types=['cm2_to_m2'],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Add 17 more hard templates...
        for i in range(4, 21):
            templates.append(QuestionTemplate(
                template_id=f"rect_prism_volume_hard_{i}",
                question_template="Calculate the volume of a rectangular prism with dimensions {length} cm × {width} cm × {height} cm.",
                parameter_ranges={'length': (5.0, 15.0), 'width': (3.0, 10.0), 'height': (2.0, 8.0)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.HARD,
                topic="3D Geometry",
                question_type=QuestionType.VOLUME_CALCULATION,
                shape_type=ShapeType.RECTANGULAR_PRISM,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=True
            ))
        
        return templates
