"""
Curriculum Validation System
Ensures all quiz questions align with Grade 7 CAPS curriculum requirements
"""

from typing import Dict, List, Any, Tuple
from enum import Enum
from dataclasses import dataclass
from .quiz_models import QuizQuestion, DifficultyLevel, QuestionType, ShapeType

class CurriculumArea(Enum):
    """Grade 7 CAPS curriculum areas for geometry"""
    PROPERTIES_2D_SHAPES = "Properties of 2D Shapes"
    CALCULATIONS_2D_SHAPES = "Calculations involving 2D Shapes"
    SIMILARITY_CONGRUENCY = "Similarity and Congruency"
    PROBLEM_SOLVING = "Problem Solving"
    UNIT_CONVERSIONS = "Unit Conversions"
    REAL_WORLD_APPLICATIONS = "Real-world Applications"

class ValidationResult(Enum):
    """Validation result status"""
    VALID = "valid"
    WARNING = "warning"
    INVALID = "invalid"

@dataclass
class CurriculumValidation:
    """Result of curriculum validation"""
    is_valid: bool
    result: ValidationResult
    curriculum_areas: List[CurriculumArea]
    missing_areas: List[CurriculumArea]
    warnings: List[str]
    errors: List[str]
    suggestions: List[str]

class CurriculumValidator:
    """
    Validates quiz questions against Grade 7 CAPS curriculum requirements
    """
    
    def __init__(self):
        self.curriculum_requirements = self._initialize_curriculum_requirements()
        self.south_african_contexts = self._initialize_south_african_contexts()
        self.metric_units = self._initialize_metric_units()
    
    def _initialize_curriculum_requirements(self) -> Dict[CurriculumArea, Dict[str, Any]]:
        """Initialize Grade 7 CAPS curriculum requirements"""
        return {
            CurriculumArea.PROPERTIES_2D_SHAPES: {
                'required_concepts': [
                    'triangle_classification', 'quadrilateral_classification',
                    'angle_types', 'shape_properties', 'geometric_relationships'
                ],
                'difficulty_levels': ['easy', 'medium', 'hard'],
                'required_shapes': ['triangles', 'quadrilaterals', 'circles', 'angles']
            },
            CurriculumArea.CALCULATIONS_2D_SHAPES: {
                'required_concepts': [
                    'area_calculations', 'perimeter_calculations', 'angle_calculations',
                    'composite_areas', 'shaded_regions'
                ],
                'difficulty_levels': ['easy', 'medium', 'hard'],
                'required_formulas': ['area_triangle', 'area_rectangle', 'area_circle', 'perimeter']
            },
            CurriculumArea.SIMILARITY_CONGRUENCY: {
                'required_concepts': [
                    'similarity_recognition', 'congruency_recognition',
                    'proportional_reasoning', 'shape_comparison'
                ],
                'difficulty_levels': ['medium', 'hard'],
                'required_shapes': ['triangles', 'quadrilaterals']
            },
            CurriculumArea.PROBLEM_SOLVING: {
                'required_concepts': [
                    'multi_step_problems', 'real_world_applications',
                    'reasoning_skills', 'problem_decomposition'
                ],
                'difficulty_levels': ['hard'],
                'required_contexts': ['south_african', 'practical', 'mathematical']
            },
            CurriculumArea.UNIT_CONVERSIONS: {
                'required_concepts': [
                    'metric_length_conversions', 'metric_area_conversions',
                    'unit_appropriateness', 'conversion_reasoning'
                ],
                'difficulty_levels': ['easy', 'medium', 'hard'],
                'required_units': ['mm', 'cm', 'm', 'km', 'mm²', 'cm²', 'm²']
            },
            CurriculumArea.REAL_WORLD_APPLICATIONS: {
                'required_concepts': [
                    'practical_problems', 'contextual_reasoning',
                    'south_african_contexts', 'everyday_applications'
                ],
                'difficulty_levels': ['easy', 'medium', 'hard'],
                'required_contexts': ['garden', 'construction', 'school', 'home', 'sports']
            }
        }
    
    def _initialize_south_african_contexts(self) -> Dict[str, List[str]]:
        """Initialize South African real-world contexts"""
        return {
            'garden_landscaping': [
                'Johannesburg garden', 'Cape Town flower bed', 'Durban garden plot',
                'Pretoria school garden', 'Port Elizabeth community garden'
            ],
            'construction_home': [
                'Soweto house', 'Sandton building', 'Cape Town construction',
                'Durban home improvement', 'Pretoria school project'
            ],
            'school_education': [
                'Soweto school', 'Sandton school', 'Cape Town school',
                'Durban school project', 'Pretoria science fair'
            ],
            'sports_recreation': [
                'Orlando soccer field', 'Newlands cricket pitch', 'Ellis Park rugby field',
                'Loftus stadium', 'Kings Park sports complex'
            ],
            'farming_agriculture': [
                'Free State farm', 'Mpumalanga crop field', 'Western Cape vineyard',
                'KwaZulu-Natal farm', 'Northern Cape agricultural project'
            ]
        }
    
    def _initialize_metric_units(self) -> Dict[str, List[str]]:
        """Initialize appropriate metric units for different contexts"""
        return {
            'length_units': ['mm', 'cm', 'm', 'km'],
            'area_units': ['mm²', 'cm²', 'm²', 'ha'],
            'context_appropriate_units': {
                'garden_landscaping': ['cm', 'm', 'cm²', 'm²'],
                'construction_home': ['cm', 'm', 'cm²', 'm²'],
                'school_education': ['mm', 'cm', 'm', 'mm²', 'cm²', 'm²'],
                'sports_recreation': ['m', 'km', 'm²', 'ha'],
                'farming_agriculture': ['m', 'km', 'm²', 'ha']
            }
        }
    
    def validate_question(self, question: QuizQuestion) -> CurriculumValidation:
        """Validate a single quiz question against curriculum requirements"""
        errors = []
        warnings = []
        suggestions = []
        curriculum_areas = []
        missing_areas = []
        
        # Check curriculum alignment
        curriculum_areas = self._identify_curriculum_areas(question)
        
        # Validate South African context
        if question.south_african_context:
            context_validation = self._validate_south_african_context(question)
            if not context_validation['valid']:
                errors.extend(context_validation['errors'])
                warnings.extend(context_validation['warnings'])
        
        # Validate metric units
        metric_validation = self._validate_metric_units(question)
        if not metric_validation['valid']:
            errors.extend(metric_validation['errors'])
            warnings.extend(metric_validation['warnings'])
        
        # Validate difficulty progression
        difficulty_validation = self._validate_difficulty_progression(question)
        if not difficulty_validation['valid']:
            warnings.extend(difficulty_validation['warnings'])
            suggestions.extend(difficulty_validation['suggestions'])
        
        # Validate educational value
        educational_validation = self._validate_educational_value(question)
        if not educational_validation['valid']:
            warnings.extend(educational_validation['warnings'])
            suggestions.extend(educational_validation['suggestions'])
        
        # Determine overall validation result
        is_valid = len(errors) == 0
        result = ValidationResult.VALID if is_valid else (ValidationResult.WARNING if len(warnings) > 0 else ValidationResult.INVALID)
        
        return CurriculumValidation(
            is_valid=is_valid,
            result=result,
            curriculum_areas=curriculum_areas,
            missing_areas=missing_areas,
            warnings=warnings,
            errors=errors,
            suggestions=suggestions
        )
    
    def _identify_curriculum_areas(self, question: QuizQuestion) -> List[CurriculumArea]:
        """Identify which curriculum areas a question covers"""
        areas = []
        
        # Check curriculum alignments
        if question.curriculum_alignments:
            for alignment in question.curriculum_alignments:
                if "Properties" in alignment:
                    areas.append(CurriculumArea.PROPERTIES_2D_SHAPES)
                elif "Calculations" in alignment:
                    areas.append(CurriculumArea.CALCULATIONS_2D_SHAPES)
                elif "Similarity" in alignment or "Congruency" in alignment:
                    areas.append(CurriculumArea.SIMILARITY_CONGRUENCY)
                elif "Unit Conversions" in alignment:
                    areas.append(CurriculumArea.UNIT_CONVERSIONS)
                elif "Problem Solving" in alignment:
                    areas.append(CurriculumArea.PROBLEM_SOLVING)
        
        # Check question type
        if question.question_type == QuestionType.UNIT_CONVERSION:
            areas.append(CurriculumArea.UNIT_CONVERSIONS)
        elif question.question_type in [QuestionType.SHAPE_CLASSIFICATION, QuestionType.QUADRILATERAL_SORTING, QuestionType.QUADRILATERAL_GROUPING]:
            areas.append(CurriculumArea.PROPERTIES_2D_SHAPES)
        elif question.question_type in [QuestionType.AREA_CALCULATION, QuestionType.PERIMETER_CALCULATION, QuestionType.COMPOSITE_AREA_CALCULATION]:
            areas.append(CurriculumArea.CALCULATIONS_2D_SHAPES)
        elif question.question_type in [QuestionType.SIMILARITY_RECOGNITION, QuestionType.CONGRUENCY_RECOGNITION]:
            areas.append(CurriculumArea.SIMILARITY_CONGRUENCY)
        
        # Check for real-world context
        if question.south_african_context:
            areas.append(CurriculumArea.REAL_WORLD_APPLICATIONS)
        
        return list(set(areas))  # Remove duplicates
    
    def _validate_south_african_context(self, question: QuizQuestion) -> Dict[str, Any]:
        """Validate South African context appropriateness"""
        errors = []
        warnings = []
        
        # Check if question text contains South African context
        question_text = question.question.lower()
        has_sa_context = any(
            any(location.lower() in question_text for location in locations)
            for locations in self.south_african_contexts.values()
        )
        
        if question.south_african_context and not has_sa_context:
            warnings.append("Question marked as South African context but no SA location found in text")
        
        # Check context appropriateness for question type
        if question.question_type == QuestionType.UNIT_CONVERSION:
            if not any(unit in question_text for unit in ['cm', 'm', 'mm', 'km', 'cm²', 'm²']):
                warnings.append("Unit conversion question should include metric units")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def _validate_metric_units(self, question: QuizQuestion) -> Dict[str, Any]:
        """Validate metric unit usage"""
        errors = []
        warnings = []
        
        # Check if metric units are present
        if question.metric_units:
            units = question.metric_units.values()
            if not any(unit in ['mm', 'cm', 'm', 'km', 'mm²', 'cm²', 'm²', 'ha'] for unit in units):
                errors.append("Question must use appropriate metric units")
        
        # Check unit appropriateness for context
        if question.south_african_context:
            question_text = question.question.lower()
            if 'garden' in question_text or 'plot' in question_text:
                if not any(unit in question_text for unit in ['cm', 'm', 'cm²', 'm²']):
                    warnings.append("Garden context should use cm/m units, not mm/km")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def _validate_difficulty_progression(self, question: QuizQuestion) -> Dict[str, Any]:
        """Validate difficulty progression appropriateness"""
        warnings = []
        suggestions = []
        
        # Check if difficulty matches question complexity
        if question.difficulty == DifficultyLevel.EASY:
            if question.reasoning_required:
                warnings.append("Easy questions should not require complex reasoning")
            if len(question.parameters) > 3:
                warnings.append("Easy questions should have simple parameters")
        
        elif question.difficulty == DifficultyLevel.HARD:
            if not question.reasoning_required:
                suggestions.append("Hard questions should require reasoning")
            if len(question.parameters) < 2:
                suggestions.append("Hard questions should have multiple parameters")
        
        return {
            'valid': len(warnings) == 0,
            'warnings': warnings,
            'suggestions': suggestions
        }
    
    def _validate_educational_value(self, question: QuizQuestion) -> Dict[str, Any]:
        """Validate educational value and learning objectives"""
        warnings = []
        suggestions = []
        
        # Check explanation quality
        if not question.explanation or len(question.explanation) < 20:
            warnings.append("Explanation should be detailed and educational")
        
        # Check options quality
        if len(question.options) < 4:
            warnings.append("Question should have 4 options")
        
        # Check for educational progression
        if question.difficulty == DifficultyLevel.MEDIUM:
            if not any(keyword in question.explanation.lower() for keyword in ['formula', 'calculate', 'step']):
                suggestions.append("Medium questions should include step-by-step explanations")
        
        return {
            'valid': len(warnings) == 0,
            'warnings': warnings,
            'suggestions': suggestions
        }
    
    def validate_question_batch(self, questions: List[QuizQuestion]) -> Dict[str, Any]:
        """Validate a batch of questions for curriculum coverage"""
        validation_results = [self.validate_question(q) for q in questions]
        
        # Calculate coverage statistics
        all_areas = set()
        covered_areas = set()
        
        for result in validation_results:
            all_areas.update(result.curriculum_areas)
            covered_areas.update(result.curriculum_areas)
        
        coverage_percentage = (len(covered_areas) / len(CurriculumArea)) * 100
        
        # Calculate validation statistics
        valid_count = sum(1 for r in validation_results if r.is_valid)
        warning_count = sum(1 for r in validation_results if r.result == ValidationResult.WARNING)
        invalid_count = sum(1 for r in validation_results if r.result == ValidationResult.INVALID)
        
        return {
            'total_questions': len(questions),
            'valid_questions': valid_count,
            'warning_questions': warning_count,
            'invalid_questions': invalid_count,
            'curriculum_coverage': coverage_percentage,
            'covered_areas': list(covered_areas),
            'missing_areas': [area for area in CurriculumArea if area not in covered_areas],
            'validation_results': validation_results
        }
