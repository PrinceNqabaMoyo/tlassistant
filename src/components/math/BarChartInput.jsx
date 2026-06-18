import React, { useState, useEffect } from 'react';

const BarChartInput = ({ initialData, onChange, isSubmitted }) => {
    const [points, setPoints] = useState(initialData.points || [{ label: '', y: '', color: '#3B82F6' }]);
    const [xAxisLabel, setXAxisLabel] = useState(initialData.x_axis_label || '');
    const [yAxisLabel, setYAxisLabel] = useState(initialData.y_axis_label || '');
    const [title, setTitle] = useState(initialData.title || '');
    const [showPreview, setShowPreview] = useState(false);
    const [chartTheme, setChartTheme] = useState(initialData.theme || 'default');

    // Calculate statistics
    const validPoints = points.filter(p => p.label.trim() !== '' && p.y !== '');
    const total = validPoints.reduce((sum, p) => sum + (Number(p.y) || 0), 0);
    const maxValue = Math.max(...validPoints.map(p => Number(p.y) || 0), 0);
    const minValue = Math.min(...validPoints.map(p => Number(p.y) || 0), 0);

    useEffect(() => {
        const formattedData = {
            type: "bar_chart",
            title: title,
            x_axis_label: xAxisLabel,
            y_axis_label: yAxisLabel,
            theme: chartTheme,
            points: validPoints.map(p => ({ 
                label: p.label, 
                y: Number(p.y) || 0,
                color: p.color || '#3B82F6'
            }))
        };
        onChange(formattedData);
    }, [points, xAxisLabel, yAxisLabel, title, chartTheme, onChange]);

    const handleAddRow = () => { 
        if (!isSubmitted) {
            const colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4', '#F97316', '#84CC16'];
            const randomColor = colors[Math.floor(Math.random() * colors.length)];
            setPoints([...points, { label: '', y: '', color: randomColor }]); 
        }
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

    const handleColorChange = (index, color) => {
        if (isSubmitted) return;
        const newPoints = [...points];
        newPoints[index] = { ...newPoints[index], color };
        setPoints(newPoints);
    };

    const getPercentage = (value) => {
        if (total === 0) return 0;
        return ((Number(value) / total) * 100).toFixed(1);
    };

    const predefinedThemes = {
        default: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4', '#F97316', '#84CC16'],
        warm: ['#F59E0B', '#F97316', '#EF4444', '#DC2626', '#B91C1C', '#991B1B', '#7F1D1D', '#450A0A'],
        cool: ['#3B82F6', '#1D4ED8', '#1E40AF', '#1E3A8A', '#1E293B', '#0F172A', '#020617', '#000000'],
        pastel: ['#FEF3C7', '#FDE68A', '#FCD34D', '#FBBF24', '#F59E0B', '#D97706', '#B45309', '#92400E']
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Bar Chart Builder</h3>
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
                        placeholder="e.g., Monthly Sales Data" 
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
                        placeholder="e.g., Categories" 
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
                        placeholder="e.g., Values" 
                    />
                </div>
            </div>

            {/* Theme Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-3">Color Theme:</label>
                <div className="flex flex-wrap gap-3">
                    {Object.entries(predefinedThemes).map(([themeName, colors]) => (
                        <button
                            key={themeName}
                            onClick={() => !isSubmitted && setChartTheme(themeName)}
                            className={`px-4 py-2 rounded-lg border-2 transition-all ${
                                chartTheme === themeName
                                    ? 'border-blue-500 bg-blue-50 text-blue-700'
                                    : 'border-gray-200 bg-white text-gray-700 hover:border-gray-300'
                            }`}
                        >
                            <div className="flex items-center space-x-2">
                                <div className="flex space-x-1">
                                    {colors.slice(0, 4).map((color, i) => (
                                        <div key={i} className="w-3 h-3 rounded-full" style={{ backgroundColor: color }}></div>
                                    ))}
                                </div>
                                <span className="capitalize">{themeName}</span>
                            </div>
                        </button>
                    ))}
                </div>
            </div>

            {/* Data Input Table */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <div className="flex items-center justify-between mb-4">
                    <h4 className="text-md font-medium text-gray-800">Data Points</h4>
                    {!isSubmitted && (
                        <button 
                            onClick={handleAddRow} 
                            className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors flex items-center space-x-2"
                        >
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                            </svg>
                            <span>Add Data Point</span>
                        </button>
                    )}
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full divide-y divide-gray-200">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Label</th>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Value</th>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Color</th>
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Percentage</th>
                                {!isSubmitted && <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>}
                            </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                            {points.map((point, index) => (
                                <tr key={index} className="hover:bg-gray-50 transition-colors">
                                    <td className="px-4 py-3">
                                        <input 
                                            type="text" 
                                            className="w-full p-2 border border-gray-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                            value={point.label} 
                                            onChange={(e) => handlePointChange(index, 'label', e.target.value)} 
                                            placeholder="e.g., Apples" 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3">
                                        <input 
                                            type="number" 
                                            className="w-full p-2 border border-gray-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                            value={point.y} 
                                            onChange={(e) => handlePointChange(index, 'y', e.target.value)} 
                                            placeholder="e.g., 20" 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3">
                                        <input 
                                            type="color" 
                                            className="w-12 h-10 border border-gray-200 rounded-md cursor-pointer" 
                                            value={point.color || '#3B82F6'} 
                                            onChange={(e) => handleColorChange(index, e.target.value)} 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3 text-sm text-gray-600">
                                        {point.y && point.y !== '' ? `${getPercentage(point.y)}%` : '-'}
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

            {/* Statistics Summary */}
            {validPoints.length > 0 && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6 p-4 bg-blue-50 rounded-lg">
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{validPoints.length}</div>
                        <div className="text-sm text-blue-700">Data Points</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-green-600">{total}</div>
                        <div className="text-sm text-green-700">Total Value</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-purple-600">{maxValue}</div>
                        <div className="text-sm text-purple-700">Maximum</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-orange-600">{minValue}</div>
                        <div className="text-sm text-orange-700">Minimum</div>
                    </div>
                </div>
            )}

            {/* Interactive Chart Preview */}
            {showPreview && validPoints.length > 0 && (
                <div className="border border-gray-200 rounded-lg p-6 bg-white">
                    <h4 className="text-lg font-medium text-gray-800 mb-4">Chart Preview</h4>
                    <div className="h-64 flex items-end justify-center space-x-2">
                        {validPoints.map((point, index) => {
                            const height = maxValue > 0 ? (Number(point.y) / maxValue) * 100 : 0;
                            return (
                                <div key={index} className="flex flex-col items-center space-y-2">
                                    <div 
                                        className="w-12 rounded-t-lg transition-all duration-300 hover:scale-105 cursor-pointer"
                                        style={{ 
                                            height: `${height}%`, 
                                            backgroundColor: point.color || '#3B82F6',
                                            minHeight: '20px'
                                        }}
                                        title={`${point.label}: ${point.y} (${getPercentage(point.y)}%)`}
                                    ></div>
                                    <div className="text-xs text-gray-600 text-center max-w-16">
                                        {point.label}
                                    </div>
                                    <div className="text-xs font-medium text-gray-800">
                                        {point.y}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                    <div className="mt-4 text-center text-sm text-gray-500">
                        {yAxisLabel && <div>Y-Axis: {yAxisLabel}</div>}
                        {xAxisLabel && <div>X-Axis: {xAxisLabel}</div>}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Use descriptive labels for better chart readability</li>
                    <li>• Choose contrasting colors for different data points</li>
                    <li>• Preview your chart to ensure it looks as expected</li>
                    <li>• The percentage is automatically calculated based on total values</li>
                </ul>
            </div>
        </div>
    );
};

export default BarChartInput;
