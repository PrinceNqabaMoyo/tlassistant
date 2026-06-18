"""
Grade 7 Template Module Implementation
Main module class that coordinates all Grade 7 templates
"""

from typing import Dict, List
from ..base.template_base import GradeTemplateModule
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType
from .triangles import Grade7Triangles
from .quadrilaterals import Grade7Quadrilaterals
from .circles import Grade7Circles
from .angles import Grade7Angles
from .composite_areas import Grade7CompositeAreas
from .classification import Grade7Classification
from .similarity_congruency import Grade7SimilarityCongruency
from .cubes import Grade7Cubes
from .rectangular_prisms import Grade7RectangularPrisms


class Grade7TemplateModule(GradeTemplateModule):
    """
    Grade 7 Template Module
    Coordinates all Grade 7 geometry templates
    """
    
    def __init__(self, grade: int = 7):
        self.grade = grade
        self.shape_modules = {
            'triangles': Grade7Triangles(),
            'quadrilaterals': Grade7Quadrilaterals(),
            'circles': Grade7Circles(),
            'angles': Grade7Angles(),
            'composite_areas': Grade7CompositeAreas(),
            'classification': Grade7Classification(),
            'similarity_congruency': Grade7SimilarityCongruency(),
            'cubes': Grade7Cubes(),
            'rectangular_prisms': Grade7RectangularPrisms()
        }
        self.templates = self._initialize_templates()
    
    def _initialize_templates(self) -> Dict[str, Dict[str, List[QuestionTemplate]]]:
        """
        Initialize all Grade 7 templates
        Returns: Dictionary with shape -> difficulty -> templates structure
        """
        templates = {}
        
        for shape_name, shape_module in self.shape_modules.items():
            templates[shape_name] = {
                'easy': shape_module.get_easy_templates(),
                'medium': shape_module.get_medium_templates(),
                'hard': shape_module.get_hard_templates()
            }
        
        return templates
    
    def get_templates(self, shape: str, difficulty: str) -> List[QuestionTemplate]:
        """
        Get templates for specific shape and difficulty
        Args:
            shape: Shape type
            difficulty: Difficulty level
        Returns: List of QuestionTemplate objects
        """
        if shape not in self.shape_modules:
            return []
        
        shape_module = self.shape_modules[shape]
        
        if difficulty == 'easy':
            return shape_module.get_easy_templates()
        elif difficulty == 'medium':
            return shape_module.get_medium_templates()
        elif difficulty == 'hard':
            return shape_module.get_hard_templates()
        else:
            return []
    
    def get_available_shapes(self) -> List[str]:
        """
        Get list of available shapes for Grade 7
        Returns: List of shape names
        """
        return list(self.shape_modules.keys())
    
    def get_available_difficulties(self) -> List[str]:
        """
        Get list of available difficulties for Grade 7
        Returns: List of difficulty levels
        """
        return ['easy', 'medium', 'hard']
    
    def get_shape_info(self, shape: str) -> Dict:
        """
        Get information about a specific shape
        Args:
            shape: Shape name
        Returns: Dictionary with shape information
        """
        if shape not in self.shape_modules:
            return {}
        
        shape_module = self.shape_modules[shape]
        return {
            'shape': shape,
            'easy_count': len(shape_module.get_easy_templates()),
            'medium_count': len(shape_module.get_medium_templates()),
            'hard_count': len(shape_module.get_hard_templates()),
            'total_count': (
                len(shape_module.get_easy_templates()) +
                len(shape_module.get_medium_templates()) +
                len(shape_module.get_hard_templates())
            )
        }
    
    def get_all_shapes_info(self) -> Dict[str, Dict]:
        """
        Get information about all shapes
        Returns: Dictionary with shape -> info mapping
        """
        return {
            shape: self.get_shape_info(shape)
            for shape in self.get_available_shapes()
        }
