/**
 * Enhanced MathComponentsRepository with Grade and Term Awareness
 * 
 * This enhancement makes visual aid tools contextually adaptive to:
 * - Current grade level
 * - Current term (1-4)
 * - Current curriculum topics being studied
 * - Student's learning progression
 */

import React, { useState, useEffect, useMemo } from 'react';
import { X, FunctionSquare, Ruler, Calculator, BarChart3, PieChart, LineChart, Square, Circle, Triangle, Compass, Settings, RulerIcon, Sigma, ArrowRight, Grid, BookOpen, Target, Zap, Bell, Box, Clock, GraduationCap, Filter, BookmarkIcon } from 'lucide-react';
import VisualToolOverlay from '../workspace/VisualToolOverlay';

// Import curriculum term mapping
import { curriculumData } from '../../curriculumData';

// Enhanced component metadata with term and curriculum alignment
const enhancedMathComponents = [
    {
        id: 'number_line',
        name: 'Number Line',
        description: 'Interactive number line for visualizing numbers and operations',
        icon: Ruler,
        category: 'Number Systems',
        gradeLevel: '7-9',
        subjects: ['Mathematics', 'Technical Mathematics', 'Mathematical Literacy'],
        
        // NEW: Term and curriculum alignment
        termAlignment: {
            7: [1, 2], // Grade 7: Terms 1 and 2
            8: [1, 2], // Grade 8: Terms 1 and 2  
            9: [1]     // Grade 9: Term 1 only
        },
        curriculumTopics: {
            7: ['Integers', 'Working with whole numbers', 'Fractions'],
            8: ['Integers', 'Whole numbers', 'Common fractions'],
            9: ['Integers', 'Fractions']
        },
        
        // NEW: Adaptive configurations based on grade/term
        adaptiveConfigs: {
            'grade_7_term_1': {
                title: "Number Line - Whole Numbers",
                start: 0,
                end: 20,
                showIntegers: true,
                showFractions: false,
                showDecimals: false,
                showOperations: true,
                focusAreas: ['positive integers', 'counting', 'ordering']
            },
            'grade_7_term_2': {
                title: "Number Line - Integers",
                start: -10,
                end: 10,
                showIntegers: true,
                showFractions: false,
                showDecimals: false,
                showOperations: true,
                focusAreas: ['negative numbers', 'integer operations']
            },
            'grade_8_term_1': {
                title: "Number Line - Integers & Fractions",
                start: -5,
                end: 5,
                showIntegers: true,
                showFractions: true,
                showDecimals: false,
                showOperations: true,
                focusAreas: ['integer operations', 'fraction placement']
            },
            'grade_9_term_1': {
                title: "Number Line - Advanced Operations",
                start: -10,
                end: 10,
                showIntegers: true,
                showFractions: true,
                showDecimals: true,
                showOperations: true,
                focusAreas: ['mixed operations', 'decimal placement']
            }
        },
        
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
        id: 'quadratic_function',
        name: 'Quadratic Function Graph',
        description: 'Interactive quadratic function visualization',
        icon: FunctionSquare,
        category: 'Functions & Graphs',
        gradeLevel: '10-12',
        subjects: ['Mathematics', 'Technical Mathematics'],
        
        // Term alignment for quadratic functions
        termAlignment: {
            10: [2, 3], // Grade 10: Terms 2 and 3
            11: [1, 2], // Grade 11: Terms 1 and 2
            12: [1, 2]  // Grade 12: Terms 1 and 2
        },
        curriculumTopics: {
            10: ['Functions', 'Analytical geometry'],
            11: ['Functions', 'Analytical geometry'],
            12: ['Functions', 'Polynomials']
        },
        
        adaptiveConfigs: {
            'grade_10_term_2': {
                title: "Quadratic Functions - Introduction",
                a: 1,
                b: 0,
                c: 0,
                showVertex: true,
                showAxis: true,
                showRoots: false,
                showTable: true,
                xMin: -5,
                xMax: 5,
                yMin: -5,
                yMax: 10,
                focusAreas: ['parabola shape', 'vertex form', 'basic transformations'],
                examples: ['y = x²', 'y = 2x²', 'y = x² + 3']
            },
            'grade_10_term_3': {
                title: "Quadratic Functions - Transformations",
                a: 1,
                b: 0,
                c: -4,
                showVertex: true,
                showAxis: true,
                showRoots: true,
                showTable: true,
                xMin: -5,
                xMax: 5,
                yMin: -10,
                yMax: 5,
                focusAreas: ['vertical shifts', 'horizontal shifts', 'finding roots'],
                examples: ['y = x² - 4', 'y = (x-2)²', 'y = x² + 2x + 1']
            },
            'grade_11_term_1': {
                title: "Quadratic Functions - Advanced Analysis",
                a: 2,
                b: -4,
                c: -6,
                showVertex: true,
                showAxis: true,
                showRoots: true,
                showTable: true,
                showDiscriminant: true,
                xMin: -3,
                xMax: 5,
                yMin: -10,
                yMax: 5,
                focusAreas: ['completing the square', 'discriminant', 'nature of roots'],
                examples: ['y = 2x² - 4x - 6', 'y = -x² + 4x + 5']
            },
            'grade_12_term_1': {
                title: "Polynomial Functions - Quadratics",
                a: 1,
                b: -3,
                c: 2,
                showVertex: true,
                showAxis: true,
                showRoots: true,
                showTable: true,
                showDiscriminant: true,
                showDerivative: true,
                xMin: -2,
                xMax: 4,
                yMin: -5,
                yMax: 5,
                focusAreas: ['optimization', 'turning points', 'calculus applications'],
                examples: ['y = x² - 3x + 2', 'optimization problems']
            }
        },
        
        componentType: 'quadratic_function_data',
        initialData: {
            title: "Quadratic Function",
            a: 1,
            b: 0,
            c: -4,
            showVertex: true,
            showAxis: true,
            showRoots: true,
            xMin: -5,
            xMax: 5,
            yMin: -5,
            yMax: 5
        }
    },
    
    {
        id: 'trigonometric_function',
        name: 'Trigonometric Functions',
        description: 'Interactive trigonometric function graphing',
        icon: Circle,
        category: 'Trigonometry',
        gradeLevel: '10-12',
        subjects: ['Mathematics', 'Technical Mathematics'],
        
        termAlignment: {
            10: [4], // Grade 10: Term 4
            11: [3, 4], // Grade 11: Terms 3 and 4
            12: [3] // Grade 12: Term 3
        },
        curriculumTopics: {
            10: ['Trigonometry'],
            11: ['Trigonometry'],
            12: ['Trigonometry']
        },
        
        adaptiveConfigs: {
            'grade_10_term_4': {
                title: "Trigonometry - Basic Functions",
                function: 'sin',
                amplitude: 1,
                period: 2 * Math.PI,
                phase: 0,
                vertical: 0,
                showUnitCircle: true,
                showSpecialAngles: true,
                angleMode: 'degrees',
                xMin: 0,
                xMax: 360,
                focusAreas: ['sine ratio', 'special angles', 'unit circle'],
                examples: ['sin(30°)', 'sin(45°)', 'sin(60°)']
            },
            'grade_11_term_3': {
                title: "Trig Functions - Graphs",
                function: 'sin',
                amplitude: 2,
                period: Math.PI,
                phase: 0,
                vertical: 0,
                showUnitCircle: false,
                showSpecialAngles: false,
                angleMode: 'radians',
                xMin: 0,
                xMax: 4 * Math.PI,
                focusAreas: ['function graphs', 'amplitude', 'period'],
                examples: ['y = 2sin(x)', 'y = sin(2x)', 'y = sin(x) + 1']
            },
            'grade_12_term_3': {
                title: "Trig Functions - Advanced",
                function: 'sin',
                amplitude: 1,
                period: 2 * Math.PI,
                phase: Math.PI/4,
                vertical: 2,
                showUnitCircle: false,
                showSpecialAngles: false,
                angleMode: 'radians',
                showDerivative: true,
                xMin: 0,
                xMax: 4 * Math.PI,
                focusAreas: ['transformations', 'composite functions', 'derivatives'],
                examples: ['y = sin(x + π/4) + 2', 'compound angle identities']
            }
        },
        
        componentType: 'trigonometric_function_data',
        initialData: {
            title: "Trigonometric Function",
            function: 'sin',
            amplitude: 1,
            period: 2 * Math.PI,
            phase: 0,
            vertical: 0,
            xMin: 0,
            xMax: 4 * Math.PI
        }
    }
];

