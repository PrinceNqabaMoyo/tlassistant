import React, { useState, useEffect } from 'react';
import GeometryDiagram from '../GeometryDiagram';

const PythonBasicShapes = ({ 
    geometryData, 
    onChange, 
    isSubmitted, 
    selectedSubConcept 
}) => {
    const [selectedTool, setSelectedTool] = useState('point');
    const [diagramParameters, setDiagramParameters] = useState({});
    const [diagramType, setDiagramType] = useState('point');

    // Update diagram parameters when tool or geometry data changes
    useEffect(() => {
        updateDiagramParameters();
    }, [selectedTool, geometryData, selectedSubConcept]);

    const updateDiagramParameters = () => {
        if (!selectedTool) return;
        const params = getParametersForTool(selectedTool, geometryData || {});
        setDiagramParameters(params);
        setDiagramType(getDiagramTypeForTool(selectedTool));
    };

    const getParametersForTool = (tool, data = {}) => {
        const baseParams = {
            size: 3, // 3x size for informal assessment
            showMarkings: true, // Enable enhanced markings
            equalSides: [],
            parallelSides: [],
            rightAngles: [],
            angleMeasurements: {}
        };
        
        switch (tool) {
            case 'point':
                return {
                    ...baseParams,
                    x: 0,
                    y: 0,
                    label: 'P',
                    color: data.pointColor || '#EF4444'
                };
            
            case 'line':
                return {
                    ...baseParams,
                    start: [-2, 0],
                    end: [2, 0],
                    label: 'AB',
                    color: data.lineColor || '#10B981'
                };
            
            case 'ray':
                return {
                    ...baseParams,
                    start: [0, 0],
                    end: [3, 0],
                    label: 'AB',
                    color: data.lineColor || '#10B981'
                };
            
            case 'segment':
                return {
                    ...baseParams,
                    start: [-1.5, 0],
                    end: [1.5, 0],
                    label: 'AB',
                    color: data.lineColor || '#10B981'
                };
            
            case 'circle':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2,
                    color: data.shapeColor || '#3B82F6'
                };
            
            case 'triangle':
                return {
                    ...baseParams,
                    vertices: [[-1, -1], [1, -1], [0, 1]],
                    color: data.shapeColor || '#3B82F6',
                    equalSides: [] // Will be populated based on triangle type
                };
            
            case 'rectangle':
                return {
                    ...baseParams,
                    vertices: [[-1.5, -1], [1.5, -1], [1.5, 1], [-1.5, 1]],
                    color: data.shapeColor || '#3B82F6',
                    parallelSides: [
                        [[-1.5, -1], [1.5, -1]], // top and bottom
                        [[1.5, -1], [1.5, 1]],   // right sides
                        [[1.5, 1], [-1.5, 1]],   // top and bottom
                        [[-1.5, 1], [-1.5, -1]]  // left sides
                    ],
                    rightAngles: [
                        [[-1.5, -1], [1.5, -1], [1.5, 1]], // bottom-right
                        [[1.5, -1], [1.5, 1], [-1.5, 1]],   // top-right
                        [[1.5, 1], [-1.5, 1], [-1.5, -1]],  // top-left
                        [[-1.5, 1], [-1.5, -1], [1.5, -1]]  // bottom-left
                    ]
                };
            
            case 'arms_of_angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [3, 0],
                    arm2: [2, 2],
                    color: data.shapeColor || '#3B82F6',
                    angleMeasurements: { 'angle_1': '45°' }
                };
            
            case 'angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [1, 1.5],
                    type: 'acute',
                    color: data.shapeColor || '#3B82F6',
                    angleMeasurements: { 'angle_1': '45°' }
                };
            
            case 'acute_angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [1.5, 1.2],
                    type: 'acute',
                    color: data.shapeColor || '#10B981',
                    angleMeasurements: { 'angle_1': '45°' }
                };
            
            case 'right_angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [0, 2],
                    type: 'right',
                    color: data.shapeColor || '#EF4444',
                    rightAngles: [[[2, 0], [0, 0], [0, 2]]],
                    angleMeasurements: { 'angle_1': '90°' }
                };
            
            case 'obtuse_angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [-1, 1.5],
                    type: 'obtuse',
                    color: data.shapeColor || '#F97316',
                    angleMeasurements: { 'angle_1': '135°' }
                };
            
            case 'straight_angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [-2, 0],
                    type: 'straight',
                    color: data.shapeColor || '#8B5CF6',
                    angleMeasurements: { 'angle_1': '180°' }
                };
            
            case 'reflex_angle':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [1.5, -1.2],
                    type: 'reflex',
                    color: data.shapeColor || '#6366F1',
                    angleMeasurements: { 'angle_1': '225°' }
                };
            
            case 'revolution':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [2, 0],
                    type: 'revolution',
                    color: data.shapeColor || '#EC4899',
                    angleMeasurements: { 'angle_1': '360°' }
                };
            
            case 'parallel_lines':
                return {
                    ...baseParams,
                    line1: { start: [-2, -1], end: [2, -1] },
                    line2: { start: [-2, 1], end: [2, 1] },
                    color: data.lineColor || '#10B981',
                    parallelSides: [
                        [[-2, -1], [2, -1]],
                        [[-2, 1], [2, 1]]
                    ]
                };
            
            case 'perpendicular_lines':
                return {
                    ...baseParams,
                    line1: { start: [-2, 0], end: [2, 0] },
                    line2: { start: [0, -1.5], end: [0, 1.5] },
                    intersection: [0, 0],
                    color: data.lineColor || '#10B981',
                    rightAngles: [
                        [[-2, 0], [0, 0], [0, 1.5]],
                        [[2, 0], [0, 0], [0, -1.5]]
                    ]
                };
            
            case 'chord':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2,
                    point1: [1.4, 1.4],
                    point2: [1.4, -1.4],
                    color: data.shapeColor || '#3B82F6'
                };
            
            case 'circle_segment':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2,
                    point1: [1.4, 1.4],
                    point2: [1.4, -1.4],
                    color: data.shapeColor || '#3B82F6'
                };
            
            case 'radius':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2,
                    endpoint: [0, 2],
                    color: data.shapeColor || '#10B981'
                };
            
            case 'diameter':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2,
                    point1: [-2, 0],
                    point2: [2, 0],
                    color: data.shapeColor || '#F97316'
                };
            
            case 'arc':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2,
                    point1: [1.4, 1.4],
                    point2: [1.4, -1.4],
                    color: data.shapeColor || '#EF4444'
                };
            
            case 'equilateral_triangle':
                return {
                    ...baseParams,
                    vertices: [[0, 1.73], [-1.5, -0.87], [1.5, -0.87]],
                    color: data.shapeColor || '#3B82F6',
                    equalSides: [
                        [[0, 1.73], [-1.5, -0.87]], // side 1
                        [[-1.5, -0.87], [1.5, -0.87]], // side 2
                        [[1.5, -0.87], [0, 1.73]] // side 3
                    ]
                };
            
            case 'isosceles_triangle':
                return {
                    ...baseParams,
                    vertices: [[0, 2], [-1.5, -1], [1.5, -1]],
                    color: data.shapeColor || '#10B981',
                    equalSides: [
                        [[0, 2], [-1.5, -1]], // side 1
                        [[0, 2], [1.5, -1]] // side 2 (equal to side 1)
                    ]
                };
            
            case 'scalene_triangle':
                return {
                    ...baseParams,
                    vertices: [[-1.5, 1], [2, 0.5], [0, -1.5]],
                    color: data.shapeColor || '#F97316'
                };
            
            case 'right_triangle':
                return {
                    ...baseParams,
                    vertices: [[0, 0], [3, 0], [0, 2]],
                    color: data.shapeColor || '#EF4444',
                    rightAngles: [
                        [[3, 0], [0, 0], [0, 2]] // right angle at origin
                    ]
                };
            
            case 'acute_triangle':
                return {
                    ...baseParams,
                    vertices: [[0, 2], [-1.2, -0.5], [1.2, -0.5]],
                    color: data.shapeColor || '#8B5CF6'
                };
            
            case 'obtuse_triangle':
                return {
                    ...baseParams,
                    vertices: [[-1, 1], [2, 0.5], [0.5, -1.5]],
                    color: data.shapeColor || '#EC4899'
                };
            
            case 'square':
                return {
                    ...baseParams,
                    vertices: [[-1, -1], [1, -1], [1, 1], [-1, 1]],
                    color: data.shapeColor || '#3B82F6',
                    equalSides: [
                        [[-1, -1], [1, -1]], // top and bottom
                        [[1, -1], [1, 1]],   // right sides
                        [[1, 1], [-1, 1]],   // top and bottom
                        [[-1, 1], [-1, -1]]  // left sides
                    ],
                    parallelSides: [
                        [[-1, -1], [1, -1]], // top and bottom
                        [[1, -1], [1, 1]],   // right sides
                        [[1, 1], [-1, 1]],   // top and bottom
                        [[-1, 1], [-1, -1]]  // left sides
                    ],
                    rightAngles: [
                        [[-1, -1], [1, -1], [1, 1]], // bottom-right
                        [[1, -1], [1, 1], [-1, 1]],   // top-right
                        [[1, 1], [-1, 1], [-1, -1]],  // top-left
                        [[-1, 1], [-1, -1], [1, -1]]  // bottom-left
                    ]
                };
            
            // rectangle case already handled above (line 89)
            
            case 'rhombus':
                return {
                    ...baseParams,
                    vertices: [[0, 1.5], [1.5, 0], [0, -1.5], [-1.5, 0]],
                    color: data.shapeColor || '#F97316',
                    equalSides: [
                        [[0, 1.5], [1.5, 0]], // side 1
                        [[1.5, 0], [0, -1.5]], // side 2
                        [[0, -1.5], [-1.5, 0]], // side 3
                        [[-1.5, 0], [0, 1.5]] // side 4
                    ],
                    parallelSides: [
                        [[0, 1.5], [1.5, 0]], // side 1
                        [[0, -1.5], [-1.5, 0]] // side 3 (parallel to side 1)
                    ]
                };
            
            case 'parallelogram':
                return {
                    ...baseParams,
                    vertices: [[-1.5, -0.5], [1.5, -0.5], [2.5, 1.5], [-0.5, 1.5]],
                    color: data.shapeColor || '#8B5CF6',
                    parallelSides: [
                        [[-1.5, -0.5], [1.5, -0.5]], // side 1
                        [[2.5, 1.5], [-0.5, 1.5]] // side 3 (parallel to side 1)
                    ]
                };
            
            case 'kite':
                return {
                    ...baseParams,
                    vertices: [[0, 1.5], [1, 0], [0, -0.5], [-1, 0]],
                    color: data.shapeColor || '#EF4444',
                    equalSides: [
                        [[0, 1.5], [1, 0]], // side 1
                        [[0, 1.5], [-1, 0]] // side 4 (equal to side 1)
                    ]
                };
            
            case 'trapezium':
                return {
                    ...baseParams,
                    vertices: [[-1.5, -1], [1.5, -1], [1, 1], [-1, 1]],
                    color: data.shapeColor || '#EC4899',
                    parallelSides: [
                        [[-1.5, -1], [1.5, -1]], // side 1
                        [[1, 1], [-1, 1]] // side 3 (parallel to side 1)
                    ]
                };
            
            default:
                return {};
        }
    };

    const getDiagramTypeForTool = (tool) => {
        const toolToDiagramMap = {
            'point': 'point',
            'line': 'line',
            'ray': 'ray',
            'segment': 'segment',
            'circle': 'circle',
            'triangle': 'triangle',
            'rectangle': 'quadrilateral',
            'arms_of_angle': 'angle_arms',
            'acute_angle': 'angle',
            'right_angle': 'angle',
            'obtuse_angle': 'angle',
            'straight_angle': 'angle',
            'reflex_angle': 'angle',
            'revolution': 'angle',
            'chord': 'chord',
            'circle_segment': 'circle_segment',
            'radius': 'radius',
            'diameter': 'diameter',
            'arc': 'arc',
            'equilateral_triangle': 'equilateral_triangle',
            'isosceles_triangle': 'isosceles_triangle',
            'scalene_triangle': 'scalene_triangle',
            'right_triangle': 'right_triangle',
            'acute_triangle': 'acute_triangle',
            'obtuse_triangle': 'obtuse_triangle',
            'square': 'square',
            // 'rectangle' already mapped above
            'rhombus': 'rhombus',
            'parallelogram': 'parallelogram',
            'kite': 'kite',
            'trapezium': 'trapezium',
            'parallel_lines': 'parallel_lines',
            'perpendicular_lines': 'perpendicular_lines'
        };
        return toolToDiagramMap[tool] || 'point';
    };

    const handleToolChange = (tool) => {
        setSelectedTool(tool);
        if (onChange) {
            onChange({
                ...geometryData,
                selectedTool: tool
            });
        }
    };

    const handleDiagramError = (error) => {
        console.warn('Diagram generation failed, using fallback:', error);
        // The GeometryDiagram component will automatically fall back to Canvas rendering
    };

    const getToolsForSection = (section) => {
        switch (section) {
            case 'points_and_lines':
                return [
                    { id: 'point', name: 'Point', description: 'Place a point on the plane' },
                    { id: 'line', name: 'Line', description: 'Draw a line extending infinitely' },
                    { id: 'ray', name: 'Ray', description: 'Draw a ray with one endpoint' },
                    { id: 'segment', name: 'Segment', description: 'Draw a line segment' },
                    { id: 'parallel_lines', name: 'Parallel Lines', description: 'Draw parallel lines' },
                    { id: 'perpendicular_lines', name: 'Perpendicular Lines', description: 'Draw perpendicular lines' }
                ];
            case 'angles':
                return [
                    { id: 'arms_of_angle', name: 'Arms of an Angle', description: 'The two rays that form the angle' },
                    { id: 'acute_angle', name: 'Acute Angle', description: 'Less than 90° (0° < θ < 90°)' },
                    { id: 'right_angle', name: 'Right Angle', description: 'Exactly 90° (θ = 90°)' },
                    { id: 'obtuse_angle', name: 'Obtuse Angle', description: 'Between 90° and 180° (90° < θ < 180°)' },
                    { id: 'straight_angle', name: 'Straight Angle', description: 'Exactly 180° (θ = 180°)' },
                    { id: 'reflex_angle', name: 'Reflex Angle', description: 'Between 180° and 360° (180° < θ < 360°)' },
                    { id: 'revolution', name: 'Revolution', description: 'Exactly 360° (θ = 360°)' }
                ];
            case 'circles':
                return [
                    { id: 'chord', name: 'Chord', description: 'Line segment connecting two points on circle' },
                    { id: 'circle_segment', name: 'Segment', description: 'Region between chord and arc' },
                    { id: 'radius', name: 'Radius', description: 'Distance from center to edge (r)' },
                    { id: 'diameter', name: 'Diameter', description: 'Twice the radius (d = 2r)' },
                    { id: 'arc', name: 'Arc', description: 'Part of circumference between two points' }
                ];
            case 'triangles':
                return [
                    { id: 'equilateral_triangle', name: 'Equilateral Triangle', description: 'All sides equal (60° angles)' },
                    { id: 'isosceles_triangle', name: 'Isosceles Triangle', description: 'Two equal sides and angles' },
                    { id: 'scalene_triangle', name: 'Scalene Triangle', description: 'All sides and angles different' },
                    { id: 'right_triangle', name: 'Right-Angled Triangle', description: 'One 90° angle' },
                    { id: 'acute_triangle', name: 'Acute Triangle', description: 'All angles < 90°' },
                    { id: 'obtuse_triangle', name: 'Obtuse Triangle', description: 'One angle > 90°' }
                ];
            case 'quadrilaterals':
                return [
                    { id: 'square', name: 'Square', description: 'All sides equal, all angles 90°' },
                    { id: 'rectangle', name: 'Rectangle', description: 'Opposite sides equal, all angles 90°' },
                    { id: 'rhombus', name: 'Rhombus', description: 'All sides equal, opposite angles equal' },
                    { id: 'parallelogram', name: 'Parallelogram', description: 'Opposite sides parallel and equal' },
                    { id: 'kite', name: 'Kite', description: 'Two pairs of adjacent sides equal' },
                    { id: 'trapezium', name: 'Trapezium', description: 'One pair of parallel sides' }
                ];
            default:
                return [
                    { id: 'point', name: 'Point', description: 'Place a point on the plane' }
                ];
        }
    };

    const tools = getToolsForSection(selectedSubConcept);

    return (
        <div className="h-full flex flex-col">
            {/* Tool Selection */}
            <div className="bg-gray-50 border-b border-gray-200 p-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">
                    {selectedSubConcept === 'points_and_lines' && 'Basic Geometric Elements'}
                    {selectedSubConcept === 'angles' && 'Angle Tools'}
                    {selectedSubConcept === 'circles' && 'Circle Tools'}
                    {selectedSubConcept === 'triangles' && 'Triangle Tools'}
                    {selectedSubConcept === 'quadrilaterals' && 'Quadrilateral Tools'}
                </h3>
                <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
                    {tools.map((tool) => (
                        <button
                            key={tool.id}
                            onClick={() => handleToolChange(tool.id)}
                            disabled={isSubmitted}
                            className={`p-3 rounded-lg text-sm font-medium transition-colors ${
                                selectedTool === tool.id
                                    ? 'bg-blue-600 text-white border-2 border-blue-700'
                                    : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
                            } ${isSubmitted ? 'opacity-50 cursor-not-allowed' : ''}`}
                            title={tool.description}
                        >
                            {tool.name}
                        </button>
                    ))}
                </div>
            </div>

            {/* Diagram Display Area */}
            <div className="flex-1 p-6 bg-white">
                <div className="h-full flex items-center justify-center">
                    <GeometryDiagram
                        type={diagramType}
                        dimension="2d"
                        parameters={diagramParameters}
                        fallbackToCanvas={true}
                        className="max-w-full max-h-full"
                        style={{ minHeight: '400px', minWidth: '400px' }}
                    />
                </div>
            </div>

            {/* Instructions */}
            <div className="bg-blue-50 border-t border-blue-200 p-4">
                <div className="text-sm text-blue-800">
                    <strong>Instructions:</strong> Select a tool above to generate a geometric diagram. 
                    The diagram is generated using Python libraries for mathematical accuracy. 
                    If the backend is unavailable, a fallback Canvas rendering will be used.
                </div>
            </div>
        </div>
    );
};

export default PythonBasicShapes;
