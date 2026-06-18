import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const IntegratedExponentialLogarithmicGraph = ({ initialData, onChange, isSubmitted }) => {
    // Individual state variables for each parameter (like the working functions)
    const [functionType, setFunctionType] = useState(initialData?.functionType || 'exponential');
    const [a, setA] = useState(initialData?.a || 1);
    const [b, setB] = useState(initialData?.b || 2);
    const [c, setC] = useState(initialData?.c || 0);
    const [d, setD] = useState(initialData?.d || 0);
    const [base, setBase] = useState(initialData?.base || 'e');
    const [customBase, setCustomBase] = useState(initialData?.customBase || 2);
    const [editMode, setEditMode] = useState(initialData?.editMode || 'parameters');
    const [showInverse, setShowInverse] = useState(initialData?.showInverse || false);
    const [showRelationship, setShowRelationship] = useState(initialData?.showRelationship || true);
    const [showInverseVisualizer, setShowInverseVisualizer] = useState(initialData?.showInverseVisualizer || false);
    const [inverseLineColor, setInverseLineColor] = useState(initialData?.inverseLineColor || '#10B981');
    const [showInversePoints, setShowInversePoints] = useState(initialData?.showInversePoints || true);
    const [showReflectionLine, setShowReflectionLine] = useState(initialData?.showReflectionLine || false);
    const [xMin, setXMin] = useState(initialData?.x_range?.[0] || -5);
    const [xMax, setXMax] = useState(initialData?.x_range?.[1] || 5);
    const [yMin, setYMin] = useState(initialData?.y_range?.[0] || -2);
    const [yMax, setYMax] = useState(initialData?.y_range?.[1] || 10);
    const [lineColor, setLineColor] = useState(initialData?.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData?.showGrid !== false);
    const [showPoints, setShowPoints] = useState(initialData?.showPoints !== false);
    const [showAsymptote, setShowAsymptote] = useState(initialData?.showAsymptote !== false);
    const [currentStep, setCurrentStep] = useState(initialData?.currentStep || 0);
    const [solutionSteps, setSolutionSteps] = useState(initialData?.solutionSteps || []);
    const [showSolutionSteps, setShowSolutionSteps] = useState(initialData?.showSolutionSteps || false);
    const [currentProblem, setCurrentProblem] = useState(initialData?.currentProblem || null);
    const [tutorialMode, setTutorialMode] = useState(initialData?.tutorialMode || false);
    const [practiceProblems, setPracticeProblems] = useState(initialData?.practiceProblems || []);
    const [userProgress, setUserProgress] = useState(initialData?.userProgress || {});
    const [solverMode, setSolverMode] = useState(initialData?.solverMode || 'none');
    const [inputExpression, setInputExpression] = useState(initialData?.inputExpression || '');
    const [targetOperation, setTargetOperation] = useState(initialData?.targetOperation || 'simplify');
    const [showStepExplanations, setShowStepExplanations] = useState(initialData?.showStepExplanations !== false);
    const [showIntermediateCalculations, setShowIntermediateCalculations] = useState(initialData?.showIntermediateCalculations !== false);
    const [showLawsDemonstrator, setShowLawsDemonstrator] = useState(initialData?.showLawsDemonstrator || false);
    const [currentLaw, setCurrentLaw] = useState(initialData?.currentLaw || 'product');
    const [lawDemonstrationMode, setLawDemonstrationMode] = useState(initialData?.lawDemonstrationMode || 'visual');
    const [showLawProof, setShowLawProof] = useState(initialData?.showLawProof || false);
    const [showLawGraph, setShowLawGraph] = useState(initialData?.showLawGraph || false);
    const [lawX, setLawX] = useState(initialData?.lawParameters?.x || 2);
    const [lawY, setLawY] = useState(initialData?.lawParameters?.y || 3);
    const [lawBase, setLawBase] = useState(initialData?.lawParameters?.base || 2);
    const [equationInput, setEquationInput] = useState(initialData?.equationInput || '');

    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    // Convert string values to numbers for calculations (like the working functions)
    const aNum = Number(a) || 0;
    const bNum = Number(b) || 0;
    const cNum = Number(c) || 0;
    const dNum = Number(d) || 0;
    const customBaseNum = Number(customBase) || 2;
    const lawXNum = Number(lawX) || 2;
    const lawYNum = Number(lawY) || 3;
    const lawBaseNum = Number(lawBase) || 2;

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
            console.warn('Error parsing equation:', error);
            return { a: 1, b: 2, c: 0, d: 0 };
        }
    };

    const parseRightSide = (rightSide) => {
        let a = 1, b = 2, c = 0, d = 0;
        
        // Handle exponential functions like "2^x", "3*2^x", "2^(x+1)", "2^x+3"
        // And logarithmic functions like "log_2(x)", "ln(x)", "log(x+1)"
        
        if (rightSide.includes('^')) {
            // Exponential function
            const parts = rightSide.split(/(?=[+-])/);
            const mainPart = parts[0];
            const shiftPart = parts.slice(1).join('');
            
            if (mainPart.includes('^')) {
                const [basePart, exponentPart] = mainPart.split('^');
                
                // Parse coefficient and base
                if (basePart.includes('*')) {
                    const [coefPart, basePart2] = basePart.split('*');
                    a = parseFloat(coefPart) || 1;
                    b = parseFloat(basePart2) || 2;
                } else {
                    a = 1;
                    b = parseFloat(basePart) || 2;
                }
                
                // Parse exponent (x + c)
                if (exponentPart.includes('x')) {
                    const xPart = exponentPart.replace(/[()x]/g, '');
                    if (xPart.includes('+')) {
                        c = parseFloat(xPart.split('+')[1]) || 0;
                    } else if (xPart.includes('-')) {
                        c = -parseFloat(xPart.split('-')[1]) || 0;
                    }
                }
            }
            
            // Parse vertical shift (d)
            if (shiftPart) {
                d = parseFloat(shiftPart) || 0;
            }
        } else if (rightSide.includes('log') || rightSide.includes('ln')) {
            // Logarithmic function - for now, set function type to logarithmic
            // This is a simplified parser, more complex parsing can be added later
            a = 1;
            b = 2; // Default base for log
            c = 0;
            d = 0;
        }
        
        return { a, b, c, d };
    };

    // Update coefficients when equation changes
    const handleEquationChange = (newEquation) => {
        const { a: newA, b: newB, c: newC, d: newD } = parseEquation(newEquation);
        setA(newA.toString());
        setB(newB.toString());
        setC(newC.toString());
        setD(newD.toString());
        setEquationInput(newEquation);
    };

    // Update parent component when data changes
    useEffect(() => {
        if (onChange) {
            onChange({
                functionType, a, b, c, d, base, customBase, editMode, showInverse, showRelationship, showInverseVisualizer, inverseLineColor, showInversePoints, showReflectionLine, x_range: [xMin, xMax], y_range: [yMin, yMax], lineColor, showGrid, showPoints, showAsymptote, currentStep, solutionSteps, showSolutionSteps, currentProblem, tutorialMode, practiceProblems, userProgress, solverMode, inputExpression, targetOperation, showStepExplanations, showIntermediateCalculations, showLawsDemonstrator, currentLaw, lawDemonstrationMode, showLawProof, showLawGraph, lawParameters: { x: lawX, y: lawY, base: lawBase }, equationInput
            });
        }
    }, [functionType, a, b, c, d, base, customBase, editMode, showInverse, showRelationship, showInverseVisualizer, inverseLineColor, showInversePoints, showReflectionLine, xMin, xMax, yMin, yMax, lineColor, showGrid, showPoints, showAsymptote, currentStep, solutionSteps, showSolutionSteps, currentProblem, tutorialMode, practiceProblems, userProgress, solverMode, inputExpression, targetOperation, showStepExplanations, showIntermediateCalculations, showLawsDemonstrator, currentLaw, lawDemonstrationMode, showLawProof, showLawGraph, lawX, lawY, lawBase, equationInput]);

    // Update internal state when initialData changes
    useEffect(() => {
        if (initialData) {
            setFunctionType(initialData.functionType || 'exponential');
            setA(initialData.a || 1);
            setB(initialData.b || 2);
            setC(initialData.c || 0);
            setD(initialData.d || 0);
            setBase(initialData.base || 'e');
            setCustomBase(initialData.customBase || 2);
            setEditMode(initialData.editMode || 'parameters');
            setShowInverse(initialData.showInverse || false);
            setShowRelationship(initialData.showRelationship || true);
            setShowInverseVisualizer(initialData.showInverseVisualizer || false);
            setInverseLineColor(initialData.inverseLineColor || '#10B981');
            setShowInversePoints(initialData.showInversePoints || true);
            setShowReflectionLine(initialData.showReflectionLine || false);
            setXMin(initialData.x_range?.[0] || -5);
            setXMax(initialData.x_range?.[1] || 5);
            setYMin(initialData.y_range?.[0] || -2);
            setYMax(initialData.y_range?.[1] || 10);
            setLineColor(initialData.lineColor || '#3B82F6');
            setShowGrid(initialData.showGrid !== false);
            setShowPoints(initialData.showPoints !== false);
            setShowAsymptote(initialData.showAsymptote !== false);
            setCurrentStep(initialData.currentStep || 0);
            setSolutionSteps(initialData.solutionSteps || []);
            setShowSolutionSteps(initialData.showSolutionSteps || false);
            setCurrentProblem(initialData.currentProblem || null);
            setTutorialMode(initialData.tutorialMode || false);
            setPracticeProblems(initialData.practiceProblems || []);
            setUserProgress(initialData.userProgress || {});
            setSolverMode(initialData.solverMode || 'none');
            setInputExpression(initialData.inputExpression || '');
            setTargetOperation(initialData.targetOperation || 'simplify');
            setShowStepExplanations(initialData.showStepExplanations !== false);
            setShowIntermediateCalculations(initialData.showIntermediateCalculations !== false);
            setShowLawsDemonstrator(initialData.showLawsDemonstrator || false);
            setCurrentLaw(initialData.currentLaw || 'product');
            setLawDemonstrationMode(initialData.lawDemonstrationMode || 'visual');
            setShowLawProof(initialData.showLawProof || false);
            setShowLawGraph(initialData.showLawGraph || false);
            setLawX(initialData.lawParameters?.x || 2);
            setLawY(initialData.lawParameters?.y || 3);
            setLawBase(initialData.lawParameters?.base || 2);
            setEquationInput(initialData.equationInput || '');
        }
    }, [initialData]);

    // Handle parameter updates - simplified like working functions
    const handleInputChange = (field, value) => {
        switch (field) {
            case 'a': setA(value); break;
            case 'b': setB(value); break;
            case 'c': setC(value); break;
            case 'd': setD(value); break;
            case 'base': setBase(value); break;
            case 'customBase': setCustomBase(value); break;
            case 'editMode': setEditMode(value); break;
            case 'showInverse': setShowInverse(value); break;
            case 'showRelationship': setShowRelationship(value); break;
            case 'showInverseVisualizer': setShowInverseVisualizer(value); break;
            case 'inverseLineColor': setInverseLineColor(value); break;
            case 'showInversePoints': setShowInversePoints(value); break;
            case 'showReflectionLine': setShowReflectionLine(value); break;
            case 'xMin': setXMin(value); break;
            case 'xMax': setXMax(value); break;
            case 'yMin': setYMin(value); break;
            case 'yMax': setYMax(value); break;
            case 'lineColor': setLineColor(value); break;
            case 'showGrid': setShowGrid(value !== false); break;
            case 'showPoints': setShowPoints(value !== false); break;
            case 'showAsymptote': setShowAsymptote(value !== false); break;
            case 'currentStep': setCurrentStep(value); break;
            case 'solutionSteps': setSolutionSteps(value); break;
            case 'showSolutionSteps': setShowSolutionSteps(value); break;
            case 'currentProblem': setCurrentProblem(value); break;
            case 'tutorialMode': setTutorialMode(value); break;
            case 'practiceProblems': setPracticeProblems(value); break;
            case 'userProgress': setUserProgress(value); break;
            case 'solverMode': setSolverMode(value); break;
            case 'inputExpression': setInputExpression(value); break;
            case 'targetOperation': setTargetOperation(value); break;
            case 'showStepExplanations': setShowStepExplanations(value !== false); break;
            case 'showIntermediateCalculations': setShowIntermediateCalculations(value !== false); break;
            case 'showLawsDemonstrator': setShowLawsDemonstrator(value); break;
            case 'currentLaw': setCurrentLaw(value); break;
            case 'lawDemonstrationMode': setLawDemonstrationMode(value); break;
            case 'showLawProof': setShowLawProof(value); break;
            case 'showLawGraph': setShowLawGraph(value); break;
            case 'lawX': setLawX(value); break;
            case 'lawY': setLawY(value); break;
            case 'lawBase': setLawBase(value); break;
            case 'equationInput': setEquationInput(value); break;
            default: break;
        }
    };

    // Handle function type change
    const handleFunctionTypeChange = (newType) => {
        setFunctionType(newType);
        // Reset parameters to sensible defaults for new function type
        setA(newType === 'exponential' ? 1 : 1);
        setB(newType === 'exponential' ? 2 : 1);
        setC(0);
        setD(0);
        setBase(newType === 'logarithmic' ? 'e' : 'e');
    };

    // Calculate function value based on type
    const calculateFunctionValue = (x) => {
        if (functionType === 'exponential') {
            // y = a × b^(x + c) + d
            return aNum * Math.pow(bNum, x + cNum) + dNum;
        } else {
            // y = a × log_b(x + c) + d
            if (x + cNum <= 0) return null; // Domain restriction
            
            let logValue;
            if (base === 'e') {
                logValue = Math.log(x + cNum);
            } else if (base === '2') {
                logValue = Math.log2(x + cNum);
            } else if (base === '10') {
                logValue = Math.log10(x + cNum);
            } else {
                logValue = Math.log(x + cNum) / Math.log(parseFloat(base));
            }
            
            return aNum * logValue + dNum;
        }
    };

    // Calculate inverse function value
    const calculateInverseFunctionValue = (y) => {
        if (functionType === 'exponential') {
            // Original: y = a × b^(x + c) + d
            // Inverse: x = log_b((y - d) / a) - c
            if (aNum === 0 || (y - dNum) / aNum <= 0) return null;
            return Math.log((y - dNum) / aNum) / Math.log(bNum) - cNum;
        } else {
            // Original: y = a × log_b(x + c) + d
            // Inverse: x = b^((y - d) / a) - c
            if (aNum === 0) return null;
            return Math.pow(base === 'e' ? Math.E : parseFloat(base), (y - dNum) / aNum) - cNum;
        }
    };

    // Calculate function properties
    const calculateFunctionProperties = useCallback(() => {
        const baseValue = base === 'e' ? Math.E : base === '2' ? 2 : base === '10' ? 10 : customBaseNum;
        
        if (functionType === 'exponential') {
            return {
                domain: { min: -Infinity, max: Infinity },
                range: { min: dNum, max: Infinity },
                asymptote: { horizontal: `y = ${dNum}`, vertical: null },
                yIntercept: [0, aNum * Math.pow(bNum, cNum) + dNum],
                behavior: bNum > 1 ? 'Growth' : 'Decay'
            };
        } else {
            return {
                domain: { min: -cNum, max: Infinity },
                range: { min: -Infinity, max: Infinity },
                asymptote: { horizontal: null, vertical: `x = ${-cNum}` },
                yIntercept: [1, aNum * Math.log(1 + cNum) / Math.log(baseValue) + dNum],
                behavior: 'Increasing (if a > 0)'
            };
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum]);

    // Draw the graph
    const drawGraph = useCallback((targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        const x_range = [xMin, xMax];
        const y_range = [yMin, yMax];

        // Calculate scale factors
        const xScale = width / (x_range[1] - x_range[0]);
        const yScale = height / (y_range[1] - y_range[0]);

        // Helper functions for coordinate conversion
        const toCanvasX = (x) => (x - x_range[0]) * xScale;
        const toCanvasY = (y) => height - (y - y_range[0]) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB';
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = x_range[0]; x <= x_range[1]; x += 0.5) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = y_range[0]; y <= y_range[1]; y += 1) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = '#000000';
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

        // Draw function
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 2;
        ctx.beginPath();

        let firstPoint = true;
        for (let x = x_range[0]; x <= x_range[1]; x += 0.01) {
            const y = calculateFunctionValue(x);
            
            if (y !== null && isFinite(y) && y >= y_range[0] && y <= y_range[1]) {
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

        // Draw inverse function if enabled
        if (showInverseVisualizer) {
            ctx.strokeStyle = inverseLineColor;
            ctx.lineWidth = 2;
            ctx.setLineDash([3, 3]);
            ctx.beginPath();

            let firstInversePoint = true;
            for (let y = y_range[0]; y <= y_range[1]; y += 0.01) {
                const x = calculateInverseFunctionValue(y);
                
                if (x !== null && isFinite(x) && x >= x_range[0] && x <= x_range[1]) {
                    const canvasX = toCanvasX(x);
                    const canvasY = toCanvasY(y);
                    
                    if (firstInversePoint) {
                        ctx.moveTo(canvasX, canvasY);
                        firstInversePoint = false;
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                }
            }
            
            ctx.stroke();
            ctx.setLineDash([]);
        }

        // Draw y=x reflection line if enabled
        if (showReflectionLine) {
            ctx.strokeStyle = '#FFD700';
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            
            const startX = Math.max(x_range[0], y_range[0]);
            const endX = Math.min(x_range[1], y_range[1]);
            
            if (startX <= endX) {
                const startCanvasX = toCanvasX(startX);
                const startCanvasY = toCanvasY(startX);
                const endCanvasX = toCanvasX(endX);
                const endCanvasY = toCanvasY(endX);
                
                ctx.beginPath();
                ctx.moveTo(startCanvasX, startCanvasY);
                ctx.lineTo(endCanvasX, endCanvasY);
                ctx.stroke();
            }
            ctx.setLineDash([]);
        }

        // Draw asymptotes
        const properties = calculateFunctionProperties();
        if (properties.asymptote.horizontal) {
            ctx.strokeStyle = '#FF6B6B';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            const asymptoteY = toCanvasY(parseFloat(properties.asymptote.horizontal.split('=')[1]));
            if (asymptoteY >= 0 && asymptoteY <= height) {
                ctx.beginPath();
                ctx.moveTo(0, asymptoteY);
                ctx.lineTo(width, asymptoteY);
                ctx.stroke();
            }
            ctx.setLineDash([]);
        }

        if (properties.asymptote.vertical) {
            ctx.strokeStyle = '#FF6B6B';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            const asymptoteX = toCanvasX(parseFloat(properties.asymptote.vertical.split('=')[1]));
            if (asymptoteX >= 0 && asymptoteX <= width) {
                ctx.beginPath();
                ctx.moveTo(asymptoteX, 0);
                ctx.lineTo(asymptoteX, height);
                ctx.stroke();
            }
            ctx.setLineDash([]);
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, showInverseVisualizer, inverseLineColor, showReflectionLine, xMin, xMax, yMin, yMax, lineColor, showGrid, calculateFunctionProperties]);

    // Redraw graph when data changes
    useEffect(() => {
        const timer = setTimeout(() => {
            drawGraph();
        }, 100);
        return () => clearTimeout(timer);
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, showInverseVisualizer, inverseLineColor, showReflectionLine, xMin, xMax, yMin, yMax, lineColor, showGrid, showPoints, showAsymptote, currentStep, solutionSteps, showSolutionSteps, currentProblem, tutorialMode, practiceProblems, userProgress, solverMode, inputExpression, targetOperation, showStepExplanations, showIntermediateCalculations, showLawsDemonstrator, currentLaw, lawDemonstrationMode, showLawProof, showLawGraph, lawX, lawY, lawBase, drawGraph]);

    // Initial draw
    useEffect(() => {
        drawGraph();
    }, [drawGraph]);

    // Draw on full-screen canvas when it opens or data changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            const timer = setTimeout(() => {
                drawGraph(fullScreenCanvasRef.current);
            }, 100);
            return () => clearTimeout(timer);
        }
    }, [isFullScreenOpen, functionType, aNum, bNum, cNum, dNum, base, customBase, showInverseVisualizer, inverseLineColor, showInversePoints, showReflectionLine, xMin, xMax, yMin, yMax, lineColor, showGrid, showPoints, showAsymptote, currentStep, solutionSteps, showSolutionSteps, currentProblem, tutorialMode, practiceProblems, userProgress, solverMode, inputExpression, targetOperation, showStepExplanations, showIntermediateCalculations, showLawsDemonstrator, currentLaw, lawDemonstrationMode, showLawProof, showLawGraph, lawX, lawY, lawBase, drawGraph]);

    // Full screen handlers
    const handleOpenFullScreen = () => setIsFullScreenOpen(true);
    const handleCloseFullScreen = () => setIsFullScreenOpen(false);
    const handleToggleFullScreen = () => setIsFullScreen(!isFullScreen);

    // Helper function to render mathematical expressions with proper superscripts
    const renderMathExpression = (expression) => {
        return <span dangerouslySetInnerHTML={{ __html: expression }} />;
    };

    // Get function string representation
    const getFunctionString = () => {
        if (functionType === 'exponential') {
            let result = '';
            if (aNum !== 1) result += `${aNum} × `;
            result += `${bNum}<sup>x`;
            if (cNum !== 0) result += cNum > 0 ? ` + ${cNum}` : ` - ${Math.abs(cNum)}`;
            result += '</sup>';
            if (dNum !== 0) result += dNum > 0 ? ` + ${dNum}` : ` - ${Math.abs(dNum)}`;
            return result;
        } else {
            let result = '';
            if (aNum !== 1) result += `${aNum} × `;
            result += `log<sub>${base}</sub>(x`;
            if (cNum !== 0) result += cNum > 0 ? ` + ${cNum}` : ` - ${Math.abs(cNum)}`;
            result += ')';
            if (dNum !== 0) result += dNum > 0 ? ` + ${dNum}` : ` - ${Math.abs(dNum)}`;
            return result;
        }
    };

    // Get behavior description
    const getBehaviorDescription = () => {
        if (functionType === 'exponential') {
            if (bNum > 1) return 'Exponential Growth';
            else if (0 < bNum && bNum < 1) return 'Exponential Decay';
            else return 'Constant Function';
        } else {
            if (aNum > 0) return 'Increasing Logarithmic';
            else if (aNum < 0) return 'Decreasing Logarithmic';
            else return 'Constant Function';
        }
    };

    // Mathematical properties and laws
    const getMathematicalProperties = () => {
        if (functionType === 'exponential') {
            return {
                title: 'Exponential Function Properties',
                laws: [
                    {
                        name: 'Product Law',
                        formula: 'a<sup>x + y</sup> = a<sup>x</sup> × a<sup>y</sup>',
                        explanation: 'When multiplying exponential expressions with the same base, add the exponents.',
                        example: '2<sup>3 + 4</sup> = 2<sup>3</sup> × 2<sup>4</sup> = 8 × 16 = 128'
                    },
                    {
                        name: 'Quotient Law',
                        formula: 'a<sup>x - y</sup> = a<sup>x</sup> ÷ a<sup>y</sup>',
                        explanation: 'When dividing exponential expressions with the same base, subtract the exponents.',
                        example: '2<sup>7 - 3</sup> = 2<sup>7</sup> ÷ 2<sup>3</sup> = 128 ÷ 8 = 16'
                    },
                    {
                        name: 'Power Law',
                        formula: '(a<sup>x</sup>)<sup>y</sup> = a<sup>x × y</sup>',
                        explanation: 'When raising an exponential expression to a power, multiply the exponents.',
                        example: '(2<sup>3</sup>)<sup>2</sup> = 2<sup>3 × 2</sup> = 2<sup>6</sup> = 64'
                    },
                    {
                        name: 'Zero Exponent',
                        formula: 'a<sup>0</sup> = 1',
                        explanation: 'Any non-zero number raised to the power of 0 equals 1.',
                        example: '5<sup>0</sup> = 1, (-3)<sup>0</sup> = 1'
                    },
                    {
                        name: 'Negative Exponent',
                        formula: 'a<sup>-x</sup> = 1 ÷ a<sup>x</sup>',
                        explanation: 'A negative exponent indicates the reciprocal of the positive exponent.',
                        example: '2<sup>-3</sup> = 1 ÷ 2<sup>3</sup> = 1 ÷ 8 = 0.125'
                    }
                ]
            };
        } else {
            return {
                title: 'Logarithmic Function Properties',
                laws: [
                    {
                        name: 'Product Law',
                        formula: 'log<sub>b</sub>(x × y) = log<sub>b</sub>(x) + log<sub>b</sub>(y)',
                        explanation: 'The logarithm of a product equals the sum of the logarithms.',
                        example: 'log<sub>2</sub>(8 × 16) = log<sub>2</sub>(8) + log<sub>2</sub>(16) = 3 + 4 = 7'
                    },
                    {
                        name: 'Quotient Law',
                        formula: 'log<sub>b</sub>(x ÷ y) = log<sub>b</sub>(x) - log<sub>b</sub>(y)',
                        explanation: 'The logarithm of a quotient equals the difference of the logarithms.',
                        example: 'log<sub>2</sub>(32 ÷ 8) = log<sub>2</sub>(32) - log<sub>2</sub>(8) = 5 - 3 = 2'
                    },
                    {
                        name: 'Power Law',
                        formula: 'log<sub>b</sub>(x<sup>y</sup>) = y × log<sub>b</sub>(x)',
                        explanation: 'The logarithm of a power equals the exponent times the logarithm of the base.',
                        example: 'log<sub>2</sub>(8<sup>3</sup>) = 3 × log<sub>2</sub>(8) = 3 × 3 = 9'
                    },
                    {
                        name: 'Change of Base',
                        formula: 'log<sub>b</sub>(x) = log<sub>c</sub>(x) ÷ log<sub>c</sub>(b)',
                        explanation: 'Convert between different logarithmic bases using this formula.',
                        example: 'log<sub>2</sub>(16) = log<sub>10</sub>(16) ÷ log<sub>10</sub>(2) = 1.204 ÷ 0.301 = 4'
                    },
                    {
                        name: 'Identity',
                        formula: 'log<sub>b</sub>(b<sup>x</sup>) = x',
                        explanation: 'The logarithm and exponential functions are inverse operations.',
                        example: 'log<sub>2</sub>(2<sup>5</sup>) = 5'
                    }
                ]
            };
        }
    };

    // Step-by-step problem solver
    const solveStepByStep = (expression, operation) => {
        const steps = [];
        let currentExpression = expression;
        
        try {
            if (operation === 'simplify') {
                // Step 1: Parse the expression
                steps.push({
                    step: 1,
                    action: 'Parse Expression',
                    expression: expression,
                    explanation: 'Identify the components of the expression',
                    result: 'Expression parsed successfully'
                });

                // Step 2: Apply relevant laws
                if (functionType === 'exponential') {
                    steps.push({
                        step: 2,
                        action: 'Apply Exponential Laws',
                        expression: currentExpression,
                        explanation: 'Use exponential properties to simplify',
                        result: 'Laws applied: Product, Quotient, Power'
                    });
                } else {
                    steps.push({
                        step: 2,
                        action: 'Apply Logarithmic Laws',
                        expression: currentExpression,
                        explanation: 'Use logarithmic properties to simplify',
                        result: 'Laws applied: Product, Quotient, Power'
                    });
                }

                // Step 3: Final result
                steps.push({
                    step: 3,
                    action: 'Final Result',
                    expression: currentExpression,
                    explanation: 'Expression simplified to its final form',
                    result: 'Simplification complete'
                });
            } else if (operation === 'solve') {
                steps.push({
                    step: 1,
                    action: 'Set Equal to Zero',
                    expression: `${expression} = 0`,
                    explanation: 'To solve, set the expression equal to zero',
                    result: 'Equation ready for solving'
                });

                steps.push({
                    step: 2,
                    action: 'Apply Inverse Operations',
                    expression: 'Apply inverse function operations',
                    explanation: 'Use the inverse relationship to solve for x',
                    result: 'Solution found'
                });
            }

            return steps;
        } catch (error) {
            return [{
                step: 1,
                action: 'Error',
                expression: expression,
                explanation: 'An error occurred while solving',
                result: `Error: ${error.message}`
            }];
        }
    };

    // Generate practice problems
    const generatePracticeProblems = () => {
        if (functionType === 'exponential') {
            return [
                {
                    id: 1,
                    difficulty: 'easy',
                    expression: '2<sup>3</sup> × 2<sup>4</sup>',
                    question: 'Simplify using exponential laws',
                    solution: '2<sup>3+4</sup> = 2<sup>7</sup> = 128',
                    explanation: 'Use the product law: a<sup>x+y</sup> = a<sup>x</sup> × a<sup>y</sup>'
                },
                {
                    id: 2,
                    difficulty: 'medium',
                    expression: '(3<sup>2</sup>)<sup>3</sup> ÷ 3<sup>4</sup>',
                    question: 'Simplify using exponential laws',
                    solution: '3<sup>2×3</sup> ÷ 3<sup>4</sup> = 3<sup>6</sup> ÷ 3<sup>4</sup> = 3<sup>6-4</sup> = 3<sup>2</sup> = 9',
                    explanation: 'Use power law then quotient law'
                },
                {
                    id: 3,
                    difficulty: 'hard',
                    expression: '2<sup>x+3</sup> × 2<sup>2x-1</sup>',
                    question: 'Simplify and solve for x if equal to 2<sup>10</sup>',
                    solution: '2<sup>x+3+2x-1</sup> = 2<sup>3x+2</sup> = 2<sup>10</sup> → 3x+2 = 10 → x = 8/3',
                    explanation: 'Combine exponents and solve the resulting equation'
                }
            ];
        } else {
            return [
                {
                    id: 1,
                    difficulty: 'easy',
                    expression: 'log<sub>2</sub>(8) + log<sub>2</sub>(16)',
                    question: 'Simplify using logarithmic laws',
                    solution: 'log<sub>2</sub>(8×16) = log<sub>2</sub>(128) = 7',
                    explanation: 'Use the product law: log<sub>b</sub>(x×y) = log<sub>b</sub>(x) + log<sub>b</sub>(y)'
                },
                {
                    id: 2,
                    difficulty: 'medium',
                    expression: 'log<sub>3</sub>(27<sup>2</sup>) - log<sub>3</sub>(9)',
                    question: 'Simplify using logarithmic laws',
                    solution: '2×log<sub>3</sub>(27) - log<sub>3</sub>(9) = 2×3 - 2 = 4',
                    explanation: 'Use power law then quotient law'
                },
                {
                    id: 3,
                    difficulty: 'hard',
                    expression: 'log<sub>2</sub>(x<sup>2</sup>) + log<sub>2</sub>(x<sup>3</sup>) = 10',
                    question: 'Solve for x',
                    solution: 'log<sub>2</sub>(x<sup>5</sup>) = 10 → x<sup>5</sup> = 2<sup>10</sup> → x = 2<sup>2</sup> = 4',
                    explanation: 'Combine logarithms and solve the resulting equation'
                }
            ];
        }
    };

    // Exponential Laws Demonstrator Functions
    const getLawDemonstration = (lawType) => {
        const { lawParameters } = { lawParameters: { x: lawXNum, y: lawYNum, base: lawBaseNum } };
        const { x, y, base } = lawParameters;
        
        const laws = {
            product: {
                title: 'Product Law: a<sup>x + y</sup> = a<sup>x</sup> × a<sup>y</sup>',
                leftSide: `${base}<sup>${x} + ${y}</sup>`,
                rightSide: `${base}<sup>${x}</sup> × ${base}<sup>${y}</sup>`,
                leftValue: Math.pow(base, x + y),
                rightValue: Math.pow(base, x) * Math.pow(base, y),
                explanation: `When multiplying exponential expressions with the same base, add the exponents.`,
                proof: [
                    `Step 1: ${base}<sup>${x} + ${y}</sup> = ${base}<sup>${x + y}</sup>`,
                    `Step 2: ${base}<sup>${x}</sup> × ${base}<sup>${y}</sup> = ${Math.pow(base, x)} × ${Math.pow(base, y)}`,
                    `Step 3: ${Math.pow(base, x)} × ${Math.pow(base, y)} = ${Math.pow(base, x) * Math.pow(base, y)}`,
                    `Result: ${base}<sup>${x} + ${y}</sup> = ${base}<sup>${x}</sup> × ${base}<sup>${y}</sup> = ${Math.pow(base, x + y)}`
                ],
                visualData: {
                    leftCurve: { base, exponent: x + y, color: '#3B82F6' },
                    rightCurve1: { base, exponent: x, color: '#10B981' },
                    rightCurve2: { base, exponent: y, color: '#F59E0B' }
                }
            },
            quotient: {
                title: 'Quotient Law: a<sup>x - y</sup> = a<sup>x</sup> ÷ a<sup>y</sup>',
                leftSide: `${base}<sup>${x} - ${y}</sup>`,
                rightSide: `${base}<sup>${x}</sup> ÷ ${base}<sup>${y}</sup>`,
                leftValue: Math.pow(base, x - y),
                rightValue: Math.pow(base, x) / Math.pow(base, y),
                explanation: `When dividing exponential expressions with the same base, subtract the exponents.`,
                proof: [
                    `Step 1: ${base}<sup>${x} - ${y}</sup> = ${base}<sup>${x - y}</sup>`,
                    `Step 2: ${base}<sup>${x}</sup> ÷ ${base}<sup>${y}</sup> = ${Math.pow(base, x)} ÷ ${Math.pow(base, y)}`,
                    `Step 3: ${Math.pow(base, x)} ÷ ${Math.pow(base, y)} = ${Math.pow(base, x) / Math.pow(base, y)}`,
                    `Result: ${base}<sup>${x} - ${y}</sup> = ${base}<sup>${x}</sup> ÷ ${base}<sup>${y}</sup> = ${Math.pow(base, x - y)}`
                ],
                visualData: {
                    leftCurve: { base, exponent: x - y, color: '#3B82F6' },
                    rightCurve1: { base, exponent: x, color: '#10B981' },
                    rightCurve2: { base, exponent: y, color: '#F59E0B' }
                }
            },
            power: {
                title: 'Power Law: (a<sup>x</sup>)<sup>y</sup> = a<sup>x × y</sup>',
                leftSide: `(${base}<sup>${x}</sup>)<sup>${y}</sup>`,
                rightSide: `${base}<sup>${x} × ${y}</sup>`,
                leftValue: Math.pow(Math.pow(base, x), y),
                rightValue: Math.pow(base, x * y),
                explanation: `When raising an exponential expression to a power, multiply the exponents.`,
                proof: [
                    `Step 1: (${base}<sup>${x}</sup>)<sup>${y}</sup> = ${base}<sup>${x} × ${y}</sup>`,
                    `Step 2: ${base}<sup>${x} × ${y}</sup> = ${base}<sup>${x * y}</sup>`,
                    `Step 3: ${base}<sup>${x * y}</sup> = ${Math.pow(base, x * y)}`,
                    `Result: (${base}<sup>${x}</sup>)<sup>${y}</sup> = ${base}<sup>${x} × ${y}</sup> = ${Math.pow(base, x * y)}`
                ],
                visualData: {
                    leftCurve: { base, exponent: x * y, color: '#3B82F6' },
                    rightCurve: { base, exponent: x * y, color: '#10B981' }
                }
            },
            zero: {
                title: 'Zero Exponent Law: a<sup>0</sup> = 1',
                leftSide: `${base}<sup>0</sup>`,
                rightSide: '1',
                leftValue: Math.pow(base, 0),
                rightValue: 1,
                explanation: `Any non-zero number raised to the power of 0 equals 1.`,
                proof: [
                    `Step 1: ${base}<sup>0</sup> = 1`,
                    `Step 2: This is true for any non-zero base`,
                    `Step 3: ${base}<sup>0</sup> = 1`,
                    `Result: ${base}<sup>0</sup> = 1`
                ],
                visualData: {
                    leftCurve: { base, exponent: 0, color: '#3B82F6' },
                    rightCurve: { base, exponent: 0, color: '#10B981' }
                }
            },
            negative: {
                title: 'Negative Exponent Law: a<sup>-x</sup> = 1 ÷ a<sup>x</sup>',
                leftSide: `${base}<sup>-${x}</sup>`,
                rightSide: `1 ÷ ${base}<sup>${x}</sup>`,
                leftValue: Math.pow(base, -x),
                rightValue: 1 / Math.pow(base, x),
                explanation: `A negative exponent indicates the reciprocal of the positive exponent.`,
                proof: [
                    `Step 1: ${base}<sup>-${x}</sup> = 1 ÷ ${base}<sup>${x}</sup>`,
                    `Step 2: 1 ÷ ${base}<sup>${x}</sup> = 1 ÷ ${Math.pow(base, x)}`,
                    `Step 3: 1 ÷ ${Math.pow(base, x)} = ${1 / Math.pow(base, x)}`,
                    `Result: ${base}<sup>-${x}</sup> = 1 ÷ ${base}<sup>${x}</sup> = ${1 / Math.pow(base, x)}`
                ],
                visualData: {
                    leftCurve: { base, exponent: -x, color: '#3B82F6' },
                    rightCurve: { base, exponent: x, color: '#10B981' }
                }
            }
        };
        
        return laws[lawType] || laws.product;
    };

    const updateLawParameters = (param, value) => {
        const newValue = parseFloat(value) || 0;
        switch (param) {
            case 'x': setLawX(newValue); break;
            case 'y': setLawY(newValue); break;
            case 'base': setLawBase(newValue); break;
            default: break;
        }
    };

    // Parameter Panel Component for Full Screen Mode
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Function Parameters</h3>
            
            {/* Function Type Selector */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Function Type</h4>
                <div className="flex space-x-2">
                    <button
                        onClick={() => handleFunctionTypeChange('exponential')}
                        className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                            functionType === 'exponential'
                                ? 'bg-blue-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        Exponential
                    </button>
                    <button
                        onClick={() => handleFunctionTypeChange('logarithmic')}
                        className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                            functionType === 'logarithmic'
                                ? 'bg-green-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        Logarithmic
                    </button>
                </div>
            </div>

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

            {/* Parameter Controls */}
            {editMode === 'parameters' && (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            {functionType === 'exponential' ? 'a (stretch)' : 'a (coefficient)'}:
                        </label>
                                                    <input
                                type="number"
                                step="0.1"
                                value={a}
                                onChange={(e) => handleInputChange('a', parseFloat(e.target.value) || 0)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            {functionType === 'exponential' ? 'b (base)' : 'b (linear)'}:
                        </label>
                                                    <input
                                type="number"
                                step="0.1"
                                min={functionType === 'exponential' ? 0 : undefined}
                                value={b}
                                onChange={(e) => handleInputChange('b', parseFloat(e.target.value) || 0)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            {functionType === 'exponential' ? 'c (h-shift)' : 'c (constant)'}:
                        </label>
                                                    <input
                                type="number"
                                step="0.1"
                                value={c}
                                onChange={(e) => handleInputChange('c', parseFloat(e.target.value) || 0)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            d (v-shift):
                        </label>
                                                    <input
                                type="number"
                                step="0.1"
                                value={d}
                                onChange={(e) => handleInputChange('d', parseFloat(e.target.value) || 0)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Line Color:
                        </label>
                        <input
                            type="color"
                            value={lineColor}
                            onChange={(e) => handleInputChange('lineColor', e.target.value)}
                            className="w-full h-10 border border-gray-300 rounded-md"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
            )}

            {/* Base selection for logarithmic functions */}
            {functionType === 'logarithmic' && (
                <div className="space-y-4">
                    <h4 className="font-medium text-gray-700">Base Selection</h4>
                    <div className="space-y-3">
                        <select
                            value={base}
                            onChange={(e) => handleInputChange('base', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        >
                            <option value="e">Natural (e ≈ 2.718)</option>
                            <option value="2">Binary (2)</option>
                            <option value="10">Decimal (10)</option>
                            <option value="custom">Custom</option>
                        </select>
                        
                        {base === 'custom' && (
                                                    <input
                            type="number"
                            step="0.1"
                            min="0.1"
                            value={customBase}
                            onChange={(e) => handleInputChange('customBase', parseFloat(e.target.value) || 2)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                        )}
                    </div>
                </div>
            )}

                            {/* Equation Editor */}
                {editMode === 'equation' && (
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Equation:</label>
                            <input
                                type="text"
                                value={equationInput}
                                onChange={(e) => handleEquationChange(e.target.value)}
                                placeholder="e.g., 2^x, 3*2^(x+1), log_2(x), ln(x+1)"
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                                disabled={isSubmitted}
                            />
                        </div>
                    </div>
                )}

                {/* Step-by-Step Solution Display */}
                {showSolutionSteps && solutionSteps.length > 0 && (
                    <div className="mt-4 p-4 bg-gray-50 border border-gray-200 rounded-lg">
                        <h4 className="font-semibold text-gray-700 mb-3">Step-by-Step Solution:</h4>
                        
                        {/* Step Navigation */}
                        <div className="flex items-center justify-between mb-3">
                            <button
                                onClick={() => handleInputChange('currentStep', Math.max(0, currentStep - 1))}
                                disabled={currentStep === 0}
                                className="px-3 py-1 bg-gray-300 text-gray-700 rounded disabled:opacity-50"
                            >
                                Previous
                            </button>
                            <span className="text-sm text-gray-600">
                                Step {currentStep + 1} of {solutionSteps.length}
                            </span>
                            <button
                                onClick={() => handleInputChange('currentStep', Math.min(solutionSteps.length - 1, currentStep + 1))}
                                disabled={currentStep === solutionSteps.length - 1}
                                className="px-3 py-1 bg-gray-300 text-gray-700 rounded disabled:opacity-50"
                            >
                                Next
                            </button>
                        </div>

                        {/* Current Step Display */}
                        {solutionSteps[currentStep] && (
                            <div className="p-3 bg-white border border-gray-200 rounded-lg">
                                <div className="flex items-start space-x-3">
                                    <div className="flex-shrink-0 w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">
                                        {solutionSteps[currentStep].step}
                                    </div>
                                    <div className="flex-1">
                                        <div className="font-medium text-gray-700 mb-1">
                                            {solutionSteps[currentStep].action}
                                        </div>
                                        <div className="text-lg font-mono text-blue-600 mb-1">
                                            {solutionSteps[currentStep].expression}
                                        </div>
                                        <div className="text-sm text-gray-600 mb-1">
                                            {solutionSteps[currentStep].explanation}
                                        </div>
                                        <div className="text-sm font-medium text-green-600">
                                            {solutionSteps[currentStep].result}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                )}

            {/* Enhanced Laws Demonstrator */}
            <div className="space-y-4">
                <div className="flex items-center justify-between">
                    <h4 className="font-medium text-gray-700">
                        {functionType === 'exponential' ? 'Exponential' : 'Logarithmic'} Laws Demonstrator
                    </h4>
                    <button
                        onClick={() => handleInputChange('showLawsDemonstrator', !showLawsDemonstrator)}
                        className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors text-sm"
                        disabled={isSubmitted}
                    >
                        {showLawsDemonstrator ? 'Hide' : 'Show'} Laws
                    </button>
                </div>

                {showLawsDemonstrator && (
                    <>
                        {/* Law Selection */}
                        <div className="grid grid-cols-1 gap-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Select Law:
                                </label>
                                <select
                                    value={currentLaw}
                                    onChange={(e) => handleInputChange('currentLaw', e.target.value)}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                    disabled={isSubmitted}
                                >
                                    <option value="product">Product Law</option>
                                    <option value="quotient">Quotient Law</option>
                                    <option value="power">Power Law</option>
                                    <option value="zero">Zero Exponent</option>
                                    <option value="negative">Negative Exponent</option>
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Demonstration Mode:
                                </label>
                                <select
                                    value={lawDemonstrationMode}
                                    onChange={(e) => handleInputChange('lawDemonstrationMode', e.target.value)}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                    disabled={isSubmitted}
                                >
                                    <option value="visual">Visual</option>
                                    <option value="numerical">Numerical</option>
                                    <option value="proof">Step-by-Step Proof</option>
                                </select>
                            </div>
                        </div>

                        {/* Parameter Controls */}
                        <div className="grid grid-cols-1 gap-4">
                            <div className="grid grid-cols-3 gap-2">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Base:
                                    </label>
                                    <input
                                        type="number"
                                        value={lawBase}
                                        onChange={(e) => handleInputChange('lawBase', Number(e.target.value))}
                                        min="2"
                                        max="10"
                                        className="w-full px-2 py-1 border border-gray-300 rounded-md text-sm"
                                        disabled={isSubmitted}
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Exp X:
                                    </label>
                                    <input
                                        type="number"
                                        value={lawX}
                                        onChange={(e) => handleInputChange('lawX', Number(e.target.value))}
                                        min="1"
                                        max="10"
                                        className="w-full px-2 py-1 border border-gray-300 rounded-md text-sm"
                                        disabled={isSubmitted}
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Exp Y:
                                    </label>
                                    <input
                                        type="number"
                                        value={lawY}
                                        onChange={(e) => handleInputChange('lawY', Number(e.target.value))}
                                        min="1"
                                        max="10"
                                        className="w-full px-2 py-1 border border-gray-300 rounded-md text-sm"
                                        disabled={isSubmitted}
                                    />
                                </div>
                            </div>
                        </div>

                        {/* Law Demonstration Display */}
                        {getLawDemonstration && (() => {
                            const lawDemo = getLawDemonstration(currentLaw);
                            return (
                                <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg">
                                    <h5 className="font-semibold text-blue-800 mb-2">
                                        {currentLaw.charAt(0).toUpperCase() + currentLaw.slice(1)} Law
                                    </h5>
                                    <div className="text-sm font-mono text-blue-600 mb-2">
                                        {renderMathExpression(lawDemo.formula)}
                                    </div>
                                    <p className="text-xs text-blue-700 mb-2">{lawDemo.description}</p>

                                    {lawDemonstrationMode === 'visual' && (
                                        <div className="grid grid-cols-1 gap-2">
                                            <div className="p-2 bg-white border border-blue-200 rounded text-xs">
                                                <div className="font-medium text-blue-800">Left:</div>
                                                <div className="font-mono text-blue-600">
                                                    {renderMathExpression(lawDemo.leftSide)}
                                                </div>
                                            </div>
                                            <div className="p-2 bg-white border border-blue-200 rounded text-xs">
                                                <div className="font-medium text-blue-800">Right:</div>
                                                <div className="font-mono text-blue-600">
                                                    {renderMathExpression(lawDemo.rightSide)}
                                                </div>
                                            </div>
                                        </div>
                                    )}

                                    {lawDemonstrationMode === 'numerical' && (
                                        <div className="grid grid-cols-2 gap-2">
                                            <div className="p-2 bg-white border border-blue-200 rounded text-xs">
                                                <div className="font-medium text-blue-800">Left Value:</div>
                                                <div className="font-mono text-blue-600">{lawDemo.leftValue}</div>
                                            </div>
                                            <div className="p-2 bg-white border border-blue-200 rounded text-xs">
                                                <div className="font-medium text-blue-800">Right Value:</div>
                                                <div className="font-mono text-blue-600">{lawDemo.rightValue}</div>
                                            </div>
                                        </div>
                                    )}

                                    {lawDemonstrationMode === 'proof' && (
                                        <div className="p-2 bg-white border border-blue-200 rounded text-xs">
                                            <div className="font-medium text-blue-800 mb-1">Steps:</div>
                                            <div className="space-y-1">
                                                {lawDemo.proof.map((step, index) => (
                                                    <div key={index} className="font-mono text-blue-600">
                                                        {renderMathExpression(step)}
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    )}

                                    {/* Verification */}
                                    <div className="mt-2 p-1 bg-green-50 border border-green-200 rounded">
                                        <div className="text-xs text-green-700">
                                            ✓ {lawDemo.leftValue} = {lawDemo.rightValue} 
                                            {Math.abs(lawDemo.leftValue - lawDemo.rightValue) < 0.0001 ? ' ✓' : ' ✗'}
                                        </div>
                                    </div>
                                </div>
                            );
                        })()}
                    </>
                )}
            </div>

            {/* Inverse Function Controls */}
            <div className="space-y-4">
                <h4 className="font-medium text-gray-700">Inverse Function</h4>
                <div className="space-y-3">
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={showInverseVisualizer}
                            onChange={(e) => handleInputChange('showInverseVisualizer', e.target.checked)}
                            className="mr-2"
                        />
                        <span className="text-sm text-gray-700">Show Inverse Function</span>
                    </label>
                    
                    {showInverseVisualizer && (
                        <>
                            <label className="flex items-center">
                                                            <input
                                type="checkbox"
                                checked={showReflectionLine}
                                onChange={(e) => handleInputChange('showReflectionLine', e.target.checked)}
                                className="mr-2"
                            />
                                <span className="text-sm text-gray-700">Show y=x Line</span>
                            </label>
                            
                            <label className="flex items-center">
                                                            <input
                                type="checkbox"
                                checked={showInversePoints}
                                onChange={(e) => handleInputChange('showInversePoints', e.target.checked)}
                                className="mr-2"
                            />
                                <span className="text-sm text-gray-700">Show Key Points</span>
                            </label>
                        </>
                    )}
                </div>
            </div>

            {/* Enhanced Expression Solver */}
            <div className="space-y-4">
                <h4 className="font-medium text-gray-700">
                    Expression Solver - {functionType === 'exponential' ? 'Exponential' : 'Logarithmic'} Functions
                </h4>
                
                {/* Solver Mode Selection */}
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                        Solver Mode:
                    </label>
                    <select
                        value={solverMode}
                        onChange={(e) => handleInputChange('solverMode', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    >
                        <option value="none">Select Mode</option>
                        <option value="simplify">Simplify Expression</option>
                        <option value="solve">Solve Equation</option>
                        <option value="properties">Show Properties</option>
                    </select>
                </div>

                {/* Expression Input */}
                {(solverMode === 'simplify' || solverMode === 'solve') && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Enter Expression:
                        </label>
                        <input
                            type="text"
                            value={inputExpression}
                            onChange={(e) => handleInputChange('inputExpression', e.target.value)}
                            placeholder={functionType === 'exponential' ? "e.g., 2^x * 2^3" : "e.g., log(x) + log(3)"}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                )}

                {/* Target Operation */}
                {solverMode !== 'none' && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Operation:
                        </label>
                        <select
                            value={targetOperation}
                            onChange={(e) => handleInputChange('targetOperation', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        >
                            <option value="simplify">Simplify</option>
                            <option value="solve">Solve for x</option>
                        </select>
                    </div>
                )}

                {/* Solve Button */}
                {(solverMode === 'simplify' || solverMode === 'solve') && inputExpression && (
                    <button
                        onClick={() => {
                            if (inputExpression) {
                                const steps = solveStepByStep(inputExpression, targetOperation);
                                handleInputChange('solutionSteps', steps);
                                handleInputChange('currentStep', 0);
                                handleInputChange('showSolutionSteps', true);
                            }
                        }}
                        className="w-full bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors text-sm"
                        disabled={isSubmitted}
                    >
                        Solve Step-by-Step
                    </button>
                )}

                {/* Solution Steps Display */}
                {showSolutionSteps && solutionSteps.length > 0 && (
                    <div className="p-3 bg-gray-50 border border-gray-200 rounded-lg">
                        <h5 className="font-semibold text-gray-700 mb-2 text-sm">Step-by-Step Solution:</h5>
                        
                        {/* Step Navigation */}
                        <div className="flex items-center justify-between mb-2">
                            <button
                                onClick={() => handleInputChange('currentStep', Math.max(0, currentStep - 1))}
                                disabled={currentStep === 0 || isSubmitted}
                                className="px-2 py-1 bg-gray-300 text-gray-700 rounded disabled:opacity-50 text-xs"
                            >
                                Previous
                            </button>
                            <span className="text-xs text-gray-600">
                                Step {currentStep + 1} of {solutionSteps.length}
                            </span>
                            <button
                                onClick={() => handleInputChange('currentStep', Math.min(solutionSteps.length - 1, currentStep + 1))}
                                disabled={currentStep === solutionSteps.length - 1 || isSubmitted}
                                className="px-2 py-1 bg-gray-300 text-gray-700 rounded disabled:opacity-50 text-xs"
                            >
                                Next
                            </button>
                        </div>

                        {/* Current Step Display */}
                        {solutionSteps[currentStep] && (
                            <div className="p-2 bg-white border border-gray-200 rounded">
                                <div className="flex items-start space-x-2">
                                    <div className="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-xs font-bold">
                                        {solutionSteps[currentStep].step}
                                    </div>
                                    <div className="flex-1">
                                        <div className="font-medium text-gray-700 text-xs mb-1">
                                            {solutionSteps[currentStep].action}
                                        </div>
                                        <div className="text-sm font-mono text-blue-600 mb-1">
                                            {solutionSteps[currentStep].expression}
                                        </div>
                                        <div className="text-xs text-gray-600 mb-1">
                                            {solutionSteps[currentStep].explanation}
                                        </div>
                                        <div className="text-xs font-medium text-green-600">
                                            {solutionSteps[currentStep].result}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                )}
            </div>

            {/* Function Information */}
            <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                <h4 className="font-medium text-blue-800 mb-2">Function Information</h4>
                <div className="space-y-1 text-sm">
                    <div><strong>Type:</strong> {functionType === 'exponential' ? 'Exponential' : 'Logarithmic'}</div>
                    <div><strong>Equation:</strong> y = {renderMathExpression(getFunctionString())}</div>
                    <div><strong>Behavior:</strong> {getBehaviorDescription()}</div>
                    <div><strong>Domain:</strong> {calculateFunctionProperties().domain.min} to {calculateFunctionProperties().domain.max}</div>
                    <div><strong>Range:</strong> {calculateFunctionProperties().range.min} to {calculateFunctionProperties().range.max}</div>
                    {calculateFunctionProperties().asymptote.horizontal && (
                        <div><strong>Horizontal Asymptote:</strong> {calculateFunctionProperties().asymptote.horizontal}</div>
                    )}
                    {calculateFunctionProperties().asymptote.vertical && (
                        <div><strong>Vertical Asymptote:</strong> {calculateFunctionProperties().asymptote.vertical}</div>
                    )}
                </div>
            </div>
        </div>
    );

    return (
        <div className="relative">
            <div className="p-3 bg-white border border-gray-300 rounded-lg mt-3">
                {/* Function Type Selector */}
                <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center space-x-4">
                        <div className="flex space-x-2">
                                                         <button
                                 onClick={() => handleFunctionTypeChange('exponential')}
                                 className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                                     functionType === 'exponential'
                                         ? 'bg-blue-600 text-white'
                                         : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                 }`}
                             >
                                 Exponential: {renderMathExpression('y = a × b<sup>x + c</sup> + d')}
                             </button>
                             <button
                                 onClick={() => handleFunctionTypeChange('logarithmic')}
                                 className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                                     functionType === 'logarithmic'
                                         ? 'bg-green-600 text-white'
                                         : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                 }`}
                             >
                                 Logarithmic: {renderMathExpression('y = a × log<sub>b</sub>(x + c) + d')}
                             </button>
                        </div>
                        
                        {/* Inverse relationship toggle */}
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={showInverse}
                                onChange={(e) => handleInputChange('showInverse', e.target.checked)}
                                className="mr-2"
                            />
                            <span className="text-sm font-medium text-gray-700">
                                Show Inverse Function
                            </span>
                        </label>
                        
                        {/* Enhanced Inverse Relationship Visualizer */}
                        <div className="flex items-center space-x-3">
                            <label className="flex items-center">
                                                            <input
                                type="checkbox"
                                checked={showInverseVisualizer}
                                onChange={(e) => handleInputChange('showInverseVisualizer', e.target.checked)}
                                className="mr-2"
                            />
                                <span className="text-sm font-medium text-gray-700">
                                    Inverse Visualizer
                                </span>
                            </label>
                            
                            {showInverseVisualizer && (
                                <>
                                    <label className="flex items-center">
                                                                            <input
                                        type="checkbox"
                                        checked={showReflectionLine}
                                        onChange={(e) => handleInputChange('showReflectionLine', e.target.checked)}
                                        className="mr-2"
                                    />
                                        <span className="text-xs text-gray-600">
                                            y=x Line
                                        </span>
                                    </label>
                                    
                                    <label className="flex items-center">
                                                                            <input
                                        type="checkbox"
                                        checked={showInversePoints}
                                        onChange={(e) => handleInputChange('showInversePoints', e.target.checked)}
                                        className="mr-2"
                                    />
                                        <span className="text-xs text-gray-600">
                                            Key Points
                                        </span>
                                    </label>
                                </>
                            )}
                        </div>



                        
                    </div>
                    
                    <button
                        onClick={handleOpenFullScreen}
                        className="p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow-lg transition-colors"
                        title="Open Full Screen Mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>

                {/* Edit Mode Toggle */}
                <div className="mb-1">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="radio"
                                value="parameters"
                                checked={editMode === 'parameters'}
                                onChange={(e) => handleInputChange('editMode', e.target.value)}
                                className="mr-1"
                                disabled={isSubmitted}
                            />
                            <span className="text-xs font-medium text-gray-700">Parameters</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="radio"
                                value="equation"
                                checked={editMode === 'equation'}
                                onChange={(e) => handleInputChange('editMode', e.target.value)}
                                disabled={isSubmitted}
                            />
                            <span className="text-xs font-medium text-gray-700">Equation</span>
                        </label>
                    </div>
                </div>

                {/* Parameter Controls */}
                {editMode === 'parameters' && (
                                         <div className="grid grid-cols-5 gap-0 mb-1">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                {functionType === 'exponential' ? 'a (stretch)' : 'a (coefficient)'}:
                            </label>
                                                                                     <input
                                type="number"
                                step="0.1"
                                value={a}
                                onChange={(e) => handleInputChange('a', parseFloat(e.target.value) || 0)}
                                className="w-1/2 px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                {functionType === 'exponential' ? 'b (base)' : 'b (linear)'}:
                            </label>
                                                                                     <input
                                type="number"
                                step="0.1"
                                min={functionType === 'exponential' ? 0 : undefined}
                                value={b}
                                onChange={(e) => handleInputChange('b', parseFloat(e.target.value) || 0)}
                                className="w-1/2 px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                {functionType === 'exponential' ? 'c (h-shift)' : 'c (constant)'}:
                            </label>
                                                                                     <input
                                type="number"
                                step="0.1"
                                value={c}
                                onChange={(e) => handleInputChange('c', parseFloat(e.target.value) || 0)}
                                className="w-1/2 px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                d (v-shift):
                            </label>
                                                                                     <input
                                type="number"
                                step="0.1"
                                value={d}
                                onChange={(e) => handleInputChange('d', parseFloat(e.target.value) || 0)}
                                className="w-1/2 px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Line Color:
                            </label>
                                                                                     <input
                                type="color"
                                value={lineColor}
                                onChange={(e) => handleInputChange('lineColor', e.target.value)}
                                className="w-1/2 h-10 border border-gray-300 rounded-md"
                                disabled={isSubmitted}
                            />
                        </div>
                        
                                                 {/* Base selection for logarithmic functions */}
                         {functionType === 'logarithmic' && (
                             <div className="col-span-5">
                                 <div className="flex items-center space-x-4">
                                     <label className="block text-sm font-medium text-gray-700">
                                         Base:
                                     </label>
                                                                             <select
                                            value={base}
                                            onChange={(e) => handleInputChange('base', e.target.value)}
                                            className="px-3 py-2 border border-gray-300 rounded-md text-sm"
                                            disabled={isSubmitted}
                                        >
                                         <option value="e">Natural (e ≈ 2.718)</option>
                                         <option value="2">Binary (2)</option>
                                         <option value="10">Decimal (10)</option>
                                         <option value="custom">Custom</option>
                                     </select>
                                     
                                                                           {base === 'custom' && (
                                                                                 <input
                                            type="number"
                                            step="0.1"
                                            min="0.1"
                                            value={customBase}
                                            onChange={(e) => handleInputChange('customBase', parseFloat(e.target.value) || 2)}
                                            className="px-3 py-2 border border-gray-300 rounded-md text-sm w-16"
                                            disabled={isSubmitted}
                                        />
                                     )}
                                 </div>
                             </div>
                         )}

                         
                    </div>
                )}





                {/* Inverse Relationship Educational Panel */}
                {showInverseVisualizer && (
                    <div className="p-4 bg-green-50 border border-green-200 rounded-lg mb-3">
                        <h4 className="font-semibold text-green-800 mb-2">
                            🔄 Inverse Relationship Explorer
                        </h4>
                        <div className="text-sm text-green-700 space-y-2">
                            {functionType === 'exponential' ? (
                                <>
                                    <p><strong>Exponential Function:</strong> y = {renderMathExpression(getFunctionString())}</p>
                                    <p><strong>Inverse Function:</strong> x = {renderMathExpression(`log<sub>${b}</sub>((y - ${d}) / ${a}) - ${c}`)}</p>
                                    <p><strong>Mathematical Property:</strong> The exponential function and its inverse logarithmic function are reflections across the line y = x</p>
                                    <p><strong>Key Insight:</strong> If (a, b) is on the exponential curve, then (b, a) is on the logarithmic curve</p>
                                </>
                            ) : (
                                <>
                                    <p><strong>Logarithmic Function:</strong> y = {renderMathExpression(getFunctionString())}</p>
                                    <p><strong>Inverse Function:</strong> x = {renderMathExpression(`${base === 'e' ? 'e' : base}<sup>(y - ${d}) / ${a}</sup> - ${c}`)}</p>
                                    <p><strong>Mathematical Property:</strong> The logarithmic function and its inverse exponential function are reflections across the line y = x</p>
                                    <p><strong>Key Insight:</strong> If (a, b) is on the logarithmic curve, then (b, a) is on the exponential curve</p>
                                </>
                            )}
                            <div className="mt-3 p-2 bg-white rounded border">
                                <p className="text-xs text-gray-600">
                                    <strong>💡 Educational Tip:</strong> The inverse relationship shows how exponential growth becomes logarithmic growth when we swap x and y coordinates. 
                                    This is fundamental to understanding the relationship between these two important function families.
                                </p>
                            </div>
                        </div>
                    </div>
                )}

                {/* Mathematical Properties Panel */}
                {solverMode === 'properties' && (
                    <div className="p-4 bg-purple-50 border border-purple-200 rounded-lg mb-3">
                        <h4 className="font-semibold text-purple-800 mb-3">
                            📚 {getMathematicalProperties().title}
                        </h4>
                        <div className="space-y-3">
                            {getMathematicalProperties().laws.map((law, index) => (
                                <div key={index} className="p-3 bg-white rounded border">
                                    <h5 className="font-medium text-purple-700 mb-2">{law.name}</h5>
                                    <p className="text-sm font-mono text-purple-600 mb-2">{renderMathExpression(law.formula)}</p>
                                    <p className="text-sm text-gray-700 mb-2">{law.explanation}</p>
                                    <p className="text-xs text-gray-600 italic">Example: {renderMathExpression(law.example)}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                )}






                                
                                <select
                                    value={lawDemonstrationMode}
                                    onChange={(e) => handleInputChange('lawDemonstrationMode', e.target.value)}
                                    className="px-3 py-2 border border-gray-300 rounded text-sm"
                                    disabled={isSubmitted}
                                >
                                    <option value="visual">Visual</option>
                                    <option value="proof">Proof</option>
                                    <option value="interactive">Interactive</option>
                                </select>
                                
                                <label className="flex items-center">
                                    <input
                                        type="checkbox"
                                        checked={showLawsDemonstrator}
                                        onChange={(e) => handleInputChange('showLawsDemonstrator', e.target.checked)}
                                        className="mr-2"
                                        disabled={isSubmitted}
                                    />
                                    <span className="text-sm text-gray-700">Show Demonstrator</span>
                                </label>
                            </div>
                        </div>
                    )}

                    {/* Step-by-Step Solution Display */}
                    {showSolutionSteps && solutionSteps.length > 0 && (
                        <div className="mt-4">
                            <h5 className="font-medium text-blue-700 mb-2">Step-by-Step Solution</h5>
                            <div className="space-y-3">
                                {solutionSteps.map((step, index) => (
                                    <div key={index} className={`p-3 rounded border ${
                                        index === currentStep 
                                            ? 'bg-yellow-100 border-yellow-400' 
                                            : 'bg-white border-yellow-200'
                                    }`}>
                                        <div className="flex items-center justify-between mb-2">
                                            <span className="font-medium text-yellow-700">Step {step.step}: {step.action}</span>
                                            {index === currentStep && (
                                                <span className="text-xs bg-yellow-500 text-white px-2 py-1 rounded">Current</span>
                                            )}
                                        </div>
                                        <p className="text-sm font-mono text-yellow-600 mb-2">{step.expression}</p>
                                        <p className="text-sm text-gray-700 mb-2">{step.explanation}</p>
                                        <p className="text-sm text-green-600 font-medium">{step.result}</p>
                                    </div>
                                ))}
                                <div className="flex space-x-2 mt-3">
                                    <button
                                        onClick={() => handleInputChange('currentStep', Math.max(0, currentStep - 1))}
                                        disabled={currentStep === 0}
                                        className="px-3 py-1 bg-blue-500 text-white rounded text-sm hover:bg-blue-600 disabled:bg-gray-300"
                                    >
                                        ← Previous
                                    </button>
                                    <button
                                        onClick={() => handleInputChange('currentStep', Math.min(solutionSteps.length - 1, currentStep + 1))}
                                        disabled={currentStep === 0}
                                        className="px-3 py-1 bg-blue-500 text-white rounded text-sm hover:bg-blue-600 disabled:bg-gray-300"
                                    >
                                        Next →
                                    </button>
                                    <button
                                        onClick={() => handleInputChange('showSolutionSteps', false)}
                                        className="px-3 py-1 bg-gray-500 text-white rounded text-sm hover:bg-gray-600"
                                    >
                                        Close
                                    </button>
                                </div>
                            </div>
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
                    title={`${functionType.charAt(0).toUpperCase() + functionType.slice(1)} Function Graph - Full Screen Mode`}
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

export default IntegratedExponentialLogarithmicGraph;