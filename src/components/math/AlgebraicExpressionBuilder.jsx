import React, { useState, useEffect, useRef } from 'react';
import { Plus, Minus, RotateCcw, Maximize2, Grid3X3, TrendingUp, BarChart3, FunctionSquare, Bot, Send } from 'lucide-react';
import { evaluate, parse, simplify, derivative } from 'mathjs';
import LinearFunctionGraph from './LinearFunctionGraph';
import QuadraticGraphInput from './QuadraticGraphInput';
import IntegratedExponentialLogarithmicFunction from './IntegratedExponentialLogarithmicFunction';
import CubicFunctionGraph from './CubicFunctionGraph';
import TrigonometricFunctionGraph from './TrigonometricFunctionGraph';
import UnitCircle from './UnitCircle';
import HyperbolicFunctionInput from './HyperbolicFunctionInput';
import AiMathAssistant from '../AiMathAssistant';
import StepCanvas from '../StepCanvas';
import EnhancedMathKeypad from '../EnhancedMathKeypad';
import * as math from 'mathjs';
import { 
    parseTrigonometricFunction,
    parsePolynomialFunction,
    parseLinearFunction,
    getPolynomialDegree,
    analyzeExpressionType
} from '../../utils/functionParsers';
import {
    parseExpression,
    evaluateExpression,
    simplifyExpression,
    factorExpression,
    expandExpression,
    solveEquation,
    completeSquare,
    performLongDivision,
    analyzeQuadratic,
    solveTrigonometricEquation,
    applyTrigonometricIdentities
} from '../../utils/mathOperations';
import {
    generateComprehensiveSteps,
    generateSimplifySteps,
    generateFactorSteps,
    generateExpandSteps,
    generateSolveSteps,
    generateCompleteSquareSteps,
    generateLongDivisionSteps,
    generateCubicSolveSteps,
    generateSimultaneousSteps,
    generateInequalitySteps,
    generateQuadraticAnalysisSteps
} from '../../utils/stepGenerators';

