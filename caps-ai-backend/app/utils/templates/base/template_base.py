"""
Abstract base classes for grade-specific template modules
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class GradeTemplateModule(ABC):
    """
    Abstract base class for grade-specific template modules
    Each grade implements this interface to provide its templates
    """
    
    def __init__(self, grade: int):
        self.grade = grade
        self.templates = self._initialize_templates()
    
    @abstractmethod
    def _initialize_templates(self) -> Dict[str, Dict[str, List[QuestionTemplate]]]:
        """
        Initialize templates for this grade
        Returns: Dictionary with shape -> difficulty -> templates structure
        """
        pass
    
    @abstractmethod
    def get_templates(self, shape: str, difficulty: str) -> List[QuestionTemplate]:
        """
        Get templates for specific shape and difficulty
        Args:
            shape: Shape type (e.g., 'triangles', 'quadrilaterals')
            difficulty: Difficulty level (e.g., 'easy', 'medium', 'hard')
        Returns: List of QuestionTemplate objects
        """
        pass
    
    @abstractmethod
    def get_available_shapes(self) -> List[str]:
        """
        Get list of available shapes for this grade
        Returns: List of shape names
        """
        pass
    
    @abstractmethod
    def get_available_difficulties(self) -> List[str]:
        """
        Get list of available difficulties for this grade
        Returns: List of difficulty levels
        """
        pass
    
    def get_template_count(self) -> int:
        """
        Get total number of templates for this grade
        Returns: Total template count
        """
        total = 0
        for shape_templates in self.templates.values():
            for difficulty_templates in shape_templates.values():
                total += len(difficulty_templates)
        return total
    
    def get_shape_template_count(self, shape: str) -> int:
        """
        Get number of templates for a specific shape
        Args:
            shape: Shape type
        Returns: Number of templates for the shape
        """
        if shape not in self.templates:
            return 0
        
        total = 0
        for difficulty_templates in self.templates[shape].values():
            total += len(difficulty_templates)
        return total
    
    def get_difficulty_template_count(self, difficulty: str) -> int:
        """
        Get number of templates for a specific difficulty
        Args:
            difficulty: Difficulty level
        Returns: Number of templates for the difficulty
        """
        total = 0
        for shape_templates in self.templates.values():
            if difficulty in shape_templates:
                total += len(shape_templates[difficulty])
        return total
    
    def validate_templates(self) -> List[str]:
        """
        Validate all templates in this grade
        Returns: List of validation errors (empty if all valid)
        """
        errors = []
        
        for shape, shape_templates in self.templates.items():
            for difficulty, templates in shape_templates.items():
                for i, template in enumerate(templates):
                    # Basic validation
                    if not template.template_id:
                        errors.append(f"Grade {self.grade}, {shape}, {difficulty}, template {i}: Missing template_id")
                    
                    if not template.question_template:
                        errors.append(f"Grade {self.grade}, {shape}, {difficulty}, template {i}: Missing question_template")
                    
                    if not template.difficulty:
                        errors.append(f"Grade {self.grade}, {shape}, {difficulty}, template {i}: Missing difficulty")
                    
                    if not template.topic:
                        errors.append(f"Grade {self.grade}, {shape}, {difficulty}, template {i}: Missing topic")
        
        return errors
