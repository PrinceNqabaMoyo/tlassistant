import React, { useState, useEffect } from 'react';
import VisualAidFactory from './VisualAidFactory';
import VisualAidSerializer from './VisualAidSerializer';

/**
 * AI Question Generator Component
 * Generates questions with embedded visual aids that can be instantiated by AI
 * Now centralized to work with all subject types
 */
const AIQuestionGenerator = ({ 
    questionSpecification, 
    onQuestionComplete,
    mode = 'ai-generated' // 'ai-generated' | 'user-interactive'
}) => {
    const [currentQuestion, setCurrentQuestion] = useState(null);
    const [visualAidData, setVisualAidData] = useState(null);
    const [userAnswer, setUserAnswer] = useState('');
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [serializedResponse, setSerializedResponse] = useState(null);

    // Parse question specification (JSON or POML)
    const parseQuestionSpec = (spec) => {
        if (typeof spec === 'string') {
            try {
                return JSON.parse(spec);
            } catch {
                return parsePOML(spec);
            }
        }
        return spec;
    };

    // Parse POML format for questions
    const parsePOML = (pomlString) => {
        const lines = pomlString.trim().split('\n');
        const result = {};
        let currentSection = null;
        
        lines.forEach(line => {
            const trimmed = line.trim();
            if (!trimmed || trimmed.startsWith('#')) return;
            
            if (trimmed.startsWith('[') && trimmed.endsWith(']')) {
                currentSection = trimmed.slice(1, -1);
                result[currentSection] = {};
            } else if (currentSection && trimmed.includes('=')) {
                const [key, value] = trimmed.split('=').map(s => s.trim());
                result[currentSection][key] = parseValue(value);
            } else if (trimmed.includes('=')) {
                const [key, value] = trimmed.split('=').map(s => s.trim());
                result[key] = parseValue(value);
            }
        });
        
        return result;
    };

    const parseValue = (value) => {
        if (value === 'true') return true;
        if (value === 'false') return false;
        if (value === 'null') return null;
        if (!isNaN(value) && value !== '') return parseFloat(value);
        if (value.startsWith('[') && value.endsWith(']')) {
            return value.slice(1, -1).split(',').map(v => parseValue(v.trim()));
        }
        if (value.startsWith('"') && value.endsWith('"')) {
            return value.slice(1, -1);
        }
        return value;
    };

    // Initialize question when specification changes
    useEffect(() => {
        if (questionSpecification) {
            const parsed = parseQuestionSpec(questionSpecification);
            setCurrentQuestion(parsed);
            setVisualAidData(null);
            setUserAnswer('');
            setIsSubmitted(false);
        }
    }, [questionSpecification]);

    // Handle visual aid changes
    const handleVisualAidChange = (data) => {
        setVisualAidData(data);
    };

    // Handle serialization of response
    const handleSerialize = (serialized) => {
        setSerializedResponse(serialized);
        
        // Prepare complete response for AI
        const completeResponse = {
            question: currentQuestion,
            user_answer: userAnswer,
            visual_aid_response: serialized,
            timestamp: new Date().toISOString()
        };

        if (onQuestionComplete) {
            onQuestionComplete(completeResponse);
        }
    };

    // Generate visual aid from question specification
    const generateVisualAid = () => {
        if (!currentQuestion?.visual_aid) return null;
        
        try {
            return VisualAidFactory.createVisualAid(
                currentQuestion.visual_aid,
                {},
                mode,
                handleVisualAidChange
            );
        } catch (error) {
            console.error('Error generating visual aid:', error);
            return null;
        }
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        setIsSubmitted(true);
        
        // Trigger serialization
        if (visualAidData && currentQuestion?.visual_aid?.type) {
            // The VisualAidSerializer will handle this automatically
            // via the onSerialize callback
        }
    };

    // Get available visual aid types for reference
    const availableTypes = VisualAidFactory.getAvailableTypes();

    return (
        <div className="ai-question-generator bg-white border border-gray-200 rounded-lg p-6">
            <div className="mb-6">
                <h2 className="text-2xl font-bold text-gray-800 mb-2">
                    AI Question Generator
                </h2>
                <p className="text-gray-600">
                    Generate interactive questions with visual aids for all subjects
                </p>
            </div>

            {/* Question Display */}
            {currentQuestion && (
                <div className="mb-6">
                    <div className="bg-blue-50 p-4 rounded-lg mb-4">
                        <h3 className="text-lg font-semibold text-blue-800 mb-2">Question</h3>
                        <p className="text-blue-700">{currentQuestion.question || currentQuestion.text}</p>
                        {currentQuestion.subject && (
                            <p className="text-sm text-blue-600 mt-2">
                                <strong>Subject:</strong> {currentQuestion.subject}
                            </p>
                        )}
                        {currentQuestion.difficulty && (
                            <p className="text-sm text-blue-600">
                                <strong>Difficulty:</strong> {currentQuestion.difficulty}
                            </p>
                        )}
                    </div>

                    {/* Visual Aid Display */}
                    {currentQuestion.visual_aid && (
                        <div className="mb-4">
                            <h4 className="text-md font-semibold text-gray-700 mb-2">Visual Aid</h4>
                            <div className="border border-gray-200 rounded-lg p-4">
                                {generateVisualAid()}
                            </div>
                        </div>
                    )}

                    {/* Answer Input */}
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Your Answer
                            </label>
                            <textarea
                                value={userAnswer}
                                onChange={(e) => setUserAnswer(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                                rows="3"
                                placeholder="Enter your answer here..."
                                disabled={isSubmitted}
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={isSubmitted || !userAnswer.trim()}
                            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
                        >
                            {isSubmitted ? 'Submitted' : 'Submit Answer'}
                        </button>
                    </form>
                </div>
            )}

            {/* Serialization Display */}
            {serializedResponse && (
                <div className="mb-6">
                    <h3 className="text-lg font-semibold text-gray-700 mb-2">Serialized Response</h3>
                    <div className="space-y-4">
                        {serializedResponse.json && (
                            <div>
                                <h4 className="text-md font-medium text-gray-600 mb-2">JSON Format</h4>
                                <pre className="bg-gray-100 p-3 rounded text-sm overflow-x-auto">
                                    {JSON.stringify(serializedResponse.json, null, 2)}
                                </pre>
                            </div>
                        )}
                        {serializedResponse.poml && (
                            <div>
                                <h4 className="text-md font-medium text-gray-600 mb-2">POML Format</h4>
                                <pre className="bg-gray-100 p-3 rounded text-sm overflow-x-auto">
                                    {serializedResponse.poml}
                                </pre>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Available Visual Aid Types */}
            <div className="mb-6">
                <h3 className="text-lg font-semibold text-gray-700 mb-2">Available Visual Aid Types</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {Object.entries(availableTypes).map(([subject, types]) => (
                        <div key={subject} className="bg-gray-50 p-3 rounded">
                            <h4 className="font-medium text-gray-800 mb-2">{subject}</h4>
                            <div className="flex flex-wrap gap-1">
                                {types.map(type => (
                                    <span
                                        key={type}
                                        className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full"
                                    >
                                        {type.replace('-', ' ')}
                                    </span>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Serializer Component */}
            {visualAidData && currentQuestion?.visual_aid?.type && (
                <div className="border-t pt-6">
                    <VisualAidSerializer
                        visualAidData={visualAidData}
                        visualAidType={currentQuestion.visual_aid.type}
                        format="both"
                        onSerialize={handleSerialize}
                    />
                </div>
            )}

            {/* No Question State */}
            {!currentQuestion && (
                <div className="text-center text-gray-500 py-8">
                    <div className="text-4xl mb-4">🤖</div>
                    <div className="text-lg font-medium mb-2">No Question Loaded</div>
                    <div className="text-sm">
                        Provide a question specification to get started
                    </div>
                </div>
            )}
        </div>
    );
};

export default AIQuestionGenerator;
