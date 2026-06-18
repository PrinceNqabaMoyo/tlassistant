"""
Quiz Generation System
Base classes and core functionality for generating geometry quiz questions
"""

import random
import uuid
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

from .quiz_models import (
    QuizQuestion, QuestionTemplate, QuizGenerationRequest, QuizGenerationResponse,
    DifficultyLevel, QuestionType, ShapeType, MetricUnit, CURRICULUM_TOPICS
)
from .geometric_validators import GeometricConstraintValidator, ValidationResult
from .parameter_generators import (
    TriangleParameterGenerator, QuadrilateralParameterGenerator, CircleParameterGenerator,
    AngleParameterGenerator, MetricUnitGenerator, SouthAfricanContextGenerator
)
from .templates.base.template_registry import TemplateRegistry
from .advanced_question_types import AdvancedQuestionGenerator, AdvancedQuestionType


class QuizGenerator(ABC):
    """Abstract base class for quiz question generators"""
    
    def __init__(self):
        self.validator = GeometricConstraintValidator()
        self.generated_questions = 0
    
    @abstractmethod
    def generate_question(self, request: QuizGenerationRequest) -> QuizQuestion:
        """Generate a single quiz question"""
        pass
    
    @abstractmethod
    def get_available_templates(self, topic: str, difficulty: DifficultyLevel) -> List[QuestionTemplate]:
        """Get available question templates for a topic and difficulty"""
        pass
    
    def validate_question(self, question: QuizQuestion) -> ValidationResult:
        """Validate a generated question"""
        if question.shape_type:
            return self.validator.validate_parameters(question.shape_type, question.parameters)
        return ValidationResult(is_valid=True)
    
    def generate_question_id(self) -> str:
        """Generate unique question ID"""
        self.generated_questions += 1
        return f"q_{self.generated_questions}_{uuid.uuid4().hex[:8]}"


