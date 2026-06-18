"""
Quiz System Data Models
Comprehensive data structures for the enhanced geometry quiz system
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple, Optional
from enum import Enum


class DifficultyLevel(Enum):
    """Difficulty levels for quiz questions"""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class QuestionType(Enum):
    """Types of quiz questions"""
    # Shape Classification
    SHAPE_CLASSIFICATION = "shape_classification"
    
    # Area & Perimeter Calculations
    AREA_CALCULATION = "area_calculation"
    PERIMETER_CALCULATION = "perimeter_calculation"
    COMPOSITE_AREA_CALCULATION = "composite_area_calculation"
    
    # Angle Calculations
    ANGLE_CALCULATION = "angle_calculation"
    ANGLE_CLASSIFICATION = "angle_classification"
    
    # Unit Conversions
    UNIT_CONVERSION = "unit_conversion"
    
    # Quadrilateral Operations
    QUADRILATERAL_SORTING = "quadrilateral_sorting"
    QUADRILATERAL_GROUPING = "quadrilateral_grouping"
    
    # Similarity & Congruency
    SIMILARITY_RECOGNITION = "similarity_recognition"
    CONGRUENCY_RECOGNITION = "congruency_recognition"
    
    # Equation Solving
    EQUATION_SOLVING = "equation_solving"
    
    # Triangle Height Concepts
    TRIANGLE_HEIGHT = "triangle_height"
    
    # Problem Solving
    PROBLEM_SOLVING = "problem_solving"
    
    # 3D Geometry
    VOLUME_CALCULATION = "volume_calculation"
    SURFACE_AREA_CALCULATION = "surface_area_calculation"
    CAPACITY_CALCULATION = "capacity_calculation"
    THREE_D_SHAPE_RECOGNITION = "three_d_shape_recognition"
    
    # Real World Applications
    REAL_WORLD_APPLICATION = "real_world_application"


class ShapeType(Enum):
    """Geometric shape types"""
    # Triangles
    TRIANGLE_EQUILATERAL = "triangle_equilateral"
    TRIANGLE_ISOSCELES = "triangle_isosceles"
    TRIANGLE_SCALENE = "triangle_scalene"
    TRIANGLE_RIGHT_ANGLED = "triangle_right_angled"
    TRIANGLE_ACUTE = "triangle_acute"
    TRIANGLE_OBTUSE = "triangle_obtuse"
    
    # Quadrilaterals
    SQUARE = "square"
    RECTANGLE = "rectangle"
    RHOMBUS = "rhombus"
    PARALLELOGRAM = "parallelogram"
    KITE = "kite"
    TRAPEZIUM = "trapezium"
    
    # Circles
    CIRCLE = "circle"
    CIRCLE_SECTOR = "circle_sector"
    CIRCLE_SEGMENT = "circle_segment"
    
    # Angles
    ANGLE_ACUTE = "angle_acute"
    ANGLE_RIGHT = "angle_right"
    ANGLE_OBTUSE = "angle_obtuse"
    ANGLE_STRAIGHT = "angle_straight"
    ANGLE_REFLEX = "angle_reflex"
    
    # 3D Shapes
    CUBE = "cube"
    RECTANGULAR_PRISM = "rectangular_prism"
    CYLINDER = "cylinder"
    SPHERE = "sphere"
    CONE = "cone"
    PYRAMID = "pyramid"


class MetricUnit(Enum):
    """Metric system units"""
    # Length units
    MILLIMETER = "mm"
    CENTIMETER = "cm"
    METER = "m"
    KILOMETER = "km"
    
    # Area units
    SQUARE_MILLIMETER = "mm²"
    SQUARE_CENTIMETER = "cm²"
    SQUARE_METER = "m²"
    SQUARE_KILOMETER = "km²"


@dataclass
class QuizQuestion:
    """Core quiz question data structure"""
    question: str
    options: List[str]
    correct_answer: str
    explanation: str
    topic: str
    difficulty: DifficultyLevel
    question_type: QuestionType
    shape_type: Optional[ShapeType]
    parameters: Dict[str, Any]
    geometric_constraints: List[str]
    curriculum_alignments: List[str]
    metric_units: Dict[str, str]  # {'length': 'cm', 'area': 'cm²'}
    south_african_context: bool
    conversion_required: bool
    question_id: str
    template_id: Optional[str] = None
    expected_concepts: List[str] = None
    reasoning_required: bool = False
    decimal_precision: int = 1


@dataclass
class QuestionTemplate:
    """Question template for generating variations"""
    template_id: str
    question_template: str
    parameter_ranges: Dict[str, Tuple[float, float]]
    constraints: List[str]
    difficulty: DifficultyLevel
    topic: str
    question_type: QuestionType
    shape_type: ShapeType
    metric_units: List[str]  # ['mm', 'cm', 'm']
    conversion_types: List[str]  # ['mm_cm', 'cm_m', 'mm²_cm²']
    real_world_context: str  # 'garden', 'construction', 'school'
    south_african_context: bool = True
    reasoning_required: bool = False


@dataclass
class MetricConversion:
    """Metric unit conversion data"""
    from_unit: str
    to_unit: str
    conversion_factor: float
    context: str  # 'length', 'area', 'volume'
    south_african_appropriate: bool = True


@dataclass
class GeometricConstraints:
    """Geometric constraint validation data"""
    shape_type: ShapeType
    constraints: List[str]
    parameter_limits: Dict[str, Tuple[float, float]]
    validation_rules: List[str]


@dataclass
class QuizGenerationRequest:
    """Request structure for quiz generation"""
    topic: str
    difficulty: DifficultyLevel
    question_type: QuestionType
    shape_type: Optional[ShapeType] = None
    count: int = 1
    include_diagram: bool = True
    south_african_context: bool = True
    conversion_required: bool = False
    reasoning_required: bool = False


@dataclass
class QuizGenerationResponse:
    """Response structure for quiz generation"""
    success: bool
    questions: List[QuizQuestion]
    generation_method: str  # 'constraint_based', 'template_based', 'fallback'
    error_message: Optional[str] = None
    metadata: Dict[str, Any] = None


# Pre-defined metric conversions for South African curriculum
METRIC_CONVERSIONS = [
    # Length conversions
    MetricConversion("mm", "cm", 0.1, "length", True),
    MetricConversion("cm", "mm", 10.0, "length", True),
    MetricConversion("cm", "m", 0.01, "length", True),
    MetricConversion("m", "cm", 100.0, "length", True),
    MetricConversion("m", "km", 0.001, "length", True),
    MetricConversion("km", "m", 1000.0, "length", True),
    
    # Area conversions
    MetricConversion("mm²", "cm²", 0.01, "area", True),
    MetricConversion("cm²", "mm²", 100.0, "area", True),
    MetricConversion("cm²", "m²", 0.0001, "area", True),
    MetricConversion("m²", "cm²", 10000.0, "area", True),
    MetricConversion("m²", "km²", 0.000001, "area", True),
    MetricConversion("km²", "m²", 1000000.0, "area", True),
]

# South African real-world contexts
SOUTH_AFRICAN_CONTEXTS = {
    "garden": [
        "garden plot", "flower bed", "vegetable patch", "lawn area", 
        "garden bed", "planting area", "landscaping"
    ],
    "construction": [
        "room floor", "wall area", "roof section", "patio", "floor tiles",
        "construction site", "building project", "renovation"
    ],
    "school": [
        "classroom floor", "sports field", "art room", "science project",
        "school garden", "playground", "assembly area"
    ],
    "home": [
        "living room", "bedroom", "kitchen", "bathroom", "garage",
        "home office", "study area", "family room"
    ]
}

# Grade 7 Curriculum Topics (CAPS aligned)
CURRICULUM_TOPICS = [
    "Properties of 2D Shapes",
    "Calculations involving 2D Shapes", 
    "Similarity and Congruency",
    "Problem Solving",
    "Unit Conversions",
    "Real-world Applications",
    "Shape Classification",
    "Area and Perimeter",
    "Angle Calculations",
    "Quadrilateral Properties",
    "Triangle Properties"
]