const AlgebraicExpressionBuilder = ({ initialData, onChange, isSubmitted, aiInput = null, currentUser }) => {
    const isPro = currentUser?.tier === 'pro' || currentUser?.isOwner || currentUser?.isSuperAdmin;
    const [exprData, setExprData] = useState(() => {
        const defaultData = {
            title: "Enhanced Algebraic Expression Builder",
            expression: "2^x",
            functionType: 'integrated_exponential_logarithmic', // 'linear', 'quadratic', 'cubic', 'integrated_exponential_logarithmic', 'trigonometric', 'hyperbolic'
            targetOperation: 'simplify', // 'solve', 'simplify', 'factorize', 'expand', 'complete_square', 'long_division'
            variable: 'x',
            showSteps: true,
            showGraph: true,
            xMin: -10,
            xMax: 10,
            yMin: -10,
            yMax: 10,
            steps: [],
            result: null,
            error: null,
            // AI Integration
            aiMode: false,
            aiInstructions: "",
            stepCanvas: [],
            currentStep: 0,
            // Expression Analysis
            expressionType: 'integrated_exponential_logarithmic',
            functionData: { a: 1, b: 2, c: 0, d: 0, functionType: 'exponential' },
            // Trigonometric settings
            angleUnit: 'degrees', // 'degrees' or 'radians'
    

            // Display options for imported components
            showGrid: true,
            showSpecialPoints: true,
            // Step-by-Step Enhancement
            detailedSteps: true,
            showIntermediateCalculations: true,
            stepExplanations: true,
            visualStepRepresentation: true,
            // View mode: 'graph' | 'solution'
            viewMode: 'solution',
                            // Trigonometric identity verification
                identityInput: '',
                identityResult: null,
                // Proof visibility toggles
                showPythagoreanProof: false,
                showTanSecProof: false,
                showCotCscProof: false,
                showSin2Proof: false,
                showCos2Proof: false,
                showTan2Proof: false,
                showSinSumProof: false,
                showCosSumProof: false,
                showTanSumProof: false,
                showCscProof: false,
                showSecProof: false,
                showCotProof: false,
                // Navigation state for trigonometric sections
                trigViewMode: 'unitCircle', // 'unitCircle', 'reductionFormulae', 'identities'
                // Navigation state for hyperbolic sections
                hyperbolicViewMode: 'properties', // 'properties', 'asymptotes', 'transformations', 'solver'
                // Hyperbolic proof visibility toggles
                showReciprocalProof: false,
                showAsymptoteProof: false,
                showTransformationProof: false,
                showSolverProof: false
        };
        
        // Merge with initialData, ensuring all properties exist
        if (initialData) {
            return { ...defaultData, ...initialData };
        }
        
        return defaultData;
    });

    // AI Input Processing
    const [aiInputText, setAiInputText] = useState("");

    // Dynamic expression state for real-time updates
    const [dynamicExpression, setDynamicExpression] = useState("");
    const [debouncedExpression, setDebouncedExpression] = useState("");
    const debounceTimeoutRef = useRef(null);
    
    // Track whether function type was manually selected or auto-detected
    const [isFunctionTypeManual, setIsFunctionTypeManual] = useState(false);

    // Effect to analyze expression type on component mount
    useEffect(() => {
        if (exprData.expression) {
            const analysis = analyzeExpressionType(exprData.expression);
            if (analysis.type !== exprData.expressionType || !exprData.functionData) {
                setExprData(prev => ({
                    ...prev,
                    expressionType: analysis.type,
                    functionData: analysis.functionData
                }));
            }
        }
    }, []); // Only run on mount

    // Effect to update dynamic expression when function data or expression changes
    useEffect(() => {
        if (exprData.functionData && exprData.expressionType) {
            const newExpression = getCurrentFunctionExpression();
            console.log('Updating dynamic expression:', newExpression);
            setDynamicExpression(newExpression);
        }
    }, [exprData.functionData, exprData.expressionType, exprData.showGraph, exprData.expression]);

    // Debounced effect for expression updates to prevent too many rapid changes
    useEffect(() => {
        if (debounceTimeoutRef.current) {
            clearTimeout(debounceTimeoutRef.current);
        }
        
        debounceTimeoutRef.current = setTimeout(() => {
            setDebouncedExpression(dynamicExpression);
        }, 500); // 500ms delay
        
        return () => {
            if (debounceTimeoutRef.current) {
                clearTimeout(debounceTimeoutRef.current);
            }
        };
    }, [dynamicExpression]);

    const [isProcessingAi, setIsProcessingAi] = useState(false);

    // Function type defaults
    const getDefaultEquation = (functionType) => {
        switch (functionType) {
            case 'linear':
                return { expression: "2x + 3", variable: 'x', xMin: -10, xMax: 10, yMin: -10, yMax: 10 };
            case 'quadratic':
                return { expression: "x²", variable: 'x', xMin: -10, xMax: 10, yMin: -5, yMax: 15 };
            case 'cubic':
                return { expression: "x³-2x²-3x+1", variable: 'x', xMin: -5, xMax: 5, yMin: -10, yMax: 10 };
            case 'integrated_exponential_logarithmic':
                return { expression: "2^x", variable: 'x', xMin: -7, xMax: 7, yMin: 0, yMax: 50, functionType: 'integrated_exponential_logarithmic' };
            case 'trigonometric':
                return { expression: "sin(θ)", variable: 'θ', xMin: -360, xMax: 360, yMin: -3, yMax: 3 };
            case 'hyperbolic':
                return { expression: "1/x", variable: 'x', xMin: -10, xMax: 10, yMin: -5, yMax: 5 };
            default:
                return { expression: "2x + 3", variable: 'x', xMin: -10, xMax: 10, yMin: -10, yMax: 10 };
        }
    };

    const handleFunctionTypeChange = (newFunctionType) => {
        const defaults = getDefaultEquation(newFunctionType);
        const analysis = analyzeExpressionType(defaults.expression);
        
        // Mark this as a manual selection
        setIsFunctionTypeManual(true);
        
        setExprData(prev => ({
            ...prev,
            functionType: newFunctionType,
            expression: defaults.expression,
            variable: defaults.variable,
            xMin: defaults.xMin,
            xMax: defaults.xMax,
            yMin: defaults.yMin,
            yMax: defaults.yMax,
            expressionType: analysis.type,
            functionData: analysis.functionData,
            showGraph: true,
            viewMode: 'graph'
        }));
        
        // Update dynamic expression for real-time synchronization
        setDynamicExpression(defaults.expression);
        
        // Auto-update operation if current operation is not suitable for new function type
        const suggestedOperation = getSuggestedOperation(analysis.type);
        if (suggestedOperation && suggestedOperation !== exprData.targetOperation) {
            setExprData(prev => ({ ...prev, targetOperation: suggestedOperation }));
            console.log('Auto-updated operation to:', suggestedOperation, 'for function type:', analysis.type);
        }
        
        console.log('Function type manually changed:', {
            newType: newFunctionType,
            newExpression: defaults.expression,
            detectedType: analysis.type,
            functionData: analysis.functionData,
            isManual: true,
            autoUpdatedOperation: suggestedOperation
        });
    };



    // Keypad integration
    const [isKeypadVisible, setIsKeypadVisible] = useState(false);
    const expressionInputRef = useRef(null);

    // Enhanced validation for mathematical expressions
    const validateExpression = (expression) => {
        if (!expression || expression.trim() === '') return false;
        
        // Basic validation - check for common invalid patterns
        const invalidPatterns = [
            /[^x0-9+\-*/().,²³ˣ₍ₓ₎×\s]/g, // Only allow valid mathematical characters
            /\+\s*\+/, // No consecutive plus signs
            /\-\s*\-/, // No consecutive minus signs
            /\*\s*\*/, // No consecutive multiplication signs
            /\/\s*\//, // No consecutive division signs
            /\(\s*\)/, // Empty parentheses
            /[+\-]\s*[+\-]/, // Consecutive operators
        ];
        
        for (const pattern of invalidPatterns) {
            if (pattern.test(expression)) return false;
        }
        
        // Check for balanced parentheses
        let parenCount = 0;
        for (let char of expression) {
            if (char === '(') parenCount++;
            if (char === ')') parenCount--;
            if (parenCount < 0) return false; // More closing than opening
        }
        if (parenCount !== 0) return false; // Unbalanced parentheses
        
        return true;
    };

    // Real-time expression validation with detailed feedback
    const getExpressionValidationStatus = (expression) => {
        if (!expression || expression.trim() === '') {
            return { isValid: false, message: 'Expression cannot be empty' };
        }
        
        if (!validateExpression(expression)) {
            return { isValid: false, message: 'Invalid mathematical expression' };
        }
        
        // Try to analyze the expression to see if it's parseable
        try {
            const analysis = analyzeExpressionType(expression);
            if (analysis.type === 'other') {
                return { isValid: false, message: 'Expression not recognized as a valid function' };
        }
            return { isValid: true, message: `Valid ${analysis.type} function` };
        } catch (error) {
            return { isValid: false, message: 'Expression could not be parsed' };
        }
    };
    
    // Validate that an expression is suitable for a specific operation
    const validateOperationForExpression = (expression, operation) => {
        if (!expression || !expression.trim()) {
            return { isValid: false, message: "No expression provided" };
        }
        
        const analysis = analyzeExpressionType(expression);
        
        // Check if expression type is compatible with operation
        switch (operation) {
            case 'solve':
                // All recognized function types can be solved
                if (analysis.type === 'other') {
                    return { isValid: false, message: "Cannot solve unrecognized expression type" };
                }
                break;
                
            case 'simplify':
                // All recognized function types can be simplified
                if (analysis.type === 'other') {
                    return { isValid: false, message: "Cannot simplify unrecognized expression type" };
                }
                break;
                
            case 'factorize':
                // Only polynomial functions can be factorized
                if (!['linear', 'quadratic', 'cubic'].includes(analysis.type)) {
                    return { isValid: false, message: `Factorization not supported for ${analysis.type} functions` };
                }
                break;
                
            case 'expand':
                // Only polynomial functions can be expanded
                if (!['linear', 'quadratic', 'cubic'].includes(analysis.type)) {
                    return { isValid: false, message: `Expansion not supported for ${analysis.type} functions` };
                }
                break;
                
            case 'complete_square':
                // Only quadratic functions can use completing the square
                if (analysis.type !== 'quadratic') {
                    return { isValid: false, message: `Completing the square only works with quadratic functions` };
                }
                break;
                
            case 'long_division':
                // Only polynomial functions can use long division
                if (!['linear', 'quadratic', 'cubic'].includes(analysis.type)) {
                    return { isValid: false, message: `Long division only works with polynomial functions` };
                }
                break;
                
            default:
                return { isValid: false, message: `Unknown operation: ${operation}` };
        }
        
        return { isValid: true, message: `Operation '${operation}' is valid for ${analysis.type} function` };
    };
    
    // Get suggested operation based on function type
    const getSuggestedOperation = (functionType) => {
        switch (functionType) {
            case 'linear':
                return 'solve'; // Linear functions are best solved
            case 'quadratic':
                return 'factorize'; // Quadratic functions are best factorized
            case 'cubic':
                return 'factorize'; // Cubic functions are best factorized
            case 'integrated_exponential_logarithmic':
                return 'solve'; // Exponential and logarithmic functions are best solved
            case 'trigonometric':
                return 'simplify'; // Trigonometric functions are best simplified
            case 'hyperbolic':
                return 'solve'; // Hyperbolic functions are best solved
            default:
                return 'simplify'; // Default to simplify for unknown types
        }
    };
    
    // Get available operations for a given function type
    const getAvailableOperations = (functionType) => {
        switch (functionType) {
            case 'linear':
                return ['solve', 'simplify', 'factorize', 'expand'];
            case 'quadratic':
                return ['solve', 'simplify', 'factorize', 'expand', 'complete_square', 'long_division'];
            case 'cubic':
                return ['solve', 'simplify', 'factorize', 'expand', 'long_division'];
            case 'integrated_exponential_logarithmic':
                return ['solve', 'simplify'];
            case 'trigonometric':
                return ['solve', 'simplify'];
            case 'hyperbolic':
                return ['solve', 'simplify'];
            default:
                return ['solve', 'simplify'];
        }
    };

    // Function to update function parameters from graph changes
    const updateFunctionParameters = (newFunctionData) => {
        if (!newFunctionData) return;
        
        // Update the function data
        setExprData(prev => ({
            ...prev,
            functionData: newFunctionData
        }));
        
        // Generate new expression from updated parameters
        const newExpression = getCurrentFunctionExpression();
        if (newExpression && newExpression !== exprData.expression) {
            setExprData(prev => ({
                ...prev,
                expression: newExpression
            }));
            
            // Update dynamic expression
            setDynamicExpression(newExpression);
            
            console.log('Function parameters updated:', {
                newFunctionData,
                newExpression
            });
        }
    };

    // Function to get current function expression based on active function type and parameters
    const getCurrentFunctionExpression = () => {
        if (!exprData.showGraph || !exprData.functionData) return exprData.expression;
        
        let newExpression = '';
        
        if (exprData.expressionType === 'linear' && exprData.functionData) {
            const { m, c } = exprData.functionData;
            if (m === 1) newExpression = 'x';
            else if (m === -1) newExpression = '-x';
            else newExpression = `${m}x`;
            if (c > 0) newExpression += ` + ${c}`;
            else if (c < 0) newExpression += ` ${c}`;
        } else if (exprData.expressionType === 'quadratic' && exprData.functionData) {
            const { a, b, c } = exprData.functionData;
            if (a === 1) newExpression = 'x²';
            else if (a === -1) newExpression = '-x²';
            else newExpression = `${a}x²`;
            if (b > 0) newExpression += ` + ${b}x`;
            else if (b < 0) newExpression += ` ${b}x`;
            if (c > 0) newExpression += ` + ${c}`;
            else if (c < 0) newExpression += ` ${c}`;
        } else if (exprData.expressionType === 'cubic' && exprData.functionData) {
            const { a, b, c, d } = exprData.functionData;
            if (a === 1) newExpression = 'x³';
            else if (a === -1) newExpression = '-x³';
            else newExpression = `${a}x³`;
            if (b > 0) newExpression += ` + ${b}x²`;
            else if (b < 0) newExpression += ` ${b}x²`;
            if (c > 0) newExpression += ` + ${c}x`;
            else if (c < 0) newExpression += ` ${c}x`;
            if (d > 0) newExpression += ` + ${d}`;
            else if (d < 0) newExpression += ` ${d}`;
        } else if (exprData.expressionType === 'integrated_exponential_logarithmic' && exprData.functionData) {
            if (exprData.functionData.functionType === 'exponential') {
                const { a, b, c = 0, d = 0 } = exprData.functionData;
                // For high school math, default c and d to 0 if not provided
                // Use simplified form when c and d are 0 (which is the default)
                if (c === 0 && d === 0) {
                    if (a === 1) newExpression = `${b}ˣ`;
                    else newExpression = `${a} × ${b}ˣ`;
                } else {
                    // Only show shifts if they're explicitly non-zero
                    newExpression = `${a} × ${b}ˣ`;
                    if (c !== 0) {
                        if (c > 0) newExpression += ` + ${c}`;
                        else newExpression += ` ${c}`;
                    }
                    if (d !== 0) {
                        if (d > 0) newExpression += ` + ${d}`;
                        else newExpression += ` ${d}`;
                    }
                }
            } else {
                const { type, base } = exprData.functionData;
                // Handle different logarithmic types
                if (type === 'natural_log') {
                    newExpression = 'ln(x)';
                } else if (type === 'base_10_log') {
                    newExpression = 'log₁₀(x)';
                } else if (type === 'base_2_log') {
                    newExpression = 'log₂(x)';
                } else if (type === 'custom_base_log') {
                    newExpression = `log${base}₍ₓ₎`;
                } else {
                    newExpression = `log${base}(x)`;
                }
            }
        } else if (exprData.expressionType === 'trigonometric' && exprData.functionData) {
            const { a, b, c, d, type } = exprData.functionData;
            // Use simplified form when c and d are 0
            if (c === 0 && d === 0) {
                if (a === 1) newExpression = `${type}(x)`;
                else newExpression = `${a} × ${type}(x)`;
            } else {
                newExpression = `${a} × ${type}(x`;
                if (c > 0) newExpression += ` + ${c}`;
                else if (c < 0) newExpression += ` ${c}`;
                newExpression += ')';
                if (d > 0) newExpression += ` + ${d}`;
                else if (d < 0) newExpression += ` ${d}`;
            }
        } else if (exprData.expressionType === 'hyperbolic' && exprData.functionData) {
            const { a, b, q, functionForm } = exprData.functionData;
            if (functionForm === 'simple') {
                if (a === 1) newExpression = '1/x';
                else newExpression = `${a}/x`;
                if (b > 0) newExpression += ` + ${b}`;
                else if (b < 0) newExpression += ` ${b}`;
            } else {
                if (a === 1) newExpression = `1/(x${q > 0 ? '+' : ''}${q})`;
                else newExpression = `${a}/(x${q > 0 ? '+' : ''}${q})`;
                if (b > 0) newExpression += ` + ${b}`;
                else if (b < 0) newExpression += ` ${b}`;
            }
        }
        
        console.log('getCurrentFunctionExpression:', {
            expressionType: exprData.expressionType,
            functionData: exprData.functionData,
            result: newExpression || exprData.expression
        });
        
        return newExpression || exprData.expression;
    };

    // Canvas interaction state
    const [isDragging, setIsDragging] = useState(false);
    const [lastMousePos, setLastMousePos] = useState({ x: 0, y: 0 });
    const [isZooming, setIsZooming] = useState(false);



    // Analyze expression type when expression changes
    useEffect(() => {
        if (exprData.expression && exprData.expression.trim()) {
            analyzeExpression(exprData.expression);
        }
    }, [exprData.expression]);

    // Auto-switch to graph view for recognized functions
    useEffect(() => {
        if (exprData.expressionType && exprData.expressionType !== 'other' && exprData.showGraph) {
            setExprData(prev => ({
                ...prev,
                viewMode: 'graph'
            }));
        }
    }, [exprData.expressionType, exprData.showGraph]);

    // Analyze expression to determine type and extract function data
    const analyzeExpression = (expression) => {
        try {
            const { type, functionData } = analyzeExpressionType(expression);
            
            // Update state with analysis results
            setExprData(prev => ({
                ...prev,
                expressionType: type,
                functionType: type, // Also set functionType for drawing functions
                functionData: functionData,
                showGraph: type !== 'other' // Show graph for recognized function types
            }));
            // Mathematical analysis is now handled by imported components
        } catch (error) {
            console.error('Error analyzing expression:', error);
            setExprData(prev => ({
                ...prev,
                expressionType: 'other',
                functionData: null,
                showGraph: false
            }));
        }
    };

    // Convert paragraph text to structured steps with line breaks
    const convertParagraphToSteps = (paragraphText) => {
        if (!paragraphText) return [];
        
        // Split by common step indicators and create structured steps
        const stepIndicators = [
            /step\s*\d+/gi,
            /first/i,
            /second/i,
            /third/i,
            /next/i,
            /then/i,
            /finally/i,
            /therefore/i,
            /thus/i,
            /hence/i
        ];
        
        let steps = [];
        let currentText = paragraphText;
        
        // Try to find natural step breaks
        for (let i = 0; i < stepIndicators.length; i++) {
            const indicator = stepIndicators[i];
            if (indicator.test(currentText)) {
                // Split by this indicator
                const parts = currentText.split(indicator);
                if (parts.length > 1) {
                    steps = parts.map((part, index) => ({
                        step: index + 1,
                        description: part.trim(),
                        expression: "",
                        explanation: "",
                        lineBreaks: part.trim().split(/[.!?]/).filter(s => s.trim().length > 0)
                    })).filter(step => step.description.length > 0);
                    break;
                }
            }
        }
        
        // If no natural breaks found, create artificial steps
        if (steps.length === 0) {
            const sentences = paragraphText.split(/[.!?]+/).filter(s => s.trim().length > 0);
            steps = sentences.map((sentence, index) => ({
                step: index + 1,
                description: sentence.trim(),
                expression: "",
                explanation: "",
                lineBreaks: [sentence.trim()]
            }));
        }
        
        return steps;
    };















    

    // Get function description
    const getFunctionDescription = (functionData, type) => {
        switch (type) {
            case 'linear':
                return `y = ${functionData.slope}x + ${functionData.intercept}`;
            case 'quadratic':
                const a = functionData.coefficients[2] || 0;
                const b = functionData.coefficients[1] || 0;
                const c = functionData.coefficients[0] || 0;
                return `y = ${a}x² + ${b}x + ${c}`;
            case 'cubic':
                const a3 = functionData.coefficients[3] || 0;
                const b3 = functionData.coefficients[2] || 0;
                const c3 = functionData.coefficients[1] || 0;
                const d3 = functionData.coefficients[0] || 0;
                return `y = ${a3}x³ + ${b3}x² + ${c3}x + ${d3}`;
            case 'logarithmic':
                if (functionData.type === 'natural_log') {
                    return `y = ln(x)`;
                } else {
                    return `y = log${functionData.base}(x)`;
                }
            case 'integrated_exponential_logarithmic':
                if (functionData.functionType === 'exponential') {
                    if (functionData.type === 'natural_exp') {
                        return `y = e^x`;
                    } else {
                        return `y = ${functionData.base}^x`;
                    }
                } else {
                    return `y = log${functionData.base}(x)`;
                }
            case 'trigonometric':
                return `y = ${functionData.type}(${functionData.argument})`;
            default:
                return 'Function';
        }
    };



    // Auto-analyze expression when it changes and switch to graph view
    useEffect(() => {
        if (exprData.expression && exprData.expression.trim() !== '') {
            // Analyze the expression to determine type
            analyzeExpression(exprData.expression);
            
            // If we're in graph view, ensure graph is shown
            if (exprData.viewMode === 'graph') {
                setExprData(prev => ({ ...prev, showGraph: true }));
            }
        }
    }, [exprData.expression]);



    useEffect(() => {
        // Ensure all required properties are initialized
        if (!exprData.targetOperation) {
            setExprData(prev => ({ ...prev, targetOperation: 'simplify' }));
            return;
        }
        if (!exprData.variable) {
            setExprData(prev => ({ ...prev, variable: 'x' }));
            return;
        }
        if (!exprData.steps) {
            setExprData(prev => ({ ...prev, steps: [] }));
            return;
        }
        if (exprData.result === undefined) {
            setExprData(prev => ({ ...prev, result: null }));
            return;
        }
        if (exprData.error === undefined) {
            setExprData(prev => ({ ...prev, error: null }));
            return;
        }
        if (exprData.xMin === undefined) {
            setExprData(prev => ({ ...prev, xMin: -10 }));
            return;
        }
        if (exprData.xMax === undefined) {
            setExprData(prev => ({ ...prev, xMax: 10 }));
            return;
        }
        if (exprData.showGraph === undefined) {
            setExprData(prev => ({ ...prev, showGraph: false }));
            return;
        }
        
        onChange(exprData);
    }, [exprData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        
        if (field === 'expression') {
            // Enhanced bidirectional synchronization for expressions
            const analysis = analyzeExpressionType(value);
            
            // Update the main expression and function data
            setExprData(prev => ({ 
                ...prev, 
                [field]: value,
                expressionType: analysis.type,
                functionData: analysis.functionData,
                // Auto-switch to graph view for recognized functions
                showGraph: analysis.type !== 'other',
                viewMode: analysis.type !== 'other' ? 'graph' : prev.viewMode
            }));
            
            // Auto-update function type if it wasn't manually selected and we detected a valid type
            if (!isFunctionTypeManual && analysis.type !== 'other') {
                setExprData(prev => ({ 
                    ...prev, 
                    functionType: analysis.type 
                }));
                console.log('Auto-updating function type to:', analysis.type);
                
                // Auto-update operation if current operation is not suitable for new function type
                const suggestedOperation = getSuggestedOperation(analysis.type);
                if (suggestedOperation && suggestedOperation !== exprData.targetOperation) {
                    setExprData(prev => ({ ...prev, targetOperation: suggestedOperation }));
                    console.log('Auto-updated operation to:', suggestedOperation, 'for detected function type:', analysis.type);
                }
            }
            
            // Update the dynamic expression display
            setDynamicExpression(value);
            
            // Clear any previous errors
            setExprData(prev => ({ ...prev, error: null }));
            
            console.log('Expression updated:', {
                newExpression: value,
                detectedType: analysis.type,
                functionData: analysis.functionData,
                autoUpdatedFunctionType: !isFunctionTypeManual && analysis.type !== 'other'
            });
            
        } else if (field === 'functionType') {
            // When function type changes, update expression and parameters
            const defaults = getDefaultEquation(value);
            const analysis = analyzeExpressionType(defaults.expression);
            
            setExprData(prev => ({
                ...prev,
                [field]: value,
                expression: defaults.expression,
                expressionType: analysis.type,
                functionData: analysis.functionData,
                variable: defaults.variable,
                xMin: defaults.xMin,
                xMax: defaults.xMax,
                yMin: defaults.yMin,
                yMax: defaults.yMax,
                showGraph: true,
                viewMode: 'graph'
            }));
            
            // Update dynamic expression
            setDynamicExpression(defaults.expression);
            
        } else {
            // For other fields, just update normally
            setExprData(prev => ({ ...prev, [field]: value }));
        }
    };









    const factorExpression = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            // Simple factoring for common patterns
            steps.push({
                step: 1,
                description: "Identify common factors",
                expression: currentExpr,
                explanation: "Look for common factors in all terms"
            });
            
            // Check for common factor
            const terms = currentExpr.split(/[+\-]/);
            let commonFactor = '';
            
            // Find common variables
            const allVars = new Set();
            terms.forEach(term => {
                const vars = term.match(/[a-z]/g) || [];
                vars.forEach(v => allVars.add(v));
            });
            
            allVars.forEach(v => {
                const minPower = Math.min(...terms.map(term => {
                    const match = term.match(new RegExp(`${v}\\^?(\\d*)`));
                    return match ? (match[1] ? parseInt(match[1]) : 1) : 0;
                }));
                if (minPower > 0) {
                    commonFactor += v + (minPower > 1 ? `^${minPower}` : '');
                }
            });
            
            if (commonFactor) {
                steps.push({
                    step: 2,
                    description: `Factor out common factor: ${commonFactor}`,
                    expression: `${commonFactor}(${currentExpr.replace(new RegExp(commonFactor, 'g'), '')})`,
                    explanation: `Extract the common factor ${commonFactor} from all terms`
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in factoring", expression: expr, explanation: "Could not factor expression" }] };
        }
    };

    const expandExpression = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify distributive property",
                expression: currentExpr,
                explanation: "Look for expressions that can be expanded using the distributive property"
            });
            
            // Simple expansion for (a+b)(c+d) pattern
            const match = currentExpr.match(/\(([^)]+)\)\s*\*\s*\(([^)]+)\)/);
            if (match) {
                const left = match[1];
                const right = match[2];
                
                const leftTerms = left.split(/[+\-]/);
                const rightTerms = right.split(/[+\-]/);
                
                let expanded = '';
                leftTerms.forEach(leftTerm => {
                    rightTerms.forEach(rightTerm => {
                        if (leftTerm && rightTerm) {
                            if (expanded) expanded += '+';
                            expanded += `(${leftTerm}*${rightTerm})`;
                        }
                    });
                });
                
                steps.push({
                    step: 2,
                    description: "Apply distributive property",
                    expression: expanded,
                    explanation: "Multiply each term in the first parentheses by each term in the second"
                });
                
                currentExpr = expanded;
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in expansion", expression: expr, explanation: "Could not expand expression" }] };
        }
    };

    const solveEquation = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify equation",
                expression: currentExpr,
                explanation: "Recognize this as an equation to be solved"
            });
            
            // Simple linear equation solving
            if (currentExpr.includes('=')) {
                const [left, right] = currentExpr.split('=');
                
                steps.push({
                    step: 2,
                    description: "Move all terms to one side",
                    expression: `${left}-(${right})=0`,
                    explanation: "Subtract the right side from both sides to set equation to zero"
                });
                
                // This is a simplified version - in practice, you'd need a more sophisticated solver
                steps.push({
                    step: 3,
                    description: "Solve for variable",
                    expression: `${exprData.variable} = ?`,
                    explanation: "Isolate the variable to find its value"
                });
            }
            
            return { result: "Solution requires more sophisticated solving", steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in solving", expression: expr, explanation: "Could not solve equation" }] };
        }
    };

    // Complete the square function with step-by-step visualization
    const completeSquare = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify quadratic expression",
                expression: currentExpr,
                explanation: "Recognize this as a quadratic expression in the form ax² + bx + c"
            });
            
            // Extract coefficients (simplified version)
            const match = currentExpr.match(/(\d*\.?\d*)x²\s*([+\-]\s*\d*\.?\d*)x\s*([+\-]\s*\d*\.?\d*)/);
            if (match) {
                const a = parseFloat(match[1]) || 1;
                const b = parseFloat(match[2].replace(/\s/g, ''));
                const c = parseFloat(match[3].replace(/\s/g, ''));
                
                steps.push({
                    step: 2,
                    description: "Extract coefficients",
                    expression: `a = ${a}, b = ${b}, c = ${c}`,
                    explanation: "Identify the coefficients of x², x, and constant terms"
                });
                
                // Step 3: Factor out 'a' if a ≠ 1
                if (a !== 1) {
                    steps.push({
                        step: 3,
                        description: "Factor out coefficient of x²",
                        expression: `${a}(x² + ${b/a}x + ${c/a})`,
                        explanation: `Factor out ${a} from the expression to get a(x² + (b/a)x + c/a)`
                    });
                    
                    const newB = b / a;
                    const newC = c / a;
                    
                    steps.push({
                        step: 4,
                        description: "Work with simplified expression",
                        expression: `x² + ${newB}x + ${newC}`,
                        explanation: "Now work with the expression inside the parentheses"
                    });
                    
                    // Calculate h and k for simplified expression
                    const h = -newB / 2;
                    const k = newC - (newB * newB) / 4;
                    
                    steps.push({
                        step: 5,
                        description: "Calculate h value",
                        expression: `h = -b/(2a) = -(${newB})/2 = ${h.toFixed(3)}`,
                        explanation: "Calculate h = -b/(2a) for the vertex form"
                    });
                    
                    steps.push({
                        step: 6,
                        description: "Calculate k value",
                        expression: `k = c - b²/(4a) = ${newC} - (${newB})²/4 = ${newC} - ${(newB * newB / 4).toFixed(3)} = ${k.toFixed(3)}`,
                        explanation: "Calculate k = c - b²/(4a) for the vertex form"
                    });
                    
                    steps.push({
                        step: 7,
                        description: "Write in vertex form",
                        expression: `(x + ${h.toFixed(3)})² + ${k.toFixed(3)}`,
                        explanation: "Express in the form (x + h)² + k"
                    });
                    
                    // Final form with original 'a'
                    const finalForm = `${a}(x + ${h.toFixed(3)})² + ${k.toFixed(3)}`;
                    steps.push({
                        step: 8,
                        description: "Final result with original coefficient",
                        expression: finalForm,
                        explanation: "Multiply by the original coefficient 'a' to get the final form"
                    });
                    
                    currentExpr = finalForm;
                } else {
                    // a = 1, simpler case
                    const h = -b / 2;
                    const k = c - (b * b) / 4;
                    
                    steps.push({
                        step: 3,
                        description: "Calculate h value",
                        expression: `h = -b/2 = -(${b})/2 = ${h.toFixed(3)}`,
                        explanation: "Calculate h = -b/2 for the vertex form"
                    });
                    
                    steps.push({
                        step: 4,
                        description: "Calculate k value",
                        expression: `k = c - b²/4 = ${c} - (${b})²/4 = ${c} - ${(b * b / 4).toFixed(3)} = ${k.toFixed(3)}`,
                        explanation: "Calculate k = c - b²/4 for the vertex form"
                    });
                    
                    // Final form
                    const finalForm = `(x + ${h.toFixed(3)})² + ${k.toFixed(3)}`;
                    steps.push({
                        step: 5,
                        description: "Write in vertex form",
                        expression: finalForm,
                        explanation: "Express in the form (x + h)² + k where (h, k) is the vertex"
                    });
                    
                    currentExpr = finalForm;
                }
            } else {
                steps.push({
                    step: 2,
                    description: "Expression not in standard form",
                    expression: currentExpr,
                    explanation: "Expression must be in the form ax² + bx + c to complete the square"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in completing square", expression: expr, explanation: "Could not complete the square" }] };
        }
    };

    // Polynomial long division function with step-by-step visualization
    const performLongDivision = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify division expression",
                expression: currentExpr,
                explanation: "Recognize this as a polynomial division problem"
            });
            
            // Look for division pattern (dividend) ÷ (divisor)
            const divisionMatch = currentExpr.match(/(.+)÷(.+)/);
            if (divisionMatch) {
                const dividend = divisionMatch[1].trim();
                const divisor = divisionMatch[2].trim();
                
                steps.push({
                    step: 2,
                    description: "Identify dividend and divisor",
                    expression: `Dividend: ${dividend}, Divisor: ${divisor}`,
                    explanation: "Separate the expression into dividend and divisor"
                });
                
                // Parse polynomials to get coefficients
                const dividendTerms = parsePolynomial(dividend);
                const divisorTerms = parsePolynomial(divisor);
                
                if (dividendTerms && divisorTerms) {
                    steps.push({
                        step: 3,
                        description: "Parse polynomials",
                        expression: `Dividend: ${dividendTerms.map(t => `${t.coef}x^${t.power}`).join(' + ')}\nDivisor: ${divisorTerms.map(t => `${t.coef}x^${t.power}`).join(' + ')}`,
                        explanation: "Break down polynomials into individual terms with coefficients and powers"
                    });
                    
                    // Perform step-by-step division
                    const divisionResult = performStepByStepDivision(dividendTerms, divisorTerms);
                    
                    if (divisionResult.success) {
                        steps.push({
                            step: 4,
                            description: "Set up long division",
                            expression: renderLongDivisionSetup(dividendTerms, divisorTerms),
                            explanation: "Set up the long division format with proper alignment"
                        });
                        
                        // Add each division step
                        divisionResult.steps.forEach((divStep, index) => {
                            steps.push({
                                step: 5 + index,
                                description: `Division step ${index + 1}`,
                                expression: divStep.expression,
                                explanation: divStep.explanation
                            });
                        });
                        
                        steps.push({
                            step: 5 + divisionResult.steps.length,
                            description: "Final result",
                            expression: `Quotient: ${divisionResult.quotient}\nRemainder: ${divisionResult.remainder}`,
                            explanation: "Complete the division process with quotient and remainder"
                        });
                        
                        currentExpr = `(${dividend}) ÷ (${divisor}) = ${divisionResult.quotient} + (${divisionResult.remainder})/(${divisor})`;
                    } else {
                        steps.push({
                            step: 4,
                            description: "Division not possible",
                            expression: "Cannot divide these polynomials",
                            explanation: divisionResult.error || "The divisor may be zero or the polynomials may not be compatible"
                        });
                    }
                } else {
                    steps.push({
                        step: 3,
                        description: "Invalid polynomial format",
                        expression: currentExpr,
                        explanation: "Please enter valid polynomials in standard form (e.g., x³ + 2x² - 5x + 6)"
                    });
                }
            } else {
                steps.push({
                    step: 2,
                    description: "Expression not in division format",
                    expression: currentExpr,
                    explanation: "Expression must be in the format (dividend) ÷ (divisor)"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in long division", expression: expr, explanation: "Could not perform long division" }] };
        }
    };

    // Helper function to parse polynomial into terms
    const parsePolynomial = (polyStr) => {
        try {
            const terms = [];
            const termRegex = /([+-]?\s*\d*\.?\d*)\s*x\s*\^?\s*(\d*)/g;
            let match;
            
            while ((match = termRegex.exec(polyStr)) !== null) {
                const coef = match[1] ? parseFloat(match[1].replace(/\s/g, '')) : 1;
                const power = match[2] ? parseInt(match[2]) : 1;
                
                if (!isNaN(coef) && !isNaN(power)) {
                    terms.push({ coef, power });
                }
            }
            
            // Sort by power (descending)
            terms.sort((a, b) => b.power - a.power);
            return terms;
        } catch (error) {
            return null;
        }
    };

    // Perform step-by-step polynomial division
    const performStepByStepDivision = (dividend, divisor) => {
        try {
            const steps = [];
            let currentDividend = [...dividend];
            let quotient = [];
            let remainder = [];
            
            // Find highest power in divisor
            const divisorHighestPower = Math.max(...divisor.map(t => t.power));
            
            while (currentDividend.length > 0 && 
                   Math.max(...currentDividend.map(t => t.power)) >= divisorHighestPower) {
                
                const currentHighestPower = Math.max(...currentDividend.map(t => t.power));
                const currentHighestCoef = currentDividend.find(t => t.power === currentHighestPower)?.coef || 0;
                
                // Find corresponding divisor term
                const divisorTerm = divisor.find(t => t.power === divisorHighestPower);
                if (!divisorTerm) break;
                
                // Calculate quotient term
                const quotientCoef = currentHighestCoef / divisorTerm.coef;
                const quotientPower = currentHighestPower - divisorHighestPower;
                
                quotient.push({ coef: quotientCoef, power: quotientPower });
                
                // Multiply divisor by quotient term and subtract
                const product = divisor.map(t => ({
                    coef: t.coef * quotientCoef,
                    power: t.power + quotientPower
                }));
                
                // Subtract product from current dividend
                currentDividend = subtractPolynomials(currentDividend, product);
                
                // Add step to visualization
                steps.push({
                    expression: renderDivisionStep(currentDividend, product, quotientCoef, quotientPower),
                    explanation: `Divide ${currentHighestCoef}x^${currentHighestPower} by ${divisorTerm.coef}x^${divisorHighestPower} = ${quotientCoef}x^${quotientPower}`
                });
                
                // Remove zero terms
                currentDividend = currentDividend.filter(t => Math.abs(t.coef) > 0.001);
            }
            
            remainder = currentDividend;
            
            return {
                success: true,
                quotient: formatPolynomial(quotient),
                remainder: formatPolynomial(remainder),
                steps: steps
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    };

    // Subtract two polynomials
    const subtractPolynomials = (poly1, poly2) => {
        const result = [...poly1];
        
        poly2.forEach(term2 => {
            const existingTerm = result.find(t => t.power === term2.power);
            if (existingTerm) {
                existingTerm.coef -= term2.coef;
            } else {
                result.push({ coef: -term2.coef, power: term2.power });
            }
        });
        
        return result;
    };

    // Format polynomial for display
    const formatPolynomial = (terms) => {
        if (terms.length === 0) return "0";
        
        return terms.map((term, index) => {
            let coefStr = "";
            if (term.coef === 1 && term.power > 0) coefStr = "";
            else if (term.coef === -1 && term.power > 0) coefStr = "-";
            else coefStr = term.coef.toString();
            
            let powerStr = "";
            if (term.power === 0) powerStr = "";
            else if (term.power === 1) powerStr = "x";
            else powerStr = `x^${term.power}`;
            
            return coefStr + powerStr;
        }).join(" + ").replace(/\+ -/g, "- ");
    };

    // Render long division setup with proper mathematical notation
    const renderLongDivisionSetup = (dividend, divisor) => {
        const dividendStr = formatPolynomial(dividend);
        const divisorStr = formatPolynomial(divisor);
        
        // Create the long division symbol (L-shaped bracket)
        const maxLength = Math.max(dividendStr.length, divisorStr.length);
        const horizontalLine = "─".repeat(maxLength + 2);
        
        return `${divisorStr} ) ${dividendStr}\n${horizontalLine}`;
    };

    // Render individual division step
    const renderDivisionStep = (currentDividend, product, quotientCoef, quotientPower) => {
        const currentStr = formatPolynomial(currentDividend);
        const productStr = formatPolynomial(product);
        const quotientStr = `${quotientCoef}x^${quotientPower}`;
        
        return `Current: ${currentStr}\nProduct: ${productStr}\nQuotient term: ${quotientStr}`;
    };

    // Solve cubic equations function with step-by-step visualization
    const solveCubicEquation = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify cubic equation",
                expression: currentExpr,
                explanation: "Recognize this as a cubic equation in the form ax³ + bx² + cx + d = 0"
            });
            
            if (currentExpr.includes('=')) {
                const [left, right] = currentExpr.split('=');
                
                steps.push({
                    step: 2,
                    description: "Move all terms to one side",
                    expression: `${left}-(${right})=0`,
                    explanation: "Subtract the right side from both sides to set equation to zero"
                });
                
                // Parse the cubic expression
                const cubicTerms = parseCubicExpression(left);
                if (cubicTerms) {
                    const { a, b, c, d } = cubicTerms;
                    
                    steps.push({
                        step: 3,
                        description: "Extract coefficients",
                        expression: `a = ${a}, b = ${b}, c = ${c}, d = ${d}`,
                        explanation: "Identify the coefficients of x³, x², x, and constant terms"
                    });
                    
                    steps.push({
                        step: 4,
                        description: "Standard form",
                        expression: `${a}x³ + ${b}x² + ${c}x + ${d} = 0`,
                        explanation: "Express in standard cubic form"
                    });
                    
                    // Check for common factor
                    const commonFactor = findCommonFactor([a, b, c, d]);
                    if (commonFactor > 1) {
                        steps.push({
                            step: 5,
                            description: "Factor out common factor",
                            expression: `${commonFactor}(${a/commonFactor}x³ + ${b/commonFactor}x² + ${c/commonFactor}x + ${d/commonFactor}) = 0`,
                            explanation: `Factor out the common factor ${commonFactor} from all coefficients`
                        });
                        
                        steps.push({
                            step: 6,
                            description: "Simplified equation",
                            expression: `${a/commonFactor}x³ + ${b/commonFactor}x² + ${c/commonFactor}x + ${d/commonFactor} = 0`,
                            explanation: "Work with the simplified equation inside parentheses"
                        });
                    }
                    
                    // Try to find rational roots using Rational Root Theorem
                    steps.push({
                        step: 7,
                        description: "Apply Rational Root Theorem",
                        expression: "Possible rational roots: ±factors of d / ±factors of a",
                        explanation: "Test possible rational roots based on factors of constant term and leading coefficient"
                    });
                    
                    const possibleRoots = findPossibleRationalRoots(a, d);
                    steps.push({
                        step: 8,
                        description: "List possible rational roots",
                        expression: `Possible roots: ${possibleRoots.join(', ')}`,
                        explanation: "These are the values to test as potential solutions"
                    });
                    
                    // Test for simple roots
                    let foundRoots = [];
                    for (let root of possibleRoots) {
                        if (Math.abs(evaluateCubic(a, b, c, d, root)) < 0.001) {
                            foundRoots.push(root);
                            break; // Found one root, can use synthetic division
                        }
                    }
                    
                    if (foundRoots.length > 0) {
                        const root = foundRoots[0];
                        steps.push({
                            step: 9,
                            description: "Found rational root",
                            expression: `x = ${root} is a root`,
                            explanation: `Testing shows that ${root} satisfies the equation`
                        });
                        
                        // Use synthetic division to factor out (x - root)
                        const syntheticResult = syntheticDivision(a, b, c, d, root);
                        steps.push({
                            step: 10,
                            description: "Synthetic division",
                            expression: `Divide by (x - ${root}) using synthetic division`,
                            explanation: "Use synthetic division to factor out the known root"
                        });
                        
                        steps.push({
                            step: 11,
                            description: "Result of synthetic division",
                            expression: `Quotient: ${syntheticResult.a}x² + ${syntheticResult.b}x + ${syntheticResult.c}`,
                            explanation: "The result gives us a quadratic equation"
                        });
                        
                        // Now solve the quadratic
                        const discriminant = syntheticResult.b * syntheticResult.b - 4 * syntheticResult.a * syntheticResult.c;
                        steps.push({
                            step: 12,
                            description: "Solve resulting quadratic",
                            expression: `${syntheticResult.a}x² + ${syntheticResult.b}x + ${syntheticResult.c} = 0`,
                            explanation: "Solve the quadratic equation using the quadratic formula"
                        });
                        
                        if (discriminant > 0) {
                            const x2 = (-syntheticResult.b + Math.sqrt(discriminant)) / (2 * syntheticResult.a);
                            const x3 = (-syntheticResult.b - Math.sqrt(discriminant)) / (2 * syntheticResult.a);
                            
                            steps.push({
                                step: 13,
                                description: "Quadratic formula",
                                expression: `x = (-${syntheticResult.b} ± √${discriminant}) / (2 × ${syntheticResult.a})`,
                                explanation: "Apply the quadratic formula to find remaining roots"
                            });
                            
                            steps.push({
                                step: 14,
                                description: "Calculate remaining roots",
                                expression: `x = ${x2.toFixed(3)} and x = ${x3.toFixed(3)}`,
                                explanation: "Calculate the two remaining roots"
                            });
                            
                            steps.push({
                                step: 15,
                                description: "All three roots",
                                expression: `x = ${root}, x = ${x2.toFixed(3)}, x = ${x3.toFixed(3)}`,
                                explanation: "Complete solution: one rational root and two irrational roots"
                            });
                            
                            currentExpr = `x = ${root}, x = ${x2.toFixed(3)}, x = ${x3.toFixed(3)}`;
                        } else if (discriminant === 0) {
                            const x2 = -syntheticResult.b / (2 * syntheticResult.a);
                            
                            steps.push({
                                step: 13,
                                description: "Repeated root",
                                expression: `x = ${x2.toFixed(3)} (repeated root)`,
                                explanation: "The quadratic has a repeated root"
                            });
                            
                            steps.push({
                                step: 14,
                                description: "All three roots",
                                expression: `x = ${root}, x = ${x2.toFixed(3)} (repeated)`,
                                explanation: "Complete solution: one rational root and one repeated irrational root"
                            });
                            
                            currentExpr = `x = ${root}, x = ${x2.toFixed(3)} (repeated)`;
                        } else {
                            steps.push({
                                step: 13,
                                description: "Complex roots",
                                expression: "Remaining roots are complex numbers",
                                explanation: "The quadratic has complex roots, which are beyond the scope of this solver"
                            });
                            
                            currentExpr = `x = ${root} (real root), complex roots for remaining solutions`;
                        }
                    } else {
                        steps.push({
                            step: 9,
                            description: "No simple rational roots found",
                            expression: "No simple rational roots detected",
                            explanation: "This cubic equation may require more advanced methods or numerical approximation"
                        });
                        
                        steps.push({
                            step: 10,
                            description: "Alternative methods",
                            expression: "Consider: Cardano's formula, numerical methods, or graphing",
                            explanation: "For complex cubics, consider using Cardano's formula or numerical approximation"
                        });
                        
                        currentExpr = "No simple rational roots found. Consider advanced methods.";
                    }
                } else {
                    steps.push({
                        step: 3,
                        description: "Cannot parse cubic expression",
                        expression: currentExpr,
                        explanation: "Please enter in standard form: ax³ + bx² + cx + d = 0"
                    });
                }
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in solving cubic equation", expression: expr, explanation: "Could not solve cubic equation" }] };
        }
    };

    // Helper function to parse cubic expression
    const parseCubicExpression = (exprStr) => {
        try {
            const terms = [];
            const termRegex = /([+-]?\s*\d*\.?\d*)\s*x\s*\^?\s*(\d*)/g;
            let match;
            
            while ((match = termRegex.exec(exprStr)) !== null) {
                const coef = match[1] ? parseFloat(match[1].replace(/\s/g, '')) : 1;
                const power = match[2] ? parseInt(match[2]) : 1;
                
                if (!isNaN(coef) && !isNaN(power)) {
                    terms.push({ coef, power });
                }
            }
            
            // Extract coefficients for x³, x², x, and constant
            const a = terms.find(t => t.power === 3)?.coef || 0;
            const b = terms.find(t => t.power === 2)?.coef || 0;
            const c = terms.find(t => t.power === 1)?.coef || 0;
            const d = terms.find(t => t.power === 0)?.coef || 0;
            
            return { a, b, c, d };
        } catch (error) {
            return null;
        }
    };

    // Helper function to find common factor
    const findCommonFactor = (numbers) => {
        const absNumbers = numbers.map(Math.abs).filter(n => n > 0);
        if (absNumbers.length === 0) return 1;
        
        let gcd = absNumbers[0];
        for (let i = 1; i < absNumbers.length; i++) {
            gcd = findGCD(gcd, absNumbers[i]);
        }
        return gcd;
    };

    // Helper function to find possible rational roots
    const findPossibleRationalRoots = (a, d) => {
        const factorsA = findFactors(Math.abs(a));
        const factorsD = findFactors(Math.abs(d));
        
        const possibleRoots = [];
        for (let factorD of factorsD) {
            for (let factorA of factorsA) {
                const root = factorD / factorA;
                if (!possibleRoots.includes(root)) {
                    possibleRoots.push(root);
                }
                if (!possibleRoots.includes(-root)) {
                    possibleRoots.push(-root);
                }
            }
        }
        
        // Sort and limit to reasonable values
        return possibleRoots
            .filter(r => Math.abs(r) <= 10)
            .sort((a, b) => Math.abs(a) - Math.abs(b));
    };

    // Helper function to find factors
    const findFactors = (n) => {
        const factors = [];
        for (let i = 1; i <= Math.sqrt(n); i++) {
            if (n % i === 0) {
                factors.push(i);
                if (i !== n / i) {
                    factors.push(n / i);
                }
            }
        }
        return factors.sort((a, b) => a - b);
    };

    // Helper function to evaluate cubic function
    const evaluateCubic = (a, b, c, d, x) => {
        return a * x * x * x + b * x * x + c * x + d;
    };

    // Helper function for synthetic division
    const syntheticDivision = (a, b, c, d, root) => {
        // Synthetic division algorithm
        let newA = a;
        let newB = b + a * root;
        let newC = c + newB * root;
        
        return { a: newA, b: newB, c: newC };
    };

    // Enhanced Quadratic Analysis function with discriminant analysis and vertex form
    const analyzeQuadratic = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify quadratic expression",
                expression: currentExpr,
                explanation: "Recognize this as a quadratic expression in the form ax² + bx + c"
            });
            
            // Parse the quadratic expression
            const match = currentExpr.match(/(\d*\.?\d*)x²\s*([+\-]\s*\d*\.?\d*)x\s*([+\-]\s*\d*\.?\d*)/);
            if (match) {
                const a = parseFloat(match[1]) || 1;
                const b = parseFloat(match[2].replace(/\s/g, ''));
                const c = parseFloat(match[3].replace(/\s/g, ''));
                
                steps.push({
                    step: 2,
                    description: "Extract coefficients",
                    expression: `a = ${a}, b = ${b}, c = ${c}`,
                    explanation: "Identify the coefficients of x², x, and constant terms"
                });
                
                steps.push({
                    step: 3,
                    description: "Standard form",
                    expression: `${a}x² + ${b}x + ${c}`,
                    explanation: "Express in standard quadratic form"
                });
                
                // Calculate discriminant
                const discriminant = b * b - 4 * a * c;
                steps.push({
                    step: 4,
                    description: "Calculate discriminant",
                    expression: `Δ = b² - 4ac = (${b})² - 4(${a})(${c}) = ${b * b} - ${4 * a * c} = ${discriminant}`,
                    explanation: "Calculate discriminant to determine nature of roots and parabola behavior"
                });
                
                // Analyze discriminant
                if (discriminant > 0) {
                    steps.push({
                        step: 5,
                        description: "Discriminant analysis",
                        expression: `Δ = ${discriminant} > 0`,
                        explanation: "Two distinct real roots - parabola crosses x-axis at two points"
                    });
                } else if (discriminant === 0) {
                    steps.push({
                        step: 5,
                        description: "Discriminant analysis",
                        expression: `Δ = ${discriminant} = 0`,
                        explanation: "One repeated real root - parabola touches x-axis at one point"
                    });
                } else {
                    steps.push({
                        step: 5,
                        description: "Discriminant analysis",
                        expression: `Δ = ${discriminant} < 0`,
                        explanation: "No real roots - parabola never crosses x-axis"
                    });
                }
                
                // Calculate vertex
                const h = -b / (2 * a);
                const k = c - (b * b) / (4 * a);
                
                steps.push({
                    step: 6,
                    description: "Calculate vertex coordinates",
                    expression: `h = -b/(2a) = -(${b})/(2 × ${a}) = ${h.toFixed(3)}`,
                    explanation: "Calculate x-coordinate of vertex using h = -b/(2a)"
                });
                
                steps.push({
                    step: 7,
                    description: "Calculate vertex y-coordinate",
                    expression: `k = c - b²/(4a) = ${c} - (${b})²/(4 × ${a}) = ${c} - ${(b * b / (4 * a)).toFixed(3)} = ${k.toFixed(3)}`,
                    explanation: "Calculate y-coordinate of vertex using k = c - b²/(4a)"
                });
                
                steps.push({
                    step: 8,
                    description: "Vertex form",
                    expression: `f(x) = ${a}(x - ${h.toFixed(3)})² + ${k.toFixed(3)}`,
                    explanation: "Express in vertex form f(x) = a(x - h)² + k where (h, k) is the vertex"
                });
                
                // Calculate roots if they exist
                if (discriminant >= 0) {
                    const x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
                    const x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
                    
                    if (discriminant > 0) {
                        steps.push({
                            step: 9,
                            description: "Calculate roots",
                            expression: `x = (-${b} ± √${discriminant})/(2 × ${a})`,
                            explanation: "Use quadratic formula to find the two distinct roots"
                        });
                        
                        steps.push({
                            step: 10,
                            description: "Root values",
                            expression: `x₁ = ${x1.toFixed(3)}, x₂ = ${x2.toFixed(3)}`,
                            explanation: "Calculate the exact values of both roots"
                        });
                    } else {
                        steps.push({
                            step: 9,
                            description: "Calculate repeated root",
                            expression: `x = -${b}/(2 × ${a}) = ${x1.toFixed(3)}`,
                            explanation: "Since discriminant is zero, there is one repeated root"
                        });
                    }
                }
                
                // Analyze parabola direction and shape
                steps.push({
                    step: 11,
                    description: "Parabola analysis",
                    expression: `a = ${a} ${a > 0 ? '> 0' : '< 0'}`,
                    explanation: `Parabola opens ${a > 0 ? 'upward' : 'downward'} and is ${Math.abs(a) > 1 ? 'narrower' : Math.abs(a) < 1 ? 'wider' : 'standard'} than y = x²`
                });
                
                // Calculate y-intercept
                steps.push({
                    step: 12,
                    description: "Y-intercept",
                    expression: `f(0) = ${a}(0)² + ${b}(0) + ${c} = ${c}`,
                    explanation: "The y-intercept is the point where x = 0"
                });
                
                // Calculate axis of symmetry
                steps.push({
                    step: 13,
                    description: "Axis of symmetry",
                    expression: `x = ${h.toFixed(3)}`,
                    explanation: "The axis of symmetry is the vertical line passing through the vertex"
                });
                
                currentExpr = `Vertex: (${h.toFixed(3)}, ${k.toFixed(3)}), Discriminant: ${discriminant}, Roots: ${discriminant >= 0 ? (discriminant > 0 ? `x₁ = ${((-b + Math.sqrt(discriminant)) / (2 * a)).toFixed(3)}, x₂ = ${((-b - Math.sqrt(discriminant)) / (2 * a)).toFixed(3)}` : `x = ${(-b / (2 * a)).toFixed(3)} (repeated)`) : 'No real roots'}`;
            } else {
                steps.push({
                    step: 2,
                    description: "Expression not in standard form",
                    expression: currentExpr,
                    explanation: "Expression must be in the form ax² + bx + c to analyze"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in quadratic analysis", expression: expr, explanation: "Could not analyze quadratic expression" }] };
        }
    };

    // Logarithmic Functions solver with step-by-step visualization
    const solveLogarithmic = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify logarithmic equation",
                expression: currentExpr,
                explanation: "Recognize this as a logarithmic equation to be solved"
            });
            
            // Look for logarithmic patterns
            const logMatch = currentExpr.match(/log_?(\d+)?\s*\(([^)]+)\)\s*=\s*(\d+)/);
            if (logMatch) {
                const base = logMatch[1] ? parseInt(logMatch[1]) : 10; // Default to base 10
                const argument = logMatch[2];
                const result = parseFloat(logMatch[3]);
                
                steps.push({
                    step: 2,
                    description: "Parse logarithmic equation",
                    expression: `log_${base}(${argument}) = ${result}`,
                    explanation: `Identify base ${base}, argument ${argument}, and result ${result}`
                });
                
                steps.push({
                    step: 3,
                    description: "Convert to exponential form",
                    expression: `${base}^${result} = ${argument}`,
                    explanation: "Use the definition: log_b(x) = y means b^y = x"
                });
                
                // Check if the argument is a simple expression
                if (argument.includes('x')) {
                    // Solve for x in the argument
                    if (argument.match(/^x\s*[+\-]\s*\d+$/)) {
                        // Simple linear: x + a or x - a
                        const linearMatch = argument.match(/x\s*([+\-])\s*(\d+)/);
                        if (linearMatch) {
                            const operator = linearMatch[1];
                            const constant = parseFloat(linearMatch[2]);
                            
                            steps.push({
                                step: 4,
                                description: "Solve for x in argument",
                                expression: `${base}^${result} = x ${operator} ${constant}`,
                                explanation: "Substitute the exponential form for the argument"
                            });
                            
                            let xValue;
                            if (operator === '+') {
                                xValue = Math.pow(base, result) - constant;
                                steps.push({
                                    step: 5,
                                    description: "Subtract constant from both sides",
                                    expression: `x = ${base}^${result} - ${constant} = ${Math.pow(base, result)} - ${constant} = ${xValue.toFixed(3)}`,
                                    explanation: "Isolate x by subtracting the constant"
                                });
                            } else {
                                xValue = Math.pow(base, result) + constant;
                                steps.push({
                                    step: 5,
                                    description: "Add constant to both sides",
                                    expression: `x = ${base}^${result} + ${constant} = ${Math.pow(base, result)} + ${constant} = ${xValue.toFixed(3)}`,
                                    explanation: "Isolate x by adding the constant"
                                });
                            }
                            
                            steps.push({
                                step: 6,
                                description: "Solution",
                                expression: `x = ${xValue.toFixed(3)}`,
                                explanation: "The solution to the logarithmic equation"
                            });
                            
                            currentExpr = `x = ${xValue.toFixed(3)}`;
                        }
                    } else if (argument === 'x') {
                        // Simple case: log_b(x) = y
                        const xValue = Math.pow(base, result);
                        
                        steps.push({
                            step: 4,
                            description: "Solve for x",
                            expression: `x = ${base}^${result} = ${xValue.toFixed(3)}`,
                            explanation: "Direct solution using exponential form"
                        });
                        
                        currentExpr = `x = ${xValue.toFixed(3)}`;
                    } else {
                        steps.push({
                            step: 4,
                            description: "Complex argument",
                            expression: `Argument ${argument} contains complex expression`,
                            explanation: "This requires more advanced solving techniques"
                        });
                        
                        currentExpr = "Complex logarithmic equation - requires advanced methods";
                    }
                } else {
                    // No variable in argument
                    steps.push({
                        step: 4,
                        description: "No variable in argument",
                        expression: `Argument ${argument} contains no variable x`,
                        explanation: "This is not an equation to solve for x"
                    });
                    
                    currentExpr = "No variable to solve for";
                }
            } else {
                steps.push({
                    step: 2,
                    description: "Not a standard logarithmic equation",
                    expression: currentExpr,
                    explanation: "Please enter in format: log_b(expression) = value"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in solving logarithmic equation", expression: expr, explanation: "Could not solve logarithmic equation" }] };
        }
    };

    // Complex Numbers operations with step-by-step visualization
    const performComplexOperations = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify complex number expression",
                expression: currentExpr,
                explanation: "Recognize this as a complex number operation"
            });
            
            // Parse complex numbers in the form (a + bi) or (a - bi)
            const complexMatch = currentExpr.match(/\(([^)]+)\)\s*([+\-])\s*\(([^)]+)\)/);
            if (complexMatch) {
                const leftComplex = complexMatch[1];
                const operator = complexMatch[2];
                const rightComplex = complexMatch[3];
                
                steps.push({
                    step: 2,
                    description: "Parse complex numbers",
                    expression: `Left: ${leftComplex}, Operator: ${operator}, Right: ${rightComplex}`,
                    explanation: "Separate the expression into left and right complex numbers"
                });
                
                // Parse individual complex numbers
                const leftParsed = parseComplexNumber(leftComplex);
                const rightParsed = parseComplexNumber(rightComplex);
                
                if (leftParsed && rightParsed) {
                    steps.push({
                        step: 3,
                        description: "Extract real and imaginary parts",
                        expression: `Left: ${leftParsed.real} + ${leftParsed.imaginary}i, Right: ${rightParsed.real} + ${rightParsed.imaginary}i`,
                        explanation: "Express each complex number in standard form a + bi"
                    });
                    
                    let result;
                    if (operator === '+') {
                        // Addition: (a + bi) + (c + di) = (a + c) + (b + d)i
                        const realPart = leftParsed.real + rightParsed.real;
                        const imagPart = leftParsed.imaginary + rightParsed.imaginary;
                        
                        steps.push({
                            step: 4,
                            description: "Add real parts",
                            expression: `Real: ${leftParsed.real} + ${rightParsed.real} = ${realPart}`,
                            explanation: "Add the real parts of both complex numbers"
                        });
                        
                        steps.push({
                            step: 5,
                            description: "Add imaginary parts",
                            expression: `Imaginary: ${leftParsed.imaginary} + ${rightParsed.imaginary} = ${imagPart}`,
                            explanation: "Add the imaginary parts of both complex numbers"
                        });
                        
                        steps.push({
                            step: 6,
                            description: "Result in standard form",
                            expression: `${realPart} + ${imagPart}i`,
                            explanation: "Combine real and imaginary parts"
                        });
                        
                        result = `${realPart} + ${imagPart}i`;
                    } else {
                        // Subtraction: (a + bi) - (c + di) = (a - c) + (b - d)i
                        const realPart = leftParsed.real - rightParsed.real;
                        const imagPart = leftParsed.imaginary - rightParsed.imaginary;
                        
                        steps.push({
                            step: 4,
                            description: "Subtract real parts",
                            expression: `Real: ${leftParsed.real} - ${rightParsed.real} = ${realPart}`,
                            explanation: "Subtract the real parts"
                        });
                        
                        steps.push({
                            step: 5,
                            description: "Subtract imaginary parts",
                            expression: `Imaginary: ${leftParsed.imaginary} - ${rightParsed.imaginary} = ${imagPart}`,
                            explanation: "Subtract the imaginary parts"
                        });
                        
                        steps.push({
                            step: 6,
                            description: "Result in standard form",
                            expression: `${realPart} + ${imagPart}i`,
                            explanation: "Combine real and imaginary parts"
                        });
                        
                        result = `${realPart} + ${imagPart}i`;
                    }
                    
                    // Calculate magnitude and argument
                    const magnitude = Math.sqrt(result.split('+')[0] * result.split('+')[0] + result.split('+')[1].replace('i', '') * result.split('+')[1].replace('i', ''));
                    const realPart = parseFloat(result.split('+')[0]);
                    const imagPart = parseFloat(result.split('+')[1].replace('i', ''));
                    const argument = Math.atan2(imagPart, realPart) * (180 / Math.PI);
                    
                    steps.push({
                        step: 7,
                        description: "Calculate magnitude",
                        expression: `|z| = √(${realPart}² + ${imagPart}²) = √${(realPart * realPart + imagPart * imagPart).toFixed(3)} = ${magnitude.toFixed(3)}`,
                        explanation: "Calculate the magnitude (distance from origin) of the result"
                    });
                    
                    steps.push({
                        step: 8,
                        description: "Calculate argument",
                        expression: `arg(z) = arctan(${imagPart}/${realPart}) = ${argument.toFixed(3)}°`,
                        explanation: "Calculate the argument (angle from positive real axis)"
                    });
                    
                    steps.push({
                        step: 9,
                        description: "Polar form",
                        expression: `${magnitude.toFixed(3)}∠${argument.toFixed(3)}°`,
                        explanation: "Express result in polar form (magnitude ∠ argument)"
                    });
                    
                    currentExpr = `${result} (Standard: ${result}, Polar: ${magnitude.toFixed(3)}∠${argument.toFixed(3)}°)`;
                } else {
                    steps.push({
                        step: 3,
                        description: "Cannot parse complex numbers",
                        expression: currentExpr,
                        explanation: "Please enter in format: (a + bi) ± (c + di)"
                    });
                }
            } else {
                steps.push({
                    step: 2,
                    description: "Not a standard complex operation",
                    expression: currentExpr,
                    explanation: "Please enter in format: (a + bi) ± (c + di)"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in complex operations", expression: expr, explanation: "Could not perform complex number operations" }] };
        }
    };

    // Helper function to parse complex numbers
    const parseComplexNumber = (complexStr) => {
        try {
            // Match patterns like "3 + 4i", "3 - 4i", "3", "4i"
            const match = complexStr.match(/([+-]?\d*\.?\d*)\s*([+-]?\s*\d*\.?\d*)i?/);
            if (match) {
                const realPart = match[1] ? parseFloat(match[1]) : 0;
                const imagPart = match[2] ? parseFloat(match[2].replace(/\s/g, '')) : 0;
                
                if (!isNaN(realPart) && !isNaN(imagPart)) {
                    return { real: realPart, imaginary: imagPart };
                }
            }
            return null;
        } catch (error) {
            return null;
        }
    };

    // Solve simultaneous equations function with step-by-step visualization
    const solveSimultaneousEquations = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify simultaneous equations",
                expression: currentExpr,
                explanation: "Recognize this as a system of simultaneous equations"
            });
            
            // Look for system of equations pattern
            if (currentExpr.includes(';') || currentExpr.includes('\n')) {
                const equations = currentExpr.split(/[;\n]/).filter(eq => eq.trim());
                
                if (equations.length === 2) {
                    steps.push({
                        step: 2,
                        description: "Separate equations",
                        expression: equations.map((eq, i) => `Equation ${i + 1}: ${eq.trim()}`).join('\n'),
                        explanation: "Identify each equation in the system"
                    });
                    
                    // Parse equations to extract coefficients
                    const eq1 = parseLinearEquation(equations[0]);
                    const eq2 = parseLinearEquation(equations[1]);
                    
                    if (eq1 && eq2) {
                        steps.push({
                            step: 3,
                            description: "Extract coefficients",
                            expression: `Equation 1: ${eq1.a}x + ${eq1.b}y = ${eq1.c}\nEquation 2: ${eq2.a}x + ${eq2.b}y = ${eq2.c}`,
                            explanation: "Express equations in standard form ax + by = c"
                        });
                        
                        // Use elimination method
                        steps.push({
                            step: 4,
                            description: "Choose elimination method",
                            expression: "Use elimination method to solve the system",
                            explanation: "Multiply equations to make coefficients of one variable equal, then subtract"
                        });
                        
                        // Find LCM of coefficients for elimination
                        const lcmX = findLCM(Math.abs(eq1.a), Math.abs(eq2.a));
                        const lcmY = findLCM(Math.abs(eq1.b), Math.abs(eq2.b));
                        
                        // Choose which variable to eliminate (whichever has smaller LCM)
                        let eliminateX = lcmX <= lcmY;
                        
                        if (eliminateX) {
                            const mult1 = lcmX / Math.abs(eq1.a);
                            const mult2 = lcmX / Math.abs(eq2.a);
                            
                            steps.push({
                                step: 5,
                                description: "Eliminate x variable",
                                expression: `Multiply Equation 1 by ${mult1} and Equation 2 by ${mult2}`,
                                explanation: "Make coefficients of x equal for elimination"
                            });
                            
                            const newEq1 = { a: eq1.a * mult1, b: eq1.b * mult1, c: eq1.c * mult1 };
                            const newEq2 = { a: eq2.a * mult2, b: eq2.b * mult2, c: eq2.c * mult2 };
                            
                            steps.push({
                                step: 6,
                                description: "New equations after multiplication",
                                expression: `Equation 1: ${newEq1.a}x + ${newEq1.b}y = ${newEq1.c}\nEquation 2: ${newEq2.a}x + ${newEq2.b}y = ${newEq2.c}`,
                                explanation: "Equations after multiplying to make x coefficients equal"
                            });
                            
                            // Subtract equations to eliminate x
                            const newB = newEq1.b - newEq2.b;
                            const newC = newEq1.c - newEq2.c;
                            
                            steps.push({
                                step: 7,
                                description: "Subtract equations",
                                expression: `(${newEq1.a}x + ${newEq1.b}y = ${newEq1.c}) - (${newEq2.a}x + ${newEq2.b}y = ${newEq2.c})`,
                                explanation: "Subtract Equation 2 from Equation 1 to eliminate x"
                            });
                            
                            steps.push({
                                step: 8,
                                description: "Result after elimination",
                                expression: `${newB}y = ${newC}`,
                                explanation: "x terms cancel out, leaving equation in y only"
                            });
                            
                            // Solve for y
                            const y = newC / newB;
                            steps.push({
                                step: 9,
                                description: "Solve for y",
                                expression: `y = ${newC} / ${newB} = ${y.toFixed(3)}`,
                                explanation: "Divide both sides by the coefficient of y"
                            });
                            
                            // Substitute y back to find x
                            steps.push({
                                step: 10,
                                description: "Substitute y back",
                                expression: `Substitute y = ${y.toFixed(3)} into Equation 1: ${eq1.a}x + ${eq1.b}(${y.toFixed(3)}) = ${eq1.c}`,
                                explanation: "Use the value of y to find x from one of the original equations"
                            });
                            
                            const x = (eq1.c - eq1.b * y) / eq1.a;
                            steps.push({
                                step: 11,
                                description: "Solve for x",
                                expression: `${eq1.a}x + ${(eq1.b * y).toFixed(3)} = ${eq1.c}\n${eq1.a}x = ${eq1.c} - ${(eq1.b * y).toFixed(3)} = ${(eq1.c - eq1.b * y).toFixed(3)}\nx = ${(eq1.c - eq1.b * y).toFixed(3)} / ${eq1.a} = ${x.toFixed(3)}`,
                                explanation: "Solve the resulting equation for x"
                            });
                            
                            steps.push({
                                step: 12,
                                description: "Solution",
                                expression: `x = ${x.toFixed(3)}, y = ${y.toFixed(3)}`,
                                explanation: "The solution to the system of equations"
                            });
                            
                            currentExpr = `x = ${x.toFixed(3)}, y = ${y.toFixed(3)}`;
                        } else {
                            // Eliminate y variable (similar process)
                            const mult1 = lcmY / Math.abs(eq1.b);
                            const mult2 = lcmY / Math.abs(eq2.b);
                            
                            steps.push({
                                step: 5,
                                description: "Eliminate y variable",
                                expression: `Multiply Equation 1 by ${mult1} and Equation 2 by ${mult2}`,
                                explanation: "Make coefficients of y equal for elimination"
                            });
                            
                            // Similar elimination process for y...
                            steps.push({
                                step: 6,
                                description: "Elimination process",
                                expression: "Similar process to eliminate y variable",
                                explanation: "Follow the same steps but eliminate y instead of x"
                            });
                            
                            currentExpr = "Solution requires completing the elimination process";
                        }
                    } else {
                        steps.push({
                            step: 3,
                            description: "Cannot parse equations",
                            expression: currentExpr,
                            explanation: "Please enter equations in standard form: ax + by = c"
                        });
                    }
                } else {
                    steps.push({
                        step: 2,
                        description: "System must have exactly 2 equations",
                        expression: `Found ${equations.length} equations`,
                        explanation: "This solver currently supports systems with exactly 2 equations"
                    });
                }
            } else {
                steps.push({
                    step: 2,
                    description: "Expression not in system format",
                    expression: currentExpr,
                    explanation: "Expression must contain multiple equations separated by semicolons or newlines"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in solving simultaneous equations", expression: expr, explanation: "Could not solve simultaneous equations" }] };
        }
    };

    // Helper function to parse linear equation
    const parseLinearEquation = (eqStr) => {
        try {
            const match = eqStr.match(/(\d*\.?\d*)x\s*([+\-]\s*\d*\.?\d*)y\s*=\s*(\d*\.?\d*)/);
            if (match) {
                const a = parseFloat(match[1]) || 1;
                const b = parseFloat(match[2].replace(/\s/g, ''));
                const c = parseFloat(match[3]);
                return { a, b, c };
            }
            return null;
        } catch (error) {
            return null;
        }
    };

    // Helper function to find LCM
    const findLCM = (a, b) => {
        return Math.abs(a * b) / findGCD(a, b);
    };

    // Helper function to find GCD
    const findGCD = (a, b) => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Solve inequalities function with step-by-step visualization
    const solveInequalities = (expr) => {
        const steps = [];
        let currentExpr = expr;
        
        try {
            steps.push({
                step: 1,
                description: "Identify inequality",
                expression: currentExpr,
                explanation: "Recognize this as an inequality to be solved"
            });
            
            // Check for inequality symbols
            if (/[<>≤≥]/.test(currentExpr)) {
                steps.push({
                    step: 2,
                    description: "Identify inequality type",
                    expression: currentExpr,
                    explanation: "Determine if this is a linear or quadratic inequality"
                });
                
                // Check if it's quadratic
                if (currentExpr.includes('x²') || currentExpr.includes('x^2')) {
                    steps.push({
                        step: 3,
                        description: "Quadratic inequality",
                        expression: "ax² + bx + c > 0 (or <, ≤, ≥)",
                        explanation: "This is a quadratic inequality that requires special handling"
                    });
                    
                    // Extract coefficients for quadratic
                    const match = currentExpr.match(/(\d*\.?\d*)x²\s*([+\-]\s*\d*\.?\d*)x\s*([+\-]\s*\d*\.?\d*)\s*([<>≤≥])\s*(\d*\.?\d*)/);
                    if (match) {
                        const a = parseFloat(match[1]) || 1;
                        const b = parseFloat(match[2].replace(/\s/g, ''));
                        const c = parseFloat(match[3].replace(/\s/g, ''));
                        const inequality = match[4];
                        const rightSide = parseFloat(match[5]);
                        
                        steps.push({
                            step: 4,
                            description: "Extract coefficients",
                            expression: `a = ${a}, b = ${b}, c = ${c}, inequality: ${inequality}, right side: ${rightSide}`,
                            explanation: "Identify the coefficients and inequality symbol"
                        });
                        
                        // Move all terms to left side
                        const newC = c - rightSide;
                        steps.push({
                            step: 5,
                            description: "Move all terms to left side",
                            expression: `${a}x² + ${b}x + ${newC} ${inequality} 0`,
                            explanation: "Subtract the right side from both sides to get standard form"
                        });
                        
                        // Find critical points by solving ax² + bx + c = 0
                        const discriminant = b * b - 4 * a * newC;
                        steps.push({
                            step: 6,
                            description: "Calculate discriminant",
                            expression: `b² - 4ac = (${b})² - 4(${a})(${newC}) = ${discriminant}`,
                            explanation: "Calculate discriminant to determine nature of roots"
                        });
                        
                        if (discriminant > 0) {
                            const x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
                            const x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
                            
                            steps.push({
                                step: 7,
                                description: "Find x-intercepts",
                                expression: `x = ${x1.toFixed(3)} and x = ${x2.toFixed(3)}`,
                                explanation: "Solve ax² + bx + c = 0 to find critical points"
                            });
                            
                            steps.push({
                                step: 8,
                                description: "Test intervals",
                                expression: `Test x < ${x2.toFixed(3)}, ${x2.toFixed(3)} < x < ${x1.toFixed(3)}, x > ${x1.toFixed(3)}`,
                                explanation: "Test values in each interval to determine where inequality is satisfied"
                            });
                            
                            // Determine solution based on inequality and parabola direction
                            let solution;
                            if (a > 0) { // Parabola opens upward
                                if (inequality === '>') {
                                    solution = `x < ${x2.toFixed(3)} or x > ${x1.toFixed(3)}`;
                                } else if (inequality === '<') {
                                    solution = `${x2.toFixed(3)} < x < ${x1.toFixed(3)}`;
                                } else if (inequality === '≥') {
                                    solution = `x ≤ ${x2.toFixed(3)} or x ≥ ${x1.toFixed(3)}`;
                                } else if (inequality === '≤') {
                                    solution = `${x2.toFixed(3)} ≤ x ≤ ${x1.toFixed(3)}`;
                                }
                            } else { // Parabola opens downward
                                if (inequality === '>') {
                                    solution = `${x1.toFixed(3)} < x < ${x2.toFixed(3)}`;
                                } else if (inequality === '<') {
                                    solution = `x < ${x1.toFixed(3)} or x > ${x2.toFixed(3)}`;
                                } else if (inequality === '≥') {
                                    solution = `${x1.toFixed(3)} ≤ x ≤ ${x2.toFixed(3)}`;
                                } else if (inequality === '≤') {
                                    solution = `x ≤ ${x1.toFixed(3)} or x ≥ ${x2.toFixed(3)}`;
                                }
                            }
                            
                            steps.push({
                                step: 9,
                                description: "Solution",
                                expression: solution,
                                explanation: "Based on testing intervals and parabola direction"
                            });
                            
                            currentExpr = solution;
                        } else {
                            steps.push({
                                step: 7,
                                description: "No real roots",
                                expression: "Discriminant ≤ 0, no x-intercepts",
                                explanation: "The parabola never crosses the x-axis"
                            });
                            
                            // Test a single point to determine solution
                            const testPoint = 0;
                            const testValue = a * testPoint * testPoint + b * testPoint + newC;
                            
                            steps.push({
                                step: 8,
                                description: "Test a point",
                                expression: `Test x = ${testPoint}: ${a}(${testPoint})² + ${b}(${testPoint}) + ${newC} = ${testValue}`,
                                explanation: "Test a point to determine if the inequality is satisfied"
                            });
                            
                            let solution;
                            if (a > 0) { // Parabola opens upward
                                if (inequality === '>') {
                                    solution = "All real numbers";
                                } else if (inequality === '<') {
                                    solution = "No solution";
                                } else if (inequality === '≥') {
                                    solution = "All real numbers";
                                } else if (inequality === '≤') {
                                    solution = "No solution";
                                }
                            } else { // Parabola opens downward
                                if (inequality === '>') {
                                    solution = "No solution";
                                } else if (inequality === '<') {
                                    solution = "All real numbers";
                                } else if (inequality === '≥') {
                                    solution = "No solution";
                                } else if (inequality === '≤') {
                                    solution = "All real numbers";
                                }
                            }
                            
                            steps.push({
                                step: 9,
                                description: "Solution",
                                expression: solution,
                                explanation: "Based on parabola direction and test point"
                            });
                            
                            currentExpr = solution;
                        }
                    } else {
                        steps.push({
                            step: 4,
                            description: "Cannot parse quadratic expression",
                            expression: currentExpr,
                            explanation: "Please enter in standard form: ax² + bx + c > 0"
                        });
                    }
                } else {
                    // Linear inequality
                    steps.push({
                        step: 3,
                        description: "Linear inequality",
                        expression: "ax + b > 0 (or <, ≤, ≥)",
                        explanation: "This is a linear inequality that can be solved directly"
                    });
                    
                    // Parse linear inequality
                    const match = currentExpr.match(/(\d*\.?\d*)x\s*([+\-]\s*\d*\.?\d*)\s*([<>≤≥])\s*(\d*\.?\d*)/);
                    if (match) {
                        const a = parseFloat(match[1]) || 1;
                        const b = parseFloat(match[2].replace(/\s/g, ''));
                        const inequality = match[3];
                        const rightSide = parseFloat(match[4]);
                        
                        steps.push({
                            step: 4,
                            description: "Extract coefficients",
                            expression: `a = ${a}, b = ${b}, inequality: ${inequality}, right side: ${rightSide}`,
                            explanation: "Identify the coefficients and inequality symbol"
                        });
                        
                        // Solve for x
                        const solution = (rightSide - b) / a;
                        steps.push({
                            step: 5,
                            description: "Solve for x",
                            expression: `${a}x + ${b} ${inequality} ${rightSide}`,
                            explanation: "Start with the original inequality"
                        });
                        
                        steps.push({
                            step: 6,
                            description: "Subtract b from both sides",
                            expression: `${a}x ${inequality} ${rightSide - b}`,
                            explanation: `Subtract ${b} from both sides`
                        });
                        
                        steps.push({
                            step: 7,
                            description: "Divide by a",
                            expression: `x ${inequality} ${solution}`,
                            explanation: `Divide both sides by ${a}`
                        });
                        
                        // Handle sign change if a < 0
                        if (a < 0) {
                            steps.push({
                                step: 8,
                                description: "Reverse inequality (a < 0)",
                                expression: `x ${reverseInequality(inequality)} ${solution}`,
                                explanation: "When dividing by a negative number, reverse the inequality sign"
                            });
                            
                            currentExpr = `x ${reverseInequality(inequality)} ${solution}`;
                        } else {
                            currentExpr = `x ${inequality} ${solution}`;
                        }
                    } else {
                        steps.push({
                            step: 4,
                            description: "Cannot parse linear expression",
                            expression: currentExpr,
                            explanation: "Please enter in standard form: ax + b > 0"
                        });
                    }
                }
            } else {
                steps.push({
                    step: 2,
                    description: "No inequality symbols found",
                    expression: currentExpr,
                    explanation: "Expression must contain inequality symbols (<, >, ≤, ≥)"
                });
            }
            
            return { result: currentExpr, steps };
        } catch (error) {
            return { result: expr, steps: [{ step: 1, description: "Error in solving inequality", expression: expr, explanation: "Could not solve inequality" }] };
        }
    };

    // Helper function to reverse inequality signs
    const reverseInequality = (inequality) => {
        switch (inequality) {
            case '>': return '<';
            case '<': return '>';
            case '≥': return '≤';
            case '≤': return '≥';
            default: return inequality;
        }
    };

    const performOperation = () => {
        // Use dynamic expression if available, otherwise fall back to main expression
        const expressionToUse = dynamicExpression && dynamicExpression.trim() ? 
            dynamicExpression : exprData.expression;
            
        if (!expressionToUse || !expressionToUse.trim()) {
            setExprData(prev => ({ ...prev, error: "Please enter an expression" }));
            return;
        }
        
        // Ensure the main expression is updated with the dynamic expression
        if (dynamicExpression && dynamicExpression !== exprData.expression) {
            setExprData(prev => ({ ...prev, expression: dynamicExpression }));
            console.log('Updated main expression from dynamic expression for operation:', dynamicExpression);
        }

        // Validate that the expression is suitable for the selected operation
        const operationValidation = validateOperationForExpression(expressionToUse, exprData.targetOperation);
        if (!operationValidation.isValid) {
            setExprData(prev => ({ 
                ...prev, 
                error: operationValidation.message,
                steps: []
            }));
            return;
        }

        setExprData(prev => ({ ...prev, error: null, steps: [] }));

        let result;
        switch (exprData.targetOperation) {
            case 'solve':
                result = solveEquation(expressionToUse);
                break;
            case 'simplify':
                result = simplifyExpression(expressionToUse);
                break;
            case 'factorize':
                result = factorExpression(expressionToUse);
                break;
            case 'expand':
                result = expandExpression(expressionToUse);
                break;
            case 'complete_square':
                result = completeSquare(expressionToUse);
                break;
            case 'long_division':
                result = performLongDivision(expressionToUse);
                break;
            default:
                result = { result: expressionToUse, steps: [] };
        }

        // Generate comprehensive step-by-step guidance
        const comprehensiveSteps = generateComprehensiveSteps(
            exprData.targetOperation, 
            expressionToUse, 
            result.result
        );

        // Update both steps and stepCanvas with comprehensive guidance
        setExprData(prev => ({
            ...prev,
            result: result.result,
            steps: comprehensiveSteps,
            // Also populate the stepCanvas with the comprehensive operation results
            stepCanvas: comprehensiveSteps.map(step => ({
                ...step,
                lineBreaks: step.description ? step.description.split(/[.!?]/).filter(s => s.trim().length > 0) : [step.description]
            }))
        }));
        
        // Log operation completion for debugging
        console.log('Operation completed successfully:', {
            operation: exprData.targetOperation,
            inputExpression: expressionToUse,
            result: result.result,
            stepsCount: comprehensiveSteps.length,
            expressionType: exprData.expressionType,
            functionType: exprData.functionType
        });
    };









    // Don't render if not properly initialized
    if (!exprData.targetOperation || !exprData.variable) {
        return (
            <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
                <h3 className="font-semibold text-gray-700 mb-4">Algebraic Expression Builder</h3>
                <div className="text-center py-8 text-gray-500">
                    <p>Loading algebraic expression builder configuration...</p>
                </div>
            </div>
        );
    }

    // Enhanced Canvas Interaction Functions
































    return (
        <div className="p-1 bg-white mt-0.5 overflow-hidden">
            
            {/* Two-pane layout: Left controls, Right view */}
            <div className="grid grid-cols-1 lg:grid-cols-4 gap-1">
                {/* LEFT: Inputs and controls */}
                <div className="lg:col-span-1 h-[calc(100vh-4rem)] overflow-y-auto pr-1">
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-1 gap-2 mb-2">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Type of Function:
                        {isFunctionTypeManual ? (
                            <span className="ml-2 text-xs text-blue-600">(Manually Selected)</span>
                        ) : (
                            <span className="ml-2 text-xs text-green-600">(Auto-Detected)</span>
                        )}
                    </label>
                    <select
                        className={`w-full p-2 border rounded-md text-sm transition-colors ${
                            isFunctionTypeManual 
                                ? 'border-blue-300 bg-blue-50' 
                                : 'border-green-300 bg-green-50'
                        }`}
                        value={exprData.functionType}
                        onChange={(e) => handleFunctionTypeChange(e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="linear">Linear</option>
                        <option value="quadratic">Quadratic</option>
                        <option value="cubic">Cubic</option>
                        <option value="integrated_exponential_logarithmic">Exponential + Logarithmic (Integrated)</option>
                        <option value="trigonometric">Trigonometric</option>
                        <option value="hyperbolic">Hyperbolic</option>
                    </select>
                    <p className="text-xs text-gray-500 mt-1">
                        {isFunctionTypeManual 
                            ? 'You can manually override the detected type'
                            : 'Type will automatically update based on your expression'
                        }
                    </p>
                    <div className="text-xs text-gray-500 mt-1">
                        Current expression: <span className="font-mono">{exprData.expression || 'None'}</span>
                    </div>
                    <div className="text-xs text-gray-500 mt-1">
                        <label className="block mb-1">Preview expression as:</label>
                        <select
                            className="w-full p-1 text-xs border border-gray-300 rounded"
                            onChange={(e) => {
                                const previewType = e.target.value;
                                if (previewType && previewType !== 'preview') {
                                    // Temporarily change the expression type to preview
                                    const originalType = exprData.expressionType;
                                    setExprData(prev => ({ ...prev, expressionType: previewType }));
                                    
                                    // Get the preview expression
                                    const previewExpression = getCurrentFunctionExpression();
                                    console.log(`Preview as ${previewType}:`, previewExpression);
                                    
                                    // Show preview in a temporary display
                                    setExprData(prev => ({ 
                                        ...prev, 
                                        expressionType: originalType,
                                        previewExpression: previewExpression,
                                        previewType: previewType
                                    }));
                                }
                            }}
                            defaultValue="preview"
                        >
                            <option value="preview">Select to preview...</option>
                            <option value="linear">Linear</option>
                            <option value="quadratic">Quadratic</option>
                            <option value="cubic">Cubic</option>
                            <option value="integrated_exponential_logarithmic">Exponential + Logarithmic (Integrated)</option>
                            <option value="trigonometric">Trigonometric</option>
                            <option value="hyperbolic">Hyperbolic</option>
                        </select>
                        {exprData.previewExpression && (
                            <div className="mt-1 p-1 bg-gray-100 rounded text-xs">
                                <span className="font-medium">{exprData.previewType}:</span> {exprData.previewExpression}
                            </div>
                        )}
                    </div>
                    {isFunctionTypeManual && (
                        <button
                            type="button"
                            onClick={() => {
                                setIsFunctionTypeManual(false);
                                // Re-analyze current expression to auto-detect type
                                if (exprData.expression) {
                                    const analysis = analyzeExpressionType(exprData.expression);
                                    if (analysis.type !== 'other') {
                                        setExprData(prev => ({
                                            ...prev,
                                            functionType: analysis.type
                                        }));
                                        console.log('Reset to auto-detection mode, detected type:', analysis.type);
                                    }
                                }
                            }}
                            className="mt-1 px-2 py-1 text-xs bg-gray-100 text-gray-600 rounded hover:bg-gray-200 transition-colors"
                            title="Reset to auto-detection mode"
                        >
                            Reset to Auto-Detection
                        </button>
                    )}
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Operation:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={exprData.targetOperation}
                        onChange={(e) => handleFieldChange('targetOperation', e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="solve">Solve</option>
                        <option value="simplify">Simplify</option>
                        <option value="factorize" disabled={!['linear', 'quadratic', 'cubic'].includes(exprData.expressionType)}>
                            Factorize {!['linear', 'quadratic', 'cubic'].includes(exprData.expressionType) ? '(Polynomials only)' : ''}
                        </option>
                        <option value="expand" disabled={!['linear', 'quadratic', 'cubic'].includes(exprData.expressionType)}>
                            Expand {!['linear', 'quadratic', 'cubic'].includes(exprData.expressionType) ? '(Polynomials only)' : ''}
                        </option>
                        <option value="complete_square" disabled={exprData.expressionType !== 'quadratic'}>
                            Solve by Completing the Square {exprData.expressionType !== 'quadratic' ? '(Quadratic only)' : ''}
                        </option>
                        <option value="long_division" disabled={!['linear', 'quadratic', 'cubic'].includes(exprData.expressionType)}>
                            Solve by Long Division {!['linear', 'quadratic', 'cubic'].includes(exprData.expressionType) ? '(Polynomials only)' : ''}
                        </option>
                    </select>
                    <p className="text-xs text-gray-500 mt-1">
                        {(() => {
                            const currentExpression = dynamicExpression || exprData.expression;
                            if (currentExpression) {
                                const validation = validateOperationForExpression(currentExpression, exprData.targetOperation);
                                return validation.isValid ? 
                                    `✅ ${validation.message}` : 
                                    `⚠️ ${validation.message}`;
                            }
                            return 'Select an operation to perform';
                        })()}
                    </p>
                    {(() => {
                        const currentExpression = dynamicExpression || exprData.expression;
                        if (currentExpression && exprData.expressionType && exprData.expressionType !== 'other') {
                            const suggestedOperation = getSuggestedOperation(exprData.expressionType);
                            if (suggestedOperation && suggestedOperation !== exprData.targetOperation) {
                                return (
                                    <div className="mt-1 p-1 bg-blue-50 border border-blue-200 rounded text-xs">
                                        💡 Suggested operation for {exprData.expressionType}: <strong>{suggestedOperation}</strong>
                                        <button
                                            type="button"
                                            onClick={() => handleFieldChange('targetOperation', suggestedOperation)}
                                            className="ml-2 px-1 py-0.5 bg-blue-100 text-blue-700 rounded hover:bg-blue-200 transition-colors"
                                        >
                                            Use
                                        </button>
                                    </div>
                                );
                            }
                        }
                        return null;
                    })()}
                    {(() => {
                        const currentExpression = dynamicExpression || exprData.expression;
                        if (currentExpression && exprData.expressionType && exprData.expressionType !== 'other') {
                            const availableOperations = getAvailableOperations(exprData.expressionType);
                            return (
                                <div className="mt-1 p-1 bg-gray-50 border border-gray-200 rounded text-xs">
                                    📋 Available operations: {availableOperations.join(', ')}
                                </div>
                            );
                        }
                        return null;
                    })()}
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Variable:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={exprData.variable}
                        onChange={(e) => handleFieldChange('variable', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="x"
                        maxLength="1"
                    />
                </div>
                
                {exprData.functionType === 'trigonometric' && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Angle Unit:</label>
                        <select
                            className="w-full p-2 border border-gray-300 rounded-md text-sm"
                            value={exprData.angleUnit}
                            onChange={(e) => handleFieldChange('angleUnit', e.target.value)}
                            disabled={isSubmitted}
                        >
                            <option value="degrees">Degrees (-360° to +360°)</option>
                            <option value="radians">Radians</option>
                        </select>
                    </div>
                )}
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Expression:</label>
                    <div className="flex space-x-2">
                        <input
                            ref={expressionInputRef}
                            type="text"
                            className="flex-1 p-2 border border-gray-300 rounded-md text-sm font-mono"
                            value={exprData.showGraph ? '' : exprData.expression}
                            onChange={(e) => handleFieldChange('expression', e.target.value)}
                            disabled={isSubmitted || exprData.showGraph}
                            placeholder={
                                exprData.showGraph ? "Expression will be imported from graph..." :
                                exprData.targetOperation === 'complete_square' ? "Enter quadratic expression (e.g., x² + 6x + 5)" :
                                exprData.targetOperation === 'long_division' ? "Enter division (e.g., x³ + 2x² ÷ x - 2)" :
                                "Enter expression (e.g., y = 2x + 3)"
                            }
                        />

                            <button
                                type="button"
                                onClick={() => setIsKeypadVisible(!isKeypadVisible)}
                                className="px-3 py-1 bg-blue-500 text-white rounded text-sm font-medium hover:bg-blue-600 transition-colors"
                                title="Toggle Math Keypad"
                                disabled={isSubmitted}
                            >
                                Keypad
                            </button>
                    </div>
                    {/* Action - moved under Expression input */}
                    <div className="mt-2 flex space-x-2">
                        {!isSubmitted && (
                            <button
                                onClick={performOperation}
                                className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm hover:bg-blue-600"
                            >
                                {exprData.targetOperation?.charAt(0)?.toUpperCase() + exprData.targetOperation?.slice(1) || 'Operation'} Expression
                            </button>
                        )}
                        {exprData.result && (
                            <div className="text-xs text-gray-600 bg-green-50 border border-green-200 rounded px-2 py-1">
                                ✅ Operation completed: {exprData.result}
                                <button
                                    type="button"
                                    onClick={() => {
                                        const summary = `Operation: ${exprData.targetOperation}\nInput: ${exprData.expression}\nResult: ${exprData.result}\nSteps: ${exprData.steps.length}`;
                                        navigator.clipboard.writeText(summary);
                                        console.log('Operation summary copied to clipboard:', summary);
                                    }}
                                    className="ml-2 px-1 py-0.5 bg-green-100 text-green-700 rounded hover:bg-green-200 transition-colors"
                                    title="Copy operation summary"
                                >
                                    📋
                                </button>
                            </div>
                        )}
                        {exprData.showGraph && (
                            <button
                                type="button"
                                onClick={() => {
                                    // Import expression from graph based on current function type
                                    let newExpression = '';
                                    
                                    if (exprData.expressionType === 'linear' && exprData.functionData) {
                                        const { m, c } = exprData.functionData;
                                        if (m === 1) newExpression = 'x';
                                        else if (m === -1) newExpression = '-x';
                                        else newExpression = `${m}x`;
                                        if (c > 0) newExpression += `+${c}`;
                                        else if (c < 0) newExpression += `${c}`;
                                    } else if (exprData.expressionType === 'quadratic' && exprData.functionData) {
                                        const { a, b, c } = exprData.functionData;
                                        if (a === 1) newExpression = 'x²';
                                        else if (a === -1) newExpression = '-x²';
                                        else newExpression = `${a}x²`;
                                        if (b > 0) newExpression += `+${b}x`;
                                        else if (b < 0) newExpression += `${b}x`;
                                        if (c > 0) newExpression += `+${c}`;
                                        else if (c < 0) newExpression += `${c}`;
                                    } else if (exprData.expressionType === 'cubic' && exprData.functionData) {
                                        const { a, b, c, d } = exprData.functionData;
                                        if (a === 1) newExpression = 'x³';
                                        else if (a === -1) newExpression = '-x³';
                                        else newExpression = `${a}x³`;
                                        if (b > 0) newExpression += `+${b}x²`;
                                        else if (b < 0) newExpression += `${b}x²`;
                                        if (c > 0) newExpression += `+${c}x`;
                                        else if (c < 0) newExpression += `${c}x`;
                                        if (d > 0) newExpression += `+${d}`;
                                        else if (d < 0) newExpression += `${d}`;
                                    } else if (exprData.expressionType === 'integrated_exponential_logarithmic' && exprData.functionData) {
                                        if (exprData.functionData.functionType === 'exponential') {
                                            const { a, b, c, d } = exprData.functionData;
                                            newExpression = `${a}*${b}^(x`;
                                            if (c > 0) newExpression += `+${c}`;
                                            else if (c < 0) newExpression += `${c}`;
                                            newExpression += ')';
                                            if (d > 0) newExpression += `+${d}`;
                                            else if (d < 0) newExpression += `${d}`;
                                        } else {
                                            const { a, b, c, d } = exprData.functionData;
                                            newExpression = `${a}*ln(${b}*x`;
                                            if (c > 0) newExpression += `+${c}`;
                                            else if (c < 0) newExpression += `${c}`;
                                            newExpression += ')';
                                            if (d > 0) newExpression += `+${d}`;
                                            else if (d < 0) newExpression += `${d}`;
                                        }
                                    } else if (exprData.expressionType === 'trigonometric' && exprData.functionData) {
                                        const { a, b, c, d, type } = exprData.functionData;
                                        newExpression = `${a}*${type}(${b}*x`;
                                        if (c > 0) newExpression += `+${c}`;
                                        else if (c < 0) newExpression += `${c}`;
                                        newExpression += ')';
                                        if (d > 0) newExpression += `+${d}`;
                                        else if (d < 0) newExpression += `${d}`;
                                    } else if (exprData.expressionType === 'hyperbolic' && exprData.functionData) {
                                        const { a, b, q, functionForm } = exprData.functionData;
                                        if (functionForm === 'simple') {
                                            if (a === 1) newExpression = '1/x';
                                            else newExpression = `${a}/x`;
                                            if (b > 0) newExpression += `+${b}`;
                                            else if (b < 0) newExpression += `${b}`;
                                        } else {
                                            if (a === 1) newExpression = `1/(x${q > 0 ? '+' : ''}${q})`;
                                            else newExpression = `${a}/(x${q > 0 ? '+' : ''}${q})`;
                                            if (b > 0) newExpression += `+${b}`;
                                            else if (b < 0) newExpression += `${b}`;
                                        }
                                    }
                                    
                                    if (newExpression) {
                                        handleFieldChange('expression', newExpression);
                                    }
                                }}
                                className="px-4 py-2 bg-green-500 text-white rounded-md text-sm hover:bg-green-600"
                                title="Import Expression from Graph"
                                disabled={isSubmitted}
                            >
                                Import Expression From Graph
                            </button>
                        )}
                    </div>
                    
                    {/* Dynamic Expression Display - Always Visible */}
                    <div className="mt-3">
                        <label className="block text-sm font-medium text-blue-700 mb-1">
                            Current Function Expression:
                        </label>
                        <div className="flex space-x-2">
                            <input
                                type="text"
                                className="flex-1 p-2 border border-blue-300 rounded-md text-sm font-mono bg-blue-50 text-blue-800"
                                value={dynamicExpression || getCurrentFunctionExpression()}
                                onChange={(e) => {
                                    const newValue = e.target.value;
                                    // Always update the dynamic expression state for real-time feedback
                                    setDynamicExpression(newValue);
                                    
                                    // Reset manual selection flag when user starts typing new expression
                                    if (isFunctionTypeManual) {
                                        setIsFunctionTypeManual(false);
                                        console.log('Resetting manual function type selection - allowing auto-detection');
                                    }
                                    
                                    // Validate the expression before updating the main system
                                    if (validateExpression(newValue)) {
                                        // When user edits this expression, update the main expression
                                        handleFieldChange('expression', newValue);
                                        
                                        // Trigger immediate graph update if we're in graph mode
                                        if (exprData.showGraph && exprData.viewMode === 'graph') {
                                            // Force a re-render of the graph by updating a timestamp
                                            setExprData(prev => ({
                                                ...prev,
                                                lastUpdate: Date.now()
                                            }));
                                        }
                                    }
                                }}
                                onBlur={() => {
                                    // When user finishes editing, ensure the expression is properly updated
                                    if (dynamicExpression && validateExpression(dynamicExpression)) {
                                        handleFieldChange('expression', dynamicExpression);
                                    }
                                }}
                                disabled={isSubmitted}
                                placeholder="Function expression will appear here..."
                                title="Edit the current function expression - changes will update the graph and parameters"
                            />
                            <button
                                type="button"
                                onClick={() => {
                                    // Refresh the expression from current function data
                                    const currentExpr = getCurrentFunctionExpression();
                                    if (currentExpr && currentExpr !== exprData.expression) {
                                        handleFieldChange('expression', currentExpr);
                                    }
                                }}
                                className="px-3 py-1 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700 transition-colors"
                                title="Refresh expression from current function parameters"
                                disabled={isSubmitted}
                            >
                                ↻
                            </button>
                        </div>
                        <p className="text-xs text-blue-600 mt-1">
                            This expression updates automatically based on function parameters. Edit it to change the graph.
                        </p>
                        <div className="text-xs text-gray-500 mt-1">
                            <span className="inline-flex items-center">
                                <span className={`w-2 h-2 rounded-full mr-1 ${exprData.expression === dynamicExpression ? 'bg-green-500' : 'bg-yellow-500'}`}></span>
                                {exprData.expression === dynamicExpression ? 'Synchronized' : 'Updating...'}
                            </span>
                        </div>
                        {dynamicExpression && (
                            (() => {
                                const validation = getExpressionValidationStatus(dynamicExpression);
                                const detectedType = validation.isValid ? 
                                    analyzeExpressionType(dynamicExpression).type : null;
                                
                                return (
                                    <div className="space-y-1">
                                        <p className={`text-xs ${validation.isValid ? 'text-green-600' : 'text-red-600'}`}>
                                            {validation.isValid ? '✅ ' : '⚠️ '}{validation.message}
                                        </p>
                                        {validation.isValid && detectedType && detectedType !== exprData.functionType && !isFunctionTypeManual && (
                                            <div className="flex items-center space-x-2">
                                                <p className="text-xs text-blue-600">
                                                    💡 Suggested function type: <strong>{detectedType}</strong>
                                                </p>
                                                <button
                                                    type="button"
                                                    onClick={() => {
                                                        setExprData(prev => ({
                                                            ...prev,
                                                            functionType: detectedType
                                                        }));
                                                        console.log('Applied suggested function type:', detectedType);
                                                    }}
                                                    className="px-2 py-0.5 text-xs bg-blue-100 text-blue-700 rounded hover:bg-blue-200 transition-colors"
                                                    title="Apply suggested function type"
                                                >
                                                    Apply
                                                </button>
                                            </div>
                                        )}
                                    </div>
                                );
                            })()
                        )}
                    </div>
                </div>
            </div>
            </div>

            {/* RIGHT: View area (graph or solution) */}
            <div className="lg:col-span-3 max-h-[calc(100vh-7rem)] overflow-y-auto pr-1">
                    <div className="flex items-center justify-between mb-1">
                        <h4 className="font-semibold text-gray-700 text-sm">
                            Function Graph: {exprData.expressionType ? (exprData.expressionType.charAt(0).toUpperCase() + exprData.expressionType.slice(1)) : 'Function'}
                        </h4>
                        <div className="flex items-center gap-2">
                    <button
                                className={`px-2 py-0.5 text-xs rounded ${exprData.viewMode === 'solution' ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700'}`}
                                onClick={() => setExprData(prev => ({ ...prev, viewMode: 'solution' }))}
                    >
                                Solution Procedure
                    </button>
                            <button
                                className={`px-2 py-0.5 text-xs rounded ${exprData.viewMode === 'graph' ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700'}`}
                                onClick={() => setExprData(prev => ({ ...prev, viewMode: 'graph', showGraph: true }))}
                            >
                                Graph View
                            </button>
            </div>
            </div>

                                        {exprData.viewMode === 'graph' ? (
                    <div>
                            {!exprData.expression || exprData.expression.trim() === '' ? (
                                <div className="bg-white border-2 border-gray-300 rounded-lg p-4 shadow-inner flex items-center justify-center h-96">
                                    <div className="text-center text-gray-500">
                                        <p className="text-lg mb-2">Enter an expression to see the graph</p>
                                        <p className="text-sm">Try: y = 2x+3, y = x²+2x+1, or y = ln(x)</p>
                                    </div>
                                </div>
                            ) : exprData.expressionType === 'linear' ? (
                                <div className="bg-white border border-gray-200 rounded">
                                    <LinearFunctionGraph 
                                        initialData={{
                                            title: exprData.title || "Linear Function",
                                            m: exprData.functionData?.m || 2,
                                            c: exprData.functionData?.c || 3,
                                            equation: exprData.expression || "2x+3",
                                            editMode: 'equation',
                                            x_range: [exprData.xMin || -10, exprData.xMax || 10],
                                            y_range: [exprData.yMin || -20, exprData.yMax || 20],
                                            lineColor: '#3B82F6',
                                            showGrid: exprData.showGrid !== false,
                                            showPoints: exprData.showSpecialPoints !== false,
                                            showSlope: true,
                                            showYIntercept: true,
                                            showXIntercept: true
                                        }}
                                        isSubmitted={isSubmitted}
                                        isConfigMode={false}
                                        onChange={() => {}}
                                    />
                                </div>
                            ) : exprData.expressionType === 'quadratic' ? (
                                <div className="bg-white border border-gray-200 rounded">
                                    <QuadraticGraphInput 
                                        initialData={{
                                            title: exprData.title || "Quadratic Function",
                                            a: exprData.functionData?.a || 1,
                                            b: exprData.functionData?.b || 0,
                                            c: exprData.functionData?.c || 0,
                                            equation: exprData.expression || "x²",
                                            x_range: [exprData.xMin || -10, exprData.xMax || 10],
                                            y_range: [exprData.yMin || -10, exprData.yMax || 10],
                                            lineColor: '#3B82F6',
                                            showGrid: exprData.showGrid !== false,
                                            showPoints: exprData.showSpecialPoints !== false,
                                            showVertex: true,
                                            showRoots: true
                                        }}
                                        isSubmitted={isSubmitted}
                                        onChange={() => {}}
                                    />
                                </div>
                            ) : (exprData.expressionType === 'integrated_exponential_logarithmic') ? (
                                <div className="bg-white border border-gray-200 rounded">
                                    <IntegratedExponentialLogarithmicFunction 
                                        initialData={{
                                            functionType: exprData.functionData?.functionType || 'exponential',
                                            a: exprData.functionData?.a || 1,
                                            b: exprData.functionData?.b || 2,
                                            c: exprData.functionData?.c || 0,
                                            d: exprData.functionData?.d || 0,
                                            base: exprData.functionData?.base || 'e',
                                            customBase: exprData.functionData?.customBase || 10,
                                            x_range: [exprData.xMin || -7, exprData.xMax || 7],
                                            y_range: [exprData.yMin || 0, exprData.yMax || 50],
                                            lineColor: '#3B82F6',
                                            showGrid: exprData.showGrid !== false,
                                            showPoints: exprData.showSpecialPoints !== false,
                                            showAsymptotes: true,

                                        }}
                                        isSubmitted={isSubmitted}
                                        onChange={(graphData) => {
                                            // Clean synchronization: Update expression when parameters change
                                            if (graphData.a !== undefined && graphData.b !== undefined) {
                                                let newExpression = '';
                                                
                                                if (graphData.functionType === 'exponential') {
                                                    // Build exponential expression: a × b^(x + c) + d
                                                    if (graphData.a === 1) newExpression = `${graphData.b}^x`;
                                                    else newExpression = `${graphData.a}×${graphData.b}^x`;
                                                    
                                                    if (graphData.c !== 0) {
                                                        newExpression = newExpression.replace('^x', `^(x${graphData.c > 0 ? '+' : ''}${graphData.c})`);
                                                    }
                                                    if (graphData.d !== 0) {
                                                        newExpression += `${graphData.d > 0 ? '+' : ''}${graphData.d}`;
                                                    }
                                                } else {
                                                    // Build logarithmic expression: a × log_b(x + c) + d
                                                    const base = graphData.base === 'custom' ? graphData.customBase : graphData.base;
                                                    if (graphData.a === 1) newExpression = `log_${base}(x)`;
                                                    else newExpression = `${graphData.a}×log_${base}(x)`;
                                                    
                                                    if (graphData.c !== 0) {
                                                        newExpression = newExpression.replace('(x)', `(x${graphData.c > 0 ? '+' : ''}${graphData.c})`);
                                                    }
                                                    if (graphData.d !== 0) {
                                                        newExpression += `${graphData.d > 0 ? '+' : ''}${graphData.d}`;
                                                    }
                                                }
                                                
                                                // Only update if expression actually changed
                                                if (newExpression && newExpression !== exprData.expression) {
                                                    setTimeout(() => {
                                                        setExprData(prev => ({
                                                            ...prev,
                                                            expression: newExpression,
                                                            functionData: {
                                                                ...prev.functionData,
                                                                a: graphData.a,
                                                                b: graphData.b,
                                                                c: graphData.c,
                                                                d: graphData.d,
                                                                base: graphData.base,
                                                                customBase: graphData.customBase,
                                                                functionType: graphData.functionType
                                                            }
                                                        }));
                                                    }, 300);
                                                }
                                            }
                                        }}
                                    />
                                </div>
                            ) : exprData.expressionType === 'cubic' ? (
                                <div className="bg-white border border-gray-200 rounded">
                                    <CubicFunctionGraph 
                                        initialData={{
                                            title: exprData.title || "Cubic Function",
                                            a: exprData.functionData?.a || 1,
                                            b: exprData.functionData?.b || -2,
                                            c: exprData.functionData?.c || -3,
                                            d: exprData.functionData?.d || 1,
                                            equation: exprData.expression || "x³-2x²-3x+1",
                                            x_range: [exprData.xMin || -5, exprData.xMax || 5],
                                            y_range: [exprData.yMin || -10, exprData.yMax || 10],
                                            lineColor: '#3B82F6',
                                            showGrid: exprData.showGrid !== false,
                                            showPoints: exprData.showSpecialPoints !== false,
                                            showRoots: true,
                                            showTurningPoints: true,
                                            editMode: 'parameters'
                                        }}
                                        isSubmitted={isSubmitted}
                                        onChange={(graphData) => {
                                            // Clean synchronization: Update expression when parameters change
                                            // Only update if we have valid parameter data
                                            if (graphData.a !== undefined && graphData.b !== undefined && graphData.c !== undefined && graphData.d !== undefined) {
                                                let newExpression = '';
                                                
                                                // Build expression from parameters
                                                if (graphData.a === 1) newExpression = 'x³';
                                                else if (graphData.a === -1) newExpression = '-x³';
                                                else newExpression = `${graphData.a}x³`;
                                                
                                                if (graphData.b > 0) newExpression += `+${graphData.b}x²`;
                                                else if (graphData.b < 0) newExpression += `${graphData.b}x²`;
                                                
                                                if (graphData.c > 0) newExpression += `+${graphData.c}x`;
                                                else if (graphData.c < 0) newExpression += `${graphData.c}x`;
                                                
                                                if (graphData.d > 0) newExpression += `+${graphData.d}`;
                                                else if (graphData.d < 0) newExpression += `${graphData.d}`;
                                                
                                                // Only update if expression actually changed and is different from current
                                                if (newExpression && newExpression !== exprData.expression) {
                                                    // Use a longer timeout to prevent rapid updates during parameter changes
                                                    setTimeout(() => {
                                                        setExprData(prev => ({
                                                            ...prev,
                                                            expression: newExpression
                                                        }));
                                                    }, 300);
                                                }
                                            }
                                        }}
                                    />
                                </div>
                            ) : exprData.expressionType === 'hyperbolic' ? (
                                <div className="bg-white border border-gray-200 rounded">
                                    <HyperbolicFunctionInput 
                                        initialData={{
                                            title: exprData.title || "Hyperbolic Function",
                                            a: exprData.functionData?.a || 1,
                                            b: exprData.functionData?.b || 0,
                                            q: exprData.functionData?.q || 0,
                                            functionForm: exprData.functionData?.functionForm || 'simple',
                                            equation: exprData.expression || "1/x",
                                            x_range: [exprData.xMin || -10, exprData.xMax || 10],
                                            y_range: [exprData.yMin || -5, exprData.yMax || 5],
                                            lineColor: '#3B82F6',
                                            showGrid: exprData.showGrid !== false,
                                            showPoints: exprData.showSpecialPoints !== false,
                                            showAsymptotes: true
                                        }}
                                        isSubmitted={isSubmitted}
                                        onChange={(graphData) => {
                                            // Clean synchronization: Update expression when parameters change
                                            if (graphData.a !== undefined && graphData.b !== undefined) {
                                                let newExpression = '';
                                                
                                                if (graphData.functionForm === 'simple') {
                                                    // Build simple form: a/x + b
                                                    if (graphData.a === 1) newExpression = '1/x';
                                                    else newExpression = `${graphData.a}/x`;
                                                    
                                                    if (graphData.b > 0) newExpression += `+${graphData.b}`;
                                                    else if (graphData.b < 0) newExpression += `${graphData.b}`;
                                                } else {
                                                    // Build shifted form: a/(x+q) + b
                                                    if (graphData.a === 1) newExpression = `1/(x${graphData.q > 0 ? '+' : ''}${graphData.q})`;
                                                    else newExpression = `${graphData.a}/(x${graphData.q > 0 ? '+' : ''}${graphData.q})`;
                                                    
                                                    if (graphData.b > 0) newExpression += `+${graphData.b}`;
                                                    else if (graphData.b < 0) newExpression += `${graphData.b}`;
                                                }
                                                
                                                // Only update if expression actually changed
                                                if (newExpression && newExpression !== exprData.expression) {
                                                    setTimeout(() => {
                                                        setExprData(prev => ({
                                                            ...prev,
                                                            expression: newExpression,
                                                            functionData: {
                                                                ...prev.functionData,
                                                                a: graphData.a,
                                                                b: graphData.b,
                                                                q: graphData.q,
                                                                functionForm: graphData.functionForm
                                                            }
                                                        }));
                                                    }, 300);
                                                }
                                            }
                                        }}
                                    />
                                </div>
                            ) : exprData.expressionType === 'trigonometric' ? (
                                <div className="bg-white border border-gray-200 rounded">
                                    {/* Quick Trig Function Selector */}
                                    <div className="bg-gray-50 border-b border-gray-200 p-3">
                                        <h5 className="text-sm font-medium text-gray-700 mb-2">Quick Function Selection:</h5>
                                        <div className="flex flex-wrap gap-2">
                                            {['sin', 'cos', 'tan', 'csc', 'sec', 'cot'].map((func) => (
                                                <button
                                                    key={func}
                                                    onClick={() => {
                                                        const newFuncType = func;
                                                        const newEquation = `${func}(x)`;
                                                        setExprData(prev => ({
                                                            ...prev,
                                                            expression: newEquation,
                                                            functionData: {
                                                                ...prev.functionData,
                                                                funcType: newFuncType,
                                                                a: 1,
                                                                b: 1,
                                                                c: 0,
                                                                d: 0
                                                            }
                                                        }));
                                                    }}
                                                    className={`px-3 py-1 text-xs font-medium rounded-md transition-colors ${
                                                        exprData.functionData?.funcType === func
                                                            ? 'bg-blue-500 text-white'
                                                            : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
                                                    }`}
                                                >
                                                    {func}(x)
                                                </button>
                                            ))}
                                        </div>
                                        <div className="mt-2 flex items-center justify-between">
                                            <div className="text-xs text-gray-500">
                                                Click any function above to quickly switch. Use the controls below for detailed customization.
                                            </div>
                                            <div className="flex items-center space-x-2">

                                            </div>
                                        </div>
                                    </div>
                                    
                                    <TrigonometricFunctionGraph 
                                        initialData={{
                                            title: exprData.title || "Trigonometric Function",
                                            funcType: exprData.functionData?.funcType || 'sin',
                                            a: exprData.functionData?.a || 1,
                                            b: exprData.functionData?.b || 1,
                                            c: exprData.functionData?.c || 0,
                                            d: exprData.functionData?.d || 0,
                                            equation: exprData.expression || "sin(x)",
                                            x_range: [exprData.xMin || -10, exprData.xMax || 10],
                                            y_range: [exprData.yMin || -3, exprData.yMax || 3],
                                            lineColor: '#3B82F6',
                                            showGrid: exprData.showGrid !== false,
                                            showPoints: exprData.showSpecialPoints !== false,
                                            showAsymptotes: true,
                                            showPeriod: true,
                                            showAmplitude: true,
                                            showPhaseShift: true,
                                            angleUnit: exprData.angleUnit || 'radians',


                                        }}
                                        isSubmitted={isSubmitted}
                                        onChange={(newData) => {
                                            // Update the main expression when graph parameters change
                                            setExprData(prev => ({
                                                ...prev,
                                                expression: newData.equation,
                                                functionData: {
                                                    ...prev.functionData,
                                                    funcType: newData.funcType,
                                                    a: newData.a,
                                                    b: newData.b,
                                                    c: newData.c,
                                                    d: newData.d
                                                }
                                            }));
                                        }}
                                    />
                                </div>
                            ) : (
                                <div className="text-center text-gray-500 p-8">
                                    <p>Graph view for {exprData.expressionType} functions coming soon...</p>
                                    <p className="text-sm mt-2">Supported types: linear, quadratic, cubic, exponential, logarithmic, trigonometric, hyperbolic</p>
                                </div>
                            )}
                        </div>
                    ) : (
                        <div>
                            {exprData.expressionType === 'trigonometric' ? (
                                <div className="bg-white border border-gray-200 rounded-lg p-4">
                                    <h3 className="text-lg font-semibold text-gray-800 mb-4">Trigonometric Solution Tools</h3>
                                    
                                    {/* Navigation Buttons */}
                                    <div className="flex space-x-2 mb-6">
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, trigViewMode: 'unitCircle' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.trigViewMode === 'unitCircle'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Unit Circle
                                        </button>
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, trigViewMode: 'reductionFormulae' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.trigViewMode === 'reductionFormulae'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Reduction Formulae
                                        </button>
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, trigViewMode: 'identities' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.trigViewMode === 'identities'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Identities
                                        </button>
                                    </div>
                                    
                                    {/* Reduction Formulae (Unit Circle Method) */}
                                    {exprData.trigViewMode === 'reductionFormulae' && (
                                    <div className="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                                        <h4 className="text-md font-semibold text-blue-800 mb-3">Reduction Formulae (Unit Circle Method)</h4>
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                            <div>
                                                <h5 className="font-medium text-blue-700 mb-2">Quadrant I (0° to 90°):</h5>
                                                <ul className="space-y-1 text-blue-600">
                                                    <li>• sin(θ) = sin(θ)</li>
                                                    <li>• cos(θ) = cos(θ)</li>
                                                    <li>• tan(θ) = tan(θ)</li>
                                                </ul>
                                            </div>
                                            <div>
                                                <h5 className="font-medium text-blue-700 mb-2">Quadrant II (90° to 180°):</h5>
                                                <ul className="space-y-1 text-blue-600">
                                                    <li>• sin(180° - θ) = sin(θ)</li>
                                                    <li>• cos(180° - θ) = -cos(θ)</li>
                                                    <li>• tan(180° - θ) = -tan(θ)</li>
                                                </ul>
                                            </div>
                                            <div>
                                                <h5 className="font-medium text-blue-700 mb-2">Quadrant III (180° to 270°):</h5>
                                                <ul className="space-y-1 text-blue-600">
                                                    <li>• sin(180° + θ) = -sin(θ)</li>
                                                    <li>• cos(180° + θ) = -cos(θ)</li>
                                                    <li>• tan(180° + θ) = tan(θ)</li>
                                                </ul>
                                            </div>
                                            <div>
                                                <h5 className="font-medium text-blue-700 mb-2">Quadrant IV (270° to 360°):</h5>
                                                <ul className="space-y-1 text-blue-600">
                                                    <li>• sin(360° - θ) = -sin(θ)</li>
                                                    <li>• cos(360° - θ) = cos(θ)</li>
                                                    <li>• tan(360° - θ) = -tan(θ)</li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div className="mt-3 p-3 bg-blue-100 border border-blue-300 rounded">
                                            <p className="text-xs text-blue-700">
                                                <strong>Memory Aid:</strong> "All Students Take Calculus" - All functions are positive in Quadrant I, 
                                                only Sine in Quadrant II, only Tangent in Quadrant III, only Cosine in Quadrant IV.
                                            </p>
                                        </div>
                                    </div>
                                    )}

                                    {/* Interactive Unit Circle */}
                                    {exprData.trigViewMode === 'unitCircle' && (
                                    <div className="mb-6">
                                        <UnitCircle 
                                            key={`unit-circle-${exprData.trigViewMode}`}
                                            initialData={{
                                                angle: 30,
                                                showValues: true,
                                                showGrid: true,
                                                showLabels: true,
                                                zoom: 1
                                            }}
                                            onChange={(data) => {
                                                // Update the main expression data if needed
                                                console.log('Unit Circle changed:', data);
                                            }}
                                        />
                                        

                                    </div>
                                    )}

                                    {/* Trigonometric Identities */}
                                    {exprData.trigViewMode === 'identities' && (
                                    <div className="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg">
                                        <h4 className="text-md font-semibold text-green-800 mb-3">Trigonometric Identities</h4>
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                            <div>
                                                <h5 className="font-medium text-green-700 mb-2">Pythagorean Identities:</h5>
                                                <ul className="space-y-2 text-green-600">
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• sin²θ + cos²θ = 1</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showPythagoreanProof: !prev.showPythagoreanProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showPythagoreanProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showPythagoreanProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Start with the unit circle: x² + y² = 1</li>
                                                                    <li>For any angle θ, x = cos(θ) and y = sin(θ)</li>
                                                                    <li>Substitute: cos²(θ) + sin²(θ) = 1</li>
                                                                    <li>Therefore: sin²θ + cos²θ = 1 ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• 1 + tan²θ = sec²θ</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showTanSecProof: !prev.showTanSecProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showTanSecProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showTanSecProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Start with: sin²θ + cos²θ = 1</li>
                                                                    <li>Divide both sides by cos²θ: sin²θ/cos²θ + cos²θ/cos²θ = 1/cos²θ</li>
                                                                    <li>Simplify: tan²θ + 1 = sec²θ</li>
                                                                    <li>Therefore: 1 + tan²θ = sec²θ ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• 1 + cot²θ = csc²θ</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showCotCscProof: !prev.showCotCscProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showCotCscProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showCotCscProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Start with: sin²θ + cos²θ = 1</li>
                                                                    <li>Divide both sides by sin²θ: sin²θ/sin²θ + cos²θ/sin²θ = 1/sin²θ</li>
                                                                    <li>Simplify: 1 + cot²θ = csc²θ</li>
                                                                    <li>Therefore: 1 + cot²θ = csc²θ ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                </ul>
                                            </div>
                                            <div>
                                                <h5 className="font-medium text-green-700 mb-2">Double Angle Identities:</h5>
                                                <ul className="space-y-2 text-green-600">
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• sin(2θ) = 2sin(θ)cos(θ)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showSin2Proof: !prev.showSin2Proof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showSin2Proof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showSin2Proof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Use sum identity: sin(A+B) = sin(A)cos(B) + cos(A)sin(B)</li>
                                                                    <li>Let A = θ and B = θ: sin(θ+θ) = sin(θ)cos(θ) + cos(θ)sin(θ)</li>
                                                                    <li>Simplify: sin(2θ) = 2sin(θ)cos(θ) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• cos(2θ) = cos²θ - sin²θ</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showCos2Proof: !prev.showCos2Proof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showCos2Proof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showCos2Proof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Use sum identity: cos(A+B) = cos(A)cos(B) - sin(A)sin(B)</li>
                                                                    <li>Let A = θ and B = θ: cos(θ+θ) = cos(θ)cos(θ) - sin(θ)sin(θ)</li>
                                                                    <li>Simplify: cos(2θ) = cos²θ - sin²θ ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• tan(2θ) = 2tan(θ)/(1-tan²θ)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showTan2Proof: !prev.showTan2Proof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showTan2Proof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showTan2Proof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Use sum identity: tan(A+B) = (tan(A)+tan(B))/(1-tan(A)tan(B))</li>
                                                                    <li>Let A = θ and B = θ: tan(θ+θ) = (tan(θ)+tan(θ))/(1-tan(θ)tan(θ))</li>
                                                                    <li>Simplify: tan(2θ) = 2tan(θ)/(1-tan²θ) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                </ul>
                                            </div>
                                            <div>
                                                <h5 className="font-medium text-green-700 mb-2">Sum & Difference Identities:</h5>
                                                <ul className="space-y-2 text-green-600">
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• sin(A+B) = sin(A)cos(B) + cos(A)sin(B)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showSinSumProof: !prev.showSinSumProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showSinSumProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showSinSumProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Use complex exponential: e^(iθ) = cos(θ) + i·sin(θ)</li>
                                                                    <li>e^(i(A+B)) = e^(iA) · e^(iB)</li>
                                                                    <li>Expand: [cos(A) + i·sin(A)][cos(B) + i·sin(B)]</li>
                                                                    <li>Multiply and equate imaginary parts</li>
                                                                    <li>Result: sin(A+B) = sin(A)cos(B) + cos(A)sin(B) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• cos(A+B) = cos(A)cos(B) - sin(A)sin(B)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showCosSumProof: !prev.showCosSumProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showCosSumProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showCosSumProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Use complex exponential: e^(iθ) = cos(θ) + i·sin(θ)</li>
                                                                    <li>e^(i(A+B)) = e^(iA) · e^(iB)</li>
                                                                    <li>Expand: [cos(A) + i·sin(A)][cos(B) + i·sin(B)]</li>
                                                                    <li>Multiply and equate real parts</li>
                                                                    <li>Result: cos(A+B) = cos(A)cos(B) - sin(A)sin(B) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• tan(A+B) = (tan(A)+tan(B))/(1-tan(A)tan(B))</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showTanSumProof: !prev.showTanSumProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showTanSumProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showTanSumProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>Use definition: tan(θ) = sin(θ)/cos(θ)</li>
                                                                    <li>tan(A+B) = sin(A+B)/cos(A+B)</li>
                                                                    <li>Substitute sum identities for sin(A+B) and cos(A+B)</li>
                                                                    <li>Simplify the fraction</li>
                                                                    <li>Result: tan(A+B) = (tan(A)+tan(B))/(1-tan(A)tan(B)) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                </ul>
                                            </div>
                                            <div>
                                                <h5 className="font-medium text-green-700 mb-2">Reciprocal Identities:</h5>
                                                <ul className="space-y-2 text-green-600">
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• csc(θ) = 1/sin(θ)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showCscProof: !prev.showCscProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showCscProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showCscProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>By definition: csc(θ) is the reciprocal of sin(θ)</li>
                                                                    <li>Therefore: csc(θ) = 1/sin(θ) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• sec(θ) = 1/cos(θ)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showSecProof: !prev.showSecProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showSecProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showSecProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>By definition: sec(θ) is the reciprocal of cos(θ)</li>
                                                                    <li>Therefore: sec(θ) = 1/cos(θ) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                    <li>
                                                        <div className="flex items-center justify-between">
                                                            <span>• cot(θ) = 1/tan(θ)</span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showCotProof: !prev.showCotProof }))}
                                                                className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                            >
                                                                {exprData.showCotProof ? 'Hide Proof' : 'Show Proof'}
                                                            </button>
                                                        </div>
                                                        {exprData.showCotProof && (
                                                            <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                <h6 className="font-medium text-green-800 mb-2">Step-by-Step Proof:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-green-700">
                                                                    <li>By definition: cot(θ) is the reciprocal of tan(θ)</li>
                                                                    <li>Therefore: cot(θ) = 1/tan(θ) ✓</li>
                                                                </ol>
                                                            </div>
                                                        )}
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        
                                        {/* Interactive Identity Verifier */}
                                        <div className="mt-6 p-4 bg-orange-50 border border-orange-200 rounded-lg">
                                            <h4 className="text-md font-semibold text-orange-800 mb-3">Interactive Identity Verifier</h4>
                                            <div className="space-y-3">
                                                <div>
                                                    <label className="block text-sm font-medium text-orange-700 mb-2">
                                                        Enter a trigonometric expression to verify:
                                                    </label>
                                                    <input
                                                        type="text"
                                                        placeholder="e.g., sin²θ + cos²θ"
                                                        className="w-full px-3 py-2 border border-orange-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-500 text-sm"
                                                        value={exprData.identityInput || ''}
                                                        onChange={(e) => setExprData(prev => ({ ...prev, identityInput: e.target.value }))}
                                                    />
                                                </div>
                                                <button
                                                    onClick={() => {
                                                        // Simple verification logic for common identities
                                                        const input = exprData.identityInput?.trim();
                                                        if (!input) return;
                                                        
                                                        const inputLower = input.toLowerCase().replace(/\s/g, '');
                                                        let result = { isValid: false, explanation: '' };
                                                        
                                                        // Check for common known identities
                                                        if (inputLower.includes('sin²θ+cos²θ') || inputLower.includes('sin²θ') && inputLower.includes('cos²θ')) {
                                                            result = { isValid: true, explanation: '✅ This is the Pythagorean Identity: sin²θ + cos²θ = 1' };
                                                        } else if (inputLower.includes('1+tan²θ')) {
                                                            result = { isValid: true, explanation: '✅ This is the Pythagorean Identity: 1 + tan²θ = sec²θ' };
                                                        } else if (inputLower.includes('sin(2θ)') && inputLower.includes('2sin(θ)cos(θ)')) {
                                                            result = { isValid: true, explanation: '✅ This is the Double Angle Identity: sin(2θ) = 2sin(θ)cos(θ)' };
                                                        } else {
                                                            result = { isValid: true, explanation: '✅ Expression appears to be a valid trigonometric expression. Verify manually for complete accuracy.' };
                                                        }
                                                        
                                                        setExprData(prev => ({ ...prev, identityResult: result }));
                                                    }}
                                                    className="px-4 py-2 bg-orange-500 text-white rounded hover:bg-orange-600 transition-colors text-sm"
                                                >
                                                    Verify Identity
                                                </button>
                                                {exprData.identityResult && (
                                                    <div className={`p-3 rounded text-sm ${
                                                        exprData.identityResult.isValid 
                                                            ? 'bg-green-100 border border-green-300 text-green-700' 
                                                            : 'bg-red-100 border border-red-300 text-red-700'
                                                    }`}>
                                                        {exprData.identityResult.explanation}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    </div>
                                    )}


                                </div>
                            ) : exprData.expressionType === 'hyperbolic' ? (
                                <div className="bg-white border border-gray-200 rounded-lg p-4">
                                    <h3 className="text-lg font-semibold text-gray-800 mb-4">Reciprocal Function Solution Tools</h3>
                                    
                                    {/* Navigation Buttons */}
                                    <div className="flex space-x-2 mb-6">
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, hyperbolicViewMode: 'properties' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.hyperbolicViewMode === 'properties'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Properties
                                        </button>
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, hyperbolicViewMode: 'asymptotes' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.hyperbolicViewMode === 'asymptotes'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Asymptotes & Domain
                                        </button>
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, hyperbolicViewMode: 'transformations' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.hyperbolicViewMode === 'transformations'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Transformations
                                        </button>
                                        <button
                                            onClick={() => setExprData(prev => ({ ...prev, hyperbolicViewMode: 'solver' }))}
                                            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                                                exprData.hyperbolicViewMode === 'solver'
                                                    ? 'bg-blue-600 text-white'
                                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                            }`}
                                        >
                                            Equation Solver
                                        </button>
                                    </div>
                                    
                                    {/* Properties Section */}
                                    {exprData.hyperbolicViewMode === 'properties' && (
                                        <div className="mb-6 p-4 bg-purple-50 border border-purple-200 rounded-lg">
                                            <h4 className="text-md font-semibold text-purple-800 mb-3">Reciprocal Function Properties</h4>
                                            
                                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                                <div>
                                                    <h5 className="font-medium text-purple-700 mb-2">Parameter Effects:</h5>
                                                    <ul className="space-y-2 text-purple-600">
                                                        <li>
                                                            <div className="flex items-center justify-between">
                                                                <span>• <strong>Parameter 'a'</strong>: Scale & Direction</span>
                                                                <button
                                                                    onClick={() => setExprData(prev => ({ ...prev, showReciprocalProof: !prev.showReciprocalProof }))}
                                                                    className="text-xs px-2 py-1 bg-purple-200 text-purple-700 rounded hover:bg-purple-300 transition-colors"
                                                                >
                                                                    {exprData.showReciprocalProof ? 'Hide Details' : 'Show Details'}
                                                                </button>
                                                            </div>
                                                            {exprData.showReciprocalProof && (
                                                                <div className="mt-2 p-3 bg-purple-100 border border-purple-300 rounded text-xs">
                                                                    <h6 className="font-medium text-purple-800 mb-2">Parameter 'a' Effects:</h6>
                                                                    <ul className="list-disc list-inside space-y-1 text-purple-700">
                                                                        <li>If a &gt; 0: Function branches in Quadrants I and III</li>
                                                                        <li>If a &lt; 0: Function branches in Quadrants II and IV</li>
                                                                        <li>Larger |a|: Steeper curves (more rapid change)</li>
                                                                        <li>Smaller |a|: Flatter curves (more gradual change)</li>
                                                                    </ul>
                                                                </div>
                                                            )}
                                                        </li>
                                                        <li>• <strong>Parameter 'b'</strong>: Vertical shift (y = b is horizontal asymptote)</li>
                                                        <li>• <strong>Parameter 'q'</strong>: Horizontal shift (x = -q is vertical asymptote)</li>
                                                    </ul>
                                                </div>
                                                
                                                <div>
                                                    <h5 className="font-medium text-purple-700 mb-2">Function Behavior:</h5>
                                                    <ul className="space-y-1 text-purple-600">
                                                        <li>• <strong>Quadrant I (x &gt; 0, y &gt; 0)</strong>: When a &gt; 0</li>
                                                        <li>• <strong>Quadrant II (x &lt; 0, y &gt; 0)</strong>: When a &lt; 0</li>
                                                        <li>• <strong>Quadrant III (x &lt; 0, y &lt; 0)</strong>: When a &gt; 0</li>
                                                        <li>• <strong>Quadrant IV (x &gt; 0, y &lt; 0)</strong>: When a &lt; 0</li>
                                                    </ul>
                                                </div>
                                            </div>
                                            
                                            <div className="mt-3 p-3 bg-purple-100 border border-purple-300 rounded">
                                                <p className="text-xs text-purple-700">
                                                    <strong>Memory Aid:</strong> "Reciprocal means flip" - 1/x is the reciprocal of x. 
                                                    Think of reciprocal functions as representing inverse proportional relationships.
                                                </p>
                                            </div>
                                        </div>
                                    )}

                                    {/* Asymptotes & Domain Section */}
                                    {exprData.hyperbolicViewMode === 'asymptotes' && (
                                        <div className="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                                            <h4 className="text-md font-semibold text-blue-800 mb-3">Asymptotes & Domain Analysis</h4>
                                            
                                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                                <div>
                                                    <h5 className="font-medium text-blue-700 mb-2">Vertical Asymptotes:</h5>
                                                    <ul className="space-y-2 text-blue-600">
                                                        <li>
                                                            <div className="flex items-center justify-between">
                                                                <span>• <strong>y = a/x + b</strong>: x = 0</span>
                                                                <button
                                                                    onClick={() => setExprData(prev => ({ ...prev, showAsymptoteProof: !prev.showAsymptoteProof }))}
                                                                    className="text-xs px-2 py-1 bg-blue-200 text-blue-700 rounded hover:bg-blue-300 transition-colors"
                                                                >
                                                                    {exprData.showAsymptoteProof ? 'Hide Proof' : 'Show Proof'}
                                                                </button>
                                                            </div>
                                                            {exprData.showAsymptoteProof && (
                                                                <div className="mt-2 p-3 bg-blue-100 border border-blue-300 rounded text-xs">
                                                                    <h6 className="font-medium text-blue-800 mb-2">Why x = 0 is a vertical asymptote:</h6>
                                                                    <ol className="list-decimal list-inside space-y-1 text-blue-700">
                                                                        <li>As x approaches 0 from the right: a/x → +∞ (if a &gt; 0)</li>
                                                                        <li>As x approaches 0 from the left: a/x → -∞ (if a &gt; 0)</li>
                                                                        <li>The function is undefined at x = 0 (division by zero)</li>
                                                                        <li>Therefore, x = 0 is a vertical asymptote</li>
                                                                    </ol>
                                                                </div>
                                                            )}
                                                        </li>
                                                        <li>• <strong>y = a/(x+q) + b</strong>: x = -q</li>
                                                    </ul>
                                                </div>
                                                
                                                <div>
                                                    <h5 className="font-medium text-blue-700 mb-2">Horizontal Asymptotes:</h5>
                                                    <ul className="space-y-1 text-blue-600">
                                                        <li>• <strong>All forms</strong>: y = b</li>
                                                        <li>• As x → ±∞, function approaches y = b</li>
                                                        <li>• Function never actually reaches y = b</li>
                                                    </ul>
                                                </div>
                                            </div>
                                            
                                            <div className="mt-4">
                                                <h5 className="font-medium text-blue-700 mb-2">Domain & Range:</h5>
                                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                                    <div>
                                                        <p className="text-blue-600"><strong>Domain</strong>:</p>
                                                        <ul className="list-disc list-inside text-blue-600 ml-4">
                                                            <li>y = a/x + b: All real numbers except x = 0</li>
                                                            <li>y = a/(x+q) + b: All real numbers except x = -q</li>
                                                        </ul>
                                                    </div>
                                                    <div>
                                                        <p className="text-blue-600"><strong>Range</strong>:</p>
                                                        <ul className="list-disc list-inside text-blue-600 ml-4">
                                                            <li>All real numbers except y = b</li>
                                                            <li>Function can get arbitrarily close to y = b but never reaches it</li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    )}

                                    {/* Transformations Section */}
                                    {exprData.hyperbolicViewMode === 'transformations' && (
                                        <div className="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg">
                                            <h4 className="text-md font-semibold text-green-800 mb-3">Function Transformations</h4>
                                            
                                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                                <div>
                                                    <h5 className="font-medium text-green-700 mb-2">Basic Transformations:</h5>
                                                    <ul className="space-y-2 text-green-600">
                                                        <li>
                                                            <div className="flex items-center justify-between">
                                                                <span>• <strong>Vertical Stretch/Compression</strong></span>
                                                                <button
                                                                    onClick={() => setExprData(prev => ({ ...prev, showTransformationProof: !prev.showTransformationProof }))}
                                                                    className="text-xs px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 transition-colors"
                                                                >
                                                                    {exprData.showTransformationProof ? 'Hide Examples' : 'Show Examples'}
                                                                </button>
                                                            </div>
                                                            {exprData.showTransformationProof && (
                                                                <div className="mt-2 p-3 bg-green-100 border border-green-300 rounded text-xs">
                                                                    <h6 className="font-medium text-green-800 mb-2">Transformation Examples:</h6>
                                                                    <ul className="list-disc list-inside space-y-1 text-green-700">
                                                                        <li>y = 1/x → y = 2/x (vertical stretch by factor of 2)</li>
                                                                        <li>y = 1/x → y = (1/2)/x (vertical compression by factor of 1/2)</li>
                                                                        <li>y = 1/x → y = -1/x (reflection across x-axis)</li>
                                                                        <li>y = 1/x → y = 1/(-x) (reflection across y-axis)</li>
                                                                    </ul>
                                                                </div>
                                                            )}
                                                        </li>
                                                        <li>• <strong>Vertical Shift</strong>: y = a/x + b</li>
                                                        <li>• <strong>Horizontal Shift</strong>: y = a/(x+q) + b</li>
                                                    </ul>
                                                </div>
                                                
                                                <div>
                                                    <h5 className="font-medium text-green-700 mb-2">Transformation Order:</h5>
                                                    <ol className="list-decimal list-inside space-y-1 text-green-600">
                                                        <li>Start with parent function: y = 1/x</li>
                                                        <li>Apply parameter 'a': y = a/x</li>
                                                        <li>Apply horizontal shift 'q': y = a/(x+q)</li>
                                                        <li>Apply vertical shift 'b': y = a/(x+q) + b</li>
                                                    </ol>
                                                </div>
                                            </div>
                                            
                                            <div className="mt-3 p-3 bg-green-100 border border-green-300 rounded">
                                                <p className="text-xs text-green-700">
                                                    <strong>Key Insight:</strong> All transformations preserve the basic hyperbolic shape - 
                                                    they just move or scale the asymptotes and branches.
                                                </p>
                                            </div>
                                        </div>
                                    )}

                                    {/* Equation Solver Section */}
                                    {exprData.hyperbolicViewMode === 'solver' && (
                                        <div className="mb-6 p-4 bg-orange-50 border border-orange-200 rounded-lg">
                                            <h4 className="text-md font-semibold text-orange-800 mb-3">Reciprocal Function Equation Solver</h4>
                                            
                                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                                <div>
                                                    <h5 className="font-medium text-orange-700 mb-2">Solving a/x + b = c:</h5>
                                                    <div className="space-y-2 text-orange-600">
                                                        <div className="flex items-center justify-between">
                                                            <span><strong>Step-by-Step Process:</strong></span>
                                                            <button
                                                                onClick={() => setExprData(prev => ({ ...prev, showSolverProof: !prev.showSolverProof }))}
                                                                className="text-xs px-2 py-1 bg-orange-200 text-orange-700 rounded hover:bg-orange-300 transition-colors"
                                                            >
                                                                {exprData.showSolverProof ? 'Hide Steps' : 'Show Steps'}
                                                            </button>
                                                        </div>
                                                        {exprData.showSolverProof && (
                                                            <div className="mt-2 p-3 bg-orange-100 border border-orange-300 rounded text-xs">
                                                                <h6 className="font-medium text-orange-800 mb-2">Solving a/x + b = c:</h6>
                                                                <ol className="list-decimal list-inside space-y-1 text-orange-700">
                                                                    <li>Start: a/x + b = c</li>
                                                                    <li>Subtract b from both sides: a/x = c - b</li>
                                                                    <li>Multiply both sides by x: a = x(c - b)</li>
                                                                    <li>Divide both sides by (c - b): x = a/(c - b)</li>
                                                                    <li>Check: c - b &ne; 0 (no solution if c = b)</li>
                                                                </ol>
                                                                <p className="mt-2 text-orange-700">
                                                                    <strong>Example:</strong> Solve 2/x + 3 = 7<br/>
                                                                    → 2/x = 4 → x = 2/4 = 0.5
                                                                </p>
                                                            </div>
                                                        )}
                                                    </div>
                                                </div>
                                                
                                                <div>
                                                    <h5 className="font-medium text-orange-700 mb-2">Special Cases & Restrictions:</h5>
                                                    <ul className="space-y-1 text-orange-600">
                                                        <li>• <strong>No solution</strong> when c = b (horizontal asymptote)</li>
                                                        <li>• <strong>Domain restrictions</strong>: x &ne; 0 (or x &ne; -q)</li>
                                                        <li>• <strong>Always check</strong> that solution is in domain</li>
                                                        <li>• <strong>Graphical method</strong>: Find intersection points</li>
                                                    </ul>
                                                </div>
                                            </div>
                                            
                                            <div className="mt-4">
                                                <h5 className="font-medium text-orange-700 mb-2">Finding Intercepts:</h5>
                                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                                                    <div>
                                                        <p className="text-orange-600"><strong>Y-intercept</strong>:</p>
                                                        <ul className="list-disc list-inside text-orange-600 ml-4">
                                                            <li>Set x = 0: Usually undefined (vertical asymptote)</li>
                                                            <li>For y = a/(x+q) + b: Set x = 0 → y = a/q + b (if q &ne; 0)</li>
                                                        </ul>
                                                    </div>
                                                    <div>
                                                        <p className="text-orange-600"><strong>X-intercept</strong>:</p>
                                                        <ul className="list-disc list-inside text-orange-600 ml-4">
                                                            <li>Set y = 0: a/x + b = 0</li>
                                                            <li>Solve: x = -a/b (if b &ne; 0)</li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    )}

                                </div>
                            ) : (
                                <StepCanvas 
                                    exprData={exprData}
                                    setExprData={setExprData}
                                    showSteps={exprData.showSteps}
                                    showGraph={exprData.showGraph}
                                    xMin={exprData.xMin}
                                    xMax={exprData.xMax}
                                />
                            )}
                        </div>
                    )}
                </div>
            </div>
            {/* End of grid layout */}

            {/* Error Display */}
            {exprData.error && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
                    <p className="text-sm text-red-800">{exprData.error}</p>
                </div>
            )}

            {/* Result Display */}
            {exprData.result && (
                <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">Result:</h4>
                    <div className="text-lg font-mono text-green-700">{exprData.result}</div>
                </div>
            )}

            {/* Enhanced Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Enhanced Algebraic Expression Builder Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                                            <li><strong>Function Types:</strong> Select from Linear, Quadratic, Cubic, Exponential, Logarithmic, Trigonometric, and Hyperbolic functions</li>
                    <li><strong>Default Equations:</strong> Each function type loads with an appropriate default equation and graph</li>
                    <li><strong>Mathematical Operations:</strong> Solve, Simplify, Factorize, Expand, Complete Square, and Long Division</li>
                    <li><strong>Enhanced Interactive Graphing:</strong> All function types render graphs with zoom, pan, and interactive controls</li>
                    <li><strong>Trigonometric Support:</strong> Functions use degrees by default (-360° to +360°) with option to switch to radians</li>
                    <li><strong>Comprehensive Step-by-Step Solutions:</strong> Detailed procedural guidance for all mathematical operations</li>
                    <li><strong>AI Integration:</strong> Receive expressions and instructions from AI/curriculum helper</li>
                    <li><strong>Advanced Function Analysis:</strong> Automatic calculation of intercepts, critical points, domain, range, asymptotes</li>
                    <li><strong>Interactive Canvas:</strong> Zoom, pan, toggle grid/axes, adjustable resolution, fit-to-view</li>
                    <li><strong>Canvas Controls:</strong> Use mouse to drag/pan, scroll to zoom, or use precise controls</li>
                    <li><strong>Resolution Options:</strong> Choose from 100 to 2000 points for smooth or detailed graphs</li>
                </ul>
            </div>

            {/* Enhanced Math Keypad */}
            <EnhancedMathKeypad 
                isVisible={isKeypadVisible}
                onClose={() => setIsKeypadVisible(false)}
                inputRef={expressionInputRef}
                onExpressionChange={(newValue) => handleFieldChange('expression', newValue)}
                isSubmitted={isSubmitted}
            />

            {/* AI Integration */}
            {isPro ? (
                <AiMathAssistant 
                    aiInputText={aiInputText}
                    setAiInputText={setAiInputText}
                    isSubmitted={isSubmitted}
                    isProcessingAi={isProcessingAi}
                    setIsProcessingAi={setIsProcessingAi}
                    exprData={exprData}
                    setExprData={setExprData}
                    processOperation={performOperation}
                    analyzeExpression={analyzeExpression}
                />
            ) : (
                <div className="mt-6 p-4 rounded-xl border-2 border-orange-100 bg-orange-50 flex items-start gap-4">
                    <div className="p-2 bg-orange-100 rounded-lg text-orange-600">
                        <Bot size={24} />
                    </div>
                    <div>
                        <h4 className="font-semibold text-gray-800">AI Math Assistant</h4>
                        <p className="text-sm text-gray-600 mt-1">
                            The AI Tutor feature is available in the Pro package. Pro is coming soon and not yet available in South Africa.
                        </p>
                    </div>
                </div>
            )}
         </div>
    );
};

export default AlgebraicExpressionBuilder;
