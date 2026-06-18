import React from 'react';

/**
 * Math Visual Aid Components
 * Moved from math folder to centralized visual aids structure
 * Handles functions, graphs, statistical analysis, etc.
 */

// Linear Function Graph Component
export const LinearFunctionGraph = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        m: 2,
        c: 3,
        x_range: [-5, 10],
        y_range: [-10, 25],
        showGrid: true,
        showPoints: true,
        showSlope: true,
        showYIntercept: true,
        showXIntercept: true
    });

    const handleDataChange = (field, value) => {
        const newData = { ...visualData };
        newData[field] = parseFloat(value) || 0;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateY = (x) => {
        return visualData.m * x + visualData.c;
    };

    const calculateXIntercept = () => {
        return -visualData.c / visualData.m;
    };

    const generatePoints = () => {
        const points = [];
        const step = (visualData.x_range[1] - visualData.x_range[0]) / 100;
        
        for (let x = visualData.x_range[0]; x <= visualData.x_range[1]; x += step) {
            const y = calculateY(x);
            if (y >= visualData.y_range[0] && y <= visualData.y_range[1]) {
                points.push({ x, y });
            }
        }
        return points;
    };

    const points = generatePoints();

    return (
        <div className="linear-function-graph bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Linear Function: f(x) = {visualData.m}x + {visualData.c}
            </h3>
            
            {/* Controls */}
            {mode === 'user-interactive' && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Slope (m)</label>
                        <input
                            type="number"
                            value={visualData.m}
                            onChange={(e) => handleDataChange('m', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Y-Intercept (c)</label>
                        <input
                            type="number"
                            value={visualData.c}
                            onChange={(e) => handleDataChange('c', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">X Range Start</label>
                        <input
                            type="number"
                            value={visualData.x_range[0]}
                            onChange={(e) => {
                                const newData = { ...visualData };
                                newData.x_range[0] = parseFloat(e.target.value);
                                setVisualData(newData);
                                if (onVisualAidChange) onVisualAidChange(newData);
                            }}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">X Range End</label>
                        <input
                            type="number"
                            value={visualData.x_range[1]}
                            onChange={(e) => {
                                const newData = { ...visualData };
                                newData.x_range[1] = parseFloat(e.target.value);
                                setVisualData(newData);
                                if (onVisualAidChange) onVisualAidChange(newData);
                            }}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                </div>
            )}

            {/* Graph Display */}
            <div className="border border-gray-300 rounded-lg p-4 bg-gray-50">
                <div className="text-center mb-4">
                    <div className="inline-block bg-blue-100 px-4 py-2 rounded-lg">
                        <span className="font-medium">Function:</span> f(x) = {visualData.m}x + {visualData.c}
                    </div>
                </div>
                
                {/* Simple ASCII Graph Representation */}
                <div className="font-mono text-xs text-center">
                    <div className="mb-2">Y</div>
                    {Array.from({ length: 10 }, (_, i) => {
                        const y = visualData.y_range[1] - (i * (visualData.y_range[1] - visualData.y_range[0]) / 9);
                        const x = calculateXIntercept();
                        const isOnLine = Math.abs(y - calculateY(x)) < 0.1;
                        
                        return (
                            <div key={i} className="flex justify-center items-center h-4">
                                <span className="w-8 text-right pr-2">{y.toFixed(1)}</span>
                                <div className="w-64 h-full border-l border-gray-300 relative">
                                    {isOnLine && <span className="absolute left-0 text-blue-600">●</span>}
                                </div>
                            </div>
                        );
                    })}
                    <div className="flex justify-center items-center h-4">
                        <span className="w-8 text-right pr-2">{visualData.y_range[0].toFixed(1)}</span>
                        <div className="w-64 h-full border-l border-gray-300"></div>
                    </div>
                    <div className="flex justify-center mt-2">
                        <span className="w-8"></span>
                        <div className="w-64 text-center">
                            {visualData.x_range[0].toFixed(1)} X {visualData.x_range[1].toFixed(1)}
                        </div>
                    </div>
                </div>
            </div>

            {/* Function Properties */}
            <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-blue-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-blue-600 font-medium">Slope</div>
                    <div className="text-xl font-bold text-blue-800">{visualData.m}</div>
                    <div className="text-xs text-blue-600">
                        {visualData.m > 0 ? 'Increasing' : visualData.m < 0 ? 'Decreasing' : 'Constant'}
                    </div>
                </div>
                <div className="bg-green-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-green-600 font-medium">Y-Intercept</div>
                    <div className="text-xl font-bold text-green-800">({visualData.c})</div>
                    <div className="text-xs text-green-600">Point (0, {visualData.c})</div>
                </div>
                <div className="bg-purple-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-purple-600 font-medium">X-Intercept</div>
                    <div className="text-xl font-bold text-purple-800">({calculateXIntercept().toFixed(2)}, 0)</div>
                    <div className="text-xs text-purple-600">Root of function</div>
                </div>
            </div>

            {/* Sample Points */}
            {visualData.showPoints && (
                <div className="mt-6">
                    <h4 className="text-lg font-semibold text-gray-800 mb-3">Sample Points</h4>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        {[-2, -1, 0, 1, 2, 3, 4, 5].map(x => (
                            <div key={x} className="bg-gray-50 p-3 rounded-lg text-center">
                                <div className="text-sm text-gray-600">x = {x}</div>
                                <div className="font-medium">f({x}) = {calculateY(x)}</div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

// Quadratic Function Graph Component
export const QuadraticFunctionGraph = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        a: 1,
        b: -4,
        c: 3,
        x_range: [-2, 6],
        y_range: [-2, 8],
        showGrid: true,
        showPoints: true,
        showVertex: true,
        showRoots: true
    });

    const handleDataChange = (field, value) => {
        const newData = { ...visualData };
        newData[field] = parseFloat(value) || 0;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateY = (x) => {
        return visualData.a * x * x + visualData.b * x + visualData.c;
    };

    const calculateVertex = () => {
        const x = -visualData.b / (2 * visualData.a);
        const y = calculateY(x);
        return { x, y };
    };

    const calculateRoots = () => {
        const discriminant = visualData.b * visualData.b - 4 * visualData.a * visualData.c;
        if (discriminant < 0) return [];
        if (discriminant === 0) {
            const x = -visualData.b / (2 * visualData.a);
            return [x];
        }
        const x1 = (-visualData.b + Math.sqrt(discriminant)) / (2 * visualData.a);
        const x2 = (-visualData.b - Math.sqrt(discriminant)) / (2 * visualData.a);
        return [x1, x2];
    };

    const vertex = calculateVertex();
    const roots = calculateRoots();

    return (
        <div className="quadratic-function-graph bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Quadratic Function: f(x) = {visualData.a}x² + {visualData.b}x + {visualData.c}
            </h3>
            
            {/* Controls */}
            {mode === 'user-interactive' && (
                <div className="grid grid-cols-3 gap-4 mb-6">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient a</label>
                        <input
                            type="number"
                            value={visualData.a}
                            onChange={(e) => handleDataChange('a', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient b</label>
                        <input
                            type="number"
                            value={visualData.b}
                            onChange={(e) => handleDataChange('b', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient c</label>
                        <input
                            type="number"
                            value={visualData.c}
                            onChange={(e) => handleDataChange('c', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                        />
                    </div>
                </div>
            )}

            {/* Graph Display */}
            <div className="border border-gray-300 rounded-lg p-4 bg-gray-50">
                <div className="text-center mb-4">
                    <div className="inline-block bg-green-100 px-4 py-2 rounded-lg">
                        <span className="font-medium">Function:</span> f(x) = {visualData.a}x² + {visualData.b}x + {visualData.c}
                    </div>
                </div>
                
                {/* Simple ASCII Graph Representation */}
                <div className="font-mono text-xs text-center">
                    <div className="mb-2">Y</div>
                    {Array.from({ length: 10 }, (_, i) => {
                        const y = visualData.y_range[1] - (i * (visualData.y_range[1] - visualData.y_range[0]) / 9);
                        const x = vertex.x;
                        const isOnLine = Math.abs(y - calculateY(x)) < 0.1;
                        
                        return (
                            <div key={i} className="flex justify-center items-center h-4">
                                <span className="w-8 text-right pr-2">{y.toFixed(1)}</span>
                                <div className="w-64 h-full border-l border-gray-300 relative">
                                    {isOnLine && <span className="absolute left-0 text-green-600">●</span>}
                                </div>
                            </div>
                        );
                    })}
                    <div className="flex justify-center items-center h-4">
                        <span className="w-8 text-right pr-2">{visualData.y_range[0].toFixed(1)}</span>
                        <div className="w-64 h-full border-l border-gray-300"></div>
                    </div>
                    <div className="flex justify-center mt-2">
                        <span className="w-8"></span>
                        <div className="w-64 text-center">
                            {visualData.x_range[0].toFixed(1)} X {visualData.x_range[1].toFixed(1)}
                        </div>
                    </div>
                </div>
            </div>

            {/* Function Properties */}
            <div className="mt-6 grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="bg-green-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-green-600 font-medium">Direction</div>
                    <div className="text-xl font-bold text-green-800">
                        {visualData.a > 0 ? 'Upward' : 'Downward'}
                    </div>
                    <div className="text-xs text-green-600">
                        {visualData.a > 0 ? 'Opens up' : 'Opens down'}
                    </div>
                </div>
                <div className="bg-blue-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-blue-600 font-medium">Vertex</div>
                    <div className="text-xl font-bold text-blue-800">
                        ({vertex.x.toFixed(2)}, {vertex.y.toFixed(2)})
                    </div>
                    <div className="text-xs text-blue-600">
                        {visualData.a > 0 ? 'Minimum' : 'Maximum'} point
                    </div>
                </div>
                <div className="bg-purple-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-purple-600 font-medium">Axis of Symmetry</div>
                    <div className="text-xl font-bold text-purple-800">x = {vertex.x.toFixed(2)}</div>
                    <div className="text-xs text-purple-600">Vertical line</div>
                </div>
                <div className="bg-orange-50 p-4 rounded-lg text-center">
                    <div className="text-sm text-orange-600 font-medium">Roots</div>
                    <div className="text-xl font-bold text-orange-800">
                        {roots.length === 0 ? 'None' : roots.length === 1 ? roots[0].toFixed(2) : `${roots[0].toFixed(2)}, ${roots[1].toFixed(2)}`}
                    </div>
                    <div className="text-xs text-orange-600">
                        {roots.length === 0 ? 'No real roots' : roots.length === 1 ? 'Double root' : 'Two roots'}
                    </div>
                </div>
            </div>

            {/* Sample Points */}
            {visualData.showPoints && (
                <div className="mt-6">
                    <h4 className="text-lg font-semibold text-gray-800 mb-3">Sample Points</h4>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        {[-1, 0, 1, 2, 3, 4, 5, 6].map(x => (
                            <div key={x} className="bg-gray-50 p-3 rounded-lg text-center">
                                <div className="text-sm text-gray-600">x = {x}</div>
                                <div className="font-medium">f({x}) = {calculateY(x).toFixed(2)}</div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

// Box and Whisker Plot Component
export const BoxWhiskerPlot = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        dataSet: [
            {
                label: "Test Scores",
                values: [45, 52, 58, 62, 65, 68, 72, 75, 78, 82, 85, 88, 92, 95, 98]
            }
        ],
        showOutliers: true,
        showMean: true,
        showMedian: true,
        showQuartiles: true
    });

    const calculateStatistics = (values) => {
        const sorted = [...values].sort((a, b) => a - b);
        const n = sorted.length;
        
        const min = sorted[0];
        const max = sorted[n - 1];
        const q1 = sorted[Math.floor(n * 0.25)];
        const median = sorted[Math.floor(n * 0.5)];
        const q3 = sorted[Math.floor(n * 0.75)];
        const mean = values.reduce((sum, val) => sum + val, 0) / n;
        
        const iqr = q3 - q1;
        const lowerBound = q1 - 1.5 * iqr;
        const upperBound = q3 + 1.5 * iqr;
        
        const outliers = values.filter(val => val < lowerBound || val > upperBound);
        
        return { min, max, q1, median, q3, mean, iqr, outliers, lowerBound, upperBound };
    };

    const stats = calculateStatistics(visualData.dataSet[0].values);

    return (
        <div className="box-whisker-plot bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Box and Whisker Plot: {visualData.dataSet[0].label}
            </h3>
            
            {/* Plot Visualization */}
            <div className="border border-gray-300 rounded-lg p-6 bg-gray-50">
                <div className="text-center mb-4">
                    <div className="inline-block bg-purple-100 px-4 py-2 rounded-lg">
                        <span className="font-medium">Data Set:</span> {visualData.dataSet[0].label}
                    </div>
                </div>
                
                {/* ASCII Box Plot */}
                <div className="font-mono text-center text-sm">
                    <div className="mb-2">Value Scale</div>
                    <div className="flex justify-center items-center space-x-1 mb-4">
                        <span className="text-xs text-gray-500">{stats.min}</span>
                        <div className="w-8 h-1 bg-gray-400"></div>
                        <span className="text-xs text-gray-500">{stats.q1}</span>
                        <div className="w-16 h-4 bg-blue-200 border border-blue-400"></div>
                        <span className="text-xs text-gray-500">{stats.median}</span>
                        <div className="w-16 h-4 bg-blue-200 border border-blue-400"></div>
                        <span className="text-xs text-gray-500">{stats.q3}</span>
                        <div className="w-8 h-1 bg-gray-400"></div>
                        <span className="text-xs text-gray-500">{stats.max}</span>
                    </div>
                    <div className="text-xs text-gray-600">
                        Min | Q1 | Median | Q3 | Max
                    </div>
                </div>
            </div>

            {/* Statistics Display */}
            <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-blue-50 p-4 rounded-lg">
                    <h4 className="font-semibold text-blue-800 mb-3">Quartiles</h4>
                    <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                            <span>Minimum:</span>
                            <span className="font-medium">{stats.min}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Q1 (25th percentile):</span>
                            <span className="font-medium">{stats.q1}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Median (50th percentile):</span>
                            <span className="font-medium">{stats.median}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Q3 (75th percentile):</span>
                            <span className="font-medium">{stats.q3}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Maximum:</span>
                            <span className="font-medium">{stats.max}</span>
                        </div>
                    </div>
                </div>
                
                <div className="bg-green-50 p-4 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-3">Measures</h4>
                    <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                            <span>Mean:</span>
                            <span className="font-medium">{stats.mean.toFixed(2)}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Range:</span>
                            <span className="font-medium">{stats.max - stats.min}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>IQR:</span>
                            <span className="font-medium">{stats.iqr}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Data Points:</span>
                            <span className="font-medium">{visualData.dataSet[0].values.length}</span>
                        </div>
                    </div>
                </div>
                
                <div className="bg-orange-50 p-4 rounded-lg">
                    <h4 className="font-semibold text-orange-800 mb-3">Outliers</h4>
                    <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                            <span>Lower Bound:</span>
                            <span className="font-medium">{stats.lowerBound.toFixed(2)}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Upper Bound:</span>
                            <span className="font-medium">{stats.upperBound.toFixed(2)}</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Outliers:</span>
                            <span className="font-medium">{stats.outliers.length}</span>
                        </div>
                        {stats.outliers.length > 0 && (
                            <div className="text-xs text-orange-600">
                                Values: {stats.outliers.join(', ')}
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* Data Values */}
            <div className="mt-6">
                <h4 className="text-lg font-semibold text-gray-800 mb-3">Data Values</h4>
                <div className="bg-gray-50 p-4 rounded-lg">
                    <div className="text-sm text-gray-600 mb-2">
                        Sorted values: {visualData.dataSet[0].values.sort((a, b) => a - b).join(', ')}
                    </div>
                    <div className="text-xs text-gray-500">
                        Total: {visualData.dataSet[0].values.length} values
                    </div>
                </div>
            </div>
        </div>
    );
};

export default {
    LinearFunctionGraph,
    QuadraticFunctionGraph,
    BoxWhiskerPlot
};
