"""
Geometry Diagram Generation Module
Generates precise 2D and 3D geometric diagrams using matplotlib and plotly
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arc
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import io
import base64
from typing import Dict, List, Tuple, Optional, Any
import math
import json
from dataclasses import dataclass
from enum import Enum

# Configure matplotlib font to avoid font errors
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# Enums for geometric classifications
class AngleType(Enum):
    ACUTE = "acute"
    RIGHT = "right"
    OBTUSE = "obtuse"
    STRAIGHT = "straight"
    REFLEX = "reflex"

class TriangleType(Enum):
    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"
    RIGHT_ANGLED = "right_angled"
    ACUTE = "acute"
    OBTUSE = "obtuse"

class QuadrilateralType(Enum):
    SQUARE = "square"
    RECTANGLE = "rectangle"
    RHOMBUS = "rhombus"
    PARALLELOGRAM = "parallelogram"
    KITE = "kite"
    TRAPEZIUM = "trapezium"
    IRREGULAR = "irregular"

class Shape3DType(Enum):
    CUBE = "cube"
    RECTANGULAR_PRISM = "rectangular_prism"
    SPHERE = "sphere"
    CYLINDER = "cylinder"
    PYRAMID = "pyramid"

# Data classes for geometric properties
@dataclass
class GeometricProperties:
    area: float
    perimeter: float
    angles: List[float]
    sides: List[float]
    classification: str
    properties: List[str]

@dataclass
class AngleMeasurement:
    degrees: float
    angle_type: AngleType
    vertex: Tuple[float, float]
    arms: Tuple[Tuple[float, float], Tuple[float, float]]

# Enhanced data structures for comprehensive quiz system
@dataclass
class QuizQuestion:
    question: str
    options: List[str]
    correct_answer: str
    explanation: str
    difficulty: str
    topic: str
    shape_type: str
    metric_units: str
    south_african_context: bool
    conversion_required: bool
    expected_concepts: List[str]
    parameters: Dict[str, Any]

@dataclass
class QuestionTemplate:
    template_id: str
    question_template: str
    answer_generator: str
    explanation_template: str
    difficulty: str
    shape_type: str
    parameter_ranges: Dict[str, Tuple[float, float]]
    geometric_constraints: List[str]

@dataclass
class MetricConversion:
    from_unit: str
    to_unit: str
    conversion_factor: float
    unit_type: str  # 'length' or 'area'

# Mathematical Calculation Classes
class TriangleCalculator:
    """Handles triangle calculations and classifications for Grade 7 curriculum"""
    
    def __init__(self):
        self.precision = 0.1  # Tolerance for floating point comparisons
    
    def calculate_unknown_side(self, side_a: float, side_b: float, angle_c: float) -> float:
        """
        Calculate unknown side using cosine law: c² = a² + b² - 2ab cos(C)
        Args:
            side_a: Length of side A
            side_b: Length of side B  
            angle_c: Angle between sides A and B in degrees
        Returns:
            Length of side C
        """
        angle_c_rad = math.radians(angle_c)
        return math.sqrt(side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(angle_c_rad))
    
    def calculate_unknown_angle(self, side_a: float, side_b: float, side_c: float) -> float:
        """
        Calculate unknown angle using cosine law: cos(A) = (b² + c² - a²) / (2bc)
        Args:
            side_a: Length of side A
            side_b: Length of side B
            side_c: Length of side C
        Returns:
            Angle A in degrees
        """
        if side_b == 0 or side_c == 0:
            return 0
        cos_a = (side_b**2 + side_c**2 - side_a**2) / (2*side_b*side_c)
        # Clamp to valid range for arccos
        cos_a = max(-1, min(1, cos_a))
        return math.degrees(math.acos(cos_a))
    
    def calculate_area(self, side_a: float, side_b: float, angle_c: float) -> float:
        """Calculate triangle area using: Area = 0.5 * a * b * sin(C)"""
        angle_c_rad = math.radians(angle_c)
        return 0.5 * side_a * side_b * math.sin(angle_c_rad)
    
    def calculate_perimeter(self, sides: List[float]) -> float:
        """Calculate triangle perimeter"""
        return sum(sides)
    
    def classify_triangle_by_sides(self, sides: List[float]) -> TriangleType:
        """Classify triangle by side lengths"""
        if len(sides) != 3:
            return TriangleType.SCALENE
            
        # Sort sides for comparison
        sorted_sides = sorted(sides)
        a, b, c = sorted_sides
        
        if self._approx_equal(a, b) and self._approx_equal(b, c):
            return TriangleType.EQUILATERAL
        elif self._approx_equal(a, b) or self._approx_equal(b, c) or self._approx_equal(a, c):
            return TriangleType.ISOSCELES
        else:
            return TriangleType.SCALENE
    
    def classify_triangle_by_angles(self, angles: List[float]) -> TriangleType:
        """Classify triangle by angle measures"""
        if len(angles) != 3:
            return TriangleType.ACUTE
            
        # Check for right angle first
        for angle in angles:
            if self._approx_equal(angle, 90):
                return TriangleType.RIGHT_ANGLED
        
        # Check for obtuse angle
        for angle in angles:
            if angle > 90:
                return TriangleType.OBTUSE
                
        return TriangleType.ACUTE
    
    def get_triangle_properties(self, sides: List[float], angles: List[float]) -> GeometricProperties:
        """Get comprehensive triangle properties"""
        side_classification = self.classify_triangle_by_sides(sides)
        angle_classification = self.classify_triangle_by_angles(angles)
        
        # Determine final classification
        if side_classification == TriangleType.EQUILATERAL:
            classification = "Equilateral Triangle"
        elif side_classification == TriangleType.ISOSCELES:
            if angle_classification == TriangleType.RIGHT_ANGLED:
                classification = "Right-angled Isosceles Triangle"
            else:
                classification = "Isosceles Triangle"
        elif angle_classification == TriangleType.RIGHT_ANGLED:
            classification = "Right-angled Triangle"
        elif angle_classification == TriangleType.OBTUSE:
            classification = "Obtuse Triangle"
        else:
            classification = "Acute Triangle"
        
        # Calculate properties
        area = self.calculate_area(sides[0], sides[1], angles[2]) if len(sides) >= 2 and len(angles) >= 1 else 0
        perimeter = self.calculate_perimeter(sides)
        
        properties = []
        if side_classification == TriangleType.EQUILATERAL:
            properties.append("All sides are equal")
            properties.append("All angles are 60°")
        elif side_classification == TriangleType.ISOSCELES:
            properties.append("Two sides are equal")
        
        if angle_classification == TriangleType.RIGHT_ANGLED:
            properties.append("One angle is 90°")
        elif angle_classification == TriangleType.OBTUSE:
            properties.append("One angle is greater than 90°")
        else:
            properties.append("All angles are less than 90°")
        
        return GeometricProperties(
            area=area,
            perimeter=perimeter,
            angles=angles,
            sides=sides,
            classification=classification,
            properties=properties
        )
    
    def _approx_equal(self, a: float, b: float) -> bool:
        """Check if two floats are approximately equal within tolerance"""
        return abs(a - b) < self.precision

class QuadrilateralAnalyzer:
    """Handles quadrilateral analysis and classification for Grade 7 curriculum"""
    
    def __init__(self):
        self.precision = 0.1
    
    def check_all_sides_equal(self, sides: List[float]) -> bool:
        """Check if all four sides are equal"""
        if len(sides) != 4:
            return False
        return all(abs(sides[0] - side) < self.precision for side in sides[1:])
    
    def check_opposite_sides_equal(self, sides: List[float]) -> bool:
        """Check if opposite sides are equal"""
        if len(sides) != 4:
            return False
        return (abs(sides[0] - sides[2]) < self.precision and 
                abs(sides[1] - sides[3]) < self.precision)
    
    def check_all_angles_right(self, angles: List[float]) -> bool:
        """Check if all angles are right angles (90°)"""
        if len(angles) != 4:
            return False
        return all(abs(angle - 90) < self.precision for angle in angles)
    
    def check_parallel_sides(self, angles: List[float]) -> bool:
        """Check if opposite sides are parallel (sum of adjacent angles = 180°)"""
        if len(angles) != 4:
            return False
        # Check if opposite angles are equal (indicates parallel sides)
        return (abs(angles[0] - angles[2]) < self.precision and 
                abs(angles[1] - angles[3]) < self.precision)
    
    def check_adjacent_sides_equal(self, sides: List[float]) -> bool:
        """Check if adjacent sides are equal (for kites)"""
        if len(sides) != 4:
            return False
        return ((abs(sides[0] - sides[1]) < self.precision and abs(sides[2] - sides[3]) < self.precision) or
                (abs(sides[1] - sides[2]) < self.precision and abs(sides[3] - sides[0]) < self.precision))
    
    def check_one_pair_parallel(self, angles: List[float]) -> bool:
        """Check if only one pair of opposite sides is parallel"""
        if len(angles) != 4:
            return False
        # Check if sum of adjacent angles equals 180° for one pair
        return ((abs(angles[0] + angles[1] - 180) < self.precision and abs(angles[2] + angles[3] - 180) < self.precision) or
                (abs(angles[1] + angles[2] - 180) < self.precision and abs(angles[3] + angles[0] - 180) < self.precision))
    
    def classify_quadrilateral(self, sides: List[float], angles: List[float]) -> GeometricProperties:
        """Classify quadrilateral based on sides and angles"""
        properties = {
            'all_sides_equal': self.check_all_sides_equal(sides),
            'opposite_sides_equal': self.check_opposite_sides_equal(sides),
            'all_angles_right': self.check_all_angles_right(angles),
            'parallel_sides': self.check_parallel_sides(angles),
            'adjacent_sides_equal': self.check_adjacent_sides_equal(sides),
            'one_pair_parallel': self.check_one_pair_parallel(angles)
        }
        
        # Classification logic based on Grade 7 curriculum
        if properties['all_sides_equal'] and properties['all_angles_right']:
            classification = "Square"
            shape_properties = ["All sides equal", "All angles are 90°", "Opposite sides parallel"]
        elif properties['opposite_sides_equal'] and properties['all_angles_right']:
            classification = "Rectangle"
            shape_properties = ["Opposite sides equal", "All angles are 90°", "Opposite sides parallel"]
        elif properties['all_sides_equal'] and properties['parallel_sides']:
            classification = "Rhombus"
            shape_properties = ["All sides equal", "Opposite sides parallel", "Opposite angles equal"]
        elif properties['opposite_sides_equal'] and properties['parallel_sides']:
            classification = "Parallelogram"
            shape_properties = ["Opposite sides equal", "Opposite sides parallel", "Opposite angles equal"]
        elif properties['adjacent_sides_equal'] and not properties['parallel_sides']:
            classification = "Kite"
            shape_properties = ["Two pairs of adjacent sides equal", "One pair of opposite angles equal"]
        elif properties['one_pair_parallel']:
            classification = "Trapezium"
            shape_properties = ["One pair of opposite sides parallel"]
        else:
            classification = "Irregular Quadrilateral"
            shape_properties = ["No special properties"]
        
        # Calculate area (simplified - would need more complex calculation for irregular shapes)
        area = self._calculate_quadrilateral_area(sides, angles)
        perimeter = sum(sides)
        
        return GeometricProperties(
            area=area,
            perimeter=perimeter,
            angles=angles,
            sides=sides,
            classification=classification,
            properties=shape_properties
        )
    
    def _calculate_quadrilateral_area(self, sides: List[float], angles: List[float]) -> float:
        """Calculate quadrilateral area (simplified calculation)"""
        # For regular shapes, use specific formulas
        if len(sides) == 4 and len(angles) == 4:
            # This is a simplified calculation - in practice, you'd need more complex geometry
            # For now, return a basic approximation
            return sum(sides) * 0.5  # Very rough approximation
        return 0.0

class CircleCalculator:
    """Handles circle calculations for Grade 7 curriculum"""
    
    def calculate_circumference(self, radius: float) -> float:
        """Calculate circle circumference: C = 2πr"""
        return 2 * math.pi * radius
    
    def calculate_area(self, radius: float) -> float:
        """Calculate circle area: A = πr²"""
        return math.pi * radius**2
    
    def calculate_diameter(self, radius: float) -> float:
        """Calculate diameter: d = 2r"""
        return 2 * radius
    
    def calculate_radius_from_diameter(self, diameter: float) -> float:
        """Calculate radius from diameter: r = d/2"""
        return diameter / 2
    
    def calculate_chord_length(self, radius: float, central_angle: float) -> float:
        """Calculate chord length: chord = 2r sin(θ/2)"""
        return 2 * radius * math.sin(math.radians(central_angle / 2))
    
    def calculate_arc_length(self, radius: float, central_angle: float) -> float:
        """Calculate arc length: arc = rθ (where θ is in radians)"""
        return radius * math.radians(central_angle)
    
    def calculate_sector_area(self, radius: float, central_angle: float) -> float:
        """Calculate sector area: A = (θ/360°) × πr²"""
        return (central_angle / 360) * math.pi * radius**2
    
    def calculate_segment_area(self, radius: float, central_angle: float) -> float:
        """Calculate segment area: sector area - triangle area"""
        sector_area = self.calculate_sector_area(radius, central_angle)
        # Triangle area = 0.5 * r² * sin(θ)
        triangle_area = 0.5 * radius**2 * math.sin(math.radians(central_angle))
        return sector_area - triangle_area

class Geometry3DCalculator:
    """Handles 3D geometry calculations for Grade 7 curriculum"""
    
    def __init__(self):
        self.precision = 0.1  # Tolerance for floating point comparisons
    
    def calculate_surface_area_cube(self, side_length: float) -> float:
        """Calculate surface area of cube: 6 × side²"""
        return 6 * (side_length ** 2)
    
    def calculate_volume_cube(self, side_length: float) -> float:
        """Calculate volume of cube: side³"""
        return side_length ** 3
    
    def calculate_surface_area_rectangular_prism(self, length: float, breadth: float, height: float) -> float:
        """Calculate surface area of rectangular prism: 2(lb + bh + hl)"""
        return 2 * (length * breadth + breadth * height + height * length)
    
    def calculate_volume_rectangular_prism(self, length: float, breadth: float, height: float) -> float:
        """Calculate volume of rectangular prism: l × b × h"""
        return length * breadth * height
    
    def convert_volume_to_capacity(self, volume_cm3: float) -> float:
        """Convert volume in cm³ to capacity in ml (1cm³ = 1ml)"""
        return volume_cm3
    
    def convert_volume_units(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert between mm³, cm³, m³"""
        conversions = {
            'mm3_to_cm3': 0.001,
            'cm3_to_m3': 0.000001,
            'mm3_to_m3': 0.000000001,
            'cm3_to_mm3': 1000,
            'm3_to_cm3': 1000000,
            'm3_to_mm3': 1000000000
        }
        
        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key in conversions:
            return value * conversions[conversion_key]
        else:
            raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")
    
    def get_all_calculations(self, shape_type: str, dimensions: Dict[str, float]) -> Dict[str, Any]:
        """Get all calculations for a 3D shape"""
        if shape_type == 'cube':
            side_length = dimensions.get('side_length', 1.0)
            surface_area = self.calculate_surface_area_cube(side_length)
            volume = self.calculate_volume_cube(side_length)
            capacity = self.convert_volume_to_capacity(volume)
            
            return {
                'surface_area': round(surface_area, 1),
                'volume': round(volume, 1),
                'capacity': round(capacity, 1),
                'side_length': side_length,
                'shape_type': 'cube'
            }
        
        elif shape_type == 'rectangular_prism':
            length = dimensions.get('length', 1.0)
            breadth = dimensions.get('breadth', 1.0)
            height = dimensions.get('height', 1.0)
            surface_area = self.calculate_surface_area_rectangular_prism(length, breadth, height)
            volume = self.calculate_volume_rectangular_prism(length, breadth, height)
            capacity = self.convert_volume_to_capacity(volume)
            
            return {
                'surface_area': round(surface_area, 1),
                'volume': round(volume, 1),
                'capacity': round(capacity, 1),
                'length': length,
                'breadth': breadth,
                'height': height,
                'shape_type': 'rectangular_prism'
            }
        
        else:
            raise ValueError(f"Unsupported 3D shape type: {shape_type}")

