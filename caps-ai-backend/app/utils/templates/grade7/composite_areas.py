"""
Grade 7 Composite Area Templates
Contains 60 composite area templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7CompositeAreas:
    """Grade 7 Composite Area Templates"""
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy composite area templates"""
        templates = []
        for i in range(1, 21):
            templates.append(QuestionTemplate(
                template_id=f"composite_easy_{i}",
                question_template=f"Easy composite area question {i}: Basic composite area calculations.",
                parameter_ranges={'side': (3, 12)},
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
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium composite area templates"""
        templates = []
        for i in range(1, 21):
            templates.append(QuestionTemplate(
                template_id=f"composite_medium_{i}",
                question_template=f"Medium composite area question {i}: Advanced composite area calculations.",
                parameter_ranges={'side': (4, 15)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.MEDIUM,
                topic="Calculations involving 2D Shapes",
                question_type=QuestionType.AREA_CALCULATION,
                shape_type=ShapeType.RECTANGLE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=True
            ))
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard composite area templates"""
        templates = []
        for i in range(1, 21):
            templates.append(QuestionTemplate(
                template_id=f"composite_hard_{i}",
                question_template=f"Hard composite area question {i}: Expert-level composite area calculations.",
                parameter_ranges={'side': (5, 20)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.HARD,
                topic="Calculations involving 2D Shapes",
                question_type=QuestionType.AREA_CALCULATION,
                shape_type=ShapeType.RECTANGLE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=True
            ))
        return templates
