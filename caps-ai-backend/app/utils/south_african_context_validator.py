"""
South African Context Validation System
Ensures authentic South African real-world contexts and practical problems
"""

from typing import Dict, List, Any, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
from .quiz_models import QuizQuestion, DifficultyLevel, QuestionType, ShapeType

class ContextValidationResult(Enum):
    """Context validation result status"""
    VALID = "valid"
    WARNING = "warning"
    INVALID = "invalid"

class ContextType(Enum):
    """Types of South African contexts"""
    GARDEN_LANDSCAPING = "garden_landscaping"
    CONSTRUCTION_HOME = "construction_home"
    SCHOOL_EDUCATION = "school_education"
    SPORTS_RECREATION = "sports_recreation"
    FARMING_AGRICULTURE = "farming_agriculture"
    URBAN_DEVELOPMENT = "urban_development"
    COMMUNITY_PROJECTS = "community_projects"
    CULTURAL_EVENTS = "cultural_events"

@dataclass
class ContextValidation:
    """Result of South African context validation"""
    is_valid: bool
    result: ContextValidationResult
    context_authenticity: float  # Percentage of authentic SA context
    cultural_appropriateness: float  # Percentage of cultural appropriateness
    practical_relevance: float  # Percentage of practical relevance
    location_accuracy: float  # Percentage of accurate SA locations
    warnings: List[str]
    errors: List[str]
    suggestions: List[str]
    missing_context_elements: List[str]
    inappropriate_elements: List[str]

