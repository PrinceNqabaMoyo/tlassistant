import React, { useRef, useEffect, useState } from 'react';

const BasicShapes = ({ 
    canvasRef, 
    geometryData, 
    onChange, 
    isSubmitted, 
    onCanvasClick, 
    onCanvasDraw,
    selectedSubConcept 
}) => {
    const localCanvasRef = useRef(null);
    const [selectedTool, setSelectedTool] = useState('point');

    useEffect(() => {
        const canvas = localCanvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const rect = canvas.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = rect.height;

        // Clear canvas
        ctx.fillStyle = geometryData.backgroundColor || '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw grid if enabled
        if (geometryData.showGrid) {
            drawGrid(ctx, canvas.width, canvas.height, geometryData.gridSize || 20, geometryData.gridColor || '#e5e7eb');
        }

        // Draw axes if enabled
        if (geometryData.showAxes) {
            drawAxes(ctx, canvas.width, canvas.height, geometryData.axisColor || '#374151');
        }

        // Draw existing geometry elements
        drawGeometryElements(ctx, canvas.width, canvas.height, geometryData);

    }, [geometryData, selectedSubConcept]);

    const drawGrid = (ctx, width, height, gridSize, gridColor) => {
        ctx.strokeStyle = gridColor;
        ctx.lineWidth = 0.5;
        ctx.setLineDash([]);
        
        for (let x = 0; x < width; x += gridSize) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }
        
        for (let y = 0; y < height; y += gridSize) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }
    };

    const drawAxes = (ctx, width, height, axisColor) => {
        const centerX = width / 2;
        const centerY = height / 2;
        
        ctx.strokeStyle = axisColor;
        ctx.lineWidth = 2;
        ctx.setLineDash([]);
        
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
    };

    const drawGeometryElements = (ctx, width, height, data) => {
        const centerX = width / 2;
        const centerY = height / 2;
        const gridSize = data.gridSize || 20;

        // Draw points
        if (data.points) {
            data.points.forEach(point => {
                drawPoint(ctx, point, centerX, centerY, gridSize, data.pointColor || '#EF4444');
            });
        }

        // Draw lines
        if (data.lines) {
            data.lines.forEach(line => {
                drawLine(ctx, line, centerX, centerY, gridSize, data.lineColor || '#10B981');
            });
        }

        // Draw rays
        if (data.rays) {
            data.rays.forEach(ray => {
                drawRay(ctx, ray, centerX, centerY, gridSize, data.lineColor || '#10B981');
            });
        }

        // Draw line segments
        if (data.lineSegments) {
            data.lineSegments.forEach(segment => {
                drawLineSegment(ctx, segment, centerX, centerY, gridSize, data.lineColor || '#10B981');
            });
        }
    };

    const drawPoint = (ctx, point, centerX, centerY, gridSize, color) => {
        const x = centerX + point.x * gridSize;
        const y = centerY - point.y * gridSize;
        
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, 2 * Math.PI);
        ctx.fill();
        
        // Draw label if exists
        if (point.label && geometryData.showLabels) {
            ctx.fillStyle = geometryData.axisColor || '#374151';
            ctx.font = '12px Arial';
            ctx.fillText(point.label, x + 8, y - 8);
        }
    };

    const drawLine = (ctx, line, centerX, centerY, gridSize, color) => {
        const x1 = centerX + line.x1 * gridSize;
        const y1 = centerY - line.y1 * gridSize;
        const x2 = centerX + line.x2 * gridSize;
        const y2 = centerY - line.y2 * gridSize;
        
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.setLineDash([]);
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        
        // Draw special indicators
        if (line.isParallel) {
            ctx.fillStyle = '#10B981';
            ctx.font = '10px Arial';
            ctx.fillText('∥', (x1 + x2) / 2, (y1 + y2) / 2 - 5);
        }
        if (line.isPerpendicular) {
            ctx.fillStyle = '#EF4444';
            ctx.font = '10px Arial';
            ctx.fillText('⊥', (x1 + x2) / 2, (y1 + y2) / 2 - 5);
        }
    };

    const drawRay = (ctx, ray, centerX, centerY, gridSize, color) => {
        const x1 = centerX + ray.x1 * gridSize;
        const y1 = centerY - ray.y1 * gridSize;
        const x2 = centerX + ray.x2 * gridSize;
        const y2 = centerY - ray.y2 * gridSize;
        
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.setLineDash([]);
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        
        // Draw arrowhead
        const angle = Math.atan2(y2 - y1, x2 - x1);
        const arrowLength = 10;
        const arrowAngle = Math.PI / 6;
        
        ctx.beginPath();
        ctx.moveTo(x2, y2);
        ctx.lineTo(
            x2 - arrowLength * Math.cos(angle - arrowAngle),
            y2 - arrowLength * Math.sin(angle - arrowAngle)
        );
        ctx.moveTo(x2, y2);
        ctx.lineTo(
            x2 - arrowLength * Math.cos(angle + arrowAngle),
            y2 - arrowLength * Math.sin(angle + arrowAngle)
        );
        ctx.stroke();
    };

    const drawLineSegment = (ctx, segment, centerX, centerY, gridSize, color) => {
        const x1 = centerX + segment.x1 * gridSize;
        const y1 = centerY - segment.y1 * gridSize;
        const x2 = centerX + segment.x2 * gridSize;
        const y2 = centerY - segment.y2 * gridSize;
        
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.setLineDash([]);
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        
        // Draw endpoints
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(x1, y1, 3, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(x2, y2, 3, 0, 2 * Math.PI);
        ctx.fill();
    };

    const handleCanvasClick = (e) => {
        if (isSubmitted) return;
        
        const canvas = localCanvasRef.current;
        if (!canvas) return;
        
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const gridSize = geometryData.gridSize || 20;
        
        const gridX = (x - centerX) / gridSize;
        const gridY = (centerY - y) / gridSize;
        
        // Add element based on selected tool
        addElement(selectedTool, { x: gridX, y: gridY });
    };

    const addElement = (type, coords) => {
        const newElement = {
            id: Date.now(),
            x: coords.x,
            y: coords.y,
            timestamp: new Date().toISOString()
        };

        switch (type) {
            case 'point':
                newElement.label = `P${(geometryData.points?.length || 0) + 1}`;
                onChange('points', [...(geometryData.points || []), newElement]);
                break;
            case 'line':
                // For lines, we need two points - this is a simplified version
                newElement.x2 = coords.x + 2;
                newElement.y2 = coords.y;
                newElement.label = `L${(geometryData.lines?.length || 0) + 1}`;
                onChange('lines', [...(geometryData.lines || []), newElement]);
                break;
            case 'ray':
                newElement.x2 = coords.x + 2;
                newElement.y2 = coords.y;
                newElement.label = `R${(geometryData.rays?.length || 0) + 1}`;
                onChange('rays', [...(geometryData.rays || []), newElement]);
                break;
            case 'line_segment':
                newElement.x2 = coords.x + 1;
                newElement.y2 = coords.y;
                newElement.label = `S${(geometryData.lineSegments?.length || 0) + 1}`;
                onChange('lineSegments', [...(geometryData.lineSegments || []), newElement]);
                break;
            case 'parallel_lines':
                // Create two parallel lines
                const line1 = {
                    id: Date.now(),
                    x1: coords.x - 1,
                    y1: coords.y - 0.5,
                    x2: coords.x + 2,
                    y2: coords.y - 0.5,
                    label: `L${(geometryData.lines?.length || 0) + 1}`,
                    isParallel: true,
                    timestamp: new Date().toISOString()
                };
                const line2 = {
                    id: Date.now() + 1,
                    x1: coords.x - 1,
                    y1: coords.y + 0.5,
                    x2: coords.x + 2,
                    y2: coords.y + 0.5,
                    label: `L${(geometryData.lines?.length || 0) + 2}`,
                    isParallel: true,
                    timestamp: new Date().toISOString()
                };
                onChange('lines', [...(geometryData.lines || []), line1, line2]);
                break;
            case 'perpendicular_lines':
                // Create two perpendicular lines
                const perpLine1 = {
                    id: Date.now(),
                    x1: coords.x - 1,
                    y1: coords.y,
                    x2: coords.x + 2,
                    y2: coords.y,
                    label: `L${(geometryData.lines?.length || 0) + 1}`,
                    isPerpendicular: true,
                    timestamp: new Date().toISOString()
                };
                const perpLine2 = {
                    id: Date.now() + 1,
                    x1: coords.x + 0.5,
                    y1: coords.y - 1,
                    x2: coords.x + 0.5,
                    y2: coords.y + 2,
                    label: `L${(geometryData.lines?.length || 0) + 2}`,
                    isPerpendicular: true,
                    timestamp: new Date().toISOString()
                };
                onChange('lines', [...(geometryData.lines || []), perpLine1, perpLine2]);
                break;
        }
    };

    const tools = [
        { id: 'point', name: 'Point', icon: '•', description: 'Click to add a point' },
        { id: 'line', name: 'Line', icon: '—', description: 'Click to add a line' },
        { id: 'ray', name: 'Ray', icon: '→', description: 'Click to add a ray' },
        { id: 'line_segment', name: 'Segment', icon: '—', description: 'Click to add a line segment' },
        { id: 'parallel_lines', name: 'Parallel', icon: '∥', description: 'Click to add parallel lines' },
        { id: 'perpendicular_lines', name: 'Perpendicular', icon: '⊥', description: 'Click to add perpendicular lines' }
    ];

    return (
        <div className="w-full h-full flex flex-col">
            {/* Tool Selection Bar */}
            <div className="bg-gray-50 border-b border-gray-200 p-2">
                <div className="flex flex-wrap gap-1">
                    {tools.map(tool => (
                        <button
                            key={tool.id}
                            onClick={() => setSelectedTool(tool.id)}
                            className={`px-3 py-1 rounded text-sm font-medium transition-colors ${
                                selectedTool === tool.id
                                    ? 'bg-blue-600 text-white'
                                    : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
                            }`}
                            title={tool.description}
                        >
                            <span className="mr-1">{tool.icon}</span>
                            {tool.name}
                        </button>
                    ))}
                </div>
            </div>
            
            {/* Canvas Area */}
            <div className="flex-1">
                <canvas
                    ref={localCanvasRef}
                    className="w-full h-full cursor-crosshair border border-gray-200 rounded"
                    onClick={handleCanvasClick}
                    style={{ backgroundColor: geometryData.backgroundColor || '#ffffff' }}
                />
            </div>
        </div>
    );
};

export default BasicShapes;
