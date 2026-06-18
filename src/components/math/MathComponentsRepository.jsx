import React, { useState, useEffect } from 'react';
import { X, FunctionSquare, Ruler, Calculator, BarChart3, PieChart, LineChart, Square, Circle, Triangle, Compass, Settings, RulerIcon, Sigma, ArrowRight, Grid, BookOpen, Target, Zap, Bell, Box } from 'lucide-react';
import VisualToolOverlay from '../workspace/VisualToolOverlay';

// Import all math components
import NumberLineInput from './NumberLineInput';
import FractionVisualizer from './FractionVisualizer';
import ComplexNumbersInput from './ComplexNumbersInput';
import GeometricConstructionInput from './GeometricConstructionInput';
import StatisticalAnalysisInput from './StatisticalAnalysisInput';
import CoordinatePlaneInput from './CoordinatePlaneInput';
import ProbabilitySimulator from './ProbabilitySimulator';
import AlgebraicExpressionBuilder from './AlgebraicExpressionBuilder';
import VectorCalculator from './VectorCalculator';
import MatrixCalculator from './MatrixCalculator';
import CalculusTools from './CalculusTools';
import MathematicalInstruments from './MathematicalInstruments';
import QuadraticGraphInput from './QuadraticGraphInput';
import TrigonometricFunctionInput from './TrigonometricFunctionInput';
import CircleInput from './CircleInput';
import HyperbolicFunctionInput from './HyperbolicFunctionInput';
import BarChartInput from './BarChartInput';
import LineGraphInput from './LineGraphInput';
import PieChartInput from './PieChartInput';
import LinearFunctionGraph from './LinearFunctionGraph';
import CubicFunctionGraph from './CubicFunctionGraph';

import BoxWhiskerPlot from './BoxWhiskerPlot';
import ScatterPlot from './ScatterPlot';
import Histogram from './Histogram';
import VennDiagram from './VennDiagram';
import TreeDiagram from './TreeDiagram';
import PolarCoordinateSystem from './PolarCoordinateSystem';
import ThreeDCoordinateSystem from './ThreeDCoordinateSystem';
import StemAndLeafPlot from './StemAndLeafPlot';
import FrequencyPolygon from './FrequencyPolygon';
import NormalDistribution from './NormalDistribution';
import CumulativeFrequencyCurve from './CumulativeFrequencyCurve';
import ComplexNumberPlane from './ComplexNumberPlane';
import ConicSections from './ConicSections';
import GeometryStudio from './GeometryStudio';

// Import thumbnail registry
import MathComponentThumbnail, { hasThumbnail } from './ThumbnailRegistry';

