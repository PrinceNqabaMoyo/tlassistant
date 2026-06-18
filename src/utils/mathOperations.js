/**
 * Math Operations Utilities
 * 
 * This module contains mathematical operations and expression manipulation functions
 * for algebraic computations, including simplification, factoring, solving equations, etc.
 */

import { evaluate, parse, simplify, derivative } from 'mathjs';
import * as math from 'mathjs';

/**
 * Simple expression parser and evaluator
 * Converts mathematical notation to JavaScript-evaluable format
 * @param {string} expr - The mathematical expression
 * @returns {string|null} - Parsed expression or null if error
 */
export const parseExpression = (expr) => {
    try {
        // Remove spaces and convert to lowercase
        expr = expr.replace(/\s/g, '').toLowerCase();
        
        // Replace mathematical symbols with computer-readable format
        expr = expr
            .replace(/²/g, '^2')           // Convert superscript ² to ^2
            .replace(/₂/g, '_2')           // Convert subscript ₂ to _2
            .replace(/×/g, '*')            // Convert × to *
            .replace(/÷/g, '/')            // Convert ÷ to /
            .replace(/√/g, 'sqrt')         // Convert √ to sqrt
            .replace(/π/g, 'Math.PI')      // Convert π to Math.PI
            .replace(/\^/g, '**')          // Convert ^ to **
            .replace(/(\d+)x/g, '$1*x')   // Add * between number and x
            .replace(/x(\d+)/g, 'x*$1')   // Add * between x and number
            .replace(/([a-z])\(/g, '$1*(') // Add * between letter and (
            .replace(/\)([a-z])/g, ')*$1'); // Add * between ) and letter
        
        return expr;
    } catch (error) {
        return null;
    }
};

/**
 * Evaluates a mathematical expression for a given x value
 * @param {string} expr - The mathematical expression
 * @param {number} x - The value to substitute for x
 * @returns {number|null} - Result or null if error
 */
export const evaluateExpression = (expr, x) => {
    try {
        const parsedExpr = parseExpression(expr);
        if (!parsedExpr) return null;
        
        // Create a safe evaluation environment with mathematical functions
        const safeEval = (expression, xValue) => {
            const func = new Function('x', 'Math', `return ${expression}`);
            return func(xValue, Math);
        };
        
        return safeEval(parsedExpr, x);
    } catch (error) {
        return null;
    }
};

/**
 * Simplifies a mathematical expression with step-by-step explanation
 * @param {string} expr - The expression to simplify
 * @returns {Object} - Object containing steps and result
 */
export const simplifyExpression = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        // Step 1: Remove spaces and standardize
        steps.push({
            step: 1,
            description: "Remove spaces and standardize notation",
            expression: currentExpr,
            explanation: "Clean up the expression for processing"
        });
        
        // Step 2: Use mathjs to simplify
        const simplified = simplify(currentExpr).toString();
        currentExpr = simplified;
        
        steps.push({
            step: 2,
            description: "Apply algebraic simplification",
            expression: currentExpr,
            explanation: "Combine like terms and simplify the expression"
        });
        
        return {
            result: currentExpr,
            steps: steps,
            success: true
        };
    } catch (error) {
        steps.push({
            step: steps.length + 1,
            description: "Error in simplification",
            expression: currentExpr,
            explanation: `Could not simplify: ${error.message}`
        });
        
        return {
            result: expr,
            steps: steps,
            success: false,
            error: error.message
        };
    }
};

/**
 * Factors a mathematical expression
 * @param {string} expr - The expression to factor
 * @returns {Object} - Object containing steps and result
 */
