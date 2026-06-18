import React, { useState, useEffect } from 'react';

const FractionVisualizer = ({ initialData, onChange, isSubmitted }) => {
    const [fractionData, setFractionData] = useState(initialData || {
        numerator: 1,
        denominator: 2,
        representation: 'circle', // 'circle', 'rectangle', 'numberLine', 'mixed'
        showEquivalent: false,
        showDecimal: false,
        showPercentage: false,
        color: '#3B82F6',
        title: "Fraction Visualizer"
    });

    useEffect(() => {
        onChange(fractionData);
    }, [fractionData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setFractionData(prev => ({ ...prev, [field]: value }));
    };

    const calculateFraction = () => {
        const num = parseInt(fractionData.numerator) || 0;
        const den = parseInt(fractionData.denominator) || 1;
        return den !== 0 ? num / den : 0;
    };

    const getEquivalentFractions = () => {
        const num = parseInt(fractionData.numerator) || 0;
        const den = parseInt(fractionData.denominator) || 1;
        if (den === 0) return [];
        
        const equivalents = [];
        for (let i = 2; i <= 10; i++) {
            equivalents.push({
                numerator: num * i,
                denominator: den * i,
                multiplier: i
            });
        }
        return equivalents;
    };

    const renderCircleFraction = () => {
        const num = parseInt(fractionData.numerator) || 0;
        const den = parseInt(fractionData.denominator) || 1;
        const filledSectors = Math.min(num, den);
        const totalSectors = den;
        
        return (
            <div className="flex flex-col items-center">
                <div className="relative w-32 h-32 mb-2">
                    <svg width="128" height="128" viewBox="0 0 128 128" className="transform -rotate-90">
                        <circle
                            cx="64"
                            cy="64"
                            r="60"
                            fill="none"
                            stroke="#E5E7EB"
                            strokeWidth="4"
                        />
                        {Array.from({ length: totalSectors }, (_, i) => {
                            const angle = (360 / totalSectors) * i;
                            const nextAngle = (360 / totalSectors) * (i + 1);
                            const isFilled = i < filledSectors;
                            
                            const x1 = 64 + 60 * Math.cos((angle * Math.PI) / 180);
                            const y1 = 64 + 60 * Math.sin((angle * Math.PI) / 180);
                            const x2 = 64 + 60 * Math.cos((nextAngle * Math.PI) / 180);
                            const y2 = 64 + 60 * Math.sin((nextAngle * Math.PI) / 180);
                            
                            const largeArcFlag = (360 / totalSectors) > 180 ? 1 : 0;
                            
                            return (
                                <path
                                    key={i}
                                    d={`M 64 64 L ${x1} ${y1} A 60 60 0 ${largeArcFlag} 1 ${x2} ${y2} Z`}
                                    fill={isFilled ? fractionData.color : 'none'}
                                    stroke="#6B7280"
                                    strokeWidth="1"
                                />
                            );
                        })}
                    </svg>
                    <div className="absolute inset-0 flex items-center justify-center">
                        <span className="text-lg font-bold text-gray-700">
                            {fractionData.numerator}/{fractionData.denominator}
                        </span>
                    </div>
                </div>
                <p className="text-sm text-gray-600">Circle Representation</p>
            </div>
        );
    };

    const renderRectangleFraction = () => {
        const num = parseInt(fractionData.numerator) || 0;
        const den = parseInt(fractionData.denominator) || 1;
        const filledParts = Math.min(num, den);
        const totalParts = den;
        
        return (
            <div className="flex flex-col items-center">
                <div className="w-48 h-16 border-2 border-gray-300 rounded-lg overflow-hidden mb-2">
                    <div className="flex h-full">
                        {Array.from({ length: totalParts }, (_, i) => (
                            <div
                                key={i}
                                className={`flex-1 border-r border-gray-300 ${
                                    i < filledParts ? '' : ''
                                }`}
                                style={{
                                    backgroundColor: i < filledParts ? fractionData.color : 'transparent'
                                }}
                            />
                        ))}
                    </div>
                </div>
                <p className="text-sm text-gray-600">Rectangle Representation</p>
            </div>
        );
    };

    const renderNumberLineFraction = () => {
        const fraction = calculateFraction();
        const position = Math.min(100, Math.max(0, fraction * 100));
        
        return (
            <div className="flex flex-col items-center">
                <div className="relative w-48 h-8 bg-gray-100 border-2 border-gray-300 rounded-lg mb-2">
                    <div className="absolute top-0 bottom-0 left-0 right-0 flex">
                        {Array.from({ length: parseInt(fractionData.denominator) + 1 }, (_, i) => (
                            <div
                                key={i}
                                className="flex-1 border-r border-gray-400 last:border-r-0"
                            >
                                <div className="text-xs text-gray-600 text-center mt-1">
                                    {i}
                                </div>
                            </div>
                        ))}
                    </div>
                    <div
                        className="absolute top-1 bottom-1 w-1 bg-red-500 rounded"
                        style={{ left: `${position}%` }}
                    />
                </div>
                <p className="text-sm text-gray-600">Number Line Representation</p>
            </div>
        );
    };

    const renderMixedNumber = () => {
        const num = parseInt(fractionData.numerator) || 0;
        const den = parseInt(fractionData.denominator) || 1;
        const wholePart = Math.floor(num / den);
        const remainder = num % den;
        
        return (
            <div className="flex flex-col items-center">
                <div className="flex items-center space-x-2 mb-2">
                    {wholePart > 0 && (
                        <div className="flex space-x-1">
                            {Array.from({ length: wholePart }, (_, i) => (
                                <div
                                    key={i}
                                    className="w-8 h-8 border-2 border-gray-300 rounded"
                                    style={{ backgroundColor: fractionData.color }}
                                />
                            ))}
                        </div>
                    )}
                    {remainder > 0 && (
                        <div className="flex items-center space-x-1">
                            <div className="w-8 h-8 border-2 border-gray-300 rounded overflow-hidden">
                                <div className="flex h-full">
                                    {Array.from({ length: den }, (_, i) => (
                                        <div
                                            key={i}
                                            className={`flex-1 border-r border-gray-300 ${
                                                i < remainder ? '' : ''
                                            }`}
                                            style={{
                                                backgroundColor: i < remainder ? fractionData.color : 'transparent'
                                            }}
                                        />
                                    ))}
                                </div>
                            </div>
                        </div>
                    )}
                </div>
                <p className="text-sm text-gray-600">
                    {wholePart > 0 ? `${wholePart} ` : ''}{remainder > 0 ? `${remainder}/${den}` : ''}
                </p>
            </div>
        );
    };

    const renderFractionRepresentation = () => {
        switch (fractionData.representation) {
            case 'circle':
                return renderCircleFraction();
            case 'rectangle':
                return renderRectangleFraction();
            case 'numberLine':
                return renderNumberLineFraction();
            case 'mixed':
                return renderMixedNumber();
            default:
                return renderCircleFraction();
        }
    };

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Fraction Visualizer</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={fractionData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Fraction Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Numerator:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={fractionData.numerator}
                        onChange={(e) => handleFieldChange('numerator', parseInt(e.target.value) || 0)}
                        disabled={isSubmitted}
                        placeholder="1"
                        min="0"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Denominator:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={fractionData.denominator}
                        onChange={(e) => handleFieldChange('denominator', parseInt(e.target.value) || 1)}
                        disabled={isSubmitted}
                        placeholder="2"
                        min="1"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Color:</label>
                    <input
                        type="color"
                        className="w-full h-10 border border-gray-300 rounded-md"
                        value={fractionData.color}
                        onChange={(e) => handleFieldChange('color', e.target.value)}
                        disabled={isSubmitted}
                    />
                </div>
            </div>

            {/* Representation Type */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Representation Type:</label>
                <div className="flex space-x-4">
                    {['circle', 'rectangle', 'numberLine', 'mixed'].map((type) => (
                        <label key={type} className="flex items-center">
                            <input
                                type="radio"
                                name="representation"
                                className="mr-2"
                                checked={fractionData.representation === type}
                                onChange={() => handleFieldChange('representation', type)}
                                disabled={isSubmitted}
                            />
                            <span className="text-sm text-gray-700 capitalize">
                                {type.replace(/([A-Z])/g, ' $1').trim()}
                            </span>
                        </label>
                    ))}
                </div>
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={fractionData.showEquivalent}
                        onChange={(e) => handleFieldChange('showEquivalent', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Equivalent Fractions</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={fractionData.showDecimal}
                        onChange={(e) => handleFieldChange('showDecimal', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Decimal</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={fractionData.showPercentage}
                        onChange={(e) => handleFieldChange('showPercentage', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Percentage</span>
                </label>
            </div>

            {/* Fraction Visualization */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Fraction Visualization:</label>
                <div className="flex justify-center">
                    {renderFractionRepresentation()}
                </div>
            </div>

            {/* Fraction Information */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                <div className="bg-white p-3 border border-gray-200 rounded-lg">
                    <h4 className="font-semibold text-gray-700 mb-2">Fraction</h4>
                    <p className="text-2xl font-bold text-center" style={{ color: fractionData.color }}>
                        {fractionData.numerator}/{fractionData.denominator}
                    </p>
                </div>
                
                {fractionData.showDecimal && (
                    <div className="bg-white p-3 border border-gray-200 rounded-lg">
                        <h4 className="font-semibold text-gray-700 mb-2">Decimal</h4>
                        <p className="text-2xl font-bold text-center text-blue-600">
                            {calculateFraction().toFixed(3)}
                        </p>
                    </div>
                )}
                
                {fractionData.showPercentage && (
                    <div className="bg-white p-3 border border-gray-200 rounded-lg">
                        <h4 className="font-semibold text-gray-700 mb-2">Percentage</h4>
                        <p className="text-2xl font-bold text-center text-green-600">
                            {(calculateFraction() * 100).toFixed(1)}%
                        </p>
                    </div>
                )}
            </div>

            {/* Equivalent Fractions */}
            {fractionData.showEquivalent && (
                <div className="mb-4">
                    <h4 className="font-semibold text-gray-700 mb-2">Equivalent Fractions:</h4>
                    <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
                        {getEquivalentFractions().map((equiv, index) => (
                            <div key={index} className="bg-white p-2 border border-gray-200 rounded text-center">
                                <p className="text-sm font-semibold" style={{ color: fractionData.color }}>
                                    {equiv.numerator}/{equiv.denominator}
                                </p>
                                <p className="text-xs text-gray-500">×{equiv.multiplier}</p>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Enter the numerator and denominator to visualize the fraction</li>
                    <li>Choose different representation types: circle, rectangle, number line, or mixed number</li>
                    <li>Use the color picker to customize the visualization</li>
                    <li>Enable options to see decimal, percentage, and equivalent fractions</li>
                    <li>Observe how the same fraction can be represented in different ways</li>
                </ul>
            </div>
        </div>
    );
};

export default FractionVisualizer;