const MathComponentsRepository = ({ onSelectComponent, isVisible, selectedSubject, selectedGrade, aiRequest = null, setView }) => {
    // Custom scrollbar styles
    useEffect(() => {
        const style = document.createElement('style');
        style.textContent = `
            .custom-scrollbar::-webkit-scrollbar {
                width: 8px;
            }
            .custom-scrollbar::-webkit-scrollbar-track {
                background: #f3f4f6;
                border-radius: 4px;
            }
            .custom-scrollbar::-webkit-scrollbar-thumb {
                background: #d1d5db;
                border-radius: 4px;
            }
            .custom-scrollbar::-webkit-scrollbar-thumb:hover {
                background: #9ca3af;
            }
            .custom-scrollbar {
                scrollbar-width: thin;
                scrollbar-color: #d1d5db #f3f4f6;
            }
        `;
        document.head.appendChild(style);
        
        return () => {
            document.head.removeChild(style);
        };
    }, []);
    const [selectedComponent, setSelectedComponent] = useState(null);
    const [componentData, setComponentData] = useState(null);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [aiMode, setAiMode] = useState(false);
    const [aiParameters, setAiParameters] = useState(null);
    const [isFullScreen, setIsFullScreen] = useState(false);

    // All available mathematical components with metadata
    const mathComponents = [
        {
            id: 'number_line',
            name: 'Number Line',
            description: 'Interactive number line for visualizing numbers and operations',
            icon: Ruler,
            category: 'Number Systems',
            gradeLevel: '7-9',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'number_line_data',
            initialData: {
                title: "Number Line",
                start: -10,
                end: 10,
                showIntegers: true,
                showFractions: false,
                showDecimals: false,
                showOperations: true
            }
        },
        {
            id: 'complex_numbers',
            name: 'Complex Numbers',
            description: 'Calculator and visualizer for complex numbers, imaginary numbers, and Argand diagrams',
            icon: Calculator,
            category: 'Number Systems',
            gradeLevel: '10-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'complex_numbers_data',
            initialData: {
                title: "Complex Numbers Calculator",
                operation: 'add',
                viewMode: 'calculator',
                z1_real: 3,
                z1_imag: 2,
                z2_real: 1,
                z2_imag: -1,
                simplifyExpression: 'sqrt(-16) + sqrt(-4) - sqrt(-1)',
                equationInput: '2x - 15i = 3 + 5yi',
                showGrid: true,
                showAxes: true,
                showUnitCircle: false,
                showPolarForm: false
            }
        },
        {
            id: 'fraction_visualizer',
            name: 'Fraction Visualizer',
            description: 'Interactive fraction visualization with circles and rectangles',
            icon: Circle,
            category: 'Number Systems',
            gradeLevel: '7-9',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'fraction_visualizer_data',
            initialData: {
                title: "Fraction Visualizer",
                numerator: 3,
                denominator: 4,
                shape: 'circle',
                showEquivalent: true,
                showDecimal: true,
                showPercentage: true
            }
        },
        {
            id: 'linear_function',
            name: 'Linear Function Graph',
            description: 'Interactive linear function graphing with slope and y-intercept analysis',
            icon: FunctionSquare,
            category: 'Algebra & Geometry',
            gradeLevel: '7-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'linear_function_data',
            initialData: {
                title: "Linear Function",
                m: 2,
                c: 3,
                x_range: [-10, 10],
                y_range: [-20, 20],
                lineColor: '#3B82F6',
                showGrid: true,
                showPoints: true,
                showSlope: true,
                showYIntercept: true,
                showXIntercept: true
            }
        },
        {
            id: 'quadratic_function',
            name: 'Quadratic Function Graph',
            description: 'Interactive quadratic function graphing with vertex and roots analysis',
            icon: FunctionSquare,
            category: 'Algebra & Geometry',
            gradeLevel: '8-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'quadratic_function_data',
            initialData: {
                title: "Quadratic Function",
                a: 1,
                b: -2,
                c: 1,
                x_range: [-5, 5],
                y_range: [-5, 10],
                lineColor: '#3B82F6',
                showGrid: true,
                showPoints: true,
                showVertex: true,
                showRoots: true,
                showAxisOfSymmetry: true
            }
        },
        {
            id: 'cubic_function',
            name: 'Cubic Function Graph',
            description: 'Interactive cubic function graphing with roots and turning points analysis',
            icon: FunctionSquare,
            category: 'Algebra & Geometry',
            gradeLevel: '10-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'cubic_function_data',
            initialData: {
                title: "Cubic Function",
                a: 1,
                b: 0,
                c: -4,
                d: 0,
                x_range: [-5, 5],
                y_range: [-20, 20],
                lineColor: '#3B82F6',
                showGrid: true,
                showPoints: true,
                showRoots: true,
                showTurningPoints: true
            }
        },
        {
            id: 'exponential_function',
            name: 'Exponential Function Graph',
            description: 'Interactive exponential function graphing with growth and decay analysis',
            icon: FunctionSquare,
            category: 'Algebra & Geometry',
            gradeLevel: '10-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'exponential_function_data',
            initialData: {
                title: "Exponential Function",
                a: 1,
                b: 2,
                c: 0,
                d: 0,
                x_range: [-5, 5],
                y_range: [0, 50],
                lineColor: '#3B82F6',
                showGrid: true,
                showPoints: true,
                showAsymptote: true
            }
        },
        {
            id: 'logarithmic_function',
            name: 'Logarithmic Function Graph',
            description: 'Interactive logarithmic function graphing with domain and range analysis',
            icon: FunctionSquare,
            category: 'Algebra & Geometry',
            gradeLevel: '10-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'logarithmic_function_data',
            initialData: {
                title: "Logarithmic Function",
                a: 1,
                b: 1,
                c: 0,
                d: 0,
                base: 10,
                x_range: [0.1, 10],
                y_range: [-5, 5],
                lineColor: '#3B82F6',
                showGrid: true,
                showPoints: true,
                showAsymptote: true
            }
        },
        {
            id: 'coordinate_plane',
            name: 'Coordinate Plane',
            description: 'Interactive coordinate plane for plotting points and shapes',
            icon: Grid,
            category: 'Geometry',
            gradeLevel: '7-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'coordinate_plane_data',
            initialData: {
                title: "Coordinate Plane",
                x_range: [-10, 10],
                y_range: [-10, 10],
                showGrid: true,
                showAxes: true,
                showNumbers: true,
                points: [],
                shapes: []
            }
        },
        {
            id: 'box_whisker_plot',
            name: 'Box and Whisker Plot',
            description: 'Interactive box and whisker plot creation',
            icon: BarChart3,
            category: 'Statistics & Data',
            gradeLevel: '9-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'box_whisker_plot_data',
            initialData: {
                title: "Box and Whisker Plot",
                data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                showOutliers: true,
                showStatistics: true,
                showGrid: true
            }
        },
        {
            id: 'scatter_plot',
            name: 'Scatter Plot',
            description: 'Interactive scatter plot creation and analysis',
            icon: Target,
            category: 'Statistics & Data',
            gradeLevel: '9-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'scatter_plot_data',
            initialData: {
                title: "Scatter Plot",
                data: [[1, 2], [2, 4], [3, 3], [4, 6], [5, 5]],
                showTrendLine: true,
                showCorrelation: true,
                showGrid: true
            }
        },
        {
            id: 'histogram',
            name: 'Histogram',
            description: 'Interactive histogram creation and analysis',
            icon: BarChart3,
            category: 'Statistics & Data',
            gradeLevel: '9-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'histogram_data',
            initialData: {
                title: "Histogram",
                dataSet: [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10],
                binCount: 5,
                x_axis_label: "Values",
                y_axis_label: "Frequency",
                showStatistics: true,
                showGrid: true,
                showBins: true,
                showDataPoints: true,
                color: '#3B82F6',
                gridColor: '#e5e7eb',
                binWidth: 'auto'
            }
        },
        {
            id: 'venn_diagram',
            name: 'Venn Diagram',
            description: 'Interactive Venn diagram creation',
            icon: Circle,
            category: 'Set Theory',
            gradeLevel: '8-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'venn_diagram_data',
            initialData: {
                title: "Venn Diagram",
                sets: [
                    { name: "Set A", elements: ["1", "2", "3"] },
                    { name: "Set B", elements: ["3", "4", "5"] }
                ],
                showIntersection: true,
                showUnion: true,
                showElements: true
            }
        },
        {
            id: 'tree_diagram',
            name: 'Tree Diagram',
            description: 'Interactive tree diagram creation',
            icon: Target,
            category: 'Probability',
            gradeLevel: '9-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'tree_diagram_data',
            initialData: {
                title: "Tree Diagram",
                levels: 2,
                branches: 2,
                probabilities: [0.5, 0.5],
                showProbabilities: true,
                showOutcomes: true
            }
        },
        {
            id: 'geometric_construction',
            name: 'Geometric Construction',
            description: 'Interactive geometric construction tools (compass, ruler, protractor)',
            icon: Compass,
            category: 'Geometry',
            gradeLevel: '7-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'geometric_construction_data',
            initialData: {
                title: "Geometric Construction",
                tools: ['compass', 'ruler', 'protractor'],
                shapes: [],
                measurements: true,
                grid: true
            }
        },
        {
            id: 'statistical_analysis',
            name: 'Statistical Analysis',
            description: 'Interactive statistical analysis with data visualization',
            icon: BarChart3,
            category: 'Statistics',
            gradeLevel: '8-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'statistical_analysis_data',
            initialData: {
                title: "Statistical Analysis",
                data: [],
                chartType: 'histogram',
                showMean: true,
                showMedian: true,
                showMode: true,
                showRange: true
            }
        },
        {
            id: 'probability_simulator',
            name: 'Probability Simulator',
            description: 'Interactive probability simulations and experiments',
            icon: Target,
            category: 'Probability',
            gradeLevel: '8-12',
            subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
            componentType: 'probability_simulator_data',
            initialData: {
                title: "Probability Simulator",
                experimentType: 'coin_flip',
                trials: 100,
                showResults: true,
                showGraph: true
            }
        },
        {
            id: 'algebraic_expression_builder',
            name: 'Algebraic Expression Builder',
            description: 'Interactive algebraic expression manipulation with step-by-step solutions',
            icon: FunctionSquare,
            category: 'Algebra & Geometry',
            gradeLevel: '7-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'algebraic_expression_builder_data',
            initialData: {
                title: "Algebraic Expression Builder",
                expression: "",
                targetOperation: 'simplify',
                variable: 'x',
                showSteps: true,
                showGraph: false,
                xMin: -10,
                xMax: 10
            }
        },
        {
            id: 'geometry_studio',
            name: 'Geometry Studio',
            description: 'Comprehensive geometry tool with 2D constructions, 3D shapes, and advanced geometry',
            icon: Compass,
            category: 'Algebra & Geometry',
            gradeLevel: '7-12',
            subjects: ['Mathematics', 'Technical Mathematics'],
            componentType: 'geometry_studio_data',
            initialData: {
                title: "Geometry Studio",
                mode: '2d',
                viewMode: 'construction',
                showGrid: true,
                showAxes: true,
                showLabels: true,
                gridSize: 20,
                unitScale: 1,
                backgroundColor: '#ffffff',
                gridColor: '#e5e7eb',
                axisColor: '#374151',
                shapeColor: '#3B82F6',
                pointColor: '#EF4444',
                lineColor: '#10B981',
                points: [],
                lines: [],
                shapes: [],
                shapes3D: [],
                circles: [],
                angles: [],
                sectors: []
            }
        }
    ];

    // Filter components based on subject and grade
    const filteredComponents = mathComponents.filter(component => {
        if (!selectedSubject?.name || !selectedGrade) return true;
        
        const subjectName = selectedSubject.name;
        const grade = parseInt(selectedGrade);
        
        const isIncluded = component.subjects.includes(subjectName) && 
               component.gradeLevel.split('-').some(g => parseInt(g) === grade);
        
        console.log('🔍 MathComponentsRepository: Filtering component', component.id, 'subject:', subjectName, 'grade:', grade, 'included:', isIncluded);
        
        return isIncluded;
    });

    console.log('🔍 MathComponentsRepository: All components:', mathComponents.map(c => c.id));
    console.log('🔍 MathComponentsRepository: Filtered components:', filteredComponents.map(c => c.id));
    console.log('🔍 MathComponentsRepository: algebraic_expression_builder in filtered:', filteredComponents.some(c => c.id === 'algebraic_expression_builder'));

    // Group components by category
    const groupedComponents = filteredComponents.reduce((acc, component) => {
        if (!acc[component.category]) {
            acc[component.category] = [];
        }
        acc[component.category].push(component);
        return acc;
    }, {});

    const handleComponentSelect = (component) => {
        setSelectedComponent(component);
        setComponentData(component.initialData);
        setIsSubmitted(false);
        setAiMode(false);
    };

    const handleSendToWorkspace = () => {
        if (selectedComponent && componentData) {
            onSelectComponent({
                ...selectedComponent,
                data: componentData
            });
        }
    };

    return (
        <VisualToolOverlay
            isVisible={isVisible}
            onClose={() => onSelectComponent(null)}
            title="Mathematical Visual Aids"
            isFullScreen={isFullScreen}
            onToggleFullScreen={() => setIsFullScreen(!isFullScreen)}
            onSendToWorkspace={handleSendToWorkspace}
            workspaceData={selectedComponent && componentData ? { ...selectedComponent, data: componentData } : null}
        >
            <div className="p-4">
                {!selectedComponent ? (
                    // Component selection view
                    <div className="space-y-4">
                        {Object.entries(groupedComponents).map(([category, components]) => (
                            <div key={category} className="space-y-2">
                                <h3 className="text-sm font-semibold text-gray-800 border-b border-gray-200 pb-1">
                                    {category}
                                </h3>
                                <div className="grid grid-cols-1 gap-2">
                                    {components.map((component) => {
                                        const Icon = component.icon;
                                        return (
                                            <div
                                                key={component.id}
                                                onClick={() => handleComponentSelect(component)}
                                                className="flex items-center space-x-3 p-3 border border-gray-200 rounded-lg hover:border-blue-300 hover:shadow-md cursor-pointer transition-all duration-200"
                                            >
                                                <Icon className="h-5 w-5 text-blue-600" />
                                                <div className="flex-1">
                                                    <h4 className="text-sm font-medium text-gray-800">{component.name}</h4>
                                                    <p className="text-xs text-gray-600">{component.description}</p>
                                                    <div className="flex items-center space-x-2 mt-1">
                                                        <span className="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">
                                                            Grade {component.gradeLevel}
                                                        </span>
                                                    </div>
                                                </div>
                                                {/* Simple frontend thumbnail rendering */}
                                                {(() => {
                                                    const hasThumb = hasThumbnail(component.id);
                                                    console.log('🔍 MathComponentsRepository: Component', component.id, 'hasThumbnail:', hasThumb);
                                                    return hasThumb && (
                                                        <div className="flex-shrink-0">
                                                            <MathComponentThumbnail 
                                                                componentId={component.id} 
                                                                width={80} 
                                                                height={60} 
                                                            />
                                                        </div>
                                                    );
                                                })()}
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    // Component configuration view
                    isFullScreen ? (
                        // Fullscreen layout with left pane for parameters
                        <div className="h-full flex">
                            {/* Left pane - Parameter inputs */}
                            <div className="w-80 p-4 border-r border-gray-200 overflow-y-auto">
                                <div className="flex items-center justify-between mb-4">
                                    <h3 className="text-sm font-semibold text-gray-800">{selectedComponent.name}</h3>
                                    <button
                                        onClick={() => setSelectedComponent(null)}
                                        className="text-gray-500 hover:text-gray-700"
                                    >
                                        <X className="h-4 w-4" />
                                    </button>
                                </div>
                                
                                <p className="text-xs text-gray-600 mb-4">{selectedComponent.description}</p>
                                
                                {/* Parameter inputs for linear function */}
                                {selectedComponent.id === 'linear_function' && (
                                    <div className="space-y-4">
                                        <h4 className="font-medium text-gray-700">Parameters</h4>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Slope (m):</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={componentData.m}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, m: parseFloat(e.target.value) || 0 }))}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Y-Intercept (c):</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={componentData.c}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, c: parseFloat(e.target.value) || 0 }))}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                                            <input
                                                type="color"
                                                value={componentData.lineColor}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, lineColor: e.target.value }))}
                                                className="w-full h-10 border border-gray-300 rounded-md"
                                            />
                                        </div>
                                    </div>
                                )}
                                
                                {/* Parameter inputs for histogram */}
                                {selectedComponent.id === 'histogram' && (
                                    <div className="space-y-4">
                                        <h4 className="font-medium text-gray-700">Parameters</h4>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Bin Count:</label>
                                            <input
                                                type="number"
                                                min="1"
                                                max="20"
                                                value={componentData.binCount}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, binCount: parseInt(e.target.value) || 5 }))}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Show Frequencies:</label>
                                            <input
                                                type="checkbox"
                                                checked={componentData.showFrequencies}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, showFrequencies: e.target.checked }))}
                                                className="mr-2"
                                            />
                                            <span className="text-sm text-gray-700">Display frequency counts</span>
                                        </div>
                                    </div>
                                )}
                                
                                {/* Parameter inputs for quadratic function */}
                                {selectedComponent.id === 'quadratic_function' && (
                                    <div className="space-y-4">
                                        <h4 className="font-medium text-gray-700">Parameters</h4>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient a:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={componentData.a}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, a: parseFloat(e.target.value) || 1 }))}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient b:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={componentData.b}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, b: parseFloat(e.target.value) || 0 }))}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient c:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={componentData.c}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, c: parseFloat(e.target.value) || 0 }))}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                                            <input
                                                type="color"
                                                value={componentData.lineColor}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, lineColor: e.target.value }))}
                                                className="w-full h-10 border border-gray-300 rounded-md"
                                            />
                                        </div>
                                    </div>
                                )}
                                
                                {/* Parameter inputs for coordinate plane */}
                                {selectedComponent.id === 'coordinate_plane' && (
                                    <div className="space-y-4">
                                        <h4 className="font-medium text-gray-700">Parameters</h4>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">X Range:</label>
                                            <div className="grid grid-cols-2 gap-2">
                                                <input
                                                    type="number"
                                                    value={componentData.x_range[0]}
                                                    onChange={(e) => setComponentData(prev => ({ 
                                                        ...prev, 
                                                        x_range: [parseFloat(e.target.value) || -10, prev.x_range[1]] 
                                                    }))}
                                                    className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                                                    placeholder="Min"
                                                />
                                                <input
                                                    type="number"
                                                    value={componentData.x_range[1]}
                                                    onChange={(e) => setComponentData(prev => ({ 
                                                        ...prev, 
                                                        x_range: [prev.x_range[0], parseFloat(e.target.value) || 10] 
                                                    }))}
                                                    className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                                                    placeholder="Max"
                                                />
                                            </div>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-1">Show Grid:</label>
                                            <input
                                                type="checkbox"
                                                checked={componentData.showGrid}
                                                onChange={(e) => setComponentData(prev => ({ ...prev, showGrid: e.target.checked }))}
                                                className="mr-2"
                                            />
                                            <span className="text-sm text-gray-700">Display grid lines</span>
                                        </div>
                                    </div>
                                )}
                                
                                {/* Add more parameter panels for other components as needed */}
                                
                                <div className="flex justify-end space-x-2 pt-4 border-t border-gray-200 mt-4">
                                    <button
                                        onClick={() => setSelectedComponent(null)}
                                        className="px-3 py-1 text-sm text-gray-600 hover:text-gray-800"
                                    >
                                        Cancel
                                    </button>
                                    <button
                                        onClick={handleSendToWorkspace}
                                        className="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
                                    >
                                        Add to Workspace
                                    </button>
                                </div>
                            </div>
                            
                            {/* Right pane - Visual aid */}
                            <div className="flex-1 p-4 flex items-center justify-center">
                                {selectedComponent.id === 'linear_function' && (
                                    <LinearFunctionGraph
                                        initialData={componentData}
                                        onChange={setComponentData}
                                        isSubmitted={isSubmitted}
                                        isConfigMode={true}
                                    />
                                )}
                                {selectedComponent.id === 'quadratic_function' && (
                                    <QuadraticGraphInput
                                        data={componentData}
                                        onChange={setComponentData}
                                        isConfigMode={true}
                                    />
                                )}
                                {selectedComponent.id === 'coordinate_plane' && (
                                    <CoordinatePlaneInput
                                        data={componentData}
                                        onChange={setComponentData}
                                        isConfigMode={true}
                                    />
                                )}
                                {selectedComponent.id === 'histogram' && (
                                    <div className="h-full flex">
                                        {/* Left pane - Parameter inputs */}
                                        <div className="w-80 p-4 border-r border-gray-200 overflow-y-auto">
                                            <div className="flex items-center justify-between mb-4">
                                                <h3 className="text-sm font-semibold text-gray-800">Histogram Parameters</h3>
                                            </div>
                                            
                                            <p className="text-xs text-gray-600 mb-4">Configure histogram settings and data</p>
                                            
                                            {/* Parameter inputs for histogram */}
                                            <div className="space-y-4">
                                                <h4 className="font-medium text-gray-700">Display Settings</h4>
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                                                    <input
                                                        type="text"
                                                        value={componentData.title}
                                                        onChange={(e) => setComponentData(prev => ({ ...prev, title: e.target.value }))}
                                                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                                    />
                                                </div>
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-1">Bin Count:</label>
                                                    <input
                                                        type="number"
                                                        min="1"
                                                        max="20"
                                                        value={componentData.binCount}
                                                        onChange={(e) => setComponentData(prev => ({ ...prev, binCount: parseInt(e.target.value) || 5 }))}
                                                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                                    />
                                                </div>
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-1">X-Axis Label:</label>
                                                    <input
                                                        type="text"
                                                        value={componentData.x_axis_label}
                                                        onChange={(e) => setComponentData(prev => ({ ...prev, x_axis_label: e.target.value }))}
                                                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                                    />
                                                </div>
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-1">Y-Axis Label:</label>
                                                    <input
                                                        type="text"
                                                        value={componentData.y_axis_label}
                                                        onChange={(e) => setComponentData(prev => ({ ...prev, y_axis_label: e.target.value }))}
                                                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                                    />
                                                </div>
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-1">Bar Color:</label>
                                                    <input
                                                        type="color"
                                                        value={componentData.color}
                                                        onChange={(e) => setComponentData(prev => ({ ...prev, color: e.target.value }))}
                                                        className="w-full h-10 border border-gray-300 rounded-md"
                                                    />
                                                </div>
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-1">Grid Color:</label>
                                                    <input
                                                        type="color"
                                                        value={componentData.gridColor}
                                                        onChange={(e) => setComponentData(prev => ({ ...prev, gridColor: e.target.value }))}
                                                        className="w-full h-10 border border-gray-300 rounded-md"
                                                    />
                                                </div>
                                                
                                                <h4 className="font-medium text-gray-700 pt-2">Display Options</h4>
                                                <div className="space-y-2">
                                                    <label className="flex items-center">
                                                        <input
                                                            type="checkbox"
                                                            checked={componentData.showGrid}
                                                            onChange={(e) => setComponentData(prev => ({ ...prev, showGrid: e.target.checked }))}
                                                            className="mr-2"
                                                        />
                                                        <span className="text-sm text-gray-700">Show Grid</span>
                                                    </label>
                                                    <label className="flex items-center">
                                                        <input
                                                            type="checkbox"
                                                            checked={componentData.showBins}
                                                            onChange={(e) => setComponentData(prev => ({ ...prev, showBins: e.target.checked }))}
                                                            className="mr-2"
                                                        />
                                                        <span className="text-sm text-gray-700">Show Bin Labels</span>
                                                    </label>
                                                    <label className="flex items-center">
                                                        <input
                                                            type="checkbox"
                                                            checked={componentData.showDataPoints}
                                                            onChange={(e) => setComponentData(prev => ({ ...prev, showDataPoints: e.target.checked }))}
                                                            className="mr-2"
                                                        />
                                                        <span className="text-sm text-gray-700">Show Data Points</span>
                                                    </label>
                                                    <label className="flex items-center">
                                                        <input
                                                            type="checkbox"
                                                            checked={componentData.showStatistics}
                                                            onChange={(e) => setComponentData(prev => ({ ...prev, showStatistics: e.target.checked }))}
                                                            className="mr-2"
                                                        />
                                                        <span className="text-sm text-gray-700">Show Statistics</span>
                                                    </label>
                                                </div>
                                                
                                                <h4 className="font-medium text-gray-700 pt-2">Data Management</h4>
                                                <div className="space-y-2">
                                                    <div>
                                                        <label className="block text-sm font-medium text-gray-700 mb-1">Data Set:</label>
                                                        <textarea
                                                            value={componentData.dataSet.join(', ')}
                                                            onChange={(e) => {
                                                                const numbers = e.target.value.split(',').map(s => s.trim()).filter(s => s !== '').map(s => parseFloat(s)).filter(n => !isNaN(n));
                                                                setComponentData(prev => ({ ...prev, dataSet: numbers }));
                                                            }}
                                                            rows="3"
                                                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                                                            placeholder="Enter numbers separated by commas..."
                                                        />
                                                    </div>
                                                    <div className="flex space-x-2">
                                                        <button
                                                            onClick={() => {
                                                                const newData = [];
                                                                const count = Math.floor(Math.random() * 20) + 10;
                                                                const mean = Math.floor(Math.random() * 10) + 5;
                                                                const stdDev = Math.floor(Math.random() * 3) + 1;
                                                                
                                                                for (let i = 0; i < count; i++) {
                                                                    const u1 = Math.random();
                                                                    const u2 = Math.random();
                                                                    const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
                                                                    const value = mean + z * stdDev;
                                                                    newData.push(Math.max(0, Math.round(value * 10) / 10));
                                                                }
                                                                setComponentData(prev => ({ ...prev, dataSet: newData }));
                                                            }}
                                                            className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                                                        >
                                                            Random Data
                                                        </button>
                                                        <button
                                                            onClick={() => {
                                                                const newData = [];
                                                                const count = Math.floor(Math.random() * 20) + 10;
                                                                const min = Math.floor(Math.random() * 5);
                                                                const max = min + Math.floor(Math.random() * 10) + 5;
                                                                
                                                                for (let i = 0; i < count; i++) {
                                                                    newData.push(Math.floor(Math.random() * (max - min + 1)) + min);
                                                                }
                                                                setComponentData(prev => ({ ...prev, dataSet: newData }));
                                                            }}
                                                            className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                                                        >
                                                            Uniform Data
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        
                                        {/* Right pane - Histogram visualization */}
                                        <div className="flex-1 p-4 flex items-center justify-center">
                                            <Histogram
                                                initialData={componentData}
                                                onChange={setComponentData}
                                                isSubmitted={isSubmitted}
                                                isConfigMode={true}
                                            />
                                        </div>
                                    </div>
                                )}
                                {selectedComponent.id === 'scatter_plot' && (
                                    <ScatterPlot
                                        initialData={componentData}
                                        onChange={setComponentData}
                                        isSubmitted={isSubmitted}
                                    />
                                )}
                                {selectedComponent.id === 'venn_diagram' && (
                                    <VennDiagram
                                        initialData={componentData}
                                        onChange={setComponentData}
                                        isSubmitted={isSubmitted}
                                    />
                                )}
                                {selectedComponent.id === 'tree_diagram' && (
                                    <TreeDiagram
                                        initialData={componentData}
                                        onChange={setComponentData}
                                        isSubmitted={isSubmitted}
                                    />
                                )}
                                {selectedComponent.id === 'geometric_construction' && (
                                    <GeometricConstructionInput
                                        data={componentData}
                                        onChange={setComponentData}
                                        isConfigMode={true}
                                    />
                                )}
                                {selectedComponent.id === 'statistical_analysis' && (
                                    <StatisticalAnalysisInput
                                        data={componentData}
                                        onChange={setComponentData}
                                        isConfigMode={true}
                                    />
                                )}
                                {/* Add more visual aid renderings for other components */}
                            </div>
                        </div>
                    ) : (
                        // Normal layout
                        <div className="space-y-4 overflow-y-auto pr-2 custom-scrollbar" style={{ maxHeight: '85vh' }}>
                            <div className="flex items-center justify-between">
                                <h3 className="text-sm font-semibold text-gray-800">{selectedComponent.name}</h3>
                                <button
                                    onClick={() => setSelectedComponent(null)}
                                    className="text-gray-500 hover:text-gray-700"
                                >
                                    <X className="h-4 w-4" />
                                </button>
                            </div>
                            
                            <p className="text-xs text-gray-600">{selectedComponent.description}</p>
                            
                            {/* Render the appropriate component configuration */}
                            {selectedComponent.id === 'linear_function' && (
                                <LinearFunctionGraph
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                    isConfigMode={true}
                                />
                            )}
                            {selectedComponent.id === 'quadratic_function' && (
                                <QuadraticGraphInput
                                    data={componentData}
                                    onChange={setComponentData}
                                    isConfigMode={true}
                                />
                            )}
                            {selectedComponent.id === 'coordinate_plane' && (
                                <CoordinatePlaneInput
                                    data={componentData}
                                    onChange={setComponentData}
                                    isConfigMode={true}
                                />
                            )}
                            {selectedComponent.id === 'histogram' && (
                                <Histogram
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                />
                            )}
                            {selectedComponent.id === 'scatter_plot' && (
                                <ScatterPlot
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                />
                            )}
                            {selectedComponent.id === 'venn_diagram' && (
                                <VennDiagram
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                />
                            )}
                            {selectedComponent.id === 'tree_diagram' && (
                                <TreeDiagram
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                />
                            )}
                            {selectedComponent.id === 'complex_numbers' && (
                                <ComplexNumbersInput
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                />
                            )}
                            {selectedComponent.id === 'geometric_construction' && (
                                <GeometricConstructionInput
                                    data={componentData}
                                    onChange={setComponentData}
                                    isConfigMode={true}
                                />
                            )}
                            {selectedComponent.id === 'statistical_analysis' && (
                                <StatisticalAnalysisInput
                                    data={componentData}
                                    onChange={setComponentData}
                                    isConfigMode={true}
                                />
                            )}
                            {selectedComponent.id === 'geometry_studio' && (
                                <GeometryStudio
                                    initialData={componentData}
                                    onChange={setComponentData}
                                    isSubmitted={isSubmitted}
                                    setView={setView}
                                />
                            )}
                            
                            <div className="flex justify-end space-x-2 pt-4 border-t border-gray-200">
                                <button
                                    onClick={() => setSelectedComponent(null)}
                                    className="px-3 py-1 text-sm text-gray-600 hover:text-gray-800"
                                >
                                    Cancel
                                </button>
                                <button
                                    onClick={handleSendToWorkspace}
                                    className="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
                                >
                                    Add to Workspace
                                </button>
                            </div>
                        </div>
                    )
                )}
            </div>
        </VisualToolOverlay>
    );
};

export default MathComponentsRepository;
