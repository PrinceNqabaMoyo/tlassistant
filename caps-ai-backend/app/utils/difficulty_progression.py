"""
Difficulty Progression System
Implements proper scaling algorithms for educational progression as per plan Phase 5
"""

from typing import Dict, List, Any, Tuple, Optional
from enum import Enum
import random
import math
from .quiz_models import DifficultyLevel, QuestionType, ShapeType


class ProgressionStage(Enum):
    """Educational progression stages"""
    FOUNDATION = "foundation"      # Basic concepts and simple calculations
    DEVELOPMENT = "development"    # Intermediate concepts with decimals
    MASTERY = "mastery"           # Advanced concepts with complex reasoning
    EXPERT = "expert"             # Expert-level problem solving


class DifficultyProgressionSystem:
    """
    Implements difficulty progression system with proper scaling algorithms
    Ensures educational progression from basic to advanced concepts
    """
    
    def __init__(self):
        self.stage_mapping = self._initialize_stage_mapping()
        self.parameter_scaling = self._initialize_parameter_scaling()
        self.concept_complexity = self._initialize_concept_complexity()
    
    def _initialize_stage_mapping(self) -> Dict[DifficultyLevel, ProgressionStage]:
        """Map difficulty levels to progression stages"""
        return {
            DifficultyLevel.EASY: ProgressionStage.FOUNDATION,
            DifficultyLevel.MEDIUM: ProgressionStage.DEVELOPMENT,
            DifficultyLevel.HARD: ProgressionStage.MASTERY,
        }
    
    def _initialize_parameter_scaling(self) -> Dict[ProgressionStage, Dict[str, Tuple[float, float]]]:
        """Define parameter ranges for each progression stage"""
        return {
            ProgressionStage.FOUNDATION: {
                'triangle_base': (1, 10),
                'triangle_height': (1, 10),
                'rectangle_length': (2, 8),
                'rectangle_width': (2, 8),
                'circle_radius': (1, 5),
                'angle_values': (30, 90),
                'conversion_values': (1, 20),
            },
            ProgressionStage.DEVELOPMENT: {
                'triangle_base': (5, 20),
                'triangle_height': (5, 20),
                'rectangle_length': (8, 25),
                'rectangle_width': (6, 20),
                'circle_radius': (3, 15),
                'angle_values': (20, 160),
                'conversion_values': (10, 100),
            },
            ProgressionStage.MASTERY: {
                'triangle_base': (10, 50),
                'triangle_height': (10, 50),
                'rectangle_length': (20, 100),
                'rectangle_width': (15, 80),
                'circle_radius': (5, 30),
                'angle_values': (10, 170),
                'conversion_values': (50, 500),
            },
            ProgressionStage.EXPERT: {
                'triangle_base': (20, 100),
                'triangle_height': (20, 100),
                'rectangle_length': (50, 200),
                'rectangle_width': (30, 150),
                'circle_radius': (10, 50),
                'angle_values': (5, 175),
                'conversion_values': (100, 1000),
            }
        }
    
    def _initialize_concept_complexity(self) -> Dict[ProgressionStage, List[str]]:
        """Define concept complexity for each stage"""
        return {
            ProgressionStage.FOUNDATION: [
                'basic_area_calculation',
                'basic_perimeter_calculation',
                'simple_unit_conversion',
                'basic_shape_identification',
                'whole_number_parameters',
            ],
            ProgressionStage.DEVELOPMENT: [
                'decimal_calculations',
                'intermediate_unit_conversion',
                'shape_classification',
                'angle_calculations',
                'real_world_contexts',
            ],
            ProgressionStage.MASTERY: [
                'complex_calculations',
                'advanced_unit_conversion',
                'composite_areas',
                'similarity_congruency',
                'equation_solving',
                'reasoning_required',
            ],
            ProgressionStage.EXPERT: [
                'expert_calculations',
                'multi_step_problems',
                'optimization_problems',
                'proof_required',
                'advanced_reasoning',
            ]
        }
    
    def get_parameter_range(self, difficulty: DifficultyLevel, parameter_type: str) -> Tuple[float, float]:
        """Get parameter range for a specific difficulty and parameter type"""
        stage = self.stage_mapping.get(difficulty, ProgressionStage.FOUNDATION)
        scaling = self.parameter_scaling.get(stage, {})
        return scaling.get(parameter_type, (1, 10))
    
    def get_concept_complexity(self, difficulty: DifficultyLevel) -> List[str]:
        """Get concept complexity for a difficulty level"""
        stage = self.stage_mapping.get(difficulty, ProgressionStage.FOUNDATION)
        return self.concept_complexity.get(stage, [])
    
    def scale_parameters(self, difficulty: DifficultyLevel, base_parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Scale parameters based on difficulty progression"""
        scaled_parameters = {}
        
        for param_name, value in base_parameters.items():
            if isinstance(value, (int, float)):
                # Scale numeric parameters
                if 'base' in param_name.lower():
                    range_min, range_max = self.get_parameter_range(difficulty, 'triangle_base')
                elif 'height' in param_name.lower():
                    range_min, range_max = self.get_parameter_range(difficulty, 'triangle_height')
                elif 'length' in param_name.lower():
                    range_min, range_max = self.get_parameter_range(difficulty, 'rectangle_length')
                elif 'width' in param_name.lower():
                    range_min, range_max = self.get_parameter_range(difficulty, 'rectangle_width')
                elif 'radius' in param_name.lower():
                    range_min, range_max = self.get_parameter_range(difficulty, 'circle_radius')
                elif 'angle' in param_name.lower():
                    range_min, range_max = self.get_parameter_range(difficulty, 'angle_values')
                else:
                    range_min, range_max = (1, 10)
                
                # Scale the value proportionally
                if difficulty == DifficultyLevel.EASY:
                    scaled_value = random.uniform(range_min, range_max)
                elif difficulty == DifficultyLevel.MEDIUM:
                    scaled_value = random.uniform(range_min, range_max)
                else:  # HARD
                    scaled_value = random.uniform(range_min, range_max)
                
                scaled_parameters[param_name] = round(scaled_value, 1)
            else:
                scaled_parameters[param_name] = value
        
        return scaled_parameters
    
    def get_question_complexity_requirements(self, difficulty: DifficultyLevel) -> Dict[str, Any]:
        """Get question complexity requirements for a difficulty level"""
        stage = self.stage_mapping.get(difficulty, ProgressionStage.FOUNDATION)
        
        if stage == ProgressionStage.FOUNDATION:
            return {
                'require_reasoning': False,
                'require_explanation': False,
                'allow_decimals': False,
                'require_unit_conversion': False,
                'max_parameters': 2,
                'concept_depth': 'basic'
            }
        elif stage == ProgressionStage.DEVELOPMENT:
            return {
                'require_reasoning': False,
                'require_explanation': True,
                'allow_decimals': True,
                'require_unit_conversion': random.random() < 0.3,
                'max_parameters': 3,
                'concept_depth': 'intermediate'
            }
        elif stage == ProgressionStage.MASTERY:
            return {
                'require_reasoning': True,
                'require_explanation': True,
                'allow_decimals': True,
                'require_unit_conversion': random.random() < 0.5,
                'max_parameters': 4,
                'concept_depth': 'advanced'
            }
        else:  # EXPERT
            return {
                'require_reasoning': True,
                'require_explanation': True,
                'allow_decimals': True,
                'require_unit_conversion': random.random() < 0.7,
                'max_parameters': 6,
                'concept_depth': 'expert'
            }
    
    def get_educational_progression_path(self, current_difficulty: DifficultyLevel) -> List[DifficultyLevel]:
        """Get the educational progression path from current difficulty"""
        if current_difficulty == DifficultyLevel.EASY:
            return [DifficultyLevel.EASY, DifficultyLevel.MEDIUM, DifficultyLevel.HARD]
        elif current_difficulty == DifficultyLevel.MEDIUM:
            return [DifficultyLevel.MEDIUM, DifficultyLevel.HARD]
        else:  # HARD
            return [DifficultyLevel.HARD]
    
    def assess_student_readiness(self, performance_data: Dict[str, Any]) -> DifficultyLevel:
        """Assess student readiness based on performance data"""
        accuracy = performance_data.get('accuracy', 0.0)
        completion_time = performance_data.get('avg_completion_time', 0.0)
        attempts = performance_data.get('avg_attempts', 1.0)
        
        # Simple readiness assessment
        if accuracy >= 0.8 and completion_time <= 30 and attempts <= 1.5:
            return DifficultyLevel.HARD
        elif accuracy >= 0.6 and completion_time <= 60 and attempts <= 2.0:
            return DifficultyLevel.MEDIUM
        else:
            return DifficultyLevel.EASY
    
    def get_adaptive_difficulty(self, recent_performance: List[Dict[str, Any]]) -> DifficultyLevel:
        """Get adaptive difficulty based on recent performance"""
        if not recent_performance:
            return DifficultyLevel.EASY
        
        # Calculate average performance metrics
        avg_accuracy = sum(p.get('accuracy', 0) for p in recent_performance) / len(recent_performance)
        avg_time = sum(p.get('completion_time', 0) for p in recent_performance) / len(recent_performance)
        
        # Adaptive difficulty logic
        if avg_accuracy >= 0.85 and avg_time <= 45:
            return DifficultyLevel.HARD
        elif avg_accuracy >= 0.7 and avg_time <= 90:
            return DifficultyLevel.MEDIUM
        else:
            return DifficultyLevel.EASY
    
    def get_learning_objectives(self, difficulty: DifficultyLevel) -> List[str]:
        """Get learning objectives for a difficulty level"""
        stage = self.stage_mapping.get(difficulty, ProgressionStage.FOUNDATION)
        
        objectives = {
            ProgressionStage.FOUNDATION: [
                "Understand basic geometric shapes and their properties",
                "Calculate simple areas and perimeters using whole numbers",
                "Identify and classify basic shapes",
                "Perform simple unit conversions",
                "Apply basic geometric formulas"
            ],
            ProgressionStage.DEVELOPMENT: [
                "Work with decimal numbers in geometric calculations",
                "Solve problems involving multiple geometric concepts",
                "Apply geometric knowledge to real-world contexts",
                "Understand relationships between different shapes",
                "Perform intermediate unit conversions"
            ],
            ProgressionStage.MASTERY: [
                "Solve complex multi-step geometric problems",
                "Apply advanced geometric concepts and reasoning",
                "Work with composite shapes and complex calculations",
                "Demonstrate understanding through explanation and reasoning",
                "Solve problems requiring critical thinking"
            ],
            ProgressionStage.EXPERT: [
                "Solve expert-level geometric problems",
                "Apply advanced mathematical reasoning",
                "Work with optimization and proof problems",
                "Demonstrate mastery through complex problem solving",
                "Apply geometric concepts to novel situations"
            ]
        }
        
        return objectives.get(stage, [])
    
    def get_practice_recommendations(self, difficulty: DifficultyLevel, weak_areas: List[str]) -> List[str]:
        """Get practice recommendations based on difficulty and weak areas"""
        recommendations = []
        
        if difficulty == DifficultyLevel.EASY:
            if 'area_calculation' in weak_areas:
                recommendations.append("Practice basic area calculations with simple shapes")
            if 'perimeter_calculation' in weak_areas:
                recommendations.append("Practice perimeter calculations with basic shapes")
            if 'unit_conversion' in weak_areas:
                recommendations.append("Practice simple unit conversions (cm to mm, etc.)")
        
        elif difficulty == DifficultyLevel.MEDIUM:
            if 'decimal_calculations' in weak_areas:
                recommendations.append("Practice calculations with decimal numbers")
            if 'shape_classification' in weak_areas:
                recommendations.append("Practice identifying and classifying different shapes")
            if 'real_world_problems' in weak_areas:
                recommendations.append("Practice solving real-world geometry problems")
        
        else:  # HARD
            if 'complex_calculations' in weak_areas:
                recommendations.append("Practice complex multi-step calculations")
            if 'reasoning' in weak_areas:
                recommendations.append("Practice explaining your reasoning and problem-solving steps")
            if 'advanced_concepts' in weak_areas:
                recommendations.append("Practice advanced geometric concepts and applications")
        
        return recommendations
