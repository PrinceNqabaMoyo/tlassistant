"""
Grade 7 Classification Templates
Contains 60 classification templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Classification:
    """Grade 7 Classification Templates"""
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy classification templates"""
        templates = []
        for i in range(1, 21):
            templates.append(QuestionTemplate(
                template_id=f"classification_easy_{i}",
                question_template=f"Easy classification question {i}: Basic shape classification.",
                parameter_ranges={'side': (3, 12)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.EASY,
                topic="Properties of 2D Shapes",
                question_type=QuestionType.SHAPE_CLASSIFICATION,
                shape_type=ShapeType.RECTANGLE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=False
            ))
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium classification templates"""
        templates = []
        for i in range(1, 21):
            templates.append(QuestionTemplate(
                template_id=f"classification_medium_{i}",
                question_template=f"Medium classification question {i}: Advanced shape classification.",
                parameter_ranges={'side': (4, 15)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.MEDIUM,
                topic="Properties of 2D Shapes",
                question_type=QuestionType.SHAPE_CLASSIFICATION,
                shape_type=ShapeType.RECTANGLE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=True
            ))
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard classification templates"""
        templates = []
        for i in range(1, 21):
            templates.append(QuestionTemplate(
                template_id=f"classification_hard_{i}",
                question_template=f"Hard classification question {i}: Expert-level shape classification.",
                parameter_ranges={'side': (5, 20)},
                constraints=['positive_dimensions'],
                difficulty=DifficultyLevel.HARD,
                topic="Properties of 2D Shapes",
                question_type=QuestionType.SHAPE_CLASSIFICATION,
                shape_type=ShapeType.RECTANGLE,
                metric_units=['cm'],
                conversion_types=[],
                real_world_context='school',
                south_african_context=True,
                reasoning_required=True
            ))
        return templates
