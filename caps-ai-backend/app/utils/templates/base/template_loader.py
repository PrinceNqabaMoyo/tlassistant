"""
Dynamic template loading system
Automatically discovers and loads grade template modules
"""

import os
import importlib
from typing import Dict, List, Optional
from .template_registry import TemplateRegistry
from .template_base import GradeTemplateModule


class TemplateLoader:
    """
    Dynamic template loading system
    Automatically discovers and loads all available grade modules
    """
    
    def __init__(self):
        self.registry = TemplateRegistry()
        self._loaded_modules = set()
        self._load_grade_modules()
    
    def _load_grade_modules(self):
        """
        Dynamically load all available grade modules
        Searches for grade* directories and loads their modules
        """
        # Get the directory containing this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.dirname(current_dir)  # Go up one level to templates/
        
        print(f"Loading template modules from: {templates_dir}")
        
        # Look for grade* directories
        for item in os.listdir(templates_dir):
            if item.startswith('grade') and os.path.isdir(os.path.join(templates_dir, item)):
                try:
                    grade_num = int(item.replace('grade', ''))
                    if 1 <= grade_num <= 12:  # Valid grade range
                        self._load_grade_module(grade_num, item, templates_dir)
                except ValueError:
                    print(f"Warning: Invalid grade directory name: {item}")
                    continue
    
    def _load_grade_module(self, grade_num: int, module_name: str, templates_dir: str):
        """
        Load a specific grade module
        Args:
            grade_num: Grade number
            module_name: Directory name (e.g., 'grade7')
            templates_dir: Path to templates directory
        """
        try:
            # Import the grade module
            module_path = f"app.utils.templates.{module_name}"
            module = importlib.import_module(module_path)
            
            # Look for the GradeTemplateModule class
            if hasattr(module, 'GradeTemplateModule'):
                template_module = module.GradeTemplateModule(grade_num)
                self.registry.register_grade(grade_num, template_module)
                self._loaded_modules.add(grade_num)
                print(f"Successfully loaded Grade {grade_num} module")
            else:
                print(f"Warning: Grade {grade_num} module does not have GradeTemplateModule class")
                
        except ImportError as e:
            print(f"Warning: Could not load grade {grade_num}: {e}")
        except Exception as e:
            print(f"Error loading grade {grade_num}: {e}")
    
    def reload_grade(self, grade_num: int) -> bool:
        """
        Reload a specific grade module
        Args:
            grade_num: Grade number to reload
        Returns: True if successful
        """
        try:
            module_name = f"grade{grade_num}"
            current_dir = os.path.dirname(os.path.abspath(__file__))
            templates_dir = os.path.dirname(current_dir)
            
            # Remove from registry if exists
            if grade_num in self.registry.grades:
                del self.registry.grades[grade_num]
                self._loaded_modules.discard(grade_num)
            
            # Reload the module
            self._load_grade_module(grade_num, module_name, templates_dir)
            return grade_num in self.registry.grades
            
        except Exception as e:
            print(f"Error reloading grade {grade_num}: {e}")
            return False
    
    def reload_all_grades(self):
        """
        Reload all grade modules
        """
        loaded_grades = list(self._loaded_modules)
        self.registry.grades.clear()
        self._loaded_modules.clear()
        self._load_grade_modules()
        
        print(f"Reloaded {len(self._loaded_modules)} grade modules")
    
    def get_loaded_grades(self) -> List[int]:
        """
        Get list of currently loaded grades
        Returns: List of loaded grade numbers
        """
        return list(self._loaded_modules)
    
    def is_grade_loaded(self, grade_num: int) -> bool:
        """
        Check if a grade is currently loaded
        Args:
            grade_num: Grade number
        Returns: True if grade is loaded
        """
        return grade_num in self._loaded_modules
    
    def get_loading_status(self) -> Dict[int, bool]:
        """
        Get loading status for all grades
        Returns: Dictionary with grade -> loaded status
        """
        status = {}
        for grade in range(1, 13):  # Grades 1-12
            status[grade] = self.is_grade_loaded(grade)
        return status
