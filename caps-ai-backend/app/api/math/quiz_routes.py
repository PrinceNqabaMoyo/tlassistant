"""
Enhanced Quiz Generation API Routes
New endpoints for the comprehensive geometry quiz system
"""

from flask import request, jsonify
from . import math_bp
from ...utils.cache import cache
import logging
import json
from enum import Enum

# Initialize the quiz generation service conditionally
try:
    from ...utils.quiz_generators import QuizGenerationService
    from ...utils.quiz_models import (
        QuizGenerationRequest, QuizQuestion, DifficultyLevel, QuestionType, ShapeType,
        CURRICULUM_TOPICS, SOUTH_AFRICAN_CONTEXTS
    )
    from ...utils.curriculum_validator import CurriculumValidator
    from ...utils.metric_system_validator import MetricSystemValidator
    from ...utils.south_african_context_validator import SouthAfricanContextValidator
    from ...utils.educational_features import EducationalFeaturesSystem
    quiz_service = QuizGenerationService()
    curriculum_validator = CurriculumValidator()
    metric_validator = MetricSystemValidator()
    context_validator = SouthAfricanContextValidator()
    educational_features = EducationalFeaturesSystem()
    QUIZ_SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"Quiz system not available: {e}")
    quiz_service = None
    curriculum_validator = None
    metric_validator = None
    context_validator = None
    educational_features = None
    QUIZ_SYSTEM_AVAILABLE = False

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def serialize_enum_value(obj):
    """Convert enum objects to their string values for JSON serialization"""
    if isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, dict):
        return {k: serialize_enum_value(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize_enum_value(item) for item in obj]
    else:
        return obj


@math_bp.route('/geometry/generate-quiz-question', methods=['POST'])
# @cache.memoize(timeout=300)  # Cache disabled for testing infinite variations
def generate_quiz_question():
    """Enhanced quiz question generation endpoint"""
    if not QUIZ_SYSTEM_AVAILABLE:
        return jsonify({
            'success': False,
            'error': 'Quiz system not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        # Extract parameters with defaults
        topic = data.get('topic', 'Calculations involving 2D Shapes')
        difficulty_str = data.get('difficulty', 'easy').lower()
        question_type_str = data.get('question_type', 'area_calculation')
        shape_type_str = data.get('shape_type')
        count = data.get('count', 1)
        include_diagram = data.get('include_diagram', True)
        south_african_context = data.get('south_african_context', True)
        conversion_required = data.get('conversion_required', False)
        reasoning_required = data.get('reasoning_required', False)
        
        # Validate and convert enums
        try:
            difficulty = DifficultyLevel(difficulty_str)
        except ValueError:
            return jsonify({
                'success': False,
                'error': f'Invalid difficulty level: {difficulty_str}. Must be one of: easy, medium, hard'
            }), 400
        
        try:
            question_type = QuestionType(question_type_str)
        except ValueError:
            return jsonify({
                'success': False,
                'error': f'Invalid question type: {question_type_str}'
            }), 400
        
        shape_type = None
        if shape_type_str:
            try:
                shape_type = ShapeType(shape_type_str)
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': f'Invalid shape type: {shape_type_str}'
                }), 400
        
        # Validate count
        if not isinstance(count, int) or count < 1 or count > 10:
            return jsonify({
                'success': False,
                'error': 'Count must be an integer between 1 and 10'
            }), 400
        
        # Create generation request
        generation_request = QuizGenerationRequest(
            topic=topic,
            difficulty=difficulty,
            question_type=question_type,
            shape_type=shape_type,
            count=count,
            include_diagram=include_diagram,
            south_african_context=south_african_context,
            conversion_required=conversion_required,
            reasoning_required=reasoning_required
        )
        
        # Generate questions
        # Convert request to dict with string values for logging
        request_dict = {
            'topic': generation_request.topic,
            'difficulty': generation_request.difficulty.value,
            'question_type': generation_request.question_type.value,
            'shape_type': generation_request.shape_type.value if generation_request.shape_type else None,
            'count': generation_request.count,
            'include_diagram': generation_request.include_diagram,
            'south_african_context': generation_request.south_african_context,
            'conversion_required': generation_request.conversion_required,
            'reasoning_required': generation_request.reasoning_required
        }
        logger.info(f"Generating questions with request: {request_dict}")
        response = quiz_service.generate_questions(generation_request)
        logger.info(f"Generation response: success={response.success}, method={response.generation_method}, questions_count={len(response.questions) if response.questions else 0}")
        
        if response.success:
            # Convert questions to JSON-serializable format
            questions_data = []
            for question in response.questions:
                try:
                    question_data = {
                        'question_id': question.question_id,
                        'question': question.question,
                        'options': question.options,
                        'correct_answer': question.correct_answer,
                        'explanation': question.explanation,
                        'topic': question.topic,
                        'difficulty': question.difficulty.value if hasattr(question.difficulty, 'value') else str(question.difficulty),
                        'question_type': question.question_type.value if hasattr(question.question_type, 'value') else str(question.question_type),
                        'shape_type': question.shape_type.value if question.shape_type and hasattr(question.shape_type, 'value') else str(question.shape_type) if question.shape_type else None,
                        'parameters': serialize_enum_value(question.parameters),
                        'geometric_constraints': serialize_enum_value(question.geometric_constraints),
                        'curriculum_alignments': serialize_enum_value(question.curriculum_alignments),
                        'metric_units': serialize_enum_value(question.metric_units),
                        'south_african_context': question.south_african_context,
                        'conversion_required': question.conversion_required,
                        'reasoning_required': question.reasoning_required,
                        'template_id': question.template_id
                    }
                    questions_data.append(question_data)
                except Exception as e:
                    logger.error(f"Error serializing question: {e}")
                    # Create a simple fallback question
                    questions_data.append({
                        'question_id': 'fallback_001',
                        'question': 'What is the area of a triangle with base 3 cm and height 4 cm?',
                        'options': ['6.0 cm²', '7.0 cm²', '5.0 cm²', '8.0 cm²'],
                        'correct_answer': '6.0 cm²',
                        'explanation': 'Area = ½ × base × height = ½ × 3 × 4 = 6.0 cm²',
                        'topic': 'Calculations involving 2D Shapes',
                        'difficulty': 'easy',
                        'question_type': 'area_calculation',
                        'shape_type': 'triangle_equilateral',
                        'parameters': {'base': 3, 'height': 4},
                        'geometric_constraints': [],
                        'curriculum_alignments': ['Calculations involving 2D Shapes'],
                        'metric_units': {'length': 'cm', 'area': 'cm²'},
                        'south_african_context': True,
                        'conversion_required': False,
                        'reasoning_required': False,
                        'template_id': None
                    })
            
            return jsonify({
                'success': True,
                'questions': questions_data,
                'generation_method': response.generation_method,
                'metadata': response.metadata,
                'count': len(questions_data)
            })
        else:
            return jsonify({
                'success': False,
                'error': response.error_message or 'Failed to generate questions',
                'generation_method': response.generation_method
            }), 500
            
    except Exception as e:
        logger.error(f"Error in generate_quiz_question: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/quiz-templates/<topic>/<difficulty>', methods=['GET'])
def get_quiz_templates(topic, difficulty):
    """Get available question templates for a topic and difficulty"""
    if not QUIZ_SYSTEM_AVAILABLE:
        return jsonify({
            'success': False,
            'error': 'Quiz system not available. Please check server logs.'
        }), 503
    
    try:
        # Validate difficulty
        try:
            difficulty_enum = DifficultyLevel(difficulty.lower())
        except ValueError:
            return jsonify({
                'success': False,
                'error': f'Invalid difficulty level: {difficulty}'
            }), 400
        
        # Get templates from both generators
        constraint_templates = quiz_service.constraint_generator.get_available_templates(topic, difficulty_enum)
        template_templates = quiz_service.template_generator.get_available_templates(topic, difficulty_enum)
        
        # Combine templates
        all_templates = constraint_templates + template_templates
        
        # Convert to JSON-serializable format
        templates_data = []
        for template in all_templates:
            template_data = {
                'template_id': template.template_id,
                'question_template': template.question_template,
                'parameter_ranges': template.parameter_ranges,
                'constraints': template.constraints,
                'difficulty': template.difficulty.value,
                'topic': template.topic,
                'question_type': template.question_type.value,
                'shape_type': template.shape_type.value,
                'metric_units': template.metric_units,
                'conversion_types': template.conversion_types,
                'real_world_context': template.real_world_context,
                'south_african_context': template.south_african_context,
                'reasoning_required': template.reasoning_required
            }
            templates_data.append(template_data)
        
        return jsonify({
            'success': True,
            'templates': templates_data,
            'count': len(templates_data),
            'topic': topic,
            'difficulty': difficulty
        })
        
    except Exception as e:
        logger.error(f"Error in get_quiz_templates: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/validate-parameters', methods=['POST'])
def validate_parameters():
    """Validate geometric parameters for a shape"""
    if not QUIZ_SYSTEM_AVAILABLE:
        return jsonify({
            'success': False,
            'error': 'Quiz system not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        shape_type_str = data.get('shape_type')
        parameters = data.get('parameters', {})
        
        if not shape_type_str:
            return jsonify({
                'success': False,
                'error': 'Missing required parameter: shape_type'
            }), 400
        
        try:
            shape_type = ShapeType(shape_type_str)
        except ValueError:
            return jsonify({
                'success': False,
                'error': f'Invalid shape type: {shape_type_str}'
            }), 400
        
        # Validate parameters
        validator = quiz_service.constraint_generator.validator
        result = validator.validate_parameters(shape_type, parameters)
        
        return jsonify({
            'success': True,
            'is_valid': result.is_valid,
            'error_message': result.error_message,
            'corrected_parameters': result.corrected_parameters,
            'warnings': result.warnings or []
        })
        
    except Exception as e:
        logger.error(f"Error in validate_parameters: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/curriculum-topics', methods=['GET'])
def get_curriculum_topics():
    """Get curriculum-aligned topics for Grade 7 Geometry"""
    if not QUIZ_SYSTEM_AVAILABLE:
        return jsonify({
            'success': False,
            'error': 'Quiz system not available. Please check server logs.'
        }), 503
    
    try:
        return jsonify({
            'success': True,
            'topics': CURRICULUM_TOPICS,
            'south_african_contexts': SOUTH_AFRICAN_CONTEXTS,
            'question_types': [qt.value for qt in QuestionType],
            'difficulty_levels': [dl.value for dl in DifficultyLevel],
            'shape_types': [st.value for st in ShapeType]
        })
        
    except Exception as e:
        logger.error(f"Error in get_curriculum_topics: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/quiz-stats', methods=['GET'])
def get_quiz_stats():
    """Get statistics about the quiz generation system"""
    if not QUIZ_SYSTEM_AVAILABLE:
        return jsonify({
            'success': False,
            'error': 'Quiz system not available. Please check server logs.'
        }), 503
    
    try:
        constraint_stats = {
            'generated_questions': quiz_service.constraint_generator.generated_questions,
            'generator_type': 'constraint_based'
        }
        
        template_stats = {
            'available_templates': len(quiz_service.template_generator.templates),
            'generator_type': 'template_based'
        }
        
        return jsonify({
            'success': True,
            'constraint_generator': constraint_stats,
            'template_generator': template_stats,
            'total_curriculum_topics': len(CURRICULUM_TOPICS),
            'total_question_types': len(QuestionType),
            'total_shape_types': len(ShapeType)
        })
        
    except Exception as e:
        logger.error(f"Error in get_quiz_stats: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/validate-curriculum', methods=['POST'])
def validate_curriculum():
    """Validate quiz questions against Grade 7 CAPS curriculum requirements"""
    if not QUIZ_SYSTEM_AVAILABLE or not curriculum_validator:
        return jsonify({
            'success': False,
            'error': 'Curriculum validation not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        if not data or 'questions' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: questions'
            }), 400
        
        questions_data = data['questions']
        
        # Convert question data to QuizQuestion objects
        questions = []
        for q_data in questions_data:
            try:
                # Convert string enums to proper enum objects
                difficulty_str = q_data.get('difficulty', 'easy')
                question_type_str = q_data.get('question_type', 'area_calculation')
                shape_type_str = q_data.get('shape_type', 'triangle_equilateral')
                
                difficulty = DifficultyLevel(difficulty_str)
                question_type = QuestionType(question_type_str)
                shape_type = ShapeType(shape_type_str) if shape_type_str else None
                
                logger.info(f"Converting question: difficulty={difficulty_str}, question_type={question_type_str}, shape_type={shape_type_str}")
                
                question = QuizQuestion(
                    question=q_data.get('question', ''),
                    options=q_data.get('options', []),
                    correct_answer=q_data.get('correct_answer', ''),
                    explanation=q_data.get('explanation', ''),
                    topic=q_data.get('topic', ''),
                    difficulty=difficulty,
                    question_type=question_type,
                    shape_type=shape_type,
                    parameters=q_data.get('parameters', {}),
                    geometric_constraints=q_data.get('geometric_constraints', []),
                    curriculum_alignments=q_data.get('curriculum_alignments', []),
                    metric_units=q_data.get('metric_units', {}),
                    south_african_context=q_data.get('south_african_context', False),
                    conversion_required=q_data.get('conversion_required', False),
                    reasoning_required=q_data.get('reasoning_required', False),
                    question_id=q_data.get('question_id', 'unknown')
                )
                questions.append(question)
            except Exception as e:
                logger.warning(f"Failed to convert question data: {e}")
                logger.warning(f"Question data: {q_data}")
                continue
        
        if not questions:
            return jsonify({
                'success': False,
                'error': 'No valid questions found in request'
            }), 400
        
        # Validate questions
        validation_result = curriculum_validator.validate_question_batch(questions)
        
        return jsonify({
            'success': True,
            'validation_result': {
                'total_questions': validation_result['total_questions'],
                'valid_questions': validation_result['valid_questions'],
                'warning_questions': validation_result['warning_questions'],
                'invalid_questions': validation_result['invalid_questions'],
                'curriculum_coverage_percentage': round(validation_result['curriculum_coverage'], 2),
                'covered_curriculum_areas': [area.value for area in validation_result['covered_areas']],
                'missing_curriculum_areas': [area.value for area in validation_result['missing_areas']],
                'detailed_results': [
                    {
                        'question_id': getattr(result, 'question_id', f'question_{i}'),
                        'is_valid': result.is_valid,
                        'result': result.result.value,
                        'curriculum_areas': [area.value for area in result.curriculum_areas],
                        'warnings': result.warnings,
                        'errors': result.errors,
                        'suggestions': result.suggestions
                    }
                    for i, result in enumerate(validation_result['validation_results'])
                ]
            }
        })
        
    except Exception as e:
        logger.error(f"Error in validate_curriculum: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/validate-metric-system', methods=['POST'])
def validate_metric_system():
    """Validate comprehensive metric system coverage and compliance"""
    if not QUIZ_SYSTEM_AVAILABLE or not metric_validator:
        return jsonify({
            'success': False,
            'error': 'Metric system validation not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        if not data or 'questions' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: questions'
            }), 400
        
        questions_data = data['questions']
        
        # Convert question data to QuizQuestion objects
        questions = []
        for q_data in questions_data:
            try:
                # Convert string enums to proper enum objects
                difficulty_str = q_data.get('difficulty', 'easy')
                question_type_str = q_data.get('question_type', 'area_calculation')
                shape_type_str = q_data.get('shape_type', 'triangle_equilateral')
                
                difficulty = DifficultyLevel(difficulty_str)
                question_type = QuestionType(question_type_str)
                shape_type = ShapeType(shape_type_str) if shape_type_str else None
                
                question = QuizQuestion(
                    question=q_data.get('question', ''),
                    options=q_data.get('options', []),
                    correct_answer=q_data.get('correct_answer', ''),
                    explanation=q_data.get('explanation', ''),
                    topic=q_data.get('topic', ''),
                    difficulty=difficulty,
                    question_type=question_type,
                    shape_type=shape_type,
                    parameters=q_data.get('parameters', {}),
                    geometric_constraints=q_data.get('geometric_constraints', []),
                    curriculum_alignments=q_data.get('curriculum_alignments', []),
                    metric_units=q_data.get('metric_units', {}),
                    south_african_context=q_data.get('south_african_context', False),
                    conversion_required=q_data.get('conversion_required', False),
                    reasoning_required=q_data.get('reasoning_required', False),
                    question_id=q_data.get('question_id', 'unknown')
                )
                questions.append(question)
            except Exception as e:
                logger.warning(f"Failed to convert question data: {e}")
                continue
        
        if not questions:
            return jsonify({
                'success': False,
                'error': 'No valid questions found in request'
            }), 400
        
        # Validate metric system coverage
        validation_result = metric_validator.validate_metric_system_coverage(questions)
        
        return jsonify({
            'success': True,
            'metric_validation_result': {
                'total_questions': validation_result['total_questions'],
                'valid_questions': validation_result['valid_questions'],
                'warning_questions': validation_result['warning_questions'],
                'invalid_questions': validation_result['invalid_questions'],
                'metric_compliance_percentage': validation_result['metric_compliance_percentage'],
                'unit_appropriateness_percentage': validation_result['unit_appropriateness_percentage'],
                'conversion_coverage_percentage': validation_result['conversion_coverage_percentage'],
                'conversion_questions_count': validation_result['conversion_questions_count'],
                'conversion_questions_percentage': validation_result['conversion_questions_percentage'],
                'total_warnings': validation_result['total_warnings'],
                'total_errors': validation_result['total_errors'],
                'total_suggestions': validation_result['total_suggestions'],
                'detailed_results': validation_result['detailed_results']
            }
        })
        
    except Exception as e:
        logger.error(f"Error in validate_metric_system: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/validate-south-african-context', methods=['POST'])
def validate_south_african_context():
    """Validate South African real-world contexts and practical problems"""
    if not QUIZ_SYSTEM_AVAILABLE or not context_validator:
        return jsonify({
            'success': False,
            'error': 'South African context validation not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        if not data or 'questions' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: questions'
            }), 400
        
        questions_data = data['questions']
        
        # Convert question data to QuizQuestion objects
        questions = []
        for q_data in questions_data:
            try:
                # Convert string enums to proper enum objects
                difficulty_str = q_data.get('difficulty', 'easy')
                question_type_str = q_data.get('question_type', 'area_calculation')
                shape_type_str = q_data.get('shape_type', 'triangle_equilateral')
                
                difficulty = DifficultyLevel(difficulty_str)
                question_type = QuestionType(question_type_str)
                shape_type = ShapeType(shape_type_str) if shape_type_str else None
                
                question = QuizQuestion(
                    question=q_data.get('question', ''),
                    options=q_data.get('options', []),
                    correct_answer=q_data.get('correct_answer', ''),
                    explanation=q_data.get('explanation', ''),
                    topic=q_data.get('topic', ''),
                    difficulty=difficulty,
                    question_type=question_type,
                    shape_type=shape_type,
                    parameters=q_data.get('parameters', {}),
                    geometric_constraints=q_data.get('geometric_constraints', []),
                    curriculum_alignments=q_data.get('curriculum_alignments', []),
                    metric_units=q_data.get('metric_units', {}),
                    south_african_context=q_data.get('south_african_context', False),
                    conversion_required=q_data.get('conversion_required', False),
                    reasoning_required=q_data.get('reasoning_required', False),
                    question_id=q_data.get('question_id', 'unknown')
                )
                questions.append(question)
            except Exception as e:
                logger.warning(f"Failed to convert question data: {e}")
                continue
        
        if not questions:
            return jsonify({
                'success': False,
                'error': 'No valid questions found in request'
            }), 400
        
        # Validate South African context coverage
        validation_result = context_validator.validate_context_coverage(questions)
        
        return jsonify({
            'success': True,
            'context_validation_result': {
                'total_questions': validation_result['total_questions'],
                'valid_questions': validation_result['valid_questions'],
                'warning_questions': validation_result['warning_questions'],
                'invalid_questions': validation_result['invalid_questions'],
                'context_authenticity_percentage': validation_result['context_authenticity_percentage'],
                'cultural_appropriateness_percentage': validation_result['cultural_appropriateness_percentage'],
                'practical_relevance_percentage': validation_result['practical_relevance_percentage'],
                'location_accuracy_percentage': validation_result['location_accuracy_percentage'],
                'context_type_distribution': validation_result['context_type_distribution'],
                'total_warnings': validation_result['total_warnings'],
                'total_errors': validation_result['total_errors'],
                'total_suggestions': validation_result['total_suggestions'],
                'detailed_results': validation_result['detailed_results']
            }
        })
        
    except Exception as e:
        logger.error(f"Error in validate_south_african_context: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/generate-hints', methods=['POST'])
def generate_hints():
    """Generate educational hints for a question"""
    if not QUIZ_SYSTEM_AVAILABLE or not educational_features:
        return jsonify({
            'success': False,
            'error': 'Educational features not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: question'
            }), 400
        
        # Convert question data to QuizQuestion object
        q_data = data['question']
        student_performance = data.get('student_performance')
        
        try:
            difficulty = DifficultyLevel(q_data.get('difficulty', 'easy'))
            question_type = QuestionType(q_data.get('question_type', 'area_calculation'))
            shape_type = ShapeType(q_data.get('shape_type', 'triangle_equilateral')) if q_data.get('shape_type') else None
            
            question = QuizQuestion(
                question=q_data.get('question', ''),
                options=q_data.get('options', []),
                correct_answer=q_data.get('correct_answer', ''),
                explanation=q_data.get('explanation', ''),
                topic=q_data.get('topic', ''),
                difficulty=difficulty,
                question_type=question_type,
                shape_type=shape_type,
                parameters=q_data.get('parameters', {}),
                geometric_constraints=q_data.get('geometric_constraints', []),
                curriculum_alignments=q_data.get('curriculum_alignments', []),
                metric_units=q_data.get('metric_units', {}),
                south_african_context=q_data.get('south_african_context', False),
                conversion_required=q_data.get('conversion_required', False),
                reasoning_required=q_data.get('reasoning_required', False),
                question_id=q_data.get('question_id', 'unknown')
            )
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Invalid question data: {str(e)}'
            }), 400
        
        # Generate hints
        hints = educational_features.generate_hints(question, student_performance)
        
        return jsonify({
            'success': True,
            'hints': [
                {
                    'hint_id': hint.hint_id,
                    'hint_type': hint.hint_type.value,
                    'hint_text': hint.hint_text,
                    'difficulty_level': hint.difficulty_level.value,
                    'learning_stage': hint.learning_stage.value,
                    'prerequisite_concepts': hint.prerequisite_concepts
                }
                for hint in hints
            ]
        })
        
    except Exception as e:
        logger.error(f"Error in generate_hints: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/generate-solution', methods=['POST'])
def generate_solution():
    """Generate step-by-step solution for a question"""
    if not QUIZ_SYSTEM_AVAILABLE or not educational_features:
        return jsonify({
            'success': False,
            'error': 'Educational features not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required field: question'
            }), 400
        
        # Convert question data to QuizQuestion object
        q_data = data['question']
        
        try:
            difficulty = DifficultyLevel(q_data.get('difficulty', 'easy'))
            question_type = QuestionType(q_data.get('question_type', 'area_calculation'))
            shape_type = ShapeType(q_data.get('shape_type', 'triangle_equilateral')) if q_data.get('shape_type') else None
            
            question = QuizQuestion(
                question=q_data.get('question', ''),
                options=q_data.get('options', []),
                correct_answer=q_data.get('correct_answer', ''),
                explanation=q_data.get('explanation', ''),
                topic=q_data.get('topic', ''),
                difficulty=difficulty,
                question_type=question_type,
                shape_type=shape_type,
                parameters=q_data.get('parameters', {}),
                geometric_constraints=q_data.get('geometric_constraints', []),
                curriculum_alignments=q_data.get('curriculum_alignments', []),
                metric_units=q_data.get('metric_units', {}),
                south_african_context=q_data.get('south_african_context', False),
                conversion_required=q_data.get('conversion_required', False),
                reasoning_required=q_data.get('reasoning_required', False),
                question_id=q_data.get('question_id', 'unknown')
            )
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Invalid question data: {str(e)}'
            }), 400
        
        # Generate step-by-step solution
        solution_steps = educational_features.generate_step_by_step_solution(question)
        
        return jsonify({
            'success': True,
            'solution_steps': [
                {
                    'step_id': step.step_id,
                    'step_number': step.step_number,
                    'step_description': step.step_description,
                    'step_action': step.step_action,
                    'step_result': step.step_result,
                    'step_explanation': step.step_explanation,
                    'visual_aid': step.visual_aid,
                    'common_mistakes': step.common_mistakes or []
                }
                for step in solution_steps
            ]
        })
        
    except Exception as e:
        logger.error(f"Error in generate_solution: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500


@math_bp.route('/geometry/generate-feedback', methods=['POST'])
def generate_feedback():
    """Generate educational feedback for student response"""
    if not QUIZ_SYSTEM_AVAILABLE or not educational_features:
        return jsonify({
            'success': False,
            'error': 'Educational features not available. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        
        if not data or 'question' not in data or 'student_answer' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: question, student_answer'
            }), 400
        
        # Convert question data to QuizQuestion object
        q_data = data['question']
        student_answer = data['student_answer']
        student_performance = data.get('student_performance')
        
        try:
            difficulty = DifficultyLevel(q_data.get('difficulty', 'easy'))
            question_type = QuestionType(q_data.get('question_type', 'area_calculation'))
            shape_type = ShapeType(q_data.get('shape_type', 'triangle_equilateral')) if q_data.get('shape_type') else None
            
            question = QuizQuestion(
                question=q_data.get('question', ''),
                options=q_data.get('options', []),
                correct_answer=q_data.get('correct_answer', ''),
                explanation=q_data.get('explanation', ''),
                topic=q_data.get('topic', ''),
                difficulty=difficulty,
                question_type=question_type,
                shape_type=shape_type,
                parameters=q_data.get('parameters', {}),
                geometric_constraints=q_data.get('geometric_constraints', []),
                curriculum_alignments=q_data.get('curriculum_alignments', []),
                metric_units=q_data.get('metric_units', {}),
                south_african_context=q_data.get('south_african_context', False),
                conversion_required=q_data.get('conversion_required', False),
                reasoning_required=q_data.get('reasoning_required', False),
                question_id=q_data.get('question_id', 'unknown')
            )
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Invalid question data: {str(e)}'
            }), 400
        
        # Check if answer is correct
        is_correct = student_answer.strip().lower() == question.correct_answer.strip().lower()
        
        # Generate feedback
        feedback = educational_features.generate_feedback(question, student_answer, is_correct, student_performance)
        
        return jsonify({
            'success': True,
            'feedback': {
                'is_correct': feedback.is_correct,
                'feedback_type': feedback.feedback_type,
                'message': feedback.message,
                'explanation': feedback.explanation,
                'encouragement': feedback.encouragement,
                'next_steps': feedback.next_steps,
                'related_concepts': feedback.related_concepts,
                'difficulty_adjustment': feedback.difficulty_adjustment
            }
        })
        
    except Exception as e:
        logger.error(f"Error in generate_feedback: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500
