import { buildApiUrl } from '../../utils/apiBaseUrl';
import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import { Plus, Minus, RotateCcw, Maximize2, Grid3X3, Shapes, Box, Zap, Settings, Eye, Construction } from 'lucide-react';
import BasicShapes from './geometry/2D/BasicShapes';
import PythonBasicShapes from './geometry/2D/PythonBasicShapes';
import AIGeometryAssistant from './geometry/AIGeometryAssistant';
import InteractiveParameterControls from './geometry/InteractiveParameterControls';
import VisualFeedbackOverlay from './geometry/VisualFeedbackOverlay';
import ConstructionGuide from './geometry/ConstructionGuide';
import Plotly from 'plotly.js-dist-min';

const GeometryStudio = ({ initialData, onChange, isSubmitted, setView }) => {
    const [geometryData, setGeometryData] = useState(() => {
        const defaultData = {
        title: "Geometry Studio",
        mode: '2d', // '2d', '3d', 'advanced'
            selectedTool: 'basics_of_geometry', // Tool selection within each mode
            selectedConcept: null, // For foundational concepts
            selectedSubConcept: 'points_and_lines', // For sub-concepts within foundational concepts
            // Canvas settings
        showGrid: true,
        showAxes: true,
        backgroundColor: '#ffffff',
            // Geometry data
        points: [],
        lines: [],
        shapes: [],
            // View settings
            isFullscreen: false,
            // Tool-specific data
            toolData: {},
            // Backend integration settings
            usePythonBackend: true
        };
        return { ...defaultData, ...initialData };
    });

    // State for Properties of 2D Shapes panel
    const [selectedShapeType, setSelectedShapeType] = useState('triangles');
    const [shapeProperties, setShapeProperties] = useState(null);
    const [isCalculating, setIsCalculating] = useState(false);

    // State for Calculations involving 2D Shapes panel
    const [selectedCalculation, setSelectedCalculation] = useState('area_perimeter');
    const [quizQuestion, setQuizQuestion] = useState(null);
    const [userAnswer, setUserAnswer] = useState('');
    const [quizResult, setQuizResult] = useState(null);
    const [isGeneratingQuiz, setIsGeneratingQuiz] = useState(false);

    // Educational Features State
    const [hints, setHints] = useState([]);
    const [solutionSteps, setSolutionSteps] = useState([]);
    const [educationalFeedback, setEducationalFeedback] = useState(null);
    const [studentPerformance, setStudentPerformance] = useState({
        correct_percentage: 0.5,
        questions_attempted: 0,
        hints_used: 0,
        time_taken: 0
    });
    const [showHints, setShowHints] = useState(false);
    const [showSolution, setShowSolution] = useState(false);
    const [currentHintIndex, setCurrentHintIndex] = useState(0);
    const [isLoadingEducational, setIsLoadingEducational] = useState(false);

    // 3D Quiz State
    const [selectedQuizType, setSelectedQuizType] = useState('volume');
    const [selectedDifficulty, setSelectedDifficulty] = useState('medium');
    const [isGenerating3DQuiz, setIsGenerating3DQuiz] = useState(false);

    // State for 3D Net Generation
    const [selectedNetType, setSelectedNetType] = useState('cube');
    const [netDimensions, setNetDimensions] = useState({
        cube: { side_length: 3.0 },
        rectangular_prism: { length: 4.0, breadth: 3.0, height: 2.0 }
    });
    const [netImage, setNetImage] = useState(null);
    const [isGeneratingNet, setIsGeneratingNet] = useState(false);

    // State for Interactive 3D Parameter Adjustment
    const [selected3DShape, setSelected3DShape] = useState('cube');
    const [interactiveDimensions, setInteractiveDimensions] = useState({
        cube: { side_length: 3.0 },
        rectangular_prism: { length: 4.0, breadth: 3.0, height: 2.0 },
        cylinder: { radius: 2.0, height: 5.0 },
        sphere: { radius: 3.0 }
    });
    const [interactiveProperties, setInteractiveProperties] = useState(null);
    const [interactiveDiagram, setInteractiveDiagram] = useState(null);
    const [isCalculatingProperties, setIsCalculatingProperties] = useState(false);
    const [isGeneratingInteractive, setIsGeneratingInteractive] = useState(false);
    const [shapeTypes, setShapeTypes] = useState(null);

    // State for South African 3D Problems
    const [sa3dCategories, setSa3dCategories] = useState([]);
    const [selectedSa3dCategory, setSelectedSa3dCategory] = useState('all');
    const [selectedSa3dDifficulty, setSelectedSa3dDifficulty] = useState('all');
    const [currentSa3dProblem, setCurrentSa3dProblem] = useState(null);
    const [isLoadingSa3dProblem, setIsLoadingSa3dProblem] = useState(false);
    const [showSa3dSolution, setShowSa3dSolution] = useState(false);

    const canvasRef = useRef(null);
    const plotlyRef = useRef(null);

    // Educational Features API Functions
    const generateHints = async (question, performance) => {
        if (!question) return;
        
        setIsLoadingEducational(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/generate-hints'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: question,
                    student_performance: performance
                })
            });
            
            const data = await response.json();
            if (data.success) {
                setHints(data.hints);
                setCurrentHintIndex(0);
            } else {
                console.error('Failed to generate hints:', data.error);
            }
        } catch (error) {
            console.error('Error generating hints:', error);
        } finally {
            setIsLoadingEducational(false);
        }
    };

    const generateSolution = async (question) => {
        if (!question) return;
        
        setIsLoadingEducational(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/generate-solution'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: question
                })
            });
            
            const data = await response.json();
            if (data.success) {
                setSolutionSteps(data.solution_steps);
            } else {
                console.error('Failed to generate solution:', data.error);
            }
        } catch (error) {
            console.error('Error generating solution:', error);
        } finally {
            setIsLoadingEducational(false);
        }
    };

    const generateEducationalFeedback = async (question, studentAnswer, performance) => {
        if (!question || !studentAnswer) return;
        
        setIsLoadingEducational(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/generate-feedback'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: question,
                    student_answer: studentAnswer,
                    student_performance: performance
                })
            });
            
            const data = await response.json();
            if (data.success) {
                setEducationalFeedback(data.feedback);
            } else {
                console.error('Failed to generate feedback:', data.error);
            }
        } catch (error) {
            console.error('Error generating feedback:', error);
        } finally {
            setIsLoadingEducational(false);
        }
    };

    // Handle data changes
    const handleFieldChange = (field, value) => {
        console.log('handleFieldChange called:', field, value);
        setGeometryData(prevData => {
            const newData = { ...prevData, [field]: value };
            console.log('New geometry data:', newData);
            if (onChange) {
                onChange(newData);
            }
            return newData;
        });
    };

    // Handle canvas interactions
    const handleCanvasClick = (e) => {
        if (isSubmitted) return;
        // Canvas click handling will be delegated to individual modules
    };

    const handleCanvasHover = (e) => {
        if (isSubmitted) return;
        // Canvas hover handling will be delegated to individual modules
    };

    // Mode definitions
    const modes = [
        { id: '2d', name: '2D Geometry', icon: Shapes, description: 'Points, lines, shapes, and 2D transformations' },
        { id: '3d', name: '3D Geometry', icon: Box, description: '3D shapes, rotations, and spatial geometry' },
        { id: 'advanced', name: 'Advanced', icon: Zap, description: 'Coordinate geometry, proofs, and calculations' }
    ];

    // Tool definitions for each mode
    const getToolsForMode = (mode) => {
        switch (mode) {
            case '2d':
            return [
                    { id: 'basics_of_geometry', name: 'Basics of Geometry', description: 'Points, lines, rays, segments, parallel and perpendicular lines' },
                    { id: 'properties_of_2d_shapes', name: 'Properties of 2D Shapes', description: 'Triangles, circles, angles, quadrilaterals' },
                    { id: 'calculations_2d_shapes', name: 'Calculations involving 2D Shapes', description: 'Area, perimeter, transformations, measurements' },
                ];
        case '3d':
            return [
                { id: 'basics_of_3d_geometry', name: 'Basics of 3D Geometry', description: '3D shapes, nets, and spatial relationships' },
                { id: 'net_generation', name: '3D Net Generation', description: 'Generate 2D nets that fold into 3D shapes' },
                { id: 'interactive_3d', name: 'Interactive 3D Shapes', description: 'Real-time parameter adjustment and visualization' },
                { id: 'south_african_3d', name: 'South African 3D Problems', description: 'Culturally relevant 3D geometry problems from South Africa' },
        { id: 'interactive_controls', name: 'Interactive Controls', description: 'Real-time parameter adjustment and visual feedback' },
        { id: 'construction_guide', name: 'Construction Guide', description: 'Step-by-step construction instructions' },
                { id: 'properties_of_3d_shapes', name: 'Properties of 3D Shapes', description: 'Cubes, rectangular prisms, surface area, volume, capacity' },
                { id: 'calculations_3d_shapes', name: 'Calculations involving 3D Shapes', description: 'Surface area, volume, capacity, and unit conversions' },
                { id: '3d_quiz', name: '3D Quiz', description: 'Test your 3D geometry knowledge' }
            ];
            case 'advanced':
                return [
                    { id: 'coordinate_geometry', name: 'Coordinate Geometry', description: 'Line equations, intersections' },
                    { id: 'transformations', name: 'Transformations', description: 'Reflections, rotations, translations' },
                    { id: 'congruency', name: 'Congruency', description: 'Congruent shapes and proofs' },
                    { id: 'similarity', name: 'Similarity', description: 'Similar shapes and ratios' },
                    { id: 'calculator', name: 'Geometry Calculator', description: 'Area, perimeter, volume calculations' }
                ];
            default:
                return [];
        }
    };

    // 3D Quiz Functions
    const generate3DQuiz = async (quizType, difficulty) => {
        setIsGenerating3DQuiz(true);
        try {
            // Map frontend quiz types to backend question types
            const questionTypeMap = {
                'volume': 'volume_calculation',
                'surface_area': 'surface_area_calculation', 
                'capacity': 'capacity_calculation',
                'shape_recognition': 'three_d_shape_recognition'
            };

            const response = await fetch(buildApiUrl('/api/math/geometry/generate-quiz-question'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question_type: questionTypeMap[quizType],
                    difficulty: difficulty,
                    shape_type: 'cube', // Default shape type
                    count: 1
                })
            });

            if (response.ok) {
                const data = await response.json();
                if (data.success && data.questions && data.questions.length > 0) {
                    setQuizQuestion(data.questions[0]);
                    setUserAnswer('');
                    setQuizResult(null);
                    setShowHints(false);
                    setSolutionSteps([]);
                    setEducationalFeedback(null);
                }
            } else {
                console.error('Failed to generate 3D quiz question');
            }
        } catch (error) {
            console.error('Error generating 3D quiz:', error);
            // Fallback to mock data
            const mockQuestion = {
                question_text: `Calculate the volume of a cube with side length 4 cm.`,
                options: ['64 cm³', '16 cm³', '24 cm³', '32 cm³'],
                correct_answer: '64 cm³',
                explanation: 'Volume = side × side × side = 4 × 4 × 4 = 64 cm³',
                difficulty: 'medium',
                question_type: 'volume_calculation'
            };
            setQuizQuestion(mockQuestion);
            setUserAnswer('');
            setQuizResult(null);
        } finally {
            setIsGenerating3DQuiz(false);
        }
    };

    // Net Generation Functions
    const generateNet = async () => {
        setIsGeneratingNet(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/generate-net'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    shape_type: selectedNetType,
                    dimensions: netDimensions[selectedNetType]
                })
            });
            
            const data = await response.json();
            if (data.success) {
                setNetImage(data.net_image);
            } else {
                console.error('Error generating net:', data.error);
            }
        } catch (error) {
            console.error('Error generating net:', error);
        } finally {
            setIsGeneratingNet(false);
        }
    };

    const updateNetDimensions = (shapeType, dimension, value) => {
        setNetDimensions(prev => ({
            ...prev,
            [shapeType]: {
                ...prev[shapeType],
                [dimension]: parseFloat(value) || 0
            }
        }));
    };

    // Interactive 3D Functions
    const loadShapeTypes = async () => {
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/3d/shape-types'));
            const data = await response.json();
            if (data.success) {
                setShapeTypes(data.shape_types);
            }
        } catch (error) {
            console.error('Error loading shape types:', error);
        }
    };

    const calculate3DProperties = async () => {
        setIsCalculatingProperties(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/3d/calculate-properties'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    shape_type: selected3DShape,
                    dimensions: interactiveDimensions[selected3DShape]
                })
            });
            
            const data = await response.json();
            if (data.success) {
                setInteractiveProperties(data);
            } else {
                console.error('Error calculating properties:', data.error);
            }
        } catch (error) {
            console.error('Error calculating properties:', error);
        } finally {
            setIsCalculatingProperties(false);
        }
    };

    const generateInteractive3D = async () => {
        setIsGeneratingInteractive(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/3d/generate-interactive'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    shape_type: selected3DShape,
                    dimensions: interactiveDimensions[selected3DShape]
                })
            });
            
            const data = await response.json();
            if (data.success) {
                // Parse the JSON string from diagram_data
                const diagramData = JSON.parse(data.diagram_data);
                setInteractiveDiagram(diagramData);
            } else {
                console.error('Error generating interactive 3D:', data.error);
            }
        } catch (error) {
            console.error('Error generating interactive 3D:', error);
        } finally {
            setIsGeneratingInteractive(false);
        }
    };

    const updateInteractiveDimensions = (shapeType, dimension, value) => {
        setInteractiveDimensions(prev => ({
            ...prev,
            [shapeType]: {
                ...prev[shapeType],
                [dimension]: parseFloat(value) || 0
            }
        }));
    };

    const handleDimensionChange = (dimension, value) => {
        updateInteractiveDimensions(selected3DShape, dimension, value);
        // Trigger real-time calculation
        setTimeout(() => {
            calculate3DProperties();
            generateInteractive3D();
        }, 100);
    };

    // South African 3D Problems Functions (memoized for performance)
    const loadSa3dCategories = useCallback(async () => {
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/3d/south-african/categories'));
            const data = await response.json();
            if (data.success) {
                setSa3dCategories(data.categories);
            }
        } catch (error) {
            console.error('Error loading SA 3D categories:', error);
        }
    }, []);

    const loadSa3dProblem = useCallback(async () => {
        setIsLoadingSa3dProblem(true);
        try {
            let url = buildApiUrl('/api/math/geometry/3d/south-african/random');
            const params = new URLSearchParams();
            
            if (selectedSa3dCategory !== 'all') {
                params.append('category', selectedSa3dCategory);
            }
            if (selectedSa3dDifficulty !== 'all') {
                params.append('difficulty', selectedSa3dDifficulty);
            }
            
            if (params.toString()) {
                url += '?' + params.toString();
            }
            
            const response = await fetch(url);
            const data = await response.json();
            if (data.success) {
                setCurrentSa3dProblem(data.problem);
                setShowSa3dSolution(false);
            } else {
                console.error('Error loading SA 3D problem:', data.error);
            }
        } catch (error) {
            console.error('Error loading SA 3D problem:', error);
        } finally {
            setIsLoadingSa3dProblem(false);
        }
    }, [selectedSa3dCategory, selectedSa3dDifficulty]);

    // Load shape types on component mount
    useEffect(() => {
        if (geometryData.mode === '3d' && geometryData.selectedTool === 'interactive_3d') {
            loadShapeTypes();
            calculate3DProperties();
            generateInteractive3D();
        }
    }, [geometryData.mode, geometryData.selectedTool]);

    // Load SA 3D categories when tool is selected (with debouncing)
    useEffect(() => {
        if (geometryData.mode === '3d' && geometryData.selectedTool === 'south_african_3d') {
            const timeoutId = setTimeout(() => {
                loadSa3dCategories();
                loadSa3dProblem();
            }, 100); // Small delay to prevent rapid re-loading
            
            return () => clearTimeout(timeoutId);
        }
    }, [geometryData.mode, geometryData.selectedTool]);

    // Plotly effect for interactive 3D diagrams
    useEffect(() => {
        if (interactiveDiagram && plotlyRef.current) {
            try {
                // Clear previous plot
                plotlyRef.current.innerHTML = '';
                
                // Create new Plotly plot
                window.Plotly.newPlot(plotlyRef.current, interactiveDiagram.data, interactiveDiagram.layout, {
                    responsive: true,
                    displayModeBar: true,
                    displaylogo: false,
                    modeBarButtonsToRemove: ['pan2d', 'lasso2d', 'select2d']
                });
            } catch (error) {
                console.error('Error rendering Plotly diagram:', error);
            }
        }
    }, [interactiveDiagram]);

    // 3D State
    const [shapeDimensions, setShapeDimensions] = useState({
        cube: { side_length: 3 },
        rectangular_prism: { length: 4, breadth: 3, height: 2 }
    });
    const [threeDCalculations, setThreeDCalculations] = useState(null);
    const [isGenerating3D, setIsGenerating3D] = useState(false);
    const [threeDDiagram, setThreeDDiagram] = useState(null);

    // 3D API Functions
    const generate3DDiagram = async (shapeType, dimensions) => {
        setIsGenerating3D(true);
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/generate-3d-diagram'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    diagram_type: shapeType,
                    parameters: {
                        ...dimensions,
                        show_calculations: true
                    }
                })
            });
            
            const data = await response.json();
            if (data.success) {
                setThreeDDiagram(data.diagram_data);
                setThreeDCalculations(data.calculations);
            } else {
                console.error('Failed to generate 3D diagram:', data.error);
            }
        } catch (error) {
            console.error('Error generating 3D diagram:', error);
            // Mock response when backend is not available
            console.log('Backend not available, using mock response');
            const mockCalculations = calculateMock3DProperties(shapeType, dimensions);
            setThreeDDiagram('mock_diagram_data');
            setThreeDCalculations(mockCalculations);
        } finally {
            setIsGenerating3D(false);
        }
    };

    // Mock 3D calculations for testing when backend is not available
    const calculateMock3DProperties = (shapeType, dimensions) => {
        if (shapeType === 'cube') {
            const side = dimensions.side_length || 3;
            return {
                surface_area: Math.round(6 * side * side * 10) / 10,
                volume: Math.round(side * side * side * 10) / 10,
                capacity: Math.round(side * side * side * 10) / 10,
                side_length: side,
                shape_type: 'cube'
            };
        } else if (shapeType === 'rectangular_prism') {
            const { length = 4, breadth = 3, height = 2 } = dimensions;
            return {
                surface_area: Math.round(2 * (length * breadth + breadth * height + height * length) * 10) / 10,
                volume: Math.round(length * breadth * height * 10) / 10,
                capacity: Math.round(length * breadth * height * 10) / 10,
                length,
                breadth,
                height,
                shape_type: 'rectangular_prism'
            };
        }
        return null;
    };

    // Render Plotly 3D diagram
    const renderPlotlyDiagram = (plotlyData) => {
        if (!plotlyData || !plotlyRef.current) return;
        
        try {
            const data = JSON.parse(plotlyData);
            Plotly.newPlot(plotlyRef.current, data.data, data.layout, {
                responsive: true,
                displayModeBar: true,
                displaylogo: false,
                modeBarButtonsToRemove: ['pan2d', 'lasso2d', 'select2d']
            });
        } catch (error) {
            console.error('Error rendering Plotly diagram:', error);
        }
    };

    // Effect to render Plotly diagram when data changes
    useEffect(() => {
        if (threeDDiagram && threeDDiagram !== 'mock_diagram_data') {
            renderPlotlyDiagram(threeDDiagram);
        }
    }, [threeDDiagram]);


    // 3D Rendering Functions
    const render3DBasics = () => {
        return (
            <div className="w-full h-full flex flex-col">
                <div className="bg-white rounded-lg border p-6 mb-4">
                    <h3 className="text-xl font-semibold mb-4">3D Geometry Basics</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h4 className="text-lg font-medium mb-3">3D Shapes</h4>
                            <div className="space-y-3">
                                <div className="flex items-center space-x-3">
                                    <div className="w-8 h-8 bg-blue-100 rounded flex items-center justify-center">
                                        <Box className="w-4 h-4 text-blue-600" />
                                    </div>
                                    <div>
                                        <p className="font-medium">Cube</p>
                                        <p className="text-sm text-gray-600">6 square faces, all edges equal</p>
                                    </div>
                                </div>
                                <div className="flex items-center space-x-3">
                                    <div className="w-8 h-8 bg-green-100 rounded flex items-center justify-center">
                                        <Box className="w-4 h-4 text-green-600" />
                                    </div>
                                    <div>
                                        <p className="font-medium">Rectangular Prism</p>
                                        <p className="text-sm text-gray-600">6 rectangular faces, opposite faces equal</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div>
                            <h4 className="text-lg font-medium mb-3">Key Concepts</h4>
                            <div className="space-y-2 text-sm">
                                <p><strong>Surface Area:</strong> Total area of all faces</p>
                                <p><strong>Volume:</strong> Space inside the shape</p>
                                <p><strong>Capacity:</strong> Volume in liquid units (ml, l)</p>
                                <p><strong>Nets:</strong> 2D patterns that fold to make 3D shapes</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div className="bg-white rounded-lg border p-6">
                    <h4 className="text-lg font-medium mb-4">Interactive 3D Visualization</h4>
                    <div className="text-center text-gray-600">
                        <p>Use the "Properties of 3D Shapes" tool to create interactive 3D diagrams</p>
                        <p className="text-sm mt-2">Or try the "Calculations involving 3D Shapes" for detailed calculations</p>
                    </div>
                </div>
            </div>
        );
    };

    const render3DShapes = () => {
        return (
            <div className="w-full h-full p-6">
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-full">
                    {/* Left Panel - Controls */}
                    <div className="space-y-6">
                        <div className="bg-white rounded-lg border p-4">
                            <h3 className="text-lg font-semibold mb-4">3D Shape Generator</h3>
                            
                            {/* Shape Selection */}
                            <div className="mb-4">
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Select 3D Shape
                                </label>
                                <div className="grid grid-cols-2 gap-2">
                                    <button
                                        onClick={() => setSelected3DShape('cube')}
                                        className={`p-3 rounded-lg border text-center transition-colors ${
                                            selected3DShape === 'cube'
                                                ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                : 'bg-white border-gray-300 hover:bg-gray-50'
                                        }`}
                                    >
                                        <Box className="w-6 h-6 mx-auto mb-1" />
                                        <div className="text-sm font-medium">Cube</div>
                                    </button>
                                    <button
                                        onClick={() => setSelected3DShape('rectangular_prism')}
                                        className={`p-3 rounded-lg border text-center transition-colors ${
                                            selected3DShape === 'rectangular_prism'
                                                ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                : 'bg-white border-gray-300 hover:bg-gray-50'
                                        }`}
                                    >
                                        <Box className="w-6 h-6 mx-auto mb-1" />
                                        <div className="text-sm font-medium">Rectangular Prism</div>
                                    </button>
                                </div>
                            </div>

                            {/* Dimension Controls */}
                            <div className="space-y-4">
                                {selected3DShape === 'cube' ? (
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-2">
                                            Side Length (cm)
                                        </label>
                                        <input
                                            type="number"
                                            value={shapeDimensions.cube.side_length}
                                            onChange={(e) => setShapeDimensions(prev => ({
                                                ...prev,
                                                cube: { ...prev.cube, side_length: parseFloat(e.target.value) || 1 }
                                            }))}
                                            className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                            min="0.1"
                                            step="0.1"
                                        />
                                    </div>
                                ) : (
                                    <div className="grid grid-cols-3 gap-3">
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Length (cm)
                                            </label>
                                            <input
                                                type="number"
                                                value={shapeDimensions.rectangular_prism.length}
                                                onChange={(e) => setShapeDimensions(prev => ({
                                                    ...prev,
                                                    rectangular_prism: { ...prev.rectangular_prism, length: parseFloat(e.target.value) || 1 }
                                                }))}
                                                className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                min="0.1"
                                                step="0.1"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Breadth (cm)
                                            </label>
                                            <input
                                                type="number"
                                                value={shapeDimensions.rectangular_prism.breadth}
                                                onChange={(e) => setShapeDimensions(prev => ({
                                                    ...prev,
                                                    rectangular_prism: { ...prev.rectangular_prism, breadth: parseFloat(e.target.value) || 1 }
                                                }))}
                                                className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                min="0.1"
                                                step="0.1"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Height (cm)
                                            </label>
                                            <input
                                                type="number"
                                                value={shapeDimensions.rectangular_prism.height}
                                                onChange={(e) => setShapeDimensions(prev => ({
                                                    ...prev,
                                                    rectangular_prism: { ...prev.rectangular_prism, height: parseFloat(e.target.value) || 1 }
                                                }))}
                                                className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                min="0.1"
                                                step="0.1"
                                            />
                                        </div>
                                    </div>
                                )}
                            </div>

                            {/* Generate Button */}
                            <button
                                onClick={() => generate3DDiagram(selected3DShape, shapeDimensions[selected3DShape])}
                                disabled={isGenerating3D}
                                className="w-full mt-4 bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                                {isGenerating3D ? 'Generating...' : 'Generate 3D Diagram'}
                            </button>
                            
                            {/* Educational Features for 3D Shapes */}
                            {threeDCalculations && (
                                <div className="mt-4 border-t border-blue-200 pt-4">
                                    <h6 className="text-sm font-semibold text-blue-800 mb-2">Educational Help</h6>
                                    <div className="flex space-x-2">
                                        <button
                                            onClick={() => generateHints({
                                                question_text: `Calculate the properties of a ${threeDCalculations.shape_type} with the given dimensions`,
                                                question_type: threeDCalculations.shape_type === 'cube' ? 'volume_calculation' : 'surface_area_calculation',
                                                difficulty: threeDCalculations.shape_type === 'cube' ? 'easy' : 'medium'
                                            }, studentPerformance)}
                                            className="px-3 py-1 bg-yellow-500 text-white text-xs rounded hover:bg-yellow-600"
                                        >
                                            Get Hint
                                        </button>
                                        <button
                                            onClick={() => generateSolution({
                                                question_text: `Calculate the properties of a ${threeDCalculations.shape_type} with the given dimensions`,
                                                question_type: threeDCalculations.shape_type === 'cube' ? 'volume_calculation' : 'surface_area_calculation',
                                                difficulty: threeDCalculations.shape_type === 'cube' ? 'easy' : 'medium'
                                            })}
                                            className="px-3 py-1 bg-green-500 text-white text-xs rounded hover:bg-green-600"
                                        >
                                            Show Solution
                                        </button>
                                    </div>
                                </div>
                            )}
                        </div>

                        {/* Calculations Display */}
                        {threeDCalculations && (
                            <div className="bg-green-50 rounded-lg border border-green-200 p-4">
                                <h4 className="text-lg font-semibold text-green-800 mb-3">Calculations & Formulas</h4>
                                
                                {/* Formula Display */}
                                <div className="mb-4 bg-white rounded-lg p-3 border border-green-300">
                                    <h5 className="text-sm font-semibold text-gray-800 mb-2">Formulas:</h5>
                                    {threeDCalculations.shape_type === 'cube' ? (
                                        <div className="space-y-1 text-sm">
                                            <div className="font-mono text-blue-800">SA = 6 × s² = 6 × {threeDCalculations.side_length}²</div>
                                            <div className="font-mono text-green-800">V = s × s × s = {threeDCalculations.side_length} × {threeDCalculations.side_length} × {threeDCalculations.side_length}</div>
                                        </div>
                                    ) : (
                                        <div className="space-y-1 text-sm">
                                            <div className="font-mono text-blue-800">SA = 2(lw + lh + wh) = 2({threeDCalculations.length}×{threeDCalculations.breadth} + {threeDCalculations.length}×{threeDCalculations.height} + {threeDCalculations.breadth}×{threeDCalculations.height})</div>
                                            <div className="font-mono text-green-800">V = l × w × h = {threeDCalculations.length} × {threeDCalculations.breadth} × {threeDCalculations.height}</div>
                                        </div>
                                    )}
                                    <div className="font-mono text-purple-800 text-sm mt-1">Capacity: 1 cm³ = 1 ml</div>
                                </div>

                                {/* Results */}
                                <div className="space-y-2">
                                    <div className="flex justify-between">
                                        <span className="text-green-700">Surface Area:</span>
                                        <span className="font-medium">{threeDCalculations.surface_area} cm²</span>
                                    </div>
                                    <div className="flex justify-between">
                                        <span className="text-green-700">Volume:</span>
                                        <span className="font-medium">{threeDCalculations.volume} cm³</span>
                                    </div>
                                    <div className="flex justify-between">
                                        <span className="text-green-700">Capacity:</span>
                                        <span className="font-medium">{threeDCalculations.capacity} ml</span>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>

                    {/* Right Panel - 3D Diagram */}
                    <div className="bg-white rounded-lg border p-4">
                        <h3 className="text-lg font-semibold mb-4">3D Visualization</h3>
                        <div className="h-96 border-2 border-gray-300 rounded-lg">
                            {threeDDiagram && threeDDiagram !== 'mock_diagram_data' ? (
                                <div 
                                    ref={plotlyRef} 
                                    className="w-full h-full"
                                    style={{ minHeight: '384px' }}
                                />
                            ) : threeDDiagram === 'mock_diagram_data' ? (
                                <div className="h-full flex items-center justify-center">
                                    <div className="text-center">
                                        <div className="text-green-600 mb-2">✅ 3D Diagram Generated (Mock)</div>
                                        <div className="text-sm text-gray-600">
                                            Interactive 3D visualization would be displayed here
                                        </div>
                                    </div>
                                </div>
                            ) : (
                                <div className="h-full flex items-center justify-center text-gray-500">
                                    <div className="text-center">
                                        <Box className="w-12 h-12 mx-auto mb-2" />
                                        <p>Click "Generate 3D Diagram" to create a 3D visualization</p>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    const render3DCalculations = () => {
        return (
            <div className="w-full h-full p-6">
                <div className="max-w-4xl mx-auto">
                    <h3 className="text-2xl font-bold mb-6">3D Geometry Calculations</h3>
                    
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* Cube Calculations */}
                        <div className="bg-white rounded-lg border p-6">
                            <h4 className="text-xl font-semibold mb-4 text-blue-800">Cube</h4>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                        Side Length (cm)
                                    </label>
                                    <input
                                        type="number"
                                        value={shapeDimensions.cube.side_length}
                                        onChange={(e) => setShapeDimensions(prev => ({
                                            ...prev,
                                            cube: { ...prev.cube, side_length: parseFloat(e.target.value) || 1 }
                                        }))}
                                        className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                        min="0.1"
                                        step="0.1"
                                    />
                                </div>
                                <button
                                    onClick={() => calculate3DProperties('cube', shapeDimensions.cube)}
                                    className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
                                >
                                    Calculate Cube Properties
                                </button>
                                
                                {/* Educational Features for Cube */}
                                {threeDCalculations && threeDCalculations.shape_type === 'cube' && (
                                    <div className="mt-4 border-t border-blue-200 pt-4">
                                        <h6 className="text-sm font-semibold text-blue-800 mb-2">Educational Help</h6>
                                        <div className="flex space-x-2">
                                            <button
                                                onClick={() => generateHints({
                                                    question_text: `Calculate the volume and surface area of a cube with side length ${threeDCalculations.side_length} cm`,
                                                    question_type: 'volume_calculation',
                                                    difficulty: 'easy'
                                                }, studentPerformance)}
                                                className="px-3 py-1 bg-yellow-500 text-white text-xs rounded hover:bg-yellow-600"
                                            >
                                                Get Hint
                                            </button>
                                            <button
                                                onClick={() => generateSolution({
                                                    question_text: `Calculate the volume and surface area of a cube with side length ${threeDCalculations.side_length} cm`,
                                                    question_type: 'volume_calculation',
                                                    difficulty: 'easy'
                                                })}
                                                className="px-3 py-1 bg-green-500 text-white text-xs rounded hover:bg-green-600"
                                            >
                                                Show Solution
                                            </button>
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>

                        {/* Rectangular Prism Calculations */}
                        <div className="bg-white rounded-lg border p-6">
                            <h4 className="text-xl font-semibold mb-4 text-green-800">Rectangular Prism</h4>
                            <div className="space-y-4">
                                <div className="grid grid-cols-3 gap-2">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">
                                            Length (cm)
                                        </label>
                                        <input
                                            type="number"
                                            value={shapeDimensions.rectangular_prism.length}
                                            onChange={(e) => setShapeDimensions(prev => ({
                                                ...prev,
                                                rectangular_prism: { ...prev.rectangular_prism, length: parseFloat(e.target.value) || 1 }
                                            }))}
                                            className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500"
                                            min="0.1"
                                            step="0.1"
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">
                                            Breadth (cm)
                                        </label>
                                        <input
                                            type="number"
                                            value={shapeDimensions.rectangular_prism.breadth}
                                            onChange={(e) => setShapeDimensions(prev => ({
                                                ...prev,
                                                rectangular_prism: { ...prev.rectangular_prism, breadth: parseFloat(e.target.value) || 1 }
                                            }))}
                                            className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500"
                                            min="0.1"
                                            step="0.1"
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">
                                            Height (cm)
                                        </label>
                                        <input
                                            type="number"
                                            value={shapeDimensions.rectangular_prism.height}
                                            onChange={(e) => setShapeDimensions(prev => ({
                                                ...prev,
                                                rectangular_prism: { ...prev.rectangular_prism, height: parseFloat(e.target.value) || 1 }
                                            }))}
                                            className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500"
                                            min="0.1"
                                            step="0.1"
                                        />
                                    </div>
                                </div>
                                <button
                                    onClick={() => calculate3DProperties('rectangular_prism', shapeDimensions.rectangular_prism)}
                                    className="w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors"
                                >
                                    Calculate Prism Properties
                                </button>
                                
                                {/* Educational Features for Rectangular Prism */}
                                {threeDCalculations && threeDCalculations.shape_type === 'rectangular_prism' && (
                                    <div className="mt-4 border-t border-green-200 pt-4">
                                        <h6 className="text-sm font-semibold text-green-800 mb-2">Educational Help</h6>
                                        <div className="flex space-x-2">
                                            <button
                                                onClick={() => generateHints({
                                                    question_text: `Calculate the volume and surface area of a rectangular prism with dimensions ${threeDCalculations.length}cm × ${threeDCalculations.breadth}cm × ${threeDCalculations.height}cm`,
                                                    question_type: 'volume_calculation',
                                                    difficulty: 'medium'
                                                }, studentPerformance)}
                                                className="px-3 py-1 bg-yellow-500 text-white text-xs rounded hover:bg-yellow-600"
                                            >
                                                Get Hint
                                            </button>
                                            <button
                                                onClick={() => generateSolution({
                                                    question_text: `Calculate the volume and surface area of a rectangular prism with dimensions ${threeDCalculations.length}cm × ${threeDCalculations.breadth}cm × ${threeDCalculations.height}cm`,
                                                    question_type: 'volume_calculation',
                                                    difficulty: 'medium'
                                                })}
                                                className="px-3 py-1 bg-green-500 text-white text-xs rounded hover:bg-green-600"
                                            >
                                                Show Solution
                                            </button>
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>

                    {/* Results Display */}
                    {threeDCalculations && (
                        <div className="mt-6 bg-gray-50 rounded-lg border p-6">
                            <h4 className="text-xl font-semibold mb-4">Calculation Results & Formulas</h4>
                            
                            {/* Formula Display */}
                            <div className="mb-6 bg-white rounded-lg border p-4">
                                <h5 className="text-lg font-semibold mb-3 text-gray-800">Formulas Used:</h5>
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    {threeDCalculations.shape_type === 'cube' ? (
                                        <>
                                            <div className="bg-blue-50 rounded-lg p-3">
                                                <div className="text-sm font-medium text-blue-800 mb-1">Surface Area</div>
                                                <div className="text-lg font-mono text-blue-900">SA = 6 × s²</div>
                                                <div className="text-sm text-blue-700">= 6 × {threeDCalculations.side_length}²</div>
                                            </div>
                                            <div className="bg-green-50 rounded-lg p-3">
                                                <div className="text-sm font-medium text-green-800 mb-1">Volume</div>
                                                <div className="text-lg font-mono text-green-900">V = s × s × s</div>
                                                <div className="text-sm text-green-700">= {threeDCalculations.side_length} × {threeDCalculations.side_length} × {threeDCalculations.side_length}</div>
                                            </div>
                                        </>
                                    ) : (
                                        <>
                                            <div className="bg-blue-50 rounded-lg p-3">
                                                <div className="text-sm font-medium text-blue-800 mb-1">Surface Area</div>
                                                <div className="text-lg font-mono text-blue-900">SA = 2(lw + lh + wh)</div>
                                                <div className="text-sm text-blue-700">= 2({threeDCalculations.length}×{threeDCalculations.breadth} + {threeDCalculations.length}×{threeDCalculations.height} + {threeDCalculations.breadth}×{threeDCalculations.height})</div>
                                            </div>
                                            <div className="bg-green-50 rounded-lg p-3">
                                                <div className="text-sm font-medium text-green-800 mb-1">Volume</div>
                                                <div className="text-lg font-mono text-green-900">V = l × w × h</div>
                                                <div className="text-sm text-green-700">= {threeDCalculations.length} × {threeDCalculations.breadth} × {threeDCalculations.height}</div>
                                            </div>
                                        </>
                                    )}
                                    <div className="bg-purple-50 rounded-lg p-3">
                                        <div className="text-sm font-medium text-purple-800 mb-1">Capacity</div>
                                        <div className="text-lg font-mono text-purple-900">1 cm³ = 1 ml</div>
                                        <div className="text-sm text-purple-700">= {threeDCalculations.volume} cm³ = {threeDCalculations.capacity} ml</div>
                                    </div>
                                </div>
                            </div>

                            {/* Results Display */}
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                <div className="bg-white rounded-lg p-4 text-center border-2 border-blue-200">
                                    <div className="text-2xl font-bold text-blue-600">{threeDCalculations.surface_area}</div>
                                    <div className="text-sm text-gray-600">Surface Area (cm²)</div>
                                </div>
                                <div className="bg-white rounded-lg p-4 text-center border-2 border-green-200">
                                    <div className="text-2xl font-bold text-green-600">{threeDCalculations.volume}</div>
                                    <div className="text-sm text-gray-600">Volume (cm³)</div>
                                </div>
                                <div className="bg-white rounded-lg p-4 text-center border-2 border-purple-200">
                                    <div className="text-2xl font-bold text-purple-600">{threeDCalculations.capacity}</div>
                                    <div className="text-sm text-gray-600">Capacity (ml)</div>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        );
    };

    const renderNetGeneration = () => {
        return (
            <div className="w-full h-full p-6">
                <div className="max-w-6xl mx-auto">
                    <h3 className="text-2xl font-bold mb-6">3D Net Generation</h3>

                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                        {/* Left Panel - Controls */}
                        <div className="space-y-6">
                            {/* Shape Type Selection */}
                            <div className="bg-white rounded-lg border p-6">
                                <h4 className="text-lg font-semibold mb-4">Select Shape Type</h4>
                                <div className="space-y-3">
                                    <label className="flex items-center space-x-3">
                                        <input
                                            type="radio"
                                            name="netType"
                                            value="cube"
                                            checked={selectedNetType === 'cube'}
                                            onChange={(e) => setSelectedNetType(e.target.value)}
                                            className="w-4 h-4 text-blue-600"
                                        />
                                        <span className="text-sm font-medium">Cube</span>
                                    </label>
                                    <label className="flex items-center space-x-3">
                                        <input
                                            type="radio"
                                            name="netType"
                                            value="rectangular_prism"
                                            checked={selectedNetType === 'rectangular_prism'}
                                            onChange={(e) => setSelectedNetType(e.target.value)}
                                            className="w-4 h-4 text-blue-600"
                                        />
                                        <span className="text-sm font-medium">Rectangular Prism</span>
                                    </label>
                                </div>
                            </div>

                            {/* Dimensions Input */}
                            <div className="bg-white rounded-lg border p-6">
                                <h4 className="text-lg font-semibold mb-4">Set Dimensions (cm)</h4>
                                {selectedNetType === 'cube' ? (
                                    <div className="space-y-4">
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Side Length
                                            </label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                min="0.5"
                                                max="10"
                                                value={netDimensions.cube.side_length}
                                                onChange={(e) => updateNetDimensions('cube', 'side_length', e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                            />
                                        </div>
                                    </div>
                                ) : (
                                    <div className="space-y-4">
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Length
                                            </label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                min="0.5"
                                                max="15"
                                                value={netDimensions.rectangular_prism.length}
                                                onChange={(e) => updateNetDimensions('rectangular_prism', 'length', e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Breadth
                                            </label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                min="0.5"
                                                max="15"
                                                value={netDimensions.rectangular_prism.breadth}
                                                onChange={(e) => updateNetDimensions('rectangular_prism', 'breadth', e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Height
                                            </label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                min="0.5"
                                                max="15"
                                                value={netDimensions.rectangular_prism.height}
                                                onChange={(e) => updateNetDimensions('rectangular_prism', 'height', e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                            />
                                        </div>
                                    </div>
                                )}
                            </div>

                            {/* Generate Button */}
                            <button
                                onClick={generateNet}
                                disabled={isGeneratingNet}
                                className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                                {isGeneratingNet ? 'Generating Net...' : 'Generate Net'}
                            </button>

                            {/* Instructions */}
                            <div className="bg-blue-50 rounded-lg p-4">
                                <h5 className="font-semibold text-blue-800 mb-2">Instructions:</h5>
                                <ul className="text-sm text-blue-700 space-y-1">
                                    <li>• Cut along the outer edges</li>
                                    <li>• Fold along the dashed lines</li>
                                    <li>• Tape or glue the tabs together</li>
                                    <li>• You'll have a 3D shape!</li>
                                </ul>
                            </div>
                        </div>

                        {/* Right Panel - Net Display */}
                        <div className="bg-white rounded-lg border p-6">
                            <h4 className="text-lg font-semibold mb-4">Generated Net</h4>
                            {netImage ? (
                                <div className="text-center">
                                    <img
                                        src={`data:image/png;base64,${netImage}`}
                                        alt={`${selectedNetType} net`}
                                        className="max-w-full h-auto border border-gray-200 rounded-lg"
                                    />
                                    <div className="mt-4">
                                        <button
                                            onClick={() => {
                                                const link = document.createElement('a');
                                                link.href = `data:image/png;base64,${netImage}`;
                                                link.download = `${selectedNetType}_net.png`;
                                                link.click();
                                            }}
                                            className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors"
                                        >
                                            Download Net
                                        </button>
                                    </div>
                                </div>
                            ) : (
                                <div className="text-center text-gray-500 py-12">
                                    <Box className="w-16 h-16 mx-auto mb-4 text-gray-400" />
                                    <p>Click "Generate Net" to create a 2D net</p>
                                    <p className="text-sm mt-2">The net will show how to fold the shape</p>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    const renderInteractive3D = () => {
        if (!shapeTypes) {
            return (
                <div className="w-full h-full flex items-center justify-center">
                    <div className="text-center">
                        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
                        <p>Loading interactive 3D shapes...</p>
                    </div>
                </div>
            );
        }

        const currentShape = shapeTypes[selected3DShape];
        const currentDimensions = interactiveDimensions[selected3DShape];

        return (
            <div className="w-full h-full p-6">
                <div className="max-w-7xl mx-auto">
                    <h3 className="text-2xl font-bold mb-6">Interactive 3D Shapes</h3>
                    <p className="text-gray-600 mb-6">Adjust parameters in real-time and see how they affect the 3D shape and its properties.</p>

                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        {/* Left Panel - Shape Selection & Controls */}
                        <div className="space-y-6">
                            {/* Shape Type Selection */}
                            <div className="bg-white rounded-lg border p-6">
                                <h4 className="text-lg font-semibold mb-4">Select 3D Shape</h4>
                                <div className="space-y-3">
                                    {Object.entries(shapeTypes).map(([key, shape]) => (
                                        <label key={key} className="flex items-center space-x-3 cursor-pointer">
                                            <input
                                                type="radio"
                                                name="3dShape"
                                                value={key}
                                                checked={selected3DShape === key}
                                                onChange={(e) => setSelected3DShape(e.target.value)}
                                                className="w-4 h-4 text-blue-600"
                                            />
                                            <div>
                                                <span className="text-sm font-medium">{shape.name}</span>
                                                <p className="text-xs text-gray-500">{shape.description}</p>
                                            </div>
                                        </label>
                                    ))}
                                </div>
                            </div>

                            {/* Interactive Controls */}
                            <div className="bg-white rounded-lg border p-6">
                                <h4 className="text-lg font-semibold mb-4">Adjust Dimensions</h4>
                                <div className="space-y-4">
                                    {Object.entries(currentShape.parameters).map(([paramKey, param]) => (
                                        <div key={paramKey}>
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                {param.label}
                                            </label>
                                            <div className="flex items-center space-x-3">
                                                <input
                                                    type="range"
                                                    min={param.min}
                                                    max={param.max}
                                                    step={param.step}
                                                    value={currentDimensions[paramKey]}
                                                    onChange={(e) => handleDimensionChange(paramKey, e.target.value)}
                                                    className="flex-1 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                                                />
                                                <input
                                                    type="number"
                                                    min={param.min}
                                                    max={param.max}
                                                    step={param.step}
                                                    value={currentDimensions[paramKey]}
                                                    onChange={(e) => handleDimensionChange(paramKey, e.target.value)}
                                                    className="w-20 px-2 py-1 text-sm border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                />
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            {/* Real-time Properties */}
                            {interactiveProperties && (
                                <div className="bg-white rounded-lg border p-6">
                                    <h4 className="text-lg font-semibold mb-4">Calculated Properties</h4>
                                    <div className="space-y-3">
                                        {Object.entries(interactiveProperties.properties).map(([key, value]) => (
                                            <div key={key} className="flex justify-between items-center">
                                                <span className="text-sm font-medium text-gray-700 capitalize">
                                                    {key.replace('_', ' ')}:
                                                </span>
                                                <span className="text-sm font-bold text-blue-600">
                                                    {typeof value === 'number' ? value.toFixed(2) : value} cm{key.includes('area') ? '²' : key.includes('volume') ? '³' : ''}
                                                </span>
                                            </div>
                                        ))}
                                    </div>
                                    
                                    {/* Formulas */}
                                    <div className="mt-4 pt-4 border-t">
                                        <h5 className="text-sm font-semibold text-gray-700 mb-2">Formulas Used:</h5>
                                        <div className="space-y-1">
                                            {Object.entries(interactiveProperties.formulas).map(([key, formula]) => (
                                                <div key={key} className="text-xs text-gray-600">
                                                    <span className="font-medium">{key.replace('_', ' ')}:</span> {formula}
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>

                        {/* Center Panel - 3D Visualization */}
                        <div className="bg-white rounded-lg border p-6">
                            <h4 className="text-lg font-semibold mb-4">3D Visualization</h4>
                            <div className="h-96 flex items-center justify-center">
                                {interactiveDiagram ? (
                                    <div className="w-full h-full">
                                        <div
                                            ref={plotlyRef}
                                            className="w-full h-full"
                                            style={{ minHeight: '300px' }}
                                        />
                                    </div>
                                ) : (
                                    <div className="text-center text-gray-500">
                                        <Box className="w-16 h-16 mx-auto mb-4 text-gray-400" />
                                        <p>Adjust dimensions to see the 3D shape</p>
                                        <p className="text-sm mt-2">The visualization will update in real-time</p>
                                    </div>
                                )}
                            </div>
                        </div>

                        {/* Right Panel - Educational Information */}
                        <div className="space-y-6">
                            <div className="bg-blue-50 rounded-lg p-6">
                                <h4 className="text-lg font-semibold text-blue-800 mb-3">Learning Tips</h4>
                                <ul className="text-sm text-blue-700 space-y-2">
                                    <li>• Drag the sliders to see how dimensions affect volume and surface area</li>
                                    <li>• Notice the relationship between dimensions and 3D properties</li>
                                    <li>• Try different combinations to understand geometric principles</li>
                                    <li>• The formulas show the mathematical relationships</li>
                                </ul>
                            </div>

                            <div className="bg-green-50 rounded-lg p-6">
                                <h4 className="text-lg font-semibold text-green-800 mb-3">Real-world Applications</h4>
                                <ul className="text-sm text-green-700 space-y-2">
                                    <li>• <strong>Cubes:</strong> Dice, sugar cubes, storage boxes</li>
                                    <li>• <strong>Rectangular Prisms:</strong> Books, buildings, containers</li>
                                    <li>• <strong>Cylinders:</strong> Cans, pipes, towers</li>
                                    <li>• <strong>Spheres:</strong> Balls, planets, bubbles</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    const renderSouthAfrican3D = () => {
        return (
            <div className="w-full h-full p-6">
                <div className="max-w-7xl mx-auto">
                    <h3 className="text-2xl font-bold mb-6">South African 3D Problems</h3>
                    <p className="text-gray-600 mb-6">Explore 3D geometry through culturally relevant problems from South Africa.</p>

                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        {/* Left Panel - Problem Selection */}
                        <div className="space-y-6">
                            {/* Category and Difficulty Selection */}
                            <div className="bg-white rounded-lg border p-6">
                                <h4 className="text-lg font-semibold mb-4">Filter Problems</h4>
                                
                                {/* Category Selection */}
                                <div className="mb-4">
                                    <label className="block text-sm font-medium text-gray-700 mb-2">Category</label>
                                    <select
                                        value={selectedSa3dCategory}
                                        onChange={(e) => setSelectedSa3dCategory(e.target.value)}
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    >
                                        <option value="all">All Categories</option>
                                        {sa3dCategories.map((category) => (
                                            <option key={category.value} value={category.value}>
                                                {category.label}
                                            </option>
                                        ))}
                                    </select>
                                </div>

                                {/* Difficulty Selection */}
                                <div className="mb-4">
                                    <label className="block text-sm font-medium text-gray-700 mb-2">Difficulty</label>
                                    <select
                                        value={selectedSa3dDifficulty}
                                        onChange={(e) => setSelectedSa3dDifficulty(e.target.value)}
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    >
                                        <option value="all">All Difficulties</option>
                                        <option value="easy">Easy</option>
                                        <option value="medium">Medium</option>
                                        <option value="hard">Hard</option>
                                    </select>
                                </div>

                                {/* Load New Problem Button */}
                                <button
                                    onClick={loadSa3dProblem}
                                    disabled={isLoadingSa3dProblem}
                                    className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                                    aria-label="Load a new South African 3D geometry problem"
                                    aria-describedby="load-problem-description"
                                >
                                    {isLoadingSa3dProblem ? 'Loading...' : 'Load New Problem'}
                                </button>
                                <div id="load-problem-description" className="sr-only">
                                    Click to load a new 3D geometry problem based on your selected category and difficulty filters
                                </div>
                            </div>

                            {/* Problem Information */}
                            {currentSa3dProblem && (
                                <div className="bg-white rounded-lg border p-6">
                                    <h4 className="text-lg font-semibold mb-4">Problem Details</h4>
                                    <div className="space-y-3">
                                        <div>
                                            <span className="text-sm font-medium text-gray-700">Category:</span>
                                            <span className="ml-2 text-sm text-blue-600 capitalize">
                                                {currentSa3dProblem.category.replace('_', ' ')}
                                            </span>
                                        </div>
                                        <div>
                                            <span className="text-sm font-medium text-gray-700">Difficulty:</span>
                                            <span className={`ml-2 text-sm font-medium ${
                                                currentSa3dProblem.difficulty === 'easy' ? 'text-green-600' :
                                                currentSa3dProblem.difficulty === 'medium' ? 'text-yellow-600' :
                                                'text-red-600'
                                            }`}>
                                                {currentSa3dProblem.difficulty.charAt(0).toUpperCase() + currentSa3dProblem.difficulty.slice(1)}
                                            </span>
                                        </div>
                                        <div>
                                            <span className="text-sm font-medium text-gray-700">Shape Type:</span>
                                            <span className="ml-2 text-sm text-blue-600 capitalize">
                                                {currentSa3dProblem.shape_type.replace('_', ' ')}
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>

                        {/* Center Panel - Problem Display */}
                        <div className="lg:col-span-2">
                            {currentSa3dProblem ? (
                                <div className="bg-white rounded-lg border p-6">
                                    <h4 className="text-xl font-semibold mb-4">{currentSa3dProblem.title}</h4>
                                    
                                    {/* Problem Description */}
                                    <div className="mb-6">
                                        <p className="text-gray-700 mb-4">{currentSa3dProblem.description}</p>
                                        
                                        {/* Cultural Context */}
                                        <div className="bg-blue-50 border-l-4 border-blue-400 p-4 mb-4">
                                            <h5 className="font-medium text-blue-800 mb-2">Cultural Context</h5>
                                            <p className="text-blue-700 text-sm">{currentSa3dProblem.cultural_context}</p>
                                        </div>

                                        {/* Given Values */}
                                        <div className="mb-4">
                                            <h5 className="font-medium text-gray-800 mb-2">Given Values:</h5>
                                            <div className="grid grid-cols-2 gap-2">
                                                {Object.entries(currentSa3dProblem.given_values).map(([key, value]) => (
                                                    <div key={key} className="flex justify-between">
                                                        <span className="text-sm text-gray-600 capitalize">
                                                            {key.replace('_', ' ')}:
                                                        </span>
                                                        <span className="text-sm font-medium">
                                                            {value} {key.includes('length') || key.includes('breadth') || key.includes('height') || key.includes('radius') ? 'm' : ''}
                                                        </span>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>

                                        {/* Question */}
                                        <div className="mb-6">
                                            <h5 className="font-medium text-gray-800 mb-2">Question:</h5>
                                            <p className="text-lg text-gray-700">{currentSa3dProblem.question}</p>
                                        </div>

                                        {/* Solution Toggle */}
                                        <div className="mb-4">
                                            <button
                                                onClick={() => setShowSa3dSolution(!showSa3dSolution)}
                                                className="bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
                                                aria-label={showSa3dSolution ? 'Hide the step-by-step solution' : 'Show the step-by-step solution'}
                                                aria-expanded={showSa3dSolution}
                                            >
                                                {showSa3dSolution ? 'Hide Solution' : 'Show Solution'}
                                            </button>
                                        </div>

                                        {/* Solution Steps */}
                                        {showSa3dSolution && (
                                            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                                                <h5 className="font-medium text-green-800 mb-3">Step-by-Step Solution:</h5>
                                                <ol className="space-y-2">
                                                    {currentSa3dProblem.solution_steps.map((step, index) => (
                                                        <li key={index} className="text-sm text-green-700">
                                                            {step}
                                                        </li>
                                                    ))}
                                                </ol>
                                                <div className="mt-4 pt-3 border-t border-green-200">
                                                    <div className="flex justify-between items-center">
                                                        <span className="font-medium text-green-800">Answer:</span>
                                                        <span className="text-lg font-bold text-green-600">
                                                            {currentSa3dProblem.answer} {currentSa3dProblem.units}
                                                        </span>
                                                    </div>
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                </div>
                            ) : (
                                <div className="bg-white rounded-lg border p-6 text-center">
                                    <div className="text-gray-500">
                                        <div className="text-4xl mb-4">🇿🇦</div>
                                        <h4 className="text-lg font-medium mb-2">No Problem Loaded</h4>
                                        <p>Select filters and click "Load New Problem" to start exploring South African 3D geometry problems.</p>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    const render3DQuiz = () => {
        const quizTypes = [
            { id: 'volume', name: 'Volume Calculations', description: 'Calculate volume of cubes and rectangular prisms' },
            { id: 'surface_area', name: 'Surface Area', description: 'Calculate surface area of 3D shapes' },
            { id: 'capacity', name: 'Capacity', description: 'Convert between volume and capacity units' },
            { id: 'shape_recognition', name: '3D Shape Recognition', description: 'Identify 3D shapes from descriptions' }
        ];

        return (
            <div className="w-full h-full p-6">
                <div className="max-w-4xl mx-auto">
                    <h3 className="text-2xl font-bold mb-6">3D Geometry Quiz</h3>
                    
                    {/* Quiz Type Selection */}
                    <div className="bg-white rounded-lg border p-6 mb-6">
                        <h4 className="text-lg font-semibold mb-4">Select Quiz Type</h4>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                            {quizTypes.map((type) => (
                                <button
                                    key={type.id}
                                    onClick={() => setSelectedQuizType(type.id)}
                                    className={`p-4 rounded-lg border text-left transition-colors ${
                                        selectedQuizType === type.id
                                            ? 'bg-blue-100 border-blue-500 text-blue-800'
                                            : 'bg-gray-50 border-gray-200 hover:bg-gray-100 text-gray-700'
                                    }`}
                                >
                                    <div className="font-medium">{type.name}</div>
                                    <div className="text-sm text-gray-600 mt-1">{type.description}</div>
                                </button>
                            ))}
                        </div>

                        {/* Difficulty Selection */}
                        <div className="mb-4">
                            <label className="block text-sm font-medium text-gray-700 mb-2">Difficulty Level:</label>
                            <div className="flex space-x-4">
                                {['easy', 'medium', 'hard'].map((diff) => (
                                    <button
                                        key={diff}
                                        onClick={() => setSelectedDifficulty(diff)}
                                        className={`px-4 py-2 rounded-lg border transition-colors ${
                                            selectedDifficulty === diff
                                                ? 'bg-green-100 border-green-500 text-green-800'
                                                : 'bg-gray-50 border-gray-200 hover:bg-gray-100 text-gray-700'
                                        }`}
                                    >
                                        {diff.charAt(0).toUpperCase() + diff.slice(1)}
                                    </button>
                                ))}
                            </div>
                        </div>

                        {/* Generate Quiz Button */}
                        <button
                            onClick={() => generate3DQuiz(selectedQuizType, selectedDifficulty)}
                            disabled={isGenerating3DQuiz}
                            className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                        >
                            {isGenerating3DQuiz ? 'Generating Quiz...' : 'Generate 3D Quiz Question'}
                        </button>
                    </div>

                    {/* Quiz Question Display */}
                    {quizQuestion && (
                        <div className="bg-white rounded-lg border p-6 mb-6">
                            <h4 className="text-lg font-semibold mb-4">Question</h4>
                            <p className="text-gray-800 mb-4">{quizQuestion.question_text}</p>
                            
                            <div className="space-y-2 mb-4">
                                {quizQuestion.options.map((option, index) => (
                                    <button
                                        key={index}
                                        onClick={() => setUserAnswer(option)}
                                        className={`w-full p-3 text-left rounded-lg border transition-colors ${
                                            userAnswer === option
                                                ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                : 'bg-gray-50 border-gray-200 hover:bg-gray-100 text-gray-700'
                                        }`}
                                    >
                                        {String.fromCharCode(65 + index)}. {option}
                                    </button>
                                ))}
                            </div>

                            <div className="flex space-x-4">
                                <button
                                    onClick={() => {
                                        if (userAnswer) {
                                            const isCorrect = userAnswer === quizQuestion.correct_answer;
                                            setQuizResult({
                                                correct: isCorrect,
                                                userAnswer: userAnswer,
                                                correctAnswer: quizQuestion.correct_answer,
                                                explanation: quizQuestion.explanation
                                            });
                                        }
                                    }}
                                    disabled={!userAnswer}
                                    className="bg-green-600 text-white py-2 px-6 rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                                >
                                    Check Answer
                                </button>

                                <button
                                    onClick={() => generateHints(quizQuestion, studentPerformance)}
                                    className="bg-yellow-500 text-white py-2 px-6 rounded-lg hover:bg-yellow-600 transition-colors"
                                >
                                    Get Hint
                                </button>

                                <button
                                    onClick={() => generateSolution(quizQuestion)}
                                    className="bg-purple-600 text-white py-2 px-6 rounded-lg hover:bg-purple-700 transition-colors"
                                >
                                    Show Solution
                                </button>
                            </div>
                        </div>
                    )}

                    {/* Quiz Result */}
                    {quizResult && (
                        <div className={`rounded-lg border p-6 mb-6 ${
                            quizResult.correct 
                                ? 'bg-green-50 border-green-200' 
                                : 'bg-red-50 border-red-200'
                        }`}>
                            <h4 className={`text-lg font-semibold mb-2 ${
                                quizResult.correct ? 'text-green-800' : 'text-red-800'
                            }`}>
                                {quizResult.correct ? '✅ Correct!' : '❌ Incorrect'}
                            </h4>
                            <p className="text-gray-700 mb-2">Your answer: {quizResult.userAnswer}</p>
                            <p className="text-gray-700 mb-2">Correct answer: {quizResult.correctAnswer}</p>
                            {quizResult.explanation && (
                                <p className="text-gray-600">{quizResult.explanation}</p>
                            )}
                        </div>
                    )}

                    {/* Educational Features Display */}
                    {showHints && hints.length > 0 && (
                        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6 mb-6">
                            <h4 className="text-lg font-semibold text-yellow-800 mb-3">💡 Hints</h4>
                            <div className="space-y-2">
                                {hints.map((hint, index) => (
                                    <div key={index} className="text-yellow-700">
                                        <strong>{hint.hint_type}:</strong> {hint.hint_text}
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {solutionSteps.length > 0 && (
                        <div className="bg-purple-50 border border-purple-200 rounded-lg p-6 mb-6">
                            <h4 className="text-lg font-semibold text-purple-800 mb-3">📝 Step-by-Step Solution</h4>
                            <div className="space-y-3">
                                {solutionSteps.map((step, index) => (
                                    <div key={index} className="text-purple-700">
                                        <strong>Step {index + 1}:</strong> {step.step_text}
                                        {step.common_mistakes && (
                                            <div className="text-sm text-purple-600 mt-1 ml-4">
                                                <strong>Common mistakes:</strong> {step.common_mistakes}
                                            </div>
                                        )}
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {educationalFeedback && (
                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
                            <h4 className="text-lg font-semibold text-blue-800 mb-3">📚 Educational Feedback</h4>
                            <p className="text-blue-700 mb-2">{educationalFeedback.message}</p>
                            {educationalFeedback.next_steps && (
                                <p className="text-blue-600 text-sm">{educationalFeedback.next_steps}</p>
                            )}
                        </div>
                    )}
                </div>
            </div>
        );
    };

    // Render the appropriate module based on mode and tool
    const renderModule = () => {
        const { mode, selectedTool, selectedConcept, selectedSubConcept } = geometryData;
        console.log('renderModule - Current mode:', mode, 'selectedTool:', selectedTool);

        switch (mode) {
            case '2d':
                switch (selectedTool) {
                    case 'basics_of_geometry':
                        // Show sub-buttons and content based on selected sub-concept
                        return renderBasicsOfGeometry();
                    case 'properties_of_2d_shapes':
                        return renderPropertiesOf2DShapes();
                    case 'calculations_2d_shapes':
                        return renderCalculations2DShapes();
                    default:
                        return (
                            <div className="w-full h-full flex items-center justify-center bg-gray-50 border-2 border-dashed border-gray-300 rounded">
                                <div className="text-center text-gray-500">
                                    <Shapes className="w-12 h-12 mx-auto mb-2" />
                                    <p className="text-lg font-medium">Select a 2D Tool</p>
                                    <p className="text-sm">Choose a tool from the left panel</p>
                                </div>
                            </div>
                        );
                }
        case '3d':
            switch (selectedTool) {
                case 'basics_of_3d_geometry':
                    return render3DBasics();
                case 'net_generation':
                    return renderNetGeneration();
                case 'interactive_3d':
                    return renderInteractive3D();
            case 'south_african_3d':
                return renderSouthAfrican3D();
            case 'interactive_controls':
                return renderInteractiveControls();
            case 'construction_guide':
                return renderConstructionGuide();
                case 'properties_of_3d_shapes':
                    return render3DShapes();
                case 'calculations_3d_shapes':
                    return render3DCalculations();
                case '3d_quiz':
                    return render3DQuiz();
                default:
                    return (
                        <div className="w-full h-full flex items-center justify-center bg-gray-50 border-2 border-dashed border-gray-300 rounded">
                            <div className="text-center text-gray-500">
                                <Box className="w-12 h-12 mx-auto mb-2" />
                                <p className="text-lg font-medium">3D Geometry</p>
                                <p className="text-sm">Choose a tool from the left panel</p>
                            </div>
                        </div>
                    );
            }
            case 'advanced':
                return (
                    <div className="w-full h-full flex items-center justify-center bg-gray-50 border-2 border-dashed border-gray-300 rounded">
                        <div className="text-center text-gray-500">
                            <Zap className="w-12 h-12 mx-auto mb-2" />
                            <p className="text-lg font-medium">Advanced Geometry</p>
                            <p className="text-sm">Coming soon...</p>
                        </div>
                    </div>
                );
            default:
                return (
                    <div className="w-full h-full flex items-center justify-center bg-gray-50 border-2 border-dashed border-gray-300 rounded">
                        <div className="text-center text-gray-500">
                            <Shapes className="w-12 h-12 mx-auto mb-2" />
                            <p className="text-lg font-medium">Select a Mode</p>
                            <p className="text-sm">Choose a mode from the left panel</p>
                        </div>
                    </div>
                );
        }
    };

    // Render Basics of Geometry with sub-buttons and content
    const renderBasicsOfGeometry = () => {
        return (
            <div className="w-full h-full flex flex-col bg-gray-50">
                {/* Sub-buttons for Basics of Geometry */}
                <div className="bg-white border-b border-gray-200 p-4">
                    <div className="flex justify-center gap-2">
                        {[
                            { id: 'points_and_lines', name: 'Points and Lines' },
                            { id: 'angles', name: 'Angles' },
                            { id: 'circles', name: 'Circles' },
                            { id: 'triangles', name: 'Triangles' },
                            { id: 'quadrilaterals', name: 'Quadrilaterals' },
                            { id: 'ai_assistant', name: '🤖 AI Assistant' }
                        ].map((button) => (
                            <button
                                key={button.id}
                                onClick={() => handleFieldChange('selectedSubConcept', button.id)}
                                className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                                    geometryData.selectedSubConcept === button.id
                                        ? 'bg-blue-600 text-white border-2 border-blue-700'
                                        : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
                                }`}
                            >
                                {button.name}
                            </button>
                        ))}
                </div>
                </div>
                
                {/* Backend Integration Toggle */}
                <div className="bg-white border-b border-gray-200 p-3">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center space-x-2">
                            <span className="text-sm font-medium text-gray-700">Rendering Mode:</span>
                            <div className="flex items-center space-x-2">
                                <button
                                    onClick={() => handleFieldChange('usePythonBackend', true)}
                                    className={`px-3 py-1 text-xs rounded ${
                                        geometryData.usePythonBackend
                                            ? 'bg-green-600 text-white'
                                            : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                    }`}
                                >
                                    🐍 Python Backend
                                </button>
                                <button
                                    onClick={() => handleFieldChange('usePythonBackend', false)}
                                    className={`px-3 py-1 text-xs rounded ${
                                        !geometryData.usePythonBackend
                                            ? 'bg-blue-600 text-white'
                                            : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                    }`}
                                >
                                    🎨 Canvas Fallback
                                </button>
                            </div>
                        </div>
                        <div className="text-xs text-gray-500">
                            {geometryData.usePythonBackend 
                                ? 'Using Python libraries for mathematical accuracy' 
                                : 'Using Canvas rendering for offline mode'
                            }
                        </div>
                    </div>
                </div>

                {/* Content based on selected sub-concept */}
                <div className="flex-1 overflow-y-auto">
                    {geometryData.selectedSubConcept === 'points_and_lines' && (
                        geometryData.usePythonBackend ? (
                            <PythonBasicShapes
                                geometryData={geometryData}
                                onChange={handleFieldChange}
                                isSubmitted={isSubmitted}
                                selectedSubConcept={geometryData.selectedSubConcept}
                            />
                        ) : (
                            <div className="p-4 space-y-4">
                                {/* Visual Examples with Definitions */}
                                <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
                                    <h5 className="text-xs font-semibold text-gray-800 mb-3">Basic Geometric Elements</h5>
                                    <div className="space-y-4">
                            {/* Point */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Point</div>
                                        <div className="text-xs text-gray-500">A location in space (•)</div>
                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="60" height="50" viewBox="0 0 60 50">
                                            <circle cx="30" cy="20" r="4" fill="#ef4444" />
                                            <text x="30" y="40" textAnchor="middle" fontSize="12" fill="#374151">P</text>
                                        </svg>
                </div>
            </div>
                                <p className="text-sm text-gray-600 mb-2">A location in space with no size, length, or width. Represented by a dot (•).</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: Intersection of two lines</div>
                            </div>
                            
                            {/* Line */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Line</div>
                                        <div className="text-xs text-gray-500">Extends infinitely in both directions (AB)</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="80" height="40" viewBox="0 0 80 40">
                                            <defs>
                                                <marker id="arrowhead-blue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                                                    <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6" />
                                                </marker>
                                            </defs>
                                            <line x1="10" y1="20" x2="70" y2="20" stroke="#3b82f6" strokeWidth="2" markerEnd="url(#arrowhead-blue)" markerStart="url(#arrowhead-blue)" />
                                            <text x="40" y="35" textAnchor="middle" fontSize="12" fill="#374151">AB</text>
                                        </svg>
                        </div>
                    </div>
                                <p className="text-sm text-gray-600 mb-2">A straight path that extends infinitely in both directions. Has no endpoints.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: AB or line AB</div>
                            </div>
                            
                            {/* Ray */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Ray</div>
                                        <div className="text-xs text-gray-500">One endpoint, extends infinitely (AB)</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="80" height="40" viewBox="0 0 80 40">
                                            <defs>
                                                <marker id="arrowhead-green" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                                                    <polygon points="0 0, 10 3.5, 0 7" fill="#10b981" />
                                                </marker>
                                            </defs>
                                            <circle cx="15" cy="20" r="3" fill="#10b981" />
                                            <line x1="15" y1="20" x2="70" y2="20" stroke="#10b981" strokeWidth="2" markerEnd="url(#arrowhead-green)" />
                                            <text x="15" y="35" textAnchor="middle" fontSize="10" fill="#374151">A</text>
                                            <text x="40" y="35" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                        </svg>
                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">A part of a line that has one endpoint and extends infinitely in one direction.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: AB (starts at A, goes through B)</div>
                            </div>
                            
                            {/* Line Segment */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Line Segment</div>
                                        <div className="text-xs text-gray-500">Two endpoints, definite length (AB)</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="80" height="40" viewBox="0 0 80 40">
                                            <circle cx="15" cy="20" r="3" fill="#8b5cf6" />
                                            <line x1="15" y1="20" x2="65" y2="20" stroke="#8b5cf6" strokeWidth="2" />
                                            <circle cx="65" cy="20" r="3" fill="#8b5cf6" />
                                            <text x="15" y="35" textAnchor="middle" fontSize="10" fill="#374151">A</text>
                                            <text x="65" y="35" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                        </svg>
                        </div>
                    </div>
                                <p className="text-sm text-gray-600 mb-2">A part of a line with two endpoints. Has a definite length.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: AB or segment AB</div>
                            </div>
                            
                            {/* Parallel Lines */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Parallel Lines</div>
                                        <div className="text-xs text-gray-500">Never intersect, same distance apart (AB ∥ CD)</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="80" height="40" viewBox="0 0 80 40">
                                            <line x1="10" y1="12" x2="70" y2="12" stroke="#f97316" strokeWidth="2" />
                                            <line x1="10" y1="28" x2="70" y2="28" stroke="#f97316" strokeWidth="2" />
                                            <text x="40" y="35" textAnchor="middle" fontSize="10" fill="#374151">AB ∥ CD</text>
                                        </svg>
                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">Two lines in the same plane that never intersect. They are always the same distance apart.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: AB ∥ CD</div>
                            </div>
                            
                            {/* Perpendicular Lines */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Perpendicular Lines</div>
                                        <div className="text-xs text-gray-500">Intersect at 90° angle (AB ⊥ CD)</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="80" height="50" viewBox="0 0 80 50">
                                            <line x1="10" y1="25" x2="70" y2="25" stroke="#ef4444" strokeWidth="2" />
                                            <line x1="40" y1="8" x2="40" y2="42" stroke="#ef4444" strokeWidth="2" />
                                            <rect x="37" y="22" width="6" height="6" fill="none" stroke="#ef4444" strokeWidth="1" />
                                            <text x="40" y="45" textAnchor="middle" fontSize="10" fill="#374151">AB ⊥ CD</text>
                                        </svg>
                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">Two lines that intersect at a right angle (90°).</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: AB ⊥ CD</div>
                            </div>


                        </div>
                    </div>
                    
                            {/* Interactive Instructions */}
                            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                                <h5 className="text-xs font-semibold text-green-800 mb-2">Interactive Drawing</h5>
                                <div className="text-green-700 text-xs space-y-1">
                                    <div>• Click anywhere on the canvas to add points</div>
                                    <div>• Drag to create lines and line segments</div>
                                    <div>• Use the tool buttons to switch between different drawing modes</div>
                                    <div>• Each element gets an automatic label for identification</div>
                                </div>
                            </div>
                        </div>
                        )
                    )}

                    {geometryData.selectedSubConcept === 'ai_assistant' && (
                        <div className="h-full">
                            <AIGeometryAssistant />
                        </div>
                    )}

                    {geometryData.selectedSubConcept === 'angles' && (
                        geometryData.usePythonBackend ? (
                            <PythonBasicShapes
                                geometryData={geometryData}
                                onChange={handleFieldChange}
                                isSubmitted={isSubmitted}
                                selectedSubConcept={geometryData.selectedSubConcept}
                            />
                        ) : (
                            <div className="space-y-4">
                            {/* Arms of an Angle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Arms of an Angle</div>
                                        <div className="text-xs text-gray-500">The two rays that form the angle</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <line x1="35" y1="30" x2="60" y2="30" stroke="#3b82f6" strokeWidth="2" />
                                            <line x1="35" y1="30" x2="35" y2="10" stroke="#3b82f6" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="3" fill="#3b82f6" />
                                            <path d="M 35 30 L 40 30 A 8 8 0 0 0 35 22 Z" fill="none" stroke="#3b82f6" strokeWidth="1" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="60" y="35" fontSize="10" fill="#374151">A</text>
                                            <text x="35" y="8" textAnchor="middle" fontSize="10" fill="#374151">C</text>
                                        </svg>
                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">The two rays that meet at a common endpoint (vertex) to form an angle.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: In ∠ABC, BA and BC are the arms</div>
                            </div>

                            {/* Acute Angle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Acute Angle</div>
                                        <div className="text-xs text-gray-500">Less than 90° (0° &lt; θ &lt; 90°)</div>
                        </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <line x1="35" y1="30" x2="60" y2="30" stroke="#10b981" strokeWidth="2" />
                                            <line x1="35" y1="30" x2="55" y2="15" stroke="#10b981" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="3" fill="#10b981" />
                                            <path d="M 35 30 L 40 30 A 10 10 0 0 1 38 20 Z" fill="none" stroke="#10b981" strokeWidth="1" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="60" y="35" fontSize="10" fill="#374151">A</text>
                                            <text x="55" y="12" fontSize="10" fill="#374151">C</text>
                                        </svg>
                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">An angle that measures less than 90 degrees.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: 30°, 45°, 60°</div>
                            </div>

                            {/* Right Angle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Right Angle</div>
                                        <div className="text-xs text-gray-500">Exactly 90° (θ = 90°)</div>
                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <line x1="35" y1="30" x2="60" y2="30" stroke="#ef4444" strokeWidth="2" />
                                            <line x1="35" y1="30" x2="35" y2="10" stroke="#ef4444" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="3" fill="#ef4444" />
                                            <rect x="35" y="25" width="6" height="6" fill="none" stroke="#ef4444" strokeWidth="1" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="60" y="35" fontSize="10" fill="#374151">A</text>
                                            <text x="35" y="8" textAnchor="middle" fontSize="10" fill="#374151">C</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">An angle that measures exactly 90 degrees.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: Marked with a small square</div>
                            </div>

                                                        {/* Obtuse Angle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Obtuse Angle</div>
                                        <div className="text-xs text-gray-500">Between 90° and 180° (90° &lt; θ &lt; 180°)</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <line x1="35" y1="30" x2="60" y2="30" stroke="#f97316" strokeWidth="2" />
                                            <line x1="35" y1="30" x2="20" y2="10" stroke="#f97316" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="3" fill="#f97316" />
                                            <path d="M 35 30 L 40 30 A 15 15 0 0 1 25 15 Z" fill="none" stroke="#f97316" strokeWidth="1" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="60" y="35" fontSize="10" fill="#374151">A</text>
                                            <text x="20" y="8" fontSize="10" fill="#374151">C</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">An angle that measures more than 90 degrees but less than 180 degrees.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: 120°, 150°</div>
                            </div>
                        
                                                        {/* Straight Angle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Straight Angle</div>
                                        <div className="text-xs text-gray-500">Exactly 180° (θ = 180°)</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="80" height="40" viewBox="0 0 80 40">
                                            <line x1="10" y1="20" x2="70" y2="20" stroke="#8b5cf6" strokeWidth="2" />
                                            <circle cx="40" cy="20" r="3" fill="#8b5cf6" />
                                            <path d="M 40 20 L 45 20 A 8 8 0 0 1 45 20 Z" fill="none" stroke="#8b5cf6" strokeWidth="1" />
                                            <text x="40" y="35" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="10" y="30" fontSize="10" fill="#374151">A</text>
                                            <text x="70" y="30" fontSize="10" fill="#374151">C</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">An angle that measures exactly 180 degrees. Forms a straight line.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: A straight line</div>
                            </div>

                                                        {/* Reflex Angle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Reflex Angle</div>
                                        <div className="text-xs text-gray-500">Between 180° and 360° (180° &lt; θ &lt; 360°)</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <line x1="35" y1="30" x2="60" y2="30" stroke="#6366f1" strokeWidth="2" />
                                            <line x1="35" y1="30" x2="35" y2="10" stroke="#6366f1" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="3" fill="#6366f1" />
                                            <path d="M 35 30 L 40 30 A 18 18 0 1 1 25 15 Z" fill="none" stroke="#6366f1" strokeWidth="1" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="60" y="35" fontSize="10" fill="#374151">A</text>
                                            <text x="35" y="8" textAnchor="middle" fontSize="10" fill="#374151">C</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">An angle that measures more than 180 degrees but less than 360 degrees.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: 270°</div>
                            </div>

                            {/* Revolution */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Revolution</div>
                                        <div className="text-xs text-gray-500">Exactly 360° (θ = 360°)</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <line x1="35" y1="30" x2="55" y2="30" stroke="#ec4899" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="3" fill="#ec4899" />
                                            <circle cx="35" cy="30" r="18" fill="none" stroke="#ec4899" strokeWidth="1" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="10" fill="#374151">B</text>
                                            <text x="55" y="35" fontSize="10" fill="#374151">A</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">A complete turn around a point. Measures exactly 360 degrees.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: Full circle rotation</div>
                            </div>
                            </div>
                        )
                    )}

                    {geometryData.selectedSubConcept === 'circles' && (
                        <div className="space-y-4">
                            {/* Python Backend Toggle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-4">
                                    <h5 className="text-sm font-semibold text-gray-800">Circles</h5>
                                    <div className="flex items-center space-x-3">
                                        <span className="text-xs text-gray-500">Rendering:</span>
                                        <button
                                            onClick={() => setGeometryData(prev => ({ ...prev, usePythonBackend: true }))}
                                            className={`px-3 py-1 text-xs rounded-full transition-colors ${
                                                geometryData.usePythonBackend 
                                                    ? 'bg-green-100 text-green-800 border border-green-300' 
                                                    : 'bg-gray-100 text-gray-600 border border-gray-300'
                                            }`}
                                        >
                                            🐍 Python Backend
                                        </button>
                                        <button
                                            onClick={() => setGeometryData(prev => ({ ...prev, usePythonBackend: false }))}
                                            className={`px-3 py-1 text-xs rounded-full transition-colors ${
                                                !geometryData.usePythonBackend 
                                                    ? 'bg-blue-100 text-blue-800 border border-blue-300' 
                                                    : 'bg-gray-100 text-gray-600 border border-gray-300'
                                            }`}
                                        >
                                            🎨 Canvas Fallback
                                        </button>
                                    </div>
                                </div>
                                
                                {geometryData.usePythonBackend ? (
                                    <PythonBasicShapes
                                        selectedSubConcept="circles"
                                        onChange={onChange}
                                    />
                                ) : (
                                    <div className="space-y-4">
                                                        {/* Chord */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Chord</div>
                                        <div className="text-xs text-gray-500">Line segment connecting two points on circle</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <circle cx="35" cy="30" r="20" fill="none" stroke="#3b82f6" strokeWidth="2" />
                                            <line x1="20" y1="20" x2="50" y2="40" stroke="#ef4444" strokeWidth="2" />
                                            <circle cx="20" cy="20" r="2" fill="#ef4444" />
                                            <circle cx="50" cy="40" r="2" fill="#ef4444" />
                                            <text x="20" y="15" fontSize="8" fill="#374151">A</text>
                                            <text x="50" y="50" fontSize="8" fill="#374151">B</text>
                                            <text x="35" y="55" textAnchor="middle" fontSize="8" fill="#374151">O</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">A line segment whose endpoints both lie on the circle.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: AB is a chord of circle O</div>
                            </div>

                                                        {/* Segment */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Segment</div>
                                        <div className="text-xs text-gray-500">Region between chord and arc</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <circle cx="35" cy="30" r="20" fill="none" stroke="#3b82f6" strokeWidth="2" />
                                            <line x1="20" y1="20" x2="50" y2="40" stroke="#ef4444" strokeWidth="2" />
                                            <path d="M 20 20 A 20 20 0 0 1 50 40 L 20 20 Z" fill="#10b981" fillOpacity="0.3" />
                                            <circle cx="20" cy="20" r="2" fill="#ef4444" />
                                            <circle cx="50" cy="40" r="2" fill="#ef4444" />
                                            <text x="20" y="15" fontSize="8" fill="#374151">A</text>
                                            <text x="50" y="50" fontSize="8" fill="#374151">B</text>
                                            <text x="35" y="55" textAnchor="middle" fontSize="8" fill="#374151">O</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">The region between a chord and the arc it subtends.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Example: Minor segment and major segment</div>
                            </div>

                                                        {/* Radius */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Radius</div>
                                        <div className="text-xs text-gray-500">Distance from center to edge (r)</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <circle cx="35" cy="30" r="20" fill="none" stroke="#3b82f6" strokeWidth="2" />
                                            <line x1="35" y1="30" x2="35" y2="10" stroke="#10b981" strokeWidth="2" />
                                            <circle cx="35" cy="30" r="2" fill="#10b981" />
                                            <circle cx="35" cy="10" r="2" fill="#10b981" />
                                            <text x="35" y="55" textAnchor="middle" fontSize="8" fill="#374151">O</text>
                                            <text x="35" y="8" textAnchor="middle" fontSize="8" fill="#374151">A</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">The distance from the center of the circle to any point on the circle.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: r or OA (where O is center, A is on circle)</div>
                            </div>

                                                        {/* Diameter */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Diameter</div>
                                        <div className="text-xs text-gray-500">Twice the radius (d = 2r)</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <circle cx="35" cy="30" r="20" fill="none" stroke="#3b82f6" strokeWidth="2" />
                                            <line x1="15" y1="30" x2="55" y2="30" stroke="#f97316" strokeWidth="2" />
                                            <circle cx="15" cy="30" r="2" fill="#f97316" />
                                            <circle cx="55" cy="30" r="2" fill="#f97316" />
                                            <circle cx="35" cy="30" r="2" fill="#f97316" />
                                            <text x="15" y="25" fontSize="8" fill="#374151">A</text>
                                            <text x="55" y="25" fontSize="8" fill="#374151">B</text>
                                            <text x="35" y="55" textAnchor="middle" fontSize="8" fill="#374151">O</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">A chord that passes through the center of the circle. It is twice the length of the radius.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: d = 2r or AB (where A and B are endpoints)</div>
                            </div>

                                                        {/* Arc */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex-1">
                                        <div className="text-sm font-medium text-gray-800">Arc</div>
                                        <div className="text-xs text-gray-500">Part of circumference between two points</div>
                                    </div>
                                    <div className="flex-shrink-0 ml-4">
                                        <svg width="70" height="60" viewBox="0 0 70 60">
                                            <circle cx="35" cy="30" r="20" fill="none" stroke="#3b82f6" strokeWidth="2" />
                                            <path d="M 20 20 A 20 20 0 0 1 50 40" stroke="#ef4444" strokeWidth="3" fill="none" />
                                            <circle cx="20" cy="20" r="2" fill="#ef4444" />
                                            <circle cx="50" cy="40" r="2" fill="#ef4444" />
                                            <text x="20" y="15" fontSize="8" fill="#374151">A</text>
                                            <text x="50" y="50" fontSize="8" fill="#374151">B</text>
                                            <text x="35" y="55" textAnchor="middle" fontSize="8" fill="#374151">O</text>
                                        </svg>
                                    </div>
                                </div>
                                <p className="text-sm text-gray-600 mb-2">A portion of the circumference of a circle between two points.</p>
                                <div className="text-sm text-gray-500 bg-gray-50 p-2 rounded">Notation: AB (arc from A to B) or minor arc, major arc</div>
                            </div>
                                    </div>
                                )}
                            </div>
                        </div>
                    )}

                    {geometryData.selectedSubConcept === 'triangles' && (
                        <div className="space-y-4">
                            {/* Python Backend Toggle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-4">
                                    <h5 className="text-sm font-semibold text-gray-800">Triangles</h5>
                                    <div className="flex items-center space-x-3">
                                        <span className="text-xs text-gray-500">Rendering:</span>
                                        <button
                                            onClick={() => setGeometryData(prev => ({ ...prev, usePythonBackend: true }))}
                                            className={`px-3 py-1 text-xs rounded-full transition-colors ${
                                                geometryData.usePythonBackend 
                                                    ? 'bg-green-100 text-green-800 border border-green-300' 
                                                    : 'bg-gray-100 text-gray-600 border border-gray-300'
                                            }`}
                                        >
                                            🐍 Python Backend
                                        </button>
                                        <button
                                            onClick={() => setGeometryData(prev => ({ ...prev, usePythonBackend: false }))}
                                            className={`px-3 py-1 text-xs rounded-full transition-colors ${
                                                !geometryData.usePythonBackend 
                                                    ? 'bg-blue-100 text-blue-800 border border-blue-300' 
                                                    : 'bg-gray-100 text-gray-600 border border-gray-300'
                                            }`}
                                        >
                                            🎨 Canvas Fallback
                                        </button>
                                    </div>
                                </div>
                                
                                {geometryData.usePythonBackend ? (
                                    <PythonBasicShapes
                                        selectedSubConcept="triangles"
                                        onChange={onChange}
                                    />
                                ) : (
                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                        <h5 className="text-sm font-semibold text-gray-800 mb-3">Triangles</h5>
                                        <p className="text-sm text-gray-600">Coming soon...</p>
                                    </div>
                                )}
                            </div>
                        </div>
                    )}

                    {geometryData.selectedSubConcept === 'quadrilaterals' && (
                        <div className="space-y-4">
                            {/* Python Backend Toggle */}
                            <div className="bg-white rounded-lg p-4 border">
                                <div className="flex items-center justify-between mb-4">
                                    <h5 className="text-sm font-semibold text-gray-800">Quadrilaterals</h5>
                                    <div className="flex items-center space-x-3">
                                        <span className="text-xs text-gray-500">Rendering:</span>
                                        <button
                                            onClick={() => setGeometryData(prev => ({ ...prev, usePythonBackend: true }))}
                                            className={`px-3 py-1 text-xs rounded-full transition-colors ${
                                                geometryData.usePythonBackend 
                                                    ? 'bg-green-100 text-green-800 border border-green-300' 
                                                    : 'bg-gray-100 text-gray-600 border border-gray-300'
                                            }`}
                                        >
                                            🐍 Python Backend
                                        </button>
                                        <button
                                            onClick={() => setGeometryData(prev => ({ ...prev, usePythonBackend: false }))}
                                            className={`px-3 py-1 text-xs rounded-full transition-colors ${
                                                !geometryData.usePythonBackend 
                                                    ? 'bg-blue-100 text-blue-800 border border-blue-300' 
                                                    : 'bg-gray-100 text-gray-600 border border-gray-300'
                                            }`}
                                        >
                                            🎨 Canvas Fallback
                                        </button>
                                    </div>
                                </div>
                                
                                {geometryData.usePythonBackend ? (
                                    <PythonBasicShapes
                                        selectedSubConcept="quadrilaterals"
                                        onChange={onChange}
                                    />
                                ) : (
                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                        <h5 className="text-sm font-semibold text-gray-800 mb-3">Quadrilaterals</h5>
                                        <p className="text-sm text-gray-600">Coming soon...</p>
                                    </div>
                                )}
                            </div>
                        </div>
                    )}
                            </div>
                        </div>
        );
    };

    // Render Properties of 2D Shapes
    const renderPropertiesOf2DShapes = () => {

        const shapeTypes = [
            { id: 'triangles', name: 'Triangles', icon: '🔺' },
            { id: 'quadrilaterals', name: 'Quadrilaterals', icon: '⬜' },
            { id: 'circles', name: 'Circles', icon: '⭕' },
            { id: 'angles', name: 'Angles', icon: '📐' }
        ];

        const calculateProperties = async (shapeType, parameters) => {
            setIsCalculating(true);
            try {
                const response = await fetch(buildApiUrl('/api/math/geometry/calculate-properties'), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        shape: shapeType,
                        parameters: parameters,
                        include_diagram: true
                    })
                });
                const data = await response.json();
                if (data.success) {
                    setShapeProperties(data);
                } else {
                    console.error('Calculation failed:', data.error);
                }
            } catch (error) {
                console.error('Error calculating properties:', error);
            } finally {
                setIsCalculating(false);
            }
        };

        return (
            <div className="w-full h-full overflow-y-auto p-4 bg-gray-50">
                <div className="space-y-4">
                    {/* Title */}
                    <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                        <h4 className="text-sm font-semibold text-blue-800 mb-2">Properties of 2D Shapes</h4>
                        <p className="text-blue-700 text-xs">Analyze and calculate properties of geometric shapes</p>
                    </div>
                    
                    {/* Shape Type Selection */}
                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                        <h5 className="text-sm font-semibold text-gray-800 mb-3">Select Shape Type</h5>
                        <div className="grid grid-cols-2 gap-2">
                            {shapeTypes.map(type => (
                                <button
                                    key={type.id}
                                    onClick={() => setSelectedShapeType(type.id)}
                                    className={`p-3 rounded-lg text-left transition-colors ${
                                        selectedShapeType === type.id
                                            ? 'bg-blue-100 border-2 border-blue-500 text-blue-800'
                                            : 'bg-gray-50 border border-gray-200 hover:bg-gray-100 text-gray-700'
                                    }`}
                                >
                                    <div className="flex items-center">
                                        <span className="text-lg mr-2">{type.icon}</span>
                                        <span className="text-sm font-medium">{type.name}</span>
                                    </div>
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Shape-specific Properties */}
                    {selectedShapeType === 'triangles' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Triangle Properties</h5>
                            <div className="space-y-3">
                                <div className="grid grid-cols-2 gap-3">
                                    <button
                                        onClick={() => calculateProperties('triangle', { 
                                            vertices: [[0, 0], [3, 0], [1.5, 2.6]], 
                                            type: 'equilateral' 
                                        })}
                                        className="p-2 bg-green-50 border border-green-200 rounded text-sm hover:bg-green-100"
                                    >
                                        Equilateral Triangle
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('triangle', { 
                                            vertices: [[0, 0], [4, 0], [2, 3]], 
                                            type: 'isosceles' 
                                        })}
                                        className="p-2 bg-blue-50 border border-blue-200 rounded text-sm hover:bg-blue-100"
                                    >
                                        Isosceles Triangle
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('triangle', { 
                                            vertices: [[0, 0], [3, 0], [1, 2]], 
                                            type: 'scalene' 
                                        })}
                                        className="p-2 bg-purple-50 border border-purple-200 rounded text-sm hover:bg-purple-100"
                                    >
                                        Scalene Triangle
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('triangle', { 
                                            vertices: [[0, 0], [3, 0], [0, 2]], 
                                            type: 'right' 
                                        })}
                                        className="p-2 bg-red-50 border border-red-200 rounded text-sm hover:bg-red-100"
                                    >
                                        Right Triangle
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {selectedShapeType === 'quadrilaterals' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Quadrilateral Properties</h5>
                            <div className="space-y-3">
                                <div className="grid grid-cols-2 gap-3">
                                    <button
                                        onClick={() => calculateProperties('square', { 
                                            vertices: [[0, 0], [2, 0], [2, 2], [0, 2]] 
                                        })}
                                        className="p-2 bg-green-50 border border-green-200 rounded text-sm hover:bg-green-100"
                                    >
                                        Square
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('rectangle', { 
                                            vertices: [[0, 0], [3, 0], [3, 2], [0, 2]] 
                                        })}
                                        className="p-2 bg-blue-50 border border-blue-200 rounded text-sm hover:bg-blue-100"
                                    >
                                        Rectangle
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('rhombus', { 
                                            vertices: [[1, 0], [2, 1], [1, 2], [0, 1]] 
                                        })}
                                        className="p-2 bg-purple-50 border border-purple-200 rounded text-sm hover:bg-purple-100"
                                    >
                                        Rhombus
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('parallelogram', { 
                                            vertices: [[0, 0], [3, 0], [4, 2], [1, 2]] 
                                        })}
                                        className="p-2 bg-orange-50 border border-orange-200 rounded text-sm hover:bg-orange-100"
                                    >
                                        Parallelogram
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {selectedShapeType === 'circles' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Circle Properties</h5>
                            <div className="space-y-3">
                                <div className="grid grid-cols-2 gap-3">
                                    <button
                                        onClick={() => calculateProperties('circle', { radius: 2 })}
                                        className="p-2 bg-green-50 border border-green-200 rounded text-sm hover:bg-green-100"
                                    >
                                        Circle (r=2)
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('circle', { radius: 3 })}
                                        className="p-2 bg-blue-50 border border-blue-200 rounded text-sm hover:bg-blue-100"
                                    >
                                        Circle (r=3)
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {selectedShapeType === 'angles' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Angle Properties</h5>
                            <div className="space-y-3">
                                <div className="grid grid-cols-2 gap-3">
                                    <button
                                        onClick={() => calculateProperties('angles', { 
                                            angle_type: 'acute', 
                                            measurement: 45 
                                        })}
                                        className="p-2 bg-green-50 border border-green-200 rounded text-sm hover:bg-green-100"
                                    >
                                        Acute Angle (45°)
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('angles', { 
                                            angle_type: 'right', 
                                            measurement: 90 
                                        })}
                                        className="p-2 bg-red-50 border border-red-200 rounded text-sm hover:bg-red-100"
                                    >
                                        Right Angle (90°)
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('angles', { 
                                            angle_type: 'obtuse', 
                                            measurement: 135 
                                        })}
                                        className="p-2 bg-orange-50 border border-orange-200 rounded text-sm hover:bg-orange-100"
                                    >
                                        Obtuse Angle (135°)
                                    </button>
                                    <button
                                        onClick={() => calculateProperties('angles', { 
                                            angle_type: 'straight', 
                                            measurement: 180 
                                        })}
                                        className="p-2 bg-purple-50 border border-purple-200 rounded text-sm hover:bg-purple-100"
                                    >
                                        Straight Angle (180°)
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Results Display */}
                    {isCalculating && (
                        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                            <div className="flex items-center">
                                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-yellow-600 mr-2"></div>
                                <span className="text-sm text-yellow-800">Calculating properties...</span>
                            </div>
                        </div>
                    )}

                    {shapeProperties && (
                        <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-green-800 mb-3">Calculated Properties</h5>
                            <div className="space-y-2">
                                {shapeProperties.calculations && Object.entries(shapeProperties.calculations).map(([key, value]) => (
                                    <div key={key} className="flex justify-between text-sm">
                                        <span className="text-green-700 capitalize">{key.replace('_', ' ')}:</span>
                                        <span className="text-green-800 font-medium">{typeof value === 'number' ? value.toFixed(2) : value}</span>
                                    </div>
                                ))}
                                {shapeProperties.classification && (
                                    <div className="mt-3 p-2 bg-white rounded border">
                                        <span className="text-sm font-medium text-green-800">Classification: </span>
                                        <span className="text-sm text-green-700">{shapeProperties.classification}</span>
                                    </div>
                                )}
                            </div>
                            {(shapeProperties.diagram || shapeProperties.calculations?.diagram) && (
                                <div className="mt-3">
                                    <img 
                                        src={shapeProperties.diagram || shapeProperties.calculations?.diagram} 
                                        alt="Shape diagram" 
                                        className="max-w-full h-auto border rounded"
                                    />
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>
        );
    };

    // Render Calculations involving 2D Shapes
    const renderCalculations2DShapes = () => {

        const calculationTypes = [
            { id: 'area_perimeter', name: 'Area & Perimeter', icon: '📐' },
            { id: 'angles', name: 'Angle Calculations', icon: '📏' },
            { id: 'similarity_congruency', name: 'Similarity & Congruency', icon: '🔄' },
            { id: 'quiz', name: 'Quiz Generator', icon: '🧠' },
            { id: 'educational', name: 'Educational Mode', icon: '🎓' }
        ];

        const generateQuiz = async (topic, difficulty = 'medium') => {
            console.log('Generating quiz for topic:', topic, 'difficulty:', difficulty);
            setIsGeneratingQuiz(true);
            // Switch to quiz view to show the quiz when it's generated
            setSelectedCalculation('quiz');
            try {
                // Determine question type and shape type based on topic
                let questionType = 'area_calculation';
                let shapeType = selectedShapeType === 'triangles' ? 'triangle_equilateral' : 
                               selectedShapeType === 'quadrilaterals' ? 'rectangle' : 'circle';
                
                if (topic === 'similarity') {
                    questionType = 'shape_classification';
                    shapeType = 'triangle_equilateral';
                } else if (topic === 'congruency') {
                    questionType = 'shape_classification';
                    shapeType = 'triangle_equilateral';
                } else if (topic === 'similarity_congruency') {
                    questionType = 'shape_classification';
                    shapeType = 'triangle_equilateral';
                }

                const response = await fetch(buildApiUrl('/api/math/geometry/generate-quiz-question'), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        topic: topic || 'Calculations involving 2D Shapes',
                        difficulty: difficulty || 'easy',
                        question_type: questionType,
                        shape_type: shapeType,
                        count: 1,
                        include_diagram: true,
                        south_african_context: true,
                        conversion_required: false,
                        reasoning_required: difficulty === 'hard'
                    })
                });
                console.log('Enhanced quiz response status:', response.status);
                const data = await response.json();
                console.log('Enhanced quiz response data:', data);
                if (data.success && data.questions && data.questions.length > 0) {
                    // Use the first question from the enhanced response
                    const question = data.questions[0];
                    setQuizQuestion({
                        question: question.question,
                        options: question.options,
                        correct_answer: question.correct_answer,
                        explanation: question.explanation,
                        topic: question.topic,
                        difficulty: question.difficulty,
                        question_type: question.question_type,
                        shape_type: question.shape_type,
                        parameters: question.parameters,
                        geometric_constraints: question.geometric_constraints,
                        curriculum_alignments: question.curriculum_alignments,
                        metric_units: question.metric_units,
                        south_african_context: question.south_african_context,
                        conversion_required: question.conversion_required,
                        reasoning_required: question.reasoning_required,
                        question_id: question.question_id
                    });
                    setQuizResult(null);
                    setUserAnswer('');
                    console.log('Enhanced quiz question generated successfully');
                } else {
                    console.error('Enhanced quiz generation failed:', data.error || 'No questions generated');
                    // Fallback to legacy system
                    const legacyResponse = await fetch(buildApiUrl('/api/math/geometry/generate-quiz-question'), {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            topic: topic,
                            difficulty: difficulty
                        })
                    });
                    const legacyData = await legacyResponse.json();
                    if (legacyData.success) {
                        setQuizQuestion(legacyData);
                        setQuizResult(null);
                        setUserAnswer('');
                        console.log('Fallback to legacy quiz system');
                    } else {
                        console.error('Both enhanced and legacy quiz generation failed');
                    }
                }
            } catch (error) {
                console.error('Error generating quiz:', error);
            } finally {
                setIsGeneratingQuiz(false);
            }
        };

        const checkAnswer = async () => {
            if (!quizQuestion || !userAnswer) return;
            
            const correctAnswer = quizQuestion.correct_answer;
            const isCorrect = userAnswer.toLowerCase().trim() === correctAnswer.toLowerCase().trim();
            
            // Update student performance
            const newPerformance = {
                ...studentPerformance,
                questions_attempted: studentPerformance.questions_attempted + 1,
                correct_percentage: isCorrect ? 
                    (studentPerformance.correct_percentage * studentPerformance.questions_attempted + 1) / (studentPerformance.questions_attempted + 1) :
                    (studentPerformance.correct_percentage * studentPerformance.questions_attempted) / (studentPerformance.questions_attempted + 1)
            };
            setStudentPerformance(newPerformance);
            
            // Generate educational feedback
            await generateEducationalFeedback(quizQuestion, userAnswer, newPerformance);
            
            setQuizResult({
                correct: isCorrect,
                userAnswer: userAnswer,
                correctAnswer: correctAnswer,
                explanation: quizQuestion.explanation
            });
        };

        return (
            <div className="w-full h-full overflow-y-auto p-4 bg-gray-50">
                <div className="space-y-4">
                    {/* Title */}
                    <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                        <h4 className="text-sm font-semibold text-blue-800 mb-2">Calculations involving 2D Shapes</h4>
                        <p className="text-blue-700 text-xs">Advanced calculations, quizzes, and educational tools</p>
                    </div>
                    
                    {/* Progress Tracking */}
                    <div className="bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 rounded-lg p-4">
                        <h5 className="text-sm font-semibold text-purple-800 mb-3">📊 Learning Progress</h5>
                        <div className="grid grid-cols-2 gap-4">
                            <div className="bg-white rounded-lg p-3 border border-purple-200">
                                <div className="text-xs text-purple-600 font-medium mb-1">Accuracy</div>
                                <div className="text-lg font-bold text-purple-800">
                                    {Math.round(studentPerformance.correct_percentage * 100)}%
                                </div>
                                <div className="w-full bg-purple-200 rounded-full h-2 mt-1">
                                    <div 
                                        className="bg-purple-500 h-2 rounded-full transition-all duration-300"
                                        style={{ width: `${studentPerformance.correct_percentage * 100}%` }}
                                    ></div>
                                </div>
                            </div>
                            <div className="bg-white rounded-lg p-3 border border-purple-200">
                                <div className="text-xs text-purple-600 font-medium mb-1">Questions Attempted</div>
                                <div className="text-lg font-bold text-purple-800">
                                    {studentPerformance.questions_attempted}
                                </div>
                                <div className="text-xs text-purple-600 mt-1">
                                    Hints used: {studentPerformance.hints_used}
                                </div>
                            </div>
                        </div>
                        {studentPerformance.correct_percentage >= 0.8 && (
                            <div className="mt-3 p-2 bg-green-100 border border-green-300 rounded text-center">
                                <span className="text-xs text-green-700 font-medium">🌟 Great job! You're mastering this topic!</span>
                            </div>
                        )}
                    </div>
                    
                    {/* Calculation Type Selection */}
                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                        <h5 className="text-sm font-semibold text-gray-800 mb-3">Select Calculation Type</h5>
                        <div className="grid grid-cols-2 gap-2">
                            {calculationTypes.map(type => (
                                <button
                                    key={type.id}
                                    onClick={() => setSelectedCalculation(type.id)}
                                    className={`p-3 rounded-lg text-left transition-colors ${
                                        selectedCalculation === type.id
                                            ? 'bg-green-100 border-2 border-green-500 text-green-800'
                                            : 'bg-gray-50 border border-gray-200 hover:bg-gray-100 text-gray-700'
                                    }`}
                                >
                                    <div className="flex items-center">
                                        <span className="text-lg mr-2">{type.icon}</span>
                                        <span className="text-sm font-medium">{type.name}</span>
                                    </div>
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Area & Perimeter Calculations */}
                    {selectedCalculation === 'area_perimeter' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Area & Perimeter Calculator</h5>
                            <div className="space-y-4">
                                <div className="grid grid-cols-2 gap-3">
                                    <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                                        <h6 className="text-sm font-medium text-blue-800 mb-2">Triangle Calculator</h6>
                                        <p className="text-xs text-blue-600 mb-2">Calculate area, perimeter, and angles</p>
                                        <button
                                            onClick={() => generateQuiz('triangles', 'easy')}
                                            className="text-xs bg-blue-600 text-white px-2 py-1 rounded hover:bg-blue-700"
                                        >
                                            Try Triangle Quiz
                                        </button>
                                    </div>
                                    <div className="p-3 bg-green-50 border border-green-200 rounded">
                                        <h6 className="text-sm font-medium text-green-800 mb-2">Circle Calculator</h6>
                                        <p className="text-xs text-green-600 mb-2">Calculate area, circumference, diameter</p>
                                        <button
                                            onClick={() => generateQuiz('circles', 'easy')}
                                            className="text-xs bg-green-600 text-white px-2 py-1 rounded hover:bg-green-700"
                                        >
                                            Try Circle Quiz
                                        </button>
                                    </div>
                                    <div className="p-3 bg-purple-50 border border-purple-200 rounded">
                                        <h6 className="text-sm font-medium text-purple-800 mb-2">Rectangle Calculator</h6>
                                        <p className="text-xs text-purple-600 mb-2">Calculate area, perimeter, diagonal</p>
                                        <button
                                            onClick={() => generateQuiz('quadrilaterals', 'medium')}
                                            className="text-xs bg-purple-600 text-white px-2 py-1 rounded hover:bg-purple-700"
                                        >
                                            Try Rectangle Quiz
                                        </button>
                                    </div>
                                    <div className="p-3 bg-orange-50 border border-orange-200 rounded">
                                        <h6 className="text-sm font-medium text-orange-800 mb-2">Quadrilateral Calculator</h6>
                                        <p className="text-xs text-orange-600 mb-2">Calculate properties of various quadrilaterals</p>
                                        <button
                                            onClick={() => generateQuiz('quadrilaterals', 'hard')}
                                            className="text-xs bg-orange-600 text-white px-2 py-1 rounded hover:bg-orange-700"
                                        >
                                            Try Quadrilateral Quiz
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Angle Calculations */}
                    {selectedCalculation === 'angles' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Angle Calculations</h5>
                            <div className="space-y-4">
                                <div className="grid grid-cols-2 gap-3">
                                    <div className="p-3 bg-red-50 border border-red-200 rounded">
                                        <h6 className="text-sm font-medium text-red-800 mb-2">Angle Classification</h6>
                                        <p className="text-xs text-red-600 mb-2">Identify acute, right, obtuse, straight angles</p>
                                        <button
                                            onClick={() => generateQuiz('angles', 'easy')}
                                            className="text-xs bg-red-600 text-white px-2 py-1 rounded hover:bg-red-700"
                                        >
                                            Try Angle Quiz
                                        </button>
                                    </div>
                                    <div className="p-3 bg-indigo-50 border border-indigo-200 rounded">
                                        <h6 className="text-sm font-medium text-indigo-800 mb-2">Angle Measurement</h6>
                                        <p className="text-xs text-indigo-600 mb-2">Calculate unknown angles in triangles</p>
                                        <button
                                            onClick={() => generateQuiz('angle_measurement', 'medium')}
                                            className="text-xs bg-indigo-600 text-white px-2 py-1 rounded hover:bg-indigo-700"
                                        >
                                            Try Measurement Quiz
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Similarity & Congruency */}
                    {selectedCalculation === 'similarity_congruency' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Similarity & Congruency</h5>
                            <div className="space-y-4">
                                <div className="grid grid-cols-2 gap-3">
                                    <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                                        <h6 className="text-sm font-medium text-blue-800 mb-2">Shape Similarity</h6>
                                        <p className="text-xs text-blue-600 mb-2">Identify similar shapes with proportional sides</p>
                                        <button
                                            onClick={() => generateQuiz('similarity', 'medium')}
                                            className="text-xs bg-blue-600 text-white px-2 py-1 rounded hover:bg-blue-700"
                                        >
                                            Try Similarity Quiz
                                        </button>
                                    </div>
                                    <div className="p-3 bg-green-50 border border-green-200 rounded">
                                        <h6 className="text-sm font-medium text-green-800 mb-2">Shape Congruency</h6>
                                        <p className="text-xs text-green-600 mb-2">Identify congruent shapes with equal sides and angles</p>
                                        <button
                                            onClick={() => generateQuiz('congruency', 'medium')}
                                            className="text-xs bg-green-600 text-white px-2 py-1 rounded hover:bg-green-700"
                                        >
                                            Try Congruency Quiz
                                        </button>
                                    </div>
                                </div>
                                <div className="p-3 bg-purple-50 border border-purple-200 rounded">
                                    <h6 className="text-sm font-medium text-purple-800 mb-2">Advanced Comparison</h6>
                                    <p className="text-xs text-purple-600 mb-2">Complex similarity and congruency problems with reasoning</p>
                                    <button
                                        onClick={() => generateQuiz('similarity_congruency', 'hard')}
                                        className="text-xs bg-purple-600 text-white px-2 py-1 rounded hover:bg-purple-700"
                                    >
                                        Try Advanced Quiz
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Quiz Generator */}
                    {selectedCalculation === 'quiz' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Interactive Quiz Generator</h5>
                            <div className="space-y-4">
                                {/* Shape Selection */}
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-2">Select Shape:</label>
                                    <div className="grid grid-cols-2 gap-2">
                                        <button
                                            onClick={() => setSelectedShapeType('triangles')}
                                            className={`p-2 text-xs rounded border ${
                                                selectedShapeType === 'triangles'
                                                    ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                    : 'bg-gray-50 border-gray-200 text-gray-700 hover:bg-gray-100'
                                            }`}
                                        >
                                            Triangles
                                        </button>
                                        <button
                                            onClick={() => setSelectedShapeType('quadrilaterals')}
                                            className={`p-2 text-xs rounded border ${
                                                selectedShapeType === 'quadrilaterals'
                                                    ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                    : 'bg-gray-50 border-gray-200 text-gray-700 hover:bg-gray-100'
                                            }`}
                                        >
                                            Quadrilaterals
                                        </button>
                                        <button
                                            onClick={() => setSelectedShapeType('circles')}
                                            className={`p-2 text-xs rounded border ${
                                                selectedShapeType === 'circles'
                                                    ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                    : 'bg-gray-50 border-gray-200 text-gray-700 hover:bg-gray-100'
                                            }`}
                                        >
                                            Circles
                                        </button>
                                        <button
                                            onClick={() => setSelectedShapeType('angles')}
                                            className={`p-2 text-xs rounded border ${
                                                selectedShapeType === 'angles'
                                                    ? 'bg-blue-100 border-blue-500 text-blue-800'
                                                    : 'bg-gray-50 border-gray-200 text-gray-700 hover:bg-gray-100'
                                            }`}
                                        >
                                            Angles
                                        </button>
                                    </div>
                                </div>

                                {/* Difficulty Selection */}
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-2">Select Difficulty:</label>
                                    <div className="grid grid-cols-3 gap-2">
                                        <button
                                            onClick={() => generateQuiz(selectedShapeType, 'easy')}
                                            disabled={isGeneratingQuiz}
                                            className="p-2 bg-green-50 border border-green-200 rounded text-sm hover:bg-green-100 disabled:opacity-50"
                                        >
                                            Easy {selectedShapeType.charAt(0).toUpperCase() + selectedShapeType.slice(1)}
                                        </button>
                                        <button
                                            onClick={() => generateQuiz(selectedShapeType, 'medium')}
                                            disabled={isGeneratingQuiz}
                                            className="p-2 bg-blue-50 border border-blue-200 rounded text-sm hover:bg-blue-100 disabled:opacity-50"
                                        >
                                            Medium {selectedShapeType.charAt(0).toUpperCase() + selectedShapeType.slice(1)}
                                        </button>
                                        <button
                                            onClick={() => generateQuiz(selectedShapeType, 'hard')}
                                            disabled={isGeneratingQuiz}
                                            className="p-2 bg-red-50 border border-red-200 rounded text-sm hover:bg-red-100 disabled:opacity-50"
                                        >
                                            Hard {selectedShapeType.charAt(0).toUpperCase() + selectedShapeType.slice(1)}
                                        </button>
                                    </div>
                                </div>

                                {isGeneratingQuiz && (
                                    <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                                        <div className="flex items-center">
                                            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-yellow-600 mr-2"></div>
                                            <span className="text-sm text-yellow-800">Generating quiz question...</span>
                                        </div>
                                    </div>
                                )}

                                {quizQuestion && (
                                    <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                                        <h6 className="text-sm font-semibold text-blue-800 mb-2">Quiz Question</h6>
                                        <p className="text-sm text-blue-700 mb-3">{quizQuestion.question}</p>
                                        
                                        <div className="space-y-2">
                                            {quizQuestion.options && quizQuestion.options.map((option, index) => (
                                                <label key={index} className="flex items-center">
                                                    <input
                                                        type="radio"
                                                        name="quizAnswer"
                                                        value={option}
                                                        onChange={(e) => setUserAnswer(e.target.value)}
                                                        className="mr-2"
                                                    />
                                                    <span className="text-sm text-blue-700">{option}</span>
                                                </label>
                                            ))}
                                        </div>

                                        <div className="mt-4 flex space-x-2">
                                            <button
                                                onClick={checkAnswer}
                                                className="px-3 py-1 bg-blue-600 text-white text-sm rounded hover:bg-blue-700"
                                            >
                                                Check Answer
                                            </button>
                                            <button
                                                onClick={() => generateQuiz(quizQuestion.topic, quizQuestion.difficulty)}
                                                className="px-3 py-1 bg-gray-600 text-white text-sm rounded hover:bg-gray-700"
                                            >
                                                New Question
                                            </button>
                                        </div>

                                        {/* Educational Features */}
                                        <div className="mt-4 border-t border-blue-200 pt-4">
                                            <div className="flex space-x-2 mb-3">
                                                <button
                                                    onClick={() => {
                                                        generateHints(quizQuestion, studentPerformance);
                                                        setShowHints(true);
                                                    }}
                                                    disabled={isLoadingEducational}
                                                    className="px-3 py-1 bg-yellow-500 text-white text-sm rounded hover:bg-yellow-600 disabled:opacity-50"
                                                >
                                                    {isLoadingEducational ? 'Loading...' : '💡 Get Hints'}
                                                </button>
                                                <button
                                                    onClick={() => {
                                                        generateSolution(quizQuestion);
                                                        setShowSolution(true);
                                                    }}
                                                    disabled={isLoadingEducational}
                                                    className="px-3 py-1 bg-green-500 text-white text-sm rounded hover:bg-green-600 disabled:opacity-50"
                                                >
                                                    {isLoadingEducational ? 'Loading...' : '📝 Show Solution'}
                                                </button>
                                            </div>

                                            {/* Hints Display */}
                                            {showHints && hints.length > 0 && (
                                                <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3 mb-3">
                                                    <div className="flex items-center justify-between mb-2">
                                                        <h6 className="text-sm font-semibold text-yellow-800">💡 Hints</h6>
                                                        <button
                                                            onClick={() => setShowHints(false)}
                                                            className="text-yellow-600 hover:text-yellow-800"
                                                        >
                                                            ✕
                                                        </button>
                                                    </div>
                                                    <div className="space-y-2">
                                                        {hints.map((hint, index) => (
                                                            <div key={hint.hint_id} className={`p-2 rounded ${index === currentHintIndex ? 'bg-yellow-100' : 'bg-yellow-50'}`}>
                                                                <div className="flex items-start justify-between">
                                                                    <div className="flex-1">
                                                                        <div className="text-xs text-yellow-600 mb-1">
                                                                            {hint.hint_type.charAt(0).toUpperCase() + hint.hint_type.slice(1)} Hint
                                                                        </div>
                                                                        <p className="text-sm text-yellow-800">{hint.hint_text}</p>
                                                                    </div>
                                                                    {hints.length > 1 && (
                                                                        <div className="ml-2 flex space-x-1">
                                                                            <button
                                                                                onClick={() => setCurrentHintIndex(Math.max(0, currentHintIndex - 1))}
                                                                                disabled={currentHintIndex === 0}
                                                                                className="px-2 py-1 text-xs bg-yellow-200 text-yellow-800 rounded disabled:opacity-50"
                                                                            >
                                                                                ←
                                                                            </button>
                                                                            <button
                                                                                onClick={() => setCurrentHintIndex(Math.min(hints.length - 1, currentHintIndex + 1))}
                                                                                disabled={currentHintIndex === hints.length - 1}
                                                                                className="px-2 py-1 text-xs bg-yellow-200 text-yellow-800 rounded disabled:opacity-50"
                                                                            >
                                                                                →
                                                                            </button>
                                                                        </div>
                                                                    )}
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                            )}

                                            {/* Solution Steps Display */}
                                            {showSolution && solutionSteps.length > 0 && (
                                                <div className="bg-green-50 border border-green-200 rounded-lg p-3 mb-3">
                                                    <div className="flex items-center justify-between mb-2">
                                                        <h6 className="text-sm font-semibold text-green-800">📝 Step-by-Step Solution</h6>
                                                        <button
                                                            onClick={() => setShowSolution(false)}
                                                            className="text-green-600 hover:text-green-800"
                                                        >
                                                            ✕
                                                        </button>
                                                    </div>
                                                    <div className="space-y-3">
                                                        {solutionSteps.map((step, index) => (
                                                            <div key={step.step_id} className="bg-white rounded p-3 border border-green-200">
                                                                <div className="flex items-start">
                                                                    <div className="flex-shrink-0 w-6 h-6 bg-green-500 text-white text-xs rounded-full flex items-center justify-center mr-3 mt-0.5">
                                                                        {step.step_number}
                                                                    </div>
                                                                    <div className="flex-1">
                                                                        <h7 className="text-sm font-medium text-green-800 mb-1">{step.step_description}</h7>
                                                                        <p className="text-sm text-gray-700 mb-1"><strong>Action:</strong> {step.step_action}</p>
                                                                        <p className="text-sm text-gray-700 mb-1"><strong>Result:</strong> {step.step_result}</p>
                                                                        <p className="text-sm text-gray-600">{step.step_explanation}</p>
                                                                        {step.common_mistakes && step.common_mistakes.length > 0 && (
                                                                            <div className="mt-2 p-2 bg-red-50 border border-red-200 rounded">
                                                                                <p className="text-xs text-red-600 font-medium mb-1">Common mistakes to avoid:</p>
                                                                                <ul className="text-xs text-red-600 list-disc list-inside">
                                                                                    {step.common_mistakes.map((mistake, i) => (
                                                                                        <li key={i}>{mistake}</li>
                                                                                    ))}
                                                                                </ul>
                                                                            </div>
                                                                        )}
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                )}

                                {quizResult && (
                                    <div className={`border rounded-lg p-4 ${
                                        quizResult.correct 
                                            ? 'bg-green-50 border-green-200' 
                                            : 'bg-red-50 border-red-200'
                                    }`}>
                                        <h6 className={`text-sm font-semibold mb-2 ${
                                            quizResult.correct ? 'text-green-800' : 'text-red-800'
                                        }`}>
                                            {quizResult.correct ? '✅ Correct!' : '❌ Incorrect'}
                                        </h6>
                                        <p className="text-sm text-gray-700 mb-2">
                                            Your answer: <strong>{quizResult.userAnswer}</strong>
                                        </p>
                                        <p className="text-sm text-gray-700 mb-2">
                                            Correct answer: <strong>{quizResult.correctAnswer}</strong>
                                        </p>
                                        {quizResult.explanation && (
                                            <p className="text-sm text-gray-600">
                                                <strong>Explanation:</strong> {quizResult.explanation}
                                            </p>
                                        )}

                                        {/* Educational Feedback */}
                                        {educationalFeedback && (
                                            <div className="mt-4 border-t border-gray-200 pt-4">
                                                <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                                                    <h6 className="text-sm font-semibold text-blue-800 mb-2">🎓 Educational Feedback</h6>
                                                    <p className="text-sm text-blue-700 mb-2">{educationalFeedback.message}</p>
                                                    <p className="text-sm text-gray-700 mb-2">{educationalFeedback.explanation}</p>
                                                    
                                                    {educationalFeedback.next_steps && educationalFeedback.next_steps.length > 0 && (
                                                        <div className="mt-2">
                                                            <p className="text-xs text-blue-600 font-medium mb-1">Next steps:</p>
                                                            <ul className="text-xs text-blue-600 list-disc list-inside">
                                                                {educationalFeedback.next_steps.map((step, index) => (
                                                                    <li key={index}>{step}</li>
                                                                ))}
                                                            </ul>
                                                        </div>
                                                    )}
                                                    
                                                    {educationalFeedback.related_concepts && educationalFeedback.related_concepts.length > 0 && (
                                                        <div className="mt-2">
                                                            <p className="text-xs text-blue-600 font-medium mb-1">Related concepts:</p>
                                                            <div className="flex flex-wrap gap-1">
                                                                {educationalFeedback.related_concepts.map((concept, index) => (
                                                                    <span key={index} className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded">
                                                                        {concept}
                                                                    </span>
                                                                ))}
                                                            </div>
                                                        </div>
                                                    )}
                                                    
                                                    {educationalFeedback.difficulty_adjustment && (
                                                        <div className="mt-2 p-2 bg-yellow-50 border border-yellow-200 rounded">
                                                            <p className="text-xs text-yellow-700">
                                                                <strong>Difficulty suggestion:</strong> {educationalFeedback.difficulty_adjustment}
                                                            </p>
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        </div>
                    )}

                    {/* Educational Mode */}
                    {selectedCalculation === 'educational' && (
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <h5 className="text-sm font-semibold text-gray-800 mb-3">Educational Learning Mode</h5>
                            <div className="space-y-4">
                                <div className="grid grid-cols-2 gap-3">
                                    <div className="p-3 bg-emerald-50 border border-emerald-200 rounded">
                                        <h6 className="text-sm font-medium text-emerald-800 mb-2">Construction Mode</h6>
                                        <p className="text-xs text-emerald-600 mb-2">Step-by-step shape construction</p>
                                        <button
                                            onClick={() => generateQuiz('construction', 'easy')}
                                            className="text-xs bg-emerald-600 text-white px-2 py-1 rounded hover:bg-emerald-700"
                                        >
                                            Try Construction
                                        </button>
                                    </div>
                                    <div className="p-3 bg-teal-50 border border-teal-200 rounded">
                                        <h6 className="text-sm font-medium text-teal-800 mb-2">Measurement Mode</h6>
                                        <p className="text-xs text-teal-600 mb-2">Interactive measurement tools</p>
                                        <button
                                            onClick={() => generateQuiz('measurement', 'medium')}
                                            className="text-xs bg-teal-600 text-white px-2 py-1 rounded hover:bg-teal-700"
                                        >
                                            Try Measurement
                                        </button>
                                    </div>
                                    <div className="p-3 bg-cyan-50 border border-cyan-200 rounded">
                                        <h6 className="text-sm font-medium text-cyan-800 mb-2">Classification Mode</h6>
                                        <p className="text-xs text-cyan-600 mb-2">Shape classification and properties</p>
                                        <button
                                            onClick={() => generateQuiz('classification', 'medium')}
                                            className="text-xs bg-cyan-600 text-white px-2 py-1 rounded hover:bg-cyan-700"
                                        >
                                            Try Classification
                                        </button>
                                    </div>
                                    <div className="p-3 bg-sky-50 border border-sky-200 rounded">
                                        <h6 className="text-sm font-medium text-sky-800 mb-2">Assessment Mode</h6>
                                        <p className="text-xs text-sky-600 mb-2">Comprehensive geometry assessment</p>
                                        <button
                                            onClick={() => generateQuiz('assessment', 'hard')}
                                            className="text-xs bg-sky-600 text-white px-2 py-1 rounded hover:bg-sky-700"
                                        >
                                            Try Assessment
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        );
    };

    return (
        <div className={`w-full h-full flex flex-col bg-white ${geometryData.isFullscreen ? 'fixed inset-0 z-50' : ''}`}>
            {/* Header */}
            <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-4">
                <div className="flex items-center justify-between">
                    <div>
                        <h1 className="text-2xl font-bold">{geometryData.title}</h1>
                        <p className="text-blue-100 text-sm">Interactive Geometry Learning Studio</p>
                                                </div>
                    <div className="flex items-center space-x-2">
                        <button
                            onClick={() => handleFieldChange('showGrid', !geometryData.showGrid)}
                            className={`p-2 rounded transition-colors ${
                                geometryData.showGrid ? 'bg-white bg-opacity-20' : 'bg-white bg-opacity-10'
                            }`}
                            title="Toggle Grid"
                        >
                            <Grid3X3 className="w-5 h-5" />
                        </button>
                        <button
                            onClick={() => handleFieldChange('isFullscreen', !geometryData.isFullscreen)}
                            className="p-2 rounded bg-white bg-opacity-10 hover:bg-opacity-20 transition-colors"
                            title="Toggle Fullscreen"
                        >
                            <Maximize2 className="w-5 h-5" />
                        </button>
                                        </div>
                </div>
            </div>

            {/* Main Content */}
            <div className="flex-1 flex">
                {/* Left Panel - Mode and Tool Selection */}
                <div className="w-80 bg-gray-50 border-r border-gray-200 flex flex-col">
                    {/* Mode Selection */}
                    <div className="p-4 border-b border-gray-200">
                        <h3 className="text-lg font-semibold text-gray-800 mb-3">Geometry Modes</h3>
                        <div className="space-y-2">
                            {modes.map(mode => {
                                const IconComponent = mode.icon;
                                return (
                                    <button
                                        key={mode.id}
                                        onClick={() => {
                                            console.log('Mode button clicked:', mode.id);
                                            // Reset tool selection when changing modes
                                            const tools = getToolsForMode(mode.id);
                                            console.log('Available tools for mode:', tools);
                                            
                                            // Update both mode and selectedTool in a single state update
                                            setGeometryData(prevData => {
                                                const newData = {
                                                    ...prevData,
                                                    mode: mode.id,
                                                    selectedTool: tools.length > 0 ? tools[0].id : prevData.selectedTool
                                                };
                                                console.log('Mode switch - New geometry data:', newData);
                                                if (onChange) {
                                                    onChange(newData);
                                                }
                                                return newData;
                                            });
                                        }}
                                        className={`w-full p-3 rounded-lg text-left transition-colors ${
                                            geometryData.mode === mode.id
                                                ? 'bg-blue-100 border-2 border-blue-500 text-blue-800'
                                                : 'bg-white border border-gray-200 hover:bg-gray-50 text-gray-700'
                                        }`}
                                    >
                                        <div className="flex items-center">
                                            <IconComponent className="w-5 h-5 mr-3" />
                                            <div>
                                                <div className="font-medium">{mode.name}</div>
                                                <div className="text-xs opacity-75">{mode.description}</div>
                                                </div>
                                        </div>
                                    </button>
                                );
                            })}
                        </div>
                    </div>

                    {/* Tool Selection */}
                    <div className="flex-1 p-4">
                        <h3 className="text-lg font-semibold text-gray-800 mb-3">Tools</h3>
                        <div className="space-y-2">
                            {getToolsForMode(geometryData.mode).map(tool => (
                                <button
                                    key={tool.id}
                                    onClick={() => handleFieldChange('selectedTool', tool.id)}
                                    className={`w-full p-3 rounded-lg text-left transition-colors ${
                                        geometryData.selectedTool === tool.id
                                            ? 'bg-green-100 border-2 border-green-500 text-green-800'
                                            : 'bg-white border border-gray-200 hover:bg-gray-50 text-gray-700'
                                    }`}
                                >
                                    <div className="font-medium">{tool.name}</div>
                                    <div className="text-xs opacity-75">{tool.description}</div>
                                </button>
                            ))}
                                                </div>
                    </div>
                </div>

                {/* Right Panel - Canvas/Module Area */}
                <div className="flex-1 flex flex-col">
                    {/* 2D Geometry Sub-buttons (only when 2D mode is selected) */}
                    {geometryData.mode === '2d' && (
                        <div className="bg-gray-50 border-b border-gray-200 p-4">
                            <div className="flex justify-center gap-2">
                                {[
                                    { id: 'basics_of_geometry', name: 'Basics of Geometry' },
                                    { id: 'properties_of_2d_shapes', name: 'Properties of 2D Shapes' },
                                    { id: 'calculations_2d_shapes', name: 'Calculations involving 2D Shapes' }
                                                                ].map((button) => (
                                    <button
                                        key={button.id}
                                        onClick={() => handleFieldChange('selectedTool', button.id)}
                                        className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                                            geometryData.selectedTool === button.id
                                                ? 'bg-blue-600 text-white border-2 border-blue-700'
                                                : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
                                        }`}
                                    >
                                        {button.name}
                                    </button>
                                ))}
                            </div>
                            {/* Backend Test Button */}
                            <div className="mt-2 flex justify-center">
                                <button
                                    onClick={() => {
                                        if (setView) {
                                            setView('geometry_backend_test');
                                        } else {
                                            console.log('setView prop not available');
                                        }
                                    }}
                                    className="px-3 py-1 bg-green-600 text-white text-xs rounded hover:bg-green-700 transition-colors"
                                >
                                    🧪 Test Backend Integration
                                </button>
                            </div>
                        </div>
                    )}
                                    
                    {/* Tool Instructions */}
                    <div className="bg-blue-50 border-b border-blue-200 p-3">
                        <div className="flex items-center justify-between">
                            <div>
                                <h4 className="font-semibold text-blue-800">
                                    {getToolsForMode(geometryData.mode).find(t => t.id === geometryData.selectedTool)?.name || 'No Tool Selected'}
                                </h4>
                                <p className="text-sm text-blue-600">
                                    {getToolsForMode(geometryData.mode).find(t => t.id === geometryData.selectedTool)?.description || 'Select a tool to begin'}
                                </p>
                                                </div>
                            <div className="flex items-center space-x-2">
                                <span className="text-xs text-blue-500 bg-blue-100 px-2 py-1 rounded">
                                    {geometryData.mode.toUpperCase()}
                                </span>
                                        </div>
                                </div>
                            </div>

                    {/* Module Content */}
                    <div className="flex-1">
                        {renderModule()}
                        </div>
                </div>
            </div>
        </div>
    );

    // Interactive Controls Rendering
    const renderInteractiveControls = () => {
        const [currentShape, setCurrentShape] = useState('cube');
        const [currentDimensions, setCurrentDimensions] = useState({
            side_length: 3.0,
            length: 4.0,
            breadth: 3.0,
            height: 2.0,
            radius: 2.0
        });
        const [showVisualFeedback, setShowVisualFeedback] = useState(true);
        const [showFormulas, setShowFormulas] = useState(true);
        const [showHints, setShowHints] = useState(false);
        const [hintText, setHintText] = useState("");

        const handleParameterChange = (newDimensions) => {
            setCurrentDimensions(newDimensions);
            // Trigger diagram regeneration here
        };

        const handleReset = () => {
            setCurrentDimensions({
                side_length: 3.0,
                length: 4.0,
                breadth: 3.0,
                height: 2.0,
                radius: 2.0
            });
        };

        const handleMaximize = () => {
            // Implement maximize functionality
        };

        const handleToggleHint = () => {
            setShowHints(!showHints);
            if (!showHints) {
                setHintText("Try adjusting the parameters to see how the shape changes in real-time!");
            }
        };

        return (
            <div className="space-y-6">
                <div className="bg-white rounded-lg border p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4 flex items-center">
                        <Settings className="w-6 h-6 mr-2" />
                        Interactive Parameter Controls
                    </h3>
                    
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                        {/* Parameter Controls */}
                        <div>
                            <InteractiveParameterControls
                                shapeType={currentShape}
                                initialDimensions={currentDimensions}
                                onParameterChange={handleParameterChange}
                                onReset={handleReset}
                                onMaximize={handleMaximize}
                                isGenerating={false}
                            />
                        </div>

                        {/* Visual Feedback Controls */}
                        <div className="space-y-4">
                            <div className="bg-gray-50 rounded-lg p-4">
                                <h4 className="font-medium text-gray-800 mb-3 flex items-center">
                                    <Eye className="w-5 h-5 mr-2" />
                                    Visual Feedback Options
                                </h4>
                                
                                <div className="space-y-3">
                                    <label className="flex items-center">
                                        <input
                                            type="checkbox"
                                            checked={showVisualFeedback}
                                            onChange={(e) => setShowVisualFeedback(e.target.checked)}
                                            className="mr-3"
                                        />
                                        <span className="text-sm text-gray-700">Show Visual Feedback</span>
                                    </label>
                                    
                                    <label className="flex items-center">
                                        <input
                                            type="checkbox"
                                            checked={showFormulas}
                                            onChange={(e) => setShowFormulas(e.target.checked)}
                                            className="mr-3"
                                        />
                                        <span className="text-sm text-gray-700">Show Formulas</span>
                                    </label>
                                    
                                    <label className="flex items-center">
                                        <input
                                            type="checkbox"
                                            checked={showHints}
                                            onChange={handleToggleHint}
                                            className="mr-3"
                                        />
                                        <span className="text-sm text-gray-700">Show Hints</span>
                                    </label>
                                </div>
                            </div>

                            {/* Shape Selection */}
                            <div className="bg-gray-50 rounded-lg p-4">
                                <h4 className="font-medium text-gray-800 mb-3">Select Shape Type</h4>
                                <select
                                    value={currentShape}
                                    onChange={(e) => setCurrentShape(e.target.value)}
                                    className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                >
                                    <option value="cube">Cube</option>
                                    <option value="rectangular_prism">Rectangular Prism</option>
                                    <option value="cylinder">Cylinder</option>
                                    <option value="sphere">Sphere</option>
                                    <option value="triangle">Triangle</option>
                                    <option value="rectangle">Rectangle</option>
                                    <option value="circle">Circle</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Visual Feedback Overlay Demo */}
                <div className="bg-white rounded-lg border p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4">Visual Feedback Preview</h3>
                    <div className="relative bg-gray-100 rounded-lg p-8 min-h-[300px]">
                        <VisualFeedbackOverlay
                            diagramData={null}
                            shapeType={currentShape}
                            dimensions={currentDimensions}
                            calculations={{
                                volume: 27,
                                surface_area: 54,
                                area: 9
                            }}
                            showMeasurements={showVisualFeedback}
                            showFormulas={showFormulas}
                            showHints={showHints}
                            onToggleHint={handleToggleHint}
                            hintText={hintText}
                        />
                        <div className="text-center text-gray-500 mt-8">
                            <p>Interactive diagram will appear here</p>
                            <p className="text-sm">Adjust parameters above to see real-time changes</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    // Construction Guide Rendering
    const renderConstructionGuide = () => {
        const [selectedShape, setSelectedShape] = useState('triangle');
        const [guideDimensions, setGuideDimensions] = useState({
            base: 8,
            height: 6,
            side_length: 4,
            length: 6,
            width: 4,
            radius: 3
        });

        const handleStepComplete = (stepId, stepData) => {
            console.log(`Step ${stepId} completed:`, stepData);
        };

        return (
            <div className="space-y-6">
                <div className="bg-white rounded-lg border p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4 flex items-center">
                        <Construction className="w-6 h-6 mr-2" />
                        Step-by-Step Construction Guide
                    </h3>
                    
                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        {/* Shape Selection */}
                        <div className="space-y-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Select Shape to Construct
                                </label>
                                <select
                                    value={selectedShape}
                                    onChange={(e) => setSelectedShape(e.target.value)}
                                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                >
                                    <option value="triangle">Triangle</option>
                                    <option value="rectangle">Rectangle</option>
                                    <option value="circle">Circle</option>
                                    <option value="cube">3D Cube</option>
                                    <option value="cylinder">3D Cylinder</option>
                                </select>
                            </div>

                            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                                <h4 className="font-medium text-blue-800 mb-2">Construction Tools</h4>
                                <div className="space-y-2 text-sm text-blue-700">
                                    <div className="flex items-center">
                                        <span className="mr-2">📏</span>
                                        Ruler - for straight lines
                                    </div>
                                    <div className="flex items-center">
                                        <span className="mr-2">🧭</span>
                                        Compass - for circles
                                    </div>
                                    <div className="flex items-center">
                                        <span className="mr-2">📐</span>
                                        Protractor - for angles
                                    </div>
                                    <div className="flex items-center">
                                        <span className="mr-2">✏️</span>
                                        Pencil - for marking
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Construction Guide */}
                        <div className="lg:col-span-2">
                            <ConstructionGuide
                                shapeType={selectedShape}
                                dimensions={guideDimensions}
                                onStepComplete={handleStepComplete}
                                autoPlay={false}
                                speed={1}
                            />
                        </div>
                    </div>
                </div>
            </div>
        );
    };
};

export default GeometryStudio;