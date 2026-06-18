import React, { useState, useEffect, useRef } from 'react';

const PolarCoordinateSystem = ({ initialData, onChange, isSubmitted }) => {
    const [polarData, setPolarData] = useState(initialData || {
        title: "Polar Coordinate System",
        radius: 100,
        angle: 45,
        showGrid: true,
        showAxes: true,
        showAngle: true,
        showCoordinates: true,
        showTrigRatios: true,
        showReferenceAngle: true,
        showCAST: true,
        showUnitCircle: true,
        showDegrees: true,
        showRadians: false,
        gridSpacing: 20,
        backgroundColor: '#ffffff',
        gridColor: '#e5e7eb',
        axisColor: '#374151',
        pointColor: '#3B82F6',
        angleColor: '#10B981',
        referenceColor: '#F59E0B'
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(polarData);
        }
    }, [polarData, onChange]);

    useEffect(() => {
        drawPolarSystem();
    }, [polarData]);

    const drawPolarSystem = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        const centerX = width / 2;
        const centerY = height / 2;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = polarData.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        const { radius, angle, showGrid, showAxes, showAngle, showCoordinates, showTrigRatios, showReferenceAngle, showCAST, showUnitCircle, showDegrees, showRadians, gridSpacing, gridColor, axisColor, pointColor, angleColor, referenceColor } = polarData;

        // Convert angle to radians
        const angleRad = (angle * Math.PI) / 180;
        
        // Calculate point coordinates
        const x = radius * Math.cos(angleRad);
        const y = radius * Math.sin(angleRad);

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = gridColor;
            ctx.lineWidth = 1;
            
            // Draw concentric circles
            for (let r = gridSpacing; r <= Math.min(width, height) / 2; r += gridSpacing) {
                ctx.beginPath();
                ctx.arc(centerX, centerY, r, 0, 2 * Math.PI);
                ctx.stroke();
            }
            
            // Draw radial lines
            for (let a = 0; a < 360; a += 30) {
                const rad = (a * Math.PI) / 180;
                const endX = centerX + Math.cos(rad) * (Math.min(width, height) / 2);
                const endY = centerY + Math.sin(rad) * (Math.min(width, height) / 2);
                
                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.lineTo(endX, endY);
                ctx.stroke();
            }
        }

        // Draw axes
        if (showAxes) {
            ctx.strokeStyle = axisColor;
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
        }

        // Draw unit circle
        if (showUnitCircle) {
            ctx.strokeStyle = '#d1d5db';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.arc(centerX, centerY, 100, 0, 2 * Math.PI);
            ctx.stroke();
            ctx.setLineDash([]);
        }

        // Draw CAST quadrants
        if (showCAST) {
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            
            // First quadrant - All positive
            ctx.fillStyle = '#10B981';
            ctx.fillText('A', centerX + 50, centerY - 50);
            
            // Second quadrant - Sine positive
            ctx.fillStyle = '#3B82F6';
            ctx.fillText('S', centerX - 50, centerY - 50);
            
            // Third quadrant - Tangent positive
            ctx.fillStyle = '#F59E0B';
            ctx.fillText('T', centerX - 50, centerY + 50);
            
            // Fourth quadrant - Cosine positive
            ctx.fillStyle = '#EF4444';
            ctx.fillText('C', centerX + 50, centerY + 50);
        }

        // Draw angle
        if (showAngle) {
            ctx.strokeStyle = angleColor;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(centerX + radius * Math.cos(angleRad), centerY - radius * Math.sin(angleRad));
            ctx.stroke();

            // Draw angle arc
            ctx.strokeStyle = angleColor;
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(centerX, centerY, 30, 0, -angleRad, true);
            ctx.stroke();
        }

        // Draw reference angle
        if (showReferenceAngle) {
            const referenceAngle = getReferenceAngle(angle);
            const referenceRad = (referenceAngle * Math.PI) / 180;
            
            ctx.strokeStyle = referenceColor;
            ctx.lineWidth = 2;
            ctx.setLineDash([3, 3]);
            ctx.beginPath();
            ctx.arc(centerX, centerY, 40, 0, -referenceRad, true);
            ctx.stroke();
            ctx.setLineDash([]);
        }

        // Draw point
        ctx.fillStyle = pointColor;
        ctx.beginPath();
        ctx.arc(centerX + x, centerY - y, 6, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#1e40af';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Draw coordinates
        if (showCoordinates) {
            ctx.fillStyle = '#374151';
            ctx.font = '14px Arial';
            ctx.textAlign = 'left';
            ctx.fillText(`(${x.toFixed(1)}, ${y.toFixed(1)})`, centerX + x + 10, centerY - y);
            
            ctx.textAlign = 'center';
            ctx.fillText(`r = ${radius}`, centerX, centerY - radius - 20);
            
            if (showDegrees) {
                ctx.fillText(`θ = ${angle}°`, centerX, centerY - radius - 40);
            }
            if (showRadians) {
                ctx.fillText(`θ = ${angleRad.toFixed(3)} rad`, centerX, centerY - radius - 60);
            }
        }

        // Draw trigonometric ratios
        if (showTrigRatios) {
            const sinValue = Math.sin(angleRad);
            const cosValue = Math.cos(angleRad);
            const tanValue = Math.tan(angleRad);
            
            ctx.fillStyle = '#374151';
            ctx.font = '12px Arial';
            ctx.textAlign = 'left';
            
            let yOffset = 30;
            ctx.fillText(`sin(${angle}°) = ${sinValue.toFixed(3)}`, 20, yOffset);
            yOffset += 20;
            ctx.fillText(`cos(${angle}°) = ${cosValue.toFixed(3)}`, 20, yOffset);
            yOffset += 20;
            ctx.fillText(`tan(${angle}°) = ${tanValue.toFixed(3)}`, 20, yOffset);
            
            // Show quadrant information
            const quadrant = getQuadrant(angle);
            yOffset += 30;
            ctx.fillText(`Quadrant: ${quadrant}`, 20, yOffset);
            
            if (showReferenceAngle) {
                yOffset += 20;
                ctx.fillText(`Reference Angle: ${getReferenceAngle(angle)}°`, 20, yOffset);
            }
        }

        // Draw reduction formula
        if (showReferenceAngle) {
            const referenceAngle = getReferenceAngle(angle);
            const quadrant = getQuadrant(angle);
            const reductionInfo = getReductionFormula(angle, referenceAngle, quadrant);
            
            ctx.fillStyle = '#7c3aed';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('Reduction Formula:', 20, height - 80);
            
            ctx.fillStyle = '#374151';
            ctx.font = '12px Arial';
            ctx.fillText(reductionInfo.sin, 20, height - 60);
            ctx.fillText(reductionInfo.cos, 20, height - 40);
            ctx.fillText(reductionInfo.tan, 20, height - 20);
        }
    };

    const getReferenceAngle = (angle) => {
        const normalizedAngle = ((angle % 360) + 360) % 360;
        if (normalizedAngle <= 90) return normalizedAngle;
        if (normalizedAngle <= 180) return 180 - normalizedAngle;
        if (normalizedAngle <= 270) return normalizedAngle - 180;
        return 360 - normalizedAngle;
    };

    const getQuadrant = (angle) => {
        const normalizedAngle = ((angle % 360) + 360) % 360;
        if (normalizedAngle <= 90) return 1;
        if (normalizedAngle <= 180) return 2;
        if (normalizedAngle <= 270) return 3;
        return 4;
    };

    const getReductionFormula = (angle, referenceAngle, quadrant) => {
        const refSin = Math.sin((referenceAngle * Math.PI) / 180);
        const refCos = Math.cos((referenceAngle * Math.PI) / 180);
        const refTan = Math.tan((referenceAngle * Math.PI) / 180);

        let sinSign = '+';
        let cosSign = '+';
        let tanSign = '+';

        switch (quadrant) {
            case 1:
                sinSign = '+';
                cosSign = '+';
                tanSign = '+';
                break;
            case 2:
                sinSign = '+';
                cosSign = '-';
                tanSign = '-';
                break;
            case 3:
                sinSign = '-';
                cosSign = '-';
                tanSign = '+';
                break;
            case 4:
                sinSign = '-';
                cosSign = '+';
                tanSign = '-';
                break;
        }

        return {
            sin: `sin(${angle}°) = ${sinSign}sin(${referenceAngle}°) = ${sinSign}${refSin.toFixed(3)}`,
            cos: `cos(${angle}°) = ${cosSign}cos(${referenceAngle}°) = ${cosSign}${refCos.toFixed(3)}`,
            tan: `tan(${angle}°) = ${tanSign}tan(${referenceAngle}°) = ${tanSign}${refTan.toFixed(3)}`
        };
    };

    const handleInputChange = (field, value) => {
        setPolarData(prev => ({
            ...prev,
            [field]: field === 'radius' || field === 'angle' || field === 'gridSpacing' ? parseFloat(value) || 0 : value
        }));
    };

    const setAngle = (newAngle) => {
        setPolarData(prev => ({
            ...prev,
            angle: newAngle
        }));
    };

    const generateRandomAngle = () => {
        const randomAngle = Math.floor(Math.random() * 360);
        setAngle(randomAngle);
    };

    const setCommonAngles = () => {
        const commonAngles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330];
        const randomAngle = commonAngles[Math.floor(Math.random() * commonAngles.length)];
        setAngle(randomAngle);
    };

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
                        value={polarData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Radius
                    </label>
                    <input
                        type="number"
                        min="10"
                        max="200"
                        value={polarData.radius}
                        onChange={(e) => handleInputChange('radius', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Angle (degrees)
                    </label>
                    <input
                        type="number"
                        min="0"
                        max="360"
                        value={polarData.angle}
                        onChange={(e) => handleInputChange('angle', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Grid Spacing
                    </label>
                    <input
                        type="number"
                        min="10"
                        max="50"
                        value={polarData.gridSpacing}
                        onChange={(e) => handleInputChange('gridSpacing', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showAxes}
                                onChange={(e) => handleInputChange('showAxes', e.target.checked)}
                                className="mr-2"
                            />
                            Show Axes
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showAngle}
                                onChange={(e) => handleInputChange('showAngle', e.target.checked)}
                                className="mr-2"
                            />
                            Show Angle
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showCoordinates}
                                onChange={(e) => handleInputChange('showCoordinates', e.target.checked)}
                                className="mr-2"
                            />
                            Show Coordinates
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showTrigRatios}
                                onChange={(e) => handleInputChange('showTrigRatios', e.target.checked)}
                                className="mr-2"
                            />
                            Show Trig Ratios
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showReferenceAngle}
                                onChange={(e) => handleInputChange('showReferenceAngle', e.target.checked)}
                                className="mr-2"
                            />
                            Show Reference Angle
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showCAST}
                                onChange={(e) => handleInputChange('showCAST', e.target.checked)}
                                className="mr-2"
                            />
                            Show CAST
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={polarData.showUnitCircle}
                                onChange={(e) => handleInputChange('showUnitCircle', e.target.checked)}
                                className="mr-2"
                            />
                            Show Unit Circle
                        </label>
                    </div>
                </div>
            </div>

            {/* Quick Angle Buttons */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h4 className="font-semibold text-blue-800 mb-3">Quick Angle Selection</h4>
                <div className="grid grid-cols-4 gap-2">
                    {[0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330].map((angle) => (
                        <button
                            key={angle}
                            onClick={() => setAngle(angle)}
                            className={`px-3 py-2 text-sm rounded border transition-colors ${
                                polarData.angle === angle
                                    ? 'bg-blue-600 text-white border-blue-600'
                                    : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
                            }`}
                        >
                            {angle}°
                        </button>
                    ))}
                </div>
                <div className="mt-3 flex space-x-2">
                    <button
                        onClick={generateRandomAngle}
                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                    >
                        Random Angle
                    </button>
                    <button
                        onClick={setCommonAngles}
                        className="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded text-sm"
                    >
                        Common Angle
                    </button>
                </div>
            </div>

            {/* CAST Rule Explanation */}
            <div className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                <h4 className="font-semibold text-yellow-800 mb-2">CAST Rule</h4>
                <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                        <strong className="text-green-600">A (All):</strong> 1st Quadrant - All ratios positive
                    </div>
                    <div>
                        <strong className="text-blue-600">S (Sine):</strong> 2nd Quadrant - Sine positive
                    </div>
                    <div>
                        <strong className="text-orange-600">T (Tangent):</strong> 3rd Quadrant - Tangent positive
                    </div>
                    <div>
                        <strong className="text-red-600">C (Cosine):</strong> 4th Quadrant - Cosine positive
                    </div>
                </div>
            </div>

            {/* Polar Coordinate Canvas */}
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

export default PolarCoordinateSystem;
