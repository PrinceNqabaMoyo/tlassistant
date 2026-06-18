import React, { useState, useEffect } from 'react';
import { useGeometryBackend } from '../../../hooks/useGeometryBackend';
import GeometryDiagram from './GeometryDiagram';

/**
 * GeometryBackendTest Component
 * Test component to demonstrate the Python backend integration
 */
const GeometryBackendTest = () => {
    const { generateDiagram, calculateProperties, getAvailableDiagrams, loading, error } = useGeometryBackend();
    const [availableDiagrams, setAvailableDiagrams] = useState(null);
    const [testResults, setTestResults] = useState([]);

    useEffect(() => {
        loadAvailableDiagrams();
    }, []);

    const loadAvailableDiagrams = async () => {
        try {
            const diagrams = await getAvailableDiagrams();
            setAvailableDiagrams(diagrams);
        } catch (err) {
            console.error('Failed to load available diagrams:', err);
        }
    };

    const testDiagramGeneration = async (diagramType, parameters) => {
        try {
            const result = await generateDiagram(diagramType, '2d', parameters);
            setTestResults(prev => [...prev, {
                type: 'diagram',
                diagramType,
                result,
                timestamp: new Date().toLocaleTimeString()
            }]);
        } catch (err) {
            setTestResults(prev => [...prev, {
                type: 'error',
                message: err.message,
                timestamp: new Date().toLocaleTimeString()
            }]);
        }
    };

    const testPropertyCalculation = async (shape, parameters) => {
        try {
            const result = await calculateProperties(shape, parameters, true);
            setTestResults(prev => [...prev, {
                type: 'calculation',
                shape,
                result,
                timestamp: new Date().toLocaleTimeString()
            }]);
        } catch (err) {
            setTestResults(prev => [...prev, {
                type: 'error',
                message: err.message,
                timestamp: new Date().toLocaleTimeString()
            }]);
        }
    };

    const runTests = () => {
        setTestResults([]);
        
        // Test basic 2D diagrams
        testDiagramGeneration('point', { x: 0, y: 0, label: 'P' });
        testDiagramGeneration('line', { start: [-2, 0], end: [2, 0], label: 'AB' });
        testDiagramGeneration('circle', { center: [0, 0], radius: 2 });
        testDiagramGeneration('triangle', { vertices: [[-1, -1], [1, -1], [0, 1]] });
        
        // Test property calculations
        testPropertyCalculation('circle', { radius: 3 });
        testPropertyCalculation('rectangle', { length: 4, width: 3 });
        testPropertyCalculation('triangle', { base: 4, height: 3 });
    };

    return (
        <div className="p-6 max-w-4xl mx-auto">
            <h2 className="text-2xl font-bold mb-4">Geometry Backend Integration Test</h2>
            
            {error && (
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    <strong>Error:</strong> {error}
                </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Controls */}
                <div className="space-y-4">
                    <div className="bg-white p-4 rounded-lg border">
                        <h3 className="text-lg font-semibold mb-3">Test Controls</h3>
                        <button
                            onClick={runTests}
                            disabled={loading}
                            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:opacity-50"
                        >
                            {loading ? 'Running Tests...' : 'Run All Tests'}
                        </button>
                    </div>

                    {/* Available Diagrams */}
                    {availableDiagrams && (
                        <div className="bg-white p-4 rounded-lg border">
                            <h3 className="text-lg font-semibold mb-3">Available Diagrams</h3>
                            <div className="space-y-2">
                                <div>
                                    <h4 className="font-medium text-sm text-gray-700">2D Diagrams:</h4>
                                    <div className="text-xs text-gray-600 ml-2">
                                        {Object.keys(availableDiagrams['2d']).join(', ')}
                                    </div>
                                </div>
                                <div>
                                    <h4 className="font-medium text-sm text-gray-700">3D Diagrams:</h4>
                                    <div className="text-xs text-gray-600 ml-2">
                                        {Object.keys(availableDiagrams['3d']).join(', ')}
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}
                </div>

                {/* Test Results */}
                <div className="bg-white p-4 rounded-lg border">
                    <h3 className="text-lg font-semibold mb-3">Test Results</h3>
                    <div className="space-y-3 max-h-96 overflow-y-auto">
                        {testResults.length === 0 ? (
                            <div className="text-gray-500 text-sm">No tests run yet. Click "Run All Tests" to start.</div>
                        ) : (
                            testResults.map((result, index) => (
                                <div key={index} className="border-l-4 border-blue-500 pl-3 py-2">
                                    <div className="text-xs text-gray-500">{result.timestamp}</div>
                                    {result.type === 'error' ? (
                                        <div className="text-red-600 text-sm">{result.message}</div>
                                    ) : result.type === 'diagram' ? (
                                        <div>
                                            <div className="text-sm font-medium">Generated {result.diagramType} diagram</div>
                                            {result.result?.image_data && (
                                                <img 
                                                    src={result.result.image_data} 
                                                    alt={`${result.diagramType} diagram`}
                                                    className="mt-2 max-w-32 h-auto"
                                                />
                                            )}
                                        </div>
                                    ) : result.type === 'calculation' ? (
                                        <div>
                                            <div className="text-sm font-medium">{result.shape} calculations</div>
                                            <div className="text-xs text-gray-600 mt-1">{result.result?.calculations}</div>
                                            {result.result?.diagram && (
                                                <img 
                                                    src={result.result.diagram} 
                                                    alt={`${result.shape} diagram`}
                                                    className="mt-2 max-w-32 h-auto"
                                                />
                                            )}
                                        </div>
                                    ) : null}
                                </div>
                            ))
                        )}
                    </div>
                </div>
            </div>

            {/* Quick Test Examples */}
            <div className="mt-6 bg-white p-4 rounded-lg border">
                <h3 className="text-lg font-semibold mb-3">Quick Test Examples</h3>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <button
                        onClick={() => testDiagramGeneration('point', { x: 0, y: 0, label: 'A' })}
                        className="bg-green-500 hover:bg-green-700 text-white text-sm py-2 px-3 rounded"
                    >
                        Test Point
                    </button>
                    <button
                        onClick={() => testDiagramGeneration('line', { start: [-2, 0], end: [2, 0], label: 'AB' })}
                        className="bg-green-500 hover:bg-green-700 text-white text-sm py-2 px-3 rounded"
                    >
                        Test Line
                    </button>
                    <button
                        onClick={() => testDiagramGeneration('circle', { center: [0, 0], radius: 2 })}
                        className="bg-green-500 hover:bg-green-700 text-white text-sm py-2 px-3 rounded"
                    >
                        Test Circle
                    </button>
                    <button
                        onClick={() => testPropertyCalculation('circle', { radius: 2 })}
                        className="bg-purple-500 hover:bg-purple-700 text-white text-sm py-2 px-3 rounded"
                    >
                        Test Circle Calc
                    </button>
                </div>
            </div>
        </div>
    );
};

export default GeometryBackendTest;




