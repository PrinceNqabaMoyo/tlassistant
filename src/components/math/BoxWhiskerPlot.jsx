import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const BoxWhiskerPlot = ({ initialData, onChange, isSubmitted }) => {
    const [plotData, setPlotData] = useState(initialData || {
        title: "Box and Whisker Plot",
        dataSet: [
            { label: "Group A", values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] },
            { label: "Group B", values: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] }
        ],
        showOutliers: true,
        showMean: true,
        showMedian: true,
        showQuartiles: true,
        color: '#3B82F6'
    });

    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    useEffect(() => {
        if (onChange) {
            onChange(plotData);
        }
    }, [plotData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawPlot();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [plotData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawPlot();
    }, []);

    // Redraw full-screen canvas when modal opens or plotData changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            drawPlot(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, plotData]);

    // Calculate statistics for a dataset
    const calculateStatistics = (values) => {
        const sorted = [...values].sort((a, b) => a - b);
        const n = sorted.length;
        
        if (n === 0) return null;
        
        // Median
        const median = n % 2 === 0 
            ? (sorted[n/2 - 1] + sorted[n/2]) / 2 
            : sorted[Math.floor(n/2)];
        
        // Quartiles
        const q1Index = Math.floor((n + 1) * 0.25);
        const q3Index = Math.floor((n + 1) * 0.75);
        const q1 = sorted[q1Index];
        const q3 = sorted[q3Index];
        
        // Interquartile range
        const iqr = q3 - q1;
        
        // Outlier bounds
        const lowerBound = q1 - 1.5 * iqr;
        const upperBound = q3 + 1.5 * iqr;
        
        // Outliers
        const outliers = sorted.filter(x => x < lowerBound || x > upperBound);
        
        // Mean
        const mean = sorted.reduce((sum, x) => sum + x, 0) / n;
        
        // Min and max (excluding outliers)
        const nonOutliers = sorted.filter(x => x >= lowerBound && x <= upperBound);
        const min = nonOutliers[0];
        const max = nonOutliers[nonOutliers.length - 1];
        
        return {
            min, max, q1, median, q3, mean, outliers, iqr
        };
    };

    const drawPlot = (targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff'; // White background
        ctx.fillRect(0, 0, width, height);

        const { dataSet, showOutliers, showMean, showMedian, showQuartiles, color } = plotData;

        if (!dataSet || dataSet.length === 0) return;

        // Calculate plot dimensions
        const margin = 60;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;
        const boxWidth = Math.min(80, plotWidth / dataSet.length);
        const spacing = (plotWidth - boxWidth * dataSet.length) / (dataSet.length + 1);

        // Find global min and max for scaling
        let globalMin = Infinity;
        let globalMax = -Infinity;
        
        dataSet.forEach(dataset => {
            if (dataset.values && dataset.values.length > 0) {
                const stats = calculateStatistics(dataset.values);
                if (stats) {
                    globalMin = Math.min(globalMin, stats.min);
                    globalMax = Math.max(globalMax, stats.max);
                    if (showOutliers && stats.outliers.length > 0) {
                        globalMin = Math.min(globalMin, ...stats.outliers);
                        globalMax = Math.max(globalMax, ...stats.outliers);
                    }
                }
            }
        });

        if (globalMin === Infinity || globalMax === -Infinity) return;

        // Add some padding
        const range = globalMax - globalMin;
        const padding = range * 0.1;
        globalMin -= padding;
        globalMax += padding;

        // Scale function
        const scaleY = (value) => {
            return height - margin - ((value - globalMin) / (globalMax - globalMin)) * plotHeight;
        };

        // Draw y-axis
        ctx.strokeStyle = '#000000'; // Black bold axes
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(margin, margin);
        ctx.lineTo(margin, height - margin);
        ctx.stroke();

        // Draw y-axis labels
        ctx.fillStyle = '#374151';
        ctx.font = '12px Arial';
        ctx.textAlign = 'right';
        const yTicks = 5;
        for (let i = 0; i <= yTicks; i++) {
            const value = globalMin + (i / yTicks) * (globalMax - globalMin);
            const y = scaleY(value);
            ctx.beginPath();
            ctx.moveTo(margin - 5, y);
            ctx.lineTo(margin, y);
            ctx.stroke();
            ctx.fillText(value.toFixed(1), margin - 10, y + 4);
        }

        // Draw x-axis
        ctx.strokeStyle = '#000000'; // Black bold axes
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(margin, height - margin);
        ctx.lineTo(width - margin, height - margin);
        ctx.stroke();

        // Draw each box plot
        dataSet.forEach((dataset, index) => {
            if (!dataset.values || dataset.values.length === 0) return;

            const stats = calculateStatistics(dataset.values);
            if (!stats) return;

            const x = margin + spacing + index * (boxWidth + spacing) + boxWidth / 2;
            const boxLeft = x - boxWidth / 2;
            const boxRight = x + boxWidth / 2;

            // Draw whiskers
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            
            // Lower whisker
            ctx.beginPath();
            ctx.moveTo(x, scaleY(stats.min));
            ctx.lineTo(x, scaleY(stats.q1));
            ctx.stroke();
            
            // Upper whisker
            ctx.beginPath();
            ctx.moveTo(x, scaleY(stats.q3));
            ctx.lineTo(x, scaleY(stats.max));
            ctx.stroke();

            // Draw box
            ctx.fillStyle = color + '20'; // Add transparency
            ctx.fillRect(boxLeft, scaleY(stats.q3), boxWidth, scaleY(stats.q1) - scaleY(stats.q3));
            ctx.strokeRect(boxLeft, scaleY(stats.q3), boxWidth, scaleY(stats.q1) - scaleY(stats.q3));

            // Draw median line
            if (showMedian) {
                ctx.strokeStyle = '#ef4444';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(boxLeft, scaleY(stats.median));
                ctx.lineTo(boxRight, scaleY(stats.median));
                ctx.stroke();
            }

            // Draw mean line
            if (showMean) {
                ctx.strokeStyle = '#10b981';
                ctx.lineWidth = 2;
                ctx.setLineDash([3, 3]);
                ctx.beginPath();
                ctx.moveTo(boxLeft, scaleY(stats.mean));
                ctx.lineTo(boxRight, scaleY(stats.mean));
                ctx.stroke();
                ctx.setLineDash([]);
            }

            // Draw outliers
            if (showOutliers && stats.outliers.length > 0) {
                ctx.fillStyle = '#ef4444';
                stats.outliers.forEach(outlier => {
                    const outlierY = scaleY(outlier);
                    ctx.beginPath();
                    ctx.arc(x, outlierY, 3, 0, 2 * Math.PI);
                    ctx.fill();
                });
            }

            // Draw quartile lines
            if (showQuartiles) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 1;
                // Q1 line
                ctx.beginPath();
                ctx.moveTo(boxLeft, scaleY(stats.q1));
                ctx.lineTo(boxRight, scaleY(stats.q1));
                ctx.stroke();
                // Q3 line
                ctx.beginPath();
                ctx.moveTo(boxLeft, scaleY(stats.q3));
                ctx.lineTo(boxRight, scaleY(stats.q3));
                ctx.stroke();
            }

            // Draw dataset label
            ctx.fillStyle = '#374151';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(dataset.label, x, height - margin + 20);
        });

        // Draw title
        ctx.fillStyle = '#374151';
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(plotData.title, width / 2, 30);

        // Draw legend
        let legendY = 50;
        ctx.font = '12px Arial';
        ctx.textAlign = 'left';
        
        if (showMedian) {
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(width - 150, legendY);
            ctx.lineTo(width - 120, legendY);
            ctx.stroke();
            ctx.fillStyle = '#374151';
            ctx.fillText('Median', width - 110, legendY + 4);
            legendY += 20;
        }
        
        if (showMean) {
            ctx.strokeStyle = '#10b981';
            ctx.lineWidth = 2;
            ctx.setLineDash([3, 3]);
            ctx.beginPath();
            ctx.moveTo(width - 150, legendY);
            ctx.lineTo(width - 120, legendY);
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = '#374151';
            ctx.fillText('Mean', width - 110, legendY + 4);
            legendY += 20;
        }
        
        if (showOutliers) {
            ctx.fillStyle = '#ef4444';
            ctx.beginPath();
            ctx.arc(width - 135, legendY, 3, 0, 2 * Math.PI);
            ctx.fill();
            ctx.fillStyle = '#374151';
            ctx.fillText('Outliers', width - 110, legendY + 4);
        }
    };

    const handleInputChange = (field, value) => {
        setPlotData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    const handleDatasetChange = (index, field, value) => {
        setPlotData(prev => ({
            ...prev,
            dataSet: prev.dataSet.map((dataset, i) => 
                i === index ? { ...dataset, [field]: value } : dataset
            )
        }));
    };

    const addDataset = () => {
        setPlotData(prev => ({
            ...prev,
            dataSet: [...prev.dataSet, { label: `Group ${prev.dataSet.length + 1}`, values: [1, 2, 3, 4, 5] }]
        }));
    };

    const removeDataset = (index) => {
        setPlotData(prev => ({
            ...prev,
            dataSet: prev.dataSet.filter((_, i) => i !== index)
        }));
    };

    const addValue = (datasetIndex) => {
        setPlotData(prev => ({
            ...prev,
            dataSet: prev.dataSet.map((dataset, i) => 
                i === datasetIndex 
                    ? { ...dataset, values: [...dataset.values, Math.floor(Math.random() * 20) + 1] }
                    : dataset
            )
        }));
    };

    const removeValue = (datasetIndex, valueIndex) => {
        setPlotData(prev => ({
            ...prev,
            dataSet: prev.dataSet.map((dataset, i) => 
                i === datasetIndex 
                    ? { ...dataset, values: dataset.values.filter((_, j) => j !== valueIndex) }
                    : dataset
            )
        }));
    };

    const updateValue = (datasetIndex, valueIndex, newValue) => {
        setPlotData(prev => ({
            ...prev,
            dataSet: prev.dataSet.map((dataset, i) => 
                i === datasetIndex 
                    ? { 
                        ...dataset, 
                        values: dataset.values.map((val, j) => 
                            j === valueIndex ? parseFloat(newValue) || 0 : val
                        )
                    }
                    : dataset
            )
        }));
    };

    const handleToggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    const handleOpenFullScreen = () => {
        setIsFullScreenOpen(true);
        // Redraw the plot in full-screen canvas after modal opens
        setTimeout(() => {
            if (fullScreenCanvasRef.current) {
                drawPlot(fullScreenCanvasRef.current);
            }
        }, 100);
    };

    const handleCloseFullScreen = () => {
        setIsFullScreenOpen(false);
    };

    // Parameter Panel Component
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Box and Whisker Plot Parameters</h3>
            
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                <input
                    type="text"
                    value={plotData.title}
                    onChange={(e) => handleInputChange('title', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                    disabled={isSubmitted}
                />
            </div>

            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Color:</label>
                <input
                    type="color"
                    value={plotData.color}
                    onChange={(e) => handleInputChange('color', e.target.value)}
                    className="w-full h-10 border border-gray-300 rounded-md"
                    disabled={isSubmitted}
                />
            </div>

            {/* Display Options */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Display Options</h4>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={plotData.showOutliers}
                        onChange={(e) => handleInputChange('showOutliers', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Outliers</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={plotData.showMean}
                        onChange={(e) => handleInputChange('showMean', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Mean</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={plotData.showMedian}
                        onChange={(e) => handleInputChange('showMedian', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Median</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={plotData.showQuartiles}
                        onChange={(e) => handleInputChange('showQuartiles', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Quartiles</span>
                </label>
            </div>

            {/* Dataset Management */}
            <div className="space-y-4">
                <div className="flex justify-between items-center">
                    <h4 className="font-medium text-gray-700">Datasets</h4>
                    <button
                        onClick={addDataset}
                        className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                        disabled={isSubmitted}
                    >
                        Add Dataset
                    </button>
                </div>
                
                <div className="space-y-3 max-h-96 overflow-y-auto">
                    {plotData.dataSet.map((dataset, datasetIndex) => (
                        <div key={datasetIndex} className="border border-gray-200 rounded-lg p-3 bg-gray-50">
                            <div className="flex justify-between items-center mb-2">
                                <input
                                    type="text"
                                    value={dataset.label}
                                    onChange={(e) => handleDatasetChange(datasetIndex, 'label', e.target.value)}
                                    className="font-medium text-gray-800 border border-gray-300 rounded px-2 py-1 text-sm w-32"
                                    disabled={isSubmitted}
                                />
                                <button
                                    onClick={() => removeDataset(datasetIndex)}
                                    className="text-red-600 hover:text-red-800 text-sm"
                                    disabled={isSubmitted}
                                >
                                    Remove
                                </button>
                            </div>
                            
                            <div className="flex items-center space-x-2 mb-2">
                                <span className="text-sm text-gray-600">Values:</span>
                                <button
                                    onClick={() => addValue(datasetIndex)}
                                    className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                                    disabled={isSubmitted}
                                >
                                    Add Value
                                </button>
                            </div>
                            
                            <div className="flex flex-wrap gap-1 max-h-32 overflow-y-auto">
                                {dataset.values.map((value, valueIndex) => (
                                    <div key={valueIndex} className="flex items-center space-x-1">
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => updateValue(datasetIndex, valueIndex, e.target.value)}
                                            className="w-14 px-1 py-1 border border-gray-300 rounded text-xs"
                                            disabled={isSubmitted}
                                        />
                                        <button
                                            onClick={() => removeValue(datasetIndex, valueIndex)}
                                            className="text-red-500 hover:text-red-700 text-xs"
                                            disabled={isSubmitted}
                                        >
                                            ×
                                        </button>
                                    </div>
                                ))}
                            </div>
                            
                            {/* Statistics Display */}
                            {(() => {
                                const stats = calculateStatistics(dataset.values);
                                if (!stats) return null;
                                
                                return (
                                    <div className="mt-2 p-2 bg-white rounded text-xs border">
                                        <div className="grid grid-cols-2 gap-1">
                                            <div>Min: {stats.min.toFixed(2)}</div>
                                            <div>Q1: {stats.q1.toFixed(2)}</div>
                                            <div>Median: {stats.median.toFixed(2)}</div>
                                            <div>Q3: {stats.q3.toFixed(2)}</div>
                                            <div>Max: {stats.max.toFixed(2)}</div>
                                            <div>Mean: {stats.mean.toFixed(2)}</div>
                                            {stats.outliers.length > 0 && (
                                                <div className="col-span-2 text-red-600">
                                                    Outliers: {stats.outliers.map(x => x.toFixed(2)).join(', ')}
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                );
                            })()}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );

    return (
        <div className="relative">
            <div className="p-4 bg-white border border-gray-300 rounded-lg mt-4">
                <div className="flex items-center justify-between mb-4">
                    <h3 className="font-semibold text-gray-700">Box and Whisker Plot</h3>
                    <button
                        onClick={handleOpenFullScreen}
                        className="p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow-lg transition-colors"
                        title="Open Full Screen Mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>

                {/* Controls */}
                <div className="grid grid-cols-2 gap-4 p-4 bg-gray-50 rounded-lg mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Title
                    </label>
                    <input
                        type="text"
                        value={plotData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Color
                    </label>
                    <input
                        type="color"
                        value={plotData.color}
                        onChange={(e) => handleInputChange('color', e.target.value)}
                        className="w-full h-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                
                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showOutliers}
                                onChange={(e) => handleInputChange('showOutliers', e.target.checked)}
                                className="mr-2"
                            />
                            Show Outliers
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showMean}
                                onChange={(e) => handleInputChange('showMean', e.target.checked)}
                                className="mr-2"
                            />
                            Show Mean
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showMedian}
                                onChange={(e) => handleInputChange('showMedian', e.target.checked)}
                                className="mr-2"
                            />
                            Show Median
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showQuartiles}
                                onChange={(e) => handleInputChange('showQuartiles', e.target.checked)}
                                className="mr-2"
                            />
                            Show Quartiles
                        </label>
                    </div>
                </div>
            </div>

            {/* Dataset Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="flex justify-between items-center mb-4">
                    <h4 className="font-semibold text-blue-800">Datasets</h4>
                    <button
                        onClick={addDataset}
                        className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                    >
                        Add Dataset
                    </button>
                </div>
                
                <div className="space-y-4">
                    {plotData.dataSet.map((dataset, datasetIndex) => (
                        <div key={datasetIndex} className="border border-blue-200 rounded-lg p-4 bg-white">
                            <div className="flex justify-between items-center mb-3">
                                <input
                                    type="text"
                                    value={dataset.label}
                                    onChange={(e) => handleDatasetChange(datasetIndex, 'label', e.target.value)}
                                    className="font-medium text-blue-800 border border-blue-200 rounded px-2 py-1"
                                />
                                <button
                                    onClick={() => removeDataset(datasetIndex)}
                                    className="text-red-600 hover:text-red-800 text-sm"
                                >
                                    Remove
                                </button>
                            </div>
                            
                            <div className="flex items-center space-x-2 mb-2">
                                <span className="text-sm text-gray-600">Values:</span>
                                <button
                                    onClick={() => addValue(datasetIndex)}
                                    className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                                >
                                    Add Value
                                </button>
                            </div>
                            
                            <div className="flex flex-wrap gap-2">
                                {dataset.values.map((value, valueIndex) => (
                                    <div key={valueIndex} className="flex items-center space-x-1">
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => updateValue(datasetIndex, valueIndex, e.target.value)}
                                            className="w-16 px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <button
                                            onClick={() => removeValue(datasetIndex, valueIndex)}
                                            className="text-red-500 hover:text-red-700 text-xs"
                                        >
                                            ×
                                        </button>
                                    </div>
                                ))}
                            </div>
                            
                            {/* Statistics Display */}
                            {(() => {
                                const stats = calculateStatistics(dataset.values);
                                if (!stats) return null;
                                
                                return (
                                    <div className="mt-3 p-2 bg-gray-50 rounded text-xs">
                                        <div className="grid grid-cols-2 gap-2">
                                            <div>Min: {stats.min.toFixed(2)}</div>
                                            <div>Q1: {stats.q1.toFixed(2)}</div>
                                            <div>Median: {stats.median.toFixed(2)}</div>
                                            <div>Q3: {stats.q3.toFixed(2)}</div>
                                            <div>Max: {stats.max.toFixed(2)}</div>
                                            <div>Mean: {stats.mean.toFixed(2)}</div>
                                            {stats.outliers.length > 0 && (
                                                <div className="col-span-2 text-red-600">
                                                    Outliers: {stats.outliers.map(x => x.toFixed(2)).join(', ')}
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                );
                            })()}
                        </div>
                    ))}
                </div>
            </div>

            {/* Plot Canvas */}
            <div className="border border-gray-300 rounded-lg overflow-hidden">
                <canvas
                    ref={canvasRef}
                    width={800}
                    height={500}
                    className="w-full h-auto"
                />
            </div>

            {/* Full Screen Modal */}
            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title="Box and Whisker Plot - Full Screen Mode"
                onToggleFullScreen={handleToggleFullScreen}
                isFullScreen={isFullScreen}
                parameterPanel={<ParameterPanel />}
            >
                <div className="h-full flex items-center justify-center">
                    <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                        <canvas
                            ref={fullScreenCanvasRef}
                            width={1000}
                            height={700}
                            className="w-full h-auto"
                        />
                    </div>
                </div>
            </FullScreenModal>
        </div>
    </div>
    );
};

export default BoxWhiskerPlot;
