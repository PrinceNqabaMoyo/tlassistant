import React, { useState, useEffect, useRef } from 'react';

const MathematicalInstruments = ({ initialData, onChange, isSubmitted }) => {
    const [instrumentsData, setInstrumentsData] = useState(initialData || {
        title: "Mathematical Instruments",
        activeTool: 'protractor', // 'protractor', 'compass', 'ruler', 'set_square', 'triangle'
        showGrid: true,
        showMeasurements: true,
        showLabels: true,
        gridSize: 20,
        canvasWidth: 800,
        canvasHeight: 600,
        measurements: [],
        constructions: []
    });

    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [startPoint, setStartPoint] = useState(null);
    const [currentAngle, setCurrentAngle] = useState(0);
    const [protractorCenter, setProtractorCenter] = useState(null);
    const [compassCenter, setCompassCenter] = useState(null);
    const [compassRadius, setCompassRadius] = useState(null);

    useEffect(() => {
        // Ensure measurements and constructions arrays are always initialized
        if (!instrumentsData.measurements) {
            setInstrumentsData(prev => ({ ...prev, measurements: [] }));
        }
        if (!instrumentsData.constructions) {
            setInstrumentsData(prev => ({ ...prev, constructions: [] }));
        }
        
        onChange(instrumentsData);
    }, [instrumentsData, onChange]);

    useEffect(() => {
        // Only draw canvas if instrumentsData is properly initialized
        if (instrumentsData && instrumentsData.measurements && instrumentsData.constructions) {
            drawCanvas();
        }
    }, [instrumentsData, startPoint, currentAngle, protractorCenter, compassCenter, compassRadius]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setInstrumentsData(prev => ({ ...prev, [field]: value }));
    };

    const addMeasurement = (type, value, start, end, label = '') => {
        if (isSubmitted) return;
        const newMeasurement = {
            id: Date.now(),
            type,
            value,
            start,
            end,
            label: label || `${type} ${(instrumentsData.measurements?.length || 0) + 1}`
        };
        setInstrumentsData(prev => ({
            ...prev,
            measurements: [...(prev.measurements || []), newMeasurement]
        }));
    };

    const addConstruction = (type, data, label = '') => {
        if (isSubmitted) return;
        const newConstruction = {
            id: Date.now(),
            type,
            data,
            label: label || `${type} ${(instrumentsData.constructions?.length || 0) + 1}`
        };
        setInstrumentsData(prev => ({
            ...prev,
            constructions: [...(prev.constructions || []), newConstruction]
        }));
    };

    const calculateDistance = (p1, p2) => {
        const dx = p2.x - p1.x;
        const dy = p2.y - p1.y;
        return Math.sqrt(dx * dx + dy * dy);
    };

    const calculateAngle = (center, p1, p2) => {
        const angle1 = Math.atan2(p1.y - center.y, p1.x - center.x);
        const angle2 = Math.atan2(p2.y - center.y, p2.x - center.x);
        let angle = (angle2 - angle1) * (180 / Math.PI);
        if (angle < 0) angle += 360;
        return angle;
    };

    const drawProtractor = (ctx, center, radius = 100) => {
        ctx.strokeStyle = '#3B82F6';
        ctx.lineWidth = 2;
        ctx.fillStyle = 'rgba(59, 130, 246, 0.1)';

        // Draw protractor base
        ctx.beginPath();
        ctx.arc(center.x, center.y, radius, 0, Math.PI, false);
        ctx.stroke();
        ctx.fill();

        // Draw degree markings
        ctx.strokeStyle = '#1E40AF';
        ctx.lineWidth = 1;
        ctx.font = '12px Arial';
        ctx.fillStyle = '#1E40AF';

        for (let angle = 0; angle <= 180; angle += 10) {
            const rad = (angle * Math.PI) / 180;
            const x1 = center.x + (radius - 20) * Math.cos(rad);
            const y1 = center.y - (radius - 20) * Math.sin(rad);
            const x2 = center.x + radius * Math.cos(rad);
            const y2 = center.y - radius * Math.sin(rad);

            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.stroke();

            // Add degree labels
            if (angle % 30 === 0) {
                const labelX = center.x + (radius - 35) * Math.cos(rad);
                const labelY = center.y - (radius - 35) * Math.sin(rad);
                ctx.fillText(angle.toString(), labelX - 10, labelY + 4);
            }
        }

        // Draw center point
        ctx.fillStyle = '#3B82F6';
        ctx.beginPath();
        ctx.arc(center.x, center.y, 3, 0, 2 * Math.PI);
        ctx.fill();
    };

    const drawCompass = (ctx, center, radius) => {
        if (!center || !radius) return;

        ctx.strokeStyle = '#10B981';
        ctx.lineWidth = 2;
        ctx.fillStyle = 'rgba(16, 185, 129, 0.1)';

        // Draw compass circle
        ctx.beginPath();
        ctx.arc(center.x, center.y, radius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();

        // Draw compass needle
        ctx.strokeStyle = '#059669';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(center.x, center.y);
        ctx.lineTo(center.x + radius, center.y);
        ctx.stroke();

        // Draw center point
        ctx.fillStyle = '#10B981';
        ctx.beginPath();
        ctx.arc(center.x, center.y, 4, 0, 2 * Math.PI);
        ctx.fill();
    };

    const drawRuler = (ctx, start, end) => {
        if (!start || !end) return;

        ctx.strokeStyle = '#6B7280';
        ctx.lineWidth = 3;
        ctx.setLineDash([5, 5]);

        // Draw ruler line
        ctx.beginPath();
        ctx.moveTo(start.x, start.y);
        ctx.lineTo(end.x, end.y);
        ctx.stroke();

        // Draw measurement markings
        ctx.setLineDash([]);
        ctx.lineWidth = 1;
        ctx.strokeStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.fillStyle = '#374151';

        const distance = calculateDistance(start, end);
        const numMarkings = Math.floor(distance / 20);
        
        for (let i = 0; i <= numMarkings; i++) {
            const t = i / numMarkings;
            const x = start.x + t * (end.x - start.x);
            const y = start.y + t * (end.y - start.y);
            
            // Perpendicular marking
            const perpLength = 8;
            const dx = end.x - start.x;
            const dy = end.y - start.y;
            const length = Math.sqrt(dx * dx + dy * dy);
            
            if (length > 0) {
                const perpX = -dy / length * perpLength;
                const perpY = dx / length * perpLength;
                
                ctx.beginPath();
                ctx.moveTo(x - perpX, y - perpY);
                ctx.lineTo(x + perpX, y + perpY);
                ctx.stroke();
            }

            // Add measurement labels
            if (i % 5 === 0) {
                const measurement = Math.round((distance * i) / numMarkings);
                ctx.fillText(measurement.toString(), x + 5, y - 5);
            }
        }

        // Reset line dash
        ctx.setLineDash([]);
    };

    const drawSetSquare = (ctx, center, angle = 0, size = 60) => {
        ctx.strokeStyle = '#F59E0B';
        ctx.lineWidth = 2;
        ctx.fillStyle = 'rgba(245, 158, 11, 0.1)';

        // Calculate triangle vertices
        const rad = (angle * Math.PI) / 180;
        const cos = Math.cos(rad);
        const sin = Math.sin(rad);

        const p1 = { x: center.x, y: center.y };
        const p2 = { 
            x: center.x + size * cos, 
            y: center.y - size * sin 
        };
        const p3 = { 
            x: center.x - size * sin, 
            y: center.y - size * cos 
        };

        // Draw triangle
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.lineTo(p3.x, p3.y);
        ctx.closePath();
        ctx.stroke();
        ctx.fill();

        // Draw right angle symbol
        ctx.strokeStyle = '#D97706';
        ctx.lineWidth = 1;
        const rightAngleSize = 8;
        ctx.beginPath();
        ctx.moveTo(p1.x + rightAngleSize, p1.y);
        ctx.lineTo(p1.x + rightAngleSize, p1.y - rightAngleSize);
        ctx.lineTo(p1.x, p1.y - rightAngleSize);
        ctx.stroke();
    };

    const drawCanvas = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw grid
        if (instrumentsData.showGrid) {
            ctx.strokeStyle = '#E5E7EB';
            ctx.lineWidth = 1;

            for (let x = 0; x <= canvas.width; x += instrumentsData.gridSize) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, canvas.height);
                ctx.stroke();
            }

            for (let y = 0; y <= canvas.height; y += instrumentsData.gridSize) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(canvas.width, y);
                ctx.stroke();
            }
        }

        // Draw existing constructions
        instrumentsData.constructions?.forEach(construction => {
            if (!construction || !construction.data) return;
            
            switch (construction.type) {
                case 'circle':
                    if (construction.data.center && construction.data.radius) {
                        ctx.strokeStyle = '#10B981';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.arc(construction.data.center.x, construction.data.center.y, construction.data.radius, 0, 2 * Math.PI);
                        ctx.stroke();
                    }
                    break;
                case 'line':
                    if (construction.data.start && construction.data.end) {
                        ctx.strokeStyle = '#6B7280';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.moveTo(construction.data.start.x, construction.data.start.y);
                        ctx.lineTo(construction.data.end.x, construction.data.end.y);
                        ctx.stroke();
                    }
                    break;
                case 'angle':
                    if (construction.data.center && construction.data.p1 && construction.data.p2) {
                        ctx.strokeStyle = '#3B82F6';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.moveTo(construction.data.center.x, construction.data.center.y);
                        ctx.lineTo(construction.data.p1.x, construction.data.p1.y);
                        ctx.moveTo(construction.data.center.x, construction.data.center.y);
                        ctx.lineTo(construction.data.p2.x, construction.data.p2.y);
                        ctx.stroke();
                    }
                    break;
            }
        });

        // Draw measurements
        if (instrumentsData.showMeasurements) {
            instrumentsData.measurements?.forEach(measurement => {
                if (!measurement || !measurement.start || !measurement.end) return;
                
                ctx.strokeStyle = '#EF4444';
                ctx.lineWidth = 1;
                ctx.font = '12px Arial';
                ctx.fillStyle = '#EF4444';

                switch (measurement.type) {
                    case 'distance':
                        // Draw measurement line
                        ctx.beginPath();
                        ctx.moveTo(measurement.start.x, measurement.start.y);
                        ctx.lineTo(measurement.end.x, measurement.end.y);
                        ctx.stroke();

                        // Draw measurement label
                        const midX = (measurement.start.x + measurement.end.x) / 2;
                        const midY = (measurement.start.y + measurement.end.y) / 2;
                        ctx.fillText(`${measurement.value.toFixed(1)}px`, midX + 5, midY - 5);
                        break;

                    case 'angle':
                        // Draw angle arc
                        const radius = 30;
                        ctx.beginPath();
                        ctx.arc(measurement.start.x, measurement.start.y, radius, 0, (measurement.value * Math.PI) / 180);
                        ctx.stroke();

                        // Draw angle label
                        const angleMidX = measurement.start.x + (radius * 0.7) * Math.cos((measurement.value * Math.PI) / 360);
                        const angleMidY = measurement.start.y - (radius * 0.7) * Math.sin((measurement.value * Math.PI) / 360);
                        ctx.fillText(`${measurement.value.toFixed(1)}°`, angleMidX, angleMidY);
                        break;
                }
            });
        }

        // Draw active tool
        switch (instrumentsData.activeTool) {
            case 'protractor':
                if (protractorCenter) {
                    drawProtractor(ctx, protractorCenter);
                    if (startPoint) {
                        // Draw angle measurement
                        const angle = calculateAngle(protractorCenter, protractorCenter, startPoint);
                        setCurrentAngle(angle);
                        
                        ctx.strokeStyle = '#EF4444';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.moveTo(protractorCenter.x, protractorCenter.y);
                        ctx.lineTo(startPoint.x, startPoint.y);
                        ctx.stroke();

                        // Draw angle label
                        ctx.fillStyle = '#EF4444';
                        ctx.font = '14px Arial';
                        ctx.fillText(`${angle.toFixed(1)}°`, startPoint.x + 10, startPoint.y - 10);
                    }
                }
                break;

            case 'compass':
                if (compassCenter) {
                    drawCompass(ctx, compassCenter, compassRadius);
                }
                break;

            case 'ruler':
                if (startPoint) {
                    drawRuler(ctx, startPoint, { x: startPoint.x + 100, y: startPoint.y });
                }
                break;

            case 'set_square':
                if (startPoint) {
                    drawSetSquare(ctx, startPoint, currentAngle);
                }
                break;

            case 'triangle':
                if (startPoint) {
                    // Draw equilateral triangle
                    const size = 60;
                    const height = size * Math.sqrt(3) / 2;
                    
                    ctx.strokeStyle = '#8B5CF6';
                    ctx.lineWidth = 2;
                    ctx.fillStyle = 'rgba(139, 92, 246, 0.1)';
                    
                    ctx.beginPath();
                    ctx.moveTo(startPoint.x, startPoint.y);
                    ctx.lineTo(startPoint.x + size, startPoint.y);
                    ctx.lineTo(startPoint.x + size/2, startPoint.y - height);
                    ctx.closePath();
                    ctx.stroke();
                    ctx.fill();
                }
                break;
        }

        // Draw start point if exists
        if (startPoint) {
            ctx.fillStyle = '#EF4444';
            ctx.beginPath();
            ctx.arc(startPoint.x, startPoint.y, 4, 0, 2 * Math.PI);
            ctx.fill();
        }
    };

    const handleCanvasClick = (e) => {
        if (isSubmitted) return;

        const canvas = canvasRef.current;
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const point = { x, y };

        switch (instrumentsData.activeTool) {
            case 'protractor':
                if (!protractorCenter) {
                    setProtractorCenter(point);
                } else if (!startPoint) {
                    setStartPoint(point);
                    const angle = calculateAngle(protractorCenter, protractorCenter, point);
                    addMeasurement('angle', angle, protractorCenter, point, `Angle: ${angle.toFixed(1)}°`);
                } else {
                    // Reset for new measurement
                    setStartPoint(null);
                    setProtractorCenter(null);
                }
                break;

            case 'compass':
                if (!compassCenter) {
                    setCompassCenter(point);
                } else if (!compassRadius) {
                    const radius = calculateDistance(compassCenter, point);
                    setCompassRadius(radius);
                    addConstruction('circle', { center: compassCenter, radius }, `Circle r=${radius.toFixed(1)}`);
                    // Reset for new circle
                    setCompassCenter(null);
                    setCompassRadius(null);
                }
                break;

            case 'ruler':
                if (!startPoint) {
                    setStartPoint(point);
                } else {
                    const distance = calculateDistance(startPoint, point);
                    addMeasurement('distance', distance, startPoint, point, `Distance: ${distance.toFixed(1)}px`);
                    addConstruction('line', { start: startPoint, end: point }, `Line ${distance.toFixed(1)}px`);
                    setStartPoint(null);
                }
                break;

            case 'set_square':
            case 'triangle':
                setStartPoint(point);
                addConstruction(instrumentsData.activeTool, { center: point, angle: currentAngle }, `${instrumentsData.activeTool} at (${point.x}, ${point.y})`);
                break;
        }
    };

    const clearAll = () => {
        if (isSubmitted) return;
        setInstrumentsData(prev => ({
            ...prev,
            measurements: [],
            constructions: []
        }));
        setStartPoint(null);
        setProtractorCenter(null);
        setCompassCenter(null);
        setCompassRadius(null);
        setCurrentAngle(0);
    };

    const resetTool = () => {
        setStartPoint(null);
        setProtractorCenter(null);
        setCompassCenter(null);
        setCompassRadius(null);
        setCurrentAngle(0);
    };

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Mathematical Instruments</h3>
            
            {/* Tool Selection */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={instrumentsData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Instruments Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Active Tool:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={instrumentsData.activeTool}
                        onChange={(e) => {
                            handleFieldChange('activeTool', e.target.value);
                            resetTool();
                        }}
                        disabled={isSubmitted}
                    >
                        <option value="protractor">📐 Protractor</option>
                        <option value="compass">🔄 Compass</option>
                        <option value="ruler">📏 Ruler</option>
                        <option value="set_square">📐 Set Square</option>
                        <option value="triangle">🔺 Triangle</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Grid Size:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={instrumentsData.gridSize}
                        onChange={(e) => handleFieldChange('gridSize', parseInt(e.target.value))}
                        disabled={isSubmitted}
                    >
                        <option value={10}>10px</option>
                        <option value={20}>20px</option>
                        <option value={50}>50px</option>
                    </select>
                </div>

                <div className="flex space-x-2">
                    {!isSubmitted && (
                        <>
                            <button
                                onClick={resetTool}
                                className="flex-1 px-3 py-2 bg-yellow-500 text-white text-sm rounded-md hover:bg-yellow-600"
                            >
                                Reset Tool
                            </button>
                            <button
                                onClick={clearAll}
                                className="flex-1 px-3 py-2 bg-red-500 text-white text-sm rounded-md hover:bg-red-600"
                            >
                                Clear All
                            </button>
                        </>
                    )}
                </div>
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={instrumentsData.showGrid}
                        onChange={(e) => handleFieldChange('showGrid', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={instrumentsData.showMeasurements}
                        onChange={(e) => handleFieldChange('showMeasurements', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Measurements</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={instrumentsData.showLabels}
                        onChange={(e) => handleFieldChange('showLabels', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Labels</span>
                </label>
            </div>

            {/* Canvas */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700 mb-2">Instruments Canvas:</label>
                <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                    <canvas
                        ref={canvasRef}
                        width={instrumentsData.canvasWidth}
                        height={instrumentsData.canvasHeight}
                        onClick={handleCanvasClick}
                        className="cursor-crosshair bg-white"
                        style={{ maxWidth: '100%', height: 'auto' }}
                    />
                </div>
            </div>

            {/* Tool Instructions */}
            <div className="mb-4">
                <h4 className="font-semibold text-gray-700 mb-2">Tool Instructions:</h4>
                <div className="text-sm text-gray-600 space-y-2">
                    {instrumentsData.activeTool === 'protractor' && (
                        <div>
                            <p><strong>📐 Protractor:</strong></p>
                            <ol className="list-decimal list-inside space-y-1 ml-4">
                                <li>Click to place the protractor center</li>
                                <li>Click again to measure an angle</li>
                                <li>The angle will be displayed and saved</li>
                            </ol>
                        </div>
                    )}
                    
                    {instrumentsData.activeTool === 'compass' && (
                        <div>
                            <p><strong>🔄 Compass:</strong></p>
                            <ol className="list-decimal list-inside space-y-1 ml-4">
                                <li>Click to place the compass center</li>
                                <li>Click again to set the radius</li>
                                <li>A circle will be drawn automatically</li>
                            </ol>
                        </div>
                    )}
                    
                    {instrumentsData.activeTool === 'ruler' && (
                        <div>
                            <p><strong>📏 Ruler:</strong></p>
                            <ol className="list-decimal list-inside space-y-1 ml-4">
                                <li>Click to place the start point</li>
                                <li>Click again to place the end point</li>
                                <li>The distance will be measured and displayed</li>
                            </ol>
                        </div>
                    )}
                    
                    {instrumentsData.activeTool === 'set_square' && (
                        <div>
                            <p><strong>📐 Set Square:</strong></p>
                            <ol className="list-decimal list-inside space-y-1 ml-4">
                                <li>Click to place the set square</li>
                                <li>A right-angled triangle will be drawn</li>
                                <li>Use for perpendicular and parallel lines</li>
                            </ol>
                        </div>
                    )}
                    
                    {instrumentsData.activeTool === 'triangle' && (
                        <div>
                            <p><strong>🔺 Triangle:</strong></p>
                            <ol className="list-decimal list-inside space-y-1 ml-4">
                                <li>Click to place the triangle</li>
                                <li>An equilateral triangle will be drawn</li>
                                <li>Use for geometric constructions</li>
                            </ol>
                        </div>
                    )}
                </div>
            </div>

            {/* Measurements and Constructions */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div className="bg-white p-3 border border-gray-200 rounded-lg">
                    <h4 className="font-semibold text-gray-700 mb-2">Measurements ({instrumentsData.measurements?.length || 0})</h4>
                    <div className="text-sm text-gray-600 max-h-32 overflow-y-auto">
                        {instrumentsData.measurements?.map((measurement) => (
                            <div key={measurement.id} className="flex justify-between mb-1">
                                <span>{measurement.label}</span>
                                <span className="text-blue-600">
                                    {measurement.type === 'distance' ? `${measurement.value.toFixed(1)}px` : `${measurement.value.toFixed(1)}°`}
                                </span>
                            </div>
                        )) || <div className="text-gray-400">No measurements yet</div>}
                    </div>
                </div>
                
                <div className="bg-white p-3 border border-gray-200 rounded-lg">
                    <h4 className="font-semibold text-gray-700 mb-2">Constructions ({instrumentsData.constructions?.length || 0})</h4>
                    <div className="text-sm text-gray-600 max-h-32 overflow-y-auto">
                        {instrumentsData.constructions?.map((construction) => (
                            <div key={construction.id} className="flex justify-between mb-1">
                                <span>{construction.label}</span>
                                <span className="text-green-600">●</span>
                            </div>
                        )) || <div className="text-gray-400">No constructions yet</div>}
                    </div>
                </div>
            </div>

            {/* Help Text */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Mathematical Instruments Guide:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li><strong>Protractor:</strong> Measure angles with precision</li>
                    <li><strong>Compass:</strong> Draw perfect circles and arcs</li>
                    <li><strong>Ruler:</strong> Measure distances and draw straight lines</li>
                    <li><strong>Set Square:</strong> Create right angles and parallel lines</li>
                    <li><strong>Triangle:</strong> Draw equilateral triangles for constructions</li>
                    <li>All measurements are automatically saved and displayed</li>
                    <li>Use the grid for precise positioning</li>
                </ul>
            </div>
        </div>
    );
};

export default MathematicalInstruments;
