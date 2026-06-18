import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const CoordinatePlaneInput = ({ initialData, onChange, isSubmitted }) => {
    const [planeData, setPlaneData] = useState(initialData || {
        title: "Coordinate Plane",
        xMin: -10,
        xMax: 10,
        yMin: -10,
        yMax: 10,
        gridSpacing: 1,
        showGrid: true,
        showAxes: true,
        showLabels: true,
        points: [],
        functions: [],
        shapes: [],
        color: '#3B82F6'
    });

    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [currentTool, setCurrentTool] = useState('point'); // 'point', 'function', 'shape'
    const [selectedPoint, setSelectedPoint] = useState(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    useEffect(() => {
        if (onChange) {
            onChange(planeData);
        }
    }, [planeData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawCanvas();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [planeData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawCanvas();
    }, []);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({ ...prev, [field]: value }));
    };

    const addPoint = (x, y, label = '') => {
        if (isSubmitted) return;
        const newPoint = {
            id: Date.now(),
            x: parseFloat(x),
            y: parseFloat(y),
            label: label || `(${x}, ${y})`,
            color: planeData.color
        };
        setPlaneData(prev => ({
            ...prev,
            points: [...(prev.points || []), newPoint]
        }));
        return newPoint;
    };

    const addFunction = (expression, color = planeData.color) => {
        if (isSubmitted) return;
        const newFunction = {
            id: Date.now(),
            expression,
            color,
            visible: true
        };
        setPlaneData(prev => ({
            ...prev,
            functions: [...(prev.functions || []), newFunction]
        }));
    };

    const addShape = (type, points, color = planeData.color) => {
        if (isSubmitted) return;
        const newShape = {
            id: Date.now(),
            type, // 'line', 'triangle', 'rectangle', 'circle'
            points,
            color,
            visible: true
        };
        setPlaneData(prev => ({
            ...prev,
            shapes: [...(prev.shapes || []), newShape]
        }));
    };

    const removePoint = (pointId) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({
            ...prev,
            points: (prev.points || []).filter(p => p.id !== pointId)
        }));
    };

    const removeFunction = (functionId) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({
            ...prev,
            functions: (prev.functions || []).filter(f => f.id !== functionId)
        }));
    };

    const removeShape = (shapeId) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({
            ...prev,
            shapes: (prev.shapes || []).filter(s => s.id !== shapeId)
        }));
    };

    const updatePoint = (pointId, field, value) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({
            ...prev,
            points: (prev.points || []).map(p => 
                p.id === pointId ? { ...p, [field]: value } : p
            )
        }));
    };

    const updateFunction = (functionId, field, value) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({
            ...prev,
            functions: (prev.functions || []).map(f => 
                f.id === functionId ? { ...f, [field]: value } : f
            )
        }));
    };

    const updateShape = (shapeId, field, value) => {
        if (isSubmitted) return;
        setPlaneData(prev => ({
            ...prev,
            shapes: (prev.shapes || []).map(s => 
                s.id === shapeId ? { ...s, [field]: value } : s
            )
        }));
    };

    const canvasToCoord = (canvasX, canvasY) => {
        const canvas = canvasRef.current;
        if (!canvas) return { x: 0, y: 0 };
        
        const rect = canvas.getBoundingClientRect();
        const x = ((canvasX - rect.left) / rect.width) * (planeData.xMax - planeData.xMin) + planeData.xMin;
        const y = planeData.yMax - ((canvasY - rect.top) / rect.height) * (planeData.yMax - planeData.yMin);
        
        return { x, y };
    };

    const coordToCanvas = (x, y) => {
        const canvas = canvasRef.current;
        if (!canvas) return { x: 0, y: 0 };
        
        const rect = canvas.getBoundingClientRect();
        const canvasX = ((x - planeData.xMin) / (planeData.xMax - planeData.xMin)) * rect.width;
        const canvasY = ((planeData.yMax - y) / (planeData.yMax - planeData.yMin)) * rect.height;
        
        return { x: canvasX, y: canvasY };
    };

    const evaluateFunction = (expression, x) => {
        try {
            // Simple function evaluation - can be extended for more complex expressions
            const safeExpression = expression
                .replace(/x/g, `(${x})`)
                .replace(/sin/g, 'Math.sin')
                .replace(/cos/g, 'Math.cos')
                .replace(/tan/g, 'Math.tan')
                .replace(/sqrt/g, 'Math.sqrt')
                .replace(/pow/g, 'Math.pow')
                .replace(/log/g, 'Math.log')
                .replace(/exp/g, 'Math.exp');
            
            return eval(safeExpression);
        } catch (error) {
            return null;
        }
    };

    const drawCanvas = () => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.log('CoordinatePlaneInput: Canvas not found');
            return;
        }
        
        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('CoordinatePlaneInput: Canvas context not available');
            return;
        }
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set canvas size
        canvas.width = 600;
        canvas.height = 400;
        
        // Draw grid
        if (planeData.showGrid) {
            ctx.strokeStyle = '#D1D5DB'; // Subtle grey grid lines
            ctx.lineWidth = 1;
            
            // Vertical grid lines
            for (let x = planeData.xMin; x <= planeData.xMax; x += planeData.gridSpacing) {
                const canvasX = coordToCanvas(x, 0).x;
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, canvas.height);
                ctx.stroke();
            }
            
            // Horizontal grid lines
            for (let y = planeData.yMin; y <= planeData.yMax; y += planeData.gridSpacing) {
                const canvasY = coordToCanvas(0, y).y;
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(canvas.width, canvasY);
                ctx.stroke();
            }
        }
        
        // Draw axes
        if (planeData.showAxes) {
            ctx.strokeStyle = '#000000'; // Black bold axes
            ctx.lineWidth = 3;
            
            // X-axis
            const xAxisY = coordToCanvas(0, 0).y;
            ctx.beginPath();
            ctx.moveTo(0, xAxisY);
            ctx.lineTo(canvas.width, xAxisY);
            ctx.stroke();
            
            // Y-axis
            const yAxisX = coordToCanvas(0, 0).x;
            ctx.beginPath();
            ctx.moveTo(yAxisX, 0);
            ctx.lineTo(yAxisX, canvas.height);
            ctx.stroke();
        }
        
        // Draw axis labels
        if (planeData.showLabels) {
            ctx.fillStyle = '#000000'; // Black labels
            ctx.font = 'bold 12px Arial';
            ctx.textAlign = 'center';
            
            // X-axis labels
            for (let x = planeData.xMin; x <= planeData.xMax; x += planeData.gridSpacing) {
                if (x !== 0) {
                    const canvasX = coordToCanvas(x, 0).x;
                    const canvasY = coordToCanvas(0, 0).y + 15;
                    ctx.fillText(x.toString(), canvasX, canvasY);
                }
            }
            
            // Y-axis labels
            for (let y = planeData.yMin; y <= planeData.yMax; y += planeData.gridSpacing) {
                if (y !== 0) {
                    const canvasX = coordToCanvas(0, 0).x - 10;
                    const canvasY = coordToCanvas(0, y).y + 4;
                    ctx.fillText(y.toString(), canvasX, canvasY);
                }
            }
            
            // Origin label
            const originX = coordToCanvas(0, 0).x - 10;
            const originY = coordToCanvas(0, 0).y + 15;
            ctx.fillText('0', originX, originY);
        }
        
        // Draw functions
        (planeData.functions || []).forEach(func => {
            if (!func.visible) return;
            
            ctx.strokeStyle = func.color;
            ctx.lineWidth = 2;
            ctx.beginPath();
            
            let firstPoint = true;
            for (let x = planeData.xMin; x <= planeData.xMax; x += 0.1) {
                const y = evaluateFunction(func.expression, x);
                if (y !== null && y >= planeData.yMin && y <= planeData.yMax) {
                    const canvasPoint = coordToCanvas(x, y);
                    if (firstPoint) {
                        ctx.moveTo(canvasPoint.x, canvasPoint.y);
                        firstPoint = false;
                    } else {
                        ctx.lineTo(canvasPoint.x, canvasPoint.y);
                    }
                }
            }
            ctx.stroke();
        });
        
        // Draw shapes
        (planeData.shapes || []).forEach(shape => {
            if (!shape.visible) return;
            
            ctx.strokeStyle = shape.color;
            ctx.lineWidth = 2;
            ctx.fillStyle = shape.color + '20'; // Semi-transparent fill
            
            if (shape.type === 'line' && shape.points.length >= 2) {
                ctx.beginPath();
                const start = coordToCanvas(shape.points[0].x, shape.points[0].y);
                ctx.moveTo(start.x, start.y);
                shape.points.slice(1).forEach(point => {
                    const canvasPoint = coordToCanvas(point.x, point.y);
                    ctx.lineTo(canvasPoint.x, canvasPoint.y);
                });
                ctx.stroke();
            } else if (shape.type === 'triangle' && shape.points.length >= 3) {
                ctx.beginPath();
                const first = coordToCanvas(shape.points[0].x, shape.points[0].y);
                ctx.moveTo(first.x, first.y);
                shape.points.slice(1).forEach(point => {
                    const canvasPoint = coordToCanvas(point.x, point.y);
                    ctx.lineTo(canvasPoint.x, canvasPoint.y);
                });
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
            } else if (shape.type === 'rectangle' && shape.points.length >= 2) {
                const [p1, p2] = shape.points;
                const canvasP1 = coordToCanvas(p1.x, p1.y);
                const canvasP2 = coordToCanvas(p2.x, p2.y);
                
                const width = Math.abs(canvasP2.x - canvasP1.x);
                const height = Math.abs(canvasP2.y - canvasP1.y);
                const x = Math.min(canvasP1.x, canvasP2.x);
                const y = Math.min(canvasP1.y, canvasP2.y);
                
                ctx.fillRect(x, y, width, height);
                ctx.strokeRect(x, y, width, height);
            } else if (shape.type === 'circle' && shape.points.length >= 2) {
                const [center, radiusPoint] = shape.points;
                const canvasCenter = coordToCanvas(center.x, center.y);
                const canvasRadius = coordToCanvas(radiusPoint.x, radiusPoint.y);
                
                const radius = Math.sqrt(
                    Math.pow(canvasRadius.x - canvasCenter.x, 2) + 
                    Math.pow(canvasRadius.y - canvasCenter.y, 2)
                );
                
                ctx.beginPath();
                ctx.arc(canvasCenter.x, canvasCenter.y, radius, 0, 2 * Math.PI);
                ctx.fill();
                ctx.stroke();
            }
        });
        
        // Draw points
        (planeData.points || []).forEach(point => {
            const canvasPoint = coordToCanvas(point.x, point.y);
            
            // Point circle
            ctx.fillStyle = point.color;
            ctx.beginPath();
            ctx.arc(canvasPoint.x, canvasPoint.y, 4, 0, 2 * Math.PI);
            ctx.fill();
            
            // Point label
            if (planeData.showLabels) {
                ctx.fillStyle = '#000000'; // Black labels
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'left';
                ctx.fillText(point.label, canvasPoint.x + 8, canvasPoint.y - 8);
            }
        });
    };

    const handleCanvasClick = (e) => {
        if (isSubmitted) return;
        
        const canvas = canvasRef.current;
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const coord = canvasToCoord(x, y);
        
        if (currentTool === 'point') {
            addPoint(coord.x.toFixed(2), coord.y.toFixed(2));
        }
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

    // Parameter Panel Component
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Coordinate Plane Parameters</h3>
            
            {/* Configuration Section */}
            <div className="space-y-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={planeData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Coordinate Plane Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">X Range:</label>
                    <div className="flex space-x-2">
                        <input
                            type="number"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            value={planeData.xMin}
                            onChange={(e) => handleFieldChange('xMin', parseInt(e.target.value) || -10)}
                            disabled={isSubmitted}
                            placeholder="-10"
                        />
                        <span className="self-center text-gray-500">to</span>
                        <input
                            type="number"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            value={planeData.xMax}
                            onChange={(e) => handleFieldChange('xMax', parseInt(e.target.value) || 10)}
                            disabled={isSubmitted}
                            placeholder="10"
                        />
                    </div>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Y Range:</label>
                    <div className="flex space-x-2">
                        <input
                            type="number"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            value={planeData.yMin}
                            onChange={(e) => handleFieldChange('yMin', parseInt(e.target.value) || -10)}
                            disabled={isSubmitted}
                            placeholder="-10"
                        />
                        <span className="self-center text-gray-500">to</span>
                        <input
                            type="number"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            value={planeData.yMax}
                            onChange={(e) => handleFieldChange('yMax', parseInt(e.target.value) || 10)}
                            disabled={isSubmitted}
                            placeholder="10"
                        />
                    </div>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Grid Spacing:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={planeData.gridSpacing}
                        onChange={(e) => handleFieldChange('gridSpacing', parseInt(e.target.value) || 1)}
                        disabled={isSubmitted}
                        placeholder="1"
                        min="0.5"
                        step="0.5"
                    />
                </div>
            </div>

            {/* Options */}
            <div className="space-y-2">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={planeData.showGrid}
                        onChange={(e) => handleFieldChange('showGrid', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={planeData.showAxes}
                        onChange={(e) => handleFieldChange('showAxes', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Axes</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={planeData.showLabels}
                        onChange={(e) => handleFieldChange('showLabels', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Labels</span>
                </label>
            </div>

            {/* Tools */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Current Tool:</label>
                <div className="space-y-2">
                    {['point', 'function', 'shape'].map((tool) => (
                        <label key={tool} className="flex items-center">
                            <input
                                type="radio"
                                name="tool"
                                className="mr-2"
                                checked={currentTool === tool}
                                onChange={() => setCurrentTool(tool)}
                                disabled={isSubmitted}
                            />
                            <span className="text-sm text-gray-700 capitalize">{tool}</span>
                        </label>
                    ))}
                </div>
            </div>

            {/* Function Input */}
            {currentTool === 'function' && (
                <div>
                    <div className="flex space-x-2">
                        <input
                            type="text"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            placeholder="Enter function (e.g., x^2, sin(x), 2*x+1)"
                            onKeyPress={(e) => {
                                if (e.key === 'Enter' && !isSubmitted) {
                                    addFunction(e.target.value);
                                    e.target.value = '';
                                }
                            }}
                            disabled={isSubmitted}
                        />
                        {!isSubmitted && (
                            <button
                                onClick={(e) => {
                                    const input = e.target.previousSibling;
                                    if (input.value.trim()) {
                                        addFunction(input.value.trim());
                                        input.value = '';
                                    }
                                }}
                                className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm hover:bg-blue-600"
                            >
                                Add
                            </button>
                        )}
                    </div>
                </div>
            )}

            {/* Points Management */}
            <div>
                <h4 className="font-semibold text-gray-700 mb-2">Points ({planeData.points?.length || 0}):</h4>
                {(planeData.points?.length || 0) === 0 ? (
                    <p className="text-sm text-gray-500 italic">No points added yet. Click on the coordinate plane to add points.</p>
                ) : (
                    <div className="space-y-2 max-h-40 overflow-y-auto">
                        {(planeData.points || []).map((point) => (
                            <div key={point.id} className="flex items-center space-x-2 p-2 bg-white border border-gray-200 rounded-md">
                                <input
                                    type="number"
                                    className="w-16 p-1 border border-gray-300 rounded text-sm"
                                    value={point.x}
                                    onChange={(e) => updatePoint(point.id, 'x', parseFloat(e.target.value) || 0)}
                                    disabled={isSubmitted}
                                    step="any"
                                />
                                <span className="text-gray-500">,</span>
                                <input
                                    type="number"
                                    className="w-16 p-1 border border-gray-300 rounded text-sm"
                                    value={point.y}
                                    onChange={(e) => updatePoint(point.id, 'y', parseFloat(e.target.value) || 0)}
                                    disabled={isSubmitted}
                                    step="any"
                                />
                                <input
                                    type="text"
                                    className="flex-1 p-1 border border-gray-300 rounded text-sm"
                                    value={point.label}
                                    onChange={(e) => updatePoint(point.id, 'label', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Label"
                                />
                                {!isSubmitted && (
                                    <button
                                        onClick={() => removePoint(point.id)}
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

            {/* Functions Management */}
            {(planeData.functions?.length || 0) > 0 && (
                <div>
                    <h4 className="font-semibold text-gray-700 mb-2">Functions ({planeData.functions?.length || 0}):</h4>
                    <div className="space-y-2">
                        {(planeData.functions || []).map((func) => (
                            <div key={func.id} className="flex items-center space-x-2 p-2 bg-white border border-gray-200 rounded-md">
                                <input
                                    type="text"
                                    className="flex-1 p-1 border border-gray-300 rounded text-sm"
                                    value={func.expression}
                                    onChange={(e) => updateFunction(func.id, 'expression', e.target.value)}
                                    disabled={isSubmitted}
                                />
                                <input
                                    type="color"
                                    className="w-8 h-8 border border-gray-300 rounded"
                                    value={func.color}
                                    onChange={(e) => updateFunction(func.id, 'color', e.target.value)}
                                    disabled={isSubmitted}
                                />
                                {!isSubmitted && (
                                    <button
                                        onClick={() => removeFunction(func.id)}
                                        className="text-red-600 hover:text-red-800 text-lg font-bold"
                                    >
                                        ×
                                    </button>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );

    return (
        <div className="relative">
            <div className="p-4 bg-white border border-gray-300 rounded-lg mt-4">
                <div className="flex items-center justify-between mb-4">
                    <h3 className="font-semibold text-gray-700">Coordinate Plane</h3>
                    <button
                        onClick={handleOpenFullScreen}
                        className="p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow-lg transition-colors"
                        title="Open Full Screen Mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>
            
            {/* Quick Controls */}
            <div className="grid grid-cols-2 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Grid Spacing:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={planeData.gridSpacing}
                        onChange={(e) => handleFieldChange('gridSpacing', parseInt(e.target.value) || 1)}
                        disabled={isSubmitted}
                        placeholder="1"
                        min="0.5"
                        step="0.5"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Current Tool:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={currentTool}
                        onChange={(e) => setCurrentTool(e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="point">Point</option>
                        <option value="function">Function</option>
                        <option value="shape">Shape</option>
                    </select>
                </div>
            </div>

            {/* Coordinate Plane Canvas */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Coordinate Plane:</label>
                <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                    <canvas
                        ref={canvasRef}
                        width={600}
                        height={400}
                        onClick={handleCanvasClick}
                        className="cursor-crosshair bg-white"
                        style={{ maxWidth: '100%', height: 'auto' }}
                    />
                </div>
            </div>

            {/* Function Input */}
            {currentTool === 'function' && (
                <div className="mb-4">
                    <div className="flex space-x-2">
                        <input
                            type="text"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                            placeholder="Enter function (e.g., x^2, sin(x), 2*x+1)"
                            onKeyPress={(e) => {
                                if (e.key === 'Enter' && !isSubmitted) {
                                    addFunction(e.target.value);
                                    e.target.value = '';
                                }
                            }}
                            disabled={isSubmitted}
                        />
                        {!isSubmitted && (
                            <button
                                onClick={(e) => {
                                    const input = e.target.previousSibling;
                                    if (input.value.trim()) {
                                        addFunction(input.value.trim());
                                        input.value = '';
                                    }
                                }}
                                className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm hover:bg-blue-600"
                            >
                                Add
                            </button>
                        )}
                    </div>
                </div>
            )}

            {/* Quick Stats */}
            <div className="text-sm text-gray-600 mb-4">
                <p>Points: {planeData.points?.length || 0} | Functions: {planeData.functions?.length || 0}</p>
            </div>

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Quick Start:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Click the full-screen button for detailed controls</li>
                    <li>Click on the plane to add points</li>
                    <li>Use the function tool to plot equations</li>
                </ul>
            </div>

            {/* Full Screen Modal */}
            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title="Coordinate Plane - Full Screen Mode"
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
                            onClick={handleCanvasClick}
                            className="cursor-crosshair bg-white"
                            style={{ maxWidth: '100%', height: 'auto' }}
                        />
                    </div>
                </div>
            </FullScreenModal>
        </div>
        </div>
    );
};

export default CoordinatePlaneInput;
