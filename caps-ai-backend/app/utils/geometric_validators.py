"""
Geometric Constraint Validators
Mathematical validation engine for ensuring geometric accuracy in quiz questions
"""

import math
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from .quiz_models import ShapeType, MetricUnit, GeometricConstraints


@dataclass
class ValidationResult:
    """Result of geometric constraint validation"""
    is_valid: bool
    error_message: Optional[str] = None
    corrected_parameters: Optional[Dict[str, Any]] = None
    warnings: List[str] = None


class GeometricConstraintValidator:
    """Main validator class for geometric constraints"""
    
    def __init__(self):
        self.tolerance = 1e-6  # Tolerance for floating point comparisons
        
    def validate_triangle(self, parameters: Dict[str, Any]) -> ValidationResult:
        """Validate triangle parameters using triangle inequality and angle sum"""
        try:
            # Extract parameters
            sides = parameters.get('sides', [])
            angles = parameters.get('angles', [])
            
            if len(sides) == 3:
                a, b, c = sides
                
                # Check triangle inequality: sum of any two sides > third side
                if not (a + b > c and b + c > a and a + c > b):
                    return ValidationResult(
                        is_valid=False,
                        error_message="Triangle inequality violated: sum of any two sides must be greater than the third side"
                    )
                
                # Check for positive sides
                if any(side <= 0 for side in sides):
                    return ValidationResult(
                        is_valid=False,
                        error_message="All triangle sides must be positive"
                    )
                
                # If angles are provided, check angle sum = 180°
                if len(angles) == 3:
                    angle_sum = sum(angles)
                    if not abs(angle_sum - 180) < self.tolerance:
                        return ValidationResult(
                            is_valid=False,
                            error_message=f"Triangle angle sum must be 180°, got {angle_sum}°"
                        )
                    
                    # Check for valid angle ranges
                    for angle in angles:
                        if angle <= 0 or angle >= 180:
                            return ValidationResult(
                                is_valid=False,
                                error_message=f"Triangle angles must be between 0° and 180°, got {angle}°"
                            )
            
            return ValidationResult(is_valid=True)
            
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating triangle: {str(e)}"
            )
    
    def validate_quadrilateral(self, parameters: Dict[str, Any]) -> ValidationResult:
        """Validate quadrilateral parameters"""
        try:
            # Extract parameters
            sides = parameters.get('sides', [])
            angles = parameters.get('angles', [])
            
            if len(sides) == 4:
                # Check for positive sides
                if any(side <= 0 for side in sides):
                    return ValidationResult(
                        is_valid=False,
                        error_message="All quadrilateral sides must be positive"
                    )
            
            if len(angles) == 4:
                # Check angle sum = 360°
                angle_sum = sum(angles)
                if not abs(angle_sum - 360) < self.tolerance:
                    return ValidationResult(
                        is_valid=False,
                        error_message=f"Quadrilateral angle sum must be 360°, got {angle_sum}°"
                    )
                
                # Check for valid angle ranges
                for angle in angles:
                    if angle <= 0 or angle >= 360:
                        return ValidationResult(
                            is_valid=False,
                            error_message=f"Quadrilateral angles must be between 0° and 360°, got {angle}°"
                        )
            
            return ValidationResult(is_valid=True)
            
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating quadrilateral: {str(e)}"
            )
    
    def validate_circle(self, parameters: Dict[str, Any]) -> ValidationResult:
        """Validate circle parameters"""
        try:
            radius = parameters.get('radius', 0)
            diameter = parameters.get('diameter', 0)
            
            # Check for positive radius
            if radius <= 0:
                return ValidationResult(
                    is_valid=False,
                    error_message="Circle radius must be positive"
                )
            
            # If diameter is provided, check consistency
            if diameter > 0:
                if not abs(diameter - 2 * radius) < self.tolerance:
                    return ValidationResult(
                        is_valid=False,
                        error_message=f"Circle diameter must equal 2 × radius, got diameter={diameter}, radius={radius}"
                    )
            
            return ValidationResult(is_valid=True)
            
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating circle: {str(e)}"
            )
    
    def validate_angle(self, parameters: Dict[str, Any]) -> ValidationResult:
        """Validate angle parameters"""
        try:
            angle = parameters.get('angle', 0)
            
            # Check angle range
            if angle < 0 or angle >= 360:
                return ValidationResult(
                    is_valid=False,
                    error_message=f"Angle must be between 0° and 360°, got {angle}°"
                )
            
            return ValidationResult(is_valid=True)
            
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating angle: {str(e)}"
            )
    
    def validate_pythagorean_triple(self, sides: List[float]) -> bool:
        """Check if three sides form a Pythagorean triple (right triangle)"""
        if len(sides) != 3:
            return False
        
        a, b, c = sorted(sides)
        return abs(a**2 + b**2 - c**2) < self.tolerance
    
    def validate_metric_conversion(self, from_unit: str, to_unit: str, value: float) -> ValidationResult:
        """Validate metric unit conversion parameters"""
        try:
            # Check for positive values
            if value <= 0:
                return ValidationResult(
                    is_valid=False,
                    error_message="Conversion value must be positive"
                )
            
            # Check unit compatibility
            length_units = ['mm', 'cm', 'm', 'km']
            area_units = ['mm²', 'cm²', 'm²', 'km²']
            
            from_length = from_unit in length_units
            from_area = from_unit in area_units
            to_length = to_unit in length_units
            to_area = to_unit in area_units
            
            if from_length != to_length or from_area != to_area:
                return ValidationResult(
                    is_valid=False,
                    error_message=f"Cannot convert between length and area units: {from_unit} to {to_unit}"
                )
            
            return ValidationResult(is_valid=True)
            
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating metric conversion: {str(e)}"
            )
    
    def validate_composite_area(self, parameters: Dict[str, Any]) -> ValidationResult:
        """Validate composite area calculation parameters"""
        try:
            # Check for required parameters
            required_params = ['total_area', 'unshaded_area']
            for param in required_params:
                if param not in parameters:
                    return ValidationResult(
                        is_valid=False,
                        error_message=f"Missing required parameter: {param}"
                    )
            
            total_area = parameters['total_area']
            unshaded_area = parameters['unshaded_area']
            
            # Check for positive areas
            if total_area <= 0 or unshaded_area <= 0:
                return ValidationResult(
                    is_valid=False,
                    error_message="Areas must be positive"
                )
            
            # Check that unshaded area is not greater than total area
            if unshaded_area > total_area:
                return ValidationResult(
                    is_valid=False,
                    error_message="Unshaded area cannot be greater than total area"
                )
            
            # Calculate shaded area
            shaded_area = total_area - unshaded_area
            
            # Check for reasonable shaded area (not negative)
            if shaded_area < 0:
                return ValidationResult(
                    is_valid=False,
                    error_message="Shaded area cannot be negative"
                )
            
            return ValidationResult(is_valid=True)
            
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating composite area: {str(e)}"
            )
    
    def validate_parameters(self, shape_type: ShapeType, parameters: Dict[str, Any]) -> ValidationResult:
        """Main validation method that routes to specific validators"""
        try:
            if shape_type.value.startswith('triangle'):
                return self.validate_triangle(parameters)
            elif shape_type.value in ['square', 'rectangle', 'rhombus', 'parallelogram', 'kite', 'trapezium']:
                return self.validate_quadrilateral(parameters)
            elif shape_type.value.startswith('circle'):
                return self.validate_circle(parameters)
            elif shape_type.value.startswith('angle'):
                return self.validate_angle(parameters)
            else:
                return ValidationResult(
                    is_valid=False,
                    error_message=f"No validator available for shape type: {shape_type}"
                )
                
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                error_message=f"Error validating parameters: {str(e)}"
            )
    
    def get_geometric_constraints(self, shape_type: ShapeType) -> GeometricConstraints:
        """Get geometric constraints for a specific shape type"""
        constraints_map = {
            ShapeType.TRIANGLE_EQUILATERAL: GeometricConstraints(
                shape_type=shape_type,
                constraints=['triangle_inequality', 'angle_sum_180', 'all_sides_equal', 'all_angles_60'],
                parameter_limits={'sides': (1, 20), 'angles': (60, 60)},
                validation_rules=['sides_equal', 'angles_equal_60']
            ),
            ShapeType.TRIANGLE_ISOSCELES: GeometricConstraints(
                shape_type=shape_type,
                constraints=['triangle_inequality', 'angle_sum_180', 'two_sides_equal'],
                parameter_limits={'sides': (1, 20), 'angles': (0, 180)},
                validation_rules=['two_sides_equal']
            ),
            ShapeType.TRIANGLE_RIGHT_ANGLED: GeometricConstraints(
                shape_type=shape_type,
                constraints=['triangle_inequality', 'angle_sum_180', 'pythagorean_theorem'],
                parameter_limits={'sides': (1, 20), 'angles': (0, 180)},
                validation_rules=['pythagorean_triple']
            ),
            ShapeType.SQUARE: GeometricConstraints(
                shape_type=shape_type,
                constraints=['angle_sum_360', 'all_sides_equal', 'all_angles_90'],
                parameter_limits={'sides': (1, 20), 'angles': (90, 90)},
                validation_rules=['sides_equal', 'angles_equal_90']
            ),
            ShapeType.RECTANGLE: GeometricConstraints(
                shape_type=shape_type,
                constraints=['angle_sum_360', 'opposite_sides_equal', 'all_angles_90'],
                parameter_limits={'sides': (1, 20), 'angles': (90, 90)},
                validation_rules=['opposite_sides_equal', 'angles_equal_90']
            ),
            ShapeType.CIRCLE: GeometricConstraints(
                shape_type=shape_type,
                constraints=['positive_radius', 'diameter_equals_2r'],
                parameter_limits={'radius': (0.1, 50)},
                validation_rules=['positive_radius']
            )
        }
        
        return constraints_map.get(shape_type, GeometricConstraints(
            shape_type=shape_type,
            constraints=[],
            parameter_limits={},
            validation_rules=[]
        ))


# Utility functions for common geometric calculations
def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate triangle area using base and height"""
    return 0.5 * base * height


def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate rectangle area"""
    return length * width


def calculate_circle_area(radius: float) -> float:
    """Calculate circle area"""
    return math.pi * radius ** 2


def calculate_circle_circumference(radius: float) -> float:
    """Calculate circle circumference"""
    return 2 * math.pi * radius


def convert_metric_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between metric units"""
    # Length conversions
    length_conversions = {
        'mm': 1, 'cm': 10, 'm': 1000, 'km': 1000000
    }
    
    # Area conversions (squared)
    area_conversions = {
        'mm²': 1, 'cm²': 100, 'm²': 1000000, 'km²': 1000000000000
    }
    
    if from_unit in length_conversions and to_unit in length_conversions:
        return value * length_conversions[from_unit] / length_conversions[to_unit]
    elif from_unit in area_conversions and to_unit in area_conversions:
        return value * area_conversions[from_unit] / area_conversions[to_unit]
    else:
        raise ValueError(f"Cannot convert from {from_unit} to {to_unit}")


def round_to_precision(value: float, precision: int = 1) -> float:
    """Round value to specified decimal precision"""
    return round(value, precision)
