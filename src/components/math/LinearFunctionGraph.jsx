import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const LinearFunctionGraph = ({ initialData, onChange, isSubmitted, isConfigMode = false }) => {
    const [graphData, setGraphData] = useState(() => {
        const defaultData = {
            title: "Linear Function",
            m: 2,
            c: 3,
            xIntercept: -1.5, // New: x-intercept control
            equation: "2x + 3", // New: editable equation string
            x_range: [-10, 10],
            y_range: [-20, 20],
            lineColor: '#3B82F6',
            showGrid: true,
            showPoints: true,
            showSlope: true,
            showYIntercept: true,
            showXIntercept: true,
            editMode: 'parameters' // New: 'parameters' or 'equation'
        };
        
        if (initialData) {
            // Ensure xIntercept is calculated if not provided
            const mergedData = { ...defaultData, ...initialData };
            if (mergedData.xIntercept === undefined && mergedData.m !== 0) {
                mergedData.xIntercept = -mergedData.c / mergedData.m;
            }
            return mergedData;
        }
        
        return defaultData;
    });

    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    // Parse equation string to extract m and c
    const parseEquation = (equation) => {
        try {
            // Remove spaces and convert to lowercase
            const cleanEq = equation.replace(/\s/g, '').toLowerCase();
            
            // Handle different equation formats
            if (cleanEq.includes('y=')) {
                const rightSide = cleanEq.split('y=')[1];
                return parseRightSide(rightSide);
            } else if (cleanEq.includes('=')) {
                const rightSide = cleanEq.split('=')[1];
                return parseRightSide(rightSide);
            } else {
                return parseRightSide(cleanEq);
            }
        } catch (error) {
            console.log('Error parsing equation:', error);
            return { m: graphData.m, c: graphData.c };
        }
    };

    const parseRightSide = (rightSide) => {
        let m = 0, c = 0;
        
        // Handle cases like "2x+3", "2x", "3", "x+3", "-2x-3"
        const terms = rightSide.split(/(?=[+-])/);
        
        terms.forEach(term => {
            if (term.includes('x')) {
                const coef = term.replace('x', '');
                if (coef === '' || coef === '+') m = 1;
                else if (coef === '-') m = -1;
                else m = parseFloat(coef);
            } else {
                c = parseFloat(term) || 0;
            }
        });
        
        return { m, c };
    };

    // Update equation when m or c changes
    useEffect(() => {
        const newEquation = `${graphData.m}x ${graphData.c >= 0 ? '+' : ''}${graphData.c}`;
        setGraphData(prev => ({
            ...prev,
            equation: newEquation
        }));
    }, [graphData.m, graphData.c]);

    // Update x-intercept when m or c changes
    useEffect(() => {
        if (graphData.m !== 0) {
            const newXIntercept = -graphData.c / graphData.m;
            setGraphData(prev => ({
                ...prev,
                xIntercept: newXIntercept
            }));
        }
    }, [graphData.m, graphData.c]);

    // Update m and c when x-intercept changes
    const handleXInterceptChange = (newXIntercept) => {
        if (graphData.m !== 0) {
            const newC = -graphData.m * newXIntercept;
            setGraphData(prev => ({
                ...prev,
                xIntercept: newXIntercept,
                c: newC
            }));
        }
    };

    // Update m and c when equation changes
    const handleEquationChange = (newEquation) => {
        const { m, c } = parseEquation(newEquation);
        setGraphData(prev => ({
            ...prev,
            equation: newEquation,
            m: m,
            c: c
        }));
    };

    // Parse initial equation when component mounts or initialData changes
    useEffect(() => {
        if (initialData?.equation && initialData.equation !== graphData.equation) {
            const { m, c } = parseEquation(initialData.equation);
            setGraphData(prev => ({
                ...prev,
                equation: initialData.equation,
                m: m,
                c: c
            }));
        }
    }, [initialData?.equation]);

    // Update internal state when initialData changes (for function type switching)
    useEffect(() => {
        if (initialData) {
            setGraphData(prev => ({
                ...prev,
                ...initialData,
                // Ensure xIntercept is calculated if not provided
                xIntercept: initialData.xIntercept !== undefined ? initialData.xIntercept : 
                           (initialData.m !== 0 ? -initialData.c / initialData.m : prev.xIntercept)
            }));
        }
    }, []); // Only run once on mount

    useEffect(() => {
        if (onChange) {
            onChange(graphData);
        }
    }, [graphData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawGraph();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [graphData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawGraph();
    }, []);

    // Redraw full-screen canvas when modal opens or graphData changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            drawGraph(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, graphData]);

    const drawGraph = (targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) {
            console.log('LinearFunctionGraph: Canvas not found');
            return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('LinearFunctionGraph: Canvas context not available');
            return;
        }

        // HiDPI crisp rendering: match backing store to CSS size and DPR
        const dpr = typeof window !== 'undefined' ? (window.devicePixelRatio || 1) : 1;
        const rect = canvas.getBoundingClientRect();
        const cssWidth = Math.max(1, Math.round(rect.width));
        const cssHeight = Math.max(1, Math.round(rect.height));
        // Only resize when needed to avoid clearing too often
        const desiredWidth = Math.round(cssWidth * dpr);
        const desiredHeight = Math.round(cssHeight * dpr);
        if (canvas.width !== desiredWidth || canvas.height !== desiredHeight) {
            canvas.width = desiredWidth;
            canvas.height = desiredHeight;
        }
        // Draw in CSS pixel coordinates
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        const width = cssWidth;
        const height = cssHeight;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff'; // White background
        ctx.fillRect(0, 0, width, height);

        const { m, c, x_range, y_range, lineColor, showGrid, showPoints, showSlope, showYIntercept, showXIntercept } = graphData;

        // Calculate scale factors
        const xScale = width / (x_range[1] - x_range[0]);
        const yScale = height / (y_range[1] - y_range[0]);

        // Helper function to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - x_range[0]) * xScale;
        const toCanvasY = (y) => height - (y - y_range[0]) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB'; // Subtle grey grid lines
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = x_range[0]; x <= x_range[1]; x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = y_range[0]; y <= y_range[1]; y++) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = '#000000'; // Black bold axes
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

        // Draw the linear function
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 3;
        ctx.beginPath();

        // Calculate two points on the line
        const x1 = x_range[0];
        const y1 = m * x1 + c;
        const x2 = x_range[1];
        const y2 = m * x2 + c;

        const canvasX1 = toCanvasX(x1);
        const canvasY1 = toCanvasY(y1);
        const canvasX2 = toCanvasX(x2);
        const canvasY2 = toCanvasY(y2);

        ctx.moveTo(canvasX1, canvasY1);
        ctx.lineTo(canvasX2, canvasY2);
        ctx.stroke();

        // Draw points if enabled
        if (showPoints) {
            ctx.fillStyle = lineColor;
            ctx.beginPath();
            ctx.arc(canvasX1, canvasY1, 4, 0, 2 * Math.PI);
            ctx.fill();
            ctx.beginPath();
            ctx.arc(canvasX2, canvasY2, 4, 0, 2 * Math.PI);
            ctx.fill();
        }

        // Draw slope triangle if enabled
        if (showSlope && m !== 0) {
            ctx.strokeStyle = '#EF4444';
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);

            // Draw a slope triangle
            const triangleX = 2;
            const triangleY = m * triangleX + c;
            const triangleCanvasX = toCanvasX(triangleX);
            const triangleCanvasY = toCanvasY(triangleY);

            // Vertical line
            ctx.beginPath();
            ctx.moveTo(triangleCanvasX, triangleCanvasY);
            ctx.lineTo(triangleCanvasX, triangleCanvasY - m * xScale);
            ctx.stroke();

            // Horizontal line
            ctx.beginPath();
            ctx.moveTo(triangleCanvasX, triangleCanvasY - m * xScale);
            ctx.lineTo(triangleCanvasX + xScale, triangleCanvasY - m * xScale);
            ctx.stroke();

            ctx.setLineDash([]);

            // Label the slope
            ctx.fillStyle = '#EF4444';
            ctx.font = 'bold 12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`m = ${m}`, triangleCanvasX + xScale/2, triangleCanvasY - m * xScale - 10);
        }

        // Draw y-intercept if enabled
        if (showYIntercept) {
            const yInterceptX = 0;
            const yInterceptY = c;
            const yInterceptCanvasX = toCanvasX(yInterceptX);
            const yInterceptCanvasY = toCanvasY(yInterceptY);

            if (yInterceptCanvasY >= 0 && yInterceptCanvasY <= height) {
                ctx.fillStyle = '#10B981';
                ctx.beginPath();
                ctx.arc(yInterceptCanvasX, yInterceptCanvasY, 6, 0, 2 * Math.PI);
                ctx.fill();

                ctx.fillStyle = '#10B981';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'left';
                ctx.fillText(`(0, ${c})`, yInterceptCanvasX + 10, yInterceptCanvasY - 10);
            }
        }

        // Draw x-intercept if enabled
        if (showXIntercept && m !== 0) {
            const xInterceptX = -c / m;
            const xInterceptY = 0;
            const xInterceptCanvasX = toCanvasX(xInterceptX);
            const xInterceptCanvasY = toCanvasY(xInterceptY);

            if (xInterceptCanvasX >= 0 && xInterceptCanvasX <= width) {
                ctx.fillStyle = '#F59E0B';
                ctx.beginPath();
                ctx.arc(xInterceptCanvasX, xInterceptCanvasY, 6, 0, 2 * Math.PI);
                ctx.fill();

                ctx.fillStyle = '#F59E0B';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`(${xInterceptX.toFixed(2)}, 0)`, xInterceptCanvasX, xInterceptCanvasY - 15);
            }
        }

        // Draw axis labels
        ctx.fillStyle = '#000000'; // Black labels
        ctx.font = 'bold 14px Arial';
        
        // Y label - shifted to the right
        ctx.textAlign = 'left';
        ctx.fillText('Y', width / 2 + 15, height - 10);
        
        // X label - shifted up and rotated 90 degrees
        ctx.save();
        ctx.translate(20, height / 2 - 15);
        ctx.rotate(-Math.PI / 2);
        ctx.textAlign = 'center';
        ctx.fillText('X', 0, 0);
        ctx.restore();

        // Draw title
        ctx.font = 'bold 16px Arial';
        ctx.fillText(graphData.title, width / 2, 25);
    };

    const handleInputChange = (field, value) => {
        setGraphData(prev => ({
            ...prev,
            [field]: field === 'm' || field === 'c' || field === 'xIntercept' ? parseFloat(value) || 0 : value
        }));
    };

    const handleToggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    const handleOpenFullScreen = () => {
        setIsFullScreenOpen(true);
        setIsFullScreen(true); // Skip intermediate step - go directly to full screen
        // Redraw the graph in full-screen canvas after modal opens
        setTimeout(() => {
            if (fullScreenCanvasRef.current) {
                drawGraph(fullScreenCanvasRef.current);
            }
        }, 100);
    };

    const handleCloseFullScreen = () => {
        setIsFullScreenOpen(false);
    };

    // Parameter Panel Component
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Linear Function Parameters</h3>
            
            {/* Edit Mode Toggle */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Edit Mode</h4>
                <div className="flex space-x-2">
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="parameters"
                            checked={graphData.editMode === 'parameters'}
                            onChange={(e) => handleInputChange('editMode', e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Parameters</span>
                    </label>
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="equation"
                            checked={graphData.editMode === 'equation'}
                            onChange={(e) => handleInputChange('editMode', e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Equation</span>
                    </label>
                </div>
            </div>

            {/* Equation Editor */}
            {graphData.editMode === 'equation' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Equation:</label>
                        <input
                            type="text"
                            value={graphData.equation}
                            onChange={(e) => handleEquationChange(e.target.value)}
                            placeholder="e.g., 2x + 3, y = -x + 5"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                            disabled={isSubmitted}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                            Format: mx + c or y = mx + c
                        </p>
                    </div>
                </div>
            )}

            {/* Parameter Editor */}
            {graphData.editMode === 'parameters' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                        <input
                            type="text"
                            value={graphData.title}
                            onChange={(e) => handleInputChange('title', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Slope (m):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={graphData.m}
                            onChange={(e) => handleInputChange('m', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Y-Intercept (c):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={graphData.c}
                            onChange={(e) => handleInputChange('c', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">X-Intercept:</label>
                        <input
                            type="number"
                            step="0.1"
                            value={graphData.xIntercept}
                            onChange={(e) => handleXInterceptChange(parseFloat(e.target.value) || 0)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted || graphData.m === 0}
                        />
                        {graphData.m === 0 && (
                            <p className="text-xs text-gray-500 mt-1">
                                X-intercept not available for horizontal lines
                            </p>
                        )}
                    </div>
                </div>
            )}

            {/* Range Settings */}
            <div className="space-y-4">
                <h4 className="font-medium text-gray-700">Range Settings</h4>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Min:</label>
                        <input
                            type="number"
                            step="1"
                            value={graphData.x_range[0]}
                            onChange={(e) => handleInputChange('x_range', [parseFloat(e.target.value) || -10, graphData.x_range[1]])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Max:</label>
                        <input
                            type="number"
                            step="1"
                            value={graphData.x_range[1]}
                            onChange={(e) => handleInputChange('x_range', [graphData.x_range[0], parseFloat(e.target.value) || 10])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Y Min:</label>
                        <input
                            type="number"
                            step="1"
                            value={graphData.y_range[0]}
                            onChange={(e) => handleInputChange('y_range', [parseFloat(e.target.value) || -20, graphData.y_range[1]])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Y Max:</label>
                        <input
                            type="number"
                            step="1"
                            value={graphData.y_range[1]}
                            onChange={(e) => handleInputChange('y_range', [graphData.y_range[0], parseFloat(e.target.value) || 20])}
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
                        checked={graphData.showGrid}
                        onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={graphData.showPoints}
                        onChange={(e) => handleInputChange('showPoints', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Points</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={graphData.showSlope}
                        onChange={(e) => handleInputChange('showSlope', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Slope</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={graphData.showYIntercept}
                        onChange={(e) => handleInputChange('showYIntercept', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Y-Intercept</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={graphData.showXIntercept}
                        onChange={(e) => handleInputChange('showXIntercept', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show X-Intercept</span>
                </label>
            </div>

            {/* Line Color */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                <input
                    type="color"
                    value={graphData.lineColor}
                    onChange={(e) => handleInputChange('lineColor', e.target.value)}
                    className="w-full h-10 border border-gray-300 rounded-md"
                    disabled={isSubmitted}
                />
            </div>

            {/* Function Information */}
            <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                <h4 className="font-medium text-blue-800 mb-2">Function Information</h4>
                <div className="space-y-1 text-sm">
                    <div><strong>Equation:</strong> y = {graphData.m}x {graphData.c >= 0 ? '+' : ''}{graphData.c}</div>
                    <div><strong>Slope (m):</strong> {graphData.m}</div>
                    <div><strong>Y-Intercept (c):</strong> {graphData.c}</div>
                    {graphData.m !== 0 && (
                        <div><strong>X-Intercept:</strong> {(graphData.xIntercept || 0).toFixed(2)}</div>
                    )}
                </div>
            </div>
        </div>
    );

    return (
        <div className="relative overflow-hidden">
            <div className="relative group border border-gray-200 rounded overflow-hidden">
                {/* Hover-reveal controls overlay */}
                <div className="absolute top-0 left-0 right-0 z-10 bg-white/95 backdrop-blur-sm border-b border-gray-200 px-3 py-2 opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-opacity duration-150 overflow-hidden">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            {/* Edit Mode Toggle (compact) */}
                            <div className="flex items-center gap-3">
                                <label className="flex items-center text-xs text-gray-700">
                                    <input type="radio" value="parameters" checked={graphData.editMode === 'parameters'} onChange={(e) => handleInputChange('editMode', e.target.value)} className="mr-1" disabled={isSubmitted} />
                                    Parameters
                                </label>
                                <label className="flex items-center text-xs text-gray-700">
                                    <input type="radio" value="equation" checked={graphData.editMode === 'equation'} onChange={(e) => handleInputChange('editMode', e.target.value)} className="mr-1" disabled={isSubmitted} />
                                    Equation
                                </label>
                            </div>
                        </div>
                        {!isConfigMode && (
                            <button onClick={handleOpenFullScreen} className="p-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded transition-colors" title="Full screen">
                                <Maximize2 size={16} />
                            </button>
                        )}
                    </div>

                    {/* Compact Controls */}
                    {graphData.editMode === 'parameters' ? (
                        <div className="grid grid-cols-4 gap-2 mt-2">
                            <input type="number" step="0.1" value={graphData.m} onChange={(e) => handleInputChange('m', e.target.value)} className="px-2 py-1 border border-gray-300 rounded text-xs" placeholder="Slope m" disabled={isSubmitted} />
                            <input type="number" step="0.1" value={graphData.c} onChange={(e) => handleInputChange('c', e.target.value)} className="px-2 py-1 border border-gray-300 rounded text-xs" placeholder="Y-int c" disabled={isSubmitted} />
                            <input type="number" step="0.1" value={graphData.xIntercept || 0} onChange={(e) => handleXInterceptChange(parseFloat(e.target.value) || 0)} className="px-2 py-1 border border-gray-300 rounded text-xs" placeholder="X-int" disabled={isSubmitted || graphData.m === 0} />
                            <input type="color" value={graphData.lineColor} onChange={(e) => handleInputChange('lineColor', e.target.value)} className="h-8 w-full border border-gray-300 rounded" disabled={isSubmitted} />
                        </div>
                    ) : (
                        <div className="mt-2">
                            <input type="text" value={graphData.equation} onChange={(e) => handleEquationChange(e.target.value)} placeholder="y = mx + c" className="w-full px-2 py-1 border border-gray-300 rounded text-xs font-mono" disabled={isSubmitted} />
                        </div>
                    )}

                    {/* Compact function info */}
                    <div className="mt-2 text-[11px] text-blue-700">
                        y = {graphData.m}x {graphData.c >= 0 ? '+' : ''}{graphData.c}{graphData.m !== 0 ? ` • x-int ${(graphData.xIntercept || 0).toFixed(2)}` : ''}
                    </div>
                </div>

                {/* subtle peek bar */}
                <div className="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-b from-white/60 to-transparent z-0 pointer-events-none"></div>

                {/* Graph Canvas */}
                <div className="overflow-hidden rounded">
                    <canvas ref={canvasRef} width={800} height={600} className="w-full h-[calc(100vh-10rem)]" />
                </div>
            </div>

            {/* Full Screen Modal */}
            {!isConfigMode && (
                <FullScreenModal
                    isOpen={isFullScreenOpen}
                    onClose={handleCloseFullScreen}
                    title="Linear Function Graph - Full Screen Mode"
                    onToggleFullScreen={handleToggleFullScreen}
                    isFullScreen={isFullScreen}
                    hideFullScreenToggle={true}
                    parameterPanel={<ParameterPanel />}
                >
                    <div className="h-full flex items-center justify-center">
                        <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                            <canvas ref={fullScreenCanvasRef} width={800} height={600} className="w-full h-auto" />
                        </div>
                    </div>
                </FullScreenModal>
            )}
        </div>
    );
};

export default LinearFunctionGraph;
