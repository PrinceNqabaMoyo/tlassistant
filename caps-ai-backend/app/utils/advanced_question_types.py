"""
Advanced Question Types Generator
Implements composite areas, classification, similarity, congruency, and other advanced question types
"""

from typing import Dict, List, Any, Tuple, Optional
from enum import Enum
import random
import math
from .quiz_models import DifficultyLevel, QuestionType, ShapeType


class AdvancedQuestionType(Enum):
    """Advanced question types for enhanced geometry learning"""
    COMPOSITE_AREA = "composite_area"
    SHADED_REGION = "shaded_region"
    QUADRILATERAL_CLASSIFICATION = "quadrilateral_classification"
    TRIANGLE_CLASSIFICATION = "triangle_classification"
    SIMILARITY_COMPARISON = "similarity_comparison"
    CONGRUENCY_COMPARISON = "congruency_comparison"
    EQUATION_SOLVING = "equation_solving"
    TRIANGLE_HEIGHT = "triangle_height"
    ANGLE_CALCULATION = "angle_calculation"
    PERIMETER_OPTIMIZATION = "perimeter_optimization"


class AdvancedQuestionGenerator:
    """
    Generates advanced question types for enhanced geometry learning
    Implements Phase 3 advanced question types from the plan
    """
    
    def __init__(self):
        self.question_templates = self._initialize_templates()
    
    def _initialize_templates(self) -> Dict[AdvancedQuestionType, List[str]]:
        """Initialize templates for advanced question types"""
        return {
            AdvancedQuestionType.COMPOSITE_AREA: [
                "A rectangular garden {length} m × {width} m has a triangular flower bed {base} m × {height} m. What is the area of the remaining grass?",
                "A square patio {side} m × {side} m has a circular fountain with radius {radius} m. What is the area of the patio not covered by the fountain?",
                "A rectangular room {length} m × {width} m has a triangular corner cut out {base} m × {height} m. What is the remaining floor area?",
            ],
            AdvancedQuestionType.SHADED_REGION: [
                "A square {side} m × {side} m has a circle inscribed with radius {radius} m. What is the area of the shaded region?",
                "A rectangle {length} m × {width} m has a triangle cut out from one corner {base} m × {height} m. What is the area of the shaded region?",
                "A circle with radius {radius} m has a square inscribed with side {side} m. What is the area of the shaded region?",
            ],
            AdvancedQuestionType.QUADRILATERAL_CLASSIFICATION: [
                "Classify this quadrilateral with sides {a} cm, {b} cm, {c} cm, {d} cm and angles {angle1}°, {angle2}°, {angle3}°, {angle4}°.",
                "A quadrilateral has opposite sides equal: {a} cm = {c} cm and {b} cm = {d} cm. All angles are {angle}°. What type is it?",
                "A quadrilateral has all sides equal ({side} cm) and all angles equal ({angle}°). What type is it?",
            ],
            AdvancedQuestionType.TRIANGLE_CLASSIFICATION: [
                "Classify this triangle with sides {a} cm, {b} cm, {c} cm and angles {angle1}°, {angle2}°, {angle3}°.",
                "A triangle has sides {a} cm, {b} cm, {c} cm. What type of triangle is it?",
                "A triangle has angles {angle1}°, {angle2}°, {angle3}°. What type of triangle is it?",
            ],
            AdvancedQuestionType.SIMILARITY_COMPARISON: [
                "Triangle A has sides {a1} cm, {b1} cm, {c1} cm. Triangle B has sides {a2} cm, {b2} cm, {c2} cm. Are they similar?",
                "Rectangle A is {l1} cm × {w1} cm. Rectangle B is {l2} cm × {w2} cm. Are they similar?",
                "Circle A has radius {r1} cm. Circle B has radius {r2} cm. Are they similar?",
            ],
            AdvancedQuestionType.CONGRUENCY_COMPARISON: [
                "Triangle A has sides {a1} cm, {b1} cm, {c1} cm. Triangle B has sides {a2} cm, {b2} cm, {c2} cm. Are they congruent?",
                "Rectangle A is {l1} cm × {w1} cm. Rectangle B is {l2} cm × {w2} cm. Are they congruent?",
                "Circle A has radius {r1} cm. Circle B has radius {r2} cm. Are they congruent?",
            ],
            AdvancedQuestionType.EQUATION_SOLVING: [
                "A triangle has area {area} cm² and base {base} cm. What is its height?",
                "A rectangle has area {area} cm² and length {length} cm. What is its width?",
                "A circle has area {area} cm². What is its radius?",
            ],
            AdvancedQuestionType.TRIANGLE_HEIGHT: [
                "A triangle has base {base} cm and area {area} cm². What is its height?",
                "A triangle has height {height} cm and area {area} cm². What is its base?",
                "A triangle has base {base} cm and height {height} cm. What is its area?",
            ],
            AdvancedQuestionType.ANGLE_CALCULATION: [
                "In a triangle, two angles are {angle1}° and {angle2}°. What is the third angle?",
                "In a quadrilateral, three angles are {angle1}°, {angle2}°, and {angle3}°. What is the fourth angle?",
                "In a pentagon, four angles are {angle1}°, {angle2}°, {angle3}°, and {angle4}°. What is the fifth angle?",
            ],
            AdvancedQuestionType.PERIMETER_OPTIMIZATION: [
                "A rectangle has area {area} cm². What are the dimensions that give the minimum perimeter?",
                "A triangle has area {area} cm². What are the dimensions that give the minimum perimeter?",
                "A square has the same area as a rectangle {length} cm × {width} cm. Which has the smaller perimeter?",
            ],
        }
    
    def generate_composite_area_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate a composite area calculation question with South African contexts"""
        contexts = self._get_south_african_contexts()
        context = random.choice(contexts)
        
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_composite_area(context)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_composite_area(context)
        else:  # HARD
            return self._generate_hard_composite_area(context)
    
    def _get_south_african_contexts(self) -> List[Dict[str, str]]:
        """Get South African real-world contexts for composite area questions"""
        return [
            {
                'location': 'school playground',
                'description': 'A school playground in Johannesburg',
                'shapes': ['rectangle', 'triangle', 'circle'],
                'activities': ['sports field', 'garden', 'fountain', 'seating area']
            },
            {
                'location': 'township house',
                'description': 'A house in Soweto township',
                'shapes': ['rectangle', 'triangle', 'circle'],
                'activities': ['yard', 'garden', 'patio', 'braai area']
            },
            {
                'location': 'shopping mall',
                'description': 'A shopping mall in Cape Town',
                'shapes': ['rectangle', 'triangle', 'circle'],
                'activities': ['food court', 'fountain', 'seating', 'garden']
            },
            {
                'location': 'farm',
                'description': 'A farm in the Free State',
                'shapes': ['rectangle', 'triangle', 'circle'],
                'activities': ['crop field', 'water tank', 'silo', 'barn']
            },
            {
                'location': 'beachfront',
                'description': 'A beachfront area in Durban',
                'shapes': ['rectangle', 'triangle', 'circle'],
                'activities': ['promenade', 'garden', 'fountain', 'seating']
            }
        ]
    
    def _generate_easy_composite_area(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate easy composite area question"""
        # Rectangle with triangular cutout
        length = random.uniform(8, 12)
        width = random.uniform(6, 10)
        base = random.uniform(2, 4)
        height = random.uniform(2, 4)
        
        rect_area = length * width
        tri_area = 0.5 * base * height
        remaining_area = rect_area - tri_area
        
        question = f"A rectangular {context['activities'][0]} {length:.1f} m × {width:.1f} m at a {context['location']} has a triangular {context['activities'][1]} {base:.1f} m × {height:.1f} m. What is the area of the remaining space?"
        
        return {
            'question': question,
            'answer': f"{remaining_area:.1f} m²",
            'explanation': f"Rectangle area = {length:.1f} × {width:.1f} = {rect_area:.1f} m². Triangle area = ½ × {base:.1f} × {height:.1f} = {tri_area:.1f} m². Remaining area = {rect_area:.1f} - {tri_area:.1f} = {remaining_area:.1f} m²",
            'parameters': {
                'length': length, 'width': width, 'base': base, 'height': height, 
                'remaining_area': remaining_area, 'context': context['location']
            },
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_medium_composite_area(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate medium composite area question"""
        # Square with circular cutout
        side = random.uniform(10, 20)
        radius = random.uniform(2, 5)
        
        square_area = side * side
        circle_area = math.pi * radius * radius
        remaining_area = square_area - circle_area
        
        question = f"A square {context['activities'][0]} {side:.1f} m × {side:.1f} m at a {context['location']} has a circular {context['activities'][2]} with radius {radius:.1f} m. What is the area not covered by the {context['activities'][2]}?"
        
        return {
            'question': question,
            'answer': f"{remaining_area:.1f} m²",
            'explanation': f"Square area = {side:.1f} × {side:.1f} = {square_area:.1f} m². Circle area = π × {radius:.1f}² = {circle_area:.1f} m². Remaining area = {square_area:.1f} - {circle_area:.1f} = {remaining_area:.1f} m²",
            'parameters': {
                'side': side, 'radius': radius, 'remaining_area': remaining_area,
                'context': context['location']
            },
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_hard_composite_area(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate hard composite area question with multiple shapes"""
        # Complex composite shape with multiple cutouts
        length = random.uniform(15, 25)
        width = random.uniform(10, 20)
        tri_base = random.uniform(3, 6)
        tri_height = random.uniform(3, 6)
        circle_radius = random.uniform(2, 4)
        
        rect_area = length * width
        tri_area = 0.5 * tri_base * tri_height
        circle_area = math.pi * circle_radius * circle_radius
        remaining_area = rect_area - tri_area - circle_area
        
        question = f"A rectangular {context['activities'][0]} {length:.1f} m × {width:.1f} m at a {context['location']} has a triangular {context['activities'][1]} {tri_base:.1f} m × {tri_height:.1f} m and a circular {context['activities'][2]} with radius {circle_radius:.1f} m. What is the remaining area?"
        
        return {
            'question': question,
            'answer': f"{remaining_area:.1f} m²",
            'explanation': f"Rectangle area = {length:.1f} × {width:.1f} = {rect_area:.1f} m². Triangle area = ½ × {tri_base:.1f} × {tri_height:.1f} = {tri_area:.1f} m². Circle area = π × {circle_radius:.1f}² = {circle_area:.1f} m². Remaining area = {rect_area:.1f} - {tri_area:.1f} - {circle_area:.1f} = {remaining_area:.1f} m²",
            'parameters': {
                'length': length, 'width': width, 'tri_base': tri_base, 'tri_height': tri_height, 
                'circle_radius': circle_radius, 'remaining_area': remaining_area,
                'context': context['location']
            },
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def generate_shaded_region_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate a shaded region calculation question"""
        contexts = self._get_south_african_contexts()
        context = random.choice(contexts)
        
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_shaded_region(context)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_shaded_region(context)
        else:  # HARD
            return self._generate_hard_shaded_region(context)
    
    def _generate_easy_shaded_region(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate easy shaded region question"""
        # Square with inscribed circle
        side = random.uniform(8, 12)
        radius = side / 2  # Circle inscribed in square
        
        square_area = side * side
        circle_area = math.pi * radius * radius
        shaded_area = square_area - circle_area
        
        question = f"A square {context['activities'][0]} {side:.1f} m × {side:.1f} m at a {context['location']} has a circular {context['activities'][2]} inscribed with radius {radius:.1f} m. What is the area of the shaded region?"
        
        return {
            'question': question,
            'answer': f"{shaded_area:.1f} m²",
            'explanation': f"Square area = {side:.1f} × {side:.1f} = {square_area:.1f} m². Circle area = π × {radius:.1f}² = {circle_area:.1f} m². Shaded area = {square_area:.1f} - {circle_area:.1f} = {shaded_area:.1f} m²",
            'parameters': {
                'side': side, 'radius': radius, 'shaded_area': shaded_area,
                'context': context['location']
            },
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_medium_shaded_region(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate medium shaded region question"""
        # Rectangle with triangular cutout
        length = random.uniform(10, 16)
        width = random.uniform(8, 12)
        base = random.uniform(3, 6)
        height = random.uniform(3, 6)
        
        rect_area = length * width
        tri_area = 0.5 * base * height
        shaded_area = rect_area - tri_area
        
        question = f"A rectangular {context['activities'][0]} {length:.1f} m × {width:.1f} m at a {context['location']} has a triangular {context['activities'][1]} cut out from one corner {base:.1f} m × {height:.1f} m. What is the area of the shaded region?"
        
        return {
            'question': question,
            'answer': f"{shaded_area:.1f} m²",
            'explanation': f"Rectangle area = {length:.1f} × {width:.1f} = {rect_area:.1f} m². Triangle area = ½ × {base:.1f} × {height:.1f} = {tri_area:.1f} m². Shaded area = {rect_area:.1f} - {tri_area:.1f} = {shaded_area:.1f} m²",
            'parameters': {
                'length': length, 'width': width, 'base': base, 'height': height, 
                'shaded_area': shaded_area, 'context': context['location']
            },
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_hard_shaded_region(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate hard shaded region question"""
        # Circle with inscribed square
        radius = random.uniform(6, 12)
        side = radius * math.sqrt(2)  # Square inscribed in circle
        
        circle_area = math.pi * radius * radius
        square_area = side * side
        shaded_area = circle_area - square_area
        
        question = f"A circular {context['activities'][2]} with radius {radius:.1f} m at a {context['location']} has a square {context['activities'][0]} inscribed with side {side:.1f} m. What is the area of the shaded region?"
        
        return {
            'question': question,
            'answer': f"{shaded_area:.1f} m²",
            'explanation': f"Circle area = π × {radius:.1f}² = {circle_area:.1f} m². Square area = {side:.1f} × {side:.1f} = {square_area:.1f} m². Shaded area = {circle_area:.1f} - {square_area:.1f} = {shaded_area:.1f} m²",
            'parameters': {
                'radius': radius, 'side': side, 'shaded_area': shaded_area,
                'context': context['location']
            },
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def generate_classification_question(self, shape_type: str, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate a shape classification question with South African contexts"""
        contexts = self._get_south_african_contexts()
        context = random.choice(contexts)
        
        if shape_type == 'quadrilateral':
            return self._generate_quadrilateral_classification(context, difficulty)
        elif shape_type == 'triangle':
            return self._generate_triangle_classification(context, difficulty)
        else:
            return self._generate_general_classification(context, difficulty)
    
    def _generate_quadrilateral_classification(self, context: Dict[str, str], difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate quadrilateral classification question with South African context"""
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_quadrilateral_classification(context)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_quadrilateral_classification(context)
        else:  # HARD
            return self._generate_hard_quadrilateral_classification(context)
    
    def _generate_easy_quadrilateral_classification(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate easy quadrilateral classification question"""
        # Square
        side = random.uniform(3, 8)
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a quadrilateral with all sides equal ({side:.1f} cm) and all angles equal (90°). What type of quadrilateral is it?"
        
        return {
            'question': question,
            'answer': 'Square',
            'explanation': 'A quadrilateral with all sides equal and all angles equal (90°) is a square.',
            'parameters': {'side': side, 'type': 'square', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_medium_quadrilateral_classification(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate medium quadrilateral classification question"""
        # Rectangle
        length = random.uniform(4, 10)
        width = random.uniform(3, 8)
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a quadrilateral with opposite sides equal: {length:.1f} cm = {length:.1f} cm and {width:.1f} cm = {width:.1f} cm. All angles are 90°. What type of quadrilateral is it?"
        
        return {
            'question': question,
            'answer': 'Rectangle',
            'explanation': 'A quadrilateral with opposite sides equal and all angles equal (90°) is a rectangle.',
            'parameters': {'length': length, 'width': width, 'type': 'rectangle', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_hard_quadrilateral_classification(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate hard quadrilateral classification question"""
        # Rhombus
        side = random.uniform(4, 10)
        angle1 = random.uniform(60, 120)
        angle2 = 180 - angle1
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a quadrilateral with all sides equal ({side:.1f} cm) and opposite angles equal ({angle1:.1f}° and {angle2:.1f}°). What type of quadrilateral is it?"
        
        return {
            'question': question,
            'answer': 'Rhombus',
            'explanation': 'A quadrilateral with all sides equal and opposite angles equal is a rhombus.',
            'parameters': {'side': side, 'angle1': angle1, 'angle2': angle2, 'type': 'rhombus', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_triangle_classification(self, context: Dict[str, str], difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate triangle classification question with South African context"""
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_triangle_classification(context)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_triangle_classification(context)
        else:  # HARD
            return self._generate_hard_triangle_classification(context)
    
    def _generate_easy_triangle_classification(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate easy triangle classification question"""
        # Equilateral triangle
        side = random.uniform(3, 8)
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a triangle with all sides equal ({side:.1f} cm) and all angles equal (60°). What type of triangle is it?"
        
        return {
            'question': question,
            'answer': 'Equilateral triangle',
            'explanation': 'A triangle with all sides equal and all angles equal (60°) is an equilateral triangle.',
            'parameters': {'side': side, 'type': 'equilateral', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_medium_triangle_classification(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate medium triangle classification question"""
        # Isosceles triangle
        equal_side = random.uniform(4, 8)
        base = random.uniform(3, 7)
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a triangle with two sides equal ({equal_side:.1f} cm) and one different side ({base:.1f} cm). What type of triangle is it?"
        
        return {
            'question': question,
            'answer': 'Isosceles triangle',
            'explanation': 'A triangle with two sides equal is an isosceles triangle.',
            'parameters': {'equal_side': equal_side, 'base': base, 'type': 'isosceles', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_hard_triangle_classification(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate hard triangle classification question"""
        # Scalene triangle
        a = random.uniform(3, 8)
        b = random.uniform(4, 9)
        c = random.uniform(5, 10)
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a triangle with sides {a:.1f} cm, {b:.1f} cm, and {c:.1f} cm. What type of triangle is it?"
        
        return {
            'question': question,
            'answer': 'Scalene triangle',
            'explanation': 'A triangle with all sides different lengths is a scalene triangle.',
            'parameters': {'a': a, 'b': b, 'c': c, 'type': 'scalene', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_general_classification(self, context: Dict[str, str], difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate general classification question"""
        # Fallback for other shape types
        return {
            'question': f"What type of shape is this?",
            'answer': 'Unknown',
            'explanation': 'This is a general classification question.',
            'parameters': {'type': 'unknown', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def generate_quadrilateral_sorting_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate a quadrilateral sorting/grouping question"""
        contexts = self._get_south_african_contexts()
        context = random.choice(contexts)
        
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_quadrilateral_sorting(context)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_quadrilateral_sorting(context)
        else:  # HARD
            return self._generate_hard_quadrilateral_sorting(context)
    
    def _generate_easy_quadrilateral_sorting(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate easy quadrilateral sorting question"""
        shapes = [
            {'name': 'Square', 'sides': 'all equal', 'angles': 'all 90°'},
            {'name': 'Rectangle', 'sides': 'opposite equal', 'angles': 'all 90°'},
            {'name': 'Rhombus', 'sides': 'all equal', 'angles': 'opposite equal'},
            {'name': 'Parallelogram', 'sides': 'opposite equal', 'angles': 'opposite equal'}
        ]
        
        question = f"At a {context['location']}, you have four {context['activities'][0]} shapes. Group them by their properties: Square (all sides equal, all angles 90°), Rectangle (opposite sides equal, all angles 90°), Rhombus (all sides equal, opposite angles equal), Parallelogram (opposite sides equal, opposite angles equal). Which group does a shape with all sides equal and all angles 90° belong to?"
        
        return {
            'question': question,
            'answer': 'Square group',
            'explanation': 'A shape with all sides equal and all angles 90° is a square.',
            'parameters': {'shapes': shapes, 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_medium_quadrilateral_sorting(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate medium quadrilateral sorting question"""
        question = f"At a {context['location']}, you need to sort {context['activities'][0]} shapes into groups. You have shapes with these properties: (1) All sides equal, all angles 90°, (2) Opposite sides equal, all angles 90°, (3) All sides equal, opposite angles equal, (4) Opposite sides equal, opposite angles equal. Which two shapes belong in the same group?"
        
        return {
            'question': question,
            'answer': 'Rectangle and Parallelogram (both have opposite sides equal)',
            'explanation': 'Both rectangle and parallelogram have opposite sides equal, but rectangle has all angles 90° while parallelogram has opposite angles equal.',
            'parameters': {'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_hard_quadrilateral_sorting(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate hard quadrilateral sorting question"""
        question = f"At a {context['location']}, you have a complex {context['activities'][0]} with multiple quadrilateral shapes. Create a classification system that groups them by: (1) Side properties (all equal vs opposite equal), (2) Angle properties (all 90° vs opposite equal vs all different). How many different groups can you create?"
        
        return {
            'question': question,
            'answer': '6 different groups',
            'explanation': 'You can create 6 groups: Square (all equal sides, all 90°), Rectangle (opposite equal sides, all 90°), Rhombus (all equal sides, opposite equal angles), Parallelogram (opposite equal sides, opposite equal angles), Trapezoid (one pair parallel), and Kite (two pairs adjacent equal sides).',
            'parameters': {'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def generate_quadrilateral_properties_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate a quadrilateral properties identification question"""
        contexts = self._get_south_african_contexts()
        context = random.choice(contexts)
        
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_quadrilateral_properties(context)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_quadrilateral_properties(context)
        else:  # HARD
            return self._generate_hard_quadrilateral_properties(context)
    
    def _generate_easy_quadrilateral_properties(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate easy quadrilateral properties question"""
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a square. What are the properties of a square?"
        
        return {
            'question': question,
            'answer': 'All sides equal, all angles 90°, opposite sides parallel, diagonals equal and perpendicular',
            'explanation': 'A square has all sides equal, all angles are 90°, opposite sides are parallel, and the diagonals are equal in length and perpendicular to each other.',
            'parameters': {'shape': 'square', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_medium_quadrilateral_properties(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate medium quadrilateral properties question"""
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a rectangle. What properties does it share with a square, and what properties are different?"
        
        return {
            'question': question,
            'answer': 'Shared: opposite sides equal, all angles 90°, opposite sides parallel. Different: rectangle has different adjacent sides, square has all sides equal',
            'explanation': 'Both rectangle and square have opposite sides equal, all angles 90°, and opposite sides parallel. The difference is that a square has all sides equal while a rectangle has different adjacent sides.',
            'parameters': {'shape': 'rectangle', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def _generate_hard_quadrilateral_properties(self, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate hard quadrilateral properties question"""
        question = f"A {context['activities'][0]} at a {context['location']} has the shape of a rhombus. Compare its properties with a square and identify the key differences in side lengths and angle measures."
        
        return {
            'question': question,
            'answer': 'Rhombus: all sides equal, opposite angles equal (not 90°). Square: all sides equal, all angles 90°. Key difference: angle measures',
            'explanation': 'Both rhombus and square have all sides equal. The key difference is that a square has all angles equal to 90°, while a rhombus has opposite angles equal but not necessarily 90°.',
            'parameters': {'shape': 'rhombus', 'context': context['location']},
            'south_african_context': True,
            'real_world_context': context['location']
        }
    
    def generate_similarity_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate a similarity comparison question"""
        if difficulty == DifficultyLevel.EASY:
            # Similar triangles
            a1, b1, c1 = 3, 4, 5
            scale_factor = random.uniform(1.5, 3)
            a2, b2, c2 = a1 * scale_factor, b1 * scale_factor, c1 * scale_factor
            
            return {
                'question': f"Triangle A has sides {a1} cm, {b1} cm, {c1} cm. Triangle B has sides {a2:.1f} cm, {b2:.1f} cm, {c2:.1f} cm. Are they similar?",
                'answer': 'Yes, they are similar',
                'explanation': f'Yes, they are similar because the ratio of corresponding sides is constant: {a2/a1:.1f} = {b2/b1:.1f} = {c2/c1:.1f}',
                'parameters': {'a1': a1, 'b1': b1, 'c1': c1, 'a2': a2, 'b2': b2, 'c2': c2, 'similar': True}
            }
        
        elif difficulty == DifficultyLevel.MEDIUM:
            # Similar rectangles
            l1, w1 = 4, 6
            scale_factor = random.uniform(1.2, 2.5)
            l2, w2 = l1 * scale_factor, w1 * scale_factor
            
            return {
                'question': f"Rectangle A is {l1} cm × {w1} cm. Rectangle B is {l2:.1f} cm × {w2:.1f} cm. Are they similar?",
                'answer': 'Yes, they are similar',
                'explanation': f'Yes, they are similar because the ratio of corresponding sides is constant: {l2/l1:.1f} = {w2/w1:.1f}',
                'parameters': {'l1': l1, 'w1': w1, 'l2': l2, 'w2': w2, 'similar': True}
            }
        
        else:  # HARD
            # Non-similar shapes
            a1, b1, c1 = 3, 4, 5
            a2, b2, c2 = 6, 8, 7  # Not similar
            
            return {
                'question': f"Triangle A has sides {a1} cm, {b1} cm, {c1} cm. Triangle B has sides {a2} cm, {b2} cm, {c2} cm. Are they similar?",
                'answer': 'No, they are not similar',
                'explanation': f'No, they are not similar because the ratio of corresponding sides is not constant: {a2/a1:.1f} ≠ {b2/b1:.1f} ≠ {c2/c1:.1f}',
                'parameters': {'a1': a1, 'b1': b1, 'c1': c1, 'a2': a2, 'b2': b2, 'c2': c2, 'similar': False}
            }
    
    def generate_equation_solving_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate an equation solving question"""
        if difficulty == DifficultyLevel.EASY:
            # Triangle height
            area = random.uniform(10, 30)
            base = random.uniform(4, 10)
            height = (2 * area) / base
            
            return {
                'question': f"A triangle has area {area:.1f} cm² and base {base:.1f} cm. What is its height?",
                'answer': f"{height:.1f} cm",
                'explanation': f"Area = ½ × base × height, so height = 2 × area ÷ base = 2 × {area:.1f} ÷ {base:.1f} = {height:.1f} cm",
                'parameters': {'area': area, 'base': base, 'height': height}
            }
        
        elif difficulty == DifficultyLevel.MEDIUM:
            # Rectangle width
            area = random.uniform(20, 60)
            length = random.uniform(5, 12)
            width = area / length
            
            return {
                'question': f"A rectangle has area {area:.1f} cm² and length {length:.1f} cm. What is its width?",
                'answer': f"{width:.1f} cm",
                'explanation': f"Area = length × width, so width = area ÷ length = {area:.1f} ÷ {length:.1f} = {width:.1f} cm",
                'parameters': {'area': area, 'length': length, 'width': width}
            }
        
        else:  # HARD
            # Circle radius
            area = random.uniform(50, 200)
            radius = math.sqrt(area / math.pi)
            
            return {
                'question': f"A circle has area {area:.1f} cm². What is its radius?",
                'answer': f"{radius:.1f} cm",
                'explanation': f"Area = π × radius², so radius = √(area ÷ π) = √({area:.1f} ÷ π) = {radius:.1f} cm",
                'parameters': {'area': area, 'radius': radius}
            }
    
    def generate_angle_calculation_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate an angle calculation question"""
        if difficulty == DifficultyLevel.EASY:
            # Triangle angles
            angle1 = random.uniform(30, 60)
            angle2 = random.uniform(40, 70)
            angle3 = 180 - angle1 - angle2
            
            return {
                'question': f"In a triangle, two angles are {angle1:.1f}° and {angle2:.1f}°. What is the third angle?",
                'answer': f"{angle3:.1f}°",
                'explanation': f"The sum of angles in a triangle is 180°, so the third angle = 180° - {angle1:.1f}° - {angle2:.1f}° = {angle3:.1f}°",
                'parameters': {'angle1': angle1, 'angle2': angle2, 'angle3': angle3}
            }
        
        elif difficulty == DifficultyLevel.MEDIUM:
            # Quadrilateral angles
            angle1 = random.uniform(60, 90)
            angle2 = random.uniform(70, 100)
            angle3 = random.uniform(80, 110)
            angle4 = 360 - angle1 - angle2 - angle3
            
            return {
                'question': f"In a quadrilateral, three angles are {angle1:.1f}°, {angle2:.1f}°, and {angle3:.1f}°. What is the fourth angle?",
                'answer': f"{angle4:.1f}°",
                'explanation': f"The sum of angles in a quadrilateral is 360°, so the fourth angle = 360° - {angle1:.1f}° - {angle2:.1f}° - {angle3:.1f}° = {angle4:.1f}°",
                'parameters': {'angle1': angle1, 'angle2': angle2, 'angle3': angle3, 'angle4': angle4}
            }
        
        else:  # HARD
            # Pentagon angles
            angle1 = random.uniform(100, 120)
            angle2 = random.uniform(110, 130)
            angle3 = random.uniform(120, 140)
            angle4 = random.uniform(130, 150)
            angle5 = 540 - angle1 - angle2 - angle3 - angle4
            
            return {
                'question': f"In a pentagon, four angles are {angle1:.1f}°, {angle2:.1f}°, {angle3:.1f}°, and {angle4:.1f}°. What is the fifth angle?",
                'answer': f"{angle5:.1f}°",
                'explanation': f"The sum of angles in a pentagon is 540°, so the fifth angle = 540° - {angle1:.1f}° - {angle2:.1f}° - {angle3:.1f}° - {angle4:.1f}° = {angle5:.1f}°",
                'parameters': {'angle1': angle1, 'angle2': angle2, 'angle3': angle3, 'angle4': angle4, 'angle5': angle5}
            }
    
    def generate_similarity_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate similarity comparison questions with South African contexts"""
        contexts = self._get_south_african_contexts()
        context_data = random.choice(contexts)
        context = context_data['description']
        location = context_data['location']
        
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_similarity_question(context, location)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_similarity_question(context, location)
        else:  # HARD
            return self._generate_hard_similarity_question(context, location)
    
    def _generate_easy_similarity_question(self, context: str, location: str) -> Dict[str, Any]:
        """Generate easy similarity question"""
        # Simple triangle similarity with basic ratios
        side1_a, side1_b = random.randint(3, 8), random.randint(6, 16)
        side2_a, side2_b = random.randint(4, 10), random.randint(8, 20)
        side3_a, side3_b = random.randint(5, 12), random.randint(10, 24)
        
        # Ensure they form similar triangles (same ratio)
        ratio = side1_b / side1_a
        side2_b = int(side2_a * ratio)
        side3_b = int(side3_a * ratio)
        
        question = f"At a {location}, two {context} triangles have sides: Triangle A: {side1_a} cm, {side2_a} cm, {side3_a} cm and Triangle B: {side1_b} cm, {side2_b} cm, {side3_b} cm. Are these triangles similar?"
        
        # Calculate ratio to determine answer
        ratio_a = side1_b / side1_a
        ratio_b = side2_b / side2_a
        ratio_c = side3_b / side3_a
        
        if abs(ratio_a - ratio_b) < 0.01 and abs(ratio_b - ratio_c) < 0.01:
            answer = "Yes, they are similar"
            explanation = f"Yes, the triangles are similar because all corresponding sides have the same ratio: {side1_b}/{side1_a} = {side2_b}/{side2_a} = {side3_b}/{side3_a} = {ratio_a:.2f}"
        else:
            answer = "No, they are not similar"
            explanation = f"No, the triangles are not similar because the ratios of corresponding sides are not equal: {side1_b}/{side1_a} = {ratio_a:.2f}, {side2_b}/{side2_a} = {ratio_b:.2f}, {side3_b}/{side3_a} = {ratio_c:.2f}"
        
        return {
            'question': question,
            'answer': answer,
            'explanation': explanation,
            'parameters': {
                'triangle_a': [side1_a, side2_a, side3_a],
                'triangle_b': [side1_b, side2_b, side3_b],
                'ratio': ratio_a
            }
        }
    
    def _generate_medium_similarity_question(self, context: str, location: str) -> Dict[str, Any]:
        """Generate medium similarity question with angle considerations"""
        # Triangle similarity with angles and sides
        angle1, angle2 = random.randint(30, 60), random.randint(60, 90)
        angle3 = 180 - angle1 - angle2
        
        # Create similar triangle with different scale
        scale_factor = random.uniform(1.5, 3.0)
        side1 = random.randint(4, 10)
        side2 = random.randint(5, 12)
        side3 = random.randint(6, 15)
        
        side1_scaled = int(side1 * scale_factor)
        side2_scaled = int(side2 * scale_factor)
        side3_scaled = int(side3 * scale_factor)
        
        question = f"At a {location}, two {context} triangles have: Triangle A: sides {side1} cm, {side2} cm, {side3} cm with angles {angle1}°, {angle2}°, {angle3}°. Triangle B: sides {side1_scaled} cm, {side2_scaled} cm, {side3_scaled} cm with angles {angle1}°, {angle2}°, {angle3}°. Are they similar?"
        
        answer = "Yes, they are similar"
        explanation = f"Yes, the triangles are similar because they have equal corresponding angles ({angle1}°, {angle2}°, {angle3}°) and the ratio of corresponding sides is constant: {side1_scaled}/{side1} = {side2_scaled}/{side2} = {side3_scaled}/{side3} = {scale_factor:.2f}"
        
        return {
            'question': question,
            'answer': answer,
            'explanation': explanation,
            'parameters': {
                'triangle_a': [side1, side2, side3],
                'triangle_b': [side1_scaled, side2_scaled, side3_scaled],
                'angles': [angle1, angle2, angle3],
                'scale_factor': scale_factor
            }
        }
    
    def _generate_hard_similarity_question(self, context: str, location: str) -> Dict[str, Any]:
        """Generate hard similarity question with complex scenarios"""
        # Multiple triangles comparison
        triangle_count = random.randint(3, 4)
        triangles = []
        
        # Create one reference triangle
        base_side = random.randint(6, 12)
        scale_factors = [1.0, random.uniform(1.2, 2.0), random.uniform(2.0, 3.0)]
        if triangle_count == 4:
            scale_factors.append(random.uniform(0.8, 1.2))
        
        for i, scale in enumerate(scale_factors):
            side1 = int(base_side * scale)
            side2 = int((base_side + 2) * scale)
            side3 = int((base_side + 4) * scale)
            triangles.append([side1, side2, side3])
        
        # Make one triangle different (not similar)
        if random.random() < 0.3:  # 30% chance of non-similar triangle
            triangles[-1] = [random.randint(8, 15), random.randint(10, 18), random.randint(12, 20)]
        
        question = f"At a {location}, you have {triangle_count} {context} triangles with sides: "
        for i, triangle in enumerate(triangles):
            question += f"Triangle {chr(65+i)}: {triangle[0]} cm, {triangle[1]} cm, {triangle[2]} cm"
            if i < len(triangles) - 1:
                question += "; "
        question += ". Which triangles are similar to each other?"
        
        # Analyze similarity
        similar_groups = []
        for i in range(len(triangles)):
            for j in range(i + 1, len(triangles)):
                ratio1 = triangles[j][0] / triangles[i][0]
                ratio2 = triangles[j][1] / triangles[i][1]
                ratio3 = triangles[j][2] / triangles[i][2]
                
                if abs(ratio1 - ratio2) < 0.1 and abs(ratio2 - ratio3) < 0.1:
                    similar_groups.append(f"Triangles {chr(65+i)} and {chr(65+j)}")
        
        if similar_groups:
            answer = "; ".join(similar_groups)
            explanation = f"The similar triangles have proportional sides. {answer} are similar because their corresponding sides have the same ratio."
        else:
            answer = "No triangles are similar"
            explanation = "None of the triangles are similar because their corresponding sides do not have the same ratio."
        
        return {
            'question': question,
            'answer': answer,
            'explanation': explanation,
            'parameters': {
                'triangles': triangles,
                'similar_groups': similar_groups
            }
        }
    
    def generate_congruency_question(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate congruency comparison questions with South African contexts"""
        contexts = self._get_south_african_contexts()
        context = random.choice(contexts['contexts'])
        location = random.choice(contexts['locations'])
        
        if difficulty == DifficultyLevel.EASY:
            return self._generate_easy_congruency_question(context, location)
        elif difficulty == DifficultyLevel.MEDIUM:
            return self._generate_medium_congruency_question(context, location)
        else:  # HARD
            return self._generate_hard_congruency_question(context, location)
    
    def _generate_easy_congruency_question(self, context: str, location: str) -> Dict[str, Any]:
        """Generate easy congruency question"""
        # Simple triangle congruency with SSS
        side1, side2, side3 = random.randint(4, 10), random.randint(5, 12), random.randint(6, 15)
        
        # Create congruent triangle (same sides)
        question = f"At a {location}, two {context} triangles have sides: Triangle A: {side1} cm, {side2} cm, {side3} cm and Triangle B: {side1} cm, {side2} cm, {side3} cm. Are these triangles congruent?"
        
        answer = "Yes, they are congruent"
        explanation = f"Yes, the triangles are congruent because all three corresponding sides are equal (SSS - Side-Side-Side). Both triangles have sides {side1} cm, {side2} cm, and {side3} cm."
        
        return {
            'question': question,
            'answer': answer,
            'explanation': explanation,
            'parameters': {
                'triangle_a': [side1, side2, side3],
                'triangle_b': [side1, side2, side3],
                'congruency_type': 'SSS'
            }
        }
    
    def _generate_medium_congruency_question(self, context: str, location: str) -> Dict[str, Any]:
        """Generate medium congruency question with different congruency criteria"""
        congruency_type = random.choice(['SAS', 'ASA', 'AAS'])
        
        if congruency_type == 'SAS':
            # Side-Angle-Side
            side1_a, side1_b = random.randint(4, 8), random.randint(4, 8)
            angle = random.randint(30, 90)
            side2_a, side2_b = random.randint(5, 10), random.randint(5, 10)
            
            question = f"At a {location}, two {context} triangles have: Triangle A: sides {side1_a} cm and {side2_a} cm with included angle {angle}°. Triangle B: sides {side1_b} cm and {side2_b} cm with included angle {angle}°. Are they congruent?"
            
            if side1_a == side1_b and side2_a == side2_b:
                answer = "Yes, they are congruent"
                explanation = f"Yes, the triangles are congruent by SAS (Side-Angle-Side) because they have two equal sides and the included angle is equal."
            else:
                answer = "No, they are not congruent"
                explanation = f"No, the triangles are not congruent because the corresponding sides are not equal: {side1_a} ≠ {side1_b} or {side2_a} ≠ {side2_b}."
        
        elif congruency_type == 'ASA':
            # Angle-Side-Angle
            angle1, angle2 = random.randint(30, 60), random.randint(60, 90)
            angle3 = 180 - angle1 - angle2
            side_a, side_b = random.randint(5, 10), random.randint(5, 10)
            
            question = f"At a {location}, two {context} triangles have: Triangle A: angles {angle1}° and {angle2}° with included side {side_a} cm. Triangle B: angles {angle1}° and {angle2}° with included side {side_b} cm. Are they congruent?"
            
            if side_a == side_b:
                answer = "Yes, they are congruent"
                explanation = f"Yes, the triangles are congruent by ASA (Angle-Side-Angle) because they have two equal angles and the included side is equal."
            else:
                answer = "No, they are not congruent"
                explanation = f"No, the triangles are not congruent because the included sides are not equal: {side_a} ≠ {side_b}."
        
        else:  # AAS
            # Angle-Angle-Side
            angle1, angle2 = random.randint(30, 60), random.randint(60, 90)
            angle3 = 180 - angle1 - angle2
            side_a, side_b = random.randint(5, 10), random.randint(5, 10)
            
            question = f"At a {location}, two {context} triangles have: Triangle A: angles {angle1}° and {angle2}° with non-included side {side_a} cm. Triangle B: angles {angle1}° and {angle2}° with non-included side {side_b} cm. Are they congruent?"
            
            if side_a == side_b:
                answer = "Yes, they are congruent"
                explanation = f"Yes, the triangles are congruent by AAS (Angle-Angle-Side) because they have two equal angles and the non-included side is equal."
            else:
                answer = "No, they are not congruent"
                explanation = f"No, the triangles are not congruent because the non-included sides are not equal: {side_a} ≠ {side_b}."
        
        return {
            'question': question,
            'answer': answer,
            'explanation': explanation,
            'parameters': {
                'congruency_type': congruency_type,
                'triangle_a': [side1_a if congruency_type == 'SAS' else angle1, side2_a if congruency_type == 'SAS' else angle2, side_a],
                'triangle_b': [side1_b if congruency_type == 'SAS' else angle1, side2_b if congruency_type == 'SAS' else angle2, side_b]
            }
        }
    
    def _generate_hard_congruency_question(self, context: str, location: str) -> Dict[str, Any]:
        """Generate hard congruency question with complex scenarios"""
        # Multiple triangles with different congruency criteria
        triangle_count = random.randint(3, 4)
        triangles = []
        congruency_types = []
        
        # Create reference triangle
        base_sides = [random.randint(6, 10), random.randint(7, 12), random.randint(8, 14)]
        base_angles = [random.randint(40, 70), random.randint(50, 80), 180 - random.randint(40, 70) - random.randint(50, 80)]
        
        for i in range(triangle_count):
            if i == 0:
                # Reference triangle
                triangles.append({
                    'sides': base_sides.copy(),
                    'angles': base_angles.copy(),
                    'type': 'reference'
                })
            else:
                # Create variations
                variation_type = random.choice(['congruent', 'similar', 'different'])
                
                if variation_type == 'congruent':
                    # Same sides and angles
                    triangles.append({
                        'sides': base_sides.copy(),
                        'angles': base_angles.copy(),
                        'type': 'congruent'
                    })
                elif variation_type == 'similar':
                    # Proportional sides, same angles
                    scale = random.uniform(1.2, 2.5)
                    triangles.append({
                        'sides': [int(s * scale) for s in base_sides],
                        'angles': base_angles.copy(),
                        'type': 'similar'
                    })
                else:
                    # Different triangle
                    triangles.append({
                        'sides': [random.randint(5, 15) for _ in range(3)],
                        'angles': [random.randint(30, 80) for _ in range(3)],
                        'type': 'different'
                    })
        
        question = f"At a {location}, you have {triangle_count} {context} triangles: "
        for i, triangle in enumerate(triangles):
            question += f"Triangle {chr(65+i)}: sides {triangle['sides'][0]} cm, {triangle['sides'][1]} cm, {triangle['sides'][2]} cm with angles {triangle['angles'][0]}°, {triangle['angles'][1]}°, {triangle['angles'][2]}°"
            if i < len(triangles) - 1:
                question += "; "
        question += ". Which triangles are congruent to Triangle A?"
        
        # Find congruent triangles
        congruent_triangles = []
        for i, triangle in enumerate(triangles[1:], 1):
            if triangle['type'] == 'congruent':
                congruent_triangles.append(f"Triangle {chr(65+i)}")
        
        if congruent_triangles:
            answer = ", ".join(congruent_triangles)
            explanation = f"Triangles A and {', '.join(congruent_triangles)} are congruent because they have identical corresponding sides and angles."
        else:
            answer = "No triangles are congruent to Triangle A"
            explanation = "No other triangles are congruent to Triangle A because they don't have identical corresponding sides and angles."
        
        return {
            'question': question,
            'answer': answer,
            'explanation': explanation,
            'parameters': {
                'triangles': triangles,
                'congruent_triangles': congruent_triangles
            }
        }
    
    def generate_question(self, question_type: AdvancedQuestionType, difficulty: DifficultyLevel, shape_type: str = None) -> Dict[str, Any]:
        """Generate an advanced question of the specified type"""
        if question_type == AdvancedQuestionType.COMPOSITE_AREA:
            return self.generate_composite_area_question(difficulty)
        elif question_type == AdvancedQuestionType.SHADED_REGION:
            return self.generate_shaded_region_question(difficulty)
        elif question_type == AdvancedQuestionType.QUADRILATERAL_CLASSIFICATION:
            # Randomly choose between basic classification, sorting, or properties
            classification_type = random.choice(['basic', 'sorting', 'properties'])
            if classification_type == 'basic':
                return self.generate_classification_question('quadrilateral', difficulty)
            elif classification_type == 'sorting':
                return self.generate_quadrilateral_sorting_question(difficulty)
            else:  # properties
                return self.generate_quadrilateral_properties_question(difficulty)
        elif question_type == AdvancedQuestionType.TRIANGLE_CLASSIFICATION:
            return self.generate_classification_question('triangle', difficulty)
        elif question_type == AdvancedQuestionType.SIMILARITY_COMPARISON:
            return self.generate_similarity_question(difficulty)
        elif question_type == AdvancedQuestionType.CONGRUENCY_COMPARISON:
            return self.generate_congruency_question(difficulty)
        elif question_type == AdvancedQuestionType.EQUATION_SOLVING:
            return self.generate_equation_solving_question(difficulty)
        elif question_type == AdvancedQuestionType.ANGLE_CALCULATION:
            return self.generate_angle_calculation_question(difficulty)
        else:
            # Default fallback
            return {
                'question': "What is the area of a triangle with base 5 cm and height 4 cm?",
                'answer': "10 cm²",
                'explanation': "Area = ½ × base × height = ½ × 5 × 4 = 10 cm²",
                'parameters': {'base': 5, 'height': 4, 'area': 10}
            }
