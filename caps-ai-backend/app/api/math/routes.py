from flask import request, jsonify
from . import math_bp
# from ...utils.math_engine import MathEngine  # Temporarily disabled due to SymPy issues
from ...utils.cache import cache
from ...geometry_diagrams import GeometryDiagramGenerator, Geometry3DCalculator
from ...utils.net_generator import NetGenerator
from ...utils.south_african_3d_problems import SouthAfrican3DProblemGenerator, ProblemCategory
from ...utils.optimized_3d_generator import Optimized3DGenerator

# Import quiz service conditionally to avoid circular imports
try:
    from .quiz_routes import quiz_service
except ImportError:
    quiz_service = None

# math_engine = MathEngine()  # Temporarily disabled due to SymPy issues
net_generator = NetGenerator()
geometry_3d_calculator = Geometry3DCalculator()
south_african_3d_generator = SouthAfrican3DProblemGenerator()
optimized_3d_generator = Optimized3DGenerator()

@math_bp.route('/calculate', methods=['POST'])
@cache.memoize(timeout=300)  # Cache for 5 minutes
def calculate_math_operation():
    """Calculate mathematical operations server-side"""
    data = request.get_json()
    operation = data.get('operation')
    expression = data.get('expression')
    params = data.get('params', {})
    
    try:
        # result = math_engine.calculate(operation, expression, params)  # Temporarily disabled
        result = {"error": "Math engine temporarily disabled"}
        return jsonify({
            'success': True,
            'result': result,
            'operation': operation,
            'expression': expression
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@math_bp.route('/validate', methods=['POST'])
def validate_expression():
    """Validate mathematical expressions"""
    data = request.get_json()
    expression = data.get('expression')
    
    try:
        # is_valid = math_engine.validate(expression)  # Temporarily disabled
        is_valid = True
        return jsonify({
            'valid': is_valid,
            'expression': expression
        })
    except Exception as e:
        return jsonify({
            'valid': False,
            'error': str(e)
        }), 400

@math_bp.route('/solve', methods=['POST'])
def solve_equation():
    """Solve mathematical equations"""
    data = request.get_json()
    equation = data.get('equation')
    
    try:
        # result = math_engine.solve_equation(equation)  # Temporarily disabled
        result = {"error": "Math engine temporarily disabled"}
        return jsonify({
            'success': True,
            'result': result,
            'equation': equation
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@math_bp.route('/evaluate', methods=['POST'])
def evaluate_expression():
    """Evaluate mathematical expressions with optional substitutions"""
    data = request.get_json()
    expression = data.get('expression')
    substitutions = data.get('substitutions', {})
    
    try:
        # result = math_engine.evaluate_expression(expression, substitutions)  # Temporarily disabled
        result = {"error": "Math engine temporarily disabled"}
        return jsonify({
            'success': True,
            'result': result,
            'expression': expression,
            'substitutions': substitutions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# Geometry Diagram Generation Endpoints
@math_bp.route('/geometry/generate-diagram', methods=['POST'])
def generate_geometry_diagram():
    """Generate a 2D or 3D geometric diagram using enhanced generator"""
    try:
        data = request.get_json()
        diagram_type = data.get('diagram_type')
        dimension = data.get('dimension', '2d')
        parameters = data.get('parameters', {})
        
        if not diagram_type:
            return jsonify({"error": "Missing required parameter: diagram_type"}), 400
        
        # Use the enhanced geometry diagram generator
        generator = GeometryDiagramGenerator()
        result = generator.generate_diagram(diagram_type, dimension, parameters)
        
        if result.get('success'):
            return jsonify(result)
        else:
            return jsonify({"error": result.get('error', 'Failed to generate diagram')}), 500
            
    except Exception as e:
        return jsonify({"error": f"Error generating diagram: {str(e)}"}), 500


@math_bp.route('/geometry/available-diagrams', methods=['GET'])
def get_available_diagrams():
    """Get list of available diagram types"""
    try:
        available_diagrams = {
            "2d": ["point", "line", "ray", "segment", "parallel_lines", "perpendicular_lines", 
                   "angle", "angle_arms", "acute_angle", "right_angle", "obtuse_angle", "straight_angle", "reflex_angle", "revolution",
                   "circle", "chord", "segment", "radius", "diameter", "arc", 
                   "equilateral_triangle", "isosceles_triangle", "scalene_triangle", "right_triangle", "acute_triangle", "obtuse_triangle",
                   "square", "rectangle", "rhombus", "parallelogram", "kite", "trapezium",
                   "triangle", "quadrilateral"],
            "3d": ["cube", "sphere", "cylinder", "pyramid"]
        }
        return jsonify({
            "success": True,
            "available_diagrams": available_diagrams
        })
    except Exception as e:
        return jsonify({"error": f"Error getting available diagrams: {str(e)}"}), 500

@math_bp.route('/geometry/calculate-properties', methods=['POST'])
def calculate_geometry_properties():
    """Calculate geometric properties using enhanced generator"""
    try:
        data = request.get_json()
        shape = data.get('shape')
        parameters = data.get('parameters', {})
        include_diagram = data.get('include_diagram', True)
        
        if not shape:
            return jsonify({"error": "Missing required parameter: shape"}), 400
        
        # Use the enhanced geometry diagram generator
        generator = GeometryDiagramGenerator()
        properties = generator.calculate_geometric_properties(shape, parameters)
        
        # Convert GeometricProperties object to dictionary
        result = {
            "success": True,
            "shape": shape,
            "calculations": {
                "area": properties.area,
                "perimeter": properties.perimeter,
                "classification": properties.classification,
                "properties": properties.properties
            }
        }
        
        # Add diagram if requested
        if include_diagram:
            try:
                # Map shape types to diagram types for generation
                diagram_type = shape
                if shape == 'angles':
                    diagram_type = 'angle'
                elif shape in ['acute', 'right', 'obtuse', 'straight', 'reflex']:
                    diagram_type = 'angle'
                
                # Generate a simple diagram for the shape
                diagram_result = generator.generate_diagram(diagram_type, '2d', parameters)
                if diagram_result.get('success'):
                    result["diagram"] = diagram_result.get('image_data')
            except Exception as diagram_error:
                print(f"Warning: Could not generate diagram: {diagram_error}")
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": f"Error calculating properties: {str(e)}"}), 500

# Quiz question generation moved to quiz_routes.py
# This endpoint is now handled by the enhanced quiz system

# 3D Geometry API Endpoints
@math_bp.route('/geometry/generate-3d-diagram', methods=['POST'])
@cache.memoize(timeout=300)  # Cache for 5 minutes
def generate_3d_diagram():
    """Generate 3D geometric diagrams with educational features"""
    try:
        data = request.get_json()
        diagram_type = data.get('diagram_type', 'cube')
        parameters = data.get('parameters', {})
        
        # Initialize the diagram generator
        generator = GeometryDiagramGenerator()
        
        # Generate the 3D diagram
        diagram_result = generator.generate_diagram(diagram_type, '3d', parameters)
        
        if diagram_result.get('success'):
            return jsonify({
                'success': True,
                'diagram_data': diagram_result.get('plotly_data') or diagram_result.get('image_data'),
                'calculations': diagram_result.get('calculations', {}),
                'diagram_type': diagram_type,
                'parameters': parameters
            })
        else:
            return jsonify({
                'success': False,
                'error': diagram_result.get('error', 'Failed to generate 3D diagram')
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error generating 3D diagram: {str(e)}"
        }), 500

@math_bp.route('/geometry/calculate-3d-properties', methods=['POST'])
@cache.memoize(timeout=300)  # Cache for 5 minutes
def calculate_3d_properties():
    """Calculate 3D geometric properties (surface area, volume, capacity)"""
    try:
        data = request.get_json()
        shape_type = data.get('shape_type', 'cube')
        dimensions = data.get('dimensions', {})
        
        # Initialize the 3D calculator
        calculator = Geometry3DCalculator()
        
        # Calculate properties
        calculations = calculator.get_all_calculations(shape_type, dimensions)
        
        return jsonify({
            'success': True,
            'calculations': calculations,
            'shape_type': shape_type,
            'dimensions': dimensions
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error calculating 3D properties: {str(e)}"
        }), 500

@math_bp.route('/geometry/convert-3d-units', methods=['POST'])
def convert_3d_units():
    """Convert between 3D volume units (mm³, cm³, m³)"""
    try:
        data = request.get_json()
        value = data.get('value', 0)
        from_unit = data.get('from_unit', 'cm3')
        to_unit = data.get('to_unit', 'm3')
        
        # Initialize the 3D calculator
        calculator = Geometry3DCalculator()
        
        # Convert units
        converted_value = calculator.convert_volume_units(value, from_unit, to_unit)
        
        return jsonify({
            'success': True,
            'original_value': value,
            'converted_value': converted_value,
            'from_unit': from_unit,
            'to_unit': to_unit
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error converting 3D units: {str(e)}"
        }), 500

# 3D Net Generation Endpoints

@math_bp.route('/geometry/generate-net', methods=['POST'])
@cache.memoize(timeout=600)  # Cache for 10 minutes
def generate_3d_net():
    """Generate 2D net for 3D shapes"""
    data = request.get_json()
    shape_type = data.get('shape_type')  # 'cube' or 'rectangular_prism'
    dimensions = data.get('dimensions', {})
    
    try:
        if shape_type == 'cube':
            side_length = dimensions.get('side_length', 3.0)
            net_image = net_generator.generate_cube_net(side_length)
            
            return jsonify({
                'success': True,
                'net_image': net_image,
                'shape_type': 'cube',
                'dimensions': {'side_length': side_length},
                'instructions': 'Cut along the outer edges and fold along the dashed lines to create a cube'
            })
            
        elif shape_type == 'rectangular_prism':
            length = dimensions.get('length', 4.0)
            breadth = dimensions.get('breadth', 3.0)
            height = dimensions.get('height', 2.0)
            net_image = net_generator.generate_rectangular_prism_net(length, breadth, height)
            
            return jsonify({
                'success': True,
                'net_image': net_image,
                'shape_type': 'rectangular_prism',
                'dimensions': {'length': length, 'breadth': breadth, 'height': height},
                'instructions': 'Cut along the outer edges and fold along the dashed lines to create a rectangular prism'
            })
            
        else:
            return jsonify({
                'success': False,
                'error': f"Unsupported shape type: {shape_type}. Supported types: 'cube', 'rectangular_prism'"
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error generating 3D net: {str(e)}"
        }), 500

@math_bp.route('/geometry/net-types', methods=['GET'])
def get_net_types():
    """Get available net types and their parameters"""
    return jsonify({
        'success': True,
        'net_types': {
            'cube': {
                'description': 'Cube net in cross pattern',
                'parameters': {
                    'side_length': {
                        'type': 'float',
                        'description': 'Length of each side in cm',
                        'default': 3.0,
                        'min': 0.5,
                        'max': 10.0
                    }
                }
            },
            'rectangular_prism': {
                'description': 'Rectangular prism net',
                'parameters': {
                    'length': {
                        'type': 'float',
                        'description': 'Length in cm',
                        'default': 4.0,
                        'min': 0.5,
                        'max': 15.0
                    },
                    'breadth': {
                        'type': 'float',
                        'description': 'Breadth in cm',
                        'default': 3.0,
                        'min': 0.5,
                        'max': 15.0
                    },
                    'height': {
                        'type': 'float',
                        'description': 'Height in cm',
                        'default': 2.0,
                        'min': 0.5,
                        'max': 15.0
                    }
                }
            }
        }
    })

# Interactive 3D Parameter Adjustment Endpoints

@math_bp.route('/geometry/3d/calculate-properties', methods=['POST'])
@cache.memoize(timeout=60)  # Cache for 1 minute
def calculate_interactive_3d_properties():
    """Calculate 3D shape properties in real-time"""
    data = request.get_json()
    shape_type = data.get('shape_type')
    dimensions = data.get('dimensions', {})
    
    try:
        if shape_type == 'cube':
            side_length = dimensions.get('side_length', 3.0)
            volume = side_length ** 3
            surface_area = 6 * (side_length ** 2)
            diagonal = side_length * (3 ** 0.5)
            
            return jsonify({
                'success': True,
                'shape_type': 'cube',
                'dimensions': {'side_length': side_length},
                'properties': {
                    'volume': round(volume, 2),
                    'surface_area': round(surface_area, 2),
                    'diagonal': round(diagonal, 2),
                    'edge_length': side_length
                },
                'formulas': {
                    'volume': 'side³',
                    'surface_area': '6 × side²',
                    'diagonal': 'side × √3'
                }
            })
            
        elif shape_type == 'rectangular_prism':
            length = dimensions.get('length', 4.0)
            breadth = dimensions.get('breadth', 3.0)
            height = dimensions.get('height', 2.0)
            volume = length * breadth * height
            surface_area = 2 * (length * breadth + length * height + breadth * height)
            diagonal = (length ** 2 + breadth ** 2 + height ** 2) ** 0.5
            
            return jsonify({
                'success': True,
                'shape_type': 'rectangular_prism',
                'dimensions': {'length': length, 'breadth': breadth, 'height': height},
                'properties': {
                    'volume': round(volume, 2),
                    'surface_area': round(surface_area, 2),
                    'diagonal': round(diagonal, 2),
                    'length': length,
                    'breadth': breadth,
                    'height': height
                },
                'formulas': {
                    'volume': 'l × w × h',
                    'surface_area': '2(lw + lh + wh)',
                    'diagonal': '√(l² + w² + h²)'
                }
            })
            
        elif shape_type == 'cylinder':
            radius = dimensions.get('radius', 2.0)
            height = dimensions.get('height', 5.0)
            volume = 3.14159 * (radius ** 2) * height
            surface_area = 2 * 3.14159 * radius * (radius + height)
            
            return jsonify({
                'success': True,
                'shape_type': 'cylinder',
                'dimensions': {'radius': radius, 'height': height},
                'properties': {
                    'volume': round(volume, 2),
                    'surface_area': round(surface_area, 2),
                    'radius': radius,
                    'height': height
                },
                'formulas': {
                    'volume': 'π × r² × h',
                    'surface_area': '2πr(r + h)'
                }
            })
            
        elif shape_type == 'sphere':
            radius = dimensions.get('radius', 3.0)
            volume = (4/3) * 3.14159 * (radius ** 3)
            surface_area = 4 * 3.14159 * (radius ** 2)
            
            return jsonify({
                'success': True,
                'shape_type': 'sphere',
                'dimensions': {'radius': radius},
                'properties': {
                    'volume': round(volume, 2),
                    'surface_area': round(surface_area, 2),
                    'radius': radius
                },
                'formulas': {
                    'volume': '(4/3)πr³',
                    'surface_area': '4πr²'
                }
            })
            
        else:
            return jsonify({
                'success': False,
                'error': f"Unsupported shape type: {shape_type}"
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error calculating 3D properties: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/generate-interactive', methods=['POST'])
@cache.memoize(timeout=600)  # Cache for 10 minutes - 3D diagrams are expensive to generate
def generate_interactive_3d():
    """Generate interactive 3D visualization with real-time parameters"""
    data = request.get_json()
    shape_type = data.get('shape_type')
    dimensions = data.get('dimensions', {})
    
    try:
        # Use GeometryDiagramGenerator for 3D diagrams
        diagram_generator = GeometryDiagramGenerator()
        
        if shape_type == 'cube':
            side_length = dimensions.get('side_length', 3.0)
            diagram_data = diagram_generator.generate_3d_diagram('cube', {
                'side_length': side_length
            })
            
        elif shape_type == 'rectangular_prism':
            length = dimensions.get('length', 4.0)
            breadth = dimensions.get('breadth', 3.0)
            height = dimensions.get('height', 2.0)
            diagram_data = diagram_generator.generate_3d_diagram('rectangular_prism', {
                'length': length,
                'breadth': breadth,
                'height': height
            })
            
        elif shape_type == 'cylinder':
            radius = dimensions.get('radius', 2.0)
            height = dimensions.get('height', 5.0)
            diagram_data = diagram_generator.generate_3d_diagram('cylinder', {
                'radius': radius,
                'height': height
            })
            
        elif shape_type == 'sphere':
            radius = dimensions.get('radius', 3.0)
            diagram_data = diagram_generator.generate_3d_diagram('sphere', {
                'radius': radius
            })
            
        else:
            return jsonify({
                'success': False,
                'error': f"Unsupported shape type: {shape_type}"
            }), 400
            
        return jsonify({
            'success': True,
            'shape_type': shape_type,
            'dimensions': dimensions,
            'diagram_data': diagram_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error generating interactive 3D: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/shape-types', methods=['GET'])
def get_3d_shape_types():
    """Get available 3D shape types for interactive adjustment"""
    return jsonify({
        'success': True,
        'shape_types': {
            'cube': {
                'name': 'Cube',
                'description': 'A 3D shape with 6 equal square faces',
                'parameters': {
                    'side_length': {
                        'type': 'float',
                        'label': 'Side Length (cm)',
                        'min': 0.5,
                        'max': 10.0,
                        'step': 0.1,
                        'default': 3.0
                    }
                }
            },
            'rectangular_prism': {
                'name': 'Rectangular Prism',
                'description': 'A 3D shape with 6 rectangular faces',
                'parameters': {
                    'length': {
                        'type': 'float',
                        'label': 'Length (cm)',
                        'min': 0.5,
                        'max': 15.0,
                        'step': 0.1,
                        'default': 4.0
                    },
                    'breadth': {
                        'type': 'float',
                        'label': 'Breadth (cm)',
                        'min': 0.5,
                        'max': 15.0,
                        'step': 0.1,
                        'default': 3.0
                    },
                    'height': {
                        'type': 'float',
                        'label': 'Height (cm)',
                        'min': 0.5,
                        'max': 15.0,
                        'step': 0.1,
                        'default': 2.0
                    }
                }
            },
            'cylinder': {
                'name': 'Cylinder',
                'description': 'A 3D shape with circular bases and curved surface',
                'parameters': {
                    'radius': {
                        'type': 'float',
                        'label': 'Radius (cm)',
                        'min': 0.5,
                        'max': 10.0,
                        'step': 0.1,
                        'default': 2.0
                    },
                    'height': {
                        'type': 'float',
                        'label': 'Height (cm)',
                        'min': 0.5,
                        'max': 20.0,
                        'step': 0.1,
                        'default': 5.0
                    }
                }
            },
            'sphere': {
                'name': 'Sphere',
                'description': 'A perfectly round 3D shape',
                'parameters': {
                    'radius': {
                        'type': 'float',
                        'label': 'Radius (cm)',
                        'min': 0.5,
                        'max': 10.0,
                        'step': 0.1,
                        'default': 3.0
                    }
                }
            }
        }
    })

# Optimized 3D Generation Endpoints

@math_bp.route('/geometry/3d/generate-optimized', methods=['POST'])
@cache.memoize(timeout=900)  # Cache for 15 minutes - optimized diagrams
def generate_optimized_3d():
    """Generate optimized 3D visualization with improved performance"""
    data = request.get_json()
    shape_type = data.get('shape_type')
    dimensions = data.get('dimensions', {})
    
    try:
        if shape_type == 'cube':
            side_length = dimensions.get('side_length', 3.0)
            diagram_data = optimized_3d_generator.generate_optimized_cube(side_length)
            
        elif shape_type == 'rectangular_prism':
            length = dimensions.get('length', 4.0)
            breadth = dimensions.get('breadth', 3.0)
            height = dimensions.get('height', 2.0)
            diagram_data = optimized_3d_generator.generate_optimized_rectangular_prism(length, breadth, height)
            
        elif shape_type == 'cylinder':
            radius = dimensions.get('radius', 2.0)
            height = dimensions.get('height', 5.0)
            diagram_data = optimized_3d_generator.generate_optimized_cylinder(radius, height)
            
        elif shape_type == 'sphere':
            radius = dimensions.get('radius', 3.0)
            diagram_data = optimized_3d_generator.generate_optimized_sphere(radius)
            
        else:
            return jsonify({
                'success': False,
                'error': f"Unsupported shape type: {shape_type}"
            }), 400
            
        return jsonify({
            'success': True,
            'shape_type': shape_type,
            'dimensions': dimensions,
            'diagram_data': diagram_data,
            'optimized': True
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error generating optimized 3D: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/cache-stats', methods=['GET'])
def get_3d_cache_stats():
    """Get 3D diagram cache statistics"""
    try:
        stats = optimized_3d_generator.get_cache_stats()
        return jsonify({
            'success': True,
            'cache_stats': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error getting cache stats: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/clear-cache', methods=['POST'])
def clear_3d_cache():
    """Clear 3D diagram cache"""
    try:
        optimized_3d_generator.clear_cache()
        return jsonify({
            'success': True,
            'message': '3D diagram cache cleared successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error clearing cache: {str(e)}"
        }), 500

# South African Context 3D Problems API Endpoints

@math_bp.route('/geometry/3d/south-african/problems', methods=['GET'])
@cache.memoize(timeout=1800)  # Cache for 30 minutes - problems don't change often
def get_south_african_3d_problems():
    """Get all South African context 3D problems with optional filtering"""
    category = request.args.get('category')
    difficulty = request.args.get('difficulty')
    
    try:
        if category and difficulty:
            problems = south_african_3d_generator.get_problem_by_category(ProblemCategory(category))
            problems = [p for p in problems if p.difficulty == difficulty]
        elif category:
            problems = south_african_3d_generator.get_problem_by_category(ProblemCategory(category))
        elif difficulty:
            problems = south_african_3d_generator.get_problem_by_difficulty(difficulty)
        else:
            problems = south_african_3d_generator.problems
        
        # Convert to JSON-serializable format
        problems_data = []
        for problem in problems:
            problems_data.append({
                'id': problem.id,
                'title': problem.title,
                'description': problem.description,
                'category': problem.category.value,
                'shape_type': problem.shape_type,
                'given_values': problem.given_values,
                'question': problem.question,
                'solution_steps': problem.solution_steps,
                'answer': problem.answer,
                'units': problem.units,
                'cultural_context': problem.cultural_context,
                'difficulty': problem.difficulty
            })
        
        return jsonify({
            'success': True,
            'problems': problems_data,
            'total_count': len(problems_data)
        })
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error retrieving problems: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/south-african/problem/<problem_id>', methods=['GET'])
def get_south_african_3d_problem(problem_id):
    """Get a specific South African context 3D problem by ID"""
    try:
        problem = south_african_3d_generator.get_problem_by_id(problem_id)
        
        problem_data = {
            'id': problem.id,
            'title': problem.title,
            'description': problem.description,
            'category': problem.category.value,
            'shape_type': problem.shape_type,
            'given_values': problem.given_values,
            'question': problem.question,
            'solution_steps': problem.solution_steps,
            'answer': problem.answer,
            'units': problem.units,
            'cultural_context': problem.cultural_context,
            'difficulty': problem.difficulty
        }
        
        return jsonify({
            'success': True,
            'problem': problem_data
        })
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error retrieving problem: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/south-african/random', methods=['GET'])
def get_random_south_african_3d_problem():
    """Get a random South African context 3D problem"""
    category = request.args.get('category')
    difficulty = request.args.get('difficulty')
    
    try:
        if category and difficulty:
            problem = south_african_3d_generator.get_random_problem(
                ProblemCategory(category), difficulty
            )
        elif category:
            problem = south_african_3d_generator.get_random_problem(
                category=ProblemCategory(category)
            )
        elif difficulty:
            problem = south_african_3d_generator.get_random_problem(difficulty=difficulty)
        else:
            problem = south_african_3d_generator.get_random_problem()
        
        problem_data = {
            'id': problem.id,
            'title': problem.title,
            'description': problem.description,
            'category': problem.category.value,
            'shape_type': problem.shape_type,
            'given_values': problem.given_values,
            'question': problem.question,
            'solution_steps': problem.solution_steps,
            'answer': problem.answer,
            'units': problem.units,
            'cultural_context': problem.cultural_context,
            'difficulty': problem.difficulty
        }
        
        return jsonify({
            'success': True,
            'problem': problem_data
        })
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error retrieving random problem: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/south-african/categories', methods=['GET'])
@cache.memoize(timeout=3600)  # Cache for 1 hour - categories never change
def get_south_african_3d_categories():
    """Get all available South African context problem categories"""
    try:
        categories = south_african_3d_generator.get_all_categories()
        categories_data = [{'value': cat.value, 'label': cat.value.replace('_', ' ').title()} for cat in categories]
        
        return jsonify({
            'success': True,
            'categories': categories_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error retrieving categories: {str(e)}"
        }), 500

@math_bp.route('/geometry/3d/south-african/statistics', methods=['GET'])
@cache.memoize(timeout=1800)  # Cache for 30 minutes - statistics don't change often
def get_south_african_3d_statistics():
    """Get statistics about available South African context problems"""
    try:
        stats = south_african_3d_generator.get_problem_statistics()
        
        return jsonify({
            'success': True,
            'statistics': stats
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error retrieving statistics: {str(e)}"
        }), 500
