"""
Modular Template System
Supports Grades 7-12 geometry templates with scalable architecture
"""

from .base.template_registry import TemplateRegistry
from .base.template_loader import TemplateLoader

# Initialize the template system
template_loader = TemplateLoader()
template_registry = template_loader.registry

def get_templates(grade: int, shape: str, difficulty: str):
    """Get templates for specific grade, shape, and difficulty"""
    return template_registry.get_templates(grade, shape, difficulty)

def get_available_grades():
    """Get list of available grades"""
    return template_registry.get_available_grades()

def get_available_shapes(grade: int):
    """Get list of available shapes for a specific grade"""
    if grade in template_registry.grades:
        return template_registry.grades[grade].get_available_shapes()
    return []

def get_available_difficulties(grade: int):
    """Get list of available difficulties for a specific grade"""
    if grade in template_registry.grades:
        return template_registry.grades[grade].get_available_difficulties()
    return []
