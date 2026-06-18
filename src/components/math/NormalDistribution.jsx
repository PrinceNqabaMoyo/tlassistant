import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const NormalDistribution = ({ initialData, onChange, isSubmitted }) => {
    const [normalData, setNormalData] = useState(initialData || {
        title: "Normal Distribution",
        mean: 0,
        standardDeviation: 1,
        showCurve: true,
        showArea: true,
        showMean: true,
        showStandardDeviations: true,
        showPercentiles: true,
        showZScore: true,
        showProbability: true,
        xMin: -4,
        xMax: 4,
        areaStart: -1,
        areaEnd: 1,
        backgroundColor: '#ffffff',
        gridColor: '#e5e7eb',
        axisColor: '#374151',
        curveColor: '#3B82F6',
        areaColor: '#10B981',
        meanColor: '#EF4444',
        stdDevColor: '#F59E0B'
    });

    const canvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    useEffect(() => {
        if (onChange) {
            onChange(normalData);
        }
    }, [normalData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawNormalDistribution();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [normalData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawNormalDistribution();
    }, []);

    // Normal distribution probability density function
    const normalPDF = (x, mean, stdDev) => {
        const coefficient = 1 / (stdDev * Math.sqrt(2 * Math.PI));
        const exponent = -Math.pow(x - mean, 2) / (2 * Math.pow(stdDev, 2));
        return coefficient * Math.exp(exponent);
    };

    // Cumulative distribution function (approximation)
    const normalCDF = (x, mean, stdDev) => {
        const z = (x - mean) / stdDev;
        return 0.5 * (1 + erf(z / Math.sqrt(2)));
    };

    // Error function approximation
    const erf = (x) => {
        const a1 = 0.254829592;
        const a2 = -0.284496736;
        const a3 = 1.421413741;
        const a4 = -1.453152027;
        const a5 = 1.061405429;
        const p = 0.3275911;

        const sign = x >= 0 ? 1 : -1;
        x = Math.abs(x);

        const t = 1 / (1 + p * x);
        const y = 1 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);

        return sign * y;
    };

    // Calculate area under curve between two points
    const calculateArea = (start, end, mean, stdDev) => {
        return normalCDF(end, mean, stdDev) - normalCDF(start, mean, stdDev);
    };

    // Calculate z-score
    const calculateZScore = (x, mean, stdDev) => {
        return (x - mean) / stdDev;
    };

    // Calculate percentiles
    const calculatePercentiles = () => {
        const { mean, standardDeviation } = normalData;
        const percentiles = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99];
        
        return percentiles.map(p => {
            // Approximate inverse CDF using normal approximation
            const z = Math.sqrt(2) * erf_inv(2 * p - 1);
            const x = mean + z * standardDeviation;
            return { percentile: p * 100, value: x };
        });
    };

    // Inverse error function approximation
    const erf_inv = (x) => {
        const a = 0.147;
        const sign = x >= 0 ? 1 : -1;
        const ln1mx = Math.log(1 - Math.abs(x));
        const term1 = 2 / (Math.PI * a) + ln1mx / 2;
        const term2 = ln1mx / a;
        return sign * Math.sqrt(-term1 + Math.sqrt(term1 * term1 - term2));
    };

    const drawNormalDistribution = () => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.log('NormalDistribution: Canvas not found');
            return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('NormalDistribution: Canvas context not available');
            return;
        }

        const width = canvas.width;
        const height = canvas.height;

        console.log('NormalDistribution: Drawing with dimensions:', { width, height, normalData });

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = '#ffffff'; // White background
        ctx.fillRect(0, 0, width, height);

        const { mean, standardDeviation, showCurve, showArea, showMean, showStandardDeviations, showPercentiles, showZScore, showProbability, xMin, xMax, areaStart, areaEnd, gridColor, axisColor, curveColor, areaColor, meanColor, stdDevColor } = normalData;

        const margin = 60;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;

        // Scale factors
        const xScale = plotWidth / (xMax - xMin);
        const maxY = normalPDF(mean, mean, standardDeviation);
        const yScale = plotHeight / (maxY * 1.2);

        const toCanvasX = (x) => margin + (x - xMin) * xScale;
        const toCanvasY = (y) => height - margin - y * yScale;

        // Draw grid
        ctx.strokeStyle = '#D1D5DB'; // Subtle grey grid lines
        ctx.lineWidth = 1;
        
        // Vertical grid lines
        for (let x = xMin; x <= xMax; x += 0.5) {
            const canvasX = toCanvasX(x);
            ctx.beginPath();
            ctx.moveTo(canvasX, margin);
            ctx.lineTo(canvasX, height - margin);
            ctx.stroke();
        }
        
        // Horizontal grid lines
        for (let y = 0; y <= maxY; y += maxY / 10) {
            const canvasY = toCanvasY(y);
            ctx.beginPath();
            ctx.moveTo(margin, canvasY);
            ctx.lineTo(width - margin, canvasY);
            ctx.stroke();
        }

        // Draw axes
        ctx.strokeStyle = '#000000'; // Black bold axes
        ctx.lineWidth = 3;
        
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

        // Draw area under curve
        if (showArea) {
            ctx.fillStyle = areaColor + '60';
            ctx.beginPath();
            ctx.moveTo(toCanvasX(areaStart), height - margin);
            
            for (let x = areaStart; x <= areaEnd; x += 0.01) {
                const y = normalPDF(x, mean, standardDeviation);
                ctx.lineTo(toCanvasX(x), toCanvasY(y));
            }
            
            ctx.lineTo(toCanvasX(areaEnd), height - margin);
            ctx.closePath();
            ctx.fill();
        }

        // Draw normal curve
        if (showCurve) {
            ctx.strokeStyle = curveColor;
            ctx.lineWidth = 3;
            ctx.beginPath();
            
            for (let x = xMin; x <= xMax; x += 0.01) {
                const y = normalPDF(x, mean, standardDeviation);
                if (x === xMin) {
                    ctx.moveTo(toCanvasX(x), toCanvasY(y));
                } else {
                    ctx.lineTo(toCanvasX(x), toCanvasY(y));
                }
            }
            
            ctx.stroke();
        }

        // Draw mean line
        if (showMean) {
            ctx.strokeStyle = meanColor;
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.moveTo(toCanvasX(mean), margin);
            ctx.lineTo(toCanvasX(mean), height - margin);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // Label mean
            ctx.fillStyle = meanColor;
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`μ = ${mean}`, toCanvasX(mean), height - margin + 20);
        }

        // Draw standard deviation lines
        if (showStandardDeviations) {
            ctx.strokeStyle = stdDevColor;
            ctx.lineWidth = 1;
            ctx.setLineDash([3, 3]);
            
            for (let i = 1; i <= 3; i++) {
                const leftX = mean - i * standardDeviation;
                const rightX = mean + i * standardDeviation;
                
                if (leftX >= xMin) {
                    ctx.beginPath();
                    ctx.moveTo(toCanvasX(leftX), margin);
                    ctx.lineTo(toCanvasX(leftX), height - margin);
                    ctx.stroke();
                    
                    ctx.fillStyle = stdDevColor;
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(`-${i}σ`, toCanvasX(leftX), height - margin + 35);
                }
                
                if (rightX <= xMax) {
                    ctx.beginPath();
                    ctx.moveTo(toCanvasX(rightX), margin);
                    ctx.lineTo(toCanvasX(rightX), height - margin);
                    ctx.stroke();
                    
                    ctx.fillStyle = stdDevColor;
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(`+${i}σ`, toCanvasX(rightX), height - margin + 35);
                }
            }
            ctx.setLineDash([]);
        }

        // Draw axis labels
        ctx.fillStyle = axisColor;
        ctx.font = '14px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('X', width / 2, height - 10);
        
        ctx.save();
        ctx.translate(20, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Probability Density', 0, 0);
        ctx.restore();

        // Draw title
        ctx.font = 'bold 16px Arial';
        ctx.fillText(normalData.title, width / 2, 25);

        // Draw statistics
        let yOffset = margin + 20;
        ctx.fillStyle = axisColor;
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'left';
        ctx.fillText('Statistics:', width - margin, yOffset);
        
        ctx.font = '12px Arial';
        yOffset += 20;
        ctx.fillText(`Mean (μ): ${mean}`, width - margin, yOffset);
        yOffset += 15;
        ctx.fillText(`Std Dev (σ): ${standardDeviation}`, width - margin, yOffset);
        yOffset += 15;
        ctx.fillText(`Variance (σ²): ${(standardDeviation * standardDeviation).toFixed(3)}`, width - margin, yOffset);

        // Draw area information
        if (showArea) {
            const area = calculateArea(areaStart, areaEnd, mean, standardDeviation);
            yOffset += 20;
            ctx.fillText(`Area (${areaStart} to ${areaEnd}): ${(area * 100).toFixed(2)}%`, width - margin, yOffset);
        }

        // Draw z-score information
        if (showZScore) {
            const zStart = calculateZScore(areaStart, mean, standardDeviation);
            const zEnd = calculateZScore(areaEnd, mean, standardDeviation);
            yOffset += 20;
            ctx.fillText(`Z-scores: ${zStart.toFixed(2)} to ${zEnd.toFixed(2)}`, width - margin, yOffset);
        }

        // Draw percentiles
        if (showPercentiles) {
            const percentiles = calculatePercentiles();
            yOffset += 30;
            ctx.font = 'bold 12px Arial';
            ctx.fillText('Percentiles:', width - margin, yOffset);
            
            ctx.font = '10px Arial';
            percentiles.forEach((p, index) => {
                yOffset += 12;
                ctx.fillText(`${p.percentile}%: ${p.value.toFixed(2)}`, width - margin, yOffset);
            });
        }

        // Draw probability information
        if (showProbability) {
            yOffset += 20;
            ctx.font = 'bold 12px Arial';
            ctx.fillText('Empirical Rule:', width - margin, yOffset);
            
            ctx.font = '10px Arial';
            yOffset += 15;
            ctx.fillText('68% within ±1σ', width - margin, yOffset);
            yOffset += 12;
            ctx.fillText('95% within ±2σ', width - margin, yOffset);
            yOffset += 12;
            ctx.fillText('99.7% within ±3σ', width - margin, yOffset);
        }
    };

    const handleInputChange = (field, value) => {
        setNormalData(prev => ({
            ...prev,
            [field]: field === 'mean' || field === 'standardDeviation' || field === 'xMin' || field === 'xMax' || field === 'areaStart' || field === 'areaEnd' ? parseFloat(value) || 0 : value
        }));
    };

    const handleToggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    const handleOpenFullScreen = () => {
        setIsFullScreenOpen(true);
    };

    const handleCloseFullScreen = () => {
        setIsFullScreenOpen(false);
    };

    const setStandardNormal = () => {
        setNormalData(prev => ({
            ...prev,
            mean: 0,
            standardDeviation: 1,
            xMin: -4,
            xMax: 4,
            areaStart: -1,
            areaEnd: 1
        }));
    };

    const setCommonDistributions = () => {
        const distributions = [
            { name: 'Standard Normal', mean: 0, stdDev: 1 },
            { name: 'Normal (μ=5, σ=2)', mean: 5, stdDev: 2 },
            { name: 'Normal (μ=-2, σ=0.5)', mean: -2, stdDev: 0.5 },
            { name: 'Normal (μ=10, σ=3)', mean: 10, stdDev: 3 }
        ];
        
        const randomDist = distributions[Math.floor(Math.random() * distributions.length)];
        setNormalData(prev => ({
            ...prev,
            mean: randomDist.mean,
            standardDeviation: randomDist.stdDev,
            xMin: randomDist.mean - 4 * randomDist.stdDev,
            xMax: randomDist.mean + 4 * randomDist.stdDev,
            areaStart: randomDist.mean - randomDist.stdDev,
            areaEnd: randomDist.mean + randomDist.stdDev
        }));
    };

    const currentArea = calculateArea(normalData.areaStart, normalData.areaEnd, normalData.mean, normalData.standardDeviation);

    // Parameter Panel Component
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Normal Distribution Parameters</h3>
            
            {/* Basic Parameters */}
            <div className="space-y-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        value={normalData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Mean (μ):</label>
                    <input
                        type="number"
                        step="0.1"
                        value={normalData.mean}
                        onChange={(e) => handleInputChange('mean', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Standard Deviation (σ):</label>
                    <input
                        type="number"
                        step="0.1"
                        min="0.1"
                        value={normalData.standardDeviation}
                        onChange={(e) => handleInputChange('standardDeviation', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>
            </div>

            {/* Range Parameters */}
            <div className="space-y-4">
                <h4 className="font-medium text-gray-700">Range Settings</h4>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Min:</label>
                        <input
                            type="number"
                            step="0.1"
                            value={normalData.xMin}
                            onChange={(e) => handleInputChange('xMin', e.target.value)}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Max:</label>
                        <input
                            type="number"
                            step="0.1"
                            value={normalData.xMax}
                            onChange={(e) => handleInputChange('xMax', e.target.value)}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Area Start:</label>
                        <input
                            type="number"
                            step="0.1"
                            value={normalData.areaStart}
                            onChange={(e) => handleInputChange('areaStart', e.target.value)}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Area End:</label>
                        <input
                            type="number"
                            step="0.1"
                            value={normalData.areaEnd}
                            onChange={(e) => handleInputChange('areaEnd', e.target.value)}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
            </div>

            {/* Display Options */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Display Options</h4>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showCurve}
                        onChange={(e) => handleInputChange('showCurve', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Curve</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showArea}
                        onChange={(e) => handleInputChange('showArea', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Area</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showMean}
                        onChange={(e) => handleInputChange('showMean', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Mean</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showStandardDeviations}
                        onChange={(e) => handleInputChange('showStandardDeviations', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Std Devs</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showPercentiles}
                        onChange={(e) => handleInputChange('showPercentiles', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Percentiles</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showZScore}
                        onChange={(e) => handleInputChange('showZScore', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Z-Scores</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={normalData.showProbability}
                        onChange={(e) => handleInputChange('showProbability', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Probability</span>
                </label>
            </div>

            {/* Quick Actions */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Quick Actions</h4>
                <button
                    onClick={setStandardNormal}
                    className="w-full px-3 py-2 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                    disabled={isSubmitted}
                >
                    Standard Normal
                </button>
                <button
                    onClick={setCommonDistributions}
                    className="w-full px-3 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded text-sm"
                    disabled={isSubmitted}
                >
                    Random Distribution
                </button>
            </div>

            {/* Area Information */}
            <div className="p-3 bg-green-50 border border-green-200 rounded">
                <h4 className="font-medium text-green-800 mb-2">Area Information</h4>
                <div className="space-y-1 text-sm">
                    <div><strong>Area:</strong> {(currentArea * 100).toFixed(2)}%</div>
                    <div><strong>Probability:</strong> {currentArea.toFixed(4)}</div>
                    <div><strong>Z-score range:</strong> {((normalData.areaStart - normalData.mean) / normalData.standardDeviation).toFixed(2)} to {((normalData.areaEnd - normalData.mean) / normalData.standardDeviation).toFixed(2)}</div>
                    <div><strong>Range:</strong> {normalData.areaStart} to {normalData.areaEnd}</div>
                </div>
            </div>
        </div>
    );

    return (
        <div className="relative">
            <div className="p-4 bg-white border border-gray-300 rounded-lg mt-4">
                <div className="flex items-center justify-between mb-4">
                    <h3 className="font-semibold text-gray-700">Normal Distribution</h3>
                    <button
                        onClick={handleOpenFullScreen}
                        className="p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow-lg transition-colors"
                        title="Open Full Screen Mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>
            {/* Quick Controls */}
            <div className="grid grid-cols-3 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Mean (μ):</label>
                    <input
                        type="number"
                        step="0.1"
                        value={normalData.mean}
                        onChange={(e) => handleInputChange('mean', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Std Dev (σ):</label>
                    <input
                        type="number"
                        step="0.1"
                        min="0.1"
                        value={normalData.standardDeviation}
                        onChange={(e) => handleInputChange('standardDeviation', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Area Range:</label>
                    <div className="flex space-x-1">
                        <input
                            type="number"
                            step="0.1"
                            value={normalData.areaStart}
                            onChange={(e) => handleInputChange('areaStart', e.target.value)}
                            className="flex-1 px-2 py-2 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                        <span className="self-center text-gray-500">to</span>
                        <input
                            type="number"
                            step="0.1"
                            value={normalData.areaEnd}
                            onChange={(e) => handleInputChange('areaEnd', e.target.value)}
                            className="flex-1 px-2 py-2 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
            </div>

            {/* Quick Actions */}
            <div className="flex space-x-2 mb-4">
                <button
                    onClick={setStandardNormal}
                    className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                    disabled={isSubmitted}
                >
                    Standard Normal
                </button>
                <button
                    onClick={setCommonDistributions}
                    className="px-3 py-1 bg-purple-600 hover:bg-purple-700 text-white rounded text-sm"
                    disabled={isSubmitted}
                >
                    Random Distribution
                </button>
            </div>

            {/* Area Information */}
            <div className="p-3 bg-green-50 border border-green-200 rounded mb-4">
                <div className="text-sm">
                    <div><strong>Area:</strong> {(currentArea * 100).toFixed(2)}% | <strong>Probability:</strong> {currentArea.toFixed(4)}</div>
                </div>
            </div>

            {/* Normal Distribution Canvas */}
            <div className="border border-gray-300 rounded-lg overflow-hidden">
                <canvas
                    ref={canvasRef}
                    width={600}
                    height={400}
                    className="w-full h-auto"
                />
            </div>

            {/* Full Screen Modal */}
            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title="Normal Distribution - Full Screen Mode"
                onToggleFullScreen={handleToggleFullScreen}
                isFullScreen={isFullScreen}
                parameterPanel={<ParameterPanel />}
            >
                <div className="h-full flex items-center justify-center">
                    <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                        <canvas
                            ref={canvasRef}
                            width={800}
                            height={600}
                            className="w-full h-auto"
                        />
                    </div>
                </div>
            </FullScreenModal>
        </div>
        </div>
    );
};

export default NormalDistribution;
