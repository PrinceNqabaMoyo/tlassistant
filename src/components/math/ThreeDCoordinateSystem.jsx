import React, { useState, useEffect, useRef } from 'react';

const ThreeDCoordinateSystem = ({ initialData, onChange, isSubmitted }) => {
    const [coord3DData, setCoord3DData] = useState(initialData || {
        title: "3D Coordinate System",
        xRange: [-10, 10],
        yRange: [-10, 10],
        zRange: [-10, 10],
        showGrid: true,
        showAxes: true,
        showLabels: true,
        showPoints: true,
        showVectors: true,
        showPlanes: true,
        rotationX: 0,
        rotationY: 0,
        rotationZ: 0,
        perspective: 800,
        backgroundColor: '#ffffff',
        gridColor: '#e5e7eb',
        axisColor: '#374151',
        pointColor: '#3B82F6',
        vectorColor: '#10B981',
        planeColor: '#F59E0B',
        points: [
            { x: 3, y: 2, z: 4, label: 'P1', color: '#3B82F6' },
            { x: -2, y: 5, z: -1, label: 'P2', color: '#10B981' }
        ],
        vectors: [
            { x: 2, y: 3, z: 1, label: 'v1', color: '#10B981' },
            { x: -1, y: 2, z: 3, label: 'v2', color: '#F59E0B' }
        ],
        planes: [
            { type: 'xy', z: 0, color: '#F59E0B', opacity: 0.3 },
            { type: 'xz', y: 0, color: '#EF4444', opacity: 0.3 },
            { type: 'yz', x: 0, color: '#8B5CF6', opacity: 0.3 }
        ]
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(coord3DData);
        }
    }, [coord3DData, onChange]);

    useEffect(() => {
        draw3DSystem();
    }, [coord3DData]);

    const draw3DSystem = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = coord3DData.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        const { xRange, yRange, zRange, showGrid, showAxes, showLabels, showPoints, showVectors, showPlanes, rotationX, rotationY, rotationZ, perspective, gridColor, axisColor, pointColor, vectorColor, planeColor, points, vectors, planes } = coord3DData;

        // 3D to 2D projection function
        const project3DTo2D = (x, y, z) => {
            // Apply rotations
            const cosX = Math.cos(rotationX * Math.PI / 180);
            const sinX = Math.sin(rotationX * Math.PI / 180);
            const cosY = Math.cos(rotationY * Math.PI / 180);
            const sinY = Math.sin(rotationY * Math.PI / 180);
            const cosZ = Math.cos(rotationZ * Math.PI / 180);
            const sinZ = Math.sin(rotationZ * Math.PI / 180);

            // Rotate around X-axis
            let x1 = x;
            let y1 = y * cosX - z * sinX;
            let z1 = y * sinX + z * cosX;

            // Rotate around Y-axis
            let x2 = x1 * cosY + z1 * sinY;
            let y2 = y1;
            let z2 = -x1 * sinY + z1 * cosY;

            // Rotate around Z-axis
            let x3 = x2 * cosZ - y2 * sinZ;
            let y3 = x2 * sinZ + y2 * cosZ;
            let z3 = z2;

            // Project to 2D
            const scale = perspective / (perspective + z3);
            const screenX = width / 2 + x3 * scale * 20;
            const screenY = height / 2 - y3 * scale * 20;

            return { x: screenX, y: screenY, z: z3, scale };
        };

        // Draw coordinate planes
        if (showPlanes) {
            planes.forEach(plane => {
                ctx.fillStyle = plane.color + Math.floor(plane.opacity * 255).toString(16).padStart(2, '0');
                
                if (plane.type === 'xy') {
                    const p1 = project3DTo2D(xRange[0], yRange[0], plane.z);
                    const p2 = project3DTo2D(xRange[1], yRange[0], plane.z);
                    const p3 = project3DTo2D(xRange[1], yRange[1], plane.z);
                    const p4 = project3DTo2D(xRange[0], yRange[1], plane.z);
                    
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.lineTo(p3.x, p3.y);
                    ctx.lineTo(p4.x, p4.y);
                    ctx.closePath();
                    ctx.fill();
                } else if (plane.type === 'xz') {
                    const p1 = project3DTo2D(xRange[0], plane.y, zRange[0]);
                    const p2 = project3DTo2D(xRange[1], plane.y, zRange[0]);
                    const p3 = project3DTo2D(xRange[1], plane.y, zRange[1]);
                    const p4 = project3DTo2D(xRange[0], plane.y, zRange[1]);
                    
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.lineTo(p3.x, p3.y);
                    ctx.lineTo(p4.x, p4.y);
                    ctx.closePath();
                    ctx.fill();
                } else if (plane.type === 'yz') {
                    const p1 = project3DTo2D(plane.x, yRange[0], zRange[0]);
                    const p2 = project3DTo2D(plane.x, yRange[1], zRange[0]);
                    const p3 = project3DTo2D(plane.x, yRange[1], zRange[1]);
                    const p4 = project3DTo2D(plane.x, yRange[0], zRange[1]);
                    
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.lineTo(p3.x, p3.y);
                    ctx.lineTo(p4.x, p4.y);
                    ctx.closePath();
                    ctx.fill();
                }
            });
        }

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = gridColor;
            ctx.lineWidth = 1;
            
            // XY grid at z = 0
            for (let x = xRange[0]; x <= xRange[1]; x += 2) {
                const p1 = project3DTo2D(x, yRange[0], 0);
                const p2 = project3DTo2D(x, yRange[1], 0);
                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }
            
            for (let y = yRange[0]; y <= yRange[1]; y += 2) {
                const p1 = project3DTo2D(xRange[0], y, 0);
                const p2 = project3DTo2D(xRange[1], y, 0);
                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }
        }

        // Draw axes
        if (showAxes) {
            ctx.strokeStyle = axisColor;
            ctx.lineWidth = 3;
            
            // X-axis
            const xAxisStart = project3DTo2D(xRange[0], 0, 0);
            const xAxisEnd = project3DTo2D(xRange[1], 0, 0);
            ctx.beginPath();
            ctx.moveTo(xAxisStart.x, xAxisStart.y);
            ctx.lineTo(xAxisEnd.x, xAxisEnd.y);
            ctx.stroke();
            
            // Y-axis
            const yAxisStart = project3DTo2D(0, yRange[0], 0);
            const yAxisEnd = project3DTo2D(0, yRange[1], 0);
            ctx.beginPath();
            ctx.moveTo(yAxisStart.x, yAxisStart.y);
            ctx.lineTo(yAxisEnd.x, yAxisEnd.y);
            ctx.stroke();
            
            // Z-axis
            const zAxisStart = project3DTo2D(0, 0, zRange[0]);
            const zAxisEnd = project3DTo2D(0, 0, zRange[1]);
            ctx.beginPath();
            ctx.moveTo(zAxisStart.x, zAxisStart.y);
            ctx.lineTo(zAxisEnd.x, zAxisEnd.y);
            ctx.stroke();
        }

        // Draw points
        if (showPoints) {
            points.forEach(point => {
                const projected = project3DTo2D(point.x, point.y, point.z);
                
                ctx.fillStyle = point.color;
                ctx.beginPath();
                ctx.arc(projected.x, projected.y, 6 * projected.scale, 0, 2 * Math.PI);
                ctx.fill();
                
                if (showLabels) {
                    ctx.fillStyle = '#374151';
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'left';
                    ctx.fillText(point.label, projected.x + 10, projected.y - 10);
                    ctx.fillText(`(${point.x}, ${point.y}, ${point.z})`, projected.x + 10, projected.y + 5);
                }
            });
        }

        // Draw vectors
        if (showVectors) {
            vectors.forEach(vector => {
                const start = project3DTo2D(0, 0, 0);
                const end = project3DTo2D(vector.x, vector.y, vector.z);
                
                // Draw vector line
                ctx.strokeStyle = vector.color;
                ctx.lineWidth = 3 * start.scale;
                ctx.beginPath();
                ctx.moveTo(start.x, start.y);
                ctx.lineTo(end.x, end.y);
                ctx.stroke();
                
                // Draw arrowhead
                const angle = Math.atan2(end.y - start.y, end.x - start.x);
                const arrowLength = 15 * start.scale;
                const arrowAngle = Math.PI / 6;
                
                ctx.beginPath();
                ctx.moveTo(end.x, end.y);
                ctx.lineTo(
                    end.x - arrowLength * Math.cos(angle - arrowAngle),
                    end.y - arrowLength * Math.sin(angle - arrowAngle)
                );
                ctx.moveTo(end.x, end.y);
                ctx.lineTo(
                    end.x - arrowLength * Math.cos(angle + arrowAngle),
                    end.y - arrowLength * Math.sin(angle + arrowAngle)
                );
                ctx.stroke();
                
                if (showLabels) {
                    ctx.fillStyle = '#374151';
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'left';
                    ctx.fillText(vector.label, end.x + 10, end.y - 10);
                    ctx.fillText(`<${vector.x}, ${vector.y}, ${vector.z}>`, end.x + 10, end.y + 5);
                }
            });
        }

        // Draw axis labels
        if (showLabels) {
            ctx.fillStyle = axisColor;
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            
            const xLabel = project3DTo2D(xRange[1] + 1, 0, 0);
            const yLabel = project3DTo2D(0, yRange[1] + 1, 0);
            const zLabel = project3DTo2D(0, 0, zRange[1] + 1);
            
            ctx.fillText('X', xLabel.x, xLabel.y);
            ctx.fillText('Y', yLabel.x, yLabel.y);
            ctx.fillText('Z', zLabel.x, zLabel.y);
        }
    };

    const handleInputChange = (field, value) => {
        setCoord3DData(prev => ({
            ...prev,
            [field]: field === 'rotationX' || field === 'rotationY' || field === 'rotationZ' || field === 'perspective' ? parseFloat(value) || 0 : value
        }));
    };

    const handleRangeChange = (axis, index, value) => {
        setCoord3DData(prev => ({
            ...prev,
            [axis]: prev[axis].map((val, i) => i === index ? parseFloat(value) || 0 : val)
        }));
    };

    const addPoint = () => {
        const newPoint = {
            x: Math.floor(Math.random() * 10) - 5,
            y: Math.floor(Math.random() * 10) - 5,
            z: Math.floor(Math.random() * 10) - 5,
            label: `P${coord3DData.points.length + 1}`,
            color: `#${Math.floor(Math.random()*16777215).toString(16)}`
        };
        setCoord3DData(prev => ({
            ...prev,
            points: [...prev.points, newPoint]
        }));
    };

    const addVector = () => {
        const newVector = {
            x: Math.floor(Math.random() * 6) - 3,
            y: Math.floor(Math.random() * 6) - 3,
            z: Math.floor(Math.random() * 6) - 3,
            label: `v${coord3DData.vectors.length + 1}`,
            color: `#${Math.floor(Math.random()*16777215).toString(16)}`
        };
        setCoord3DData(prev => ({
            ...prev,
            vectors: [...prev.vectors, newVector]
        }));
    };

    const removePoint = (index) => {
        setCoord3DData(prev => ({
            ...prev,
            points: prev.points.filter((_, i) => i !== index)
        }));
    };

    const removeVector = (index) => {
        setCoord3DData(prev => ({
            ...prev,
            vectors: prev.vectors.filter((_, i) => i !== index)
        }));
    };

    const calculateVectorOperations = () => {
        if (coord3DData.vectors.length >= 2) {
            const v1 = coord3DData.vectors[0];
            const v2 = coord3DData.vectors[1];
            
            // Dot product
            const dotProduct = v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
            
            // Cross product
            const crossX = v1.y * v2.z - v1.z * v2.y;
            const crossY = v1.z * v2.x - v1.x * v2.z;
            const crossZ = v1.x * v2.y - v1.y * v2.x;
            
            // Magnitudes
            const mag1 = Math.sqrt(v1.x * v1.x + v1.y * v1.y + v1.z * v1.z);
            const mag2 = Math.sqrt(v2.x * v2.x + v2.y * v2.y + v2.z * v2.z);
            
            return {
                dotProduct: dotProduct.toFixed(3),
                crossProduct: `<${crossX.toFixed(3)}, ${crossY.toFixed(3)}, ${crossZ.toFixed(3)}>`,
                magnitude1: mag1.toFixed(3),
                magnitude2: mag2.toFixed(3),
                angle: Math.acos(dotProduct / (mag1 * mag2)) * 180 / Math.PI
            };
        }
        return null;
    };

    const vectorOps = calculateVectorOperations();

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
                        value={coord3DData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Perspective Distance
                    </label>
                    <input
                        type="number"
                        min="100"
                        max="2000"
                        value={coord3DData.perspective}
                        onChange={(e) => handleInputChange('perspective', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Rotation X (degrees)
                    </label>
                    <input
                        type="range"
                        min="-180"
                        max="180"
                        value={coord3DData.rotationX}
                        onChange={(e) => handleInputChange('rotationX', e.target.value)}
                        className="w-full"
                    />
                    <span className="text-sm text-gray-600">{coord3DData.rotationX}°</span>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Rotation Y (degrees)
                    </label>
                    <input
                        type="range"
                        min="-180"
                        max="180"
                        value={coord3DData.rotationY}
                        onChange={(e) => handleInputChange('rotationY', e.target.value)}
                        className="w-full"
                    />
                    <span className="text-sm text-gray-600">{coord3DData.rotationY}°</span>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Rotation Z (degrees)
                    </label>
                    <input
                        type="range"
                        min="-180"
                        max="180"
                        value={coord3DData.rotationZ}
                        onChange={(e) => handleInputChange('rotationZ', e.target.value)}
                        className="w-full"
                    />
                    <span className="text-sm text-gray-600">{coord3DData.rotationZ}°</span>
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={coord3DData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={coord3DData.showAxes}
                                onChange={(e) => handleInputChange('showAxes', e.target.checked)}
                                className="mr-2"
                            />
                            Show Axes
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={coord3DData.showLabels}
                                onChange={(e) => handleInputChange('showLabels', e.target.checked)}
                                className="mr-2"
                            />
                            Show Labels
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={coord3DData.showPoints}
                                onChange={(e) => handleInputChange('showPoints', e.target.checked)}
                                className="mr-2"
                            />
                            Show Points
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={coord3DData.showVectors}
                                onChange={(e) => handleInputChange('showVectors', e.target.checked)}
                                className="mr-2"
                            />
                            Show Vectors
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={coord3DData.showPlanes}
                                onChange={(e) => handleInputChange('showPlanes', e.target.checked)}
                                className="mr-2"
                            />
                            Show Planes
                        </label>
                    </div>
                </div>
            </div>

            {/* Point and Vector Management */}
            <div className="grid grid-cols-2 gap-4">
                {/* Points */}
                <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                    <div className="flex justify-between items-center mb-3">
                        <h4 className="font-semibold text-blue-800">Points</h4>
                        <button
                            onClick={addPoint}
                            className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                        >
                            Add Point
                        </button>
                    </div>
                    <div className="space-y-2">
                        {coord3DData.points.map((point, index) => (
                            <div key={index} className="flex items-center justify-between p-2 bg-white rounded border">
                                <div>
                                    <span className="font-medium">{point.label}:</span>
                                    <span className="text-sm text-gray-600 ml-2">
                                        ({point.x}, {point.y}, {point.z})
                                    </span>
                                </div>
                                <button
                                    onClick={() => removePoint(index)}
                                    className="text-red-600 hover:text-red-800 text-sm"
                                >
                                    Remove
                                </button>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Vectors */}
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                    <div className="flex justify-between items-center mb-3">
                        <h4 className="font-semibold text-green-800">Vectors</h4>
                        <button
                            onClick={addVector}
                            className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                        >
                            Add Vector
                        </button>
                    </div>
                    <div className="space-y-2">
                        {coord3DData.vectors.map((vector, index) => (
                            <div key={index} className="flex items-center justify-between p-2 bg-white rounded border">
                                <div>
                                    <span className="font-medium">{vector.label}:</span>
                                    <span className="text-sm text-gray-600 ml-2">
                                        &lt;{vector.x}, {vector.y}, {vector.z}&gt;
                                    </span>
                                </div>
                                <button
                                    onClick={() => removeVector(index)}
                                    className="text-red-600 hover:text-red-800 text-sm"
                                >
                                    Remove
                                </button>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* Vector Operations */}
            {vectorOps && (
                <div className="p-4 bg-purple-50 border border-purple-200 rounded-lg">
                    <h4 className="font-semibold text-purple-800 mb-3">Vector Operations</h4>
                    <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                            <strong>Dot Product:</strong> {vectorOps.dotProduct}
                        </div>
                        <div>
                            <strong>Cross Product:</strong> {vectorOps.crossProduct}
                        </div>
                        <div>
                            <strong>Magnitude v1:</strong> {vectorOps.magnitude1}
                        </div>
                        <div>
                            <strong>Magnitude v2:</strong> {vectorOps.magnitude2}
                        </div>
                        <div className="col-span-2">
                            <strong>Angle between vectors:</strong> {vectorOps.angle.toFixed(2)}°
                        </div>
                    </div>
                </div>
            )}

            {/* 3D Coordinate Canvas */}
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

export default ThreeDCoordinateSystem;
