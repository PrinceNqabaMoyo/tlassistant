import React, { useState, useEffect } from 'react';

const VectorCalculator = ({ initialData, onChange, isSubmitted }) => {
    const [vectorData, setVectorData] = useState(initialData || {
        title: "Vector Calculator",
        dimension: 3, // 2D or 3D
        operation: 'add', // 'add', 'subtract', 'dot', 'cross', 'magnitude', 'angle'
        vectorA: { x: 0, y: 0, z: 0 },
        vectorB: { x: 0, y: 0, z: 0 },
        showSteps: true,
        showVisualization: true,
        result: null,
        steps: []
    });

    useEffect(() => {
        // Ensure all required properties are initialized
        if (vectorData.result === undefined) {
            setVectorData(prev => ({ ...prev, result: null }));
            return;
        }
        if (!vectorData.steps) {
            setVectorData(prev => ({ ...prev, steps: [] }));
            return;
        }
        if (!vectorData.vectorA) {
            setVectorData(prev => ({ ...prev, vectorA: { x: 0, y: 0, z: 0 } }));
            return;
        }
        if (!vectorData.vectorB) {
            setVectorData(prev => ({ ...prev, vectorB: { x: 0, y: 0, z: 0 } }));
            return;
        }
        
        onChange(vectorData);
    }, [vectorData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setVectorData(prev => ({ ...prev, [field]: value }));
    };

    const updateVector = (vectorName, component, value) => {
        if (isSubmitted) return;
        setVectorData(prev => ({
            ...prev,
            [vectorName]: {
                ...prev[vectorName],
                [component]: parseFloat(value) || 0
            }
        }));
    };

    const calculateMagnitude = (vector) => {
        const { x, y, z } = vector;
        return Math.sqrt(x * x + y * y + z * z);
    };

    const calculateDotProduct = (a, b) => {
        return a.x * b.x + a.y * b.y + a.z * b.z;
    };

    const calculateCrossProduct = (a, b) => {
        return {
            x: a.y * b.z - a.z * b.y,
            y: a.z * b.x - a.x * b.z,
            z: a.x * b.y - a.y * b.x
        };
    };

    const calculateAngle = (a, b) => {
        const dotProduct = calculateDotProduct(a, b);
        const magnitudeA = calculateMagnitude(a);
        const magnitudeB = calculateMagnitude(b);
        
        if (magnitudeA === 0 || magnitudeB === 0) return 0;
        
        const cosAngle = dotProduct / (magnitudeA * magnitudeB);
        // Clamp to [-1, 1] to avoid numerical errors
        const clampedCos = Math.max(-1, Math.min(1, cosAngle));
        return Math.acos(clampedCos) * (180 / Math.PI); // Convert to degrees
    };

    const addVectors = (a, b) => {
        return {
            x: a.x + b.x,
            y: a.y + b.y,
            z: a.z + b.z
        };
    };

    const subtractVectors = (a, b) => {
        return {
            x: a.x - b.x,
            y: a.y - b.y,
            z: a.z - b.z
        };
    };

    const performOperation = () => {
        const { vectorA, vectorB, operation, dimension } = vectorData;
        const steps = [];
        let result = null;

        // Adjust vectors based on dimension
        const a = dimension === 2 ? { ...vectorA, z: 0 } : vectorA;
        const b = dimension === 2 ? { ...vectorB, z: 0 } : vectorB;

        steps.push({
            step: 1,
            description: "Input Vectors",
            expression: `Vector A = (${a.x}, ${a.y}${dimension === 3 ? `, ${a.z}` : ''})`,
            explanation: `Vector A components in ${dimension}D space`
        });

        if (operation !== 'magnitude') {
            steps.push({
                step: 2,
                description: "Input Vectors",
                expression: `Vector B = (${b.x}, ${b.y}${dimension === 3 ? `, ${b.z}` : ''})`,
                explanation: `Vector B components in ${dimension}D space`
            });
        }

        switch (operation) {
            case 'add':
                result = addVectors(a, b);
                steps.push({
                    step: 3,
                    description: "Vector Addition",
                    expression: `A + B = (${a.x} + ${b.x}, ${a.y} + ${b.y}${dimension === 3 ? `, ${a.z} + ${b.z}` : ''})`,
                    explanation: "Add corresponding components"
                });
                steps.push({
                    step: 4,
                    description: "Result",
                    expression: `A + B = (${result.x}, ${result.y}${dimension === 3 ? `, ${result.z}` : ''})`,
                    explanation: "Final result vector"
                });
                break;

            case 'subtract':
                result = subtractVectors(a, b);
                steps.push({
                    step: 3,
                    description: "Vector Subtraction",
                    expression: `A - B = (${a.x} - ${b.x}, ${a.y} - ${b.y}${dimension === 3 ? `, ${a.z} - ${b.z}` : ''})`,
                    explanation: "Subtract corresponding components"
                });
                steps.push({
                    step: 4,
                    description: "Result",
                    expression: `A - B = (${result.x}, ${result.y}${dimension === 3 ? `, ${result.z}` : ''})`,
                    explanation: "Final result vector"
                });
                break;

            case 'dot':
                result = calculateDotProduct(a, b);
                steps.push({
                    step: 3,
                    description: "Dot Product",
                    expression: `A · B = ${a.x} × ${b.x} + ${a.y} × ${b.y}${dimension === 3 ? ` + ${a.z} × ${b.z}` : ''}`,
                    explanation: "Multiply corresponding components and sum"
                });
                steps.push({
                    step: 4,
                    description: "Result",
                    expression: `A · B = ${result}`,
                    explanation: "Scalar result"
                });
                break;

            case 'cross':
                if (dimension === 2) {
                    result = { x: 0, y: 0, z: a.x * b.y - a.y * b.x };
                    steps.push({
                        step: 3,
                        description: "Cross Product (2D)",
                        expression: `A × B = (0, 0, ${a.x} × ${b.y} - ${a.y} × ${b.x})`,
                        explanation: "In 2D, cross product gives a vector perpendicular to the plane"
                    });
                } else {
                    result = calculateCrossProduct(a, b);
                    steps.push({
                        step: 3,
                        description: "Cross Product (3D)",
                        expression: `A × B = (${a.y} × ${b.z} - ${a.z} × ${b.y}, ${a.z} × ${b.x} - ${a.x} × ${b.z}, ${a.x} × ${b.y} - ${a.y} × ${b.x})`,
                        explanation: "Use the cross product formula for 3D vectors"
                    });
                }
                steps.push({
                    step: 4,
                    description: "Result",
                    expression: `A × B = (${result.x}, ${result.y}, ${result.z})`,
                    explanation: "Vector result perpendicular to both input vectors"
                });
                break;

            case 'magnitude':
                result = calculateMagnitude(a);
                steps.push({
                    step: 3,
                    description: "Magnitude",
                    expression: `|A| = √(${a.x}² + ${a.y}²${dimension === 3 ? ` + ${a.z}²` : ''})`,
                    explanation: "Square root of sum of squared components"
                });
                steps.push({
                    step: 4,
                    description: "Result",
                    expression: `|A| = ${result.toFixed(4)}`,
                    explanation: "Scalar magnitude of the vector"
                });
                break;

            case 'angle':
                result = calculateAngle(a, b);
                const dotProduct = calculateDotProduct(a, b);
                const magnitudeA = calculateMagnitude(a);
                const magnitudeB = calculateMagnitude(b);
                
                steps.push({
                    step: 3,
                    description: "Dot Product",
                    expression: `A · B = ${dotProduct.toFixed(4)}`,
                    explanation: "Calculate dot product"
                });
                steps.push({
                    step: 4,
                    description: "Magnitudes",
                    expression: `|A| = ${magnitudeA.toFixed(4)}, |B| = ${magnitudeB.toFixed(4)}`,
                    explanation: "Calculate magnitudes of both vectors"
                });
                steps.push({
                    step: 5,
                    description: "Angle Formula",
                    expression: `cos(θ) = (A · B) / (|A| × |B|) = ${dotProduct.toFixed(4)} / (${magnitudeA.toFixed(4)} × ${magnitudeB.toFixed(4)})`,
                    explanation: "Use the dot product formula to find angle"
                });
                steps.push({
                    step: 6,
                    description: "Result",
                    expression: `θ = ${result.toFixed(2)}°`,
                    explanation: "Angle between the two vectors in degrees"
                });
                break;

            default:
                result = null;
        }

        setVectorData(prev => ({
            ...prev,
            result,
            steps
        }));
    };

    const renderSteps = () => {
        if (!vectorData.showSteps || vectorData.steps.length === 0) return null;

        return (
            <div className="mb-4">
                <h4 className="font-semibold text-gray-700 mb-2">Step-by-Step Solution:</h4>
                <div className="space-y-3">
                    {vectorData.steps.map((step, index) => (
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

    const renderVectorInput = (vectorName, vectorLabel) => {
        const vector = vectorData[vectorName];
        
        return (
            <div className="p-4 bg-white border border-gray-200 rounded-lg">
                <h4 className="font-semibold text-gray-700 mb-3">{vectorLabel}</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">X Component:</label>
                        <input
                            type="number"
                            className="w-full p-2 border border-gray-300 rounded-md text-sm"
                            value={vector.x}
                            onChange={(e) => updateVector(vectorName, 'x', e.target.value)}
                            disabled={isSubmitted}
                            step="any"
                            placeholder="0"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Y Component:</label>
                        <input
                            type="number"
                            className="w-full p-2 border border-gray-300 rounded-md text-sm"
                            value={vector.y}
                            onChange={(e) => updateVector(vectorName, 'y', e.target.value)}
                            disabled={isSubmitted}
                            step="any"
                            placeholder="0"
                        />
                    </div>
                    {vectorData.dimension === 3 && (
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Z Component:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-md text-sm"
                                value={vector.z}
                                onChange={(e) => updateVector(vectorName, 'z', e.target.value)}
                                disabled={isSubmitted}
                                step="any"
                                placeholder="0"
                            />
                        </div>
                    )}
                </div>
                <div className="mt-2 text-sm text-gray-600">
                    Magnitude: {calculateMagnitude(vector).toFixed(4)}
                </div>
            </div>
        );
    };

    const quickVectors = [
        { name: "Unit X", vector: { x: 1, y: 0, z: 0 } },
        { name: "Unit Y", vector: { x: 0, y: 1, z: 0 } },
        { name: "Unit Z", vector: { x: 0, y: 0, z: 1 } },
        { name: "Zero", vector: { x: 0, y: 0, z: 0 } },
        { name: "Random", vector: { x: Math.round(Math.random() * 10 - 5), y: Math.round(Math.random() * 10 - 5), z: Math.round(Math.random() * 10 - 5) } }
    ];

    // Don't render if not properly initialized
    if (!vectorData.vectorA || !vectorData.vectorB) {
        return (
            <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
                <h3 className="font-semibold text-gray-700 mb-4">Vector Calculator</h3>
                <div className="text-center py-8 text-gray-500">
                    <p>Loading vector calculator configuration...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Vector Calculator</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={vectorData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Vector Calculator Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Dimension:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={vectorData.dimension}
                        onChange={(e) => handleFieldChange('dimension', parseInt(e.target.value))}
                        disabled={isSubmitted}
                    >
                        <option value={2}>2D</option>
                        <option value={3}>3D</option>
                    </select>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Operation:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={vectorData.operation}
                        onChange={(e) => handleFieldChange('operation', e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="add">Add Vectors</option>
                        <option value="subtract">Subtract Vectors</option>
                        <option value="dot">Dot Product</option>
                        <option value="cross">Cross Product</option>
                        <option value="magnitude">Magnitude</option>
                        <option value="angle">Angle Between</option>
                    </select>
                </div>
            </div>

            {/* Vector Inputs */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
                {renderVectorInput('vectorA', 'Vector A')}
                {vectorData.operation !== 'magnitude' && renderVectorInput('vectorB', 'Vector B')}
            </div>

            {/* Quick Vector Buttons */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Quick Vectors:</label>
                <div className="flex flex-wrap gap-2">
                    {quickVectors.map((quick, index) => (
                        <button
                            key={index}
                            onClick={() => {
                                updateVector('vectorA', 'x', quick.vector.x);
                                updateVector('vectorA', 'y', quick.vector.y);
                                updateVector('vectorA', 'z', quick.vector.z);
                            }}
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
                        Calculate {vectorData.operation.charAt(0).toUpperCase() + vectorData.operation.slice(1)}
                    </button>
                )}
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={vectorData.showSteps}
                        onChange={(e) => handleFieldChange('showSteps', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Steps</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={vectorData.showVisualization}
                        onChange={(e) => handleFieldChange('showVisualization', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Visualization</span>
                </label>
            </div>

            {/* Result Display */}
            {vectorData.result !== null && (
                <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">Result:</h4>
                    <div className="text-lg font-mono text-green-700">
                        {typeof vectorData.result === 'object' && vectorData.result ? (
                            `(${vectorData.result.x?.toFixed(4) || '0.0000'}, ${vectorData.result.y?.toFixed(4) || '0.0000'}${vectorData.dimension === 3 ? `, ${vectorData.result.z?.toFixed(4) || '0.0000'}` : ''})`
                        ) : (
                            vectorData.result?.toFixed(4) || '0.0000'
                        )}
                    </div>
                    <div className="text-sm text-green-600 mt-1">
                        {vectorData.operation === 'magnitude' && 'Magnitude'}
                        {vectorData.operation === 'dot' && 'Dot Product (Scalar)'}
                        {vectorData.operation === 'cross' && 'Cross Product (Vector)'}
                        {vectorData.operation === 'angle' && 'Angle (degrees)'}
                        {(vectorData.operation === 'add' || vectorData.operation === 'subtract') && 'Result Vector'}
                    </div>
                </div>
            )}

            {/* Steps Display */}
            {renderSteps()}

            {/* Vector Properties Summary */}
            <div className="mb-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h4 className="font-semibold text-blue-800 mb-2">Vector Properties:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                    <div>
                        <strong>Vector A:</strong>
                        <div>Magnitude: {calculateMagnitude(vectorData.vectorA || { x: 0, y: 0, z: 0 })?.toFixed(4) || '0.0000'}</div>
                        <div>Unit Vector: ({((vectorData.vectorA?.x || 0) / (calculateMagnitude(vectorData.vectorA || { x: 0, y: 0, z: 0 }) || 1)).toFixed(4)}, {((vectorData.vectorA?.y || 0) / (calculateMagnitude(vectorData.vectorA || { x: 0, y: 0, z: 0 }) || 1)).toFixed(4)}{vectorData.dimension === 3 ? `, ${((vectorData.vectorA?.z || 0) / (calculateMagnitude(vectorData.vectorA || { x: 0, y: 0, z: 0 }) || 1)).toFixed(4)}` : ''})</div>
                    </div>
                    {vectorData.operation !== 'magnitude' && (
                        <div>
                            <strong>Vector B:</strong>
                            <div>Magnitude: {calculateMagnitude(vectorData.vectorB || { x: 0, y: 0, z: 0 })?.toFixed(4) || '0.0000'}</div>
                            <div>Unit Vector: ({((vectorData.vectorB?.x || 0) / (calculateMagnitude(vectorData.vectorB || { x: 0, y: 0, z: 0 }) || 1)).toFixed(4)}, {((vectorData.vectorB?.y || 0) / (calculateMagnitude(vectorData.vectorB || { x: 0, y: 0, z: 0 }) || 1)).toFixed(4)}{vectorData.dimension === 3 ? `, ${((vectorData.vectorB?.z || 0) / (calculateMagnitude(vectorData.vectorB || { x: 0, y: 0, z: 0 }) || 1)).toFixed(4)}` : ''})</div>
                        </div>
                    )}
                </div>
            </div>

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Vector Calculator Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Choose between 2D or 3D vectors</li>
                    <li>Enter vector components (x, y, z for 3D)</li>
                    <li>Select the operation: add, subtract, dot product, cross product, magnitude, or angle</li>
                    <li>View step-by-step calculations</li>
                    <li>See vector properties like magnitude and unit vectors</li>
                    <li>Use quick vector buttons for common vectors</li>
                    <li>Cross product is only available in 3D</li>
                </ul>
            </div>
        </div>
    );
};

export default VectorCalculator;
