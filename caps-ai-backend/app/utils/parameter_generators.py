"""
Parameter Generation System
Implements the 10 specific parameter generators as per the plan Section 2.2
"""

import random
import math
from typing import Dict, List, Any, Tuple, Optional
from enum import Enum

from .quiz_models import DifficultyLevel, ShapeType, QuestionType
from .metric_system import MetricSystemIntegration, SouthAfricanContext, ConversionType
from .difficulty_progression import DifficultyProgressionSystem


class ParameterVariationEngine:
    """
    Implements the 4 variation strategies from the plan Section 3.2:
    - Numeric Variation: Change parameter values within valid ranges
    - Unit Variation: Convert between mm, cm, m
    - Shape Variation: Different valid geometric configurations
    - Context Variation: Real-world problem scenarios
    """
    
    def __init__(self):
        self.unit_conversions = {
            'mm_to_cm': 0.1,
            'cm_to_mm': 10,
            'cm_to_m': 0.01,
            'm_to_cm': 100,
            'mm_to_m': 0.001,
            'm_to_mm': 1000
        }
        
        self.south_african_contexts = [
            'garden_plot', 'school_project', 'construction', 'room_measurement',
            'sports_field', 'art_room', 'classroom', 'patio', 'swimming_pool'
        ]
    
    def generate_numeric_variation(self, base_value: float, difficulty: DifficultyLevel) -> float:
        """Generate numeric variation within valid ranges based on difficulty"""
        if difficulty == DifficultyLevel.EASY:
            # Easy: ±20% variation, whole numbers preferred
            variation = random.uniform(0.8, 1.2)
            return round(base_value * variation)
        elif difficulty == DifficultyLevel.MEDIUM:
            # Medium: ±50% variation, 1 decimal place
            variation = random.uniform(0.5, 1.5)
            return round(base_value * variation, 1)
        else:  # HARD
            # Hard: ±100% variation, 2 decimal places
            variation = random.uniform(0.0, 2.0)
            return round(base_value * variation, 2)
    
    def generate_unit_variation(self, value: float, from_unit: str, to_unit: str) -> float:
        """Generate unit conversion variation"""
        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key in self.unit_conversions:
            return round(value * self.unit_conversions[conversion_key], 1)
        return value
    
    def generate_context_variation(self) -> str:
        """Generate South African real-world context"""
        return random.choice(self.south_african_contexts)


