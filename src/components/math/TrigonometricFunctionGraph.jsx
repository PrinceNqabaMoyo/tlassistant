import React, { useState, useEffect, useRef } from 'react';
import { Maximize2, TrendingUp, RotateCcw } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';
import UnitCircle from './UnitCircle';

const TrigonometricFunctionGraph = ({ initialData, onChange, isSubmitted }) => {
    const [graphData, setGraphData] = useState(initialData || {
        title: "Trigonometric Function",
        funcType: 'sin',
        a: 1,
        b: 1,
        c: 0,
        d: 0,
        equation: "sin(x)",
        x_range: [-10, 10],
        y_range: [-3, 3],
        lineColor: '#3B82F6',
        showGrid: true,
        showPoints: true,
        showAsymptotes: true,
        showPeriod: true,
        showAmplitude: true,
        showPhaseShift: true,
        angleUnit: 'radians', // 'radians' or 'degrees'

        samplingDensity: 16, // New: control sampling density for smooth curves
        showSolutionTools: false, // New: show solution tools
        identityInput: '', // New: input for identity verification
        identityResult: null, // New: result of identity verification
        showUnitCircle: false, // New: show unit circle reference
        unitCircleAngle: 0 // New: current angle for unit circle
    });

    // Store ranges for each function type independently
    const [functionRanges, setFunctionRanges] = useState({
        sin: { x: [-360, 360], y: [-3, 3] },
        cos: { x: [-360, 360], y: [-3, 3] },
        tan: { x: [-360, 360], y: [-15, 15] }, // Special range for tan as requested
        csc: { x: [-360, 360], y: [-10, 10] },
        sec: { x: [-360, 360], y: [-10, 10] },
        cot: { x: [-360, 360], y: [-3, 3] }
    });

    // Helper function to get appropriate default ranges based on function type and angle unit
    const getDefaultRanges = (funcType, angleUnit) => {
        if (angleUnit === 'degrees') {
            const xRange = [-360, 360];
            let yRange;
            
            switch (funcType) {
                case 'tan':
                    yRange = [-15, 15]; // Special range for tan as requested
                    break;
                case 'csc':
                case 'sec':
                    yRange = [-10, 10]; // Reciprocal functions
                    break;
                default:
                    yRange = [-3, 3]; // Standard range for sin, cos, cot
            }
            
            return { xRange, yRange };
        } else {
            // Radians mode
            const xRange = [-4 * Math.PI, 4 * Math.PI]; // -4π to 4π
            let yRange;
            
            switch (funcType) {
                case 'tan':
                    yRange = [-15, 15]; // Special range for tan as requested
                    break;
                case 'csc':
                case 'sec':
                    yRange = [-10, 10]; // Reciprocal functions
                    break;
                default:
                    yRange = [-3, 3]; // Standard range for sin, cos, cot
            }
            
            return { xRange, yRange };
        }
    };

    // Helper function to generate proper equation string
    const generateEquation = (funcType, a, b, c, d) => {
        let eq = '';
        
        // Add amplitude if not 1
        if (a !== 1) {
            eq += a;
        }
        
        // Add function
        eq += funcType + '(';
        
        // Add frequency if not 1
        if (b !== 1) {
            eq += b;
        }
        eq += 'x';
        
        // Add phase shift if not 0
        if (c !== 0) {
            eq += c > 0 ? '+' + c : c;
        }
        
        eq += ')';
        
        // Add vertical shift if not 0
        if (d !== 0) {
            eq += d > 0 ? '+' + d : d;
        }
        
        return eq;
    };

    // Initialize ranges when component first loads
    useEffect(() => {
        const { xRange, yRange } = getDefaultRanges(graphData.funcType, graphData.angleUnit);
        setGraphData(prev => ({
            ...prev,
            x_range: xRange,
            y_range: yRange
        }));
    }, []); // Empty dependency array means this runs only once on mount

    // Identity verification function
    const verifyIdentity = () => {
        const input = graphData.identityInput.trim();
        if (!input) {
            setGraphData(prev => ({ ...prev, identityResult: { isValid: false, explanation: 'Please enter an expression.' } }));
            return;
        }

        try {
            // Parse the input to check for common identities
            const inputLower = input.toLowerCase().replace(/\s/g, '');
            
            // Check for common known identities
            const knownIdentities = [
                { pattern: 'sin²θ+cos²θ', result: 1, name: 'Pythagorean Identity: sin²θ + cos²θ = 1' },
                { pattern: '1+tan²θ', result: 'sec²θ', name: 'Pythagorean Identity: 1 + tan²θ = sec²θ' },
                { pattern: '1+cot²θ', result: 'csc²θ', name: 'Pythagorean Identity: 1 + cot²θ = csc²θ' },
                { pattern: 'sin(2θ)', result: '2sin(θ)cos(θ)', name: 'Double Angle: sin(2θ) = 2sin(θ)cos(θ)' },
                { pattern: 'cos(2θ)', result: 'cos²θ-sin²θ', name: 'Double Angle: cos(2θ) = cos²θ - sin²θ' },
                { pattern: 'tan(2θ)', result: '2tan(θ)/(1-tan²θ)', name: 'Double Angle: tan(2θ) = 2tan(θ)/(1-tan²θ)' }
            ];

            // Check if input matches any known identity
            for (const identity of knownIdentities) {
                if (inputLower.includes(identity.pattern) || inputLower.includes(identity.result)) {
                    setGraphData(prev => ({
                        ...prev,
                        identityResult: { 
                            isValid: true, 
                            explanation: `✅ ${identity.name} - This is a well-known trigonometric identity.` 
                        }
                    }));
                    return;
                }
            }

            // For more complex expressions, try numerical verification
            const testValues = [0, Math.PI/6, Math.PI/4, Math.PI/3, Math.PI/2]; // Test at common angles
            let allValid = true;
            let testResults = [];

            for (const angle of testValues) {
                try {
                    // Replace θ with the test angle and evaluate
                    let testExpression = input
                        .replace(/θ/g, angle.toString())
                        .replace(/²/g, '**2')
                        .replace(/³/g, '**3')
                        .replace(/sin/g, 'Math.sin')
                        .replace(/cos/g, 'Math.cos')
                        .replace(/tan/g, 'Math.tan')
                        .replace(/csc/g, '1/Math.sin')
                        .replace(/sec/g, '1/Math.cos')
                        .replace(/cot/g, '1/Math.tan');

                    const result = eval(testExpression);
                    testResults.push({ angle: (angle * 180 / Math.PI).toFixed(0) + '°', result: result.toFixed(4) });
                    
                    // Check if result is finite
                    if (!isFinite(result)) {
                        allValid = false;
                        break;
                    }
                } catch (e) {
                    allValid = false;
                    break;
                }
            }

            if (allValid) {
                setGraphData(prev => ({
                    ...prev,
                    identityResult: { 
                        isValid: true, 
                        explanation: `✅ Expression evaluates to finite values at test angles: ${testResults.map(r => `${r.angle}: ${r.result}`).join(', ')}` 
                    }
                }));
            } else {
                setGraphData(prev => ({
                    ...prev,
                    identityResult: { 
                        isValid: false, 
                        explanation: `❌ Expression does not evaluate properly at all test angles. Check for division by zero or undefined values.` 
                    }
                }));
            }

        } catch (e) {
            setGraphData(prev => ({
                ...prev,
                identityResult: { 
                    isValid: false, 
                    explanation: `❌ Error evaluating expression: ${e.message}. Please check your syntax.` 
                }
            }));
        }
    };



    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);

    useEffect(() => {
        if (onChange) {
            onChange(graphData);
        }
    }, [graphData, onChange]);

    useEffect(() => {
        const timer = setTimeout(() => {
            drawGraph();
        }, 100);
        return () => clearTimeout(timer);
    }, [graphData]);

    useEffect(() => {
        drawGraph();
    }, []);

    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            drawGraph(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, graphData]);

    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            setCanvasDimensions(fullScreenCanvasRef.current);
            drawGraph(fullScreenCanvasRef.current);
        }
    }, [isFullScreenOpen, graphData]);

    // Calculate trigonometric function value
    const calculateTrigValue = (x, funcType, a, b, c, d) => {
        let xRad = x;
        if (graphData.angleUnit === 'degrees') {
            xRad = (x * Math.PI) / 180;
        }
        
        let y;
        switch (funcType) {
            case 'sin':
                y = a * Math.sin(b * xRad + c) + d;
                break;
            case 'cos':
                y = a * Math.cos(b * xRad + c) + d;
                break;
            case 'tan':
                y = a * Math.tan(b * xRad + c) + d;
                break;
            case 'csc':
                y = a / Math.sin(b * xRad + c) + d;
                break;
            case 'sec':
                y = a / Math.cos(b * xRad + c) + d;
                break;
            case 'cot':
                y = a / Math.tan(b * xRad + c) + d;
                break;
            default:
                y = 0;
        }
        
        // Handle asymptotes for reciprocal functions
        if (funcType === 'tan' || funcType === 'csc' || funcType === 'sec' || funcType === 'cot') {
            if (!isFinite(y) || Math.abs(y) > 1000) {
                return null; // Asymptote
            }
        }
        
        return y;
    };



    // Find asymptotes for reciprocal functions
    const findAsymptotes = (funcType, b, c) => {
        if (b === 0) return [];
        
        const asymptotes = [];
        
        if (funcType === 'tan') {
            // Tan has asymptotes at odd multiples of 90° (or π/2 radians)
            if (graphData.angleUnit === 'degrees') {
                // Degrees: asymptotes at 90°, 270°, -90°, -270°, etc.
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = (2 * i + 1) * 90; // Odd multiples of 90°
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            } else {
                // Radians: asymptotes at π/2, 3π/2, -π/2, -3π/2, etc.
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = (2 * i + 1) * Math.PI / 2; // Odd multiples of π/2
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            }
        } else if (funcType === 'sec') {
            // Sec has asymptotes at the same locations as tan
            if (graphData.angleUnit === 'degrees') {
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = (2 * i + 1) * 90;
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            } else {
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = (2 * i + 1) * Math.PI / 2;
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            }
        } else if (funcType === 'cot') {
            // Cot has asymptotes at even multiples of 90° (or π/2 radians)
            if (graphData.angleUnit === 'degrees') {
                // Degrees: asymptotes at 0°, 180°, -180°, 360°, etc.
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = 2 * i * 90; // Even multiples of 90°
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            } else {
                // Radians: asymptotes at 0, π, -π, 2π, etc.
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = 2 * i * Math.PI / 2; // Even multiples of π/2
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            }
        } else if (funcType === 'csc') {
            // Csc has asymptotes at the same locations as cot
            if (graphData.angleUnit === 'degrees') {
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = 2 * i * 90;
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            } else {
                for (let i = -4; i <= 4; i++) {
                    const asymptoteAngle = 2 * i * Math.PI / 2;
                    const x = (asymptoteAngle - c) / b;
                    if (x >= graphData.x_range[0] && x <= graphData.x_range[1]) {
                        asymptotes.push(x);
                    }
                }
            }
        }
        
        return asymptotes;
    };

    // Calculate function properties
    const calculateProperties = () => {
        const { funcType, a, b, c, d } = graphData;
        
        if (b === 0) return { amplitude: 0, period: 0, phaseShift: 0, verticalShift: d };
        
        const amplitude = Math.abs(a);
        const period = graphData.angleUnit === 'degrees' ? 360 / Math.abs(b) : (2 * Math.PI) / Math.abs(b);
        const phaseShift = -c / b;
        const verticalShift = d;
        
        return { amplitude, period, phaseShift, verticalShift };
    };

    const drawGraph = (targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        // Calculate scale factors
        const xScale = width / (graphData.x_range[1] - graphData.x_range[0]);
        const yScale = height / (graphData.y_range[1] - graphData.y_range[0]);

        // Draw grid
        if (graphData.showGrid) {
            drawGrid(ctx, width, height, xScale, yScale);
        }

        // Draw axes
        drawAxes(ctx, width, height, xScale, yScale);

        // Draw asymptotes
        if (graphData.showAsymptotes) {
            const asymptotes = findAsymptotes(graphData.funcType, graphData.b, graphData.c);
            drawAsymptotes(ctx, asymptotes, xScale, yScale, width, height);
        }



        // Draw main function
        drawFunction(ctx, width, height, xScale, yScale);

        // Draw special points and lines
        if (graphData.showPeriod || graphData.showAmplitude || graphData.showPhaseShift) {
            drawSpecialFeatures(ctx, width, height, xScale, yScale);
        }
    };

    const drawGrid = (ctx, width, height, xScale, yScale) => {
        ctx.strokeStyle = '#f0f0f0';
        ctx.lineWidth = 1;

        // Vertical grid lines aligned with major angle marks
        if (graphData.angleUnit === 'degrees') {
            // Degrees: grid lines at 90°, 180°, 270°, 360°, etc.
            const degreeGridMarks = [-360, -270, -180, -90, 0, 90, 180, 270, 360];
            degreeGridMarks.forEach(degree => {
                if (degree >= graphData.x_range[0] && degree <= graphData.x_range[1]) {
                    const x = (degree - graphData.x_range[0]) * xScale;
                    ctx.beginPath();
                    ctx.moveTo(x, 0);
                    ctx.lineTo(x, height);
                    ctx.stroke();
                }
            });
        } else {
            // Radians: grid lines at π/2, π, 3π/2, 2π, etc.
            const radianGridMarks = [
                -4 * Math.PI, -3 * Math.PI, -2 * Math.PI, -Math.PI, 
                -Math.PI / 2, 0, Math.PI / 2, Math.PI, 
                2 * Math.PI, 3 * Math.PI, 4 * Math.PI
            ];
            
            radianGridMarks.forEach(radian => {
                if (radian >= graphData.x_range[0] && radian <= graphData.x_range[1]) {
                    const x = (radian - graphData.x_range[0]) * xScale;
                    ctx.beginPath();
                    ctx.moveTo(x, 0);
                    ctx.lineTo(x, height);
                    ctx.stroke();
                }
            });
        }

        // Horizontal grid lines at integer Y values
        for (let y = Math.ceil(graphData.y_range[0]); y <= Math.floor(graphData.y_range[1]); y++) {
            if (y !== 0) { // Skip 0 as it's the x-axis
                const canvasY = height - (y - graphData.y_range[0]) * yScale;
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }
    };

    const drawAxes = (ctx, width, height, xScale, yScale) => {
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;

        // X-axis
        const yAxis = height - (0 - graphData.y_range[0]) * yScale;
        ctx.beginPath();
        ctx.moveTo(0, yAxis);
        ctx.lineTo(width, yAxis);
        ctx.stroke();

        // Y-axis
        const xAxis = (0 - graphData.x_range[0]) * xScale;
        ctx.beginPath();
        ctx.moveTo(xAxis, 0);
        ctx.lineTo(xAxis, height);
        ctx.stroke();

        // Axis labels
        ctx.fillStyle = '#000000';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        
        // X-axis labels
        if (graphData.angleUnit === 'degrees') {
            // Show degree marks at key angles
            const degreeMarks = [-360, -270, -180, -90, 0, 90, 180, 270, 360];
            degreeMarks.forEach(degree => {
                if (degree >= graphData.x_range[0] && degree <= graphData.x_range[1]) {
                    const x = (degree - graphData.x_range[0]) * xScale;
                    const y = yAxis + 20;
                    const label = degree === 0 ? '0' : `${degree}°`;
                    ctx.fillText(label, x, y);
                }
            });
        } else {
            // Show radian marks at key angles
            const radianMarks = [
                { value: -4 * Math.PI, label: '-4π' },
                { value: -3 * Math.PI, label: '-3π' },
                { value: -2 * Math.PI, label: '-2π' },
                { value: -Math.PI, label: '-π' },
                { value: -Math.PI / 2, label: '-π/2' },
                { value: 0, label: '0' },
                { value: Math.PI / 2, label: 'π/2' },
                { value: Math.PI, label: 'π' },
                { value: 2 * Math.PI, label: '2π' },
                { value: 3 * Math.PI, label: '3π' },
                { value: 4 * Math.PI, label: '4π' }
            ];
            
            radianMarks.forEach(mark => {
                if (mark.value >= graphData.x_range[0] && mark.value <= graphData.x_range[1]) {
                    const x = (mark.value - graphData.x_range[0]) * xScale;
                    const y = yAxis + 20;
                    ctx.fillText(mark.label, x, y);
                }
            });
        }

        // Y-axis labels
        for (let i = Math.ceil(graphData.y_range[0]); i <= graphData.y_range[1]; i++) {
            if (i !== 0) {
                const x = xAxis - 10;
                const y = height - (i - graphData.y_range[0]) * yScale + 4;
                ctx.fillText(i.toString(), x, y);
            }
        }
    };

    const drawAsymptotes = (ctx, asymptotes, xScale, yScale, width, height) => {
        ctx.strokeStyle = '#ff0000';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);

        asymptotes.forEach(x => {
            const canvasX = (x - graphData.x_range[0]) * xScale;
            if (canvasX >= 0 && canvasX <= width) {
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }
        });

        ctx.setLineDash([]);
    };

    const drawFunction = (ctx, width, height, xScale, yScale) => {
        ctx.strokeStyle = graphData.lineColor;
        ctx.lineWidth = 2;
        ctx.beginPath();

        let firstPoint = true;
        // Use much finer sampling for smooth curves - improved resolution
        const step = (graphData.x_range[1] - graphData.x_range[0]) / (width * graphData.samplingDensity);

        // For reciprocal functions, we need to be more careful about sampling
        const isReciprocal = ['csc', 'sec', 'cot'].includes(graphData.funcType);
        
        for (let x = graphData.x_range[0]; x <= graphData.x_range[1]; x += step) {
            const y = calculateTrigValue(x, graphData.funcType, graphData.a, graphData.b, graphData.c, graphData.d);
            
            // Handle reciprocal functions more carefully
            if (isReciprocal) {
                if (y !== null && isFinite(y)) {
                    // For reciprocal functions, allow values outside the current Y range
                    // but cap them to prevent extreme rendering issues
                    let clampedY = y;
                    if (Math.abs(y) > 100) {
                        clampedY = y > 0 ? 100 : -100;
                    }
                    
                    const canvasX = (x - graphData.x_range[0]) * xScale;
                    const canvasY = height - (clampedY - graphData.y_range[0]) * yScale;
                    
                    // Ensure the point is within canvas bounds
                    if (canvasY >= -50 && canvasY <= height + 50) {
                        if (firstPoint) {
                            ctx.moveTo(canvasX, canvasY);
                            firstPoint = false;
                        } else {
                            ctx.lineTo(canvasX, canvasY);
                        }
                    } else {
                        firstPoint = true; // Start new line segment
                    }
                } else {
                    firstPoint = true; // Start new line segment at asymptotes
                }
            } else {
                // Standard functions (sin, cos, tan)
                if (y !== null && isFinite(y) && y >= graphData.y_range[0] && y <= graphData.y_range[1]) {
                    const canvasX = (x - graphData.x_range[0]) * xScale;
                    const canvasY = height - (y - graphData.y_range[0]) * yScale;
                    
                    if (firstPoint) {
                        ctx.moveTo(canvasX, canvasY);
                        firstPoint = false;
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                } else {
                    firstPoint = true; // Start new line segment
                }
            }
        }

        ctx.stroke();
    };

    const drawDerivativeFunction = (ctx, width, height, xScale, yScale) => {
        ctx.strokeStyle = graphData.derivativeColor;
        ctx.lineWidth = 1.5;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();

        let firstPoint = true;
        const step = (graphData.x_range[1] - graphData.x_range[0]) / (width * graphData.samplingDensity);

        // For reciprocal functions, we need to be more careful about sampling
        const isReciprocal = ['csc', 'sec', 'cot'].includes(graphData.funcType);

        for (let x = graphData.x_range[0]; x <= graphData.x_range[1]; x += step) {
            const y = calculateDerivativeValue(x, graphData.funcType, graphData.a, graphData.b, graphData.c);
            
            // Handle reciprocal functions more carefully
            if (isReciprocal) {
                if (y !== null && isFinite(y)) {
                    // For reciprocal functions, allow values outside the current Y range
                    // but cap them to prevent extreme rendering issues
                    let clampedY = y;
                    if (Math.abs(y) > 100) {
                        clampedY = y > 0 ? 100 : -100;
                    }
                    
                    const canvasX = (x - graphData.x_range[0]) * xScale;
                    const canvasY = height - (clampedY - graphData.y_range[0]) * yScale;
                    
                    // Ensure the point is within canvas bounds
                    if (canvasY >= -50 && canvasY <= height + 50) {
                        if (firstPoint) {
                            ctx.moveTo(canvasX, canvasY);
                            firstPoint = false;
                        } else {
                            ctx.lineTo(canvasX, canvasY);
                        }
                    } else {
                        firstPoint = true; // Start new line segment
                    }
                } else {
                    firstPoint = true; // Start new line segment at asymptotes
                }
            } else {
                // Standard functions (sin, cos, tan)
                if (y !== null && isFinite(y) && y >= graphData.y_range[0] && y <= graphData.y_range[1]) {
                    const canvasX = (x - graphData.x_range[0]) * xScale;
                    const canvasY = height - (y - graphData.y_range[0]) * yScale;
                    
                    if (firstPoint) {
                        ctx.moveTo(canvasX, canvasY);
                        firstPoint = false;
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                } else {
                    firstPoint = true; // Start new line segment
                }
            }
        }

        ctx.stroke();
        ctx.setLineDash([]);
    };

    const drawSpecialFeatures = (ctx, width, height, xScale, yScale) => {
        const props = calculateProperties();
        
        if (graphData.showPeriod && props.period > 0) {
            drawPeriodMarkers(ctx, width, height, xScale, yScale, props);
        }
        
        if (graphData.showAmplitude && props.amplitude > 0) {
            drawAmplitudeLines(ctx, width, height, xScale, yScale, props);
        }
        
        if (graphData.showPhaseShift) {
            drawPhaseShiftMarker(ctx, width, height, xScale, yScale, props);
        }
    };

    const drawPeriodMarkers = (ctx, width, height, xScale, yScale, props) => {
        ctx.strokeStyle = '#00ff00';
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);

        const { period, phaseShift } = props;
        let x = phaseShift;
        
        while (x <= graphData.x_range[1]) {
            if (x >= graphData.x_range[0]) {
                const canvasX = (x - graphData.x_range[0]) * xScale;
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }
            x += period;
        }

        ctx.setLineDash([]);
    };

    const drawAmplitudeLines = (ctx, width, height, xScale, yScale, props) => {
        ctx.strokeStyle = '#ff00ff';
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);

        const { amplitude, verticalShift } = props;
        const upperLine = verticalShift + amplitude;
        const lowerLine = verticalShift - amplitude;

        if (upperLine >= graphData.y_range[0] && upperLine <= graphData.y_range[1]) {
            const canvasY = height - (upperLine - graphData.y_range[0]) * yScale;
            ctx.beginPath();
            ctx.moveTo(0, canvasY);
            ctx.lineTo(width, canvasY);
            ctx.stroke();
        }

        if (lowerLine >= graphData.y_range[0] && lowerLine <= graphData.y_range[1]) {
            const canvasY = height - (lowerLine - graphData.y_range[0]) * yScale;
            ctx.beginPath();
            ctx.moveTo(0, canvasY);
            ctx.lineTo(width, canvasY);
            ctx.stroke();
        }

        ctx.setLineDash([]);
    };

    const drawPhaseShiftMarker = (ctx, width, height, xScale, yScale, props) => {
        const { phaseShift, verticalShift } = props;
        
        if (phaseShift >= graphData.x_range[0] && phaseShift <= graphData.x_range[1]) {
            const canvasX = (phaseShift - graphData.x_range[0]) * xScale;
            const canvasY = height - (verticalShift - graphData.y_range[0]) * yScale;
            
            ctx.fillStyle = '#ff8800';
            ctx.beginPath();
            ctx.arc(canvasX, canvasY, 4, 0, 2 * Math.PI);
            ctx.fill();
        }
    };

    const handleFullScreen = () => {
        setIsFullScreenOpen(true);
        setIsFullScreen(true);
    };

    const handleCloseFullScreen = () => {
        setIsFullScreenOpen(false);
        setIsFullScreen(false);
    };

    const handleToggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    // Parameter Panel for Fullscreen Modal
    const ParameterPanel = () => (
        <div className="p-4 space-y-4">
            <h3 className="text-lg font-semibold text-gray-800">Trigonometric Function Parameters</h3>
            
            {/* Function Type */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Function Type</label>
                <select
                    value={graphData.funcType}
                    onChange={(e) => {
                        const newFuncType = e.target.value;
                        setFunctionRanges(prev => ({
                            ...prev,
                            [graphData.funcType]: { x: graphData.x_range, y: graphData.y_range }
                        }));
                        const storedRanges = functionRanges[newFuncType];
                        const { xRange, yRange } = getDefaultRanges(newFuncType, graphData.angleUnit);
                        setGraphData(prev => ({
                            ...prev,
                            funcType: newFuncType,
                            x_range: storedRanges ? storedRanges.x : xRange,
                            y_range: storedRanges ? storedRanges.y : yRange,
                            equation: generateEquation(newFuncType, prev.a, prev.b, prev.c, prev.d)
                        }));
                        if (onChange) {
                            onChange({ ...graphData, funcType: newFuncType, x_range: storedRanges ? storedRanges.x : xRange, y_range: storedRanges ? storedRanges.y : yRange, equation: generateEquation(newFuncType, graphData.a, graphData.b, graphData.c, graphData.d) });
                        }
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                    <option value="sin">Sine (sin)</option>
                    <option value="cos">Cosine (cos)</option>
                    <option value="tan">Tangent (tan)</option>
                    <option value="csc">Cosecant (csc)</option>
                    <option value="sec">Secant (sec)</option>
                    <option value="cot">Cotangent (cot)</option>
                </select>
            </div>

            {/* Amplitude */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Amplitude (a)</label>
                <input
                    type="number"
                    step="0.1"
                    value={graphData.a}
                    onChange={(e) => {
                        const newA = parseFloat(e.target.value) || 1;
                        setGraphData(prev => ({
                            ...prev,
                            a: newA,
                            equation: generateEquation(prev.funcType, newA, prev.b, prev.c, prev.d)
                        }));
                        if (onChange) onChange({ ...graphData, a: newA, equation: generateEquation(graphData.funcType, newA, graphData.b, graphData.c, graphData.d) });
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>

            {/* Frequency */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Frequency (b)</label>
                <input
                    type="number"
                    step="0.1"
                    value={graphData.b}
                    onChange={(e) => {
                        const newB = parseFloat(e.target.value) || 1;
                        setGraphData(prev => ({
                            ...prev,
                            b: newB,
                            equation: generateEquation(prev.funcType, prev.a, newB, prev.c, prev.d)
                        }));
                        if (onChange) onChange({ ...graphData, b: newB, equation: generateEquation(graphData.funcType, graphData.a, newB, graphData.c, graphData.d) });
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>

            {/* Phase Shift */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Phase Shift (c)</label>
                <input
                    type="number"
                    step="0.1"
                    value={graphData.c}
                    onChange={(e) => {
                        const newC = parseFloat(e.target.value) || 0;
                        setGraphData(prev => ({
                            ...prev,
                            c: newC,
                            equation: generateEquation(prev.funcType, prev.a, prev.b, newC, prev.d)
                        }));
                        if (onChange) onChange({ ...graphData, c: newC, equation: generateEquation(graphData.funcType, graphData.a, graphData.b, newC, graphData.d) });
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>

            {/* Vertical Shift */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Vertical Shift (d)</label>
                <input
                    type="number"
                    step="0.1"
                    value={graphData.d}
                    onChange={(e) => {
                        const newD = parseFloat(e.target.value) || 0;
                        setGraphData(prev => ({
                            ...prev,
                            d: newD,
                            equation: generateEquation(prev.funcType, prev.a, prev.b, prev.c, newD)
                        }));
                        if (onChange) onChange({ ...graphData, d: newD, equation: generateEquation(graphData.funcType, graphData.a, graphData.b, graphData.c, newD) });
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>

            {/* Angle Unit */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Angle Unit</label>
                <select
                    value={graphData.angleUnit}
                    onChange={(e) => {
                        const newAngleUnit = e.target.value;
                        const { xRange, yRange } = getDefaultRanges(graphData.funcType, newAngleUnit);
                        setGraphData(prev => ({
                            ...prev,
                            angleUnit: newAngleUnit,
                            x_range: xRange,
                            y_range: yRange
                        }));
                        if (onChange) onChange({ ...graphData, angleUnit: newAngleUnit, x_range: xRange, y_range: yRange });
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                    <option value="degrees">Degrees</option>
                    <option value="radians">Radians</option>
                </select>
            </div>

            {/* Line Color */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Line Color</label>
                <input
                    type="color"
                    value={graphData.lineColor}
                    onChange={(e) => {
                        setGraphData(prev => ({ ...prev, lineColor: e.target.value }));
                        if (onChange) onChange({ ...graphData, lineColor: e.target.value });
                    }}
                    className="w-full h-10 border border-gray-300 rounded-md"
                />
            </div>

            {/* Display Options */}
            <div className="space-y-2">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={graphData.showGrid}
                        onChange={(e) => {
                            setGraphData(prev => ({ ...prev, showGrid: e.target.checked }));
                            if (onChange) onChange({ ...graphData, showGrid: e.target.checked });
                        }}
                        className="mr-2"
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={graphData.showAsymptotes}
                        onChange={(e) => {
                            setGraphData(prev => ({ ...prev, showAsymptotes: e.target.checked }));
                            if (onChange) onChange({ ...graphData, showAsymptotes: e.target.checked });
                        }}
                        className="mr-2"
                    />
                    <span className="text-sm text-gray-700">Show Asymptotes</span>
                </label>

            </div>
        </div>
    );

    const resetToDefaults = () => {
        setGraphData(prev => ({
            ...prev,
            a: 1,
            b: 1,
            c: 0,
            d: 0,
            equation: generateEquation(prev.funcType, 1, 1, 0, 0)
        }));
    };

    // Set canvas dimensions for HiDPI
    const setCanvasDimensions = (canvas) => {
        const rect = canvas.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        canvas.width = rect.width * dpr;
        canvas.height = rect.height * dpr;
        canvas.style.width = rect.width + 'px';
        canvas.style.height = rect.height + 'px';
        const ctx = canvas.getContext('2d');
        ctx.scale(dpr, dpr);
    };

    useEffect(() => {
        if (canvasRef.current) {
            setCanvasDimensions(canvasRef.current);
        }
    }, []);

    return (
        <div className="w-full">
            <div className="flex justify-between items-center mb-2">
                <h4 className="text-sm font-medium text-gray-700">
                    {graphData.title}: {graphData.equation}
                </h4>
                <div className="flex items-center space-x-2">
                    <button
                        onClick={resetToDefaults}
                        className="p-1 text-gray-500 hover:text-gray-700 transition-colors"
                        title="Reset to defaults"
                    >
                        <RotateCcw size={16} />
                    </button>
                    <button
                        onClick={handleFullScreen}
                        className="p-1 text-gray-500 hover:text-gray-700 transition-colors"
                        title="Open full screen"
                    >
                        <Maximize2 size={16} />
                    </button>
                </div>
            </div>
            
            {/* Function Controls */}
            <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 mb-4">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-4">
                    {/* Function Type */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Function Type
                        </label>
                        <select
                            value={graphData.funcType}
                            onChange={(e) => {
                                const newFuncType = e.target.value;
                                
                                // Save current ranges for the current function type
                                setFunctionRanges(prev => ({
                                    ...prev,
                                    [graphData.funcType]: {
                                        x: graphData.x_range,
                                        y: graphData.y_range
                                    }
                                }));
                                
                                // Get the stored ranges for the new function type, or use defaults
                                const storedRanges = functionRanges[newFuncType];
                                const { xRange, yRange } = getDefaultRanges(newFuncType, graphData.angleUnit);
                                
                                setGraphData(prev => ({
                                    ...prev,
                                    funcType: newFuncType,
                                    x_range: storedRanges ? storedRanges.x : xRange,
                                    y_range: storedRanges ? storedRanges.y : yRange,
                                    equation: generateEquation(newFuncType, prev.a, prev.b, prev.c, prev.d)
                                }));

                                // Notify parent component of the function type change
                                if (onChange) {
                                    onChange({
                                        ...graphData,
                                        funcType: newFuncType,
                                        x_range: storedRanges ? storedRanges.x : xRange,
                                        y_range: storedRanges ? storedRanges.y : yRange,
                                        equation: generateEquation(newFuncType, graphData.a, graphData.b, graphData.c, graphData.d)
                                    });
                                }
                            }}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                        >
                            <option value="sin">sin(x)</option>
                            <option value="cos">cos(x)</option>
                            <option value="tan">tan(x)</option>
                            <option value="csc">csc(x)</option>
                            <option value="sec">sec(x)</option>
                            <option value="cot">cot(x)</option>
                        </select>
                    </div>

                    {/* Amplitude (a) */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Amplitude (a)
                        </label>
                        <input
                            type="number"
                            value={graphData.a}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                a: Number(e.target.value),
                                equation: generateEquation(prev.funcType, Number(e.target.value), prev.b, prev.c, prev.d)
                            }))}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                        />
                    </div>

                    {/* Frequency (b) */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Frequency (b)
                        </label>
                        <input
                            type="number"
                            value={graphData.b}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                b: Number(e.target.value),
                                equation: generateEquation(prev.funcType, prev.a, Number(e.target.value), prev.c, prev.d)
                            }))}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                        />
                    </div>

                    {/* Phase Shift (c) */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Phase Shift (c)
                        </label>
                        <input
                            type="number"
                            value={graphData.c}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                c: Number(e.target.value),
                                equation: generateEquation(prev.funcType, prev.a, prev.b, Number(e.target.value), prev.d)
                            }))}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                        />
                    </div>

                    {/* Vertical Shift (d) */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Vertical Shift (d)
                        </label>
                        <input
                            type="number"
                            value={graphData.d}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                d: Number(e.target.value),
                                equation: generateEquation(prev.funcType, prev.a, prev.b, prev.c, Number(e.target.value))
                            }))}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                        />
                    </div>

                    {/* Angle Unit */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Angle Unit
                        </label>
                        <select
                            value={graphData.angleUnit}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                angleUnit: e.target.value
                            }))}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                        >
                            <option value="radians">Radians</option>
                            <option value="degrees">Degrees</option>
                        </select>
                    </div>
                </div>

                {/* Range Controls */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                    {/* X Range */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            X Range
                        </label>
                        <div className="flex space-x-2">
                            <input
                                type="number"
                                value={graphData.x_range[0]}
                                onChange={(e) => {
                                    const newXMin = Number(e.target.value);
                                    setGraphData(prev => ({
                                        ...prev,
                                        x_range: [newXMin, prev.x_range[1]]
                                    }));
                                    // Save the updated range for current function type
                                    setFunctionRanges(prev => ({
                                        ...prev,
                                        [graphData.funcType]: {
                                            ...prev[graphData.funcType],
                                            x: [newXMin, graphData.x_range[1]]
                                        }
                                    }));
                                }}
                                step="0.1"
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                                placeholder="Min"
                            />
                            <input
                                type="number"
                                value={graphData.x_range[1]}
                                onChange={(e) => {
                                    const newXMax = Number(e.target.value);
                                    setGraphData(prev => ({
                                        ...prev,
                                        x_range: [prev.x_range[0], newXMax]
                                    }));
                                    // Save the updated range for current function type
                                    setFunctionRanges(prev => ({
                                        ...prev,
                                        [graphData.funcType]: {
                                            ...prev[graphData.funcType],
                                            x: [graphData.x_range[0], newXMax]
                                        }
                                    }));
                                }}
                                step="0.1"
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                                placeholder="Max"
                            />
                        </div>
                    </div>

                    {/* Y Range */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Y Range
                        </label>
                        <div className="flex space-x-2">
                            <input
                                type="number"
                                value={graphData.y_range[0]}
                                onChange={(e) => {
                                    const newYMin = Number(e.target.value);
                                    setGraphData(prev => ({
                                        ...prev,
                                        y_range: [newYMin, prev.y_range[1]]
                                    }));
                                    // Save the updated range for current function type
                                    setFunctionRanges(prev => ({
                                        ...prev,
                                        [graphData.funcType]: {
                                            ...prev[graphData.funcType],
                                            y: [newYMin, graphData.y_range[1]]
                                        }
                                    }));
                                }}
                                step="0.1"
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                                placeholder="Min"
                            />
                            <input
                                type="number"
                                value={graphData.y_range[1]}
                                onChange={(e) => {
                                    const newYMax = Number(e.target.value);
                                    setGraphData(prev => ({
                                        ...prev,
                                        y_range: [prev.y_range[0], newYMax]
                                    }));
                                    // Save the updated range for current function type
                                    setFunctionRanges(prev => ({
                                        ...prev,
                                        [graphData.funcType]: {
                                            ...prev[graphData.funcType],
                                            y: [graphData.y_range[0], newYMax]
                                        }
                                    }));
                                }}
                                step="0.1"
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                                placeholder="Max"
                            />
                        </div>
                    </div>
                </div>

                {/* Advanced Controls */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
                    {/* Sampling Density */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Sampling Density: {graphData.samplingDensity}x
                        </label>
                        <input
                            type="range"
                            min="8"
                            max="32"
                            value={graphData.samplingDensity}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                samplingDensity: Number(e.target.value)
                            }))}
                            className="w-full"
                        />
                        <p className="text-xs text-gray-500">Higher = smoother curves</p>
                    </div>

                    {/* Solution Tools Toggle */}
                    <div>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={graphData.showSolutionTools}
                                onChange={(e) => setGraphData(prev => ({
                                    ...prev,
                                    showSolutionTools: e.target.checked
                                }))}
                                className="mr-2"
                            />
                            <span className="text-sm font-medium text-gray-700">Show Solution Tools</span>
                        </label>
                    </div>

                    {/* Unit Circle Toggle */}
                    <div>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={graphData.showUnitCircle}
                                onChange={(e) => setGraphData(prev => ({
                                    ...prev,
                                    showUnitCircle: e.target.checked
                                }))}
                                className="mr-2"
                            />
                            <span className="text-sm font-medium text-gray-700">Show Unit Circle</span>
                        </label>
                    </div>


                </div>

                {/* Display Properties */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={graphData.showGrid}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                showGrid: e.target.checked
                            }))}
                            className="mr-2"
                        />
                        <span className="text-sm text-gray-700">Show Grid</span>
                    </label>
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={graphData.showPoints}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                showPoints: e.target.checked
                            }))}
                            className="mr-2"
                        />
                        <span className="text-sm text-gray-700">Show Points</span>
                    </label>
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={graphData.showAsymptotes}
                            onChange={(e) => setGraphData(prev => ({
                                ...prev,
                                showAsymptotes: e.target.checked
                            }))}
                            className="mr-2"
                        />
                        <span className="text-sm text-gray-700">Show Asymptotes</span>
                    </label>
                    <label className="flex items-center">
                        <input className="mr-2" type="checkbox" checked={graphData.showPeriod} onChange={(e) => setGraphData(prev => ({ ...prev, showPeriod: e.target.checked }))} />
                        <span className="text-sm text-gray-700">Show Period</span>
                    </label>
                </div>


            </div>
            
            <div className="border border-gray-200 rounded bg-white">
                <canvas
                    ref={canvasRef}
                    className="w-full h-[calc(100vh-10rem)] cursor-crosshair"
                    style={{ touchAction: 'none' }}
                />
            </div>

            {/* Unit Circle Reference */}
            {graphData.showUnitCircle && (
                <div className="mt-4">
                    <UnitCircle 
                        isCompact={true}
                        currentAngle={graphData.unitCircleAngle}
                        onChange={(data) => {
                            setGraphData(prev => ({
                                ...prev,
                                unitCircleAngle: data.angle
                            }));
                        }}
                    />
                </div>
            )}

            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title={graphData.title}
                onToggleFullScreen={handleToggleFullScreen}
                isFullScreen={isFullScreen}
                hideFullScreenToggle={true}
                parameterPanel={<ParameterPanel />}
            >
                <div className="h-full flex flex-col items-center justify-center">
                    <div className="border-2 border-gray-300 rounded-lg overflow-hidden mb-4">
                        <canvas
                            ref={fullScreenCanvasRef}
                            className="w-full h-auto"
                            style={{ touchAction: 'none' }}
                        />
                    </div>
                    
                    {/* Unit Circle in Full Screen */}
                    {graphData.showUnitCircle && (
                        <div className="w-full max-w-md">
                            <UnitCircle 
                                isCompact={true}
                                currentAngle={graphData.unitCircleAngle}
                                onChange={(data) => {
                                    setGraphData(prev => ({
                                        ...prev,
                                        unitCircleAngle: data.angle
                                    }));
                                }}
                            />
                        </div>
                    )}
                </div>
            </FullScreenModal>
        </div>
    );
};

export default TrigonometricFunctionGraph;
