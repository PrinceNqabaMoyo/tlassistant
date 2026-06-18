"""
Central registry for all grade template modules
Manages registration and retrieval of templates across all grades
"""

from typing import Dict, List, Optional, Any
from .template_base import GradeTemplateModule
from ...quiz_models import QuestionTemplate
import importlib
import os
import sys


class TemplateRegistry:
    """
    Central registry for all grade template modules
    Provides unified access to templates across all grades
    """
    
    def __init__(self):
        self.grades: Dict[int, GradeTemplateModule] = {}
        self._initialized = False
        self._load_all_grade_modules()
    
    def _load_all_grade_modules(self):
        """
        Dynamically load all grade modules from the 'templates' directory
        """
        current_dir = os.path.dirname(__file__)
        templates_root = os.path.abspath(os.path.join(current_dir, '..'))  # app/utils/templates

        if templates_root not in sys.path:
            sys.path.insert(0, templates_root)
        
        print(f"Loading template modules from: {templates_root}")

        for grade_dir in os.listdir(templates_root):
            if grade_dir.startswith('grade') and os.path.isdir(os.path.join(templates_root, grade_dir)):
                try:
                    grade_num = int(grade_dir.replace('grade', ''))
                    module_name = f"app.utils.templates.{grade_dir}"  # e.g., app.utils.templates.grade7
                    
                    module = importlib.import_module(module_name)
                    
                    if hasattr(module, 'GradeTemplateModule') and issubclass(module.GradeTemplateModule, GradeTemplateModule):
                        grade_module_instance = module.GradeTemplateModule(grade=grade_num)
                        self.register_grade(grade_num, grade_module_instance)
                        print(f"Successfully loaded Grade {grade_num} module")
                    else:
                        print(f"Warning: {grade_dir} module does not have GradeTemplateModule class or it's not a subclass of base.GradeTemplateModule")
                except Exception as e:
                    print(f"Error loading {grade_dir}: {e}")
        
        if templates_root in sys.path:
            sys.path.remove(templates_root)

    def register_grade(self, grade: int, module: GradeTemplateModule):
        """
        Register a grade module
        Args:
            grade: Grade number (7-12)
            module: GradeTemplateModule instance
        """
        if not isinstance(grade, int) or grade < 1 or grade > 12:
            raise ValueError(f"Invalid grade: {grade}. Must be integer between 1 and 12")
        
        if not isinstance(module, GradeTemplateModule):
            raise ValueError("Module must be instance of GradeTemplateModule")
        
        self.grades[grade] = module
        print(f"Registered Grade {grade} template module with {module.get_template_count()} templates")
    
    def get_templates(self, grade: int, shape: str, difficulty: str) -> List[QuestionTemplate]:
        """
        Get templates for specific grade, shape, and difficulty
        Args:
            grade: Grade number
            shape: Shape type
            difficulty: Difficulty level
        Returns: List of QuestionTemplate objects
        """
        if grade not in self.grades:
            raise ValueError(f"Grade {grade} not available. Available grades: {self.get_available_grades()}")
        
        return self.grades[grade].get_templates(shape, difficulty)
    
    def get_available_grades(self) -> List[int]:
        """
        Get list of available grades
        Returns: Sorted list of available grade numbers
        """
        return sorted(self.grades.keys())
    
    def get_available_shapes(self, grade: int) -> List[str]:
        """
        Get list of available shapes for a specific grade
        Args:
            grade: Grade number
        Returns: List of shape names
        """
        if grade not in self.grades:
            return []
        return self.grades[grade].get_available_shapes()
    
    def get_available_difficulties(self, grade: int) -> List[str]:
        """
        Get list of available difficulties for a specific grade
        Args:
            grade: Grade number
        Returns: List of difficulty levels
        """
        if grade not in self.grades:
            return []
        return self.grades[grade].get_available_difficulties()
    
    def get_grade_info(self, grade: int) -> Optional[Dict]:
        """
        Get information about a specific grade
        Args:
            grade: Grade number
        Returns: Dictionary with grade information or None if not found
        """
        if grade not in self.grades:
            return None
        
        module = self.grades[grade]
        return {
            'grade': grade,
            'total_templates': module.get_template_count(),
            'shapes': module.get_available_shapes(),
            'difficulties': module.get_available_difficulties(),
            'shape_counts': {
                shape: module.get_shape_template_count(shape) 
                for shape in module.get_available_shapes()
            },
            'difficulty_counts': {
                difficulty: module.get_difficulty_template_count(difficulty)
                for difficulty in module.get_available_difficulties()
            }
        }
    
    def get_all_grades_info(self) -> Dict[int, Dict]:
        """
        Get information about all registered grades
        Returns: Dictionary with grade -> info mapping
        """
        return {
            grade: self.get_grade_info(grade)
            for grade in self.get_available_grades()
        }
    
    def validate_all_templates(self) -> Dict[int, List[str]]:
        """
        Validate all templates across all grades
        Returns: Dictionary with grade -> validation errors
        """
        errors = {}
        for grade, module in self.grades.items():
            grade_errors = module.validate_templates()
            if grade_errors:
                errors[grade] = grade_errors
        return errors
    
    def get_total_template_count(self) -> int:
        """
        Get total number of templates across all grades
        Returns: Total template count
        """
        return sum(module.get_template_count() for module in self.grades.values())
    
    def is_grade_available(self, grade: int) -> bool:
        """
        Check if a grade is available
        Args:
            grade: Grade number
        Returns: True if grade is available
        """
        return grade in self.grades