class SouthAfricanContextValidator:
    """
    Validates South African real-world contexts and practical problems
    """
    
    def __init__(self):
        self.sa_locations = self._initialize_sa_locations()
        self.context_templates = self._initialize_context_templates()
        self.cultural_references = self._initialize_cultural_references()
        self.practical_scenarios = self._initialize_practical_scenarios()
        self.measurement_contexts = self._initialize_measurement_contexts()
    
    def _initialize_sa_locations(self) -> Dict[str, List[str]]:
        """Initialize authentic South African locations by province and context"""
        return {
            'garden_landscaping': {
                'gauteng': ['Johannesburg', 'Pretoria', 'Sandton', 'Soweto', 'Midrand', 'Centurion'],
                'western_cape': ['Cape Town', 'Stellenbosch', 'Paarl', 'George', 'Mossel Bay'],
                'kwazulu_natal': ['Durban', 'Pietermaritzburg', 'Newcastle', 'Pinetown'],
                'eastern_cape': ['Port Elizabeth', 'East London', 'Grahamstown', 'Uitenhage'],
                'free_state': ['Bloemfontein', 'Welkom', 'Bethlehem', 'Kroonstad'],
                'mpumalanga': ['Nelspruit', 'Witbank', 'Secunda', 'Middelburg'],
                'limpopo': ['Polokwane', 'Tzaneen', 'Lephalale', 'Mokopane'],
                'north_west': ['Rustenburg', 'Potchefstroom', 'Klerksdorp', 'Mahikeng'],
                'northern_cape': ['Kimberley', 'Upington', 'Kuruman', 'Springbok']
            },
            'construction_home': {
                'gauteng': ['Johannesburg', 'Pretoria', 'Sandton', 'Soweto', 'Midrand', 'Centurion', 'Roodepoort'],
                'western_cape': ['Cape Town', 'Stellenbosch', 'Paarl', 'George', 'Mossel Bay', 'Worcester'],
                'kwazulu_natal': ['Durban', 'Pietermaritzburg', 'Newcastle', 'Pinetown', 'Umhlanga'],
                'eastern_cape': ['Port Elizabeth', 'East London', 'Grahamstown', 'Uitenhage', 'Queenstown'],
                'free_state': ['Bloemfontein', 'Welkom', 'Bethlehem', 'Kroonstad', 'Sasolburg'],
                'mpumalanga': ['Nelspruit', 'Witbank', 'Secunda', 'Middelburg', 'Emalahleni'],
                'limpopo': ['Polokwane', 'Tzaneen', 'Lephalale', 'Mokopane', 'Modimolle'],
                'north_west': ['Rustenburg', 'Potchefstroom', 'Klerksdorp', 'Mahikeng', 'Brits'],
                'northern_cape': ['Kimberley', 'Upington', 'Kuruman', 'Springbok', 'De Aar']
            },
            'school_education': {
                'gauteng': ['Johannesburg', 'Pretoria', 'Sandton', 'Soweto', 'Midrand', 'Centurion', 'Roodepoort', 'Edenvale'],
                'western_cape': ['Cape Town', 'Stellenbosch', 'Paarl', 'George', 'Mossel Bay', 'Worcester', 'Somerset West'],
                'kwazulu_natal': ['Durban', 'Pietermaritzburg', 'Newcastle', 'Pinetown', 'Umhlanga', 'Westville'],
                'eastern_cape': ['Port Elizabeth', 'East London', 'Grahamstown', 'Uitenhage', 'Queenstown', 'King William\'s Town'],
                'free_state': ['Bloemfontein', 'Welkom', 'Bethlehem', 'Kroonstad', 'Sasolburg', 'Virginia'],
                'mpumalanga': ['Nelspruit', 'Witbank', 'Secunda', 'Middelburg', 'Emalahleni', 'Standerton'],
                'limpopo': ['Polokwane', 'Tzaneen', 'Lephalale', 'Mokopane', 'Modimolle', 'Makhado'],
                'north_west': ['Rustenburg', 'Potchefstroom', 'Klerksdorp', 'Mahikeng', 'Brits', 'Koster'],
                'northern_cape': ['Kimberley', 'Upington', 'Kuruman', 'Springbok', 'De Aar', 'Prieska']
            },
            'sports_recreation': {
                'gauteng': ['Orlando Stadium', 'Ellis Park', 'Loftus Versfeld', 'FNB Stadium', 'Soccer City', 'Newlands'],
                'western_cape': ['Newlands Cricket Ground', 'Cape Town Stadium', 'Green Point Stadium', 'Athlone Stadium'],
                'kwazulu_natal': ['Kings Park Stadium', 'Moses Mabhida Stadium', 'Chatsworth Stadium', 'Princess Magogo Stadium'],
                'eastern_cape': ['Nelson Mandela Bay Stadium', 'Buffalo City Stadium', 'Wolfson Stadium', 'Dan Qeqe Stadium'],
                'free_state': ['Free State Stadium', 'Toyota Stadium', 'Goble Park Stadium', 'Charles Mopeli Stadium'],
                'mpumalanga': ['Mbombela Stadium', 'Kanyamazane Stadium', 'Mpumalanga Stadium', 'Gert Sibande Stadium'],
                'limpopo': ['Peter Mokaba Stadium', 'Old Peter Mokaba Stadium', 'Thohoyandou Stadium', 'Polokwane Stadium'],
                'north_west': ['Royal Bafokeng Stadium', 'Orkney Stadium', 'Rustenburg Stadium', 'Mmabatho Stadium'],
                'northern_cape': ['Kimberley Stadium', 'Upington Stadium', 'Kuruman Stadium', 'Springbok Stadium']
            },
            'farming_agriculture': {
                'gauteng': ['Midrand', 'Centurion', 'Roodepoort', 'Edenvale', 'Kempton Park'],
                'western_cape': ['Stellenbosch', 'Paarl', 'George', 'Mossel Bay', 'Worcester', 'Somerset West', 'Robertson'],
                'kwazulu_natal': ['Pietermaritzburg', 'Newcastle', 'Pinetown', 'Umhlanga', 'Westville', 'Richards Bay'],
                'eastern_cape': ['Port Elizabeth', 'East London', 'Grahamstown', 'Uitenhage', 'Queenstown', 'King William\'s Town'],
                'free_state': ['Bloemfontein', 'Welkom', 'Bethlehem', 'Kroonstad', 'Sasolburg', 'Virginia', 'Bothaville'],
                'mpumalanga': ['Nelspruit', 'Witbank', 'Secunda', 'Middelburg', 'Emalahleni', 'Standerton', 'Ermelo'],
                'limpopo': ['Polokwane', 'Tzaneen', 'Lephalale', 'Mokopane', 'Modimolle', 'Makhado', 'Louis Trichardt'],
                'north_west': ['Rustenburg', 'Potchefstroom', 'Klerksdorp', 'Mahikeng', 'Brits', 'Koster', 'Lichtenburg'],
                'northern_cape': ['Kimberley', 'Upington', 'Kuruman', 'Springbok', 'De Aar', 'Prieska', 'Calvinia']
            }
        }
    
    def _initialize_context_templates(self) -> Dict[ContextType, List[str]]:
        """Initialize context-specific question templates"""
        return {
            ContextType.GARDEN_LANDSCAPING: [
                "A garden plot in {location} needs to be {action}",
                "The school garden at {location} requires {measurement}",
                "A community garden project in {location} involves {shape}",
                "The flower bed at {location} has dimensions {dimensions}",
                "A vegetable patch in {location} needs {calculation}"
            ],
            ContextType.CONSTRUCTION_HOME: [
                "A house construction project in {location} requires {measurement}",
                "The new building at {location} needs {calculation}",
                "A home improvement project in {location} involves {shape}",
                "The renovation at {location} requires {dimensions}",
                "A construction site in {location} needs {action}"
            ],
            ContextType.SCHOOL_EDUCATION: [
                "A school project at {location} involves {measurement}",
                "The classroom at {location} needs {calculation}",
                "A science fair project in {location} requires {shape}",
                "The school grounds at {location} have {dimensions}",
                "A mathematics project at {location} involves {action}"
            ],
            ContextType.SPORTS_RECREATION: [
                "A sports field at {location} needs {measurement}",
                "The stadium in {location} requires {calculation}",
                "A sports complex at {location} involves {shape}",
                "The playing field at {location} has {dimensions}",
                "A sports project in {location} needs {action}"
            ],
            ContextType.FARMING_AGRICULTURE: [
                "A farm in {location} needs {measurement}",
                "The agricultural project at {location} requires {calculation}",
                "A crop field in {location} involves {shape}",
                "The farming area at {location} has {dimensions}",
                "An agricultural project in {location} needs {action}"
            ]
        }
    
    def _initialize_cultural_references(self) -> Dict[str, List[str]]:
        """Initialize culturally appropriate South African references"""
        return {
            'languages': ['English', 'Afrikaans', 'isiZulu', 'isiXhosa', 'Sesotho', 'Setswana'],
            'cultural_events': ['Heritage Day', 'Freedom Day', 'Youth Day', 'Women\'s Day', 'Reconciliation Day'],
            'traditional_foods': ['braai', 'bobotie', 'bunny chow', 'boerewors', 'koeksisters', 'malva pudding'],
            'sports': ['rugby', 'cricket', 'soccer', 'netball', 'athletics', 'swimming'],
            'landmarks': ['Table Mountain', 'Kruger National Park', 'Robben Island', 'Union Buildings', 'Constitution Hill'],
            'schools': ['primary school', 'high school', 'secondary school', 'college', 'university'],
            'communities': ['township', 'suburb', 'rural area', 'urban area', 'informal settlement']
        }
    
    def _initialize_practical_scenarios(self) -> Dict[str, List[str]]:
        """Initialize practical real-world scenarios"""
        return {
            'garden_scenarios': [
                'planting vegetables', 'designing flower beds', 'installing irrigation',
                'building garden paths', 'creating compost areas', 'planning herb gardens'
            ],
            'construction_scenarios': [
                'building houses', 'renovating rooms', 'installing flooring',
                'constructing walls', 'planning layouts', 'calculating materials'
            ],
            'school_scenarios': [
                'science experiments', 'art projects', 'sports activities',
                'mathematics lessons', 'practical assessments', 'group projects'
            ],
            'sports_scenarios': [
                'field maintenance', 'equipment setup', 'event planning',
                'facility management', 'training sessions', 'competition preparation'
            ],
            'farming_scenarios': [
                'crop planning', 'field preparation', 'irrigation systems',
                'harvest planning', 'livestock management', 'equipment maintenance'
            ]
        }
    
    def _initialize_measurement_contexts(self) -> Dict[str, Dict[str, List[str]]]:
        """Initialize context-appropriate measurements"""
        return {
            'garden_landscaping': {
                'length_units': ['cm', 'm'],
                'area_units': ['cm²', 'm²'],
                'typical_measurements': ['small plots (1-10 m²)', 'medium gardens (10-100 m²)', 'large gardens (100+ m²)']
            },
            'construction_home': {
                'length_units': ['cm', 'm'],
                'area_units': ['cm²', 'm²'],
                'typical_measurements': ['room dimensions (3-6 m)', 'wall areas (10-50 m²)', 'floor areas (20-200 m²)']
            },
            'school_education': {
                'length_units': ['mm', 'cm', 'm'],
                'area_units': ['mm²', 'cm²', 'm²'],
                'typical_measurements': ['desk dimensions (50-80 cm)', 'classroom areas (30-60 m²)', 'playground areas (100-500 m²)']
            },
            'sports_recreation': {
                'length_units': ['m', 'km'],
                'area_units': ['m²', 'ha'],
                'typical_measurements': ['field lengths (50-100 m)', 'court areas (200-800 m²)', 'stadium areas (1-10 ha)']
            },
            'farming_agriculture': {
                'length_units': ['m', 'km'],
                'area_units': ['m²', 'ha'],
                'typical_measurements': ['field lengths (100-1000 m)', 'plot areas (1-100 ha)', 'farm areas (100+ ha)']
            }
        }
    
    def validate_question_context(self, question: QuizQuestion) -> ContextValidation:
        """Validate South African context for a single question"""
        errors = []
        warnings = []
        suggestions = []
        missing_context_elements = []
        inappropriate_elements = []
        
        # Check context authenticity
        context_authenticity = self._check_context_authenticity(question, errors, warnings)
        
        # Check cultural appropriateness
        cultural_appropriateness = self._check_cultural_appropriateness(question, warnings, inappropriate_elements)
        
        # Check practical relevance
        practical_relevance = self._check_practical_relevance(question, suggestions)
        
        # Check location accuracy
        location_accuracy = self._check_location_accuracy(question, errors, warnings, missing_context_elements)
        
        # Check measurement appropriateness
        self._check_measurement_appropriateness(question, warnings, suggestions)
        
        # Check context completeness
        self._check_context_completeness(question, missing_context_elements, suggestions)
        
        # Calculate overall validation
        is_valid = len(errors) == 0
        result = ContextValidationResult.VALID if is_valid else (
            ContextValidationResult.WARNING if len(warnings) > 0 else ContextValidationResult.INVALID
        )
        
        return ContextValidation(
            is_valid=is_valid,
            result=result,
            context_authenticity=context_authenticity,
            cultural_appropriateness=cultural_appropriateness,
            practical_relevance=practical_relevance,
            location_accuracy=location_accuracy,
            warnings=warnings,
            errors=errors,
            suggestions=suggestions,
            missing_context_elements=missing_context_elements,
            inappropriate_elements=inappropriate_elements
        )
    
    def _check_context_authenticity(self, question: QuizQuestion, errors: List[str], warnings: List[str]) -> float:
        """Check if question has authentic South African context"""
        if not question.south_african_context:
            errors.append("Question should have South African context enabled")
            return 0.0
        
        question_text = question.question.lower()
        authenticity_score = 0.0
        total_checks = 0
        
        # Check for SA location references
        has_sa_location = any(
            any(location.lower() in question_text for location in locations)
            for context_locations in self.sa_locations.values()
            for locations in context_locations.values()
        )
        
        if has_sa_location:
            authenticity_score += 1.0
        else:
            warnings.append("Question should reference specific South African locations")
        
        total_checks += 1
        
        # Check for SA cultural references
        cultural_refs = [ref.lower() for ref_list in self.cultural_references.values() for ref in ref_list]
        has_cultural_ref = any(ref in question_text for ref in cultural_refs)
        
        if has_cultural_ref:
            authenticity_score += 1.0
        else:
            warnings.append("Question could benefit from South African cultural references")
        
        total_checks += 1
        
        # Check for practical SA scenarios
        practical_scenarios = [scenario.lower() for scenario_list in self.practical_scenarios.values() for scenario in scenario_list]
        has_practical_scenario = any(scenario in question_text for scenario in practical_scenarios)
        
        if has_practical_scenario:
            authenticity_score += 1.0
        else:
            warnings.append("Question should include practical South African scenarios")
        
        total_checks += 1
        
        return (authenticity_score / total_checks) * 100 if total_checks > 0 else 0.0
    
    def _check_cultural_appropriateness(self, question: QuizQuestion, warnings: List[str], inappropriate_elements: List[str]) -> float:
        """Check if question is culturally appropriate for South African students"""
        question_text = question.question.lower()
        appropriateness_score = 0.0
        total_checks = 0
        
        # Check for inappropriate cultural references
        inappropriate_refs = ['American', 'British', 'European', 'dollars', 'pounds', 'feet', 'inches', 'yards', 'miles']
        found_inappropriate = [ref for ref in inappropriate_refs if ref in question_text]
        
        if found_inappropriate:
            inappropriate_elements.extend(found_inappropriate)
            warnings.append(f"Question contains non-South African references: {found_inappropriate}")
        else:
            appropriateness_score += 1.0
        
        total_checks += 1
        
        # Check for appropriate SA cultural references
        sa_cultural_refs = ['rand', 'rural', 'urban', 'township', 'suburb', 'community', 'heritage', 'diversity']
        has_sa_cultural_ref = any(ref in question_text for ref in sa_cultural_refs)
        
        if has_sa_cultural_ref:
            appropriateness_score += 1.0
        else:
            warnings.append("Question could include more South African cultural elements")
        
        total_checks += 1
        
        # Check for inclusive language
        inclusive_terms = ['learners', 'students', 'community', 'everyone', 'all']
        has_inclusive_language = any(term in question_text for term in inclusive_terms)
        
        if has_inclusive_language:
            appropriateness_score += 1.0
        else:
            warnings.append("Question should use inclusive language")
        
        total_checks += 1
        
        return (appropriateness_score / total_checks) * 100 if total_checks > 0 else 0.0
    
    def _check_practical_relevance(self, question: QuizQuestion, suggestions: List[str]) -> float:
        """Check if question has practical relevance for South African students"""
        question_text = question.question.lower()
        relevance_score = 0.0
        total_checks = 0
        
        # Check for real-world application
        real_world_keywords = ['calculate', 'measure', 'design', 'plan', 'build', 'create', 'solve', 'find']
        has_real_world_keywords = any(keyword in question_text for keyword in real_world_keywords)
        
        if has_real_world_keywords:
            relevance_score += 1.0
        else:
            suggestions.append("Question should include real-world application keywords")
        
        total_checks += 1
        
        # Check for practical context
        practical_contexts = ['garden', 'house', 'school', 'field', 'stadium', 'farm', 'community', 'project']
        has_practical_context = any(context in question_text for context in practical_contexts)
        
        if has_practical_context:
            relevance_score += 1.0
        else:
            suggestions.append("Question should include practical context")
        
        total_checks += 1
        
        # Check for problem-solving elements
        problem_solving_keywords = ['problem', 'challenge', 'task', 'project', 'assignment', 'activity']
        has_problem_solving = any(keyword in question_text for keyword in problem_solving_keywords)
        
        if has_problem_solving:
            relevance_score += 1.0
        else:
            suggestions.append("Question should include problem-solving elements")
        
        total_checks += 1
        
        return (relevance_score / total_checks) * 100 if total_checks > 0 else 0.0
    
    def _check_location_accuracy(self, question: QuizQuestion, errors: List[str], warnings: List[str], missing_context_elements: List[str]) -> float:
        """Check if South African locations are accurate and appropriate"""
        question_text = question.question.lower()
        accuracy_score = 0.0
        total_checks = 0
        
        # Check for SA location references
        found_locations = []
        for context_type, provinces in self.sa_locations.items():
            for province, locations in provinces.items():
                for location in locations:
                    if location.lower() in question_text:
                        found_locations.append((location, context_type, province))
        
        if found_locations:
            accuracy_score += 1.0
            # Check if location matches context
            context_type = self._determine_question_context_type(question)
            appropriate_locations = self.sa_locations.get(context_type, {})
            for location, found_context, province in found_locations:
                if found_context == context_type:
                    accuracy_score += 0.5
                else:
                    warnings.append(f"Location '{location}' may not be appropriate for {context_type} context")
        else:
            missing_context_elements.append("Specific South African location")
            errors.append("Question should reference specific South African locations")
        
        total_checks += 1
        
        # Check for province accuracy
        if found_locations:
            # This is a simplified check - in practice, you'd validate province accuracy
            accuracy_score += 1.0
        else:
            missing_context_elements.append("Province or region specification")
        
        total_checks += 1
        
        return (accuracy_score / total_checks) * 100 if total_checks > 0 else 0.0
    
    def _check_measurement_appropriateness(self, question: QuizQuestion, warnings: List[str], suggestions: List[str]):
        """Check if measurements are appropriate for South African context"""
        question_text = question.question.lower()
        context_type = self._determine_question_context_type(question)
        
        if context_type in self.measurement_contexts:
            appropriate_measurements = self.measurement_contexts[context_type]
            
            # Check length units
            length_units_used = [unit for unit in ['mm', 'cm', 'm', 'km'] if unit in question_text]
            appropriate_length_units = appropriate_measurements.get('length_units', ['cm', 'm'])
            
            for unit in length_units_used:
                if unit not in appropriate_length_units:
                    warnings.append(f"Unit '{unit}' may not be appropriate for {context_type} context")
            
            # Check area units
            area_units_used = [unit for unit in ['mm²', 'cm²', 'm²', 'ha'] if unit in question_text]
            appropriate_area_units = appropriate_measurements.get('area_units', ['cm²', 'm²'])
            
            for unit in area_units_used:
                if unit not in appropriate_area_units:
                    warnings.append(f"Unit '{unit}' may not be appropriate for {context_type} context")
    
    def _check_context_completeness(self, question: QuizQuestion, missing_context_elements: List[str], suggestions: List[str]):
        """Check if context is complete and comprehensive"""
        question_text = question.question.lower()
        
        # Check for essential context elements
        essential_elements = ['location', 'purpose', 'measurement', 'calculation']
        for element in essential_elements:
            if element not in question_text:
                missing_context_elements.append(f"Missing {element} specification")
        
        # Check for educational value
        if not any(keyword in question_text for keyword in ['learn', 'teach', 'understand', 'explain', 'show']):
            suggestions.append("Question could include educational value statements")
        
        # Check for engagement elements
        if not any(keyword in question_text for keyword in ['imagine', 'suppose', 'consider', 'think about']):
            suggestions.append("Question could include engagement elements")
    
    def _determine_question_context_type(self, question: QuizQuestion) -> str:
        """Determine the context type of the question"""
        question_text = question.question.lower()
        
        if any(word in question_text for word in ['garden', 'plot', 'flower', 'plant', 'vegetable']):
            return 'garden_landscaping'
        elif any(word in question_text for word in ['house', 'room', 'building', 'construction', 'renovation']):
            return 'construction_home'
        elif any(word in question_text for word in ['school', 'classroom', 'desk', 'book', 'student', 'learner']):
            return 'school_education'
        elif any(word in question_text for word in ['field', 'sport', 'stadium', 'track', 'court', 'pitch']):
            return 'sports_recreation'
        elif any(word in question_text for word in ['farm', 'crop', 'agriculture', 'field', 'livestock']):
            return 'farming_agriculture'
        else:
            return 'general'
    
    def validate_context_coverage(self, questions: List[QuizQuestion]) -> Dict[str, Any]:
        """Validate comprehensive South African context coverage across all questions"""
        validation_results = [self.validate_question_context(q) for q in questions]
        
        # Calculate overall metrics
        total_questions = len(questions)
        valid_questions = sum(1 for r in validation_results if r.is_valid)
        warning_questions = sum(1 for r in validation_results if r.result == ContextValidationResult.WARNING)
        invalid_questions = sum(1 for r in validation_results if r.result == ContextValidationResult.INVALID)
        
        # Calculate average scores
        avg_context_authenticity = sum(r.context_authenticity for r in validation_results) / total_questions if total_questions > 0 else 0
        avg_cultural_appropriateness = sum(r.cultural_appropriateness for r in validation_results) / total_questions if total_questions > 0 else 0
        avg_practical_relevance = sum(r.practical_relevance for r in validation_results) / total_questions if total_questions > 0 else 0
        avg_location_accuracy = sum(r.location_accuracy for r in validation_results) / total_questions if total_questions > 0 else 0
        
        # Count context types
        context_types = {}
        for question in questions:
            context_type = self._determine_question_context_type(question)
            context_types[context_type] = context_types.get(context_type, 0) + 1
        
        # Collect all warnings, errors, and suggestions
        all_warnings = [w for r in validation_results for w in r.warnings]
        all_errors = [e for r in validation_results for e in r.errors]
        all_suggestions = [s for r in validation_results for s in r.suggestions]
        
        return {
            'total_questions': total_questions,
            'valid_questions': valid_questions,
            'warning_questions': warning_questions,
            'invalid_questions': invalid_questions,
            'context_authenticity_percentage': round(avg_context_authenticity, 2),
            'cultural_appropriateness_percentage': round(avg_cultural_appropriateness, 2),
            'practical_relevance_percentage': round(avg_practical_relevance, 2),
            'location_accuracy_percentage': round(avg_location_accuracy, 2),
            'context_type_distribution': context_types,
            'total_warnings': len(all_warnings),
            'total_errors': len(all_errors),
            'total_suggestions': len(all_suggestions),
            'detailed_results': [
                {
                    'question_id': getattr(result, 'question_id', f'question_{i}'),
                    'is_valid': result.is_valid,
                    'result': result.result.value,
                    'context_authenticity': result.context_authenticity,
                    'cultural_appropriateness': result.cultural_appropriateness,
                    'practical_relevance': result.practical_relevance,
                    'location_accuracy': result.location_accuracy,
                    'warnings': result.warnings,
                    'errors': result.errors,
                    'suggestions': result.suggestions,
                    'missing_context_elements': result.missing_context_elements,
                    'inappropriate_elements': result.inappropriate_elements
                }
                for i, result in enumerate(validation_results)
            ]
        }
