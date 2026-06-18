import React, { useState, useEffect } from 'react';

const StatisticalAnalysisInput = ({ initialData, onChange, isSubmitted }) => {
    const [statsData, setStatsData] = useState(initialData || {
        title: "Statistical Analysis",
        dataSet: [],
        chartType: 'histogram', // 'histogram', 'box_plot', 'scatter_plot', 'bar_chart'
        showStatistics: true,
        showChart: true,
        binCount: 5,
        xAxisLabel: "Values",
        yAxisLabel: "Frequency",
        color: '#3B82F6'
    });

    useEffect(() => {
        // Ensure dataSet is always initialized
        if (!statsData.dataSet) {
            setStatsData(prev => ({ ...prev, dataSet: [] }));
            return;
        }
        
        onChange(statsData);
    }, [statsData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setStatsData(prev => ({ ...prev, [field]: value }));
    };

    const addDataPoint = () => {
        if (isSubmitted) return;
        const newPoint = {
            id: Date.now(),
            value: '',
            label: ''
        };
        setStatsData(prev => ({
            ...prev,
            dataSet: [...(prev.dataSet || []), newPoint]
        }));
    };

    const removeDataPoint = (pointId) => {
        if (isSubmitted) return;
        setStatsData(prev => ({
            ...prev,
            dataSet: (prev.dataSet || []).filter(p => p.id !== pointId)
        }));
    };

    const updateDataPoint = (pointId, field, value) => {
        if (isSubmitted) return;
        setStatsData(prev => ({
            ...prev,
            dataSet: (prev.dataSet || []).map(p => 
                p.id === pointId ? { ...p, [field]: value } : p
            )
        }));
    };

    const getNumericData = () => {
        if (!statsData.dataSet || !Array.isArray(statsData.dataSet)) {
            return [];
        }
        return statsData.dataSet
            .map(point => parseFloat(point.value))
            .filter(value => !isNaN(value))
            .sort((a, b) => a - b);
    };

    const calculateMean = (data) => {
        if (data.length === 0) return 0;
        return data.reduce((sum, val) => sum + val, 0) / data.length;
    };

    const calculateMedian = (data) => {
        if (data.length === 0) return 0;
        const sorted = [...data].sort((a, b) => a - b);
        const mid = Math.floor(sorted.length / 2);
        return sorted.length % 2 === 0 
            ? (sorted[mid - 1] + sorted[mid]) / 2 
            : sorted[mid];
    };

    const calculateMode = (data) => {
        if (data.length === 0) return [];
        const frequency = {};
        data.forEach(value => {
            frequency[value] = (frequency[value] || 0) + 1;
        });
        const maxFreq = Math.max(...Object.values(frequency));
        return Object.keys(frequency).filter(key => frequency[key] === maxFreq);
    };

    const calculateRange = (data) => {
        if (data.length === 0) return 0;
        return Math.max(...data) - Math.min(...data);
    };

    const calculateStandardDeviation = (data) => {
        if (data.length === 0) return 0;
        const mean = calculateMean(data);
        const squaredDiffs = data.map(value => Math.pow(value - mean, 2));
        const variance = calculateMean(squaredDiffs);
        return Math.sqrt(variance);
    };

    const calculateQuartiles = (data) => {
        if (data.length === 0) return { q1: 0, q2: 0, q3: 0 };
        const sorted = [...data].sort((a, b) => a - b);
        const n = sorted.length;
        
        const q1 = sorted[Math.floor(n * 0.25)];
        const q2 = sorted[Math.floor(n * 0.5)];
        const q3 = sorted[Math.floor(n * 0.75)];
        
        return { q1, q2, q3 };
    };

    const createHistogram = (data) => {
        if (data.length === 0) return [];
        
        const min = Math.min(...data);
        const max = Math.max(...data);
        const range = max - min;
        const binWidth = range / statsData.binCount;
        
        const bins = Array(statsData.binCount).fill(0);
        
        data.forEach(value => {
            const binIndex = Math.min(
                Math.floor((value - min) / binWidth),
                statsData.binCount - 1
            );
            bins[binIndex]++;
        });
        
        return bins.map((count, index) => ({
            bin: index,
            start: min + index * binWidth,
            end: min + (index + 1) * binWidth,
            count,
            label: `${(min + index * binWidth).toFixed(1)}-${(min + (index + 1) * binWidth).toFixed(1)}`
        }));
    };

    const renderHistogram = () => {
        const data = getNumericData();
        const histogram = createHistogram(data);
        const maxCount = Math.max(...histogram.map(bin => bin.count));
        
        return (
            <div className="flex flex-col items-center">
                <div className="w-full max-w-md h-48 border-l-2 border-b-2 border-gray-300 relative">
                    {histogram.map((bin, index) => (
                        <div
                            key={index}
                            className="absolute bottom-0 bg-blue-500 border border-blue-600"
                            style={{
                                left: `${(index / histogram.length) * 100}%`,
                                width: `${100 / histogram.length}%`,
                                height: `${(bin.count / maxCount) * 100}%`,
                                backgroundColor: statsData.color
                            }}
                            title={`${bin.label}: ${bin.count} values`}
                        />
                    ))}
                </div>
                <div className="w-full max-w-md flex justify-between text-xs text-gray-600 mt-2">
                    {histogram.map((bin, index) => (
                        <span key={index} className="text-center">
                            {bin.start.toFixed(1)}
                        </span>
                    ))}
                    <span>{histogram[histogram.length - 1]?.end.toFixed(1)}</span>
                </div>
                <p className="text-sm text-gray-600 mt-2">Histogram</p>
            </div>
        );
    };

    const renderBoxPlot = () => {
        const data = getNumericData();
        if (data.length === 0) return <p className="text-gray-500">No data available</p>;
        
        const { q1, q2, q3 } = calculateQuartiles(data);
        const min = Math.min(...data);
        const max = Math.max(...data);
        const iqr = q3 - q1;
        
        const totalRange = max - min;
        const q1Pos = ((q1 - min) / totalRange) * 100;
        const q2Pos = ((q2 - min) / totalRange) * 100;
        const q3Pos = ((q3 - min) / totalRange) * 100;
        
        return (
            <div className="flex flex-col items-center">
                <div className="w-full max-w-md h-16 border-2 border-gray-300 relative bg-gray-50">
                    {/* Whiskers */}
                    <div className="absolute top-1/2 transform -translate-y-1/2 w-full">
                        <div className="h-0.5 bg-gray-400" style={{ width: '100%' }} />
                    </div>
                    
                    {/* Box */}
                    <div
                        className="absolute top-2 bottom-2 bg-blue-500 border border-blue-600"
                        style={{
                            left: `${q1Pos}%`,
                            width: `${q3Pos - q1Pos}%`
                        }}
                    />
                    
                    {/* Median line */}
                    <div
                        className="absolute top-1 bottom-1 w-0.5 bg-red-500"
                        style={{ left: `${q2Pos}%` }}
                    />
                    
                    {/* Min and Max markers */}
                    <div className="absolute top-1/2 transform -translate-y-1/2 w-2 h-2 bg-gray-600 rounded-full" style={{ left: '0%' }} />
                    <div className="absolute top-1/2 transform -translate-y-1/2 w-2 h-2 bg-gray-600 rounded-full" style={{ right: '0%' }} />
                </div>
                
                <div className="w-full max-w-md flex justify-between text-xs text-gray-600 mt-2">
                    <span>{min.toFixed(1)}</span>
                    <span>Q1: {q1.toFixed(1)}</span>
                    <span>Q2: {q2.toFixed(1)}</span>
                    <span>Q3: {q3.toFixed(1)}</span>
                    <span>{max.toFixed(1)}</span>
                </div>
                <p className="text-sm text-gray-600 mt-2">Box Plot</p>
            </div>
        );
    };

    const renderScatterPlot = () => {
        const data = getNumericData();
        if (data.length === 0) return <p className="text-gray-500">No data available</p>;
        
        const min = Math.min(...data);
        const max = Math.max(...data);
        const range = max - min;
        
        return (
            <div className="flex flex-col items-center">
                <div className="w-full max-w-md h-48 border-l-2 border-b-2 border-gray-300 relative">
                    {data.map((value, index) => {
                        const xPos = (index / (data.length - 1)) * 100;
                        const yPos = range > 0 ? ((value - min) / range) * 100 : 50;
                        
                        return (
                            <div
                                key={index}
                                className="absolute w-2 h-2 rounded-full border border-white"
                                style={{
                                    left: `${xPos}%`,
                                    bottom: `${yPos}%`,
                                    backgroundColor: statsData.color,
                                    transform: 'translate(-50%, 50%)'
                                }}
                                title={`Point ${index + 1}: ${value}`}
                            />
                        );
                    })}
                </div>
                <div className="w-full max-w-md flex justify-between text-xs text-gray-600 mt-2">
                    <span>0</span>
                    <span>{Math.floor(data.length / 2)}</span>
                    <span>{data.length}</span>
                </div>
                <p className="text-sm text-gray-600 mt-2">Scatter Plot</p>
            </div>
        );
    };

    const renderChart = () => {
        switch (statsData.chartType) {
            case 'histogram':
                return renderHistogram();
            case 'box_plot':
                return renderBoxPlot();
            case 'scatter_plot':
                return renderScatterPlot();
            default:
                return renderHistogram();
        }
    };

    // Don't render if not properly initialized
    if (!statsData.dataSet) {
        return (
            <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
                <h3 className="font-semibold text-gray-700 mb-4">Statistical Analysis</h3>
                <div className="text-center py-8 text-gray-500">
                    <p>Loading statistical analysis configuration...</p>
                </div>
            </div>
        );
    }

    const numericData = getNumericData();
    const mean = calculateMean(numericData);
    const median = calculateMedian(numericData);
    const mode = calculateMode(numericData);
    const range = calculateRange(numericData);
    const stdDev = calculateStandardDeviation(numericData);

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Statistical Analysis</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={statsData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Analysis Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Chart Type:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={statsData.chartType}
                        onChange={(e) => handleFieldChange('chartType', e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="histogram">Histogram</option>
                        <option value="box_plot">Box Plot</option>
                        <option value="scatter_plot">Scatter Plot</option>
                        <option value="bar_chart">Bar Chart</option>
                    </select>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Number of Bins:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={statsData.binCount}
                        onChange={(e) => handleFieldChange('binCount', parseInt(e.target.value) || 5)}
                        disabled={isSubmitted}
                        min="2"
                        max="20"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Color:</label>
                    <input
                        type="color"
                        className="w-full h-10 border border-gray-300 rounded-md"
                        value={statsData.color}
                        onChange={(e) => handleFieldChange('color', e.target.value)}
                        disabled={isSubmitted}
                    />
                </div>
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={statsData.showStatistics}
                        onChange={(e) => handleFieldChange('showStatistics', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Statistics</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={statsData.showChart}
                        onChange={(e) => handleFieldChange('showChart', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Chart</span>
                </label>
            </div>

            {/* Data Input */}
            <div className="mb-4">
                <div className="flex justify-between items-center mb-2">
                    <label className="block text-sm font-medium text-gray-700">Data Set:</label>
                    {!isSubmitted && (
                        <button
                            onClick={addDataPoint}
                            className="px-3 py-1 bg-blue-500 text-white text-sm rounded-md hover:bg-blue-600"
                        >
                            Add Data Point
                        </button>
                    )}
                </div>
                
                {statsData.dataSet.length === 0 ? (
                    <p className="text-sm text-gray-500 italic">No data points added yet. Click "Add Data Point" to enter your data.</p>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 max-h-40 overflow-y-auto">
                        {statsData.dataSet.map((point) => (
                            <div key={point.id} className="flex items-center space-x-2 p-2 bg-white border border-gray-200 rounded-md">
                                <input
                                    type="number"
                                    className="flex-1 p-1 border border-gray-300 rounded text-sm"
                                    value={point.value}
                                    onChange={(e) => updateDataPoint(point.id, 'value', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Value"
                                    step="any"
                                />
                                <input
                                    type="text"
                                    className="flex-1 p-1 border border-gray-300 rounded text-sm"
                                    value={point.label}
                                    onChange={(e) => updateDataPoint(point.id, 'label', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Label (optional)"
                                />
                                {!isSubmitted && (
                                    <button
                                        onClick={() => removeDataPoint(point.id)}
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

            {/* Statistics Display */}
            {statsData.showStatistics && numericData.length > 0 && (
                <div className="mb-4">
                    <h4 className="font-semibold text-gray-700 mb-2">Statistical Summary:</h4>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Mean</p>
                            <p className="text-xl font-bold text-blue-600">{mean.toFixed(2)}</p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Median</p>
                            <p className="text-xl font-bold text-green-600">{median.toFixed(2)}</p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Mode</p>
                            <p className="text-xl font-bold text-purple-600">
                                {mode.length > 0 ? mode.join(', ') : 'None'}
                            </p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Range</p>
                            <p className="text-xl font-bold text-orange-600">{range.toFixed(2)}</p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Std Dev</p>
                            <p className="text-xl font-bold text-red-600">{stdDev.toFixed(2)}</p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Count</p>
                            <p className="text-xl font-bold text-gray-600">{numericData.length}</p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Min</p>
                            <p className="text-xl font-bold text-indigo-600">{Math.min(...numericData).toFixed(2)}</p>
                        </div>
                        <div className="bg-white p-3 border border-gray-200 rounded-lg text-center">
                            <p className="text-sm text-gray-600">Max</p>
                            <p className="text-xl font-bold text-pink-600">{Math.max(...numericData).toFixed(2)}</p>
                        </div>
                    </div>
                </div>
            )}

            {/* Chart Display */}
            {statsData.showChart && numericData.length > 0 && (
                <div className="mb-4">
                    <h4 className="font-semibold text-gray-700 mb-2">Data Visualization:</h4>
                    {renderChart()}
                </div>
            )}

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Statistical Analysis Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Add data points by entering numeric values</li>
                    <li>Choose different chart types to visualize your data</li>
                    <li>View calculated statistics including mean, median, mode, and standard deviation</li>
                    <li>Adjust the number of bins for histogram visualization</li>
                    <li>Use the color picker to customize chart appearance</li>
                </ul>
            </div>
        </div>
    );
};

export default StatisticalAnalysisInput;
