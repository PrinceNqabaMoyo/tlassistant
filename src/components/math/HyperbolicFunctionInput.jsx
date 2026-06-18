import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const HyperbolicFunctionInput = ({ initialData, onChange, isSubmitted }) => {
    const [a, setA] = useState(initialData.a || '1');
    const [b, setB] = useState(initialData.b || '0');
    const [q, setQ] = useState(initialData.q || '0');
    const [functionForm, setFunctionForm] = useState(initialData.functionForm || 'simple'); // 'simple' or 'shifted'
    const [xMin, setXMin] = useState(initialData.x_range ? initialData.x_range[0] : '-10');
    const [xMax, setXMax] = useState(initialData.x_range ? initialData.x_range[1] : '10');
    const [title, setTitle] = useState(initialData.title || '');

    const [lineColor, setLineColor] = useState(initialData.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData.showGrid !== false);
    const [showAsymptotes, setShowAsymptotes] = useState(initialData.showAsymptotes !== false);
    const [showPoints, setShowPoints] = useState(initialData.showPoints !== false);

    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    // Calculate hyperbolic properties
    const aNum = Number(a) || 0;
    const bNum = Number(b) || 0;
    const qNum = Number(q) || 0;
    
    // Mathematical properties based on function form
    const verticalAsymptote = functionForm === 'simple' 
        ? 0  // For y = a/x + b, vertical asymptote is always at x = 0
        : (qNum !== 0 ? -qNum : null);
    const horizontalAsymptote = aNum !== 0 ? bNum : null;
    const domain = verticalAsymptote !== null ? `x ≠ ${verticalAsymptote}` : 'All real numbers';
    const range = aNum !== 0 ? 'All real numbers except y = b' : 'y = b';

    useEffect(() => {
        const formattedData = {
            type: "hyperbolic_function",
            title: title,
            a: aNum,
            b: bNum,
            q: qNum,
            functionForm: functionForm,
            x_range: [Number(xMin) || -10, Number(xMax) || 10],
            lineColor: lineColor,
            showGrid: showGrid,
            showAsymptotes: showAsymptotes,
            showPoints: showPoints
        };
        onChange(formattedData);
    }, [a, b, q, functionForm, xMin, xMax, title, lineColor, showGrid, showAsymptotes, showPoints, onChange]);

    // Draw the hyperbolic function graph
    const drawGraph = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        // HiDPI crisp rendering
        const dpr = typeof window !== 'undefined' ? (window.devicePixelRatio || 1) : 1;
        const rect = canvas.getBoundingClientRect();
        const cssWidth = Math.max(1, Math.round(rect.width));
        const cssHeight = Math.max(1, Math.round(rect.height));
        const desiredWidth = Math.round(cssWidth * dpr);
        const desiredHeight = Math.round(cssHeight * dpr);
        
        if (canvas.width !== desiredWidth || canvas.height !== desiredHeight) {
            canvas.width = desiredWidth;
            canvas.height = desiredHeight;
        }
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        const width = cssWidth;
        const height = cssHeight;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        const xMinNum = Number(xMin);
        const xMaxNum = Number(xMax);
        const yMinNum = -10; // Fixed y-range for hyperbolic functions
        const yMaxNum = 10;

        // Calculate scale factors
        const xScale = width / (xMaxNum - xMinNum);
        const yScale = height / (yMaxNum - yMinNum);

        // Helper functions to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - xMinNum) * xScale;
        const toCanvasY = (y) => height - (y - yMinNum) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB';
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = xMinNum; x <= xMaxNum; x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = yMinNum; y <= yMaxNum; y++) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 3;

        // X-axis
        const xAxisY = toCanvasY(0);
        if (xAxisY >= 0 && xAxisY <= height) {
            ctx.beginPath();
            ctx.moveTo(0, xAxisY);
            ctx.lineTo(width, xAxisY);
            ctx.stroke();
        }

        // Y-axis
        const yAxisX = toCanvasX(0);
        if (yAxisX >= 0 && yAxisX <= width) {
            ctx.beginPath();
            ctx.moveTo(yAxisX, 0);
            ctx.lineTo(yAxisX, height);
            ctx.stroke();
        }

        // Draw the hyperbolic function
        if (aNum !== 0) {
            ctx.strokeStyle = lineColor;
            ctx.lineWidth = 3;
            
            const points = generatePoints();
            
            // Draw left branch
            const leftPoints = points.filter(p => p.branch === 'left');
            if (leftPoints.length > 0) {
                ctx.beginPath();
                let firstPoint = true;
                
                leftPoints.forEach(point => {
                    const canvasX = toCanvasX(point.x);
                    const canvasY = toCanvasY(point.y);
                    
                    if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                        if (firstPoint) {
                            ctx.moveTo(canvasX, canvasY);
                            firstPoint = false;
                        } else {
                            ctx.lineTo(canvasX, canvasY);
                        }
                    }
                });
                ctx.stroke();
            }
            
            // Draw right branch
            const rightPoints = points.filter(p => p.branch === 'right');
            if (rightPoints.length > 0) {
                ctx.beginPath();
                let firstPoint = true;
                
                rightPoints.forEach(point => {
                    const canvasX = toCanvasX(point.x);
                    const canvasY = toCanvasY(point.y);
                    
                    if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                        if (firstPoint) {
                            ctx.moveTo(canvasX, canvasY);
                            firstPoint = false;
                        } else {
                            ctx.lineTo(canvasX, canvasY);
                        }
                    }
                });
                ctx.stroke();
            }

            // Draw points if enabled
            if (showPoints) {
                ctx.fillStyle = lineColor;
                points.forEach((point, index) => {
                    if (index % 20 === 0) { // Show every 20th point to avoid clutter
                        const canvasX = toCanvasX(point.x);
                        const canvasY = toCanvasY(point.y);
                        
                        if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                            ctx.beginPath();
                            ctx.arc(canvasX, canvasY, 4, 0, 2 * Math.PI);
                            ctx.fill();
                        }
                    }
                });
            }
        }

        // Draw asymptotes
        if (showAsymptotes) {
            ctx.strokeStyle = '#EF4444';
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);

            // Vertical asymptote
            if (verticalAsymptote !== null) {
                const asymptoteX = toCanvasX(verticalAsymptote);
                if (asymptoteX >= 0 && asymptoteX <= width) {
                    ctx.beginPath();
                    ctx.moveTo(asymptoteX, 0);
                    ctx.lineTo(asymptoteX, height);
                    ctx.stroke();
                }
            }

            // Horizontal asymptote
            if (horizontalAsymptote !== null) {
                const asymptoteY = toCanvasY(horizontalAsymptote);
                if (asymptoteY >= 0 && asymptoteY <= height) {
                    ctx.beginPath();
                    ctx.moveTo(0, asymptoteY);
                    ctx.lineTo(width, asymptoteY);
                    ctx.stroke();
                }
            }

            ctx.setLineDash([]);
        }
    };

    // Full screen graph drawing function
    const drawFullScreenGraph = () => {
        const canvas = fullScreenCanvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        // HiDPI crisp rendering
        const dpr = typeof window !== 'undefined' ? (window.devicePixelRatio || 1) : 1;
        const rect = canvas.getBoundingClientRect();
        const cssWidth = Math.max(1, Math.round(rect.width));
        const cssHeight = Math.max(1, Math.round(rect.height));
        const desiredWidth = Math.round(cssWidth * dpr);
        const desiredHeight = Math.round(cssHeight * dpr);
        
        if (canvas.width !== desiredWidth || canvas.height !== desiredHeight) {
            canvas.width = desiredWidth;
            canvas.height = desiredHeight;
        }
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        const width = cssWidth;
        const height = cssHeight;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        const xMinNum = Number(xMin);
        const xMaxNum = Number(xMax);
        const yMinNum = -10; // Fixed y-range for hyperbolic functions
        const yMaxNum = 10;

        // Calculate scale factors
        const xScale = width / (xMaxNum - xMinNum);
        const yScale = height / (yMaxNum - yMinNum);

        // Helper functions to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - xMinNum) * xScale;
        const toCanvasY = (y) => height - (y - yMinNum) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB';
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = xMinNum; x <= xMaxNum; x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = yMinNum; y <= yMaxNum; y++) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 3;

        // X-axis
        const xAxisY = toCanvasY(0);
        if (xAxisY >= 0 && xAxisY <= height) {
            ctx.beginPath();
            ctx.moveTo(0, xAxisY);
            ctx.lineTo(width, xAxisY);
            ctx.stroke();
        }

        // Y-axis
        const yAxisX = toCanvasX(0);
        if (yAxisX >= 0 && yAxisX <= width) {
            ctx.beginPath();
            ctx.moveTo(yAxisX, 0);
            ctx.lineTo(yAxisX, height);
            ctx.stroke();
        }

        // Draw the hyperbolic function
        if (aNum !== 0) {
            ctx.strokeStyle = lineColor;
            ctx.lineWidth = 3;
            
            const points = generatePoints();
            
            // Draw left branch
            const leftPoints = points.filter(p => p.branch === 'left');
            if (leftPoints.length > 0) {
                ctx.beginPath();
                let firstPoint = true;
                
                leftPoints.forEach(point => {
                    const canvasX = toCanvasX(point.x);
                    const canvasY = toCanvasY(point.y);
                    
                    if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                        if (firstPoint) {
                            ctx.moveTo(canvasX, canvasY);
                            firstPoint = false;
                        } else {
                            ctx.lineTo(canvasX, canvasY);
                        }
                    }
                });
                ctx.stroke();
            }
            
            // Draw right branch
            const rightPoints = points.filter(p => p.branch === 'right');
            if (rightPoints.length > 0) {
                ctx.beginPath();
                let firstPoint = true;
                
                rightPoints.forEach(point => {
                    const canvasX = toCanvasX(point.x);
                    const canvasY = toCanvasY(point.y);
                    
                    if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                        if (firstPoint) {
                            ctx.moveTo(canvasX, canvasY);
                            firstPoint = false;
                        } else {
                            ctx.lineTo(canvasX, canvasY);
                        }
                    }
                });
                ctx.stroke();
            }

            // Draw points if enabled
            if (showPoints) {
                ctx.fillStyle = lineColor;
                points.forEach((point, index) => {
                    if (index % 20 === 0) { // Show every 20th point to avoid clutter
                        const canvasX = toCanvasX(point.x);
                        const canvasY = toCanvasY(point.y);
                        
                        if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                            ctx.beginPath();
                            ctx.arc(canvasX, canvasY, 4, 0, 2 * Math.PI);
                            ctx.fill();
                        }
                    }
                });
            }
        }

        // Draw asymptotes
        if (showAsymptotes) {
            ctx.strokeStyle = '#EF4444';
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);

            // Vertical asymptote
            if (verticalAsymptote !== null) {
                const asymptoteX = toCanvasX(verticalAsymptote);
                if (asymptoteX >= 0 && asymptoteX <= width) {
                    ctx.beginPath();
                    ctx.moveTo(asymptoteX, 0);
                    ctx.lineTo(asymptoteX, height);
                    ctx.stroke();
                }
            }

            // Horizontal asymptote
            if (horizontalAsymptote !== null) {
                const asymptoteY = toCanvasY(horizontalAsymptote);
                if (asymptoteY >= 0 && asymptoteY <= height) {
                    ctx.beginPath();
                    ctx.moveTo(0, asymptoteY);
                    ctx.lineTo(width, asymptoteY);
                    ctx.stroke();
                }
            }

            ctx.setLineDash([]);
        }
    };

    // Redraw graph when parameters change
    useEffect(() => {
        const timer = setTimeout(() => {
            drawGraph();
            drawFullScreenGraph();
        }, 100);
        return () => clearTimeout(timer);
    }, [a, b, q, functionForm, xMin, xMax, lineColor, showGrid, showPoints, showAsymptotes]);

    // Initial draw
    useEffect(() => {
        drawGraph();
        drawFullScreenGraph();
    }, []);

    // Redraw full screen graph when modal opens
    useEffect(() => {
        if (isFullScreenOpen) {
            const timer = setTimeout(() => {
                drawFullScreenGraph();
            }, 100);
            return () => clearTimeout(timer);
        }
    }, [isFullScreenOpen]);

    const generatePoints = () => {
        const points = [];
        const step = (Number(xMax) - Number(xMin)) / 200;
        
        // Determine asymptote position
        let asymptoteX;
        if (functionForm === 'simple') {
            asymptoteX = 0; // For y = a/x + b, asymptote is at x = 0
        } else {
            asymptoteX = -qNum; // For y = a/(x+q) + b, asymptote is at x = -q
        }
        
        // Generate points for left branch (before asymptote)
        for (let x = Number(xMin); x < asymptoteX - 0.01; x += step) {
            let y;
            if (functionForm === 'simple') {
                y = aNum / x + bNum;
            } else {
                y = aNum / (x + qNum) + bNum;
            }
            
            if (isFinite(y) && Math.abs(y) < 1000) {
                points.push({ x: x, y: y, branch: 'left' });
            }
        }
        
        // Generate points for right branch (after asymptote)
        for (let x = asymptoteX + 0.01; x <= Number(xMax); x += step) {
            let y;
            if (functionForm === 'simple') {
                y = aNum / x + bNum;
            } else {
                y = aNum / (x + qNum) + bNum;
            }
            
            if (isFinite(y) && Math.abs(y) < 1000) {
                points.push({ x: x, y: y, branch: 'right' });
            }
        }
        
        return points;
    };

    const getFunctionBehavior = () => {
        if (aNum === 0) return 'Constant function (y = b)';
        if (functionForm === 'simple') {
        if (bNum === 0) return 'Reciprocal function (y = a/x)';
            return 'Reciprocal function with vertical shift (y = a/x + b)';
        } else {
            if (qNum === 0) return 'Reciprocal function with vertical shift (y = a/x + b)';
            return 'Reciprocal function with horizontal and vertical shifts (y = a/(x+q) + b)';
        }
    };

    const getSymmetry = () => {
        if (aNum === 0) return 'None (constant function)';
        if (functionForm === 'simple' && bNum === 0) return 'Origin symmetry (odd function)';
        return 'Point symmetry about asymptote intersection';
    };

    // Full screen handlers
    const handleOpenFullScreen = () => {
        setIsFullScreenOpen(true);
    };

    const handleCloseFullScreen = () => {
        setIsFullScreenOpen(false);
    };

    const handleToggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    // Parameter Panel Component for Full Screen
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Hyperbolic Function Parameters</h3>
            
            {/* Function Form Selection */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Function Form</h4>
                <select
                    className="w-full p-2 border border-purple-300 rounded focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors text-sm font-medium text-purple-600 bg-purple-50"
                    value={functionForm}
                    onChange={(e) => setFunctionForm(e.target.value)}
                    disabled={isSubmitted}
                >
                    <option value="simple">y = a/x + b</option>
                    <option value="shifted">y = a/(x+q) + b</option>
                </select>
            </div>

            {/* Parameters */}
            <div className="space-y-3">
                <h4 className="font-medium text-gray-700">Parameters</h4>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">a (Numerator):</label>
                    <input 
                        type="number" 
                        step="0.1"
                        className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={a} 
                        onChange={(e) => setA(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="1" 
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">b (Vertical shift):</label>
                    <input 
                        type="number" 
                        step="0.1"
                        className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={b} 
                        onChange={(e) => setB(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="0" 
                    />
                </div>
                {functionForm === 'shifted' && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">q (Horizontal shift):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={q} 
                            onChange={(e) => setQ(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="0" 
                        />
                    </div>
                )}
            </div>

            {/* Display Range */}
            <div className="space-y-3">
                <h4 className="font-medium text-gray-700">Display Range</h4>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-xs font-medium text-gray-700 mb-1">X-Min:</label>
                        <input 
                            type="number" 
                            step="0.5"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMin} 
                            onChange={(e) => setXMin(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="-10" 
                        />
                    </div>
                    <div>
                        <label className="block text-xs font-medium text-gray-700 mb-1">X-Max:</label>
                        <input 
                            type="number" 
                            step="0.5"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMax} 
                            onChange={(e) => setXMax(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="10" 
                        />
                    </div>
                </div>
            </div>

            {/* Display Options */}
            <div className="space-y-3">
                <h4 className="font-medium text-gray-700">Display Options</h4>
                <div className="space-y-2">
                    <label className="flex items-center space-x-2">
                        <input 
                            type="checkbox" 
                            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showGrid} 
                            onChange={(e) => setShowGrid(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Grid</span>
                    </label>
                    <label className="flex items-center space-x-2">
                        <input 
                            type="checkbox" 
                            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showPoints} 
                            onChange={(e) => setShowPoints(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Points</span>
                    </label>
                    <label className="flex items-center space-x-2">
                        <input 
                            type="checkbox" 
                            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showAsymptotes} 
                            onChange={(e) => setShowAsymptotes(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Asymptotes</span>
                    </label>
                </div>
            </div>

            {/* Line Color */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Line Color</h4>
                <input 
                    type="color" 
                    className="w-full h-10 border border-gray-300 rounded cursor-pointer" 
                    value={lineColor} 
                    onChange={(e) => setLineColor(e.target.value)} 
                    disabled={isSubmitted} 
                />
            </div>

            {/* Mathematical Analysis */}
            {aNum !== 0 && (
                <div className="space-y-2 p-3 bg-purple-50 rounded-lg">
                    <h4 className="font-medium text-gray-700">Analysis</h4>
                    <div className="text-sm space-y-1">
                        <div><strong>Function:</strong> {functionForm === 'simple' ? 'y = a/x + b' : 'y = a/(x+q) + b'}</div>
                        <div><strong>Vertical Asymptote:</strong> {verticalAsymptote !== null ? verticalAsymptote.toFixed(2) : 'None'}</div>
                        <div><strong>Horizontal Asymptote:</strong> {horizontalAsymptote !== null ? horizontalAsymptote.toFixed(2) : 'None'}</div>
                        <div><strong>Domain:</strong> {domain}</div>
                    </div>
                </div>
            )}
        </div>
    );

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">






            {/* Parameters and Range - Combined */}
            <div className="bg-gray-50 rounded-lg p-3 mb-4">
                <h4 className="text-sm font-medium text-gray-800 mb-3">
                    Parameters & Range: {functionForm === 'simple' ? 'y = a/x + b' : 'y = a/(x+q) + b'}
                </h4>
                <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
                    <div>
                        <label className="block text-xs font-medium text-gray-700 mb-1">a (Numerator):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={a} 
                            onChange={(e) => !isSubmitted && setA(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="1" 
                        />
                    </div>
                    <div>
                        <label className="block text-xs font-medium text-gray-700 mb-1">b (Vertical shift):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={b} 
                            onChange={(e) => !isSubmitted && setB(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="0" 
                        />
                    </div>
                    {functionForm === 'shifted' && (
                        <div>
                            <label className="block text-xs font-medium text-gray-700 mb-1">q (Horizontal shift):</label>
                            <input 
                                type="number" 
                                step="0.1"
                                className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={q} 
                                onChange={(e) => !isSubmitted && setQ(e.target.value)} 
                                disabled={isSubmitted} 
                                placeholder="0" 
                        />
                </div>
                    )}
                    <div>
                        <label className="block text-xs font-medium text-gray-700 mb-1">X-Min:</label>
                        <input 
                            type="number" 
                            step="0.5"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMin} 
                            onChange={(e) => !isSubmitted && setXMin(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="-10" 
                        />
                    </div>
                    <div>
                        <label className="block text-xs font-medium text-gray-700 mb-1">X-Max:</label>
                        <input 
                            type="number" 
                            step="0.5"
                            className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMax} 
                            onChange={(e) => !isSubmitted && setXMax(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="10" 
                        />
                    </div>
                </div>
            </div>



            {/* Unified Control Panel with Checkboxes */}
            <div className="grid grid-cols-1 md:grid-cols-5 gap-4 mb-4 p-3 bg-purple-50 rounded-lg">
                <div className="grid grid-cols-2 md:grid-cols-4 gap-3 md:col-span-4">
                    <div className="text-center">
                        <select
                            className="w-full p-2 border border-purple-300 rounded focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors text-sm font-medium text-purple-600 bg-purple-50"
                            value={functionForm}
                            onChange={(e) => !isSubmitted && setFunctionForm(e.target.value)}
                            disabled={isSubmitted}
                        >
                            <option value="simple">y = a/x + b</option>
                            <option value="shifted">y = a/(x+q) + b</option>
                        </select>
                        <div className="text-xs text-purple-700 mt-1">Function Form</div>
                    </div>
                    <div className="text-center">
                        <div className="text-lg font-bold text-blue-600">{verticalAsymptote !== null ? verticalAsymptote.toFixed(2) : 'None'}</div>
                        <div className="text-xs text-blue-700">Vertical Asymptote</div>
                    </div>
                    <div className="text-center">
                        <div className="text-lg font-bold text-green-600">{horizontalAsymptote !== null ? horizontalAsymptote.toFixed(2) : 'None'}</div>
                        <div className="text-xs text-green-700">Horizontal Asymptote</div>
                    </div>
                    <div className="text-center">
                        <div className="flex items-center justify-center gap-2">
                            <label className="text-xs text-gray-700">Color:</label>
                            <input 
                                type="color" 
                                className="w-8 h-6 border border-gray-300 rounded cursor-pointer" 
                                value={lineColor} 
                                onChange={(e) => !isSubmitted && setLineColor(e.target.value)} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        <div className="text-xs text-gray-700 mt-1">Line Color</div>
                    </div>
                </div>
                <div className="flex flex-col justify-center space-y-2">
                    <div className="flex items-center space-x-2">
                        <input 
                            type="checkbox" 
                            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showGrid} 
                            onChange={(e) => !isSubmitted && setShowGrid(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Grid</span>
                </div>
                    <div className="flex items-center space-x-2">
                        <input 
                            type="checkbox" 
                            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showPoints} 
                            onChange={(e) => !isSubmitted && setShowPoints(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Points</span>
                </div>
                    <div className="flex items-center space-x-2">
                        <input 
                            type="checkbox" 
                            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showAsymptotes} 
                            onChange={(e) => !isSubmitted && setShowAsymptotes(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Asymptotes</span>
                        </div>
                    </div>
                </div>



            {/* Function Graph */}
            <div className="border border-gray-200 rounded-lg p-4 bg-white">
                <div className="flex items-center justify-between mb-3">
                    <h4 className="text-md font-medium text-gray-800">Function Graph</h4>
                    <button 
                        onClick={handleOpenFullScreen} 
                        className="p-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded transition-colors" 
                        title="Full screen"
                    >
                        <Maximize2 size={16} />
                    </button>
                </div>
                <div className="border border-gray-200 rounded-lg bg-white p-3">
                    <canvas 
                        ref={canvasRef} 
                        width={800} 
                        height={600} 
                        className="w-full h-[calc(100vh-10rem)] border border-gray-200 rounded-lg"
                    />
                    </div>
                </div>

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• <strong>y = a/x + b:</strong> Vertical asymptote at x = 0, horizontal asymptote at y = b</li>
                    <li>• <strong>y = a/(x+q) + b:</strong> Vertical asymptote at x = -q, horizontal asymptote at y = b</li>
                    <li>• Parameter 'a' controls the scale and direction (positive = first/third quadrants, negative = second/fourth quadrants)</li>
                    <li>• Parameter 'b' shifts the function vertically</li>
                    <li>• Parameter 'q' (in shifted form) shifts the function horizontally</li>
                </ul>
            </div>

            {/* Full Screen Modal */}
            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title="Hyperbolic Function Graph - Full Screen Mode"
                onToggleFullScreen={handleToggleFullScreen}
                isFullScreen={isFullScreen}
                hideFullScreenToggle={true}
                parameterPanel={<ParameterPanel />}
            >
                <div className="h-full flex items-center justify-center">
                    <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                        <canvas 
                            ref={fullScreenCanvasRef} 
                            width={800} 
                            height={600} 
                            className="w-full h-auto" 
                        />
                    </div>
                </div>
            </FullScreenModal>
        </div>
    );
};

export default HyperbolicFunctionInput;
