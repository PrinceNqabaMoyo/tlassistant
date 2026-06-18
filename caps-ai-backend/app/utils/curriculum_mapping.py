"""
Curriculum Mapping and Question Categories
Maps Grade 7 Geometry requirements to quiz categories with proper difficulty levels
"""

from typing import Dict, List, Tuple
from .quiz_models import (
    DifficultyLevel, QuestionType, ShapeType, CURRICULUM_TOPICS,
    SOUTH_AFRICAN_CONTEXTS
)


class CurriculumMapper:
    """Maps curriculum requirements to quiz categories and difficulty levels"""
    
    def __init__(self):
        self.question_categories = self._initialize_question_categories()
        self.difficulty_mapping = self._initialize_difficulty_mapping()
        self.shape_coverage = self._initialize_shape_coverage()
        self.metric_system_requirements = self._initialize_metric_requirements()
    
    def _initialize_question_categories(self) -> Dict[str, Dict[str, List[QuestionType]]]:
        """Initialize the 11 main question categories with their question types"""
        return {
            "Shape Classification": {
                "easy": [QuestionType.SHAPE_CLASSIFICATION],
                "medium": [QuestionType.SHAPE_CLASSIFICATION, QuestionType.QUADRILATERAL_SORTING],
                "hard": [QuestionType.SHAPE_CLASSIFICATION, QuestionType.QUADRILATERAL_GROUPING]
            },
            "Area & Perimeter Calculations": {
                "easy": [QuestionType.AREA_CALCULATION, QuestionType.PERIMETER_CALCULATION],
                "medium": [QuestionType.AREA_CALCULATION, QuestionType.PERIMETER_CALCULATION],
                "hard": [QuestionType.AREA_CALCULATION, QuestionType.PERIMETER_CALCULATION]
            },
            "Composite Area Calculations": {
                "easy": [],  # Not applicable for easy level
                "medium": [QuestionType.COMPOSITE_AREA_CALCULATION],
                "hard": [QuestionType.COMPOSITE_AREA_CALCULATION, QuestionType.PROBLEM_SOLVING]
            },
            "Angle Calculations": {
                "easy": [QuestionType.ANGLE_CLASSIFICATION],
                "medium": [QuestionType.ANGLE_CALCULATION, QuestionType.ANGLE_CLASSIFICATION],
                "hard": [QuestionType.ANGLE_CALCULATION, QuestionType.ANGLE_CLASSIFICATION]
            },
            "Unit Conversions": {
                "easy": [QuestionType.UNIT_CONVERSION],
                "medium": [QuestionType.UNIT_CONVERSION],
                "hard": [QuestionType.UNIT_CONVERSION, QuestionType.REAL_WORLD_APPLICATION]
            },
            "Quadrilateral Sorting & Grouping": {
                "easy": [QuestionType.QUADRILATERAL_SORTING],
                "medium": [QuestionType.QUADRILATERAL_SORTING, QuestionType.QUADRILATERAL_GROUPING],
                "hard": [QuestionType.QUADRILATERAL_GROUPING, QuestionType.PROBLEM_SOLVING]
            },
            "Similarity & Congruency": {
                "easy": [],  # Not applicable for easy level
                "medium": [QuestionType.SIMILARITY_RECOGNITION, QuestionType.CONGRUENCY_RECOGNITION],
                "hard": [QuestionType.SIMILARITY_RECOGNITION, QuestionType.CONGRUENCY_RECOGNITION, QuestionType.PROBLEM_SOLVING]
            },
            "Equation Solving by Inspection": {
                "easy": [QuestionType.EQUATION_SOLVING],
                "medium": [QuestionType.EQUATION_SOLVING],
                "hard": [QuestionType.EQUATION_SOLVING, QuestionType.PROBLEM_SOLVING]
            },
            "Triangle Height Concepts": {
                "easy": [],  # Not applicable for easy level
                "medium": [QuestionType.TRIANGLE_HEIGHT],
                "hard": [QuestionType.TRIANGLE_HEIGHT, QuestionType.PROBLEM_SOLVING]
            },
            "Problem Solving": {
                "easy": [QuestionType.REAL_WORLD_APPLICATION],
                "medium": [QuestionType.REAL_WORLD_APPLICATION, QuestionType.PROBLEM_SOLVING],
                "hard": [QuestionType.PROBLEM_SOLVING, QuestionType.REAL_WORLD_APPLICATION]
            },
            "Real-world Applications": {
                "easy": [QuestionType.REAL_WORLD_APPLICATION],
                "medium": [QuestionType.REAL_WORLD_APPLICATION],
                "hard": [QuestionType.REAL_WORLD_APPLICATION, QuestionType.PROBLEM_SOLVING]
            }
        }
    
    def _initialize_difficulty_mapping(self) -> Dict[str, Dict[str, any]]:
        """Initialize difficulty level characteristics"""
        return {
            "easy": {
                "description": "Simple, single-step calculations with whole numbers",
                "characteristics": [
                    "Whole numbers only",
                    "Basic shape recognition",
                    "Direct formula application",
                    "Clear, unambiguous questions",
                    "Single-step calculations"
                ],
                "numeric_complexity": "integer",
                "conceptual_complexity": "basic",
                "problem_complexity": "single_step",
                "context_complexity": "abstract"
            },
            "medium": {
                "description": "Multi-step calculations with decimal numbers and real-world contexts",
                "characteristics": [
                    "Decimal numbers (1-2 decimal places)",
                    "Multi-step calculations",
                    "Shape property identification",
                    "Formula manipulation",
                    "Real-world contexts"
                ],
                "numeric_complexity": "decimal",
                "conceptual_complexity": "intermediate",
                "problem_complexity": "multi_step",
                "context_complexity": "real_world"
            },
            "hard": {
                "description": "Complex problem solving with advanced reasoning required",
                "characteristics": [
                    "Multiple decimal places",
                    "Complex problem solving",
                    "Advanced shape relationships",
                    "Proof and reasoning required",
                    "Challenging real-world scenarios"
                ],
                "numeric_complexity": "complex",
                "conceptual_complexity": "advanced",
                "problem_complexity": "complex_reasoning",
                "context_complexity": "challenging"
            }
        }
    
    def _initialize_shape_coverage(self) -> Dict[str, List[ShapeType]]:
        """Initialize shape coverage for each category"""
        return {
            "triangles": [
                ShapeType.TRIANGLE_EQUILATERAL,
                ShapeType.TRIANGLE_ISOSCELES,
                ShapeType.TRIANGLE_SCALENE,
                ShapeType.TRIANGLE_RIGHT_ANGLED,
                ShapeType.TRIANGLE_ACUTE,
                ShapeType.TRIANGLE_OBTUSE
            ],
            "quadrilaterals": [
                ShapeType.SQUARE,
                ShapeType.RECTANGLE,
                ShapeType.RHOMBUS,
                ShapeType.PARALLELOGRAM,
                ShapeType.KITE,
                ShapeType.TRAPEZIUM
            ],
            "circles": [
                ShapeType.CIRCLE,
                ShapeType.CIRCLE_SECTOR,
                ShapeType.CIRCLE_SEGMENT
            ],
            "angles": [
                ShapeType.ANGLE_ACUTE,
                ShapeType.ANGLE_RIGHT,
                ShapeType.ANGLE_OBTUSE,
                ShapeType.ANGLE_STRAIGHT,
                ShapeType.ANGLE_REFLEX
            ]
        }
    
    def _initialize_metric_requirements(self) -> Dict[str, List[str]]:
        """Initialize metric system requirements for South African curriculum"""
        return {
            "length_units": ["mm", "cm", "m", "km"],
            "area_units": ["mm²", "cm²", "m²", "km²"],
            "conversion_focus": [
                "mm ↔ cm",
                "cm ↔ m", 
                "mm² ↔ cm²",
                "cm² ↔ m²"
            ],
            "real_world_contexts": [
                "garden_plots",
                "room_measurements", 
                "construction",
                "school_projects"
            ],
            "unit_appropriateness": {
                "garden_plots": "m²",
                "room_measurements": "cm",
                "construction": "m",
                "school_projects": "cm"
            }
        }
    
    def get_question_types_for_category(self, category: str, difficulty: DifficultyLevel) -> List[QuestionType]:
        """Get question types for a specific category and difficulty"""
        if category not in self.question_categories:
            return []
        
        difficulty_str = difficulty.value
        if difficulty_str not in self.question_categories[category]:
            return []
        
        return self.question_categories[category][difficulty_str]
    
    def get_categories_for_difficulty(self, difficulty: DifficultyLevel) -> List[str]:
        """Get all categories available for a specific difficulty level"""
        difficulty_str = difficulty.value
        available_categories = []
        
        for category, difficulties in self.question_categories.items():
            if difficulty_str in difficulties and difficulties[difficulty_str]:
                available_categories.append(category)
        
        return available_categories
    
    def get_difficulty_characteristics(self, difficulty: DifficultyLevel) -> Dict[str, any]:
        """Get characteristics for a specific difficulty level"""
        return self.difficulty_mapping.get(difficulty.value, {})
    
    def get_shapes_for_category(self, category: str) -> List[ShapeType]:
        """Get applicable shapes for a specific category"""
        shapes = []
        
        # Map categories to shape groups
        if "triangle" in category.lower() or "height" in category.lower():
            shapes.extend(self.shape_coverage["triangles"])
        elif "quadrilateral" in category.lower() or "sorting" in category.lower() or "grouping" in category.lower():
            shapes.extend(self.shape_coverage["quadrilaterals"])
        elif "circle" in category.lower():
            shapes.extend(self.shape_coverage["circles"])
        elif "angle" in category.lower():
            shapes.extend(self.shape_coverage["angles"])
        else:
            # Default to all shapes for general categories
            for shape_group in self.shape_coverage.values():
                shapes.extend(shape_group)
        
        return shapes
    
    def get_metric_requirements(self) -> Dict[str, any]:
        """Get metric system requirements"""
        return self.metric_system_requirements
    
    def get_south_african_contexts(self) -> Dict[str, List[str]]:
        """Get South African real-world contexts"""
        return SOUTH_AFRICAN_CONTEXTS
    
    def get_curriculum_topics(self) -> List[str]:
        """Get all curriculum topics"""
        return CURRICULUM_TOPICS
    
    def validate_category_difficulty_combination(self, category: str, difficulty: DifficultyLevel) -> bool:
        """Validate if a category is available for a specific difficulty level"""
        question_types = self.get_question_types_for_category(category, difficulty)
        return len(question_types) > 0
    
    def get_question_generation_guidelines(self, category: str, difficulty: DifficultyLevel) -> Dict[str, any]:
        """Get guidelines for generating questions in a specific category and difficulty"""
        characteristics = self.get_difficulty_characteristics(difficulty)
        question_types = self.get_question_types_for_category(category, difficulty)
        shapes = self.get_shapes_for_category(category)
        
        return {
            "category": category,
            "difficulty": difficulty.value,
            "question_types": [qt.value for qt in question_types],
            "applicable_shapes": [s.value for s in shapes],
            "characteristics": characteristics,
            "metric_units_required": True,
            "south_african_context": True,
            "reasoning_required": difficulty == DifficultyLevel.HARD
        }


# Global curriculum mapper instance
curriculum_mapper = CurriculumMapper()


def get_curriculum_mapping() -> CurriculumMapper:
    """Get the global curriculum mapper instance"""
    return curriculum_mapper