class TriangleParameterGenerator:
    """Generate valid side lengths and angles for triangles with difficulty progression"""
    
    def __init__(self):
        self.variation_engine = ParameterVariationEngine()
        self.progression_system = DifficultyProgressionSystem()
    
    def generate_parameters(self, difficulty: DifficultyLevel, question_type: QuestionType) -> Dict[str, Any]:
        """Generate triangle parameters based on difficulty and question type"""
        if question_type == QuestionType.AREA_CALCULATION:
            return self._generate_area_parameters(difficulty)
        elif question_type == QuestionType.PERIMETER_CALCULATION:
            return self._generate_perimeter_parameters(difficulty)
        elif question_type == QuestionType.SHAPE_CLASSIFICATION:
            return self._generate_classification_parameters(difficulty)
        else:
            return self._generate_basic_parameters(difficulty)
    
    def _generate_area_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate base and height for area calculations with difficulty progression"""
        # Add some randomness to ensure variation
        import time
        random.seed(int(time.time() * 1000000) % 1000000)
        
        # Use difficulty progression system for parameter ranges
        base_range = self.progression_system.get_parameter_range(difficulty, 'triangle_base')
        height_range = self.progression_system.get_parameter_range(difficulty, 'triangle_height')
        
        base = random.uniform(base_range[0], base_range[1])
        height = random.uniform(height_range[0], height_range[1])
        
        # Get complexity requirements
        complexity = self.progression_system.get_question_complexity_requirements(difficulty)
        
        return {
            'base': round(base, 1),
            'height': round(height, 1),
            'area': round(0.5 * base * height, 1),
            'context': self.variation_engine.generate_context_variation(),
            'complexity': complexity,
            'difficulty_stage': self.progression_system.stage_mapping.get(difficulty, 'foundation')
        }
    
    def _generate_perimeter_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate side lengths for perimeter calculations"""
        max_attempts = 100
        for _ in range(max_attempts):
            if difficulty == DifficultyLevel.EASY:
                sides = [random.uniform(1, 10) for _ in range(3)]
            elif difficulty == DifficultyLevel.MEDIUM:
                sides = [random.uniform(1, 20) for _ in range(3)]
            else:  # HARD
                sides = [random.uniform(1, 50) for _ in range(3)]
            
            # Ensure triangle inequality
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                return {
                    'sides': [round(s, 1) for s in sides],
                    'perimeter': round(sum(sides), 1),
                    'context': self.variation_engine.generate_context_variation()
                }
        
        # Fallback to valid triangle
        return {
            'sides': [3.0, 4.0, 5.0],
            'perimeter': 12.0,
            'context': self.variation_engine.generate_context_variation()
        }
    
    def _generate_classification_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate parameters for triangle classification"""
        triangle_types = ['equilateral', 'isosceles', 'scalene', 'right_angled']
        triangle_type = random.choice(triangle_types)
        
        if triangle_type == 'equilateral':
            side = random.uniform(1, 20) if difficulty != DifficultyLevel.EASY else random.uniform(1, 10)
            sides = [side, side, side]
        elif triangle_type == 'isosceles':
            base = random.uniform(1, 20) if difficulty != DifficultyLevel.EASY else random.uniform(1, 10)
            equal_sides = random.uniform(base/2, base*2)
            sides = [base, equal_sides, equal_sides]
        elif triangle_type == 'right_angled':
            # Generate Pythagorean triple
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            c = math.sqrt(a*a + b*b)
            sides = [a, b, c]
        else:  # scalene
            sides = self._generate_scalene_sides(difficulty)
        
        return {
            'sides': [round(s, 1) for s in sides],
            'triangle_type': triangle_type,
            'context': self.variation_engine.generate_context_variation()
        }
    
    def _generate_scalene_sides(self, difficulty: DifficultyLevel) -> List[float]:
        """Generate valid scalene triangle sides"""
        max_attempts = 100
        for _ in range(max_attempts):
            if difficulty == DifficultyLevel.EASY:
                sides = [random.uniform(1, 10) for _ in range(3)]
            elif difficulty == DifficultyLevel.MEDIUM:
                sides = [random.uniform(1, 20) for _ in range(3)]
            else:  # HARD
                sides = [random.uniform(1, 50) for _ in range(3)]
            
            sides.sort()
            if sides[0] + sides[1] > sides[2] and len(set(sides)) == 3:
                return sides
        
        # Fallback
        return [3.0, 4.0, 5.0]
    
    def _generate_basic_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate basic triangle parameters"""
        return self._generate_area_parameters(difficulty)


class QuadrilateralParameterGenerator:
    """Generate valid side/angle combinations for quadrilaterals"""
    
    def __init__(self):
        self.variation_engine = ParameterVariationEngine()
    
    def generate_parameters(self, difficulty: DifficultyLevel, question_type: QuestionType) -> Dict[str, Any]:
        """Generate quadrilateral parameters based on difficulty and question type"""
        if question_type == QuestionType.AREA_CALCULATION:
            return self._generate_area_parameters(difficulty)
        elif question_type == QuestionType.PERIMETER_CALCULATION:
            return self._generate_perimeter_parameters(difficulty)
        elif question_type == QuestionType.SHAPE_CLASSIFICATION:
            return self._generate_classification_parameters(difficulty)
        else:
            return self._generate_basic_parameters(difficulty)
    
    def _generate_area_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate length and width for area calculations"""
        if difficulty == DifficultyLevel.EASY:
            length = random.uniform(1, 10)
            width = random.uniform(1, 10)
        elif difficulty == DifficultyLevel.MEDIUM:
            length = random.uniform(1, 20)
            width = random.uniform(1, 20)
        else:  # HARD
            length = random.uniform(1, 50)
            width = random.uniform(1, 50)
        
        return {
            'length': round(length, 1),
            'width': round(width, 1),
            'area': round(length * width, 1),
            'context': self.variation_engine.generate_context_variation()
        }
    
    def _generate_perimeter_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate side lengths for perimeter calculations"""
        if difficulty == DifficultyLevel.EASY:
            length = random.uniform(1, 10)
            width = random.uniform(1, 10)
        elif difficulty == DifficultyLevel.MEDIUM:
            length = random.uniform(1, 20)
            width = random.uniform(1, 20)
        else:  # HARD
            length = random.uniform(1, 50)
            width = random.uniform(1, 50)
        
        return {
            'length': round(length, 1),
            'width': round(width, 1),
            'perimeter': round(2 * (length + width), 1),
            'context': self.variation_engine.generate_context_variation()
        }
    
    def _generate_classification_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate parameters for quadrilateral classification"""
        quadrilateral_types = ['square', 'rectangle', 'rhombus', 'parallelogram', 'kite', 'trapezium']
        quad_type = random.choice(quadrilateral_types)
        
        if quad_type == 'square':
            side = random.uniform(1, 20) if difficulty != DifficultyLevel.EASY else random.uniform(1, 10)
            return {
                'length': round(side, 1),
                'width': round(side, 1),
                'quadrilateral_type': quad_type,
                'context': self.variation_engine.generate_context_variation()
            }
        elif quad_type == 'rectangle':
            length = random.uniform(1, 20) if difficulty != DifficultyLevel.EASY else random.uniform(1, 10)
            width = random.uniform(1, 20) if difficulty != DifficultyLevel.EASY else random.uniform(1, 10)
            return {
                'length': round(length, 1),
                'width': round(width, 1),
                'quadrilateral_type': quad_type,
                'context': self.variation_engine.generate_context_variation()
            }
        else:
            # For other types, generate basic rectangle parameters
            return self._generate_area_parameters(difficulty)
    
    def _generate_basic_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate basic quadrilateral parameters"""
        return self._generate_area_parameters(difficulty)


