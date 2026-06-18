/**
 * Contextual Math Assistant
 * 
 * Demonstrates how to integrate grade and term-aware visual aids
 * into your existing application flow
 */

import React, { useState, useEffect } from 'react';
import { Clock, GraduationCap, BookOpen, Target, Settings, ChevronDown, ChevronUp } from 'lucide-react';
import EnhancedMathComponentsRepository from './EnhancedMathComponentsRepository';
import { 
    getContextualVisualAids, 
    getAdaptiveConfiguration,
    getCurrentCurriculumTopics,
    TERM_STRUCTURE 
} from '../../utils/curriculumTermMapping';

const ContextualMathAssistant = ({ 
    selectedSubject, 
    selectedGrade, 
    onSelectComponent 
}) => {
    // State for term and context management
    const [currentTerm, setCurrentTerm] = useState(1);
    const [showAllTools, setShowAllTools] = useState(false);
    const [contextMode, setContextMode] = useState('smart'); // 'smart' | 'manual' | 'all'
    const [showContextPanel, setShowContextPanel] = useState(true);
    const [isVisualAidsOpen, setIsVisualAidsOpen] = useState(false);

    // Auto-detect current term based on date (South African school calendar)
    useEffect(() => {
        const now = new Date();
        const month = now.getMonth() + 1; // 1-12
        
        // South African school year approximate terms:
        // Term 1: Jan-Mar, Term 2: Apr-Jun, Term 3: Jul-Sep, Term 4: Oct-Dec
        if (month >= 1 && month <= 3) setCurrentTerm(1);
        else if (month >= 4 && month <= 6) setCurrentTerm(2);
        else if (month >= 7 && month <= 9) setCurrentTerm(3);
        else setCurrentTerm(4);
    }, []);

    // Get contextual information
    const contextualAids = selectedSubject && selectedGrade 
        ? getContextualVisualAids(selectedSubject.name, parseInt(selectedGrade), currentTerm)
        : [];
    
    const currentTopics = selectedSubject && selectedGrade
        ? getCurrentCurriculumTopics(selectedSubject.name, parseInt(selectedGrade), currentTerm)
        : [];

    // Context panel component
    const ContextPanel = () => (
        <div className="mb-6 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-xl p-4">
            <div className="flex items-center justify-between mb-3">
                <div className="flex items-center space-x-2">
                    <GraduationCap className="h-5 w-5 text-blue-600" />
                    <h3 className="font-semibold text-blue-900">Learning Context</h3>
                </div>
                <button
                    onClick={() => setShowContextPanel(!showContextPanel)}
                    className="text-blue-600 hover:text-blue-800"
                >
                    {showContextPanel ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
                </button>
            </div>

            {showContextPanel && (
                <div className="space-y-4">
                    {/* Current Context Display */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="bg-white rounded-lg p-3 border border-blue-100">
                            <div className="flex items-center space-x-2 mb-2">
                                <BookOpen className="h-4 w-4 text-blue-500" />
                                <span className="text-sm font-medium text-gray-700">Subject & Grade</span>
                            </div>
                            <p className="text-blue-900 font-semibold">
                                {selectedSubject?.name || 'Not Selected'} - Grade {selectedGrade || 'N/A'}
                            </p>
                        </div>

                        <div className="bg-white rounded-lg p-3 border border-blue-100">
                            <div className="flex items-center space-x-2 mb-2">
                                <Clock className="h-4 w-4 text-blue-500" />
                                <span className="text-sm font-medium text-gray-700">Current Term</span>
                            </div>
                            <div className="flex items-center space-x-2">
                                <select
                                    value={currentTerm}
                                    onChange={(e) => setCurrentTerm(parseInt(e.target.value))}
                                    className="text-blue-900 font-semibold bg-transparent border-none outline-none"
                                >
                                    {Object.entries(TERM_STRUCTURE).map(([term, info]) => (
                                        <option key={term} value={term}>
                                            {info.name}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>

                        <div className="bg-white rounded-lg p-3 border border-blue-100">
                            <div className="flex items-center space-x-2 mb-2">
                                <Target className="h-4 w-4 text-blue-500" />
                                <span className="text-sm font-medium text-gray-700">Available Tools</span>
                            </div>
                            <p className="text-blue-900 font-semibold">
                                {contextualAids.length} Contextual Tools
                            </p>
                        </div>
                    </div>

                    {/* Current Topics */}
                    {currentTopics.length > 0 && (
                        <div className="bg-white rounded-lg p-3 border border-blue-100">
                            <h4 className="text-sm font-medium text-gray-700 mb-2">Current Curriculum Topics:</h4>
                            <div className="flex flex-wrap gap-2">
                                {currentTopics.slice(0, 6).map((topic, index) => (
                                    <span key={index} className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full">
                                        {topic}
                                    </span>
                                ))}
                                {currentTopics.length > 6 && (
                                    <span className="text-xs text-blue-600">
                                        +{currentTopics.length - 6} more
                                    </span>
                                )}
                            </div>
                        </div>
                    )}

                    {/* Context Mode Controls */}
                    <div className="bg-white rounded-lg p-3 border border-blue-100">
                        <h4 className="text-sm font-medium text-gray-700 mb-2">Tool Display Mode:</h4>
                        <div className="flex items-center space-x-4">
                            <label className="flex items-center space-x-2">
                                <input
                                    type="radio"
                                    name="contextMode"
                                    value="smart"
                                    checked={contextMode === 'smart'}
                                    onChange={(e) => setContextMode(e.target.value)}
                                    className="text-blue-600"
                                />
                                <span className="text-sm text-gray-700">Smart (Curriculum-Aware)</span>
                            </label>
                            <label className="flex items-center space-x-2">
                                <input
                                    type="radio"
                                    name="contextMode"
                                    value="manual"
                                    checked={contextMode === 'manual'}
                                    onChange={(e) => setContextMode(e.target.value)}
                                    className="text-blue-600"
                                />
                                <span className="text-sm text-gray-700">Manual Selection</span>
                            </label>
                            <label className="flex items-center space-x-2">
                                <input
                                    type="radio"
                                    name="contextMode"
                                    value="all"
                                    checked={contextMode === 'all'}
                                    onChange={(e) => setContextMode(e.target.value)}
                                    className="text-blue-600"
                                />
                                <span className="text-sm text-gray-700">Show All Tools</span>
                            </label>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );

    // Contextual recommendations
    const ContextualRecommendations = () => {
        if (!selectedSubject || !selectedGrade || contextualAids.length === 0) {
            return null;
        }

        return (
            <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
                <h4 className="font-medium text-green-800 mb-2 flex items-center">
                    <Target className="h-4 w-4 mr-2" />
                    Recommended for {TERM_STRUCTURE[currentTerm].name}
                </h4>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                    {contextualAids.slice(0, 6).map((aid) => {
                        const config = getAdaptiveConfiguration(aid.id, selectedSubject.name, parseInt(selectedGrade), currentTerm);
                        return (
                            <div key={aid.id} className="bg-white p-3 rounded-lg border border-green-100">
                                <h5 className="font-medium text-gray-800 text-sm">
                                    {config?.title || aid.id.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                                </h5>
                                {config?.focusAreas && (
                                    <p className="text-xs text-green-600 mt-1">
                                        Focus: {config.focusAreas.slice(0, 2).join(', ')}
                                    </p>
                                )}
                                <div className="flex items-center justify-between mt-2">
                                    <span className="text-xs text-green-700 bg-green-100 px-2 py-1 rounded">
                                        {aid.relevance} relevance
                                    </span>
                                    <button
                                        onClick={() => setIsVisualAidsOpen(true)}
                                        className="text-xs text-blue-600 hover:text-blue-800"
                                    >
                                        Open →
                                    </button>
                                </div>
                            </div>
                        );
                    })}
                </div>
                
                {contextualAids.length === 0 && contextMode === 'smart' && (
                    <div className="text-center py-4">
                        <p className="text-green-700 mb-2">No specific tools recommended for current term.</p>
                        <button
                            onClick={() => setContextMode('all')}
                            className="text-blue-600 hover:text-blue-800 text-sm underline"
                        >
                            View all available tools
                        </button>
                    </div>
                )}
            </div>
        );
    };

    return (
        <div className="space-y-4">
            <ContextPanel />
            
            {selectedSubject && selectedGrade && (
                <>
                    <ContextualRecommendations />
                    
                    {/* Visual Aids Access Button */}
                    <div className="text-center">
                        <button
                            onClick={() => setIsVisualAidsOpen(true)}
                            className="inline-flex items-center space-x-2 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                        >
                            <Settings className="h-5 w-5" />
                            <span>Open Visual Aid Tools</span>
                            {contextualAids.length > 0 && (
                                <span className="bg-blue-500 text-white text-xs px-2 py-1 rounded-full">
                                    {contextualAids.length}
                                </span>
                            )}
                        </button>
                    </div>
                </>
            )}

            {/* Enhanced Math Components Repository */}
            <EnhancedMathComponentsRepository
                isVisible={isVisualAidsOpen}
                onSelectComponent={(component) => {
                    setIsVisualAidsOpen(false);
                    onSelectComponent(component);
                }}
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
                currentTerm={currentTerm}
                showAllTools={contextMode === 'all'}
            />

            {/* Context Help */}
            {!selectedSubject || !selectedGrade ? (
                <div className="text-center py-8 text-gray-500">
                    <GraduationCap className="h-12 w-12 mx-auto mb-4 text-gray-300" />
                    <h3 className="text-lg font-medium mb-2">Select Subject and Grade</h3>
                    <p className="text-sm">
                        Choose a subject and grade level to see contextual visual aid tools
                        that align with your current curriculum.
                    </p>
                </div>
            ) : null}
        </div>
    );
};

export default ContextualMathAssistant;