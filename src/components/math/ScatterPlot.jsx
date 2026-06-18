import React, { useState, useEffect, useRef } from 'react';

const ScatterPlot = ({ initialData, onChange, isSubmitted }) => {
    const [plotData, setPlotData] = useState(initialData || {
        title: "Scatter Plot",
        x_axis_label: "X Variable",
        y_axis_label: "Y Variable",
        showTrendLine: true,
        showCorrelation: true,
        showGrid: true,
        showPoints: true,
        showLabels: true,
        pointSize: 6,
        lineColor: '#3B82F6',
        pointColor: '#3B82F6',
        gridColor: '#e5e7eb',
        points: [
            { x: 1, y: 2, label: "Point 1" },
            { x: 2, y: 4, label: "Point 2" },
            { x: 3, y: 3, label: "Point 3" },
            { x: 4, y: 6, label: "Point 4" },
            { x: 5, y: 5, label: "Point 5" }
        ]
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(plotData);
        }
    }, [plotData, onChange]);

    useEffect(() => {
        drawPlot();
    }, [plotData]);

    // Calculate correlation coefficient
    const calculateCorrelation = (points) => {
        if (points.length < 2) return null;

        const n = points.length;
        const sumX = points.reduce((sum, p) => sum + p.x, 0);
        const sumY = points.reduce((sum, p) => sum + p.y, 0);
        const sumXY = points.reduce((sum, p) => sum + p.x * p.y, 0);
        const sumX2 = points.reduce((sum, p) => sum + p.x * p.x, 0);
        const sumY2 = points.reduce((sum, p) => sum + p.y * p.y, 0);

        const numerator = n * sumXY - sumX * sumY;
        const denominator = Math.sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));

        if (denominator === 0) return null;
        return numerator / denominator;
    };

    // Calculate linear regression (trend line)
    const calculateTrendLine = (points) => {
        if (points.length < 2) return null;

        const n = points.length;
        const sumX = points.reduce((sum, p) => sum + p.x, 0);
        const sumY = points.reduce((sum, p) => sum + p.y, 0);
        const sumXY = points.reduce((sum, p) => sum + p.x * p.y, 0);
        const sumX2 = points.reduce((sum, p) => sum + p.x * p.x, 0);

        const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;

        return { slope, intercept };
    };

    const drawPlot = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        const { points, showGrid, showPoints, showTrendLine, showCorrelation, showLabels, pointSize, lineColor, pointColor, gridColor, x_axis_label, y_axis_label } = plotData;

        if (!points || points.length === 0) return;

        // Find data ranges
        const xValues = points.map(p => p.x);
        const yValues = points.map(p => p.y);
        const xMin = Math.min(...xValues);
        const xMax = Math.max(...xValues);
        const yMin = Math.min(...yValues);
        const yMax = Math.max(...yValues);

        // Add padding
        const xRange = xMax - xMin;
        const yRange = yMax - yMin;
        const xPadding = xRange * 0.1;
        const yPadding = yRange * 0.1;

        const plotXMin = xMin - xPadding;
        const plotXMax = xMax + xPadding;
        const plotYMin = yMin - yPadding;
        const plotYMax = yMax + yPadding;

        // Calculate scale factors
        const margin = 80;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;

        const scaleX = (x) => margin + ((x - plotXMin) / (plotXMax - plotXMin)) * plotWidth;
        const scaleY = (y) => height - margin - ((y - plotYMin) / (plotYMax - plotYMin)) * plotHeight;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = gridColor;
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);

            // Vertical grid lines
            const xTicks = 10;
            for (let i = 0; i <= xTicks; i++) {
                const x = plotXMin + (i / xTicks) * (plotXMax - plotXMin);
                const canvasX = scaleX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, margin);
                ctx.lineTo(canvasX, height - margin);
                ctx.stroke();
            }

            // Horizontal grid lines
            const yTicks = 10;
            for (let i = 0; i <= yTicks; i++) {
                const y = plotYMin + (i / yTicks) * (plotYMax - plotYMin);
                const canvasY = scaleY(y);
                ctx.beginPath();
                ctx.moveTo(margin, canvasY);
                ctx.lineTo(width - margin, canvasY);
                ctx.stroke();
            }

            ctx.setLineDash([]);
        }

        // Draw axes
        ctx.strokeStyle = '#374151';
        ctx.lineWidth = 2;

        // X-axis
        ctx.beginPath();
        ctx.moveTo(margin, height - margin);
        ctx.lineTo(width - margin, height - margin);
        ctx.stroke();

        // Y-axis
        ctx.beginPath();
        ctx.moveTo(margin, margin);
        ctx.lineTo(margin, height - margin);
        ctx.stroke();

        // Draw axis labels
        ctx.fillStyle = '#374151';
        ctx.font = '14px Arial';
        ctx.textAlign = 'center';

        // X-axis label
        ctx.fillText(x_axis_label, width / 2, height - 20);

        // Y-axis label (rotated)
        ctx.save();
        ctx.translate(20, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText(y_axis_label, 0, 0);
        ctx.restore();

        // Draw axis ticks and values
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';

        // X-axis ticks
        const xTicks = 5;
        for (let i = 0; i <= xTicks; i++) {
            const x = plotXMin + (i / xTicks) * (plotXMax - plotXMin);
            const canvasX = scaleX(x);
            const tickY = height - margin + 15;
            
            ctx.beginPath();
            ctx.moveTo(canvasX, height - margin);
            ctx.lineTo(canvasX, height - margin + 5);
            ctx.stroke();
            
            ctx.fillText(x.toFixed(1), canvasX, tickY);
        }

        // Y-axis ticks
        const yTicks = 5;
        for (let i = 0; i <= yTicks; i++) {
            const y = plotYMin + (i / yTicks) * (plotYMax - plotYMin);
            const canvasY = scaleY(y);
            const tickX = margin - 15;
            
            ctx.beginPath();
            ctx.moveTo(margin, canvasY);
            ctx.lineTo(margin - 5, canvasY);
            ctx.stroke();
            
            ctx.textAlign = 'right';
            ctx.fillText(y.toFixed(1), tickX, canvasY + 4);
            ctx.textAlign = 'center';
        }

        // Draw trend line
        if (showTrendLine && points.length >= 2) {
            const trendLine = calculateTrendLine(points);
            if (trendLine) {
                const { slope, intercept } = trendLine;
                
                // Calculate line endpoints
                const x1 = plotXMin;
                const y1 = slope * x1 + intercept;
                const x2 = plotXMax;
                const y2 = slope * x2 + intercept;

                ctx.strokeStyle = lineColor;
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(scaleX(x1), scaleY(y1));
                ctx.lineTo(scaleX(x2), scaleY(y2));
                ctx.stroke();
                ctx.setLineDash([]);

                // Draw trend line equation
                ctx.fillStyle = lineColor;
                ctx.font = '12px Arial';
                ctx.textAlign = 'left';
                const equation = `y = ${slope.toFixed(2)}x + ${intercept.toFixed(2)}`;
                ctx.fillText(equation, margin + 10, margin + 20);
            }
        }

        // Draw data points
        if (showPoints) {
            ctx.fillStyle = pointColor;
            points.forEach(point => {
                const canvasX = scaleX(point.x);
                const canvasY = scaleY(point.y);

                // Draw point
                ctx.beginPath();
                ctx.arc(canvasX, canvasY, pointSize, 0, 2 * Math.PI);
                ctx.fill();

                // Draw point label
                if (showLabels && point.label) {
                    ctx.fillStyle = '#374151';
                    ctx.font = '10px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(point.label, canvasX, canvasY - pointSize - 5);
                    ctx.fillStyle = pointColor;
                }
            });
        }

        // Draw correlation information
        if (showCorrelation && points.length >= 2) {
            const correlation = calculateCorrelation(points);
            if (correlation !== null) {
                ctx.fillStyle = '#374151';
                ctx.font = '12px Arial';
                ctx.textAlign = 'right';
                
                const correlationText = `Correlation: ${correlation.toFixed(3)}`;
                const strengthText = getCorrelationStrength(correlation);
                
                ctx.fillText(correlationText, width - margin - 10, margin + 20);
                ctx.fillText(strengthText, width - margin - 10, margin + 35);
            }
        }

        // Draw title
        ctx.fillStyle = '#374151';
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(plotData.title, width / 2, 30);
    };

    const getCorrelationStrength = (correlation) => {
        const absCorr = Math.abs(correlation);
        if (absCorr >= 0.9) return 'Very Strong';
        if (absCorr >= 0.7) return 'Strong';
        if (absCorr >= 0.5) return 'Moderate';
        if (absCorr >= 0.3) return 'Weak';
        return 'Very Weak';
    };

    const handleInputChange = (field, value) => {
        setPlotData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    const handlePointChange = (index, field, value) => {
        setPlotData(prev => ({
            ...prev,
            points: prev.points.map((point, i) => 
                i === index ? { ...point, [field]: parseFloat(value) || 0 } : point
            )
        }));
    };

    const handlePointLabelChange = (index, value) => {
        setPlotData(prev => ({
            ...prev,
            points: prev.points.map((point, i) => 
                i === index ? { ...point, label: value } : point
            )
        }));
    };

    const addPoint = () => {
        setPlotData(prev => ({
            ...prev,
            points: [...prev.points, { 
                x: Math.floor(Math.random() * 10) + 1, 
                y: Math.floor(Math.random() * 10) + 1, 
                label: `Point ${prev.points.length + 1}` 
            }]
        }));
    };

    const removePoint = (index) => {
        setPlotData(prev => ({
            ...prev,
            points: prev.points.filter((_, i) => i !== index)
        }));
    };

    const generateRandomData = () => {
        const newPoints = [];
        for (let i = 1; i <= 10; i++) {
            newPoints.push({
                x: i,
                y: Math.floor(Math.random() * 10) + 1,
                label: `Point ${i}`
            });
        }
        setPlotData(prev => ({
            ...prev,
            points: newPoints
        }));
    };

    const generateLinearData = () => {
        const newPoints = [];
        const slope = 2;
        const intercept = 1;
        for (let i = 1; i <= 10; i++) {
            const y = slope * i + intercept + (Math.random() - 0.5) * 2;
            newPoints.push({
                x: i,
                y: Math.round(y * 10) / 10,
                label: `Point ${i}`
            });
        }
        setPlotData(prev => ({
            ...prev,
            points: newPoints
        }));
    };

    return (
        <div className="space-y-4">
            {/* Controls */}
            <div className="grid grid-cols-2 gap-4 p-4 bg-gray-50 rounded-lg">
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
                        X-Axis Label
                    </label>
                    <input
                        type="text"
                        value={plotData.x_axis_label}
                        onChange={(e) => handleInputChange('x_axis_label', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Y-Axis Label
                    </label>
                    <input
                        type="text"
                        value={plotData.y_axis_label}
                        onChange={(e) => handleInputChange('y_axis_label', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Point Size
                    </label>
                    <input
                        type="range"
                        min="3"
                        max="12"
                        value={plotData.pointSize}
                        onChange={(e) => handleInputChange('pointSize', parseInt(e.target.value))}
                        className="w-full"
                    />
                    <span className="text-xs text-gray-500">{plotData.pointSize}px</span>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Point Color
                    </label>
                    <input
                        type="color"
                        value={plotData.pointColor}
                        onChange={(e) => handleInputChange('pointColor', e.target.value)}
                        className="w-full h-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Line Color
                    </label>
                    <input
                        type="color"
                        value={plotData.lineColor}
                        onChange={(e) => handleInputChange('lineColor', e.target.value)}
                        className="w-full h-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                
                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showPoints}
                                onChange={(e) => handleInputChange('showPoints', e.target.checked)}
                                className="mr-2"
                            />
                            Show Points
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showTrendLine}
                                onChange={(e) => handleInputChange('showTrendLine', e.target.checked)}
                                className="mr-2"
                            />
                            Show Trend Line
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showCorrelation}
                                onChange={(e) => handleInputChange('showCorrelation', e.target.checked)}
                                className="mr-2"
                            />
                            Show Correlation
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={plotData.showLabels}
                                onChange={(e) => handleInputChange('showLabels', e.target.checked)}
                                className="mr-2"
                            />
                            Show Labels
                        </label>
                    </div>
                </div>
            </div>

            {/* Data Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="flex justify-between items-center mb-4">
                    <h4 className="font-semibold text-blue-800">Data Points</h4>
                    <div className="flex space-x-2">
                        <button
                            onClick={generateRandomData}
                            className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                        >
                            Random Data
                        </button>
                        <button
                            onClick={generateLinearData}
                            className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                        >
                            Linear Data
                        </button>
                        <button
                            onClick={addPoint}
                            className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                        >
                            Add Point
                        </button>
                    </div>
                </div>
                
                <div className="space-y-3">
                    {plotData.points.map((point, index) => (
                        <div key={index} className="flex items-center space-x-3 p-3 bg-white rounded border">
                            <div className="flex items-center space-x-2">
                                <span className="text-sm text-gray-600">X:</span>
                                <input
                                    type="number"
                                    step="0.1"
                                    value={point.x}
                                    onChange={(e) => handlePointChange(index, 'x', e.target.value)}
                                    className="w-20 px-2 py-1 border border-gray-300 rounded text-sm"
                                />
                            </div>
                            
                            <div className="flex items-center space-x-2">
                                <span className="text-sm text-gray-600">Y:</span>
                                <input
                                    type="number"
                                    step="0.1"
                                    value={point.y}
                                    onChange={(e) => handlePointChange(index, 'y', e.target.value)}
                                    className="w-20 px-2 py-1 border border-gray-300 rounded text-sm"
                                />
                            </div>
                            
                            <div className="flex items-center space-x-2">
                                <span className="text-sm text-gray-600">Label:</span>
                                <input
                                    type="text"
                                    value={point.label}
                                    onChange={(e) => handlePointLabelChange(index, e.target.value)}
                                    className="w-24 px-2 py-1 border border-gray-300 rounded text-sm"
                                />
                            </div>
                            
                            <button
                                onClick={() => removePoint(index)}
                                className="text-red-600 hover:text-red-800 text-sm"
                            >
                                Remove
                            </button>
                        </div>
                    ))}
                </div>
                
                {/* Statistics Display */}
                {(() => {
                    if (plotData.points.length < 2) return null;
                    
                    const correlation = calculateCorrelation(plotData.points);
                    const trendLine = calculateTrendLine(plotData.points);
                    
                    return (
                        <div className="mt-4 p-3 bg-gray-50 rounded text-sm">
                            <div className="grid grid-cols-2 gap-4">
                                <div>
                                    <strong>Correlation:</strong> {correlation ? correlation.toFixed(3) : 'N/A'}
                                    {correlation && (
                                        <div className="text-xs text-gray-600">
                                            {getCorrelationStrength(correlation)}
                                        </div>
                                    )}
                                </div>
                                {trendLine && (
                                    <div>
                                        <strong>Trend Line:</strong> y = {trendLine.slope.toFixed(2)}x + {trendLine.intercept.toFixed(2)}
                                    </div>
                                )}
                                <div>
                                    <strong>Data Points:</strong> {plotData.points.length}
                                </div>
                                <div>
                                    <strong>X Range:</strong> {Math.min(...plotData.points.map(p => p.x)).toFixed(1)} to {Math.max(...plotData.points.map(p => p.x)).toFixed(1)}
                                </div>
                                <div>
                                    <strong>Y Range:</strong> {Math.min(...plotData.points.map(p => p.y)).toFixed(1)} to {Math.max(...plotData.points.map(p => p.y)).toFixed(1)}
                                </div>
                            </div>
                        </div>
                    );
                })()}
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
        </div>
    );
};

export default ScatterPlot;
