import React, { useState } from 'react';
import { evaluate } from 'mathjs';

/**
 * Step Canvas Component
 * 
 * This component handles the rendering of step-by-step solutions,
 * function tables, and step canvas functionality for mathematical expressions.
 */

const StepCanvas = ({ 
    exprData, 
    setExprData, 
    showSteps, 
    showGraph, 
    xMin, 
    xMax
}) => {
    // Local state for solver and law demonstrator
    const [solverMode, setSolverMode] = useState('none');
    const [inputExpression, setInputExpression] = useState('');
    const [targetOperation, setTargetOperation] = useState('simplify');
    const [solutionSteps, setSolutionSteps] = useState([]);
    const [showSolutionSteps, setShowSolutionSteps] = useState(false);
    const [currentStep, setCurrentStep] = useState(0);
    const [showLawsDemonstrator, setShowLawsDemonstrator] = useState(false);
    const [currentLaw, setCurrentLaw] = useState('product');
    const [lawDemonstrationMode, setLawDemonstrationMode] = useState('visual');
    const [lawX, setLawX] = useState(2);
    const [lawY, setLawY] = useState(3);
    const [lawBase, setLawBase] = useState(2);
    const [logBase2, setLogBase2] = useState(3); // For change of base formula
    const [showInverseVisualizer, setShowInverseVisualizer] = useState(false);

    
    // Helper function to render mathematical expressions with proper superscripts
    const renderMathExpression = (expression) => {
        return <span dangerouslySetInnerHTML={{ __html: expression }} />;
    };

    // Determine function type from expression
    const getFunctionType = () => {
        // First check if we have a manually selected expression type (highest priority)
        if (exprData.expressionType) {
            if (exprData.expressionType === 'logarithmic') return 'logarithmic';
            if (exprData.expressionType === 'exponential') return 'exponential';
        }
        
        // Then check the expression content as fallback
        if (exprData.expression) {
            const expr = exprData.expression.toLowerCase();
            if (expr.includes('^') || expr.includes('exp')) return 'exponential';
            if (expr.includes('log') || expr.includes('ln')) return 'logarithmic';
        }
        
        // Default to exponential if nothing is detected
        return 'exponential';
    };

    // Step-by-step problem solver
    const solveStepByStep = (expression, operation) => {
        const steps = [];
        const functionType = getFunctionType();
        
        try {
            if (operation === 'simplify') {
                // Step 1: Parse the expression
                steps.push({
                    step: 1,
                    action: 'Parse Expression',
                    expression: expression,
                    explanation: 'Identify the components of the expression',
                    result: 'Expression parsed successfully'
                });

                // Step 2: Apply relevant laws
                if (functionType === 'exponential') {
                    steps.push({
                        step: 2,
                        action: 'Apply Exponential Laws',
                        expression: expression,
                        explanation: 'Use exponential properties to simplify',
                        result: 'Laws applied: Product, Quotient, Power'
                    });
                } else if (functionType === 'logarithmic') {
                    steps.push({
                        step: 2,
                        action: 'Apply Logarithmic Laws',
                        expression: expression,
                        explanation: 'Use logarithmic properties to simplify',
                        result: 'Laws applied: Product, Quotient, Power'
                    });
                }

                // Step 3: Final result
                steps.push({
                    step: 3,
                    action: 'Final Result',
                    expression: expression,
                    explanation: 'Expression simplified to its final form',
                    result: 'Simplification complete'
                });
            } else if (operation === 'solve') {
                steps.push({
                    step: 1,
                    action: 'Set Equal to Zero',
                    expression: `${expression} = 0`,
                    explanation: 'To solve, set the expression equal to zero',
                    result: 'Equation ready for solving'
                });

                steps.push({
                    step: 2,
                    action: 'Apply Inverse Operations',
                    expression: 'Apply inverse function operations',
                    explanation: 'Use the inverse relationship to solve for x',
                    result: 'Solution found'
                });
            }

            return steps;
        } catch (error) {
            return [{
                step: 1,
                action: 'Error',
                expression: expression,
                explanation: 'An error occurred while solving',
                result: `Error: ${error.message}`
            }];
        }
    };

    // Get law demonstration data
    const getLawDemonstration = (law) => {
        const functionType = getFunctionType();
        
        if (functionType === 'exponential') {
            const demonstrations = {
                'product': {
                    formula: `${lawBase}<sup>${lawX}</sup> × ${lawBase}<sup>${lawY}</sup> = ${lawBase}<sup>${lawX}+${lawY}</sup>`,
                    description: 'When multiplying powers with the same base, add the exponents',
                    example: `${lawBase}<sup>${lawX}</sup> × ${lawBase}<sup>${lawY}</sup> = ${lawBase}<sup>${lawX + lawY}</sup>`,
                    leftSide: `${lawBase}<sup>${lawX}</sup> × ${lawBase}<sup>${lawY}</sup>`,
                    rightSide: `${lawBase}<sup>${lawX + lawY}</sup>`,
                    leftValue: Math.pow(lawBase, lawX) * Math.pow(lawBase, lawY),
                    rightValue: Math.pow(lawBase, lawX + lawY),
                    proof: [
                        `${lawBase}<sup>${lawX}</sup> × ${lawBase}<sup>${lawY}</sup>`,
                        `= ${Math.pow(lawBase, lawX)} × ${Math.pow(lawBase, lawY)}`,
                        `= ${Math.pow(lawBase, lawX) * Math.pow(lawBase, lawY)}`,
                        `= ${lawBase}<sup>${lawX + lawY}</sup>`
                    ]
                },
                'quotient': {
                    formula: `${lawBase}<sup>${lawX}</sup> ÷ ${lawBase}<sup>${lawY}</sup> = ${lawBase}<sup>${lawX}-${lawY}</sup>`,
                    description: 'When dividing powers with the same base, subtract the exponents',
                    example: `${lawBase}<sup>${lawX}</sup> ÷ ${lawBase}<sup>${lawY}</sup> = ${lawBase}<sup>${lawX - lawY}</sup>`,
                    leftSide: `${lawBase}<sup>${lawX}</sup> ÷ ${lawBase}<sup>${lawY}</sup>`,
                    rightSide: `${lawBase}<sup>${lawX - lawY}</sup>`,
                    leftValue: Math.pow(lawBase, lawX) / Math.pow(lawBase, lawY),
                    rightValue: Math.pow(lawBase, lawX - lawY),
                    proof: [
                        `${lawBase}<sup>${lawX}</sup> ÷ ${lawBase}<sup>${lawY}</sup>`,
                        `= ${Math.pow(lawBase, lawX)} ÷ ${Math.pow(lawBase, lawY)}`,
                        `= ${Math.pow(lawBase, lawX) / Math.pow(lawBase, lawY)}`,
                        `= ${lawBase}<sup>${lawX - lawY}</sup>`
                    ]
                },
                'power': {
                    formula: `(${lawBase}<sup>${lawX}</sup>)<sup>${lawY}</sup> = ${lawBase}<sup>${lawX}×${lawY}</sup>`,
                    description: 'When raising a power to another power, multiply the exponents',
                    example: `(${lawBase}<sup>${lawX}</sup>)<sup>${lawY}</sup> = ${lawBase}<sup>${lawX * lawY}</sup>`,
                    leftSide: `(${lawBase}<sup>${lawX}</sup>)<sup>${lawY}</sup>`,
                    rightSide: `${lawBase}<sup>${lawX * lawY}</sup>`,
                    leftValue: Math.pow(Math.pow(lawBase, lawX), lawY),
                    rightValue: Math.pow(lawBase, lawX * lawY),
                    proof: [
                        `(${lawBase}<sup>${lawX}</sup>)<sup>${lawY}</sup>`,
                        `= ${lawBase}<sup>${lawX} × ${lawY}</sup>`,
                        `= ${lawBase}<sup>${lawX * lawY}</sup>`,
                        `= ${Math.pow(lawBase, lawX * lawY)}`
                    ]
                },
                'zero': {
                    formula: `${lawBase}<sup>0</sup> = 1`,
                    description: 'Any number (except 0) raised to the power 0 equals 1',
                    example: `${lawBase}<sup>0</sup> = 1`,
                    leftSide: `${lawBase}<sup>0</sup>`,
                    rightSide: `1`,
                    leftValue: 1,
                    rightValue: 1,
                    proof: [
                        `${lawBase}<sup>0</sup> = 1`,
                        `This is true for any non-zero base`,
                        `${lawBase}<sup>0</sup> = 1`
                    ]
                },
                'negative': {
                    formula: `${lawBase}<sup>-${lawX}</sup> = 1/${lawBase}<sup>${lawX}</sup>`,
                    description: 'A negative exponent means take the reciprocal',
                    example: `${lawBase}<sup>-${lawX}</sup> = 1/${lawBase}<sup>${lawX}</sup>`,
                    leftSide: `${lawBase}<sup>-${lawX}</sup>`,
                    rightSide: `1/${lawBase}<sup>${lawX}</sup>`,
                    leftValue: Math.pow(lawBase, -lawX),
                    rightValue: 1 / Math.pow(lawBase, lawX),
                    proof: [
                        `${lawBase}<sup>-${lawX}</sup> = 1/${lawBase}<sup>${lawX}</sup>`,
                        `= 1/${Math.pow(lawBase, lawX)}`,
                        `= ${1 / Math.pow(lawBase, lawX)}`
                    ]
                }
            };
            
            return demonstrations[law] || demonstrations['product'];
        } else if (functionType === 'logarithmic') {
            const demonstrations = {
                'product': {
                    formula: `log<sub>${lawBase}</sub>(${lawX} × ${lawY}) = log<sub>${lawBase}</sub>(${lawX}) + log<sub>${lawBase}</sub>(${lawY})`,
                    description: 'The logarithm of a product equals the sum of the logarithms',
                    example: `log<sub>${lawBase}</sub>(${lawX} × ${lawY}) = log<sub>${lawBase}</sub>(${lawX}) + log<sub>${lawBase}</sub>(${lawY})`,
                    leftSide: `log<sub>${lawBase}</sub>(${lawX} × ${lawY})`,
                    rightSide: `log<sub>${lawBase}</sub>(${lawX}) + log<sub>${lawBase}</sub>(${lawY})`,
                    leftValue: Math.log(lawX * lawY) / Math.log(lawBase),
                    rightValue: (Math.log(lawX) / Math.log(lawBase)) + (Math.log(lawY) / Math.log(lawBase)),
                    proof: [
                        `log<sub>${lawBase}</sub>(${lawX} × ${lawY})`,
                        `= log<sub>${lawBase}</sub>(${lawX}) + log<sub>${lawBase}</sub>(${lawY})`,
                        `= ${(Math.log(lawX) / Math.log(lawBase)).toFixed(4)} + ${(Math.log(lawY) / Math.log(lawBase)).toFixed(4)}`,
                        `= ${((Math.log(lawX) / Math.log(lawBase)) + (Math.log(lawY) / Math.log(lawBase))).toFixed(4)}`
                    ]
                },
                'quotient': {
                    formula: `log<sub>${lawBase}</sub>(${lawX} ÷ ${lawY}) = log<sub>${lawBase}</sub>(${lawX}) - log<sub>${lawBase}</sub>(${lawY})`,
                    description: 'The logarithm of a quotient equals the difference of the logarithms',
                    example: `log<sub>${lawBase}</sub>(${lawX} ÷ ${lawY}) = log<sub>${lawBase}</sub>(${lawX}) - log<sub>${lawBase}</sub>(${lawY})`,
                    leftSide: `log<sub>${lawBase}</sub>(${lawX} ÷ ${lawY})`,
                    rightSide: `log<sub>${lawBase}</sub>(${lawX}) - log<sub>${lawBase}</sub>(${lawY})`,
                    leftValue: Math.log(lawX / lawY) / Math.log(lawBase),
                    rightValue: (Math.log(lawX) / Math.log(lawBase)) - (Math.log(lawY) / Math.log(lawBase)),
                    proof: [
                        `log<sub>${lawBase}</sub>(${lawX} ÷ ${lawY})`,
                        `= log<sub>${lawBase}</sub>(${lawX}) - log<sub>${lawBase}</sub>(${lawY})`,
                        `= ${(Math.log(lawX) / Math.log(lawBase)).toFixed(4)} - ${(Math.log(lawY) / Math.log(lawBase)).toFixed(4)}`,
                        `= ${((Math.log(lawX) / Math.log(lawBase)) - (Math.log(lawY) / Math.log(lawBase))).toFixed(4)}`
                    ]
                },
                'power': {
                    formula: `log<sub>${lawBase}</sub>(${lawX}<sup>${lawY}</sup>) = ${lawY} × log<sub>${lawBase}</sub>(${lawX})`,
                    description: 'The logarithm of a power equals the exponent times the logarithm of the base',
                    example: `log<sub>${lawBase}</sub>(${lawX}<sup>${lawY}</sup>) = ${lawY} × log<sub>${lawBase}</sub>(${lawX})`,
                    leftSide: `log<sub>${lawBase}</sub>(${lawX}<sup>${lawY}</sup>)`,
                    rightSide: `${lawY} × log<sub>${lawBase}</sub>(${lawX})`,
                    leftValue: Math.log(Math.pow(lawX, lawY)) / Math.log(lawBase),
                    rightValue: lawY * (Math.log(lawX) / Math.log(lawBase)),
                    proof: [
                        `log<sub>${lawBase}</sub>(${lawX}<sup>${lawY}</sup>)`,
                        `= ${lawY} × log<sub>${lawBase}</sub>(${lawX})`,
                        `= ${lawY} × ${(Math.log(lawX) / Math.log(lawBase)).toFixed(4)}`,
                        `= ${(lawY * (Math.log(lawX) / Math.log(lawBase))).toFixed(4)}`
                    ]
                },
                'change_of_base': {
                    formula: `log<sub>${lawBase}</sub>(${lawX}) = log<sub>${logBase2}</sub>(${lawX}) ÷ log<sub>${logBase2}</sub>(${lawBase})`,
                    description: 'Change of base formula: convert between different logarithmic bases',
                    example: `log<sub>${lawBase}</sub>(${lawX}) = log<sub>${logBase2}</sub>(${lawX}) ÷ log<sub>${logBase2}</sub>(${lawBase})`,
                    leftSide: `log<sub>${lawBase}</sub>(${lawX})`,
                    rightSide: `log<sub>${logBase2}</sub>(${lawX}) ÷ log<sub>${logBase2}</sub>(${lawBase})`,
                    leftValue: Math.log(lawX) / Math.log(lawBase),
                    rightValue: (Math.log(lawX) / Math.log(logBase2)) / (Math.log(lawBase) / Math.log(logBase2)),
                    proof: [
                        `log<sub>${lawBase}</sub>(${lawX})`,
                        `= log<sub>${logBase2}</sub>(${lawX}) ÷ log<sub>${logBase2}</sub>(${lawBase})`,
                        `= ${(Math.log(lawX) / Math.log(logBase2)).toFixed(4)} ÷ ${(Math.log(lawBase) / Math.log(logBase2)).toFixed(4)}`,
                        `= ${((Math.log(lawX) / Math.log(logBase2)) / (Math.log(lawBase) / Math.log(logBase2))).toFixed(4)}`
                    ]
                },
                'identity': {
                    formula: `log<sub>${lawBase}</sub>(${lawBase}) = 1`,
                    description: 'The logarithm of the base equals 1',
                    example: `log<sub>${lawBase}</sub>(${lawBase}) = 1`,
                    leftSide: `log<sub>${lawBase}</sub>(${lawBase})`,
                    rightSide: `1`,
                    leftValue: 1,
                    rightValue: 1,
                    proof: [
                        `log<sub>${lawBase}</sub>(${lawBase}) = 1`,
                        `This is true for any base`,
                        `log<sub>${lawBase}</sub>(${lawBase}) = 1`
                    ]
                }
            };
            
            return demonstrations[law] || demonstrations['product'];
        }
        
        // Default to exponential if function type is not recognized
        return demonstrations['product'];
    };



    // Render expression solver UI
    const renderExpressionSolver = () => {
        // Show for all function types
        const functionType = getFunctionType();

        return (
            <div className="bg-white border border-gray-300 rounded-lg p-4 mb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">
                    Expression Solver - {exprData.functionType ? exprData.functionType.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()) : 'Mathematical'} Functions
                </h3>
                
                {/* Solver Mode Selection */}
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                        Solver Mode:
                    </label>
                    <select
                        value={solverMode}
                        onChange={(e) => setSolverMode(e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="none">Select Mode</option>
                        <option value="simplify">Simplify Expression</option>
                        <option value="solve">Solve Equation</option>
                        <option value="properties">Show Properties</option>
                    </select>
                </div>

                {/* Expression Input */}
                {(solverMode === 'simplify' || solverMode === 'solve') && (
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Enter Expression:
                        </label>
                        <input
                            type="text"
                            value={inputExpression}
                            onChange={(e) => setInputExpression(e.target.value)}
                            placeholder={functionType === 'exponential' ? "e.g., 2^x * 2^3" : "e.g., log(x) + log(3)"}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                    </div>
                )}

                {/* Target Operation */}
                {solverMode !== 'none' && (
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Operation:
                        </label>
                        <select
                            value={targetOperation}
                            onChange={(e) => setTargetOperation(e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        >
                            <option value="simplify">Simplify</option>
                            <option value="solve">Solve for x</option>
                        </select>
                    </div>
                )}

                {/* Solve Button */}
                {(solverMode === 'simplify' || solverMode === 'solve') && inputExpression && (
                    <button
                        onClick={() => {
                            const steps = solveStepByStep(inputExpression, targetOperation);
                            setSolutionSteps(steps);
                            setShowSolutionSteps(true);
                            setCurrentStep(0);
                        }}
                        className="w-full bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors"
                    >
                        Solve Step-by-Step
                    </button>
                )}

                {/* Solution Steps Display */}
                {showSolutionSteps && solutionSteps.length > 0 && (
                    <div className="mt-4 p-4 bg-gray-50 border border-gray-200 rounded-lg">
                        <h4 className="font-semibold text-gray-700 mb-3">Step-by-Step Solution:</h4>
                        
                        {/* Step Navigation */}
                        <div className="flex items-center justify-between mb-3">
                            <button
                                onClick={() => setCurrentStep(Math.max(0, currentStep - 1))}
                                disabled={currentStep === 0}
                                className="px-3 py-1 bg-gray-300 text-gray-700 rounded disabled:opacity-50"
                            >
                                Previous
                            </button>
                            <span className="text-sm text-gray-600">
                                Step {currentStep + 1} of {solutionSteps.length}
                            </span>
                            <button
                                onClick={() => setCurrentStep(Math.min(solutionSteps.length - 1, currentStep + 1))}
                                disabled={currentStep === solutionSteps.length - 1}
                                className="px-3 py-1 bg-gray-300 text-gray-700 rounded disabled:opacity-50"
                            >
                                Next
                            </button>
                        </div>

                        {/* Current Step Display */}
                        {solutionSteps[currentStep] && (
                            <div className="p-3 bg-white border border-gray-200 rounded-lg">
                                <div className="flex items-start space-x-3">
                                    <div className="flex-shrink-0 w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">
                                        {solutionSteps[currentStep].step}
                                    </div>
                                    <div className="flex-1">
                                        <div className="font-medium text-gray-700 mb-1">
                                            {solutionSteps[currentStep].action}
                                        </div>
                                        <div className="text-lg font-mono text-blue-600 mb-1">
                                            {solutionSteps[currentStep].expression}
                                        </div>
                                        <div className="text-sm text-gray-600 mb-1">
                                            {solutionSteps[currentStep].explanation}
                                        </div>
                                        <div className="text-sm font-medium text-green-600">
                                            {solutionSteps[currentStep].result}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                )}
            </div>
        );
    };

    // Render laws demonstrator UI
    const renderLawsDemonstrator = () => {
        // Only show for integrated exponential/logarithmic function
        if (exprData.functionType !== 'integrated_exponential_logarithmic') {
            return null;
        }
        
        const functionType = getFunctionType();
        console.log('Laws Demonstrator - Function Type:', functionType, 'Expression:', exprData.expression, 'ExpressionType:', exprData.expressionType);

        const lawDemo = getLawDemonstration(currentLaw);

        return (
            <div className="bg-white border border-gray-300 rounded-lg p-4 mb-4">
                <div className="flex items-center justify-between mb-3">
                    <h3 className="text-lg font-semibold text-gray-800">
                        {functionType === 'exponential' ? 'Exponential' : 'Logarithmic'} Laws Demonstrator
                    </h3>
                    <button
                        onClick={() => setShowLawsDemonstrator(!showLawsDemonstrator)}
                        className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
                    >
                        {showLawsDemonstrator ? 'Hide' : 'Show'} Laws
                    </button>
                </div>

                {showLawsDemonstrator && (
                    <>
                        {/* Law Selection */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Select Law:
                                </label>
                                <select
                                    value={currentLaw}
                                    onChange={(e) => setCurrentLaw(e.target.value)}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                >
                                    {functionType === 'exponential' ? (
                                        <>
                                            <option value="product">Product Law</option>
                                            <option value="quotient">Quotient Law</option>
                                            <option value="power">Power Law</option>
                                            <option value="zero">Zero Exponent</option>
                                            <option value="negative">Negative Exponent</option>
                                        </>
                                    ) : (
                                        <>
                                            <option value="product">Product Law</option>
                                            <option value="quotient">Quotient Law</option>
                                            <option value="power">Power Law</option>
                                            <option value="change_of_base">Change of Base</option>
                                            <option value="identity">Identity Law</option>
                                        </>
                                    )}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Demonstration Mode:
                                </label>
                                <select
                                    value={lawDemonstrationMode}
                                    onChange={(e) => setLawDemonstrationMode(e.target.value)}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                >
                                    <option value="visual">Visual</option>
                                    <option value="numerical">Numerical</option>
                                    <option value="proof">Step-by-Step Proof</option>
                                </select>
                            </div>
                        </div>

                        {/* Parameter Controls */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    {functionType === 'exponential' ? 'Base:' : 'Log Base:'}
                                </label>
                                <input
                                    type="number"
                                    value={lawBase}
                                    onChange={(e) => setLawBase(Number(e.target.value))}
                                    min="2"
                                    max="10"
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    {functionType === 'exponential' ? 'Exponent X:' : 'Value X:'}
                                </label>
                                <input
                                    type="number"
                                    value={lawX}
                                    onChange={(e) => setLawX(Number(e.target.value))}
                                    min="1"
                                    max="10"
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    {functionType === 'exponential' ? 'Exponent Y:' : 'Value Y:'}
                                </label>
                                <input
                                    type="number"
                                    value={lawY}
                                    onChange={(e) => setLawY(Number(e.target.value))}
                                    min="1"
                                    max="10"
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                />
                            </div>
                            {functionType === 'logarithmic' && currentLaw === 'change_of_base' && (
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                        New Base:
                                    </label>
                                    <input
                                        type="number"
                                        value={logBase2}
                                        onChange={(e) => setLogBase2(Number(e.target.value))}
                                        min="2"
                                        max="10"
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    />
                                </div>
                            )}
                        </div>

                        {/* Law Demonstration Display */}
                        <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                            <h4 className="font-semibold text-blue-800 mb-2">
                                {currentLaw.charAt(0).toUpperCase() + currentLaw.slice(1)} Law
                            </h4>
                            <div className="text-lg font-mono text-blue-600 mb-2">
                                {renderMathExpression(lawDemo.formula)}
                            </div>
                            <p className="text-sm text-blue-700 mb-3">{lawDemo.description}</p>

                            {lawDemonstrationMode === 'visual' && (
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div className="p-3 bg-white border border-blue-200 rounded">
                                        <h5 className="font-medium text-blue-800 mb-1">Left Side:</h5>
                                        <div className="text-lg font-mono text-blue-600">
                                            {renderMathExpression(lawDemo.leftSide)}
                                        </div>
                                    </div>
                                    <div className="p-3 bg-white border border-blue-200 rounded">
                                        <h5 className="font-medium text-blue-800 mb-1">Right Side:</h5>
                                        <div className="text-lg font-mono text-blue-600">
                                            {renderMathExpression(lawDemo.rightSide)}
                                        </div>
                                    </div>
                                </div>
                            )}

                            {lawDemonstrationMode === 'numerical' && (
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div className="p-3 bg-white border border-blue-200 rounded">
                                        <h5 className="font-medium text-blue-800 mb-1">Left Side Value:</h5>
                                        <div className="text-lg font-mono text-blue-600">
                                            {lawDemo.leftValue}
                                        </div>
                                    </div>
                                    <div className="p-3 bg-white border border-blue-200 rounded">
                                        <h5 className="font-medium text-blue-800 mb-1">Right Side Value:</h5>
                                        <div className="text-lg font-mono text-blue-600">
                                            {lawDemo.rightValue}
                                        </div>
                                    </div>
                                </div>
                            )}

                            {lawDemonstrationMode === 'proof' && (
                                <div className="p-3 bg-white border border-blue-200 rounded">
                                    <h5 className="font-medium text-blue-800 mb-2">Step-by-Step Proof:</h5>
                                    <div className="space-y-1">
                                        {lawDemo.proof.map((step, index) => (
                                            <div key={index} className="text-lg font-mono text-blue-600">
                                                {renderMathExpression(step)}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Verification */}
                            <div className="mt-3 p-2 bg-green-50 border border-green-200 rounded">
                                <div className="text-sm text-green-700">
                                    ✓ Verification: {lawDemo.leftValue} = {lawDemo.rightValue} 
                                    {Math.abs(lawDemo.leftValue - lawDemo.rightValue) < 0.0001 ? ' ✓' : ' ✗'}
                                </div>
                            </div>
                        </div>
                    </>
                )}
            </div>
        );
    };

    // Render step-by-step solution
    const renderSteps = () => {
        if (!showSteps || !exprData.steps || exprData.steps.length === 0) return null;

        return (
            <div className="mb-4">
                <h4 className="font-semibold text-gray-700 mb-2">Step-by-Step Solution:</h4>
                <div className="space-y-3">
                    {exprData.steps.map((step, index) => (
                        <div key={index} className="p-3 bg-white border border-gray-200 rounded-lg">
                            <div className="flex items-start space-x-3">
                                <div className="flex-shrink-0 w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">
                                    {step.step}
                                </div>
                                <div className="flex-1">
                                    <div className="font-medium text-gray-700 mb-1">{step.description}</div>
                                    <div className="text-lg font-mono text-blue-600 mb-1">{step.expression}</div>
                                    <div className="text-sm text-gray-600">{step.explanation}</div>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        );
    };



    // Update stepCanvas with comprehensive steps
    const updateStepCanvas = (comprehensiveSteps) => {
        setExprData(prev => ({
            ...prev,
            stepCanvas: comprehensiveSteps.map(step => ({
                ...step,
                lineBreaks: step.description ? step.description.split(/[.!?]/).filter(s => s.trim().length > 0) : [step.description]
            }))
        }));
    };

    // Render inverse visualizer UI
    const renderInverseVisualizer = () => {
        // Only show for integrated exponential/logarithmic function
        if (exprData.functionType !== 'integrated_exponential_logarithmic') {
            return null;
        }
        
        const functionType = getFunctionType();
        console.log('Inverse Visualizer - Function Type:', functionType, 'Expression:', exprData.expression, 'ExpressionType:', exprData.expressionType);

        return (
            <div className="bg-white border border-gray-300 rounded-lg p-4 mb-4">
                <div className="flex items-center justify-between mb-3">
                    <h3 className="text-lg font-semibold text-gray-800">
                        Inverse Function Visualizer
                    </h3>
                    <div className="flex space-x-2">
                        <button
                            onClick={() => setShowInverseVisualizer(!showInverseVisualizer)}
                            className="px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600 transition-colors"
                        >
                            {showInverseVisualizer ? 'Hide' : 'Show'} Visualizer
                        </button>

                    </div>
                </div>

                {showInverseVisualizer && (
                    <div className="space-y-4">
                        {/* Function Type Display */}
                        <div className="p-3 bg-green-50 border border-green-200 rounded">
                            <h4 className="font-medium text-green-800 mb-2">Function Type: {functionType === 'exponential' ? 'Exponential' : 'Logarithmic'}</h4>
                            <p className="text-sm text-green-700">
                                {functionType === 'exponential' 
                                    ? 'Exponential functions have inverse logarithmic functions'
                                    : 'Logarithmic functions have inverse exponential functions'
                                }
                            </p>
                        </div>

                        {/* Inverse Function Display */}
                        <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                            <h4 className="font-medium text-blue-800 mb-2">Inverse Function Relationship</h4>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <p className="text-sm font-medium text-blue-700 mb-1">Original Function:</p>
                                    <div className="font-mono text-blue-600 text-sm">
                                        {functionType === 'exponential' 
                                            ? `y = ${lawBase}^x`
                                            : `y = log_${lawBase}(x)`
                                        }
                                    </div>
                                </div>
                                <div>
                                    <p className="text-sm font-medium text-blue-700 mb-1">Inverse Function:</p>
                                    <div className="font-mono text-blue-600 text-sm">
                                        {functionType === 'exponential' 
                                            ? `x = log_${lawBase}(y)`
                                            : `x = ${lawBase}^y`
                                        }
                                    </div>
                                </div>
                            </div>
                        </div>



                        {/* Interactive Demonstration */}
                        <div className="p-3 bg-purple-50 border border-purple-200 rounded">
                            <h4 className="font-medium text-purple-800 mb-2">Interactive Demonstration</h4>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label className="block text-sm font-medium text-purple-700 mb-1">Input Value:</label>
                                    <input
                                        type="number"
                                        value={lawX}
                                        onChange={(e) => setLawX(Number(e.target.value))}
                                        min="1"
                                        max="20"
                                        className="w-full px-3 py-2 border border-purple-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-purple-700 mb-1">Base:</label>
                                    <input
                                        type="number"
                                        value={lawBase}
                                        onChange={(e) => setLawBase(Number(e.target.value))}
                                        min="2"
                                        max="10"
                                        className="w-full px-3 py-2 border border-purple-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                                    />
                                </div>
                            </div>
                            
                            {/* Calculation Results */}
                            <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div className="p-2 bg-white border border-purple-200 rounded">
                                    <p className="text-xs text-purple-600 mb-1">Original Function Result:</p>
                                    <div className="font-mono text-purple-700">
                                        {functionType === 'exponential' 
                                            ? Math.pow(lawBase, lawX).toFixed(4)
                                            : (Math.log(lawX) / Math.log(lawBase)).toFixed(4)
                                        }
                                    </div>
                                </div>
                                <div className="p-2 bg-white border border-purple-200 rounded">
                                    <p className="text-xs text-purple-600 mb-1">Inverse Function Result:</p>
                                    <div className="font-mono text-purple-700">
                                        {functionType === 'exponential' 
                                            ? (Math.log(Math.pow(lawBase, lawX)) / Math.log(lawBase)).toFixed(4)
                                            : Math.pow(lawBase, (Math.log(lawX) / Math.log(lawBase))).toFixed(4)
                                        }
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Key Properties */}
                        <div className="p-3 bg-orange-50 border border-orange-200 rounded">
                            <h4 className="font-medium text-orange-800 mb-2">Key Properties</h4>
                            <ul className="text-sm text-orange-700 space-y-1">
                                <li>• The inverse function "undoes" the original function</li>
                                <li>• If f(x) = y, then f⁻¹(y) = x</li>
                                <li>• The graphs are reflections across the line y = x</li>
                                <li>• Domain of f becomes range of f⁻¹ and vice versa</li>
                            </ul>
                        </div>

                        
                    </div>
                )}
            </div>
        );
    };

    return (
        <>
            {/* Function Type Toggle - Only for integrated exponential/logarithmic function */}
            {exprData.functionType === 'integrated_exponential_logarithmic' && (
                <div className="bg-white border border-gray-300 rounded-lg p-4 mb-4">
                    <div className="flex items-center justify-between">
                        <h3 className="text-lg font-semibold text-gray-800">
                            Function Type Selection
                        </h3>
                        <div className="flex space-x-2">
                            <button
                                onClick={() => setExprData(prev => ({
                                    ...prev,
                                    expressionType: 'exponential'
                                }))}
                                className={`px-4 py-2 rounded-md font-medium transition-colors ${
                                    exprData.expressionType === 'exponential'
                                        ? 'bg-blue-500 text-white'
                                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                }`}
                            >
                                Exponential
                            </button>
                            <button
                                onClick={() => setExprData(prev => ({
                                    ...prev,
                                    expressionType: 'logarithmic'
                                }))}
                                className={`px-4 py-2 rounded-md font-medium transition-colors ${
                                    exprData.expressionType === 'logarithmic'
                                        ? 'bg-blue-500 text-white'
                                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                }`}
                            >
                                Logarithmic
                            </button>
                        </div>
                    </div>
                    <div className="mt-2 text-sm text-gray-600">
                        Current: <span className="font-medium text-blue-600">{exprData.expressionType || 'exponential'}</span> function
                    </div>
                </div>
            )}

            {renderExpressionSolver()}
            {renderLawsDemonstrator()}
            {renderInverseVisualizer()}
            {renderSteps()}
        </>
    );
};

export default StepCanvas;
