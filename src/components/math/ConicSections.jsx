import React, { useState, useEffect, useRef } from 'react';

const ConicSections = ({ initialData, onChange, isSubmitted }) => {
    const [conicData, setConicData] = useState(initialData || {
        title: "Conic Sections",
        conicType: 'circle',
        xRange: [-10, 10],
        yRange: [-10, 10],
        showGrid: true,
        showAxes: true,
        showFocus: true,
        showVertices: true,
        showCenter: true,
        showEquation: true,
        gridSpacing: 1,
        backgroundColor: '#ffffff',
        gridColor: '#e5e7eb',
        axisColor: '#374151',
        conicColor: '#3B82F6',
        focusColor: '#EF4444',
        vertexColor: '#F59E0B',
        centerColor: '#8B5CF6',
        // Circle parameters
        circleCenter: [0, 0],
        circleRadius: 3,
        // Ellipse parameters
        ellipseCenter: [0, 0],
        ellipseA: 4,
        ellipseB: 2,
        // Parabola parameters
        parabolaVertex: [0, 0],
        parabolaP: 1,
        parabolaDirection: 'right',
        // Hyperbola parameters
        hyperbolaCenter: [0, 0],
        hyperbolaA: 3,
        hyperbolaB: 2,
        hyperbolaDirection: 'horizontal'
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(conicData);
        }
    }, [conicData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawConicSection();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [conicData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawConicSection();
    }, []);

    const calculateEccentricity = () => {
        const { conicType, ellipseA, ellipseB, hyperbolaA, hyperbolaB } = conicData;
        
        switch (conicType) {
            case 'circle':
                return 0;
            case 'ellipse':
                const c = Math.sqrt(ellipseA * ellipseA - ellipseB * ellipseB);
                return c / ellipseA;
            case 'parabola':
                return 1;
            case 'hyperbola':
                const hypC = Math.sqrt(hyperbolaA * hyperbolaA + hyperbolaB * hyperbolaB);
                return hypC / hyperbolaA;
            default:
                return 0;
        }
    };

    const getEquation = () => {
        const { conicType, circleCenter, circleRadius, ellipseCenter, ellipseA, ellipseB, parabolaVertex, parabolaP, parabolaDirection, hyperbolaCenter, hyperbolaA, hyperbolaB, hyperbolaDirection } = conicData;
        
        switch (conicType) {
            case 'circle':
                const [cx, cy] = circleCenter;
                return `(x - ${cx})² + (y - ${cy})² = ${circleRadius}²`;
            case 'ellipse':
                const [ex, ey] = ellipseCenter;
                return `(x - ${ex})²/${ellipseA}² + (y - ${ey})²/${ellipseB}² = 1`;
            case 'parabola':
                const [px, py] = parabolaVertex;
                switch (parabolaDirection) {
                    case 'up':
                        return `(x - ${px})² = 4(${parabolaP})(y - ${py})`;
                    case 'down':
                        return `(x - ${px})² = -4(${parabolaP})(y - ${py})`;
                    case 'left':
                        return `(y - ${py})² = -4(${parabolaP})(x - ${px})`;
                    case 'right':
                        return `(y - ${py})² = 4(${parabolaP})(x - ${px})`;
                    default:
                        return `(y - ${py})² = 4(${parabolaP})(x - ${px})`;
                }
            case 'hyperbola':
                const [hx, hy] = hyperbolaCenter;
                if (hyperbolaDirection === 'horizontal') {
                    return `(x - ${hx})²/${hyperbolaA}² - (y - ${hy})²/${hyperbolaB}² = 1`;
                } else {
                    return `(y - ${hy})²/${hyperbolaA}² - (x - ${hx})²/${hyperbolaB}² = 1`;
                }
            default:
                return '';
        }
    };

    const drawConicSection = () => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.log('ConicSections: Canvas not found');
            return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('ConicSections: Canvas context not available');
            return;
        }

        const width = canvas.width;
        const height = canvas.height;

        console.log('ConicSections: Drawing with dimensions:', { width, height, conicType: conicData.conicType });

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = conicData.backgroundColor || '#ffffff';
        ctx.fillRect(0, 0, width, height);

        // Test drawing - draw a simple rectangle to verify canvas is working
        ctx.fillStyle = '#0000ff';
        ctx.fillRect(10, 10, 50, 50);

        const { xRange, yRange, showGrid, showAxes, showFocus, showVertices, showCenter, showEquation, gridSpacing, gridColor, axisColor, conicColor, focusColor, vertexColor, centerColor, conicType } = conicData;

        const margin = 60;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;

        // Scale factors
        const xScale = plotWidth / (xRange[1] - xRange[0]);
        const yScale = plotHeight / (yRange[1] - yRange[0]);

        const toCanvasX = (x) => margin + (x - xRange[0]) * xScale;
        const toCanvasY = (y) => height - margin - (y - yRange[0]) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = gridColor;
            ctx.lineWidth = 1;
            
            // Vertical grid lines
            for (let x = xRange[0]; x <= xRange[1]; x += gridSpacing) {
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, margin);
                ctx.lineTo(canvasX, height - margin);
                ctx.stroke();
            }
            
            // Horizontal grid lines
            for (let y = yRange[0]; y <= yRange[1]; y += gridSpacing) {
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(margin, canvasY);
                ctx.lineTo(width - margin, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        if (showAxes) {
            ctx.strokeStyle = axisColor;
            ctx.lineWidth = 2;
            
            // X-axis
            ctx.beginPath();
            ctx.moveTo(margin, toCanvasY(0));
            ctx.lineTo(width - margin, toCanvasY(0));
            ctx.stroke();
            
            // Y-axis
            ctx.beginPath();
            ctx.moveTo(toCanvasX(0), margin);
            ctx.lineTo(toCanvasX(0), height - margin);
            ctx.stroke();
        }

        // Draw conic section
        ctx.strokeStyle = conicColor;
        ctx.lineWidth = 3;
        ctx.beginPath();

        switch (conicType) {
            case 'circle':
                const [cx, cy] = conicData.circleCenter;
                const radius = conicData.circleRadius;
                const centerX = toCanvasX(cx);
                const centerY = toCanvasY(cy);
                const canvasRadius = radius * Math.min(xScale, yScale);
                
                ctx.arc(centerX, centerY, canvasRadius, 0, 2 * Math.PI);
                break;

            case 'ellipse':
                const [ex, ey] = conicData.ellipseCenter;
                const a = conicData.ellipseA;
                const b = conicData.ellipseB;
                const ellipseCenterX = toCanvasX(ex);
                const ellipseCenterY = toCanvasY(ey);
                const canvasA = a * xScale;
                const canvasB = b * yScale;
                
                ctx.ellipse(ellipseCenterX, ellipseCenterY, canvasA, canvasB, 0, 0, 2 * Math.PI);
                break;

            case 'parabola':
                const [px, py] = conicData.parabolaVertex;
                const p = conicData.parabolaP;
                const direction = conicData.parabolaDirection;
                
                // Draw parabola by plotting points
                const step = 0.1;
                let firstPoint = true;
                
                for (let t = -5; t <= 5; t += step) {
                    let x, y;
                    switch (direction) {
                        case 'up':
                            x = px + t;
                            y = py + (t * t) / (4 * p);
                            break;
                        case 'down':
                            x = px + t;
                            y = py - (t * t) / (4 * p);
                            break;
                        case 'left':
                            x = px - (t * t) / (4 * p);
                            y = py + t;
                            break;
                        case 'right':
                            x = px + (t * t) / (4 * p);
                            y = py + t;
                            break;
                        default:
                            x = px + (t * t) / (4 * p);
                            y = py + t;
                    }
                    
                    if (x >= xRange[0] && x <= xRange[1] && y >= yRange[0] && y <= yRange[1]) {
                        if (firstPoint) {
                            ctx.moveTo(toCanvasX(x), toCanvasY(y));
                            firstPoint = false;
                        } else {
                            ctx.lineTo(toCanvasX(x), toCanvasY(y));
                        }
                    }
                }
                break;

            case 'hyperbola':
                const [hx, hy] = conicData.hyperbolaCenter;
                const hypA = conicData.hyperbolaA;
                const hypB = conicData.hyperbolaB;
                const hypDirection = conicData.hyperbolaDirection;
                
                // Draw hyperbola by plotting points
                const hypStep = 0.1;
                let hypFirstPoint = true;
                
                for (let t = -5; t <= 5; t += hypStep) {
                    let x, y;
                    if (hypDirection === 'horizontal') {
                        x = hx + hypA * Math.cosh(t);
                        y = hy + hypB * Math.sinh(t);
                    } else {
                        x = hx + hypB * Math.sinh(t);
                        y = hy + hypA * Math.cosh(t);
                    }
                    
                    if (x >= xRange[0] && x <= xRange[1] && y >= yRange[0] && y <= yRange[1]) {
                        if (hypFirstPoint) {
                            ctx.moveTo(toCanvasX(x), toCanvasY(y));
                            hypFirstPoint = false;
                        } else {
                            ctx.lineTo(toCanvasX(x), toCanvasY(y));
                        }
                    }
                }
                
                // Draw second branch
                hypFirstPoint = true;
                for (let t = -5; t <= 5; t += hypStep) {
                    let x, y;
                    if (hypDirection === 'horizontal') {
                        x = hx - hypA * Math.cosh(t);
                        y = hy + hypB * Math.sinh(t);
                    } else {
                        x = hx + hypB * Math.sinh(t);
                        y = hy - hypA * Math.cosh(t);
                    }
                    
                    if (x >= xRange[0] && x <= xRange[1] && y >= yRange[0] && y <= yRange[1]) {
                        if (hypFirstPoint) {
                            ctx.moveTo(toCanvasX(x), toCanvasY(y));
                            hypFirstPoint = false;
                        } else {
                            ctx.lineTo(toCanvasX(x), toCanvasY(y));
                        }
                    }
                }
                break;
        }
        
        ctx.stroke();

        // Draw center
        if (showCenter) {
            let centerX, centerY;
            switch (conicType) {
                case 'circle':
                    [centerX, centerY] = conicData.circleCenter;
                    break;
                case 'ellipse':
                    [centerX, centerY] = conicData.ellipseCenter;
                    break;
                case 'hyperbola':
                    [centerX, centerY] = conicData.hyperbolaCenter;
                    break;
                default:
                    return;
            }
            
            ctx.fillStyle = centerColor;
            ctx.beginPath();
            ctx.arc(toCanvasX(centerX), toCanvasY(centerY), 6, 0, 2 * Math.PI);
            ctx.fill();
            
            ctx.fillStyle = centerColor;
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('C', toCanvasX(centerX), toCanvasY(centerY) + 5);
        }

        // Draw title and equation
        ctx.fillStyle = axisColor;
        ctx.font = 'bold 18px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(conicData.title, width / 2, 25);

        if (showEquation) {
            const equation = getEquation();
            ctx.font = '14px Arial';
            ctx.fillText(equation, width / 2, 45);
        }

        // Draw properties
        let yOffset = margin + 20;
        ctx.fillStyle = axisColor;
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'left';
        ctx.fillText('Properties:', width - margin, yOffset);
        
        ctx.font = '12px Arial';
        yOffset += 20;
        
        const eccentricity = calculateEccentricity();
        ctx.fillText(`Eccentricity: ${eccentricity.toFixed(3)}`, width - margin, yOffset);
        yOffset += 15;
        
        ctx.fillText(`Type: ${conicType.charAt(0).toUpperCase() + conicType.slice(1)}`, width - margin, yOffset);
    };

    const handleInputChange = (field, value) => {
        setConicData(prev => ({
            ...prev,
            [field]: field === 'xRange' || field === 'yRange' || field === 'gridSpacing' || 
                     field === 'circleRadius' || field === 'ellipseA' || field === 'ellipseB' ||
                     field === 'parabolaP' || field === 'hyperbolaA' || field === 'hyperbolaB' ? 
                     parseFloat(value) || 0 : value
        }));
    };

    const handleRangeChange = (axis, index, value) => {
        setConicData(prev => ({
            ...prev,
            [axis]: prev[axis].map((val, i) => i === index ? parseFloat(value) || 0 : val)
        }));
    };

    const handleCenterChange = (type, index, value) => {
        setConicData(prev => ({
            ...prev,
            [type]: prev[type].map((val, i) => i === index ? parseFloat(value) || 0 : val)
        }));
    };

    const setCommonConics = () => {
        const conics = [
            { type: 'circle', name: 'Unit Circle', params: { circleCenter: [0, 0], circleRadius: 1 } },
            { type: 'ellipse', name: 'Standard Ellipse', params: { ellipseCenter: [0, 0], ellipseA: 3, ellipseB: 2 } },
            { type: 'parabola', name: 'Standard Parabola', params: { parabolaVertex: [0, 0], parabolaP: 1, parabolaDirection: 'right' } },
            { type: 'hyperbola', name: 'Standard Hyperbola', params: { hyperbolaCenter: [0, 0], hyperbolaA: 2, hyperbolaB: 1, hyperbolaDirection: 'horizontal' } }
        ];
        
        const randomConic = conics[Math.floor(Math.random() * conics.length)];
        setConicData(prev => ({
            ...prev,
            conicType: randomConic.type,
            ...randomConic.params
        }));
    };

    const eccentricity = calculateEccentricity();
    const equation = getEquation();

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
                        value={conicData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Conic Type
                    </label>
                    <select
                        value={conicData.conicType}
                        onChange={(e) => handleInputChange('conicType', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="circle">Circle</option>
                        <option value="ellipse">Ellipse</option>
                        <option value="parabola">Parabola</option>
                        <option value="hyperbola">Hyperbola</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Grid Spacing
                    </label>
                    <input
                        type="number"
                        min="0.5"
                        max="2"
                        step="0.5"
                        value={conicData.gridSpacing}
                        onChange={(e) => handleInputChange('gridSpacing', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        X Range Min
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={conicData.xRange[0]}
                        onChange={(e) => handleRangeChange('xRange', 0, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        X Range Max
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={conicData.xRange[1]}
                        onChange={(e) => handleRangeChange('xRange', 1, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Y Range Min
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={conicData.yRange[0]}
                        onChange={(e) => handleRangeChange('yRange', 0, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Y Range Max
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={conicData.yRange[1]}
                        onChange={(e) => handleRangeChange('yRange', 1, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                {/* Circle parameters */}
                {conicData.conicType === 'circle' && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Center X
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.circleCenter[0]}
                                onChange={(e) => handleCenterChange('circleCenter', 0, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Center Y
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.circleCenter[1]}
                                onChange={(e) => handleCenterChange('circleCenter', 1, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Radius
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                min="0.1"
                                value={conicData.circleRadius}
                                onChange={(e) => handleInputChange('circleRadius', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                    </>
                )}

                {/* Ellipse parameters */}
                {conicData.conicType === 'ellipse' && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Center X
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.ellipseCenter[0]}
                                onChange={(e) => handleCenterChange('ellipseCenter', 0, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Center Y
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.ellipseCenter[1]}
                                onChange={(e) => handleCenterChange('ellipseCenter', 1, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Semi-major axis (a)
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                min="0.1"
                                value={conicData.ellipseA}
                                onChange={(e) => handleInputChange('ellipseA', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Semi-minor axis (b)
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                min="0.1"
                                value={conicData.ellipseB}
                                onChange={(e) => handleInputChange('ellipseB', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                    </>
                )}

                {/* Parabola parameters */}
                {conicData.conicType === 'parabola' && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Vertex X
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.parabolaVertex[0]}
                                onChange={(e) => handleCenterChange('parabolaVertex', 0, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Vertex Y
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.parabolaVertex[1]}
                                onChange={(e) => handleCenterChange('parabolaVertex', 1, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Parameter p
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                min="0.1"
                                value={conicData.parabolaP}
                                onChange={(e) => handleInputChange('parabolaP', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Direction
                            </label>
                            <select
                                value={conicData.parabolaDirection}
                                onChange={(e) => handleInputChange('parabolaDirection', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            >
                                <option value="up">Up</option>
                                <option value="down">Down</option>
                                <option value="left">Left</option>
                                <option value="right">Right</option>
                            </select>
                        </div>
                    </>
                )}

                {/* Hyperbola parameters */}
                {conicData.conicType === 'hyperbola' && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Center X
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.hyperbolaCenter[0]}
                                onChange={(e) => handleCenterChange('hyperbolaCenter', 0, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Center Y
                            </label>
                            <input
                                type="number"
                                step="0.5"
                                value={conicData.hyperbolaCenter[1]}
                                onChange={(e) => handleCenterChange('hyperbolaCenter', 1, e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Semi-transverse axis (a)
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                min="0.1"
                                value={conicData.hyperbolaA}
                                onChange={(e) => handleInputChange('hyperbolaA', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Semi-conjugate axis (b)
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                min="0.1"
                                value={conicData.hyperbolaB}
                                onChange={(e) => handleInputChange('hyperbolaB', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Direction
                            </label>
                            <select
                                value={conicData.hyperbolaDirection}
                                onChange={(e) => handleInputChange('hyperbolaDirection', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            >
                                <option value="horizontal">Horizontal</option>
                                <option value="vertical">Vertical</option>
                            </select>
                        </div>
                    </>
                )}

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={conicData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={conicData.showAxes}
                                onChange={(e) => handleInputChange('showAxes', e.target.checked)}
                                className="mr-2"
                            />
                            Show Axes
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={conicData.showFocus}
                                onChange={(e) => handleInputChange('showFocus', e.target.checked)}
                                className="mr-2"
                            />
                            Show Focus
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={conicData.showVertices}
                                onChange={(e) => handleInputChange('showVertices', e.target.checked)}
                                className="mr-2"
                            />
                            Show Vertices
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={conicData.showCenter}
                                onChange={(e) => handleInputChange('showCenter', e.target.checked)}
                                className="mr-2"
                            />
                            Show Center
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={conicData.showEquation}
                                onChange={(e) => handleInputChange('showEquation', e.target.checked)}
                                className="mr-2"
                            />
                            Show Equation
                        </label>
                    </div>
                </div>
            </div>

            {/* Quick Actions */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h4 className="font-semibold text-blue-800 mb-3">Quick Actions</h4>
                <div className="flex space-x-2">
                    <button
                        onClick={setCommonConics}
                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                    >
                        Random Conic
                    </button>
                </div>
            </div>

            {/* Properties Summary */}
            <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                <h4 className="font-semibold text-green-800 mb-3">Conic Properties</h4>
                <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                        <strong>Type:</strong> {conicData.conicType.charAt(0).toUpperCase() + conicData.conicType.slice(1)}
                    </div>
                    <div>
                        <strong>Eccentricity:</strong> {eccentricity.toFixed(3)}
                    </div>
                    <div className="col-span-2">
                        <strong>Equation:</strong> {equation}
                    </div>
                </div>
            </div>

            {/* Conic Section Canvas */}
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

export default ConicSections;