class ConstraintBasedGenerator(QuizGenerator):
    """
    Primary generator using geometric constraints and parameter space exploration
    Implements infinite variety through parameter space exploration as per plan Section 4.1
    """
    
    def __init__(self):
        super().__init__()
        # Initialize the 10 specific parameter generators as per plan Section 2.2
        self.triangle_generator = TriangleParameterGenerator()
        self.quadrilateral_generator = QuadrilateralParameterGenerator()
        self.circle_generator = CircleParameterGenerator()
        self.angle_generator = AngleParameterGenerator()
        self.metric_generator = MetricUnitGenerator()
        self.context_generator = SouthAfricanContextGenerator()
        # Initialize advanced question generator
        self.advanced_generator = AdvancedQuestionGenerator()
    
    def generate_question(self, request: QuizGenerationRequest) -> QuizQuestion:
        """
        Generate question using constraint-based approach with infinite variety
        Implements parameter space exploration as per plan Section 4.1
        """
        try:
            # Handle special question types first (before advanced question check)
            if request.question_type == QuestionType.UNIT_CONVERSION:
                parameters = self.metric_generator.generate_conversion_parameters(request.difficulty)
                return self._generate_conversion_question(request, parameters)
            elif request.question_type == QuestionType.EQUATION_SOLVING:
                parameters = self._generate_equation_parameters(request.difficulty, request.shape_type)
                return self._generate_equation_question(request, parameters)
            elif request.question_type == QuestionType.TRIANGLE_HEIGHT:
                parameters = self._generate_triangle_height_parameters(request.difficulty)
                return self._generate_triangle_height_question(request, parameters)
            elif request.question_type == QuestionType.VOLUME_CALCULATION:
                parameters = self._generate_3d_parameters(request)
                return self._generate_volume_question(request, parameters)
            elif request.question_type == QuestionType.SURFACE_AREA_CALCULATION:
                parameters = self._generate_3d_parameters(request)
                return self._generate_surface_area_question(request, parameters)
            elif request.question_type == QuestionType.CAPACITY_CALCULATION:
                parameters = self._generate_3d_parameters(request)
                return self._generate_capacity_question(request, parameters)
            elif request.question_type == QuestionType.THREE_D_SHAPE_RECOGNITION:
                parameters = self._generate_3d_parameters(request)
                return self._generate_3d_shape_recognition_question(request, parameters)
            
            # Check if this should be an advanced question type (50% chance for medium/hard)
            if request.difficulty in [DifficultyLevel.MEDIUM, DifficultyLevel.HARD] and random.random() < 0.5:
                return self._generate_advanced_question(request)
            
            # Use the appropriate parameter generator based on shape type
            if request.shape_type and request.shape_type.value.startswith('triangle'):
                parameters = self.triangle_generator.generate_parameters(request.difficulty, request.question_type)
                return self._generate_triangle_question(request, parameters)
            elif request.shape_type and request.shape_type.value in ['square', 'rectangle', 'rhombus', 'parallelogram', 'kite', 'trapezium']:
                parameters = self.quadrilateral_generator.generate_parameters(request.difficulty, request.question_type)
                return self._generate_quadrilateral_question(request, parameters)
            elif request.shape_type and request.shape_type.value.startswith('circle'):
                parameters = self.circle_generator.generate_parameters(request.difficulty, request.question_type)
                return self._generate_circle_question(request, parameters)
            else:
                # Default to triangle for unknown shapes
                parameters = self.triangle_generator.generate_parameters(request.difficulty, request.question_type)
                return self._generate_triangle_question(request, parameters)
                
        except Exception as e:
            raise ValueError(f"Error generating constraint-based question: {str(e)}")
    
    def _generate_advanced_question(self, request: QuizGenerationRequest) -> QuizQuestion:
        """Generate an advanced question type"""
        # Select appropriate advanced question type based on difficulty and shape
        if request.difficulty == DifficultyLevel.MEDIUM:
            advanced_types = [
                AdvancedQuestionType.COMPOSITE_AREA,
                AdvancedQuestionType.QUADRILATERAL_CLASSIFICATION,
                AdvancedQuestionType.TRIANGLE_CLASSIFICATION,
                AdvancedQuestionType.SIMILARITY_COMPARISON,
            ]
        else:  # HARD
            advanced_types = [
                AdvancedQuestionType.COMPOSITE_AREA,
                AdvancedQuestionType.SHADED_REGION,
                AdvancedQuestionType.QUADRILATERAL_CLASSIFICATION,
                AdvancedQuestionType.TRIANGLE_CLASSIFICATION,
                AdvancedQuestionType.SIMILARITY_COMPARISON,
                AdvancedQuestionType.CONGRUENCY_COMPARISON,
                AdvancedQuestionType.EQUATION_SOLVING,
                AdvancedQuestionType.ANGLE_CALCULATION,
            ]
        
        # Select random advanced question type
        selected_type = random.choice(advanced_types)
        
        # Generate the advanced question
        shape_type = request.shape_type.value if request.shape_type else 'triangle'
        advanced_data = self.advanced_generator.generate_question(selected_type, request.difficulty, shape_type)
        
        # Convert to QuizQuestion format
        return QuizQuestion(
            question_id=f"q_advanced_{random.randint(1000, 9999)}",
            question=advanced_data['question'],
            correct_answer=advanced_data['answer'],
            options=self._generate_advanced_options(advanced_data['answer']),
            explanation=advanced_data['explanation'],
            difficulty=request.difficulty,
            topic=request.topic,
            question_type=request.question_type,
            shape_type=request.shape_type or ShapeType.TRIANGLE_EQUILATERAL,
            parameters=advanced_data['parameters'],
            geometric_constraints=['advanced_question'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            conversion_required=False,
            reasoning_required=request.difficulty == DifficultyLevel.HARD,
            south_african_context=True,
            curriculum_alignments=[request.topic],
            template_id=f"advanced_{selected_type.value}"
        )
    
    def _generate_advanced_options(self, correct_answer: str) -> List[str]:
        """Generate options for advanced questions"""
        options = [correct_answer]
        
        # Generate 3 incorrect options
        for _ in range(3):
            if 'cm²' in correct_answer:
                # Area question
                base_value = float(correct_answer.split()[0])
                variation = random.uniform(0.7, 1.3)
                wrong_answer = f"{round(base_value * variation, 1)} cm²"
                if wrong_answer not in options:
                    options.append(wrong_answer)
            elif '°' in correct_answer:
                # Angle question
                base_value = float(correct_answer.split()[0])
                variation = random.uniform(0.8, 1.2)
                wrong_answer = f"{round(base_value * variation, 1)}°"
                if wrong_answer not in options:
                    options.append(wrong_answer)
            elif 'cm' in correct_answer:
                # Length question
                base_value = float(correct_answer.split()[0])
                variation = random.uniform(0.8, 1.2)
                wrong_answer = f"{round(base_value * variation, 1)} cm"
                if wrong_answer not in options:
                    options.append(wrong_answer)
            else:
                # Text answer
                wrong_answer = f"Option {len(options)}"
                if wrong_answer not in options:
                    options.append(wrong_answer)
        
        # Ensure we have exactly 4 options
        while len(options) < 4:
            options.append(f"Option {len(options) + 1}")
        
        random.shuffle(options)
        return options
    
    def _generate_triangle_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate triangle question using proper parameter generator"""
        if request.question_type == QuestionType.AREA_CALCULATION:
            question = f"A triangle has base {parameters['base']} cm and height {parameters['height']} cm. What is its area?"
            options = [
                f"{parameters['area']} cm²",
                f"{parameters['area'] + 1} cm²", 
                f"{parameters['area'] - 1} cm²",
                f"{parameters['area'] * 2} cm²"
            ]
            explanation = f"Area = ½ × base × height = ½ × {parameters['base']} × {parameters['height']} = {parameters['area']} cm²"
            
        elif request.question_type == QuestionType.PERIMETER_CALCULATION:
            question = f"A triangle has sides {parameters['sides'][0]} cm, {parameters['sides'][1]} cm, and {parameters['sides'][2]} cm. What is its perimeter?"
            options = [
                f"{parameters['perimeter']} cm",
                f"{parameters['perimeter'] + 1} cm",
                f"{parameters['perimeter'] - 1} cm", 
                f"{parameters['perimeter'] * 2} cm"
            ]
            explanation = f"Perimeter = sum of all sides = {parameters['sides'][0]} + {parameters['sides'][1]} + {parameters['sides'][2]} = {parameters['perimeter']} cm"
            
        elif request.question_type == QuestionType.SHAPE_CLASSIFICATION:
            # Check if this is a similarity/congruency question based on topic
            print(f"DEBUG: topic = {getattr(request, 'topic', 'NO_TOPIC')}")
            if hasattr(request, 'topic') and request.topic in ['similarity', 'congruency', 'similarity_congruency']:
                print("DEBUG: Calling similarity method")
                return self._generate_similarity_congruency_question(request, parameters)
            
            # Regular triangle classification
            triangle_type = parameters.get('triangle_type', 'scalene')
            question = f"Classify this triangle with sides {parameters['sides'][0]} cm, {parameters['sides'][1]} cm, and {parameters['sides'][2]} cm."
            options = ["Equilateral", "Isosceles", "Scalene", "Right-angled"]
            
            if triangle_type == 'equilateral':
                correct_answer = "Equilateral"
            elif triangle_type == 'isosceles':
                correct_answer = "Isosceles"
            elif triangle_type == 'right_angled':
                correct_answer = "Right-angled"
            else:
                correct_answer = "Scalene"
            
            if triangle_type == 'equilateral':
                explanation = f"This triangle has sides {parameters['sides'][0]} cm, {parameters['sides'][1]} cm, and {parameters['sides'][2]} cm. Since all sides are equal, it is an equilateral triangle."
            elif triangle_type == 'isosceles':
                explanation = f"This triangle has sides {parameters['sides'][0]} cm, {parameters['sides'][1]} cm, and {parameters['sides'][2]} cm. Since two sides are equal, it is an isosceles triangle."
            elif triangle_type == 'right_angled':
                explanation = f"This triangle has sides {parameters['sides'][0]} cm, {parameters['sides'][1]} cm, and {parameters['sides'][2]} cm. Since it has a right angle, it is a right-angled triangle."
            else:  # scalene
                explanation = f"This triangle has sides {parameters['sides'][0]} cm, {parameters['sides'][1]} cm, and {parameters['sides'][2]} cm. Since all sides are different lengths, it is a scalene triangle."
            
        else:
            # Default area question
            question = f"A triangle has base {parameters['base']} cm and height {parameters['height']} cm. What is its area?"
            options = [
                f"{parameters['area']} cm²",
                f"{parameters['area'] + 1} cm²",
                f"{parameters['area'] - 1} cm²",
                f"{parameters['area'] * 2} cm²"
            ]
            explanation = f"Area = ½ × base × height = ½ × {parameters['base']} × {parameters['height']} = {parameters['area']} cm²"
            correct_answer = f"{parameters['area']} cm²"
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer if 'correct_answer' in locals() else f"{parameters['area']} cm²",
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters=parameters,
            geometric_constraints=['positive_dimensions'],
            curriculum_alignments=['Calculations involving 2D Shapes'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            south_african_context=request.south_african_context,
            conversion_required=request.conversion_required,
            question_id=self.generate_question_id()
        )
    
    def _generate_quadrilateral_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate quadrilateral question using proper parameter generator"""
        if request.question_type == QuestionType.AREA_CALCULATION:
            question = f"A rectangle has length {parameters['length']} cm and width {parameters['width']} cm. What is its area?"
            options = [
                f"{parameters['area']} cm²",
                f"{parameters['area'] + 1} cm²",
                f"{parameters['area'] - 1} cm²",
                f"{parameters['area'] * 2} cm²"
            ]
            explanation = f"Area = length × width = {parameters['length']} × {parameters['width']} = {parameters['area']} cm²"
            
        elif request.question_type == QuestionType.PERIMETER_CALCULATION:
            question = f"A rectangle has length {parameters['length']} cm and width {parameters['width']} cm. What is its perimeter?"
            options = [
                f"{parameters['perimeter']} cm",
                f"{parameters['perimeter'] + 1} cm",
                f"{parameters['perimeter'] - 1} cm",
                f"{parameters['perimeter'] * 2} cm"
            ]
            explanation = f"Perimeter = 2 × (length + width) = 2 × ({parameters['length']} + {parameters['width']}) = {parameters['perimeter']} cm"
            
        else:
            # Default area question
            question = f"A rectangle has length {parameters['length']} cm and width {parameters['width']} cm. What is its area?"
            options = [
                f"{parameters['area']} cm²",
                f"{parameters['area'] + 1} cm²",
                f"{parameters['area'] - 1} cm²",
                f"{parameters['area'] * 2} cm²"
            ]
            explanation = f"Area = length × width = {parameters['length']} × {parameters['width']} = {parameters['area']} cm²"
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=f"{parameters['area']} cm²",
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters=parameters,
            geometric_constraints=['positive_dimensions'],
            curriculum_alignments=['Calculations involving 2D Shapes'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            south_african_context=request.south_african_context,
            conversion_required=request.conversion_required,
            question_id=self.generate_question_id()
        )
    
    def _generate_circle_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate circle question using proper parameter generator"""
        if request.question_type == QuestionType.AREA_CALCULATION:
            question = f"A circle has radius {parameters['radius']} cm. What is its area?"
            options = [
                f"{parameters['area']} cm²",
                f"{parameters['area'] + 1} cm²",
                f"{parameters['area'] - 1} cm²",
                f"{parameters['area'] * 2} cm²"
            ]
            explanation = f"Area = π × radius² = π × {parameters['radius']}² = {parameters['area']} cm²"
            
        else:
            # Default area question
            question = f"A circle has radius {parameters['radius']} cm. What is its area?"
            options = [
                f"{parameters['area']} cm²",
                f"{parameters['area'] + 1} cm²",
                f"{parameters['area'] - 1} cm²",
                f"{parameters['area'] * 2} cm²"
            ]
            explanation = f"Area = π × radius² = π × {parameters['radius']}² = {parameters['area']} cm²"
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=f"{parameters['area']} cm²",
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters=parameters,
            geometric_constraints=['positive_dimensions'],
            curriculum_alignments=['Calculations involving 2D Shapes'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            south_african_context=request.south_african_context,
            conversion_required=request.conversion_required,
            question_id=self.generate_question_id()
        )
    
    def _generate_conversion_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate unit conversion question using proper parameter generator"""
        question = f"Convert {parameters['value']} {parameters['from_unit']} to {parameters['to_unit']}."
        options = [
            f"{parameters['converted_value']} {parameters['to_unit']}",
            f"{parameters['converted_value'] + 1} {parameters['to_unit']}",
            f"{parameters['converted_value'] - 1} {parameters['to_unit']}",
            f"{parameters['converted_value'] * 2} {parameters['to_unit']}"
        ]
        explanation = f"To convert {parameters['from_unit']} to {parameters['to_unit']}, multiply by the conversion factor: {parameters['value']} {parameters['from_unit']} = {parameters['converted_value']} {parameters['to_unit']}"
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=f"{parameters['converted_value']} {parameters['to_unit']}",
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters=parameters,
            geometric_constraints=[],
            curriculum_alignments=['Unit Conversions'],
            metric_units={'length': parameters['to_unit']},
            south_african_context=request.south_african_context,
            conversion_required=True,
            question_id=self.generate_question_id()
        )
    
    def _generate_equation_parameters(self, difficulty: DifficultyLevel, shape_type: ShapeType) -> Dict[str, Any]:
        """Generate parameters for equation solving questions"""
        if difficulty == DifficultyLevel.EASY:
            # Simple formula reversal: 4s = 32, 3x = 15, etc.
            coefficient = random.randint(2, 10)
            answer = random.randint(2, 20)
            variable = random.choice(['s', 'x', 'l', 'w', 'r'])
            equation = f"{coefficient}{variable} = {coefficient * answer}"
            correct_answer = str(answer)
            
        elif difficulty == DifficultyLevel.MEDIUM:
            # Area and perimeter formula reversal
            shape = random.choice(['rectangle', 'triangle', 'circle'])
            if shape == 'rectangle':
                length = random.randint(3, 10)
                width = random.randint(2, 8)
                area = length * width
                equation = f"l × w = {area} (where l = {length})"
                correct_answer = str(width)
                variable = 'w'
            elif shape == 'triangle':
                base = random.randint(4, 12)
                height = random.randint(3, 9)
                area = (base * height) // 2
                equation = f"½ × b × h = {area} (where b = {base})"
                correct_answer = str(height)
                variable = 'h'
            else:  # circle
                radius = random.randint(2, 8)
                area = round(3.14 * radius * radius, 1)
                equation = f"π × r² = {area}"
                correct_answer = str(radius)
                variable = 'r'
        else:  # HARD
            # Complex multi-step equation solving
            shape = random.choice(['rectangle', 'triangle', 'circle'])
            if shape == 'rectangle':
                length = random.randint(5, 15)
                width = random.randint(3, 10)
                perimeter = 2 * (length + width)
                equation = f"2(l + w) = {perimeter} (where l = {length})"
                correct_answer = str(width)
                variable = 'w'
            elif shape == 'triangle':
                side1 = random.randint(4, 12)
                side2 = random.randint(3, 10)
                side3 = random.randint(5, 15)
                perimeter = side1 + side2 + side3
                equation = f"a + b + c = {perimeter} (where a = {side1}, b = {side2})"
                correct_answer = str(side3)
                variable = 'c'
            else:  # circle
                radius = random.randint(3, 10)
                circumference = round(2 * 3.14 * radius, 1)
                equation = f"2πr = {circumference}"
                correct_answer = str(radius)
                variable = 'r'
        
        return {
            'equation': equation,
            'variable': variable,
            'correct_answer': correct_answer,
            'difficulty': difficulty.value,
            'shape_type': shape if 'shape' in locals() else 'general'
        }
    
    def _generate_equation_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate equation solving question"""
        equation = parameters['equation']
        variable = parameters['variable']
        correct_answer = parameters['correct_answer']
        
        # Generate question text
        if request.difficulty == DifficultyLevel.EASY:
            question = f"Solve for {variable}: {equation}"
        elif request.difficulty == DifficultyLevel.MEDIUM:
            question = f"Find the value of {variable} in: {equation}"
        else:  # HARD
            question = f"Solve the equation and find {variable}: {equation}"
        
        # Generate options
        correct_num = float(correct_answer)
        options = [
            correct_answer,
            str(correct_num + random.randint(1, 5)),
            str(correct_num - random.randint(1, 5)),
            str(correct_num * 2)
        ]
        random.shuffle(options)
        
        # Generate explanation
        if request.difficulty == DifficultyLevel.EASY:
            explanation = f"To solve {equation}, divide both sides by the coefficient of {variable}."
        elif request.difficulty == DifficultyLevel.MEDIUM:
            explanation = f"Substitute the given values and solve for {variable} using the appropriate formula."
        else:  # HARD
            explanation = f"Use algebraic manipulation to isolate {variable} and solve the equation step by step."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters=parameters,
            geometric_constraints=['equation_solving'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            conversion_required=False,
            reasoning_required=request.difficulty == DifficultyLevel.HARD,
            south_african_context=True,
            curriculum_alignments=['Equation Solving'],
            question_id=self.generate_question_id()
        )
    
    def _generate_triangle_height_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate parameters for triangle height questions"""
        if difficulty == DifficultyLevel.MEDIUM:
            # Basic height identification and calculation
            base = random.randint(6, 15)
            height = random.randint(4, 12)
            area = (base * height) // 2
            
            # Randomly choose what to find
            find_type = random.choice(['height', 'base', 'area'])
            
            if find_type == 'height':
                question_data = {
                    'base': base,
                    'area': area,
                    'find': 'height',
                    'answer': height,
                    'given': f"base = {base} cm, area = {area} cm²"
                }
            elif find_type == 'base':
                question_data = {
                    'height': height,
                    'area': area,
                    'find': 'base',
                    'answer': base,
                    'given': f"height = {height} cm, area = {area} cm²"
                }
            else:  # area
                question_data = {
                    'base': base,
                    'height': height,
                    'find': 'area',
                    'answer': area,
                    'given': f"base = {base} cm, height = {height} cm"
                }
        else:  # HARD
            # Multiple bases and heights, complex triangle problems
            # Create a triangle with multiple possible bases
            side1 = random.randint(8, 20)
            side2 = random.randint(6, 18)
            side3 = random.randint(10, 25)
            
            # Calculate area using Heron's formula
            s = (side1 + side2 + side3) / 2
            area = round((s * (s - side1) * (s - side2) * (s - side3)) ** 0.5, 1)
            
            # Find height to a specific base
            base_side = random.choice([side1, side2, side3])
            height = round((2 * area) / base_side, 1)
            
            question_data = {
                'side1': side1,
                'side2': side2,
                'side3': side3,
                'base_side': base_side,
                'area': area,
                'height': height,
                'find': 'height_to_base',
                'answer': height,
                'given': f"triangle with sides {side1} cm, {side2} cm, {side3} cm, area = {area} cm²"
            }
        
        return {
            'question_data': question_data,
            'difficulty': difficulty.value,
            'triangle_type': random.choice(['scalene', 'isosceles', 'right'])
        }
    
    def _generate_triangle_height_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate triangle height question"""
        data = parameters['question_data']
        find_type = data['find']
        answer = data['answer']
        
        # Generate question text
        if request.difficulty == DifficultyLevel.MEDIUM:
            if find_type == 'height':
                question = f"A triangle has {data['given']}. What is the height of the triangle?"
            elif find_type == 'base':
                question = f"A triangle has {data['given']}. What is the base of the triangle?"
            else:  # area
                question = f"A triangle has {data['given']}. What is the area of the triangle?"
        else:  # HARD
            question = f"A triangle has {data['given']}. What is the height to the side of {data['base_side']} cm?"
        
        # Generate options
        correct_num = float(answer)
        options = [
            str(answer),
            str(round(correct_num + random.uniform(1, 3), 1)),
            str(round(correct_num - random.uniform(1, 3), 1)),
            str(round(correct_num * 1.5, 1))
        ]
        random.shuffle(options)
        
        # Generate explanation
        if request.difficulty == DifficultyLevel.MEDIUM:
            if find_type == 'height':
                explanation = f"Use the formula: Area = ½ × base × height. Rearrange to find height = (2 × area) ÷ base = (2 × {data['area']}) ÷ {data['base']} = {answer} cm."
            elif find_type == 'base':
                explanation = f"Use the formula: Area = ½ × base × height. Rearrange to find base = (2 × area) ÷ height = (2 × {data['area']}) ÷ {data['height']} = {answer} cm."
            else:  # area
                explanation = f"Use the formula: Area = ½ × base × height = ½ × {data['base']} × {data['height']} = {answer} cm²."
        else:  # HARD
            explanation = f"Use the formula: Height = (2 × area) ÷ base = (2 × {data['area']}) ÷ {data['base_side']} = {answer} cm. This gives the height perpendicular to the specified base."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=str(answer),
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters=parameters,
            geometric_constraints=['triangle_height'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            conversion_required=False,
            reasoning_required=request.difficulty == DifficultyLevel.HARD,
            south_african_context=True,
            curriculum_alignments=['Triangle Height Concepts'],
            question_id=self.generate_question_id()
        )
    
    def get_available_templates(self, topic: str, difficulty: DifficultyLevel) -> List[QuestionTemplate]:
        """Get available templates for constraint-based generation"""
        # For constraint-based generation, we don't use pre-defined templates
        # Instead, we generate questions dynamically based on constraints
        return []
    
    def _generate_similarity_congruency_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate similarity and congruency questions"""
        topic = getattr(request, 'topic', 'similarity')
        print(f"DEBUG: _generate_similarity_congruency_question called with topic={topic}")
        
        if topic == 'similarity':
            print("DEBUG: Calling _generate_similarity_question")
            return self._generate_similarity_question(request, parameters)
        elif topic == 'congruency':
            print("DEBUG: Calling _generate_congruency_question")
            return self._generate_congruency_question(request, parameters)
        else:  # similarity_congruency
            print("DEBUG: Calling _generate_combined_similarity_congruency_question")
            return self._generate_combined_similarity_congruency_question(request, parameters)
    
    def _generate_similarity_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate triangle similarity question"""
        # Use existing triangle parameters or generate new ones
        if 'sides' in parameters:
            base_sides = parameters['sides']
        else:
            base_sides = [random.randint(3, 6), random.randint(4, 8), random.randint(5, 10)]
        
        scale_factor = random.uniform(1.5, 3.0)
        scaled_sides = [round(side * scale_factor, 1) for side in base_sides]
        
        question = f"Triangle A has sides {base_sides[0]} cm, {base_sides[1]} cm, and {base_sides[2]} cm. Triangle B has sides {scaled_sides[0]} cm, {scaled_sides[1]} cm, and {scaled_sides[2]} cm. Are these triangles similar?"
        
        options = [
            "Yes, the shapes are similar",
            "No, the shapes are not similar",
            "Yes, the shapes are congruent",
            "No, the shapes are not congruent"
        ]
        
        correct_answer = "Yes, the shapes are similar"
        explanation = f"Triangle A and Triangle B are similar because their corresponding sides are proportional. The ratio of corresponding sides is {scale_factor:.1f}, which means Triangle B is {scale_factor:.1f} times larger than Triangle A."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={
                'triangle_a_sides': base_sides,
                'triangle_b_sides': scaled_sides,
                'scale_factor': scale_factor,
                'similarity_type': 'proportional_sides'
            },
            geometric_constraints=['triangle_inequality', 'similarity_ratio'],
            metric_units={'length': 'cm'},
            conversion_required=False,
            reasoning_required=request.difficulty.value in ['medium', 'hard'],
            south_african_context=True,
            curriculum_alignments=['Properties of 2D Shapes'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )
    
    def _generate_congruency_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate triangle congruency question"""
        # Use existing triangle parameters or generate new ones
        if 'sides' in parameters:
            sides = parameters['sides']
        else:
            sides = [random.randint(3, 6), random.randint(4, 8), random.randint(5, 10)]
        
        question = f"Triangle A has sides {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. Triangle B has sides {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. Are these triangles congruent?"
        
        options = [
            "Yes, the shapes are similar",
            "No, the shapes are not similar",
            "Yes, the shapes are congruent",
            "No, the shapes are not congruent"
        ]
        
        correct_answer = "Yes, the shapes are congruent"
        explanation = f"Triangle A and Triangle B are congruent because all their corresponding sides are equal. Both triangles have sides of {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={
                'triangle_a_sides': sides,
                'triangle_b_sides': sides,
                'congruency_type': 'equal_sides'
            },
            geometric_constraints=['triangle_inequality', 'congruency_check'],
            metric_units={'length': 'cm'},
            conversion_required=False,
            reasoning_required=request.difficulty.value in ['medium', 'hard'],
            south_african_context=True,
            curriculum_alignments=['Properties of 2D Shapes'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )
    
    def _generate_combined_similarity_congruency_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate combined similarity and congruency question"""
        # Use existing triangle parameters or generate new ones
        if 'sides' in parameters:
            base_sides = parameters['sides']
        else:
            base_sides = [random.randint(4, 8), random.randint(5, 10), random.randint(6, 12)]
        scale_factor = random.uniform(1.5, 2.5)
        similar_sides = [round(side * scale_factor, 1) for side in base_sides]
        
        question = f"Compare three triangles: Triangle A ({base_sides[0]} cm, {base_sides[1]} cm, {base_sides[2]} cm), Triangle B ({similar_sides[0]} cm, {similar_sides[1]} cm, {similar_sides[2]} cm), and Triangle C ({base_sides[0]} cm, {base_sides[1]} cm, {base_sides[2]} cm). Which triangles are similar? Which are congruent?"
        
        options = [
            "A and B are similar, A and C are congruent",
            "A and C are similar, B and C are congruent", 
            "All triangles are similar",
            "No triangles are similar or congruent"
        ]
        
        correct_answer = "A and B are similar, A and C are congruent"
        explanation = f"Triangle A and Triangle B are similar because their sides are proportional (ratio {scale_factor:.1f}). Triangle A and Triangle C are congruent because all their corresponding sides are equal."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={
                'triangle_a_sides': base_sides,
                'triangle_b_sides': similar_sides,
                'triangle_c_sides': base_sides,
                'scale_factor': scale_factor,
                'comparison_type': 'multiple_triangles'
            },
            geometric_constraints=['triangle_inequality', 'similarity_ratio', 'congruency_check'],
            metric_units={'length': 'cm'},
            conversion_required=False,
            reasoning_required=True,
            south_african_context=True,
            curriculum_alignments=['Properties of 2D Shapes'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_3d_parameters(self, request: QuizGenerationRequest) -> Dict[str, Any]:
        """Generate parameters for 3D geometry questions"""
        if request.difficulty == DifficultyLevel.EASY:
            if request.question_type == QuestionType.VOLUME_CALCULATION:
                side_length = random.randint(2, 5)
                return {
                    'shape_type': 'cube',
                    'side_length': side_length,
                    'volume': side_length ** 3,
                    'surface_area': 6 * (side_length ** 2)
                }
            else:  # SURFACE_AREA_CALCULATION
                length = random.randint(2, 4)
                width = random.randint(2, 4)
                height = random.randint(2, 4)
                return {
                    'shape_type': 'rectangular_prism',
                    'length': length,
                    'width': width,
                    'height': height,
                    'volume': length * width * height,
                    'surface_area': 2 * (length * width + length * height + width * height)
                }
        elif request.difficulty == DifficultyLevel.MEDIUM:
            if request.question_type == QuestionType.VOLUME_CALCULATION:
                side_length = random.uniform(2.5, 6.0)
                return {
                    'shape_type': 'cube',
                    'side_length': round(side_length, 1),
                    'volume': round(side_length ** 3, 2),
                    'surface_area': round(6 * (side_length ** 2), 2)
                }
            else:  # SURFACE_AREA_CALCULATION
                length = random.uniform(3.0, 8.0)
                width = random.uniform(2.0, 6.0)
                height = random.uniform(2.0, 5.0)
                return {
                    'shape_type': 'rectangular_prism',
                    'length': round(length, 1),
                    'width': round(width, 1),
                    'height': round(height, 1),
                    'volume': round(length * width * height, 2),
                    'surface_area': round(2 * (length * width + length * height + width * height), 2)
                }
        else:  # HARD
            if request.question_type == QuestionType.VOLUME_CALCULATION:
                side_length = random.uniform(4.0, 12.0)
                return {
                    'shape_type': 'cube',
                    'side_length': round(side_length, 1),
                    'volume': round(side_length ** 3, 2),
                    'surface_area': round(6 * (side_length ** 2), 2)
                }
            else:  # SURFACE_AREA_CALCULATION
                length = random.uniform(5.0, 15.0)
                width = random.uniform(3.0, 10.0)
                height = random.uniform(2.0, 8.0)
                return {
                    'shape_type': 'rectangular_prism',
                    'length': round(length, 1),
                    'width': round(width, 1),
                    'height': round(height, 1),
                    'volume': round(length * width * height, 2),
                    'surface_area': round(2 * (length * width + length * height + width * height), 2)
                }

    def _generate_volume_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate volume calculation question with variety"""
        question_variants = [
            self._generate_forward_volume_question,
            self._generate_reverse_volume_question,
            self._generate_volume_unit_conversion_question
        ]
        
        # Randomly select question variant
        variant = random.choice(question_variants)
        return variant(parameters, request.difficulty)

    def _generate_forward_volume_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Given dimensions, find volume"""
        if parameters['shape_type'] == 'cube':
            side = parameters['side_length']
            question_text = f"Calculate the volume of a cube with side length {side} cm."
            correct_answer = f"{parameters['volume']} cm³"
            
            # Generate wrong options
            wrong_options = [
                f"{parameters['surface_area']} cm³",  # Surface area instead of volume
                f"{side ** 2} cm³",  # Area instead of volume
                f"{side * 6} cm³",  # Perimeter * 6
                f"{side ** 4} cm³"   # Side to the 4th power
            ]
        else:  # rectangular prism
            l, w, h = parameters['length'], parameters['width'], parameters['height']
            question_text = f"Calculate the volume of a rectangular prism with dimensions {l} cm × {w} cm × {h} cm."
            correct_answer = f"{parameters['volume']} cm³"
            
            # Generate wrong options
            wrong_options = [
                f"{parameters['surface_area']} cm³",  # Surface area instead of volume
                f"{l * w} cm³",  # Area of one face
                f"{l + w + h} cm³",  # Sum of dimensions
                f"{2 * (l * w + l * h + w * h)} cm³"  # Double surface area
            ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        explanation = f"Volume = {'side × side × side' if parameters['shape_type'] == 'cube' else 'length × width × height'} = {correct_answer}"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Volume Calculations'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_reverse_volume_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Given volume, find dimensions"""
        if parameters['shape_type'] == 'cube':
            volume = parameters['volume']
            side = parameters['side_length']
            question_text = f"A cube has a volume of {volume} cm³. What is the length of one side?"
            correct_answer = f"{side} cm"
            
            # Generate wrong options
            wrong_options = [
                f"{volume ** (1/2):.1f} cm",  # Square root instead of cube root
                f"{volume / 6:.1f} cm",  # Volume divided by 6
                f"{volume ** (1/3) * 2:.1f} cm",  # Double the correct answer
                f"{volume / 3:.1f} cm"  # Volume divided by 3
            ]
        else:  # rectangular prism
            volume = parameters['volume']
            l, w, h = parameters['length'], parameters['width'], parameters['height']
            # Ask for one dimension, give the other two
            if random.choice([True, False]):
                question_text = f"A rectangular prism has volume {volume} cm³, length {l} cm, and width {w} cm. What is the height?"
                correct_answer = f"{h} cm"
                wrong_options = [
                    f"{volume / (l * w) * 2:.1f} cm",  # Double the correct answer
                    f"{volume / (l + w):.1f} cm",  # Volume divided by sum
                    f"{l * w:.1f} cm",  # Area instead of height
                    f"{volume / l:.1f} cm"  # Volume divided by length
                ]
            else:
                question_text = f"A rectangular prism has volume {volume} cm³, length {l} cm, and height {h} cm. What is the width?"
                correct_answer = f"{w} cm"
                wrong_options = [
                    f"{volume / (l * h) * 2:.1f} cm",  # Double the correct answer
                    f"{volume / (l + h):.1f} cm",  # Volume divided by sum
                    f"{l * h:.1f} cm",  # Area instead of width
                    f"{volume / h:.1f} cm"  # Volume divided by height
                ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        if parameters['shape_type'] == 'cube':
            explanation = f"Volume = side³, so side = ∛{volume} = {side} cm"
        else:
            explanation = f"Volume = length × width × height, so {'height' if 'height' in question_text else 'width'} = {volume} ÷ ({l} × {w if 'height' in question_text else h}) = {correct_answer}"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Volume Calculations'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_volume_unit_conversion_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Volume unit conversion questions"""
        volume_cm3 = parameters['volume']
        volume_ml = volume_cm3  # 1 cm³ = 1 ml
        volume_l = round(volume_cm3 / 1000, 3)
        
        if random.choice([True, False]):
            # Convert cm³ to ml or l
            if random.choice([True, False]):
                question_text = f"A cube has volume {volume_cm3} cm³. What is its volume in milliliters?"
                correct_answer = f"{volume_ml} ml"
                wrong_options = [
                    f"{volume_l} ml",  # Liters instead of ml
                    f"{volume_cm3 * 1000} ml",  # Incorrect conversion
                    f"{volume_cm3 / 1000} ml",  # Incorrect conversion
                    f"{volume_cm3 * 100} ml"  # Incorrect conversion
                ]
            else:
                question_text = f"A cube has volume {volume_cm3} cm³. What is its volume in liters?"
                correct_answer = f"{volume_l} l"
                wrong_options = [
                    f"{volume_ml} l",  # Milliliters instead of liters
                    f"{volume_cm3} l",  # No conversion
                    f"{volume_cm3 * 1000} l",  # Incorrect conversion
                    f"{volume_cm3 / 100} l"  # Incorrect conversion
                ]
        else:
            # Convert ml or l to cm³
            if random.choice([True, False]):
                question_text = f"A cube has volume {volume_ml} ml. What is its volume in cubic centimeters?"
                correct_answer = f"{volume_cm3} cm³"
                wrong_options = [
                    f"{volume_l} cm³",  # Liters instead of cm³
                    f"{volume_ml * 1000} cm³",  # Incorrect conversion
                    f"{volume_ml / 1000} cm³",  # Incorrect conversion
                    f"{volume_ml * 100} cm³"  # Incorrect conversion
                ]
            else:
                question_text = f"A cube has volume {volume_l} l. What is its volume in cubic centimeters?"
                correct_answer = f"{volume_cm3} cm³"
                wrong_options = [
                    f"{volume_ml} cm³",  # Milliliters instead of cm³
                    f"{volume_l * 100} cm³",  # Incorrect conversion
                    f"{volume_l / 1000} cm³",  # Incorrect conversion
                    f"{volume_l * 10} cm³"  # Incorrect conversion
                ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        explanation = f"1 cm³ = 1 ml, and 1000 cm³ = 1 l. So {volume_cm3} cm³ = {volume_ml} ml = {volume_l} l"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.VOLUME_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Volume Calculations', 'Unit Conversions'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_surface_area_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate surface area calculation question with variety"""
        question_variants = [
            self._generate_forward_surface_area_question,
            self._generate_reverse_surface_area_question,
            self._generate_surface_area_unit_conversion_question
        ]
        
        # Randomly select question variant
        variant = random.choice(question_variants)
        return variant(parameters, request.difficulty)

    def _generate_forward_surface_area_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Given dimensions, find surface area"""
        if parameters['shape_type'] == 'cube':
            side = parameters['side_length']
            question_text = f"Calculate the surface area of a cube with side length {side} cm."
            correct_answer = f"{parameters['surface_area']} cm²"
            
            # Generate wrong options
            wrong_options = [
                f"{parameters['volume']} cm²",  # Volume instead of surface area
                f"{side ** 3} cm²",  # Volume formula
                f"{side ** 2} cm²",  # Area of one face
                f"{side * 6} cm²"   # Side * 6
            ]
        else:  # rectangular prism
            l, w, h = parameters['length'], parameters['width'], parameters['height']
            question_text = f"Calculate the surface area of a rectangular prism with dimensions {l} cm × {w} cm × {h} cm."
            correct_answer = f"{parameters['surface_area']} cm²"
            
            # Generate wrong options
            wrong_options = [
                f"{parameters['volume']} cm²",  # Volume instead of surface area
                f"{l * w} cm²",  # Area of one face
                f"{l + w + h} cm²",  # Sum of dimensions
                f"{l * w * h} cm²"   # Volume formula
            ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        explanation = f"Surface Area = {'6 × side²' if parameters['shape_type'] == 'cube' else '2(lw + lh + wh)'} = {correct_answer}"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Surface Area Calculations'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_reverse_surface_area_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Given surface area, find dimensions"""
        if parameters['shape_type'] == 'cube':
            surface_area = parameters['surface_area']
            side = parameters['side_length']
            question_text = f"A cube has a surface area of {surface_area} cm². What is the length of one side?"
            correct_answer = f"{side} cm"
            
            # Generate wrong options
            wrong_options = [
                f"{(surface_area / 6) ** (1/2) * 2:.1f} cm",  # Double the correct answer
                f"{surface_area / 6:.1f} cm",  # Surface area divided by 6
                f"{surface_area ** (1/2):.1f} cm",  # Square root of surface area
                f"{surface_area / 3:.1f} cm"  # Surface area divided by 3
            ]
        else:  # rectangular prism
            surface_area = parameters['surface_area']
            l, w, h = parameters['length'], parameters['width'], parameters['height']
            # Ask for one dimension, give the other two
            if random.choice([True, False]):
                question_text = f"A rectangular prism has surface area {surface_area} cm², length {l} cm, and width {w} cm. What is the height?"
                correct_answer = f"{h} cm"
                # For rectangular prism: SA = 2(lw + lh + wh), so h = (SA/2 - lw)/(l + w)
                wrong_options = [
                    f"{h * 2:.1f} cm",  # Double the correct answer
                    f"{surface_area / (2 * (l + w)):.1f} cm",  # Incorrect formula
                    f"{l * w:.1f} cm",  # Area instead of height
                    f"{surface_area / (l + w):.1f} cm"  # Incorrect formula
                ]
            else:
                question_text = f"A rectangular prism has surface area {surface_area} cm², length {l} cm, and height {h} cm. What is the width?"
                correct_answer = f"{w} cm"
                wrong_options = [
                    f"{w * 2:.1f} cm",  # Double the correct answer
                    f"{surface_area / (2 * (l + h)):.1f} cm",  # Incorrect formula
                    f"{l * h:.1f} cm",  # Area instead of width
                    f"{surface_area / (l + h):.1f} cm"  # Incorrect formula
                ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        if parameters['shape_type'] == 'cube':
            explanation = f"Surface Area = 6 × side², so side = √({surface_area}/6) = {side} cm"
        else:
            explanation = f"Surface Area = 2(lw + lh + wh), so {'height' if 'height' in question_text else 'width'} = ({surface_area}/2 - {l}×{w if 'height' in question_text else h})/({l} + {w if 'height' in question_text else h}) = {correct_answer}"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Surface Area Calculations'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_surface_area_unit_conversion_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Surface area unit conversion questions"""
        surface_area_cm2 = parameters['surface_area']
        surface_area_m2 = round(surface_area_cm2 / 10000, 4)  # 1 m² = 10,000 cm²
        
        if random.choice([True, False]):
            # Convert cm² to m²
            question_text = f"A cube has surface area {surface_area_cm2} cm². What is its surface area in square meters?"
            correct_answer = f"{surface_area_m2} m²"
            wrong_options = [
                f"{surface_area_cm2} m²",  # No conversion
                f"{surface_area_cm2 / 100} m²",  # Incorrect conversion
                f"{surface_area_cm2 * 10000} m²",  # Incorrect conversion
                f"{surface_area_cm2 / 1000} m²"  # Incorrect conversion
            ]
        else:
            # Convert m² to cm²
            question_text = f"A cube has surface area {surface_area_m2} m². What is its surface area in square centimeters?"
            correct_answer = f"{surface_area_cm2} cm²"
            wrong_options = [
                f"{surface_area_m2} cm²",  # No conversion
                f"{surface_area_m2 * 100} cm²",  # Incorrect conversion
                f"{surface_area_m2 / 10000} cm²",  # Incorrect conversion
                f"{surface_area_m2 * 1000} cm²"  # Incorrect conversion
            ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        explanation = f"1 m² = 10,000 cm². So {surface_area_cm2} cm² = {surface_area_m2} m²"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.SURFACE_AREA_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Surface Area Calculations', 'Unit Conversions'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_capacity_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate capacity calculation question with variety"""
        question_variants = [
            self._generate_forward_capacity_question,
            self._generate_reverse_capacity_question,
            self._generate_capacity_unit_conversion_question
        ]
        
        # Randomly select question variant
        variant = random.choice(question_variants)
        return variant(parameters, request.difficulty)

    def _generate_forward_capacity_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Given dimensions, find capacity"""
        volume = parameters['volume']
        capacity_ml = volume  # 1 cm³ = 1 ml
        capacity_l = round(volume / 1000, 3)  # Convert to liters
        
        if parameters['shape_type'] == 'cube':
            side = parameters['side_length']
            question_text = f"A cube with side length {side} cm is filled with water. What is its capacity in milliliters?"
        else:
            l, w, h = parameters['length'], parameters['width'], parameters['height']
            question_text = f"A rectangular prism with dimensions {l} cm × {w} cm × {h} cm is filled with water. What is its capacity in milliliters?"
        
        correct_answer = f"{capacity_ml} ml"
        
        # Generate wrong options
        wrong_options = [
            f"{capacity_l} ml",  # Liters instead of ml
            f"{volume * 1000} ml",  # Incorrect conversion
            f"{parameters['surface_area']} ml",  # Surface area instead of volume
            f"{volume / 1000} ml"  # Incorrect conversion
        ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        explanation = f"Capacity = Volume = {volume} cm³ = {capacity_ml} ml (since 1 cm³ = 1 ml)"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.CAPACITY_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Capacity Calculations'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_reverse_capacity_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Given capacity, find dimensions"""
        volume = parameters['volume']
        capacity_ml = volume  # 1 cm³ = 1 ml
        
        if parameters['shape_type'] == 'cube':
            side = parameters['side_length']
            question_text = f"A cube has a capacity of {capacity_ml} ml when filled with water. What is the length of one side?"
            correct_answer = f"{side} cm"
            
            # Generate wrong options
            wrong_options = [
                f"{volume ** (1/2):.1f} cm",  # Square root instead of cube root
                f"{volume / 6:.1f} cm",  # Volume divided by 6
                f"{volume ** (1/3) * 2:.1f} cm",  # Double the correct answer
                f"{volume / 3:.1f} cm"  # Volume divided by 3
            ]
        else:  # rectangular prism
            l, w, h = parameters['length'], parameters['width'], parameters['height']
            # Ask for one dimension, give the other two
            if random.choice([True, False]):
                question_text = f"A rectangular prism has capacity {capacity_ml} ml, length {l} cm, and width {w} cm. What is the height?"
                correct_answer = f"{h} cm"
                wrong_options = [
                    f"{volume / (l * w) * 2:.1f} cm",  # Double the correct answer
                    f"{volume / (l + w):.1f} cm",  # Volume divided by sum
                    f"{l * w:.1f} cm",  # Area instead of height
                    f"{volume / l:.1f} cm"  # Volume divided by length
                ]
            else:
                question_text = f"A rectangular prism has capacity {capacity_ml} ml, length {l} cm, and height {h} cm. What is the width?"
                correct_answer = f"{w} cm"
                wrong_options = [
                    f"{volume / (l * h) * 2:.1f} cm",  # Double the correct answer
                    f"{volume / (l + h):.1f} cm",  # Volume divided by sum
                    f"{l * h:.1f} cm",  # Area instead of width
                    f"{volume / h:.1f} cm"  # Volume divided by height
                ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        if parameters['shape_type'] == 'cube':
            explanation = f"Capacity = Volume = side³, so side = ∛{volume} = {side} cm"
        else:
            explanation = f"Capacity = Volume = length × width × height, so {'height' if 'height' in question_text else 'width'} = {volume} ÷ ({l} × {w if 'height' in question_text else h}) = {correct_answer}"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.CAPACITY_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Capacity Calculations'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_capacity_unit_conversion_question(self, parameters: Dict[str, Any], difficulty) -> QuizQuestion:
        """Capacity unit conversion questions"""
        volume = parameters['volume']
        capacity_ml = volume  # 1 cm³ = 1 ml
        capacity_l = round(volume / 1000, 3)  # Convert to liters
        
        if random.choice([True, False]):
            # Convert ml to l or cm³ to l
            if random.choice([True, False]):
                question_text = f"A container has capacity {capacity_ml} ml. What is its capacity in liters?"
                correct_answer = f"{capacity_l} l"
                wrong_options = [
                    f"{capacity_ml} l",  # No conversion
                    f"{capacity_ml * 1000} l",  # Incorrect conversion
                    f"{capacity_ml / 100} l",  # Incorrect conversion
                    f"{capacity_ml * 100} l"  # Incorrect conversion
                ]
            else:
                question_text = f"A container has volume {volume} cm³. What is its capacity in liters?"
                correct_answer = f"{capacity_l} l"
                wrong_options = [
                    f"{volume} l",  # No conversion
                    f"{volume * 1000} l",  # Incorrect conversion
                    f"{volume / 100} l",  # Incorrect conversion
                    f"{volume * 100} l"  # Incorrect conversion
                ]
        else:
            # Convert l to ml or l to cm³
            if random.choice([True, False]):
                question_text = f"A container has capacity {capacity_l} l. What is its capacity in milliliters?"
                correct_answer = f"{capacity_ml} ml"
                wrong_options = [
                    f"{capacity_l} ml",  # No conversion
                    f"{capacity_l / 1000} ml",  # Incorrect conversion
                    f"{capacity_l * 100} ml",  # Incorrect conversion
                    f"{capacity_l / 100} ml"  # Incorrect conversion
                ]
            else:
                question_text = f"A container has capacity {capacity_l} l. What is its volume in cubic centimeters?"
                correct_answer = f"{volume} cm³"
                wrong_options = [
                    f"{capacity_l} cm³",  # No conversion
                    f"{capacity_l / 1000} cm³",  # Incorrect conversion
                    f"{capacity_l * 100} cm³",  # Incorrect conversion
                    f"{capacity_l / 100} cm³"  # Incorrect conversion
                ]
        
        options = [correct_answer] + wrong_options[:3]
        random.shuffle(options)
        
        explanation = f"1 cm³ = 1 ml, and 1000 ml = 1 l. So {volume} cm³ = {capacity_ml} ml = {capacity_l} l"
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=difficulty,
            question_type=QuestionType.CAPACITY_CALCULATION,
            shape_type=parameters['shape_type'],
            curriculum_alignments=['3D Geometry', 'Capacity Calculations', 'Unit Conversions'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )

    def _generate_3d_shape_recognition_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate 3D shape recognition question"""
        shapes = ['cube', 'rectangular prism', 'cylinder', 'sphere', 'cone', 'pyramid']
        correct_shape = random.choice(shapes)
        
        # Generate descriptions for different shapes
        descriptions = {
            'cube': 'A 3D shape with 6 square faces, all edges equal length',
            'rectangular prism': 'A 3D shape with 6 rectangular faces, opposite faces identical',
            'cylinder': 'A 3D shape with 2 circular bases and 1 curved surface',
            'sphere': 'A perfectly round 3D shape with no edges or vertices',
            'cone': 'A 3D shape with 1 circular base and 1 vertex',
            'pyramid': 'A 3D shape with a polygonal base and triangular faces meeting at a vertex'
        }
        
        question_text = f"Which 3D shape is described as: {descriptions[correct_shape]}?"
        correct_answer = correct_shape.title()
        
        # Generate wrong options
        wrong_shapes = [s for s in shapes if s != correct_shape]
        wrong_options = [s.title() for s in random.sample(wrong_shapes, 3)]
        
        options = [correct_answer] + wrong_options
        random.shuffle(options)
        
        explanation = f"The correct answer is {correct_answer} because it matches the given description."
        
        return QuizQuestion(
            question_text=question_text,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            curriculum_alignments=['3D Geometry', 'Shape Recognition'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )


class TemplateBasedGenerator(QuizGenerator):
    """
    Fallback generator using pre-defined question templates
    Implements 240 question templates as per plan Phase 3.1
    """
    
    def __init__(self):
        super().__init__()
        self.template_registry = TemplateRegistry()
        # Get templates dynamically when needed instead of loading all at once
        self.templates = None  # Will be loaded on demand
    
    def generate_question(self, request: QuizGenerationRequest) -> QuizQuestion:
        """Generate question using template-based approach with 240 templates"""
        try:
            # Get templates for the requested shape and difficulty
            shape_key = self._get_shape_key(request.shape_type)
            difficulty_key = request.difficulty.value.lower()
            
            available_templates = self.template_registry.get_templates(7, shape_key, difficulty_key)
            
            if not available_templates:
                # Fallback to triangle easy if no templates found
                available_templates = self.template_registry.get_templates(7, 'triangles', 'easy')
            
            if not available_templates:
                raise ValueError("No templates available for fallback")
            
            # Select a random template
            template = random.choice(available_templates)
            
            # Generate parameters based on template ranges
            parameters = self._generate_template_parameters(template)
            
            # Generate question text
            question_text = template.question_template.format(**parameters)
            
            # Calculate correct answer based on question type
            correct_answer = self._calculate_template_answer(template, parameters)
            
            # Generate options
            options = self._generate_template_options(correct_answer, template.question_type)
            
            return QuizQuestion(
                question_id=f"q_{random.randint(1000, 9999)}",
                question=question_text,
                correct_answer=correct_answer,
                options=options,
                explanation=self._generate_template_explanation(template, parameters, correct_answer),
                difficulty=template.difficulty,
                topic=template.topic,
                question_type=template.question_type,
                shape_type=template.shape_type,
                parameters=parameters,
                geometric_constraints=template.constraints,
                metric_units={'length': 'cm', 'area': 'cm²'},
                conversion_required=bool(template.conversion_types),
                reasoning_required=template.reasoning_required,
                south_african_context=template.south_african_context,
                curriculum_alignments=[template.topic],
                template_id=template.template_id
            )
            
        except Exception as e:
            raise ValueError(f"Error generating template-based question: {str(e)}")
    
    def _get_shape_key(self, shape_type: ShapeType) -> str:
        """Convert ShapeType to template system key"""
        if not shape_type:
            return 'triangles'
        
        shape_value = shape_type.value
        if shape_value.startswith('triangle'):
            return 'triangles'
        elif shape_value in ['square', 'rectangle', 'rhombus', 'parallelogram', 'kite', 'trapezium']:
            return 'quadrilaterals'
        elif shape_value.startswith('circle'):
            return 'circles'
        elif 'angle' in shape_value:
            return 'angles'
        elif shape_value == 'cube':
            return 'cubes'
        elif shape_value == 'rectangular_prism':
            return 'rectangular_prisms'
        else:
            return 'triangles'  # Default fallback
    
    def _generate_template_parameters(self, template: QuestionTemplate) -> Dict[str, Any]:
        """Generate parameters for a template"""
        parameters = {}
        for param, (min_val, max_val) in template.parameter_ranges.items():
            if isinstance(min_val, int) and isinstance(max_val, int):
                parameters[param] = random.randint(min_val, max_val)
            else:
                parameters[param] = round(random.uniform(min_val, max_val), 1)
        return parameters
    
    def _calculate_template_answer(self, template: QuestionTemplate, parameters: Dict[str, Any]) -> str:
        """Calculate correct answer for template-based question"""
        if template.question_type == QuestionType.AREA_CALCULATION:
            if 'base' in parameters and 'height' in parameters:
                area = 0.5 * parameters['base'] * parameters['height']
                return f"{round(area, 1)} cm²"
            elif 'radius' in parameters:
                area = 3.14159 * parameters['radius'] ** 2
                return f"{round(area, 1)} cm²"
            elif 'length' in parameters and 'width' in parameters:
                area = parameters['length'] * parameters['width']
                return f"{round(area, 1)} cm²"
        
        elif template.question_type == QuestionType.PERIMETER_CALCULATION:
            if 'a' in parameters and 'b' in parameters and 'c' in parameters:
                perimeter = parameters['a'] + parameters['b'] + parameters['c']
                return f"{round(perimeter, 1)} cm"
            elif 'side' in parameters and 'base' in parameters:
                perimeter = 2 * parameters['side'] + parameters['base']
                return f"{round(perimeter, 1)} cm"
            elif 'length' in parameters and 'width' in parameters:
                perimeter = 2 * (parameters['length'] + parameters['width'])
                return f"{round(perimeter, 1)} cm"
            elif 'radius' in parameters:
                circumference = 2 * 3.14159 * parameters['radius']
                return f"{round(circumference, 1)} cm"
        
        elif template.question_type == QuestionType.UNIT_CONVERSION:
            if 'value' in parameters:
                if 'cm_mm' in template.conversion_types:
                    return f"{parameters['value'] * 10} mm"
                elif 'mm_cm' in template.conversion_types:
                    return f"{parameters['value'] / 10} cm"
                elif 'cm_m' in template.conversion_types:
                    return f"{parameters['value'] / 100} m"
        
        elif template.question_type == QuestionType.SHAPE_CLASSIFICATION:
            # Handle similarity and congruency questions
            if 'similarity' in template.template_id or 'congruency' in template.template_id:
                return self._calculate_similarity_congruency_answer(template, parameters)
            
            # Classify triangle based on side lengths
            if 'a' in parameters and 'b' in parameters and 'c' in parameters:
                a, b, c = parameters['a'], parameters['b'], parameters['c']
                
                # Check if it's equilateral (all sides equal)
                if a == b == c:
                    return "Equilateral triangle"
                
                # Check if it's isosceles (two sides equal)
                elif a == b or b == c or a == c:
                    return "Isosceles triangle"
                
                # Otherwise it's scalene
                else:
                    return "Scalene triangle"
        
        return "Answer not calculated"
    
    def _calculate_similarity_congruency_answer(self, template: QuestionTemplate, parameters: Dict[str, Any]) -> str:
        """Calculate answer for similarity and congruency questions"""
        if 'similarity' in template.template_id:
            # Check if shapes are similar (proportional sides)
            if 'a1' in parameters and 'a2' in parameters:
                # Triangle similarity check
                a1, b1, c1 = parameters.get('a1', 0), parameters.get('b1', 0), parameters.get('c1', 0)
                a2, b2, c2 = parameters.get('a2', 0), parameters.get('b2', 0), parameters.get('c2', 0)
                
                if a1 > 0 and a2 > 0 and b1 > 0 and b2 > 0 and c1 > 0 and c2 > 0:
                    ratio1 = a2 / a1 if a1 > 0 else 0
                    ratio2 = b2 / b1 if b1 > 0 else 0
                    ratio3 = c2 / c1 if c1 > 0 else 0
                    
                    # Check if ratios are approximately equal (within 0.1 tolerance)
                    if abs(ratio1 - ratio2) < 0.1 and abs(ratio2 - ratio3) < 0.1 and abs(ratio1 - ratio3) < 0.1:
                        return "Yes, the shapes are similar"
                    else:
                        return "No, the shapes are not similar"
            
            elif 'l1' in parameters and 'l2' in parameters:
                # Rectangle similarity check
                l1, w1 = parameters.get('l1', 0), parameters.get('w1', 0)
                l2, w2 = parameters.get('l2', 0), parameters.get('w2', 0)
                
                if l1 > 0 and l2 > 0 and w1 > 0 and w2 > 0:
                    ratio_l = l2 / l1
                    ratio_w = w2 / w1
                    
                    if abs(ratio_l - ratio_w) < 0.1:
                        return "Yes, the shapes are similar"
                    else:
                        return "No, the shapes are not similar"
            
            elif 'r1' in parameters and 'r2' in parameters:
                # Circle similarity check (circles are always similar)
                return "Yes, the shapes are similar"
            
            return "Yes, the shapes are similar"  # Default for similarity
        
        elif 'congruency' in template.template_id:
            # Check if shapes are congruent (equal sides)
            if 'a1' in parameters and 'a2' in parameters:
                # Triangle congruency check
                a1, b1, c1 = parameters.get('a1', 0), parameters.get('b1', 0), parameters.get('c1', 0)
                a2, b2, c2 = parameters.get('a2', 0), parameters.get('b2', 0), parameters.get('c2', 0)
                
                if a1 > 0 and a2 > 0 and b1 > 0 and b2 > 0 and c1 > 0 and c2 > 0:
                    # Check if corresponding sides are equal
                    if abs(a1 - a2) < 0.1 and abs(b1 - b2) < 0.1 and abs(c1 - c2) < 0.1:
                        return "Yes, the shapes are congruent"
                    else:
                        return "No, the shapes are not congruent"
            
            elif 's1' in parameters and 's2' in parameters:
                # Square congruency check
                s1, s2 = parameters.get('s1', 0), parameters.get('s2', 0)
                
                if abs(s1 - s2) < 0.1:
                    return "Yes, the shapes are congruent"
                else:
                    return "No, the shapes are not congruent"
            
            elif 'r1' in parameters and 'r2' in parameters:
                # Circle congruency check
                r1, r2 = parameters.get('r1', 0), parameters.get('r2', 0)
                
                if abs(r1 - r2) < 0.1:
                    return "Yes, the shapes are congruent"
                else:
                    return "No, the shapes are not congruent"
            
            return "Yes, the shapes are congruent"  # Default for congruency
        
        return "Answer not calculated"
    
    def _generate_template_options(self, correct_answer: str, question_type: QuestionType) -> List[str]:
        """Generate options for template-based question"""
        options = [correct_answer]
        
        # Generate 3 incorrect options
        for _ in range(3):
            if question_type == QuestionType.AREA_CALCULATION:
                # Generate options with slight variations
                base_value = float(correct_answer.split()[0])
                variation = random.uniform(0.8, 1.2)
                wrong_answer = f"{round(base_value * variation, 1)} cm²"
                if wrong_answer not in options:
                    options.append(wrong_answer)
            elif question_type == QuestionType.PERIMETER_CALCULATION:
                base_value = float(correct_answer.split()[0])
                variation = random.uniform(0.9, 1.1)
                wrong_answer = f"{round(base_value * variation, 1)} cm"
                if wrong_answer not in options:
                    options.append(wrong_answer)
            elif question_type == QuestionType.SHAPE_CLASSIFICATION:
                # Check if this is a similarity/congruency question
                if "similar" in correct_answer.lower() or "congruent" in correct_answer.lower():
                    # Similarity/congruency options
                    similarity_options = [
                        "Yes, the shapes are similar",
                        "No, the shapes are not similar",
                        "Yes, the shapes are congruent", 
                        "No, the shapes are not congruent"
                    ]
                    # Remove the correct answer from available options
                    available_options = [opt for opt in similarity_options if opt != correct_answer]
                    wrong_answer = random.choice(available_options)
                    if wrong_answer not in options:
                        options.append(wrong_answer)
                else:
                    # Generate proper triangle classification options
                    triangle_types = [
                        "Equilateral triangle", "Isosceles triangle", "Scalene triangle",
                        "Right triangle", "Acute triangle", "Obtuse triangle"
                    ]
                    # Remove the correct answer from available options
                    available_types = [t for t in triangle_types if t != correct_answer]
                    wrong_answer = random.choice(available_types)
                    if wrong_answer not in options:
                        options.append(wrong_answer)
            else:
                # Generic wrong options
                wrong_answer = f"Option {len(options)}"
                if wrong_answer not in options:
                    options.append(wrong_answer)
        
        # Ensure we have exactly 4 options
        while len(options) < 4:
            if question_type == QuestionType.SHAPE_CLASSIFICATION:
                # Check if this is a similarity/congruency question
                if any("similar" in opt.lower() or "congruent" in opt.lower() for opt in options):
                    # Add more similarity/congruency options if needed
                    similarity_options = [
                        "Yes, the shapes are similar",
                        "No, the shapes are not similar",
                        "Yes, the shapes are congruent", 
                        "No, the shapes are not congruent"
                    ]
                    available_options = [opt for opt in similarity_options if opt not in options]
                    if available_options:
                        options.append(random.choice(available_options))
                    else:
                        options.append(f"Option {len(options) + 1}")
                else:
                    # Add more triangle types if needed
                    triangle_types = [
                        "Equilateral triangle", "Isosceles triangle", "Scalene triangle",
                        "Right triangle", "Acute triangle", "Obtuse triangle"
                    ]
                    available_types = [t for t in triangle_types if t not in options]
                    if available_types:
                        options.append(random.choice(available_types))
                    else:
                        options.append(f"Option {len(options) + 1}")
            else:
                options.append(f"Option {len(options) + 1}")
        
        random.shuffle(options)
        return options
    
    def _generate_template_explanation(self, template: QuestionTemplate, parameters: Dict[str, Any], correct_answer: str) -> str:
        """Generate explanation for template-based question"""
        if template.question_type == QuestionType.AREA_CALCULATION:
            if 'base' in parameters and 'height' in parameters:
                return f"Area = ½ × base × height = ½ × {parameters['base']} × {parameters['height']} = {correct_answer}"
            elif 'radius' in parameters:
                return f"Area = π × radius² = π × {parameters['radius']}² = {correct_answer}"
            elif 'length' in parameters and 'width' in parameters:
                return f"Area = length × width = {parameters['length']} × {parameters['width']} = {correct_answer}"
        
        elif template.question_type == QuestionType.PERIMETER_CALCULATION:
            if 'a' in parameters and 'b' in parameters and 'c' in parameters:
                return f"Perimeter = a + b + c = {parameters['a']} + {parameters['b']} + {parameters['c']} = {correct_answer}"
            elif 'side' in parameters and 'base' in parameters:
                return f"Perimeter = 2 × side + base = 2 × {parameters['side']} + {parameters['base']} = {correct_answer}"
            elif 'length' in parameters and 'width' in parameters:
                return f"Perimeter = 2 × (length + width) = 2 × ({parameters['length']} + {parameters['width']}) = {correct_answer}"
            elif 'radius' in parameters:
                return f"Circumference = 2π × radius = 2π × {parameters['radius']} = {correct_answer}"
        
        return f"The correct answer is {correct_answer}."
    
    def get_available_templates(self, topic: str, difficulty: DifficultyLevel) -> List[QuestionTemplate]:
        """Get available templates for a topic and difficulty"""
        return [
            t for t in self.templates
            if t.topic == topic and t.difficulty == difficulty
        ]


class QuizGenerationService:
    """Main service for quiz generation with dual fail-safe system"""
    
    def __init__(self):
        self.constraint_generator = ConstraintBasedGenerator()
        self.template_generator = TemplateBasedGenerator()
    
    def generate_questions(self, request: QuizGenerationRequest) -> QuizGenerationResponse:
        """Generate quiz questions using dual fail-safe system"""
        questions = []
        generation_method = "constraint_based"
        
        try:
            # Try constraint-based generation first
            for _ in range(request.count):
                question = self.constraint_generator.generate_question(request)
                questions.append(question)
            
        except Exception as e:
            print(f"Constraint-based generation failed: {e}")
            import traceback
            traceback.print_exc()
            
            try:
                # Fallback to template-based generation
                generation_method = "template_based"
                questions = []
                
                for _ in range(request.count):
                    question = self.template_generator.generate_question(request)
                    questions.append(question)
                    
            except Exception as e2:
                print(f"Template-based generation failed: {e2}")
                
                # Emergency fallback
                generation_method = "fallback"
                questions = [self._generate_emergency_question(request)]
        
        # Convert request to JSON-serializable format for metadata
        request_metadata = {
            'topic': request.topic,
            'difficulty': request.difficulty.value,
            'question_type': request.question_type.value,
            'shape_type': request.shape_type.value if request.shape_type else None,
            'count': request.count,
            'include_diagram': request.include_diagram,
            'south_african_context': request.south_african_context,
            'conversion_required': request.conversion_required,
            'reasoning_required': request.reasoning_required
        }
        
        return QuizGenerationResponse(
            success=len(questions) > 0,
            questions=questions,
            generation_method=generation_method,
            metadata={'request': request_metadata}
        )
    
    def _generate_emergency_question(self, request: QuizGenerationRequest) -> QuizQuestion:
        """Generate emergency fallback question"""
        return QuizQuestion(
            question="What is the area of a triangle with base 3 cm and height 4 cm?",
            options=["6.0 cm²", "7.0 cm²", "5.0 cm²", "8.0 cm²"],
            correct_answer="6.0 cm²",
            explanation="Area = ½ × base × height = ½ × 3 × 4 = 6.0 cm²",
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={'base': 3, 'height': 4},
            geometric_constraints=[],
            curriculum_alignments=['Calculations involving 2D Shapes'],
            metric_units={'length': 'cm', 'area': 'cm²'},
            south_african_context=True,
            conversion_required=False,
            question_id="emergency_001"
        )
    
    def _generate_similarity_congruency_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate similarity and congruency questions"""
        topic = getattr(request, 'topic', 'similarity')
        print(f"DEBUG: _generate_similarity_congruency_question called with topic={topic}")
        
        if topic == 'similarity':
            print("DEBUG: Calling _generate_similarity_question")
            return self._generate_similarity_question(request, parameters)
        elif topic == 'congruency':
            print("DEBUG: Calling _generate_congruency_question")
            return self._generate_congruency_question(request, parameters)
        else:  # similarity_congruency
            print("DEBUG: Calling _generate_combined_similarity_congruency_question")
            return self._generate_combined_similarity_congruency_question(request, parameters)
    
    def _generate_similarity_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate triangle similarity question"""
        # Use existing triangle parameters or generate new ones
        if 'sides' in parameters:
            base_sides = parameters['sides']
        else:
            base_sides = [random.randint(3, 6), random.randint(4, 8), random.randint(5, 10)]
        
        scale_factor = random.uniform(1.5, 3.0)
        scaled_sides = [round(side * scale_factor, 1) for side in base_sides]
        
        question = f"Triangle A has sides {base_sides[0]} cm, {base_sides[1]} cm, and {base_sides[2]} cm. Triangle B has sides {scaled_sides[0]} cm, {scaled_sides[1]} cm, and {scaled_sides[2]} cm. Are these triangles similar?"
        
        options = [
            "Yes, the shapes are similar",
            "No, the shapes are not similar",
            "Yes, the shapes are congruent",
            "No, the shapes are not congruent"
        ]
        
        correct_answer = "Yes, the shapes are similar"
        explanation = f"Triangle A and Triangle B are similar because their corresponding sides are proportional. The ratio of corresponding sides is {scale_factor:.1f}, which means Triangle B is {scale_factor:.1f} times larger than Triangle A."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={
                'triangle_a_sides': base_sides,
                'triangle_b_sides': scaled_sides,
                'scale_factor': scale_factor,
                'similarity_type': 'proportional_sides'
            },
            geometric_constraints=['triangle_inequality', 'similarity_ratio'],
            metric_units={'length': 'cm'},
            conversion_required=False,
            reasoning_required=request.difficulty.value in ['medium', 'hard'],
            south_african_context=True,
            curriculum_alignments=['Properties of 2D Shapes'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )
    
    def _generate_congruency_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate triangle congruency question"""
        # Use existing triangle parameters or generate new ones
        if 'sides' in parameters:
            sides = parameters['sides']
        else:
            sides = [random.randint(3, 6), random.randint(4, 8), random.randint(5, 10)]
        
        question = f"Triangle A has sides {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. Triangle B has sides {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. Are these triangles congruent?"
        
        options = [
            "Yes, the shapes are similar",
            "No, the shapes are not similar",
            "Yes, the shapes are congruent",
            "No, the shapes are not congruent"
        ]
        
        correct_answer = "Yes, the shapes are congruent"
        explanation = f"Triangle A and Triangle B are congruent because all their corresponding sides are equal. Both triangles have sides of {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={
                'triangle_a_sides': sides,
                'triangle_b_sides': sides,
                'congruency_type': 'equal_sides'
            },
            geometric_constraints=['triangle_inequality', 'congruency_check'],
            metric_units={'length': 'cm'},
            conversion_required=False,
            reasoning_required=request.difficulty.value in ['medium', 'hard'],
            south_african_context=True,
            curriculum_alignments=['Properties of 2D Shapes'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )
    
    def _generate_combined_similarity_congruency_question(self, request: QuizGenerationRequest, parameters: Dict[str, Any]) -> QuizQuestion:
        """Generate combined similarity and congruency question"""
        # Use existing triangle parameters or generate new ones
        if 'sides' in parameters:
            base_sides = parameters['sides']
        else:
            base_sides = [random.randint(4, 8), random.randint(5, 10), random.randint(6, 12)]
        scale_factor = random.uniform(1.5, 2.5)
        similar_sides = [round(side * scale_factor, 1) for side in base_sides]
        
        question = f"Compare three triangles: Triangle A ({base_sides[0]} cm, {base_sides[1]} cm, {base_sides[2]} cm), Triangle B ({similar_sides[0]} cm, {similar_sides[1]} cm, {similar_sides[2]} cm), and Triangle C ({base_sides[0]} cm, {base_sides[1]} cm, {base_sides[2]} cm). Which triangles are similar? Which are congruent?"
        
        options = [
            "A and B are similar, A and C are congruent",
            "A and C are similar, B and C are congruent", 
            "All triangles are similar",
            "No triangles are similar or congruent"
        ]
        
        correct_answer = "A and B are similar, A and C are congruent"
        explanation = f"Triangle A and Triangle B are similar because their sides are proportional (ratio {scale_factor:.1f}). Triangle A and Triangle C are congruent because all their corresponding sides are equal."
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            topic=request.topic,
            difficulty=request.difficulty,
            question_type=request.question_type,
            shape_type=request.shape_type,
            parameters={
                'triangle_a_sides': base_sides,
                'triangle_b_sides': similar_sides,
                'triangle_c_sides': base_sides,
                'scale_factor': scale_factor,
                'comparison_type': 'multiple_triangles'
            },
            geometric_constraints=['triangle_inequality', 'similarity_ratio', 'congruency_check'],
            metric_units={'length': 'cm'},
            conversion_required=False,
            reasoning_required=True,
            south_african_context=True,
            curriculum_alignments=['Properties of 2D Shapes'],
            question_id=f"q_{random.randint(1000, 9999)}"
        )
