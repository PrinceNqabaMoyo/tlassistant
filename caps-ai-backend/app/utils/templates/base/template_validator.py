"""
Template validation system
Validates template structure, content, and consistency
"""

from typing import Dict, List, Optional, Tuple
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class TemplateValidator:
    """
    Validates template structure, content, and consistency
    """
    
    def __init__(self):
        self.validation_rules = self._initialize_validation_rules()
    
    def _initialize_validation_rules(self) -> Dict[str, List[str]]:
        """
        Initialize validation rules for templates
        Returns: Dictionary of rule categories and their rules
        """
        return {
            'required_fields': [
                'template_id',
                'question_template', 
                'difficulty',
                'topic',
                'question_type',
                'shape_type'
            ],
            'valid_difficulties': ['easy', 'medium', 'hard'],
            'valid_question_types': [qt.value for qt in QuestionType],
            'valid_shape_types': [st.value for st in ShapeType],
            'required_parameter_fields': [
                'parameter_ranges',
                'constraints',
                'metric_units'
            ]
        }
    
    def validate_template(self, template: QuestionTemplate) -> List[str]:
        """
        Validate a single template
        Args:
            template: QuestionTemplate to validate
        Returns: List of validation errors
        """
        errors = []
        
        # Check required fields
        for field in self.validation_rules['required_fields']:
            if not hasattr(template, field) or getattr(template, field) is None:
                errors.append(f"Missing required field: {field}")
        
        # Validate difficulty
        if hasattr(template, 'difficulty') and template.difficulty:
            if isinstance(template.difficulty, DifficultyLevel):
                difficulty_value = template.difficulty.value
            else:
                difficulty_value = str(template.difficulty)
            
            if difficulty_value not in self.validation_rules['valid_difficulties']:
                errors.append(f"Invalid difficulty: {difficulty_value}")
        
        # Validate question type
        if hasattr(template, 'question_type') and template.question_type:
            if isinstance(template.question_type, QuestionType):
                question_type_value = template.question_type.value
            else:
                question_type_value = str(template.question_type)
            
            if question_type_value not in self.validation_rules['valid_question_types']:
                errors.append(f"Invalid question_type: {question_type_value}")
        
        # Validate shape type
        if hasattr(template, 'shape_type') and template.shape_type:
            if isinstance(template.shape_type, ShapeType):
                shape_type_value = template.shape_type.value
            else:
                shape_type_value = str(template.shape_type)
            
            if shape_type_value not in self.validation_rules['valid_shape_types']:
                errors.append(f"Invalid shape_type: {shape_type_value}")
        
        # Validate template_id format
        if hasattr(template, 'template_id') and template.template_id:
            if not self._validate_template_id(template.template_id):
                errors.append(f"Invalid template_id format: {template.template_id}")
        
        # Validate question_template has placeholders
        if hasattr(template, 'question_template') and template.question_template:
            if not self._validate_question_template(template.question_template):
                errors.append("Question template should contain parameter placeholders")
        
        # Validate parameter_ranges
        if hasattr(template, 'parameter_ranges') and template.parameter_ranges:
            param_errors = self._validate_parameter_ranges(template.parameter_ranges)
            errors.extend(param_errors)
        
        return errors
    
    def _validate_template_id(self, template_id: str) -> bool:
        """
        Validate template_id format
        Args:
            template_id: Template ID string
        Returns: True if valid format
        """
        if not template_id or not isinstance(template_id, str):
            return False
        
        # Should contain underscores and be descriptive
        parts = template_id.split('_')
        if len(parts) < 2:
            return False
        
        # Should not contain spaces or special characters
        if ' ' in template_id or not template_id.replace('_', '').isalnum():
            return False
        
        return True
    
    def _validate_question_template(self, question_template: str) -> bool:
        """
        Validate question template has parameter placeholders
        Args:
            question_template: Question template string
        Returns: True if has placeholders
        """
        if not question_template or not isinstance(question_template, str):
            return False
        
        # Should contain {parameter} placeholders
        return '{' in question_template and '}' in question_template
    
    def _validate_parameter_ranges(self, parameter_ranges: Dict) -> List[str]:
        """
        Validate parameter ranges
        Args:
            parameter_ranges: Dictionary of parameter ranges
        Returns: List of validation errors
        """
        errors = []
        
        if not isinstance(parameter_ranges, dict):
            errors.append("parameter_ranges must be a dictionary")
            return errors
        
        for param_name, param_range in parameter_ranges.items():
            if not isinstance(param_name, str):
                errors.append(f"Parameter name must be string: {param_name}")
                continue
            
            if not isinstance(param_range, (tuple, list)) or len(param_range) != 2:
                errors.append(f"Parameter range must be tuple/list of length 2: {param_name}")
                continue
            
            min_val, max_val = param_range
            if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
                errors.append(f"Parameter range values must be numbers: {param_name}")
                continue
            
            if min_val >= max_val:
                errors.append(f"Parameter range min must be less than max: {param_name}")
        
        return errors
    
    def validate_grade_templates(self, templates: Dict[str, Dict[str, List[QuestionTemplate]]]) -> Dict[str, List[str]]:
        """
        Validate all templates for a grade
        Args:
            templates: Grade templates dictionary
        Returns: Dictionary of validation errors by shape/difficulty
        """
        errors = {}
        
        for shape, shape_templates in templates.items():
            for difficulty, template_list in shape_templates.items():
                shape_difficulty_key = f"{shape}_{difficulty}"
                shape_difficulty_errors = []
                
                for i, template in enumerate(template_list):
                    template_errors = self.validate_template(template)
                    if template_errors:
                        shape_difficulty_errors.extend([
                            f"Template {i}: {error}" for error in template_errors
                        ])
                
                if shape_difficulty_errors:
                    errors[shape_difficulty_key] = shape_difficulty_errors
        
        return errors
    
    def validate_consistency(self, templates: Dict[str, Dict[str, List[QuestionTemplate]]]) -> List[str]:
        """
        Validate consistency across templates
        Args:
            templates: Grade templates dictionary
        Returns: List of consistency errors
        """
        errors = []
        
        # Check for duplicate template IDs
        template_ids = set()
        for shape_templates in templates.values():
            for template_list in shape_templates.values():
                for template in template_list:
                    if template.template_id in template_ids:
                        errors.append(f"Duplicate template_id: {template.template_id}")
                    template_ids.add(template.template_id)
        
        # Check for consistent difficulty levels
        difficulties = set()
        for shape_templates in templates.values():
            for difficulty in shape_templates.keys():
                difficulties.add(difficulty)
        
        expected_difficulties = set(self.validation_rules['valid_difficulties'])
        if difficulties != expected_difficulties:
            missing = expected_difficulties - difficulties
            extra = difficulties - expected_difficulties
            if missing:
                errors.append(f"Missing difficulty levels: {missing}")
            if extra:
                errors.append(f"Extra difficulty levels: {extra}")
        
        return errors
