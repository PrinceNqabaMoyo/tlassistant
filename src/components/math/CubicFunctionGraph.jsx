import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const CubicFunctionGraph = ({ initialData, onChange, isSubmitted }) => {
    const [a, setA] = useState(initialData?.a?.toString() || '1');
    const [b, setB] = useState(initialData?.b?.toString() || '-2');
    const [c, setC] = useState(initialData?.c?.toString() || '-3');
    const [d, setD] = useState(initialData?.d?.toString() || '1');
    const [title, setTitle] = useState(initialData?.title || 'Cubic Function');
    const [equationInput, setEquationInput] = useState('');
    const [xMin, setXMin] = useState(initialData?.x_range?.[0] || -5);
    const [xMax, setXMax] = useState(initialData?.x_range?.[1] || 5);
    const [yMin, setYMin] = useState(initialData?.y_range?.[0] || -20);
    const [yMax, setYMax] = useState(initialData?.y_range?.[1] || 20);
    const [lineColor, setLineColor] = useState(initialData?.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData?.showGrid !== false);
    const [showPoints, setShowPoints] = useState(initialData?.showPoints !== false);
    const [showRoots, setShowRoots] = useState(initialData?.showRoots !== false);
    const [showTurningPoints, setShowTurningPoints] = useState(initialData?.showTurningPoints !== false);
    const [editMode, setEditMode] = useState(initialData?.editMode || 'parameters');

    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    // Convert string values to numbers for calculations
    const aNum = Number(a) || 0;
    const bNum = Number(b) || 0;
    const cNum = Number(c) || 0;
    const dNum = Number(d) || 0;

    // Parse equation string to extract coefficients
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
            return { a: aNum, b: bNum, c: cNum, d: dNum };
        }
    };

    const parseRightSide = (rightSide) => {
        let a = 0, b = 0, c = 0, d = 0;
        
        // Handle cases like "x³-4x", "2x³+x²-3x+1", "x³", "x²+2x", "3"
        const terms = rightSide.split(/(?=[+-])/);
        
        terms.forEach(term => {
            const cleanTerm = term.trim();
            if (cleanTerm.includes('x³')) {
                const coef = cleanTerm.replace('x³', '').trim();
                if (coef === '' || coef === '+') a = 1;
                else if (coef === '-') a = -1;
                else a = parseFloat(coef) || 0;
            } else if (cleanTerm.includes('x²')) {
                const coef = cleanTerm.replace('x²', '').trim();
                if (coef === '' || coef === '+') b = 1;
                else if (coef === '-') b = -1;
                else b = parseFloat(coef) || 0;
            } else if (cleanTerm.includes('x') && !cleanTerm.includes('x²') && !cleanTerm.includes('x³')) {
                const coef = cleanTerm.replace('x', '').trim();
                if (coef === '' || coef === '+') c = 1;
                else if (coef === '-') c = -1;
                else c = parseFloat(coef) || 0;
            } else if (cleanTerm !== '' && cleanTerm !== '+' && cleanTerm !== '-') {
                d = parseFloat(cleanTerm) || 0;
            }
        });
        
        return { a, b, c, d };
    };

    // Update equation when coefficients change
    useEffect(() => {
        let equation = '';
        if (aNum !== 0) {
            if (aNum === 1) equation += 'x³';
            else if (aNum === -1) equation += '-x³';
            else equation += `${aNum}x³`;
        }
        
        if (bNum !== 0) {
            if (bNum > 0 && equation !== '') equation += '+';
            if (bNum === 1) equation += 'x²';
            else if (bNum === -1) equation += '-x²';
            else equation += `${bNum}x²`;
        }
        
        if (cNum !== 0) {
            if (cNum > 0 && equation !== '') equation += '+';
            if (cNum === 1) equation += 'x';
            else if (cNum === -1) equation += '-x';
            else equation += `${cNum}x`;
        }
        
        if (dNum !== 0) {
            if (dNum > 0 && equation !== '') equation += '+';
            equation += `${dNum}`;
        }
        
        // Handle edge case where all coefficients are 0
        if (equation === '') equation = '0';
        
        setEquationInput(equation);
    }, [aNum, bNum, cNum, dNum]);

    // Update internal state only once when component mounts
    useEffect(() => {
        if (initialData) {
            setA(initialData.a?.toString() || '1');
            setB(initialData.b?.toString() || '-2');
            setC(initialData.c?.toString() || '-3');
            setD(initialData.d?.toString() || '1');
            setTitle(initialData.title || 'Cubic Function');

            setXMin(initialData.x_range?.[0] || -5);
            setXMax(initialData.x_range?.[1] || 5);
            setYMin(initialData.y_range?.[0] || -20);
            setYMax(initialData.y_range?.[1] || 20);
            setLineColor(initialData.lineColor || '#3B82F6');
            setShowGrid(initialData.showGrid !== false);
            setShowPoints(initialData.showPoints !== false);
            setShowRoots(initialData.showRoots !== false);
            setShowTurningPoints(initialData.showTurningPoints !== false);
            
            // Set editMode from initialData
            if (initialData.editMode) {
                setEditMode(initialData.editMode);
            }
        }
    }, []); // Only run once on mount

    // Update coefficients when equation changes
    const handleEquationChange = (newEquation) => {
        const { a, b, c, d } = parseEquation(newEquation);
        setA(a.toString());
        setB(b.toString());
        setC(c.toString());
        setD(d.toString());
        setEquationInput(newEquation);
    };

        // Simple onChange implementation like in original workspace
    useEffect(() => {
        if (onChange) {
            const formattedData = {
                type: "cubic_graph",
                title: title,
                a: aNum,
                b: bNum,
                c: cNum,
                d: dNum,
                x_range: [xMin, xMax],
                y_range: [yMin, yMax],
                lineColor: lineColor,
                showGrid: showGrid,
                showPoints: showPoints,
                showRoots: showRoots,
                showTurningPoints: showTurningPoints,
                editMode: editMode
            };
            
            // Only call onChange if the data has actually changed from initial values
            if (initialData) {
                const hasChanged =
                    aNum !== initialData.a ||
                    bNum !== initialData.b ||
                    cNum !== initialData.c ||
                    dNum !== initialData.d ||
                    xMin !== initialData.x_range?.[0] ||
                    xMax !== initialData.x_range?.[1] ||
                    yMin !== initialData.y_range?.[0] ||
                    yMax !== initialData.y_range?.[1] ||
                    lineColor !== initialData.lineColor ||
                    showGrid !== initialData.showGrid ||
                    showPoints !== initialData.showPoints ||
                    showRoots !== initialData.showRoots ||
                    showTurningPoints !== initialData.showTurningPoints ||
                    title !== initialData.title ||
                    editMode !== initialData.editMode;

                if (hasChanged) {
                    onChange(formattedData);
                }
            } else {
                // If no initialData, always call onChange for default values
                onChange(formattedData);
            }
        }
    }, [a, b, c, d, xMin, xMax, yMin, yMax, title, lineColor, showGrid, showPoints, showRoots, showTurningPoints, editMode, onChange, initialData]);

    // Single useEffect to handle all drawing - prevents duplicate calls
    useEffect(() => {
        // Only draw on the main canvas when not in fullscreen
        if (!isFullScreenOpen) {
            const timer = setTimeout(() => {
                drawGraph();
            }, 50); // Reduced delay for more responsive parameter changes

            return () => clearTimeout(timer);
        }
    }, [a, b, c, d, xMin, xMax, yMin, yMax, title, lineColor, showGrid, showPoints, showRoots, showTurningPoints, isFullScreenOpen]);

    // Initial draw when component mounts
    useEffect(() => {
        drawGraph();
    }, []);

    // Set initial equation when component mounts
    useEffect(() => {
        // Always set initial equation based on default coefficients
        const initialA = initialData?.a || 1;
        const initialB = initialData?.b || -2;
        const initialC = initialData?.c || -3;
        const initialD = initialData?.d || 1;
        
        let equation = '';
        if (initialA !== 0) {
            if (initialA === 1) equation += 'x³';
            else if (initialA === -1) equation += '-x³';
            else equation += `${initialA}x³`;
        }
        
        if (initialB !== 0) {
            if (initialB > 0 && equation !== '') equation += '+';
            if (initialB === 1) equation += 'x²';
            else if (initialB === -1) equation += '-x²';
            else equation += `${initialB}x²`;
        }
        
        if (initialC !== 0) {
            if (initialC > 0 && equation !== '') equation += '+';
            if (initialC === 1) equation += 'x';
            else if (initialC === -1) equation += '-x';
            else equation += `${initialC}x`;
        }
        
        if (initialD !== 0) {
            if (initialD > 0 && equation !== '') equation += '+';
            equation += `${initialD}`;
        }
        
        if (equation === '') equation = '0';
        
        setEquationInput(equation);
    }, []);

    // Redraw full-screen canvas when modal opens or data changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            drawGraph(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, a, b, c, d, xMin, xMax, yMin, yMax, lineColor, showGrid, showPoints, showRoots, showTurningPoints]);

    // Calculate cubic function value
    const calculateCubic = (x, a, b, c, d) => {
        return a * Math.pow(x, 3) + b * Math.pow(x, 2) + c * x + d;
    };

    // Find roots using Newton's method approximation
    const findRoots = (a, b, c, d, xRange) => {
        // Validate xRange
        if (!xRange || !Array.isArray(xRange) || xRange.length < 2) {
            return [];
        }
        
        const roots = [];
        const step = 0.5;
        
        for (let x = xRange[0]; x <= xRange[1]; x += step) {
            let currentX = x;
            let iterations = 0;
            const maxIterations = 100;
            
            while (iterations < maxIterations) {
                const fx = calculateCubic(currentX, aNum, bNum, cNum, dNum);
                const fPrime = 3 * aNum * Math.pow(currentX, 2) + 2 * bNum * currentX + cNum;
                
                if (Math.abs(fPrime) < 1e-10) break;
                
                const nextX = currentX - fx / fPrime;
                
                if (Math.abs(nextX - currentX) < 1e-6) {
                    // Check if this root is already found (within tolerance)
                    const isDuplicate = roots.some(root => Math.abs(root - nextX) < 0.1);
                    if (!isDuplicate && Math.abs(fx) < 0.1) {
                        roots.push(parseFloat(nextX.toFixed(3)));
                    }
                    break;
                }
                
                currentX = nextX;
                iterations++;
            }
        }
        
        return roots.sort((a, b) => a - b);
    };

    // Find turning points (where derivative = 0)
    const findTurningPoints = (a, b, c, d, xRange) => {
        // Validate xRange
        if (!xRange || !Array.isArray(xRange) || xRange.length < 2) {
            return [];
        }
        
        if (Math.abs(a) < 1e-10) return []; // Not a cubic function
        
        // Solve quadratic equation: 3ax² + 2bx + c = 0
        const discriminant = 4 * b * b - 12 * a * c;
        
        if (discriminant < 0) return [];
        
        const x1 = (-2 * b + Math.sqrt(discriminant)) / (6 * a);
        const x2 = (-2 * b - Math.sqrt(discriminant)) / (6 * a);
        
        const turningPoints = [];
        
        if (x1 >= xRange[0] && x1 <= xRange[1]) {
            turningPoints.push({
                x: x1,
                y: calculateCubic(x1, aNum, bNum, cNum, dNum),
                type: 'turning'
            });
        }
        
        if (x2 >= xRange[0] && x2 <= xRange[1]) {
            turningPoints.push({
                x: x2,
                y: calculateCubic(x2, aNum, bNum, cNum, dNum),
                type: 'turning'
            });
        }
        
        return turningPoints.sort((a, b) => a.x - b.x);
    };

    // HiDPI Canvas Setup
    const setupCanvas = (canvas) => {
        const ctx = canvas.getContext('2d');
        const dpr = window.devicePixelRatio || 1;
        const rect = canvas.getBoundingClientRect();
        
        // Set actual size in memory (scaled up for HiDPI)
        canvas.width = rect.width * dpr;
        canvas.height = rect.height * dpr;
        
        // Scale the drawing context so everything draws at the correct size
        ctx.scale(dpr, dpr);
        
        // Set the display size (CSS pixels)
        canvas.style.width = rect.width + 'px';
        canvas.style.height = rect.height + 'px';
        
        return { ctx, width: rect.width, height: rect.height };
    };

    const drawGraph = (targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) {
            console.log('CubicFunctionGraph: Canvas not found');
            return;
        }

        // Check if we have valid graph data before proceeding
        if (xMin >= xMax || yMin >= yMax) {
            console.log('CubicFunctionGraph: Invalid range values, skipping draw');
            return;
        }

        const { ctx, width, height } = setupCanvas(canvas);

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff'; // White background
        ctx.fillRect(0, 0, width, height);

        // Calculate scale factors
        const xScale = width / (xMax - xMin);
        const yScale = height / (yMax - yMin);

        // Helper function to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - xMin) * xScale;
        const toCanvasY = (y) => height - (y - yMin) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB'; // Subtle grey grid lines
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = xMin; x <= xMax; x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = yMin; y <= yMax; y++) {
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

        // Draw the cubic function
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 3;
        ctx.beginPath();

        const step = (xMax - xMin) / width;
        let firstPoint = true;

        for (let x = xMin; x <= xMax; x += step) {
            const y = calculateCubic(x, aNum, bNum, cNum, dNum);
            const canvasX = toCanvasX(x);
            const canvasY = toCanvasY(y);

            if (firstPoint) {
                ctx.moveTo(canvasX, canvasY);
                firstPoint = false;
            } else {
                ctx.lineTo(canvasX, canvasY);
            }
        }

        ctx.stroke();

        // Draw points if enabled
        if (showPoints) {
            ctx.fillStyle = lineColor;
            const numPoints = 20;
            for (let i = 0; i <= numPoints; i++) {
                const x = xMin + (xMax - xMin) * i / numPoints;
                const y = calculateCubic(x, aNum, bNum, cNum, dNum);
                const canvasX = toCanvasX(x);
                const canvasY = toCanvasY(y);

                if (canvasY >= 0 && canvasY <= height) {
                    ctx.beginPath();
                    ctx.arc(canvasX, canvasY, 3, 0, 2 * Math.PI);
                    ctx.fill();
                }
            }
        }

        // Initialize points to draw array
        const pointsToDraw = [];

        // Draw roots if enabled
        if (showRoots) {
            const roots = findRoots(a, b, c, d, [xMin, xMax]);
            
            roots.forEach((root, index) => {
                if (root >= xMin && root <= xMax) {
                    const canvasX = toCanvasX(root);
                    const canvasY = toCanvasY(0);

                    if (canvasX >= 0 && canvasX <= width) {
                        // Use different colors for different roots
                        const rootColors = ['#EF4444', '#10B981', '#3B82F6'];
                        const rootColor = rootColors[index] || '#10B981';
                        
                        ctx.fillStyle = rootColor;
                        ctx.beginPath();
                        ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
                        ctx.fill();

                        pointsToDraw.push({
                            type: 'root',
                            color: rootColor,
                            text: `(${root.toFixed(2)}, 0)`
                        });
                    }
                }
            });
        }

        // Draw turning points if enabled
        if (showTurningPoints) {
            const turningPoints = findTurningPoints(a, b, c, d, [xMin, xMax]);
            
            turningPoints.forEach((point, index) => {
                if (point.x >= xMin && point.x <= xMax && point.y >= yMin && point.y <= yMax) {
                    const canvasX = toCanvasX(point.x);
                    const canvasY = toCanvasY(point.y);

                    if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                        // Use different colors for different turning points
                        const turningPointColors = ['#F97316', '#8B5CF6'];
                        const turningPointColor = turningPointColors[index] || '#F97316';
                        
                        ctx.fillStyle = turningPointColor;
                        ctx.beginPath();
                        ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
                        ctx.fill();

                        pointsToDraw.push({
                            type: 'turning_point',
                            color: turningPointColor,
                            text: `(${point.x.toFixed(2)}, ${point.y.toFixed(2)})`
                        });
                    }
                }
            });
        }

        // Add y-intercept point
        if (0 >= xMin && 0 <= xMax) {
            const yIntercept = calculateCubic(0, aNum, bNum, cNum, dNum);
            if (yIntercept >= yMin && yIntercept <= yMax) {
                const canvasX = toCanvasX(0);
                const canvasY = toCanvasY(yIntercept);
                
                ctx.fillStyle = '#3B82F6';
                ctx.beginPath();
                ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
                ctx.fill();
                
                pointsToDraw.push({
                    type: 'y_intercept',
                    color: '#3B82F6',
                    text: `(0, ${yIntercept.toFixed(2)})`
                });
            }
        }

        // Draw coordinate container
        if (pointsToDraw.length > 0) {
            const containerX = 20;
            const containerY = 60;
            const lineHeight = 20;
            const containerHeight = pointsToDraw.length * lineHeight + 20;
            
            // Calculate max text width
            ctx.font = 'bold 12px Arial';
            let maxTextWidth = 0;
            pointsToDraw.forEach(point => {
                const textWidth = ctx.measureText(point.text).width;
                maxTextWidth = Math.max(maxTextWidth, textWidth);
            });
            
            const containerWidth = maxTextWidth + 60; // Extra space for color squares and padding
            
            // Draw container background
            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
            ctx.fillRect(containerX, containerY, containerWidth, containerHeight);
            
            // Draw container border
            ctx.strokeStyle = '#000000';
            ctx.lineWidth = 2;
            ctx.strokeRect(containerX, containerY, containerWidth, containerHeight);
            
            // Draw each coordinate line
            pointsToDraw.forEach((point, index) => {
                const lineY = containerY + 15 + index * lineHeight;
                
                // Draw color square
                ctx.fillStyle = point.color;
                ctx.fillRect(containerX + 8, lineY - 6, 12, 12);
                
                // Draw coordinates text
                ctx.fillStyle = '#000000';
                ctx.textAlign = 'left';
                ctx.fillText(point.text, containerX + 25, lineY + 4);
            });
        }

        // Draw axis labels
        ctx.fillStyle = '#000000'; // Black labels
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
        ctx.fillText(title, width / 2, 25);
    };

    const handleInputChange = (field, value) => {
        switch (field) {
            case 'a': setA(value); break;
            case 'b': setB(value); break;
            case 'c': setC(value); break;
            case 'd': setD(value); break;
            case 'title': setTitle(value); break;

            case 'lineColor': setLineColor(value); break;
            case 'editMode': setEditMode(value); break;
            case 'showGrid': setShowGrid(value); break;
            case 'showPoints': setShowPoints(value); break;
            case 'showRoots': setShowRoots(value); break;
            case 'showTurningPoints': setShowTurningPoints(value); break;
            default: break;
        }
    };

    const handleRangeChange = (rangeType, index, value) => {
        if (rangeType === 'x_range') {
            if (index === 0) setXMin(parseFloat(value) || -5);
            else setXMax(parseFloat(value) || 5);
        } else {
            if (index === 0) setYMin(parseFloat(value) || -20);
            else setYMax(parseFloat(value) || 20);
        }
    };



    const handleToggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    const handleOpenFullScreen = () => {
        setIsFullScreenOpen(true);
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
                <h3 className="font-semibold text-gray-800 mb-4">Cubic Function Parameters</h3>
            
            {/* Edit Mode Toggle */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Edit Mode</h4>
                <div className="flex space-x-2">
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="parameters"
                            checked={editMode === 'parameters'}
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
                            checked={editMode === 'equation'}
                            onChange={(e) => handleInputChange('editMode', e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Equation</span>
                    </label>
                </div>
            </div>

            {/* Equation Editor */}
            {editMode === 'equation' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Equation:</label>
                        <input
                            type="text"
                            value={equationInput}
                            onChange={(e) => handleEquationChange(e.target.value)}
                            placeholder="e.g., x³ - 4x, 2x³ + x² - 3x + 1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                            disabled={isSubmitted}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                            Format: ax³ + bx² + cx + d or y = ax³ + bx² + cx + d
                        </p>
                    </div>
                </div>
            )}

            {/* Parameter Editor */}
            {editMode === 'parameters' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                        <input
                            type="text"
                            value={title}
                            onChange={(e) => handleInputChange('title', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient a (x³):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={a}
                            onChange={(e) => handleInputChange('a', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient b (x²):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={b}
                            onChange={(e) => handleInputChange('b', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient c (x):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={c}
                            onChange={(e) => handleInputChange('c', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient d (constant):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={d}
                            onChange={(e) => handleInputChange('d', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
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
                            step="0.5"
                            value={[xMin, xMax]?.[0] || -5}
                            onChange={(e) => handleRangeChange('x_range', 0, e.target.value)}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Max:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={[xMin, xMax]?.[1] || 5}
                            onChange={(e) => handleRangeChange('x_range', 1, e.target.value)}
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
                            value={[yMin, yMax]?.[0] || -20}
                            onChange={(e) => handleRangeChange('y_range', 0, e.target.value)}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Y Max:</label>
                        <input
                            type="number"
                            step="1"
                            value={[yMin, yMax]?.[1] || 20}
                            onChange={(e) => handleRangeChange('y_range', 1, e.target.value)}
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
                        checked={showGrid}
                        onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={showPoints}
                        onChange={(e) => handleInputChange('showPoints', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Points</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={showRoots}
                        onChange={(e) => handleInputChange('showRoots', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Roots</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={showTurningPoints}
                        onChange={(e) => handleInputChange('showTurningPoints', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Turning Points</span>
                </label>
            </div>

            {/* Line Color */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                <input
                    type="color"
                    value={lineColor}
                    onChange={(e) => handleInputChange('lineColor', e.target.value)}
                    className="w-full h-10 border border-gray-300 rounded-md"
                    disabled={isSubmitted}
                />
            </div>

            {/* Function Information */}
            <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                <h4 className="font-medium text-blue-800 mb-2">Function Information</h4>
                <div className="space-y-1 text-sm">
                                                <div><strong>Equation:</strong> y = {equationInput}</div>
                    <div><strong>Coefficient a (x³):</strong> {aNum}</div>
                    <div><strong>Coefficient b (x²):</strong> {bNum}</div>
                    <div><strong>Coefficient c (x):</strong> {cNum}</div>
                    <div><strong>Coefficient d (constant):</strong> {dNum}</div>
                    {showRoots && (
                        <div><strong>Roots:</strong> {findRoots(aNum, bNum, cNum, dNum, [xMin, xMax]).join(', ') || 'None found in range'}</div>
                    )}
                    {showTurningPoints && (
                        <div><strong>Turning Points:</strong> {findTurningPoints(aNum, bNum, cNum, dNum, [xMin, xMax]).map(p => `(${p.x.toFixed(2)}, ${p.y.toFixed(2)})`).join(', ') || 'None found in range'}</div>
                    )}
                </div>
            </div>
        </div>
    );



    return (
        <div className="relative">
            <div className="p-4 bg-white border border-gray-300 rounded-lg mt-2">
                <div className="flex items-center justify-end mb-2">
                    <button
                        onClick={handleOpenFullScreen}
                        className="p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow-lg transition-colors"
                        title="Open Full Screen Mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>

                {/* Edit Mode Toggle */}
                <div className="mb-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="radio"
                                value="parameters"
                                checked={editMode === 'parameters'}
                                onChange={(e) => handleInputChange('editMode', e.target.value)}
                                className="mr-2"
                                disabled={isSubmitted}
                            />
                            <span className="text-sm font-medium text-gray-700">Edit Parameters</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="radio"
                                value="equation"
                                checked={editMode === 'equation'}
                                onChange={(e) => handleInputChange('editMode', e.target.value)}
                                className="mr-2"
                                disabled={isSubmitted}
                            />
                            <span className="text-sm font-medium text-gray-700">Edit Equation</span>
                        </label>
                    </div>
                </div>

                {/* Quick Controls */}
                {editMode === 'parameters' ? (
                    <div className="grid grid-cols-5 gap-4 mb-2">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">a (x³):</label>
                            <input
                                type="number"
                                step="0.1"
                                value={a}
                                onChange={(e) => handleInputChange('a', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">b (x²):</label>
                            <input
                                type="number"
                                step="0.1"
                                value={b}
                                onChange={(e) => handleInputChange('b', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">c (x):</label>
                            <input
                                type="number"
                                step="0.1"
                                value={c}
                                onChange={(e) => handleInputChange('c', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">d (const):</label>
                            <input
                                type="number"
                                step="0.1"
                                value={d}
                                onChange={(e) => handleInputChange('d', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                            <input
                                type="color"
                                value={lineColor}
                                onChange={(e) => handleInputChange('lineColor', e.target.value)}
                                className="w-full h-10 border border-gray-300 rounded-md"
                                disabled={isSubmitted}
                            />
                        </div>
                    </div>
                ) : (
                    <div className="mb-2">
                        <label className="block text-sm font-medium text-gray-700 mb-1">Equation:</label>
                        <input
                            type="text"
                            value={equationInput}
                            onChange={(e) => handleEquationChange(e.target.value)}
                            placeholder="e.g., x³ - 4x, 2x³ + x² - 3x + 1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                            disabled={isSubmitted}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                            Format: ax³ + bx² + cx + d or y = ax³ + bx² + cx + d (e.g., "x³ - 4x", "2x³ + x² - 3x + 1")
                        </p>
                    </div>
                )}



                {/* Graph Canvas */}
                <div className="border border-gray-300 rounded-lg overflow-hidden">
                    <canvas
                        ref={canvasRef}
                        width={600}
                        height={400}
                        className="w-full h-auto"
                    />
                </div>

                {/* Full Screen Modal */}
                <FullScreenModal
                    isOpen={isFullScreenOpen}
                    onClose={handleCloseFullScreen}
                    title="Cubic Function Graph - Full Screen Mode"
                    onToggleFullScreen={handleToggleFullScreen}
                    isFullScreen={isFullScreen}
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
        </div>
);
};

export default CubicFunctionGraph;
