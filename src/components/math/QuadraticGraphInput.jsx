import React, { useState, useEffect, useRef } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const QuadraticGraphInput = ({ initialData, onChange, isSubmitted, onAttachToAnswer }) => {
    const [a, setA] = useState(initialData?.a || '1');
    const [b, setB] = useState(initialData?.b || '0');
    const [c, setC] = useState(initialData?.c || '0');
    const [title, setTitle] = useState(initialData?.title || 'Quadratic Function');
    const [lineColor, setLineColor] = useState(initialData?.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData?.showGrid !== false);
    const [showPoints, setShowPoints] = useState(initialData?.showPoints !== false);
    const [showVertex, setShowVertex] = useState(initialData?.showVertex !== false);
    const [showRoots, setShowRoots] = useState(initialData?.showRoots !== false);
    const [xMin, setXMin] = useState(initialData?.x_range?.[0] || -5);
    const [xMax, setXMax] = useState(initialData?.x_range?.[1] || 5);
    const [yMin, setYMin] = useState(initialData?.y_range?.[0] || -5);
    const [yMax, setYMax] = useState(initialData?.y_range?.[1] || 5);
    
    // New state for equation toggle and variable symbols
    const [activeTab, setActiveTab] = useState('parameters'); // 'parameters' or 'equation'
    const [equationInput, setEquationInput] = useState('');

    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);

    // Calculate quadratic properties
    const aNum = Number(a) || 0;
    const bNum = Number(b) || 0;
    const cNum = Number(c) || 0;
    
    // Mathematical properties
    const discriminant = bNum * bNum - 4 * aNum * cNum;
    const vertexX = aNum !== 0 ? -bNum / (2 * aNum) : 0;
    const vertexY = aNum !== 0 ? aNum * vertexX * vertexX + bNum * vertexX + cNum : cNum;
    const roots = aNum !== 0 ? (() => {
        if (discriminant > 0) {
            const sqrtDisc = Math.sqrt(discriminant);
            return [(-bNum + sqrtDisc) / (2 * aNum), (-bNum - sqrtDisc) / (2 * aNum)];
        } else if (discriminant === 0) {
            return [-bNum / (2 * aNum)];
        } else {
            return [];
        }
    })() : [];
    const yIntercept = cNum;
    const direction = aNum > 0 ? 'Upward' : aNum < 0 ? 'Downward' : 'Horizontal';

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

    useEffect(() => {
        if (onChange) {
            const formattedData = {
                type: "quadratic_graph",
                title: title,
                a: aNum,
                b: bNum,
                c: cNum,
                x_range: [xMin, xMax],
                y_range: [yMin, yMax],
                lineColor: lineColor,
                showGrid: showGrid,
                showPoints: showPoints,
                showVertex: showVertex,
                showRoots: showRoots
            };
            
            // Only call onChange if the data has actually changed from initial values
            // This prevents infinite loops when the component first mounts
            if (initialData) {
                const hasChanged = 
                    aNum !== initialData.a ||
                    bNum !== initialData.b ||
                    cNum !== initialData.c ||
                    xMin !== initialData.x_range?.[0] ||
                    xMax !== initialData.x_range?.[1] ||
                    yMin !== initialData.y_range?.[0] ||
                    yMax !== initialData.y_range?.[1] ||
                    lineColor !== initialData.lineColor ||
                    showGrid !== initialData.showGrid ||
                    showPoints !== initialData.showPoints ||
                    showVertex !== initialData.showVertex ||
                    showRoots !== initialData.showRoots;
                
                if (hasChanged) {
                    onChange(formattedData);
                }
            }
        }
    }, [a, b, c, xMin, xMax, yMin, yMax, title, lineColor, showGrid, showPoints, showVertex, showRoots, onChange, initialData]);

    // Single useEffect to handle all drawing - prevents duplicate calls
    useEffect(() => {
        // Only draw on the main canvas when not in fullscreen
        if (!isFullScreenOpen) {
            const timer = setTimeout(() => {
                drawGraph();
            }, 100);
            
            return () => clearTimeout(timer);
        }
    }, [a, b, c, xMin, xMax, yMin, yMax, title, lineColor, showGrid, showPoints, showVertex, showRoots, isFullScreenOpen]);

    // Update internal state when initialData changes
    useEffect(() => {
        if (initialData) {
            setA(initialData.a?.toString() || '1');
            setB(initialData.b?.toString() || '0');
            setC(initialData.c?.toString() || '0');
            setTitle(initialData.title || 'Quadratic Function');
            setLineColor(initialData.lineColor || '#3B82F6');
            setShowGrid(initialData.showGrid !== false);
            setShowPoints(initialData.showPoints !== false);
            setShowVertex(initialData.showVertex !== false);
            setShowRoots(initialData.showRoots !== false);
            setXMin(initialData.x_range?.[0] || -5);
            setXMax(initialData.x_range?.[1] || 5);
            setYMin(initialData.y_range?.[0] || -5);
            setYMax(initialData.y_range?.[1] || 5);
            
            // Initialize equation input with the equation from initialData
            if (initialData.equation) {
                setEquationInput(initialData.equation);
            }
        }
    }, []); // Only run once on mount

    // Redraw full-screen canvas when modal opens or data changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            // Only draw on fullscreen canvas when modal is open
            drawGraph(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, a, b, c, xMin, xMax, yMin, yMax, title, lineColor, showGrid, showPoints, showVertex, showRoots]);

    // Parse equation string to extract a, b, and c
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
            return { a: aNum, b: bNum, c: cNum };
        }
    };

    const parseRightSide = (rightSide) => {
        let a = 0, b = 0, c = 0;
        
        // Handle cases like "x²+2x+1", "2x²-3x+5", "x²", "2x²", "x²+2x", "2x+1"
        const terms = rightSide.split(/(?=[+-])/);
        
        terms.forEach(term => {
            if (term.includes('x²') || term.includes('x^2')) {
                const coef = term.replace('x²', '').replace('x^2', '');
                if (coef === '' || coef === '+') a = 1;
                else if (coef === '-') a = -1;
                else a = parseFloat(coef);
            } else if (term.includes('x')) {
                const coef = term.replace('x', '');
                if (coef === '' || coef === '+') b = 1;
                else if (coef === '-') b = -1;
                else b = parseFloat(coef);
            } else {
                c = parseFloat(term) || 0;
            }
        });
        
        return { a, b, c };
    };

    // Update equation when a, b, or c changes
    useEffect(() => {
        let equation = '';
        if (aNum !== 0) {
            if (aNum === 1) equation += 'x²';
            else if (aNum === -1) equation += '-x²';
            else equation += `${aNum}x²`;
        }
        
        if (bNum !== 0) {
            if (bNum > 0 && equation !== '') equation += '+';
            if (bNum === 1) equation += 'x';
            else if (bNum === -1) equation += '-x';
            else equation += `${bNum}x`;
        }
        
        if (cNum !== 0) {
            if (cNum > 0 && equation !== '') equation += '+';
            equation += `${cNum}`;
        }
        
        // Handle edge case where all coefficients are 0
        if (equation === '') equation = '0';
        
        setEquationInput(equation);
    }, [aNum, bNum, cNum]);

    // Update a, b, c when equation changes
    const handleEquationChange = (newEquation) => {
        const { a: newA, b: newB, c: newC } = parseEquation(newEquation);
        setA(newA.toString());
        setB(newB.toString());
        setC(newC.toString());
        setEquationInput(newEquation);
    };

    // Set initial equation when component mounts
    useEffect(() => {
        if (initialData) {
            const initialA = initialData.a || 1;
            const initialB = initialData.b || 0;
            const initialC = initialData.c || 0;
            
            let equation = '';
            if (initialA !== 0) {
                if (initialA === 1) equation += 'x²';
                else if (initialA === -1) equation += '-x²';
                else equation += `${initialA}x²`;
            }
            
            if (initialB !== 0) {
                if (initialB > 0 && equation !== '') equation += '+';
                if (initialB === 1) equation += 'x';
                else if (initialB === -1) equation += '-x';
                else equation += `${initialB}x`;
            }
            
            if (initialC !== 0) {
                if (initialC > 0 && equation !== '') equation += '+';
                equation += `${initialC}`;
            }
            
            if (equation === '') equation = '0';
            
            setEquationInput(equation);
        }
    }, []);

    const drawGraph = (targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) return;

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
            for (let x = Math.ceil(xMin); x <= Math.floor(xMax); x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = Math.ceil(yMin); y <= Math.floor(yMax); y++) {
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
        ctx.lineWidth = 2;

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

        // Draw axis labels
        ctx.fillStyle = '#000000'; // Black labels
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'center';
        
        // X-axis label
        ctx.fillText('X', width / 2, height - 10);
        
        // Y-axis label
        ctx.save();
        ctx.translate(20, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Y', 0, 0);
        ctx.restore();

        // Draw function
        if (aNum !== 0) {
            ctx.strokeStyle = lineColor;
            ctx.lineWidth = 2;
            ctx.beginPath();

            let firstPoint = true;
            const step = (xMax - xMin) / 400; // Increased resolution
            for (let x = xMin; x <= xMax; x += step) {
                const y = aNum * x * x + bNum * x + cNum;
                if (isFinite(y) && y >= yMin && y <= yMax) {
                    const canvasX = toCanvasX(x);
                    const canvasY = toCanvasY(y);
                    
                    if (firstPoint) {
                        ctx.moveTo(canvasX, canvasY);
                        firstPoint = false;
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                }
            }
            ctx.stroke();
        }

        // Draw points
        if (showPoints) {
            ctx.fillStyle = lineColor;
            const step = (xMax - xMin) / 100; // Increased resolution
            for (let x = xMin; x <= xMax; x += step) {
                const y = aNum * x * x + bNum * x + cNum;
                if (isFinite(y) && y >= yMin && y <= yMax) {
                    const canvasX = toCanvasX(x);
                    const canvasY = toCanvasY(y);
                    
                    ctx.beginPath();
                    ctx.arc(canvasX, canvasY, 2, 0, 2 * Math.PI);
                    ctx.fill();
                }
            }
        }

                          // Draw all points first
         const pointsToDraw = [];
         
                   // Add vertex point (but not when b = 0 since it's the same as y-intercept)
          if (showVertex && aNum !== 0 && bNum !== 0 && vertexX >= xMin && vertexX <= xMax && vertexY >= yMin && vertexY <= yMax) {
              const canvasX = toCanvasX(vertexX);
              const canvasY = toCanvasY(vertexY);
              
              // Draw vertex point (orange dot)
              ctx.fillStyle = '#f97316';
              ctx.beginPath();
              ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
              ctx.fill();
              
              pointsToDraw.push({
                  type: 'vertex',
                  color: '#f97316',
                  text: `(${vertexX.toFixed(2)}, ${vertexY.toFixed(2)})`
              });
          }
         
         // Add root points
         if (showRoots && roots.length > 0) {
             if (aNum === 1 && bNum === 0 && cNum === 0) {
                 // Special case for y = x²
                 const canvasX = toCanvasX(0);
                 const canvasY = toCanvasY(0);
                 
                 ctx.fillStyle = '#10b981';
                 ctx.beginPath();
                 ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
                 ctx.fill();
                 
                 pointsToDraw.push({
                     type: 'root_vertex',
                     color: '#10b981',
                     text: "Root = vertex = (0.00, 0.00)"
                 });
             } else {
                 roots.forEach((root, index) => {
                     if (root >= xMin && root <= xMax) {
                         const canvasX = toCanvasX(root);
                         const canvasY = toCanvasY(0);
                         
                         const rootColors = ['#ef4444', '#10b981'];
                         const rootColor = rootColors[index] || '#10b981';
                         
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
                 });
             }
         }
         
         // Add y-intercept point (but not for y = x² since it's already handled in the root_vertex case)
         if (0 >= xMin && 0 <= xMax && yIntercept >= yMin && yIntercept <= yMax && !(aNum === 1 && bNum === 0 && cNum === 0)) {
             const canvasX = toCanvasX(0);
             const canvasY = toCanvasY(yIntercept);
             
             ctx.fillStyle = '#3b82f6';
             ctx.beginPath();
             ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
             ctx.fill();
             
             pointsToDraw.push({
                 type: 'y_intercept',
                 color: '#3b82f6',
                 text: `(0, ${yIntercept})`
             });
         }
         
         // Draw single container with all coordinates
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

        // Draw title
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(title, width / 2, 20);
    };

    const handleOpenFullScreen = () => {
        setIsFullScreenOpen(true);
        // The useEffect will handle redrawing when isFullScreenOpen changes
    };

    const handleCloseFullScreen = () => {
        setIsFullScreenOpen(false);
    };

    const getGraphDescription = () => {
        let description = `Quadratic function: y = ${aNum}x² ${bNum >= 0 ? '+' : ''}${bNum}x ${cNum >= 0 ? '+' : ''}${cNum}\n`;
        description += `Direction: ${direction}\n`;
        description += `Vertex: (${vertexX.toFixed(2)}, ${vertexY.toFixed(2)})\n`;
        description += `Y-intercept: (0, ${yIntercept})\n`;
        
        if (roots.length > 0) {
            description += `X-intercepts: ${roots.map(r => `(${r.toFixed(2)}, 0)`).join(', ')}\n`;
        } else {
            description += `No real x-intercepts\n`;
        }
        
        description += `Domain: All real numbers\n`;
        description += `Range: y ${aNum > 0 ? '≥' : '≤'} ${vertexY.toFixed(2)}`;
        
        return description;
    };

    const handleAttachToAnswer = () => {
        if (onAttachToAnswer) {
            const graphData = {
                type: "quadratic_graph",
                equation: `y = ${aNum}x² ${bNum >= 0 ? '+' : ''}${bNum}x ${cNum >= 0 ? '+' : ''}${cNum}`,
                description: getGraphDescription(),
                properties: {
                    vertex: `(${vertexX.toFixed(2)}, ${vertexY.toFixed(2)})`,
                    yIntercept: yIntercept,
                    xIntercepts: roots.length > 0 ? roots.map(r => r.toFixed(2)) : [],
                    direction: direction,
                    discriminant: discriminant
                }
            };
            onAttachToAnswer(graphData);
        }
    };

    // Parameter Panel Component - Following LinearFunctionGraph structure
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Quadratic Function Parameters</h3>
            
            {/* Edit Mode Toggle */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Edit Mode</h4>
                <div className="flex space-x-2">
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="parameters"
                            checked={activeTab === 'parameters'}
                            onChange={(e) => setActiveTab(e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Parameters</span>
                    </label>
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="equation"
                            checked={activeTab === 'equation'}
                            onChange={(e) => setActiveTab(e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Equation</span>
                    </label>
                </div>
            </div>

            {/* Equation Editor */}
            {activeTab === 'equation' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Equation:</label>
                        <input
                            type="text"
                            value={equationInput}
                            onChange={(e) => handleEquationChange(e.target.value)}
                            placeholder="e.g., x² + 2x + 1, y = 2x² - 3x + 5"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                            disabled={isSubmitted}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                            Format: ax² + bx + c or y = ax² + bx + c
                        </p>
                    </div>
                </div>
            )}

            {/* Parameter Editor */}
            {activeTab === 'parameters' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                        <input
                            type="text"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient a (x²):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={a}
                            onChange={(e) => setA(e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Coefficient b (x):</label>
                        <input
                            type="number"
                            step="0.1"
                            value={b}
                            onChange={(e) => setB(e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Constant c:</label>
                        <input
                            type="number"
                            step="0.1"
                            value={c}
                            onChange={(e) => setC(e.target.value)}
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
                            value={xMin}
                            onChange={(e) => setXMin(Number(e.target.value))}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Max:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={xMax}
                            onChange={(e) => setXMax(Number(e.target.value))}
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
                            step="0.5"
                            value={yMin}
                            onChange={(e) => setYMin(Number(e.target.value))}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Y Max:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={yMax}
                            onChange={(e) => setYMax(Number(e.target.value))}
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
                        onChange={(e) => setShowGrid(e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={showPoints}
                        onChange={(e) => setShowPoints(e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Points</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={showVertex}
                        onChange={(e) => setShowVertex(e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Vertex</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={showRoots}
                        onChange={(e) => setShowRoots(e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Roots</span>
                </label>
            </div>

            {/* Line Color */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                <input
                    type="color"
                    value={lineColor}
                    onChange={(e) => setLineColor(e.target.value)}
                    className="w-full h-10 border border-gray-300 rounded-md"
                    disabled={isSubmitted}
                />
            </div>

            {/* Function Information */}
            <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                <h4 className="font-medium text-blue-800 mb-2">Function Information</h4>
                <div className="space-y-1 text-sm">
                    <div><strong>Equation:</strong> y = {aNum}x² {bNum >= 0 ? '+' : ''}{bNum}x {cNum >= 0 ? '+' : ''}{cNum}</div>
                    <div><strong>Direction:</strong> {direction}</div>
                    <div><strong>Vertex:</strong> ({vertexX.toFixed(2)}, {vertexY.toFixed(2)})</div>
                    <div><strong>Y-intercept:</strong> (0, {yIntercept})</div>
                    <div><strong>X-intercepts:</strong> {roots.length > 0 ? roots.map(r => r.toFixed(2)).join(', ') : 'None'}</div>
                    <div><strong>Discriminant:</strong> {discriminant.toFixed(2)}</div>
                    <div><strong>Axis of Symmetry:</strong> x = {vertexX.toFixed(2)}</div>
                </div>
            </div>
        </div>
    );

    return (
        <div className="relative">
            <div className="p-2 bg-white border border-gray-300 rounded-lg mt-2">
                {/* Controls - Reduced height by half */}
                <div className="flex flex-col gap-2 p-2 bg-gray-50 rounded-lg mb-2">
                    {/* Coefficient inputs in one horizontal row */}
                    <div className="flex gap-3 items-end">
                        <div className="flex-1">
                            <label className="block text-xs font-medium text-gray-700 mb-1">
                                Coefficient a (x²)
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                value={a}
                                onChange={(e) => setA(e.target.value)}
                                className="w-7/8 px-1 py-0.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-xs h-6"
                                disabled={isSubmitted}
                            />
                        </div>
                        
                        <div className="flex-1">
                            <label className="block text-xs font-medium text-gray-700 mb-1">
                                Coefficient b (x)
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                value={b}
                                onChange={(e) => setB(e.target.value)}
                                className="w-7/8 px-1 py-0.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-xs h-6"
                                disabled={isSubmitted}
                            />
                        </div>
                        
                        <div className="flex-1">
                            <label className="block text-xs font-medium text-gray-700 mb-1">
                                Constant c
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                value={c}
                                onChange={(e) => setC(e.target.value)}
                                className="w-7/8 px-1 py-0.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-xs h-6"
                                disabled={isSubmitted}
                            />
                        </div>
                        
                        <div className="flex-1">
                            <label className="block text-xs font-medium text-gray-700 mb-1">
                                Line Color
                            </label>
                            <input
                                type="color"
                                value={lineColor}
                                onChange={(e) => setLineColor(e.target.value)}
                                className="w-7/8 h-6 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                disabled={isSubmitted}
                            />
                        </div>
                    </div>
                    
                    {/* Checkboxes in one horizontal row */}
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={showGrid}
                                onChange={(e) => setShowGrid(e.target.checked)}
                                className="mr-1"
                                disabled={isSubmitted}
                            />
                            <span className="text-xs text-gray-700">Show Grid</span>
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={showPoints}
                                onChange={(e) => setShowPoints(e.target.checked)}
                                className="mr-1"
                                disabled={isSubmitted}
                            />
                            <span className="text-xs text-gray-700">Show Points</span>
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={showVertex}
                                onChange={(e) => setShowVertex(e.target.checked)}
                                className="mr-1"
                                disabled={isSubmitted}
                            />
                            <span className="text-xs text-gray-700">Show Vertex</span>
                        </label>
                        
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={showRoots}
                                onChange={(e) => setShowRoots(e.target.checked)}
                                className="mr-1"
                                disabled={isSubmitted}
                            />
                            <span className="text-xs text-gray-700">Show Roots</span>
                        </label>
                    </div>
                </div>

                {/* Graph Canvas - Moved up closer to inputs */}
                <div className="border border-gray-300 rounded-lg overflow-hidden relative">
                    {/* Blue expansion button - replaces the header expansion button */}
                    <button 
                        onClick={handleOpenFullScreen}
                        className="absolute top-2 right-2 p-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded transition-colors z-10"
                        title="Full screen"
                    >
                        <Maximize2 size={16} />
                    </button>
                    
                    <canvas
                        ref={canvasRef}
                        width={800}
                        height={600}
                        className="w-full h-auto"
                        style={{ minHeight: '400px' }}
                    />
                </div>

                                       {/* Full Screen Modal - Goes directly to maximized view with left pane */}
                       <FullScreenModal
                           isOpen={isFullScreenOpen}
                           onClose={handleCloseFullScreen}
                           title="Quadratic Function Graph - Full Screen Mode"
                           parameterPanel={<ParameterPanel />}
                       >
                    <div className="h-full w-full flex items-center justify-center">
                        <div className="w-full h-full flex items-center justify-center">
                            <div className="border-2 border-gray-300 rounded-lg overflow-hidden w-full h-full">
                                <canvas
                                    ref={fullScreenCanvasRef}
                                    width={1200}
                                    height={800}
                                    className="w-full h-full"
                                />
                            </div>
                        </div>
                    </div>
                </FullScreenModal>
            </div>
        </div>
    );
};

export default QuadraticGraphInput;
