"""
Metric System Validation System
Ensures comprehensive metric system coverage and compliance throughout all quiz types
"""

from typing import Dict, List, Any, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
from .quiz_models import QuizQuestion, DifficultyLevel, QuestionType, ShapeType

class MetricValidationResult(Enum):
    """Metric validation result status"""
    VALID = "valid"
    WARNING = "warning"
    INVALID = "invalid"

class UnitType(Enum):
    """Types of metric units"""
    LENGTH = "length"
    AREA = "area"
    VOLUME = "volume"

@dataclass
class MetricValidation:
    """Result of metric system validation"""
    is_valid: bool
    result: MetricValidationResult
    metric_compliance: float  # Percentage of metric compliance
    unit_appropriateness: float  # Percentage of context-appropriate units
    conversion_coverage: float  # Percentage of conversion questions
    warnings: List[str]
    errors: List[str]
    suggestions: List[str]
    missing_units: List[str]
    inappropriate_units: List[str]

class MetricSystemValidator:
    """
    Validates comprehensive metric system coverage and compliance
    """
    
    def __init__(self):
        self.metric_units = self._initialize_metric_units()
        self.context_appropriate_units = self._initialize_context_appropriate_units()
        self.conversion_requirements = self._initialize_conversion_requirements()
        self.south_african_standards = self._initialize_south_african_standards()
    
    def _initialize_metric_units(self) -> Dict[UnitType, List[str]]:
        """Initialize comprehensive metric unit system"""
        return {
            UnitType.LENGTH: ['mm', 'cm', 'm', 'km'],
            UnitType.AREA: ['mm²', 'cm²', 'm²', 'ha'],
            UnitType.VOLUME: ['mm³', 'cm³', 'm³', 'L', 'kL']
        }
    
    def _initialize_context_appropriate_units(self) -> Dict[str, List[str]]:
        """Initialize context-appropriate unit mappings"""
        return {
            'garden_landscaping': {
                'length': ['cm', 'm'],
                'area': ['cm²', 'm²']
            },
            'construction_home': {
                'length': ['cm', 'm'],
                'area': ['cm²', 'm²']
            },
            'school_education': {
                'length': ['mm', 'cm', 'm'],
                'area': ['mm²', 'cm²', 'm²']
            },
            'sports_recreation': {
                'length': ['m', 'km'],
                'area': ['m²', 'ha']
            },
            'farming_agriculture': {
                'length': ['m', 'km'],
                'area': ['m²', 'ha']
            },
            'general_measurement': {
                'length': ['mm', 'cm', 'm', 'km'],
                'area': ['mm²', 'cm²', 'm²', 'ha']
            }
        }
    
    def _initialize_conversion_requirements(self) -> Dict[DifficultyLevel, List[str]]:
        """Initialize conversion requirements by difficulty level"""
        return {
            DifficultyLevel.EASY: [
                'mm_cm', 'cm_m', 'mm²_cm²', 'cm²_m²'
            ],
            DifficultyLevel.MEDIUM: [
                'mm_cm', 'cm_m', 'm_km', 'mm²_cm²', 'cm²_m²', 'm²_ha'
            ],
            DifficultyLevel.HARD: [
                'mm_cm', 'cm_m', 'm_km', 'mm²_cm²', 'cm²_m²', 'm²_ha',
                'complex_conversions', 'multi_step_conversions'
            ]
        }
    
    def _initialize_south_african_standards(self) -> Dict[str, Any]:
        """Initialize South African metric system standards"""
        return {
            'preferred_units': {
                'small_measurements': ['mm', 'cm'],
                'medium_measurements': ['cm', 'm'],
                'large_measurements': ['m', 'km'],
                'small_areas': ['cm²', 'm²'],
                'large_areas': ['m²', 'ha']
            },
            'avoid_units': ['inches', 'feet', 'yards', 'miles', 'square_inches', 'acres'],
            'conversion_factors': {
                'mm_to_cm': 0.1,
                'cm_to_m': 0.01,
                'm_to_km': 0.001,
                'mm²_to_cm²': 0.01,
                'cm²_to_m²': 0.0001,
                'm²_to_ha': 0.0001
            }
        }
    
    def validate_question_metrics(self, question: QuizQuestion) -> MetricValidation:
        """Validate metric system compliance for a single question"""
        errors = []
        warnings = []
        suggestions = []
        missing_units = []
        inappropriate_units = []
        
        # Check if question uses metric units
        metric_compliance = self._check_metric_compliance(question, errors, warnings)
        
        # Check unit appropriateness for context
        unit_appropriateness = self._check_unit_appropriateness(question, warnings, inappropriate_units)
        
        # Check conversion requirements
        conversion_coverage = self._check_conversion_coverage(question, suggestions)
        
        # Check South African standards compliance
        self._check_south_african_standards(question, errors, warnings)
        
        # Check for missing essential units
        self._check_missing_essential_units(question, missing_units, suggestions)
        
        # Calculate overall validation
        is_valid = len(errors) == 0
        result = MetricValidationResult.VALID if is_valid else (
            MetricValidationResult.WARNING if len(warnings) > 0 else MetricValidationResult.INVALID
        )
        
        return MetricValidation(
            is_valid=is_valid,
            result=result,
            metric_compliance=metric_compliance,
            unit_appropriateness=unit_appropriateness,
            conversion_coverage=conversion_coverage,
            warnings=warnings,
            errors=errors,
            suggestions=suggestions,
            missing_units=missing_units,
            inappropriate_units=inappropriate_units
        )
    
    def _check_metric_compliance(self, question: QuizQuestion, errors: List[str], warnings: List[str]) -> float:
        """Check if question uses proper metric units"""
        compliance_score = 0.0
        total_checks = 0
        
        # Check question text for metric units
        question_text = question.question.lower()
        has_metric_units = any(unit in question_text for unit in 
                              ['mm', 'cm', 'm', 'km', 'mm²', 'cm²', 'm²', 'ha'])
        
        if has_metric_units:
            compliance_score += 1.0
        else:
            errors.append("Question must use metric units (mm, cm, m, km, mm², cm², m², ha)")
        
        total_checks += 1
        
        # Check options for metric units
        metric_options = sum(1 for option in question.options 
                           if any(unit in option.lower() for unit in 
                                 ['mm', 'cm', 'm', 'km', 'mm²', 'cm²', 'm²', 'ha']))
        
        if metric_options > 0:
            compliance_score += 1.0
        else:
            errors.append("Answer options must include metric units")
        
        total_checks += 1
        
        # Check metric_units field
        if question.metric_units:
            metric_units_count = len(question.metric_units)
            if metric_units_count > 0:
                compliance_score += 1.0
            else:
                warnings.append("Metric units field should specify units used")
        else:
            warnings.append("Question should specify metric units used")
        
        total_checks += 1
        
        return (compliance_score / total_checks) * 100 if total_checks > 0 else 0.0
    
    def _check_unit_appropriateness(self, question: QuizQuestion, warnings: List[str], inappropriate_units: List[str]) -> float:
        """Check if units are appropriate for the context"""
        appropriateness_score = 0.0
        total_checks = 0
        
        # Determine context from question
        context = self._determine_question_context(question)
        appropriate_units = self.context_appropriate_units.get(context, 
                                                             self.context_appropriate_units['general_measurement'])
        
        # Check length units
        question_text = question.question.lower()
        length_units_used = [unit for unit in ['mm', 'cm', 'm', 'km'] if unit in question_text]
        
        if length_units_used:
            appropriate_length_units = appropriate_units.get('length', ['cm', 'm'])
            for unit in length_units_used:
                if unit in appropriate_length_units:
                    appropriateness_score += 1.0
                else:
                    inappropriate_units.append(f"Unit '{unit}' may not be appropriate for {context} context")
            total_checks += len(length_units_used)
        
        # Check area units
        area_units_used = [unit for unit in ['mm²', 'cm²', 'm²', 'ha'] if unit in question_text]
        
        if area_units_used:
            appropriate_area_units = appropriate_units.get('area', ['cm²', 'm²'])
            for unit in area_units_used:
                if unit in appropriate_area_units:
                    appropriateness_score += 1.0
                else:
                    inappropriate_units.append(f"Unit '{unit}' may not be appropriate for {context} context")
            total_checks += len(area_units_used)
        
        return (appropriateness_score / total_checks) * 100 if total_checks > 0 else 100.0
    
    def _check_conversion_coverage(self, question: QuizQuestion, suggestions: List[str]) -> float:
        """Check if question covers appropriate conversion requirements"""
        if question.question_type == QuestionType.UNIT_CONVERSION:
            return 100.0  # Full coverage for conversion questions
        
        # Check if question requires conversion
        if question.conversion_required:
            return 80.0  # Good coverage for conversion-required questions
        
        # Check difficulty-based conversion requirements
        required_conversions = self.conversion_requirements.get(question.difficulty, [])
        if required_conversions:
            suggestions.append(f"Consider adding unit conversion for {question.difficulty.value} difficulty")
            return 40.0  # Partial coverage
        
        return 0.0  # No conversion coverage
    
    def _check_south_african_standards(self, question: QuizQuestion, errors: List[str], warnings: List[str]):
        """Check compliance with South African metric standards"""
        question_text = question.question.lower()
        
        # Check for non-metric units (should be avoided)
        non_metric_units = self.south_african_standards['avoid_units']
        found_non_metric = [unit for unit in non_metric_units if unit in question_text]
        
        if found_non_metric:
            errors.append(f"Question contains non-metric units: {found_non_metric}")
        
        # Check for South African context compliance
        if question.south_african_context:
            # Ensure appropriate units for SA context
            if 'garden' in question_text or 'plot' in question_text:
                if not any(unit in question_text for unit in ['cm', 'm', 'cm²', 'm²']):
                    warnings.append("Garden context should use cm/m units, not mm/km")
            
            elif 'field' in question_text or 'farm' in question_text:
                if not any(unit in question_text for unit in ['m', 'km', 'm²', 'ha']):
                    warnings.append("Field/farm context should use m/km/ha units")
    
    def _check_missing_essential_units(self, question: QuizQuestion, missing_units: List[str], suggestions: List[str]):
        """Check for missing essential units based on question type"""
        question_text = question.question.lower()
        
        # Check based on question type
        if question.question_type in [QuestionType.AREA_CALCULATION, QuestionType.COMPOSITE_AREA_CALCULATION]:
            if not any(unit in question_text for unit in ['cm²', 'm²', 'mm²', 'ha']):
                missing_units.append("Area calculation should include area units (cm², m², etc.)")
                suggestions.append("Add area units to make the question more complete")
        
        elif question.question_type == QuestionType.PERIMETER_CALCULATION:
            if not any(unit in question_text for unit in ['cm', 'm', 'mm', 'km']):
                missing_units.append("Perimeter calculation should include length units (cm, m, etc.)")
                suggestions.append("Add length units to make the question more complete")
        
        elif question.question_type == QuestionType.UNIT_CONVERSION:
            # Check for conversion pairs
            length_units = ['mm', 'cm', 'm', 'km']
            area_units = ['mm²', 'cm²', 'm²', 'ha']
            
            found_length = [unit for unit in length_units if unit in question_text]
            found_area = [unit for unit in area_units if unit in question_text]
            
            if len(found_length) < 2 and len(found_area) < 2:
                missing_units.append("Unit conversion should include at least two units to convert between")
                suggestions.append("Add multiple units for conversion practice")
    
    def _determine_question_context(self, question: QuizQuestion) -> str:
        """Determine the context of the question for unit appropriateness"""
        question_text = question.question.lower()
        
        if any(word in question_text for word in ['garden', 'plot', 'flower', 'plant']):
            return 'garden_landscaping'
        elif any(word in question_text for word in ['house', 'room', 'building', 'construction']):
            return 'construction_home'
        elif any(word in question_text for word in ['school', 'classroom', 'desk', 'book']):
            return 'school_education'
        elif any(word in question_text for word in ['field', 'sport', 'stadium', 'track']):
            return 'sports_recreation'
        elif any(word in question_text for word in ['farm', 'crop', 'agriculture', 'field']):
            return 'farming_agriculture'
        else:
            return 'general_measurement'
    
    def validate_metric_system_coverage(self, questions: List[QuizQuestion]) -> Dict[str, Any]:
        """Validate comprehensive metric system coverage across all questions"""
        validation_results = [self.validate_question_metrics(q) for q in questions]
        
        # Calculate overall metrics
        total_questions = len(questions)
        valid_questions = sum(1 for r in validation_results if r.is_valid)
        warning_questions = sum(1 for r in validation_results if r.result == MetricValidationResult.WARNING)
        invalid_questions = sum(1 for r in validation_results if r.result == MetricValidationResult.INVALID)
        
        # Calculate average compliance scores
        avg_metric_compliance = sum(r.metric_compliance for r in validation_results) / total_questions if total_questions > 0 else 0
        avg_unit_appropriateness = sum(r.unit_appropriateness for r in validation_results) / total_questions if total_questions > 0 else 0
        avg_conversion_coverage = sum(r.conversion_coverage for r in validation_results) / total_questions if total_questions > 0 else 0
        
        # Count conversion questions
        conversion_questions = sum(1 for q in questions if q.question_type == QuestionType.UNIT_CONVERSION)
        conversion_percentage = (conversion_questions / total_questions) * 100 if total_questions > 0 else 0
        
        # Collect all warnings, errors, and suggestions
        all_warnings = [w for r in validation_results for w in r.warnings]
        all_errors = [e for r in validation_results for e in r.errors]
        all_suggestions = [s for r in validation_results for s in r.suggestions]
        
        return {
            'total_questions': total_questions,
            'valid_questions': valid_questions,
            'warning_questions': warning_questions,
            'invalid_questions': invalid_questions,
            'metric_compliance_percentage': round(avg_metric_compliance, 2),
            'unit_appropriateness_percentage': round(avg_unit_appropriateness, 2),
            'conversion_coverage_percentage': round(avg_conversion_coverage, 2),
            'conversion_questions_count': conversion_questions,
            'conversion_questions_percentage': round(conversion_percentage, 2),
            'total_warnings': len(all_warnings),
            'total_errors': len(all_errors),
            'total_suggestions': len(all_suggestions),
            'detailed_results': [
                {
                    'question_id': getattr(result, 'question_id', f'question_{i}'),
                    'is_valid': result.is_valid,
                    'result': result.result.value,
                    'metric_compliance': result.metric_compliance,
                    'unit_appropriateness': result.unit_appropriateness,
                    'conversion_coverage': result.conversion_coverage,
                    'warnings': result.warnings,
                    'errors': result.errors,
                    'suggestions': result.suggestions,
                    'missing_units': result.missing_units,
                    'inappropriate_units': result.inappropriate_units
                }
                for i, result in enumerate(validation_results)
            ]
        }

