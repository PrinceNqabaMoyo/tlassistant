import React, { useState, useEffect } from 'react';

const NumberLineInput = ({ initialData, onChange, isSubmitted }) => {
    const [numberLineData, setNumberLineData] = useState(initialData || {
        min: -10,
        max: 10,
        step: 1,
        showFractions: false,
        showDecimals: false,
        points: [],
        title: "Number Line"
    });

    useEffect(() => {
        // Only call onChange when component is properly initialized and data has changed
        if (numberLineData && numberLineData.points && onChange) {
            // Use a ref to track if this is the first render
            const isInitialized = numberLineData.min !== undefined && 
                                numberLineData.max !== undefined && 
                                numberLineData.step !== undefined;
            
            if (isInitialized) {
                onChange(numberLineData);
            }
        }
    }, [numberLineData.min, numberLineData.max, numberLineData.step, numberLineData.points, onChange]);

    // Initialize missing properties only once
    useEffect(() => {
        const needsUpdate = !numberLineData.points || 
                           numberLineData.showFractions === undefined || 
                           numberLineData.showDecimals === undefined;
        
        if (needsUpdate) {
            setNumberLineData(prev => ({
                ...prev,
                points: prev.points || [],
                showFractions: prev.showFractions !== undefined ? prev.showFractions : false,
                showDecimals: prev.showDecimals !== undefined ? prev.showDecimals : false
            }));
        }
    }, []); // Empty dependency array - only run once

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        
        // Prevent unnecessary updates if value hasn't changed
        if (numberLineData[field] === value) return;
        
        setNumberLineData(prev => ({ ...prev, [field]: value }));
    };

    const addPoint = () => {
        if (isSubmitted) return;
        const newPoint = {
            id: Date.now(),
            value: '',
            label: '',
            color: '#3B82F6',
            position: 0
        };
        setNumberLineData(prev => ({
            ...prev,
            points: [...(prev.points || []), newPoint]
        }));
    };

    const removePoint = (pointId) => {
        if (isSubmitted) return;
        setNumberLineData(prev => ({
            ...prev,
            points: (prev.points || []).filter(p => p.id !== pointId)
        }));
    };

    const updatePoint = (pointId, field, value) => {
        if (isSubmitted) return;
        setNumberLineData(prev => ({
            ...prev,
            points: (prev.points || []).map(p => 
                p.id === pointId ? { ...p, [field]: value } : p
            )
        }));
    };

    const calculatePosition = (value) => {
        const numValue = parseFloat(value);
        if (isNaN(numValue)) return 50; // Center if invalid
        
        // Safety check for undefined min/max
        if (!numberLineData.min || !numberLineData.max) return 50;
        
        const range = numberLineData.max - numberLineData.min;
        if (range === 0) return 50; // Prevent division by zero
        
        const percentage = ((numValue - numberLineData.min) / range) * 100;
        return Math.max(0, Math.min(100, percentage));
    };

    const renderNumberLine = () => {
        // Safety checks for undefined values
        if (numberLineData.min === undefined || numberLineData.max === undefined || numberLineData.step === undefined) {
            return <div className="w-full h-16 bg-gray-100 border-2 border-gray-300 rounded-lg flex items-center justify-center text-gray-500">Please set valid min, max, and step values</div>;
        }
        
        const range = numberLineData.max - numberLineData.min;
        if (range <= 0) {
            return <div className="w-full h-16 bg-gray-100 border-2 border-gray-300 rounded-lg flex items-center justify-center text-gray-500">Maximum value must be greater than minimum value</div>;
        }
        
        const step = numberLineData.step;
        if (step <= 0) {
            return <div className="w-full h-16 bg-gray-100 border-2 border-gray-300 rounded-lg flex items-center justify-center text-gray-500">Step size must be greater than 0</div>;
        }
        
        const ticks = [];
        
        for (let i = numberLineData.min; i <= numberLineData.max; i += step) {
            const position = ((i - numberLineData.min) / range) * 100;
            ticks.push({ value: i, position });
        }

        return (
            <div className="relative w-full h-16 bg-gray-100 border-2 border-gray-300 rounded-lg overflow-hidden">
                {/* Number line ticks and labels */}
                {ticks?.map((tick, index) => (
                    <div key={`tick-${tick.value}-${index}`} className="absolute top-0 bottom-0 flex flex-col items-center">
                        <div 
                            className="w-px h-4 bg-gray-400"
                            style={{ left: `${tick.position}%` }}
                        />
                        <div 
                            className="absolute bottom-1 text-xs text-gray-600 font-medium"
                            style={{ left: `${tick.position}%`, transform: 'translateX(-50%)' }}
                        >
                            {tick.value}
                        </div>
                    </div>
                ))}
                
                {/* Points on the number line */}
                {numberLineData.points?.map((point) => {
                    if (!point || !point.value) return null;
                    const position = calculatePosition(point.value);
                    return (
                        <div
                            key={point.id}
                            className="absolute top-2 transform -translate-x-1/2 cursor-pointer"
                            style={{ 
                                left: `${position}%`,
                                zIndex: 10
                            }}
                            title={`${point.label || point.value} at position ${position.toFixed(1)}%`}
                        >
                            <div 
                                className="w-4 h-4 rounded-full border-2 border-white shadow-md"
                                style={{ backgroundColor: point.color || '#3B82F6' }}
                            />
                            {point.label && (
                                <div className="absolute top-5 left-1/2 transform -translate-x-1/2 text-xs font-medium text-gray-700 bg-white px-1 rounded">
                                    {point.label}
                                </div>
                            )}
                        </div>
                    );
                })}
                
                {/* Zero marker */}
                {numberLineData.min <= 0 && numberLineData.max >= 0 && range > 0 && (
                    <div 
                        className="absolute top-0 bottom-0 w-0.5 bg-red-500"
                        style={{ 
                            left: `${((0 - numberLineData.min) / range) * 100}%`,
                            zIndex: 5
                        }}
                    />
                )}
            </div>
        );
    };

    // Don't render if not properly initialized
    if (numberLineData.min === undefined || numberLineData.max === undefined || numberLineData.step === undefined) {
        return (
            <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
                <h3 className="font-semibold text-gray-700 mb-4">Number Line Input</h3>
                <div className="text-center py-8 text-gray-500">
                    <p>Loading number line configuration...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Number Line Input</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={numberLineData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Number Line Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Minimum Value:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={numberLineData.min}
                        onChange={(e) => handleFieldChange('min', parseInt(e.target.value) || 0)}
                        disabled={isSubmitted}
                        placeholder="-10"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Maximum Value:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={numberLineData.max}
                        onChange={(e) => handleFieldChange('max', parseInt(e.target.value) || 10)}
                        disabled={isSubmitted}
                        placeholder="10"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Step Size:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={numberLineData.step}
                        onChange={(e) => handleFieldChange('step', parseInt(e.target.value) || 1)}
                        disabled={isSubmitted}
                        placeholder="1"
                        min="0.1"
                        step="0.1"
                    />
                </div>
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={numberLineData.showFractions}
                        onChange={(e) => handleFieldChange('showFractions', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Fractions</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={numberLineData.showDecimals}
                        onChange={(e) => handleFieldChange('showDecimals', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Decimals</span>
                </label>
            </div>

            {/* Number Line Visualization */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Number Line Preview:</label>
                {renderNumberLine()}
            </div>

            {/* Points Management */}
            <div className="mb-4">
                <div className="flex justify-between items-center mb-2">
                    <label className="block text-sm font-medium text-gray-700">Points on Number Line:</label>
                    {!isSubmitted && (
                        <button
                            onClick={addPoint}
                            className="px-3 py-1 bg-blue-500 text-white text-sm rounded-md hover:bg-blue-600"
                        >
                            Add Point
                        </button>
                    )}
                </div>
                
                {numberLineData.points.length === 0 ? (
                    <p className="text-sm text-gray-500 italic">No points added yet. Click "Add Point" to place points on the number line.</p>
                ) : (
                    <div className="space-y-2">
                        {numberLineData.points.map((point) => (
                            <div key={point.id} className="flex items-center space-x-2 p-2 bg-white border border-gray-200 rounded-md">
                                <div className="flex-1 grid grid-cols-3 gap-2">
                                    <input
                                        type="text"
                                        className="p-1 border border-gray-300 rounded text-sm"
                                        value={point.value}
                                        onChange={(e) => updatePoint(point.id, 'value', e.target.value)}
                                        disabled={isSubmitted}
                                        placeholder="Value (e.g., 3, 1/2, 0.5)"
                                    />
                                    <input
                                        type="text"
                                        className="p-1 border border-gray-300 rounded text-sm"
                                        value={point.label}
                                        onChange={(e) => updatePoint(point.id, 'label', e.target.value)}
                                        disabled={isSubmitted}
                                        placeholder="Label (optional)"
                                    />
                                    <input
                                        type="color"
                                        className="w-full h-8 border border-gray-300 rounded"
                                        value={point.color}
                                        onChange={(e) => updatePoint(point.id, 'color', e.target.value)}
                                        disabled={isSubmitted}
                                    />
                                </div>
                                {!isSubmitted && (
                                    <button
                                        onClick={() => removePoint(point.id)}
                                        className="text-red-600 hover:text-red-800 text-lg font-bold"
                                    >
                                        ×
                                    </button>
                                )}
                            </div>
                        ))}
                    </div>
                )}
            </div>

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Set the minimum and maximum values for your number line</li>
                    <li>Choose the step size for tick marks</li>
                    <li>Add points by entering values (integers, fractions like 1/2, or decimals like 0.5)</li>
                    <li>Optionally add labels to identify points</li>
                    <li>Use different colors to distinguish between points</li>
                </ul>
            </div>
        </div>
    );
};

export default NumberLineInput;
