import React, { useState, useEffect } from 'react';

const LineGraphInput = ({ initialData, onChange, isSubmitted }) => {
    const [points, setPoints] = useState(initialData.points || [{ x: '', y: '' }]);
    const [xAxisLabel, setXAxisLabel] = useState(initialData.x_axis_label || '');
    const [yAxisLabel, setYAxisLabel] = useState(initialData.y_axis_label || '');
    const [title, setTitle] = useState(initialData.title || '');
    const [showPreview, setShowPreview] = useState(false);
    const [lineStyle, setLineStyle] = useState(initialData.lineStyle || 'solid');
    const [lineColor, setLineColor] = useState(initialData.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData.showGrid !== false);
    const [showPoints, setShowPoints] = useState(initialData.showPoints !== false);

    // Calculate statistics
    const validPoints = points.filter(p => p.x !== '' && p.y !== '');
    const sortedPoints = [...validPoints].sort((a, b) => Number(a.x) - Number(b.x));
    const xValues = validPoints.map(p => Number(p.x));
    const yValues = validPoints.map(p => Number(p.y));
    const xMin = Math.min(...xValues, 0);
    const xMax = Math.max(...xValues, 0);
    const yMin = Math.min(...yValues, 0);
    const yMax = Math.max(...yValues, 0);

    useEffect(() => {
        const formattedData = {
            type: "line_graph",
            title: title,
            x_axis_label: xAxisLabel,
            y_axis_label: yAxisLabel,
            lineStyle: lineStyle,
            lineColor: lineColor,
            showGrid: showGrid,
            showPoints: showPoints,
            points: validPoints.map(p => ({ x: Number(p.x) || 0, y: Number(p.y) || 0 }))
        };
        onChange(formattedData);
    }, [points, xAxisLabel, yAxisLabel, title, lineStyle, lineColor, showGrid, showPoints, onChange]);

    const handleAddRow = () => { 
        if (!isSubmitted) setPoints([...points, { x: '', y: '' }]); 
    };
    
    const handleRemoveRow = (indexToRemove) => { 
        if (!isSubmitted) setPoints(points.filter((_, index) => index !== indexToRemove)); 
    };
    
    const handlePointChange = (index, field, value) => {
        if (isSubmitted) return;
        const newPoints = [...points];
        newPoints[index] = { ...newPoints[index], [field]: value };
        setPoints(newPoints);
    };

    const handleSortPoints = () => {
        if (!isSubmitted) {
            const sorted = [...points].sort((a, b) => {
                if (a.x === '' || b.x === '') return 0;
                return Number(a.x) - Number(b.x);
            });
            setPoints(sorted);
        }
    };

    const calculateSlope = (x1, y1, x2, y2) => {
        if (x2 - x1 === 0) return 'undefined';
        return ((y2 - y1) / (x2 - x1)).toFixed(2);
    };

    const getTrend = () => {
        if (sortedPoints.length < 2) return 'Insufficient data';
        
        const firstPoint = sortedPoints[0];
        const lastPoint = sortedPoints[sortedPoints.length - 1];
        const slope = calculateSlope(firstPoint.x, firstPoint.y, lastPoint.x, lastPoint.y);
        
        if (slope === 'undefined') return 'Vertical line';
        if (slope > 0) return 'Increasing trend';
        if (slope < 0) return 'Decreasing trend';
        return 'No trend (horizontal line)';
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Line Graph Builder</h3>
                <button
                    onClick={() => setShowPreview(!showPreview)}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                        showPreview 
                            ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                            : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                >
                    {showPreview ? 'Hide Preview' : 'Show Preview'}
                </button>
            </div>

            {/* Chart Configuration */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Chart Title:</label>
                    <input 
                        type="text" 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={title} 
                        onChange={(e) => !isSubmitted && setTitle(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="e.g., Temperature Over Time" 
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">X-Axis Label:</label>
                    <input 
                        type="text" 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={xAxisLabel} 
                        onChange={(e) => !isSubmitted && setXAxisLabel(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="e.g., Time (hours)" 
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Y-Axis Label:</label>
                    <input 
                        type="text" 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={yAxisLabel} 
                        onChange={(e) => !isSubmitted && setYAxisLabel(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="e.g., Temperature (°C)" 
                    />
                </div>
            </div>

            {/* Line Styling Options */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Line Style:</label>
                    <select 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={lineStyle} 
                        onChange={(e) => !isSubmitted && setLineStyle(e.target.value)} 
                        disabled={isSubmitted}
                    >
                        <option value="solid">Solid Line</option>
                        <option value="dashed">Dashed Line</option>
                        <option value="dotted">Dotted Line</option>
                        <option value="dash-dot">Dash-Dot Line</option>
                    </select>
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Line Color:</label>
                    <input 
                        type="color" 
                        className="w-full h-12 border border-gray-300 rounded-lg cursor-pointer" 
                        value={lineColor} 
                        onChange={(e) => !isSubmitted && setLineColor(e.target.value)} 
                        disabled={isSubmitted} 
                    />
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showGrid} 
                            onChange={(e) => !isSubmitted && setShowGrid(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Show Grid</span>
                    </label>
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showPoints} 
                            onChange={(e) => !isSubmitted && setShowPoints(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Show Points</span>
                    </label>
                </div>
            </div>

            {/* Data Input Table */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <div className="flex items-center justify-between mb-4">
                    <h4 className="text-md font-medium text-gray-800">Data Points (X, Y Coordinates)</h4>
                    <div className="flex space-x-2">
                        {!isSubmitted && (
                            <button 
                                onClick={handleSortPoints} 
                                className="px-4 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700 transition-colors flex items-center space-x-2"
                                title="Sort points by X value"
                            >
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 4h13M3 8h9m-9 4h6m4 0l4-4m0 0l4 4m-4-4v12" />
                                </svg>
                                <span>Sort</span>
                            </button>
                        )}
                        {!isSubmitted && (
                            <button 
                                onClick={handleAddRow} 
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors flex items-center space-x-2"
                            >
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                                </svg>
                                <span>Add Point</span>
                            </button>
                        )}
                    </div>
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full divide-y divide-gray-200">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">X-Value</th>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Y-Value</th>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Coordinate</th>
                                {!isSubmitted && <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>}
                            </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                            {points.map((point, index) => (
                                <tr key={index} className="hover:bg-gray-50 transition-colors">
                                    <td className="px-4 py-3">
                                        <input 
                                            type="number" 
                                            className="w-full p-2 border border-gray-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                            value={point.x} 
                                            onChange={(e) => handlePointChange(index, 'x', e.target.value)} 
                                            placeholder="X" 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3">
                                        <input 
                                            type="number" 
                                            className="w-full p-2 border border-gray-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                            value={point.y} 
                                            onChange={(e) => handlePointChange(index, 'y', e.target.value)} 
                                            placeholder="Y" 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3 text-sm text-gray-600 font-mono">
                                        {point.x && point.y ? `(${point.x}, ${point.y})` : '-'}
                                    </td>
                                    {!isSubmitted && (
                                        <td className="px-4 py-3">
                                            <button 
                                                onClick={() => handleRemoveRow(index)} 
                                                className="text-red-600 hover:text-red-800 hover:bg-red-50 p-2 rounded-md transition-colors"
                                                title="Remove this data point"
                                            >
                                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                                </svg>
                                            </button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>

            {/* Statistics and Analysis */}
            {validPoints.length > 0 && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6 p-4 bg-green-50 rounded-lg">
                    <div className="text-center">
                        <div className="text-2xl font-bold text-green-600">{validPoints.length}</div>
                        <div className="text-sm text-green-700">Data Points</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{getTrend()}</div>
                        <div className="text-sm text-blue-700">Trend</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-purple-600">{xMin} to {xMax}</div>
                        <div className="text-sm text-purple-700">X Range</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-orange-600">{yMin} to {yMax}</div>
                        <div className="text-sm text-orange-700">Y Range</div>
                    </div>
                </div>
            )}

            {/* Interactive Chart Preview */}
            {showPreview && validPoints.length > 0 && (
                <div className="border border-gray-200 rounded-lg p-6 bg-white">
                    <h4 className="text-lg font-medium text-gray-800 mb-4">Chart Preview</h4>
                    <div className="h-64 border border-gray-200 rounded-lg bg-gray-50 p-4 relative">
                        {/* Grid Lines */}
                        {showGrid && (
                            <div className="absolute inset-0 pointer-events-none">
                                {Array.from({ length: 11 }, (_, i) => (
                                    <div key={i} className="absolute w-full h-px bg-gray-200" style={{ top: `${i * 10}%` }}></div>
                                ))}
                                {Array.from({ length: 11 }, (_, i) => (
                                    <div key={i} className="absolute h-full w-px bg-gray-200" style={{ left: `${i * 10}%` }}></div>
                                ))}
                            </div>
                        )}
                        
                        {/* Line Graph */}
                        <svg className="w-full h-full absolute inset-0" viewBox="0 0 100 100" preserveAspectRatio="none">
                            {sortedPoints.length > 1 && (
                                <polyline
                                    points={sortedPoints.map((point, index) => {
                                        const x = ((Number(point.x) - xMin) / (xMax - xMin)) * 100;
                                        const y = 100 - ((Number(point.y) - yMin) / (yMax - yMin)) * 100;
                                        return `${x},${y}`;
                                    }).join(' ')}
                                    fill="none"
                                    stroke={lineColor}
                                    strokeWidth="2"
                                    strokeDasharray={lineStyle === 'dashed' ? '5,5' : lineStyle === 'dotted' ? '2,2' : lineStyle === 'dash-dot' ? '5,2,2,2' : 'none'}
                                />
                            )}
                            
                            {/* Data Points */}
                            {showPoints && sortedPoints.map((point, index) => {
                                const x = ((Number(point.x) - xMin) / (xMax - xMin)) * 100;
                                const y = 100 - ((Number(point.y) - yMin) / (yMax - yMin)) * 100;
                                return (
                                    <circle
                                        key={index}
                                        cx={x}
                                        cy={y}
                                        r="3"
                                        fill={lineColor}
                                        stroke="white"
                                        strokeWidth="1"
                                    />
                                );
                            })}
                        </svg>
                        
                        {/* Axis Labels */}
                        <div className="absolute bottom-0 left-0 right-0 text-center text-xs text-gray-500">
                            {xAxisLabel || 'X-Axis'}
                        </div>
                        <div className="absolute top-0 bottom-0 left-0 text-center text-xs text-gray-500 transform -rotate-90 origin-center">
                            {yAxisLabel || 'Y-Axis'}
                        </div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Enter data points in any order - use the Sort button to organize them</li>
                    <li>• Choose line style and color to match your presentation needs</li>
                    <li>• Enable grid and points for better readability</li>
                    <li>• The trend analysis shows the overall direction of your data</li>
                </ul>
            </div>
        </div>
    );
};

export default LineGraphInput;
