import React, { useState, useEffect, useRef } from 'react';

const Histogram = ({ initialData, onChange, isSubmitted, isConfigMode = false }) => {
    const [histogramData, setHistogramData] = useState(initialData || {
        title: "Histogram",
        dataSet: [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10],
        binCount: 5,
        x_axis_label: "Values",
        y_axis_label: "Frequency",
        showStatistics: true,
        showGrid: true,
        showBins: true,
        showDataPoints: true,
        color: '#3B82F6',
        gridColor: '#e5e7eb',
        binWidth: 'auto'
    });

    // Ensure dataSet exists and handle both 'data' and 'dataSet' properties
    const getDataSet = () => {
        if (histogramData.dataSet) {
            return histogramData.dataSet;
        }
        if (histogramData.data) {
            return histogramData.data;
        }
        return [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]; // fallback
    };

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(histogramData);
        }
    }, [histogramData, onChange]);

    useEffect(() => {
        console.log('Histogram: useEffect triggered, drawing histogram');
        drawHistogram();
    }, [histogramData]);
    
    // Also draw on mount
    useEffect(() => {
        console.log('Histogram: Component mounted, drawing initial histogram');
        drawHistogram();
    }, []);

    // Calculate statistics for the dataset
    const calculateStatistics = (data) => {
        if (!data || data.length === 0) return null;

        const sorted = [...data].sort((a, b) => a - b);
        const n = data.length;
        const sum = data.reduce((acc, val) => acc + val, 0);
        const mean = sum / n;
        const median = n % 2 === 0 ? (sorted[n/2 - 1] + sorted[n/2]) / 2 : sorted[Math.floor(n/2)];
        
        // Mode calculation
        const frequency = {};
        data.forEach(val => {
            frequency[val] = (frequency[val] || 0) + 1;
        });
        const maxFreq = Math.max(...Object.values(frequency));
        const modes = Object.keys(frequency).filter(key => frequency[key] === maxFreq).map(Number);

        // Standard deviation
        const variance = data.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / n;
        const stdDev = Math.sqrt(variance);

        // Range
        const range = sorted[n - 1] - sorted[0];

        return {
            count: n,
            mean: mean,
            median: median,
            modes: modes,
            stdDev: stdDev,
            variance: variance,
            range: range,
            min: sorted[0],
            max: sorted[n - 1],
            q1: sorted[Math.floor(n * 0.25)],
            q3: sorted[Math.floor(n * 0.75)]
        };
    };

    // Create histogram bins
    const createBins = (data, binCount) => {
        if (!data || data.length === 0) return [];

        const min = Math.min(...data);
        const max = Math.max(...data);
        const range = max - min;
        const binWidth = range / binCount;

        const bins = [];
        for (let i = 0; i < binCount; i++) {
            const binStart = min + i * binWidth;
            const binEnd = min + (i + 1) * binWidth;
            const count = data.filter(val => val >= binStart && val < (i === binCount - 1 ? binEnd + 0.001 : binEnd)).length;
            
            bins.push({
                start: binStart,
                end: binEnd,
                count: count,
                center: (binStart + binEnd) / 2,
                label: `${binStart.toFixed(1)} - ${binEnd.toFixed(1)}`
            });
        }

        return bins;
    };

    const drawHistogram = () => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.log('Histogram: Canvas ref not found');
            return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('Histogram: Could not get 2D context');
            return;
        }
        
        const width = canvas.width;
        const height = canvas.height;
        
        console.log('Histogram: Drawing histogram with dimensions:', width, 'x', height);

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        const dataSet = getDataSet();
        const { binCount, showGrid, showBins, showDataPoints, color, gridColor, x_axis_label, y_axis_label } = histogramData;

        console.log('Histogram: Data set:', dataSet, 'Bin count:', binCount);

        if (!dataSet || dataSet.length === 0) {
            console.log('Histogram: No data to plot');
            return;
        }

        const bins = createBins(dataSet, binCount);
        console.log('Histogram: Created bins:', bins);
        
        const maxFrequency = Math.max(...bins.map(bin => bin.count));
        console.log('Histogram: Max frequency:', maxFrequency);

        // Calculate margins and plot area
        const margin = { top: 60, right: 80, bottom: 80, left: 80 };
        const plotWidth = width - margin.left - margin.right;
        const plotHeight = height - margin.top - margin.bottom;

        // Scale functions
        const xScale = (value) => margin.left + ((value - bins[0].start) / (bins[bins.length - 1].end - bins[0].start)) * plotWidth;
        const yScale = (value) => height - margin.bottom - (value / maxFrequency) * plotHeight;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = gridColor;
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);

            // Vertical grid lines at bin boundaries
            bins.forEach(bin => {
                const x = xScale(bin.start);
                ctx.beginPath();
                ctx.moveTo(x, margin.top);
                ctx.lineTo(x, height - margin.bottom);
                ctx.stroke();
            });

            // Horizontal grid lines
            const yTicks = 5;
            for (let i = 0; i <= yTicks; i++) {
                const y = margin.top + (i / yTicks) * plotHeight;
                ctx.beginPath();
                ctx.moveTo(margin.left, y);
                ctx.lineTo(width - margin.right, y);
                ctx.stroke();
            }

            ctx.setLineDash([]);
        }

        // Draw axes
        ctx.strokeStyle = '#374151';
        ctx.lineWidth = 2;

        // X-axis
        ctx.beginPath();
        ctx.moveTo(margin.left, height - margin.bottom);
        ctx.lineTo(width - margin.right, height - margin.bottom);
        ctx.stroke();

        // Y-axis
        ctx.beginPath();
        ctx.moveTo(margin.left, margin.top);
        ctx.lineTo(margin.left, height - margin.bottom);
        ctx.stroke();

        // Draw histogram bars
        ctx.fillStyle = color;
        bins.forEach(bin => {
            const barWidth = plotWidth / binCount;
            const barHeight = plotHeight * (bin.count / maxFrequency);
            const x = xScale(bin.start);
            const y = yScale(bin.count);

            // Draw bar
            ctx.fillRect(x, y, barWidth, height - margin.bottom - y);

            // Draw bar outline
            ctx.strokeStyle = '#1e40af';
            ctx.lineWidth = 1;
            ctx.strokeRect(x, y, barWidth, height - margin.bottom - y);
        });

        // Draw bin labels
        if (showBins) {
            ctx.fillStyle = '#374151';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            
            bins.forEach(bin => {
                const x = xScale(bin.start) + (plotWidth / binCount) / 2;
                const y = height - margin.bottom + 20;
                
                ctx.fillText(bin.label, x, y);
                
                // Frequency labels on bars
                if (bin.count > 0) {
                    const barY = yScale(bin.count);
                    ctx.fillText(bin.count.toString(), x, barY - 5);
                }
            });
        }

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

        // Y-axis ticks
        const yTicks = 5;
        for (let i = 0; i <= yTicks; i++) {
            const frequency = (maxFrequency * i) / yTicks;
            const y = yScale(frequency);
            const tickX = margin.left - 15;
            
            ctx.beginPath();
            ctx.moveTo(margin.left, y);
            ctx.lineTo(margin.left - 5, y);
            ctx.stroke();
            
            ctx.textAlign = 'right';
            ctx.fillText(frequency.toFixed(0), tickX, y + 4);
            ctx.textAlign = 'center';
        }

        // Draw data points if requested
        if (showDataPoints) {
            ctx.fillStyle = '#ef4444';
            ctx.strokeStyle = '#dc2626';
            ctx.lineWidth = 1;
            
            dataSet.forEach(value => {
                const x = xScale(value);
                const y = height - margin.bottom - 5;
                
                ctx.beginPath();
                ctx.arc(x, y, 3, 0, 2 * Math.PI);
                ctx.fill();
                ctx.stroke();
            });
        }

        // Draw title
        ctx.fillStyle = '#374151';
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(histogramData.title, width / 2, 30);
    };

    const handleInputChange = (field, value) => {
        setHistogramData(prev => ({
            ...prev,
            [field]: field === 'binCount' ? parseInt(value) || 5 : value
        }));
    };

    const handleDataSetChange = (value) => {
        const numbers = value.split(',').map(s => s.trim()).filter(s => s !== '').map(s => parseFloat(s)).filter(n => !isNaN(n));
        setHistogramData(prev => ({
            ...prev,
            dataSet: numbers
        }));
    };

    const generateRandomData = () => {
        const newData = [];
        const count = Math.floor(Math.random() * 20) + 10; // 10-30 data points
        const mean = Math.floor(Math.random() * 10) + 5; // 5-15 mean
        const stdDev = Math.floor(Math.random() * 3) + 1; // 1-4 standard deviation
        
        for (let i = 0; i < count; i++) {
            // Generate normally distributed data
            const u1 = Math.random();
            const u2 = Math.random();
            const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
            const value = mean + z * stdDev;
            newData.push(Math.max(0, Math.round(value * 10) / 10));
        }
        
        setHistogramData(prev => ({
            ...prev,
            dataSet: newData
        }));
    };

    const generateUniformData = () => {
        const newData = [];
        const count = Math.floor(Math.random() * 20) + 10;
        const min = Math.floor(Math.random() * 5);
        const max = min + Math.floor(Math.random() * 10) + 5;
        
        for (let i = 0; i < count; i++) {
            newData.push(Math.floor(Math.random() * (max - min + 1)) + min);
        }
        
        setHistogramData(prev => ({
            ...prev,
            dataSet: newData
        }));
    };

    const addDataPoint = () => {
        const newValue = Math.floor(Math.random() * 20) + 1;
        setHistogramData(prev => ({
            ...prev,
            dataSet: [...getDataSet(), newValue]
        }));
    };

    const clearData = () => {
        setHistogramData(prev => ({
            ...prev,
            dataSet: [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10] // Reset to default data
        }));
    };

    const dataSet = getDataSet();
    const stats = calculateStatistics(dataSet);
    const bins = createBins(dataSet, histogramData.binCount);

    // NEW LAYOUT: Left pane for controls, right pane for canvas
    return (
        <div className="h-full flex">
            {/* Left Pane - Scrollable Controls */}
            <div className="w-80 p-4 border-r border-gray-200 overflow-y-auto bg-gray-50">
                <div className="space-y-4">
                    <h3 className="text-lg font-semibold text-gray-800">Histogram Controls</h3>
                    
                    {/* Display Settings */}
                    <div className="space-y-3">
                        <h4 className="font-medium text-gray-700">Display Settings</h4>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                            <input
                                type="text"
                                value={histogramData.title}
                                onChange={(e) => handleInputChange('title', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Number of Bins:</label>
                            <input
                                type="number"
                                min="2"
                                max="20"
                                value={histogramData.binCount}
                                onChange={(e) => handleInputChange('binCount', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">X-Axis Label:</label>
                            <input
                                type="text"
                                value={histogramData.x_axis_label}
                                onChange={(e) => handleInputChange('x_axis_label', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Y-Axis Label:</label>
                            <input
                                type="text"
                                value={histogramData.y_axis_label}
                                onChange={(e) => handleInputChange('y_axis_label', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Bar Color:</label>
                            <input
                                type="color"
                                value={histogramData.color}
                                onChange={(e) => handleInputChange('color', e.target.value)}
                                className="w-full h-10 border border-gray-300 rounded-md"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Grid Color:</label>
                            <input
                                type="color"
                                value={histogramData.gridColor}
                                onChange={(e) => handleInputChange('gridColor', e.target.value)}
                                className="w-full h-10 border border-gray-300 rounded-md"
                            />
                        </div>
                    </div>

                    {/* Display Options */}
                    <div className="space-y-2">
                        <h4 className="font-medium text-gray-700">Display Options</h4>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={histogramData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Grid</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={histogramData.showBins}
                                onChange={(e) => handleInputChange('showBins', e.target.checked)}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Bin Labels</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={histogramData.showDataPoints}
                                onChange={(e) => handleInputChange('showDataPoints', e.target.checked)}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Data Points</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={histogramData.showStatistics}
                                onChange={(e) => handleInputChange('showStatistics', e.target.checked)}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Statistics</span>
                        </label>
                    </div>

                    {/* Data Management */}
                    <div className="space-y-3">
                        <h4 className="font-medium text-gray-700">Data Management</h4>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Data Set:</label>
                            <textarea
                                value={getDataSet().join(', ')}
                                onChange={(e) => handleDataSetChange(e.target.value)}
                                rows="3"
                                className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                                placeholder="Enter numbers separated by commas..."
                            />
                        </div>
                        <div className="flex space-x-2">
                            <button
                                onClick={generateRandomData}
                                className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                            >
                                Random Data
                            </button>
                            <button
                                onClick={generateUniformData}
                                className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                            >
                                Uniform Data
                            </button>
                            <button
                                onClick={addDataPoint}
                                className="px-2 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-xs"
                            >
                                Add Point
                            </button>
                            <button
                                onClick={clearData}
                                className="px-2 py-1 bg-red-600 hover:bg-red-700 text-white rounded text-xs"
                            >
                                Clear Data
                            </button>
                        </div>
                    </div>

                    {/* Statistics Display */}
                    {histogramData.showStatistics && stats && (
                        <div className="p-3 bg-white rounded text-sm border">
                            <h5 className="font-medium text-gray-800 mb-2">Statistical Summary:</h5>
                            <div className="grid grid-cols-2 gap-2 text-xs">
                                <div><strong>Count:</strong> {stats.count}</div>
                                <div><strong>Mean:</strong> {stats.mean.toFixed(2)}</div>
                                <div><strong>Median:</strong> {stats.median.toFixed(2)}</div>
                                <div><strong>Mode(s):</strong> {stats.modes.join(', ')}</div>
                                <div><strong>Std Dev:</strong> {stats.stdDev.toFixed(2)}</div>
                                <div><strong>Range:</strong> {stats.range.toFixed(2)}</div>
                                <div><strong>Min:</strong> {stats.min.toFixed(2)}</div>
                                <div><strong>Max:</strong> {stats.max.toFixed(2)}</div>
                            </div>
                        </div>
                    )}
                </div>
            </div>

            {/* Right Pane - Canvas Always Visible */}
            <div className="flex-1 p-4 flex items-center justify-center bg-white">
                <div className="w-full max-w-4xl">
                    <div className="text-center mb-4">
                        <h2 className="text-xl font-bold text-gray-800">{histogramData.title}</h2>
                        <p className="text-sm text-gray-600">Data points: {getDataSet().length} | Bins: {histogramData.binCount}</p>
                    </div>
                    
                    <div className="border border-gray-300 rounded-lg overflow-hidden bg-white shadow-lg">
                        <canvas
                            ref={canvasRef}
                            width={800}
                            height={500}
                            style={{ 
                                width: '100%', 
                                height: 'auto',
                                maxWidth: '800px',
                                display: 'block'
                            }}
                        />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Histogram;
