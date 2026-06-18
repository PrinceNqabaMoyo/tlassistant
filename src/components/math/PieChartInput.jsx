import React, { useState, useEffect } from 'react';

const PieChartInput = ({ initialData, onChange, isSubmitted }) => {
    const [slices, setSlices] = useState(initialData.slices || [{ label: '', value: '', color: '#3B82F6' }]);
    const [title, setTitle] = useState(initialData.title || '');
    const [showPreview, setShowPreview] = useState(false);
    const [chartTheme, setChartTheme] = useState(initialData.theme || 'default');
    const [showPercentages, setShowPercentages] = useState(initialData.showPercentages !== false);
    const [showValues, setShowValues] = useState(initialData.showValues !== false);
    const [explodeSlice, setExplodeSlice] = useState(initialData.explodeSlice || -1);

    // Calculate statistics
    const validSlices = slices.filter(s => s.label.trim() !== '' && s.value !== '');
    const total = validSlices.reduce((sum, s) => sum + (Number(s.value) || 0), 0);
    const maxValue = Math.max(...validSlices.map(s => Number(s.value) || 0), 0);
    const minValue = Math.min(...validSlices.map(s => Number(s.value) || 0), 0);

    useEffect(() => {
        const formattedData = {
            type: "pie_chart",
            title: title,
            theme: chartTheme,
            showPercentages: showPercentages,
            showValues: showValues,
            explodeSlice: explodeSlice,
            slices: validSlices.map(s => ({ 
                label: s.label, 
                value: Number(s.value) || 0,
                color: s.color || '#3B82F6'
            }))
        };
        onChange(formattedData);
    }, [slices, title, chartTheme, showPercentages, showValues, explodeSlice, onChange]);

    const handleAddRow = () => { 
        if (!isSubmitted) {
            const colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4', '#F97316', '#84CC16'];
            const randomColor = colors[Math.floor(Math.random() * colors.length)];
            setSlices([...slices, { label: '', value: '', color: randomColor }]); 
        }
    };
    
    const handleRemoveRow = (indexToRemove) => { 
        if (!isSubmitted) setSlices(slices.filter((_, index) => index !== indexToRemove)); 
    };
    
    const handleSliceChange = (index, field, value) => {
        if (isSubmitted) return;
        const newSlices = [...slices];
        newSlices[index] = { ...newSlices[index], [field]: value };
        setSlices(newSlices);
    };

    const handleColorChange = (index, color) => {
        if (isSubmitted) return;
        const newSlices = [...slices];
        newSlices[index] = { ...newSlices[index], color };
        setSlices(newSlices);
    };

    const getPercentage = (value) => {
        if (total === 0) return 0;
        return ((Number(value) / total) * 100).toFixed(1);
    };

    const getAngle = (value) => {
        if (total === 0) return 0;
        return (Number(value) / total) * 360;
    };

    const predefinedThemes = {
        default: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4', '#F97316', '#84CC16'],
        warm: ['#F59E0B', '#F97316', '#EF4444', '#DC2626', '#B91C1C', '#991B1B', '#7F1D1D', '#450A0A'],
        cool: ['#3B82F6', '#1D4ED8', '#1E40AF', '#1E3A8A', '#1E293B', '#0F172A', '#020617', '#000000'],
        pastel: ['#FEF3C7', '#FDE68A', '#FCD34D', '#FBBF24', '#F59E0B', '#D97706', '#B45309', '#92400E'],
        earth: ['#8B4513', '#A0522D', '#CD853F', '#DEB887', '#F4A460', '#DAA520', '#B8860B', '#D2691E']
    };

    const validatePercentages = () => {
        const percentages = validSlices.map(s => Number(s.value));
        const sum = percentages.reduce((a, b) => a + b, 0);
        if (sum !== 100) {
            return `Total: ${sum}% (should be 100%)`;
        }
        return 'Valid (100%)';
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Pie Chart Builder</h3>
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
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Chart Title:</label>
                    <input 
                        type="text" 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={title} 
                        onChange={(e) => !isSubmitted && setTitle(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="e.g., Favorite Hobbies Distribution" 
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Explode Slice:</label>
                    <select 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={explodeSlice} 
                        onChange={(e) => !isSubmitted && setExplodeSlice(Number(e.target.value))} 
                        disabled={isSubmitted}
                    >
                        <option value={-1}>None</option>
                        {validSlices.map((slice, index) => (
                            <option key={index} value={index}>{slice.label || `Slice ${index + 1}`}</option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Display Options */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showPercentages} 
                            onChange={(e) => !isSubmitted && setShowPercentages(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Show Percentages</span>
                    </label>
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showValues} 
                            onChange={(e) => !isSubmitted && setShowValues(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Show Values</span>
                    </label>
                </div>
                <div className="text-sm text-gray-600">
                    <span className="font-medium">Validation: </span>
                    <span className={validatePercentages().includes('Valid') ? 'text-green-600' : 'text-red-600'}>
                        {validatePercentages()}
                    </span>
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
                    <h4 className="text-md font-medium text-gray-800">Chart Slices</h4>
                    {!isSubmitted && (
                        <button 
                            onClick={handleAddRow} 
                            className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors flex items-center space-x-2"
                        >
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                            </svg>
                            <span>Add Slice</span>
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
                                <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Angle</th>
                                {!isSubmitted && <th className="px-4 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>}
                            </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                            {slices.map((slice, index) => (
                                <tr key={index} className="hover:bg-gray-50 transition-colors">
                                    <td className="px-4 py-3">
                                        <input 
                                            type="text" 
                                            className="w-full p-2 border border-gray-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                            value={slice.label} 
                                            onChange={(e) => handleSliceChange(index, 'label', e.target.value)} 
                                            placeholder="e.g., Reading" 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3">
                                        <input 
                                            type="number" 
                                            className="w-full p-2 border border-gray-200 rounded-md text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                            value={slice.value} 
                                            onChange={(e) => handleSliceChange(index, 'value', e.target.value)} 
                                            placeholder="e.g., 40" 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3">
                                        <input 
                                            type="color" 
                                            className="w-12 h-10 border border-gray-200 rounded-md cursor-pointer" 
                                            value={slice.color || '#3B82F6'} 
                                            onChange={(e) => handleColorChange(index, e.target.value)} 
                                            disabled={isSubmitted} 
                                        />
                                    </td>
                                    <td className="px-4 py-3 text-sm text-gray-600">
                                        {slice.value && slice.value !== '' ? `${getPercentage(slice.value)}%` : '-'}
                                    </td>
                                    <td className="px-4 py-3 text-sm text-gray-600">
                                        {slice.value && slice.value !== '' ? `${getAngle(slice.value).toFixed(1)}°` : '-'}
                                    </td>
                                    {!isSubmitted && (
                                        <td className="px-4 py-3">
                                            <button 
                                                onClick={() => handleRemoveRow(index)} 
                                                className="text-red-600 hover:text-red-800 hover:bg-red-50 p-2 rounded-md transition-colors"
                                                title="Remove this slice"
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
            {validSlices.length > 0 && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6 p-4 bg-purple-50 rounded-lg">
                    <div className="text-center">
                        <div className="text-2xl font-bold text-purple-600">{validSlices.length}</div>
                        <div className="text-sm text-purple-700">Slices</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-green-600">{total}</div>
                        <div className="text-sm text-green-700">Total Value</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{maxValue}</div>
                        <div className="text-sm text-blue-700">Largest Slice</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-orange-600">{minValue}</div>
                        <div className="text-sm text-orange-700">Smallest Slice</div>
                    </div>
                </div>
            )}

            {/* Interactive Chart Preview */}
            {showPreview && validSlices.length > 0 && (
                <div className="border border-gray-200 rounded-lg p-6 bg-white">
                    <h4 className="text-lg font-medium text-gray-800 mb-4">Chart Preview</h4>
                    <div className="flex justify-center">
                        <div className="relative w-64 h-64">
                            <svg className="w-full h-full" viewBox="0 0 100 100">
                                {validSlices.map((slice, index) => {
                                    const percentage = getPercentage(slice.value);
                                    const angle = getAngle(slice.value);
                                    const startAngle = validSlices.slice(0, index).reduce((sum, s) => sum + getAngle(s.value), 0);
                                    const endAngle = startAngle + angle;
                                    
                                    // Convert angles to radians and calculate arc coordinates
                                    const startRad = (startAngle - 90) * Math.PI / 180;
                                    const endRad = (endAngle - 90) * Math.PI / 180;
                                    
                                    const radius = 40;
                                    const centerX = 50;
                                    const centerY = 50;
                                    
                                    const x1 = centerX + radius * Math.cos(startRad);
                                    const y1 = centerY + radius * Math.sin(startRad);
                                    const x2 = centerX + radius * Math.cos(endRad);
                                    const y2 = centerY + radius * Math.sin(endRad);
                                    
                                    const largeArcFlag = angle > 180 ? 1 : 0;
                                    
                                    // Explode effect
                                    const explodeRadius = explodeSlice === index ? radius + 5 : radius;
                                    const explodeX = centerX + explodeRadius * Math.cos((startAngle + angle/2 - 90) * Math.PI / 180);
                                    const explodeY = centerY + explodeRadius * Math.sin((startAngle + angle/2 - 90) * Math.PI / 180);
                                    
                                    return (
                                        <g key={index}>
                                            <path
                                                d={`M ${centerX} ${centerY} L ${x1} ${y1} A ${explodeRadius} ${explodeRadius} 0 ${largeArcFlag} 1 ${x2} ${y2} Z`}
                                                fill={slice.color || '#3B82F6'}
                                                stroke="white"
                                                strokeWidth="0.5"
                                                transform={explodeSlice === index ? `translate(${explodeX - centerX}, ${explodeY - centerY})` : ''}
                                            />
                                        </g>
                                    );
                                })}
                            </svg>
                            
                            {/* Center Label */}
                            <div className="absolute inset-0 flex items-center justify-center">
                                <div className="text-center">
                                    <div className="text-lg font-bold text-gray-800">{title || 'Pie Chart'}</div>
                                    <div className="text-sm text-gray-600">{total} total</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    {/* Legend */}
                    <div className="mt-6 grid grid-cols-2 md:grid-cols-3 gap-3">
                        {validSlices.map((slice, index) => (
                            <div key={index} className="flex items-center space-x-2">
                                <div 
                                    className="w-4 h-4 rounded-full" 
                                    style={{ backgroundColor: slice.color || '#3B82F6' }}
                                ></div>
                                <span className="text-sm text-gray-700">
                                    {slice.label}: {slice.value}
                                    {showPercentages && ` (${getPercentage(slice.value)}%)`}
                                </span>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Values can be percentages (0-100) or absolute numbers</li>
                    <li>• Use the explode feature to highlight important slices</li>
                    <li>• Choose contrasting colors for better visibility</li>
                    <li>• The chart automatically calculates percentages and angles</li>
                </ul>
            </div>
        </div>
    );
};

export default PieChartInput;