class CircleParameterGenerator:
    """Generate valid radius values for circles"""
    
    def __init__(self):
        self.variation_engine = ParameterVariationEngine()
    
    def generate_parameters(self, difficulty: DifficultyLevel, question_type: QuestionType) -> Dict[str, Any]:
        """Generate circle parameters based on difficulty and question type"""
        if difficulty == DifficultyLevel.EASY:
            radius = random.uniform(1, 10)
        elif difficulty == DifficultyLevel.MEDIUM:
            radius = random.uniform(1, 20)
        else:  # HARD
            radius = random.uniform(1, 50)
        
        radius = round(radius, 1)
        
        return {
            'radius': radius,
            'diameter': round(2 * radius, 1),
            'circumference': round(2 * math.pi * radius, 1),
            'area': round(math.pi * radius * radius, 1),
            'context': self.variation_engine.generate_context_variation()
        }


class AngleParameterGenerator:
    """Generate valid angle measurements"""
    
    def __init__(self):
        self.variation_engine = ParameterVariationEngine()
    
    def generate_parameters(self, difficulty: DifficultyLevel, question_type: QuestionType) -> Dict[str, Any]:
        """Generate angle parameters based on difficulty and question type"""
        if question_type == QuestionType.SHAPE_CLASSIFICATION:
            return self._generate_angle_classification_parameters(difficulty)
        else:
            return self._generate_basic_angle_parameters(difficulty)
    
    def _generate_angle_classification_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate parameters for angle classification"""
        angle_types = ['acute', 'right', 'obtuse', 'straight', 'reflex']
        angle_type = random.choice(angle_types)
        
        if angle_type == 'acute':
            angle = random.uniform(1, 89)
        elif angle_type == 'right':
            angle = 90
        elif angle_type == 'obtuse':
            angle = random.uniform(91, 179)
        elif angle_type == 'straight':
            angle = 180
        else:  # reflex
            angle = random.uniform(181, 359)
        
        return {
            'angle': round(angle, 1),
            'angle_type': angle_type,
            'context': self.variation_engine.generate_context_variation()
        }
    
    def _generate_basic_angle_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate basic angle parameters"""
        angle = random.uniform(1, 360)
        return {
            'angle': round(angle, 1),
            'context': self.variation_engine.generate_context_variation()
        }