class InteractiveAngleTool:
    """Handles angle measurement and classification for Grade 7 curriculum"""
    
    def __init__(self):
        self.angle_types = {
            AngleType.ACUTE: (0, 90),
            AngleType.RIGHT: 90,
            AngleType.OBTUSE: (90, 180),
            AngleType.STRAIGHT: 180,
            AngleType.REFLEX: (180, 360)
        }
        self.precision = 0.1
    
    def measure_angle(self, vertex: Tuple[float, float], arm1: Tuple[float, float], arm2: Tuple[float, float]) -> AngleMeasurement:
        """Calculate angle between two arms"""
        # Convert to vectors
        v1 = np.array(arm1) - np.array(vertex)
        v2 = np.array(arm2) - np.array(vertex)
        
        # Calculate angle using dot product
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = max(-1, min(1, cos_angle))  # Clamp to valid range
        angle_rad = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_rad)
        
        # Classify angle type
        angle_type = self._classify_angle(angle_degrees)
        
        return AngleMeasurement(
            degrees=angle_degrees,
            angle_type=angle_type,
            vertex=vertex,
            arms=(arm1, arm2)
        )
    
    def _classify_angle(self, degrees: float) -> AngleType:
        """Classify angle based on its measure"""
        if abs(degrees - 90) < self.precision:
            return AngleType.RIGHT
        elif abs(degrees - 180) < self.precision:
            return AngleType.STRAIGHT
        elif 0 < degrees < 90:
            return AngleType.ACUTE
        elif 90 < degrees < 180:
            return AngleType.OBTUSE
        elif 180 < degrees < 360:
            return AngleType.REFLEX
        else:
            return AngleType.ACUTE  # Default fallback
    
    def draw_protractor_overlay(self, ax, center: Tuple[float, float], radius: float):
        """Draw protractor markings for angle measurement"""
        # Draw semicircle
        theta = np.linspace(0, math.pi, 100)
        x = center[0] + radius * np.cos(theta)
        y = center[1] + radius * np.sin(theta)
        ax.plot(x, y, 'k-', linewidth=1, alpha=0.7)
        
        # Draw degree markings
        for angle in range(0, 181, 10):
            angle_rad = math.radians(angle)
            x1 = center[0] + (radius - 0.2) * math.cos(angle_rad)
            y1 = center[1] + (radius - 0.2) * math.sin(angle_rad)
            x2 = center[0] + radius * math.cos(angle_rad)
            y2 = center[1] + radius * math.sin(angle_rad)
            ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.5, alpha=0.7)
            
            # Add degree labels
            if angle % 30 == 0:
                x_label = center[0] + (radius + 0.3) * math.cos(angle_rad)
                y_label = center[1] + (radius + 0.3) * math.sin(angle_rad)
                ax.text(x_label, y_label, str(angle), ha='center', va='center', fontsize=8)

