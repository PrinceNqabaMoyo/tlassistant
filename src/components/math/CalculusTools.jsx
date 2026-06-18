import React, { useState, useEffect } from 'react';

const CalculusTools = ({ initialData, onChange, isSubmitted }) => {
    const [calculusData, setCalculusData] = useState(initialData || {
        title: "Calculus Tools",
        operation: 'derivative', // 'derivative', 'integral', 'limit', 'analyze'
        function: "x^2 + 2*x + 1",
        variable: 'x',
        point: 2,
        lowerBound: 0,
        upperBound: 1,
        limitPoint: 0,
        showSteps: true,
        showGraph: false,
        result: null,
        steps: []
    });

    useEffect(() => {
        // Ensure all required properties are initialized
        if (!calculusData.steps) {
            setCalculusData(prev => ({ ...prev, steps: [] }));
        }
        if (!calculusData.result) {
            setCalculusData(prev => ({ ...prev, result: null }));
        }
        if (!calculusData.lowerBound) {
            setCalculusData(prev => ({ ...prev, lowerBound: 0 }));
        }
        if (!calculusData.upperBound) {
            setCalculusData(prev => ({ ...prev, upperBound: 1 }));
        }
        if (!calculusData.limitPoint) {
            setCalculusData(prev => ({ ...prev, limitPoint: 0 }));
        }
        
        onChange(calculusData);
    }, [calculusData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setCalculusData(prev => ({ ...prev, [field]: value }));
    };

    // Simple function parser and evaluator
    const parseFunction = (func) => {
        try {
            // Remove spaces and convert to lowercase
            func = func.replace(/\s/g, '').toLowerCase();
            
            // Replace common mathematical notations
            func = func
                .replace(/\^/g, '**')
                .replace(/(\d+)x/g, '$1*x')
                .replace(/x(\d+)/g, 'x*$1')
                .replace(/([a-z])\(/g, '$1*(')
                .replace(/\)([a-z])/g, ')*$1');
            
            return func;
        } catch (error) {
            return null;
        }
    };

    const evaluateFunction = (func, x) => {
        try {
            const parsedFunc = parseFunction(func);
            if (!parsedFunc) return null;
            
            // Create a safe evaluation environment
            const safeEval = (expression, xValue) => {
                const func = new Function('x', `return ${expression}`);
                return func(xValue);
            };
            
            return safeEval(parsedFunc, x);
        } catch (error) {
            return null;
        }
    };

    // Simple derivative calculator (basic rules)
    const calculateDerivative = (func) => {
        const steps = [];
        let currentFunc = func;
        
        try {
            steps.push({
                step: 1,
                description: "Original Function",
                expression: `f(x) = ${currentFunc}`,
                explanation: "Start with the given function"
            });

            // Simple derivative rules
            let derivative = currentFunc
                .replace(/\s/g, '')
                .replace(/(\d+)x\^(\d+)/g, (match, coef, power) => {
                    const newCoef = parseInt(coef) * parseInt(power);
                    const newPower = parseInt(power) - 1;
                    if (newPower === 0) return newCoef.toString();
                    if (newPower === 1) return `${newCoef}x`;
                    return `${newCoef}x^${newPower}`;
                })
                .replace(/(\d+)x/g, (match, coef) => coef)
                .replace(/x\^(\d+)/g, (match, power) => {
                    const newPower = parseInt(power) - 1;
                    if (newPower === 0) return '1';
                    if (newPower === 1) return 'x';
                    return `x^${newPower}`;
                })
                .replace(/x/g, '1');

            // Clean up the derivative
            derivative = derivative
                .replace(/\+\+/g, '+')
                .replace(/^\++/, '')
                .replace(/\++$/, '');

            if (derivative === '') derivative = '0';

            steps.push({
                step: 2,
                description: "Apply Derivative Rules",
                expression: `f'(x) = ${derivative}`,
                explanation: "Apply power rule: d/dx(x^n) = n*x^(n-1)"
            });

            return { result: derivative, steps };
        } catch (error) {
            return { result: "Error in derivative calculation", steps: [{ step: 1, description: "Error", expression: func, explanation: "Could not calculate derivative" }] };
        }
    };

    // Simple integral calculator (basic rules)
    const calculateIntegral = (func, lower, upper) => {
        const steps = [];
        let currentFunc = func;
        
        try {
            steps.push({
                step: 1,
                description: "Original Function",
                expression: `f(x) = ${currentFunc}`,
                explanation: "Start with the given function"
            });

            // Simple antiderivative rules
            let antiderivative = currentFunc
                .replace(/\s/g, '')
                .replace(/(\d+)x\^(\d+)/g, (match, coef, power) => {
                    const newCoef = parseInt(coef) / (parseInt(power) + 1);
                    const newPower = parseInt(power) + 1;
                    return `${newCoef}x^${newPower}`;
                })
                .replace(/(\d+)x/g, (match, coef) => `${parseInt(coef)/2}x^2`)
                .replace(/x\^(\d+)/g, (match, power) => {
                    const newPower = parseInt(power) + 1;
                    return `x^${newPower}/${newPower}`;
                })
                .replace(/x/g, 'x^2/2');

            // Add constant of integration
            antiderivative += ' + C';

            steps.push({
                step: 2,
                description: "Find Antiderivative",
                expression: `∫f(x)dx = ${antiderivative}`,
                explanation: "Apply power rule: ∫x^n dx = x^(n+1)/(n+1)"
            });

            // Calculate definite integral
            if (lower !== undefined && upper !== undefined) {
                const lowerValue = evaluateFunction(antiderivative.replace(' + C', ''), lower);
                const upperValue = evaluateFunction(antiderivative.replace(' + C', ''), upper);
                const definiteIntegral = upperValue - lowerValue;

                steps.push({
                    step: 3,
                    description: "Evaluate Definite Integral",
                    expression: `∫[${lower} to ${upper}] f(x)dx = F(${upper}) - F(${lower}) = ${upperValue} - ${lowerValue} = ${definiteIntegral}`,
                    explanation: "Apply Fundamental Theorem of Calculus"
                });

                return { result: definiteIntegral, steps };
            }

            return { result: antiderivative, steps };
        } catch (error) {
            return { result: "Error in integral calculation", steps: [{ step: 1, description: "Error", expression: func, explanation: "Could not calculate integral" }] };
        }
    };

    // Simple limit calculator
    const calculateLimit = (func, point) => {
        const steps = [];
        
        try {
            steps.push({
                step: 1,
                description: "Original Function",
                expression: `f(x) = ${func}`,
                explanation: "Start with the given function"
            });

            steps.push({
                step: 2,
                description: "Limit Point",
                expression: `lim(x → ${point})`,
                explanation: `Find limit as x approaches ${point}`
            });

            // Try direct substitution first
            const directValue = evaluateFunction(func, point);
            
            if (directValue !== null && !isNaN(directValue)) {
                steps.push({
                    step: 3,
                    description: "Direct Substitution",
                    expression: `f(${point}) = ${directValue}`,
                    explanation: "Function is continuous at this point"
                });
                return { result: directValue, steps };
            }

            // For simple cases, try approaching from both sides
            const leftValue = evaluateFunction(func, point - 0.001);
            const rightValue = evaluateFunction(func, point + 0.001);

            if (Math.abs(leftValue - rightValue) < 0.01) {
                steps.push({
                    step: 3,
                    description: "Approach from Both Sides",
                    expression: `lim(x → ${point}^-) ≈ ${leftValue.toFixed(3)}, lim(x → ${point}^+) ≈ ${rightValue.toFixed(3)}`,
                    explanation: "Limit exists and equals the common value"
                });
                return { result: leftValue, steps };
            }

            steps.push({
                step: 3,
                description: "Limit Analysis",
                expression: "Limit may not exist or requires further analysis",
                explanation: "Function may have a discontinuity or undefined behavior"
            });

            return { result: "Limit requires further analysis", steps };
        } catch (error) {
            return { result: "Error in limit calculation", steps: [{ step: 1, description: "Error", expression: func, explanation: "Could not calculate limit" }] };
        }
    };

    // Function analysis
    const analyzeFunction = (func) => {
        const steps = [];
        
        try {
            steps.push({
                step: 1,
                description: "Original Function",
                expression: `f(x) = ${func}`,
                explanation: "Start with the given function"
            });

            // Find critical points (where derivative = 0)
            const derivative = calculateDerivative(func);
            steps.push({
                step: 2,
                description: "Derivative",
                expression: `f'(x) = ${derivative.result}`,
                explanation: "Find derivative to locate critical points"
            });

            // Analyze behavior at key points
            const points = [-2, -1, 0, 1, 2];
            const values = points.map(x => evaluateFunction(func, x));
            
            steps.push({
                step: 3,
                description: "Function Values",
                expression: `f(-2) = ${values[0]?.toFixed(3)}, f(-1) = ${values[1]?.toFixed(3)}, f(0) = ${values[2]?.toFixed(3)}, f(1) = ${values[3]?.toFixed(3)}, f(2) = ${values[4]?.toFixed(3)}`,
                explanation: "Evaluate function at key points"
            });

            // Determine if function is increasing/decreasing
            const increasing = values[4] > values[0];
            steps.push({
                step: 4,
                description: "Function Behavior",
                expression: `Function is ${increasing ? 'increasing' : 'decreasing'} on the interval [-2, 2]`,
                explanation: "Compare function values at endpoints"
            });

            return { result: "Function analysis complete", steps };
        } catch (error) {
            return { result: "Error in function analysis", steps: [{ step: 1, description: "Error", expression: func, explanation: "Could not analyze function" }] };
        }
    };

    const performOperation = () => {
        if (!calculusData.function.trim()) {
            setCalculusData(prev => ({ ...prev, result: "Please enter a function" }));
            return;
        }

        setCalculusData(prev => ({ ...prev, result: null, steps: [] }));

        let result;
        switch (calculusData.operation) {
            case 'derivative':
                result = calculateDerivative(calculusData.function);
                break;
            case 'integral':
                result = calculateIntegral(calculusData.function, calculusData.lowerBound, calculusData.upperBound);
                break;
            case 'limit':
                result = calculateLimit(calculusData.function, calculusData.limitPoint);
                break;
            case 'analyze':
                result = analyzeFunction(calculusData.function);
                break;
            default:
                result = { result: calculusData.function, steps: [] };
        }

        setCalculusData(prev => ({
            ...prev,
            result: result.result,
            steps: result.steps || []
        }));
    };

    const renderSteps = () => {
        if (!calculusData.showSteps || !calculusData.steps || calculusData.steps.length === 0) return null;

        return (
            <div className="mb-4">
                <h4 className="font-semibold text-gray-700 mb-2">Step-by-Step Solution:</h4>
                <div className="space-y-3">
                    {calculusData.steps?.map((step, index) => (
                        <div key={index} className="p-3 bg-white border border-gray-200 rounded-lg">
                            <div className="flex items-start space-x-3">
                                <div className="flex-shrink-0 w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">
                                    {step?.step || index + 1}
                                </div>
                                <div className="flex-1">
                                    <div className="font-medium text-gray-700 mb-1">{step?.description || 'Step description'}</div>
                                    <div className="text-lg font-mono text-blue-600 mb-1">{step?.expression || 'Expression'}</div>
                                    <div className="text-sm text-gray-600">{step?.explanation || 'Step explanation'}</div>
                                </div>
                            </div>
                        </div>
                    )) || <div className="text-gray-400 text-center py-4">No steps available</div>}
                </div>
            </div>
        );
    };

    const quickFunctions = [
        { name: "Linear", func: "2*x + 3" },
        { name: "Quadratic", func: "x^2 + 2*x + 1" },
        { name: "Cubic", func: "x^3 - x" },
        { name: "Exponential", func: "2^x" },
        { name: "Trigonometric", func: "sin(x)" },
        { name: "Rational", func: "1/(x + 1)" }
    ];

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Calculus Tools</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={calculusData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Calculus Tools Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Operation:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={calculusData.operation}
                        onChange={(e) => handleFieldChange('operation', e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="derivative">Calculate Derivative</option>
                        <option value="integral">Calculate Integral</option>
                        <option value="limit">Calculate Limit</option>
                        <option value="analyze">Analyze Function</option>
                    </select>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Variable:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={calculusData.variable}
                        onChange={(e) => handleFieldChange('variable', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="x"
                        maxLength="1"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Function:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm font-mono"
                        value={calculusData.function}
                        onChange={(e) => handleFieldChange('function', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Enter function (e.g., x^2 + 2*x + 1)"
                    />
                </div>
            </div>

            {/* Operation-specific inputs */}
            {calculusData.operation === 'integral' && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Lower Bound:</label>
                        <input
                            type="number"
                            className="w-full p-2 border border-gray-300 rounded-md text-sm"
                            value={calculusData.lowerBound}
                            onChange={(e) => handleFieldChange('lowerBound', parseFloat(e.target.value) || 0)}
                            disabled={isSubmitted}
                            step="any"
                            placeholder="0"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Upper Bound:</label>
                        <input
                            type="number"
                            className="w-full p-2 border border-gray-300 rounded-md text-sm"
                            value={calculusData.upperBound}
                            onChange={(e) => handleFieldChange('upperBound', parseFloat(e.target.value) || 1)}
                            disabled={isSubmitted}
                            step="any"
                            placeholder="1"
                        />
                    </div>
                </div>
            )}

            {calculusData.operation === 'limit' && (
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-1">Limit Point:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={calculusData.limitPoint}
                        onChange={(e) => handleFieldChange('limitPoint', parseFloat(e.target.value) || 0)}
                        disabled={isSubmitted}
                        step="any"
                        placeholder="0"
                    />
                </div>
            )}

            {/* Quick Function Buttons */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Quick Functions:</label>
                <div className="flex flex-wrap gap-2">
                    {quickFunctions.map((quick, index) => (
                        <button
                            key={index}
                            onClick={() => handleFieldChange('function', quick.func)}
                            disabled={isSubmitted}
                            className="px-3 py-1 bg-gray-200 text-gray-700 rounded-md text-sm hover:bg-gray-300"
                        >
                            {quick.name}
                        </button>
                    ))}
                </div>
            </div>

            {/* Controls */}
            <div className="flex flex-wrap gap-2 mb-4">
                {!isSubmitted && (
                    <button
                        onClick={performOperation}
                        className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm hover:bg-blue-600"
                    >
                        Calculate {calculusData.operation?.charAt(0)?.toUpperCase() + calculusData.operation?.slice(1) || 'Operation'}
                    </button>
                )}
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={calculusData.showSteps}
                        onChange={(e) => handleFieldChange('showSteps', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Steps</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={calculusData.showGraph}
                        onChange={(e) => handleFieldChange('showGraph', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Graph</span>
                </label>
            </div>

            {/* Result Display */}
            {calculusData.result && (
                <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">Result:</h4>
                    <div className="text-lg font-mono text-green-700">{calculusData.result}</div>
                    <div className="text-sm text-green-600 mt-1">
                        {calculusData.operation === 'derivative' && 'Derivative'}
                        {calculusData.operation === 'integral' && 'Integral'}
                        {calculusData.operation === 'limit' && 'Limit'}
                        {calculusData.operation === 'analyze' && 'Function Analysis'}
                        {!['derivative', 'integral', 'limit', 'analyze'].includes(calculusData.operation) && 'Result'}
                    </div>
                </div>
            )}

            {/* Steps Display */}
            {renderSteps()}

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Calculus Tools Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Enter a function using standard mathematical notation</li>
                    <li>Use ^ for exponents (e.g., x^2 for x²)</li>
                    <li>Use * for multiplication (e.g., 2*x for 2x)</li>
                    <li>Choose operation: derivative, integral, limit, or function analysis</li>
                    <li>For definite integrals, specify lower and upper bounds</li>
                    <li>For limits, specify the point to approach</li>
                    <li>View step-by-step solutions to understand the process</li>
                    <li>Use quick function buttons for common examples</li>
                </ul>
            </div>
        </div>
    );
};

export default CalculusTools;
