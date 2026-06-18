import React, { useState, useEffect } from 'react';
import { Bot, Send, RefreshCw } from 'lucide-react';

/**
 * AI Math Assistant Component
 * 
 * This component handles AI integration for mathematical expressions,
 * including processing AI input, managing step canvas, and providing
 * AI interface functionality.
 */

const AiMathAssistant = ({ 
    aiInputText, 
    setAiInputText, 
    isSubmitted, 
    isProcessingAi, 
    setIsProcessingAi,
    exprData,
    setExprData,
    processOperation,
    analyzeExpression
}) => {
    const [stepCanvasRef] = useState(React.useRef(null));

    // Handle AI-provided input (expression, operation, instructions)
    const processAiInput = (aiPayload) => {
        try {
            if (!aiPayload || typeof aiPayload !== 'object') return;
            const { expression, operation, instructions } = aiPayload;

            const operationMap = {
                simplify: 'simplify',
                factor: 'factor',
                expand: 'expand',
                solve: 'solve',
                complete_square: 'complete_square',
                long_division: 'long_division',
                cubic_solve: 'cubic_solve',
                simultaneous: 'simultaneous',
                inequalities: 'inequalities',
                quadratic_analysis: 'quadratic_analysis',
                logarithmic_solve: 'logarithmic_solve',
                logarithmic: 'logarithmic_solve',
                complex_operations: 'complex_operations',
                complex: 'complex_operations'
            };

            const mappedOperation = operationMap[operation] || exprData.targetOperation || 'simplify';

            // Update core fields
            setExprData(prev => ({
                ...prev,
                aiMode: true,
                aiInstructions: instructions ?? prev.aiInstructions,
                expression: expression ?? prev.expression,
                targetOperation: mappedOperation
            }));

            // Convert instructions to steps on the canvas if available
            if (instructions && typeof instructions === 'string') {
                const stepsFromAi = convertParagraphToSteps(instructions);
                if (stepsFromAi.length > 0) {
                    setExprData(prev => ({
                        ...prev,
                        stepCanvas: stepsFromAi,
                        currentStep: 0
                    }));
                }
            }

            // Trigger analysis and the selected operation on the next tick
            if (expression && typeof expression === 'string' && expression.trim().length > 0) {
                try {
                    analyzeExpression(expression);
                } catch {}
                setTimeout(() => {
                    try { processOperation(); } catch {}
                }, 0);
            }
        } catch (err) {
            console.error('Error in processAiInput:', err);
        }
    };

    // Convert paragraph text to structured steps
    const convertParagraphToSteps = (paragraphText) => {
        if (!paragraphText || typeof paragraphText !== 'string') return [];
        
        try {
            // Split by sentences and create steps
            const sentences = paragraphText.split(/[.!?]+/).filter(s => s.trim().length > 0);
            return sentences.map((sentence, index) => ({
                step: index + 1,
                description: sentence.trim(),
                expression: "",
                explanation: sentence.trim(),
                lineBreaks: sentence.trim().split(/[.!?]/).filter(s => s.trim().length > 0)
            }));
        } catch (error) {
            console.error('Error converting paragraph to steps:', error);
            return [];
        }
    };

    // Add a new step to the canvas
    const addStepToCanvas = (description, expression = "", explanation = "") => {
        const newStep = {
            step: exprData.stepCanvas.length + 1,
            description: description,
            expression: expression,
            explanation: explanation,
            lineBreaks: description ? description.split(/[.!?]/).filter(s => s.trim().length > 0) : [description]
        };
        
        setExprData(prev => ({
            ...prev,
            stepCanvas: [...prev.stepCanvas, newStep],
            currentStep: prev.stepCanvas.length
        }));
    };

    // Clear the step canvas
    const clearStepCanvas = () => {
        setExprData(prev => ({
            ...prev,
            stepCanvas: [],
            currentStep: 0
        }));
    };

    // AI Input Handler
    const handleAiInput = () => {
        if (!aiInputText.trim()) return;
        
        // Simulate AI input processing
        const mockAiData = {
            expression: aiInputText,
            operation: 'simplify',
            instructions: `Simplify the expression: ${aiInputText}`,
            steps: `First, identify the terms in the expression. Then, combine like terms. Finally, write the simplified result.`
        };
        
        processAiInput(mockAiData);
        setAiInputText("");
    };

    // External AI Input Handler (for curriculum helper integration)
    const handleExternalAiInput = (aiData) => {
        if (aiData && typeof aiData === 'object') {
            processAiInput(aiData);
        }
    };

    // Expose function for external use
    useEffect(() => {
        if (window.algebraicExpressionBuilder) {
            window.algebraicExpressionBuilder = {
                ...window.algebraicExpressionBuilder,
                processAiInput: handleExternalAiInput
            };
        } else {
            window.algebraicExpressionBuilder = {
                processAiInput: handleExternalAiInput
            };
        }
    }, []);

    // Enhanced step rendering with dedicated canvas
    const renderStepCanvas = () => {
        if (!exprData.showSteps || exprData.stepCanvas.length === 0) return null;

        return (
            <div className="mb-6">
                <div className="flex items-center justify-between mb-3">
                    <h4 className="font-semibold text-gray-700">Step-by-Step Work Canvas:</h4>
                    <div className="flex space-x-2">
                        <button
                            onClick={clearStepCanvas}
                            className="px-3 py-1 text-xs bg-red-100 text-red-700 rounded hover:bg-red-200 transition-colors"
                            disabled={isSubmitted}
                        >
                            Clear Canvas
                        </button>
                        <button
                            onClick={() => addStepToCanvas("New step added manually")}
                            className="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded hover:bg-blue-200 transition-colors"
                            disabled={isSubmitted}
                        >
                            Add Step
                        </button>
                    </div>
                </div>
                
                {/* Paper-like canvas */}
                <div 
                    ref={stepCanvasRef}
                    className="bg-white border-2 border-gray-300 rounded-lg p-6 min-h-96 shadow-inner transition-all duration-300 hover:shadow-lg"
                    style={{
                        backgroundImage: 'linear-gradient(#f9f9f9 1px, transparent 1px)',
                        backgroundSize: '100% 24px',
                        fontFamily: 'monospace'
                    }}
                >
                    {exprData.stepCanvas.map((step, index) => (
                        <div 
                            key={index} 
                            className="mb-6 last:mb-0"
                        >
                            {/* Step number */}
                            <div className="flex items-center mb-2">
                                <div className="w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold mr-3 shadow-md">
                                    {step.step}
                                </div>
                                <span className="text-sm font-medium text-gray-600">Step {step.step}</span>
                            </div>
                            
                            {/* Step content with automatic line breaks */}
                            <div className="ml-11">
                                {/* Description with automatic line breaks */}
                                {step.lineBreaks.map((line, lineIndex) => (
                                    <div key={lineIndex} className="mb-2 leading-relaxed">
                                        <span className="text-gray-800">{line.trim()}</span>
                                        {lineIndex < step.lineBreaks.length - 1 && <span className="text-gray-400">.</span>}
                                    </div>
                                ))}
                                
                                {/* Expression if present */}
                                {step.expression && (
                                    <div className="mt-3 p-2 bg-blue-50 border border-blue-200 rounded text-sm font-mono text-blue-800">
                                        {step.expression}
                                    </div>
                                )}
                                
                                {/* Explanation if present */}
                                {step.explanation && step.explanation !== step.description && (
                                    <div className="mt-2 text-sm text-gray-600 italic">
                                        {step.explanation}
                                    </div>
                                )}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    // AI Input Interface
    const renderAiInterface = () => {
        return (
            <div className="mb-6 p-4 bg-gradient-to-r from-blue-50 to-purple-50 border border-blue-200 rounded-lg">
                <div className="flex items-center mb-3">
                    <Bot className="w-5 h-5 text-blue-600 mr-2" />
                    <h4 className="font-semibold text-blue-800">AI Integration</h4>
                </div>
                <div className="space-y-3">
                    <div>
                        <label className="block text-sm font-medium text-blue-700 mb-1">
                            AI Instructions or Expression:
                        </label>
                        <textarea
                            value={aiInputText}
                            onChange={(e) => setAiInputText(e.target.value)}
                            placeholder="Enter AI instructions, expressions, or step-by-step procedures..."
                            className="w-full p-3 border border-blue-300 rounded-md text-sm resize-none"
                            rows={3}
                            disabled={isSubmitted || isProcessingAi}
                        />
                    </div>
                    {/* AI Control Buttons */}
                    <div className="flex space-x-3">
                        <button
                            onClick={handleAiInput}
                            disabled={!aiInputText.trim() || isSubmitted || isProcessingAi}
                            className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400 transition-colors"
                        >
                            {isProcessingAi ? (
                                <RefreshCw className="w-4 h-4 mr-2 animate-spin" />
                            ) : (
                                <Send className="w-4 h-4 mr-2" />
                            )}
                            {isProcessingAi ? 'Processing...' : 'Process AI Input'}
                        </button>
                        <button
                            onClick={() => setAiInputText("")}
                            disabled={!aiInputText.trim() || isSubmitted}
                            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 disabled:bg-gray-50 transition-colors"
                        >
                            Clear
                        </button>
                        {/* Demo AI Input Button */}
                        <button
                            onClick={() => {
                                const demoAiData = {
                                    expression: "2x² + 3x + 1",
                                    operation: "factor",
                                    instructions: "Factor the quadratic expression step by step",
                                    steps: "First, check if the expression can be factored using the AC method. Then, find two numbers that multiply to give the product of the coefficient of x² and the constant term, and add to give the coefficient of x. Finally, rewrite the expression using these numbers and factor by grouping."
                                };
                                processAiInput(demoAiData);
                            }}
                            disabled={isSubmitted}
                            className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 disabled:bg-gray-400 transition-colors"
                        >
                            Demo AI Input
                        </button>
                    </div>
                    {exprData.aiMode && (
                        <div className="flex items-center text-sm text-blue-600">
                            <Bot className="w-4 h-4 mr-2" />
                            <span>AI Mode Active - Canvas populated with structured steps</span>
                        </div>
                    )}
                </div>
            </div>
        );
    };

    return (
        <>
            {renderAiInterface()}
            {renderStepCanvas()}
        </>
    );
};

export default AiMathAssistant;
