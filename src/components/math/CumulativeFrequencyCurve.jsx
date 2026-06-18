import React, { useState, useEffect, useRef } from 'react';

const CumulativeFrequencyCurve = ({ initialData, onChange, isSubmitted }) => {
    const [cumulativeData, setCumulativeData] = useState(initialData || {
        title: "Cumulative Frequency Curve",
        dataSet: [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        showHistogram: false,
        showPolygon: true,
        showCumulative: true,
        showPoints: true,
        showGrid: true,
        showStatistics: true,
        showPercentiles: true,
        showQuartiles: true,
        binCount: 8,
        xAxisLabel: "Values",
        yAxisLabel: "Cumulative Frequency",
        backgroundColor: '#ffffff',
        gridColor: '#e5e7eb',
        axisColor: '#374151',
        histogramColor: '#3B82F6',
        polygonColor: '#10B981',
        cumulativeColor: '#EF4444',
        pointColor: '#F59E0B'
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(cumulativeData);
        }
    }, [cumulativeData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawCumulativeFrequencyCurve();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [cumulativeData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawCumulativeFrequencyCurve();
    }, []);

    const createBins = () => {
        const sortedData = [...cumulativeData.dataSet].sort((a, b) => a - b);
        const min = sortedData[0];
        const max = sortedData[sortedData.length - 1];
        const range = max - min;
        const binWidth = range / cumulativeData.binCount;

        const bins = [];
        for (let i = 0; i < cumulativeData.binCount; i++) {
            const binStart = min + i * binWidth;
            const binEnd = min + (i + 1) * binWidth;
            const binCenter = (binStart + binEnd) / 2;
            const frequency = sortedData.filter(value => 
                value >= binStart && (i === cumulativeData.binCount - 1 ? value <= binEnd : value < binEnd)
            ).length;

            bins.push({
                start: binStart,
                end: binEnd,
                center: binCenter,
                frequency: frequency,
                cumulative: 0
            });
        }

        // Calculate cumulative frequencies
        let cumulative = 0;
        bins.forEach(bin => {
            cumulative += bin.frequency;
            bin.cumulative = cumulative;
        });

        return bins;
    };

    const calculateStatistics = () => {
        const sortedData = [...cumulativeData.dataSet].sort((a, b) => a - b);
        const n = sortedData.length;
        
        if (n === 0) return null;

        const sum = sortedData.reduce((acc, val) => acc + val, 0);
        const mean = sum / n;
        const median = n % 2 === 0 
            ? (sortedData[n/2 - 1] + sortedData[n/2]) / 2 
            : sortedData[Math.floor(n/2)];
        
        // Calculate quartiles
        const q1Index = Math.floor(n * 0.25);
        const q3Index = Math.floor(n * 0.75);
        const q1 = sortedData[q1Index];
        const q3 = sortedData[q3Index];
        const iqr = q3 - q1;
        
        // Calculate mode
        const frequency = {};
        sortedData.forEach(val => {
            frequency[val] = (frequency[val] || 0) + 1;
        });
        const maxFreq = Math.max(...Object.values(frequency));
        const mode = Object.keys(frequency).filter(key => frequency[key] === maxFreq).map(Number);
        
        // Calculate variance and standard deviation
        const variance = sortedData.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / n;
        const stdDev = Math.sqrt(variance);
        
        const range = sortedData[n - 1] - sortedData[0];
        const min = sortedData[0];
        const max = sortedData[n - 1];

        return { mean, median, mode, range, min, max, n, variance, stdDev, q1, q3, iqr };
    };

    const calculatePercentiles = () => {
        const sortedData = [...cumulativeData.dataSet].sort((a, b) => a - b);
        const n = sortedData.length;
        
        if (n === 0) return null;

        const percentiles = [10, 25, 50, 75, 90, 95, 99];
        return percentiles.map(p => {
            const index = Math.floor(n * p / 100);
            return { percentile: p, value: sortedData[Math.min(index, n - 1)] };
        });
    };

    const drawCumulativeFrequencyCurve = () => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.log('CumulativeFrequencyCurve: Canvas not found');
            return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('CumulativeFrequencyCurve: Canvas context not available');
            return;
        }

        const width = canvas.width;
        const height = canvas.height;

        console.log('CumulativeFrequencyCurve: Drawing with dimensions:', { width, height, dataSet: cumulativeData.dataSet });

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = cumulativeData.backgroundColor || '#ffffff';
        ctx.fillRect(0, 0, width, height);

        // Test drawing - draw a simple rectangle to verify canvas is working
        ctx.fillStyle = '#00ff00';
        ctx.fillRect(10, 10, 50, 50);

        const bins = createBins();
        const stats = calculateStatistics();
        const percentiles = calculatePercentiles();

        if (!stats || bins.length === 0) return;

        const margin = 60;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;

        // Find max frequency and cumulative for scaling
        const maxFreq = Math.max(...bins.map(bin => bin.frequency));
        const maxCumulative = Math.max(...bins.map(bin => bin.cumulative));

        // Scale factors
        const xScale = plotWidth / (bins.length + 1);
        const yScale = plotHeight / (maxFreq * 1.2);
        const yCumulativeScale = plotHeight / (maxCumulative * 1.2);

        const toCanvasX = (index) => margin + (index + 0.5) * xScale;
        const toCanvasY = (freq) => height - margin - freq * yScale;
        const toCanvasYCumulative = (cum) => height - margin - cum * yCumulativeScale;

        // Draw grid
        if (cumulativeData.showGrid) {
            ctx.strokeStyle = cumulativeData.gridColor;
            ctx.lineWidth = 1;
            
            // Vertical grid lines
            for (let i = 0; i <= bins.length; i++) {
                const x = margin + i * xScale;
                ctx.beginPath();
                ctx.moveTo(x, margin);
                ctx.lineTo(x, height - margin);
                ctx.stroke();
            }
            
            // Horizontal grid lines for frequency
            for (let i = 0; i <= maxFreq; i += Math.ceil(maxFreq / 10)) {
                const y = height - margin - i * yScale;
                ctx.beginPath();
                ctx.moveTo(margin, y);
                ctx.lineTo(width - margin, y);
                ctx.stroke();
            }
            
            // Horizontal grid lines for cumulative
            for (let i = 0; i <= maxCumulative; i += Math.ceil(maxCumulative / 10)) {
                const y = height - margin - i * yCumulativeScale;
                ctx.beginPath();
                ctx.moveTo(margin, y);
                ctx.lineTo(width - margin, y);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = cumulativeData.axisColor;
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

        // Draw histogram bars
        if (cumulativeData.showHistogram) {
            ctx.fillStyle = cumulativeData.histogramColor + '80';
            ctx.strokeStyle = cumulativeData.histogramColor;
            ctx.lineWidth = 2;
            
            bins.forEach((bin, index) => {
                const x = toCanvasX(index);
                const y = toCanvasY(bin.frequency);
                const barWidth = xScale * 0.8;
                const barHeight = bin.frequency * yScale;
                
                ctx.fillRect(x - barWidth/2, y, barWidth, barHeight);
                ctx.strokeRect(x - barWidth/2, y, barWidth, barHeight);
            });
        }

        // Draw frequency polygon
        if (cumulativeData.showPolygon) {
            ctx.strokeStyle = cumulativeData.polygonColor;
            ctx.lineWidth = 3;
            ctx.beginPath();
            
            // Start at first bin center
            const firstX = toCanvasX(0);
            const firstY = toCanvasY(bins[0].frequency);
            ctx.moveTo(firstX, firstY);
            
            // Connect to each bin center
            for (let i = 1; i < bins.length; i++) {
                const x = toCanvasX(i);
                const y = toCanvasY(bins[i].frequency);
                ctx.lineTo(x, y);
            }
            
            ctx.stroke();
        }

        // Draw cumulative frequency curve
        if (cumulativeData.showCumulative) {
            ctx.strokeStyle = cumulativeData.cumulativeColor;
            ctx.lineWidth = 3;
            ctx.beginPath();
            
            // Start at first bin center
            const firstX = toCanvasX(0);
            const firstY = toCanvasYCumulative(bins[0].cumulative);
            ctx.moveTo(firstX, firstY);
            
            // Connect to each bin center
            for (let i = 1; i < bins.length; i++) {
                const x = toCanvasX(i);
                const y = toCanvasYCumulative(bins[i].cumulative);
                ctx.lineTo(x, y);
            }
            
            ctx.stroke();
        }

        // Draw points
        if (cumulativeData.showPoints) {
            // Frequency points
            ctx.fillStyle = cumulativeData.polygonColor;
            bins.forEach((bin, index) => {
                const x = toCanvasX(index);
                const y = toCanvasY(bin.frequency);
                
                ctx.beginPath();
                ctx.arc(x, y, 4, 0, 2 * Math.PI);
                ctx.fill();
            });

            // Cumulative points
            ctx.fillStyle = cumulativeData.cumulativeColor;
            bins.forEach((bin, index) => {
                const x = toCanvasX(index);
                const y = toCanvasYCumulative(bin.cumulative);
                
                ctx.beginPath();
                ctx.arc(x, y, 4, 0, 2 * Math.PI);
                ctx.fill();
            });
        }

        // Draw bin labels
        ctx.fillStyle = cumulativeData.axisColor;
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        
        bins.forEach((bin, index) => {
            const x = toCanvasX(index);
            const y = height - margin + 20;
            
            ctx.fillText(`${bin.start.toFixed(1)}-${bin.end.toFixed(1)}`, x, y);
            ctx.fillText(`(${bin.frequency})`, x, y + 15);
        });

        // Draw frequency labels
        ctx.textAlign = 'right';
        for (let i = 0; i <= maxFreq; i += Math.ceil(maxFreq / 5)) {
            const y = height - margin - i * yScale;
            ctx.fillText(i.toString(), margin - 10, y + 4);
        }

        // Draw cumulative labels
        ctx.textAlign = 'right';
        ctx.fillStyle = cumulativeData.cumulativeColor;
        for (let i = 0; i <= maxCumulative; i += Math.ceil(maxCumulative / 5)) {
            const y = height - margin - i * yCumulativeScale;
            ctx.fillText(i.toString(), margin - 30, y + 4);
        }

        // Draw title and labels
        ctx.fillStyle = cumulativeData.axisColor;
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(cumulativeData.title, width / 2, 25);
        
        ctx.font = '14px Arial';
        ctx.fillText(cumulativeData.xAxisLabel, width / 2, height - 10);
        
        ctx.save();
        ctx.translate(20, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText(cumulativeData.yAxisLabel, 0, 0);
        ctx.restore();

        // Draw legend
        let legendY = margin + 20;
        ctx.font = '12px Arial';
        ctx.textAlign = 'left';
        
        if (cumulativeData.showPolygon) {
            ctx.fillStyle = cumulativeData.polygonColor;
            ctx.fillRect(width - margin, legendY, 15, 3);
            ctx.fillStyle = cumulativeData.axisColor;
            ctx.fillText('Frequency Polygon', width - margin + 20, legendY + 8);
            legendY += 20;
        }
        
        if (cumulativeData.showCumulative) {
            ctx.fillStyle = cumulativeData.cumulativeColor;
            ctx.fillRect(width - margin, legendY, 15, 3);
            ctx.fillStyle = cumulativeData.axisColor;
            ctx.fillText('Cumulative Frequency', width - margin + 20, legendY + 8);
            legendY += 20;
        }

        // Draw statistics if enabled
        if (cumulativeData.showStatistics) {
            ctx.fillStyle = cumulativeData.axisColor;
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('Statistics:', margin, legendY + 20);
            
            ctx.font = '12px Arial';
            let yOffset = legendY + 40;
            ctx.fillText(`Count: ${stats.n}`, margin, yOffset);
            ctx.fillText(`Mean: ${stats.mean.toFixed(2)}`, margin + 100, yOffset);
            yOffset += 15;
            ctx.fillText(`Median: ${stats.median}`, margin, yOffset);
            ctx.fillText(`Mode: ${stats.mode.join(', ')}`, margin + 100, yOffset);
            yOffset += 15;
            ctx.fillText(`Std Dev: ${stats.stdDev.toFixed(2)}`, margin, yOffset);
            ctx.fillText(`Range: ${stats.range}`, margin + 100, yOffset);
        }

        // Draw quartiles if enabled
        if (cumulativeData.showQuartiles) {
            let yOffset = legendY + 100;
            ctx.font = 'bold 12px Arial';
            ctx.fillText('Quartiles:', margin, yOffset);
            
            ctx.font = '12px Arial';
            yOffset += 15;
            ctx.fillText(`Q1: ${stats.q1}`, margin, yOffset);
            ctx.fillText(`Q3: ${stats.q3}`, margin + 60, yOffset);
            ctx.fillText(`IQR: ${stats.iqr}`, margin + 120, yOffset);
        }

        // Draw percentiles if enabled
        if (cumulativeData.showPercentiles) {
            let yOffset = legendY + 140;
            ctx.font = 'bold 12px Arial';
            ctx.fillText('Percentiles:', margin, yOffset);
            
            ctx.font = '10px Arial';
            percentiles.forEach((p, index) => {
                if (index % 2 === 0) {
                    yOffset += 12;
                    ctx.fillText(`${p.percentile}%: ${p.value}`, margin, yOffset);
                } else {
                    ctx.fillText(`${p.percentile}%: ${p.value}`, margin + 80, yOffset);
                }
            });
        }
    };

    const handleInputChange = (field, value) => {
        setCumulativeData(prev => ({
            ...prev,
            [field]: field === 'binCount' ? parseInt(value) || 8 : value
        }));
    };

    const handleDataSetChange = (value) => {
        const numbers = value.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
        setCumulativeData(prev => ({
            ...prev,
            dataSet: numbers
        }));
    };

    const generateRandomData = () => {
        const count = Math.floor(Math.random() * 30) + 20;
        const data = Array.from({ length: count }, () => Math.floor(Math.random() * 50) + 1);
        setCumulativeData(prev => ({
            ...prev,
            dataSet: data
        }));
    };

    const addDataPoint = () => {
        const newValue = Math.floor(Math.random() * 50) + 1;
        setCumulativeData(prev => ({
            ...prev,
            dataSet: [...prev.dataSet, newValue]
        }));
    };

    const clearData = () => {
        setCumulativeData(prev => ({
            ...prev,
            dataSet: []
        }));
    };

    const stats = calculateStatistics();
    const bins = createBins();

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
                        value={cumulativeData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Number of Bins
                    </label>
                    <input
                        type="number"
                        min="2"
                        max="20"
                        value={cumulativeData.binCount}
                        onChange={(e) => handleInputChange('binCount', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        X-Axis Label
                    </label>
                    <input
                        type="text"
                        value={cumulativeData.xAxisLabel}
                        onChange={(e) => handleInputChange('xAxisLabel', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Y-Axis Label
                    </label>
                    <input
                        type="text"
                        value={cumulativeData.yAxisLabel}
                        onChange={(e) => handleInputChange('yAxisLabel', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div className="col-span-2">
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Data Set (comma-separated numbers)
                    </label>
                    <input
                        type="text"
                        value={cumulativeData.dataSet.join(', ')}
                        onChange={(e) => handleDataSetChange(e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Enter numbers separated by commas..."
                    />
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showHistogram}
                                onChange={(e) => handleInputChange('showHistogram', e.target.checked)}
                                className="mr-2"
                            />
                            Show Histogram
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showPolygon}
                                onChange={(e) => handleInputChange('showPolygon', e.target.checked)}
                                className="mr-2"
                            />
                            Show Polygon
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showCumulative}
                                onChange={(e) => handleInputChange('showCumulative', e.target.checked)}
                                className="mr-2"
                            />
                            Show Cumulative
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showPoints}
                                onChange={(e) => handleInputChange('showPoints', e.target.checked)}
                                className="mr-2"
                            />
                            Show Points
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showStatistics}
                                onChange={(e) => handleInputChange('showStatistics', e.target.checked)}
                                className="mr-2"
                            />
                            Show Statistics
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showPercentiles}
                                onChange={(e) => handleInputChange('showPercentiles', e.target.checked)}
                                className="mr-2"
                            />
                            Show Percentiles
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={cumulativeData.showQuartiles}
                                onChange={(e) => handleInputChange('showQuartiles', e.target.checked)}
                                className="mr-2"
                            />
                            Show Quartiles
                        </label>
                    </div>
                </div>
            </div>

            {/* Data Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h4 className="font-semibold text-blue-800 mb-3">Data Management</h4>
                <div className="flex space-x-2">
                    <button
                        onClick={generateRandomData}
                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                    >
                        Generate Random Data
                    </button>
                    <button
                        onClick={addDataPoint}
                        className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                    >
                        Add Random Point
                    </button>
                    <button
                        onClick={clearData}
                        className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded text-sm"
                    >
                        Clear Data
                    </button>
                </div>
            </div>

            {/* Statistics Summary */}
            {stats && (
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-3">Quick Statistics</h4>
                    <div className="grid grid-cols-3 gap-4 text-sm">
                        <div>
                            <strong>Count:</strong> {stats.n}
                        </div>
                        <div>
                            <strong>Mean:</strong> {stats.mean.toFixed(2)}
                        </div>
                        <div>
                            <strong>Median:</strong> {stats.median}
                        </div>
                        <div>
                            <strong>Mode:</strong> {stats.mode.join(', ')}
                        </div>
                        <div>
                            <strong>Std Dev:</strong> {stats.stdDev.toFixed(2)}
                        </div>
                        <div>
                            <strong>Range:</strong> {stats.range}
                        </div>
                        <div>
                            <strong>Q1:</strong> {stats.q1}
                        </div>
                        <div>
                            <strong>Q3:</strong> {stats.q3}
                        </div>
                        <div>
                            <strong>IQR:</strong> {stats.iqr}
                        </div>
                    </div>
                </div>
            )}

            {/* Cumulative Frequency Curve Canvas */}
            <div className="border border-gray-300 rounded-lg overflow-hidden">
                <canvas
                    ref={canvasRef}
                    width={800}
                    height={600}
                    className="w-full h-auto"
                />
            </div>
        </div>
    );
};

export default CumulativeFrequencyCurve;
