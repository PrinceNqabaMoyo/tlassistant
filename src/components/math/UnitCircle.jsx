import React, { useState, useEffect, useRef, useCallback } from 'react';
import { RotateCcw, Maximize2, Minus, Plus } from 'lucide-react';

const UnitCircle = ({ 
    initialData = {}, 
    isCompact = false, 
    currentAngle = null,
    onChange = null 
}) => {
    const canvasRef = useRef(null);
    const [angle, setAngle] = useState(initialData.angle || 0);
    const [showValues, setShowValues] = useState(initialData.showValues !== false);
    const [showGrid, setShowGrid] = useState(initialData.showGrid !== false);
    const [showLabels, setShowLabels] = useState(initialData.showLabels !== false);
    const [zoom, setZoom] = useState(initialData.zoom || 1);
    const [isDragging, setIsDragging] = useState(false);
    const [lastMousePos, setLastMousePos] = useState({ x: 0, y: 0 });

    // Use currentAngle prop if provided (for graph view integration)
    const displayAngle = currentAngle !== null ? currentAngle : angle;

    // Convert angle to radians
    const angleRad = (displayAngle * Math.PI) / 180;
    
    // Calculate coordinates (reflected about x-axis)
    const x = Math.cos(angleRad);
    const y = -Math.sin(angleRad); // Negative to reflect about x-axis
    
    // Calculate trigonometric values (note: sin is reflected)
    const sinValue = -y; // Reflect back to get correct sin value
    const cosValue = x;
    const tanValue = sinValue !== 0 ? sinValue / cosValue : 'undefined';

    // Determine quadrant (for reflected coordinate system)
    const getQuadrant = (deg) => {
        // Normalize angle to 0-360 range
        const normalizedDeg = ((deg % 360) + 360) % 360;
        
        // In reflected system: 0-180° is top half, 180-360° is bottom half
        if (normalizedDeg >= 0 && normalizedDeg < 90) return 'I';      // Top right
        if (normalizedDeg >= 90 && normalizedDeg < 180) return 'II';   // Top left
        if (normalizedDeg >= 180 && normalizedDeg < 270) return 'III'; // Bottom left
        if (normalizedDeg >= 270 && normalizedDeg < 360) return 'IV';  // Bottom right
        return 'I'; // Default case
    };

    const quadrant = getQuadrant(displayAngle);

    // Handle angle change
    const handleAngleChange = (newAngle) => {
        const normalizedAngle = ((newAngle % 360) + 360) % 360;
        setAngle(normalizedAngle);
        
        if (onChange) {
            onChange({ angle: normalizedAngle, x: Math.cos(normalizedAngle * Math.PI / 180), y: Math.sin(normalizedAngle * Math.PI / 180) });
        }
    };

    // Handle canvas click to set angle
    const handleCanvasClick = (event) => {
        if (isCompact) return; // Disable in compact mode
        
        const canvas = canvasRef.current;
        if (!canvas) return;
        
        const rect = canvas.getBoundingClientRect();
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const clickX = event.clientX - rect.left - centerX;
        const clickY = event.clientY - rect.top - centerY;
        
        // Calculate angle from click position (for reflected system)
        const newAngle = (Math.atan2(-clickY, clickX) * 180 / Math.PI + 360) % 360;
        
        // Only update if click is within reasonable distance from circle
        const distance = Math.sqrt(clickX * clickX + clickY * clickY);
        const radius = Math.min(rect.width, rect.height) * 0.35;
        
        if (Math.abs(distance - radius) < radius * 0.3) {
            handleAngleChange(newAngle);
        }
    };

    // Handle mouse drag for angle adjustment
    const handleMouseDown = (event) => {
        if (isCompact) return;
        setIsDragging(true);
        setLastMousePos({ x: event.clientX, y: event.clientY });
    };

    const handleMouseMove = (event) => {
        if (!isDragging || isCompact) return;
        
        const canvas = canvasRef.current;
        if (!canvas) return;
        
        const rect = canvas.getBoundingClientRect();
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        // Calculate mouse position relative to canvas center
        const mouseX = event.clientX - rect.left - centerX;
        const mouseY = event.clientY - rect.top - centerY;
        
        // Calculate angle from mouse position (for reflected system)
        const newAngle = (Math.atan2(-mouseY, mouseX) * 180 / Math.PI + 360) % 360;
        
        // Update angle smoothly (with throttling for performance)
        if (Math.abs(newAngle - angle) > 0.5) { // Only update if change is significant
            handleAngleChange(newAngle);
        }
    };

    const handleMouseUp = () => {
        setIsDragging(false);
    };

    // Draw the unit circle
    const drawUnitCircle = useCallback(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) * 0.35 * zoom;
        
        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        
        // Draw grid if enabled
        if (showGrid) {
            ctx.strokeStyle = '#e5e7eb';
            ctx.lineWidth = 1;
            
            // Vertical lines
            for (let x = centerX % 20; x < width; x += 20) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, height);
                ctx.stroke();
            }
            
            // Horizontal lines
            for (let y = centerY % 20; y < height; y += 20) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(width, y);
                ctx.stroke();
            }
        }
        
        // Draw axes
        ctx.strokeStyle = '#6b7280';
        ctx.lineWidth = 2;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(0, centerY);
        ctx.lineTo(width, centerY);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(centerX, 0);
        ctx.lineTo(centerX, height);
        ctx.stroke();
        
        // Draw unit circle
        ctx.strokeStyle = '#3b82f6';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
        ctx.stroke();
        
        // Draw angle markers (using reflected coordinates)
        if (showLabels) {
            ctx.fillStyle = '#6b7280';
            ctx.font = `${12 * zoom}px Arial`;
            ctx.textAlign = 'center';
            
            const markerRadius = radius + 20;
            for (let i = 0; i < 360; i += 30) {
                const markerAngle = (i * Math.PI) / 180;
                const markerX = centerX + Math.cos(markerAngle) * markerRadius;
                const markerY = centerY - Math.sin(markerAngle) * markerRadius; // Negative to reflect
                
                ctx.fillText(`${i}°`, markerX, markerY + 4);
            }
        }
        
        // Draw third outer circle for special angle coordinates
        if (showLabels) {
            ctx.strokeStyle = '#f59e0b';
            ctx.lineWidth = 1;
            ctx.setLineDash([3, 3]);
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius + 40, 0, 2 * Math.PI);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // Show exact coordinates at special angles
            ctx.fillStyle = '#dc2626';
            ctx.font = `bold ${11 * zoom}px Arial`;
            ctx.textAlign = 'center';
            
            // Static coordinates - ALWAYS VISIBLE
            // 0° coordinates: (1, 0)
            const angle0 = (0 * Math.PI) / 180;
            const coord0X = centerX + Math.cos(angle0) * (radius + 40);
            const coord0Y = centerY - Math.sin(angle0) * (radius + 40);
            ctx.fillText('(1, 0)', coord0X, coord0Y + 4);
            
            // 30° coordinates: (√3/2, 1/2)
            const angle30 = (30 * Math.PI) / 180;
            const coord30X = centerX + Math.cos(angle30) * (radius + 40);
            const coord30Y = centerY - Math.sin(angle30) * (radius + 40);
            ctx.fillText('(√3/2, 1/2)', coord30X, coord30Y + 4);
            
            // 90° coordinates: (0, 1)
            const angle90 = (90 * Math.PI) / 180;
            const coord90X = centerX + Math.cos(angle90) * (radius + 40);
            const coord90Y = centerY - Math.sin(angle90) * (radius + 40);
            ctx.fillText('(0, 1)', coord90X, coord90Y + 4);
            
            // Dynamic coordinates that appear when dot reaches them
            const specialAngles = [
                { angle: 45, coords: '(√2/2, √2/2)' },
                { angle: 60, coords: '(1/2, √3/2)' },
                { angle: 120, coords: '(-1/2, √3/2)' },
                { angle: 135, coords: '(-√2/2, √2/2)' },
                { angle: 150, coords: '(-√3/2, 1/2)' },
                { angle: 180, coords: '(-1, 0)' },
                { angle: 210, coords: '(-√3/2, -1/2)' },
                { angle: 225, coords: '(-√2/2, -√2/2)' },
                { angle: 240, coords: '(-1/2, -√3/2)' },
                { angle: 270, coords: '(0, -1)' },
                { angle: 300, coords: '(1/2, -√3/2)' },
                { angle: 330, coords: '(√3/2, -1/2)' }
            ];
            
            specialAngles.forEach(({ angle, coords }) => {
                // Only show coordinates when dot is within ±1° of the special angle
                if (Math.abs(displayAngle - angle) < 1) {
                    const angleRad = (angle * Math.PI) / 180;
                    const coordX = centerX + Math.cos(angleRad) * (radius + 40);
                    const coordY = centerY - Math.sin(angleRad) * (radius + 40);
                    ctx.fillText(coords, coordX, coordY + 4);
                }
            });
        }
        
        // Draw current angle point (using reflected coordinates)
        const pointX = centerX + Math.cos(angleRad) * radius;
        const pointY = centerY - Math.sin(angleRad) * radius; // Negative to reflect about x-axis
        
        // Draw reference triangle
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        
        // Vertical line to x-axis (opposite side - y)
        ctx.beginPath();
        ctx.moveTo(pointX, pointY);
        ctx.lineTo(pointX, centerY);
        ctx.stroke();
        
        // Horizontal line to y-axis (adjacent side - x)
        ctx.beginPath();
        ctx.moveTo(pointX, centerY);
        ctx.lineTo(centerX, centerY);
        ctx.stroke();
        
        // Hypotenuse (radius - r)
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(pointX, pointY);
        ctx.stroke();
        
        ctx.setLineDash([]);
        
        // Draw triangle labels
        if (showLabels) {
            ctx.font = `bold ${12 * zoom}px Arial`;
            ctx.textAlign = 'center';
            
            // Label for hypotenuse (r) - RED
            const hypMidX = (centerX + pointX) / 2;
            const hypMidY = (centerY + pointY) / 2;
            ctx.fillStyle = '#ef4444'; // Red color for r label
            ctx.fillText('r', hypMidX, hypMidY + 4);
            
            // Label for opposite side (y) - add negative sign for quadrants III and IV
            const oppMidX = pointX;
            const oppMidY = (pointY + centerY) / 2;
            const yLabel = (quadrant === 'III' || quadrant === 'IV') ? '-y' : 'y';
            ctx.fillStyle = '#10b981'; // Green color for y label
            ctx.fillText(yLabel, oppMidX - 15, oppMidY);
            
            // Label for adjacent side (x) - add negative sign for quadrants II and III
            const adjMidX = (pointX + centerX) / 2;
            const adjMidY = centerY;
            const xLabel = (quadrant === 'II' || quadrant === 'III') ? '-x' : 'x';
            ctx.fillStyle = '#10b981'; // Green color for x label
            ctx.fillText(xLabel, adjMidX, adjMidY + 15);
        }
        
        // Draw current point
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(pointX, pointY, 6, 0, 2 * Math.PI);
        ctx.fill();
        
        // Draw angle arc (reversed to match visual direction)
        ctx.strokeStyle = '#8b5cf6';
        ctx.lineWidth = 2;
        ctx.beginPath();
        // Reverse the arc direction to match the visual movement of the red dot
        const originalAngleRad = (displayAngle * Math.PI) / 180;
        ctx.arc(centerX, centerY, radius * 0.3, 0, -originalAngleRad, true);
        ctx.stroke();
        
        // Draw angle label (using reflected coordinates)
        if (showLabels) {
            ctx.fillStyle = '#8b5cf6';
            ctx.font = `${14 * zoom}px Arial`;
            ctx.textAlign = 'center';
            const labelAngle = angleRad / 2;
            const labelRadius = radius * 0.2;
            const labelX = centerX + Math.cos(labelAngle) * labelRadius;
            const labelY = centerY - Math.sin(labelAngle) * labelRadius; // Negative to reflect
            ctx.fillText(`${displayAngle.toFixed(1)}°`, labelX, labelY + 4);
            
            // Note: Special angle coordinates now shown on outer circle layer
        }
        
        // Draw quadrant labels
        if (showLabels) {
            ctx.fillStyle = '#f59e0b';
            ctx.font = `bold ${16 * zoom}px Arial`;
            ctx.textAlign = 'center';
            
            const quadLabels = [
                { text: 'I', x: centerX + radius * 0.7, y: centerY - radius * 0.7 },   // Top right
                { text: 'II', x: centerX - radius * 0.7, y: centerY - radius * 0.7 },  // Top left
                { text: 'III', x: centerX - radius * 0.7, y: centerY + radius * 0.7 }, // Bottom left
                { text: 'IV', x: centerX + radius * 0.7, y: centerY + radius * 0.7 }   // Bottom right
            ];
            
            quadLabels.forEach(label => {
                ctx.fillText(label.text, label.x, label.y);
            });
        }
        
    }, [displayAngle, angleRad, zoom, showGrid, showLabels]);

    // Update angle when initialData changes
    useEffect(() => {
        if (initialData.angle !== undefined) {
            setAngle(initialData.angle);
        }
    }, [initialData.angle]);

    // Force redraw when component mounts or initialData changes
    useEffect(() => {
        // Small delay to ensure canvas is ready
        const timer = setTimeout(() => {
            drawUnitCircle();
        }, 100);
        return () => clearTimeout(timer);
    }, [initialData.angle, drawUnitCircle]);

    // Redraw when dependencies change
    useEffect(() => {
        drawUnitCircle();
    }, [drawUnitCircle]);

    // Handle window resize
    useEffect(() => {
        const handleResize = () => {
            const canvas = canvasRef.current;
            if (canvas) {
                canvas.width = canvas.offsetWidth;
                canvas.height = canvas.offsetHeight;
                drawUnitCircle();
            }
        };

        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, [drawUnitCircle]);

    // Handle canvas size
    useEffect(() => {
        const canvas = canvasRef.current;
        if (canvas) {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
        }
    }, []);

    if (isCompact) {
        // Compact version for graph view
        return (
            <div className="bg-white border border-gray-200 rounded-lg p-3">
                <div className="flex items-center justify-between mb-2">
                    <h4 className="text-sm font-semibold text-gray-700">Unit Circle Reference</h4>
                    <span className="text-xs text-gray-500">Angle: {displayAngle.toFixed(1)}°</span>
                </div>
                <canvas
                    ref={canvasRef}
                    className="w-full h-32 border border-gray-300 rounded cursor-pointer"
                    onClick={handleCanvasClick}
                    onMouseDown={handleMouseDown}
                    onMouseMove={handleMouseMove}
                    onMouseUp={handleMouseUp}
                    onMouseLeave={handleMouseUp}
                />
                <div className="mt-2 text-xs text-gray-600">
                    <div className="grid grid-cols-3 gap-2">
                        <div>sin: {sinValue.toFixed(3)}</div>
                        <div>cos: {cosValue.toFixed(3)}</div>
                        <div>tan: {typeof tanValue === 'number' ? tanValue.toFixed(3) : tanValue}</div>
                    </div>
                    <div className="mt-1 text-center text-orange-600 font-medium">
                        Quadrant {quadrant}
                    </div>
                </div>
            </div>
        );
    }

    // Full version for solution procedure view
    return (
        <div className="bg-white border border-gray-200 rounded-lg p-4">
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-semibold text-gray-800">Interactive Unit Circle</h3>
                <div className="flex items-center space-x-2">
                    <button
                        onClick={() => handleAngleChange(0)}
                        className="px-2 py-1 text-xs bg-blue-100 text-blue-700 rounded hover:bg-blue-200 transition-colors"
                    >
                        Reset
                    </button>
                    <button
                        onClick={() => setShowValues(!showValues)}
                        className="px-2 py-1 text-xs bg-green-100 text-green-700 rounded hover:bg-green-200 transition-colors"
                    >
                        {showValues ? 'Hide' : 'Show'} Values
                    </button>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
                {/* Main Unit Circle Canvas */}
                <div className="lg:col-span-2">
                    <div className="relative">
                        <canvas
                            ref={canvasRef}
                            className="w-full h-80 border border-gray-300 rounded cursor-pointer"
                            onClick={handleCanvasClick}
                            onMouseDown={handleMouseDown}
                            onMouseMove={handleMouseMove}
                            onMouseUp={handleMouseUp}
                            onMouseLeave={handleMouseUp}
                        />
                        
                        {/* Zoom Controls */}
                        <div className="absolute top-2 right-2 flex flex-col space-y-1">
                            <button
                                onClick={() => setZoom(Math.min(zoom + 0.1, 2))}
                                className="p-1 bg-white border border-gray-300 rounded hover:bg-gray-50"
                            >
                                <Plus className="w-3 h-3" />
                            </button>
                            <button
                                onClick={() => setZoom(Math.max(zoom - 0.1, 0.5))}
                                className="p-1 bg-white border border-gray-300 rounded hover:bg-gray-50"
                            >
                                <Minus className="w-3 h-3" />
                            </button>
                        </div>
                    </div>
                    
                    {/* Canvas Controls */}
                    <div className="mt-3 flex items-center justify-center space-x-4">
                        <label className="flex items-center text-sm text-gray-700">
                            <input
                                type="checkbox"
                                checked={showGrid}
                                onChange={(e) => setShowGrid(e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>
                        <label className="flex items-center text-sm text-gray-700">
                            <input
                                type="checkbox"
                                checked={showLabels}
                                onChange={(e) => setShowLabels(e.target.checked)}
                                className="mr-2"
                            />
                            Show Labels
                        </label>
                    </div>
                    
                    {/* Common Trigonometric Values Table - INSIDE the circle container */}
                    <div className="mt-4 p-3 bg-purple-50 border border-purple-200 rounded-lg">
                        <h4 className="text-sm font-semibold text-purple-800 mb-2">Common Trigonometric Values</h4>
                        <div className="overflow-x-auto">
                            <table className="w-full text-xs">
                                <thead>
                                    <tr className="bg-purple-100">
                                        <th className="px-2 py-1 border border-purple-300 text-left">Angle</th>
                                        <th className="px-2 py-1 border border-purple-300 text-left">Radians</th>
                                        <th className="px-2 py-1 border border-purple-300 text-left">sin(θ)</th>
                                        <th className="px-2 py-1 border border-purple-300 text-left">cos(θ)</th>
                                        <th className="px-2 py-1 border border-purple-300 text-left">tan(θ)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td className="px-2 py-1 border border-purple-300">0°</td>
                                        <td className="px-2 py-1 border border-purple-300">0</td>
                                        <td className="px-2 py-1 border border-purple-300">0</td>
                                        <td className="px-2 py-1 border border-purple-300">1</td>
                                        <td className="px-2 py-1 border border-purple-300">0</td>
                                    </tr>
                                    <tr className="bg-purple-50">
                                        <td className="px-2 py-1 border border-purple-300">30°</td>
                                        <td className="px-2 py-1 border border-purple-300">π/6</td>
                                        <td className="px-2 py-1 border border-purple-300">1/2</td>
                                        <td className="px-2 py-1 border border-purple-300">√3/2</td>
                                        <td className="px-2 py-1 border border-purple-300">1/√3</td>
                                    </tr>
                                    <tr>
                                        <td className="px-2 py-1 border border-purple-300">45°</td>
                                        <td className="px-2 py-1 border border-purple-300">π/4</td>
                                        <td className="px-2 py-1 border border-purple-300">1/√2</td>
                                        <td className="px-2 py-1 border border-purple-300">1/√2</td>
                                        <td className="px-2 py-1 border border-purple-300">1</td>
                                    </tr>
                                    <tr className="bg-purple-50">
                                        <td className="px-2 py-1 border border-purple-300">60°</td>
                                        <td className="px-2 py-1 border border-purple-300">π/3</td>
                                        <td className="px-2 py-1 border border-purple-300">√3/2</td>
                                        <td className="px-2 py-1 border border-purple-300">1/2</td>
                                        <td className="px-2 py-1 border border-purple-300">√3</td>
                                    </tr>
                                    <tr>
                                        <td className="px-2 py-1 border border-purple-300">90°</td>
                                        <td className="px-2 py-1 border border-purple-300">π/2</td>
                                        <td className="px-2 py-1 border border-purple-300">1</td>
                                        <td className="px-2 py-1 border border-purple-300">0</td>
                                        <td className="px-2 py-1 border border-purple-300">undefined</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div className="mt-2 p-2 bg-purple-100 border border-purple-300 rounded">
                            <p className="text-xs text-purple-700">
                                <strong>Note:</strong> These values are fundamental and should be memorized.
                            </p>
                        </div>
                    </div>
                </div>

                {/* Control Panel */}
                <div className="space-y-4">
                    {/* Angle Control */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Angle Control
                        </label>
                        <div className="space-y-2">
                            <input
                                type="range"
                                min="0"
                                max="360"
                                value={displayAngle}
                                onChange={(e) => handleAngleChange(parseFloat(e.target.value))}
                                className="w-full"
                            />
                            <div className="flex space-x-2">
                                <input
                                    type="number"
                                    min="0"
                                    max="360"
                                    value={displayAngle}
                                    onChange={(e) => handleAngleChange(parseFloat(e.target.value))}
                                    className="flex-1 px-2 py-1 border border-gray-300 rounded text-sm"
                                    placeholder="Degrees"
                                />
                                <input
                                    type="number"
                                    min="0"
                                    max="6.28"
                                    value={(displayAngle * Math.PI / 180).toFixed(3)}
                                    onChange={(e) => handleAngleChange((parseFloat(e.target.value) * 180 / Math.PI))}
                                    className="flex-1 px-2 py-1 border border-gray-300 rounded text-sm"
                                    placeholder="Radians"
                                />
                            </div>
                        </div>
                    </div>

                    {/* Quick Angle Buttons */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Quick Angles
                        </label>
                        <div className="grid grid-cols-2 gap-2">
                            {[0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330].map((deg) => (
                                <button
                                    key={deg}
                                    onClick={() => handleAngleChange(deg)}
                                    className={`px-2 py-1 text-xs rounded transition-colors ${
                                        Math.abs(displayAngle - deg) < 1
                                            ? 'bg-blue-500 text-white'
                                            : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                                    }`}
                                >
                                    {deg}°
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Trigonometric Values */}
                    {showValues && (
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Trigonometric Values
                            </label>
                            <div className="space-y-2 text-sm">
                                <div className="flex justify-between">
                                    <span className="text-blue-600">sin({displayAngle.toFixed(1)}°):</span>
                                    <span className="font-mono">{sinValue.toFixed(4)}</span>
                                </div>
                                <div className="flex justify-between">
                                    <span className="text-green-600">cos({displayAngle.toFixed(1)}°):</span>
                                    <span className="font-mono">{cosValue.toFixed(4)}</span>
                                </div>
                                <div className="flex justify-between">
                                    <span className="text-red-600">tan({displayAngle.toFixed(1)}°):</span>
                                    <span className="font-mono">
                                        {typeof tanValue === 'number' ? tanValue.toFixed(4) : tanValue}
                                    </span>
                                </div>
                                <div className="flex justify-between">
                                    <span className="text-purple-600">Coordinates:</span>
                                    <span className="font-mono">({x.toFixed(3)}, {y.toFixed(3)})</span>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Quadrant Information */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Quadrant {quadrant}
                        </label>
                        <div className="text-xs text-gray-600 space-y-1">
                            {quadrant === 'I' && (
                                <div>0° to 90°: Top right - All functions positive</div>
                            )}
                            {quadrant === 'II' && (
                                <div>90° to 180°: Top left - Only sine positive</div>
                            )}
                            {quadrant === 'III' && (
                                <div>180° to 270°: Bottom left - Only tangent positive</div>
                            )}
                            {quadrant === 'IV' && (
                                <div>270° to 360°: Bottom right - Only cosine positive</div>
                            )}
                            <div className="text-orange-600 font-medium">
                                ASTC: All Students Take Calculus
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default UnitCircle;