export const factorExpression = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        // Simple factoring for common patterns
        steps.push({
            step: 1,
            description: "Identify factoring pattern",
            expression: currentExpr,
            explanation: "Look for common factors, difference of squares, or trinomial patterns"
        });
        
        // Check for quadratic expressions
        if (currentExpr.includes('x²') || currentExpr.includes('x^2')) {
            // Try to factor as quadratic
            const factored = simplify(`factor(${currentExpr})`).toString();
            currentExpr = factored;
            
            steps.push({
                step: 2,
                description: "Factor the quadratic expression",
                expression: currentExpr,
                explanation: "Apply quadratic factoring techniques"
            });
        } else {
            // General factoring
            const factored = simplify(`factor(${currentExpr})`).toString();
            currentExpr = factored;
            
            steps.push({
                step: 2,
                description: "Factor the expression",
                expression: currentExpr,
                explanation: "Extract common factors"
            });
        }
        
        return {
            result: currentExpr,
            steps: steps,
            success: true
        };
    } catch (error) {
        return {
            result: expr,
            steps: [{
                step: 1,
                description: "Cannot factor",
                expression: expr,
                explanation: "This expression cannot be factored further or is already in simplest form"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Expands a mathematical expression
 * @param {string} expr - The expression to expand
 * @returns {Object} - Object containing steps and result
 */
export const expandExpression = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        steps.push({
            step: 1,
            description: "Identify terms to expand",
            expression: currentExpr,
            explanation: "Look for parentheses and multiplication patterns"
        });
        
        const expanded = simplify(`expand(${currentExpr})`).toString();
        currentExpr = expanded;
        
        steps.push({
            step: 2,
            description: "Expand and simplify",
            expression: currentExpr,
            explanation: "Distribute terms and combine like terms"
        });
        
        return {
            result: currentExpr,
            steps: steps,
            success: true
        };
    } catch (error) {
        return {
            result: expr,
            steps: [{
                step: 1,
                description: "Cannot expand",
                expression: expr,
                explanation: "This expression cannot be expanded or is already expanded"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Solves an equation
 * @param {string} expr - The equation to solve
 * @returns {Object} - Object containing steps and result
 */
export const solveEquation = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        steps.push({
            step: 1,
            description: "Identify equation type",
            expression: currentExpr,
            explanation: "Determine the best solving method"
        });
        
        // Use mathjs to solve
        const solutions = math.evaluate(`solve(${currentExpr}, x)`);
        let solutionStr = '';
        
        if (Array.isArray(solutions)) {
            solutionStr = solutions.map(sol => sol.toString()).join(', ');
        } else {
            solutionStr = solutions.toString();
        }
        
        steps.push({
            step: 2,
            description: "Solve for x",
            expression: `x = ${solutionStr}`,
            explanation: "Apply algebraic methods to isolate x"
        });
        
        return {
            result: solutionStr,
            steps: steps,
            success: true
        };
    } catch (error) {
        return {
            result: "No solution found",
            steps: [{
                step: 1,
                description: "Cannot solve",
                expression: expr,
                explanation: "This equation cannot be solved or has no real solutions"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Completes the square for a quadratic expression
 * @param {string} expr - The quadratic expression
 * @returns {Object} - Object containing steps and result
 */
export const completeSquare = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        steps.push({
            step: 1,
            description: "Identify quadratic form",
            expression: currentExpr,
            explanation: "Ensure the expression is in the form ax² + bx + c"
        });
        
        // Parse coefficients (simplified approach)
        const aMatch = currentExpr.match(/([+-]?\d*\.?\d*)x²|([+-]?\d*\.?\d*)x\^2/);
        const bMatch = currentExpr.match(/([+-]?\d*\.?\d*)x(?![²^])/);
        const cMatch = currentExpr.match(/([+-]?\d+\.?\d*)(?![x²^])/);
        
        const a = aMatch ? (aMatch[1] === '' || aMatch[1] === '+' ? 1 : aMatch[1] === '-' ? -1 : parseFloat(aMatch[1])) : 0;
        const b = bMatch ? (bMatch[1] === '' || bMatch[1] === '+' ? 1 : bMatch[1] === '-' ? -1 : parseFloat(bMatch[1])) : 0;
        const c = cMatch ? parseFloat(cMatch[1]) : 0;
        
        if (a === 0) {
            throw new Error("Not a quadratic expression");
        }
        
        // Complete the square: a(x + b/(2a))² + (c - b²/(4a))
        const h = -b / (2 * a);
        const k = c - (b * b) / (4 * a);
        
        const vertexForm = `${a}(x ${h >= 0 ? '+' : ''}${h.toFixed(3)})² ${k >= 0 ? '+' : ''}${k.toFixed(3)}`;
        
        steps.push({
            step: 2,
            description: "Complete the square",
            expression: vertexForm,
            explanation: `Transform to vertex form: a(x - h)² + k where vertex is (${h.toFixed(3)}, ${k.toFixed(3)})`
        });
        
        return {
            result: vertexForm,
            steps: steps,
            success: true,
            vertex: { x: h, y: k }
        };
    } catch (error) {
        return {
            result: expr,
            steps: [{
                step: 1,
                description: "Cannot complete square",
                expression: expr,
                explanation: "This expression is not a valid quadratic or is already in vertex form"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Performs polynomial long division
 * @param {string} expr - The division expression (dividend ÷ divisor)
 * @returns {Object} - Object containing steps and result
 */
export const performLongDivision = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        steps.push({
            step: 1,
            description: "Identify division expression",
            expression: currentExpr,
            explanation: "Recognize this as a polynomial division problem"
        });
        
        // Split dividend and divisor
        const parts = currentExpr.split(/÷|\/|\sdiv\s/);
        if (parts.length !== 2) {
            throw new Error("Invalid division format");
        }
        
        const dividend = parts[0].trim();
        const divisor = parts[1].trim();
        
        steps.push({
            step: 2,
            description: "Set up long division",
            expression: `(${dividend}) ÷ (${divisor})`,
            explanation: "Arrange the dividend and divisor for polynomial long division"
        });
        
        // Simplified polynomial division (would need more complex implementation for full functionality)
        try {
            const result = math.evaluate(`(${dividend}) / (${divisor})`);
            const resultStr = simplify(result).toString();
            
            steps.push({
                step: 3,
                description: "Perform division",
                expression: resultStr,
                explanation: "Complete the polynomial long division process"
            });
            
            return {
                result: resultStr,
                steps: steps,
                success: true
            };
        } catch (divError) {
            throw new Error("Cannot perform division");
        }
        
    } catch (error) {
        return {
            result: expr,
            steps: [{
                step: 1,
                description: "Cannot perform long division",
                expression: expr,
                explanation: "Invalid format or unsupported polynomial division"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Analyzes a quadratic expression for key properties
 * @param {string} expr - The quadratic expression
 * @returns {Object} - Object containing analysis and steps
 */
export const analyzeQuadratic = (expr) => {
    const steps = [];
    let currentExpr = expr;
    
    try {
        steps.push({
            step: 1,
            description: "Identify quadratic expression",
            expression: currentExpr,
            explanation: "Recognize this as a quadratic expression in the form ax² + bx + c"
        });
        
        // Parse coefficients
        const aMatch = currentExpr.match(/([+-]?\d*\.?\d*)x²|([+-]?\d*\.?\d*)x\^2/);
        const bMatch = currentExpr.match(/([+-]?\d*\.?\d*)x(?![²^])/);
        const cMatch = currentExpr.match(/([+-]?\d+\.?\d*)(?![x²^])/);
        
        const a = aMatch ? (aMatch[1] === '' || aMatch[1] === '+' ? 1 : aMatch[1] === '-' ? -1 : parseFloat(aMatch[1])) : 0;
        const b = bMatch ? (bMatch[1] === '' || bMatch[1] === '+' ? 1 : bMatch[1] === '-' ? -1 : parseFloat(bMatch[1])) : 0;
        const c = cMatch ? parseFloat(cMatch[1]) : 0;
        
        if (a === 0) {
            throw new Error("Not a quadratic expression");
        }
        
        // Calculate discriminant
        const discriminant = b * b - 4 * a * c;
        
        steps.push({
            step: 2,
            description: "Calculate discriminant",
            expression: `Δ = b² - 4ac = ${b}² - 4(${a})(${c}) = ${discriminant}`,
            explanation: "The discriminant determines the nature of the roots"
        });
        
        // Determine root nature
        let rootNature = '';
        if (discriminant > 0) {
            rootNature = "Two distinct real roots";
        } else if (discriminant === 0) {
            rootNature = "One repeated real root";
        } else {
            rootNature = "Two complex conjugate roots";
        }
        
        steps.push({
            step: 3,
            description: "Analyze roots",
            expression: rootNature,
            explanation: `Since Δ ${discriminant > 0 ? '> 0' : discriminant === 0 ? '= 0' : '< 0'}, the quadratic has ${rootNature.toLowerCase()}`
        });
        
        // Calculate vertex
        const vertexX = -b / (2 * a);
        const vertexY = a * vertexX * vertexX + b * vertexX + c;
        
        steps.push({
            step: 4,
            description: "Find vertex",
            expression: `Vertex: (${vertexX.toFixed(3)}, ${vertexY.toFixed(3)})`,
            explanation: "The vertex represents the maximum or minimum point of the parabola"
        });
        
        return {
            result: {
                coefficients: { a, b, c },
                discriminant,
                rootNature,
                vertex: { x: vertexX, y: vertexY },
                opensUpward: a > 0
            },
            steps: steps,
            success: true
        };
        
    } catch (error) {
        return {
            result: null,
            steps: [{
                step: 1,
                description: "Cannot analyze",
                expression: expr,
                explanation: "This expression is not a valid quadratic"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Solves trigonometric equations
 * @param {string} expr - The trigonometric equation to solve
 * @returns {Object} - Object containing steps and solutions
 */
export const solveTrigonometricEquation = (expr) => {
    const steps = [];
    
    try {
        steps.push({
            step: 1,
            description: "Identify trigonometric equation",
            expression: expr,
            explanation: "Recognize this as a trigonometric equation to solve"
        });
        
        // Parse the equation to extract function type and coefficients
        const cleanExpr = expr.replace(/\s/g, '').toLowerCase();
        
        // Handle basic forms: sin(x) = k, cos(x) = k, tan(x) = k
        const sinMatch = cleanExpr.match(/sin\(([^)]+)\)\s*=\s*([+-]?\d*\.?\d*)/);
        const cosMatch = cleanExpr.match(/cos\(([^)]+)\)\s*=\s*([+-]?\d*\.?\d*)/);
        const tanMatch = cleanExpr.match(/tan\(([^)]+)\)\s*=\s*([+-]?\d*\.?\d*)/);
        
        if (sinMatch) {
            const argument = sinMatch[1];
            const value = parseFloat(sinMatch[2]);
            
            if (argument === 'x') {
                const solutions = solveSinEquation(value);
                steps.push({
                    step: 2,
                    description: "Solve sin(x) = " + value,
                    expression: `x = ${solutions.map(s => s.toFixed(3)).join(', ')}`,
                    explanation: `Use inverse sine: x = arcsin(${value}) + 2πn or x = π - arcsin(${value}) + 2πn`
                });
                
                return {
                    result: `x = ${solutions.map(s => s.toFixed(3)).join(', ')} + 2πn`,
                    solutions: solutions,
                    steps: steps,
                    success: true
                };
            }
        } else if (cosMatch) {
            const argument = cosMatch[1];
            const value = parseFloat(cosMatch[2]);
            
            if (argument === 'x') {
                const solutions = solveCosEquation(value);
                steps.push({
                    step: 2,
                    description: "Solve cos(x) = " + value,
                    expression: `x = ${solutions.map(s => s.toFixed(3)).join(', ')}`,
                    explanation: `Use inverse cosine: x = ±arccos(${value}) + 2πn`
                });
                
                return {
                    result: `x = ±${Math.acos(value).toFixed(3)} + 2πn`,
                    solutions: solutions,
                    steps: steps,
                    success: true
                };
            }
        } else if (tanMatch) {
            const argument = tanMatch[1];
            const value = parseFloat(tanMatch[2]);
            
            if (argument === 'x') {
                const solutions = solveTanEquation(value);
                steps.push({
                    step: 2,
                    description: "Solve tan(x) = " + value,
                    expression: `x = ${solutions.map(s => s.toFixed(3)).join(', ')}`,
                    explanation: `Use inverse tangent: x = arctan(${value}) + πn`
                });
                
                return {
                    result: `x = ${Math.atan(value).toFixed(3)} + πn`,
                    solutions: solutions,
                    steps: steps,
                    success: true
                };
            }
        }
        
        throw new Error("Unsupported trigonometric equation format");
        
    } catch (error) {
        return {
            result: expr,
            steps: [{
                step: 1,
                description: "Cannot solve trigonometric equation",
                expression: expr,
                explanation: "This equation format is not supported or cannot be solved"
            }],
            success: false,
            error: error.message
        };
    }
};

/**
 * Solves sin(x) = k
 * @param {number} k - The value to solve for
 * @returns {Array} - Array of solutions in [0, 2π]
 */
const solveSinEquation = (k) => {
    if (k < -1 || k > 1) return [];
    
    const solutions = [];
    const principal = Math.asin(k);
    
    // Add principal solution
    if (principal >= 0) {
        solutions.push(principal);
    }
    
    // Add supplementary solution
    if (principal !== 0) {
        solutions.push(Math.PI - principal);
    }
    
    return solutions;
};

/**
 * Solves cos(x) = k
 * @param {number} k - The value to solve for
 * @returns {Array} - Array of solutions in [0, 2π]
 */
const solveCosEquation = (k) => {
    if (k < -1 || k > 1) return [];
    
    const solutions = [];
    const principal = Math.acos(k);
    
    // Add principal solution
    if (principal >= 0) {
        solutions.push(principal);
    }
    
    // Add negative solution
    if (principal !== 0 && principal !== Math.PI) {
        solutions.push(2 * Math.PI - principal);
    }
    
    return solutions;
};

/**
 * Solves tan(x) = k
 * @param {number} k - The value to solve for
 * @returns {Array} - Array of solutions in [0, π]
 */
const solveTanEquation = (k) => {
    const solutions = [];
    const principal = Math.atan(k);
    
    // Add principal solution
    if (principal >= 0) {
        solutions.push(principal);
    }
    
    return solutions;
};

/**
 * Applies trigonometric identities and reduction formulae
 * @param {string} expr - The trigonometric expression to simplify
 * @returns {Object} - Object containing steps and simplified result
 */
export const applyTrigonometricIdentities = (expr) => {
    const steps = [];
    
    try {
        steps.push({
            step: 1,
            description: "Identify trigonometric expression",
            expression: expr,
            explanation: "Recognize this as a trigonometric expression to simplify using identities"
        });
        
        let currentExpr = expr;
        
        // Apply common identities
        // sin²(x) + cos²(x) = 1
        if (currentExpr.includes('sin²(x)') && currentExpr.includes('cos²(x)')) {
            currentExpr = currentExpr.replace(/sin²\(x\)\s*\+\s*cos²\(x\)/g, '1');
            steps.push({
                step: 2,
                description: "Apply Pythagorean identity",
                expression: currentExpr,
                explanation: "Use sin²(x) + cos²(x) = 1"
            });
        }
        
        // sin(2x) = 2sin(x)cos(x)
        if (currentExpr.includes('sin(2x)')) {
            currentExpr = currentExpr.replace(/sin\(2x\)/g, '2sin(x)cos(x)');
            steps.push({
                step: 3,
                description: "Apply double angle formula",
                expression: currentExpr,
                explanation: "Use sin(2x) = 2sin(x)cos(x)"
            });
        }
        
        // cos(2x) = cos²(x) - sin²(x) = 2cos²(x) - 1 = 1 - 2sin²(x)
        if (currentExpr.includes('cos(2x)')) {
            currentExpr = currentExpr.replace(/cos\(2x\)/g, 'cos²(x) - sin²(x)');
            steps.push({
                step: 4,
                description: "Apply double angle formula",
                expression: currentExpr,
                explanation: "Use cos(2x) = cos²(x) - sin²(x)"
            });
        }
        
        // tan(x) = sin(x)/cos(x)
        if (currentExpr.includes('tan(x)')) {
            currentExpr = currentExpr.replace(/tan\(x\)/g, 'sin(x)/cos(x)');
            steps.push({
                step: 5,
                description: "Apply quotient identity",
                expression: currentExpr,
                explanation: "Use tan(x) = sin(x)/cos(x)"
            });
        }
        
        return {
            result: currentExpr,
            steps: steps,
            success: true
        };
        
    } catch (error) {
        return {
            result: expr,
            steps: steps,
            success: false,
            error: error.message
        };
    }
};
