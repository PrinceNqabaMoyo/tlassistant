import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';
import { useMathOperations } from '../../hooks/useMathOperations';

const LinearFunctionGraphMigrated = ({ initialData, onChange, isSubmitted }) => {
    const { calculate, loading, error } = useMathOperations();
    
    const [graphData, setGraphData] = useState(() => {
        const defaultData = {
            title: "Linear Function",
            m: 2,
            c: 3,
            xIntercept: -1.5,
            equation: "2x + 3",
            x_range: [-10, 10],
            y_range: [-20, 20],
            lineColor: '#3B82F6',
            showGrid: true,
            showPoints: true,
            showSlope: true,
            showYIntercept: true,
            showXIntercept: true,
            editMode: 'parameters'
        };
        
        if (initialData) {
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
    const [calculationResults, setCalculationResults] = useState({});

    // Parse equation string to extract m and c
    const parseEquation = (equation) => {
        try {
            const cleanEq = equation.replace(/\s/g, '').toLowerCase();
            
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

    // Use backend to calculate function values
    const calculateFunctionValues = async (m, c, xValues) => {
        try {
            const results = {};
            
            // Calculate y values for each x using backend
            for (const x of xValues) {
                const expression = `${m}*x + ${c}`;
                const result = await calculate('evaluate', expression, { x });
                results[x] = parseFloat(result.result);
            }
            
            return results;
        } catch (error) {
            console.error('Backend calculation failed, using frontend fallback:', error);
            // Fallback to frontend calculation
            const results = {};
            xValues.forEach(x => {
                results[x] = m * x + c;
            });
            return results;
        }
    };

    // Use backend to calculate intercepts
    const calculateIntercepts = async (m, c) => {
        try {
            // Calculate x-intercept: solve for x when y = 0
            if (m !== 0) {
                const xInterceptResult = await calculate('solve', `${m}*x + ${c} = 0`);
                const xIntercept = parseFloat(xInterceptResult.result);
                
                return {
                    xIntercept,
                    yIntercept: c
                };
            } else {
                return {
                    xIntercept: null, // No x-intercept for horizontal line
                    yIntercept: c
                };
            }
        } catch (error) {
            console.error('Backend intercept calculation failed, using frontend fallback:', error);
            // Fallback to frontend calculation
            return {
                xIntercept: m !== 0 ? -c / m : null,
                yIntercept: c
            };
        }
    };

    // Update equation when m or c changes
    useEffect(() => {
        const newEquation = `${graphData.m}x ${graphData.c >= 0 ? '+' : ''}${graphData.c}`;
        setGraphData(prev => ({
            ...prev,
            equation: newEquation
        }));
    }, [graphData.m, graphData.c]);

    // Calculate intercepts when m or c changes
    useEffect(() => {
        const updateIntercepts = async () => {
            const intercepts = await calculateIntercepts(graphData.m, graphData.c);
            setGraphData(prev => ({
                ...prev,
                xIntercept: intercepts.xIntercept
            }));
        };
        
        updateIntercepts();
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

    useEffect(() => {
        if (onChange) {
            onChange(graphData);
        }
    }, [graphData, onChange]);

    useEffect(() => {
        const timer = setTimeout(() => {
            drawGraph();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [graphData, calculationResults]);

    // Initial draw when component mounts
    useEffect(() => {
        drawGraph();
    }, []);

    // Redraw full-screen canvas when modal opens or graphData changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            drawGraph(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, graphData, calculationResults]);

    const drawGraph = async (targetCanvas = null) => {
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

        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
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
            ctx.strokeStyle = '#D1D5DB';
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = x_range[0]; x <= x_range[1]; x++) {
                if (x === 0) continue;
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = y_range[0]; y <= y_range[1]; y++) {
                if (y === 0) continue;
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

        // Calculate function values using backend
        const x1 = x_range[0];
        const x2 = x_range[1];
        
        // Use cached results or calculate new ones
        let y1, y2;
        if (calculationResults[x1] !== undefined && calculationResults[x2] !== undefined) {
            y1 = calculationResults[x1];
            y2 = calculationResults[x2];
        } else {
            // Calculate using backend
            const results = await calculateFunctionValues(m, c, [x1, x2]);
            y1 = results[x1];
            y2 = results[x2];
            
            // Cache results
            setCalculationResults(prev => ({
                ...prev,
                [x1]: y1,
                [x2]: y2
            }));
        }

        // Draw the linear function
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 3;
        ctx.beginPath();

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
        if (showXIntercept && m !== 0 && graphData.xIntercept !== null) {
            const xInterceptX = graphData.xIntercept;
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
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('X', width / 2, height - 10);
        
        ctx.save();
        ctx.translate(20, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Y', 0, 0);
        ctx.restore();

        // Draw title
        ctx.font = 'bold 16px Arial';
        ctx.fillText(graphData.title, width / 2, 25);

        // Show loading indicator if backend is calculating
        if (loading) {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
            ctx.fillRect(0, 0, width, height);
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('Calculating...', width / 2, height / 2);
        }

        // Show error if backend calculation failed
        if (error) {
            ctx.fillStyle = 'rgba(255, 0, 0, 0.1)';
            ctx.fillRect(0, 0, width, height);
            ctx.fillStyle = '#ff0000';
            ctx.font = 'bold 12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('Backend Error - Using Frontend Fallback', width / 2, height - 20);
        }
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

            {graphData.editMode === 'parameters' ? (
                <>
                    {/* Slope (m) */}
                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-gray-700">
                            Slope (m)
                        </label>
                        <input
                            type="number"
                            value={graphData.m}
                            onChange={(e) => handleInputChange('m', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            step="0.1"
                            disabled={isSubmitted}
                        />
                    </div>

                    {/* Y-intercept (c) */}
                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-gray-700">
                            Y-intercept (c)
                        </label>
                        <input
                            type="number"
                            value={graphData.c}
                            onChange={(e) => handleInputChange('c', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            step="0.1"
                            disabled={isSubmitted}
                        />
                    </div>

                    {/* X-intercept */}
                    {graphData.m !== 0 && (
                        <div className="space-y-2">
                            <label className="block text-sm font-medium text-gray-700">
                                X-intercept
                            </label>
                            <input
                                type="number"
                                value={graphData.xIntercept}
                                onChange={(e) => handleXInterceptChange(parseFloat(e.target.value) || 0)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                step="0.1"
                                disabled={isSubmitted}
                            />
                        </div>
                    )}
                </>
            ) : (
                /* Equation Input */
                <div className="space-y-2">
                    <label className="block text-sm font-medium text-gray-700">
                        Equation
                    </label>
                    <input
                        type="text"
                        value={graphData.equation}
                        onChange={(e) => handleEquationChange(e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="e.g., 2x + 3"
                        disabled={isSubmitted}
                    />
                </div>
            )}

            {/* Display Options */}
            <div className="space-y-3">
                <h4 className="font-medium text-gray-700">Display Options</h4>
                
                <div className="space-y-2">
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
                        <span className="text-sm text-gray-700">Show Slope Triangle</span>
                    </label>
                    
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={graphData.showYIntercept}
                            onChange={(e) => handleInputChange('showYIntercept', e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Show Y-intercept</span>
                    </label>
                    
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={graphData.showXIntercept}
                            onChange={(e) => handleInputChange('showXIntercept', e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Show X-intercept</span>
                    </label>
                </div>
            </div>

            {/* Backend Status */}
            <div className="mt-4 p-3 bg-gray-50 rounded-lg">
                <h4 className="font-medium text-gray-700 mb-2">Backend Status</h4>
                {loading && (
                    <div className="text-blue-600 text-sm">🔄 Calculating with backend...</div>
                )}
                {error && (
                    <div className="text-red-600 text-sm">⚠️ Backend error - using frontend fallback</div>
                )}
                {!loading && !error && (
                    <div className="text-green-600 text-sm">✅ Backend calculations active</div>
                )}
            </div>
        </div>
    );

    return (
        <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-bold text-gray-800">Linear Function Graph</h2>
                <button
                    onClick={handleOpenFullScreen}
                    className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors"
                    title="Open in full screen"
                >
                    <Maximize2 size={20} />
                </button>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Graph Canvas */}
                <div className="lg:col-span-2">
                    <div className="border border-gray-200 rounded-lg overflow-hidden">
                        <canvas
                            ref={canvasRef}
                            width={600}
                            height={400}
                            className="w-full h-auto"
                        />
                    </div>
                </div>

                {/* Parameter Panel */}
                <div className="lg:col-span-1">
                    <ParameterPanel />
                </div>
            </div>

            {/* Full Screen Modal */}
            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title="Linear Function Graph - Full Screen"
            >
                <div className="w-full h-full flex items-center justify-center">
                    <canvas
                        ref={fullScreenCanvasRef}
                        width={800}
                        height={600}
                        className="border border-gray-200 rounded-lg"
                    />
                </div>
            </FullScreenModal>
        </div>
    );
};

export default LinearFunctionGraphMigrated;