class ComprehensiveQuizGenerator:
    """Comprehensive quiz generation system with two fail-safe mechanisms for Grade 7 Geometry"""
    
    def __init__(self):
        self.triangle_calculator = TriangleCalculator()
        self.quadrilateral_analyzer = QuadrilateralAnalyzer()
        self.circle_calculator = CircleCalculator()
        self.angle_tool = InteractiveAngleTool()
        
        # Initialize question templates
        self.question_templates = self._initialize_question_templates()
        
        # Initialize metric conversions
        self.metric_conversions = self._initialize_metric_conversions()
        
        # Initialize South African contexts
        self.south_african_contexts = self._initialize_south_african_contexts()
    
    def generate_question(self, topic: str, difficulty: str) -> QuizQuestion:
        """Generate a quiz question using two fail-safe systems"""
        try:
            # System 1: Constraint-based generation
            question = self._generate_constraint_based_question(topic, difficulty)
            if question:
                return question
        except Exception as e:
            print(f"Constraint-based generation failed: {e}")
        
        try:
            # System 2: Template-based generation (fail-safe)
            return self._generate_template_based_question(topic, difficulty)
        except Exception as e:
            print(f"Template-based generation failed: {e}")
            # Ultimate fallback
            return self._generate_fallback_question(topic, difficulty)
    
    def _generate_constraint_based_question(self, topic: str, difficulty: str) -> QuizQuestion:
        """System 1: Generate questions using geometric constraints"""
        if topic == 'triangles':
            return self._generate_triangle_constraint_question(difficulty)
        elif topic == 'quadrilaterals':
            return self._generate_quadrilateral_constraint_question(difficulty)
        elif topic == 'circles':
            return self._generate_circle_constraint_question(difficulty)
        elif topic == 'angles':
            return self._generate_angle_constraint_question(difficulty)
        elif topic == 'unit_conversions':
            return self._generate_conversion_constraint_question(difficulty)
        elif topic == 'composite_areas':
            return self._generate_composite_constraint_question(difficulty)
        else:
            raise ValueError(f"Unsupported topic: {topic}")
    
    def _generate_template_based_question(self, topic: str, difficulty: str) -> QuizQuestion:
        """System 2: Generate questions using pre-defined templates"""
        templates = [t for t in self.question_templates if t.topic == topic and t.difficulty == difficulty]
        if not templates:
            raise ValueError(f"No templates found for {topic} {difficulty}")
        
        import random
        template = random.choice(templates)
        return self._instantiate_template(template)
    
    def _generate_triangle_constraint_question(self, difficulty: str) -> QuizQuestion:
        """Generate triangle question using geometric constraints"""
        import random
        
        if difficulty == 'easy':
            # Equilateral triangle
            side = random.randint(2, 8)
            sides = [side, side, side]
            correct = "Equilateral"
            explanation = "all three sides are equal"
            question = f"Classify this triangle with sides {sides[0]}, {sides[1]}, and {sides[2]} cm"
            
        elif difficulty == 'medium':
            # Right-angled triangle using Pythagorean triples
            triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
            a, b, c = random.choice(triples)
            sides = [a, b, c]
            correct = "Right-angled"
            explanation = f"it satisfies the Pythagorean theorem ({a}² + {b}² = {c}²)"
            question = f"Classify this triangle with sides {sides[0]}, {sides[1]}, and {sides[2]} cm"
            
        else:  # hard
            # Generate valid triangle using triangle inequality
            while True:
                sides = [random.randint(2, 10) for _ in range(3)]
                sides.sort()
                if sides[0] + sides[1] > sides[2]:  # Triangle inequality
                    break
            
            props = self.triangle_calculator.get_triangle_properties(sides, [])
            correct = props.classification
            explanation = ', '.join(props.properties) if props.properties else "based on its side lengths"
            question = f"Classify this triangle with sides {sides[0]}, {sides[1]}, and {sides[2]} cm"
        
        options = ["Equilateral", "Isosceles", "Scalene", "Right-angled", "Acute", "Obtuse"]
        random.shuffle(options)
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct,
            explanation=f"This triangle is {correct.lower()} because {explanation}",
            difficulty=difficulty,
            topic='triangles',
            shape_type='triangle',
            metric_units='cm',
            south_african_context=False,
            conversion_required=False,
            expected_concepts=['triangle classification', 'side properties'],
            parameters={'sides': sides}
        )
    
    def _generate_quadrilateral_constraint_question(self, difficulty: str) -> QuizQuestion:
        """Generate quadrilateral question using geometric constraints"""
        import random
        
        if difficulty == 'easy':
            # Square
            side = random.randint(2, 8)
            sides = [side, side, side, side]
            angles = [90, 90, 90, 90]
            correct = "Square"
            explanation = "all sides are equal and all angles are 90°"
            
        elif difficulty == 'medium':
            # Rectangle
            length = random.randint(4, 10)
            width = random.randint(2, 6)
            sides = [length, width, length, width]
            angles = [90, 90, 90, 90]
            correct = "Rectangle"
            explanation = "opposite sides are equal and all angles are 90°"
            
        else:  # hard
            # Generate valid quadrilateral
            sides = [random.randint(2, 8) for _ in range(4)]
            angles = [random.randint(60, 120) for _ in range(4)]
            props = self.quadrilateral_analyzer.classify_quadrilateral(sides, angles)
            correct = props.classification
            explanation = ', '.join(props.properties) if props.properties else "based on its side and angle measurements"
        
        question = f"Classify this quadrilateral with sides {sides} cm and angles {angles}°"
        options = ["Square", "Rectangle", "Rhombus", "Parallelogram", "Kite", "Trapezium", "Irregular"]
        random.shuffle(options)
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct,
            explanation=f"This quadrilateral is a {correct.lower()} because {explanation}",
            difficulty=difficulty,
            topic='quadrilaterals',
            shape_type='quadrilateral',
            metric_units='cm',
            south_african_context=False,
            conversion_required=False,
            expected_concepts=['quadrilateral classification', 'side properties', 'angle properties'],
            parameters={'sides': sides, 'angles': angles}
        )
    
    def _generate_circle_constraint_question(self, difficulty: str) -> QuizQuestion:
        """Generate circle question using geometric constraints"""
        import random
        
        radius = random.randint(1, 10)
        
        if difficulty == 'easy':
            question = f"What is the circumference of a circle with radius {radius} cm?"
            correct = round(self.circle_calculator.calculate_circumference(radius), 1)
            explanation = f"Circumference = 2πr = 2 × π × {radius} = {correct} cm"
            
        elif difficulty == 'medium':
            question = f"What is the area of a circle with radius {radius} cm?"
            correct = round(self.circle_calculator.calculate_area(radius), 1)
            explanation = f"Area = πr² = π × {radius}² = {correct} cm²"
            
        else:  # hard
            question = f"What is the chord length of a circle with radius {radius} cm and central angle 60°?"
            correct = round(self.circle_calculator.calculate_chord_length(radius, 60), 1)
            explanation = f"Chord length = 2r sin(θ/2) = 2 × {radius} × sin(30°) = {correct} cm"
        
        # Generate options
        options = [correct, round(correct + random.randint(1, 5), 1), 
                  round(correct - random.randint(1, 5), 1), round(correct * 2, 1)]
        random.shuffle(options)
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            difficulty=difficulty,
            topic='circles',
            shape_type='circle',
            metric_units='cm',
            south_african_context=False,
            conversion_required=False,
            expected_concepts=['circle formulas', 'circumference', 'area', 'chord length'],
            parameters={'radius': radius}
        )
    
    def _generate_angle_constraint_question(self, difficulty: str) -> QuizQuestion:
        """Generate angle question using geometric constraints"""
        import random
        
        if difficulty == 'easy':
            angle = random.choice([30, 45, 60, 90, 120, 150])
        elif difficulty == 'medium':
            angle = random.randint(10, 170)
        else:  # hard
            angle = random.randint(1, 179)
        
        question = f"What type of angle is {angle}°?"
        
        if angle < 90:
            correct = "Acute"
        elif angle == 90:
            correct = "Right"
        elif angle < 180:
            correct = "Obtuse"
        elif angle == 180:
            correct = "Straight"
        else:
            correct = "Reflex"
        
        options = ["Acute", "Right", "Obtuse", "Straight", "Reflex"]
        random.shuffle(options)
        
        explanation = f"An angle of {angle}° is classified as {correct.lower()} because "
        if angle < 90:
            explanation += "it is less than 90°"
        elif angle == 90:
            explanation += "it is exactly 90°"
        elif angle < 180:
            explanation += "it is between 90° and 180°"
        elif angle == 180:
            explanation += "it is exactly 180°"
        else:
            explanation += "it is greater than 180°"
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            difficulty=difficulty,
            topic='angles',
            shape_type='angle',
            metric_units='degrees',
            south_african_context=False,
            conversion_required=False,
            expected_concepts=['angle classification', 'angle measurement'],
            parameters={'angle': angle}
        )
    
    def _generate_conversion_constraint_question(self, difficulty: str) -> QuizQuestion:
        """Generate unit conversion question using metric constraints"""
        import random
        
        conversions = self.metric_conversions
        conversion = random.choice(conversions)
        
        if difficulty == 'easy':
            value = random.randint(1, 9)
        elif difficulty == 'medium':
            value = random.randint(10, 99)
        else:  # hard
            value = random.randint(100, 999)
        
        converted_value = round(value * conversion.conversion_factor, 1)
        
        if conversion.unit_type == 'area':
            question = f"Convert {value} {conversion.from_unit} to {conversion.to_unit}"
            correct = f"{converted_value} {conversion.to_unit}"
            explanation = f"Since 1 {conversion.from_unit} = {conversion.conversion_factor} {conversion.to_unit}, then {value} {conversion.from_unit} = {value} × {conversion.conversion_factor} = {converted_value} {conversion.to_unit}"
        else:
            question = f"Convert {value} {conversion.from_unit} to {conversion.to_unit}"
            correct = f"{converted_value} {conversion.to_unit}"
            explanation = f"Since 1 {conversion.from_unit} = {conversion.conversion_factor} {conversion.to_unit}, then {value} {conversion.from_unit} = {value} × {conversion.conversion_factor} = {converted_value} {conversion.to_unit}"
        
        # Generate options
        options = [correct, f"{converted_value + random.randint(1, 5)} {conversion.to_unit}",
                  f"{converted_value - random.randint(1, 5)} {conversion.to_unit}", 
                  f"{converted_value * 2} {conversion.to_unit}"]
        random.shuffle(options)
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            difficulty=difficulty,
            topic='unit_conversions',
            shape_type='conversion',
            metric_units=conversion.from_unit,
            south_african_context=True,
            conversion_required=True,
            expected_concepts=['unit conversion', 'metric system', 'area conversion'],
            parameters={'value': value, 'conversion': conversion}
        )
    
    def _generate_composite_constraint_question(self, difficulty: str) -> QuizQuestion:
        """Generate composite area question using geometric constraints"""
        import random
        
        if difficulty == 'easy':
            # Rectangle with triangle cutout
            length = random.randint(6, 12)
            width = random.randint(4, 8)
            triangle_base = random.randint(2, length-2)
            triangle_height = random.randint(2, width-2)
            
            rect_area = length * width
            triangle_area = 0.5 * triangle_base * triangle_height
            shaded_area = round(rect_area - triangle_area, 1)
            
            question = f"A rectangle has length {length} cm and width {width} cm. A triangle with base {triangle_base} cm and height {triangle_height} cm is cut out. What is the area of the remaining shaded part?"
            correct = f"{shaded_area} cm²"
            explanation = f"Rectangle area = {length} × {width} = {rect_area} cm². Triangle area = 0.5 × {triangle_base} × {triangle_height} = {triangle_area} cm². Shaded area = {rect_area} - {triangle_area} = {shaded_area} cm²"
            
        elif difficulty == 'medium':
            # Circle with square cutout
            radius = random.randint(3, 8)
            square_side = random.randint(2, radius)
            
            circle_area = round(math.pi * radius**2, 1)
            square_area = square_side**2
            shaded_area = round(circle_area - square_area, 1)
            
            question = f"A circle has radius {radius} cm. A square with side {square_side} cm is cut out. What is the area of the remaining shaded part?"
            correct = f"{shaded_area} cm²"
            explanation = f"Circle area = π × {radius}² = {circle_area} cm². Square area = {square_side}² = {square_area} cm². Shaded area = {circle_area} - {square_area} = {shaded_area} cm²"
            
        else:  # hard
            # Complex composite shape
            rect_length = random.randint(8, 15)
            rect_width = random.randint(6, 10)
            triangle_base = random.randint(3, rect_length-3)
            triangle_height = random.randint(3, rect_width-3)
            circle_radius = random.randint(1, min(triangle_base, triangle_height)//2)
            
            rect_area = rect_length * rect_width
            triangle_area = 0.5 * triangle_base * triangle_height
            circle_area = round(math.pi * circle_radius**2, 1)
            shaded_area = round(rect_area - triangle_area - circle_area, 1)
            
            question = f"A rectangle ({rect_length}×{rect_width} cm) has a triangle (base {triangle_base} cm, height {triangle_height} cm) and a circle (radius {circle_radius} cm) cut out. What is the area of the remaining shaded part?"
            correct = f"{shaded_area} cm²"
            explanation = f"Rectangle area = {rect_length} × {rect_width} = {rect_area} cm². Triangle area = 0.5 × {triangle_base} × {triangle_height} = {triangle_area} cm². Circle area = π × {circle_radius}² = {circle_area} cm². Shaded area = {rect_area} - {triangle_area} - {circle_area} = {shaded_area} cm²"
        
        # Generate options
        options = [correct, f"{shaded_area + random.randint(1, 5)} cm²",
                  f"{shaded_area - random.randint(1, 5)} cm²", f"{shaded_area * 2} cm²"]
        random.shuffle(options)
        
        return QuizQuestion(
            question=question,
            options=options,
            correct_answer=correct,
            explanation=explanation,
            difficulty=difficulty,
            topic='composite_areas',
            shape_type='composite',
            metric_units='cm²',
            south_african_context=True,
            conversion_required=False,
            expected_concepts=['composite areas', 'area calculation', 'shape subtraction'],
            parameters={'shaded_area': shaded_area}
        )
    
    def _generate_fallback_question(self, topic: str, difficulty: str) -> QuizQuestion:
        """Ultimate fallback question generation"""
        return QuizQuestion(
            question=f"Basic {topic} question for {difficulty} level",
            options=["Option A", "Option B", "Option C", "Option D"],
            correct_answer="Option A",
            explanation="This is a fallback question",
            difficulty=difficulty,
            topic=topic,
            shape_type='basic',
            metric_units='cm',
            south_african_context=False,
            conversion_required=False,
            expected_concepts=['basic geometry'],
            parameters={}
        )
    
    def _initialize_question_templates(self) -> List[QuestionTemplate]:
        """Initialize question templates for template-based generation"""
        templates = []
        
        # Triangle templates
        for difficulty in ['easy', 'medium', 'hard']:
            for i in range(20):  # 20 templates per difficulty
                templates.append(QuestionTemplate(
                    template_id=f"triangle_{difficulty}_{i}",
                    question_template=f"Triangle classification question {i}",
                    answer_generator="constraint_based",
                    explanation_template="Based on geometric properties",
                    difficulty=difficulty,
                    shape_type='triangle',
                    parameter_ranges={'sides': (1, 10)},
                    geometric_constraints=['triangle_inequality', 'angle_sum_180']
                ))
        
        return templates
    
    def _initialize_metric_conversions(self) -> List[MetricConversion]:
        """Initialize metric conversion factors"""
        return [
            MetricConversion('mm²', 'cm²', 0.01, 'area'),
            MetricConversion('cm²', 'mm²', 100, 'area'),
            MetricConversion('cm²', 'm²', 0.0001, 'area'),
            MetricConversion('m²', 'cm²', 10000, 'area'),
            MetricConversion('mm', 'cm', 0.1, 'length'),
            MetricConversion('cm', 'mm', 10, 'length'),
            MetricConversion('cm', 'm', 0.01, 'length'),
            MetricConversion('m', 'cm', 100, 'length')
        ]
    
    def _initialize_south_african_contexts(self) -> List[str]:
        """Initialize South African real-world contexts"""
        return [
            "Calculate the area of a soccer field",
            "Find the perimeter of a classroom",
            "Determine the area of a garden plot",
            "Calculate the area of a swimming pool",
            "Find the perimeter of a playground",
            "Determine the area of a parking lot",
            "Calculate the area of a school hall",
            "Find the perimeter of a sports field"
        ]
    
    def _instantiate_template(self, template: QuestionTemplate) -> QuizQuestion:
        """Instantiate a question from a template"""
        # This would implement template instantiation
        # For now, return a basic question
        return self._generate_fallback_question(template.shape_type, template.difficulty)

class GeometryDiagramGenerator:
    """Generates precise geometric diagrams for the Geometry Studio with interactive educational features"""
    
    def __init__(self):
        # Set matplotlib style for professional diagrams
        plt.style.use('default')
        plt.rcParams['figure.facecolor'] = 'white'
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 1.5
        
        # Initialize calculators
        self.triangle_calculator = TriangleCalculator()
        self.circle_calculator = CircleCalculator()
        self.angle_tool = InteractiveAngleTool()
        self.quadrilateral_analyzer = QuadrilateralAnalyzer()
        self.geometry_3d_calculator = Geometry3DCalculator()
        
        # Ensure font configuration is set
        plt.rcParams['font.family'] = 'DejaVu Sans'
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False
        
        # Initialize calculation tools
        self.triangle_calculator = TriangleCalculator()
        self.quadrilateral_analyzer = QuadrilateralAnalyzer()
        self.circle_calculator = CircleCalculator()
        self.angle_tool = InteractiveAngleTool()
        
        # Interactive mode settings
        self.interactive_mode = False
        self.show_calculations = True
        self.show_classifications = True
        
    def _add_enhanced_markings(self, ax, parameters: Dict[str, Any], size_multiplier: float = 1):
        """Add enhanced markings like hash marks, arrows, angle indicators"""
        show_markings = parameters.get('showMarkings', False)
        if not show_markings:
            return
            
        # Get marking parameters
        equal_sides = parameters.get('equalSides', [])
        parallel_sides = parameters.get('parallelSides', [])
        right_angles = parameters.get('rightAngles', [])
        angle_measurements = parameters.get('angleMeasurements', {})
        
        # Add hash marks for equal sides
        for side in equal_sides:
            self._draw_hash_marks(ax, side, size_multiplier)
            
        # Add arrows for parallel sides
        for side in parallel_sides:
            self._draw_parallel_arrows(ax, side, size_multiplier)
            
        # Add right angle squares
        for angle in right_angles:
            self._draw_right_angle_square(ax, angle, size_multiplier)
            
        # Add angle measurements
        for angle_id, measurement in angle_measurements.items():
            self._draw_angle_measurement(ax, angle_id, measurement, size_multiplier)
    
    def _draw_hash_marks(self, ax, side_coords, size_multiplier):
        """Draw hash marks on a side to indicate equal length"""
        if len(side_coords) != 2:
            return
            
        x1, y1 = side_coords[0]
        x2, y2 = side_coords[1]
        
        # Calculate midpoint and perpendicular direction
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        # Perpendicular vector
        dx = x2 - x1
        dy = y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        if length == 0:
            return
            
        perp_x = -dy / length
        perp_y = dx / length
        
        # Draw hash marks
        mark_length = 0.5 * size_multiplier
        offset = 0.3 * size_multiplier
        
        for i in range(3):  # 3 hash marks
            t = (i + 1) / 4  # Position along the line
            mark_x = x1 + t * dx
            mark_y = y1 + t * dy
            
            # Draw hash mark perpendicular to the line
            ax.plot([mark_x - perp_x * mark_length/2, mark_x + perp_x * mark_length/2],
                   [mark_y - perp_y * mark_length/2, mark_y + perp_y * mark_length/2],
                   'k-', linewidth=2 * size_multiplier)
    
    def _draw_parallel_arrows(self, ax, side_coords, size_multiplier):
        """Draw arrows to indicate parallel sides"""
        if len(side_coords) != 2:
            return
            
        x1, y1 = side_coords[0]
        x2, y2 = side_coords[1]
        
        # Calculate direction
        dx = x2 - x1
        dy = y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        if length == 0:
            return
            
        # Normalize direction
        dx /= length
        dy /= length
        
        # Draw arrows at 1/3 and 2/3 positions
        arrow_length = 0.8 * size_multiplier
        for t in [1/3, 2/3]:
            arrow_x = x1 + t * (x2 - x1)
            arrow_y = y1 + t * (y2 - y1)
            
            # Draw arrow
            ax.annotate('', xy=(arrow_x + dx * arrow_length, arrow_y + dy * arrow_length),
                       xytext=(arrow_x, arrow_y),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=2 * size_multiplier))
    
    def _draw_right_angle_square(self, ax, angle_coords, size_multiplier):
        """Draw a square to indicate right angle"""
        if len(angle_coords) != 3:
            return
            
        vertex = angle_coords[1]  # Middle point is the vertex
        side1 = np.array(angle_coords[0]) - np.array(vertex)
        side2 = np.array(angle_coords[2]) - np.array(vertex)
        
        # Normalize sides
        side1 = side1 / np.linalg.norm(side1)
        side2 = side2 / np.linalg.norm(side2)
        
        # Square size
        square_size = 0.5 * size_multiplier
        
        # Draw square
        square_vertices = [
            vertex,
            vertex + side1 * square_size,
            vertex + side1 * square_size + side2 * square_size,
            vertex + side2 * square_size
        ]
        
        square = patches.Polygon(square_vertices, fill=False, edgecolor='red', linewidth=2 * size_multiplier)
        ax.add_patch(square)
    
    def _draw_angle_measurement(self, ax, angle_id, measurement, size_multiplier):
        """Draw angle measurement text"""
        # This would need angle coordinates - simplified for now
        ax.text(0, 0, f"{measurement}°", fontsize=12 * size_multiplier, 
               fontweight='bold', ha='center', va='center',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
        
    def generate_diagram(self, diagram_type: str, dimension: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a geometric diagram (2D or 3D) and return structured result
        
        Args:
            diagram_type: Type of diagram (point, line, ray, segment, angle, circle, etc.)
            dimension: '2d' or '3d'
            parameters: Dictionary containing diagram parameters
            
        Returns:
            Dictionary with success status, image data, and metadata
        """
        try:
            if dimension.lower() == '2d':
                image_base64 = self.generate_2d_diagram(diagram_type, parameters)
                return {
                    "success": True,
                    "diagram_type": diagram_type,
                    "dimension": "2d",
                    "image_data": f"data:image/png;base64,{image_base64}"
                }
            elif dimension.lower() == '3d':
                plotly_json = self.generate_3d_diagram(diagram_type, parameters)
                # Get calculations from the 3D diagram
                calculations = {}
                try:
                    if diagram_type in ['cube', 'rectangular_prism']:
                        calculations = self.geometry_3d_calculator.get_all_calculations(diagram_type, parameters)
                except Exception as e:
                    print(f"Warning: Could not get 3D calculations: {e}")
                
                return {
                    "success": True,
                    "diagram_type": diagram_type,
                    "dimension": "3d",
                    "plotly_data": plotly_json,
                    "calculations": calculations
                }
            else:
                return {
                    "success": False,
                    "error": f"Invalid dimension: {dimension}. Must be '2d' or '3d'"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error generating {dimension} diagram: {str(e)}"
            }

    def generate_2d_diagram(self, diagram_type: str, parameters: Dict[str, Any]) -> str:
        """
        Generate a 2D geometric diagram and return as base64 encoded image
        
        Args:
            diagram_type: Type of diagram (point, line, ray, segment, angle, circle, etc.)
            parameters: Dictionary containing diagram parameters
            
        Returns:
            Base64 encoded PNG image string
        """
        try:
            # Ensure font configuration is set
            plt.rcParams['font.family'] = 'DejaVu Sans'
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
            plt.rcParams['axes.unicode_minus'] = False
            
            # Get size multiplier (default 1, but can be 3 for informal assessment)
            size_multiplier = parameters.get('size', 1)
            
            # Keep canvas size the same, scale objects instead
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            
            # Keep axis limits the same
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            
            # Scale font sizes
            base_font_size = 10 * size_multiplier
            plt.rcParams['font.size'] = base_font_size
            
            # Generate diagram based on type
            if diagram_type == 'point':
                self._draw_point(ax, parameters, size_multiplier)
            elif diagram_type == 'line':
                self._draw_line(ax, parameters, size_multiplier)
            elif diagram_type == 'ray':
                self._draw_ray(ax, parameters, size_multiplier)
            elif diagram_type == 'segment':
                self._draw_segment(ax, parameters, size_multiplier)
            elif diagram_type == 'parallel_lines':
                self._draw_parallel_lines(ax, parameters, size_multiplier)
            elif diagram_type == 'perpendicular_lines':
                self._draw_perpendicular_lines(ax, parameters, size_multiplier)
            elif diagram_type == 'angle':
                self._draw_angle(ax, parameters, size_multiplier)
            elif diagram_type == 'angle_arms':
                self._draw_angle_arms(ax, parameters, size_multiplier)
            elif diagram_type == 'circle':
                self._draw_circle(ax, parameters, size_multiplier)
            elif diagram_type == 'chord':
                self._draw_chord(ax, parameters, size_multiplier)
            elif diagram_type == 'segment':
                self._draw_segment(ax, parameters, size_multiplier)
            elif diagram_type == 'radius':
                self._draw_radius(ax, parameters, size_multiplier)
            elif diagram_type == 'diameter':
                self._draw_diameter(ax, parameters, size_multiplier)
            elif diagram_type == 'arc':
                self._draw_arc(ax, parameters, size_multiplier)
            elif diagram_type == 'equilateral_triangle':
                self._draw_equilateral_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'isosceles_triangle':
                self._draw_isosceles_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'scalene_triangle':
                self._draw_scalene_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'right_triangle':
                self._draw_right_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'acute_triangle':
                self._draw_acute_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'obtuse_triangle':
                self._draw_obtuse_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'square':
                self._draw_square(ax, parameters, size_multiplier)
            elif diagram_type == 'rectangle':
                self._draw_rectangle(ax, parameters, size_multiplier)
            elif diagram_type == 'rhombus':
                self._draw_rhombus(ax, parameters, size_multiplier)
            elif diagram_type == 'parallelogram':
                self._draw_parallelogram(ax, parameters, size_multiplier)
            elif diagram_type == 'kite':
                self._draw_kite(ax, parameters, size_multiplier)
            elif diagram_type == 'trapezium':
                self._draw_trapezium(ax, parameters, size_multiplier)
            elif diagram_type == 'triangle':
                self._draw_triangle(ax, parameters, size_multiplier)
            elif diagram_type == 'quadrilateral':
                self._draw_quadrilateral(ax, parameters, size_multiplier)
            else:
                raise ValueError(f"Unsupported diagram type: {diagram_type}")
            
            # Add enhanced markings if requested
            self._add_enhanced_markings(ax, parameters, size_multiplier)
            
            # Convert to base64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
            plt.close(fig)
            
            return image_base64
            
        except Exception as e:
            plt.close('all')
            raise Exception(f"Error generating 2D diagram: {str(e)}")
    
    def generate_3d_diagram(self, diagram_type: str, parameters: Dict[str, Any]) -> str:
        """
        Generate a 3D geometric diagram and return as JSON for plotly
        
        Args:
            diagram_type: Type of 3D diagram (cube, sphere, cylinder, etc.)
            parameters: Dictionary containing diagram parameters
            
        Returns:
            JSON string of plotly figure
        """
        try:
            if diagram_type == 'cube':
                fig = self._create_cube(parameters)
            elif diagram_type == 'rectangular_prism':
                fig = self._create_rectangular_prism(parameters)
            elif diagram_type == 'sphere':
                fig = self._create_sphere(parameters)
            elif diagram_type == 'cylinder':
                fig = self._create_cylinder(parameters)
            elif diagram_type == 'pyramid':
                fig = self._create_pyramid(parameters)
            else:
                raise ValueError(f"Unsupported 3D diagram type: {diagram_type}")
            
            import plotly.utils
            return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            
        except Exception as e:
            raise Exception(f"Error generating 3D diagram: {str(e)}")
    
    # 2D Drawing Methods
    def _draw_point(self, ax, params, size_multiplier=1):
        """Draw a point with label"""
        x, y = params.get('x', 0), params.get('y', 0)
        # Scale the coordinates
        x *= size_multiplier
        y *= size_multiplier
        label = params.get('label', 'P')
        color = params.get('color', 'red')
        
        ax.plot(x, y, 'o', color=color, markersize=8, markeredgecolor='black', markeredgewidth=1)
        ax.annotate(label, (x, y), xytext=(5, 5), textcoords='offset points', 
                   fontsize=12 * size_multiplier, fontweight='bold')
    
    def _draw_line(self, ax, params, size_multiplier=1):
        """Draw a line with arrows on both ends"""
        x1, y1 = params.get('start', [0, 0])
        x2, y2 = params.get('end', [5, 0])
        # Scale the coordinates
        x1 *= size_multiplier
        y1 *= size_multiplier
        x2 *= size_multiplier
        y2 *= size_multiplier
        label = params.get('label', 'AB')
        color = params.get('color', 'blue')
        
        # Draw line with arrows
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='<->', color=color, lw=2))
        
        # Add labels
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.annotate(label, (mid_x, mid_y), xytext=(0, 10), 
                   textcoords='offset points', ha='center', fontsize=12, fontweight='bold')
    
    def _draw_ray(self, ax, params, size_multiplier=1):
        """Draw a ray with starting point and arrow"""
        x1, y1 = params.get('start', [0, 0])
        x2, y2 = params.get('end', [5, 0])
        label = params.get('label', 'AB')
        color = params.get('color', 'green')
        
        # Draw starting point
        ax.plot(x1, y1, 'o', color=color, markersize=6, markeredgecolor='black', markeredgewidth=1)
        
        # Draw ray with arrow
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=color, lw=2))
        
        # Add labels
        ax.annotate(label.split()[0] if ' ' in label else label[0], (x1, y1), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        ax.annotate(label.split()[1] if ' ' in label else label[1], (x2, y2), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    
    def _draw_segment(self, ax, params, size_multiplier=1):
        """Draw a line segment with endpoints"""
        x1, y1 = params.get('start', [0, 0])
        x2, y2 = params.get('end', [5, 0])
        # Scale the coordinates
        x1 *= size_multiplier
        y1 *= size_multiplier
        x2 *= size_multiplier
        y2 *= size_multiplier
        label = params.get('label', 'AB')
        color = params.get('color', 'purple')
        
        # Draw endpoints
        ax.plot(x1, y1, 'o', color=color, markersize=6, markeredgecolor='black', markeredgewidth=1)
        ax.plot(x2, y2, 'o', color=color, markersize=6, markeredgecolor='black', markeredgewidth=1)
        
        # Draw segment
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2)
        
        # Add labels
        ax.annotate(label.split()[0] if ' ' in label else label[0], (x1, y1), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        ax.annotate(label.split()[1] if ' ' in label else label[1], (x2, y2), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    
    def _draw_parallel_lines(self, ax, params, size_multiplier=1):
        """Draw two parallel lines"""
        line1 = params.get('line1', {'start': [0, 0], 'end': [5, 0]})
        line2 = params.get('line2', {'start': [0, 2], 'end': [5, 2]})
        color = params.get('color', 'orange')
        
        # Draw first line
        ax.plot([line1['start'][0], line1['end'][0]], 
                [line1['start'][1], line1['end'][1]], color=color, linewidth=2)
        
        # Draw second line
        ax.plot([line2['start'][0], line2['end'][0]], 
                [line2['start'][1], line2['end'][1]], color=color, linewidth=2)
        
        # Add parallel symbol
        mid1_x, mid1_y = (line1['start'][0] + line1['end'][0]) / 2, (line1['start'][1] + line1['end'][1]) / 2
        mid2_x, mid2_y = (line2['start'][0] + line2['end'][0]) / 2, (line2['start'][1] + line2['end'][1]) / 2
        
        ax.annotate('∥', (mid1_x, mid1_y), xytext=(0, 10), textcoords='offset points', 
                   ha='center', fontsize=14 * size_multiplier, fontweight='bold')
        ax.annotate('∥', (mid2_x, mid2_y), xytext=(0, -15), textcoords='offset points', 
                   ha='center', fontsize=14 * size_multiplier, fontweight='bold')
    
    def _draw_perpendicular_lines(self, ax, params, size_multiplier=1):
        """Draw two perpendicular lines"""
        line1 = params.get('line1', {'start': [0, 0], 'end': [5, 0]})
        line2 = params.get('line2', {'start': [2.5, 0], 'end': [2.5, 3]})
        color = params.get('color', 'red')
        
        # Draw lines
        ax.plot([line1['start'][0], line1['end'][0]], 
                [line1['start'][1], line1['end'][1]], color=color, linewidth=2)
        ax.plot([line2['start'][0], line2['end'][0]], 
                [line2['start'][1], line2['end'][1]], color=color, linewidth=2)
        
        # Draw right angle symbol
        intersection = params.get('intersection', [2.5, 0])
        size = 0.3
        square = patches.Rectangle((intersection[0] - size/2, intersection[1] - size/2), 
                                 size, size, fill=False, edgecolor=color, linewidth=1.5)
        ax.add_patch(square)
    
    def _draw_angle(self, ax, params, size_multiplier=1):
        """Draw an angle with proper arc"""
        vertex = params.get('vertex', [0, 0])
        measurement = params.get('measurement', 45)
        angle_type = params.get('angle_type', 'acute')  # acute, right, obtuse, straight, reflex
        color = params.get('color', 'blue')
        
        # Calculate arm positions based on measurement
        import math
        arm1 = [2, 0]  # Fixed horizontal arm
        arm2 = [2 * math.cos(math.radians(measurement)), 2 * math.sin(math.radians(measurement))]
        
        # Draw arms
        ax.plot([vertex[0], arm1[0]], [vertex[1], arm1[1]], color=color, linewidth=2)
        ax.plot([vertex[0], arm2[0]], [vertex[1], arm2[1]], color=color, linewidth=2)
        
        # Draw vertex
        ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw angle arc
        self._draw_angle_arc(ax, vertex, arm1, arm2, angle_type, color)
        
        # Add angle measurement label
        mid_angle = measurement / 2
        label_x = 0.8 * math.cos(math.radians(mid_angle))
        label_y = 0.8 * math.sin(math.radians(mid_angle))
        ax.text(label_x, label_y, f"{measurement}°", fontsize=12 * size_multiplier, 
               fontweight='bold', ha='center', va='center',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
        
        # Add labels
        ax.annotate('B', vertex, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('A', arm1, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('C', arm2, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_angle_arc(self, ax, vertex, arm1, arm2, angle_type, color):
        """Draw the arc for an angle"""
        # Calculate angle between arms
        v1 = np.array(arm1) - np.array(vertex)
        v2 = np.array(arm2) - np.array(vertex)
        
        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])
        
        # Determine arc parameters based on angle type
        radius = 0.5
        if angle_type == 'right':
            # Draw square for right angle
            square = patches.Rectangle((vertex[0] - radius/2, vertex[1] - radius/2), 
                                     radius, radius, fill=False, edgecolor=color, linewidth=1.5)
            ax.add_patch(square)
        elif angle_type == 'revolution':
            # Draw full circle for revolution (360°)
            circle = Circle(vertex, radius, fill=False, edgecolor=color, linewidth=1.5)
            ax.add_patch(circle)
        else:
            # Draw arc for other angle types
            arc = Arc(vertex, 2*radius, 2*radius, angle=0, 
                     theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                     color=color, linewidth=1.5)
            ax.add_patch(arc)
    
    def _draw_angle_arms(self, ax, params, size_multiplier=1):
        """Draw an angle with labeled arms (for 'Arms of an Angle' tool)"""
        vertex = params.get('vertex', [0, 0])
        arm1 = params.get('arm1', [3, 0])
        arm2 = params.get('arm2', [2, 2])
        color = params.get('color', 'blue')
        
        # Draw arms as rays (extending beyond the endpoints)
        # Calculate direction vectors
        v1 = np.array(arm1) - np.array(vertex)
        v2 = np.array(arm2) - np.array(vertex)
        
        # Normalize and extend
        v1_norm = v1 / np.linalg.norm(v1)
        v2_norm = v2 / np.linalg.norm(v2)
        
        # Extend arms by 1.5x their original length
        arm1_extended = vertex + v1_norm * np.linalg.norm(v1) * 1.5
        arm2_extended = vertex + v2_norm * np.linalg.norm(v2) * 1.5
        
        # Draw the arms
        ax.plot([vertex[0], arm1_extended[0]], [vertex[1], arm1_extended[1]], 
                color=color, linewidth=3, solid_capstyle='round')
        ax.plot([vertex[0], arm2_extended[0]], [vertex[1], arm2_extended[1]], 
                color=color, linewidth=3, solid_capstyle='round')
        
        # Draw vertex as a point
        ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=8, 
               markeredgecolor='black', markeredgewidth=2)
        
        # Add arrowheads to show direction
        # Arrow for arm1
        arrow1 = patches.FancyArrowPatch(vertex, arm1_extended, 
                                       arrowstyle='->', mutation_scale=20, 
                                       color=color, linewidth=2)
        ax.add_patch(arrow1)
        
        # Arrow for arm2  
        arrow2 = patches.FancyArrowPatch(vertex, arm2_extended,
                                       arrowstyle='->', mutation_scale=20,
                                       color=color, linewidth=2)
        ax.add_patch(arrow2)
        
        # Label the arms
        mid1 = vertex + v1_norm * np.linalg.norm(v1) * 0.7
        mid2 = vertex + v2_norm * np.linalg.norm(v2) * 0.7
        
        ax.annotate('Arm 1', mid1, xytext=(10, 5), textcoords='offset points',
                   fontsize=12, fontweight='bold', color=color,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
        ax.annotate('Arm 2', mid2, xytext=(10, 5), textcoords='offset points',
                   fontsize=12, fontweight='bold', color=color,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
        
        # Label the vertex
        ax.annotate('Vertex', vertex, xytext=(0, -20), textcoords='offset points',
                   fontsize=10, fontweight='bold', ha='center',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.8))
    
    def _draw_circle(self, ax, params, size_multiplier=1):
        """Draw a circle with center and radius"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        color = params.get('color', 'blue')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_chord(self, ax, params, size_multiplier=1):
        """Draw a chord (line segment connecting two points on circle)"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        point1 = params.get('point1', [1.4, 1.4])
        point2 = params.get('point2', [1.4, -1.4])
        color = params.get('color', '#3B82F6')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Draw chord
        ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 
                color='#EF4444', linewidth=3, solid_capstyle='round')
        
        # Draw points
        ax.plot(point1[0], point1[1], 'o', color='#EF4444', markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        ax.plot(point2[0], point2[1], 'o', color='#EF4444', markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('A', point1, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('B', point2, xytext=(5, -10), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_segment(self, ax, params, size_multiplier=1):
        """Draw a segment (region between chord and arc)"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        point1 = params.get('point1', [1.4, 1.4])
        point2 = params.get('point2', [1.4, -1.4])
        color = params.get('color', '#3B82F6')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Draw chord
        ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 
                color='#EF4444', linewidth=3, solid_capstyle='round')
        
        # Draw segment (filled area between chord and arc)
        # Calculate arc path
        theta1 = np.arctan2(point1[1] - center[1], point1[0] - center[0])
        theta2 = np.arctan2(point2[1] - center[1], point2[0] - center[0])
        
        # Create arc path for segment
        arc_path = patches.Arc(center, 2*radius, 2*radius, angle=0, 
                              theta1=np.degrees(theta1), theta2=np.degrees(theta2),
                              color='#10B981', linewidth=2)
        ax.add_patch(arc_path)
        
        # Fill the segment area
        segment_vertices = [point1, point2, center]
        segment = patches.Polygon(segment_vertices, fill=True, 
                                facecolor='#10B981', alpha=0.3, edgecolor='none')
        ax.add_patch(segment)
        
        # Draw points
        ax.plot(point1[0], point1[1], 'o', color='#EF4444', markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        ax.plot(point2[0], point2[1], 'o', color='#EF4444', markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('A', point1, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('B', point2, xytext=(5, -10), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_radius(self, ax, params, size_multiplier=1):
        """Draw a radius (line from center to edge)"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        endpoint = params.get('endpoint', [0, 2])
        color = params.get('color', '#10B981')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Draw radius
        ax.plot([center[0], endpoint[0]], [center[1], endpoint[1]], 
                color=color, linewidth=3, solid_capstyle='round')
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw endpoint
        ax.plot(endpoint[0], endpoint[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('A', endpoint, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_diameter(self, ax, params, size_multiplier=1):
        """Draw a diameter (chord passing through center)"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        point1 = params.get('point1', [-2, 0])
        point2 = params.get('point2', [2, 0])
        color = params.get('color', '#F97316')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Draw diameter
        ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 
                color=color, linewidth=3, solid_capstyle='round')
        
        # Draw points
        ax.plot(point1[0], point1[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        ax.plot(point2[0], point2[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('A', point1, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('B', point2, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_arc(self, ax, params, size_multiplier=1):
        """Draw an arc (part of circumference between two points)"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        point1 = params.get('point1', [1.4, 1.4])
        point2 = params.get('point2', [1.4, -1.4])
        color = params.get('color', '#EF4444')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Calculate arc angles
        theta1 = np.arctan2(point1[1] - center[1], point1[0] - center[0])
        theta2 = np.arctan2(point2[1] - center[1], point2[0] - center[0])
        
        # Draw arc
        arc = patches.Arc(center, 2*radius, 2*radius, angle=0, 
                         theta1=np.degrees(theta1), theta2=np.degrees(theta2),
                         color=color, linewidth=3)
        ax.add_patch(arc)
        
        # Draw points
        ax.plot(point1[0], point1[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        ax.plot(point2[0], point2[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('A', point1, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('B', point2, xytext=(5, -10), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_triangle(self, ax, params, size_multiplier=1):
        """Draw a triangle"""
        vertices = params.get('vertices', [[0, 0], [3, 0], [1.5, 2.5]])
        color = params.get('color', 'green')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_equilateral_triangle(self, ax, params, size_multiplier=1):
        """Draw an equilateral triangle (all sides equal, 60° angles)"""
        vertices = params.get('vertices', [[0, 1.73], [-1.5, -0.87], [1.5, -0.87]])
        color = params.get('color', '#3B82F6')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Add angle markers (60°)
        for i in range(3):
            vertex = vertices[i]
            prev_vertex = vertices[(i-1) % 3]
            next_vertex = vertices[(i+1) % 3]
            
            # Calculate angle bisector for arc
            v1 = np.array(prev_vertex) - np.array(vertex)
            v2 = np.array(next_vertex) - np.array(vertex)
            v1_norm = v1 / np.linalg.norm(v1)
            v2_norm = v2 / np.linalg.norm(v2)
            bisector = (v1_norm + v2_norm) / 2
            bisector = bisector / np.linalg.norm(bisector) * 0.3
            
            # Draw 60° arc
            angle1 = np.arctan2(v1[1], v1[0])
            angle2 = np.arctan2(v2[1], v2[0])
            arc = patches.Arc(vertex, 0.6, 0.6, angle=0, 
                             theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                             color=color, linewidth=1.5)
            ax.add_patch(arc)
    
    def _draw_isosceles_triangle(self, ax, params, size_multiplier=1):
        """Draw an isosceles triangle (two equal sides and angles)"""
        vertices = params.get('vertices', [[0, 2], [-1.5, -1], [1.5, -1]])
        color = params.get('color', '#10B981')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Mark equal sides with small lines
        # Side AB and AC are equal
        mid_ab = [(vertices[0][0] + vertices[1][0])/2, (vertices[0][1] + vertices[1][1])/2]
        mid_ac = [(vertices[0][0] + vertices[2][0])/2, (vertices[0][1] + vertices[2][1])/2]
        
        # Draw small lines to indicate equal sides
        ax.plot([mid_ab[0]-0.1, mid_ab[0]+0.1], [mid_ab[1], mid_ab[1]], 
                color=color, linewidth=2)
        ax.plot([mid_ac[0]-0.1, mid_ac[0]+0.1], [mid_ac[1], mid_ac[1]], 
                color=color, linewidth=2)
    
    def _draw_scalene_triangle(self, ax, params, size_multiplier=1):
        """Draw a scalene triangle (all sides and angles different)"""
        vertices = params.get('vertices', [[-1.5, 1], [2, 0.5], [0, -1.5]])
        color = params.get('color', '#F97316')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_right_triangle(self, ax, params, size_multiplier=1):
        """Draw a right-angled triangle (one 90° angle)"""
        vertices = params.get('vertices', [[0, 0], [3, 0], [0, 2]])
        color = params.get('color', '#EF4444')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Draw right angle square at vertex A (0,0)
        square_size = 0.3
        square = patches.Rectangle((square_size/2, square_size/2), square_size, square_size, 
                                 fill=False, edgecolor=color, linewidth=1.5)
        ax.add_patch(square)
    
    def _draw_acute_triangle(self, ax, params, size_multiplier=1):
        """Draw an acute triangle (all angles < 90°)"""
        vertices = params.get('vertices', [[0, 2], [-1.2, -0.5], [1.2, -0.5]])
        color = params.get('color', '#8B5CF6')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Add angle arcs to show all angles are acute
        for i in range(3):
            vertex = vertices[i]
            prev_vertex = vertices[(i-1) % 3]
            next_vertex = vertices[(i+1) % 3]
            
            v1 = np.array(prev_vertex) - np.array(vertex)
            v2 = np.array(next_vertex) - np.array(vertex)
            angle1 = np.arctan2(v1[1], v1[0])
            angle2 = np.arctan2(v2[1], v2[0])
            
            arc = patches.Arc(vertex, 0.4, 0.4, angle=0, 
                             theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                             color=color, linewidth=1.5)
            ax.add_patch(arc)
    
    def _draw_obtuse_triangle(self, ax, params, size_multiplier=1):
        """Draw an obtuse triangle (one angle > 90°)"""
        vertices = params.get('vertices', [[-1, 1], [2, 0.5], [0.5, -1.5]])
        color = params.get('color', '#EC4899')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Mark the obtuse angle (at vertex B) with a larger arc
        vertex = vertices[1]  # Vertex B
        prev_vertex = vertices[0]  # Vertex A
        next_vertex = vertices[2]  # Vertex C
        
        v1 = np.array(prev_vertex) - np.array(vertex)
        v2 = np.array(next_vertex) - np.array(vertex)
        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])
        
        # Draw larger arc for obtuse angle
        arc = patches.Arc(vertex, 0.6, 0.6, angle=0, 
                         theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                         color=color, linewidth=2)
        ax.add_patch(arc)
    
    def _draw_quadrilateral(self, ax, params, size_multiplier=1):
        """Draw a quadrilateral"""
        vertices = params.get('vertices', [[0, 0], [3, 0], [3, 2], [0, 2]])
        color = params.get('color', 'purple')
        
        # Draw quadrilateral
        quad = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(quad)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
    
    def _draw_square(self, ax, params, size_multiplier=1):
        """Draw a square (all sides equal, all angles 90°)"""
        vertices = params.get('vertices', [[-1, -1], [1, -1], [1, 1], [-1, 1]])
        color = params.get('color', '#3B82F6')
        
        # Draw square
        square = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(square)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Draw right angle squares at each corner
        square_size = 0.2
        for i, vertex in enumerate(vertices):
            square = patches.Rectangle((vertex[0] - square_size/2, vertex[1] - square_size/2), 
                                     square_size, square_size, fill=False, edgecolor=color, linewidth=1.5)
            ax.add_patch(square)
    
    def _draw_rectangle(self, ax, params, size_multiplier=1):
        """Draw a rectangle (opposite sides equal, all angles 90°)"""
        vertices = params.get('vertices', [[-1.5, -1], [1.5, -1], [1.5, 1], [-1.5, 1]])
        color = params.get('color', '#10B981')
        
        # Draw rectangle
        rectangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(rectangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Draw right angle squares at each corner
        square_size = 0.2
        for i, vertex in enumerate(vertices):
            square = patches.Rectangle((vertex[0] - square_size/2, vertex[1] - square_size/2), 
                                     square_size, square_size, fill=False, edgecolor=color, linewidth=1.5)
            ax.add_patch(square)
    
    def _draw_rhombus(self, ax, params, size_multiplier=1):
        """Draw a rhombus (all sides equal, opposite angles equal)"""
        vertices = params.get('vertices', [[0, 1.5], [1.5, 0], [0, -1.5], [-1.5, 0]])
        color = params.get('color', '#F97316')
        
        # Draw rhombus
        rhombus = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(rhombus)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Mark equal sides with small lines
        for i in range(4):
            mid_point = [(vertices[i][0] + vertices[(i+1)%4][0])/2, 
                        (vertices[i][1] + vertices[(i+1)%4][1])/2]
            # Calculate perpendicular direction for side markers
            v = np.array(vertices[(i+1)%4]) - np.array(vertices[i])
            perp = np.array([-v[1], v[0]]) / np.linalg.norm(v) * 0.1
            marker_start = np.array(mid_point) - perp
            marker_end = np.array(mid_point) + perp
            ax.plot([marker_start[0], marker_end[0]], [marker_start[1], marker_end[1]], 
                    color=color, linewidth=2)
    
    def _draw_parallelogram(self, ax, params, size_multiplier=1):
        """Draw a parallelogram (opposite sides parallel and equal)"""
        vertices = params.get('vertices', [[-1.5, -0.5], [1.5, -0.5], [2.5, 1.5], [-0.5, 1.5]])
        color = params.get('color', '#8B5CF6')
        
        # Draw parallelogram
        parallelogram = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(parallelogram)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Mark parallel sides with arrows
        # Top and bottom sides (parallel)
        mid_top = [(vertices[2][0] + vertices[3][0])/2, (vertices[2][1] + vertices[3][1])/2]
        mid_bottom = [(vertices[0][0] + vertices[1][0])/2, (vertices[0][1] + vertices[1][1])/2]
        
        # Draw parallel arrows
        ax.annotate('', xy=(mid_top[0] + 0.3, mid_top[1]), xytext=(mid_top[0] - 0.3, mid_top[1]),
                   arrowprops=dict(arrowstyle='<->', color=color, lw=1.5))
        ax.annotate('', xy=(mid_bottom[0] + 0.3, mid_bottom[1]), xytext=(mid_bottom[0] - 0.3, mid_bottom[1]),
                   arrowprops=dict(arrowstyle='<->', color=color, lw=1.5))
    
    def _draw_kite(self, ax, params, size_multiplier=1):
        """Draw a kite (two pairs of adjacent sides equal)"""
        vertices = params.get('vertices', [[0, 1.5], [1, 0], [0, -0.5], [-1, 0]])
        color = params.get('color', '#EF4444')
        
        # Draw kite
        kite = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(kite)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Mark equal adjacent sides
        # Sides AB and AD are equal
        mid_ab = [(vertices[0][0] + vertices[1][0])/2, (vertices[0][1] + vertices[1][1])/2]
        mid_ad = [(vertices[0][0] + vertices[3][0])/2, (vertices[0][1] + vertices[3][1])/2]
        
        # Draw small lines to indicate equal sides
        ax.plot([mid_ab[0]-0.1, mid_ab[0]+0.1], [mid_ab[1], mid_ab[1]], 
                color=color, linewidth=2)
        ax.plot([mid_ad[0]-0.1, mid_ad[0]+0.1], [mid_ad[1], mid_ad[1]], 
                color=color, linewidth=2)
        
        # Sides BC and CD are equal
        mid_bc = [(vertices[1][0] + vertices[2][0])/2, (vertices[1][1] + vertices[2][1])/2]
        mid_cd = [(vertices[2][0] + vertices[3][0])/2, (vertices[2][1] + vertices[3][1])/2]
        
        ax.plot([mid_bc[0]-0.1, mid_bc[0]+0.1], [mid_bc[1], mid_bc[1]], 
                color=color, linewidth=2)
        ax.plot([mid_cd[0]-0.1, mid_cd[0]+0.1], [mid_cd[1], mid_cd[1]], 
                color=color, linewidth=2)
    
    def _draw_trapezium(self, ax, params, size_multiplier=1):
        """Draw a trapezium (one pair of parallel sides)"""
        vertices = params.get('vertices', [[-1.5, -1], [1.5, -1], [1, 1], [-1, 1]])
        color = params.get('color', '#EC4899')
        
        # Draw trapezium
        trapezium = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(trapezium)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10 * size_multiplier, fontweight='bold')
        
        # Mark parallel sides with arrows
        # Top and bottom sides are parallel
        mid_top = [(vertices[2][0] + vertices[3][0])/2, (vertices[2][1] + vertices[3][1])/2]
        mid_bottom = [(vertices[0][0] + vertices[1][0])/2, (vertices[0][1] + vertices[1][1])/2]
        
        # Draw parallel arrows
        ax.annotate('', xy=(mid_top[0] + 0.3, mid_top[1]), xytext=(mid_top[0] - 0.3, mid_top[1]),
                   arrowprops=dict(arrowstyle='<->', color=color, lw=1.5))
        ax.annotate('', xy=(mid_bottom[0] + 0.3, mid_bottom[1]), xytext=(mid_bottom[0] - 0.3, mid_bottom[1]),
                   arrowprops=dict(arrowstyle='<->', color=color, lw=1.5))
    
    # 3D Drawing Methods
    def _create_cube(self, params):
        """Create a 3D cube using plotly with educational features"""
        side_length = params.get('side_length', params.get('size', 2))
        center = params.get('center', [0, 0, 0])
        show_calculations = params.get('show_calculations', True)
        show_net = params.get('show_net', False)
        
        # Calculate educational values
        calculations = self.geometry_3d_calculator.get_all_calculations('cube', {'side_length': side_length})
        
        # Define cube vertices
        vertices = np.array([
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # bottom face
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # top face
        ]) * side_length / 2 + np.array(center)
        
        # Define faces
        faces = [
            [0, 1, 2, 3],  # bottom
            [4, 5, 6, 7],  # top
            [0, 1, 5, 4],  # front
            [2, 3, 7, 6],  # back
            [0, 3, 7, 4],  # left
            [1, 2, 6, 5]   # right
        ]
        
        # Create the 3D cube
        fig = go.Figure(data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=[face[0] for face in faces],
                j=[face[1] for face in faces],
                k=[face[2] for face in faces],
                opacity=0.7,
                color='lightblue',
                name='Cube'
            )
        ])
        
        # Add dimension labels
        if show_calculations:
            # Add side length labels
            fig.add_trace(go.Scatter3d(
                x=[vertices[0, 0], vertices[1, 0]],
                y=[vertices[0, 1], vertices[1, 1]],
                z=[vertices[0, 2], vertices[1, 2]],
                mode='lines+markers+text',
                line=dict(color='red', width=4),
                text=[f'{side_length}cm', f'{side_length}cm'],
                textposition='top center',
                name='Side Length',
                showlegend=False
            ))
        
        # Update layout with educational information
        title_text = f'3D Cube (Side: {side_length}cm)'
        if show_calculations:
            title_text += f'<br>Surface Area: {calculations["surface_area"]}cm² | Volume: {calculations["volume"]}cm³ | Capacity: {calculations["capacity"]}ml'
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X (cm)',
                yaxis_title='Y (cm)',
                zaxis_title='Z (cm)',
                aspectmode='cube',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            title=dict(
                text=title_text,
                x=0.5,
                font=dict(size=14)
            ),
            width=600,
            height=500
        )
        
        # Store calculations for later use
        fig._calculations = calculations
        
        return fig
    
    def _create_rectangular_prism(self, params):
        """Create a 3D rectangular prism using plotly with educational features"""
        length = params.get('length', 3)
        breadth = params.get('breadth', 2)
        height = params.get('height', 1)
        center = params.get('center', [0, 0, 0])
        show_calculations = params.get('show_calculations', True)
        
        # Calculate educational values
        calculations = self.geometry_3d_calculator.get_all_calculations('rectangular_prism', {
            'length': length, 'breadth': breadth, 'height': height
        })
        
        # Define rectangular prism vertices
        vertices = np.array([
            [-length/2, -breadth/2, -height/2], [length/2, -breadth/2, -height/2], 
            [length/2, breadth/2, -height/2], [-length/2, breadth/2, -height/2],  # bottom face
            [-length/2, -breadth/2, height/2], [length/2, -breadth/2, height/2], 
            [length/2, breadth/2, height/2], [-length/2, breadth/2, height/2]     # top face
        ]) + np.array(center)
        
        # Define faces
        faces = [
            [0, 1, 2, 3],  # bottom
            [4, 5, 6, 7],  # top
            [0, 1, 5, 4],  # front
            [2, 3, 7, 6],  # back
            [0, 3, 7, 4],  # left
            [1, 2, 6, 5]   # right
        ]
        
        # Create the 3D rectangular prism
        fig = go.Figure(data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=[face[0] for face in faces],
                j=[face[1] for face in faces],
                k=[face[2] for face in faces],
                opacity=0.7,
                color='lightgreen',
                name='Rectangular Prism'
            )
        ])
        
        # Add dimension labels
        if show_calculations:
            # Add length label
            fig.add_trace(go.Scatter3d(
                x=[vertices[0, 0], vertices[1, 0]],
                y=[vertices[0, 1], vertices[1, 1]],
                z=[vertices[0, 2], vertices[1, 2]],
                mode='lines+markers+text',
                line=dict(color='red', width=4),
                text=[f'{length}cm', f'{length}cm'],
                textposition='top center',
                name='Length',
                showlegend=False
            ))
            
            # Add breadth label
            fig.add_trace(go.Scatter3d(
                x=[vertices[0, 0], vertices[3, 0]],
                y=[vertices[0, 1], vertices[3, 1]],
                z=[vertices[0, 2], vertices[3, 2]],
                mode='lines+markers+text',
                line=dict(color='blue', width=4),
                text=[f'{breadth}cm', f'{breadth}cm'],
                textposition='middle right',
                name='Breadth',
                showlegend=False
            ))
            
            # Add height label
            fig.add_trace(go.Scatter3d(
                x=[vertices[0, 0], vertices[4, 0]],
                y=[vertices[0, 1], vertices[4, 1]],
                z=[vertices[0, 2], vertices[4, 2]],
                mode='lines+markers+text',
                line=dict(color='green', width=4),
                text=[f'{height}cm', f'{height}cm'],
                textposition='top center',
                name='Height',
                showlegend=False
            ))
        
        # Update layout with educational information
        title_text = f'3D Rectangular Prism (L:{length}cm × B:{breadth}cm × H:{height}cm)'
        if show_calculations:
            title_text += f'<br>Surface Area: {calculations["surface_area"]}cm² | Volume: {calculations["volume"]}cm³ | Capacity: {calculations["capacity"]}ml'
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X (cm)',
                yaxis_title='Y (cm)',
                zaxis_title='Z (cm)',
                aspectmode='cube',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            title=dict(
                text=title_text,
                x=0.5,
                font=dict(size=14)
            ),
            width=600,
            height=500
        )
        
        # Store calculations for later use
        fig._calculations = calculations
        
        return fig
    
    def _create_sphere(self, params):
        """Create a 3D sphere using plotly"""
        radius = params.get('radius', 1)
        center = params.get('center', [0, 0, 0])
        
        # Generate sphere coordinates
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
        y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
        
        fig = go.Figure(data=[
            go.Surface(x=x, y=y, z=z, opacity=0.7, colorscale='Blues')
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Sphere'
        )
        
        return fig
    
    def _create_cylinder(self, params):
        """Create a 3D cylinder using plotly"""
        radius = params.get('radius', 1)
        height = params.get('height', 3)
        center = params.get('center', [0, 0, 0])
        
        # Generate cylinder coordinates
        theta = np.linspace(0, 2 * np.pi, 20)
        z = np.linspace(0, height, 20)
        theta_grid, z_grid = np.meshgrid(theta, z)
        
        x = radius * np.cos(theta_grid) + center[0]
        y = radius * np.sin(theta_grid) + center[1]
        z = z_grid + center[2]
        
        fig = go.Figure(data=[
            go.Surface(x=x, y=y, z=z, opacity=0.7, colorscale='Greens')
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Cylinder'
        )
        
        return fig
    
    def _create_pyramid(self, params):
        """Create a 3D pyramid using plotly"""
        base_size = params.get('base_size', 2)
        height = params.get('height', 3)
        center = params.get('center', [0, 0, 0])
        
        # Define pyramid vertices
        base_vertices = np.array([
            [-1, -1, 0], [1, -1, 0], [1, 1, 0], [-1, 1, 0]
        ]) * base_size / 2 + np.array(center[:2] + [0])
        
        apex = np.array([center[0], center[1], height])
        
        vertices = np.vstack([base_vertices, apex])
        
        # Define faces
        faces = [
            [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4],  # sides
            [0, 1, 2, 3]  # base
        ]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=[face[0] for face in faces],
                j=[face[1] for face in faces],
                k=[face[2] for face in faces],
                opacity=0.7,
                color='orange'
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Pyramid'
        )
        
        return fig
    
    # Enhanced Educational Methods
    def generate_educational_diagram(self, diagram_type: str, parameters: Dict[str, Any], learning_mode: str = 'construction') -> str:
        """
        Generate educational diagram with interactive features based on learning mode
        
        Args:
            diagram_type: Type of diagram to generate
            parameters: Diagram parameters
            learning_mode: 'construction', 'measurement', 'classification', or 'assessment'
            
        Returns:
            Base64 encoded PNG image string with educational features
        """
        try:
            # Set interactive mode based on learning mode
            self.interactive_mode = True
            self.show_calculations = learning_mode in ['measurement', 'assessment']
            self.show_classifications = learning_mode in ['classification', 'assessment']
            
            # Generate base diagram
            image_base64 = self.generate_2d_diagram(diagram_type, parameters)
            
            # Add educational overlays based on mode
            if learning_mode == 'construction':
                image_base64 = self._add_construction_guides(diagram_type, parameters, image_base64)
            elif learning_mode == 'measurement':
                image_base64 = self._add_measurement_tools(diagram_type, parameters, image_base64)
            elif learning_mode == 'classification':
                image_base64 = self._add_classification_hints(diagram_type, parameters, image_base64)
            elif learning_mode == 'assessment':
                image_base64 = self._add_assessment_features(diagram_type, parameters, image_base64)
            
            return image_base64
            
        except Exception as e:
            raise Exception(f"Error generating educational diagram: {str(e)}")
    
    def calculate_geometric_properties(self, shape_type: str, parameters: Dict[str, Any]) -> GeometricProperties:
        """
        Calculate comprehensive geometric properties for a shape
        
        Args:
            shape_type: Type of shape ('triangle', 'quadrilateral', 'circle', 'angles', etc.)
            parameters: Shape parameters
            
        Returns:
            GeometricProperties object with calculated values
        """
        try:
            if shape_type in ['triangle', 'equilateral_triangle', 'isosceles_triangle', 'scalene_triangle', 'right_triangle', 'acute_triangle', 'obtuse_triangle']:
                return self._calculate_triangle_properties(parameters)
            elif shape_type in ['quadrilateral', 'square', 'rectangle', 'rhombus', 'parallelogram', 'kite', 'trapezium']:
                return self._calculate_quadrilateral_properties(parameters)
            elif shape_type in ['circle', 'chord', 'segment', 'arc', 'radius', 'diameter']:
                return self._calculate_circle_properties(parameters)
            elif shape_type in ['angles', 'acute', 'right', 'obtuse', 'straight', 'reflex']:
                return self._calculate_angle_properties(parameters)
            else:
                raise ValueError(f"Unsupported shape type for calculations: {shape_type}")
                
        except Exception as e:
            raise Exception(f"Error calculating geometric properties: {str(e)}")
    
    def _calculate_triangle_properties(self, parameters: Dict[str, Any]) -> GeometricProperties:
        """Calculate triangle properties using TriangleCalculator"""
        # Extract sides and angles from parameters
        sides = parameters.get('sides', [3, 4, 5])  # Default right triangle
        angles = parameters.get('angles', [90, 53.13, 36.87])  # Default angles
        
        # If only two sides and one angle given, calculate the third side
        if len(sides) == 2 and len(angles) >= 1:
            side_c = self.triangle_calculator.calculate_unknown_side(sides[0], sides[1], angles[0])
            sides = [sides[0], sides[1], side_c]
        
        # If only sides given, calculate angles
        if len(sides) == 3 and len(angles) < 3:
            angle_a = self.triangle_calculator.calculate_unknown_angle(sides[1], sides[2], sides[0])
            angle_b = self.triangle_calculator.calculate_unknown_angle(sides[0], sides[2], sides[1])
            angle_c = self.triangle_calculator.calculate_unknown_angle(sides[0], sides[1], sides[2])
            angles = [angle_a, angle_b, angle_c]
        
        return self.triangle_calculator.get_triangle_properties(sides, angles)
    
    def _calculate_quadrilateral_properties(self, parameters: Dict[str, Any]) -> GeometricProperties:
        """Calculate quadrilateral properties using QuadrilateralAnalyzer"""
        sides = parameters.get('sides', [4, 4, 4, 4])  # Default square
        angles = parameters.get('angles', [90, 90, 90, 90])  # Default right angles
        
        return self.quadrilateral_analyzer.classify_quadrilateral(sides, angles)
    
    def _calculate_circle_properties(self, parameters: Dict[str, Any]) -> GeometricProperties:
        """Calculate circle properties using CircleCalculator"""
        radius = parameters.get('radius', 2)
        diameter = self.circle_calculator.calculate_diameter(radius)
        circumference = self.circle_calculator.calculate_circumference(radius)
        area = self.circle_calculator.calculate_area(radius)
        
        return GeometricProperties(
            area=area,
            perimeter=circumference,
            angles=[],  # Circles don't have angles
            sides=[radius, diameter],  # radius and diameter
            classification="Circle",
            properties=[
                f"Radius: {radius:.2f}",
                f"Diameter: {diameter:.2f}",
                f"Circumference: {circumference:.2f}",
                f"Area: {area:.2f}"
            ]
        )
    
    def _calculate_angle_properties(self, parameters: Dict[str, Any]) -> GeometricProperties:
        """
        Calculate properties for angle measurements
        
        Args:
            parameters: Dictionary containing angle parameters
            
        Returns:
            GeometricProperties object with angle calculations
        """
        try:
            angle_type = parameters.get('angle_type', 'acute')
            measurement = parameters.get('measurement', 45)
            
            # Use the InteractiveAngleTool to get angle properties
            angle_measurement = self.angle_tool.measure_angle(
                vertex=(0, 0),
                arm1=(1, 0),
                arm2=(math.cos(math.radians(measurement)), math.sin(math.radians(measurement)))
            )
            
            # Calculate complementary and supplementary angles
            complementary = 90 - measurement if measurement < 90 else None
            supplementary = 180 - measurement if measurement < 180 else None
            
            properties = {
                'angle_type': angle_type,
                'measurement': measurement,
                'classification': angle_measurement.angle_type.value,
                'complementary_angle': complementary,
                'supplementary_angle': supplementary,
                'is_acute': measurement < 90,
                'is_right': measurement == 90,
                'is_obtuse': 90 < measurement < 180,
                'is_straight': measurement == 180,
                'is_reflex': measurement > 180
            }
            
            return GeometricProperties(
                area=0.0,  # Angles don't have area
                perimeter=0.0,  # Angles don't have perimeter
                angles=[measurement],  # The angle measurement
                sides=[],  # Angles don't have sides
                classification=angle_measurement.angle_type.value,
                properties=[f"{k}: {v}" for k, v in properties.items()]
            )
            
        except Exception as e:
            raise Exception(f"Error calculating angle properties: {str(e)}")
    
    def generate_quiz_question(self, topic: str, difficulty: str = 'medium') -> Dict[str, Any]:
        """
        Generate comprehensive quiz questions for different geometry topics using two fail-safe systems
        
        Args:
            topic: 'angles', 'triangles', 'quadrilaterals', 'circles', 'unit_conversions', 'composite_areas'
            difficulty: 'easy', 'medium', 'hard'
            
        Returns:
            Dictionary with question, options, correct answer, explanation, and metadata
        """
        try:
            # Initialize comprehensive quiz generator
            quiz_generator = ComprehensiveQuizGenerator()
            
            # Generate question using fail-safe system
            question = quiz_generator.generate_question(topic, difficulty)
            
            # Convert to dictionary format for API response
            return {
                'question': question.question,
                'options': question.options,
                'correct_answer': question.correct_answer,
                'explanation': question.explanation,
                'difficulty': question.difficulty,
                'topic': question.topic,
                'shape_type': question.shape_type,
                'metric_units': question.metric_units,
                'south_african_context': question.south_african_context,
                'conversion_required': question.conversion_required,
                'expected_concepts': question.expected_concepts,
                'parameters': question.parameters
            }
                
        except Exception as e:
            raise Exception(f"Error generating quiz question: {str(e)}")
    
    
    def _add_construction_guides(self, diagram_type: str, parameters: Dict[str, Any], image_base64: str) -> str:
        """Add construction guides to diagram"""
        # This would add step-by-step construction indicators
        # For now, return the original image
        return image_base64
    
    def _add_measurement_tools(self, diagram_type: str, parameters: Dict[str, Any], image_base64: str) -> str:
        """Add measurement tools to diagram"""
        # This would add protractor overlays and measurement indicators
        # For now, return the original image
        return image_base64
    
    def _add_classification_hints(self, diagram_type: str, parameters: Dict[str, Any], image_base64: str) -> str:
        """Add classification hints to diagram"""
        # This would add property indicators and classification hints
        # For now, return the original image
        return image_base64
    
    def _add_assessment_features(self, diagram_type: str, parameters: Dict[str, Any], image_base64: str) -> str:
        """Add assessment features to diagram"""
        # This would add quiz elements and assessment tools
        # For now, return the original image
        return image_base64

# Global instance for use in API endpoints
geometry_generator = GeometryDiagramGenerator()
