import React, { useState, useEffect } from 'react';

const ScientificNotationConverter = ({ initialData, onChange, isSubmitted }) => {
    const [inputValue, setInputValue] = useState(initialData.inputValue || '123456');
    const [inputFormat, setInputFormat] = useState(initialData.inputFormat || 'decimal');
    const [outputFormat, setOutputFormat] = useState(initialData.outputFormat || 'scientific');
    const [significantFigures, setSignificantFigures] = useState(initialData.significantFigures || 3);
    const [showUnitConversion, setShowUnitConversion] = useState(false);
    const [showSignificantFigures, setShowSignificantFigures] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [fromUnit, setFromUnit] = useState(initialData.fromUnit || 'meters');
    const [toUnit, setToUnit] = useState(initialData.toUnit || 'feet');
    const [unitValue, setUnitValue] = useState(initialData.unitValue || '100');

    useEffect(() => {
        const formattedData = {
            type: "scientific_notation_converter",
            inputValue: inputValue,
            inputFormat: inputFormat,
            outputFormat: outputFormat,
            significantFigures: significantFigures,
            fromUnit: fromUnit,
            toUnit: toUnit,
            unitValue: unitValue,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [inputValue, inputFormat, outputFormat, significantFigures, fromUnit, toUnit, unitValue, onChange]);

    const calculateResults = () => {
        const results = {};
        
        try {
            const numValue = parseFloat(inputValue);
            
            if (isNaN(numValue)) {
                results.error = 'Invalid number input';
                return results;
            }
            
            // Convert to scientific notation
            results.scientificNotation = numValue.toExponential(significantFigures - 1);
            
            // Convert to standard form
            results.standardForm = numValue.toFixed(significantFigures);
            
            // Convert to engineering notation
            results.engineeringNotation = toEngineeringNotation(numValue, significantFigures);
            
            // Significant figures analysis
            results.significantFiguresAnalysis = analyzeSignificantFigures(inputValue);
            
            // Unit conversion
            if (showUnitConversion) {
                results.unitConversion = convertUnits(parseFloat(unitValue), fromUnit, toUnit);
            }
            
        } catch (error) {
            results.error = 'Calculation error';
        }
        
        return results;
    };

    const toEngineeringNotation = (num, sigFigs) => {
        if (num === 0) return '0';
        
        const exponent = Math.floor(Math.log10(Math.abs(num)));
        const engineeringExponent = Math.floor(exponent / 3) * 3;
        const mantissa = num / Math.pow(10, engineeringExponent);
        
        return mantissa.toFixed(sigFigs - 1) + '×10^' + engineeringExponent;
    };

    const analyzeSignificantFigures = (value) => {
        const str = value.toString();
        let count = 0;
        let hasDecimal = false;
        let leadingZeros = 0;
        
        for (let i = 0; i < str.length; i++) {
            const char = str[i];
            
            if (char === '.') {
                hasDecimal = true;
                continue;
            }
            
            if (char === '0' && count === 0 && !hasDecimal) {
                leadingZeros++;
                continue;
            }
            
            if (char >= '1' && char <= '9') {
                count++;
            } else if (char === '0' && (hasDecimal || count > 0)) {
                count++;
            }
        }
        
        return {
            count: count,
            hasLeadingZeros: leadingZeros > 0,
            leadingZeros: leadingZeros,
            isExact: !hasDecimal && str.endsWith('0')
        };
    };

    const convertUnits = (value, from, to) => {
        const conversions = {
            // Length
            'meters': { 'feet': 3.28084, 'inches': 39.3701, 'centimeters': 100, 'kilometers': 0.001 },
            'feet': { 'meters': 0.3048, 'inches': 12, 'centimeters': 30.48, 'kilometers': 0.0003048 },
            'inches': { 'meters': 0.0254, 'feet': 0.0833333, 'centimeters': 2.54, 'kilometers': 0.0000254 },
            'centimeters': { 'meters': 0.01, 'feet': 0.0328084, 'inches': 0.393701, 'kilometers': 0.00001 },
            'kilometers': { 'meters': 1000, 'feet': 3280.84, 'inches': 39370.1, 'centimeters': 100000 },
            
            // Mass
            'kilograms': { 'pounds': 2.20462, 'grams': 1000, 'ounces': 35.274, 'tons': 0.00110231 },
            'pounds': { 'kilograms': 0.453592, 'grams': 453.592, 'ounces': 16, 'tons': 0.0005 },
            'grams': { 'kilograms': 0.001, 'pounds': 0.00220462, 'ounces': 0.035274, 'tons': 0.00000110231 },
            'ounces': { 'kilograms': 0.0283495, 'pounds': 0.0625, 'grams': 28.3495, 'tons': 0.00003125 },
            'tons': { 'kilograms': 907.185, 'pounds': 2000, 'grams': 907185, 'ounces': 32000 },
            
            // Volume
            'liters': { 'gallons': 0.264172, 'cubic_meters': 0.001, 'milliliters': 1000, 'cubic_feet': 0.0353147 },
            'gallons': { 'liters': 3.78541, 'cubic_meters': 0.00378541, 'milliliters': 3785.41, 'cubic_feet': 0.133681 },
            'cubic_meters': { 'liters': 1000, 'gallons': 264.172, 'milliliters': 1000000, 'cubic_feet': 35.3147 },
            'milliliters': { 'liters': 0.001, 'gallons': 0.000264172, 'cubic_meters': 0.000001, 'cubic_feet': 0.0000353147 },
            'cubic_feet': { 'liters': 28.3168, 'gallons': 7.48052, 'cubic_meters': 0.0283168, 'milliliters': 28316.8 }
        };
        
        if (conversions[from] && conversions[from][to]) {
            return value * conversions[from][to];
        }
        
        return value; // No conversion available
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        if (Math.abs(num) < 0.001) return '0';
        return Math.abs(num) < 0.01 ? num.toExponential(3) : num.toFixed(3);
    };

    const results = calculateResults();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Scientific Notation Converter</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowUnitConversion(!showUnitConversion)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showUnitConversion 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showUnitConversion ? 'Hide Unit Conversion' : 'Show Unit Conversion'}
                    </button>
                    <button
                        onClick={() => setShowSignificantFigures(!showSignificantFigures)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showSignificantFigures 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showSignificantFigures ? 'Hide Sig Figs' : 'Show Sig Figs'}
                    </button>
                    <button
                        onClick={() => setShowCalculations(!showCalculations)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showCalculations 
                                ? 'bg-yellow-100 text-yellow-700 hover:bg-yellow-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showCalculations ? 'Hide Calculations' : 'Show Calculations'}
                    </button>
                </div>
            </div>

            {/* Input Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Number Input:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Input Value:</label>
                            <input 
                                type="text" 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={inputValue} 
                                onChange={(e) => !isSubmitted && setInputValue(e.target.value)} 
                                disabled={isSubmitted}
                                placeholder="Enter a number"
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Input Format:</label>
                            <select 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={inputFormat} 
                                onChange={(e) => !isSubmitted && setInputFormat(e.target.value)} 
                                disabled={isSubmitted}
                            >
                                <option value="decimal">Decimal</option>
                                <option value="scientific">Scientific Notation</option>
                                <option value="engineering">Engineering Notation</option>
                            </select>
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Significant Figures:</label>
                            <input 
                                type="number" 
                                min="1" 
                                max="10"
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={significantFigures} 
                                onChange={(e) => !isSubmitted && setSignificantFigures(parseInt(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Output Format:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Output Format:</label>
                            <select 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={outputFormat} 
                                onChange={(e) => !isSubmitted && setOutputFormat(e.target.value)} 
                                disabled={isSubmitted}
                            >
                                <option value="scientific">Scientific Notation</option>
                                <option value="standard">Standard Form</option>
                                <option value="engineering">Engineering Notation</option>
                                <option value="all">All Formats</option>
                            </select>
                        </div>
                        
                        <div className="pt-4">
                            <div className="text-sm text-gray-600">
                                <div><strong>Current Input:</strong></div>
                                <div className="font-mono text-lg">{inputValue}</div>
                                <div><strong>Parsed Value:</strong></div>
                                <div className="font-mono text-lg">{formatNumber(parseFloat(inputValue) || 0)}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Conversion Results:</h4>
                {results.error ? (
                    <div className="text-red-600 text-center p-4">{results.error}</div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Scientific Notation</div>
                            <div className="text-xl text-purple-700 font-mono">{results.scientificNotation}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Standard Form</div>
                            <div className="text-xl text-purple-700 font-mono">{results.standardForm}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Engineering Notation</div>
                            <div className="text-xl text-purple-700 font-mono">{results.engineeringNotation}</div>
                        </div>
                    </div>
                )}
            </div>

            {/* Unit Conversion */}
            {showUnitConversion && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Unit Conversion:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">From Unit:</label>
                            <select 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={fromUnit} 
                                onChange={(e) => !isSubmitted && setFromUnit(e.target.value)} 
                                disabled={isSubmitted}
                            >
                                <optgroup label="Length">
                                    <option value="meters">Meters</option>
                                    <option value="feet">Feet</option>
                                    <option value="inches">Inches</option>
                                    <option value="centimeters">Centimeters</option>
                                    <option value="kilometers">Kilometers</option>
                                </optgroup>
                                <optgroup label="Mass">
                                    <option value="kilograms">Kilograms</option>
                                    <option value="pounds">Pounds</option>
                                    <option value="grams">Grams</option>
                                    <option value="ounces">Ounces</option>
                                    <option value="tons">Tons</option>
                                </optgroup>
                                <optgroup label="Volume">
                                    <option value="liters">Liters</option>
                                    <option value="gallons">Gallons</option>
                                    <option value="cubic_meters">Cubic Meters</option>
                                    <option value="milliliters">Milliliters</option>
                                    <option value="cubic_feet">Cubic Feet</option>
                                </optgroup>
                            </select>
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Value:</label>
                            <input 
                                type="number" 
                                min="0" 
                                step="0.01"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={unitValue} 
                                onChange={(e) => !isSubmitted && setUnitValue(e.target.value)} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">To Unit:</label>
                            <select 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={toUnit} 
                                onChange={(e) => !isSubmitted && setToUnit(e.target.value)} 
                                disabled={isSubmitted}
                            >
                                <optgroup label="Length">
                                    <option value="meters">Meters</option>
                                    <option value="feet">Feet</option>
                                    <option value="inches">Inches</option>
                                    <option value="centimeters">Centimeters</option>
                                    <option value="kilometers">Kilometers</option>
                                </optgroup>
                                <optgroup label="Mass">
                                    <option value="kilograms">Kilograms</option>
                                    <option value="pounds">Pounds</option>
                                    <option value="grams">Grams</option>
                                    <option value="ounces">Ounces</option>
                                    <option value="tons">Tons</option>
                                </optgroup>
                                <optgroup label="Volume">
                                    <option value="liters">Liters</option>
                                    <option value="gallons">Gallons</option>
                                    <option value="cubic_meters">Cubic Meters</option>
                                    <option value="milliliters">Milliliters</option>
                                    <option value="cubic_feet">Cubic Feet</option>
                                </optgroup>
                            </select>
                        </div>
                    </div>
                    
                    {results.unitConversion && (
                        <div className="text-center p-4 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Conversion Result:</div>
                            <div className="text-2xl text-blue-700 font-mono">
                                {formatNumber(parseFloat(unitValue))} {fromUnit} = {formatNumber(results.unitConversion)} {toUnit}
                            </div>
                        </div>
                    )}
                </div>
            )}

            {/* Significant Figures Analysis */}
            {showSignificantFigures && results.significantFiguresAnalysis && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Significant Figures Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total Sig Figs</div>
                            <div className="text-xl text-green-700">{results.significantFiguresAnalysis.count}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Leading Zeros</div>
                            <div className="text-xl text-green-700">{results.significantFiguresAnalysis.leadingZeros}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Has Leading Zeros</div>
                            <div className="text-xl text-green-700">{results.significantFiguresAnalysis.hasLeadingZeros ? 'Yes' : 'No'}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Exact Number</div>
                            <div className="text-xl text-green-700">{results.significantFiguresAnalysis.isExact ? 'Yes' : 'No'}</div>
                        </div>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Input Analysis:</strong></div>
                        <div>• Raw Input: "{inputValue}"</div>
                        <div>• Parsed Number: {formatNumber(parseFloat(inputValue) || 0)}</div>
                        <div>• Significant Figures Requested: {significantFigures}</div>
                        
                        <div><strong>Scientific Notation:</strong></div>
                        <div>• Format: a × 10^b where 1 ≤ |a| < 10</div>
                        <div>• Result: {results.scientificNotation}</div>
                        
                        <div><strong>Standard Form:</strong></div>
                        <div>• Format: Decimal with specified significant figures</div>
                        <div>• Result: {results.standardForm}</div>
                        
                        <div><strong>Engineering Notation:</strong></div>
                        <div>• Format: a × 10^b where b is a multiple of 3</div>
                        <div>• Result: {results.engineeringNotation}</div>
                        
                        {showUnitConversion && results.unitConversion && (
                            <>
                                <div><strong>Unit Conversion:</strong></div>
                                <div>• {formatNumber(parseFloat(unitValue))} {fromUnit} × conversion factor = {formatNumber(results.unitConversion)} {toUnit}</div>
                            </>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Scientific notation: a × 10^b where 1 ≤ |a| < 10</li>
                    <li>• Engineering notation: a × 10^b where b is a multiple of 3</li>
                    <li>• Significant figures determine precision, not accuracy</li>
                    <li>• Leading zeros are never significant</li>
                    <li>• Trailing zeros are significant only if there's a decimal point</li>
                    <li>• Unit conversions maintain the same physical quantity</li>
                </ul>
            </div>
        </div>
    );
};

export default ScientificNotationConverter;