/**
 * Enhanced MathComponentsRepository with contextual awareness
 */
const EnhancedMathComponentsRepository = ({ 
    isVisible, 
    onSelectComponent, 
    selectedSubject, 
    selectedGrade,
    currentTerm = 1, // NEW: Current term (1-4)
    learnerProfile = null, // NEW: Individual learner context
    showAllTools = false // NEW: Toggle to show all tools vs contextual
}) => {
    const [selectedComponent, setSelectedComponent] = useState(null);
    const [componentData, setComponentData] = useState(null);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [aiMode, setAiMode] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);
    
    // NEW: Filtering and context state
    const [filterMode, setFilterMode] = useState('contextual'); // 'contextual' | 'all' | 'grade_only'
    const [selectedTermFilter, setSelectedTermFilter] = useState(currentTerm);

    // Get current curriculum topics for context
    const getCurrentTopics = useMemo(() => {
        if (!selectedSubject?.name || !selectedGrade) return [];
        
        const subjectKey = selectedSubject.name.replace(' ', '_').toLowerCase();
        const subjectData = curriculumData[subjectKey];
        
        if (subjectData && subjectData[selectedGrade]) {
            return subjectData[selectedGrade].topics || [];
        }
        
        return [];
    }, [selectedSubject, selectedGrade]);

    // Enhanced filtering logic
    const filteredComponents = useMemo(() => {
        if (!selectedSubject?.name || !selectedGrade) return enhancedMathComponents;
        
        const subjectName = selectedSubject.name;
        const grade = parseInt(selectedGrade);
        
        return enhancedMathComponents.filter(component => {
            // Basic subject and grade filtering
            const matchesSubject = component.subjects.includes(subjectName);
            const matchesGrade = component.gradeLevel.split('-').some(g => parseInt(g) === grade);
            
            if (!matchesSubject || !matchesGrade) return false;
            
            // If showing all tools, stop here
            if (showAllTools || filterMode === 'all') return true;
            
            // If grade-only filtering
            if (filterMode === 'grade_only') return true;
            
            // Contextual filtering (default)
            if (filterMode === 'contextual') {
                // Check term alignment
                const termAlignment = component.termAlignment?.[grade];
                if (termAlignment && !termAlignment.includes(selectedTermFilter)) {
                    return false;
                }
                
                // Check curriculum topic overlap
                const componentTopics = component.curriculumTopics?.[grade] || [];
                const currentTopics = getCurrentTopics;
                
                if (componentTopics.length > 0 && currentTopics.length > 0) {
                    const hasTopicOverlap = componentTopics.some(topic => 
                        currentTopics.some(currTopic => 
                            currTopic.toLowerCase().includes(topic.toLowerCase()) ||
                            topic.toLowerCase().includes(currTopic.toLowerCase())
                        )
                    );
                    
                    if (!hasTopicOverlap) return false;
                }
            }
            
            return true;
        });
    }, [selectedSubject, selectedGrade, filterMode, selectedTermFilter, showAllTools, getCurrentTopics]);

    // Get adaptive configuration for selected component
    const getAdaptiveConfig = (component) => {
        if (!component || !selectedGrade || !currentTerm) return component.initialData;
        
        const configKey = `grade_${selectedGrade}_term_${currentTerm}`;
        const adaptiveConfig = component.adaptiveConfigs?.[configKey];
        
        if (adaptiveConfig) {
            return { ...component.initialData, ...adaptiveConfig };
        }
        
        return component.initialData;
    };

    // Enhanced component selection with adaptive configuration
    const handleComponentSelect = (component) => {
        setSelectedComponent(component);
        const adaptiveData = getAdaptiveConfig(component);
        setComponentData(adaptiveData);
        setIsSubmitted(false);
        setAiMode(false);
    };

    // Group components by category
    const groupedComponents = filteredComponents.reduce((acc, component) => {
        if (!acc[component.category]) {
            acc[component.category] = [];
        }
        acc[component.category].push(component);
        return acc;
    }, {});

    const handleSendToWorkspace = () => {
        if (selectedComponent && componentData) {
            onSelectComponent({
                ...selectedComponent,
                data: componentData
            });
        }
    };

    // NEW: Context information component
    const ContextInfo = () => (
        <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
            <div className="flex items-center space-x-2 mb-2">
                <GraduationCap className="h-4 w-4 text-blue-600" />
                <span className="text-sm font-medium text-blue-800">
                    Current Context: Grade {selectedGrade} {selectedSubject?.name} - Term {selectedTermFilter}
                </span>
            </div>
            
            <div className="flex items-center space-x-4 text-xs text-blue-600">
                <button
                    onClick={() => setFilterMode(filterMode === 'contextual' ? 'all' : 'contextual')}
                    className="flex items-center space-x-1 hover:text-blue-800"
                >
                    <Filter className="h-3 w-3" />
                    <span>{filterMode === 'contextual' ? 'Show All Tools' : 'Show Contextual Tools'}</span>
                </button>
                
                <select
                    value={selectedTermFilter}
                    onChange={(e) => setSelectedTermFilter(parseInt(e.target.value))}
                    className="text-xs border border-blue-300 rounded px-2 py-1"
                >
                    <option value={1}>Term 1</option>
                    <option value={2}>Term 2</option>
                    <option value={3}>Term 3</option>
                    <option value={4}>Term 4</option>
                </select>
            </div>
            
            {filteredComponents.length === 0 && (
                <div className="mt-2 text-xs text-orange-600">
                    No tools available for current context. <button onClick={() => setFilterMode('all')} className="underline">Show all tools</button>
                </div>
            )}
        </div>
    );

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
                        <ContextInfo />
                        
                        {Object.entries(groupedComponents).map(([category, components]) => (
                            <div key={category} className="space-y-2">
                                <h3 className="text-sm font-semibold text-gray-800 border-b border-gray-200 pb-1">
                                    {category}
                                </h3>
                                <div className="grid grid-cols-1 gap-2">
                                    {components.map((component) => {
                                        const Icon = component.icon;
                                        const isContextual = component.termAlignment?.[parseInt(selectedGrade)]?.includes(selectedTermFilter);
                                        const adaptiveConfig = getAdaptiveConfig(component);
                                        
                                        return (
                                            <div
                                                key={component.id}
                                                onClick={() => handleComponentSelect(component)}
                                                className={`flex items-center space-x-3 p-3 border rounded-lg cursor-pointer transition-all duration-200 ${
                                                    isContextual 
                                                        ? 'border-blue-300 bg-blue-50 hover:border-blue-400 hover:shadow-md' 
                                                        : 'border-gray-200 hover:border-blue-300 hover:shadow-md'
                                                }`}
                                            >
                                                <Icon className={`h-5 w-5 ${isContextual ? 'text-blue-600' : 'text-gray-600'}`} />
                                                <div className="flex-1">
                                                    <h4 className="text-sm font-medium text-gray-800">
                                                        {adaptiveConfig.title || component.name}
                                                    </h4>
                                                    <p className="text-xs text-gray-600">{component.description}</p>
                                                    <div className="flex items-center space-x-2 mt-1">
                                                        <span className="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">
                                                            Grade {component.gradeLevel}
                                                        </span>
                                                        {isContextual && (
                                                            <span className="text-xs bg-blue-100 text-blue-600 px-2 py-1 rounded">
                                                                Current Term
                                                            </span>
                                                        )}
                                                        {adaptiveConfig.focusAreas && (
                                                            <span className="text-xs bg-green-100 text-green-600 px-2 py-1 rounded">
                                                                Adaptive
                                                            </span>
                                                        )}
                                                    </div>
                                                    {adaptiveConfig.focusAreas && (
                                                        <div className="mt-1">
                                                            <p className="text-xs text-blue-600">
                                                                Focus: {adaptiveConfig.focusAreas.join(', ')}
                                                            </p>
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        ))}
                        
                        {Object.keys(groupedComponents).length === 0 && (
                            <div className="text-center py-8 text-gray-500">
                                <BookmarkIcon className="h-12 w-12 mx-auto mb-4 text-gray-300" />
                                <h3 className="text-lg font-medium mb-2">No tools available</h3>
                                <p className="text-sm">
                                    No visual aid tools are available for the current context.
                                </p>
                                <button
                                    onClick={() => setFilterMode('all')}
                                    className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                                >
                                    Show All Available Tools
                                </button>
                            </div>
                        )}
                    </div>
                ) : (
                    // Component configuration view with enhanced adaptive features
                    <div className="space-y-4">
                        <div className="flex items-center justify-between">
                            <div>
                                <h3 className="text-lg font-semibold text-gray-800">{componentData.title}</h3>
                                <p className="text-sm text-gray-600">{selectedComponent.description}</p>
                                {componentData.focusAreas && (
                                    <div className="mt-2">
                                        <h4 className="text-xs font-medium text-blue-800 mb-1">Learning Focus:</h4>
                                        <div className="flex flex-wrap gap-1">
                                            {componentData.focusAreas.map((area, index) => (
                                                <span key={index} className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded">
                                                    {area}
                                                </span>
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>
                            <button
                                onClick={() => setSelectedComponent(null)}
                                className="text-gray-500 hover:text-gray-700"
                            >
                                <X className="h-6 w-6" />
                            </button>
                        </div>
                        
                        {componentData.examples && (
                            <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                                <h4 className="text-sm font-medium text-yellow-800 mb-2">Curriculum Examples:</h4>
                                <div className="text-xs text-yellow-700">
                                    {componentData.examples.join(' • ')}
                                </div>
                            </div>
                        )}
                        
                        {/* Rest of component configuration UI would go here */}
                        {/* This would include the parameter inputs specific to each component type */}
                        
                    </div>
                )}
            </div>
        </VisualToolOverlay>
    );
};

export default EnhancedMathComponentsRepository;