import React from 'react';
import { Calculator, Hash, Shapes, BarChart3, FunctionSquare, Circle, Square, Triangle, Zap, Target, PieChart, TrendingUp } from 'lucide-react';

const MathematicalVisualAids = ({ onComponentSelect }) => {
    const handleComponentClick = (component) => {
        if (onComponentSelect) {
            onComponentSelect(component);
        }
    };

    const visualAids = [
        // Number Systems
        {
            category: 'Number Systems',
            color: 'bg-blue-500',
            icon: Hash,
            tools: [
                {
                    name: 'Number Line',
                    description: 'Interactive number line for visualizing numbers and operations',
                    type: 'number_line',
                    component: 'NumberLineInput',
                    icon: Calculator
                },
                {
                    name: 'Complex Numbers',
                    description: 'Calculator, Argand diagram, and polar form conversion',
                    type: 'complex_numbers',
                    component: 'ComplexNumbersInput',
                    icon: FunctionSquare
                },
                {
                    name: 'Fraction Visualizer',
                    description: 'Visual representation and manipulation of fractions',
                    type: 'fraction_visualizer',
                    component: 'FractionVisualizer',
                    icon: PieChart
                }
            ]
        },
        // Algebra
        {
            category: 'Algebra',
            color: 'bg-green-500',
            icon: FunctionSquare,
            tools: [
                {
                    name: 'Coordinate Plane',
                    description: 'Plot points, functions, and geometric shapes',
                    type: 'coordinate_plane',
                    component: 'CoordinatePlaneInput',
                    icon: Target
                },
                {
                    name: 'Algebraic Expressions',
                    description: 'Build, simplify, and solve algebraic expressions',
                    type: 'algebraic_expression_builder',
                    component: 'AlgebraicExpressionBuilder',
                    icon: TrendingUp
                },
                {
                    name: 'Matrix Calculator',
                    description: 'Matrix operations and transformations',
                    type: 'matrix_calculator',
                    component: 'MatrixCalculator',
                    icon: Square
                },
                {
                    name: 'Vector Calculator',
                    description: 'Vector operations and visualizations',
                    type: 'vector_calculator',
                    component: 'VectorCalculator',
                    icon: Zap
                }
            ]
        },
        // Geometry
        {
            category: 'Geometry',
            color: 'bg-purple-500',
            icon: Shapes,
            tools: [
                {
                    name: 'Geometric Construction',
                    description: 'Interactive geometric constructions and proofs',
                    type: 'geometric_construction',
                    component: 'GeometricConstructionInput',
                    icon: Triangle
                },
                {
                    name: 'Mathematical Instruments',
                    description: 'Protractor, compass, and ruler tools',
                    type: 'mathematical_instruments',
                    component: 'MathematicalInstruments',
                    icon: Circle
                },
                {
                    name: 'Circle Input',
                    description: 'Circle properties and calculations',
                    type: 'circle_input',
                    component: 'CircleInput',
                    icon: Circle
                },
                {
                    name: 'Conic Sections',
                    description: 'Ellipse, parabola, and hyperbola visualizations',
                    type: 'conic_sections',
                    component: 'ConicSections',
                    icon: Target
                },
                {
                    name: 'Geometry Studio',
                    description: 'Comprehensive 2D and 3D geometry tools',
                    type: 'geometry_studio',
                    component: 'GeometryStudio',
                    icon: Shapes
                },
                {
                    name: '3D Coordinate System',
                    description: 'Three-dimensional coordinate visualization',
                    type: '3d_coordinate_system',
                    component: 'ThreeDCoordinateSystem',
                    icon: Square
                }
            ]
        },
        // Statistics
        {
            category: 'Statistics',
            color: 'bg-orange-500',
            icon: BarChart3,
            tools: [
                {
                    name: 'Statistical Analysis',
                    description: 'Data analysis and statistical calculations',
                    type: 'statistical_analysis',
                    component: 'StatisticalAnalysisInput',
                    icon: BarChart3
                },
                {
                    name: 'Probability Simulator',
                    description: 'Interactive probability simulations',
                    type: 'probability_simulator',
                    component: 'ProbabilitySimulator',
                    icon: PieChart
                }
            ]
        }
    ];

    return (
        <div className="space-y-8">
            {visualAids.map((category) => {
                const CategoryIcon = category.icon;
                return (
                    <div key={category.category} className="space-y-4">
                        {/* Category Header */}
                        <div className="flex items-center space-x-3">
                            <div className={`p-2 rounded-lg ${category.color}`}>
                                <CategoryIcon className="h-6 w-6 text-white" />
                            </div>
                            <h3 className="text-xl font-bold text-gray-800">{category.category}</h3>
                        </div>
                        
                        {/* Tools Grid */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                            {category.tools.map((tool) => {
                                const ToolIcon = tool.icon;
                                return (
                                    <div
                                        key={tool.name}
                                        className="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-lg hover:border-blue-300 transition-all duration-200 cursor-pointer group"
                                        onClick={() => handleComponentClick({
                                            name: tool.name,
                                            category: category.category,
                                            type: tool.type,
                                            component: tool.component
                                        })}
                                    >
                                        <div className="flex items-start space-x-4">
                                            <div className={`p-3 rounded-lg ${category.color} group-hover:scale-110 transition-transform duration-200`}>
                                                <ToolIcon className="h-6 w-6 text-white" />
                                            </div>
                                            <div className="flex-1 min-w-0">
                                                <h4 className="text-lg font-semibold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors">
                                                    {tool.name}
                                                </h4>
                                                <p className="text-sm text-gray-600 leading-relaxed">
                                                    {tool.description}
                                                </p>
                                            </div>
                                        </div>
                                        <div className="mt-4 flex items-center text-blue-600 text-sm font-medium group-hover:text-blue-700">
                                            <span>Open Tool</span>
                                            <svg className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                                            </svg>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                );
            })}
        </div>
    );
};

export default MathematicalVisualAids;