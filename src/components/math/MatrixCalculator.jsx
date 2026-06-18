import React, { useState, useEffect } from 'react';

const MatrixCalculator = ({ initialData, onChange, isSubmitted }) => {
    const [matrixData, setMatrixData] = useState(initialData || {
        title: "Matrix Calculator",
        operation: 'add', // 'add', 'multiply', 'determinant', 'inverse', 'solve'
        matrixA: { rows: 2, cols: 2, data: [[1, 0], [0, 1]] },
        matrixB: { rows: 2, cols: 2, data: [[1, 0], [0, 1]] },
        showSteps: true,
        showResult: true,
        result: null,
        steps: []
    });

    useEffect(() => {
        // Ensure all required properties are initialized
        if (matrixData.result === undefined) {
            setMatrixData(prev => ({ ...prev, result: null }));
            return;
        }
        if (!matrixData.steps) {
            setMatrixData(prev => ({ ...prev, steps: [] }));
            return;
        }
        if (!matrixData.matrixA) {
            setMatrixData(prev => ({ ...prev, matrixA: { rows: 2, cols: 2, data: [[1, 0], [0, 1]] } }));
            return;
        }
        if (!matrixData.matrixB) {
            setMatrixData(prev => ({ ...prev, matrixB: { rows: 2, cols: 2, data: [[1, 0], [0, 1]] } }));
            return;
        }
        
        onChange(matrixData);
    }, [matrixData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setMatrixData(prev => ({ ...prev, [field]: value }));
    };

    const updateMatrixSize = (matrixName, rows, cols) => {
        if (isSubmitted) return;
        const newData = [];
        for (let i = 0; i < rows; i++) {
            newData[i] = [];
            for (let j = 0; j < cols; j++) {
                newData[i][j] = matrixData[matrixName].data[i]?.[j] || 0;
            }
        }
        
        setMatrixData(prev => ({
            ...prev,
            [matrixName]: { rows, cols, data: newData }
        }));
    };

    const updateMatrixElement = (matrixName, row, col, value) => {
        if (isSubmitted) return;
        setMatrixData(prev => ({
            ...prev,
            [matrixName]: {
                ...prev[matrixName],
                data: prev[matrixName].data.map((r, i) =>
                    i === row ? r.map((c, j) => j === col ? parseFloat(value) || 0 : c) : r
                )
            }
        }));
    };

    const createIdentityMatrix = (size) => {
        const matrix = [];
        for (let i = 0; i < size; i++) {
            matrix[i] = [];
            for (let j = 0; j < size; j++) {
                matrix[i][j] = i === j ? 1 : 0;
            }
        }
        return matrix;
    };

    const createZeroMatrix = (rows, cols) => {
        const matrix = [];
        for (let i = 0; i < rows; i++) {
            matrix[i] = [];
            for (let j = 0; j < cols; j++) {
                matrix[i][j] = 0;
            }
        }
        return matrix;
    };

    const addMatrices = (a, b) => {
        const result = [];
        for (let i = 0; i < a.rows; i++) {
            result[i] = [];
            for (let j = 0; j < a.cols; j++) {
                result[i][j] = a.data[i][j] + b.data[i][j];
            }
        }
        return result;
    };

    const multiplyMatrices = (a, b) => {
        const result = [];
        for (let i = 0; i < a.rows; i++) {
            result[i] = [];
            for (let j = 0; j < b.cols; j++) {
                result[i][j] = 0;
                for (let k = 0; k < a.cols; k++) {
                    result[i][j] += a.data[i][k] * b.data[k][j];
                }
            }
        }
        return result;
    };

    const calculateDeterminant = (matrix) => {
        const size = matrix.length;
        if (size === 1) return matrix[0][0];
        if (size === 2) {
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
        }
        
        let det = 0;
        for (let j = 0; j < size; j++) {
            const minor = [];
            for (let i = 1; i < size; i++) {
                minor[i - 1] = [];
                for (let k = 0; k < size; k++) {
                    if (k !== j) {
                        minor[i - 1].push(matrix[i][k]);
                    }
                }
            }
            det += matrix[0][j] * Math.pow(-1, j) * calculateDeterminant(minor);
        }
        return det;
    };

    const calculateInverse = (matrix) => {
        const det = calculateDeterminant(matrix);
        if (Math.abs(det) < 1e-10) return null; // Matrix is not invertible
        
        const size = matrix.length;
        const adjoint = [];
        
        for (let i = 0; i < size; i++) {
            adjoint[i] = [];
            for (let j = 0; j < size; j++) {
                const minor = [];
                for (let r = 0; r < size; r++) {
                    if (r !== i) {
                        minor[r > i ? r - 1 : r] = [];
                        for (let c = 0; c < size; c++) {
                            if (c !== j) {
                                minor[r > i ? r - 1 : r].push(matrix[r][c]);
                            }
                        }
                    }
                }
                adjoint[i][j] = Math.pow(-1, i + j) * calculateDeterminant(minor);
            }
        }
        
        // Transpose the adjoint
        const transposed = [];
        for (let i = 0; i < size; i++) {
            transposed[i] = [];
            for (let j = 0; j < size; j++) {
                transposed[i][j] = adjoint[j][i];
            }
        }
        
        // Multiply by 1/det
        const inverse = [];
        for (let i = 0; i < size; i++) {
            inverse[i] = [];
            for (let j = 0; j < size; j++) {
                inverse[i][j] = transposed[i][j] / det;
            }
        }
        
        return inverse;
    };

    const performOperation = () => {
        const { matrixA, matrixB, operation } = matrixData;
        const steps = [];
        let result = null;

        steps.push({
            step: 1,
            description: "Input Matrix A",
            expression: `Matrix A (${matrixA.rows}×${matrixA.cols}):`,
            matrix: matrixA.data,
            explanation: `Matrix A with dimensions ${matrixA.rows}×${matrixA.cols}`
        });

        if (operation !== 'determinant' && operation !== 'inverse') {
            steps.push({
                step: 2,
                description: "Input Matrix B",
                expression: `Matrix B (${matrixB.rows}×${matrixB.cols}):`,
                matrix: matrixB.data,
                explanation: `Matrix B with dimensions ${matrixB.rows}×${matrixB.cols}`
            });
        }

        switch (operation) {
            case 'add':
                if (matrixA.rows !== matrixB.rows || matrixA.cols !== matrixB.cols) {
                    result = "Error: Matrices must have the same dimensions for addition";
                } else {
                    result = addMatrices(matrixA, matrixB);
                    steps.push({
                        step: 3,
                        description: "Matrix Addition",
                        expression: "A + B = C",
                        matrix: result,
                        explanation: "Add corresponding elements of matrices A and B"
                    });
                }
                break;

            case 'multiply':
                if (matrixA.cols !== matrixB.rows) {
                    result = "Error: Number of columns in A must equal number of rows in B";
                } else {
                    result = multiplyMatrices(matrixA, matrixB);
                    steps.push({
                        step: 3,
                        description: "Matrix Multiplication",
                        expression: "A × B = C",
                        matrix: result,
                        explanation: "Multiply matrices using row-by-column method"
                    });
                }
                break;

            case 'determinant':
                if (matrixA.rows !== matrixA.cols) {
                    result = "Error: Matrix must be square to calculate determinant";
                } else {
                    result = calculateDeterminant(matrixA.data);
                    steps.push({
                        step: 3,
                        description: "Determinant Calculation",
                        expression: `det(A) = ${result}`,
                        explanation: "Calculate determinant using expansion by minors"
                    });
                }
                break;

            case 'inverse':
                if (matrixA.rows !== matrixA.cols) {
                    result = "Error: Matrix must be square to calculate inverse";
                } else {
                    result = calculateInverse(matrixA.data);
                    if (result === null) {
                        result = "Error: Matrix is not invertible (determinant = 0)";
                    } else {
                        steps.push({
                            step: 3,
                            description: "Matrix Inverse",
                            expression: "A⁻¹ = (1/det(A)) × adj(A)",
                            matrix: result,
                            explanation: "Calculate inverse using adjoint method"
                        });
                    }
                }
                break;

            default:
                result = null;
        }

        setMatrixData(prev => ({
            ...prev,
            result,
            steps
        }));
    };

    const renderMatrix = (matrix, label) => {
        return (
            <div className="mb-4">
                <h4 className="font-semibold text-gray-700 mb-2">{label}</h4>
                <div className="overflow-x-auto">
                    <table className="border-collapse border border-gray-300">
                        <tbody>
                            {matrix.map((row, i) => (
                                <tr key={i}>
                                    {row.map((cell, j) => (
                                        <td key={j} className="border border-gray-300 p-2 w-16 h-12">
                                            <input
                                                type="number"
                                                className="w-full h-full text-center border-none focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                value={cell}
                                                onChange={(e) => updateMatrixElement(label === 'Matrix A' ? 'matrixA' : 'matrixB', i, j, e.target.value)}
                                                disabled={isSubmitted}
                                                step="any"
                                            />
                                        </td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    };

    const renderSteps = () => {
        if (!matrixData.showSteps || !matrixData.steps || matrixData.steps.length === 0) return null;

        return (
            <div className="mb-4">
                <h4 className="font-semibold text-gray-700 mb-2">Step-by-Step Solution:</h4>
                <div className="space-y-3">
                    {matrixData.steps.map((step, index) => (
                        <div key={index} className="p-3 bg-white border border-gray-200 rounded-lg">
                            <div className="flex items-start space-x-3">
                                <div className="flex-shrink-0 w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">
                                    {step.step}
                                </div>
                                <div className="flex-1">
                                    <div className="font-medium text-gray-700 mb-1">{step.description}</div>
                                    <div className="text-lg font-mono text-blue-600 mb-1">{step.expression}</div>
                                    {step.matrix && (
                                        <div className="mb-2">
                                            <table className="border-collapse border border-gray-300">
                                                <tbody>
                                                    {step.matrix.map((row, i) => (
                                                        <tr key={i}>
                                                            {row.map((cell, j) => (
                                                                <td key={j} className="border border-gray-300 p-1 w-12 h-8 text-center text-sm">
                                                                    {typeof cell === 'number' ? cell.toFixed(3) : cell}
                                                                </td>
                                                            ))}
                                                        </tr>
                                                    ))}
                                                </tbody>
                                            </table>
                                        </div>
                                    )}
                                    <div className="text-sm text-gray-600">{step.explanation}</div>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    const quickMatrices = [
        { name: "Identity 2×2", matrix: { rows: 2, cols: 2, data: createIdentityMatrix(2) } },
        { name: "Identity 3×3", matrix: { rows: 3, cols: 3, data: createIdentityMatrix(3) } },
        { name: "Zero 2×2", matrix: { rows: 2, cols: 2, data: createZeroMatrix(2, 2) } },
        { name: "Zero 3×3", matrix: { rows: 3, cols: 3, data: createZeroMatrix(3, 3) } }
    ];

    // Don't render if not properly initialized
    if (!matrixData.matrixA || !matrixData.matrixB) {
        return (
            <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
                <h3 className="font-semibold text-gray-700 mb-4">Matrix Calculator</h3>
                <div className="text-center py-8 text-gray-500">
                    <p>Loading matrix calculator configuration...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Matrix Calculator</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={matrixData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Matrix Calculator Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Operation:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={matrixData.operation}
                        onChange={(e) => handleFieldChange('operation', e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="add">Add Matrices</option>
                        <option value="multiply">Multiply Matrices</option>
                        <option value="determinant">Calculate Determinant</option>
                        <option value="inverse">Calculate Inverse</option>
                    </select>
                </div>
            </div>

            {/* Matrix Size Controls */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Matrix A Size:</label>
                    <div className="flex space-x-2">
                        <select
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            value={matrixData.matrixA.rows}
                            onChange={(e) => updateMatrixSize('matrixA', parseInt(e.target.value), matrixData.matrixA.cols)}
                            disabled={isSubmitted}
                        >
                            {[1, 2, 3, 4, 5].map(size => (
                                <option key={size} value={size}>{size}</option>
                            ))}
                        </select>
                        <span className="self-center text-gray-500">×</span>
                        <select
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            value={matrixData.matrixA.cols}
                            onChange={(e) => updateMatrixSize('matrixA', matrixData.matrixA.rows, parseInt(e.target.value))}
                            disabled={isSubmitted}
                        >
                            {[1, 2, 3, 4, 5].map(size => (
                                <option key={size} value={size}>{size}</option>
                            ))}
                        </select>
                    </div>
                </div>
                
                {matrixData.operation !== 'determinant' && matrixData.operation !== 'inverse' && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Matrix B Size:</label>
                        <div className="flex space-x-2">
                            <select
                                className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                                value={matrixData.matrixB.rows}
                                onChange={(e) => updateMatrixSize('matrixB', parseInt(e.target.value), matrixData.matrixB.cols)}
                                disabled={isSubmitted}
                            >
                                {[1, 2, 3, 4, 5].map(size => (
                                    <option key={size} value={size}>{size}</option>
                                ))}
                            </select>
                            <span className="self-center text-gray-500">×</span>
                            <select
                                className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                                value={matrixData.matrixB.cols}
                                onChange={(e) => updateMatrixSize('matrixB', matrixData.matrixB.rows, parseInt(e.target.value))}
                                disabled={isSubmitted}
                            >
                                {[1, 2, 3, 4, 5].map(size => (
                                    <option key={size} value={size}>{size}</option>
                                ))}
                            </select>
                        </div>
                    </div>
                )}
            </div>

            {/* Matrix Inputs */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
                {renderMatrix(matrixData.matrixA.data, 'Matrix A')}
                {matrixData.operation !== 'determinant' && matrixData.operation !== 'inverse' && 
                 renderMatrix(matrixData.matrixB.data, 'Matrix B')}
            </div>

            {/* Quick Matrix Buttons */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Quick Matrices:</label>
                <div className="flex flex-wrap gap-2">
                    {quickMatrices.map((quick, index) => (
                        <button
                            key={index}
                            onClick={() => {
                                updateMatrixSize('matrixA', quick.matrix.rows, quick.matrix.cols);
                                setMatrixData(prev => ({
                                    ...prev,
                                    matrixA: quick.matrix
                                }));
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
                        Calculate {matrixData.operation.charAt(0).toUpperCase() + matrixData.operation.slice(1)}
                    </button>
                )}
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={matrixData.showSteps}
                        onChange={(e) => handleFieldChange('showSteps', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Steps</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={matrixData.showResult}
                        onChange={(e) => handleFieldChange('showResult', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Result</span>
                </label>
            </div>

            {/* Result Display */}
            {matrixData.result && matrixData.showResult && (
                <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">Result:</h4>
                    {typeof matrixData.result === 'string' ? (
                        <div className="text-red-600">{matrixData.result}</div>
                    ) : (
                        <div>
                            <div className="text-sm text-green-600 mb-2">
                                {matrixData.operation === 'add' && 'Matrix Addition Result'}
                                {matrixData.operation === 'multiply' && 'Matrix Multiplication Result'}
                                {matrixData.operation === 'determinant' && 'Determinant'}
                                {matrixData.operation === 'inverse' && 'Matrix Inverse'}
                            </div>
                            <div className="overflow-x-auto">
                                <table className="border-collapse border border-gray-300">
                                    <tbody>
                                        {matrixData.result.map((row, i) => (
                                            <tr key={i}>
                                                {row.map((cell, j) => (
                                                    <td key={j} className="border border-gray-300 p-2 w-16 h-12 text-center">
                                                        {typeof cell === 'number' ? cell.toFixed(3) : cell}
                                                    </td>
                                                ))}
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    )}
                </div>
            )}

            {/* Steps Display */}
            {renderSteps()}

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Matrix Calculator Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Set matrix dimensions using the size controls</li>
                    <li>Enter matrix elements by clicking on cells</li>
                    <li>Choose operation: add, multiply, determinant, or inverse</li>
                    <li>For addition: matrices must have same dimensions</li>
                    <li>For multiplication: columns of A must equal rows of B</li>
                    <li>For determinant/inverse: matrix must be square</li>
                    <li>Use quick matrix buttons for common matrices</li>
                    <li>View step-by-step calculations for understanding</li>
                </ul>
            </div>
        </div>
    );
};

export default MatrixCalculator;