class MetricUnitGenerator:
    """Generate appropriate metric units and conversions with enhanced South African contexts"""
    
    def __init__(self):
        self.variation_engine = ParameterVariationEngine()
        self.conversion_factors = {
            # Length conversions
            'mm_to_cm': 0.1, 'cm_to_mm': 10,
            'cm_to_m': 0.01, 'm_to_cm': 100,
            'mm_to_m': 0.001, 'm_to_mm': 1000,
            'm_to_km': 0.001, 'km_to_m': 1000,
            # Area conversions (using both formats for compatibility)
            'mm2_to_cm2': 0.01, 'cm2_to_mm2': 100,
            'cm2_to_m2': 0.0001, 'm2_to_cm2': 10000,
            'mm2_to_m2': 0.000001, 'm2_to_mm2': 1000000,
            'm2_to_ha': 0.0001, 'ha_to_m2': 10000,
            # Unicode superscript versions
            'mm²_to_cm²': 0.01, 'cm²_to_mm²': 100,
            'cm²_to_m²': 0.0001, 'm²_to_cm²': 10000,
            'mm²_to_m²': 0.000001, 'm²_to_mm²': 1000000,
            'm²_to_ha': 0.0001, 'ha_to_m²': 10000
        }
    
    def generate_conversion_parameters(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Generate enhanced unit conversion parameters with South African contexts"""
        if difficulty == DifficultyLevel.EASY:
            conversions = [
                ('mm', 'cm'), ('cm', 'mm'), ('cm', 'm'), ('m', 'cm')
            ]
            value = random.randint(1, 20)
        elif difficulty == DifficultyLevel.MEDIUM:
            conversions = [
                ('mm', 'cm'), ('cm', 'mm'), ('cm', 'm'), ('m', 'cm'),
                ('mm', 'm'), ('m', 'mm'), ('mm²', 'cm²'), ('cm²', 'mm²'),
                ('cm²', 'm²'), ('m²', 'cm²')
            ]
            value = random.uniform(1, 50)
        else:  # HARD
            conversions = [
                ('mm', 'cm'), ('cm', 'mm'), ('cm', 'm'), ('m', 'cm'),
                ('mm', 'm'), ('m', 'mm'), ('m', 'km'), ('km', 'm'),
                ('mm²', 'cm²'), ('cm²', 'mm²'), ('cm²', 'm²'), ('m²', 'cm²'),
                ('mm²', 'm²'), ('m²', 'mm²'), ('m²', 'ha'), ('ha', 'm²')
            ]
            value = random.uniform(1, 100)
        
        from_unit, to_unit = random.choice(conversions)
        value = round(value, 1) if isinstance(value, float) else value
        converted_value = self._convert_value(value, from_unit, to_unit)
        
        # Generate South African context
        context = self._generate_south_african_context(difficulty, from_unit, to_unit)
        
        return {
            'value': value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'converted_value': converted_value,
            'context': context,
            'south_african_context': True
        }
    
    def _convert_value(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert value between units"""
        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key in self.conversion_factors:
            return round(value * self.conversion_factors[conversion_key], 2)
        else:
            # Reverse conversion
            reverse_key = f"{to_unit}_to_{from_unit}"
            if reverse_key in self.conversion_factors:
                return round(value / self.conversion_factors[reverse_key], 2)
        return value
    
    def _generate_south_african_context(self, difficulty: DifficultyLevel, from_unit: str, to_unit: str) -> str:
        """Generate South African real-world context for conversions"""
        contexts = {
            'garden_plot': [
                'A triangular garden bed in Johannesburg',
                'A rectangular garden plot in Cape Town',
                'A circular flower bed in Durban'
            ],
            'school_project': [
                'A student project at a Soweto school',
                'A science fair project in Pretoria',
                'An art project at a township school'
            ],
            'construction': [
                'A building project in Sandton',
                'A house construction in Soweto',
                'A shopping mall in Rosebank'
            ],
            'farming': [
                'A crop field in the Free State',
                'A farm in Mpumalanga',
                'A vineyard in the Western Cape'
            ],
            'sports': [
                'A soccer field in Orlando',
                'A cricket pitch in Newlands',
                'A rugby field in Ellis Park'
            ]
        }
        
        context_type = random.choice(list(contexts.keys()))
        location = random.choice(contexts[context_type])
        
        if difficulty == DifficultyLevel.HARD and 'm²' in from_unit and 'm²' in to_unit:
            # Add cost context for area conversions
            cost_per_unit = random.randint(50, 500)  # R50-R500 per m²
            return f"{location} - Material costs R{cost_per_unit} per m²"
        
        return location


class SouthAfricanContextGenerator:
    """Generate comprehensive real-world SA contexts with cost calculations"""
    
    def __init__(self):
        self.metric_system = MetricSystemIntegration()
        self.contexts = {
            'garden_plot': {
                'locations': ['Johannesburg', 'Cape Town', 'Durban', 'Pretoria', 'Port Elizabeth'],
                'templates': [
                    'A triangular garden bed in {location} is {base} m × {height} m. What is its area in cm²?',
                    'A rectangular garden plot in {location} is {length} m × {width} m. How many cm² is this?',
                    'A circular flower bed in {location} has radius {radius} m. What is its area in cm²?'
                ],
                'cost_contexts': [
                    'If soil costs R{cost} per m², what is the total cost?',
                    'If fertilizer costs R{cost} per m², what is the total cost in cm² units?'
                ]
            },
            'school_project': {
                'locations': ['Soweto', 'Sandton', 'Pretoria', 'Cape Town', 'Durban'],
                'templates': [
                    'A student at {location} school draws a triangle with base {base} cm and height {height} cm. What is its area?',
                    'A science project at {location} school needs a circular area of {radius} m. What is this in cm²?',
                    'An art project at {location} school uses a rectangle {length} cm × {width} cm. What is its area in mm²?'
                ],
                'cost_contexts': [
                    'If art supplies cost R{cost} per cm², what is the total cost?',
                    'If materials cost R{cost} per m², what is the cost in cm² units?'
                ]
            },
            'construction': {
                'locations': ['Sandton', 'Soweto', 'Rosebank', 'Pretoria', 'Cape Town'],
                'templates': [
                    'A rectangular room in {location} is {length} m × {width} m. If floor tiles are 30 cm × 30 cm, how many tiles are needed?',
                    'A triangular roof section in {location} is {base} m × {height} m. What is its area in cm²?',
                    'A square patio in {location} is {side} m × {side} m. What is its area in mm²?'
                ],
                'cost_contexts': [
                    'If tiles cost R{cost} per m², what is the total cost?',
                    'If roofing material costs R{cost} per m², what is the cost in cm² units?'
                ]
            },
            'farming': {
                'locations': ['Free State', 'Mpumalanga', 'Western Cape', 'KwaZulu-Natal', 'Limpopo'],
                'templates': [
                    'A crop field in {location} is {length} m × {width} m. What is its area in hectares?',
                    'A triangular farm plot in {location} is {base} m × {height} m. What is its area in cm²?',
                    'A circular water tank in {location} has radius {radius} m. What is its area in cm²?'
                ],
                'cost_contexts': [
                    'If seeds cost R{cost} per hectare, what is the total cost?',
                    'If irrigation costs R{cost} per m², what is the cost in cm² units?'
                ]
            },
            'sports': {
                'locations': ['Orlando', 'Newlands', 'Ellis Park', 'Loftus', 'Kings Park'],
                'templates': [
                    'A soccer field in {location} is {length} m × {width} m. What is its area in cm²?',
                    'A cricket pitch in {location} is {length} m × {width} m. What is its area in mm²?',
                    'A circular running track in {location} has radius {radius} m. What is its area in cm²?'
                ],
                'cost_contexts': [
                    'If grass costs R{cost} per m², what is the total cost?',
                    'If maintenance costs R{cost} per m², what is the cost in cm² units?'
                ]
            }
        }
    
    def generate_context(self, context_type: str, difficulty: DifficultyLevel, **params) -> str:
        """Generate enhanced South African context with cost calculations"""
        if context_type not in self.contexts:
            context_type = 'school_project'
        
        context_data = self.contexts[context_type]
        location = random.choice(context_data['locations'])
        template = random.choice(context_data['templates'])
        
        # Add location to parameters
        params['location'] = location
        
        # Format the template with parameters
        question = template.format(**params)
        
        # Add cost context for medium and hard difficulties
        if difficulty in [DifficultyLevel.MEDIUM, DifficultyLevel.HARD] and random.random() < 0.3:
            cost_template = random.choice(context_data['cost_contexts'])
            cost = random.randint(50, 500)  # R50-R500
            params['cost'] = cost
            cost_question = cost_template.format(**params)
            question += f" {cost_question}"
        
        return question
    
    def get_available_contexts(self) -> List[str]:
        """Get list of available context types"""
        return list(self.contexts.keys())
    
    def generate_cost_calculation(self, area: float, unit: str, context_type: str) -> Dict[str, Any]:
        """Generate cost calculation for area"""
        cost_per_unit = random.randint(50, 500)  # R50-R500 per unit
        total_cost = area * cost_per_unit
        
        return {
            'cost_per_unit': cost_per_unit,
            'total_cost': round(total_cost, 2),
            'area': area,
            'unit': unit,
            'context': context_type
        }
