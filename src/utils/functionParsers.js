/**
 * Function Parsing Utilities
 * 
 * This module contains functions for parsing and analyzing mathematical expressions
 * to determine their type and extract relevant parameters for graphing components.
 */

/**
 * Parses logarithmic functions to extract base and type
 * @param {string} expr - The mathematical expression
 * @returns {Object} - Object containing type and base information
 */
export function parseLogarithmicFunction(expr) {
    try {
        if (expr.includes('ln(')) {
            return { type: 'natural_log', base: Math.E };
        } else if (expr.includes('log(')) {
            return { type: 'base_10_log', base: 10 };
        } else if (expr.includes('log₂(')) {
            return { type: 'base_2_log', base: 2 };
        } else {
            // Extract base from log_b(x) format
            const match = expr.match(/log_(\d+)\(/);
            if (match) {
                return { type: 'custom_base_log', base: parseInt(match[1]) };
            }
        }
        return { type: 'natural_log', base: Math.E };
    } catch (error) {
        console.error('Error parsing logarithmic function:', error);
        return { type: 'natural_log', base: Math.E };
    }
}

/**
 * Parses exponential functions to extract base and type
 * @param {string} expr - The mathematical expression
 * @returns {Object} - Object containing type and base information
 */
export function parseExponentialFunction(expr) {
    try {
        // Handle e^x format
        if (expr.includes('e^') || expr.includes('exp(')) {
            return { a: 1, b: Math.E, c: 0, d: 0 };
        }
        
        // Handle b^x format (like 2^x)
        const match = expr.match(/(\d+)\^/);
        if (match) {
            const base = parseInt(match[1]);
            return { a: 1, b: base, c: 0, d: 0 };
        }
        
        // Handle a*b^x format (like 3*2^x)
        const complexMatch = expr.match(/(\d+)\*(\d+)\^/);
        if (complexMatch) {
            const coefficient = parseInt(complexMatch[1]);
            const base = parseInt(complexMatch[2]);
            return { a: coefficient, b: base, c: 0, d: 0 };
        }
        
        return { a: 1, b: 2, c: 0, d: 0 };
    } catch (error) {
        console.error('Error parsing exponential function:', error);
        return { a: 1, b: 2, c: 0, d: 0 };
    }
}

/**
 * Parses trigonometric functions to extract type, coefficients, and parameters
 * @param {string} expr - The mathematical expression
 * @returns {Object} - Object containing type, coefficients, and parameters
 */
export function parseTrigonometricFunction(expr) {
    try {
        // Clean the expression
        const cleanExpr = expr.replace(/\s/g, '').toLowerCase();
        
        // Determine function type
        let funcType = 'sin';
        if (cleanExpr.includes('cos(')) funcType = 'cos';
        else if (cleanExpr.includes('tan(')) funcType = 'tan';
        else if (cleanExpr.includes('csc(')) funcType = 'csc';
        else if (cleanExpr.includes('sec(')) funcType = 'sec';
        else if (cleanExpr.includes('cot(')) funcType = 'cot';
        
        // Extract coefficients using regex patterns
        // Pattern: A*sin(B*x + C) + D or similar
        const pattern = new RegExp(`([+-]?\\d*\\.?\\d*)\\s*${funcType}\\s*\\(\\s*([+-]?\\d*\\.?\\d*)\\s*\\*?\\s*x\\s*([+-]\\s*\\d*\\.?\\d*)?\\s*\\)\\s*([+-]\\s*\\d*\\.?\\d*)?`);
        const match = cleanExpr.match(pattern);
        
        let a = 1, b = 1, c = 0, d = 0;
        
        if (match) {
            // Coefficient A (amplitude)
            if (match[1] && match[1] !== '+' && match[1] !== '-') {
                a = parseFloat(match[1]) || 1;
            } else if (match[1] === '-') {
                a = -1;
            }
            
            // Coefficient B (frequency/period)
            if (match[2]) {
                b = parseFloat(match[2]) || 1;
            }
            
            // Coefficient C (phase shift)
            if (match[3]) {
                c = parseFloat(match[3].replace(/\s/g, '')) || 0;
            }
            
            // Coefficient D (vertical shift)
            if (match[4]) {
                d = parseFloat(match[4].replace(/\s/g, '')) || 0;
            }
        }
        
        // Handle special cases like sin(x), cos(2x), tan(x+π/3)
        if (!match) {
            // Simple case: sin(x)
            if (cleanExpr.includes(`${funcType}(x)`)) {
                a = 1; b = 1; c = 0; d = 0;
            }
            // Case: sin(2x)
            else if (cleanExpr.includes(`${funcType}(\\d+x)`)) {
                const bMatch = cleanExpr.match(new RegExp(`${funcType}\\((\\d+)x\\)`));
                if (bMatch) b = parseFloat(bMatch[1]);
            }
            // Case: sin(x+π/3) or sin(x+pi/3)
            else if (cleanExpr.includes(`${funcType}(x[+-]`)) {
                const cMatch = cleanExpr.match(new RegExp(`${funcType}\\(x([+-][^)]+)\\)`));
                if (cMatch) {
                    const cStr = cMatch[1];
                    if (cStr.includes('π') || cStr.includes('pi')) {
                        // Convert π to radians
                        c = parseFloat(cStr.replace(/π|pi/g, '')) * Math.PI;
                    } else {
                        c = parseFloat(cStr);
                    }
                }
            }
        }
        
        return {
            type: funcType,
            a: a,
            b: b,
            c: c,
            d: d,
            argument: 'x',
            amplitude: Math.abs(a),
            period: b !== 0 ? (2 * Math.PI) / Math.abs(b) : 0,
            phaseShift: b !== 0 ? -c / b : 0,
            verticalShift: d
        };
    } catch (error) {
        console.error('Error parsing trigonometric function:', error);
        return { type: 'sin', a: 1, b: 1, c: 0, d: 0, argument: 'x' };
    }
}

/**
 * Parses polynomial functions to extract coefficients
 * @param {string} expr - The mathematical expression
 * @returns {Object} - Object containing coefficients array
 */
export function parsePolynomialFunction(expr) {
    try {
        const coefficients = [0, 0, 0, 0]; // Initialize all coefficients to 0
        
        // Extract coefficients for different powers of x
        if (expr.includes('x³') || expr.includes('x^3')) {
            const match = expr.match(/([+-]?\d*)x³/);
            if (match) {
                if (match[1] === '+' || match[1] === '') {
                    coefficients[3] = 1;
                } else if (match[1] === '-') {
                    coefficients[3] = -1;
                } else {
                    coefficients[3] = parseInt(match[1]);
                }
            }
        }
        
        if (expr.includes('x²') || expr.includes('x^2')) {
            const match = expr.match(/([+-]?\d*)x²/);
            if (match) {
                if (match[1] === '+' || match[1] === '') {
                    coefficients[2] = 1;
                } else if (match[1] === '-') {
                    coefficients[2] = -1;
                } else {
                    coefficients[2] = parseInt(match[1]);
                }
            }
        }
        
        if (expr.includes('x') && !expr.includes('x²') && !expr.includes('x³') && !expr.includes('x^2') && !expr.includes('x^3')) {
            const match = expr.match(/([+-]?\d*)x/);
            if (match) {
                if (match[1] === '+' || match[1] === '') {
                    coefficients[1] = 1;
                } else if (match[1] === '-') {
                    coefficients[1] = -1;
                } else {
                    coefficients[1] = parseInt(match[1]);
                }
            }
        }
        
        // Extract constant term (standalone numbers)
        const constMatch = expr.match(/([+-]?\d+)(?!x)/);
        if (constMatch) {
            coefficients[0] = parseInt(constMatch[1]);
        }
        
        return { coefficients: coefficients };
    } catch (error) {
        console.error('Error parsing polynomial function:', error);
        return { coefficients: [0, 0, 0, 0] };
    }
}

/**
 * Parses hyperbolic functions to extract parameters
 * @param {string} expr - The mathematical expression
 * @returns {Object} - Object containing a, b, q, and functionForm
 */
export function parseHyperbolicFunction(expr) {
    try {
        const cleanExpr = expr.replace(/\s/g, '');
        
        // Check for simple form: a/x + b
        const simpleMatch = cleanExpr.match(/([+-]?\d*)\/x\s*([+-]\s*\d+)?/);
        if (simpleMatch) {
            const a = simpleMatch[1] === '' || simpleMatch[1] === '+' ? 1 : 
                     simpleMatch[1] === '-' ? -1 : parseFloat(simpleMatch[1]);
            const b = simpleMatch[2] ? parseFloat(simpleMatch[2].replace(/\s/g, '')) : 0;
            return { a, b, q: 0, functionForm: 'simple' };
        }
        
        // Check for shifted form: a/(x+q) + b
        const shiftedMatch = cleanExpr.match(/([+-]?\d*)\/\(x\s*([+-]\s*\d+)\)\s*([+-]\s*\d+)?/);
        if (shiftedMatch) {
            const a = shiftedMatch[1] === '' || shiftedMatch[1] === '+' ? 1 : 
                     shiftedMatch[1] === '-' ? -1 : parseFloat(shiftedMatch[1]);
            const q = parseFloat(shiftedMatch[2].replace(/\s/g, ''));
            const b = shiftedMatch[3] ? parseFloat(shiftedMatch[3].replace(/\s/g, '')) : 0;
            return { a, b, q, functionForm: 'shifted' };
        }
        
        // Default values
        return { a: 1, b: 0, q: 0, functionForm: 'simple' };
    } catch (error) {
        console.error('Error parsing hyperbolic function:', error);
        return { a: 1, b: 0, q: 0, functionForm: 'simple' };
    }
}

/**
 * Parses linear functions to extract slope and y-intercept
 * @param {string} expr - The mathematical expression
 * @returns {Object} - Object containing slope (m) and y-intercept (c)
 */
export function parseLinearFunction(expr) {
    if (!expr) return { m: 0, c: 0 };
    
    try {
        // Remove spaces and handle y= format
        let cleanExpr = expr.replace(/\s/g, '');
        if (cleanExpr.toLowerCase().includes('y=')) {
            cleanExpr = cleanExpr.split('=')[1];
        }
        
        const slopeMatch = cleanExpr.match(/([+-]?\d*)x/);
        const interceptMatch = cleanExpr.match(/([+-]?\d+)(?!x)/);
        
        const slope = slopeMatch ? (slopeMatch[1] === '+' || slopeMatch[1] === '' ? 1 : slopeMatch[1] === '-' ? -1 : parseInt(slopeMatch[1])) : 0;
        const intercept = interceptMatch ? parseInt(interceptMatch[1]) : 0;
        
        return { m: slope, c: intercept };
    } catch (error) {
        console.error('Error parsing linear function:', error);
        return { m: 0, c: 0 };
    }
}

/**
 * Determines the degree of a polynomial expression
 * @param {string} expr - The mathematical expression
 * @returns {number} - The degree of the polynomial (0-3)
 */
export function getPolynomialDegree(expr) {
    if (expr.includes('x³') || expr.includes('x^3')) return 3;
    if (expr.includes('x²') || expr.includes('x^2')) return 2;
    if (expr.includes('x')) return 1;
    return 0;
}

/**
 * Main function to analyze an expression and determine its type and properties
 * @param {string} expression - The mathematical expression to analyze
 * @returns {Object} - Object containing type and functionData
 */
export function analyzeExpressionType(expression) {
    try {
        const cleanedExpr = expression.replace(/\s+/g, '').toLowerCase();
        let type = 'other';
        let functionData = null;
        
        // Check for exponential and logarithmic functions (integrated)
        if (cleanedExpr.includes('ln') || cleanedExpr.includes('log') || 
            (cleanedExpr.includes('^') && (cleanedExpr.includes('e^') || cleanedExpr.includes('exp') || /\d+\^/.test(cleanedExpr)))) {
            type = 'integrated_exponential_logarithmic';
            if (cleanedExpr.includes('ln') || cleanedExpr.includes('log')) {
                functionData = { ...parseLogarithmicFunction(cleanedExpr), functionType: 'logarithmic' };
            } else {
                functionData = { ...parseExponentialFunction(cleanedExpr), functionType: 'exponential' };
            }
        }
        // Check for hyperbolic functions
        else if (cleanedExpr.includes('/x') || (cleanedExpr.includes('/(') && cleanedExpr.includes('x'))) {
            type = 'hyperbolic';
            functionData = parseHyperbolicFunction(cleanedExpr);
        }
        // Check for trigonometric functions
        else if (cleanedExpr.includes('sin') || cleanedExpr.includes('cos') || cleanedExpr.includes('tan') || 
                 cleanedExpr.includes('csc') || cleanedExpr.includes('sec') || cleanedExpr.includes('cot')) {
            type = 'trigonometric';
            functionData = parseTrigonometricFunction(cleanedExpr);
        }
        // Check for polynomial functions
        else if (cleanedExpr.includes('^') || cleanedExpr.includes('²') || cleanedExpr.includes('³')) {
            const degree = getPolynomialDegree(cleanedExpr);
            if (degree === 1) type = 'linear';
            else if (degree === 2) type = 'quadratic';
            else if (degree === 3) type = 'cubic';
            else type = 'polynomial';
            
            const polyData = parsePolynomialFunction(cleanedExpr);
            if (degree === 3) {
                // Map coefficients for cubic functions: ax³ + bx² + cx + d
                functionData = {
                    a: polyData.coefficients[3] || 0,
                    b: polyData.coefficients[2] || 0,
                    c: polyData.coefficients[1] || 0,
                    d: polyData.coefficients[0] || 0
                };
            } else if (degree === 2) {
                // Map coefficients for quadratic functions: ax² + bx + c
                functionData = {
                    a: polyData.coefficients[2] || 0,
                    b: polyData.coefficients[1] || 0,
                    c: polyData.coefficients[0] || 0
                };
            } else {
                functionData = polyData;
            }
        }
        // Check for linear functions (no exponents, just x terms)
        else if (cleanedExpr.includes('x') && !cleanedExpr.includes('^')) {
            type = 'linear';
            functionData = parseLinearFunction(cleanedExpr);
        }
        
        return { type, functionData };
    } catch (error) {
        console.error('Error analyzing expression type:', error);
        return { type: 'other', functionData: null };
    }
}
