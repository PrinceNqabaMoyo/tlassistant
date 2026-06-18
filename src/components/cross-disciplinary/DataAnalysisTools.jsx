import React, { useState, useEffect } from 'react';

const DataAnalysisTools = ({ initialData, onChange, isSubmitted }) => {
    const [dataPoints, setDataPoints] = useState(initialData.dataPoints || [
        { x: 1, y: 2.5, error: 0.3 },
        { x: 2, y: 4.1, error: 0.4 },
        { x: 3, y: 5.8, error: 0.5 },
        { x: 4, y: 7.2, error: 0.6 },
        { x: 5, y: 8.9, error: 0.7 }
    ]);
    const [analysisType, setAnalysisType] = useState(initialData.analysisType || 'linear');
    const [showGraph, setShowGraph] = useState(false);
    const [showTrendAnalysis, setShowTrendAnalysis] = useState(false);
    const [showErrorAnalysis, setShowErrorAnalysis] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [confidenceLevel, setConfidenceLevel] = useState(initialData.confidenceLevel || 0.95);

    useEffect(() => {
        const formattedData = {
            type: "data_analysis_tools",
            dataPoints: dataPoints,
            analysisType: analysisType,
            confidenceLevel: confidenceLevel,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [dataPoints, analysisType, confidenceLevel, onChange]);

    const calculateResults = () => {
        const results = {};
        
        if (dataPoints.length < 2) {
            results.error = 'Need at least 2 data points for analysis';
            return results;
        }
        
        // Basic statistics
        results.basicStats = calculateBasicStats();
        
        // Trend analysis
        if (analysisType === 'linear') {
            results.linearRegression = calculateLinearRegression();
        } else if (analysisType === 'polynomial') {
            results.polynomialFit = calculatePolynomialFit();
        } else if (analysisType === 'exponential') {
            results.exponentialFit = calculateExponentialFit();
        }
        
        // Error analysis
        results.errorAnalysis = calculateErrorAnalysis();
        
        // Correlation analysis
        results.correlation = calculateCorrelation();
        
        return results;
    };

    const calculateBasicStats = () => {
        const xValues = dataPoints.map(p => p.x);
        const yValues = dataPoints.map(p => p.y);
        
        const xMean = xValues.reduce((sum, val) => sum + val, 0) / xValues.length;
        const yMean = yValues.reduce((sum, val) => sum + val, 0) / yValues.length;
        
        const xVariance = xValues.reduce((sum, val) => sum + Math.pow(val - xMean, 2), 0) / xValues.length;
        const yVariance = yValues.reduce((sum, val) => sum + Math.pow(val - yMean, 2), 0) / yValues.length;
        
        return {
            xMean: xMean,
            yMean: yMean,
            xStdDev: Math.sqrt(xVariance),
            yStdDev: Math.sqrt(yVariance),
            xRange: Math.max(...xValues) - Math.min(...xValues),
            yRange: Math.max(...yValues) - Math.min(...yValues),
            count: dataPoints.length
        };
    };

    const calculateLinearRegression = () => {
        const n = dataPoints.length;
        const sumX = dataPoints.reduce((sum, p) => sum + p.x, 0);
        const sumY = dataPoints.reduce((sum, p) => sum + p.y, 0);
        const sumXY = dataPoints.reduce((sum, p) => sum + p.x * p.y, 0);
        const sumX2 = dataPoints.reduce((sum, p) => sum + p.x * p.x, 0);
        
        const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;
        
        // Calculate R-squared
        const yMean = sumY / n;
        const ssRes = dataPoints.reduce((sum, p) => sum + Math.pow(p.y - (slope * p.x + intercept), 2), 0);
        const ssTot = dataPoints.reduce((sum, p) => sum + Math.pow(p.y - yMean, 2), 0);
        const rSquared = 1 - (ssRes / ssTot);
        
        return {
            slope: slope,
            intercept: intercept,
            equation: `y = ${slope.toFixed(3)}x + ${intercept.toFixed(3)}`,
            rSquared: rSquared,
            correlation: Math.sqrt(rSquared) * (slope >= 0 ? 1 : -1)
        };
    };

    const calculatePolynomialFit = () => {
        // Simple quadratic fit (y = ax² + bx + c)
        const n = dataPoints.length;
        const sumX = dataPoints.reduce((sum, p) => sum + p.x, 0);
        const sumY = dataPoints.reduce((sum, p) => sum + p.y, 0);
        const sumX2 = dataPoints.reduce((sum, p) => sum + p.x * p.x, 0);
        const sumX3 = dataPoints.reduce((sum, p) => sum + Math.pow(p.x, 3), 0);
        const sumX4 = dataPoints.reduce((sum, p) => sum + Math.pow(p.x, 4), 0);
        const sumXY = dataPoints.reduce((sum, p) => sum + p.x * p.y, 0);
        const sumX2Y = dataPoints.reduce((sum, p) => sum + p.x * p.x * p.y, 0);
        
        // Solve system of equations using Cramer's rule
        const det = n * sumX2 * sumX4 + 2 * sumX * sumX2 * sumX3 - sumX2 * sumX2 * sumX2 - n * sumX3 * sumX3 - sumX * sumX * sumX4;
        
        if (Math.abs(det) < 1e-10) {
            return { error: 'Cannot fit polynomial to this data' };
        }
        
        const a = (n * sumX2 * sumX2Y + sumX * sumX3 * sumY + sumX2 * sumX * sumXY - sumX2 * sumX2 * sumY - n * sumX3 * sumXY - sumX * sumX * sumX2Y) / det;
        const b = (sumX * sumX2 * sumX2Y + sumX2 * sumX3 * sumY + sumX2 * sumX2 * sumXY - sumX2 * sumX2 * sumY - sumX * sumX3 * sumXY - sumX2 * sumX * sumX2Y) / det;
        const c = (sumX2 * sumX2 * sumX2Y + sumX3 * sumX3 * sumY + sumX * sumX2 * sumXY - sumX2 * sumX2 * sumY - sumX3 * sumX3 * sumXY - sumX * sumX2 * sumX2Y) / det;
        
        return {
            a: a,
            b: b,
            c: c,
            equation: `y = ${a.toFixed(3)}x² + ${b.toFixed(3)}x + ${c.toFixed(3)}`
        };
    };

    const calculateExponentialFit = () => {
        // y = ae^(bx) -> ln(y) = ln(a) + bx
        const n = dataPoints.length;
        const validPoints = dataPoints.filter(p => p.y > 0);
        
        if (validPoints.length !== n) {
            return { error: 'All y values must be positive for exponential fit' };
        }
        
        const lnY = validPoints.map(p => Math.log(p.y));
        const sumX = validPoints.reduce((sum, p) => sum + p.x, 0);
        const sumLnY = lnY.reduce((sum, val) => sum + val, 0);
        const sumXLnY = validPoints.reduce((sum, p, i) => sum + p.x * lnY[i], 0);
        const sumX2 = validPoints.reduce((sum, p) => sum + p.x * p.x, 0);
        
        const slope = (n * sumXLnY - sumX * sumLnY) / (n * sumX2 - sumX * sumX);
        const intercept = (sumLnY - slope * sumX) / n;
        
        return {
            a: Math.exp(intercept),
            b: slope,
            equation: `y = ${Math.exp(intercept).toFixed(3)}e^(${slope.toFixed(3)}x)`
        };
    };

    const calculateErrorAnalysis = () => {
        const errors = dataPoints.map(p => p.error || 0);
        const meanError = errors.reduce((sum, err) => sum + err, 0) / errors.length;
        const errorVariance = errors.reduce((sum, err) => sum + Math.pow(err - meanError, 2), 0) / errors.length;
        
        // Calculate weighted statistics
        const weights = errors.map(err => 1 / (err * err));
        const totalWeight = weights.reduce((sum, w) => sum + w, 0);
        const weightedMean = dataPoints.reduce((sum, p, i) => sum + p.y * weights[i], 0) / totalWeight;
        
        return {
            meanError: meanError,
            errorStdDev: Math.sqrt(errorVariance),
            weightedMean: weightedMean,
            totalError: errors.reduce((sum, err) => sum + err, 0)
        };
    };

    const calculateCorrelation = () => {
        const n = dataPoints.length;
        const xMean = dataPoints.reduce((sum, p) => sum + p.x, 0) / n;
        const yMean = dataPoints.reduce((sum, p) => sum + p.y, 0) / n;
        
        const numerator = dataPoints.reduce((sum, p) => sum + (p.x - xMean) * (p.y - yMean), 0);
        const xDenominator = Math.sqrt(dataPoints.reduce((sum, p) => sum + Math.pow(p.x - xMean, 2), 0));
        const yDenominator = Math.sqrt(dataPoints.reduce((sum, p) => sum + Math.pow(p.y - yMean, 2), 0));
        
        const correlation = numerator / (xDenominator * yDenominator);
        
        // Calculate confidence interval
        const tValue = getTValue(confidenceLevel, n - 2);
        const standardError = Math.sqrt((1 - correlation * correlation) / (n - 2));
        const marginOfError = tValue * standardError;
        
        return {
            pearson: correlation,
            confidenceInterval: [correlation - marginOfError, correlation + marginOfError],
            strength: getCorrelationStrength(correlation)
        };
    };

    const getTValue = (confidence, df) => {
        // Simplified t-distribution values for common confidence levels
        const tValues = {
            0.90: { 1: 6.314, 2: 2.920, 3: 2.353, 4: 2.132, 5: 2.015, 10: 1.812, 20: 1.725, 30: 1.697, 100: 1.660 },
            0.95: { 1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 10: 2.228, 20: 2.086, 30: 2.042, 100: 1.984 },
            0.99: { 1: 63.657, 2: 9.925, 3: 5.841, 4: 4.604, 5: 4.032, 10: 3.169, 20: 2.845, 30: 2.750, 100: 2.626 }
        };
        
        const level = confidenceLevel;
        const dfKey = df <= 5 ? df : df <= 10 ? 10 : df <= 20 ? 20 : df <= 30 ? 30 : 100;
        
        return tValues[level][dfKey] || 2.0;
    };

    const getCorrelationStrength = (correlation) => {
        const absCorr = Math.abs(correlation);
        if (absCorr >= 0.8) return 'Very Strong';
        if (absCorr >= 0.6) return 'Strong';
        if (absCorr >= 0.4) return 'Moderate';
        if (absCorr >= 0.2) return 'Weak';
        return 'Very Weak';
    };

    const addDataPoint = () => {
        const newId = Math.max(...dataPoints.map(p => p.id || 0)) + 1;
        const newPoint = {
            id: newId,
            x: dataPoints.length + 1,
            y: 0,
            error: 0.1
        };
        setDataPoints([...dataPoints, newPoint]);
    };

    const removeDataPoint = (index) => {
        if (dataPoints.length > 2) {
            setDataPoints(dataPoints.filter((_, i) => i !== index));
        }
    };

    const updateDataPoint = (index, field, value) => {
        const newDataPoints = [...dataPoints];
        newDataPoints[index] = { ...newDataPoints[index], [field]: parseFloat(value) || 0 };
        setDataPoints(newDataPoints);
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
                <h3 className="text-lg font-semibold text-gray-800">Data Analysis Tools</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowGraph(!showGraph)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showGraph 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showGraph ? 'Hide Graph' : 'Show Graph'}
                    </button>
                    <button
                        onClick={() => setShowTrendAnalysis(!showTrendAnalysis)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showTrendAnalysis 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showTrendAnalysis ? 'Hide Trend Analysis' : 'Show Trend Analysis'}
                    </button>
                    <button
                        onClick={() => setShowErrorAnalysis(!showErrorAnalysis)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showErrorAnalysis 
                                ? 'bg-purple-100 text-purple-700 hover:bg-purple-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showErrorAnalysis ? 'Hide Error Analysis' : 'Show Error Analysis'}
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

            {/* Analysis Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Analysis Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={analysisType} 
                    onChange={(e) => !isSubmitted && setAnalysisType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="linear">Linear Regression</option>
                    <option value="polynomial">Polynomial Fit (Quadratic)</option>
                    <option value="exponential">Exponential Fit</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {analysisType === 'linear' 
                        ? 'Fit a straight line to the data (y = mx + b)'
                        : analysisType === 'polynomial'
                        ? 'Fit a quadratic curve to the data (y = ax² + bx + c)'
                        : 'Fit an exponential curve to the data (y = ae^(bx))'
                    }
                </p>
            </div>

            {/* Data Input */}
            <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                <div className="flex items-center justify-between mb-4">
                    <h4 className="text-md font-medium text-blue-800">Data Points:</h4>
                    <button
                        onClick={addDataPoint}
                        disabled={isSubmitted}
                        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 transition-colors"
                    >
                        Add Point
                    </button>
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {dataPoints.map((point, index) => (
                        <div key={index} className="p-3 bg-white rounded border">
                            <div className="flex items-center justify-between mb-2">
                                <span className="font-medium text-gray-800">Point {index + 1}</span>
                                {dataPoints.length > 2 && (
                                    <button
                                        onClick={() => removeDataPoint(index)}
                                        disabled={isSubmitted}
                                        className="text-red-600 hover:text-red-800 disabled:opacity-50"
                                    >
                                        ×
                                    </button>
                                )}
                            </div>
                            <div className="grid grid-cols-3 gap-2">
                                <input
                                    type="number"
                                    step="0.1"
                                    className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
                                    value={point.x}
                                    onChange={(e) => updateDataPoint(index, 'x', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="X"
                                />
                                <input
                                    type="number"
                                    step="0.1"
                                    className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
                                    value={point.y}
                                    onChange={(e) => updateDataPoint(index, 'y', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Y"
                                />
                                <input
                                    type="number"
                                    step="0.1"
                                    min="0"
                                    className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
                                    value={point.error}
                                    onChange={(e) => updateDataPoint(index, 'error', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Error"
                                />
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Confidence Level */}
            <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                <h4 className="text-md font-medium text-green-800 mb-3">Analysis Settings:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Confidence Level:</label>
                        <select 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                            value={confidenceLevel} 
                            onChange={(e) => !isSubmitted && setConfidenceLevel(parseFloat(e.target.value))} 
                            disabled={isSubmitted}
                        >
                            <option value={0.90}>90% (α = 0.10)</option>
                            <option value={0.95}>95% (α = 0.05)</option>
                            <option value={0.99}>99% (α = 0.01)</option>
                        </select>
                    </div>
                    <div className="pt-6">
                        <div className="text-sm text-gray-600">
                            <div><strong>Current Level:</strong> {(confidenceLevel * 100).toFixed(0)}%</div>
                            <div><strong>Significance Level:</strong> α = {formatNumber(1 - confidenceLevel)}</div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Analysis Results:</h4>
                {results.error ? (
                    <div className="text-red-600 text-center p-4">{results.error}</div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Data Points</div>
                            <div className="text-xl text-purple-700">{results.basicStats?.count || 0}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">X Range</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.basicStats?.xRange || 0)}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Y Range</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.basicStats?.yRange || 0)}</div>
                        </div>
                    </div>
                )}
            </div>

            {/* Trend Analysis */}
            {showTrendAnalysis && results && !results.error && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Trend Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {analysisType === 'linear' && results.linearRegression && (
                            <div className="p-3 bg-white rounded border">
                                <h5 className="font-medium text-gray-800 mb-2">Linear Regression:</h5>
                                <div className="text-sm text-gray-600 space-y-1">
                                    <div><strong>Equation:</strong> {results.linearRegression.equation}</div>
                                    <div><strong>Slope:</strong> {formatNumber(results.linearRegression.slope)}</div>
                                    <div><strong>Intercept:</strong> {formatNumber(results.linearRegression.intercept)}</div>
                                    <div><strong>R²:</strong> {formatNumber(results.linearRegression.rSquared)}</div>
                                    <div><strong>Correlation:</strong> {formatNumber(results.linearRegression.correlation)}</div>
                                </div>
                            </div>
                        )}
                        
                        {analysisType === 'polynomial' && results.polynomialFit && (
                            <div className="p-3 bg-white rounded border">
                                <h5 className="font-medium text-gray-800 mb-2">Polynomial Fit:</h5>
                                <div className="text-sm text-gray-600 space-y-1">
                                    <div><strong>Equation:</strong> {results.polynomialFit.equation}</div>
                                    <div><strong>Coefficient a:</strong> {formatNumber(results.polynomialFit.a)}</div>
                                    <div><strong>Coefficient b:</strong> {formatNumber(results.polynomialFit.b)}</div>
                                    <div><strong>Coefficient c:</strong> {formatNumber(results.polynomialFit.c)}</div>
                                </div>
                            </div>
                        )}
                        
                        {analysisType === 'exponential' && results.exponentialFit && (
                            <div className="p-3 bg-white rounded border">
                                <h5 className="font-medium text-gray-800 mb-2">Exponential Fit:</h5>
                                <div className="text-sm text-gray-600 space-y-1">
                                    <div><strong>Equation:</strong> {results.exponentialFit.equation}</div>
                                    <div><strong>Coefficient a:</strong> {formatNumber(results.exponentialFit.a)}</div>
                                    <div><strong>Coefficient b:</strong> {formatNumber(results.exponentialFit.b)}</div>
                                </div>
                            </div>
                        )}
                        
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Correlation Analysis:</h5>
                            <div className="text-sm text-gray-600 space-y-1">
                                <div><strong>Pearson Correlation:</strong> {formatNumber(results.correlation?.pearson || 0)}</div>
                                <div><strong>Strength:</strong> {results.correlation?.strength || 'N/A'}</div>
                                <div><strong>Confidence Interval:</strong></div>
                                <div className="ml-2">[{formatNumber(results.correlation?.confidenceInterval?.[0] || 0)}, {formatNumber(results.correlation?.confidenceInterval?.[1] || 0)}]</div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Error Analysis */}
            {showErrorAnalysis && results && !results.error && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Error Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Mean Error</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.errorAnalysis?.meanError || 0)}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Error Std Dev</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.errorAnalysis?.errorStdDev || 0)}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Weighted Mean</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.errorAnalysis?.weightedMean || 0)}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total Error</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.errorAnalysis?.totalError || 0)}</div>
                        </div>
                    </div>
                </div>
            )}

            {/* Data Graph */}
            {showGraph && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Data Visualization:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Graph axes */}
                            <line x1="50" y1="250" x2="350" y2="250" stroke="black" strokeWidth="1" />
                            <line x1="50" y1="50" x2="50" y2="250" stroke="black" strokeWidth="1" />
                            
                            {/* Labels */}
                            <text x="200" y="270" className="text-xs">X Values</text>
                            <text x="30" y="150" transform="rotate(-90 30 150)" className="text-xs">Y Values</text>
                            
                            {/* Plot data points with error bars */}
                            {dataPoints.map((point, index) => {
                                const x = 50 + (point.x / Math.max(...dataPoints.map(p => p.x))) * 300;
                                const y = 250 - (point.y / Math.max(...dataPoints.map(p => p.y))) * 200;
                                const errorBar = (point.error / Math.max(...dataPoints.map(p => p.y))) * 200;
                                
                                return (
                                    <g key={index}>
                                        {/* Error bar */}
                                        <line x1={x} y1={y - errorBar} x2={x} y2={y + errorBar} stroke="red" strokeWidth="1" />
                                        <line x1={x - 5} y1={y - errorBar} x2={x + 5} y2={y - errorBar} stroke="red" strokeWidth="1" />
                                        <line x1={x - 5} y1={y + errorBar} x2={x + 5} y2={y + errorBar} stroke="red" strokeWidth="1" />
                                        
                                        {/* Data point */}
                                        <circle cx={x} cy={y} r="4" fill="blue" />
                                    </g>
                                );
                            })}
                            
                            {/* Trend line for linear regression */}
                            {analysisType === 'linear' && results.linearRegression && !results.error && (
                                <line 
                                    x1="50" 
                                    y1={250 - (results.linearRegression.intercept / Math.max(...dataPoints.map(p => p.y))) * 200} 
                                    x2="350" 
                                    y2={250 - ((results.linearRegression.slope * Math.max(...dataPoints.map(p => p.x)) + results.linearRegression.intercept) / Math.max(...dataPoints.map(p => p.y))) * 200} 
                                    stroke="green" 
                                    strokeWidth="2" 
                                    strokeDasharray="5,5"
                                />
                            )}
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Basic Statistics:</strong></div>
                        <div>• X Mean: {formatNumber(results.basicStats?.xMean || 0)}</div>
                        <div>• Y Mean: {formatNumber(results.basicStats?.yMean || 0)}</div>
                        <div>• X Standard Deviation: {formatNumber(results.basicStats?.xStdDev || 0)}</div>
                        <div>• Y Standard Deviation: {formatNumber(results.basicStats?.yStdDev || 0)}</div>
                        
                        {analysisType === 'linear' && results.linearRegression && (
                            <>
                                <div><strong>Linear Regression:</strong></div>
                                <div>• Slope (m): Σ(xy) - nΣxΣy / (Σx² - n(Σx)²) = {formatNumber(results.linearRegression.slope)}</div>
                                <div>• Intercept (b): (Σy - mΣx) / n = {formatNumber(results.linearRegression.intercept)}</div>
                                <div>• R²: 1 - (SSres / SStot) = {formatNumber(results.linearRegression.rSquared)}</div>
                            </>
                        )}
                        
                        <div><strong>Correlation Analysis:</strong></div>
                        <div>• Pearson Correlation: r = {formatNumber(results.correlation?.pearson || 0)}</div>
                        <div>• Strength: {results.correlation?.strength || 'N/A'}</div>
                        <div>• Confidence Level: {(confidenceLevel * 100).toFixed(0)}%</div>
                        <div>• T-value: {getTValue(confidenceLevel, dataPoints.length - 2)}</div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Linear regression fits a straight line: y = mx + b</li>
                    <li>• R² measures how well the line fits the data (0 to 1)</li>
                    <li>• Correlation ranges from -1 (perfect negative) to +1 (perfect positive)</li>
                    <li>• Error bars show uncertainty in measurements</li>
                    <li>• Confidence intervals indicate statistical reliability</li>
                    <li>• Use polynomial fit for curved relationships</li>
                    <li>• Exponential fit for growth/decay patterns</li>
                </ul>
            </div>
        </div>
    );
};

export default DataAnalysisTools;
